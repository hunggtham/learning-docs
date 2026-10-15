# 1. 현행 시스템 분석 (Current System Analysis)

## 학습 목표 (Mục tiêu)
- Nắm vững các chỉ số đo lường hiệu năng của nền tảng phần mềm hiện tại: Tính sẵn sàng (`가용성`), Thời gian đáp ứng (`응답 시간`), Thời gian quay vòng (`경과 시간`), và Tỷ lệ sử dụng tài nguyên (`사용률`).
- Nhận diện các tiêu chuẩn kỹ thuật khi lựa chọn và đánh giá Hệ điều hành (`OS`) và Hệ quản trị cơ sở dữ liệu (`DBMS`) cho dự án mới.
- Hiểu rõ mục đích phân tích hệ thống hiện tại nhằm xác định tính tương thích, khả năng mở rộng và ước lượng chi phí tái cấu trúc.

## 핵심 키워드 (Từ khóa)
- 현행 시스템 분석 (Phân tích hệ thống hiện tại / Current System Analysis)
- 플랫폼 성능 특성 (Đặc tính hiệu năng nền tảng / Platform Performance)
- 가용성 (Tính sẵn sàng / Availability)
- 응답 시간 / 경과 시간 (Response Time / Turnaround Time)
- 자원 사용률 (Tỷ lệ sử dụng tài nguyên / Utilization)
- OS / DBMS 고려사항 (Tiêu chí cân nhắc OS & DBMS: 신뢰도, 성능, 기술 지원, 비용)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([A+ Deep Dive: 개발 모형 선택과 요구사항 검증](11-bai-hoc.md)):** Sau khi hoàn tất giai đoạn phân tích yêu cầu và lựa chọn mô hình SDLC, kỹ sư bắt tay vào việc khảo sát chi tiết môi trường vận hành hiện tại trước khi thiết kế kiến trúc mới.
- **Tiếp nối sang bài sau ([3. 현행 시스템 파악](13-bai-hoc.md)):** Khảo sát 3 tầng cấu trúc cụ thể: Tầng nghiệp vụ phần mềm, Tầng kiến trúc công nghệ và Tầng hạ tầng phần cứng/mạng.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để ghi nhớ 4 chỉ số hiệu năng nền tảng và 6 tiêu chuẩn lựa chọn OS/DBMS - đề thi thường hỏi từ khóa nào KHÔNG PHẢI là tiêu chuẩn lựa chọn.
- Đọc TẦNG B để phân biệt sự khác nhau giữa Thời gian đáp ứng (Response Time) và Thời gian quay vòng (Turnaround Time) trong môi trường xử lý hàng loạt và thời gian thực.

---

## 1. 현행 시스템 분석 (Current System Analysis)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **개념 (Mục đích phân tích hệ thống hiện tại):** Là quá trình tìm hiểu rõ cấu trúc các phân hệ nghiệp vụ, phần mềm, phần cứng và hạ tầng mạng hiện đang hoạt động nhằm xác định những hạn chế kỹ thuật và định hình chính xác phạm vi phát triển cho hệ thống mới.
- **4 chỉ số đánh giá hiệu năng nền tảng (플랫폼 성능 특성):**
  1. `가용성 (Availability - Tính sẵn sàng)`: Khả năng hệ thống duy trì trạng thái hoạt động liên tục, không bị gián đoạn khi người dùng yêu cầu dịch vụ. Đo lường qua MTBF (Mean Time Between Failures) và MTTR (Mean Time To Repair).
  2. `응답 시간 (Response Time - Thời gian đáp ứng)`: Khoảng thời gian từ khi người dùng gửi một yêu cầu truy vấn đến khi nhận được phản hồi đầu tiên từ hệ thống.
  3. `경과 시간 (Turnaround Time - Thời gian quay vòng)`: Tổng thời gian từ khi một công việc/tác vụ (Job) được đưa vào hệ thống cho đến khi hoàn tất toàn bộ và xuất ra kết quả cuối cùng.
  4. `자원 사용률 (Utilization - Tỷ lệ sử dụng tài nguyên)`: Tỷ lệ phần trăm tài nguyên CPU, RAM, băng thông mạng và đĩa I/O được sử dụng khi hệ thống xử lý công việc.
