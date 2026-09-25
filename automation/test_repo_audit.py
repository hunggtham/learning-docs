import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import repo_audit


class RepoAuditTests(unittest.TestCase):
    def test_parse_catalog_domains(self):
        text = """---
domains:
  - id: frontend
    path: 10_frontend/
    entrypoint: 10_frontend/README.md
    status: canonical
    last_reviewed: 2026-09-26
    scope: Frontend
supporting:
"""
        domains = repo_audit.parse_catalog_domains(text)
        self.assertEqual(len(domains), 1)
        self.assertEqual(domains[0].id, "frontend")
        self.assertEqual(domains[0].entrypoint, "10_frontend/README.md")

    def test_strip_fenced_code(self):
        text = (
            "[ok](a.md)\n"
            "```md\n"
            "[ignore](missing.md)\n"
            "```\n"
            "[ok2](b.md)\n"
        )
        targets = [target for target, _ in repo_audit.extract_markdown_targets(text)]
        self.assertEqual(targets, ["a.md", "b.md"])

    def test_link_audit_relative_fragment_and_external(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            docs = root / "docs"
            docs.mkdir()
            (docs / "target.md").write_text("# Target\n", encoding="utf-8")
            source = docs / "source.md"
            source.write_text(
                "[good](target.md#section) "
                "[external](https://example.com) "
                "[anchor](#local)\n",
                encoding="utf-8",
            )

            result = repo_audit.AuditResult()
            repo_audit.audit_markdown_links(root, [source], True, result)

            self.assertEqual(result.errors, 0)
            self.assertEqual(result.checked_links, 1)

    def test_missing_link_can_be_error(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            source = root / "source.md"
            source.write_text("[bad](missing.md)\n", encoding="utf-8")

            result = repo_audit.AuditResult()
            repo_audit.audit_markdown_links(root, [source], True, result)

            self.assertEqual(result.errors, 1)
            self.assertEqual(result.findings[0].code, "link.missing")

    def test_catalog_validation(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            docs = root / "docs"
            docs.mkdir()
            (docs / "README.md").write_text("# Docs\n", encoding="utf-8")
            (root / "CATALOG.md").write_text(
                """domains:
  - id: docs
    path: docs/
    entrypoint: docs/README.md
    status: canonical
    last_reviewed: 2026-09-26
    scope: Docs
supporting:
""",
                encoding="utf-8",
            )

            result = repo_audit.AuditResult()
            repo_audit.validate_catalog(root, -1, result)

            self.assertEqual(result.errors, 0)
            self.assertEqual(result.checked_domains, 1)

    def test_reference_style_definition(self):
        text = "Read [the guide][guide].\n\n[guide]: docs/guide.md\n"
        targets = [target for target, _ in repo_audit.extract_markdown_targets(text)]
        self.assertEqual(targets, ["docs/guide.md"])


if __name__ == "__main__":
    unittest.main()
