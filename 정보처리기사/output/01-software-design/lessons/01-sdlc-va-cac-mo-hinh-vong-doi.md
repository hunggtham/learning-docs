# 소프트웨어 생명 주기 및 개발 모형 (Vòng đời phần mềm và Các mô hình phát triển)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và bối cảnh ra đời của Vòng đời phát triển phần mềm (`소프트웨어 생명 주기` - SDLC) nhằm vượt qua cuộc khủng hoảng phần mềm (`소프트웨어 위기`).
- Phân tích sâu sắc đặc trưng, ưu nhược điểm và phạm vi ứng dụng của 4 mô hình SDLC kinh điển: Mô hình Thác nước (`폭포수 모형`), Mô hình Nguyên mẫu (`프로토타입 모형`), Mô hình Xoắn ốc (`나선형 모형`), và Mô hình Chữ V (`V-모형`).
- Thuộc nằm lòng chu trình 4 giai đoạn lặp lại của mô hình Xoắn ốc do Boehm đề xuất và bảng ánh xạ 1-1 giữa các pha phát triển với các cấp độ kiểm thử trong V-Model.
- Làm chủ ma trận lựa chọn mô hình phát triển dựa trên mức độ ổn định của yêu cầu và kiểm soát rủi ro kỹ thuật.

## 핵심 키워드 (Từ khóa)
- 소프트웨어 생명 주기 (Vòng đời phát triển phần mềm / Software Development Life Cycle - SDLC)
- 소프트웨어 위기 (Khủng hoảng phần mềm / Software Crisis)
- 폭포수 모형 (Mô hình thác nước / Waterfall Model / 선형 순차적)
- 프로토타입 모형 (Mô hình nguyên mẫu / Prototype Model / 시제품)
- 나선형 모형 (Mô hình xoắn ốc / Spiral Model / Boehm / 점진적 모형)
- 위험 분석 (Phân tích rủi ro / Risk Analysis)
- V-모형 (Mô hình chữ V / V-Model / 단위·통합·시스템·인수 테스트)
- 유지보수 (Bảo trì phần mềm / Software Maintenance / 60~70% 비용)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin / Prerequisite):** Đây là bài học khởi đầu của toàn bộ chương trình Môn 1 (소프트웨어 설계). Mọi dự án công nghệ thông tin đều bắt nguồn từ nhu cầu vượt qua "Khủng hoảng phần mềm" (chi phí phần cứng giảm nhưng chi phí phần mềm tăng vọt, trễ hạn và phát sinh vô số lỗi do phát triển tự phát không có quy trình kỹ nghệ kiểm soát).
- **Đang giải quyết gì (Current Problem):** Bài học này thiết lập khung quản lý tiến trình chuẩn từ khi hình thành ý tưởng, xác định yêu cầu, thiết kế, lập trình, kiểm thử cho đến khi vận hành và bảo trì; đồng thời so sánh 4 mô hình kinh điển để trả lời câu hỏi: Khi nào nên làm tuần tự dứt điểm, khi nào cần làm bản mẫu thử nghiệm, và khi nào bắt buộc phải đưa quản lý rủi ro vào từng vòng lặp?
- **Dùng đi đâu (Forward Handoff):** Các mô hình kinh điển (đặc biệt là Waterfall) dựa trên giả định yêu cầu có thể đóng băng và ổn định từ đầu. Khi bước vào kỷ nguyên dịch vụ số với yêu cầu biến động liên tục, các mô hình này bộc lộ sự chậm chạp, bàn giao trực tiếp sang [02-phuong-phap-luan-agile-scrum-xp.md](02-phuong-phap-luan-agile-scrum-xp.md) để khảo sát tư duy linh hoạt thích ứng (Agile, Scrum, XP).

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để ghi nhớ chuẩn xác các mẫu câu đề thi tiếng Hàn đi trước: nhận diện từ khóa `선형 순차적` gắn với Waterfall; `시제품` gắn với Prototype; `보헴(Boehm)` và `위험 분석` gắn với Spiral; bảng đối xứng 4 cấp độ Dev-Test của V-Model.
- Đọc TẦNG B để hiểu sâu bản chất chi phí phát hiện lỗi sớm (Cost of Change Curve) và tình huống đề thi trắc nghiệm đưa ra bài toán thực tế yêu cầu lựa chọn mô hình tối ưu.

