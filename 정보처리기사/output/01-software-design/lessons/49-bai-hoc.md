# 6. 분산 데이터베이스 (Distributed Database)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và kiến trúc logic hợp nhất của Cơ sở dữ liệu phân tán (`분산 데이터베이스 - Distributed Database`).
- Thuộc nằm lòng 4 tính trong suốt cốt lõi của CSDL phân tán: Trong suốt vị trí (`위치 투명성`), Trong suốt phân mảnh (`분할 투명성`), Trong suốt sao chép (`복제 투명성`), và Trong suốt đồng thời (`병행 투명성`).
- Hiểu cơ chế hoạt động của Giao thức cam kết hai pha (`2PC - Two-Phase Commit Protocol`) trong việc đảm bảo tính nguyên tử của giao dịch phân tán.

## 핵심 키워드 (Từ khóa)
- 분산 데이터베이스 (Cơ sở dữ liệu phân tán / Distributed Database)
- 분산 투명성 4대 요소 (4 tính trong suốt phân tán)
- 위치 투명성 (Location Transparency / 물리적 위치 불필요)
- 분할 투명성 (Fragmentation Transparency / 수평·수직 분할)
- 복제 투명성 (Replication Transparency / 다중 복제본)
- 병행 투명성 (Concurrency Transparency / 다중 트랜잭션 일관성)
- 2단계 커밋 프로토콜 (2PC - Two-Phase Commit / Prepare + Commit)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([5. 보안 및 암호화 (Security & Encryption)](48-bai-hoc.md)):** Sau khi xem xét các kỹ thuật bảo mật dữ liệu, bài này khảo sát kiến trúc lưu trữ phân tán hiện đại trên quy mô nhiều cụm máy chủ.
- **Tiếp nối sang bài sau ([7. 자료 구조 (Data Structures)](50-bai-hoc.md)):** Chuyển từ tầng cơ sở dữ liệu sang phân loại và phân tích các Cấu trúc dữ liệu nền tảng trong khoa học máy tính (Tuyến tính vs Phi tuyến tính).

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc làu định nghĩa 4 tính trong suốt (Vị trí, Phân mảnh, Sao chép, Đồng thời) - dạng bài trắc nghiệm đưa ra một tình huống sử dụng rồi hỏi tương ứng với tính trong suốt nào.
- Đọc TẦNG B để theo dõi quy trình điều phối bỏ phiếu trong 2PC giữa Coordinator và các Participant.

---

## 6. 분산 데이터베이스 (Distributed Database)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **개념 (Định nghĩa CSDL Phân tán):**
  - Là hệ thống cơ sở dữ liệu mà về mặt vật lý, dữ liệu được phân tán lưu trữ trên nhiều máy tính/máy chủ khác nhau kết nối qua mạng viễn thông, nhưng nhìn từ góc độ người dùng và ứng dụng, nó vẫn là **một cơ sở dữ liệu logic duy nhất hoàn chỉnh (`논리적으로는 하나의 데이터베이스로 보임`)**.
- **4 tính trong suốt cốt lõi của CSDL phân tán (분산 투명성 4대 특성):**
  1. **위치 투명성 (Location Transparency - Tính trong suốt về vị trí):**
     - Người dùng chỉ cần sử dụng **tên logic của đối tượng dữ liệu** để truy vấn (`데이터베이스의 논리적 명칭만으로 접근`); hệ thống tự động tìm đến máy chủ chứa dữ liệu mà người dùng không cần biết dữ liệu đó đang nằm ở vị trí địa lý hay địa chỉ IP máy chủ nào.
  2. **분할 투명성 (Fragmentation Transparency - Tính trong suốt về phân mảnh):**
     - Một bảng quan hệ logic lớn có thể bị chia nhỏ thành nhiều mảnh (Phân mảnh ngang theo hàng, Phân mảnh dọc theo cột) lưu rải rác trên nhiều trạm khác nhau, nhưng **người dùng chỉ nhìn thấy và thao tác như trên một bảng toàn vẹn duy nhất**, không cần biết bảng bị cắt xẻ thế nào.
  3. **복제 투명성 (Replication Transparency - Tính trong suốt về sao chép):**
     - Để tăng tốc độ đọc và khả năng chịu lỗi, cùng một mẩu dữ liệu có thể được sao chép nhân bản thành nhiều bản sao lưu trên nhiều máy chủ khác nhau; tuy nhiên **người dùng chỉ thấy duy nhất một bản dữ liệu** và khi cập nhật, hệ thống tự động đồng bộ hóa tất cả các bản sao.
  4. **병행 투명성 (Concurrency Transparency - Tính trong suốt về đồng thời):**
     - Nhiều giao dịch phân tán có thể cùng thực thi đồng thời trên các trạm khác nhau mà kết quả vẫn đảm bảo tính tuần tự, nhất quán như thể các giao dịch chạy riêng rẽ độc lập.
  - *(Bổ sung: 장애 투명성 - Failure Transparency)*: Khi một máy chủ trạm bị sự cố, toàn bộ hệ thống vẫn tiếp tục duy trì hoạt động phục vụ bình thường.
