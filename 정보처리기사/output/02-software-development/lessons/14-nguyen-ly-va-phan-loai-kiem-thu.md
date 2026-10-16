# 소프트웨어 테스트 기본 원리와 분류 (Nguyên lý và phân loại kiểm thử)

## 학습 목표
- Nắm vững 7 nguyên lý kiểm thử phần mềm theo chuẩn quốc tế ISTQB: Chứng minh có lỗi (`결함 존재 증명`), Không thể kiểm thử kiệt quệ (`완벽한 테스팅 불가능`), Kiểm thử sớm (`조기 테스팅`), Tập trung lỗi (`결함 집중` / Pareto 80:20), Nghịch lý thuốc trừ sâu (`살충제 패러독스`), Phụ thuộc ngữ cảnh (`정황 의존성`), và Ngụy biện vắng bóng lỗi (`오류-부재의 궤변`).
- Phân biệt sâu sắc giữa Kiểm tra xác minh (`검증 / Verification` - Are we building the product right?) và Kiểm tra xác nhận (`확인 / Validation` - Are we building the right product?).
- Phân loại kiểm thử theo trạng thái thực thi: Kiểm thử tĩnh (`정적 테스트` - Desk checking, Walkthrough, Inspection) và Kiểm thử động (`동적 테스트` - Chạy chương trình thật).
- Nắm vững các loại hình kiểm thử theo mục đích đặc biệt: Hồi quy (`회귀 / Regression`), Phục hồi sự cố (`회복 / Recovery`), An ninh bảo mật (`안전 / Security`), Chịu tải quá mức (`강도 / Stress`), và Hiệu năng (`성능 / Performance`).

## 핵심 키워드
- 소프트웨어 테스트 7대 원리 (7 nguyên lý kiểm thử ISTQB)
- 결함 존재 증명 (Testing shows presence of defects / 결함 없음 증명 불가)
- 살충제 패러독스 (Pesticide Paradox / ca test cũ bị nhờn lỗi)
- 결함 집중 (Defect Clustering / 파레토 법칙 80:20)
- 오류-부재의 궤변 (Absence-of-Errors Fallacy)
- 검증 vs 확인 (Verification vs Validation / Barry Boehm)
- 회귀 테스트 (Regression Testing / 변경 후 사이드 이펙트 검증)
- 강도 테스트 (Stress Testing / 과부하 한계 시험)

## 선행·연결 개념
- **Từ đâu (Origin / Prerequisite):** Ở bài học trước [13-ide-va-tu-dong-hoa-build.md](13-ide-va-tu-dong-hoa-build.md), chúng ta đã tự động hóa việc build và đóng gói sản phẩm phần mềm.
- **Đang giải quyết gì (Current Problem):** Kiểm thử không phải là công việc mò tìm lỗi ngẫu nhiên mà là một quy trình kỹ thuật có phương pháp luận. Bài học này thiết lập hệ thống 7 nguyên lý nền tảng, phân biệt góc nhìn nhà phát triển (Verification) với người dùng (Validation) và phân loại các mục đích kiểm thử chuyên biệt.
- **Dùng đi đâu (Forward Handoff):** Sau khi nắm vững lý thuyết kiểm thử tổng quát, bài học tiếp theo [15-kiem-thu-hop-trang-va-coverage.md](15-kiem-thu-hop-trang-va-coverage.md) sẽ đi sâu vào kỹ thuật Kiểm thử hộp trắng dựa trên cấu trúc mã nguồn nội bộ.

## 읽는 방법
- Đọc TẦNG A để thuộc lòng 7 nguyên lý kiểm thử ISTQB, bảng đối đầu Verification vs Validation, bảng phân loại kiểm thử theo mục đích và các bẫy trắc nghiệm.
- Đọc TẦNG B để hiểu sâu giải thích song ngữ từng nguyên lý, các bẫy đề thi hay nhầm lẫn giữa Pesticide Paradox và Defect Clustering, và quy trình kiểm thử chuẩn.

---

