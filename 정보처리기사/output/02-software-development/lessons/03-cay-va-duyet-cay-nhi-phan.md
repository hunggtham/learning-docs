# 트리와 이진 트리 순회 (Cây và duyệt cây nhị phân)

## 학습 목표
- Nắm vững định nghĩa và hệ thống thuật ngữ đo lường cấu trúc Cây: Nút gốc (`루트`), Nút lá (`단말 노드 / 잎 노드` - Degree = 0), Nút cha/con, Bậc của nút (`노드의 차수`), Bậc của cây (`트리의 차수`), Chiều cao (`깊이/높이`), và Rừng cây (`숲 / Forest`).
- Áp dụng thành thạo định lý toán học: Cây có $N$ đỉnh thì luôn có đúng $N - 1$ cạnh nối; Cây bão hòa có độ sâu $h$ có đúng $2^h - 1$ nút.
- Phân biệt 5 dạng cây nhị phân đặc thù: Cây bão hòa (`포화 이진 트리`), Cây hoàn chỉnh (`완전 이진 트리`), Cây đầy đủ (`전 이진 트리`), Cây lệch (`편향 이진 트리`), và Cây có ren (`스레드 이진 트리`).
- Làm chủ 3 phương pháp duyệt cây nhị phân: Tiền thứ tự (`전위 순회 / Preorder`), Trung thứ tự (`중위 순회 / Inorder`), và Hậu thứ tự (`후위 순회 / Postorder`).
- Thành thạo kỹ thuật tái dựng cây nhị phân từ kết quả duyệt (kết hợp Inorder với Preorder hoặc Postorder).

## 핵심 키워드
- 트리 (Cây / Tree / 비선형 구조 / 사이클 없는 연결 그래프)
- 단말 노드 (Nút lá / Leaf Node / 차수 = 0)
- 트리의 차수 (Bậc của cây / Degree of Tree / max 차수)
- 숲 (Rừng cây / Forest / 루트 제거 시 생성)
- 이진 트리 (Cây nhị phân / Binary Tree / 차수 ≤ 2)
- 포화 vs 완전 이진 트리 (Perfect vs Complete Binary Tree)
- 스레드 이진 트리 (Threaded Binary Tree / NULL 포인터 활용)
- 트리 순회 (Duyệt cây / Preorder, Inorder, Postorder)

## 선행·연결 개념
- **Từ đâu (Origin / Prerequisite):** Ở bài học trước [02-ky-phap-bieu-thuc-va-stack.md](02-ky-phap-bieu-thuc-va-stack.md), chúng ta đã làm quen với mô hình Cây biểu thức nhị phân và mối tương quan giữa duyệt cây với các dạng ký pháp Infix, Prefix, Postfix.
- **Đang giải quyết gì (Current Problem):** Cấu trúc cây giải quyết bài toán mô hình hóa các hệ thống có tính phân cấp cha - con (thư mục tệp tin, cây cú pháp AST, bảng chỉ mục CSDL). Bài học này trang bị toàn bộ thuật ngữ đo lường cây, các dạng cây nhị phân đặc thù và 3 thuật toán duyệt cây chuẩn mực.
- **Dùng đi đâu (Forward Handoff):** Từ cấu trúc cây phân cấp không có chu trình, khi cho phép các nút liên kết tự do đa chiều N-M và tồn tại chu trình, bài học bàn giao sang [04-do-thi-va-bieu-dien-do-thi.md](04-do-thi-va-bieu-dien-do-thi.md) để khảo sát lý thuyết Đồ thị toàn diện.

## 읽는 방법
- Đọc TẦNG A để nắm chắc các công thức tính số cạnh ($N - 1$), số nút tối đa ($2^h - 1$), thuật toán tìm Root để tái dựng cây nhị phân từ 2 chuỗi duyệt, và bảng nhận diện 5 dạng cây nhị phân.
- Đọc TẦNG B để hiểu sâu cơ chế của cây có ren (Threaded Binary Tree) tận dụng con trỏ NULL để duyệt Inorder không cần dùng Stack hay đệ quy.

