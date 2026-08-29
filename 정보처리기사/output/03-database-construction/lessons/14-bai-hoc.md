# 14. 키(Key)의 종류와 데이터베이스 무결성 (Các loại Khóa & Tính Toàn vẹn)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **14. 키(Key)의 종류와 데이터베이스 무결성 (Các loại Khóa & Tính Toàn vẹn)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

14. 키(Key)의 종류와 데이터베이스 무결성 (Các loại Khóa & Tính Toàn vẹn)

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 14. 키(Key)의 종류와 데이터베이스 무결성 (Các loại Khóa & Tính Toàn vẹn)

### 키(Key) 종류 (Các loại Khóa)
| 종류 (Loại) | 설명 (Mô tả) | Tính chất (VN) |
|---|---|---|
| **슈퍼키 (Super Key)** | 튜플을 구별할 수 있는 속성 집합. | **Tính duy nhất (유일성).** |
| **후보키 (Candidate Key)** | 기본키가 될 수 있는 키 (유일성 + 최소성). | **Duy nhất + Tối thiểu (최소성).** (Không dư thừa thuộc tính). |
| **기본키 (Primary Key)** | 후보키 중 선택된 주키. NULL 불가. | Khóa chính. **Không được trùng, Không được NULL.** |
| **대체키 (Alternate Key)** | 기본키로 선택되지 못한 나머지 후보키. | Khóa thay thế (Khóa phụ). |
| **외래키 (Foreign Key)** | 다른 릴레이션의 기본키를 참조하는 속성. | Khóa ngoại. Dùng để liên kết 2 bảng. |

### 무결성 (Integrity - Tính toàn vẹn / chính xác)
- **개체 무결성 (Entity):** Khóa chính (Primary Key) không được trùng lặp và **không được NULL**.
- **참조 무결성 (Referential):** Khóa ngoại (Foreign Key) phải khớp với Khóa chính của bảng tham chiếu, hoặc có thể là NULL.
- **도메인 무결성 (Domain):** Giá trị phải nằm trong phạm vi định nghĩa (ví dụ: Giới tính chỉ là Nam/Nữ).
- **사용자 정의 무결성 (User-defined):** Phải thỏa mãn các điều kiện do người dùng tự định nghĩa.

---
