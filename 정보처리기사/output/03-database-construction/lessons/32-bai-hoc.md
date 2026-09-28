# 193. 뷰 (View)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **193. 뷰 (View)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

193. 뷰 (View)

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **150-155. 데이터 조작어 (DML) 확장 및 조건 연산자**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **8. 서브쿼리와 뷰 (Truy vấn con và View)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **193. 뷰 (View)** và nối nó với **8. 서브쿼리와 뷰 (Truy vấn con và View)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 193. 뷰 (View)
- 기본 테이블로부터 유도된 가상 테이블 (물리적 구현 X).
- 장점: 논리적 데이터 독립성, 보안 강화. 단점: 인덱스 불가, 뷰 정의 변경 불가, 갱신 제약.
- **VI (Vietnamese) (Tiếng Việt):** Khung nhìn (View). Bảng ảo. Ưu điểm: Độc lập dữ liệu, bảo mật. Nhược điểm: Không có chỉ mục (index / 인덱스) độc lập, khó cập nhật.
