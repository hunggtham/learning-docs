# 프로세스 동작 특성 (Đặc tính Hoạt động của Tiến trình: Locality, Working Set, Thrashing)

## 학습 목표 (Mục tiêu)
- Phân biệt bản chất của hai dạng tính cục bộ tham chiếu bộ nhớ: Cục bộ thời gian (시간 구역성 - Temporal Locality) và Cục bộ không gian (공간 구역성 - Spatial Locality).
- Nắm vững mô hình tập làm việc (Working Set) của Peter Denning và vai trò của việc duy trì Working Set trong việc giảm lỗi thiếu trang.
- Hiểu rõ nguyên nhân phát sinh hiện tượng nghẽn hoán đổi trang (Thrashing) và các giải pháp ngăn chặn (kiểm soát mức độ đa chương, thuật toán tần số lỗi trang PFF).

## 핵심 키워드 (Từ khóa)
- **Locality (국부성/구역성)**: Xu hướng tham chiếu tập trung vào vùng nhớ hạn chế (Denning đề xuất).
- **시간 구역성 (Temporal Locality)**: Dùng lại vị trí vừa dùng (vòng lặp for, biến đếm, stack).
- **공간 구역성 (Spatial Locality)**: Dùng các vị trí nằm liền kề kế bên (mảng tuần tự, lệnh kế tiếp).
- **워킹 셋 (Working Set)**: Tập hợp các trang thường xuyên được tham chiếu trong cửa sổ thời gian $\Delta$.
- **스래싱 (Thrashing)**: Thời gian tráo trang trên đĩa lớn hơn thời gian thực thi CPU $\rightarrow$ sập hiệu năng.
- **PFF (Page Fault Frequency)**: Điều chỉnh cấp phát khung trang dựa trên ngưỡng lỗi trang trên và dưới.

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [59-bai-hoc.md](59-bai-hoc.md) (Quản lý bộ nhớ ảo và Paging).
- Liên kết với [60-bai-hoc.md](60-bai-hoc.md) (Thuật toán thay thế trang).
- Liên kết với [04-programming-language/85-bai-hoc.md](../../04-programming-language/lessons/85-bai-hoc.md) (Locality và Working Set chi tiết).

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh câu hỏi trắc nghiệm:
  - Xuất hiện từ khóa: "Vòng lặp (for/while)", "Biến đếm (Counter)", "Ngăn xếp (Stack)", "Chương trình con gọi lại" $\rightarrow$ **시간 구역성 (Temporal Locality)**.
  - Xuất hiện từ khóa: "Mảng tuần tự (Array)", "Lệnh thực hiện kế tiếp nhau", "Bảng dữ liệu" $\rightarrow$ **공간 구역성 (Spatial Locality)**.
  - Hiện tượng: "Máy tính bận rộn đọc ghi đĩa liên tục khiến CPU rảnh rỗi và hệ thống bị đơ" $\rightarrow$ **Thrashing (스래싱)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Tính cục bộ tham chiếu (Locality / 국부성)
| Loại tính cục bộ (KR / EN) | Khái niệm bản chất | Cấu trúc chương trình tiêu biểu |
| :--- | :--- | :--- |
| **시간 구역성 / (Temporal Locality)** | Một ô nhớ vừa mới được truy xuất thì có khả năng rất cao sẽ được **truy xuất lặp lại nhiều lần** trong tương lai gần | - Các cấu trúc vòng lặp lặp lại (`for`, `while`) / - Biến đếm số lần (Counter/Accumulator) / - Đỉnh ngăn xếp (Top of Stack) / - Các hàm gọi đệ quy (Recursion) |
| **공간 구역성 / (Spatial Locality)** | Một ô nhớ được truy xuất thì các ô nhớ **nằm ngay liền kề sát cạnh nó** cũng có xu hướng được truy xuất tiếp theo | - Duyệt mảng tuần tự một chiều hoặc hai chiều (`arr[i]` rồi `arr[i+1]`) / - Các dòng lệnh nằm nối tiếp nhau trong mã nguồn tuần tự / - Duyệt danh sách bản ghi trong bảng |

