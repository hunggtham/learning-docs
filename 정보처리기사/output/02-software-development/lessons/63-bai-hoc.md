# 132 ~ 136: 개발 단계에 따른 애플리케이션 테스트 (V-Model Test Levels)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **132 ~ 136: 개발 단계에 따른 애플리케이션 테스트 (V-Model Test Levels)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

개발, 단계에, 따른, 애플리케이션, 테스트

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 132 ~ 136: 개발 단계에 따른 애플리케이션 테스트 (V-Model Test Levels)

Thực hiện theo mô hình V (V-Model), từ nhỏ đến lớn:

1. **단위 테스트 (Unit Test):** Test từng Module con. Thường dùng White Box.
2. **통합 테스트 (Integration Test):** Ghép các module lại. (Có thể test kiểu Big Bang - Gom 1 cục, hoặc dần dần từ trên xuống, từ dưới lên). Tìm lỗi giao tiếp (Interface).
3. **시스템 테스트 (System Test):** Test toàn bộ hệ thống trong môi trường giống thực tế nhất. Đánh giá tính năng + hiệu năng (Bảo mật, tốc độ).
4. **인수 테스트 (Acceptance Test):** Khách hàng test để nghiệm thu.
   - **알파 (Alpha):** Khách hàng test tại văn phòng dev (có dev đứng xem).
   - **베타 (Beta):** Khách hàng tự test ở nhà (Giống Game Open Beta).

- 💡 **Mẹo ghi nhớ (Mnemonics):** Đơn vị (Unit) -> Tích hợp (Integration) -> Hệ thống (System) -> Nghiệm thu (Acceptance). Alpha = Nội bộ, Beta = Ở nhà.

# 136-1. 통합 테스트 (Integration Test - Kiểm thử tích hợp)

**[1] 개념 (Khái niệm):** 단위 테스트가 끝난 모듈을 통합하는 과정에서 발생하는 오류 및 결함을 찾는 테스트 기법.
*(Kiểm thử tích hợp là quá trình kết hợp các module đã qua kiểm thử đơn vị lại với nhau để tìm lỗi và khiếm khuyết phát sinh trong quá trình tương tác.)*

**[2] 핵심 키워드 (Từ khóa chính):**
- 모듈 통합 (Module Integration - Tích hợp module)
- 인터페이스 오류 (Interface Error - Lỗi giao diện/kết nối)
- 비점진적 (Big Bang - Không tăng dần) vs 점진적 (Incremental - Tăng dần)

**[3] 특징 (Đặc điểm):**
- **비점진적 통합 방식 (Non-incremental / Big Bang):**
  - 모든 모듈을 한꺼번에 결합해서 테스트함. *(Gộp tất cả module lại và kiểm thử cùng một lúc.)*
  - **장점 (Ưu điểm):** 규모가 작은 소프트웨어에 유리, 단시간 내 테스트 가능. *(Thích hợp cho phần mềm nhỏ, tốn ít thời gian.)*
  - **단점 (Nhược điểm):** 오류 발견 및 원인 식별이 매우 어려움. *(Khó phát hiện lỗi và xác định nguyên nhân do test một cục lớn.)*
- **점진적 통합 방식 (Incremental):**
  - 모듈 단위로 단계적으로 통합하면서 테스트함. *(Tích hợp từng bước theo từng module để kiểm thử.)*
  - 종류 (Các loại): 하향식(Top-down), 상향식(Bottom-up), 혼합식(Sandwich).
  - **장점 (Ưu điểm):** 오류 수정이 쉽고, 인터페이스와 관련된 오류를 완전히 테스트할 가능성이 높음. *(Dễ sửa lỗi và kiểm tra kỹ được các lỗi kết nối giữa các module.)*

**[4] 예시 (Ví dụ thực tế):**
- **비유 (자동차 조립 - Lắp ráp ô tô):**
  - *Unit Test:* Kiểm tra động cơ, bánh xe, vô lăng riêng biệt. Tất cả đều tốt.
  - *Big Bang:* Lắp ráp toàn bộ rồi mới khởi động. Xe không nổ máy $\rightarrow$ Không biết do động cơ, bình ắc quy hay bugi.
  - *Incremental:* Lắp động cơ vào hộp số rồi test (OK). Lắp thêm bánh xe rồi test (OK) $\rightarrow$ Nếu có lỗi sẽ biết ngay tại bộ phận vừa lắp thêm.

