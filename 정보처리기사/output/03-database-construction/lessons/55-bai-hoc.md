# 22. 기타 주요 개념 (Các khái niệm quan trọng khác)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **22. 기타 주요 개념 (Các khái niệm quan trọng khác)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

기타, 주요, 개념

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 22. 기타 주요 개념 (Các khái niệm quan trọng khác)

### CRUD 분석 (Phân tích CRUD)
- Tạo ma trận (Matrix) giữa **Process (Tiến trình)** và **Table (Bảng)**.
- Đánh dấu **C**reate, **R**ead, **U**pdate, **D**elete để xem bảng nào bị thao tác nhiều/ít, phát hiện bảng bị bỏ sót (ít nhất mỗi bảng phải có 1 thao tác).

### MyBatis (프레임워크)
- Khung làm việc (Framework) giúp đơn giản hóa JDBC trong Java.
- **Đặc điểm:** Tách mã SQL ra khỏi mã Java (lưu trong file XML hoặc Annotation), thân thiện với lập trình viên SQL.

### 시스템 카탈로그 (System Catalog)
- **Định nghĩa:** CSDL đặc biệt chứa "dữ liệu về dữ liệu" (Metadata / Data Dictionary).
- **Đặc điểm:** Chỉ có hệ thống (DBMS) mới được quyền cập nhật (Tự động cập nhật). Người dùng chỉ có quyền **SELECT (Đọc)**.

### 연산자 우선순위 (Thứ tự ưu tiên toán tử trong SQL)
- 산술 연산자 (Toán học: `* / + -`) **>** 관계 연산자 (So sánh: `< > = !=`) **>** 논리 연산자 (Logic: `NOT > AND > OR`).

> 💡 **Mẹo ghi nhớ:** **Toán - Quan - Lo** (Toán học - Quan hệ - Logic). Nhân chia trước, cộng trừ sau, rồi đến so sánh, cuối cùng là AND/OR.

EOF
