# 10. 코드 (Code) 개요 & 종류

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa của Mã (Code) và 5 chức năng cơ bản trong hệ thống thông tin: 식별 (Nhận dạng), 분류 (Phân loại), 배열 (Sắp xếp), 표준화 (Chuẩn hóa) và 간소화 (Thu gọn/Đơn giản hóa).
- Nằm lòng đặc điểm phân biệt của 7 loại mã hóa kinh điển: 순차 코드 (Sequential), 블록 코드 (Block), 10진 코드 (Decimal), 그룹 분류 코드 (Group Classification), 연상 코드 (Mnemonic), 표의 숫자 코드 (Significant Digit), 합성 코드 (Combined).
- Hiểu nguyên tắc thiết kế hệ thống gán mã (Code Assignment System) để đảm bảo tính mở rộng và khả năng nhận diện đối tượng chính xác.

## 핵심 키워드 (Từ khóa)
- 코드 (Code)
- 순차 코드 (Sequential Code)
- 블록 코드 (Block Code)
- 10진 코드 (Decimal Code / Dewey Decimal)
- 그룹 분류 코드 (Group Classification Code)
- 연상 코드 (Mnemonic Code)
- 표의 숫자 코드 (Significant Digit Code)
- 합성 코드 (Combined Code)
- 코드 부여 체계 (Code Assignment System)

## 선행·연결 개념 (Kiến thức liên kết)
- [68-bai-hoc.md](68-bai-hoc.md): 재사용 (Reuse) - Chuẩn hóa mã nguồn và thành phần hệ thống.
- [04-bai-hoc.md](04-bai-hoc.md): Khảo sát và phân tích yêu cầu dữ liệu.
- [10-bai-hoc.md](10-bai-hoc.md): Thiết kế từ điển dữ liệu (Data Dictionary).

## 읽는 방법 (Cách đọc)
- Đi thi trắc nghiệm thường cho ví dụ thực tế rồi hỏi đó là loại mã nào:
  - Thấy **"Thứ tự liên tục 1, 2, 3..."** $\rightarrow$ **순차 코드 (Sequential)**.
  - Thấy **"Chia dải số theo nhóm 1~100, 101~200"** $\rightarrow$ **블록 코드 (Block)**.
  - Thấy **"Phân loại sách thư viện (도서관 분류), chia 0~9 lặp lại"** $\rightarrow$ **10진 코드 (Decimal)**.
  - Thấy **"Đại - Trung - Tiểu phân loại (대분류-중분류-소분류)"** $\rightarrow$ **그룹 분류 코드 (Group Classification)**.
  - Thấy **"Ký tự gợi nhớ TV-40 (Tivi 40 inch)"** $\rightarrow$ **연상 코드 (Mnemonic)**.
  - Thấy **"Lấy trực tiếp kích thước vật lý (dài, rộng, trọng lượng) làm mã"** $\rightarrow$ **표의 숫자 코드 (Significant Digit)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Khái niệm và 5 chức năng cơ bản của Code:**
  - **Khái niệm:** Code là hệ thống các ký hiệu (chữ số, chữ cái, ký tự đặc biệt) được quy ước để đại diện cho các đối tượng dữ liệu nhằm phục vụ việc xử lý, lưu trữ và truyền tải tự động trên máy tính.
  - **5 chức năng cơ bản (코드의 5대 기능):**
    1. **식별 (Identification):** Định danh duy nhất từng thực thể, không bị trùng lặp.
    2. **분류 (Classification):** Gom nhóm các đối tượng có cùng đặc trưng chung.
    3. **배열 (Arrangement / Sorting):** Sắp xếp dữ liệu theo một trật tự logic nhất định.
    4. **표준화 (Standardization):** Thống nhất cách gọi và định dạng trong toàn hệ thống.
    5. **간소화 (Simplification):** Rút gọn tên gọi dài dòng thành chuỗi ký tự ngắn gọn, tiết kiệm bộ nhớ và giảm sai sót khi nhập liệu.

