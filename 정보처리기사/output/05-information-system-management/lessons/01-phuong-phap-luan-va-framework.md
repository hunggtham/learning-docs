# 소프트웨어 개발 방법론 & 프레임워크 (Phương pháp luận phát triển phần mềm, SDLC & Framework)

## 학습 목표 (Mục tiêu)
- Nắm vững đặc trưng, triết lý vận hành và sự tiến hóa của các mô hình vòng đời phát triển phần mềm kinh điển: Thác nước (폭포수), Mẫu thử (프로토타입), Xoắn ốc (나선형), Mô hình chữ V (V-모델), và Linh hoạt (애자일).
- Phân biệt sự khác nhau giữa các phương pháp luận: Trọng tâm tiến trình (구조적 - Process-centric), Trọng tâm dữ liệu (정보공학 - Data-centric), Trọng tâm đối tượng (객체지향 - Object-centric), và Lắp ghép thành phần (CBD - Component-based).
- Làm chủ 4 đặc tính kiến trúc của Khung phát triển phần mềm (소프트웨어 프레임워크): 모듈화 (Modularity), 재사용성 (Reusability), 확장성 (Extensibility), 제어의 역전 (Inversion of Control / IoC).
- Phân loại chính xác các tiêu chí cắt may phương pháp luận (방법론 테일러링): Tiêu chí nội bộ (내부적 기준) vs Tiêu chí bên ngoài (외부적 기준).

## 핵심 키워드 (Từ khóa song ngữ)
- 소프트웨어 생명주기 (SDLC - Software Development Life Cycle)
- 폭포수 모형 (Waterfall Model — Tuyến tính, tuần tự, tài liệu hóa chặt chẽ)
- 나선형 모형 (Spiral Model — Barry Boehm, lặp lại kèm phân tích rủi ro)
- 구조적 방법론 (Structured Methodology — Process 중심, 분할과 정복, DFD)
- 정보공학 방법론 (Information Engineering — Data 중심, ERD)
- 컴포넌트 기반 방법론 (CBD — Component-Based Development, COTS 조립)
- 애자일 방법론 (Agile Methodology — 변화 대응, 고객 협업, 짧은 반복)
- 프레임워크 4대 특성 (Framework Characteristics — 모듈화, 재사용성, 확장성, 제어의 역전 IoC)
- 방법론 테일러링 (Methodology Tailoring — 내부적 기준 vs 외부적 기준)
- 전자정부 표준 프레임워크 (eGovFrame — Java Spring 기반 공공 표준)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Từ bài toán tổ chức dự án phần mềm quy mô lớn, việc lập trình tự phát dẫn đến khủng hoảng phần mềm (소프트웨어 위기). Để kiểm soát chất lượng và tiến độ, kỹ nghệ phần mềm đưa ra vòng đời SDLC và các phương pháp luận chuẩn.
- **Đang giải quyết gì (Current Problem):** Bài học này chuẩn hóa toàn bộ các mô hình vòng đời từ cổ điển đến hiện đại, so sánh các phương pháp luận theo trọng tâm kiến trúc, định nghĩa bản chất của Framework và cách cắt may quy trình (Tailoring) phù hợp với thực tế dự án.
- **Dùng đi đâu (Forward Handoff):** Sau khi xác định phương pháp luận và khung kiến trúc, dự án cần tận dụng tài sản sẵn có thông qua bài học [02-tai-su-dung-va-cong-cu-case.md](02-tai-su-dung-va-cong-cu-case.md) và thiết lập mô hình tính toán chi phí, lập tiến độ đường găng tại [03-quan-ly-du-an-chi-phi-va-tien-do.md](03-quan-ly-du-an-chi-phi-va-tien-do.md).