> 💡 **Mẹo ghi nhớ (Mnemonics):** 
> - **Big Bang** = "Bùm" một phát gom hết lại, nếu hỏng thì không biết sửa từ đâu.
> - **Incremental** = "Từng bước", thêm một phần tử vào nếu sai thì do phần tử đó.

---

# 137 & 138. 하향식 / 상향식 통합 테스트 (Top Down & Bottom Up Integration Test)

**[1] 개념 (Khái niệm):**
- **하향식 (Top-down):** 프로그램의 상위 모듈에서 하위 모듈 방향으로 통합하며 테스트. *(Kiểm thử từ module cấp cao nhất (chính) xuống các module cấp thấp (phụ).)*
- **상향식 (Bottom-up):** 프로그램의 하위 모듈에서 상위 모듈 방향으로 통합하며 테스트. *(Kiểm thử từ các module cấp thấp (cơ sở) dần lên module cấp cao.)*

**[2] 핵심 키워드 (Từ khóa chính):**
- **하향식:** 깊이 우선(Depth-first), 넓이 우선(Breadth-first), **스텁(Stub)**.
- **상향식:** 클러스터(Cluster), **테스트 드라이버(Driver)**.

**[3] 차이점 비교 (So sánh chi tiết):**
- **하향식 (Top-Down):** 
  - 하위 모듈이 아직 없으므로, 이를 thay thế bằng **Stub** (모듈의 흉내를 내는 가짜 하위 모듈 - module giả lập cấp dưới).
  - 테스트 초기부터 시스템의 전체 구조를 보여주기 유리.
- **상향식 (Bottom-Up):**
  - 하위 모듈들을 클러스터(Cluster)로 묶어서 수행.
  - 상위 모듈이 없으므로, 하위 모듈을 gọi bằng **Driver** (테스트를 제어하는 가짜 상위 모듈 - module giả lập cấp trên điều khiển test).

**[4] 예시 (Ví dụ thực tế):**
- **Top-Down:** Kiểm tra màn hình Đăng nhập (Main). Vì chưa có database, ta tạo một `Stub` (hàm giả) cứ nhận id/pass là trả về "Thành công".
- **Bottom-Up:** Đã viết xong hàm mã hóa mật khẩu (phụ), nhưng chưa có màn hình Đăng nhập. Ta viết một đoạn code ngắn (`Driver`) để gọi hàm mã hóa đó với các chuỗi khác nhau xem nó mã hóa đúng không.

> 💡 **Mẹo ghi nhớ (Mnemonics):** 
> - **Top-Down = Stub** (Từ trên xuống gặp tảng đá - S).
> - **Bottom-Up = Driver** (Từ dưới lên cần tài xế lái lên - D).

---

# 139. 테스트 드라이버와 테스트 스텁 (Test Driver vs Test Stub)

**[1] 개념 (Khái niệm):** 결합 테스트 시 미구현된 모듈을 대체하거나 구동하기 위한 가짜(Dummy) 모듈.
*(Module giả lập được dùng thay thế cho các module chưa hoàn thiện trong quá trình kiểm thử tích hợp.)*

**[2] 비교 (So sánh):**
- **드라이버 (Driver):** 상위 모듈 대체. 하위 모듈을 호출하고 매개변수 전달. (Dùng trong Bottom-Up).
- **스텁 (Stub):** 하위 모듈 대체. 상위 모듈의 호출에 단순 응답(결과값)만 제공. (Dùng trong Top-Down).

*(Ví dụ và mẹo nhớ đã tích hợp ở mục 137 & 138 phía trên để tránh lặp lại).*

---

# 140. 회귀 테스팅 (Regression Testing - Kiểm thử hồi quy)

