from __future__ import annotations

import base64

import hashlib
import json
import os
import re
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote

import httpx


@dataclass
class Usage:
    input_tokens: int = 0
    output_tokens: int = 0
    api_calls: int = 0
    estimated_usd: float = 0.0

PARTS = [
    ("01_소프트웨어_설계.md", "1과목 소프트웨어 설계", r"^#{1,4}\s*(?:1과목\s*소프트웨어\s*설계|Môn\s*1\s*[:.]\s*Thiết kế Phần mềm)"),
    ("02_소프트웨어_개발.md", "2과목 소프트웨어 개발", r"^#{1,4}\s*(?:2과목\s*소프트웨어\s*개발|Môn\s*2\s*[:.]\s*Phát triển phần mềm)"),
    ("03_데이터베이스_구축.md", "3과목 데이터베이스 구축", r"^#{1,4}\s*(?:3과목\s*데이터베이스\s*구축|Môn\s*3\s*[:.]\s*Xây dựng Cơ sở dữ liệu)"),
    ("04_프로그래밍_언어_활용.md", "4과목 프로그래밍 언어 활용", r"^#{1,4}\s*(?:4과목\s*프로그래밍\s*언어\s*활용|Môn\s*4\s*[:.]\s*Vận dụng Ngôn ngữ lập trình)"),
    ("05_정보시스템_구축관리.md", "5과목 정보시스템 구축관리", r"^#{1,4}\s*(?:5과목\s*정보시스템\s*구축\s*관리|Môn\s*5\s*[:.]\s*Quản lý Xây dựng Hệ thống Thông tin)"),
]

