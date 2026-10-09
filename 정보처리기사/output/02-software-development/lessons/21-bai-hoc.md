# 084: 퀵 정렬 (Quick Sort)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **084: 퀵 정렬 (Quick Sort)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối quick sort với partition, pivot và recursion, để tốc độ phụ thuộc cách chia và phân bố đầu vào.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **084: 퀵 정렬 (Quick Sort)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **084: 퀵 정렬 (Quick Sort)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **085: 힙 정렬 (Heap Sort)** khi chuyển sang phần tiếp theo.

Mục tiêu xác định quick sort dựa vào pivot và partition ra sao; từ khóa khoanh vùng recursion và độ lệch của cách chia.

## 핵심 키워드 (Từ khóa)

정렬

Kiến thức liên kết đặt quick sort trên nền partition và recursion; cách đọc tiếp theo giúp đối chiếu pivot với phân bố dữ liệu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **083: 버블 정렬 (Bubble Sort)**에서 만든 기준을 이어받아 **084: 퀵 정렬 (Quick Sort)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

Cách đọc đã đặt khung đối tượng–điều kiện–hệ quả; phần quick sort dùng khung đó để nối partition với chi phí đệ quy.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

Phần này khép lại bằng ảnh hưởng của pivot đến độ sâu đệ quy; khi sang heap sort, hãy đối chiếu partition với cấu trúc heap.

## 084: 퀵 정렬 (Quick Sort)

Từ **083: 버블 정렬 (Bubble Sort)**, ta đã có điểm tựa để bước vào **084: 퀵 정렬 (Quick Sort)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 21/101 trước khi đi vào chi tiết.

Để đọc **084: 퀵 정렬 (Quick Sort)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “084: 퀵 정렬 (Quick Sort)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **분할과 정복 (Divide and Conquer):** 파일 나누어 정렬.
- **피벗 (Pivot):** 기준값. Nhỏ hơn Pivot sang trái, lớn hơn Pivot sang phải.
- **스택 (Stack) 필요:** 재귀 (Recursion) 호출을 위해. (Dùng đệ quy nên cần Stack nhớ vị trí).
- **가장 빠른 방식:** Trung bình nhanh nhất.
- **시간 복잡도:** 평균 **O(n log n)**, 최악 **O(n²)** (Khi mảng đã sắp xếp sẵn mà chọn Pivot ngu).

- 💡 **Mẹo ghi nhớ (Mnemonics):** Quick = Pivot, Đệ quy, Stack. Tốt: n log n. Xấu: n².

---

Điểm chốt của **084: 퀵 정렬 (Quick Sort)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **085: 힙 정렬 (Heap Sort)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

> **Bàn giao:** Sau **084: 퀵 정렬 (Quick Sort)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
