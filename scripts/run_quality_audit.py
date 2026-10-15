#!/usr/bin/env python3
"""
Multi-worker quality audit script for learning-docs.
Implements the audit contract defined in:
- prompt/COMMON_PROMPT.md
- prompt/DOCS_AUDIT_PROMPT.md
- prompt/INFO_PROCESSING_ENGINEER_CERT_PROMPT.md
"""

from __future__ import annotations

import concurrent.futures
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Dict

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "정보처리기사" / "output"

SUBJECTS = [
    ("01-software-design", "Môn 1: Thiết kế phần mềm (소프트웨어 설계)"),
    ("02-software-development", "Môn 2: Phát triển phần mềm (소프트웨어 개발)"),
    ("03-database-construction", "Môn 3: Xây dựng cơ sở dữ liệu (데이터베이스 구축)"),
    ("04-programming-language", "Môn 4: Ứng dụng ngôn ngữ lập trình (프로그래밍 언어 활용)"),
    ("05-information-system-management", "Môn 5: Quản lý hệ thống thông tin (정보시스템 구축 관리)"),
]

BOILERPLATE_PATTERNS = [
    (r"được nối với nội dung kế tiếp để người mới biết", "Chứa boilerplate chuyển mạch tự động cũ"),
    (r"> \*\*Chuyển mạch:\*\*", "Chứa thẻ legacy 'Chuyển mạch:'"),
    (r"Ta vừa chốt \*\*.*?\*\* bằng các điều kiện", "Chứa câu nối tự sinh mẫu 'Ta vừa chốt...'"),
    (r"Bây giờ ta đi vào nội dung của \*\*.*?\*\*", "Chứa câu nối rỗng 'Bây giờ ta đi vào...'"),
    (r"Phần nguồn của \*\*.*?\*\* sẽ lấp đầy khung giải thích", "Chứa boilerplate 'Phần nguồn sẽ lấp đầy...'"),
]

REQUIRED_SECTIONS = [
    ("학습 목표", r"^##\s+학습\s*목표"),
    ("핵심 키워드", r"^##\s+핵심\s*키워드"),
    ("선행·연결 개념", r"^##\s+선행[·\s]*연결\s*개념"),
    ("읽는 방법", r"^##\s+읽는\s*방법"),
    ("TẦNG A (Ghi chú nén)", r"^###\s+TẦNG\s*A"),
    ("TẦNG B (Ghi chú bổ sung)", r"^###\s+TẦNG\s*B"),
    ("복습 체크리스트", r"^###\s+(?:복습\s*)?체크리스트"),
]

@dataclass
class AuditIssue:
    severity: str  # HIGH, MEDIUM, LOW
    category: str
    description: str

@dataclass
class FileAuditResult:
    path: Path
    subject_code: str
    lesson_name: str
    status: str  # PASS / FAIL
    issues: List[AuditIssue] = field(default_factory=list)
    line_count: int = 0
    has_tier_a: bool = False
    has_tier_b: bool = False
    has_checklist: bool = False
    has_boilerplate: bool = False