## 소프트웨어 테스트 기본 원리와 분류

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng 7 nguyên lý kiểm thử phần mềm chuẩn ISTQB
| Nguyên lý | Tên tiếng Hàn & Anh | Bản chất kỹ thuật cốt lõi |
| :--- | :--- | :--- |
| **1. Chứng minh có lỗi** | **결함 존재 증명 (Presence of defects)** | Kiểm thử chỉ chứng minh sự tồn tại của lỗi, **tuyệt đối không thể chứng minh phần mềm sạch 100% không còn lỗi** |
| **2. Không thể test kiệt quệ** | **완벽한 테스팅 불가능 (Exhaustive testing)** | Không thể kiểm thử toàn bộ mọi tổ hợp dữ liệu vào và điều kiện; phải ưu tiên dựa trên rủi ro |
| **3. Kiểm thử sớm** | **조기 테스팅 (Early Testing)** | Tiến hành kiểm thử càng sớm càng tốt từ pha yêu cầu để tiết kiệm tối đa chi phí sửa lỗi (chi phí tăng gấp 60-100 lần ở pha vận hành) |
| **4. Tập trung lỗi** | **결함 집중 (Defect Clustering)** | **Quy luật Pareto 80:20**: Khoảng 80% lỗi thường tập trung ở 20% mô-đun phức tạp nhất |
| **5. Nghịch lý thuốc trừ sâu** | **살충제 패러독스 (Pesticide Paradox)** | Chạy mãi một bộ Test Case cũ sẽ làm hệ thống "nhờn lỗi", **bắt buộc phải định kỳ cập nhật và bổ sung ca test mới** |
| **6. Phụ thuộc ngữ cảnh** | **정황 의존성 (Context dependent)** | Không có một chiến lược test duy nhất cho mọi dự án; y tế, hàng không đòi hỏi tiêu chuẩn khắt khe hơn mạng xã hội |
| **7. Ngụy biện vắng bóng lỗi** | **오류-부재의 궤변 (Absence-of-errors)** | Dù sửa sạch 100% lỗi kỹ thuật nhưng sản phẩm **không đáp ứng nhu cầu thực tế của người dùng** thì phần mềm vẫn thất bại |

#### 2. Phân loại kiểm thử theo trạng thái thực thi: Kiểm thử tĩnh vs Kiểm thử động

```text
                           [PHÂN LOẠI KIỂM THỬ PHẦN MỀM]
                                        │
             ┌──────────────────────────┴──────────────────────────┐
             ▼                                                     ▼
    [THEO TRẠNG THÁI CHẠY MÃ]                             [THEO MỤC ĐÍCH KIỂM THỬ]
    ├─ 정적 테스트 (Static - Không chạy mã)                 ├─ 회귀 (Regression - Chống tác dụng phụ)
    │  ├─ 동료 검토 (Peer Review)                         ├─ 회복 (Recovery - Khôi phục sau sập)
    │  ├─ 워크스루 (Walkthrough - Tác giả dẫn)             ├─ 안전 (Security - Chống tấn công mạng)
    │  ├─ 인스펙션 (Inspection - Moderator chủ tọa)        ├─ 강도 (Stress - Tải cực hạn vượt ngưỡng)
    │  └─ 정적 분석 (Static Code Analysis)                ├─ 부하 (Load - Tăng tải tìm điểm nghẽn)
    │                                                      ├─ 성능 (Performance - Đo phản hồi/thông lượng)
    └─ 동적 테스트 (Dynamic - Thực thi mã thật)             └─ 구조 (Structure - Kiểm tra độ phủ mã)
       ├─ 화이트박스 테스트 (White-box - Cấu trúc nội bộ)
       └─ 블랙박스 테스트 (Black-box - Chức năng bên ngoài)
```

| Tiêu chí | 정적 테스트 (Static Testing — Kiểm thử tĩnh) | 동적 테스트 (Dynamic Testing — Kiểm thử động) |
|:---|:---|:---|
| **Cơ chế thực thi** | **KHÔNG THỰC THI MÃ NGUỒN (코드 실행 없음)** | **BẮT BUỘC THỰC THI CHƯƠNG TRÌNH (코드 실행 필수)** |
| **Đối tượng kiểm tra** | Tài liệu đặc tả yêu cầu, thiết kế kiến trúc, mã nguồn thô | Chương trình thực thi, file nhị phân đang chạy |
| **Thời điểm áp dụng** | Rất sớm, ngay từ giai đoạn khởi đầu dự án | Sau khi đã có mã nguồn chạy được (từ Unit Test trở đi) |
| **Kỹ thuật tiêu biểu** | **Walkthrough, Inspection, Peer Review, Static Analysis** | **White-box Testing, Black-box Testing** |

