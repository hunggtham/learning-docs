# 추가: 응용 SW 기초 기술 (4과목 핵심 요약 1)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **추가: 응용 SW 기초 기술 (4과목 핵심 요약 1)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

추가, 응용, 기초, 기술

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 추가: 응용 SW 기초 기술 (4과목 핵심 요약 1)

### 232. 배치 프로그램 (Batch Program)
- 대량의 데이터를 사용자 개입 없이 정해진 순서에 따라 **일괄적으로 처리**하는 방식.
- 야간 시간대 등 자원 소모가 적은 시간에 실행됨.
- **필수 요소 5가지**: 대용량, 자동화, 견고성, 안정성, 성능.

**Giải thích (Vietnamese):**
Chương trình Batch (xử lý hàng loạt) là loại phần mềm tự động chạy ngầm, thường vào ban đêm. Ví dụ: Cuối ngày ngân hàng tổng hợp lại toàn bộ giao dịch trong ngày, xử lý một lúc hàng triệu giao dịch mà không cần người bấm nút.

### 233 & 235. 데이터 타입 크기 (Data Type Sizes - C/C++ vs JAVA)
- **C/C++**: `char`(1바이트), `short`(2바이트), `int`(4바이트), `float`(4바이트), `double`(8바이트).
- **JAVA**: `byte`(1바이트), **`char`(2바이트, 유니코드 지원)**, `int`(4바이트), `boolean`(1바이트).

**Giải thích (Vietnamese):**
Lưu ý quan trọng: Trong C, `char` (kí tự) chiếm 1 byte. Nhưng trong Java, `char` chiếm 2 byte vì Java dùng bảng mã Unicode để hỗ trợ mọi ngôn ngữ trên thế giới (kể cả tiếng Hàn, tiếng Việt).

### 234. C언어의 구조체 (struct)
- 서로 다른 데이터 타입을 하나로 묶어 관리하는 사용자 정의 자료형. 배열(동일 타입)과의 차이점.
- (Ví dụ: Một `struct SinhVien` có thể chứa Tên(string), Tuổi(int), Điểm(float)).

### 236. Python 시퀀스 자료형
- 리스트(List): `[]` 변경 가능.
- 튜플(Tuple): `()` **변경 불가능(Immutable)**.
- (Ví dụ: Tuple dùng để lưu toạ độ GPS không bao giờ đổi).

### 238. 가비지 콜렉터 (Garbage Collector)
- 사용되지 않는 메모리를 자동으로 해제해주는 기능 (메모리 누수 방지). Java 등 현대 언어의 핵심.

### 239 - 244. 각종 연산자
- 산술(`%`, `++`), 관계(`==`, `!=`), 비트(`&`, `|`, `^`, `<<`), 논리(`&&`, `||`), 대입(`+=`), 조건 삼항연산자.
- `a += 1`은 `a = a + 1`과 같다.
- 비트 XOR(`^`): 두 비트가 다를 때만 1을 반환.