---

## 소프트웨어 생명 주기 및 개발 모형

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Định nghĩa và Bản chất SDLC
- **핵심 원리 (Nguyên tắc cốt lõi):**
  - [Hàn/Anh]: `소프트웨어 생명 주기는 소프트웨어를 개발하기 위하여 정의, 운용, 유지보수 등의 과정을 각 단계별로 나눈 것이다.`
  - [Tiếng Việt]: Vòng đời phần mềm (SDLC) là khung quản lý chia nhỏ toàn bộ tiến trình từ xác định bài toán, vận hành cho đến bảo trì thành các giai đoạn có mốc kiểm soát rõ ràng, lấy sản phẩm bàn giao (`산출물 - Deliverables`) ở từng mốc làm thước đo chất lượng.
- **Mục đích tối thượng của SDLC:** Khắc phục cuộc khủng hoảng phần mềm (`소프트웨어 위기 극복`), nâng cao năng suất (`생산성 향상`) và chất lượng (`품질 향상`), tối ưu hóa việc quản lý ngân sách và lịch trình.
- **Các giai đoạn kinh điển của SDLC:**
  1. `타당성 검토` (Khảo sát tính khả thi: kinh tế, kỹ thuật, pháp lý)
  2. `요구사항 분석` (Phân tích yêu cầu $\rightarrow$ tạo tài liệu đặc tả SRS)
  3. `설계` (Thiết kế kiến trúc tổng thể, cơ sở dữ liệu, giao diện, module)
  4. `구현 (코딩)` (Hiện thực hóa thiết kế bằng mã nguồn)
  5. `테스트 (검사)` (Kiểm thử chức năng, phi chức năng, tích hợp)
  6. `운용 및 유지보수` (Vận hành thực tế và bảo trì sau triển khai)

#### 2. So sánh 4 mô hình SDLC kinh điển

##### A. 폭포수 모형 (Waterfall Model — Mô hình thác nước)
- **Đặc trưng nhận diện đề thi:**
  - [Hàn/Anh]: `가장 오래되고 폭넓게 사용된 전통적인 선형 순차적 개발 모형으로, 이전 단계로 돌아갈 수 없다는 전제로 각 단계가 완전히 끝나야 다음 단계로 진행된다.`
  - [Tiếng Việt]: Là mô hình cổ điển nhất, phát triển theo chuỗi thẳng tuần tự (`선형 순차적`). Giai đoạn trước phải kết thúc hoàn toàn và có sản phẩm bàn giao được phê duyệt (`검토·승인`) mới được chuyển sang giai đoạn sau; tiền đề là không quay lại giai đoạn trước.
- **Ưu điểm:** Quản lý tiến độ và phạm vi dễ dàng nhờ sản phẩm bàn giao minh bạch ở từng mốc.
- **Nhược điểm:** Cực kỳ kém linh hoạt trước các thay đổi yêu cầu; người dùng chỉ thấy được sản phẩm ở cuối chu trình; lỗi phát hiện muộn ở khâu kiểm thử dẫn đến chi phí khắc phục tăng vọt.

##### B. 프로토타입 모형 (Prototype Model — Mô hình nguyên mẫu)
- **Đặc trưng nhận diện đề thi:**
  - [Hàn/Anh]: `사용자의 요구사항을 정확히 파악하기 위해 실제 개발될 소프트웨어의 견본품(시제품)을 만들어 최종 결과물을 예측하게 하는 모형이다.`
  - [Tiếng Việt]: Nhằm nắm bắt chính xác yêu cầu của người dùng, đội dự án tạo ra một bản mẫu thử nghiệm (`시제품 - Prototype`) có giao diện và tính năng cơ bản để người dùng trải nghiệm thực tế, từ đó thu thập phản hồi và làm rõ các yêu cầu còn mơ hồ.
