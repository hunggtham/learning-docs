# 097-2: 테스트 프로세스 (Test Process - Quy trình kiểm thử)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **097-2: 테스트 프로세스 (Test Process - Quy trình kiểm thử)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối test process với planning, design, execution, defect và closure, để kiểm thử là một vòng lặp có bằng chứng.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **097-2: 테스트 프로세스 (Test Process - Quy trình kiểm thử)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **097-2: 테스트 프로세스 (Test Process - Quy trình kiểm thử)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **105: 시각에 따른 테스트 (Verification vs Validation)** khi chuyển sang phần tiếp theo.

Mục tiêu mô tả test process từ planning, design và execution đến defect closure; từ khóa khoanh vùng entry criteria, exit criteria và report.

## 핵심 키워드 (Từ khóa)

테스트, 프로세스

Kiến thức liên kết đặt test process trên nền V-model và traceability; cách đọc tiếp theo giúp phân biệt điều kiện bắt đầu với tiêu chí kết thúc.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **45. V-모델 (V-Model) 기반 애플리케이션 테스트 단계**에서 만든 기준을 이어받아 **097-2: 테스트 프로세스 (Test Process - Quy trình kiểm thử)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

Cách đọc đã đặt khung đối tượng–điều kiện–hệ quả; phần test process dùng khung đó để nối hoạt động với artifact và quyết định release.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

Phần này khép lại bằng vai trò của report và defect feedback; khi sang verification/validation, hãy đối chiếu đúng sản phẩm với đúng nhu cầu.

## 097-2: 테스트 프로세스 (Test Process - Quy trình kiểm thử)

Ở bước 61/101, **097-2: 테스트 프로세스 (Test Process - Quy trình kiểm thử)** xuất hiện như phần tiếp nối của **45. V-모델 (V-Model) 기반 애플리케이션 테스트 단계**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **097-2: 테스트 프로세스 (Test Process - Quy trình kiểm thử)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

**Quy trình 5 bước (5 단계):**
1. **계획 및 제어 (Planning & Control):** Lập kế hoạch, mục tiêu, chi phí.
2. **분석 및 설계 (Analysis & Design):** Viết Kịch bản (Test Scenario) và Ca kiểm thử (**Test Case**).
3. **구현 및 실현 (Implementation & Execution):** Viết Thủ tục test (**Test Procedure** - Trình tự chạy các case) và Thực thi test.
4. **평가 (Evaluation):** Đánh giá kết quả xem đạt chưa.
5. **완료 (Completion):** Lưu trữ hồ sơ, bàn giao.

- **Vietnamese Explanation:** Test Case là danh sách các món ăn cần nấu (Ví dụ: Trứng rán). Test Procedure là công thức nấu (Bước 1 bật bếp, bước 2 đập trứng). Phải có món (Case) rồi mới ghi công thức (Procedure) được.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Kế hoạch -> Phân tích (Ra Test Case) -> Thực hiện (Ra Test Procedure) -> Đánh giá -> Hoàn thành. (Kế Phân Thực Đánh Hoàn (Kế hoạch - Phân tích - Thực hiện - Đánh giá - Hoàn thành)).

---

Như vậy, **097-2: 테스트 프로세스 (Test Process - Quy trình kiểm thử)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **105: 시각에 따른 테스트 (Verification vs Validation)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

> **Bàn giao:** Sau **097-2: 테스트 프로세스 (Test Process - Quy trình kiểm thử)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
