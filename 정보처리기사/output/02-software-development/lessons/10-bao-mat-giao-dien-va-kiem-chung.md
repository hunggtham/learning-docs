# 인터페이스 보안 및 검증 도구 (Bảo mật giao diện và công cụ kiểm chứng)

## 학습 목표
- Nắm vững 3 giao thức bảo mật đường truyền theo tầng mạng OSI: IPSec (`네트워크 계층 L3`), SSL/TLS (`전송 계층 L4/L5`), và S-HTTP (`응용 계층 L7`).
- Phân tích 3 thành phần của bộ giao thức IPSec: AH (`인증 헤더` - tính toàn vẹn/xác thực, không mã hóa), ESP (`암호화 페이로드` - mã hóa bảo mật), và IKE (`키 교환`).
- So sánh hai chế độ hoạt động của IPSec: Chế độ truyền dẫn (`전송 모드` - Host-to-Host, không tạo New IP Header) vs Chế độ đường hầm (`터널 모드` - Gateway-to-Gateway qua VPN, tạo New IP Header).
- Hiểu rõ nguyên lý hoạt động của công cụ kiểm tra tính toàn vẹn Tripwire (`트립와이어`): so sánh mã băm (MD5, SHA) của tệp tin hệ thống để phát hiện cửa sau (`백도어 / Backdoor`).
- Nhận diện chính xác 5 công cụ kiểm chứng triển khai giao diện: xUnit (kiểm thử đơn vị), STAF (môi trường phân tán), FitNesse (giao diện Web/Wiki), NTAF (Naver = FitNesse + STAF), và watir (Ruby).

## 핵심 키워드
- 인터페이스 보안 (Bảo mật giao diện / Interface Security)
- 보안 프로토콜 (IPSec L3, SSL/TLS L4/L5 HTTPS 443, S-HTTP L7)
- IPSec 구성 요소 (AH 무결성·인증·비암호화, ESP 기밀성·암호화, IKE)
- IPSec 동작 모드 (전송 모드 Transport Host-to-Host vs 터널 모드 Tunnel New IP Header)
- 트립와이어 (Tripwire / 무결성 검사 HIDS / 해시 값 비교 / 백도어 탐지)
- 구현 검증 도구 (xUnit 단위테스트, STAF 분산환경, FitNesse 웹/Wiki, NTAF 네이버, watir 루비)

## 선행·연결 개념
- **Từ đâu (Origin / Prerequisite):** Ở bài học trước [09-tich-hop-he-thong-eai-esb.md](09-tich-hop-he-thong-eai-esb.md), chúng ta đã khảo sát các kiến trúc tích hợp hệ thống doanh nghiệp qua EAI/ESB và định dạng dữ liệu mở JSON/XML.
- **Đang giải quyết gì (Current Problem):** Khi các giao diện API kết nối qua mạng diện rộng, dữ liệu đối mặt với nguy cơ bị nghe lén, giả mạo và lỗi sai lệch chức năng. Bài học này giải quyết việc thiết lập các giao thức mã hóa đường truyền (IPSec, SSL/TLS), công cụ kiểm tra tính toàn vẹn chống backdoor (Tripwire) và bộ khung kiểm chứng giao diện tự động.
- **Dùng đi đâu (Forward Handoff):** Sau khi các giao diện được bảo mật và kiểm chứng hoàn tất, sản phẩm sẵn sàng bước vào khâu phân phối và bảo vệ bản quyền số thương mại tại [11-dong-goi-phan-mem-va-drm.md](11-dong-goi-phan-mem-va-drm.md).

## 읽는 방법
- Đọc TẦNG A để nắm chắc bảng nhận diện 3 giao thức mạng, sự khác nhau giữa AH vs ESP, hai chế độ Transport vs Tunnel của IPSec, vai trò của Tripwire và bảng đối chiếu 5 công cụ test tự động.
- Đọc TẦNG B để hiểu sâu quy trình 3 pha của Tripwire và vai trò giám sát hiệu năng của công cụ APM.

---

## 인터페이스 보안 및 검증 도구

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng so sánh 3 giao thức bảo mật đường truyền
| Giao thức | Tầng OSI đối ứng | Cơ chế hoạt động cốt lõi | Phạm vi ứng dụng thực tế |
| :--- | :--- | :--- | :--- |
| **IPSec (IP Security)** | **Tầng mạng (L3 - Network)** | Mã hóa và xác thực trực tiếp tại mức gói tin IP qua **AH** và **ESP** | Mạng riêng ảo **VPN**, kết nối mạng an toàn giữa các chi nhánh |
| **SSL / TLS** | **Tầng giao vận (L4/L5 - Transport)** | Bắt tay khóa bất đối xứng, truyền dữ liệu tốc độ cao bằng mã hóa đối xứng | Web an toàn (**HTTPS / Port 443**), email an toàn (FTPS, SMTPS) |
| **S-HTTP** | **Tầng ứng dụng (L7 - Application)**| Chỉ mã hóa nội dung thông điệp HTTP cụ thể, không mã hóa toàn kênh | Kiểm soát bảo mật chi tiết từng thông điệp riêng lẻ |

