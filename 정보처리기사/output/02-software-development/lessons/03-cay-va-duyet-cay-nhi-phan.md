# 이진 트리와 트리 순회 (Cây và duyệt cây nhị phân)

## 학습 목표
- Nắm vững định nghĩa Cây (`트리 / Tree`): đồ thị liên thông vô hướng không có chu trình (`사이클 없는 연결 그래프`), và định lý số cạnh luôn bằng $N - 1$.
- Thuộc lòng hệ thống thuật ngữ đo lường cấu trúc cây: Nút gốc (`루트`), Nút lá (`단말 / 잎 노드`), Bậc của nút (`노드의 차수`), Bậc của cây (`트리의 차수`), Mức (`레벨`), Độ sâu (`깊이 / 높이`), và Rừng (`숲 / Forest` - bỏ Root thu được Forest).
- Phân biệt 5 dạng cây nhị phân đặc thù: Cây nhị phân bão hòa (`포화 이진 트리 / Perfect`), Cây nhị phân hoàn chỉnh (`완전 이진 트리 / Complete`), Cây nhị phân đầy đủ (`전 이진 트리 / Full`), Cây nhị phân lệch (`편향 이진 트리 / Skewed`), và Cây nhị phân có ren (`스레드 이진 트리 / Threaded`).
- Làm chủ 3 thuật toán duyệt cây nhị phân: Tiền thứ tự (`전위 순회 / Preorder` - Root L R), Trung thứ tự (`중위 순회 / Inorder` - L Root R), và Hậu thứ tự (`후위 순회 / Postorder` - L R Root).
- Áp dụng thành thạo kỹ thuật tái dựng lại hình dạng cây nhị phân khi biết chuỗi duyệt Inorder kết hợp với Preorder hoặc Postorder.

## 핵심 키워드
- 비선형 구조 (Cấu trúc phi tuyến / Non-linear Data Structure)
- 트리 & 이진 트리 (Cây & Cây nhị phân / Tree & Binary Tree)
- 단말 노드 (Nút lá / Leaf Node / 차수 = 0)
- 트리의 차수 (Bậc của cây / Degree of Tree / max degree)
- 숲 (Rừng / Forest / 루트 제거 시 생성)
- 포화·완전·편향·스레드 이진 트리 (Perfect, Complete, Skewed, Threaded Binary Tree)
- 트리 순회 (Duyệt cây / 전위 Preorder, 중위 Inorder, 후위 Postorder)
- 트리 복원 기 pháp (Tái dựng cây nhị phân từ Inorder và Preorder/Postorder)

## 선행·연결 개념
- **Từ đâu (Origin / Prerequisite):** Ở bài học trước [02-ky-phap-bieu-thuc-va-stack.md](02-ky-phap-bieu-thuc-va-stack.md), chúng ta đã khảo sát mô hình Cây biểu thức nhị phân và ánh xạ giữa thứ tự duyệt với các ký pháp Prefix, Infix, Postfix.
- **Đang giải quyết gì (Current Problem):** Cấu trúc cây giải quyết bài toán mô hình hóa các hệ thống có tính phân cấp cha - con (thư mục tệp tin, cây cú pháp AST, bảng chỉ mục CSDL). Bài học này làm chủ hệ thống thuật ngữ đo lường cây, các dạng cây nhị phân và thuật toán duyệt cây.
- **Dùng đi đâu (Forward Handoff):** Khi nới lỏng điều kiện và cho phép các nút liên kết tự do đa chiều và có chu trình, ta mở rộng sang cấu trúc mạng lưới tổng quát [04-do-thi-va-bieu-dien-do-thi.md](04-do-thi-va-bieu-dien-do-thi.md) để khảo sát cấu trúc Đồ thị (Graph).

## 읽는 방법
- Đọc TẦNG A để nắm chắc bảng thuật ngữ đo lường cây, bảng so sánh 5 dạng cây nhị phân và các bẫy đề thi trắc nghiệm kinh điển.
- Đọc TẦNG B để theo dõi các sơ đồ ASCII trực quan của 3 loại cây, ví dụ trace duyệt cây nhị phân từng bước và quy tắc 3 bước tái dựng hình dạng cây.

---

