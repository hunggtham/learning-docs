# 025: 트리 (Tree / Cây)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **025: 트리 (Tree / Cây)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **025: 트리 (Tree / Cây)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **026: 그래프 (Graph / Đồ thị)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

트리

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **30. 트리 구조 추가 용어 (Tree Terminology Additional)**에서 만든 기준을 이어받아 **025: 트리 (Tree / Cây)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 025: 트리 (Tree / Cây)

Ở bước 7/95, **025: 트리 (Tree / Cây)** xuất hiện như phần tiếp nối của **30. 트리 구조 추가 용어 (Tree Terminology Additional)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **025: 트리 (Tree / Cây)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng cho ta tiêu chí đối chiếu, còn công thức cho ta quan hệ giữa các đại lượng; hãy dùng cả hai để kiểm tra cùng một kết luận.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

| 용어 (Thuật ngữ) | 설명 (Giải thích) | 예시 (Ví dụ) |
|---|---|---|
| 루트 노드 (Root Node) | Nút gốc, không có cha. Chỉ có 1 gốc. | A |
| 단말 노드 (Leaf/Terminal Node) | Nút lá, ở cuối cùng, không có con. | D, E, H, I, G |
| 레벨 (Level) | Độ sâu từ gốc tới nút. | E có Level là 3. |
| 깊이 (Depth) | Độ sâu lớn nhất của cây (Max Level - 1 hoặc tùy cách tính). | Depth = 3. |
| 차수 (Degree of Node) | Bậc của một nút: Số lượng con của nút đó. | B có 3 con => Degree = 3. |
| 트리의 차수 (Degree of Tree) | Bậc của cây: Bậc lớn nhất trong tất cả các nút. | Cả cây có nút max là 3 => Degree của cây = 3. |

Trước hết, ta đặt **트리 순회 (Tree Traversal - Duyệt cây)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **트리 순회 (Tree Traversal - Duyệt cây)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 트리 순회 (Tree Traversal - Duyệt cây)

Bây giờ ta đi vào nội dung của **트리 순회 (Tree Traversal - Duyệt cây)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- **전위 순회 (Preorder):** Root -> Left -> Right.
- **중위 순회 (Inorder):** Left -> Root -> Right.
- **후위 순회 (Postorder):** Left -> Right -> Root.

- **Vietnamese Explanation:** Cách tính Bậc của cây rất hay thi: Tìm cái nút nào đẻ nhiều con nhất, số con đó chính là Bậc của toàn bộ cây. Khi duyệt cây, chữ "Pre/In/Post" (Trước/Giữa/Sau) dùng để chỉ vị trí của Root. Root đứng trước là Pre, ở giữa là In, ở cuối là Post.
- 💡 **Mẹo ghi nhớ (Mnemonics):** 단말 (Đoạn mạt = Cuối) = Leaf (Lá). Degree = Bậc = Số con. Pre/In/Post = Vị trí của Gốc (Root).

---

Với **트리 순회 (Tree Traversal - Duyệt cây)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Với **트리 순회 (Tree Traversal - Duyệt cây)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Như vậy, **025: 트리 (Tree / Cây)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **026: 그래프 (Graph / Đồ thị)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.