- **Ưu điểm:** Giảm thiểu rủi ro hiểu sai yêu cầu; tăng cường sự tham gia và đồng thuận của khách hàng.
- **Nhược điểm:** Dễ gây hiểu lầm cho khách hàng rằng hệ thống đã hoàn thiện; có thể tốn thời gian làm đi làm lại bản mẫu nếu không kiểm soát phạm vi; bản mẫu thường bỏ qua các tiêu chuẩn bảo mật và tối ưu hiệu năng.

##### C. 나선형 모형 (Spiral Model — Mô hình xoắn ốc)
- **Đặc trưng nhận diện đề thi:**
  - [Hàn/Anh]: `보헴(Boehm)이 제안한 모형으로, 폭포수와 프로토타입 모형의 장점에 위험 분석 기능을 추가하여 점진적으로 개발을 반복해 나가는 모형이다.`
  - [Tiếng Việt]: Do Barry Boehm đề xuất; kết hợp ưu điểm kiểm soát tuần tự của Waterfall và thử nghiệm của Prototype, bổ sung chức năng sống còn là **Phân tích rủi ro (`위험 분석`)** để phát triển tăng dần qua nhiều vòng lặp (`점진적 모형`).
- **Chu trình 4 bước lặp lại bất di bất dịch:**
  $$\text{계획 수립 (Lập kế hoạch)} \rightarrow \text{위험 분석 (Phân tích rủi ro)} \rightarrow \text{개발 및 검증 (Phát triển \& Xác minh)} \rightarrow \text{고객 평가 (Đánh giá của khách hàng)}$$
- **Phạm vi áp dụng:** Dự án quy mô lớn (`대규모 시스템`), độ phức tạp kỹ thuật cao, tiềm ẩn nhiều rủi ro công nghệ mới chưa được kiểm chứng.

##### D. V-모형 (V-Model — Mô hình chữ V)
- **Đặc trưng nhận diện đề thi:**
  - [Hàn/Anh]: `폭포수 모형의 변형으로, 개발 단계와 테스트 단계 간의 1:1 대응 관계를 시각화하여 품질 보증과 검증(Verification) 및 확인(Validation)을 강조한다.`
  - [Tiếng Việt]: Là biến thể tăng cường của Waterfall, nhấn mạnh mối quan hệ tương ứng 1-1 đối xứng giữa nhánh phát triển (nhánh trái đi xuống) và nhánh kiểm thử (nhánh phải đi lên) nhằm bảo đảm chất lượng toàn diện.
- **Bảng ánh xạ 1-1 giữa Pha phát triển và Cấp độ kiểm thử:**

| Nhánh phát triển (Trái $\downarrow$) | Nhánh kiểm thử tương ứng (Phải $\uparrow$) | Mục tiêu kiểm tra cốt lõi |
|:---|:---|:---|
| **요구사항 분석** (Phân tích yêu cầu) | **인수 테스트** (Acceptance Testing) | Xác nhận đáp ứng đúng nhu cầu nghiệp vụ của người dùng cuối |
| **시스템 설계** (Thiết kế hệ thống) | **시스템 테스트** (System Testing) | Kiểm tra toàn bộ hệ thống về hiệu năng, bảo mật, tải |
| **상세 설계** (Thiết kế chi tiết) | **통합 테스트** (Integration Testing) | Kiểm tra sự tương tác và giao tiếp giữa các module |
| **구현 / 코딩** (Hiện thực mã nguồn) | **단위 테스트** (Unit Testing) | Kiểm tra tính đúng đắn của từng hàm, phương thức, lớp |

#### 3. Ma trận lựa chọn mô hình phát triển (Development Model Selection)

