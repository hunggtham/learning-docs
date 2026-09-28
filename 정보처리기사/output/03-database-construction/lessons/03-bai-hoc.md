# 103. 물리적 설계 (Physical Design)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **103. 물리적 설계 (Physical Design)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

물리적, 설계

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **102. 논리적 설계 (Logical Design / Data Modeling)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **163-167. 데이터베이스 설계 순서 (Database Design Process)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **103. 물리적 설계 (Physical Design)** và nối nó với **163-167. 데이터베이스 설계 순서 (Database Design Process)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 103. 물리적 설계 (Physical Design)
- 논리적 구조로 표현된 데이터를 물리적 구조의 데이터로 변환하는 과정이다.
- 데이터베이스 파일의 저장 구조 및 액세스 경로를 결정한다.
- **VI (Vietnamese) (Tiếng Việt):** Thiết kế vật lý. Quá trình chuyển đổi dữ liệu cấu trúc lô-gic (logic / 논리) thành cấu trúc vật lý (lưu trữ ổ đĩa, đường dẫn truy cập).
- **Example (Korean/Vietnamese):** 테이블에 인덱스를 생성하여 검색 속도를 높이는 것. / Tạo chỉ mục (index / 인덱스) trên bảng để tăng tốc độ tìm kiếm.
- 💡 **Mẹo ghi nhớ:** Vật-Lưu (Thiết kế Vật lý = Cấu trúc Lưu trữ).
