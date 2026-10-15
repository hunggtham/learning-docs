# 5. 네트워크 및 인프라 기술 (Công nghệ Mạng & Hạ tầng)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, kiến trúc phân tầng và lợi ích vận hành của các công nghệ hạ tầng định nghĩa bằng phần mềm (**SDE - Software-Defined Everything**): **SDN**, **SDS**, và **SDDC**.
- Phân biệt sự khác nhau giữa công nghệ Mạng định nghĩa bằng phần mềm (**SDN**) và Ảo hóa chức năng mạng (**NFV - Network Functions Virtualization**).
- Thuộc lòng 3 mô hình dịch vụ điện toán đám mây kinh điển (**IaaS**, **PaaS**, **SaaS**) và phạm vi trách nhiệm quản trị giữa nhà cung cấp dịch vụ đám mây với khách hàng.

## 핵심 키워드 (Từ khóa)
- 네트워크 인프라 기술 (Network Infrastructure Technologies)
- SDN (Software-Defined Networking - 제어와 데이터 분리)
- SDS (Software-Defined Storage - 스토리지 풀 가상화)
- SDDC (Software-Defined Data Center - 데이터센터 전면 가상화)
- NFV (Network Functions Virtualization - 네트워크 기능 가상화)
- 클라우드 컴퓨팅 3대 서비스 모델 (IaaS, PaaS, SaaS)
- 오픈플로우 (OpenFlow 프로토콜)

## 선행·연결 개념 (Kiến thức liên kết)
- [17-bai-hoc.md](17-bai-hoc.md): Lỗi quản lý tài nguyên hệ thống và con trỏ lơ lửng.
- [19-bai-hoc.md](19-bai-hoc.md): Các thiết bị phần cứng mạng viễn thông (Hub, Switch, Router).
- [20-bai-hoc.md](20-bai-hoc.md): Cấu trúc hình học mạng (Topologies) và các chuẩn IEEE 802.

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh trong các câu hỏi đề thi:
  - **SDN:** Nhớ từ khóa then chốt **"Tách rời Control Plane (Mặt phẳng điều khiển) và Data Plane (Mặt phẳng dữ liệu)"**, dùng giao thức **OpenFlow** để bộ điều khiển trung tâm (SDN Controller) quản lý đường đi của các thiết bị Switch.
  - **NFV:** Chuyển đổi các thiết bị phần cứng mạng chuyên dụng đắt đỏ (Tường lửa, Router, Bộ cân bằng tải) thành **các phần mềm ảo hóa (Virtual Appliances)** chạy trên máy chủ x86 thông thường.
  - Phân biệt 3 mô hình Cloud:
    - **IaaS:** Thuê **Phần cứng thô** (Máy ảo, Ổ đĩa, Mạng) $\rightarrow$ Người dùng tự cài OS, middleware, app.
    - **PaaS:** Thuê **Môi trường phát triển** (Đã có sẵn OS, runtime Java/Python, DB) $\rightarrow$ Người dùng chỉ việc deploy code.
    - **SaaS:** Thuê **Ứng dụng hoàn thiện** chạy trên web $\rightarrow$ Người dùng chỉ việc đăng nhập dùng.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng đối chiếu các công nghệ SDE (Software-Defined Everything):**

