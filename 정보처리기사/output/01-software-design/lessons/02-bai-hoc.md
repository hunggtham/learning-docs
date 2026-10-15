# 1. 소프트웨어 생명 주기 (SDLC - Software Development Life Cycle)

## 학습 목표 (Mục tiêu)
- Nắm vững đặc trưng, ưu nhược điểm và phạm vi áp dụng của 4 mô hình SDLC kinh điển: Mô hình Thác nước (`폭포수 모형`), Mô hình Nguyên mẫu (`프로토타입 모형`), Mô hình Xoắn ốc (`나선형 모형`), và Mô hình Chữ V (`V-모형`).
- Thuộc nằm lòng 4 giai đoạn lặp lại của mô hình Xoắn ốc do Boehm đề xuất: Kế hoạch (`계획`) -> Phân tích rủi ro (`위험 분석`) -> Phát triển (`개발`) -> Đánh giá của khách hàng (`고객 평가`).
- Hiểu cấu trúc đối xứng kiểm thử của V-Model: ánh xạ chính xác từng bước phát triển với cấp độ kiểm thử tương ứng.

## 핵심 키워드 (Từ khóa)
- 폭포수 모형 (Mô hình thác nước / Waterfall Model / 선형 순차적)
- 프로토타입 모형 (Mô hình nguyên mẫu / Prototype Model / 시제품)
- 나선형 모형 (Mô hình xoắn ốc / Spiral Model / Boehm / 점진적)
- 위험 분석 (Phân tích rủi ro / Risk Analysis)
- V-모형 (Mô hình chữ V / V-Model / 테스트 검증)
- 단위·통합·시스템·인수 테스트 (Kiểm thử đơn vị, tích hợp, hệ thống, chấp nhận)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([소프트웨어 생명 주기 개요](01-bai-hoc.md)):** Sau khi hiểu khung vòng đời chung của phần mềm, bài này đi sâu vào việc so sánh 4 mô hình tổ chức thực hiện các giai đoạn đó theo hướng cổ điển và lặp cải tiến.
- **Tiếp nối sang bài sau ([1. 소프트웨어 공학 및 개발 방법론](03-bai-hoc.md)):** Từ các mô hình kinh điển, bước tiếp theo là tiếp cận các nguyên tắc kỹ nghệ phần mềm hiện đại và sự chuyển dịch sang các phương pháp luận Agile linh hoạt (Scrum, XP).

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để nắm vững các từ khóa nhận diện đề thi: từ khóa `선형 순차적` gắn với Waterfall; `시제품` gắn với Prototype; `보헴(Boehm)` và `위험 분석` gắn với Spiral; bảng ánh xạ Dev-Test gắn với V-Model.
- Đọc TẦNG B để phân tích sâu sự khác nhau về cơ chế ứng phó rủi ro và các tình huống thực tế áp dụng từng mô hình.

---

