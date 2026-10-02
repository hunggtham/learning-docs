# 083: 버블 정렬 (Bubble Sort)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **083: 버블 정렬 (Bubble Sort)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối bubble sort với adjacent swap, invariant và early exit, để hiểu vì sao thuật toán phù hợp hoặc không phù hợp.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **083: 버블 정렬 (Bubble Sort)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **083: 버블 정렬 (Bubble Sort)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **084: 퀵 정렬 (Quick Sort)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **083: 버블 정렬 (Bubble Sort)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

버블, 정렬

> **Chuyển mạch:** Ở chặng này của **083: 버블 정렬 (Bubble Sort)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **082: 선택 정렬 (Selection Sort)**에서 만든 기준을 이어받아 **083: 버블 정렬 (Bubble Sort)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **083: 버블 정렬 (Bubble Sort)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **083: 버블 정렬 (Bubble Sort)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **083: 버블 정렬 (Bubble Sort)**, **083: 버블 정렬 (Bubble Sort)** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 083: 버블 정렬 (Bubble Sort)

Sau khi đã đặt nền bằng **082: 선택 정렬 (Selection Sort)**, ta chuyển sang **083: 버블 정렬 (Bubble Sort)**. Đây là mắt xích 20/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **083: 버블 정렬 (Bubble Sort)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “083: 버블 정렬 (Bubble Sort)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **인접한 두 개의 레코드** 키 값을 비교하여 크기에 따라 위치 교환(Swap). (So sánh 2 phần tử cạnh nhau, số to đẩy lùi về sau. Số to nhất sẽ "nổi bọt" chìm xuống cuối mảng sau vòng đầu tiên).
- **종료 조건:** 더 이상 교환이 일어나지 않으면 정렬 끝. 플래그 비트(Flag Bit) 사용. (Dùng cờ Flag, nếu chạy hết 1 vòng mà không có ai đổi chỗ nghĩa là đã sắp xếp xong).
- **시간 복잡도:** O(n²).

- 💡 **Mẹo ghi nhớ (Mnemonics):** Bubble (Nổi bọt) = Từ khóa **Hai phần tử kề nhau** (Hai cái kề nhau), **플래그 비트** (Flag bit).

---

Ta có thể khép mục **083: 버블 정렬 (Bubble Sort)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **084: 퀵 정렬 (Quick Sort)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

> **Bàn giao:** Sau **083: 버블 정렬 (Bubble Sort)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
