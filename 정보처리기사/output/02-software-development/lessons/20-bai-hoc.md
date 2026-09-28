# 094 & 094-1: IPC 및 모듈별 알고리즘 구현 (IPC & Algorithm by Module Type)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **094 & 094-1: IPC 및 모듈별 알고리즘 구현 (IPC & Algorithm by Module Type)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

IPC, 모듈별, 알고리즘, 구현

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **핵심 031: 모듈 구현 (Module Implementation)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **095 & 096: 단위 모듈 테스트 및 테스트 케이스 (Unit Test & Test Case)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **094 & 094-1: IPC 및 모듈별 알고리즘 구현 (IPC & Algorithm by Module Type)** và nối nó với **095 & 096: 단위 모듈 테스트 및 테스트 케이스 (Unit Test & Test Case)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 094 & 094-1: IPC 및 모듈별 알고리즘 구현 (IPC & Algorithm by Module Type)

### IPC (Inter-Process Communication - Giao tiếp giữa các tiến trình)
- 모듈 간 또는 복수의 프로세스 간 통신을 위한 인터페이스. (Cách các chương trình đang chạy nói chuyện với nhau).
- **Các phương pháp IPC:**
  - **dùng chung (shared / 공유) bộ nhớ (memory / 메모리):** Nhanh nhất. Các tiến trình (process / 프로세스) dùng chung 1 vùng RAM.
  - **Socket (Ổ cắm):** Giao tiếp qua mạng.
  - **Semaphores (Cờ hiệu):** Đồng bộ hóa, khóa (Locking) tài nguyên dùng chung.
  - **Pipes (Ống dẫn):** Dùng RAM theo kiểu FIFO, tại 1 thời điểm chỉ 1 tiến trình (process / 프로세스) được dùng.
  - **Message Queueing (Hàng đợi tin nhắn):** Truyền tin bất đồng bộ.

### 알고리즘 구현 모듈 (Các loại Module khi lập trình)
- **디바이스 드라이버 모듈 (Device Driver):** Điều khiển phần cứng ngoại vi (vd: Máy in).
- **네트워크 모듈 (Network):** Truyền thông dữ liệu mạng.
- **파일 모듈 (File):** Truy xuất cấu trúc tệp (file / 파일) trên đĩa cứng.
- **메모리 모듈 (Memory):** Quản lý RAM, cấp phát bộ nhớ ảo, hoặc làm IPC.
- **프로세스 모듈 (Process):** Tạo và quản lý các tiến trình khác.

- 💡 **Mẹo ghi nhớ (Mnemonics):** IPC là gửi thư cho nhau. dùng chung (shared / 공유) bộ nhớ (memory / 메모리) = Bảng tin chung (Nhanh nhất). Semaphore = Cái khóa cửa nhà vệ sinh (Ai đang dùng thì khóa lại).

---