## 읽는 방법 (Cách đọc & Dấu hiệu nhận diện đề thi)
- **SDLC & Vòng đời:**
  - Nhắc đến **"선형 순차적" (Tuyến tính tuần tự)**, **"각 단계 검토·승인 후 진행" (Xét duyệt xong mới qua pha sau)** $\rightarrow$ Chọn ngay **폭포수 모형 (Waterfall)**.
  - Nhắc đến **"보헴 (Boehm)"**, **"점진적 개발" (Phát triển tăng dần)**, **"위험 분석" (Phân tích rủi ro)** $\rightarrow$ Chọn ngay **나선형 모형 (Spiral)**.
  - Nhắc đến **"테스트 단계와 개발 단계의 대칭 매핑" (Ánh xạ kiểm thử đối xứng)** $\rightarrow$ Chọn ngay **V-모델 (V-Model)**.
- **Phương pháp luận:**
  - Nhắc đến **"처리(Process) 중심"**, **"분할과 정복" (Chia để trị)**, **"DFD/DD"** $\rightarrow$ Chọn **구조적 (Structured)**.
  - Nhắc đến **"자료(Data) 중심"**, **"ERD"** $\rightarrow$ Chọn **정보공학 (Information Engineering)**.
  - Nhắc đến **"컴포넌트 조합/조립" (Lắp ghép thành phần)**, **"COTS"** $\rightarrow$ Chọn **CBD**.
- **Đặc tính Framework:** Phải thuộc nằm lòng bộ tứ: **모듈화, 재사용성, 확장성, 제어의 역전(IoC)**.
- **Tailoring:** Nhớ bẫy đề thi: **Pháp luật (법적 제약)** và **Tiêu chuẩn chất lượng (표준 품질)** luôn là **외부적 기준 (Tiêu chí bên ngoài)**.

---

## 소프트웨어 개발 방법론 & 프레임워크

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Mô hình vòng đời phát triển phần mềm (SDLC Models)
SDLC là khung phân chia quá trình phát triển thành các giai đoạn rõ ràng nhằm quản trị tiến độ, chất lượng và nhân lực.

- **폭포수 모형 (Waterfall Model) — Mô hình thác nước:**
  - **Khái niệm:** Mô hình tuyến tính tuần tự (선형 순차적), giai đoạn sau chỉ được bắt đầu khi sản phẩm đầu ra (산출물) của giai đoạn trước đã được rà soát và phê duyệt (검토·승인).
  - **핵심 포인트 (Điểm thi trọng tâm):**
    - `가장 오래되고 널리 사용된 전통적 생명주기 모형이다.` — Là mô hình cổ điển nhất, quản lý mốc bàn giao chặt chẽ.
    - `요구사항 변경이 어렵고, 후반부에 오류가 발견되면 수정 비용이 막대하다.` — Nhược điểm lớn nhất là khó thay đổi yêu cầu giữa chừng, rủi ro dồn về cuối kỳ.
- **프로토타입 모형 (Prototyping Model) — Mô hình mẫu thử:**
  - **Khái niệm:** Xây dựng phiên bản thử nghiệm trực quan (견본품) để người dùng trải nghiệm, từ đó làm rõ các yêu cầu chưa chắc chắn và giảm thiểu hiểu lầm.
- **나선형 모형 (Spiral Model) — Mô hình xoắn ốc (Barry Boehm):**
  - **Khái niệm:** Kết hợp ưu điểm tuần tự của Waterfall và tính linh hoạt của Prototype, phát triển tăng dần (점진적) qua nhiều vòng lặp xoắn.
  - **4 bước lặp tuần tự (반복 순서):**
    1. **계획 수립 (Planning):** Xác định mục tiêu, giải pháp và ràng buộc.
    2. **위험 분석 (Risk Analysis):** Nhận diện và đánh giá rủi ro kỹ thuật, chi phí (đặc trưng phân biệt lớn nhất).
    3. **개발 및 검증 (Engineering & Verification):** Xây dựng mẫu thử và kiểm thử chức năng.
    4. **고객 평가 (Customer Evaluation):** Thu thập phản hồi để lập kế hoạch cho vòng lặp kế tiếp.