- **2단계 커밋 규약 (2PC - Two-Phase Commit Protocol):**
  - Giao thức điều phối giao dịch phân tán nhằm đảm bảo tính nguyên tử (Atomicity):
    - **1. 준비 단계 (Prepare Phase - Pha chuẩn bị / Bỏ phiếu):** Điều phối viên (Coordinator) gửi yêu cầu chuẩn bị Commit đến tất cả các trạm tham gia (Participants). Các trạm kiểm tra tài nguyên và gửi phản hồi: Đồng ý (Vote Commit) hoặc Không đồng ý (Vote Abort).
    - **2. 커밋 단계 (Commit Phase - Pha cam kết / Quyết định):** Nếu **TẤT CẢ các trạm đều đồng ý**, Coordinator ra lệnh chính thức Commit. Nếu **CHỈ CẦN 1 TRẠM từ chối hoặc mất kết nối**, Coordinator ra lệnh toàn bộ hệ thống cùng Rollback.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Người dùng chỉ cần dùng tên logic mà không cần biết dữ liệu nằm ở server nào là tính trong suốt gì?"* -> **위치 투명성 (Location Transparency)**.
  - **Bẫy 2:** *"Bảng dữ liệu bị chia nhỏ thành nhiều mảnh nhưng người dùng vẫn thấy là một bảng duy nhất là tính trong suốt gì?"* -> **분할 투명성 (Fragmentation Transparency)**.
  - **Bẫy 3:** *"Trong giao thức 2PC, nếu có 1 trạm từ chối thì hệ thống sẽ làm gì?"* -> **Toàn bộ hệ thống cùng Rollback hủy bỏ giao dịch (글로벌 롤백)**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "CSDL phân tán có 4 tính trong suốt: Vị trí không cần nhớ IP, Phân mảnh không thấy cắt xẻ, Sao chép không thấy nhân bản, Đồng thời không thấy xung đột; 2PC chuẩn bị rồi mới cam kết".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **So sánh Phân mảnh ngang vs Phân mảnh dọc:**
  - `수평 분할 (Horizontal Fragmentation)`: Cắt bảng theo các hàng (Tuples) thỏa mãn điều kiện WHERE. Ví dụ: Bảng `Khách_Hàng` tách thành `Khach_Hang_Mien_Bac` và `Khach_Hang_Mien_Nam`.
  - `수직 분할 (Vertical Fragmentation)`: Cắt bảng theo các cột (Attributes). Khóa chính phải xuất hiện ở tất cả các mảnh để sau này có thể JOIN ghép lại bảng gốc mà không mất mát thông tin.

### 복습 체크리스트
- [ ] Kể tên đầy đủ 4 tính trong suốt của CSDL phân tán: 위치, 분할, 복제, 병행 투명성.
- [ ] Phân biệt được tình huống của 위치 투명성 (không cần biết vị trí IP) và 복제 투명성 (không cần biết số bản copy).
- [ ] Nêu được 2 pha của giao thức 2PC: 준비 단계 (Prepare) và 커밋 단계 (Commit).
- [ ] Phân biệt được 수평 분할 (chia theo hàng) và 수직 분할 (chia theo cột).
