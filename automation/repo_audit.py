#!/usr/bin/env python3
"""Repository documentation/catalog auditor for learning-docs.

Standard-library only. Designed to run locally or in GitHub Actions.
"""
from __future__ import annotations

import argparse
import os
import re
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path
from typing import Iterable
from urllib.parse import unquote, urlsplit

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
INLINE_LINK_RE = re.compile(
    r"!?\[[^\]]*\]\(\s*(?P<target><[^>]+>|[^\s)]+)(?:\s+(?:\"[^\"]*\"|'[^']*'|\([^)]*\)))?\s*\)"
)
REFERENCE_DEF_RE = re.compile(r"^\s*\[[^\]]+\]:\s*(?P<target><[^>]+>|\S+)", re.MULTILINE)
FENCE_RE = re.compile(r"^\s*(```+|~~~+)")
EXTERNAL_SCHEMES = {"http", "https", "mailto", "tel", "data", "javascript"}


@dataclass
class Finding:
    severity: str
    code: str
    message: str
    path: str | None = None
    line: int | None = None

    def render(self) -> str:
        where = ""
        if self.path:
            where = self.path
            if self.line:
                where += f":{self.line}"
            where += ": "
        return f"[{self.severity}] {self.code}: {where}{self.message}"


@dataclass
class Domain:
    id: str = ""
    path: str = ""
    entrypoint: str = ""
    status: str = ""
    last_reviewed: str = ""
    scope: str = ""


@dataclass
class AuditResult:
    findings: list[Finding] = field(default_factory=list)
    checked_markdown: int = 0
    checked_links: int = 0
    checked_domains: int = 0

    def add(
        self,
        severity: str,
        code: str,
        message: str,
        path: str | None = None,
        line: int | None = None,
    ) -> None:
        self.findings.append(Finding(severity, code, message, path, line))

    @property
    def errors(self) -> int:
        return sum(f.severity == "ERROR" for f in self.findings)

    @property
    def warnings(self) -> int:
        return sum(f.severity == "WARNING" for f in self.findings)


def parse_catalog_domains(catalog_text: str) -> list[Domain]:
    """Parse the simple domain list from CATALOG.md without a YAML dependency."""
    lines = catalog_text.splitlines()
    in_domains = False
    current: dict[str, str] | None = None
    domains: list[Domain] = []

    def flush() -> None:
        nonlocal current
        if current is not None:
            domains.append(
                Domain(
                    **{
                        key: current.get(key, "")
                        for key in Domain.__dataclass_fields__
                    }
                )
            )
            current = None

    for raw in lines:
        if raw == "domains:":
            in_domains = True
            continue
        if in_domains and raw == "supporting:":
            flush()
            break
        if not in_domains:
            continue

        match = re.match(r"^  - id:\s*(.+?)\s*$", raw)
        if match:
            flush()
            current = {"id": match.group(1).strip()}
            continue

        if current is None:
            continue

        match = re.match(r"^    ([a-z_]+):\s*(.*?)\s*$", raw)
        if match and match.group(1) in Domain.__dataclass_fields__:
            current[match.group(1)] = match.group(2).strip()
    else:
        flush()

    return domains


def _is_under(child: Path, parent: Path) -> bool:
    return child.parts[: len(parent.parts)] == parent.parts