## 1. 소프트웨어 생명 주기 (SDLC - Software Development Life Cycle)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **4 mô hình SDLC trọng tâm thi trắc nghiệm:**
  1. **폭포수 모형 (Waterfall Model - Mô hình thác nước):**
     - **Đặc trưng:** Là mô hình cổ điển nhất (`가장 오래되고 폭넓게 사용된 고전적 모형`). Phát triển theo đường thẳng tuần tự (`선형 순차적`), xong dứt điểm một giai đoạn mới chuyển sang giai đoạn kế tiếp, tiền đề là không quay lại giai đoạn trước (`이전 단계로 돌아갈 수 없음`).
     - **Đầu ra:** Mỗi bước kết thúc phải có sản phẩm bàn giao được kiểm duyệt và phê duyệt rõ ràng (`결과물이 명확하게 산출`).
     - **Nhược điểm:** Khó phản ánh yêu cầu thay đổi của người dùng; lỗi phát hiện muộn ở cuối chu trình sẽ cực kỳ tốn kém để khắc phục.
  2. **프로토타입 모형 (Prototype Model - Mô hình nguyên mẫu):**
     - **Đặc trưng:** Tạo ra bản mẫu chạy thử (`시제품`) để người dùng tương tác thực tế, từ đó thu thập và xác nhận chính xác các yêu cầu còn mơ hồ.
     - **Thích hợp khi:** Người dùng không biết rõ mình cần gì, hoặc công nghệ mới chưa rõ khả năng hiện thực.
     - **Nhược điểm:** Dễ bị hiểu lầm là bản chính thức; có thể tốn thời gian lặp lại bản thử nếu không kiểm soát phạm vi.
  3. **나선형 모형 (Spiral Model - 점진적 모형 / Mô hình xoắn ốc):**
     - **Người đề xuất:** **Boehm (보헴)**.
     - **Đặc trưng cốt lõi:** Kết hợp ưu điểm tuần tự của Waterfall và thử nghiệm của Prototype, bổ sung chức năng sống còn là **Phân tích rủi ro (`위험 분석`)**.
     - **Chu trình 4 bước lặp lại theo đường xoắn ốc:**
       $$\text{계획 수립 (Lập kế hoạch)} \rightarrow \text{위험 분석 (Phân tích rủi ro)} \rightarrow \text{개발 및 검증 (Phát triển \& Kiểm chứng)} \rightarrow \text{고객 평가 (Đánh giá của khách hàng)}$$
     - **Thích hợp khi:** Dự án quy mô lớn (`대규모 시스템`), độ phức tạp và rủi ro kỹ thuật cao.
  4. **V-모형 (V-Model - Mô hình chữ V):**
     - **Đặc trưng:** Biến thể của Waterfall, nhấn mạnh mối quan hệ tương ứng 1-1 giữa các giai đoạn phát triển (nhánh xuống bên trái) và các giai đoạn kiểm thử (nhánh lên bên phải).
     - **Bảng ánh xạ Dev - Test cốt lõi:**
       - `요구사항 분석 (Phân tích yêu cầu)` $\longleftrightarrow$ `인수 테스트 (Acceptance Testing)`
       - `시스템 분석 / 구조 설계 (Phân tích hệ thống)` $\longleftrightarrow$ `시스템 테스트 (System Testing)`
       - `상세 설계 (Thiết kế chi tiết)` $\longleftrightarrow$ `통합 테스트 (Integration Testing)`
       - `구현 / 코딩 (Hiện thực code)` $\longleftrightarrow$ `단위 테스트 (Unit Testing)`
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1 (Spiral Model):** Đề hỏi *"Mô hình nào do Boehm đề xuất và có hoạt động phân tích rủi ro (위험 분석)?"* -> **Chắc chắn là 나선형 모형 (Spiral Model)**.
  - **Bẫy 2 (V-Model):** Đề hỏi *"Kiểm thử đơn vị (단위 테스트) tương ứng với giai đoạn nào?"* -> **Tương ứng với 구현/코딩 (Hiện thực/Mã hóa)**. Hỏi *"Kiểm thử tích hợp (통합 테스트) tương ứng với giai đoạn nào?"* -> **Tương ứng với 설계 (Thiết kế)**.
  - **Bẫy 3 (Waterfall):** Đề hỏi *"Mô hình thác nước có dễ dàng tiếp nhận các thay đổi yêu cầu phát sinh giữa chừng không?"* -> **Hoàn toàn KHÔNG (적용하기 어려움)**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Thác nước tuần tự, Bản mẫu lấy ý kiến, Xoắn ốc Boehm diệt rủi ro, Chữ V đối xứng Dev-Test".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **So sánh chiến lược ứng phó với rủi ro:**
  - Ở mô hình Thác nước, giả định mọi rủi ro đã được tính toán kỹ và yêu cầu đóng băng (freeze). Khi có biến cố lớn, chi phí đập đi xây lại là cực lớn.
  - Ở mô hình Xoắn ốc, rủi ro được coi là yếu tố trung tâm. Trước khi tiến hành bất kỳ đợt phát triển nào (viết code), đội dự án phải thực hiện bước `위험 분석` (đánh giá rủi ro về nhân sự, kinh phí, công nghệ). Nếu rủi ro vượt ngưỡng cho phép, dự án có thể dừng lại ngay để tránh tổn thất.
- **Ví dụ phân biệt thực tế:**
  - **Waterfall:** Hệ thống tính lương nhà nước, luật đã ban hành rõ ràng, yêu cầu không thay đổi.
  - **Prototype:** Ứng dụng đặt món ăn với giao diện người dùng mới lạ, cần làm mockup cho khách hàng bấm thử để xem thao tác có thuận tiện không.
  - **Spiral:** Phát triển hệ thống điều khiển tàu vũ trụ hoặc lò phản ứng hạt nhân; chi phí thất bại cực lớn, bắt buộc phải có phân tích rủi ro nhiều vòng.
  - **V-Model:** Phần mềm thiết bị y tế (máy thở, máy đo nhịp tim) hoặc hệ thống phanh ABS ô tô, đòi hỏi kiểm thử nghiêm ngặt tương ứng từng mức thiết kế.

### 복습 체크리스트
- [ ] Nhớ đặc trưng `선형 순차적` và `이전 단계로 돌아갈 수 없음` của 폭포수 모형 (Waterfall).
- [ ] Nhớ tên nhà khoa học Boehm gắn liền với 나선형 모형 (Spiral) và từ khóa 핵심: 위험 분석 (Phân tích rủi ro).
- [ ] Thuộc chu trình 4 bước của 나선형 모형: 계획 수립 -> 위험 분석 -> 개발 및 검증 -> 고객 평가.
- [ ] Vẽ và ánh xạ được 4 cặp đối xứng trong V-모형 (요구사항-인수, 분석-시스템, 설계-통합, 구현-단위).
