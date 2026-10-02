# 078 & 079: 트리 및 운행법 (Tree & Tree Traversal)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **078 & 079: 트리 및 운행법 (Tree & Tree Traversal)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối tree với traversal, recursion và queue/stack, để cấu trúc phân cấp được duyệt theo mục tiêu.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **078 & 079: 트리 및 운행법 (Tree & Tree Traversal)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **078 & 079: 트리 및 운행법 (Tree & Tree Traversal)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **026: 그래프 (Graph / Đồ thị)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **078 & 079: 트리 및 운행법 (Tree & Tree Traversal)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

트리, 운행법

> **Chuyển mạch:** Ở chặng này của **078 & 079: 트리 및 운행법 (Tree & Tree Traversal)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **025: 트리 (Tree / Cây)**에서 만든 기준을 이어받아 **078 & 079: 트리 및 운행법 (Tree & Tree Traversal)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **078 & 079: 트리 및 운행법 (Tree & Tree Traversal)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **078 & 079: 트리 및 운행법 (Tree & Tree Traversal)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **078 & 079: 트리 및 운행법 (Tree & Tree Traversal)**, **078 & 079: 트리 및 운행법 (Tree & Tree Traversal)** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 078 & 079: 트리 및 운행법 (Tree & Tree Traversal)

Từ **025: 트리 (Tree / Cây)**, ta đã có điểm tựa để bước vào **078 & 079: 트리 및 운행법 (Tree & Tree Traversal)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 9/101 trước khi đi vào chi tiết.

Để đọc **078 & 079: 트리 및 운행법 (Tree & Tree Traversal)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **트리 (Tree - Cây)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 트리 (Tree - Cây)

Các ý ngay dưới **트리 (Tree - Cây)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “트리 (Tree - Cây)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **사이클(Cycle)이 없는 그래프.** (Đồ thị không có vòng lặp / chu trình).
- **단말 노드 (Leaf Node):** Nút lá (Không có con / Degree = 0).
- **차수 (Degree):** Số nút con của một nút.
- **트리의 차수 (Tree's Degree):** Degree lớn nhất trong toàn bộ cây.
- **깊이 (Depth):** Số tầng (Level) tối đa của cây.

Với **트리 (Tree - Cây)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **트리 (Tree - Cây)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **트리의 운행법 (Tree Traversal - Duyệt cây)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **트리의 운행법 (Tree Traversal - Duyệt cây)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 트리의 운행법 (Tree Traversal - Duyệt cây)

Bây giờ ta đi vào nội dung của **트리의 운행법 (Tree Traversal - Duyệt cây)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “트리의 운행법 (Tree Traversal - Duyệt cây)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- Theo vị trí của **Root (Gốc)**:
  - **Preorder (전위):** **Root** -> Left -> Right.
  - **Inorder (중위):** Left -> **Root** -> Right.
  - **Postorder (후위):** Left -> Right -> **Root**.

- **Ví dụ (Example):** Cây có Gốc A, Trái B, Phải C. Pre = ABC, In = BAC, Post = BCA.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Pre (Trước) = Root đi đầu. In (Giữa) = Root ở giữa. Post (Sau) = Root đi chót.

---

Với **트리의 운행법 (Tree Traversal - Duyệt cây)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **트리의 운행법 (Tree Traversal - Duyệt cây)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **078 & 079: 트리 및 운행법 (Tree & Tree Traversal)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **026: 그래프 (Graph / Đồ thị)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

> **Bàn giao:** Sau **078 & 079: 트리 및 운행법 (Tree & Tree Traversal)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