**[1] 개념 (Khái niệm):** 수정된 모듈이나 컴포넌트가 다른 부분에 영향을 미치는지 확인하기 위해 테스트를 반복하는 것.
*(Kiểm tra lại toàn bộ hoặc một phần hệ thống sau khi đã sửa lỗi hoặc thêm tính năng mới, để đảm bảo việc sửa chữa này không làm hỏng các tính năng cũ đang hoạt động tốt.)*

**[2] 핵심 키워드 (Từ khóa chính):** 
- 새로운 오류 확인 (Xác nhận không có lỗi mới)
- 기존 기능 보장 (Đảm bảo chức năng cũ)
- 테스트 케이스 선정 (Lựa chọn test case hiệu quả)

**[3] 예시 (Ví dụ thực tế):**
- Trang web có tính năng Đăng nhập và Thanh toán đang dùng tốt. Bạn vừa sửa tính năng Đăng nhập. Bạn phải chạy lại *Regression Test* để chắc chắn rằng sửa xong Đăng nhập thì nút Thanh toán không tự nhiên bị liệt.

> 💡 **Mẹo ghi nhớ (Mnemonics):** 
> - **Regression (Hồi quy)** = Quay trở lại (Hồi) quy trình cũ để test xem có hỏng không.

---

# 140-1 ~ 143-1. 테스트 계획, 프로세스, 케이스 및 시나리오 (Test Process, Case & Scenario)

**[1] 테스트 프로세스 (Test Process - Quy trình kiểm thử):**
- 계획(Plan) $\rightarrow$ 분석(Analysis) $\rightarrow$ 설계(Design) $\rightarrow$ 수행(Execution) $\rightarrow$ 평가(Evaluation) $\rightarrow$ 관리(Management).

**[2] 테스트 케이스 (Test Case - Kịch bản kiểm thử chi tiết):**
- **개념:** 요구사항 준수 여부를 확인하기 위한 입력 값, 실행 조건, 기대 결과의 명세서. *(Tài liệu đặc tả bao gồm dữ liệu đầu vào, điều kiện thực thi và kết quả mong muốn để kiểm tra chức năng).*
- **작성 순서 (Thứ tự viết):** 자료 확보 $\rightarrow$ 위험 평가(우선순위 결정) $\rightarrow$ 요구사항 정의 $\rightarrow$ 구조 설계 $\rightarrow$ **케이스 정의 (입력값, 조건, 기대결과)** $\rightarrow$ 타당성 확인.
- **예시:** "Nhập ID 'admin', Pass '1234' (Input) tại trang Login (Condition) $\rightarrow$ Chuyển sang trang chủ (Expected Result)."

**[3] 테스트 시나리오 (Test Scenario - Kịch bản luồng kiểm thử):**
- **개념:** 테스트 케이스를 적용하는 순서에 따라 여러 개의 테스트 케이스들을 묶은 집합 문서. *(Tập hợp nhiều Test Case lại với nhau theo một trình tự để kiểm tra một luồng nghiệp vụ hoàn chỉnh).*
- **유의사항:** 시스템/모듈별로 분리 작성, 유스케이스 간 업무 흐름(Workflow) 검증.
- **예시:** Kịch bản mua hàng: "Đăng nhập (Test Case 1) $\rightarrow$ Tìm kiếm sản phẩm (Test Case 2) $\rightarrow$ Thêm vào giỏ (Test Case 3) $\rightarrow$ Thanh toán (Test Case 4)."

> 💡 **Mẹo ghi nhớ (Mnemonics):** 
> - **Test Case** = Từng bước đi độc lập (Kiểm tra 1 hành động).
> - **Test Scenario** = Chuyến hành trình (Nhiều bước nối tiếp nhau tạo thành kịch bản).

---

# 144 & 145. 테스트 오라클과 그 종류 (Test Oracle & Types)

**[1] 개념 (Khái niệm):** 테스트 결과가 올바른지 판단하기 위해 사전에 정의된 참(True) 값을 대입하여 비교하는 기법.
*(Cơ chế so sánh kết quả thực tế của phần mềm với kết quả mong đợi (đáp án chuẩn) để xác định xem phần mềm chạy đúng hay sai).*

