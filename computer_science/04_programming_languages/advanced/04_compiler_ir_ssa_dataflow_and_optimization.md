# Trình biên dịch (compiler / 컴파일러) IR, SSA, data-flow phân tích (analysis / 분석) và tối ưu hóa (optimization / 최적화)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Trình biên dịch (compiler / 컴파일러) IR, SSA, data-flow phân tích (analysis / 분석) và tối ưu hóa (optimization / 최적화)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Vì sao cần IR** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Control-flow đồ thị (graph / 그래프)** để giải thích cách điều kiện hoặc mục tiêu đó vận hành. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Trình biên dịch (compiler / 컴파일러) không tối ưu trực tiếp mã nguồn (source code / 소스 코드) như con người nhìn thấy và cũng không muốn phụ thuộc ngay vào machine instructions. Nó thường chuyển chương trình qua một hoặc nhiều **Intermediate Representations (IR / 중간 표현)** để biến ngữ nghĩa (semantics / 의미론) thành cấu trúc thuận lợi cho phân tích (analysis / 분석) và transformation.

## Vì sao cần IR

Nếu trình biên dịch (compiler / 컴파일러) hỗ trợ nhiều nguồn (source / 소스) languages và nhiều CPU targets, viết optimizer riêng cho từng cặp sẽ bùng nổ độ phức tạp (complexity / 복잡도). IR tạo điểm hội tụ: front-end hạ nguồn (source / 소스) ngữ nghĩa (semantics / 의미론) xuống IR; tối ưu hóa (optimization / 최적화) passes làm việc trên IR; backend hạ IR xuống mục tiêu (target / 대상) machine.

Một trình biên dịch (compiler / 컴파일러) có thể dùng high-level IR giữ kiểu (type / 타입)/điều khiển (control / 제어) cấu trúc (structure / 구조) rồi lower dần sang low-level IR gần machine hơn.

> **Chuyển mạch:** Trong **Trình biên dịch (compiler / 컴파일러) IR, SSA, data-flow phân tích (analysis / 분석) và tối ưu hóa (optimization / 최적화)**, **Vì sao cần IR** xác định đầu vào; **Control-flow đồ thị (graph / 그래프)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Static Single Assignment** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Control-flow đồ thị (graph / 그래프)

Hàm (function / 함수) được chia thành **basic blocks**: chuỗi instructions có một entry và điều khiển (control / 제어) chỉ rời ở cuối. Các edges giữa blocks tạo **Control-Flow đồ thị (graph / 그래프) (CFG)**.

CFG biến `if`, vòng lặp (loop / 루프), early return thành đồ thị (graph / 그래프) để trình biên dịch (compiler / 컴파일러) hỏi: khối (block / 블록) nào reachable, definition nào có thể tới điểm (point / 지점) này, expression nào bất biến (invariant / 불변식) trong vòng lặp (loop / 루프)?

> **Chuyển mạch:** Ở chặng này của **Trình biên dịch (compiler / 컴파일러) IR, SSA, data-flow phân tích (analysis / 분석) và tối ưu hóa (optimization / 최적화)**, **Control-flow đồ thị (graph / 그래프)** xác định đầu vào; **Static Single Assignment** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Data-flow phân tích (analysis / 분석)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Static Single Assignment

Trong **SSA**, mỗi variable phiên bản (version / 버전) chỉ được assign một lần. nguồn (source / 소스):

```text
x = 1
x = x + 2
```

có thể thành `x1 = 1`, `x2 = x1 + 2`. Khi control-flow merge, **phi hàm (function / 함수)** biểu diễn giá trị (value / 값) đến từ predecessor nào.

