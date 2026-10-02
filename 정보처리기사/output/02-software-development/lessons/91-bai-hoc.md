# 027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối algorithm design với paradigm, invariant và time complexity, để ý tưởng được đánh giá qua chi phí.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

알고리즘, 설계, 기법과, 시간, 복잡도

> **Chuyển mạch:** Ở chặng này của **027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **023 & 024: 자료구조 (Data Structures / Cấu trúc dữ liệu)**에서 만든 기준을 이어받아 **027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)**, **027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)

Ở bước 91/101, **027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)** xuất hiện như phần tiếp nối của **023 & 024: 자료구조 (Data Structures / Cấu trúc dữ liệu)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **알고리즘 설계 기법 (Kỹ thuật thiết kế thuật toán)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **알고리즘 설계 기법 (Kỹ thuật thiết kế thuật toán)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 알고리즘 설계 기법 (Kỹ thuật thiết kế thuật toán)

Bây giờ ta đi vào nội dung của **알고리즘 설계 기법 (Kỹ thuật thiết kế thuật toán)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “알고리즘 설계 기법 (Kỹ thuật thiết kế thuật toán)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **분할과 정복 (Divide & Conquer):** Chia để trị. Chia nhỏ vấn đề đến khi không chia được nữa rồi gộp lại. (VD: Merge Sort, Quick Sort).
- **동적계획법 (Dynamic Programming - Quy hoạch động):** Chia bài toán, nhưng CÓ lưu lại kết quả (bộ nhớ) để tận dụng cho lần sau. (VD: Fibonacci).
- **탐욕법 (Greedy):** Tham lam. Chọn cái tốt nhất ở *ngay thời điểm hiện tại*, không cần biết tương lai.
- **백트래킹 (Backtracking):** Quay lui. Đi thử, nếu thấy bế tắc (không triển vọng - promising) thì quay lại nút cha.

Các bullet của **알고리즘 설계 기법 (Kỹ thuật thiết kế thuật toán)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **알고리즘 설계 기법 (Kỹ thuật thiết kế thuật toán)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **시간 복잡도 (Time Complexity - Độ phức tạp thời gian)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **시간 복잡도 (Time Complexity - Độ phức tạp thời gian)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 시간 복잡도 (Time Complexity - Độ phức tạp thời gian)

Phần nguồn của **시간 복잡도 (Time Complexity - Độ phức tạp thời gian)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “시간 복잡도 (Time Complexity - Độ phức tạp thời gian)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- Đếm số lần thực thi các phép toán (không phải tính thời gian bằng giây).
- Ký hiệu tiệm cận: Big-O là cận trên, Omega là cận dưới, Theta là cận chặt; chúng không tự động đồng nghĩa với lần lượt 최악/평균/최상. Khi đề bài nói rõ worst/best case thì mới gắn với trường hợp đó.
- **Thứ tự (Nhanh -> Chậm):** O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ)
- O(1) nghĩa là: Dữ liệu lớn đến đâu thời gian vẫn không đổi.

- **Vietnamese Explanation:** Greedy giống như đi nhặt tiền: cứ thấy tờ to nhất trước mặt là nhặt, bất chấp sau đó dẫn vào ngõ cụt. Dynamic Programming giống như làm toán: kết quả bài 1 lưu ra nháp để dùng cho bài 2.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Divide = Cắt nhỏ. Dynamic = Nhớ bài cũ. Greedy = Tham bát bỏ mâm. Backtrack = Đi lùi. O(1) là nhanh nhất.

---

Với **시간 복잡도 (Time Complexity - Độ phức tạp thời gian)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **시간 복잡도 (Time Complexity - Độ phức tạp thời gian)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Như vậy, **027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

> **Bàn giao:** Sau **027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
