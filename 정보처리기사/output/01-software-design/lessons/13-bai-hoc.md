# 3. 현행 시스템 파악 (Understanding Current System)

## 학습 목표 (Mục tiêu)
- Nắm vững quy trình chuẩn 3 giai đoạn khảo sát và phân tích hiện trạng hệ thống thông tin (`현행 시스템 파악 3단계 절차`).
- Nhớ chính xác các hạng mục công việc cụ thể của từng giai đoạn: Giai đoạn 1 (Cấu trúc, Chức năng, Giao diện), Giai đoạn 2 (Kiến trúc, Phần mềm & Bản quyền), Giai đoạn 3 (Phần cứng & Hạ tầng mạng).
- Hiểu tầm quan trọng của việc cấu hình dự phòng phần cứng kép (`하드웨어 이중화`) và quản lý bản quyền phần mềm (`소프트웨어 라이선스`).

## 핵심 키워드 (Từ khóa)
- 현행 시스템 파악 절차 (Quy trình phân tích hệ thống hiện tại / 3-Stage Process)
- 기간 업무 / 지원 업무 (Nghiệp vụ cốt lõi / Nghiệp vụ hỗ trợ)
- 인터페이스 구성 (Cấu trúc giao diện liên kết / Interface Architecture)
- 소프트웨어 라이선스 (Bản quyền phần mềm / Software License)
- 하드웨어 이중화 (Dự phòng phần cứng kép / Hardware Redundancy)
- 네트워크 토폴로지 (Cấu trúc liên kết mạng / Network Topology)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([1. 현행 시스템 분석](12-bai-hoc.md)):** Sau khi nắm các tiêu chí định lượng hiệu năng và tiêu chuẩn chọn OS/DBMS, bài này hệ thống hóa thành quy trình thực hiện cụ thể theo 3 giai đoạn từ ứng dụng đến hạ tầng.
- **Tiếp nối sang bài sau ([3. 모델링 및 UML](14-bai-hoc.md)):** Khi đã nắm vững hiện trạng hệ thống và dữ liệu, kỹ sư chuyển sang mô hình hóa bài toán theo chuẩn thiết kế hướng đối tượng UML.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để ghi nhớ chắc chắn mẹo thi trắc nghiệm: Giai đoạn 1 là gì, Giai đoạn 2 là gì, Giai đoạn 3 là gì - đề thi thường hỏi một hạng mục cụ thể thuộc giai đoạn nào.
- Đọc TẦNG B để hiểu logic phân rã từ tầng phần mềm nghiệp vụ (gần người dùng nhất) đi sâu dần xuống tầng vật lý phần cứng và dây cáp mạng.

---

## 3. 현행 시스템 파악 (Understanding Current System)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Quy trình 3 giai đoạn phân tích hiện trạng hệ thống:**
  - **1단계 (Giai đoạn 1 - Tầng nghiệp vụ và giao diện):**
    - `시스템 구성 파악 (Nắm bắt cấu trúc hệ thống)`: Phân loại hệ thống thành Nghiệp vụ cốt lõi (`기간 업무` - Core Business) và Nghiệp vụ hỗ trợ (`지원 업무` - Support Business).
    - `시스템 기능 파악 (Nắm bắt chức năng hệ thống)`: Liệt kê toàn bộ chức năng theo sơ đồ phân cấp dạng cây (Chức năng cấp 1 -> Cấp 2 -> Cấp 3).
    - `시스템 인터페이스 파악 (Nắm bắt giao diện liên kết)`: Khảo sát các luồng dữ liệu trao đổi giữa các hệ thống, giao thức kết nối (HTTP, TCP/IP), định dạng dữ liệu (JSON, XML), và phương thức truyền (Đồng bộ, Bất đồng bộ, Batch).
  - **2단계 (Giai đoạn 2 - Tầng kiến trúc và phần mềm):**
    - `아키텍처 구성 파악 (Nắm bắt kiến trúc hệ thống)`: Khảo sát sơ đồ phân tầng công nghệ của các phân hệ chính (Client-Server, 3-Tier, Microservices).
    - `소프트웨어 구성 파악 (Nắm bắt cấu trúc phần mềm)`: Lập danh mục phần mềm ứng dụng, hệ điều hành, DBMS, Middleware kèm phiên bản, mục đích sử dụng và tình trạng bản quyền (`소프트웨어 라이선스 적용 방식 và chi phí duy trì`).
  - **3단계 (Giai đoạn 3 - Tầng hạ tầng vật lý và mạng):**
    - `하드웨어 구성 파악 (Nắm bắt cấu trúc phần cứng máy chủ)`: Xác định số lượng máy chủ (Web Server, WAS Server, DB Server), thông số kỹ thuật (CPU, RAM, Disk), và đặc biệt là phương án dự phòng kép (`하드웨어 이중화 - Redundancy/Failover`).
    - `네트워크 구성 파악 (Nắm bắt cấu trúc mạng)`: Khảo sát sơ đồ liên kết mạng vật lý và logic (`네트워크 토폴로지`), phân dải mạng LAN/WAN, vị trí máy chủ, tường lửa (Firewall) và các thiết bị định tuyến (Router, Switch).
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Khảo sát tình trạng bản quyền phần mềm (소프트웨어 라이선스) thuộc giai đoạn nào?"* -> **Giai đoạn 2 (2단계)**, không phải giai đoạn 1.
  - **Bẫy 2:** *"Khảo sát cấu hình dự phòng phần cứng (하드웨어 이중화) thuộc giai đoạn nào?"* -> **Giai đoạn 3 (3단계)**.
  - **Bẫy 3:** *"Phân loại 기간 업무 và 지원 업무 thuộc giai đoạn nào?"* -> **Giai đoạn 1 (1단계)**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "1: Cấu trúc - Chức năng - Interface; 2: Kiến trúc - Bản quyền SW; 3: Phần cứng dự phòng kép - Hạ tầng mạng".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tầm quan trọng của Cấu hình dự phòng kép (하드웨어 이중화):**
  - Trong các hệ thống tài chính hoặc y tế, việc máy chủ dừng hoạt động (Downtime) dù chỉ 1 phút cũng gây tổn thất nghiêm trọng. Khảo sát giai đoạn 3 giúp kiểm tra xem các máy chủ cơ sở dữ liệu có đang chạy cấu hình Active-Standby (khi máy chính lỗi, máy phụ tự động nhảy lên thay thế) hay Active-Active (cả 2 máy cùng gánh tải) hay không.
- **Ví dụ phân loại 기간 업무 vs 지원 업무:**
  - Trong hệ thống của một công ty bảo hiểm: Nghiệp vụ thẩm định hợp đồng bảo hiểm và bồi thường thiệt hại là `기간 업무` (Nghiệp vụ cốt lõi sinh ra doanh thu). Nghiệp vụ chấm công nhân sự và quản lý tài sản văn phòng là `지원 업무` (Nghiệp vụ phụ trợ hỗ trợ vận hành).

### 복습 체크리스트
- [ ] Nhớ tên và nội dung công việc của 1단계 (Cấu trúc hệ thống, Chức năng, Giao diện).
- [ ] Nhớ nội dung công việc của 2단계 (Kiến trúc, Danh mục phần mềm, Bản quyền).
- [ ] Nhớ nội dung công việc của 3단계 (Phần cứng, Cấu hình dự phòng kép 이중화, Hạ tầng mạng).
- [ ] Phân biệt được sự khác nhau giữa 기간 업무 (Cốt lõi) và 지원 업무 (Hỗ trợ).
