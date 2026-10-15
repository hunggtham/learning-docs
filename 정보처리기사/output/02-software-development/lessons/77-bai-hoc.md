# 23. EAI 구축 유형 (Enterprise Application Integration Types)

## 학습 목표 (Mục tiêu)
- Nắm vững khái niệm và mục tiêu của tích hợp ứng dụng doanh nghiệp (EAI - Enterprise Application Integration): kết nối và đồng bộ dữ liệu giữa các hệ thống phần mềm dị thể trong tổ chức.
- Phân biệt rõ ràng 4 mô hình kiến trúc EAI kinh điển trong đề thi: Điểm - Điểm (Point-to-Point), Trục - Nan hoa (Hub & Spoke), Trục thông điệp (Message Bus), và Hỗn hợp (Hybrid).
- Phân tích ưu và nhược điểm của từng mô hình về khả năng mở rộng, chi phí triển khai và độ phức tạp khi kết nối nhiều ứng dụng.

## 핵심 키워드 (Từ khóa)
- EAI (Enterprise Application Integration / 기업 애플리케이션 통합)
- Point-to-Point (1:1 직접 연결 / $N(N-1)/2$ 연결선)
- Hub & Spoke (단일 접점 / 중앙 집중형 허브 / 단일 장애점 병목)
- Message Bus (미들웨어 버스 / ESB 방식 / 확장성 우수)
- Hybrid (Hub & Spoke + Message Bus 결합 / 그룹 내 Hub, 그룹 간 Bus)
- 미들웨어 (Middleware)

## 선행·연결 개념 (Kiến thức liên kết)
- [76-bai-hoc.md](76-bai-hoc.md): Các công cụ phân tích tĩnh kiểm tra chất lượng mã nguồn.
- [78-bai-hoc.md](78-bai-hoc.md): Công cụ kiểm tra tính toàn vẹn hệ thống Tripwire.
- [정보처리기사/output/01-software-design/lessons/24-bai-hoc.md](../../01-software-design/lessons/24-bai-hoc.md): Kiến trúc phần mềm và hệ thống hướng dịch vụ (SOA).

## 읽는 방법 (Cách đọc)
- Nhớ hình thái kiến trúc của 4 kiểu EAI:
  - **Point-to-Point:** Mỗi ứng dụng nối dây trực tiếp 1:1 với tất cả ứng dụng khác $\rightarrow$ Khi số ứng dụng $N$ tăng, số kết nối tăng chóng mặt theo công thức $N(N-1)/2$.
  - **Hub & Spoke:** Tất cả ứng dụng nối về 1 máy chủ trung tâm (Hub) duy nhất $\rightarrow$ Rất dễ quản lý nhưng nếu Hub sập thì cả hệ thống tê liệt (Single Point of Failure - SPOF).
  - **Message Bus:** Các ứng dụng cắm vào một đường ống trục thông điệp chung (Bus) thông qua adapter $\rightarrow$ Giảm tải, mở rộng linh hoạt.
  - **Hybrid:** Kết hợp hai mô hình: bên trong nội bộ từng cụm/chi nhánh dùng Hub & Spoke, giữa các cụm lớn liên kết với nhau bằng Message Bus.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng so sánh 4 mô hình kiến trúc EAI:**

| Mô hình EAI | Cơ chế kết nối | Ưu điểm cốt lõi | Nhược điểm (Bẫy đề thi) |
| :--- | :--- | :--- | :--- |
| **Point-to-Point** | Kết nối trực tiếp 1:1 giữa từng cặp ứng dụng | Rất đơn giản khi hệ thống chỉ có 2 hoặc 3 ứng dụng | Khi số hệ thống tăng, số kết nối bùng nổ theo cấp số nhân $\frac{N(N-1)}{2}$; cực kỳ khó bảo trì |
| **Hub & Spoke** | Mọi hệ thống kết nối tập trung về một điểm tiếp xúc duy nhất là **Hub trung tâm (중앙 집중형)** | Dễ dàng quản lý dữ liệu, kiểm soát bảo mật và mở rộng thêm chi nhánh mới | **Điểm lỗi đơn (SPOF - Single Point of Failure)**; nếu Hub gặp sự cố hoặc quá tải thì toàn hệ thống ngừng trệ |
| **Message Bus (ESB)** | Các ứng dụng liên lạc thông qua một đường **trục trung gian (미들웨어 버스)** dùng bộ đệm thông điệp | Khả năng mở rộng tuyệt vời, xử lý dữ liệu lớn, liên lạc bất đồng bộ tin cậy | Chi phí mua sắm middleware và thiết kế cấu trúc ban đầu cao |
| **Hybrid** | Kết hợp mô hình: Bên trong từng nhóm là **Hub & Spoke**, giữa các nhóm liên kết bằng **Message Bus** | Tận dụng sự linh hoạt của Hub trong nội bộ và khả năng mở rộng của Bus giữa các phân vùng lớn | Đòi hỏi đội ngũ kỹ thuật trình độ cao để tích hợp hai cơ chế song song |

- **Công thức số lượng kết nối của Point-to-Point:**
  $$\text{Số kết nối} = \frac{N(N-1)}{2}$$
  - Với 10 hệ thống: $\frac{10 \times 9}{2} = 45$ đường nối trực tiếp.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Sự chuyển dịch từ EAI sang ESB (Enterprise Service Bus):**
  - EAI truyền thống tập trung chủ yếu vào Hub & Spoke để chuyển đổi dữ liệu và đồng bộ định dạng giữa các phần mềm độc quyền.
  - ESB nâng cấp mô hình Message Bus lên tầm kiến trúc hướng dịch vụ (SOA), chuẩn hóa giao tiếp thông qua Web Services (SOAP, REST) và định dạng mở XML/JSON.

### 복습 체크리스트
- [ ] Kể tên đúng 4 loại EAI: Point-to-Point, Hub & Spoke, Message Bus, Hybrid.
- [ ] Nhớ nhược điểm SPOF của Hub & Spoke khi Hub trung tâm gặp sự cố.
- [ ] Tính được số kết nối $N(N-1)/2$ của mô hình Point-to-Point.
- [ ] Hiểu cấu trúc của Hybrid: nội bộ cụm là Hub & Spoke, liên cụm là Message Bus.
