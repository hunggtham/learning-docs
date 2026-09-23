# 프로세스 관리 (Process Management)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **프로세스 관리 (Process Management)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

프로세스, 관리

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 프로세스 관리 (Process Management)
### 297. 프로세스 (Process / Tiến trình)
- 실행 중인 프로그램, PCB를 가진 프로그램. (Chương trình đang chạy, có chứa khối PCB).

### 298. PCB (Process Control Block / Khối điều khiển tiến trình)
- 프로세스의 상태, 포인터, 식별자(PID), CPU 레지스터 정보 등 저장. (Lưu trạng thái, PID, bộ nhớ, thanh ghi CPU của tiến trình).

### 299 & 300. 프로세스 상태 전이 및 용어 (Process States & Terms)
- **Dispatch (디스패치)**: 준비(Ready) -> 실행(Run). (Cấp phát CPU cho tiến trình).
- **Wake Up (깨움)**: 대기(Wait) -> 준비(Ready). (Hoàn tất I/O, sẵn sàng chạy lại).
- **Spooling (스풀링)**: 입출력 데이터를 디스크에 한꺼번에 저장. (Lưu đệm vào đĩa để xử lý I/O mượt mà).

### 301. 스레드 (Thread / Luồng)
- 프로세스 내에서의 작업 단위. (Đơn vị thực thi nhỏ nhất bên trong một tiến trình).

### 스레드 및 스케줄링 심화 (Threads & Scheduling - Advanced)
- **스레드의 분류 (Thread Types)**:
  - **사용자 수준 (User-level)**: 라이브러리 사용, 빠르지만 구현 어려움. (Dùng thư viện, nhanh nhưng khó code).
  - **커널 수준 (Kernel-level)**: OS 커널이 관리, 구현 쉽지만 속도 느림. (OS quản lý, dễ code nhưng chậm).
- **스레드 장점**: 병행성 증진, 응답 시간 단축, 기억장소 낭비 감소. (Tăng đồng thời, phản hồi nhanh, tiết kiệm RAM).
- **FCFS (First Come First Service = FIFO)**: 도착한 순서대로 처리, 공평하지만 짧은 작업이 오래 대기할 수 있음. (Đến trước phục vụ trước, công bằng nhưng dễ gây kẹt xe).

### 303. UNIX / LINUX 주요 환경 변수 (Environment Variables / Biến môi trường)
- 명령어에서 사용 시 앞에 `$`를 붙인다. (Thêm `$` phía trước để gọi biến).
- **`$HOME`**: 홈 디렉터리 (Thư mục gốc).
- **`$PATH`**: 실행 파일 경로 (Đường dẫn tìm file thực thi).
- **`$PWD`**: 현재 작업 디렉터리 (Thư mục hiện tại).
- **`$LANG`**: 기본 언어 (Ngôn ngữ mặc định).

### 304. UNIX / LINUX 기본 명령어 (Basic Commands - Bổ sung)
- **`fsck`**: 파일 시스템 검사 및 보수 (Kiểm tra và sửa lỗi File System).
- **`getpid`**: 자신의 프로세스 ID (Lấy PID của bản thân).
- **`getppid`**: 부모 프로세스 ID (Lấy PID của tiến trình cha).
