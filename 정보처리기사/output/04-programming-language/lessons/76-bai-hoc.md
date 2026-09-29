# 292. 페이지 교체 알고리즘 (Thuật toán thay thế trang / Page Replacement)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **292. 페이지 교체 알고리즘 (Thuật toán thay thế trang / Page Replacement)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **292. 페이지 교체 알고리즘 (Thuật toán thay thế trang / Page Replacement)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **298. PCB (Process Control Block)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

페이지, 교체, 알고리즘

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **287. UNIX 시스템의 구성 (Cấu trúc hệ thống UNIX)**에서 만든 기준을 이어받아 **292. 페이지 교체 알고리즘 (Thuật toán thay thế trang / Page Replacement)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 292. 페이지 교체 알고리즘 (Thuật toán thay thế trang / Page Replacement)

Ở bước 76/77, **292. 페이지 교체 알고리즘 (Thuật toán thay thế trang / Page Replacement)** xuất hiện như phần tiếp nối của **287. UNIX 시스템의 구성 (Cấu trúc hệ thống UNIX)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **292. 페이지 교체 알고리즘 (Thuật toán thay thế trang / Page Replacement)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **개념 (Khái niệm)**, **핵심 키워드 (Từ khóa)**, **시험 포인트 (Điểm thi)**, **OPT (Optimal)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### TẦNG A – NOTE NÉN (ÔN / ĐI THI)

Bây giờ ta đi vào nội dung của **TẦNG A – NOTE NÉN (ÔN / ĐI THI)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- **개념 (Khái niệm)**: 주기억장치 빈 공간이 없을 때 어떤 페이지를 내보낼지 결정하는 기법. (Kỹ thuật chọn trang để loại bỏ khi bộ nhớ chính đã đầy để nhường chỗ cho trang mới.)
- **핵심 키워드 (Từ khóa)**: OPT, FIFO, LRU, LFU, NUR.
- **시험 포인트 (Điểm thi)**: 각 알고리즘별 교체 대상 선정 기준 묻는 문제. (Tiêu chí chọn trang của từng thuật toán.)

Các bullet của **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **TẦNG B – NOTE 보충 (HIỂU SÂU)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **TẦNG B – NOTE 보충 (HIỂU SÂU)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### TẦNG B – NOTE 보충 (HIỂU SÂU)

Phần nguồn của **TẦNG B – NOTE 보충 (HIỂU SÂU)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **OPT (Optimal)**: 앞으로 가장 오랫동안 안 쓸 페이지 교체 (이론적 최고). (Thay trang sẽ lâu nhất không được dùng trong tương lai - Tốt nhất nhưng chỉ trên lý thuyết.)
- **FIFO (First-In First-Out)**: 들어온 지 가장 오래된 페이지 교체. (Thay trang vào bộ nhớ sớm nhất.)
- **LRU (Least Recently Used)**: 최근에 가장 오랫동안 안 쓴 페이지 교체. (Thay trang lâu nhất chưa được sử dụng tính từ hiện tại.)
- **LFU (Least Frequently Used)**: 참조 횟수가 가장 적은 페이지 교체. (Thay trang có số lần sử dụng ít nhất.)
- **NUR (Not Used Recently)**: 참조 비트와 변형 비트를 사용해 최근 미사용 페이지 교체. (Dùng bit tham chiếu và bit sửa đổi để loại trang không dùng gần đây.)
- **예시 (Ví dụ)**: 스마트폰에서 앱을 여러 개 켜다가 램이 부족해지면, 제일 먼저 켰던 앱(FIFO)을 끄거나 최근에 가장 안 본 앱(LRU)을 종료시킴. (Khi điện thoại đầy RAM, nó sẽ tắt app mở đầu tiên (FIFO) hoặc app lâu rồi chưa đụng tới (LRU).)
- 💡 **Mẹo ghi nhớ**: **R**ecently = Lâu không đụng (Thời gian), **F**requently = Ít dùng (Số lần).

Với **TẦNG B – NOTE 보충 (HIỂU SÂU)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **TẦNG B – NOTE 보충 (HIỂU SÂU)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Như vậy, **292. 페이지 교체 알고리즘 (Thuật toán thay thế trang / Page Replacement)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **298. PCB (Process Control Block)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.