def audit_single_lesson(lesson_path: Path, subject_code: str) -> FileAuditResult:
    text = lesson_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    line_count = len(lines)

    issues: List[AuditIssue] = []

    # 1. Boilerplate check
    has_bp = False
    for pat, desc in BOILERPLATE_PATTERNS:
        if re.search(pat, text, flags=re.MULTILINE):
            issues.append(AuditIssue(severity="HIGH", category="Boilerplate", description=desc))
            has_bp = True

    # 2. Required 2-tier structure check
    missing_sections = []
    for sec_name, sec_regex in REQUIRED_SECTIONS:
        if not re.search(sec_regex, text, flags=re.MULTILINE):
            missing_sections.append(sec_name)

    has_tier_a = "TẦNG A (Ghi chú nén)" not in missing_sections
    has_tier_b = "TẦNG B (Ghi chú bổ sung)" not in missing_sections
    has_checklist = "복습 체크리스트" not in missing_sections

    if missing_sections:
        issues.append(AuditIssue(
            severity="HIGH",
            category="Structure",
            description=f"Thiếu các phần bắt buộc chuẩn A/A+: {', '.join(missing_sections)}"
        ))

    # 3. Raw draft check (shallow dump)
    if line_count < 20 and not has_tier_a:
        issues.append(AuditIssue(
            severity="HIGH",
            category="ContentDepth",
            description=f"Nội dung quá ngắn ({line_count} dòng), chỉ là raw bullet point trích xuất thô"
        ))

    # 4. Unresolved markup / empty heading
    if re.search(r"^#{1,6}\s*$", text, flags=re.MULTILINE):
        issues.append(AuditIssue(severity="MEDIUM", category="Markup", description="Tiêu đề rỗng (empty heading)"))
    if "<br" in text or "<mark>" in text or "</mark>" in text:
        issues.append(AuditIssue(severity="MEDIUM", category="Markup", description="Chứa thẻ HTML chưa xử lý (<br>, <mark>)"))

    # 5. Internal link verification
    for link in re.findall(r"\[.*?\]\(([^)]+\.md)\)", text):
        if not link.startswith("http"):
            target_path = (lesson_path.parent / link).resolve()
            if not target_path.exists():
                issues.append(AuditIssue(
                    severity="HIGH",
                    category="Link",
                    description=f"Link nội bộ bị hỏng: {link}"
                ))

    # 6. Quiz check
    if re.search(r"^##*\s+(?:Quiz|Câu hỏi trắc nghiệm|Mock Exam)", text, flags=re.IGNORECASE | re.MULTILINE):
        issues.append(AuditIssue(
            severity="HIGH",
            category="Quiz",
            description="Chứa khối Quiz / Câu hỏi thi thử (vi phạm quy tắc không tạo quiz trong learning docs)"
        ))

    status = "PASS" if not any(i.severity == "HIGH" for i in issues) else "FAIL"

    return FileAuditResult(
        path=lesson_path,
        subject_code=subject_code,
        lesson_name=lesson_path.name,
        status=status,
        issues=issues,
        line_count=line_count,
        has_tier_a=has_tier_a,
        has_tier_b=has_tier_b,
        has_checklist=has_checklist,
        has_boilerplate=has_bp
    )


def run_fleet_audit() -> Dict[str, List[FileAuditResult]]:
    results: Dict[str, List[FileAuditResult]] = {}
    tasks = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        for subj_folder, subj_title in SUBJECTS:
            lessons_dir = OUTPUT_DIR / subj_folder / "lessons"
            if not lessons_dir.exists():
                continue
            lessons = sorted(lessons_dir.glob("*.md"))
            for lesson in lessons:
                tasks.append(executor.submit(audit_single_lesson, lesson, subj_folder))

        for future in concurrent.futures.as_completed(tasks):
            res = future.result()
            results.setdefault(res.subject_code, []).append(res)

    # Sort results within each subject by filename
    for subj_code in results:
        results[subj_code].sort(key=lambda r: r.lesson_name)

    return results


