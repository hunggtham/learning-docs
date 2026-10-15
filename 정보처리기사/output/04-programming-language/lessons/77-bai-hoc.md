# 234. C언어의 구조체 (struct in C)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, cú pháp khai báo và mục đích ứng dụng của kiểu dữ liệu cấu trúc (구조체 - `struct`) trong ngôn ngữ lập trình C.
- Phân biệt rõ sự khác nhau giữa Mảng (배열 - Array, chỉ tập hợp các phần tử **cùng kiểu dữ liệu**) và Cấu trúc (구조체 - Struct, tập hợp các biến có **khác kiểu dữ liệu**).
- Sử dụng thành thạo hai toán tử truy xuất thành viên cấu trúc: Toán tử dấu chấm (`.`) dùng cho biến cấu trúc trực tiếp và Toán tử mũi tên (`->`) dùng cho con trỏ cấu trúc (`(*p).member == p->member`).

## 핵심 키워드 (Từ khóa)
- C언어 구조체 (`struct`)
- 사용자 정의 자료형 (User-Defined Data Type)
- 이질적 데이터 집합 (Heterogeneous Data Types)
- 멤버 접근 연산자 (`.` Direct Member Access)
- 구조체 포인터와 화살표 연산자 (`->` Indirect Member Access)
- `typedef` 키워드 (Type Definition Aliasing)
- 메모리 정렬과 패딩 (Memory Alignment & Struct Padding)

## 선행·연결 개념 (Kiến thức liên kết)
- [76-bai-hoc.md](76-bai-hoc.md): Chương trình xử lý hàng loạt Batch và 5 đặc tính cốt lõi.
- [78-bai-hoc.md](78-bai-hoc.md): Trình thu gom rác tự động Garbage Collector.
- [20-bai-hoc.md](20-bai-hoc.md): Mảng nhiều chiều và đại số con trỏ trong C.

## 읽는 방법 (Cách đọc)
- Trong các câu hỏi đọc hiểu mã nguồn C của đề thi:
  - Khi thấy khai báo `struct Tag var;` $\rightarrow$ truy xuất thành viên bằng `var.member`.
  - Khi thấy khai báo con trỏ `struct Tag *p = &var;` $\rightarrow$ truy xuất thành viên bằng `p->member` (hoặc dạng tương đương `(*p).member`). Chú ý dấu ngoặc tròn `(*p)` là bắt buộc vì toán tử `.` có độ ưu tiên cao hơn toán tử giải tham chiếu `*`.
  - Nhận diện câu hỏi lý thuyết: "Cấu trúc dữ liệu gom nhóm các phần tử khác kiểu dữ liệu trong C gọi là gì?" $\rightarrow$ Chọn ngay **구조체 (struct)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Đối chiếu Mảng (Array) vs Cấu trúc (Struct):**

| Tiêu chuẩn so sánh | Mảng (배열 - Array) | Cấu trúc (구조체 - Struct) |
| :--- | :--- | :--- |
| **Bản chất kiểu dữ liệu** | Tập hợp các phần tử **đồng nhất (Homogeneous)**, cùng một kiểu dữ liệu duy nhất (ví dụ toàn bộ là `int`). | Tập hợp các thành viên **dị nhất (Heterogeneous)**, có thể mang nhiều kiểu dữ liệu khác nhau trong cùng một khối. |
| **Định danh thành viên** | Truy xuất bằng **chỉ số nguyên vị trí** (Index: `a[0], a[1]`). | Truy xuất bằng **tên định danh của thành viên** (`s.name, s.age`). |
| **Mục đích thiết kế** | Xử lý danh sách, chuỗi, ma trận số học. | Biểu diễn các đối tượng thực thể thế giới thực (Sinh viên, Nhân viên, Điểm tọa độ). |

- **2. Cú pháp khai báo và sử dụng chuẩn:**
  ```c
  #include <stdio.h>

  // Định nghĩa cấu trúc
  struct Student {
      int id;
      char grade;
      float score;
  };

  int main() {
      struct Student s1 = {101, 'A', 95.5f};
      struct Student *p = &s1; // Khai báo con trỏ trỏ tới struct

      // 1. Truy xuất bằng biến thông thường qua toán tử .
      printf("ID: %d\n", s1.id);

      // 2. Truy xuất bằng con trỏ qua toán tử ->
      printf("Grade: %c\n", p->grade);

      // 3. Dạng tương đương của p->score là (*p).score
      printf("Score: %.1f\n", (*p).score);

      return 0;
  }
  ```

- **3. Bảng quy tắc toán tử truy xuất cấu trúc:**

| Ký hiệu toán tử | Tên toán tử | Cú pháp áp dụng | Tương đương biểu thức |
| :---: | :--- | :--- | :--- |
| `.` | Direct Member Selector | `tên_biến.tên_thành_viên` | `s1.id` |
| `->` | Structure Pointer Operator | `con_trỏ->tên_thành_viên` | `(*con_trỏ).tên_thành_viên` |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Kích thước Struct và Hiện tượng căn chỉnh bộ nhớ (Memory Padding):**
  - Giả sử struct gồm: `char c;` (1B) và `int i;` (4B).
  - Về lý thuyết $1 + 4 = 5$ Byte, nhưng kích thước `sizeof(struct)` trên máy tính 32/64-bit thực tế là **8 Byte**.
  - Lý do: CPU đọc bộ nhớ theo các khối từ 4 hoặc 8 Byte (Word Alignment). Trình biên dịch sẽ tự động chèn thêm 3 Byte đệm (Padding Bytes) sau biến `c` để biến `int i` bắt đầu tại địa chỉ chia hết cho 4, giúp tối ưu hóa tốc độ bus bộ nhớ.

### 복습 체크리스트
- [ ] Phân biệt được: Mảng lưu các phần tử cùng kiểu, Struct gom các phần tử khác kiểu.
- [ ] Dùng toán tử `.` khi là biến thường, dùng toán tử `->` khi là con trỏ cấu trúc.
- [ ] Nhớ biểu thức `p->x` tương đương hoàn toàn với `(*p).x`.
- [ ] Hiểu kích thước bộ nhớ của struct có thể lớn hơn tổng số byte các thành viên do Byte Padding.
