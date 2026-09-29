# 가상기억장치 및 페이지 교체 (Virtual Memory & Page Replacement)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **가상기억장치 및 페이지 교체 (Virtual Memory & Page Replacement)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **가상기억장치 및 페이지 교체 (Virtual Memory & Page Replacement)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **소프트웨어 공학 (Software Engineering)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

가상기억장치, 페이지, 교체

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **프로그래밍 언어 종류 및 특징 (Programming Languages Types & Features)**에서 만든 기준을 이어받아 **가상기억장치 및 페이지 교체 (Virtual Memory & Page Replacement)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **가상기억장치 및 페이지 교체 (Virtual Memory & Page Replacement)** và nối nó với **소프트웨어 공학 (Software Engineering)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 가상기억장치 및 페이지 교체 (Virtual Memory & Page Replacement)

Ở bước 55/78, **가상기억장치 및 페이지 교체 (Virtual Memory & Page Replacement)** xuất hiện như phần tiếp nối của **프로그래밍 언어 종류 및 특징 (Programming Languages Types & Features)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **가상기억장치 및 페이지 교체 (Virtual Memory & Page Replacement)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **OPT (Optimal)**, **FIFO (First In First Out)**, **LRU (Least Recently Used)**, **LFU (Least Frequently Used)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **290. 페이징 기법 (Paging / Phân trang)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **290. 페이징 기법 (Paging / Phân trang)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 290. 페이징 기법 (Paging / Phân trang)

Bây giờ ta đi vào nội dung của **290. 페이징 기법 (Paging / Phân trang)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 프로그램을 **동일한 크기**로 나눔 (Chia chương trình thành các phần có kích thước BẰNG NHAU).
- 프로그램 단위 = 페이지 (Page), 기억장치 단위 = 페이지 프레임 (Page Frame).
- **내부 단편화 (Internal Fragmentation)** 발생 가능. (Có thể xảy ra phân mảnh trong).

Với **290. 페이징 기법 (Paging / Phân trang)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **290. 페이징 기법 (Paging / Phân trang)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **291. 세그먼테이션 기법 (Segmentation / Phân đoạn)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **291. 세그먼테이션 기법 (Segmentation / Phân đoạn)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 291. 세그먼테이션 기법 (Segmentation / Phân đoạn)

Phần nguồn của **291. 세그먼테이션 기법 (Segmentation / Phân đoạn)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- 프로그램을 배열이나 함수 같은 **다양한 크기의 논리적인 단위**로 나눔. (Chia theo khối logic kích thước KHÁC NHAU).
- **외부 단편화 (External Fragmentation)** 발생 가능. (Có thể xảy ra phân mảnh ngoài).
  - 💡 *Mẹo ghi nhớ*: Page = Kích thước cố định (Sinh ra rác bên trong). Segment = Kích thước logic (Sinh ra rác bên ngoài).

Với **291. 세그먼테이션 기법 (Segmentation / Phân đoạn)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Sau khi đọc **291. 세그먼테이션 기법 (Segmentation / Phân đoạn)**, đừng bắt đầu lại từ số không. **292. 페이지 교체 알고리즘 (Page Replacement Algorithms / Thuật toán thay thế trang)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **292. 페이지 교체 알고리즘 (Page Replacement Algorithms / Thuật toán thay thế trang)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 292. 페이지 교체 알고리즘 (Page Replacement Algorithms / Thuật toán thay thế trang)

Các ý ngay dưới **292. 페이지 교체 알고리즘 (Page Replacement Algorithms / Thuật toán thay thế trang)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- **OPT (Optimal)**: 앞으로 가장 오랫동안 사용하지 않을 페이지 교체. (Thay thế trang sẽ lâu được dùng nhất trong tương lai - Tốt nhất nhưng khó thực hiện).
- **FIFO (First In First Out)**: 가장 먼저 들어온 페이지 교체. (Vào trước ra trước).
- **LRU (Least Recently Used)**: 최근에 가장 오랫동안 사용하지 않은 페이지 교체. (Thay thế trang lâu nhất chưa được truy cập).
- **LFU (Least Frequently Used)**: 사용 빈도가 가장 적은 페이지 교체. (Thay thế trang có số lần truy cập ít nhất).
- **NUR (Not Used Recently)**: 참조 비트(R)와 변형/수정 비트(M)를 조합해 페이지를 네 등급으로 나누고 낮은 등급부터 교체한다. (Dùng hai bit R/M để phân loại bốn mức.)