SSA làm def-use chuỗi (chain / 사슬) rõ ràng. Nếu mỗi giá trị (value / 값) có một definition, constant propagation, dead-code elimination và phụ thuộc (dependency / 의존성) phân tích (analysis / 분석) đơn giản hơn đáng kể.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trình biên dịch (compiler / 컴파일러) IR, SSA, data-flow phân tích (analysis / 분석) và tối ưu hóa (optimization / 최적화)**, **Static Single Assignment** xác định đầu vào; **Data-flow phân tích (analysis / 분석)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Tối ưu hóa (optimization / 최적화) phải preserve ngữ nghĩa (semantics / 의미론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Data-flow phân tích (analysis / 분석)

Nhiều tối ưu hóa (optimization / 최적화) là fixed-point phân tích (analysis / 분석) trên CFG. Ví dụ liveness hỏi giá trị (value / 값) nào còn có thể được dùng trong tương lai; reaching definitions hỏi definitions nào có thể tới program điểm (point / 지점).

Trình biên dịch (compiler / 컴파일러) truyền abstract facts qua đồ thị (graph / 그래프) tới khi không còn thay đổi. Đây là liên kết (connection / 연결) trực tiếp với lattice/fixed-point lập luận (reasoning / 추론) trong static phân tích (analysis / 분석).

> **Chuyển mạch:** Trong **Trình biên dịch (compiler / 컴파일러) IR, SSA, data-flow phân tích (analysis / 분석) và tối ưu hóa (optimization / 최적화)**, **Data-flow phân tích (analysis / 분석)** xác định đầu vào; **Tối ưu hóa (optimization / 최적화) phải preserve ngữ nghĩa (semantics / 의미론)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Alias phân tích (analysis / 분석)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tối ưu hóa (optimization / 최적화) phải preserve ngữ nghĩa (semantics / 의미론)

Constant folding thay `2 * 3` bằng `6`; dùng chung (common / 공통) subexpression elimination reuse computation; loop-invariant mã (code / 코드) motion đưa expression không đổi ra ngoài vòng lặp (loop / 루프). Nhưng transformation chỉ hợp lệ dưới ngôn ngữ (language / 언어) ngữ nghĩa (semantics / 의미론).

Floating-point reassociation, overflow, exceptions, volatile bộ nhớ (memory / 메모리) và tính đồng thời (concurrency / 동시성) có thể ngăn tối ưu hóa (optimization / 최적화) tưởng như hiển nhiên. “Nhanh hơn” không đủ; trình biên dịch (compiler / 컴파일러) phải chứng minh transformation không thay observable hành vi (behavior / 동작) theo đặc tả hợp đồng (contract / 계약).

> **Chuyển mạch:** Ở chặng này của **Trình biên dịch (compiler / 컴파일러) IR, SSA, data-flow phân tích (analysis / 분석) và tối ưu hóa (optimization / 최적화)**, **Alias phân tích (analysis / 분석)** tiếp nhận điểm tựa từ **Tối ưu hóa (optimization / 최적화) phải preserve ngữ nghĩa (semantics / 의미론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lowering và backend** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Alias phân tích (analysis / 분석)

Nếu trình biên dịch (compiler / 컴파일러) không biết hai pointers có trỏ cùng bộ nhớ (memory / 메모리) hay không, nó phải bảo thủ. Alias phân tích (analysis / 분석) tốt mở đường cho reorder/vectorization nhưng phân tích (analysis / 분석) chính xác tuyệt đối cho general program là khó hoặc bất khả thi trong nhiều setting.

Đây là nơi computability limits gặp môi trường vận hành (production / 운영 환경) trình biên dịch (compiler / 컴파일러): optimizer dùng approximation có kiểm soát.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trình biên dịch (compiler / 컴파일러) IR, SSA, data-flow phân tích (analysis / 분석) và tối ưu hóa (optimization / 최적화)**, **Lowering và backend** tiếp nhận điểm tựa từ **Alias phân tích (analysis / 분석)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Debugging optimized mã (code / 코드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lowering và backend

Sau high-level tối ưu hóa (optimization / 최적화), IR được lower thành operations gần ISA. Backend làm instruction selection, register allocation và scheduling. vật lý (physical / 물리적) register hữu hạn khiến SSA virtual values phải được map, đôi khi spill ra ngăn xếp (stack / 스택).

> **Chuyển mạch:** Trong **Trình biên dịch (compiler / 컴파일러) IR, SSA, data-flow phân tích (analysis / 분석) và tối ưu hóa (optimization / 최적화)**, **Debugging optimized mã (code / 코드)** tiếp nhận điểm tựa từ **Lowering và backend** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Debugging optimized mã (code / 코드)

Tối ưu hóa (optimization / 최적화) phá ánh xạ (mapping / 매핑) 1:1 giữa dòng mã nguồn (source line / 소스 코드 줄) và machine thực thi (execution / 실행). Variable có thể bị optimized away, mã (code / 코드) được inline hoặc reorder. Vì vậy debugging bản phát hành (release / 릴리스) bản dựng (build / 빌드) khó hơn gỡ lỗi (debug / 디버그) bản dựng (build / 빌드) không chỉ vì thiếu symbols mà vì program biểu diễn (representation / 표현) đã thay đổi.

> **Chuyển mạch:** Ở chặng này của **Trình biên dịch (compiler / 컴파일러) IR, SSA, data-flow phân tích (analysis / 분석) và tối ưu hóa (optimization / 최적화)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Debugging optimized mã (code / 코드)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> IR là ngôn ngữ lập luận (reasoning / 추론) nội bộ của trình biên dịch (compiler / 컴파일러). SSA biến mutation thành tường minh (explicit / 명시적) giá trị (value / 값) versions; CFG biến điều khiển (control / 제어) thành đồ thị (graph / 그래프); data-flow phân tích (analysis / 분석) truyền facts trên đồ thị (graph / 그래프). tối ưu hóa (optimization / 최적화) là semantics-preserving đồ thị (graph / 그래프) transformation, không phải collection mẹo làm mã (code / 코드) nhanh.

> **Bàn giao:** Sau **Mô hình tư duy (mental model / 사고 모델)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