def validate_catalog(root: Path, stale_days: int, result: AuditResult) -> None:
    catalog_path = root / "CATALOG.md"
    if not catalog_path.is_file():
        result.add("ERROR", "catalog.missing", "CATALOG.md is missing")
        return

    text = catalog_path.read_text(encoding="utf-8")
    domains = parse_catalog_domains(text)
    result.checked_domains = len(domains)
    if not domains:
        result.add(
            "ERROR",
            "catalog.empty",
            "No canonical domains parsed from CATALOG.md",
            "CATALOG.md",
        )
        return

    seen_ids: set[str] = set()
    seen_entrypoints: set[str] = set()
    today = date.today()

    for domain in domains:
        prefix = f"domain '{domain.id or '?'}'"

        if not domain.id:
            result.add(
                "ERROR",
                "catalog.id_missing",
                "A domain is missing id",
                "CATALOG.md",
            )
            continue

        if domain.id in seen_ids:
            result.add(
                "ERROR",
                "catalog.id_duplicate",
                f"Duplicate id: {domain.id}",
                "CATALOG.md",
            )
        seen_ids.add(domain.id)

        if domain.status != "canonical":
            result.add(
                "WARNING",
                "catalog.status",
                f"{prefix} has status={domain.status!r}, expected canonical",
                "CATALOG.md",
            )

        if not domain.path:
            result.add(
                "ERROR",
                "catalog.path_missing",
                f"{prefix} has no path",
                "CATALOG.md",
            )
        elif not (root / domain.path).exists():
            result.add(
                "ERROR",
                "catalog.path_not_found",
                f"{prefix} path does not exist: {domain.path}",
                "CATALOG.md",
            )

        if not domain.entrypoint:
            result.add(
                "ERROR",
                "catalog.entrypoint_missing",
                f"{prefix} has no entrypoint",
                "CATALOG.md",
            )
        else:
            entrypoint = root / domain.entrypoint
            if not entrypoint.is_file():
                result.add(
                    "ERROR",
                    "catalog.entrypoint_not_found",
                    f"{prefix} entrypoint does not exist: {domain.entrypoint}",
                    "CATALOG.md",
                )

            if domain.entrypoint in seen_entrypoints:
                result.add(
                    "WARNING",
                    "catalog.entrypoint_duplicate",
                    f"Entrypoint reused: {domain.entrypoint}",
                    "CATALOG.md",
                )
            seen_entrypoints.add(domain.entrypoint)

            if domain.path and not _is_under(
                Path(domain.entrypoint), Path(domain.path)
            ):
                result.add(
                    "WARNING",
                    "catalog.entrypoint_outside",
                    f"{prefix} entrypoint is outside domain path: {domain.entrypoint}",
                    "CATALOG.md",
                )

        if not DATE_RE.match(domain.last_reviewed):
            result.add(
                "ERROR",
                "catalog.review_date",
                f"{prefix} has invalid last_reviewed: {domain.last_reviewed!r}",
                "CATALOG.md",
            )
        else:
            try:
                reviewed = datetime.strptime(
                    domain.last_reviewed, "%Y-%m-%d"
                ).date()
                age = (today - reviewed).days
                if stale_days >= 0 and age > stale_days:
                    result.add(
                        "WARNING",
                        "catalog.stale",
                        f"{prefix} last reviewed {age} days ago ({domain.last_reviewed})",
                        "CATALOG.md",
                    )
            except ValueError:
                result.add(
                    "ERROR",
                    "catalog.review_date",
                    f"{prefix} has impossible date: {domain.last_reviewed}",
                    "CATALOG.md",
                )

        if not domain.scope:
            result.add(
                "WARNING",
                "catalog.scope_missing",
                f"{prefix} has empty scope",
                "CATALOG.md",
            )

        domain_dir = root / domain.path if domain.path else None
        if domain_dir and domain_dir.is_dir():
            if not (domain_dir / "README.md").is_file():
                result.add(
                    "INFO",
                    "domain.readme_missing",
                    f"{prefix} has no root README.md; entrypoint is {domain.entrypoint}",
                    domain.path,
                )
            if not (domain_dir / "COVERAGE_AUDIT.md").is_file():
                result.add(
                    "INFO",
                    "domain.coverage_audit_missing",
                    f"{prefix} has no root COVERAGE_AUDIT.md",
                    domain.path,
                )


def strip_fenced_code(text: str) -> str:
    out: list[str] = []
    active: str | None = None

    for line in text.splitlines(keepends=True):
        match = FENCE_RE.match(line)
        if match:
            fence = match.group(1)[0]
            if active is None:
                active = fence
            elif active == fence:
                active = None
            out.append("\n" if line.endswith("\n") else "")
            continue

        if active is None:
            out.append(line)
        else:
            out.append("\n" if line.endswith("\n") else "")

    return "".join(out)


def extract_markdown_targets(text: str) -> Iterable[tuple[str, int]]:
    clean = strip_fenced_code(text)

    for regex in (INLINE_LINK_RE, REFERENCE_DEF_RE):
        for match in regex.finditer(clean):
            target = match.group("target").strip()
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            line = clean.count("\n", 0, match.start()) + 1
            yield target, line


def classify_local_target(target: str) -> str | None:
    target = target.strip()
    if not target or target.startswith("#") or target.startswith("//"):
        return None

    split = urlsplit(target)
    if split.scheme.lower() in EXTERNAL_SCHEMES or split.netloc:
        return None

    path = unquote(split.path)
    if not path:
        return None
    return path