#### 2. Đối chiếu 2 chế độ hoạt động của IPSec
| Chế độ hoạt động | Phạm vi mã hóa (Encrypted Area) | New IP Header | Ngữ cảnh ứng dụng |
| :--- | :--- | :---: | :--- |
| **전송 모드 (Transport Mode)** | Chỉ mã hóa **Payload (Dữ liệu)**; giữ nguyên IP Header gốc | **Không tạo** | Giao tiếp trực tiếp giữa 2 máy chủ trạm (**Host-to-Host**) |
| **터널 모드 (Tunnel Mode)** | Mã hóa **toàn bộ gói tin IP gốc** (cả IP Header cũ và Payload) | **Tạo mới** | Kết nối giữa 2 cổng mạng an toàn qua VPN (**Gateway-to-Gateway**) |

#### 3. Bảng đối chiếu 5 công cụ kiểm chứng giao diện (인터페이스 검증 도구)
| Tên công cụ | Nền tảng / Đặc tính | Cơ chế kỹ thuật trọng tâm | Từ khóa nhận diện đề thi |
| :--- | :--- | :--- | :--- |
| **xUnit** | Đa ngôn ngữ (Java, C++, C#...) | Khung kiểm thử đơn vị (**단위 테스트 프레임워크**) tự động hóa | **단위 테스트**, JUnit, CppUnit, NUnit |
| **STAF** | Đa nền tảng (C/S, Daemon) | Khung tự động hóa kiểm thử trong **môi trường phân tán (분산 환경)** | **서비스 호출**, **컴포넌트 재사용**, **분산 환경** |
| **FitNesse** | Nền tảng Web / Wiki | Khung kiểm thử chấp nhận; thiết kế kịch bản dạng **bảng biểu trên Web** | **웹 기반**, **Wiki 기반**, 케이스 테이블 |
| **NTAF** | Do NHN (Naver) phát triển | Giải pháp tích hợp: kết hợp giao diện Web của **FitNesse** với **STAF** | **FitNesse + STAF 결합**, **NHN(네이버)** |
| **watir** | Dựa trên **Ruby** | Khung kiểm thử tự động hóa tương tác trình duyệt ứng dụng Web bằng Ruby | **Ruby 기반**, 웹 애플리케이션 테스트 |

#### 4. Bẫy đề thi trắc nghiệm kinh điển (기출 함정 포인트)
- **Bẫy 1: Thành phần AH trong IPSec:** Khẳng định "AH mã hóa dữ liệu Payload để chống nghe lén" $\rightarrow$ **SAI**. AH chỉ cung cấp tính xác thực (Authentication) và tính toàn vẹn (Integrity), **AH không mã hóa dữ liệu**. Muốn mã hóa bảo mật bí mật (Confidentiality) phải dùng **ESP**.
- **Bẫy 2: Chế độ Tunnel Mode:** Kết nối VPN giữa 2 Gateway chi nhánh bắt buộc dùng **터널 모드 (Tunnel Mode)** và tạo thêm **New IP Header** đóng gói bên ngoài.
- **Bẫy 3: Công cụ phát hiện Backdoor:** Công cụ kiểm tra tính toàn vẹn (`무결성 검사`) dựa trên so sánh mã băm (MD5, SHA) để tìm kiếm cửa sau (`백도어`) là **트립와이어 (Tripwire)**.
- **Bẫy 4: Công cụ của Naver:** Thấy công thức **FitNesse + STAF** $\rightarrow$ Chọn ngay **NTAF**.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Quy trình 3 pha vận hành của Tripwire
```
[Hệ thống sạch ban đầu] ──► [Pha 1: Tạo Baseline DB] (Lưu mã băm SHA/MD5, Inode, Permission vào DB an toàn)
                                     │
                            [Pha 2: Quét định kỳ] (Tính lại mã băm hiện tại của các file hệ thống)
                                     │
                            [Pha 3: So sánh & Cảnh báo] (Sai lệch 1 bit ==> Báo động phát hiện Backdoor)
```
- Tripwire là hệ thống phát hiện xâm nhập trên máy chủ (HIDS). Nó không phải là Tường lửa (Firewall) và không tự động chặn gói tin mạng, mà tập trung giám sát sự thay đổi trái phép của tệp tin.

#### 2. Giám sát giao diện qua APM (Application Performance Monitoring)
- APM (như Scouter, Jennifer, Pinpoint) giám sát hiệu năng giao diện theo thời gian thực: đo lường thời gian đáp ứng API, tỷ lệ lỗi HTTP 5xx, và phát hiện sớm hiện tượng cạn kiệt Connection Pool giữa các phân hệ.

---

### 복습 체크리스트
- [ ] Phân biệt tầng OSI của 3 giao thức: IPSec (L3), SSL/TLS (L4/L5), S-HTTP (L7).
- [ ] Phân biệt rõ thành phần AH (xác thực/toàn vẹn, không mã hóa) và ESP (mã hóa bảo mật) trong IPSec.
- [ ] Phân biệt 전송 모드 (Host-to-Host, không IP header mới) và 터널 모드 (Gateway-to-Gateway, có New IP Header).
- [ ] Định nghĩa Tripwire là công cụ kiểm tra toàn vẹn so sánh mã băm để phát hiện Backdoor.
- [ ] Nhớ từ khóa 5 công cụ test: xUnit (단위), STAF (분산), FitNesse (웹/Wiki), NTAF (Naver), watir (Ruby).
