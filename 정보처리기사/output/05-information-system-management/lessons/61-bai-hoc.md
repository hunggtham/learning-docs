# 프로세스 동작 특성 (Process Behavior: Locality, Working Set, Thrashing)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **프로세스 동작 특성 (Process Behavior: Locality, Working Set, Thrashing)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **프로세스 동작 특성 (Process Behavior: Locality, Working Set, Thrashing)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **프로세스와 스레드 (Process and Thread)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

프로세스, 동작, 특성

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **페이지 교체 알고리즘과 페이지 크기 (Page Replacement & Size)**에서 만든 기준을 이어받아 **프로세스 동작 특성 (Process Behavior: Locality, Working Set, Thrashing)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **프로세스 동작 특성 (Process Behavior: Locality, Working Set, Thrashing)** và nối nó với **프로세스와 스레드 (Process and Thread)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 프로세스 동작 특성 (Process Behavior: Locality, Working Set, Thrashing)

Ở bước 61/86, **프로세스 동작 특성 (Process Behavior: Locality, Working Set, Thrashing)** xuất hiện như phần tiếp nối của **페이지 교체 알고리즘과 페이지 크기 (Page Replacement & Size)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **프로세스 동작 특성 (Process Behavior: Locality, Working Set, Thrashing)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **시간 구역성 (Temporal Locality)**, **공간 구역성 (Spatial Locality)**, **방지 방법** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **1. Locality (국부성, 구역성)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **1. Locality (국부성, 구역성)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 1. Locality (국부성, 구역성)

Bây giờ ta đi vào nội dung của **1. Locality (국부성, 구역성)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

프로세스 실행 중 일부 페이지만 집중적으로 참조하는 성질.
- **시간 구역성 (Temporal Locality)**: 하나의 페이지를 짧은 시간 동안 집중 참조 (반복문, 스택 등).
- **공간 구역성 (Spatial Locality)**: 특정 위치 주변의 페이지를 집중 참조 (배열, 순차적 코드 등).

Các bullet của **1. Locality (국부성, 구역성)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **1. Locality (국부성, 구역성)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. 워킹 셋 (Working Set)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **2. 워킹 셋 (Working Set)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 2. 워킹 셋 (Working Set)

Phần nguồn của **2. 워킹 셋 (Working Set)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

프로세스가 일정 시간 동안 자주 참조하는 페이지들의 집합. (시간에 따라 변함). 주기억장치에 상주시키면 페이지 부재 현상이 줄어듭니다.

Phần **2. 워킹 셋 (Working Set)** không có nhiều dữ liệu rời để tách nhỏ, vì vậy hãy giữ câu hỏi mục đích và tự chốt bằng một câu giải thích trước khi đi tiếp.

Sau khi đọc **2. 워킹 셋 (Working Set)**, đừng bắt đầu lại từ số không. **3. 스래싱 (Thrashing)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **3. 스래싱 (Thrashing)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 3. 스래싱 (Thrashing)

Các ý ngay dưới **3. 스래싱 (Thrashing)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

프로세스 처리 시간보다 페이지 교체에 소요되는 시간이 더 많아져 시스템 성능이 급격히 저하되는 현상.
- **방지 방법**: 다중 프로그래밍 정도 조절, 페이지 부재 빈도 조절, 워킹 셋 유지 등.

> **Vietnamese Explanation**:
> **Locality** là tính cục bộ (hay dùng lại chỗ vừa dùng). **Working Set** là tập hợp các trang bộ nhớ đang được dùng nhiều nhất, cần giữ lại ở RAM. **Thrashing** là hiện tượng "giậm chân tại chỗ", máy bận rộn tráo đổi dữ liệu với ổ cứng nhiều hơn là thực sự chạy chương trình, làm máy bị đơ.

Các bullet của **3. 스래싱 (Thrashing)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **3. 스래싱 (Thrashing)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Như vậy, **프로세스 동작 특성 (Process Behavior: Locality, Working Set, Thrashing)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **프로세스와 스레드 (Process and Thread)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.