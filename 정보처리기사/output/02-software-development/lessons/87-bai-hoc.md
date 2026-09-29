# 027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

알고리즘, 설계, 기법과, 시간, 복잡도

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **023 & 024: 자료구조 (Data Structures / Cấu trúc dữ liệu)**에서 만든 기준을 이어받아 **027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)

Từ **023 & 024: 자료구조 (Data Structures / Cấu trúc dữ liệu)**, ta đã có điểm tựa để bước vào **027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 87/95 trước khi đi vào chi tiết.

Để đọc **027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **알고리즘 설계 기법 (Kỹ thuật thiết kế thuật toán)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 알고리즘 설계 기법 (Kỹ thuật thiết kế thuật toán)

Các ý ngay dưới **알고리즘 설계 기법 (Kỹ thuật thiết kế thuật toán)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- **분할과 정복 (Divide & Conquer):** Chia để trị. Chia nhỏ vấn đề đến khi không chia được nữa rồi gộp lại. (VD: Merge Sort, Quick Sort).
- **동적계획법 (Dynamic Programming - Quy hoạch động):** Chia bài toán, nhưng CÓ lưu lại kết quả (bộ nhớ) để tận dụng cho lần sau. (VD: Fibonacci).
- **탐욕법 (Greedy):** Tham lam. Chọn cái tốt nhất ở *ngay thời điểm hiện tại*, không cần biết tương lai.
- **백트래킹 (Backtracking):** Quay lui. Đi thử, nếu thấy bế tắc (không triển vọng - promising) thì quay lại nút cha.

Các bullet của **알고리즘 설계 기법 (Kỹ thuật thiết kế thuật toán)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **알고리즘 설계 기법 (Kỹ thuật thiết kế thuật toán)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **시간 복잡도 (Time Complexity - Độ phức tạp thời gian)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **시간 복잡도 (Time Complexity - Độ phức tạp thời gian)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 시간 복잡도 (Time Complexity - Độ phức tạp thời gian)

Bây giờ ta đi vào nội dung của **시간 복잡도 (Time Complexity - Độ phức tạp thời gian)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- Đếm số lần thực thi các phép toán (không phải tính thời gian bằng giây).
- Biểu diễn: Big-O (최악 - Tệ nhất), Theta (평균 - Trung bình), Omega (최상 - Tốt nhất).
- **Thứ tự (Nhanh -> Chậm):** O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ)
- O(1) nghĩa là: Dữ liệu lớn đến đâu thời gian vẫn không đổi.

- **Vietnamese Explanation:** Greedy giống như đi nhặt tiền: cứ thấy tờ to nhất trước mặt là nhặt, bất chấp sau đó dẫn vào ngõ cụt. Dynamic Programming giống như làm toán: kết quả bài 1 lưu ra nháp để dùng cho bài 2.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Divide = Cắt nhỏ. Dynamic = Nhớ bài cũ. Greedy = Tham bát bỏ mâm. Backtrack = Đi lùi. O(1) là nhanh nhất.

---

Với **시간 복잡도 (Time Complexity - Độ phức tạp thời gian)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **시간 복잡도 (Time Complexity - Độ phức tạp thời gian)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.