**[2] 종류 (Các loại Test Oracle):**
1. **참 오라클 (True Oracle):** 모든 입력에 대해 완벽한 결과를 제공 (Độ bao phủ 100%, chi phí cực cao).
2. **샘플링 오라클 (Sampling Oracle):** 특정 몇몇 입력 값에 대해서만 결과 제공 (Lấy mẫu ngẫu nhiên, chi phí thấp).
3. **추정 오라클 (Heuristic Oracle):** 샘플링 오라클을 개선하여 일부는 참 값을, 나머지는 추정(Heuristic)으로 처리.
4. **일관성 오라클 (Consistent Oracle):** 애플리케이션 변경 시 테스트 전후 결과값이 같은지 확인 (Dùng trong Regression test).

**[3] 예시 (Ví dụ thực tế):**
- Máy tính bỏ túi: 
  - *True Oracle:* Tính thử mọi phép tính có thể (Không tưởng).
  - *Sampling Oracle:* Chỉ tính thử $1+1$, $2*3$, $10/2$.
  - *Consistent Oracle:* Bản update mới của app máy tính, lấy kết quả của bản cũ so sánh với bản mới.

> 💡 **Mẹo ghi nhớ (Mnemonics):** 
> - **Oracle** = Nhà tiên tri (đưa ra đáp án chuẩn). 4 loại: **T**rue - **S**ampling - **H**euristic - **C**onsistent.

---

# 146 & 146-1. 테스트 자동화 도구 (Test Automation Tools)

**[1] 개념 (Khái niệm):** 반복적인 테스트 활동을 스크립트나 자동화 소프트웨어로 기계가 대신 수행하게 하는 것.
*(Sử dụng công cụ phần mềm để chạy các bài test một cách tự động, thay vì con người bấm tay).*

**[2] 장점과 단점 (Ưu & Nhược điểm):**
- **장점 (Pros):** 반복 작업(Repetitive) 감소, 일관성(Consistency) 및 객관성 확보, 품질 향상.
- **단점 (Cons):** 초기 구축 비용(비용/노력)이 많이 듦, 도구 학습(교육) 필요.

**[3] 자동화 도구 유형 (Phân loại):**
- **정적 분석 도구 (Static Analysis Tool):** 코드를 실행하지 않고 결함이나 복잡도 분석 (VD: SonarQube).
- **동적 분석 도구 (Dynamic Analysis Tool):** 코드를 직접 실행하여 메모리 누수 등을 파악.

**[4] 고려사항 (Lưu ý khi áp dụng):**
- 재사용(Reusability) 불가능한 1회성 테스트는 자동화에서 제외.
- 프로젝트 초기에 엔지니어 투입 (Early Involvement) để thiết kế cấu trúc test automation.

**[5] 예시 (Ví dụ thực tế):**
- Sử dụng *Selenium* (Công cụ tự động hóa) để code một kịch bản: Tự động mở trình duyệt $\rightarrow$ Điền form $\rightarrow$ Bấm nút "Submit" hàng ngàn lần để test sức chịu đựng (Stress test). Việc này nếu dùng người bấm tay sẽ mất rất nhiều thời gian (손설거지 vs 식기세척기 - Rửa bát bằng tay vs Máy rửa bát).

> 💡 **Mẹo ghi nhớ (Mnemonics):** 
> - Tự động hóa = "Máy rửa bát". Đắt tiền mua (초기 비용) nhưng rửa 1000 cái bát rất nhanh (반복 작업 최적화).

---

# 147. 테스트 하네스 (Test Harness)

**[1] 개념 (Khái niệm):** 시스템이나 모듈을 테스트하기 위해 생성된 코드와 데이터의 집합 (환경).
*(Môi trường bao gồm các đoạn code giả lập, dữ liệu và công cụ để thực thi test).*

**[2] 구성 요소 (Thành phần chính):**
- **Driver / Stub:** (Đã giải thích ở trên).
- **Test Suite (테스트 슈트):** 테스트 케이스들의 집합 (Tập hợp các test case).
- **Test Script (테스트 스크립트):** 자동화된 테스트 실행 절차를 기록한 명세서 (Kịch bản code chạy tự động).
- **Mock Object (목 오브젝트):** 사용자의 예정된 행위를 조건부로 입력해 둔 가짜 객체 (Đối tượng giả lập dữ liệu trả về).

