# 메모리 관리 (Memory Management)

## 학습 목표 (Mục tiêu)
- Phân biệt 3 chiến lược nạp và bố trí bộ nhớ chính (배치 전략 - Placement Strategies): First Fit (최초 적합), Best Fit (최적 적합), và Worst Fit (최악 적합).
- Hiểu rõ nguyên lý hoạt động của hai kỹ thuật quản lý bộ nhớ ảo kinh điển: Phân trang (페이징 - Paging) và Phân đoạn (세그멘테이션 - Segmentation).
- Phân biệt chính xác bản chất phát sinh của Phân mảnh nội vi (내부 단편화) và Phân mảnh ngoại vi (외부 단편화) trong hai mô hình bộ nhớ ảo.

## 핵심 키워드 (Từ khóa)
- **배치 전략 (Placement Strategies)**: 최초 적합 (First Fit - nhanh nhất), 최적 적합 (Best Fit - mảnh vụn nhỏ nhất), 최악 적합 (Worst Fit - mảnh thừa lớn nhất).
- **페이징 (Paging)**: Kích thước khối cố định bằng nhau (Page vs Page Frame), bảng Page Table, chỉ phát sinh 내부 단편화 (Internal Fragmentation).
- **세그멘테이션 (Segmentation)**: Kích thước biến thiên theo đơn vị logic (Hàm, Module), bảng Segment Table (Base, Limit), chỉ phát sinh 외부 단편화 (External Fragmentation).
- **단편화 (Fragmentation)**: Lãng phí không gian bộ nhớ do việc cấp phát không lấp đầy ô nhớ.

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [60-bai-hoc.md](60-bai-hoc.md) (Thuật toán thay thế trang và kích thước Page).
- Liên kết với [61-bai-hoc.md](61-bai-hoc.md) (Hiện tượng Locality, Working Set và Thrashing).
- Liên kết với [04-programming-language/85-bai-hoc.md](../../04-programming-language/lessons/85-bai-hoc.md) (Mô hình bộ nhớ ảo trong hệ điều hành).

## 읽는 방법 (Cách đọc)
- Mẹo ghi nhớ đề thi không bao giờ nhầm lẫn:
  - **Paging (Trang cố định)**: Chia đều chằn chặn $\rightarrow$ Thừa một mẩu ở cuối trang cuối cùng $\rightarrow$ Lỗi **Bên trong (내부 단편화)**.
  - **Segmentation (Đoạn logic to nhỏ khác nhau)**: Xếp các đoạn so le trên RAM $\rightarrow$ Thừa các khe hở lổn nhổn ở giữa $\rightarrow$ Lỗi **Bên ngoài (외부 단편화)**.
  - Chiến lược nạp: Nhanh nhất là **First Fit**; mảnh thừa nhỏ nhất là **Best Fit**; mảnh thừa lớn nhất là **Worst Fit**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Ba chiến lược bố trí bộ nhớ (Placement Strategies)
| Chiến lược (KR / EN) | Cơ chế lựa chọn vùng nhớ trống | Ưu điểm cốt lõi | Nhược điểm chí mạng |
| :--- | :--- | :--- | :--- |
| **최초 적합 (First Fit)** | Duyệt từ đầu danh sách bộ nhớ và nạp ngay vào **vùng trống đầu tiên** có kích thước đủ lớn | **Tốc độ tìm kiếm nhanh nhất**, chi phí thuật toán thấp | Có thể để lại nhiều mảnh vụn nhỏ ở phần đầu bộ nhớ |
| **최적 적합 (Best Fit)** | Quét toàn bộ bộ nhớ và nạp vào vùng trống có kích thước **vừa khít nhất** (chênh lệch nhỏ nhất) | Tận dụng tối đa các vùng trống có kích thước sát với tiến trình | Quá trình tìm kiếm chậm; sinh ra các **mảnh vụn siêu nhỏ** không thể tái sử dụng |
| **최악 적합 (Worst Fit)** | Quét toàn bộ bộ nhớ và nạp vào vùng trống có kích thước **lớn nhất** hiện có | Mảnh đất trống còn thừa lại sau khi nạp vẫn đủ lớn để chứa tiến trình khác | Làm cạn kiệt nhanh chóng các khối bộ nhớ lớn dự phòng cho các tác vụ nặng |

