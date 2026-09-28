# 173-177. 키와 무결성, 관계대수 요약 (Keys, Integrity, Relational Algebra)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **173-177. 키와 무결성, 관계대수 요약 (Keys, Integrity, Relational Algebra)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

키와, 무결성, 관계대수, 요약

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **110-114. 키 (Keys)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **5. 스키마 (Schema - Lược đồ)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **173-177. 키와 무결성, 관계대수 요약 (Keys, Integrity, Relational Algebra)** và nối nó với **5. 스키마 (Schema - Lược đồ)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 173-177. 키와 무결성, 관계대수 요약 (Keys, Integrity, Relational Algebra)
*ghi chú (note / 노트): Includes duplicated points consolidated.*
- **도메인 무결성 (Domain Integrity):** 속성 값이 정의된 도메인에 속해야 함.
- **사용자 정의 무결성 (User-Defined Integrity):** 사용자가 정의한 제약 조건 만족.
- **순수 관계 연산자 (Pure Relational Operators):**
  - Select (σ): 수평 연산 (Horizontal) - 튜플 구함.
  - dự án (project / 프로젝트) (π): 수직 연산 (Vertical) - 속성 구함.
  - phép nối (join / 조인) (⋈) / Division (÷).
- **일반 집합 연산자 (Set Operators):** UNION (합집합), INTERSECTION (교집합), DIFFERENCE (차집합), CARTESIAN sản phẩm (product / 제품).
- **VI (Vietnamese) (Tiếng Việt):** Các ràng buộc và Đại số quan hệ (nhắc lại).
  - Toàn vẹn miền (Domain): Giá trị phải nằm trong miền cho phép.
  - Select: Phép toán ngang (lọc hàng).
  - dự án (project / 프로젝트): Phép toán dọc (lọc cột).
  - Phép toán tập hợp: Hợp, Giao, Hiệu, Tích Đề-các.
