# 18. 파티셔닝과 암호화 (Phân vùng và Mã hóa)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **18. 파티셔닝과 암호화 (Phân vùng và Mã hóa)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

파티셔닝과, 암호화

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 18. 파티셔닝과 암호화 (Phân vùng và Mã hóa)

### 파티셔닝 (Partitioning)
Chia các bảng lớn thành các phần nhỏ (Partition) để dễ quản lý và tăng hiệu suất.
- **범위 분할 (Range):** Phân chia theo khoảng (VD: Tháng 1, Tháng 2).
- **해시 분할 (Hash):** Dùng hàm băm để chia đều. Dữ liệu phân bố đều nhưng khó tìm theo khoảng.
- **목록 분할 (List):** Phân chia theo danh sách giá trị (VD: Nước: VN, KR, US).
- **조합 분할 (Composite):** Kết hợp các phương pháp trên.
- **라운드 로빈 (Round Robin):** Chia xoay vòng đều nhau tuần tự (Không cần khóa).

### 데이터베이스 암호화 (Mã hóa CSDL)
- **암호화 (Encryption):** Biến 평문 (Plaintext - Văn bản gốc) thành 암호문 (Ciphertext - Bản mã).
- **복호화 (Decryption):** Giải mã từ Ciphertext về Plaintext.
- **키 (Key):** Chìa khóa dùng để mã hóa và giải mã.
---
