# 운영체제 - 메모리 및 프로세스 관리 (OS - Memory & Process Management)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **운영체제 - 메모리 및 프로세스 관리 (OS - Memory & Process Management)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

운영체제, 메모리, 프로세스, 관리

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 운영체제 - 메모리 및 프로세스 관리 (OS - Memory & Process Management)
### 200. 기억장치의 배치 전략 (Memory Placement Strategies / Chiến lược cấp phát bộ nhớ)
- **최초 적합 (First Fit)**: 첫 번째 분할 영역에 배치 (Vị trí trống đầu tiên đủ lớn).
- **최적 적합 (Best Fit)**: 단편화가 가장 작은 영역 (Vị trí trống vừa vặn nhất, để lại ít rác nhất).
- **최악 적합 (Worst Fit)**: 단편화가 가장 큰 영역 (Vị trí trống lớn nhất).
  - 💡 *Mẹo ghi nhớ*: First = Nhanh nhất. Best = Tiết kiệm nhất. Worst = Còn lại khoảng trống lớn nhất.

### 201. 페이지 교체 알고리즘 - FIFO (Page Replacement - FIFO / Thuật toán thay thế trang)
- 가장 먼저 들어와서 가장 오래 있었던 페이지를 교체 (Thay thế trang vào bộ nhớ sớm nhất - First In First Out).

### 202. 스래싱 (Thrashing)
- 프로세스 처리 시간보다 페이지 교체 시간이 더 많아지는 현상 (Hiện tượng mất nhiều thời gian cho việc tráo đổi trang bộ nhớ hơn là thực thi tiến trình).
  - 💡 *Mẹo ghi nhớ*: Thrashing = Kẹt xe bộ nhớ (quá tải).

### 203. 프로세스 상태 (Process States / Trạng thái tiến trình)
- 제출(Submit) → 접수(Hold) → 준비(Ready) → 실행(Run) → 대기(Wait/Block) → 종료(Exit).
  - 💡 *Mẹo ghi nhớ*: Nộp -> Nhận -> Chờ chạy -> Chạy -> (Tạm dừng nếu cần) -> Xong.

### 204. 스케줄링 - SJF (Shortest Job First / Việc ngắn làm trước)
- 실행 시간이 가장 짧은 프로세스에게 먼저 CPU 할당 (Ưu tiên tiến trình có thời gian thực thi ngắn nhất).

### 205. 스케줄링 - HRN (Highest Response-ratio Next)
- 우선순위 = `(대기 시간 + 서비스 시간) / 서비스 시간`
- (Priority = (Wait time + Service time) / Service time).
  - *Example / Ví dụ*: Đợi 10, Chạy 5 => `(10+5)/5 = 3`.
  - 💡 *Mẹo ghi nhớ*: Công thức = `(Đợi + Chạy) / Chạy`. Số càng lớn càng ưu tiên. Giải quyết nhược điểm của SJF (tiến trình dài bị bỏ đói).
