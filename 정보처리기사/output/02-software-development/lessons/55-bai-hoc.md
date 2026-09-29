# 핵심 042: 블랙박스 테스트 / 화이트박스 테스트 (Black-Box vs White-Box)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **핵심 042: 블랙박스 테스트 / 화이트박스 테스트 (Black-Box vs White-Box)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **핵심 042: 블랙박스 테스트 / 화이트박스 테스트 (Black-Box vs White-Box)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **핵심 043: 단위 / 통합 / 시스템 / 인수 테스트 (Test Levels)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

핵심, 블랙박스, 테스트, 화이트박스

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **핵심 041: 테스트 케이스 / 시나리오 / 오라클 (Test Case/Scenario/Oracle)**에서 만든 기준을 이어받아 **핵심 042: 블랙박스 테스트 / 화이트박스 테스트 (Black-Box vs White-Box)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **핵심 042: 블랙박스 테스트 / 화이트박스 테스트 (Black-Box vs White-Box)** và nối nó với **핵심 043: 단위 / 통합 / 시스템 / 인수 테스트 (Test Levels)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 핵심 042: 블랙박스 테스트 / 화이트박스 테스트 (Black-Box vs White-Box)

Ở bước 55/95, **핵심 042: 블랙박스 테스트 / 화이트박스 테스트 (Black-Box vs White-Box)** xuất hiện như phần tiếp nối của **핵심 041: 테스트 케이스 / 시나리오 / 오라클 (Test Case/Scenario/Oracle)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **핵심 042: 블랙박스 테스트 / 화이트박스 테스트 (Black-Box vs White-Box)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Cả hai đều là **Dynamic Test** (Phải chạy code).

Trước hết, ta đặt **블랙박스 테스트 (Black-box / Hộp đen / Dựa trên Chức năng)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **블랙박스 테스트 (Black-box / Hộp đen / Dựa trên Chức năng)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 블랙박스 테스트 (Black-box / Hộp đen / Dựa trên Chức năng)

Bây giờ ta đi vào nội dung của **블랙박스 테스트 (Black-box / Hộp đen / Dựa trên Chức năng)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- Không quan tâm bên trong code viết gì, chỉ quan tâm Đầu vào -> Đầu ra. (Dựa trên 명세 - Đặc tả).
- **Kỹ thuật (Các loại):**
  - **동등 분할 (Equivalence Partitioning):** Chia vùng tương đương (Vd: Nhập từ 1-100, thì test số 50 là đủ diện cho vùng đúng).
  - **경곗값 분석 (Boundary Value):** Phân tích giá trị biên (Lỗi hay xảy ra ở ranh giới, vd test số 0, 1, 100, 101).
  - **원인-효과 그래프 (Cause-Effect Graph):** Bảng đồ nhân quả.
  - **오류 예측 (Error Guessing):** Dựa vào kinh nghiệm của tester để đoán lỗi.

Các bullet của **블랙박스 테스트 (Black-box / Hộp đen / Dựa trên Chức năng)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **블랙박스 테스트 (Black-box / Hộp đen / Dựa trên Chức năng)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **화이트박스 테스트 (White-box / Hộp trắng / Dựa trên Cấu trúc Code)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **화이트박스 테스트 (White-box / Hộp trắng / Dựa trên Cấu trúc Code)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 화이트박스 테스트 (White-box / Hộp trắng / Dựa trên Cấu trúc Code)

Phần nguồn của **화이트박스 테스트 (White-box / Hộp trắng / Dựa trên Cấu trúc Code)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- Soi thấu bên trong code. Đảm bảo mọi dòng lệnh (Statement), mọi nhánh (Branch/Decision) đều được chạy ít nhất 1 lần.
- **Kỹ thuật (Các loại):**
  - **기본 경로 검사 (Base Path):** Đi qua tất cả các con đường code.
  - **구문 커버리지 (Statement Coverage):** Bao phủ dòng lệnh (Dễ nhất).
  - **결정 커버리지 (Decision/Branch):** Bao phủ nhánh (If True / If False).
  - **조건 커버리지 (Condition):** Bao phủ mọi điều kiện con trong If.
  - **루프 검사 (Loop Testing):** Test các vòng lặp for, while.

- **Vietnamese Explanation:** Black-box giống như lái xe ô tô: đạp ga là chạy, không cần biết động cơ nổ ra sao. White-box giống như thợ máy: tháo tung động cơ ra kiểm tra từng con ốc, từng pít-tông.
- 💡 **Mẹo ghi nhớ (Mnemonics):**
  - Black-box (Chức năng): Vùng (Partition), Biên (Boundary), Nhờ kinh nghiệm (Guessing).
  - White-box (Cấu trúc code): Dòng lệnh (Statement), Nhánh (Branch), Điều kiện (Condition), Vòng lặp (Loop).

---

Các bullet của **화이트박스 테스트 (White-box / Hộp trắng / Dựa trên Cấu trúc Code)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **화이트박스 테스트 (White-box / Hộp trắng / Dựa trên Cấu trúc Code)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Như vậy, **핵심 042: 블랙박스 테스트 / 화이트박스 테스트 (Black-Box vs White-Box)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **핵심 043: 단위 / 통합 / 시스템 / 인수 테스트 (Test Levels)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.