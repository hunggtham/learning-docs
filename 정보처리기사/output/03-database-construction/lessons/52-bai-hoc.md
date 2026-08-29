# 7. 집합연산자 및 조인 (Toán tử tập hợp và JOIN)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **7. 집합연산자 및 조인 (Toán tử tập hợp và JOIN)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

집합연산자, 조인

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 7. 집합연산자 및 조인 (Toán tử tập hợp và JOIN)

### 집합 연산자 (Toán tử tập hợp)
- `UNION`: Hợp (Loại bỏ trùng lặp).
- `UNION ALL`: Hợp tất cả (Giữ nguyên trùng lặp).
- `INTERSECT`: Giao (Chỉ lấy phần chung).
- `MINUS` / `EXCEPT`: Hiệu (Lấy bảng 1 trừ đi các dòng có trong bảng 2).

### 조인 (JOIN)
- **INNER JOIN**: Lấy các dòng có dữ liệu khớp nhau (Giao). `SELECT * FROM A INNER JOIN B ON A.id = B.id;`
- **OUTER JOIN (LEFT, RIGHT, FULL)**: Lấy cả dữ liệu không khớp. Bên thiếu dữ liệu sẽ điền NULL.
  - Cú pháp Oracle (+): `WHERE A.id = B.id(+)` (Đây là LEFT OUTER JOIN vì dấu (+) nằm ở bảng B, tức là bảng B thiếu cũng không sao).
- **SELF JOIN**: Bảng tự JOIN với chính nó. (Dùng `AS` để tạo bí danh).
- **CROSS JOIN**: Tích Đề-các (Cartesian product), bắt cặp tất cả các dòng của 2 bảng.

---
