# 287. UNIX 시스템의 구성 (Cấu trúc hệ thống UNIX)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **287. UNIX 시스템의 구성 (Cấu trúc hệ thống UNIX)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

UNIX, 시스템의, 구성

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 287. UNIX 시스템의 구성 (Cấu trúc hệ thống UNIX)
### TẦNG A – NOTE NÉN (ÔN / ĐI THI)
- **개념 (Khái niệm)**: 커널(Kernel), 쉘(Shell), 유틸리티(Utility)의 계층적 구조. (Cấu trúc phân tầng gồm Kernel, Shell và Utility.)
- **핵심 키워드 (Từ khóa)**: 커널(Kernel - Hạt nhân), 쉘(Shell - Vỏ), 명령어 해석기 (Trình thông dịch lệnh).
- **시험 포인트 (Điểm thi)**: 커널(핵심 및 상주)과 쉘(명령어 해석기 및 인터페이스)의 역할을 명확히 구분. (Phân biệt vai trò của Kernel và Shell.)

### TẦNG B – NOTE 보충 (HIỂU SÂU)
- **커널 (Kernel)**: 하드웨어를 직접 관리, 프로세스/메모리/파일 관리. 주기억장치에 상주. (Quản lý trực tiếp phần cứng, tiến trình, bộ nhớ. Nằm thường trực trong RAM.)
- **쉘 (Shell)**: 사용자의 명령을 인식하여 수행하는 명령어 해석기 (인터페이스). (Trình biên dịch lệnh, nhận lệnh từ người dùng và gọi chương trình.)
- **유틸리티 (Utility)**: 에디터, 컴파일러 등 응용 프로그램. (Các chương trình ứng dụng như trình soạn thảo, biên dịch.)
- **예시 (Ví dụ)**: 식당에서 사용자가 주문(명령)을 하면 종업원(Shell)이 이를 받아 주방장(Kernel)에게 전달하여 요리(하드웨어 제어)를 하는 구조. (Khách hàng gọi món (Lệnh) -> Phục vụ bàn (Shell) -> Đầu bếp (Kernel) xử lý nấu nướng.)
- 💡 **Mẹo ghi nhớ**: Kernel là **Lõi** (Hardware), Shell là **Vỏ** (Giao tiếp người dùng).
