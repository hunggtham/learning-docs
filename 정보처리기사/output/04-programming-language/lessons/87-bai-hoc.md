# 284 & 294. 구역성 (Locality / Tính cục bộ)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, cơ sở lý thuyết và tầm quan trọng của nguyên lý tính cục bộ (구역성 / 국부성 - Locality of Reference do Peter Denning đề xuất) trong kiến trúc máy tính và hệ điều hành.
- Phân biệt sự khác biệt bản chất kỹ thuật giữa Tính cục bộ thời gian (시간 구역성 - Temporal Locality) và Tính cục bộ không gian (공간 구역성 - Spatial Locality).
- Nhận diện chính xác các cấu trúc mã nguồn điển hình tương ứng với từng loại cục bộ (vòng lặp, biến đếm, mảng tuần tự, ngăn xếp Stack).

## 핵심 키워드 (Từ khóa)
- 구역성 / 국부성 (Locality of Reference - Peter Denning)
- 시간 구역성 (Temporal Locality - Thời gian)
- 공간 구역성 (Spatial Locality - Không gian)
- 캐시 기억장치 원 lý (Cache Memory Principle)
- 워킹 셋 이론적 기초 (Theoretical Foundation of Working Set)
- 루프와 카운터 변수 (Loops & Counter Variables)
- 배열 순차 참조 (Array Sequential Traversal)

## 선행·연결 개념 (Kiến thức liên kết)
- [86-bai-hoc.md](86-bai-hoc.md): Trình thông dịch Interpreter và đặc trưng thực thi.
- [88-bai-hoc.md](88-bai-hoc.md): Mô hình Tập làm việc Working Set phòng ngừa Thrashing.
- [73-bai-hoc.md](73-bai-hoc.md): Thuật toán thay thế trang nhớ trong bộ nhớ ảo.

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh trong các câu hỏi phân loại của đề thi:
  - **시간 구역성 (Temporal Locality):** Gắn liền với khái niệm **"DÙNG LẠI CHÍNH NÓ NHIỀU LẦN"**. Nhận diện qua các từ khóa: Vòng lặp (`Loop`, `for`, `while`), Biến đếm (`Counter`), Biến tích lũy tổng (`Sum`), Hàm con được gọi liên tục.
  - **공간 구역성 (Spatial Locality):** Gắn liền với khái niệm **"DÙNG CÁC Ô NHỚ NẰM SÁT CẠNH NHAU"**. Nhận diện qua các từ khóa: Mảng một chiều (`Array`), Khối lệnh tuần tự (`Sequential Code`), Bảng dữ liệu (`Table`), Ngăn xếp (`Stack`).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Định nghĩa và ứng dụng của Locality (구역성):**
  - Là hiện tượng một tiến trình trong quá trình thực thi không truy xuất ngẫu nhiên đồng đều trên toàn bộ không gian địa chỉ bộ nhớ, mà có xu hướng **chỉ tập trung tham chiếu vào một phân vùng bộ nhớ cục bộ nhất định** trong một khoảng thời gian cụ thể.
  - Là nền tảng lý thuyết sống còn để:
    - Thiết kế hệ thống bộ nhớ đệm tốc độ cao (**Cache Memory**).
    - Xây dựng mô hình trang hoạt động (**Working Set**) nhằm ngăn chặn hiện tượng quá tải hoán đổi trang (Thrashing) trong bộ nhớ ảo.

- **2. Bảng đối chiếu chi tiết: Temporal Locality vs Spatial Locality:**

| Tiêu chuẩn so sánh | 시간 구역성 (Temporal Locality - Thời gian) | 공간 구역성 (Spatial Locality - Không gian) |
| :--- | :--- | :--- |
| **Bản chất nguyên lý** | Nếu một ô nhớ vừa được truy xuất tại thời điểm này, thì **chính ô nhớ đó có khả năng rất cao sẽ được truy xuất lặp lại nhiều lần nữa** trong tương lai gần. | Nếu một ô nhớ vừa được truy xuất, thì **các ô nhớ nằm liền kề sát cạnh nó trong không gian địa chỉ** có khả năng rất cao sẽ được truy xuất tiếp theo. |
| **Cấu trúc mã nguồn đại diện** | Thân các vòng lặp (`for`, `while`); Các biến đếm bước lặp (`i, j, count`); Biến tích lũy tổng (`sum += a`); Các hàm tiện ích con được gọi lặp lại. | Duyệt tuần tự các phần tử của mảng một chiều (`a[0], a[1], a[2]...`); Khối lệnh thực thi tuần tự từ trên xuống; Thao tác đẩy/rút trên đỉnh ngăn xếp (`Stack`). |
| **Ứng dụng phần cứng** | Lưu trữ dữ liệu và biến nóng vào thanh ghi CPU hoặc Cache L1/L2. | Nạp cả một khối dữ liệu liên tục (Cache Line / Memory Block 64 Bytes) từ RAM vào Cache mỗi khi có truy xuất. |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tối ưu hóa mã nguồn theo Spatial Locality trong mảng 2 chiều:**
  - Trong ngôn ngữ C, mảng hai chiều được tổ chức lưu trữ trên RAM theo thứ tự **Hàng trước (Row-Major Order)**: Các phần tử của cùng một hàng nằm liên tiếp nhau.
  - Do đó duyệt mảng theo thứ tự hàng `for(i) { for(j) { a[i][j]... } }` sẽ kích hoạt Spatial Locality tối đa và đạt tỷ lệ Cache Hit cực cao.
  - Ngược lại nếu duyệt theo cột `a[j][i]`, mỗi bước nhảy sẽ cách nhau một khoảng cách xa trên RAM, gây trượt bộ đệm Cache Miss liên tục và làm giảm hiệu năng thực thi nghiêm trọng.

### 복습 체크리스트
- [ ] Ghi nhớ Peter Denning là nhà khoa học đề xuất nguyên lý tính cục bộ (Locality).
- [ ] Nhớ Temporal Locality gắn với vòng lặp, biến đếm (dùng lại ô nhớ cũ).
- [ ] Nhớ Spatial Locality gắn với duyệt mảng, khối lệnh tuần tự (dùng ô nhớ lân cận).
- [ ] Hiểu nguyên lý nạp Cache Line tận dụng tính cục bộ không gian để tăng tốc độ máy tính.