| Tiêu chí so sánh | 폭포수 (Waterfall) | 프로토타입 (Prototype) | 나선형 (Spiral) | 애자일 (Agile) |
|:---|:---|:---|:---|:---|
| **Độ ổn định của yêu cầu** | Đã xác định rõ, cố định | Rất mơ hồ, chưa rõ ràng | Phức tạp, dễ phát sinh | Biến động liên tục |
| **Trọng tâm quản lý** | Kế hoạch & Sản phẩm bàn giao | Trải nghiệm người dùng | Quản lý rủi ro (Risk) | Khách hàng & Giá trị chạy được |
| **Quy mô dự án tối ưu** | Trung bình, hợp đồng cứng | Nhỏ đến trung bình | Lớn đến rất lớn | Nhỏ đến trung bình, linh hoạt |
| **Chi phí thay đổi muộn** | Cực kỳ cao | Thấp ở đầu, cao ở sau | Trung bình (đã diệt rủi ro) | Thấp (thích ứng ngắn) |

#### 4. Bẫy đề thi trắc nghiệm thường gặp (주의/함정)
- **Bẫy 1 (Chi phí trong vòng đời):** Đề hỏi *"Giai đoạn nào chiếm tỷ trọng chi phí và nhân lực lớn nhất trong SDLC?"* $\rightarrow$ **Đáp án: Bảo trì (`유지보수`)**, thường chiếm từ 60% đến 70% tổng chi phí toàn bộ vòng đời phần mềm.
- **Bẫy 2 (Nhận diện Spiral):** Cứ thấy xuất hiện tên nhà khoa học **Boehm (`보헴`)** hoặc cụm từ **위험 분석 (`Phân tích rủi ro`)** lặp lại theo vòng xoắn thì chắc chắn là **나선형 모형 (Spiral Model)**.
- **Bẫy 3 (Ánh xạ V-Model):** Đề hay hỏi gài *"Kiểm thử tích hợp (통합 테스트) kiểm tra kết quả của giai đoạn nào?"* $\rightarrow$ **Tương ứng với Thiết kế chi tiết / Thiết kế module (`상세 설계`)**, không phải giai đoạn coding.
- **Bẫy 4 (Đồng nhất SDLC và Methodology):** `소프트웨어 생명 주기 (SDLC)` là khung toàn bộ vòng đời (What & When); còn `개발 방법론 (Methodology)` như Waterfall, Agile là cách tổ chức thực hiện cụ thể (How). Không được đánh đồng hai khái niệm.

- **한 문장 설명 (Câu chốt ghi nhớ):** "Thác nước tuần tự đóng băng mốc, Bản mẫu khai thông yêu cầu mờ, Xoắn ốc Boehm diệt trừ rủi ro, Chữ V đối xứng Dev đi kèm Test".

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Quy luật chi phí phát hiện lỗi sớm (Cost of Change Curve)
- Theo nghiên cứu kinh điển của Barry Boehm, nếu một lỗi sai lệch về mặt yêu cầu được phát hiện ngay tại giai đoạn Phân tích yêu cầu (`요구사항 분석`), chi phí sửa đổi được quy chuẩn là $1\times$.
- Nếu lỗi đó trôi qua giai đoạn Thiết kế $\rightarrow$ chi phí tăng lên $3\times - 5\times$.
- Nếu trôi sang giai đoạn Coding $\rightarrow$ chi phí tăng $10\times$.
- Nếu trôi sang giai đoạn Kiểm thử hệ thống $\rightarrow$ chi phí tăng $20\times - 50\times$.
- Nếu phần mềm đã triển khai thực tế và lỗi chỉ phát hiện ở giai đoạn Bảo trì vận hành $\rightarrow$ chi phí khắc phục có thể lên tới **$100\times$ đến $200\times$** do phải thu hồi sản phẩm, đền bù hợp đồng và viết lại kiến trúc nền tảng.
- *Ý nghĩa sư phạm:* Đây chính là lý do vì sao SDLC đặt ra các mốc phê duyệt nghiêm ngặt và sản phẩm bàn giao tiêu chuẩn (`산출물`) để phát hiện và ngăn chặn lỗi trôi dạt sang các pha sau.