---

## 트리와 이진 트리 순회

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng thuật ngữ đo lường cấu trúc Cây
| Thuật ngữ (Hàn / Anh) | Định nghĩa kỹ thuật | Dấu hiệu nhận biết trong đề thi |
| :--- | :--- | :--- |
| **루트 노드 (Root Node)** | Nút đỉnh cao nhất của cây, không có nút cha | Cây luôn chỉ có duy nhất 1 Root Node |
| **단말 노드 / 잎 노드 (Leaf Node)** | Nút ở đáy tận cùng của nhánh, không có nút con | **차수 (Degree) = 0** |
| **노드의 차수 (Degree of Node)** | Số lượng nhánh con trực tiếp xuất phát từ nút | Đếm số lượng con trực tiếp của nút đó |
| **트리의 차수 (Degree of Tree)** | **Giá trị 차수 lớn nhất** trong toàn bộ cây | $\max(\text{Degree của tất cả các nút})$ |
| **깊이 / 높이 (Depth / Height)** | Mức tầng lớn nhất mà cây đạt được | $\max(\text{Level của các nút trong cây})$ |
| **숲 (Forest)** | Tập hợp các cây con không giao nhau | **Loại bỏ Root Node của cây sẽ thu được Forest** |

#### 2. Phân loại 5 dạng cây nhị phân (이진 트리)
| Dạng cây | Tên tiếng Hàn & Anh | Đặc trưng cấu trúc | Số lượng nút |
| :--- | :--- | :--- | :---: |
| **Cây bão hòa** | **포화 이진 트리 (Perfect)** | Mọi nút nội bộ có 2 con, tất cả lá nằm ở mức đáy | $N = \mathbf{2^h - 1}$ |
| **Cây hoàn chỉnh** | **완전 이진 트리 (Complete)** | Các mức trên đầy 100%, mức đáy **điền tuần tự từ trái sang phải** | $2^{h-1} \le N \le 2^h - 1$ |
| **Cây đầy đủ** | **전 이진 트리 (Full / Strict)** | Mọi nút chỉ có **đúng 0 hoặc đúng 2 nút con** | Không có nút 1 con |
| **Cây lệch** | **편향 이진 트리 (Skewed)** | Các nút chỉ phát triển lệch hoàn toàn về 1 bên (Trái/Phải) | Tương đương danh sách liên kết |
| **Cây có ren** | **스레드 이진 트리 (Threaded)** | Tận dụng con trỏ `NULL` để lưu nút kế nhiệm/tiền nhiệm | Duyệt Inorder không cần Stack |

#### 3. Bảng 3 phương pháp duyệt cây nhị phân
| Phương pháp | Tên tiếng Hàn & Anh | Thứ tự thăm các nút | Vị trí nút Root | Ký pháp |
| :--- | :--- | :--- | :---: | :---: |
| **Tiền thứ tự** | **전위 순회 (Preorder)** | $\mathbf{Root} \rightarrow \text{Left} \rightarrow \text{Right}$ | Đứng **đầu tiên** | **Prefix** |
| **Trung thứ tự** | **중위 순회 (Inorder)** | $\text{Left} \rightarrow \mathbf{Root} \rightarrow \text{Right}$ | Đứng **ở giữa** | **Infix** |
| **Hậu thứ tự** | **후위 순회 (Postorder)** | $\text{Left} \rightarrow \text{Right} \rightarrow \mathbf{Root}$ | Đứng **sau cùng** | **Postfix** |

#### 4. Kỹ thuật tái dựng Cây nhị phân từ kết quả duyệt
```
[ 1. Tìm Root ] ──> Ký tự ĐẦU của Preorder (hoặc ký tự CUỐI của Postorder)
       │
[ 2. Phân chia ] ──> Soi Root vào chuỗi Inorder:
                     • Chữ nằm bên TRÁI Root  ==> Cây con Trái (Left Subtree)
                     • Chữ nằm bên PHẢI Root ==> Cây con Phải (Right Subtree)
       │
[ 3. Đệ quy ]    ──> Lặp lại cho từng cụm con đến khi vẽ xong toàn bộ cây
```