class Pipeline:
    def __init__(self):
        self.repo = os.getenv("GITHUB_REPOSITORY", "hunggtham/learning-docs")
        self.branch = os.getenv("GITHUB_BRANCH", "docs/정보처리기사")
        self.token = os.getenv("GITHUB_TOKEN", "")
        self.worktree = Path(os.getenv("WORKTREE", "/data/repo"))
        self.openai_key = os.getenv("OPENAI_API_KEY", "")
        self.openai_base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
        self.draft_model = os.getenv("OPENAI_DRAFT_MODEL", "gpt-5.6-terra")
        self.qa_model = os.getenv("OPENAI_QA_MODEL", "gpt-5.6-sol")
        self.draft_effort = os.getenv("OPENAI_DRAFT_EFFORT", "none")
        self.qa_effort = os.getenv("OPENAI_QA_EFFORT", "low")
        self.max_chars = int(os.getenv("MAX_CHARS_PER_CHUNK", "18000"))
        self.max_output_tokens = int(os.getenv("MAX_OUTPUT_TOKENS", "10000"))
        self.max_api_calls = int(os.getenv("MAX_API_CALLS", "50"))
        self.max_run_usd = float(os.getenv("MAX_RUN_USD", "5"))
        self.push_changes = os.getenv("PUSH_CHANGES", "false").lower() == "true"
        self.target_parts = int(os.getenv("TARGET_PARTS", "0"))
        self.max_chunks_per_part = int(os.getenv("MAX_CHUNKS_PER_PART", "0"))
        self.usage = Usage()
        self.prompt_dir = Path(__file__).parent / "prompts"

    def git_env(self):
        env = os.environ.copy()
        env["GIT_AUTHOR_NAME"] = env["GIT_COMMITTER_NAME"] = "learning-docs-bot"
        env["GIT_AUTHOR_EMAIL"] = env["GIT_COMMITTER_EMAIL"] = "learning-docs-bot@users.noreply.github.com"
        env["GIT_TERMINAL_PROMPT"] = "0"
        auth = base64.b64encode(f"x-access-token:{self.token}".encode()).decode()
        env["GIT_CONFIG_COUNT"] = "1"
        env["GIT_CONFIG_KEY_0"] = "http.extraHeader"
        env["GIT_CONFIG_VALUE_0"] = f"Authorization: Basic {auth}"
        return env

    def git(self, *args, check=True):
        result = subprocess.run(
            ["git", *args],
            cwd=self.worktree if self.worktree.exists() else None,
            env=self.git_env(),
            text=True,
            capture_output=True,
        )
        if check and result.returncode:
            raise RuntimeError(result.stderr.strip() or result.stdout.strip())
        return result.stdout.strip()

    def sync(self):
        if not self.token:
            raise RuntimeError("GITHUB_TOKEN is required")

        repo_url = f"https://github.com/{self.repo}.git"
        env = self.git_env()
        if not (self.worktree / ".git").exists():
            self.worktree.parent.mkdir(parents=True, exist_ok=True)
            subprocess.run(
                ["git", "clone", "--branch", self.branch, "--single-branch", repo_url, str(self.worktree)],
                env=env,
                check=True,
                timeout=60,
            )

        # Keep the token out of .git/config and out of command arguments.
        self.git("remote", "set-url", "origin", repo_url)
        self.git("fetch", "origin", self.branch)
        self.git("checkout", self.branch)
        self.git("reset", "--hard", f"origin/{self.branch}")

    @staticmethod
    def clean(text: str) -> str:
        text = text.replace("<br>", "\n").replace("<br/>", "\n")
        text = re.sub(r"</?mark>", "", text)
        text = re.sub(r"^#{1,6}\s*$", "", text, flags=re.M)
        text = re.sub(r"[ \t]+\n", "\n", text)
        return re.sub(r"\n{3,}", "\n\n", text).strip()

    @staticmethod
    def split_parts(text: str) -> dict[str, str]:
        hits = []
        for filename, name, pattern in PARTS:
            match = re.search(pattern, text, re.I | re.M)
            if match:
                hits.append((match.start(), filename, name))
        hits.sort()
        result = {}
        for idx, (start, filename, _) in enumerate(hits):
            end = hits[idx + 1][0] if idx + 1 < len(hits) else len(text)
            result[filename] = text[start:end].strip()
        return result

    def chunks(self, text: str) -> list[str]:
        sections = re.split(r"(?=^###\s+)", text, flags=re.M)
        chunks, current = [], ""
        for section in sections:
            if current and len(current) + len(section) > self.max_chars:
                chunks.append(current.strip())
                current = ""
            if len(section) > self.max_chars:
                for i in range(0, len(section), self.max_chars):
                    if current:
                        chunks.append(current.strip()); current = ""
                    chunks.append(section[i:i+self.max_chars].strip())
            else:
                current += section
        if current.strip():
            chunks.append(current.strip())
        return chunks

    @staticmethod
    def core_ids(text: str) -> set[str]:
        return set(re.findall(r"(?<!\d)(\d{3})(?!\d)", text))

    @staticmethod
    def sections(text: str) -> list[str]:
        return [item.strip() for item in re.split(r"(?=^###\s+)", text, flags=re.M) if item.strip()]

    def aligned_translation(self, source_chunk: str, translation: str) -> str:
        wanted = self.core_ids(source_chunk)
        if not wanted:
            return "(Không tìm thấy mã 핵심 để căn chỉnh; chỉ dùng SOURCE làm evidence.)"
        matched = [section for section in self.sections(translation) if self.core_ids(section) & wanted]
        if not matched:
            return "(Không có đoạn dịch mang cùng mã 핵심; chỉ dùng SOURCE làm evidence.)"
        return "\n\n".join(matched)

    @staticmethod
    def price_per_million(model: str) -> tuple[float, float]:
        if model == "gpt-5.6-sol":
            return float(os.getenv("SOL_INPUT_USD_PER_MTOK", "5")), float(os.getenv("SOL_OUTPUT_USD_PER_MTOK", "30"))
        return float(os.getenv("TERRA_INPUT_USD_PER_MTOK", "2")), float(os.getenv("TERRA_OUTPUT_USD_PER_MTOK", "12"))

    def reserve_request(self, prompt: str, model: str, max_output_tokens: int):
        if self.usage.api_calls >= self.max_api_calls:
            raise RuntimeError(f"MAX_API_CALLS={self.max_api_calls} reached")
        input_price, output_price = self.price_per_million(model)
        approximate_input_tokens = max(1, len(prompt) // 3)
        worst_case = (approximate_input_tokens * input_price + max_output_tokens * output_price) / 1_000_000
        if self.usage.estimated_usd + worst_case > self.max_run_usd:
            raise RuntimeError(
                f"Cost guard stopped before request: estimated ${self.usage.estimated_usd + worst_case:.4f} "
                f"would exceed MAX_RUN_USD=${self.max_run_usd:.2f}"
            )

    @staticmethod
    def output_text(data: dict) -> str:
        pieces = []
        for item in data.get("output", []):
            if item.get("type") != "message":
                continue
            for content in item.get("content", []):
                if content.get("type") == "output_text":
                    pieces.append(content.get("text", ""))
        return "\n".join(pieces).strip()

    def ask(self, prompt: str, stage: str) -> tuple[str, str]:
        if not self.openai_key:
            raise RuntimeError("OPENAI_API_KEY is required")
        model = self.draft_model if stage == "draft" else self.qa_model
        effort = self.draft_effort if stage == "draft" else self.qa_effort
        output_limit = self.max_output_tokens
        self.reserve_request(prompt, model, output_limit)
        with httpx.Client(timeout=1800) as client:
            response = client.post(
                f"{self.openai_base_url}/responses",
                headers={"Authorization": f"Bearer {self.openai_key}", "Content-Type": "application/json"},
                json={
                    "model": model,
                    "input": prompt,
                    "reasoning": {"effort": effort},
                    "max_output_tokens": output_limit,
                    "store": False,
                    "text": {"verbosity": "medium"},
                },
            )
            response.raise_for_status()
            data = response.json()
        if data.get("status") != "completed":
            raise RuntimeError(f"OpenAI response incomplete: {data.get('incomplete_details')}")
        text = self.output_text(data)
        if not text:
            raise RuntimeError("OpenAI response contained no output_text")
        usage = data.get("usage") or {}
        input_tokens = int(usage.get("input_tokens", 0))
        output_tokens = int(usage.get("output_tokens", 0))
        input_price, output_price = self.price_per_million(model)
        self.usage.input_tokens += input_tokens
        self.usage.output_tokens += output_tokens
        self.usage.api_calls += 1
        self.usage.estimated_usd += (input_tokens * input_price + output_tokens * output_price) / 1_000_000
        return text, model

    @staticmethod
    def json_object(raw: str) -> dict:
        start, end = raw.find("{"), raw.rfind("}")
        if start < 0 or end < start:
            raise ValueError("Quality model did not return JSON")
        return json.loads(raw[start:end + 1])

    def render_part(self, filename, part_name, source, translation):
        chapter_prompt = (self.prompt_dir / "chapter.md").read_text(encoding="utf-8")
        quality_prompt = (self.prompt_dir / "quality.md").read_text(encoding="utf-8")
        source_chunks = self.chunks(source)
        drafts, used_models, all_issues = [], [], []
        for index, chunk in enumerate(source_chunks):
            if self.max_chunks_per_part and index >= self.max_chunks_per_part:
                break
            translated = self.aligned_translation(chunk, translation) if translation else "(Không có bản dịch tham khảo.)"
            prompt = chapter_prompt.format(
                subject="정보처리기사", part_name=part_name, chunk_number=index + 1,
                chunk_total=len(source_chunks), source=chunk, translation=translated,
            )
            draft, model = self.ask(prompt, "draft")
            used_models.append(model)
            qa_raw, qa_model = self.ask(quality_prompt.format(evidence=chunk, translation=translated, chapter=draft), "qa")
            used_models.append(qa_model)
            try:
                qa = self.json_object(qa_raw)
                drafts.append(qa.get("revised_markdown") or draft)
                all_issues.extend(qa.get("issues", []))
            except Exception as exc:
                drafts.append(draft)
                all_issues.append({"severity":"medium", "description":str(exc), "evidence":f"quality response parse, chunk {index + 1}"})
        final = "\n\n".join(drafts)
        return final.strip() + "\n", all_issues, used_models

    def run(self):
        started = time.time()
        if self.token:
            self.sync()
        elif not (self.worktree / ".git").exists():
            raise RuntimeError("GITHUB_TOKEN is required when WORKTREE is not an existing clone")
        source_path = self.worktree / "input/md_from_pdf/2025_정보처리기사_필기_핵심요약.md"
        translation_path = self.worktree / "input/md_translate/2025_정보처리기사_필기_핵심요약_vi_translate_cleaned.md"
        source = self.clean(source_path.read_text(encoding="utf-8"))
        translation = self.clean(translation_path.read_text(encoding="utf-8"))
        digest = hashlib.sha256((source + translation).encode()).hexdigest()
        manifest_path = self.worktree / "output/정보처리기사/manifest.json"
        if manifest_path.exists() and json.loads(manifest_path.read_text()).get("input_sha256") == digest:
            return {"ok": True, "status": "unchanged", "input_sha256": digest}

        source_parts, translation_parts = self.split_parts(source), self.split_parts(translation)
        if len(source_parts) != 5:
            raise RuntimeError(f"Expected 5 source subjects, found {len(source_parts)}")
        output_dir = self.worktree / "output/정보처리기사"
        output_dir.mkdir(parents=True, exist_ok=True)
        report, models = [], []
        selected_parts = PARTS[:self.target_parts] if self.target_parts else PARTS
        for filename, part_name, _ in selected_parts:
            final, issues, used = self.render_part(filename, part_name, source_parts[filename], translation_parts.get(filename, ""))
            (output_dir / filename).write_text(final, encoding="utf-8")
            report.extend({"file": filename, **item} for item in issues)
            models.extend(used)
        (output_dir / "quality-report.md").write_text(self.quality_report(report), encoding="utf-8")
        manifest = {"input_sha256": digest, "status": "sample" if self.target_parts or self.max_chunks_per_part else "complete",
                    "models": sorted(set(models)), "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
                    "quality_issues": len(report), "usage": self.usage.__dict__}
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        if not self.push_changes:
            return {"ok": True, "status": "generated-not-pushed", "seconds": round(time.time() - started),
                    "quality_issues": len(report), "usage": self.usage.__dict__}
        self.git("add", "output/정보처리기사")
        status = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=self.worktree).returncode
        if status == 0:
            return {"ok": True, "status": "no-diff"}
        self.git("commit", "-m", "generate 정보처리기사 textbook")
        self.git("push", "origin", f"HEAD:{self.branch}")
        return {"ok": True, "status": "pushed", "commit": self.git("rev-parse", "HEAD"),
                "seconds": round(time.time() - started), "quality_issues": len(report)}

    @staticmethod
    def quality_report(items):
        lines = ["# Quality report", "", "Các điểm dưới đây cần người học kiểm tra lại khi có mức `high` hoặc `[CẦN KIỂM TRA]`.", ""]
        if not items:
            return "\n".join(lines + ["Không phát hiện vấn đề qua vòng kiểm tra tự động.", ""])
        for item in items:
            lines += [f"- **{item.get('severity','unknown')}** · `{item.get('file','')}` — {item.get('description','')}",
                      f"  - Evidence: {item.get('evidence','')}"]
        return "\n".join(lines) + "\n"
