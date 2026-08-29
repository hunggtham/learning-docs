# 스크립트 및 운영체제 (Script Languages & Operating Systems)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **스크립트 및 운영체제 (Script Languages & Operating Systems)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

스크립트, 운영체제

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 스크립트 및 운영체제 (Script Languages & Operating Systems)
### 193. 스크립트 언어의 종류 (Types of Scripting Languages / Các loại ngôn ngữ kịch bản)
- **자바스크립트 (JavaScript)**: 클라이언트용 웹 동작 제어 (Phía client, điều khiển hành vi web).
- **PHP**: 서버용 스크립트 언어 (Phía server, dùng trên Linux, Unix, Windows).
- **파이썬 (Python)**: 대화형 인터프리터 언어 (Ngôn ngữ thông dịch tương tác).
- **쉘 스크립트 (Shell Script)**: 명령어들의 조합 (Tập hợp các lệnh shell).
- **Basic**: 절차지향 대화형 인터프리터 (Thông dịch tương tác, hướng thủ tục).
  - 💡 *Mẹo ghi nhớ*: JS = Client Web, PHP = Server, Python = Thông dịch, Shell = Lệnh HĐH.

### 194. 쉘 스크립트 제어문 (Shell Script Control Statements)
- **선택형 (Điều kiện)**: `if`, `case`
- **반복형 (Vòng lặp)**: `for`, `while`, `until`

### 195. 라이브러리 (Libraries / Thư viện)
- **표준 (Standard)**: 기본적으로 포함된 모듈 (Tích hợp sẵn trong ngôn ngữ).
- **외부 (External)**: 다운받아 설치한 후 사용 (Phải tải và cài đặt từ bên ngoài).
  - 💡 *Mẹo ghi nhớ*: Built-in = Không cần cài, External = Cần pip/npm/v.v.

### 196. C언어의 stdlib.h (Standard Library in C)
- 자료형 변환, 난수 발생, 메모리 할당 기능을 제공한다. (Cung cấp chức năng ép kiểu, tạo số ngẫu nhiên, cấp phát bộ nhớ).
- 주요 함수 (Các hàm chính): `atoi`, `atof`, `srand`, `rand`, `malloc`, `free`.

### 197. UNIX의 특징 (Features of UNIX / Đặc điểm của UNIX)
- 대부분 C 언어로 작성 (Viết chủ yếu bằng C -> tính di động cao).
- 다중 사용자 (Multi User), 다중 작업 (Multi Tasking) 지원 (Hỗ trợ đa người dùng, đa nhiệm).
- 트리 구조의 파일 시스템 (Hệ thống tập tin cấu trúc cây).
  - 💡 *Mẹo ghi nhớ*: UNIX = C + Cây (Tree) + Đa nhiệm/Đa người dùng.

### 198. UNIX - 커널(Kernel)의 기능 (Functions of Kernel / Chức năng hạt nhân)
- 프로세스, 기억장치, 파일 시스템, 입출력 관리 (Quản lý tiến trình, bộ nhớ, hệ thống tập tin, I/O).
  - 💡 *Mẹo ghi nhớ*: Kernel là "Trái tim" làm mọi công việc cốt lõi phần cứng.

### 199. UNIX - 쉘(Shell)
- 명령어 해석기, 시스템과 사용자 간의 인터페이스 담당. (Trình biên dịch dòng lệnh, giao diện giữa người dùng và HĐH).
  - 💡 *Mẹo ghi nhớ*: Shell là "Vỏ bọc" giao tiếp với Kernel.

### 206. UNIX의 주요 명령어 (UNIX Commands / Lệnh UNIX)
- `fork`: 새로운 프로세스 생성 (Tạo tiến trình mới).
- `uname`: 시스템 정보 표시 (Hiển thị thông tin hệ thống).
- `wait`: 자식 프로세스 종료 대기 (Chờ tiến trình con kết thúc).
- `chmod`: 파일 보호 모드 설정 (Đổi quyền truy cập file).
- `ls`: 파일 목록 확인 (Liệt kê file).
- `cat`: 파일 내용 표시 (Xem nội dung file).
- `chown`: 소유자 변경 (Đổi chủ sở hữu file).
  - 💡 *Mẹo ghi nhớ*: fork (nhân bản, nĩa), chmod (change mode), chown (change owner).