#### 5. Bẫy đề thi trắc nghiệm kinh điển (기출 함정 포인트)
- **Bẫy 1: Số cạnh nối:** Cây có $N$ nút thì luôn luôn có đúng $\mathbf{N - 1}$ cạnh nối.
- **Bẫy 2: Nút lá (단말 노드):** Nút lá là nút có bậc bằng 0 (`차수 = 0`). Đề thi hay hỏi: "Số lượng nút lá là bao nhiêu?" $\rightarrow$ Đếm tất cả các nút không có con.
- **Bẫy 3: 완전 이진 트리 vs 포화 이진 트리:** Cây Complete chỉ yêu cầu mức đáy điền liên tục từ trái sang phải, không bắt buộc phải đầy kín mức đáy như cây Perfect.
- **Bẫy 4: Tạo Forest:** Xóa bỏ nút Root của một cây thì cấu trúc còn lại được gọi là **숲 (Forest)**.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Định lý và cơ sở toán học cấu trúc cây
- **Định nghĩa đồ thị:** Cây là một đồ thị vô hướng, liên thông và không chứa bất kỳ chu trình nào (`사이클이 없는 연결 그래프`). Giữa hai nút bất kỳ trong cây chỉ tồn tại duy nhất một đường đi đơn giản.
- **Cây nhị phân và Cấu trúc Heap:** Cây nhị phân hoàn chỉnh (Complete Binary Tree) là cấu trúc nền tảng để xây dựng Max-Heap và Min-Heap trong thuật toán sắp xếp vun đống (Heap Sort) và hàng đợi ưu tiên (Priority Queue).

#### 2. Cây nhị phân có ren (Threaded Binary Tree)
- Trong một cây nhị phân gồm $N$ nút, mỗi nút có 2 con trỏ (trái và phải) nên có tổng cộng $2N$ con trỏ. Trong đó có đúng $N - 1$ con trỏ trỏ đến các nút con thật, còn lại đúng $N + 1$ con trỏ mang giá trị `NULL`.
- Cây Threaded tận dụng $N + 1$ con trỏ trống này:
  - Con trỏ trái rỗng: Trỏ đến nút đứng trước trong thứ tự duyệt Inorder (`Inorder Predecessor`).
  - Con trỏ phải rỗng: Trỏ đến nút đứng sau trong thứ tự duyệt Inorder (`Inorder Successor`).
- Lợi ích: Có thể duyệt toàn bộ cây theo Inorder chỉ bằng vòng lặp tuần tự đơn giản, loại bỏ hoàn toàn chi phí bộ nhớ đệm của Call Stack khi đệ quy.

---

### 복습 체크리스트
- [ ] Định nghĩa Cây là đồ thị liên thông không có chu trình (`사이클 없는 연결 그래프`).
- [ ] Thuộc lòng công thức: Cây $N$ đỉnh luôn có $N - 1$ cạnh nối; Cây bão hòa có $2^h - 1$ nút.
- [ ] Nhớ tính chất 단말 노드 (Leaf Node): Nút không có con, Degree = 0.
- [ ] Tính đúng Bậc của cây (트리의 차수): Lấy giá trị Degree lớn nhất trong cây.
- [ ] Nhớ định nghĩa Forest: Cấu trúc thu được sau khi bỏ đi Root Node.
- [ ] Phân biệt rõ 포화 이진 트리 (Perfect) và 완전 이진 트리 (Complete).
- [ ] Hiểu vai trò của 스레드 이진 트리: Tận dụng con trỏ NULL để duyệt Inorder không cần Stack.
- [ ] Thuộc lòng thứ tự 3 phép duyệt: Preorder (Root-L-R), Inorder (L-Root-R), Postorder (L-R-Root).
- [ ] Tái dựng được hình dạng cây nhị phân khi biết chuỗi Inorder kết hợp với Preorder hoặc Postorder.