- **Tiêu chí cân nhắc khi lựa chọn Hệ điều hành (OS) và DBMS:**
  - `신뢰도 (Độ tin cậy / Reliability)`: Hệ thống hoạt động ổn định, có cơ chế tự phục hồi khi gặp sự cố, ít lỗi hệ thống.
  - `성능 (Hiệu năng / Performance)`: Khả năng xử lý lượng lớn giao dịch đồng thời và thời gian truy xuất dữ liệu nhanh.
  - `기술 지원 (Hỗ trợ kỹ thuật / Technical Support)`: Nhà cung cấp có tài liệu đầy đủ, đội ngũ kỹ thuật phản hồi sự cố nhanh chóng.
  - `주변 기기 (Thiết bị ngoại vi / Peripherals)`: Hỗ trợ đa dạng các loại phần cứng, máy in, cảm biến kết nối ngoài.
  - `구축 비용 (Chi phí triển khai / TCO - Total Cost of Ownership)`: Chi phí bản quyền (License), chi phí bảo trì và chi phí nâng cấp hàng năm.
  - `상호 호환성 (Tính tương thích lẫn nhau / Compatibility)`: Dễ dàng liên kết và tích hợp với các ứng dụng, cơ sở dữ liệu hiện có.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** Phân biệt `응답 시간 (Response Time)` và `경과 시간 (Turnaround Time)`. Response Time chỉ tính đến khi bắt đầu có phản hồi, còn Turnaround Time tính toàn bộ quá trình đến khi kết thúc hẳn công việc.
  - **Bẫy 2:** Đề thi đưa các từ cảm tính như `최신성 (Tính thời thượng/mới nhất)` hoặc `인지도 (Độ nổi tiếng)` và hỏi có phải tiêu chí kỹ thuật lựa chọn OS không -> **Không phải**. Phải căn cứ vào Tính sẵn sàng, Hiệu năng, Độ tin cậy và Chi phí.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Hiệu năng đo bằng Sẵn sàng, Đáp ứng, Quay vòng, Sử dụng tài nguyên; chọn OS/DBMS dựa trên Tin cậy, Hiệu năng, Hỗ trợ và Chi phí".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tình huống thực tế phân tích hiệu năng:**
  - Trong một hệ thống ngân hàng trực tuyến:
    - Nếu server CPU luôn chạm ngưỡng 95% vào giờ cao điểm, chỉ số `자원 사용률` đang ở mức báo động, cần nâng cấp scale-up hoặc scale-out.
    - Nếu người dùng bấm "Chuyển tiền" và mất 0.8 giây để màn hình hiện "Đang xử lý", đó là `응답 시간`. Sau 3 giây tiền trừ và có tin nhắn SMS báo thành công, chuỗi xử lý đó hoàn tất `경과 시간`.
- **Mối liên hệ giữa phân tích hiện trạng và kiến trúc tương lai:**
  - Nếu kết quả phân tích hiện trạng cho thấy hệ thống cũ đang dùng cơ sở dữ liệu quan hệ (RDBMS) bị quá tải khi đọc dữ liệu log lớn, kiến trúc sư hệ thống sẽ đề xuất bổ sung Redis cache hoặc NoSQL cho hệ thống mới.

### 복습 체크리스트
- [ ] Kể tên và giải thích 4 chỉ số hiệu năng nền tảng: 가용성, 응답 시간, 경과 시간, 사용률.
- [ ] Phân biệt được sự khác biệt giữa Response Time và Turnaround Time.
- [ ] Liệt kê ít nhất 5 tiêu chí kỹ thuật khi đánh giá lựa chọn OS và DBMS.
- [ ] Nhận diện được các tiêu chí sai lệch (như tính mới, độ nổi tiếng) trong câu hỏi trắc nghiệm.
