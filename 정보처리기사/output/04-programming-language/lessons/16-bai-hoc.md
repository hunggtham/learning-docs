# 246 - 249. 입출력 함수와 포맷 (I/O Functions & Formats)

## 학습 목표 (Mục tiêu)
- Nắm vững cú pháp và sự khác biệt giữa các hàm nhập xuất chuyên biệt trong ngôn ngữ C: Nhập xuất ký tự đơn (`getchar`, `putchar`) và Nhập xuất chuỗi ký tự (`gets`, `puts`).
- Hiểu rõ cơ chế bộ đệm bàn phím (Input Buffer) của hàm `scanf` và cách xử lý ký tự khoảng trắng / xuống dòng còn sót lại.
- Phân tích chi tiết quy tắc định dạng độ rộng và độ chính xác số học: `%nd` (độ rộng tối thiểu $n$), `%n.mf` (độ rộng $n$, $m$ số thập phân), và dấu trừ `-` căn lề trái.

## 핵심 키워드 (Từ khóa)
- getchar() & putchar() (단일 문자 입출력)
- gets() & puts() (문자열 입출력 / puts의 자동 개행)
- 입력 버퍼 (Input Buffer / 버퍼 비우기)
- 서식 지정자 포맷팅 (`%nd`, `%n.mf`, `%-nd`)
- 필드 폭 (Field Width)
- 소수점 정밀도 (Precision)

## 선행·연결 개념 (Kiến thức liên kết)
- [15-bai-hoc.md](15-bai-hoc.md): Dữ liệu nhập xuất và hàm in cơ bản.
- [17-bai-hoc.md](17-bai-hoc.md): Câu lệnh điều khiển rẽ nhánh `if` và `switch-case`.
- [14-bai-hoc.md](14-bai-hoc.md): Nhập xuất nâng cao và các ký tự điều khiển escape.

## 읽는 방법 (Cách đọc)
- Phân biệt các cặp hàm chuyên dụng trong C:
  - **`getchar()` / `putchar()`:**
    - `getchar()`: Đọc duy nhất **1 ký tự** từ bàn phím.
    - `putchar(c)`: In đúng **1 ký tự** ra màn hình console (không xuống dòng).
  - **`gets()` / `puts()`:**
    - `gets(str)`: Đọc cả dòng văn bản từ bàn phím (bao gồm cả dấu cách) cho đến khi gặp phím Enter (`\n`).
    - `puts(str)`: In cả chuỗi ký tự ra màn hình và **TỰ ĐỘNG XUỐNG DÒNG** ở cuối chuỗi (đây là điểm khác biệt lớn nhất với `printf("%s", str)`).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng các hàm nhập xuất chuyên biệt trong C:**

| Nhóm hàm | Hàm Nhập (Input) | Hàm Xuất (Output) | Đặc trưng cốt lõi chuẩn thi |
| :--- | :--- | :--- | :--- |
| **Ký tự đơn** | `c = getchar();` | `putchar(c);` | Nhập và xuất đúng 1 ký tự kiểu `char`; nhanh và tốn ít bộ nhớ |
| **Chuỗi ký tự** | `gets(str);` | `puts(str);` | `gets` nhận cả dấu khoảng cách; **`puts` tự động in thêm ký tự xuống dòng `\n` sau khi in chuỗi** |
| **Định dạng tổng quát** | `scanf("포맷", &var);` | `printf("포맷", var);` | Đa năng nhất; hỗ trợ nhiều kiểu dữ liệu cùng lúc thông qua 서식 문자열 |

- **Bảng quy tắc định dạng độ rộng và căn lề (Formatting Modifiers):**

| Cú pháp định dạng | Ý nghĩa kỹ thuật | Ví dụ với giá trị số 123 | Kết quả hiển thị màn hình |
| :--- | :--- | :--- | :--- |
| **`%5d`** | Chiếm ít nhất 5 vị trí; **mặc định căn lề phải** | `printf("[%5d]", 123);` | `[  123]` (2 khoảng trắng ở trước) |
| **`%-5d`** | Chiếm ít nhất 5 vị trí; có dấu `-` nên **căn lề trái** | `printf("[%-5d]", 123);` | `[123  ]` (2 khoảng trắng ở sau) |
| **`%05d`** | Chiếm 5 vị trí; **chèn thêm số 0** vào các vị trí trống bên trái | `printf("[%05d]", 123);` | `[00123]` |
| **`%6.2f`** | Chiếm 6 vị trí (gồm cả dấu chấm); lấy đúng 2 số thập phân | `printf("[%6.2f]", 3.1415);` | `[  3.14]` (Làm tròn thành 3.14, rộng 6) |
| **`%.2f`** | Không giới hạn tổng độ rộng; chỉ cố định lấy 2 số thập phân | `printf("[%.2f]", 3.1415);` | `[3.14]` |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Bẫy bộ đệm khi kết hợp `scanf` và `gets`/`getchar`:**
  - Khi gõ số và bấm Enter trong `scanf("%d", &num);`, số được đọc vào biến `num`, nhưng ký tự Enter (`\n`) vẫn còn nằm lại trong bộ đệm bàn phím (Input Buffer).
  - Nếu ngay sau đó gọi `gets(str);` hoặc `getchar();`, hàm này sẽ đọc ngay ký tự `\n` còn sót lại đó và kết thúc lập tức mà không kịp chờ người dùng gõ chuỗi mới.
  - Giải pháp: Chèn thêm một lệnh `getchar();` hoặc `while(getchar() != '\n');` ở giữa để dọn sạch bộ đệm bàn phím.

### 복습 체크리스트
- [ ] Nhớ hàm `puts(str)` tự động xuống dòng sau khi in chuỗi (khác `printf`).
- [ ] Nhớ `%5d` căn lề phải (thêm khoảng trắng trước), `%-5d` căn lề trái (thêm khoảng trắng sau).
- [ ] Nhớ `%05d` chèn thêm các số 0 vào phía trước (ví dụ: `00123`).
- [ ] Giải thích được tại sao `scanf` để lại ký tự `\n` trong bộ đệm bàn phím.
