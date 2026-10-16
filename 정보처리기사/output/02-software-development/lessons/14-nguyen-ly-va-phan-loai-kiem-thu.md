# 애플리케이션 테스트 원리와 분류 체계 (Nguyên lý, phân loại và quy trình kiểm thử)

## 학습 목표
- Nắm vững 7 nguyên lý kiểm thử phần mềm chuẩn ISTQB: Chứng minh sự hiện diện của lỗi (`결함 존재 증명`), Kiểm thử kiệt quệ là bất khả thi, Kiểm thử sớm (`조기 테스팅`), Tập trung lỗi (`결함 집중 / 파레토 80:20`), Nghịch lý thuốc trừ sâu (`살충제 패러독스`), Phụ thuộc ngữ cảnh, và Ngụy biện về sự vắng bóng lỗi (`오류-부재의 궤변`).
- Phân biệt triệt để hai góc nhìn kiểm thử của Barry Boehm: Xác minh kỹ thuật (`검증 / Verification` - Are we building the product right?) vs Xác nhận người dùng (`확인 / Validation` - Are we building the right product?).
- So sánh các hình thức kiểm thử tĩnh (`정적 테스트`: Walkthrough bán chính thức, Inspection chính thức dùng checklist) và kiểm thử động (`동적 테스트`: nạp và chạy code).
- Phân biệt các loại hình kiểm thử chuyên biệt: Kiểm thử phục hồi (`회복`), Kiểm thử an toàn (`안전`), Kiểm thử áp lực (`강도 / Stress` - 과부하), Kiểm thử hiệu năng (`성능`), Kiểm thử hồi quy (`회귀 / Regression` - kiểm tra lỗi mới sau khi sửa code), và Kiểm thử song song (`병행`).
- Nắm vững quy trình 5 bước kiểm thử chuẩn ISTQB và phân biệt thời điểm tạo ra Test Case (ở bước Phân tích & Thiết kế) vs Test Procedure (ở bước Triển khai & Thực thi).

## 핵심 키워드
- 테스트 7대 원리 (7 nguyên lý kiểm thử / 결함 존재 증명, 결함 집중, 살충제 패러독스, 오류-부재의 궤변)
- 검증 vs 확인 (Verification 개발자 관점 vs Validation 사용자 관점)
- 정적 테스트 (Kiểm thử tĩnh / 워크스루 Walkthrough 비공식, 인스펙션 Inspection 공식 체크리스트)
- 목적별 테스트 (회복 Recovery, 안전 Security, 강도 Stress 과부하, 성능 Performance, 회귀 Regression)
- 테스트 프로세스 (계획·제어 → 분석·설계 Test Case → 구현·실현 Test Procedure → 평가 → 완료)

## 선행·연결 개념
- **Từ đâu (Origin / Prerequisite):** Ở bài học trước [13-ide-va-tu-dong-hoa-build.md](13-ide-va-tu-dong-hoa-build.md), chúng ta đã khảo sát các công cụ IDE và đường ống tự động hóa Build CI/CD.
- **Đang giải quyết gì (Current Problem):** Bài học này mở đầu Chương 4 về Quản lý kiểm thử ứng dụng, thiết lập hệ thống nguyên lý phương pháp luận chuẩn quốc tế ISTQB, ranh giới giữa kiểm tra kỹ thuật (Verification) với kiểm tra nhu cầu khách hàng (Validation), và quy trình kiểm thử 5 bước tiêu chuẩn.
- **Dùng đi đâu (Forward Handoff):** Từ hệ thống phân loại này, cơ sở thiết kế dựa trên cấu trúc mã nguồn bên trong sẽ bàn giao trực tiếp sang [15-kiem-thu-hop-trang-va-coverage.md](15-kiem-thu-hop-trang-va-coverage.md) để phân tích kiểm thử hộp trắng và độ bao phủ Coverage.

## 읽는 방법
- Đọc TẦNG A để thuộc lòng 7 nguyên lý kiểm thử, bảng đối chiếu Verification vs Validation, bảng nhận diện các loại kiểm thử chuyên biệt (Stress = 과부하, Regression = phát sinh lỗi mới), và vị trí sinh ra Test Case vs Test Procedure.
- Đọc TẦNG B để hiểu sâu bản chất quy luật Pareto 80:20 trong lỗi phần mềm và tiêu chí dừng kiểm thử (Exit Criteria).

---