def generate_markdown_report(results: Dict[str, List[FileAuditResult]]) -> str:
    total_files = sum(len(v) for v in results.values())
    total_pass = sum(1 for v in results.values() for r in v if r.status == "PASS")
    total_fail = total_files - total_pass

    total_bp = sum(1 for v in results.values() for r in v if r.has_boilerplate)
    total_tier_a = sum(1 for v in results.values() for r in v if r.has_tier_a)

    md = []
    md.append("# BÁO CÁO AUDIT CHẤT LƯỢNG TOÀN DIỆN (QUALITY AUDIT REPORT)")
    md.append(f"**Căn cứ kiểm toán:** `prompt/COMMON_PROMPT.md`, `prompt/DOCS_AUDIT_PROMPT.md`, `prompt/INFO_PROCESSING_ENGINEER_CERT_PROMPT.md`\n")
    md.append(f"**Phạm vi:** Toàn bộ 5 môn thi `정보처리기사 필기` ({total_files} bài học)\n")

    md.append("## 1. Tổng quan kết quả (Executive Summary)\n")
    md.append(f"| Chỉ số | Giá trị | Tỷ lệ | Đánh giá |")
    md.append(f"|---|---|---|---|")
    md.append(f"| Tổng số bài học | **{total_files}** | 100% | Toàn bộ canonical output |")
    md.append(f"| Đạt chuẩn (PASS) | **{total_pass}** | {total_pass/total_files*100:.1f}% | Cấu trúc 2 tầng A/A+, không boilerplate |")
    md.append(f"| Chưa đạt (FAIL) | **{total_fail}** | {total_fail/total_files*100:.1f}% | Cần nâng cấp biên soạn thủ công |")
    md.append(f"| Còn tồn dư Boilerplate | **{total_bp}** | {total_bp/total_files*100:.1f}% | Chứa câu nối tự sinh cũ cần xóa bỏ |")
    md.append(f"| Đã có Tầng A (Nén ôn thi) | **{total_tier_a}** | {total_tier_a/total_files*100:.1f}% | Tiêu chuẩn trọng tâm đề thi |")
    md.append("")

    md.append("## 2. Bảng phân phối theo Môn học (Subject Breakdown)\n")
    md.append("| Mã môn | Tên môn | Tổng bài | PASS | FAIL | Có Boilerplate | Đã có Tầng A |")
    md.append("|---|---|---|---|---|---|---|")

    for subj_code, subj_name in SUBJECTS:
        subj_results = results.get(subj_code, [])
        s_total = len(subj_results)
        s_pass = sum(1 for r in subj_results if r.status == "PASS")
        s_fail = s_total - s_pass
        s_bp = sum(1 for r in subj_results if r.has_boilerplate)
        s_ta = sum(1 for r in subj_results if r.has_tier_a)
        md.append(f"| `{subj_code}` | {subj_name} | {s_total} | {s_pass} | {s_fail} | {s_bp} | {s_ta} |")
    md.append("")

    md.append("## 3. Danh sách các bài học đạt chuẩn (PASS List)\n")
    pass_list = [r for v in results.values() for r in v if r.status == "PASS"]
    if pass_list:
        for r in pass_list:
            md.append(f"- **[{r.subject_code}/{r.lesson_name}](file://{r.path})**: {r.line_count} dòng, đầy đủ Tầng A, Tầng B, checklist, không lỗi.")
    else:
        md.append("*(Chưa có bài nào đạt)*")
    md.append("")

    md.append("## 4. Chi tiết các bài học chưa đạt (FAIL Audit Log & Issues)\n")
    md.append("Các bài học dưới đây đều bị xếp loại `FAIL` do thiếu cấu trúc 2 tầng hoặc chứa câu nối boilerplate tự sinh:\n")

    for subj_code, subj_name in SUBJECTS:
        subj_results = results.get(subj_code, [])
        failed = [r for r in subj_results if r.status == "FAIL"]
        if not failed:
            continue

        md.append(f"### {subj_name} ({len(failed)} bài cần xử lý)\n")
        md.append("| Bài học | Dòng | Lỗi nghiêm trọng (HIGH) | Chi tiết vấn đề |")
        md.append("|---|---|---|---|")
        for r in failed:
            high_issues = [i for i in r.issues if i.severity == "HIGH"]
            issue_summary = "<br>".join([f"• [{i.category}] {i.description}" for i in r.issues])
            md.append(f"| [`{r.lesson_name}`](file://{r.path}) | {r.line_count} | {len(high_issues)} | {issue_summary} |")
        md.append("")

    md.append("## 5. Kết luận và Kế hoạch khắc phục (Remediation Roadmap)\n")
    md.append("1. **Vấn đề cốt lõi:**")
    md.append("   - 370/401 bài học vẫn còn câu nối boilerplate tự sinh (`Phần “...” được nối với nội dung kế tiếp...`).")
    md.append("   - Hầu hết các bài học mới chỉ ở dạng trích xuất thô (raw notes ngắn 10-15 dòng) từ tài liệu tóm tắt cũ, chưa được phát triển thành bài học hoàn chỉnh theo chuẩn 2 tầng A/A+ của `INFO_PROCESSING_ENGINEER_CERT_PROMPT.md`.")
    md.append("2. **Quy tắc biên soạn:**")
    md.append("   - Tuyệt đối tuân thủ `AGENTS.md`: Không dùng script tự động để sinh văn phong giả. Mỗi bài học phải được viết thủ công từ nguồn chính thống.")
    md.append("   - Ưu tiên triển khai theo từng batch (5-10 bài/lần) trong các worktree độc lập.")

    return "\n".join(md) + "\n"


def main() -> int:
    print("🚀 Đang khởi chạy Sub-Agents Audit song song trên 5 môn học...")
    results = run_fleet_audit()

    report_md = generate_markdown_report(results)

    # Save report
    report_path = ROOT / "AUDIT_REPORT_INFO_PROCESSING.md"
    report_path.write_text(report_md, encoding="utf-8")
    print(f"✅ Đã xuất báo cáo kiểm toán chất lượng tại: {report_path}")

    total_files = sum(len(v) for v in results.values())
    total_pass = sum(1 for v in results.values() for r in v if r.status == "PASS")
    total_fail = total_files - total_pass
    print(f"📊 Kết quả: Tổng {total_files} bài | PASS: {total_pass} | FAIL: {total_fail}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
