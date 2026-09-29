# 페이지 교체 알고리즘과 페이지 크기 (Page Replacement & Size)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **페이지 교체 알고리즘과 페이지 크기 (Page Replacement & Size)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **페이지 교체 알고리즘과 페이지 크기 (Page Replacement & Size)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **프로세스 동작 특성 (Process Behavior: Locality, Working Set, Thrashing)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

페이지, 교체, 알고리즘과, 크기

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **메모리 관리 (Memory Management)**에서 만든 기준을 이어받아 **페이지 교체 알고리즘과 페이지 크기 (Page Replacement & Size)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **페이지 교체 알고리즘과 페이지 크기 (Page Replacement & Size)** và nối nó với **프로세스 동작 특성 (Process Behavior: Locality, Working Set, Thrashing)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 페이지 교체 알고리즘과 페이지 크기 (Page Replacement & Size)

Từ **메모리 관리 (Memory Management)**, ta đã có điểm tựa để bước vào **페이지 교체 알고리즘과 페이지 크기 (Page Replacement & Size)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 60/86 trước khi đi vào chi tiết.

Để đọc **페이지 교체 알고리즘과 페이지 크기 (Page Replacement & Size)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **OPT (Optimal)**, **FIFO (First In First Out)**, **LRU (Least Recently Used)**, **LFU (Least Frequently Used)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **1. 페이지 교체 알고리즘 (Page Replacement Algorithms)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 1. 페이지 교체 알고리즘 (Page Replacement Algorithms)

Các ý ngay dưới **1. 페이지 교체 알고리즘 (Page Replacement Algorithms)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

페이지 부재(Page Fault) 발생 시, 어떤 페이지 프레임을 교체할 것인지 결정합니다.
- **OPT (Optimal)**: 앞으로 가장 오랫동안 사용하지 않을 페이지 교체 (가장 효율적이나 미래 예측이 필요해 비현실적).
- **FIFO (First In First Out)**: 가장 먼저 들어와서 가장 오래 있었던 페이지 교체.
- **LRU (Least Recently Used)**: 최근에 가장 오랫동안 사용하지 않은 페이지 교체 (계수기나 스택 사용).
- **LFU (Least Frequently Used)**: 사용 빈도(횟수)가 가장 적은 페이지 교체.
- **NUR (Not Used Recently)**: LRU의 오버헤드를 줄이기 위해 참조 비트와 변형 비트를 사용하여 최근 사용 안 된 페이지 교체.
- **SCR (Second Chance Replacement)**: FIFO의 단점을 보완하여 자주 사용되는 페이지는 한 번 더 기회를 줌.

Các bullet của **1. 페이지 교체 알고리즘 (Page Replacement Algorithms)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **1. 페이지 교체 알고리즘 (Page Replacement Algorithms)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. 페이지 크기 (Page Size)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **2. 페이지 크기 (Page Size)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 2. 페이지 크기 (Page Size)

Bây giờ ta đi vào nội dung của **2. 페이지 크기 (Page Size)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “2. 페이지 크기 (Page Size)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **크기가 작을 경우**: 페이지 단편화 감소, 워킹 셋 효율 증가, Locality 일치로 기억장치 효율 상승. 단, 페이지 맵 테이블 크기가 커지고 매핑 속도가 느려지며 디스크 입출력 횟수가 증가.
- **크기가 클 경우**: 페이지 맵 테이블 크기 감소, 매핑 속도 상승, 디스크 입출력 횟수 감소. 단, 불필요한 내용까지 적재될 수 있고 페이지 단편화가 증가.

Các bullet của **2. 페이지 크기 (Page Size)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **2. 페이지 크기 (Page Size)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **페이지 교체 알고리즘과 페이지 크기 (Page Replacement & Size)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **프로세스 동작 특성 (Process Behavior: Locality, Working Set, Thrashing)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.