- **V-모델 (V-Model) — Mô hình chữ V:**
  - **Khái niệm:** Mở rộng từ Waterfall, nhấn mạnh mối quan hệ đối xứng giữa giai đoạn phát triển (bên trái) và giai đoạn kiểm thử tương ứng (bên phải):
    - Phân tích yêu cầu (요구사항 분석) $\leftrightarrow$ Kiểm thử chấp nhận (인수 테스트).
    - Phân tích hệ thống (시스템 분석) $\leftrightarrow$ Kiểm thử hệ thống (시스템 테스트).
    - Thiết kế kiến trúc (아키텍처 설계) $\leftrightarrow$ Kiểm thử tích hợp (통합 테스트).
    - Thiết kế module chi tiết (단위 설계) $\leftrightarrow$ Kiểm thử đơn vị (단위 테스트).

#### 2. Đối chiếu các phương pháp luận phát triển phần mềm

| Phương pháp luận | Trọng tâm thiết kế (중심) | Nguyên lý kỹ thuật cốt lõi | Công cụ & Sản phẩm đại diện |
| :--- | :--- | :--- | :--- |
| **구조적 (Structured)** | **처리 / Tiến trình (Process)** | Chia để trị (분할과 정복), tiếp cận từ trên xuống (Top-down). | Sơ đồ dòng dữ liệu (DFD), Từ điển dữ liệu (DD), Mini-spec. |
| **정보공학 (Info Eng)** | **자료 / Dữ liệu (Data)** | Dữ liệu là tài sản chiến lược lâu dài, ổn định hơn quy trình. | Sơ đồ thực thể liên kết (ERD), Ma trận CRUD. |
| **객체지향 (OO)** | **객체 / Đối tượng (Object)** | Đóng gói (캡슐화), Kế thừa (상속), Đa hình (다형성). | Biểu đồ UML (Class Diagram, Use Case), Phương pháp OMT. |
| **CBD (Component-Based)** | **컴포넌트 / Linh kiện** | Lắp ghép các khối phần mềm có sẵn (COTS) như mảnh Lego. | Kho lưu trữ Component, Hợp đồng giao diện (Interface). |
| **애자일 (Agile)** | **사람·소통 / Con người** | Thích ứng linh hoạt với thay đổi, chu kỳ ngắn (1-4 tuần). | Scrum (Sprint, Backlog), XP (Pair Programming, TDD, CI). |

#### 3. Khung phát triển phần mềm (Software Framework)
- **개념 (Khái niệm):** Hệ thống phần mềm dạng bán thành phẩm (반제품), cung cấp sẵn kiến trúc chuẩn, các lớp trừu tượng và module dùng chung (kết nối CSDL, quản lý giao dịch, xử lý ngoại lệ, bảo mật).
- **프레임워크 4대 특성 (4 đặc tính cốt lõi):**
  1. **모듈화 (Modularity):** Đóng gói các chức năng thành các module độc lập, giảm thiểu phụ thuộc lỏng lẻo, tăng năng suất.
  2. **재사용성 (Reusability):** Cung cấp các giao diện và lớp dùng chung, cho phép tái sử dụng nhiều lần trong các ứng dụng khác nhau.
  3. **확장성 (Extensibility):** Hỗ trợ tính đa hình (다형성), cho phép tùy biến mở rộng logic nghiệp vụ mà không cần sửa mã nguồn gốc.
  4. **제어의 역전 (IoC - Inversion of Control):** Quyền điều khiển luồng thực thi được bàn giao cho Framework; Framework sẽ chủ động gọi mã của lập trình viên thay vì lập trình viên tự gọi thư viện (Hollywood Principle: *"Don't call us, we'll call you"*).
