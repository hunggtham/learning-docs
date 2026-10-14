# Windows와 UNIX 운영체제 (Windows & UNIX)

## Windows와 UNIX 운영체제 (Windows & UNIX)

### 1. Windows 주요 특징
Phần “1. Windows 주요 특징” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **GUI (Graphic User Interface)**: 마우스 기반 그래픽 환경.
- **선점형 멀티태스킹 (Preemptive Multi-Tasking)**: 응용 프로그램 문제 시 OS가 강제 종료시켜 자원 반환.
- **PnP (Plug and Play)**: 하드웨어 설치 시 OS가 자동 감지 및 환경 구성.
- **OLE (Object Linking and Embedding)**: 문자/그림 개체를 다른 문서에 연결하거나 삽입.
- **긴 파일명**: 최대 255자 지정 가능 (VFAT 이용).

### 2. UNIX 주요 특징
Phần “2. UNIX 주요 특징” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 대화식 시분할 시스템 (Time Sharing System) 및 개방형 시스템 (Open System).
- 주로 **C언어**로 작성되어 이식성이 높고 파일 시스템은 트리(Tree) 구조를 가짐.
- **다중 사용자 (Multi-User)** 및 **다중 작업 (Multi-Tasking)** 지원.

### 3. 파일 디스크립터 (File Descriptor)
Phần “3. 파일 디스크립터 (File Descriptor)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 파일 제어 블록(FCB; File Control Block)이라고도 하며, 시스템(OS)이 필요로 하는 파일에 대한 정보를 가진 제어 블록.
- 파일마다 독립적으로 존재하며 보통 보조기억장치에 있다가 파일이 열릴(Open) 때 주기억장치로 옮겨집니다.

### 4. UNIX 시스템 구조: 커널 (Kernel)
Phần “4. UNIX 시스템 구조: 커널 (Kernel)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- UNIX의 가장 **핵심적인 부분**. 프로그램과 하드웨어 간의 인터페이스 역할을 담당하며 프로세스, 메모리, 입출력 관리 등을 수행합니다.

> **Vietnamese Explanation**:
> Windows nổi bật với giao diện chuột GUI, Plug and Play (cắm là chạy). UNIX là hệ điều hành mã nguồn mở, đa nhiệm, đa người dùng, chủ yếu viết bằng C. Trong UNIX, Kernel (nhân) là phần cốt lõi quản lý phần cứng và giao tiếp với phần mềm. File Descriptor lưu giữ thông tin quan trọng về các file đang được hệ thống quản lý.