#### 2. So sánh chi tiết hai kỹ thuật Bộ nhớ ảo: Paging vs Segmentation
| Tiêu chí kỹ thuật | 페이징 기법 (Paging) | 세그멘테이션 기법 (Segmentation) |
| :--- | :--- | :--- |
| **Đơn vị phân chia** | Phân chia vật lý thành các khối có **kích thước cố định bằng nhau** | Phân chia logic theo cấu trúc chương trình thành các khối có **kích thước biến thiên khác nhau** |
| **Thuật ngữ phân vùng** | - Chương trình: **페이지 (Page)** / - Bộ nhớ RAM: **페이지 프레임 (Page Frame)** | - Chương trình: **세그먼트 (Segment)** (Hàm `main`, Mảng dữ liệu, Ngăn xếp Stack) |
| **Bảng ánh xạ địa chỉ** | **Page Map Table** (Ánh xạ số trang $\rightarrow$ số khung trang) | **Segment Map Table** (Gồm địa chỉ cơ sở `Base` và độ dài giới hạn `Limit`) |
| **Hiện tượng phân mảnh** | **Chỉ phát sinh phân mảnh nội vi (내부 단편화)** ở trang cuối; hoàn toàn không có phân mảnh ngoại vi | **Chỉ phát sinh phân mảnh ngoại vi (외부 단편화)** giữa các đoạn; hoàn toàn không có phân mảnh nội vi |
| **Ưu điểm lớn nhất** | Quản lý bộ nhớ đơn giản, không cần gom cụm dồn bộ nhớ (Compaction) | Thuận tiện cho việc chia sẻ mã nguồn (Sharing) và bảo vệ phân quyền (Protection) |

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Bài toán tính phân mảnh nội vi trong Paging
- *Đề bài*: Kích thước của một Page trong hệ thống là $4\text{ KB}$ ($4096\text{ bytes}$). Một tiến trình có dung lượng là $10\text{ KB}$ ($10240\text{ bytes}$) được nạp vào bộ nhớ. Hỏi hệ thống cần bao nhiêu trang và độ lãng phí do phân mảnh nội vi là bao nhiêu?
- *Lời giải*:
  - Số trang cần cấp phát: $\lceil 10\text{ KB} / 4\text{ KB} \rceil = 3$ trang.
  - Tổng dung lượng bộ nhớ được cấp cho 3 trang: $3 \times 4\text{ KB} = 12\text{ KB}$.
  - Phân mảnh nội vi phát sinh ở trang thứ 3: $12\text{ KB} - 10\text{ KB} = 2\text{ KB}$ ($2048\text{ bytes}$).

#### 2. Kỹ thuật dịch địa chỉ trong Segmentation
```
Địa chỉ logic: [Segment Number (s) | Offset (d)]
                      │
                      ▼ (Tra cứu bảng Segment Table)
           ┌──────────┴──────────┐
           ▼                     ▼
     [Limit (Độ dài)]      [Base (Địa chỉ cơ sở)]
           │                     │
      Kiểm tra d < Limit ?       │
           │ (Hợp lệ)            │
           ▼                     ▼
        [Cộng] ◄─────────────────┘
           │
           ▼
     Địa chỉ vật lý: Base + d
```
- Nếu chỉ số `d >= Limit`: Phần cứng CPU lập tức phát tín hiệu ngắt báo lỗi xâm phạm vùng nhớ bất hợp pháp (**Segment Violation Trap**).

---

### 복습 체크리스트
- [ ] Trong 3 chiến lược bố trí bộ nhớ (First Fit, Best Fit, Worst Fit), chiến lược nào có tốc độ nạp nhanh nhất?
- [ ] Kỹ thuật Paging chia chương trình thành các đơn vị có kích thước cố định hay biến thiên?
- [ ] Phân mảnh nội vi (내부 단편화) phát sinh trong kỹ thuật Paging hay Segmentation?
- [ ] Bảng ánh xạ Segment Table chứa hai thông số kỹ thuật cốt lõi nào cho mỗi phân đoạn?
