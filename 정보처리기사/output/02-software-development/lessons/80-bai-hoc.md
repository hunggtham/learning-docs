# 28. 선형 리스트 심화: 연속 리스트 vs 연결 리스트 (Contiguous vs Linked List)

## 학습 목표 (Mục tiêu)
- Nắm vững sự phân loại và bản chất của danh sách tuyến tính (선형 리스트): Danh sách liên tục (연속 리스트 / 배열) và Danh sách liên kết (연결 리스트 / Linked List).
- Phân tích và so sánh toàn diện ưu nhược điểm giữa mảng liên tục và danh sách liên kết về hiệu suất sử dụng bộ nhớ (기억장소 이용 효율 밀도) và tốc độ thao tác (truy cập ngẫu nhiên vs chèn/xóa).
- Hiểu rõ hai trạng thái biên lỗi của cấu trúc dữ liệu: Tràn bộ nhớ (오버플로 - Overflow) và Thiếu hụt bộ nhớ (언더플로 - Underflow).

## 핵심 키워드 (Từ khóa)
- 선형 리스트 (Linear List)
- 연속 리스트 (Contiguous / Sequential List / 배열)
- 연결 리스트 (Linked List / 노드, 포인터, 링크)
- 이용 효율 밀도 (Storage Utilization Density / 밀도 = 1)
- 오버헤드 (Insertion/Deletion Overhead / 이동 오버헤드)
- 오버플로 vs 언더플로 (Overflow vs Underflow)

## 선행·연결 개념 (Kiến thức liên kết)
- [79-bai-hoc.md](79-bai-hoc.md): Định dạng dữ liệu JSON và công nghệ truyền thông AJAX.
- [81-bai-hoc.md](81-bai-hoc.md): Hệ thống quản lý cơ sở dữ liệu (DBMS).
- [01-bai-hoc.md](01-bai-hoc.md): Phân loại tổng quan cấu trúc dữ liệu tuyến tính và phi tuyến tính.

## 읽는 방법 (Cách đọc)
- Phân biệt bằng hình tượng thực tế:
  - **연속 리스트 (Contiguous / Mảng):** Giống như dãy nhà chung cư liền kề nhau số 101, 102, 103...
    - Muốn tìm nhà 105: nhảy thẳng tới chỉ số index rất nhanh ($O(1)$). Mật độ dùng ô nhớ đạt mức tuyệt đối $= 1$.
    - Muốn chèn một nhà mới vào giữa nhà 101 và 102: bắt buộc phải di chuyển dời toàn bộ các nhà phía sau lùi lại một bước $\rightarrow$ Tốn chi phí di chuyển dữ liệu ($O(n)$).
  - **연결 리스트 (Linked List):** Các ngôi nhà nằm rải rác khắp thành phố, nhưng nhà trước cầm mảnh giấy ghi địa chỉ dẫn sang nhà kế tiếp (Pointer/Link).
    - Muốn chèn/xóa: chỉ cần sửa lại địa chỉ trên mảnh giấy con trỏ, không phải di chuyển dữ liệu ai cả ($O(1)$ nếu biết vị trí).
    - Muốn tìm nhà thứ $k$: phải đi lần lượt từ đầu nhà số 1 theo con trỏ $\rightarrow$ Truy cập tuần tự chậm ($O(n)$). Tốn thêm bộ nhớ lưu con trỏ.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng so sánh chi tiết: 연속 리스트 (Mảng) vs 연결 리스트 (Linked List):**

| Tiêu chí so sánh | 연속 리스트 (Contiguous / Array) | 연결 리스트 (Linked List) |
| :--- | :--- | :--- |
| **Không gian lưu trữ** | Các ô nhớ **liên tiếp nhau** trong bộ nhớ vật lý | Các ô nhớ nằm **rải rác bất kỳ**, nối bằng con trỏ (Link) |
| **Mật độ sử dụng bộ nhớ** | **밀도 = 1** (Tối đa, không tốn thêm byte nào cho con trỏ) | **밀도 $\lt$ 1** (Tốn thêm vùng nhớ lưu con trỏ Pointer ở mỗi Node) |
| **Truy cập phần tử** | **Random Access ($O(1)$)**; truy xuất tức thì qua chỉ số Index | **Sequential Access ($O(n)$)**; phải duyệt tuần tự từ đầu Head Node |
| **Thao tác Chèn / Xóa** | **Chậm ($O(n)$)** do phải dịch chuyển hàng loạt phần tử phía sau | **Nhanh ($O(1)$)** khi đã ở vị trí; chỉ cần thay đổi liên kết con trỏ |
| **Rủi ro gián đoạn** | Không bị mất dữ liệu khi đứt con trỏ | Nếu một con trỏ trung gian bị lỗi/đứt, **không thể tìm thấy các Node tiếp theo** |

- **Hai trạng thái lỗi cơ bản trong quản trị bộ nhớ:**

| Trạng thái | Điều kiện phát sinh | Hành vi tương ứng |
| :--- | :--- | :--- |
| **오버플로 (Overflow)** | Cấu trúc dữ liệu hoặc bộ nhớ đã **đầy 100% (Full)** nhưng vẫn cố tình thực hiện thao tác chèn (Insert / Push) | Tràn bộ đệm, gây lỗi hệ thống hoặc sập chương trình |
| **언더플로 (Underflow)** | Cấu trúc dữ liệu đang **trống rỗng (Empty)** nhưng lại thực hiện thao tác xóa hoặc lấy ra (Delete / Pop) | Lỗi không có dữ liệu để xử lý |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Cấu trúc của một Node trong Danh sách liên kết:**
  - Mỗi Node gồm 2 trường: Trường dữ liệu (Data Field) lưu giá trị thực tế, và Trường liên kết (Link Field) lưu địa chỉ vùng nhớ của Node kế tiếp.
  - Các biến thể nâng cao:
    - **단일 연결 리스트 (Singly Linked List):** Con trỏ chỉ đi 1 chiều về phía sau.
    - **이중 연결 리스트 (Doubly Linked List):** Mỗi Node có 2 con trỏ: `Prev` (chỉ nút trước) và `Next` (chỉ nút sau), cho phép duyệt 2 chiều.
    - **원형 연결 리스트 (Circular Linked List):** Con trỏ của Node cuối cùng trỏ ngược lại Node đầu tiên (Head).

### 복습 체크리스트
- [ ] Nhớ 연속 리스트 có mật độ sử dụng bộ nhớ bằng 1 (기억장소 이용 효율 밀도 = 1).
- [ ] Nhớ 연속 리스트 truy cập nhanh $O(1)$ nhưng chèn/xóa chậm $O(n)$ do phải dịch chuyển dữ liệu.
- [ ] Nhớ 연결 리스트 chèn/xóa nhanh bằng cách đổi con trỏ nhưng truy cập ngẫu nhiên chậm.
- [ ] Phân biệt được Overflow (chèn vào danh sách đầy) và Underflow (xóa khỏi danh sách rỗng).