## 애플리케이션 테스트 원리와 분류 체계

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng 7 nguyên lý kiểm thử phần mềm chuẩn ISTQB
| Nguyên lý | Tên tiếng Hàn & Anh | Bản chất kỹ thuật cốt lõi |
| :--- | :--- | :--- |
| **1. Chứng minh có lỗi** | **결함 존재 증명 (Shows presence)** | Kiểm thử chỉ tìm ra lỗi tồn tại, **tuyệt đối không thể chứng minh phần mềm hết sạch lỗi 100%** |
| **2. Bất khả thi kiệt quệ**| **완벽한 테스팅 불가능 (Exhaustive)** | Không thể thử hết mọi tổ hợp đầu vào và điều kiện; phải ưu tiên theo rủi ro |
| **3. Kiểm thử sớm** | **조기 테스팅 (Early Testing)** | Tiến hành kiểm thử từ pha phân tích yêu cầu để giảm chi phí sửa lỗi gấp 60-100 lần |
| **4. Tập trung lỗi** | **결함 집중 (Defect Clustering)** | **Quy luật Pareto 80:20**: Khoảng 80% lỗi tập trung ở 20% module phức tạp nhất |
| **5. Nghịch lý thuốc trừ sâu**| **살충제 패러독스 (Pesticide Paradox)**| Chạy mãi bộ Test Case cũ sẽ bị "nhờn lỗi", không tìm ra lỗi mới; phải định kỳ cập nhật |
| **6. Phụ thuộc ngữ cảnh**| **정황 의존성 (Context dependent)** | Phần mềm y tế/ngân hàng đòi hỏi kiểm thử nghiêm ngặt hơn ứng dụng giải trí |
| **7. Ngụy biện vắng lỗi**| **오류-부재의 궤변 (Absence-of-Errors)**| Sửa hết 100% lỗi kỹ thuật nhưng sản phẩm sai nhu cầu người dùng thì vẫn thất bại |

#### 2. Đối chiếu Verification (검증) vs Validation (확인)
| Tiêu chí | 검증 (Verification - Xác minh kỹ thuật) | 확인 (Validation - Xác nhận người dùng) |
| :--- | :--- | :--- |
| **Góc nhìn chủ thể** | **Nhà phát triển (Developer / Engineer)** | **Người dùng cuối (User / Customer)** |
| **Câu hỏi triết lý** | *"Are we building the product right?"* | *"Are we building the right product?"* |
| **Mục đích** | Đảm bảo sản phẩm tuân thủ đúng tài liệu thiết kế và quy chuẩn | Đảm bảo sản phẩm đáp ứng đúng nhu cầu nghiệp vụ thực tế |
| **Hoạt động tiêu biểu** | Code Review, Inspection, Walkthrough, **Unit Test, Integration Test** | **System Test, Acceptance Test**, Alpha Test, Beta Test |

#### 3. Bảng phân loại các loại hình kiểm thử chuyên biệt
| Loại kiểm thử | Tên tiếng Hàn & Anh | Mục đích & Từ khóa nhận diện đề thi |
| :--- | :--- | :--- |
| **Kiểm thử áp lực** | **강도 테스트 (Stress)** | Đưa hệ thống vào trạng thái **quá tải cực đoan (과부하)** vượt ngưỡng tối đa để xem hành vi sụp đổ |
| **Kiểm thử hồi quy** | **회귀 테스트 (Regression)** | Sau khi sửa lỗi hoặc đổi code, **chạy lại kiểm thử để đảm bảo không sinh ra lỗi mới (새로운 결함)** |
| **Kiểm thử phục hồi** | **회복 테스트 (Recovery)** | Cố tình gây sự cố (ngắt điện, đứt mạng) để đo khả năng tự khôi phục dữ liệu |
| **Kiểm thử an toàn** | **안전 테스트 (Security)** | Kiểm tra các lỗ hổng bảo mật, phân quyền, chống thâm nhập trái phép |
| **Kiểm thử hiệu năng** | **성능 테스트 (Performance)** | Đo thời gian đáp ứng (Response Time), thông lượng (Throughput) trong điều kiện chuẩn |
| **Kiểm thử song song** | **병행 테스트 (Parallel)** | Nhập cùng dữ liệu vào cả hệ thống mới và cũ để so sánh đối chiếu kết quả |