def resolve_local_link(root: Path, source: Path, target_path: str) -> Path:
    if target_path.startswith("/"):
        candidate = root / target_path.lstrip("/")
    else:
        candidate = source.parent / target_path
    return Path(os.path.normpath(str(candidate)))


def discover_markdown(root: Path) -> list[Path]:
    ignored = {
        ".git",
        "node_modules",
        ".venv",
        "venv",
        "dist",
        "build",
        "__pycache__",
    }
    files: list[Path] = []

    for path in root.rglob("*.md"):
        try:
            relative = path.relative_to(root)
        except ValueError:
            continue

        if any(part in ignored for part in relative.parts):
            continue
        files.append(path)

    return sorted(files)


def load_file_selection(root: Path, files_from: Path | None) -> list[Path]:
    if files_from is None:
        return discover_markdown(root)

    selected: list[Path] = []
    for raw in files_from.read_text(encoding="utf-8").splitlines():
        raw = raw.strip()
        if not raw or not raw.lower().endswith(".md"):
            continue
        path = root / raw
        if path.is_file():
            selected.append(path)

    return sorted(set(selected))


def audit_markdown_links(
    root: Path,
    files: Iterable[Path],
    strict_links: bool,
    result: AuditResult,
) -> None:
    severity = "ERROR" if strict_links else "WARNING"

    for source in files:
        result.checked_markdown += 1
        relative_source = str(source.relative_to(root))

        try:
            text = source.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            result.add(
                "WARNING",
                "markdown.encoding",
                "Could not decode as UTF-8",
                relative_source,
            )
            continue

        for target, line in extract_markdown_targets(text):
            local = classify_local_target(target)
            if local is None:
                continue

            result.checked_links += 1
            resolved = resolve_local_link(root, source, local)

            try:
                resolved.relative_to(root)
            except ValueError:
                result.add(
                    severity,
                    "link.outside_repo",
                    f"Local link escapes repository: {target}",
                    relative_source,
                    line,
                )
                continue

            if not resolved.exists():
                result.add(
                    severity,
                    "link.missing",
                    f"Target not found: {target} -> {resolved.relative_to(root)}",
                    relative_source,
                    line,
                )


def write_github_summary(result: AuditResult) -> None:
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary_path:
        return

    errors = [f for f in result.findings if f.severity == "ERROR"]
    warnings = [f for f in result.findings if f.severity == "WARNING"]

    with open(summary_path, "a", encoding="utf-8") as summary:
        summary.write("## learning-docs repository audit\n\n")
        summary.write(
            f"- Canonical domains checked: **{result.checked_domains}**\n"
        )
        summary.write(
            f"- Markdown files checked: **{result.checked_markdown}**\n"
        )
        summary.write(f"- Local links checked: **{result.checked_links}**\n")
        summary.write(f"- Errors: **{len(errors)}**\n")
        summary.write(f"- Warnings: **{len(warnings)}**\n\n")

        if errors or warnings:
            summary.write("### Findings\n\n")
            for finding in (errors + warnings)[:100]:
                summary.write(f"- `{finding.render()}`\n")

            remaining = len(errors) + len(warnings) - 100
            if remaining > 0:
                summary.write(
                    f"- … {remaining} more findings are available in the job log.\n"
                )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Audit learning-docs catalog and Markdown links"
    )
    parser.add_argument("--root", default=".", help="Repository root")
    parser.add_argument(
        "--files-from",
        type=Path,
        help="Optional newline-separated Markdown paths to link-audit",
    )
    parser.add_argument(
        "--strict-links",
        action="store_true",
        help="Treat broken local links as errors instead of warnings",
    )
    parser.add_argument(
        "--stale-days",
        type=int,
        default=90,
        help="Warn when catalog last_reviewed is older than N days; -1 disables",
    )
    parser.add_argument(
        "--github-summary",
        action="store_true",
        help="Append summary to GITHUB_STEP_SUMMARY when available",
    )
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    result = AuditResult()

    validate_catalog(root, args.stale_days, result)
    files = load_file_selection(root, args.files_from)
    audit_markdown_links(root, files, args.strict_links, result)

    for finding in result.findings:
        print(finding.render())

    print(
        "Audit complete: "
        f"domains={result.checked_domains}, "
        f"markdown={result.checked_markdown}, "
        f"links={result.checked_links}, "
        f"errors={result.errors}, warnings={result.warnings}"
    )

    if args.github_summary:
        write_github_summary(result)

    return 1 if result.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