#### 2. Cơ chế phân tích rủi ro trong mô hình Xoắn ốc (Spiral Model Deep-Dive)
Mỗi vòng xoắn (Iteration) của mô hình Spiral mở rộng hệ thống theo chiều bán kính tăng dần và luôn tuân thủ đúng 4 góc phần tư:
1. **Góc phần tư 1 — 계획 수립 (Planning):** Xác định mục tiêu, các phương án thay thế và ràng buộc của vòng lặp hiện tại.
2. **Góc phần tư 2 — 위험 분석 (Risk Analysis):** Đội ngũ chuyên gia nhận diện các mối nguy kỹ thuật (ví dụ: công nghệ CSDL phân tán có chịu tải nổi 100.000 TPS không?), ước lượng thiệt hại và tiến hành làm thực nghiệm/nguyên mẫu kỹ thuật để triệt tiêu rủi ro.
3. **Góc phần tư 3 — 개발 및 검증 (Engineering):** Khi rủi ro đã ở mức an toàn, tiến hành thiết kế chi tiết, viết code và kiểm thử mức tương ứng.
4. **Góc phần tư 4 — 고객 평가 (Evaluation):** Bàn giao kết quả vòng lặp cho khách hàng đánh giá; sự hài lòng và phản hồi của khách hàng quyết định phạm vi công việc cho vòng xoắn tiếp theo. Nếu rủi ro vượt quá ngân sách chịu đựng, dự án có thể hủy bỏ ngay để cắt lỗ.

#### 3. Phân tích tình huống đề thi trắc nghiệm (Case Analysis)
- **Tình huống 1:** *"Một cơ quan chính phủ mở thầu xây dựng Hệ thống quản lý cơ sở dữ liệu đất đai quốc gia. Luật đất đai và các biểu mẫu hành chính đã được ban hành cố định, nhà thầu phải nộp đầy đủ hồ sơ thiết kế và nghiệm thu từng giai đoạn dứt điểm để giải ngân ngân sách. Nên chọn mô hình nào?"*
  - **Phân tích:** Yêu cầu hoàn toàn cố định, quy định pháp lý minh bạch, cần sản phẩm bàn giao chặt chẽ cho từng mốc thanh toán. $\rightarrow$ **Chọn 폭포수 모형 (Waterfall Model)**.
- **Tình huống 2:** *"Một công ty công nghệ muốn phát triển hệ thống điều khiển tự động cho tên lửa đẩy vũ trụ. Chi phí phóng thử thất bại là hàng trăm triệu USD và ảnh hưởng nghiêm trọng đến an toàn. Đội ngũ kỹ sư cần nghiên cứu vật liệu mới và phần mềm điều hướng chưa từng có tiền lệ. Mô hình nào tối ưu nhất?"*
  - **Phân tích:** Dự án quy mô siêu lớn, độ bất định công nghệ cực cao, rủi ro tài chính khổng lồ $\rightarrow$ **Chọn 나선형 모형 (Spiral Model)** với chức năng trọng tâm là `위험 분석` qua từng vòng thử nghiệm.

---

### 복습 체크리스트
- [ ] Nhớ chính xác 6 giai đoạn cơ bản của SDLC và nhận diện `유지보수` là giai đoạn tốn kém chi phí nhất.
- [ ] Phân biệt được đặc trưng `선형 순차적` và `이전 단계 복귀 불가` của Waterfall Model.
- [ ] Nhớ từ khóa `시제품 (bản mẫu thử nghiệm)` gắn liền với Prototype Model.
- [ ] Đọc vanh vách tên nhà khoa học Boehm và chu trình 4 bước của Spiral Model: 계획 수립 $\rightarrow$ 위험 분석 $\rightarrow$ 개발 및 검증 $\rightarrow$ 고객 평가.
- [ ] Vẽ và ánh xạ chính xác 4 cặp đối xứng trong V-Model: Phân tích yêu cầu $\leftrightarrow$ Kiểm thử chấp nhận; Thiết kế hệ thống $\leftrightarrow$ Kiểm thử hệ thống; Thiết kế chi tiết $\leftrightarrow$ Kiểm thử tích hợp; Hiện thực code $\leftrightarrow$ Kiểm thử đơn vị.
- [ ] Nắm vững ma trận lựa chọn mô hình SDLC theo độ ổn định của yêu cầu và mức độ rủi ro kỹ thuật.