#### 4. Quy trình 5 bước kiểm thử chuẩn ISTQB
$$\mathbf{계획\ 및\ 제어} \longrightarrow \mathbf{분석\ 및\ 설계} \longrightarrow \mathbf{구현\ 및\ 실현} \longrightarrow \mathbf{평가} \longrightarrow \mathbf{완료}$$
- **테스트 케이스 (Test Case):** Sinh ra ở bước **분석 및 설계 (Phân tích & Thiết kế)**; xác định *CẦN TEST CÁI GÌ* (điều kiện, input, expected output).
- **테스트 프로시저 (Test Procedure):** Sinh ra ở bước **구현 및 실현 (Triển khai & Thực thi)**; xác định *THỰC HIỆN TEST NHƯ THẾ NÀO* (trình tự các bước chạy).

#### 5. Bẫy đề thi trắc nghiệm kinh điển (기출 함정 포인트)
- **Bẫy 1: Không thể chứng minh sạch lỗi:** Đề thi khẳng định "Kiểm thử chứng minh phần mềm không còn lỗi" $\rightarrow$ **SAI**. Kiểm thử chỉ chứng minh sự hiện diện của lỗi (`결함 존재 증명`).
- **Bẫy 2: Walkthrough vs Inspection (Kiểm thử tĩnh):**
  - **워크스루 (Walkthrough):** Do chính tác giả chủ trì, trao đổi bán chính thức, không cần chuyên gia độc lập.
  - **인스펙션 (Inspection):** Do người điều phối độc lập (Moderator) chủ trì, kiểm tra chính thức cực kỳ nghiêm ngặt theo **Checklist** chuẩn hóa.
- **Bẫy 3: Stress Test vs Performance Test:** Cứ thấy chữ quá tải vượt ngưỡng thiết kế (**과부하**) $\rightarrow$ Chọn **강도 테스트 (Stress)**.
- **Bẫy 4: Regression Test:** Cứ thấy chữ kiểm tra phát sinh lỗi mới sau khi sửa code (**새로운 결함**) $\rightarrow$ Chọn **회귀 테스트 (Regression)**.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Tiêu chí kết thúc kiểm thử (종료 조건 / Exit Criteria)
- Được định nghĩa ngay từ bước đầu tiên `계획 및 제어`.
- Quy định các chỉ số định lượng bắt buộc để được phép dừng kiểm thử:
  - Tỷ lệ bao phủ kiểm thử (Coverage): Statement Coverage $\ge 90\%$, Branch Coverage $\ge 85\%$.
  - 100% các ca kiểm thử mức nghiêm trọng (Blocker/Critical) đều phải đạt PASS.
  - Ngưỡng giới hạn về mặt thời gian và ngân sách dự án.

#### 2. Phân loại theo cơ sở thiết kế ca kiểm thử
- `명세 기반 (Specification-based)`: Dựa trên tài liệu đặc tả chức năng bên ngoài mà không nhìn vào mã nguồn (Hộp đen / Black-box: Phân vùng tương đương, Phân tích giá trị biên).
- `구조 기반 (Structure-based)`: Dựa trên cấu trúc logic luồng điều khiển bên trong mã nguồn (Hộp trắng / White-box: Phủ câu lệnh, Phủ nhánh, Phủ điều kiện).
- `경험 기반 (Experience-based)`: Dựa trên trực giác và kinh nghiệm tích lũy của kiểm thử viên (Đoán lỗi Error Guessing, Kiểm thử khám phá Exploratory Testing).

---

### 복습 체크리스트
- [ ] Kể tên đầy đủ 7 nguyên lý kiểm thử phần mềm chuẩn ISTQB.
- [ ] Giải thích hiện tượng 결함 집중 (Defect Clustering) và quy luật Pareto 80:20.
- [ ] Phân biệt bản chất câu hỏi của 검증 (Verification) và 확인 (Validation) theo Barry Boehm.
- [ ] Phân biệt 워크스루 (Walkthrough - không chính thức) và 인스펙션 (Inspection - chính thức dùng checklist) trong kiểm thử tĩnh.
- [ ] Nhận diện 강도 테스트 (Stress Testing) qua từ khóa ép tải quá mức (과부하).
- [ ] Nhận diện 회귀 테스트 (Regression Testing) qua từ khóa kiểm tra phát sinh lỗi mới sau khi sửa đổi mã nguồn.
- [ ] Nhớ thứ tự 5 giai đoạn kiểm thử: 계획/제어 $\rightarrow$ 분석/설계 $\rightarrow$ 구현/실현 $\rightarrow$ 평가 $\rightarrow$ 완료.
- [ ] Nhớ đúng: Test Case sinh ra ở bước Phân tích & Thiết kế; Test Procedure sinh ra ở bước Triển khai & Thực thi.
