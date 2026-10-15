# 프로젝트 일정 관리 (Project Schedule Management)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, cơ chế vận hành và trường hợp ứng dụng của 3 công cụ quản lý tiến độ dự án kinh điển: **Sơ đồ mạng PERT**, **Phương pháp đường găng CPM**, và **Biểu đồ thanh Gantt Chart**.
- Thuộc lòng công thức tính thời gian kỳ vọng trung bình 3 điểm trong PERT: $t_e = \frac{O + 4M + P}{6}$ (với $O$ là Lạc quan, $M$ là Kỳ vọng nhất, $P$ là Bi quan).
- Thấu hiểu định nghĩa và ý nghĩa cốt tử của **Đường găng (임계 경로 - Critical Path)**: Là đường đi dài nhất trong sơ đồ mạng dự án, quyết định tổng thời gian hoàn thành tối thiểu của toàn bộ dự án.

## 핵심 키워드 (Từ khóa)
- 프로젝트 일정 관리 (Project Schedule Management)
- PERT (Program Evaluation and Review Technique - 3점 추정)
- 기대치 계산 공식 ($t_e = (O + 4M + P) / 6$)
- CPM (Critical Path Method - 임계 경로 기법)
- 임계 경로 (Critical Path - 최장 경로, 여유 시간 0)
- 임계 작업 (Critical Activities)
- 간트 차트 (Gantt Chart - 막대 도표, 마일스톤)

## 선행·연결 개념 (Kiến thức liên kết)
- [06-bai-hoc.md](06-bai-hoc.md): Quản lý dự án phần mềm và công thức tính Man-Month theo LOC.
- [08-bai-hoc.md](08-bai-hoc.md): Các mô hình toán học ước tính chi phí phần mềm (COCOMO, Putnam, FP).
- [09-bai-hoc.md](09-bai-hoc.md): Chuyên sâu về kỹ thuật ước lượng toán học COCOMO và FP.

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh giữa PERT và CPM:
  - **PERT:** Dùng cho dự án **chưa từng có tiền lệ trong quá khứ**, thời gian mang tính xác suất biến động $\rightarrow$ Ước tính 3 điểm (Lạc quan, Khả thi, Bi quan).
  - **CPM:** Dùng cho dự án **đã có kinh nghiệm và dữ liệu lịch sử**, thời gian mang tính xác định.
  - **Đường găng (Critical Path):** Trong đề thi luôn hỏi: "Đường găng trong sơ đồ CPM là gì?" $\rightarrow$ Luôn chọn đáp án **"Đường đi có tổng thời gian dài nhất từ điểm bắt đầu đến điểm kết thúc (네트워크에서 가장 긴 경로)"**.
  - **Gantt Chart:** Dạng biểu đồ thanh ngang, dễ nhìn mốc thời gian (**Milestone**), nhưng yếu trong việc thể hiện quan hệ phụ thuộc logic.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng so sánh toàn diện PERT vs CPM vs Gantt Chart:**

| Tiêu chuẩn so sánh | PERT (3점 추정법) | CPM (임계 경로 기법) | 간트 차트 (Gantt Chart) |
| :--- | :--- | :--- | :--- |
| **Bản chất thời gian** | **Xác suất (Probabilistic):** Không chắc chắn, chưa có kinh nghiệm quá khứ (R&D). | **Xác định (Deterministic):** Đã có kinh nghiệm và định mức thời gian chuẩn. | Lập lịch trực quan theo dòng thời gian thực (Lịch dương lịch). |
| **Phương pháp ước tính** | Đánh giá 3 giá trị: Lạc quan ($O$), Khả thi nhất ($M$), Bi quan ($P$). | Tính toán thời gian bắt đầu/kết thúc sớm nhất và muộn nhất cho từng nút. | Biểu diễn bằng các thanh ngang (Bar Chart); độ dài thanh thể hiện thời lượng. |
| **Trọng tâm quản trị** | Giảm thiểu độ rủi ro bất định của thời gian kết thúc dự án. | Tìm ra **Đường găng (Critical Path)** để tập trung kiểm soát tài nguyên. | Theo dõi tiến độ hàng ngày và các cột mốc kiểm tra (**Milestones**). |
| **Hạn chế lớn nhất** | Khó đánh giá chính xác các tham số phân phối xác suất beta. | Không thể hiện tốt yếu tố rủi ro và bất định. | Khó thể hiện mối quan hệ phụ thuộc phức tạp giữa các công việc đan xen nhau. |

- **2. Công thức ước tính thời gian trung bình trong PERT:**

$$t_e = \frac{O + 4M + P}{6}$$

| Ký hiệu | Ý nghĩa tham số | Tên tiếng Hàn tương ứng |
| :---: | :--- | :--- |
| **$O$** | Thời gian lạc quan nhất (Optimistic) khi mọi việc diễn ra hoàn hảo | **낙관치** |
| **$M$** | Thời gian có khả năng xảy ra cao nhất trong điều kiện bình thường | **기대치 (최빈치)** |
| **$P$** | Thời gian bi quan nhất (Pessimistic) khi mọi sự cố bất lợi xảy ra | **비관치** |
| **$t_e$** | Thời gian kỳ vọng trung bình có trọng số (Expected Duration) | **예측치** |

- **3. Đặc tính cốt tử của Đường găng (Critical Path - 임계 경로):**
  - Là chuỗi liên kết các công việc từ đầu đến cuối dự án có **tổng thời gian thực hiện LỚN NHẤT**.
  - Tổng thời gian của đường găng chính là **thời gian ngắn nhất cần thiết để hoàn thành toàn bộ dự án**.
  - Thời gian dự trữ (Float / Slack Time) của tất cả các công việc trên đường găng đều **bằng 0**.
  - Bất kỳ sự chậm trễ nào dù chỉ 1 ngày của một công việc trên đường găng cũng sẽ khiến **toàn bộ dự án bị chậm trễ đúng 1 ngày**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Bài toán ví dụ tính toán PERT và CPM trong đề thi:**
  - *Ví dụ PERT:* Công việc $A$ có thời gian lạc quan $O = 2$ ngày, kỳ vọng nhất $M = 5$ ngày, bi quan $P = 14$ ngày. Tính thời gian dự tính $t_e$?
    $$t_e = \frac{2 + 4 \times 5 + 14}{6} = \frac{36}{6} = 6 \text{ ngày}$$
  - *Ví dụ CPM:* Dự án có 3 đường đi độc lập:
    - Đường 1: $1 \rightarrow 2 \rightarrow 5$ (Thời gian: $3 + 4 = 7$ ngày).
    - Đường 2: $1 \rightarrow 3 \rightarrow 5$ (Thời gian: $2 + 8 = 10$ ngày).
    - Đường 3: $1 \rightarrow 4 \rightarrow 5$ (Thời gian: $4 + 2 = 6$ ngày).
    $\rightarrow$ **Đường găng là Đường 2** vì có tổng thời gian lớn nhất ($10$ ngày). Thời gian hoàn thành dự án tối thiểu là $10$ ngày.

### 복습 체크리스트
- [ ] Thuộc lòng công thức PERT: $t_e = \frac{O + 4M + P}{6}$.
- [ ] Nhớ định nghĩa đường găng CPM: Là đường đi có tổng thời gian lớn nhất trong mạng lưới.
- [ ] Ghi nhớ thời gian dự trữ (Slack Time) trên đường găng luôn bằng 0.
- [ ] Nhớ biểu đồ Gantt thể hiện bằng các thanh ngang, rất mạnh về Milestone nhưng yếu về mối phụ thuộc.
