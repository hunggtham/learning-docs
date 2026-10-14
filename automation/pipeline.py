"""Read-only helpers for the retired textbook worker.

This module deliberately does not call a model, create prose, or write files.
Learning-document authoring is manual; structural generation belongs to the
domain-specific source-preserving builders.
"""

from __future__ import annotations

import re


PARTS = [
    ("01_소프트웨어_설계.md", "1과목 소프트웨어 설계", r"^#{1,4}\s*(?:1과목\s*소프트웨어\s*설계|Môn\s*1\s*[:.]\s*Thiết kế Phần mềm)"),
    ("02_소프트웨어_개발.md", "2과목 소프트웨어 개발", r"^#{1,4}\s*(?:2과목\s*소프트웨어\s*개발|Môn\s*2\s*[:.]\s*Phát triển phần mềm)"),
    ("03_데이터베이스_구축.md", "3과목 데이터베이스 구축", r"^#{1,4}\s*(?:3과목\s*데이터베이스\s*구축|Môn\s*3\s*[:.]\s*Xây dựng Cơ sở dữ liệu)"),
    ("04_프로그래밍_언어_활용.md", "4과목 프로그래밍 언어 활용", r"^#{1,4}\s*(?:4과목\s*프로그래밍\s*언어\s*활용|Môn\s*4\s*[:.]\s*Vận dụng Ngôn ngữ lập trình)"),
    ("05_정보시스템_구축관리.md", "5과목 정보시스템 구축관리", r"^#{1,4}\s*(?:5과목\s*정보시스템\s*구축\s*관리|Môn\s*5\s*[:.]\s*Quản lý Xây dựng Hệ thống Thông tin)"),
]


class Pipeline:
    """Compatibility surface for the retired, write-capable worker."""

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
        for index, (start, filename, _) in enumerate(hits):
            end = hits[index + 1][0] if index + 1 < len(hits) else len(text)
            result[filename] = text[start:end].strip()
        return result

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
    def output_text(data: dict) -> str:
        pieces = []
        for item in data.get("output", []):
            if item.get("type") != "message":
                continue
            for content in item.get("content", []):
                if content.get("type") == "output_text":
                    pieces.append(content.get("text", ""))
        return "\n".join(pieces).strip()

    def run(self):
        raise RuntimeError(
            "The textbook worker is disabled: learning prose must be authored and reviewed manually."
        )