- **Hệ khung phổ biến:**
  - **Spring Framework:** Khung mã nguồn mở nền Java phổ biến toàn cầu, hạt nhân là IoC/DI và AOP.
  - **전자정부 표준 프레임워크 (eGovFrame):** Khung chuẩn chính phủ điện tử Hàn Quốc xây dựng dựa trên Spring Framework nhằm đồng bộ hạ tầng CNTT công và xóa bỏ tình trạng phụ thuộc vào nhà thầu tư nhân.
  - **Microsoft .NET Framework:** Khung phát triển đa ngôn ngữ (C#, VB.NET) chạy trên máy ảo CLR của Microsoft.

#### 4. Cắt may phương pháp luận (Methodology Tailoring)
- **개념 (Khái niệm):** Hoạt động điều chỉnh, bổ sung hoặc tinh giản các bước, thủ tục và sản phẩm bàn giao của phương pháp luận chuẩn sao cho vừa vặn với đặc thù dự án.
- **Bảng phân loại tiêu chí cắt may (Bẫy đề thi cực lớn):**

| Nhóm tiêu chí | Tên tiếng Hàn & Anh | Các yếu tố thực tế thuộc nhóm |
| :--- | :--- | :--- |
| **Tiêu chí nội bộ** | **내부적 기준 (Internal)** | - **목표 환경 (Môi trường mục tiêu):** Cấu hình HĐH, CSDL, phần cứng.<br>- **요구사항 (Yêu cầu):** Độ phức tạp nghiệp vụ, tần suất thay đổi.<br>- **프로젝트 규모 (Quy mô):** Ngân sách, thời hạn, số lượng nhân sự.<br>- **보유 기술 (Công nghệ sẵn có):** Trình độ, kinh nghiệm của đội ngũ. |
| **Tiêu chí bên ngoài** | **외부적 기준 (External)** | - **법적 제약사항 (Ràng buộc pháp lý):** Luật bảo vệ thông tin cá nhân (개인정보 보호법), quy định an ninh mạng bắt buộc.<br>- **표준 품질 기준 (Tiêu chuẩn chất lượng):** Yêu cầu tuân thủ chuẩn ISO/IEC 12207, CMMI từ khách hàng/nhà nước. |

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### Cơ chế Đảo ngược điều khiển (IoC) và Tiêm phụ thuộc (Dependency Injection)
- **Thư viện truyền thống (Library):** Ứng dụng nắm quyền điều khiển. Mã nguồn của bạn chủ động gọi các hàm trong thư viện khi cần.
- **Framework (IoC):** Framework nắm giữ vòng đời và luồng điều khiển của ứng dụng. Bạn viết các lớp nghiệp vụ, đăng ký với Framework; khi có sự kiện (ví dụ: HTTP Request đến), Framework sẽ tự động khởi tạo đối tượng, tiêm các phụ thuộc (DI) và kích hoạt phương thức của bạn.
- **Giá trị thực tế:** Nhờ IoC, lập trình viên thoát khỏi việc viết mã khởi tạo thủ công (như quản lý `Connection`, `Transaction`), giảm thiểu lỗi rò rỉ tài nguyên hệ thống.

#### Sự khác biệt giữa SDLC và Phương pháp luận phát triển
- **생명주기 (SDLC):** Là khung các mốc thời gian logic (Phân tích $\rightarrow$ Thiết kế $\rightarrow$ Cài đặt $\rightarrow$ Kiểm thử $\rightarrow$ Bảo trì).
- **방법론 (Methodology):** Là cách thức chi tiết, quy trình thực hiện, kỹ thuật, vai trò con người và biểu mẫu để hoàn thành các giai đoạn trong SDLC đó. Cùng một SDLC, bạn có thể triển khai bằng phương pháp luận Cấu trúc hoặc Agile.

---

### 복습 체크리스트
- [ ] Nhận diện được 4 mô hình SDLC: Waterfall (tuyến tính tuần tự), Prototyping (làm mẫu thử), Spiral (Barry Boehm, lặp lại + phân tích rủi ro), V-Model (kiểm thử đối xứng).
- [ ] Phân biệt được: Phương pháp cấu trúc lấy Xử lý (Process/DFD) làm trung tâm, Kỹ nghệ thông tin lấy Dữ liệu (Data/ERD) làm trung tâm, CBD là lắp ghép linh kiện (COTS).
- [ ] Đọc tên vanh vách 4 đặc tính của Framework: 모듈화 (Modularity), 재사용성 (Reusability), 확장성 (Extensibility), 제어의 역전 (IoC).
- [ ] Phân loại chính xác: Pháp luật (법적 제약) và Tiêu chuẩn chất lượng (표준 품질) là Tiêu chí bên ngoài (외부적 기준) của Tailoring.
