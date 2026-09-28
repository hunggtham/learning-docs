# 핵심 042: 블랙박스 테스트 / 화이트박스 테스트 (Black-Box vs White-Box)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **핵심 042: 블랙박스 테스트 / 화이트박스 테스트 (Black-Box vs White-Box)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

핵심, 블랙박스, 테스트, 화이트박스

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **핵심 041: 테스트 케이스 / 시나리오 / 오라클 (Test Case/Scenario/Oracle)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **핵심 043: 단위 / 통합 / 시스템 / 인수 테스트 (Test Levels)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **핵심 042: 블랙박스 테스트 / 화이트박스 테스트 (Black-Box vs White-Box)** và nối nó với **핵심 043: 단위 / 통합 / 시스템 / 인수 테스트 (Test Levels)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 핵심 042: 블랙박스 테스트 / 화이트박스 테스트 (Black-Box vs White-Box)

Cả hai đều là **động (dynamic / 동적) kiểm thử (test / 테스트)** (Phải chạy code).

### 블랙박스 테스트 (Black-box / Hộp đen / Dựa trên Chức năng)
- Không quan tâm bên trong mã (code / 코드) viết gì, chỉ quan tâm Đầu vào -> Đầu ra. (Dựa trên 명세 - Đặc tả).
- **Kỹ thuật (Các loại):**
  - **동등 분할 (Equivalence Partitioning):** Chia vùng tương đương (Vd: Nhập từ 1-100, thì test số 50 là đủ diện cho vùng đúng).
  - **경곗값 분석 (Boundary Value):** Phân tích giá trị biên (Lỗi hay xảy ra ở ranh giới, vd test số 0, 1, 100, 101).
  - **원인-효과 그래프 (Cause-Effect Graph):** Bảng đồ nhân quả.
  - **오류 예측 (Error Guessing):** Dựa vào kinh nghiệm của tester để đoán lỗi.

### 화이트박스 테스트 (White-box / Hộp trắng / Dựa trên Cấu trúc Code)
- Soi thấu bên trong mã (code / 코드). Đảm bảo mọi dòng lệnh (Statement), mọi nhánh (Branch/Decision) đều được chạy ít nhất 1 lần.
- **Kỹ thuật (Các loại):**
  - **기본 경로 검사 (Base Path):** Đi qua tất cả các con đường mã (code / 코드).
  - **구문 커버리지 (Statement Coverage):** Bao phủ dòng lệnh (Dễ nhất).
  - **결정 커버리지 (Decision/Branch):** Bao phủ nhánh (If True / If False).
  - **조건 커버리지 (Condition):** Bao phủ mọi điều kiện con trong If.
  - **루프 검사 (Loop Testing):** kiểm thử (test / 테스트) các vòng lặp for, while.

- **Vietnamese Explanation:** Black-box giống như lái xe ô tô: đạp ga là chạy, không cần biết động cơ nổ ra sao. White-box giống như thợ máy: tháo tung động cơ ra kiểm tra từng con ốc, từng pít-tông.
- 💡 **Mẹo ghi nhớ (Mnemonics):**
  - Black-box (Chức năng): Vùng (Partition), Biên (Boundary), Nhờ kinh nghiệm (Guessing).
  - White-box (Cấu trúc code): Dòng lệnh (Statement), Nhánh (Branch), điều kiện (condition / 조건), vòng lặp (loop / 루프).

---