## 이진 트리와 트리 순회

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng thuật ngữ đo lường cấu trúc Cây chuẩn đề thi
| Thuật ngữ | Tên tiếng Hàn & Anh | Định nghĩa kỹ thuật | Dấu hiệu nhận diện đề thi |
| :--- | :--- | :--- | :--- |
| **Nút gốc** | **루트 노드 (Root Node)** | Nút đỉnh cao nhất của cây, không có nút cha trỏ đến | Cây chỉ có duy nhất 1 Root |
| **Nút lá / Đơn vị cuối** | **단말 노드 / 잎 노드 (Terminal / Leaf)** | Nút ở đáy tận cùng của nhánh, **không có nút con nào** | **차수 (Degree) = 0** |
| **Nút trung gian** | **비단말 노드 (Non-terminal)** | Nút có ít nhất một nút con kết nối bên dưới | Degree $\ge 1$ |
| **Bậc của nút** | **노드의 차수 (Degree of Node)** | **Số lượng nhánh con trực tiếp** xuất phát từ nút đó | Đếm số con trực tiếp của nút |
| **Bậc của cây** | **트리의 차수 (Degree of Tree)** | **Giá trị 차수 lớn nhất** trong số tất cả các nút trong cây | $\max(\text{Degree của toàn bộ các nút})$ |
| **Mức / Độ sâu** | **레벨 (Level) / 깊이 (Depth)** | Tầng bậc của nút (Root ở Level 1, mỗi thế hệ tăng 1) | Chiều cao / độ sâu tối đa của cây |
| **Rừng** | **숲 (Forest)** | Tập hợp của các cây không giao nhau | **Loại bỏ Root Node của cây sẽ thu được một Forest** |

#### 2. Bảng 5 dạng cây nhị phân đặc thù
| Dạng cây | Tên tiếng Hàn & Anh | Điều kiện biên và Đặc điểm cấu trúc | Công thức số nút ($h$ là độ sâu) |
| :--- | :--- | :--- | :--- |
| **Bão hòa** | **포화 이진 트리 (Perfect)** | Mọi lá ở đáy cùng, mọi nút trong có đủ 2 con | $N = 2^h - 1$ |
| **Hoàn chỉnh** | **완전 이진 트리 (Complete)** | Đầy từ mức $1 \sim h-1$; mức $h$ điền **tuần tự từ trái sang phải** | $2^{h-1} \le N \le 2^h - 1$; nền tảng Heap |
| **Đầy đủ** | **전 이진 트리 (Full)** | Mọi nút chỉ có **đúng 0 hoặc đúng 2 con**, không có nút 1 con | Không có nút nào bậc 1 |
| **Lệch** | **편향 이진 트리 (Skewed)** | Lệch hẳn về bên trái hoặc phải; thoái hóa thành danh sách | Tìm kiếm thoái hóa xuống $O(n)$ |
| **Có ren** | **스레드 이진 트리 (Threaded)** | Tận dụng con trỏ NULL lưu nút trước/sau theo Inorder | Duyệt Inorder nhanh **không cần đệ quy/Stack** |

#### 3. Bẫy đề thi trắc nghiệm kinh điển (기출 함정 포인트)
- **Bẫy 1: Định lý số cạnh của cây:** Nếu một cây có $N$ đỉnh thì tổng số nhánh nối luôn bằng đúng $\mathbf{N - 1}$. (Ví dụ: Cây có 10 nút thì bắt buộc có 9 cạnh nối).
- **Bẫy 2: Nút lá (Terminal Node):** 단말 노드 luôn có $\mathbf{\text{차수} = 0}$.
- **Bẫy 3: Forest:** Bỏ Root Node của cây sẽ thu được **숲 (Forest)**.
- **Bẫy 4: Thứ tự thăm Root trong 3 phép duyệt:**
  - **전위 (Preorder):** $\mathbf{Root} \rightarrow \text{Left} \rightarrow \text{Right}$ (Root đứng đầu).
  - **중위 (Inorder):** $\text{Left} \rightarrow \mathbf{Root} \rightarrow \text{Right}$ (Root ở giữa).
  - **후위 (Postorder):** $\text{Left} \rightarrow \text{Right} \rightarrow \mathbf{Root}$ (Root ở cuối).

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Sơ đồ trực quan 3 loại cây nhị phân tiêu biểu
```
   [ 포화 이진 트리 ]            [ 완전 이진 트리 ]            [ 편향 이진 트리 ]
         (1)                          (1)                         (1)
        /   \                        /   \                         \
      (2)   (3)                    (2)   (3)                       (2)
      / \   / \                    / \   /                           \
    (4) (5)(6) (7)               (4) (5)(6)                          (3)
 (Đầy kín mọi lá ở đáy)     (Điền tuần tự từ trái sang phải)     (Lệch hẳn 1 bên)
```

