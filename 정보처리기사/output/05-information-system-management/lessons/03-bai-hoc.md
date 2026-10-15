# 프레임워크 특징 및 SW 신기술 (Framework & SW Tech)

## 학습 목표 (Mục tiêu)
- Nắm vững 4 đặc trưng kiến trúc nền tảng của một Framework: Tính module hóa (모듈화), Tính tái sử dụng (재사용성), Tính mở rộng (확장성), và Đảo ngược quyền điều khiển (제어의 역전 - Inversion of Control / IoC).
- Hiểu kiến trúc khái niệm công nghệ "Mọi thứ định nghĩa bằng phần mềm" (**SDE - Software-Defined Everything**) bao gồm: Mạng định nghĩa bằng phần mềm (**SDN**), Trung tâm dữ liệu định nghĩa bằng phần mềm (**SDDC**), và Lưu trữ định nghĩa bằng phần mềm (**SDS**).
- Nhận diện các thuật ngữ công nghệ mới thường xuất hiện trong đề thi: Bản sao kỹ thuật số (**Digital Twin**), Công nghệ đóng gói vùng chứa (**Docker Container**), và Thư viện học sâu (**TensorFlow**).

## 핵심 키워드 (Từ khóa)
- 프레임워크 4대 특성 (모듈화, 재사용성, 확장성, 제어의 역전 IoC)
- SDE (Software-Defined Everything)
- SDN (Software-Defined Networking - 제어와 데이터 분리)
- SDDC (Software-Defined Data Center - 컴퓨팅·스토리지·네트워크 가상화)
- SDS (Software-Defined Storage)
- 디지털 트윈 (Digital Twin - 물리 자산의 가상 복제)
- 도커 컨테이너 (Docker Container - 경량 가상화)
- 텐서플로 (TensorFlow - 구글 데이터 플로우 그래프 딥러닝)

## 선행·연결 개념 (Kiến thức liên kết)
- [02-bai-hoc.md](02-bai-hoc.md): Cắt may phương pháp luận (Tailoring) và các Framework máy chủ.
- [04-bai-hoc.md](04-bai-hoc.md): Tổng hợp tái sử dụng phần mềm, định giá và khung phát triển.
- [05-bai-hoc.md](05-bai-hoc.md): Chuyên sâu về Framework và các bẫy phân biệt thi cử.

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh trong đề thi:
  - Khi hỏi về **SDN (Software-Defined Networking):** Đặc điểm nhận diện cốt lõi là **"Tách rời mặt phẳng điều khiển (Control Plane) ra khỏi mặt phẳng chuyển tiếp dữ liệu (Data Plane)"** để quản trị tập trung toàn mạng.
  - Khi hỏi về **디지털 트윈 (Digital Twin):** Từ khóa nhận diện là **"Tạo ra một bản sao ảo (Virtual Replica) bằng phần mềm của một đối tượng/tài sản vật lý trong thế giới thực"** để chạy mô phỏng, dự báo hư hỏng và tối ưu hóa vận hành.
  - Khi hỏi về **도커 (Docker):** Là nền tảng mã nguồn mở đóng gói ứng dụng thành **Container nhẹ**, chia sẻ nhân hệ điều hành (OS Kernel) thay vì tạo máy ảo nặng (Hypervisor).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. 4 đặc tính trụ cột của Khung phát triển phần mềm (Framework):**

| Đặc tính cốt lõi | Tên tiếng Hàn & Anh | Bản chất kỹ thuật & Giá trị thiết kế |
| :--- | :--- | :--- |
| **Tính module hóa** | **모듈화** (Modularity) | Đóng gói (Encapsulation) các thành phần độc lập nhằm tối thiểu hóa tác động lan truyền khi sửa code, nâng cao tính bảo trì. |
| **Tính tái sử dụng** | **재사용성** (Reusability) | Cung cấp sẵn các module dùng chung (Security, Transaction, Logging), giảm chi phí và nâng cao chất lượng phần mềm. |
| **Tính mở rộng** | **확장성** (Extensibility) | Cho phép mở rộng thêm tính năng riêng thông qua cơ chế đa hình (**Polymorphism**) và cài đặt giao diện (Interface). |
| **Đảo ngược điều khiển** | **제어의 역전** (IoC) | **Khung phần mềm (Framework) nắm quyền điều khiển luồng chính** và tự động gọi mã nguồn do lập trình viên viết ra. |

- **2. Bảng phân loại công nghệ SDE (Software-Defined Everything):**

| Thuật ngữ | Tên đầy đủ & Khái niệm | Ý nghĩa kỹ thuật cốt lõi |
| :--- | :--- | :--- |
| **SDN** | **Software-Defined Networking** | Tách riêng tầng điều khiển mạng (**Control Plane**) khỏi tầng thiết bị định tuyến dữ liệu vật lý (**Data Plane**), quản lý đường đi gói tin tập trung bằng phần mềm qua giao thức OpenFlow. |
| **SDDC** | **Software-Defined Data Center** | Toàn bộ tài nguyên của một trung tâm dữ liệu khổng lồ (Tính toán Compute, Lưu trữ Storage, Mạng Network, Bảo mật Security) đều được ảo hóa và tự động hóa điều phối 100% bằng phần mềm. |
| **SDS** | **Software-Defined Storage** | Tách rời phần cứng ổ đĩa vật lý khỏi logic quản lý lưu trữ, gom nhóm tài nguyên lưu trữ phân tán thành một hồ bơi chung (Storage Pool) điều khiển bằng chính sách phần mềm. |

- **3. Các công nghệ phần mềm mới thường gặp:**
  - **Digital Twin (디지털 트윈):** Tạo bản sao ảo số hóa của động cơ máy bay, tòa nhà thông minh, hay nhà máy điện hạt nhân. Thu thập dữ liệu IoT thời gian thực để mô phỏng và phát hiện lỗi hỏng hóc trước khi xảy ra ngoài đời thực.
  - **Docker (도커):** Công nghệ ảo hóa mức hệ điều hành (OS-level Virtualization) đóng gói mã nguồn và môi trường thực thi vào một Image container siêu nhẹ, khởi động chỉ trong vài giây.
  - **TensorFlow (텐서플로):** Thư viện mã nguồn mở của Google ứng dụng biểu đồ dòng dữ liệu (Dataflow Graph) để xây dựng và huấn luyện các mô hình học sâu và mạng nơ-ron nhân tạo.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Container (Docker) vs Máy ảo truyền thống (Virtual Machine / Hypervisor):**
  - Máy ảo (như VMware, VirtualBox) bắt buộc phải cài đặt một hệ điều hành khách (Guest OS) hoàn chỉnh trên mỗi máy ảo, tốn hàng chục Gigabyte dung lượng và thời gian khởi động lâu.
  - Docker Container chia sẻ chung nhân Kernel của máy chủ chủ nhà (Host OS), chỉ đóng gói mã nguồn ứng dụng và các thư viện phụ thuộc, giúp tiết kiệm bộ nhớ RAM tối đa và đạt hiệu năng tính toán gần như Bare-metal.

### 복습 체크리스트
- [ ] Kể tên đầy đủ 4 đặc trưng của Framework: 모듈화, 재사용성, 확장성, 제어의 역전 (IoC).
- [ ] Ghi nhớ SDN tách biệt Control Plane và Data Plane.
- [ ] Nhớ SDDC là công nghệ ảo hóa toàn bộ trung tâm dữ liệu bằng phần mềm.
- [ ] Nắm được định nghĩa Digital Twin: Bản sao phần mềm ảo của một tài sản vật lý thực tế.