##### Phân biệt hai kỹ thuật thẩm tra tĩnh cốt lõi: Walkthrough vs Inspection
- **워크스루 (Walkthrough):**
  - Buổi họp do **chính tác giả của tài liệu/mã nguồn chủ trì và dẫn dắt**.
  - Không chính thức (Informal); mục tiêu chính là giới thiệu sản phẩm, phát hiện lỗi sơ bộ và chia sẻ kiến thức, đào tạo đồng nghiệp.
- **인스펙션 (Inspection — Fagan Inspection):**
  - Quy trình kiểm tra chính quy và nghiêm ngặt nhất do **người điều phối độc lập (Moderator / 주임 검토자) chủ trì**, không phải tác giả.
  - Sử dụng danh sách kiểm tra chuẩn hóa (`Checklist`) và quy tắc định sẵn; lập biên bản ghi nhận lỗi chính thức và có bước theo dõi khắc phục (`Follow-up`).

#### 3. Đối chiếu Verification (검증) vs Validation (확인)

| Tiêu chuẩn so sánh | 검증 (Verification — Xác minh) | 확인 (Validation — Xác nhận) |
|:---|:---|:---|
| **Câu hỏi triết lý** | *"Are we building the product right?"* | *"Are we building the right product?"* |
| **Góc nhìn** | **Nhà phát triển (Developer)** | **Người dùng cuối (User / Customer)** |
| **Bản chất** | Kiểm tra xem sản phẩm có thỏa mãn đúng các đặc tả kỹ thuật và tài liệu thiết kế đã đề ra không | Kiểm tra xem sản phẩm có thỏa mãn đúng nhu cầu nghiệp vụ thực tế và mong đợi của khách hàng không |
| **Phương pháp tiêu biểu** | Đánh giá tài liệu, Walkthrough, Inspection, Unit Test | Kiểm thử hệ thống, **Kiểm thử chấp nhận (Acceptance Test)**, Beta Test |

#### 4. Bảng phân loại kiểm thử theo mục đích đặc biệt

| Loại hình kiểm thử | Tên tiếng Hàn & Anh | Mục tiêu kiểm tra trọng tâm |
|:---|:---|:---|
| **Kiểm thử hồi quy** | **회귀 테스트 (Regression Test)** | Chạy lại các ca kiểm thử sau khi sửa lỗi hoặc nâng cấp mã nguồn để bảo đảm **không làm phát sinh lỗi mới (Side Effects)** |
| **Kiểm thử phục hồi** | **회복 테스트 (Recovery Test)** | Cố tình tạo sự cố hệ thống (ngắt điện, sập mạng) để đo lường khả năng tự khôi phục dữ liệu |
| **Kiểm thử an ninh** | **안전 테스트 (Security Test)** | Kiểm tra khả năng chống chịu trước các cuộc tấn công mạng, xâm nhập trái phép và bảo vệ dữ liệu nhạy cảm |
| **Kiểm thử chịu tải quá mức** | **강도 / 스트레스 테스트 (Stress Test)** | Nạp dữ liệu và lưu lượng truy cập **vượt quá ngưỡng thiết kế tối đa** để xem hệ thống sụp đổ ra sao và có cơ chế phòng vệ không |
| **Kiểm thử tải** | **부하 테스트 (Load Test)** | Tăng dần lưu lượng tải từ từ đến giới hạn định mức của hệ thống để xác định ngưỡng chịu tải và điểm nghẽn hiệu năng |
| **Kiểm thử hiệu năng** | **성능 테스트 (Performance Test)** | Đo thời gian phản hồi (Response Time), thông lượng xử lý (Throughput) trong điều kiện tải bình thường |

#### 5. Bẫy đề thi trắc nghiệm kinh điển (기출 함정 포인트)
- **Bẫy 1: Nhầm lẫn giữa Defect Clustering và Pesticide Paradox:**
  - Lỗi tập trung 80% ở 20% mô-đun phức tạp $\rightarrow$ **결함 집중 (Defect Clustering / Pareto)**.
  - Chạy mãi bộ test cũ không tìm thấy lỗi mới $\rightarrow$ **살충제 패러독스 (Pesticide Paradox)**.
- **Bẫy 2: Phân biệt Verification vs Validation:**
  - *"Building product right"* (làm đúng quy chuẩn kỹ thuật) $\rightarrow$ **검증 (Verification)**.
  - *"Building right product"* (làm đúng sản phẩm khách hàng cần) $\rightarrow$ **확인 (Validation)**.