Các bullet của **292. 페이지 교체 알고리즘 (Page Replacement Algorithms / Thuật toán thay thế trang)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**292. 페이지 교체 알고리즘 (Page Replacement Algorithms / Thuật toán thay thế trang)** vừa cho ta cách đặt câu hỏi. Bây giờ **293. 페이지 크기 (Page Size / Kích thước trang)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Ở đoạn **293. 페이지 크기 (Page Size / Kích thước trang)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 293. 페이지 크기 (Page Size / Kích thước trang)

Bây giờ ta đi vào nội dung của **293. 페이지 크기 (Page Size / Kích thước trang)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- **작을 경우 (Kích thước nhỏ)**: 단편화 감소, 매핑 늦어짐, 디스크 접근 많아짐. (Phân mảnh ít, nhưng bảng ánh xạ lớn, truy cập ổ đĩa nhiều hơn).
- **클 경우 (Kích thước lớn)**: 단편화 증가, 매핑 빨라짐, 불필요한 내용까지 적재될 수 있음. (Phân mảnh nhiều, ánh xạ nhanh, có thể load cả những phần thừa).

Các bullet của **293. 페이지 크기 (Page Size / Kích thước trang)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **293. 페이지 크기 (Page Size / Kích thước trang)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **294. Locality (국부성 / Tính địa phương)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **294. Locality (국부성 / Tính địa phương)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 294. Locality (국부성 / Tính địa phương)

Phần nguồn của **294. Locality (국부성 / Tính địa phương)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- 프로세스가 실행되는 동안 주기억장치의 일부 페이지만 집중적으로 참조하는 성질. (Tiến trình có xu hướng chỉ tập trung truy cập một số trang cụ thể).
- **시간 구역성 (Temporal Locality)**: Loop, 스택, 변수 (Vòng lặp, stack, biến - Truy cập cùng 1 chỗ nhiều lần).
- **공간 구역성 (Spatial Locality)**: 배열 순회, 순차적 코드 (Mảng, mã tuần tự - Truy cập các ô nhớ cạnh nhau).

Các bullet của **294. Locality (국부성 / Tính địa phương)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **294. Locality (국부성 / Tính địa phương)**, đừng bắt đầu lại từ số không. **295. 워킹 셋 (Working Set / Tập làm việc)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **295. 워킹 셋 (Working Set / Tập làm việc)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 295. 워킹 셋 (Working Set / Tập làm việc)

Các ý ngay dưới **295. 워킹 셋 (Working Set / Tập làm việc)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- 프로세스가 자주 참조하는 페이지들의 집합. (Tập hợp các trang được truy cập thường xuyên nhất).
- 주기억장치에 상주시킴으로써 페이지 부재(Page Fault)를 줄인다. (Giữ trong RAM để giảm thiểu lỗi trang).

Các bullet của **295. 워킹 셋 (Working Set / Tập làm việc)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**295. 워킹 셋 (Working Set / Tập làm việc)** vừa cho ta cách đặt câu hỏi. Bây giờ **296. 스래싱 (Thrashing / Hiện tượng tráo đổi quá mức)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Ở đoạn **296. 스래싱 (Thrashing / Hiện tượng tráo đổi quá mức)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 296. 스래싱 (Thrashing / Hiện tượng tráo đổi quá mức)

Bây giờ ta đi vào nội dung của **296. 스래싱 (Thrashing / Hiện tượng tráo đổi quá mức)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 페이지 교체 시간이 처리 시간보다 많아지는 현상. (Mất thời gian hoán đổi trang nhiều hơn thời gian xử lý thực tế).
- 방지: 다중 프로그래밍 정도 조절, 워킹 셋 유지. (Kiểm soát đa nhiệm, dùng Working Set).

Các bullet của **296. 스래싱 (Thrashing / Hiện tượng tráo đổi quá mức)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Với **296. 스래싱 (Thrashing / Hiện tượng tráo đổi quá mức)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Như vậy, **가상기억장치 및 페이지 교체 (Virtual Memory & Page Replacement)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **소프트웨어 공학 (Software Engineering)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.