#### 2. Mô hình Tập làm việc (Working Set)
- **Định nghĩa**: Khái niệm do nhà khoa học máy tính Peter Denning đưa ra. Working Set là **tập hợp tất cả các trang bộ nhớ mà tiến trình thực sự tham chiếu thường xuyên** trong một cửa sổ thời gian quan sát nhất định (Working Set Window $\Delta$).
- **Đặc điểm**:
  - Kích thước và thành phần của Working Set biến đổi động liên tục theo thời gian thực thi của tiến trình.
  - **Quy tắc an toàn**: Nếu hệ điều hành cấp đủ số khung trang trên RAM để chứa trọn vẹn Working Set của tiến trình, tỷ lệ lỗi thiếu trang (Page Fault Rate) sẽ giảm xuống mức rất thấp, tiến trình chạy mượt mà.

#### 3. Hiện tượng Thrashing (Trì trệ do hoán đổi trang)
- **Khái niệm**: Hiện tượng hệ điều hành dành phần lớn thời gian và tài nguyên CPU chỉ để phục vụ việc hoán đổi nạp trang ra vào giữa ổ đĩa và RAM (Paging I/O), trong khi thời gian thực thi các lệnh chương trình hữu ích giảm gần bằng 0.
- **Nguyên nhân cốt lõi**:
  - **Mức độ đa chương trình (Degree of Multiprogramming) quá cao**: Hệ thống cố nạp quá nhiều tiến trình cùng lúc vào RAM, khiến tổng số trang cần thiết vượt xa dung lượng RAM vật lý. Mỗi tiến trình không được cấp đủ khung trang để giữ Working Set của nó.
- **Biện pháp phòng ngừa và khắc phục**:
  - **Giảm mức độ đa chương**: Tạm dừng hoặc hoán đổi bớt (Swap-out) một số tiến trình ra đĩa để giải phóng RAM cho các tiến trình còn lại.
  - **Thuật toán PFF (Page Fault Frequency - Tần số lỗi trang)**:
    - Thiết lập một ngưỡng trên (Upper Bound) và một ngưỡng dưới (Lower Bound) cho tần số lỗi trang của từng tiến trình.
    - Nếu tần số lỗi trang của tiến trình vượt ngưỡng trên: Cấp thêm khung trang RAM cho tiến trình đó.
    - Nếu tần số lỗi trang thấp hơn ngưỡng dưới: Thu hồi bớt các khung trang thừa của tiến trình đó để chia sẻ cho tiến trình khác.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Đồ thị mối quan hệ giữa Mức độ đa chương và Hiệu suất CPU
```
Hiệu suất CPU (%)
      ▲
      │                 [Điểm tối ưu]
 100% │                     ▲
      │                    / \
      │                   /   \
      │                  /     \
      │                 /       \   ◄─── HIỆN TƯỢNG THRASHING
      │                /         \       (Hiệu suất sụt giảm dốc đứng)
      │               /           \
      │              /             \
      └─────────────┴───────────────┴──────────────► Mức độ đa chương
               (Ít tiến trình)   (Quá tải RAM)
```

---

### 복습 체크리스트
- [ ] Sự khác biệt then chốt giữa Cục bộ thời gian (Temporal) và Cục bộ không gian (Spatial) là gì?
- [ ] Vòng lặp `for(int i=0; i<100; i++) sum += i;` thể hiện rõ nét tính chất cục bộ nào?
- [ ] Hiện tượng Thrashing xảy ra khi thời gian xử lý nào vượt trội hơn thời gian thực thi CPU?
- [ ] Cơ chế PFF (Page Fault Frequency) kiểm soát việc cấp phát khung trang dựa trên những tiêu chí nào?