- **Bảng tổng hợp 7 loại mã hóa kinh điển (코드의 7가지 종류):**

| Loại mã (Hàn / Anh) | Cơ chế gán mã | Ví dụ minh họa thực tế |
| :--- | :--- | :--- |
| **순차 코드 (Sequential Code)** | Đánh số thứ tự tăng dần liên tục (1, 2, 3, ...) theo thứ tự phát sinh sự kiện | Mã số sinh viên đăng ký nhập học: 001, 002, 003 |
| **블록 코드 (Block Code)** | Chia trước một khối dải số cho từng nhóm chung thuộc tính (구분 코드) | Phòng Kế toán: 1001~2000; Phòng Kinh doanh: 2001~3000 |
| **10진 코드 (Decimal Code)** | Phân chia lặp đi lặp lại từ 0 đến 9 theo hệ thập phân, thường ứng dụng trong quản lý thư viện | Hệ thống phân loại thập phân Dewey (DDC): 500 (Khoa học), 510 (Toán học), 512 (Đại số) |
| **그룹 분류 코드 (Group Classification Code)** | Phân cấp theo cấu trúc rõ ràng: Đại phân loại - Trung phân loại - Tiểu phân loại (대분류 - 중분류 - 소분류) | Mã phân loại mặt hàng siêu thị: `1-01-005` (1: Đồ gia dụng, 01: Nhà bếp, 005: Chảo chống dính) |
| **연상 코드 (Mnemonic Code)** | Dùng chữ cái viết tắt hoặc ký tự gợi nhớ trực tiếp đến tên, đặc tính hay kích cỡ của đối tượng | `TV-55` (Tivi màn hình 55 inch); `RAM-32G` (Thanh nhớ RAM dung lượng 32GB) |
| **표의 숫자 코드 (Significant Digit Code)** | Sử dụng trực tiếp các số đo vật lý (chiều dài, độ dày, trọng lượng, dung tích) để tạo thành mã | Thanh thép tròn có đường kính 25mm, chiều dài 6000mm mã hóa thành `25-6000` |
| **합성 코드 (Combined Code)** | Kết hợp hai hoặc nhiều phương pháp mã hóa ở trên để đáp ứng yêu cầu quản lý đa chiều | Mã số nhân viên: `IT-2024-0042` (Kết hợp 연상 IT + 순차 0042) |

- **Hệ thống gán mã (코드 부여 체계 - Code Assignment System):**
  - Là bản quy chuẩn định nghĩa số ký tự (자릿수), vị trí của từng phân đoạn và ký tự ngăn cách.
  - Giúp người vận hành chỉ cần nhìn vào mã là lập tức hiểu được xuất xứ, công dụng và phạm vi áp dụng mà không cần tra cứu sổ tay dữ liệu.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Quy tắc thiết kế mã hóa tối ưu trong công nghệ thông tin:**
  - **Tính duy nhất (Uniqueness):** Mỗi đối tượng chỉ có một mã duy nhất và ngược lại.
  - **Tính mở rộng (Expandability):** Luôn phải dự phòng khoảng trống (khoảng trống số trong Block Code) để chèn thêm đối tượng mới mà không phá vỡ cấu trúc mã cũ.
  - **Tính ngắn gọn và dễ nhớ:** Hạn chế ký tự gây nhầm lẫn (như số `0` với chữ cái `O`, số `1` với chữ `I` hoặc `l`).

### 복습 체크리스트
- [ ] Nhớ 5 chức năng cơ bản của mã: 식별, 분류, 배열, 표준화, 간소화.
- [ ] Phân biệt được đặc điểm của 순차 코드 (Số thứ tự liên tiếp) và 블록 코드 (Phân khối dải số).
- [ ] Nhận diện 10진 코드 qua ứng dụng phân loại sách thư viện (도서 분류).
- [ ] Nhớ 그룹 분류 코드 gắn liền với 3 cấp: 대분류, 중분류, 소분류.
- [ ] Nhận diện 연상 코드 (Gợi nhớ TV-40) và 표의 숫자 코드 (Số đo vật lý 120-5000).
