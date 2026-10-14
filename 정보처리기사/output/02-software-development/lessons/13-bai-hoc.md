# 080: 수식의 표기법 (Expression Notation)

## 080: 수식의 표기법 (Expression Notation)

Chuyển đổi biểu thức toán học tương ứng với duyệt cây.
- **Infix (Trung tố):** `A + B` (Giống Inorder).
- **Prefix (Tiền tố):** `+ A B` (Giống Preorder).
- **Postfix (Hậu tố):** `A B +` (Giống Postorder - Máy tính rất thích kiểu này vì dùng Stack tính cực dễ).

### Cách chuyển đổi Infix sang Postfix
1. Đóng ngoặc toàn bộ theo thứ tự ưu tiên: `A / B * (C + D)` -> `((A / B) * (C + D))`
2. Kéo Dấu toán tử ra phía **SAU** dấu ngoặc của nó: `((A B /) (C D +) *)`
3. Xóa ngoặc: `A B / C D + *`

- **Vietnamese Explanation:** Máy tính không hiểu `A+B*C` vì nó không biết cái nào ưu tiên trước. Nó dùng Postfix `A B C * +` ném vào Stack để tính một lèo không cần ngoặc.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Postfix = Dấu nằm ở cuối cụm. Prefix = Dấu nằm ở đầu cụm.

---