---

# 148. 결함 (Fault / Defect)

**[1] 개념 (Khái niệm):** 소프트웨어가 개발자의 설계와 다르게 동작하거나 잘못된 결과를 발생시키는 현상 (Bug).
*(Bất kỳ lỗi, thiếu sót nào khiến phần mềm chạy không đúng với tài liệu đặc tả yêu cầu).*

**[2] 예시 (Ví dụ thực tế):** 
- Thiết kế: Nút "Hủy" phải có màu Đỏ. Thực tế: Lập trình viên làm nút "Hủy" màu Xanh $\rightarrow$ Đây cũng được tính là một 결함 (Fault) dù không gây crash app.

---

# 149 ~ 151. 성능 분석, 빅오 표기법, 순환 복잡도 (Performance Analysis, Big-O, Cyclomatic Complexity)

**[1] 애플리케이션 성능 지표 (Chỉ số hiệu năng):**
- **처리량 (Throughput):** 일정 시간 동안 처리하는 작업의 양 (Số lượng task xử lý được trong một khoảng thời gian).
- **응답 시간 (Response Time):** 요청부터 응답이 시작될 때까지의 시간 (Thời gian từ lúc click đến lúc app bắt đầu phản hồi).
- **경과 시간 (Turn Around Time):** 요청부터 처리가 완전히 끝날 때까지 걸린 시간 (Thời gian từ lúc click đến lúc hoàn thành 100% công việc).
- **자원 사용률 (Resource Usage):** CPU, 메모리 소비 정도 (Mức độ ngốn RAM, CPU).

**[2] 빅오 표기법 (Big-O Notation - Ký hiệu Big-O):**
- 최악일 때(Worst Case)를 기준으로 알고리즘의 복잡도(실행 시간)를 표기.
- **성능 순서 (Tốc độ từ nhanh $\rightarrow$ chậm):** 
  $O(1)$ (Hằng số) $\rightarrow$ $O(log n)$ (Tìm kiếm nhị phân) $\rightarrow$ $O(n)$ (Tuyến tính) $\rightarrow$ $O(n log n)$ (Sắp xếp trộn) $\rightarrow$ $O(n^2)$ (Sắp xếp nổi bọt).

**[3] 순환 복잡도 (Cyclomatic Complexity - Độ phức tạp theo chu trình McCabe):**
- 프로그램의 논리적인 복잡도를 독립적인 경로의 수로 수치화. (Số lượng đường dẫn độc lập trong code).
- **공식 (Công thức):** $V(G) = E - N + 2$ 
  *(E: Edge - số mũi tên, N: Node - số nút).*

**[4] 예시 (Ví dụ thực tế):**
- **Throughput vs Response Time:** Một quán phở có thể bán 100 bát/giờ (Throughput = 100). Nhưng khách vào gọi món phải chờ 15 phút mới bê ra (Response time = 15m).
- **McCabe $V(G)$:** Nếu vẽ sơ đồ luồng (Flowchart) của hàm If-Else có 4 Node và 4 Edge $\rightarrow$ $V(G) = 4 - 4 + 2 = 2$ (Có 2 đường đi độc lập).

> 💡 **Mẹo ghi nhớ (Mnemonics):** 
> - Công thức McCabe: **E**m **N**hớ **+ 2** ($E - N + 2$).

---

# 152 & 153. 소스 코드 최적화 및 품질 분석 (Source Code Optimization & Quality Analysis)

