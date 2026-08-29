# 프로그래밍 언어 기초 (Mở rộng) (Programming Language Basics - Extended)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **프로그래밍 언어 기초 (Mở rộng) (Programming Language Basics - Extended)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

프로그래밍, 언어, 기초

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 프로그래밍 언어 기초 (Mở rộng) (Programming Language Basics - Extended)
### 236. Python의 시퀀스 자료형 (Python Sequence Type / Kiểu chuỗi trong Python - Nhắc lại)
- **리스트 (List)**: Khác kiểu dữ liệu, thêm xóa được.
- **튜플 (Tuple)**: Không thể thay đổi (immutable).
- **range**: Sinh dãy số liên tiếp.

### 구조체 정의 예 (Struct Definition Example / Ví dụ định nghĩa Struct)
- C언어: `struct sawon { char name[10]; int pay; };`

### 235. JAVA의 데이터 타입 크기 (JAVA Data Type Sizes / Kích thước kiểu dữ liệu JAVA)
- **문자 (Char)**: `char` (2Byte - Khác với C là 1Byte).
- **정수 (Integer)**: `byte` (1Byte), `short` (2Byte), `int` (4Byte), `long` (8Byte).
- **실수 (Float)**: `float` (4Byte), `double` (8Byte).
- **논리 (Boolean)**: `boolean` (1Byte).
  - 💡 *Mẹo ghi nhớ*: Java dùng Unicode nên `char` là 2 Bytes. Có thêm kiểu `byte` (1 Byte).

### 237. 변수의 개요 및 헝가리안 표기법 (Variables & Hungarian Notation / Biến và Ký pháp Hungary)
- **헝가리안 표기법 (Hungarian Notation)**: 변수 선언 시 변수명에 데이터 타입을 명시하는 것. (Gắn tiền tố kiểu dữ liệu vào tên biến, vd: `strName`, `nAge`).
- Mọi câu lệnh khai báo biến trong C/Java đều phải kết thúc bằng dấu chấm phẩy `;`.

### 238. 가비지 콜렉터 (Garbage Collector / Trình thu gom rác - Nhắc lại)
- 메모리 공간을 강제로 해제 (Giải phóng không gian bộ nhớ không còn sử dụng).