| Công nghệ | Tên đầy đủ & Khái niệm cốt lõi | Cơ chế kỹ thuật chi tiết |
| :--- | :--- | :--- |
| **SDN** | **Software-Defined Networking** (Mạng định nghĩa bằng phần mềm) | Tách biệt hoàn toàn tầng điều khiển logic (**Control Plane**) khỏi tầng chuyển mạch phần cứng (**Data Plane**). Toàn bộ chính sách định tuyến và lưu lượng mạng được điều phối tập trung thông qua bộ điều khiển phần mềm (**SDN Controller**) sử dụng giao thức chuẩn hóa quốc tế **OpenFlow**. |
| **SDS** | **Software-Defined Storage** (Lưu trữ định nghĩa bằng phần mềm) | Ảo hóa toàn bộ các thiết bị lưu trữ vật lý (HDD, SSD, NAS, SAN) phân tán thành một kho tài nguyên lưu trữ chung thống nhất (**Storage Pool**), cho phép cấp phát dung lượng động, sao lưu và tái cấu trúc hoàn toàn thông qua phần mềm. |
| **SDDC** | **Software-Defined Data Center** (Trung tâm dữ liệu định nghĩa bằng phần mềm) | Tích hợp toàn diện SDN, SDS và ảo hóa máy chủ (Compute Virtualization); biến toàn bộ trung tâm dữ liệu khổng lồ thành một hệ thống được lập trình, giám sát và vận hành tự động 100% bằng mã nguồn (Infrastructure as Code). |
| **NFV** | **Network Functions Virtualization** (Ảo hóa chức năng mạng) | Đóng gói các chức năng mạng truyền thống vốn phụ thuộc vào các khối phần cứng chuyên dụng (Tường lửa Firewall, Hệ thống phát hiện xâm nhập IDS/IPS, Cân bằng tải Load Balancer) thành các máy ảo phần mềm độc lập chạy trên máy chủ tiêu chuẩn x86. |

- **2. Bảng phân định ranh giới trách nhiệm trong 3 mô hình Điện toán đám mây (Cloud Computing):**

| Mô hình Cloud | Tên viết tắt & Viết đầy đủ | Khách hàng quản lý | Nhà cung cấp Cloud quản lý | Đại diện thực tế điển hình |
| :--- | :--- | :--- | :--- | :--- |
| **IaaS** | **Infrastructure as a Service** (Hạ tầng như một dịch vụ) | **Hệ điều hành (OS)**, Phần mềm trung gian (Middleware), Runtime, Ứng dụng, Dữ liệu. | Máy chủ vật lý, Ảo hóa phần cứng (Hypervisor), Hệ thống mạng, Ổ lưu trữ. | AWS EC2, GCP Compute Engine, Microsoft Azure VM. |
| **PaaS** | **Platform as a Service** (Nền tảng như một dịch vụ) | **Ứng dụng của khách hàng (Application)** và **Dữ liệu nghiệp vụ (Data)**. | Phần cứng, Mạng, Ảo hóa, **Hệ điều hành (OS)**, **Môi trường chạy (Runtime: Java, Node.js)**, Cơ sở dữ liệu. | Google App Engine, Heroku, AWS Elastic Beanstalk. |
| **SaaS** | **Software as a Service** (Phần mềm như một dịch vụ) | **Chỉ sử dụng và quản lý tài khoản người dùng**. | **Toàn bộ hệ thống từ phần cứng, hệ điều hành đến chính phần mềm ứng dụng**. | Google Workspace (Gmail, Docs), Microsoft 365, Salesforce. |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Mối quan hệ cộng tác giữa SDN và NFV:**
  - SDN và NFV không loại trừ nhau mà bổ trợ hoàn hảo cho nhau: NFV cung cấp các chức năng xử lý gói tin ảo hóa (như một tường lửa ảo), trong khi SDN cung cấp hạ tầng mạng mềm dẻo để định tuyến chính xác các gói tin đi qua chuỗi các chức năng ảo hóa đó (Service Function Chaining).

### 복습 체크리스트
- [ ] Ghi nhớ SDN tách biệt hoàn toàn Control Plane và Data Plane qua giao thức OpenFlow.
- [ ] Nhớ NFV là kỹ thuật ảo hóa các chức năng mạng chuyên dụng (Firewall, Router) thành phần mềm.
- [ ] Phân biệt rõ ràng phạm vi quản lý: IaaS (khách tự cài OS), PaaS (có sẵn OS và Runtime), SaaS (phần mềm web hoàn chỉnh).
- [ ] Nhớ SDDC là sự tích hợp ảo hóa toàn diện cả Tính toán, Lưu trữ (SDS) và Mạng (SDN).