- **Bẫy 3: Phân biệt Performance Test vs Stress Test vs Load Test:**
  - Đo thời gian phản hồi ở mức tải bình thường $\rightarrow$ **성능 테스트 (Performance)**.
  - Tăng tải từ từ đến giới hạn thiết kế để tìm điểm nghẽn $\rightarrow$ **부하 테스트 (Load)**.
  - Ép hệ thống chạy vượt quá mức cực hạn tối đa để thử độ chịu đựng và cơ chế phục hồi $\rightarrow$ **강도 테스트 (Stress)**.
- **Bẫy 4: Walkthrough vs Inspection:**
  - Tác giả chủ trì, không chính thức, đào tạo $\rightarrow$ **워크스루 (Walkthrough)**.
  - Người điều phối độc lập (Moderator) chủ trì, dùng Checklist chính quy $\rightarrow$ **인스펙션 (Inspection)**.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Định nghĩa chi tiết song ngữ 7 nguyên lý kiểm thử
1. **결함 존재 증명 (Testing shows presence of defects):**
   - [한국어]: 테스팅은 결함이 존재함을 보여줄 수 있지만, 결함이 없음을 증명할 수는 없다.
   - [Tiếng Việt]: Kiểm thử làm giảm xác suất lỗi còn sót lại nhưng không bao giờ là bằng chứng khẳng định phần mềm đúng tuyệt đối không còn lỗi.
2. **완벽한 테스팅 불가능 (Exhaustive testing is impossible):**
   - [한국어]: 모든 가능한 입력과 사전 조건의 조합을 테스트하는 것은 불가능하다.
   - [Tiếng Việt]: Không thể kiểm thử toàn bộ mọi tổ hợp dữ liệu vào và điều kiện; phải ưu tiên dựa trên rủi ro.
3. **조기 테스팅 (Early Testing):**
   - [한국어]: 테스팅 활동은 소프트웨어 생명 주기 초기 단계에서부터 시작되어야 한다.
   - [Tiếng Việt]: Tiến hành kiểm thử càng sớm càng tốt từ pha phân tích yêu cầu để tiết kiệm tối đa chi phí sửa lỗi.
4. **결함 집중 (Defect Clustering):**
   - [한국어]: 대부분의 결함은 소수의 특정 모듈에 집중되어 발견된다 (파레토 80:20).
   - [Tiếng Việt]: Khoảng 80% tổng số khiếm khuyết thường nằm trong khoảng 20% số mô-đun phức tạp nhất.
5. **살충제 패러독스 (Pesticide Paradox):**
   - [한국어]: 동일한 테스트를 반복하면 더 이상 새로운 결함을 찾아낼 수 없다.
   - [Tiếng Việt]: Chạy lặp đi lặp lại một bộ Test Case cũ sẽ làm hệ thống nhờn lỗi; bắt buộc phải cập nhật ca test mới.
6. **정황 의존성 (Testing is context dependent):**
   - [한국어]: 테스팅은 정황과 환경에 따라 다르게 수행되어야 한다.
   - [Tiếng Việt]: Chiến lược kiểm thử phải thay đổi linh hoạt tùy theo đặc thù nghiệp vụ của từng hệ thống.
7. **오류-부재의 궤변 (Absence-of-Errors Fallacy):**
   - [한국어]: 결함을 모두 제거했다고 하더라도 사용자의 요구사항을 만족시키지 못하면 성공적인 소프트웨어라 할 수 없다.
   - [Tiếng Việt]: Sửa hết lỗi kỹ thuật nhưng không đáp ứng đúng bài toán của người dùng thì phần mềm vẫn thất bại.

---

### 복습 체크리스트
- [ ] Kể tên đầy đủ 7 nguyên lý kiểm thử ISTQB.
- [ ] Phân biệt Defect Clustering (80% lỗi ở 20% module) và Pesticide Paradox (nhờn ca test cũ).
- [ ] Nhớ định nghĩa Barry Boehm: Verification (product right) vs Validation (right product).
- [ ] Định nghĩa 회귀 테스트 (Regression Test) là chạy lại test sau khi sửa mã để chống lỗi dây chuyền.
- [ ] Phân biệt Stress Test (vượt quá tải tối đa) và Performance Test (đo phản hồi bình thường).
