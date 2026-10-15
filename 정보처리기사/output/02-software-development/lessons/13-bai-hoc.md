# 080: 수식의 표기법 (Expression Notation)

## 학습 목표 (Mục tiêu)
- Nắm vững mối tương quan 1-1 giữa ba dạng biểu thức toán học và ba thuật toán duyệt cây biểu thức nhị phân: Infix (Inorder), Prefix (Preorder) và Postfix (Postorder).
- Thành thạo giải thuật tính toán giá trị số thực tế của biểu thức Postfix bằng cách mô phỏng từng bước hoạt động PUSH và POP trên ngăn xếp (Stack).
- Rèn luyện kỹ năng xử lý các bài toán chuyển đổi biểu thức phức tạp có chứa nhiều mức ngoặc và các toán tử ưu tiên hỗn hợp trong đề thi trắc nghiệm.

## 핵심 키워드 (Từ khóa)
- 수식 표기법 (Expression Notation)
- 중위 표기법 (Infix / Inorder)
- 전위 표기법 (Prefix / Preorder)
- 후위 표기법 (Postfix / Postorder)
- 스택 연산 시뮬레이션 (Stack Evaluation Trace)
- 연산자 우선순위 (Operator Precedence)

## 선행·연결 개념 (Kiến thức liên kết)
- [02-bai-hoc.md](02-bai-hoc.md): Thao tác PUSH và POP trên cấu trúc dữ liệu Stack.
- [06-bai-hoc.md](06-bai-hoc.md): Ba phương pháp duyệt cây nhị phân kinh điển.
- [12-bai-hoc.md](12-bai-hoc.md): Quy trình 3 bước chuyển đổi biểu thức Infix sang Postfix.

## 읽는 방법 (Cách đọc)
- Đi thi trắc nghiệm có 2 dạng bài cốt lõi:
  - Dạng 1: Cho biểu thức chữ $A + B * C \dots$ yêu cầu chuyển sang Postfix hoặc Prefix.
  - Dạng 2: Cho biểu thức số hậu tố $3\ 4\ 2\ *\ +\dots$ yêu cầu tính ra kết quả số cuối cùng bằng mô phỏng Stack.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng tương đương Cây biểu thức và Ký hiệu toán học:**

| Ký hiệu toán học | Tương ứng duyệt cây nhị phân | Dấu toán tử nằm ở đâu? |
| :--- | :--- | :--- |
| **Prefix (전위)** | **Preorder Traversal** (Root $\rightarrow$ Left $\rightarrow$ Right) | Đứng **đầu** mỗi cụm phép toán |
| **Infix (중위)** | **Inorder Traversal** (Left $\rightarrow$ Root $\rightarrow$ Right) | Đứng **giữa** hai toán hạng |
| **Postfix (후위)** | **Postorder Traversal** (Left $\rightarrow$ Right $\rightarrow$ Root) | Đứng **cuối** mỗi cụm phép toán |

- **Quy trình mô phỏng tính giá trị biểu thức Postfix bằng Stack (Cực kỳ hay thi):**
  - **Bài toán mẫu:** Tính giá trị của biểu thức Postfix sau: `5 3 2 * + 4 -`
    1. Đọc `5`: Là số $\rightarrow$ PUSH vào Stack: `[5]`
    2. Đọc `3`: Là số $\rightarrow$ PUSH vào Stack: `[5, 3]`
    3. Đọc `2`: Là số $\rightarrow$ PUSH vào Stack: `[5, 3, 2]`
    4. Đọc `*`: Là toán tử $\rightarrow$ POP `2` và `3` ra, tính $3 \times 2 = 6$ $\rightarrow$ PUSH `6` vào Stack: `[5, 6]`
    5. Đọc `+`: Là toán tử $\rightarrow$ POP `6` và `5` ra, tính $5 + 6 = 11$ $\rightarrow$ PUSH `11` vào Stack: `[11]`
    6. Đọc `4`: Là số $\rightarrow$ PUSH vào Stack: `[11, 4]`
    7. Đọc `-`: Là toán tử $\rightarrow$ POP `4` và `11` ra, tính $11 - 4 = 7$ $\rightarrow$ PUSH `7` vào Stack: `[7]`
    - **Kết quả cuối cùng:** **`7`**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Lưu ý thứ tự ngôi toán hạng khi thực hiện phép trừ (-) và phép chia (/):**
  - Giả sử trong Stack đang có: `[A, B]` (với `B` nằm ở đỉnh Top).
  - Khi gặp toán tử `-`:
    - Phần tử POP ra đầu tiên là $B$ (toán hạng thứ hai / Subtrahend).
    - Phần tử POP ra kế tiếp là $A$ (toán hạng thứ nhất / Minuend).
    - Phép toán phải thực hiện là: $\mathbf{A - B}$ (tuyệt đối không được lấy $B - A$).
  - Tương tự với phép chia `/`: Phải thực hiện $\mathbf{A / B}$.

### 복습 체크리스트
- [ ] Nhớ phép tương quan: Infix = Inorder, Prefix = Preorder, Postfix = Postorder.
- [ ] Thực hiện chuẩn xác từng bước PUSH / POP trên Stack để tính giá trị biểu thức Postfix.
- [ ] Chú ý đúng thứ tự toán hạng: Phần tử lấy ra sau nằm bên trái phép trừ và phép chia.
- [ ] Tính nhẩm ra kết quả biểu thức số hậu tố trong vòng dưới 60 giây khi làm đề thi.
