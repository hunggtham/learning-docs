# 소프트웨어 생명 주기 및 개발 방법론 (SDLC & Methodologies)

## 학습 목표 (Mục tiêu)
- Nắm vững khái niệm cơ bản về Vòng đời phát triển phần mềm (`소프트웨어 생명 주기` - SDLC) và bối cảnh ra đời của kỹ nghệ phần mềm (`소프트웨어 공학`).
- Phân biệt rõ ràng giữa Vòng đời phần mềm (Khung tiến trình: Định nghĩa -> Vận hành -> Bảo trì) và Phương pháp luận phát triển (Cách thức tổ chức thực hiện như Waterfall, Agile).
- Nhận diện các giai đoạn cơ bản trong vòng đời phần mềm cùng các sản phẩm bàn giao (`산출물`) cốt lõi ở từng mốc.

## 핵심 키워드 (Từ khóa)
- 소프트웨어 생명 주기 (Vòng đời phát triển phần mềm / Software Development Life Cycle - SDLC)
- 소프트웨어 위기 (Khủng hoảng phần mềm / Software Crisis)
- 소프트웨어 공학 (Kỹ nghệ phần mềm / Software Engineering)
- 개발 방법론 (Phương pháp luận phát triển / Development Methodology)
- 산출물 (Sản phẩm bàn giao / Deliverables)
- 유지보수 (Bảo trì phần mềm / Software Maintenance)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ khởi đầu toàn bộ chương trình:** Đây là bài học mở đầu của Môn 1 (소프트웨어 설계). Mọi dự án công nghệ thông tin đều phải đặt trong một khung tiến trình vòng đời để kiểm soát chất lượng, tiến độ và chi phí.
- **Tiếp nối sang bài sau ([1. 소프트웨어 생명 주기](02-bai-hoc.md)):** Sau khi nắm bức tranh tổng thể về SDLC, bài tiếp theo sẽ phân tích sâu 4 mô hình vòng đời kinh điển: Thác nước (폭포수), Nguyên mẫu (프로토타입), Xoắn ốc (나선형 - Boehm) và Chữ V (V-모형).

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để nắm định nghĩa chuẩn xác thi trắc nghiệm: SDLC là gì, mục tiêu giải quyết cuộc khủng hoảng phần mềm, và sự khác biệt bản chất giữa khung vòng đời và phương pháp luận.
- Đọc TẦNG B để hiểu logic phân chia giai đoạn và tầm quan trọng sống còn của việc phát hiện lỗi sớm ngay từ khâu phân tích yêu cầu.

---

## 소프트웨어 생명 주기 및 개발 방법론 (SDLC & Methodologies)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **개념 (Định nghĩa SDLC):** Là toàn bộ quá trình từ khi phần mềm được hình thành ý tưởng, phát triển, vận hành cho đến khi ngừng sử dụng, được chia thành các giai đoạn tuần tự có kiểm soát (`정의, 운용, 유지보수 등의 과정을 각 단계별로 나눈 것`).
- **핵심 키워드 (Từ khóa nhận diện đề thi):**
  - `소프트웨어 생명 주기` (SDLC / Software Life Cycle)
  - `소프트웨어 위기 극복` (vượt qua khủng hoảng phần mềm)
  - `단계별 산출물 명확화` (làm rõ sản phẩm bàn giao từng bước)
  - `프로세스 모형 / 패러다임` (mô hình tiến trình / khuôn mẫu công nghệ)
- **시험 포인트 (Điểm thi trọng tâm):**
  - **Mục đích của SDLC:** Tiêu chuẩn hóa quy trình phát triển, nâng cao năng suất (`생산성 향상`) và chất lượng (`품질 향상`), tối ưu hóa việc quản lý chi phí, nhân lực và lịch trình dự án.
  - **Các giai đoạn kinh điển của SDLC:**
    1. `타당성 검토` (Khảo sát tính khả thi)
    2. `요구사항 분석` (Phân tích yêu cầu -> Đầu ra là Tài liệu đặc tả SRS)
    3. `설계` (Thiết kế kiến trúc, dữ liệu, giao diện)
    4. `구현 (코딩)` (Hiện thực / Lập trình)
    5. `테스트 (검사)` (Kiểm thử chức năng và phi chức năng)
    6. `운용 및 유지보수` (Vận hành và bảo trì - chiếm chi phí cao nhất trong vòng đời)
  - **Khủng hoảng phần mềm (소프트웨어 위기):** Hiện tượng chi phí phần mềm tăng vọt vượt phần cứng, chậm tiến độ, phát sinh vô số lỗi do thiếu quy trình kỹ nghệ bài bản.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** Đề hỏi *"SDLC chỉ bao gồm giai đoạn coding và test?"* -> **Sai**. SDLC bao trùm toàn bộ từ khảo sát tính khả thi cho đến bảo trì sau triển khai.
  - **Bẫy 2:** Đề hỏi *"Giai đoạn nào tốn kém chi phí nhất trong vòng đời phần mềm?"* -> **Đáp án là Bảo trì (유지보수)**, thường chiếm tới 60-70% tổng chi phí vòng đời.
  - **Bẫy 3:** Đánh đồng `소프트웨어 생명 주기 (SDLC)` với `개발 방법론 (Methodology)`. SDLC là khung giai đoạn (What & When), còn Phương pháp luận là cách thức triển khai cụ thể (How - như Waterfall hay Agile).
- **한 문장 설명 (Câu chốt ghi nhớ):** "SDLC là khung quản lý chia nhỏ vòng đời từ yêu cầu đến bảo trì, lấy sản phẩm bàn giao từng mốc làm thước đo chất lượng".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Bản chất của kỹ nghệ phần mềm và quy tắc phát hiện lỗi sớm:**
  - Nếu một lỗi ở khâu Phân tích yêu cầu (`요구사항 분석`) không được phát hiện mà trôi sang giai đoạn Bảo trì (`유지보수`), chi phí khắc phục có thể gấp từ 50 đến 100 lần so với việc sửa ngay tại giai đoạn yêu cầu. Do đó, SDLC đặt ra các mốc phê duyệt (Baseline) và sản phẩm bàn giao (Deliverables) ở cuối mỗi bước.
- **Ví dụ thực tế dễ hiểu:**
  - Xây dựng một ứng dụng ngân hàng di động: Không thể cho lập trình viên mở IDE ra viết code ngay. Trước hết phải khảo sát người dùng cần chuyển tiền, quét QR (Yêu cầu), thiết kế giao diện và cơ sở dữ liệu bảo mật (Thiết kế), viết mã nguồn (Hiện thực), kiểm thử tải và bảo mật (Kiểm thử), đưa lên kho ứng dụng và nâng cấp định kỳ (Vận hành & Bảo trì). Toàn bộ chuỗi tiến trình này chính là SDLC.
- **Mối liên hệ mạch kiến thức:**
  - Khung SDLC định hình cấu trúc cho toàn bộ Môn 1 (Thiết kế), Môn 2 (Phát triển & Kiểm thử), và Môn 5 (Quản lý hệ thống).

### 복습 체크리스트
- [ ] Định nghĩa được 소프트웨어 생명 주기 (SDLC) gồm các giai đoạn cốt lõi nào.
- [ ] Phân biệt được mục đích của SDLC trong việc khắc phục 소프트웨어 위기 (Khủng hoảng phần mềm).
- [ ] Nhớ chính xác giai đoạn chiếm nhiều chi phí nhất trong SDLC là 유지보수 (Bảo trì).
- [ ] Phân biệt được khái niệm SDLC (khung vòng đời) và 개발 방법론 (phương pháp luận phát triển).