#### 2. Ví dụ trace duyệt cây nhị phân thực hành
Xét cây nhị phân mẫu sau:
```
          [A]
         /   \
       [B]   [C]
       / \     \
     [D] [E]   [F]
```

- **Preorder (전위 순회):** Root $\rightarrow$ Left $\rightarrow$ Right
  - Thao tác: Thăm `A` $\rightarrow$ nhánh trái thăm `B` $\rightarrow$ thăm `D` $\rightarrow$ thăm `E` $\rightarrow$ nhánh phải thăm `C` $\rightarrow$ thăm `F`.
  - Kết quả: **`A - B - D - E - C - F`**
- **Inorder (중위 순회):** Left $\rightarrow$ Root $\rightarrow$ Right
  - Thao tác: Kịch sàn trái `D` $\rightarrow$ thăm Root con `B` $\rightarrow$ thăm `E` $\rightarrow$ thăm Root chính `A` $\rightarrow$ sang nhánh phải: thăm Root con `C` $\rightarrow$ thăm `F`.
  - Kết quả: **`D - B - E - A - C - F`**
- **Postorder (후위 순회):** Left $\rightarrow$ Right $\rightarrow$ Root
  - Thao tác: Cây con trái: `D` $\rightarrow$ `E` $\rightarrow$ `B` $\rightarrow$ Cây con phải: `F` $\rightarrow$ `C` $\rightarrow$ thăm Root chính `A` sau cùng.
  - Kết quả: **`D - E - B - F - C - A`**

#### 3. Kỹ thuật tái dựng Cây nhị phân từ kết quả duyệt
Khi đề bài cho trước 2 chuỗi duyệt (Inorder kết hợp với Preorder hoặc Postorder):
1. **Tìm Nút Gốc (Root):**
   - Ký tự **đầu tiên** trong chuỗi **Preorder** chắc chắn là **Root của toàn cây**.
   - Ký tự **cuối cùng** trong chuỗi **Postorder** chắc chắn là **Root của toàn cây**.
2. **Phân chia Cây con Trái / Phải:**
   - Đem nút Root vừa tìm được soi vào chuỗi **Inorder**:
   - Tất cả các ký tự nằm **bên trái Root** trong Inorder bắt buộc thuộc về **Cây con bên trái (Left Subtree)**.
   - Tất cả các ký tự nằm **bên phải Root** trong Inorder bắt buộc thuộc về **Cây con bên phải (Right Subtree)**.
3. **Lặp lại đệ quy:** Tiếp tục áp dụng quy tắc trên cho các cây con cho đến khi vẽ lại hoàn chỉnh toàn bộ hình dạng cây.

---

### 복습 체크리스트
- [ ] Định nghĩa Cây là đồ thị liên thông không có chu trình (사이클 없는 그래프).
- [ ] Nhớ tính chất: Cây có $N$ nút thì luôn có đúng $N - 1$ cạnh nối.
- [ ] Nhớ tính chất 단말 노드 (Leaf Node): Nút không có con, Degree = 0.
- [ ] Tính đúng Bậc của cây (트리의 차수): Lấy giá trị Degree lớn nhất trong các nút.
- [ ] Nhớ định nghĩa Forest: Tập hợp các cây con thu được sau khi bỏ đi Root Node.
- [ ] Phân biệt 포화 이진 트리 (Perfect - đầy mọi mức $2^h-1$) và 완전 이진 트리 (Complete - điền tuần tự từ trái sang phải).
- [ ] Hiểu vai trò của 스레드 이진 트리 (Threaded): Dùng con trỏ NULL làm con trỏ duyệt Inorder không cần Stack/đệ quy.
- [ ] Thuộc lòng thứ tự 3 phép duyệt: Preorder (Root-L-R), Inorder (L-Root-R), Postorder (L-R-Root).
- [ ] Tái dựng được hình dạng cây nhị phân khi biết chuỗi Inorder kết hợp với Preorder hoặc Postorder.