**[1] 최적화 개념 (Khái niệm tối ưu hóa):**
- 나쁜 코드(Bad Code / Spaghetti Code / Alien Code)를 배제하고, **클린 코드(Clean Code)**로 작성하여 가독성(Readability)과 유지보수성 향상.
*(Viết code sạch sẽ, rõ ràng, dễ hiểu, tránh viết code rối như tơ vò (Spaghetti) hoặc code không ai hiểu được (Alien).*

**[2] 소스 코드 품질 분석 도구 (Công cụ phân tích chất lượng code):**
- **정적 분석 도구 (Static Analysis):** 코드를 실행하지 않고 패턴 분석 (VD: pmd, cppcheck, SonarQube).
- **동적 분석 도구 (Dynamic Analysis):** 소스 코드를 실행하여 메모리 누수(Memory Leak) 분석 (VD: Valgrind, Avalanche).

**[3] 예시 (Ví dụ thực tế):**
- **Alien Code (Code người ngoài hành tinh):** Code từ chục năm trước, tài liệu bị mất, người viết code đã nghỉ việc, sếp bảo bạn sửa code đó $\rightarrow$ Không thể sửa nổi!

---

# 154 & 155. 시스템 연계: EAI와 ESB (System Integration: EAI & ESB)

**[1] EAI (Enterprise Application Integration):**
- 기업 내 각종 애플리케이션 및 플랫폼 간의 정보 전달을 위한 통합 솔루션. *(Giải pháp tích hợp các ứng dụng trong doanh nghiệp để chúng có thể chia sẻ dữ liệu với nhau).*
- **유형 (4 loại):**
  - **Point-to-Point:** 1:1 직접 연결 (Nối trực tiếp A-B, nhiều kết nối sẽ rối).
  - **Hub & Spoke:** 중앙 허브를 통한 연결 (Có một Hub ở giữa điều phối, dễ quản lý).
  - **Message Bus:** 미들웨어 버스를 통한 연계 (Gắn tất cả vào 1 trục bus chung, mở rộng tốt).
  - **Hybrid:** Hub & Spoke + Message Bus.

**[2] ESB (Enterprise Service Bus):**
- 표준 기반의 **서비스 중심 통합 (SOA - Service Oriented Architecture)**.
- 애플리케이션 간 **약한 결합 (Loosely Coupled)**을 유지하여 유연성을 극대화.
*(Cũng giống EAI nhưng ESB dựa trên các dịch vụ web tiêu chuẩn, các hệ thống kết nối lỏng lẻo (ít phụ thuộc nhau), phù hợp hệ thống cực lớn).*

> 💡 **Mẹo ghi nhớ (Mnemonics):** 
> - **EAI** = Tích hợp hệ thống ứng dụng cục bộ.
> - **ESB** = Tích hợp "Dịch vụ" (Service) theo SOA.

---

# 156. JSON (JavaScript Object Notation)

**[1] 개념 (Khái niệm):** 속성-값 쌍(Attribute-Value)으로 이루어진 데이터 객체를 전달하는 텍스트 포맷.
*(Định dạng trao đổi dữ liệu dạng văn bản nhẹ, bao gồm các cặp Thuộc tính - Giá trị).*

**[2] 핵심 (Đặc điểm chính):**
- 비동기 통신(AJAX)에서 XML을 대체하여 널리 쓰임.
- 구문이 간결하고 데이터 파싱 속도가 빠름.
*(Dùng rất phổ biến trong lập trình Web/Mobile hiện đại để gửi nhận dữ liệu thay cho XML vì nó nhẹ và dễ đọc).*

**[3] 예시 (Ví dụ thực tế):**
```json
{
  "name": "Nguyen Van A",
  "age": 25,
  "role": "Developer"
}
```
*(Đây là định dạng JSON, cực kỳ dễ đọc đối với cả người và máy).*

---

# 157. XML (eXtensible Markup Language)

**[1] 개념 (Khái niệm):** 특수한 목적을 갖는 마크업 언어를 만드는 데 사용되는 다목적 마크업 언어.
*(Ngôn ngữ đánh dấu đa mục đích, được sử dụng để tạo ra các ngôn ngữ đánh dấu khác phục vụ mục đích đặc thù).*

**[2] 핵심 키워드 (Từ khóa chính):** HTML 단점 보완 (Khắc phục nhược điểm HTML), 사용자 정의 태그 (Thẻ tự định nghĩa).

**[3] 특징 (Đặc điểm):**
- HTML chỉ có các thẻ cố định (`<h1>`, `<b>`), còn XML cho phép người dùng tự tạo thẻ mới (`<student>`, `<name>`).
- Tách biệt giữa nội dung (Content)와 cách hiển thị (Style).

**[4] 예시 (Ví dụ thực tế):**
```xml
<person>
  <name>Nguyen Van A</name>
  <age>25</age>
</person>
```

---

# 158. AJAX (Asynchronous JavaScript and XML)

**[1] 개념 (Khái niệm):** 자바스크립트를 이용해 클라이언트와 서버 간에 데이터를 주고받는 비동기 통신 기술.
*(Công nghệ giao tiếp bất đồng bộ giữa Client và Server sử dụng JavaScript).*

**[2] 핵심 키워드 (Từ khóa chính):** 비동기 통신 (Bất đồng bộ), 새로고침 없음 (Không tải lại trang).

**[3] 특징 (Đặc điểm):**
- Trang web không cần tải lại toàn bộ (Refresh), chỉ cập nhật một phần dữ liệu mong muốn.
- Ngày nay, AJAX thường dùng JSON thay vì XML để truyền dữ liệu vì JSON nhẹ và nhanh hơn.

**[4] 예시 (Ví dụ thực tế):**
- Khi lướt Facebook hoặc đọc bình luận Youtube, bấm "Tải thêm bình luận", các bình luận mới sẽ hiện ra ngay bên dưới mà trình duyệt không hề chớp màn hình tải lại nguyên trang web.

---

# 159. 인터페이스 보안 기능 적용 (Interface Security Application)

**[1] 개념 (Khái niệm):** 인터페이스 송·수신 시 데이터 탈취 및 변조를 방지하기 위해 각 영역에 보안 설정을 적용하는 활동.
*(Áp dụng các biện pháp bảo mật vào các khu vực khác nhau để ngăn chặn đánh cắp hoặc thay đổi dữ liệu trong quá trình truyền tải).*

**[2] 영역별 보안 (Bảo mật theo khu vực):**
- **네트워크 영역 (Network):** IPsec, SSL, S-HTTP 등 암호화 (Mã hóa đường truyền).
- **애플리케이션 영역 (Application):** 소프트웨어 개발 보안 가이드 적용 (Lập trình an toàn).
- **데이터베이스 영역 (Database):** 스키마, 엔티티 접근 권한 설정 (Thiết lập quyền truy cập DB).

**[3] 예시 (Ví dụ thực tế):**
- **Sniffing (Nghe lén):** Hacker dùng phần mềm bắt gói tin trên mạng Wi-Fi quán cà phê. Nếu bạn dùng SSL (https), hacker chỉ thấy chuỗi ký tự mã hóa vô nghĩa.

---

# 160. 데이터 무결성 검사 도구 (Data Integrity Check Tools)

**[1] 개념 (Khái niệm):** 시스템 파일의 변경 유무를 확인하고 파일 변동 시 관리자에게 알려주는 보안 도구.
*(Công cụ bảo mật kiểm tra xem tệp hệ thống có bị thay đổi trái phép không và cảnh báo cho quản trị viên).*

**[2] 핵심 키워드 (Từ khóa chính):** 해시(Hash) 함수, 백도어(Backdoor) 감지.
- **도구 종류 (Các công cụ phổ biến):** Tripwire, AIDE, Samhain, Claymore, Fcheck.

**[3] 예시 (Ví dụ thực tế):**
- Hacker cài **Backdoor (Cửa hậu)** vào file `login.php`. Công cụ Tripwire sử dụng hàm băm (Hash) và phát hiện ra mã băm của `login.php` hôm nay khác với hôm qua $
ightarrow$ Phát chuông cảnh báo.

---

# 161. 인터페이스 구현 검증 도구 (Interface Implementation Verification Tools)

**[1] 개념 (Khái niệm):** 구현된 인터페이스가 정상적으로 작동하는지 확인하기 위해 사용되는 테스트 자동화 프레임워크.
*(Khung tự động hóa kiểm thử để xác minh giao diện kết nối hoạt động bình thường).*

**[2] 도구 종류 (Các công cụ):**
- **FitNesse:** 웹 기반 테스트 (Kiểm thử trên nền Web).
- **Selenium:** 웹 브라우저 검증 (Hỗ trợ đa trình duyệt, cực kỳ phổ biến).
- **watir:** Ruby 기반 프레임워크 (Dùng ngôn ngữ Ruby).
- **NTAF:** FitNesse + STAF (Công cụ nội bộ do Naver phát triển).

---

# 162. APM (Application Performance Management)

*(Gộp chung hai nội dung lặp ở bản gốc)*

**[1] 개념 (Khái niệm):** 애플리케이션의 성능 관리를 위해 접속자, 자원 현황, 트랜잭션 수행 내역 등을 모니터링하는 도구.
*(Công cụ giám sát hiệu năng ứng dụng, theo dõi lượng người truy cập, tài nguyên và giao dịch theo thời gian thực).*

**[2] 유형 (Phân loại):**
- **리소스 방식 (Resource - Theo tài nguyên):** Giám sát phần cứng như CPU, RAM (VD: Nagios, Zabbix).
- **엔드투엔드 방식 (End-to-End - Toàn trình):** Giám sát từ lúc User click đến khi kết thúc giao dịch (VD: Jennifer, VisualVM, Scouter).

**[3] 예시 (Ví dụ thực tế):**
- Ngày Black Friday, hệ thống bán hàng bị chậm. Nhìn vào màn hình **Jennifer (APM)**, quản trị viên thấy biểu đồ "Database connection" đang đỏ chót $
ightarrow$ Lập tức biết lỗi do kẹt DB chứ không phải do thiếu RAM.

---

# 💡 통합 비유 (Mẹo ghi nhớ tổng hợp)

- **알고리즘 비유 (Thuật toán):**
  - **빅오(Big-O):** Mua balo, luôn nghĩ tới lúc đựng nặng nhất xem có rách không (Worst case).
  - **순환 복잡도(McCabe):** Tính xem tòa nhà có bao nhiêu ngã rẽ để khi cháy bảo vệ phải đi kiểm tra từng ngóc ngách ít nhất bao nhiêu lần.
- **인터페이스 통신 비유 (Giao tiếp & Bảo mật):**
  - **XML / JSON:** Là các "thùng container" có quy chuẩn để chứa hàng (dữ liệu).
  - **AJAX:** Hệ thống "dỡ hàng bất đồng bộ" - Tàu không cần dừng hẳn, băng chuyền cứ lấy đồ ra từ từ mà hành khách không bị gián đoạn.
  - **인터페이스 보안 (Security):** Ổ khóa khóa chặt cửa container lại.
  - **무결성 검사 (Integrity):** Hải quan kiểm tra "Tem niêm phong", xem tem có bị rách hay thay tem giả không (Tripwire).
  - **APM:** Camera giám sát toàn bộ hoạt động cảng biển xem xe nào kẹt, kho nào đầy (Jennifer).

---

# 115. 분산 저장소 방식 (Distributed Repository System)

**[1] 개념 (Khái niệm):** 버전 관리 자료가 하나의 원격 저장소와 분산된 개발자 PC의 로컬 저장소에 함께 저장되어 관리되는 방식.
*(Hệ thống quản lý phiên bản mã nguồn, trong đó dữ liệu được lưu ở cả Server từ xa và máy tính cá nhân của mỗi lập trình viên).*

**[2] 핵심 키워드 (Từ khóa chính):** 로컬 저장소 (Local Repo), 원격 저장소 (Remote Repo), Git.

**[3] 특징 (Đặc điểm):**
- 개발자는 원격 저장소의 자료를 복제(Clone)하여 오프라인에서도 작업 가능.
- Server (Remote) bị sập thì vẫn còn dữ liệu nguyên vẹn ở Local Repo의 개발자.
- **대표 도구 (Công cụ tiêu biểu):** Git, Mercurial.

**[4] 예시 (Ví dụ thực tế):**
- Bạn dùng **Git**. Khi cúp mạng internet, bạn vẫn có thể `git commit` để lưu lại phiên bản code trên máy mình. Khi có mạng lại, bạn mới `git push` để đẩy lên Server.

> 💡 **Mẹo ghi nhớ (Mnemonics):** 
> - **Phân tán (Distributed) = Git:** Không có mạng vẫn lưu code được. Trái ngược với SVN (Tập trung) rớt mạng là khỏi lưu.
