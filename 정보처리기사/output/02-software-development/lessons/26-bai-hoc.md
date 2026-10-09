# 029 & 030: 검색 알고리즘 및 해싱 (Search Algorithms & Hashing)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **029 & 030: 검색 알고리즘 및 해싱 (Search Algorithms & Hashing)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối search algorithms với ordering, hashing và collision, để truy vấn được chọn theo dữ liệu và chi phí.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **029 & 030: 검색 알고리즘 및 해싱 (Search Algorithms & Hashing)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **029 & 030: 검색 알고리즘 및 해싱 (Search Algorithms & Hashing)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **087: 이분 검색 (Binary Search - Tìm kiếm nhị phân)** khi chuyển sang phần tiếp theo.

Mục tiêu phân biệt tìm kiếm tuần tự, nhị phân và hashing theo điều kiện dữ liệu; từ khóa khoanh vùng phép so sánh và ánh xạ khóa.

## 핵심 키워드 (Từ khóa)

검색, 알고리즘, 해싱

Kiến thức liên kết đặt nhóm search/hash trên nền binary search và mô hình khóa–giá trị; cách đọc tiếp theo giúp chọn cơ chế theo dữ liệu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **7. 이분 검색 (Binary Search)**에서 만든 기준을 이어받아 **029 & 030: 검색 알고리즘 및 해싱 (Search Algorithms & Hashing)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

Cách đọc đã đặt khung đối tượng–điều kiện–hệ quả; phần search/hash dùng khung đó để nối cấu trúc dữ liệu với chi phí truy cập.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

Phần này khép lại bằng trade-off giữa so sánh tuần tự, thứ tự và collision; khi sang binary search chuyên biệt, hãy giữ lại điều kiện đầu vào.

## 029 & 030: 검색 알고리즘 및 해싱 (Search Algorithms & Hashing)

Sau khi đã đặt nền bằng **7. 이분 검색 (Binary Search)**, ta chuyển sang **029 & 030: 검색 알고리즘 및 해싱 (Search Algorithms & Hashing)**. Đây là mắt xích 26/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **029 & 030: 검색 알고리즘 및 해싱 (Search Algorithms & Hashing)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng cho ta tiêu chí đối chiếu, còn công thức cho ta quan hệ giữa các đại lượng; hãy dùng cả hai để kiểm tra cùng một kết luận.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **검색 (Search - Tìm kiếm)**. Hãy xác định **검색 (Search - Tìm kiếm)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 검색 (Search - Tìm kiếm)

Phần nguồn của **검색 (Search - Tìm kiếm)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “검색 (Search - Tìm kiếm)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **순차 검색 (Sequential/Linear Search):** Tìm tuần tự từ đầu đến cuối. Dùng cho mảng *chưa sắp xếp*. O(n).
- **이진 검색 (Binary Search):** Tìm nhị phân. Chia đôi mảng liên tục. **Bắt buộc mảng phải ĐÃ SẮP XẾP.** O(log n). Rất nhanh.

Các bullet của **검색 (Search - Tìm kiếm)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **검색 (Search - Tìm kiếm)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **해싱 (Hashing - Băm dữ liệu)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **해싱 (Hashing - Băm dữ liệu)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 해싱 (Hashing - Băm dữ liệu)

Các ý ngay dưới **해싱 (Hashing - Băm dữ liệu)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “해싱 (Hashing - Băm dữ liệu)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- Dùng hàm băm (Hash Function) tính ra trực tiếp địa chỉ bộ nhớ để lưu hoặc tìm kiếm dữ liệu. Nhanh nhất (O(1)).

- **Vietnamese Explanation:** Tìm tuần tự là lật từng trang sách. Tìm nhị phân là mở giữa cuốn từ điển, xem vần nào rồi gập nửa bỏ đi, tìm tiếp ở nửa kia. Băm (Hashing) là nhìn Mục lục rồi lật thẳng trang đó.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Binary Search = Phải Sắp Xếp (Sắp xếp), Chia đôi (절반). Hashing = O(1) Siêu Tốc.

Với **해싱 (Hashing - Băm dữ liệu)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Sau khi đọc **해싱 (Hashing - Băm dữ liệu)**, đừng bắt đầu lại từ số không. **해시 충돌 해결 방법 (Hash Collision Resolution / Các phương pháp giải quyết đụng độ Hash)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **해시 충돌 해결 방법 (Hash Collision Resolution / Các phương pháp giải quyết đụng độ Hash)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 해시 충돌 해결 방법 (Hash Collision Resolution / Các phương pháp giải quyết đụng độ Hash)

Bây giờ ta đi vào nội dung của **해시 충돌 해결 방법 (Hash Collision Resolution / Các phương pháp giải quyết đụng độ Hash)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “해시 충돌 해결 방법 (Hash Collision Resolution / Các phương pháp giải quyết đụng độ Hash)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

| 방법 (Phương pháp) | 설명 (Giải thích) |
|---|---|
| **체이닝 (Chaining - Móc xích)** | 버킷 내에 연결리스트(Linked List)를 할당하여 데이터들을 연결하는 방식. (Dùng danh sách liên kết để nối các phần tử bị đụng độ lại với nhau trong cùng 1 bucket.) |
| **개방 주소법 (Open Addressing - Địa chỉ mở)** | 충돌이 일어났을 때 다른 버킷에 데이터를 삽입해 해결하는 방식. (Khi đụng độ, tìm một ô trống khác để nhét vào. Địa chỉ dữ liệu bị thay đổi so với ban đầu.) |
| 선형 탐색 (Linear Probing) | 해시충돌 시 다음 버킷, 혹은 몇 개를 건너뛰어 삽입. (Thử tuyến tính: Tìm ô trống kế tiếp.) |
| 제곱 탐색 (Quadratic Probing) | 해시충돌 시 제곱만큼 건너뛴 버킷에 삽입 (1, 4, 9, 16...). (Thử bậc hai: Nhảy xa dần theo bình phương để tránh tụ tập.) |
| 이중 해시 (Double Hashing) | 해시충돌 시 다른 해싱함수를 한 번 더 적용. (Băm kép: Dùng thêm một hàm băm phụ để tìm khoảng nhảy.) |

- **Vietnamese Explanation:** Khi hai dữ liệu băm ra cùng một địa chỉ (Collision), ta phải giải quyết. Chaining là cho chúng ở chung một nhà nhưng nối đuôi nhau (như xâu chuỗi). Open Addressing là "nhà này có người rồi, mời anh đi tìm nhà khác".
- 💡 **Mẹo ghi nhớ (Mnemonics):** Chaining = Dây xích (Linked List). Open Addressing = Mở cửa đi tìm nhà khác (Linear, Quadratic, Double).

---

Khi đọc **해시 충돌 해결 방법 (Hash Collision Resolution / Các phương pháp giải quyết đụng độ Hash)**, hãy tách hai lớp: bảng giúp đối chiếu các loại hoặc tiêu chí, còn công thức cần được đọc theo biến, đơn vị và quan hệ giữa các đại lượng. Cách tách này giúp ta hiểu cơ chế trước khi ghi nhớ ký hiệu.

Như vậy, **해시 충돌 해결 방법 (Hash Collision Resolution / Các phương pháp giải quyết đụng độ Hash)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Ta có thể khép mục **029 & 030: 검색 알고리즘 및 해싱 (Search Algorithms & Hashing)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **087: 이분 검색 (Binary Search - Tìm kiếm nhị phân)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

> **Bàn giao:** Sau **029 & 030: 검색 알고리즘 및 해싱 (Search Algorithms & Hashing)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
