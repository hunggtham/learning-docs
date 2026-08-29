# 과목 4. 소프트웨어 공학 (Phần 2)

## 169. 일반적인 소프트웨어 생명 주기 (General Software Life Cycle / Vòng đời phát triển phần mềm chung)
- **정의 단계 (Definition Phase / Giai đoạn định nghĩa)**: ‘무엇(What)’을 처리하는 소프트웨어를 개발할 것인지 정의하는 단계. 관리자와 사용자가 가장 많이 참여함.
  - **타당성 검토 단계 (Feasibility Study)**: 법적, 경제적, 기술적으로 실현 가능성이 있는지 조사.
  - **개발 계획 단계 (Development Planning)**: 자원과 비용을 측정.
  - **요구사항 분석 단계 (Requirements Analysis)**: 사용자 요구 문제를 상세하고 정확히 분석.
- **개발 단계 (Development Phase / Giai đoạn phát triển)**: ‘어떻게(How)’에 초점을 두고 실제적으로 소프트웨어를 개발하는 단계.
  - **설계 단계 (Design)**: 구조, 알고리즘, 자료구조 등을 작성 (에러가 가장 많이 발생).
  - **구현 단계 (Implementation)**: 설계된 문서를 기초로 코딩.
  - **테스트 단계 (Testing)**: 오류를 찾는 단계.
- **유지보수 단계 (Maintenance Phase / Giai đoạn bảo trì)**: ‘변경(Change)’에 초점을 두고 환경 변화에 적응 및 유지시키는 단계 (시간과 비용이 가장 많이 투입됨).

**Giải thích (Vietnamese):**
Vòng đời phần mềm (SDLC) gồm 3 giai đoạn chính: Định nghĩa (tìm hiểu xem cần làm "cái gì"), Phát triển (tiến hành xây dựng "như thế nào"), và Bảo trì (cập nhật, sửa lỗi sau khi bàn giao - "thay đổi"). Giai đoạn bảo trì luôn tốn nhiều thời gian và chi phí nhất.

**Ví dụ (Example):**
Xây dựng ứng dụng đặt đồ ăn:
- Định nghĩa: Xác định app cần chức năng gì, ngân sách bao nhiêu (What).
- Phát triển: Code app, thiết kế database, test tính năng (How).
- Bảo trì: Cập nhật app khi có iOS mới hoặc đổi thuật toán (Change).

**💡 Mẹo ghi nhớ (Mnemonics):**
**정개유** (Định - Phát - Bảo): **정**의 (Định nghĩa), **개**발 (Phát triển), **유**지보수 (Bảo trì). Nhớ câu "Định hướng - Phát triển - Bảo vệ".

---

## 170. 소프트웨어 생명 주기 모형 - 폭포수 모형 (Waterfall Model / Mô hình thác nước)
- 소프트웨어 공학에서 가장 오래되고 폭넓게 사용된 전통적/고전적 생명 주기 모형.
- 각 단계를 확실히 매듭짓고, 철저한 검토 및 승인 후 다음 단계로 진행하는 **선형 순차적 모형(Linear Sequential Model)**.
- 이전 단계로 되돌아갈 수 없음.
- 개발 순서: 타당성 검토 → 계획 → 요구 분석 → 설계 → 구현(코딩) → 시험(검사) → 유지보수
- **장점**: 성공 사례가 많음. 단계별 산출물이 명확하여 공정 기준점이 뚜렷함.
- **단점**: 새로운 요구사항 반영이 어려움. 초기에 모든 요구사항을 명확히 해야 함. 현실적으로 오류 없이 다음 단계로 넘어가기 힘듦.

**Giải thích (Vietnamese):**
Mô hình thác nước là mô hình lâu đời nhất. Giống như nước chảy từ trên cao xuống, không thể chảy ngược, bạn phải hoàn thành xong một giai đoạn mới được sang giai đoạn tiếp theo. Rất khó để quay lại sửa đổi yêu cầu.

**Ví dụ (Example):**
Giống như việc xây một ngôi nhà truyền thống. Bạn phải hoàn thành xong bản vẽ (thiết kế) rồi mới xây móng (code). Khi đã xây xong móng, nếu muốn đổi bản vẽ để thêm tầng hầm thì cực kỳ khó và tốn kém.

**💡 Mẹo ghi nhớ (Mnemonics):**
**폭포수는 거꾸로 흐르지 않는다** (Thác nước không chảy ngược): Yêu cầu phải chuẩn ngay từ đầu, khó thay đổi về sau (고전적, 선형 순차적 - Cổ điển, tuần tự tuyến tính).

---

## 171. 소프트웨어 생명 주기 모형 - 프로토타입 모형 (Prototype Model / Mô hình nguyên mẫu)
- 사용자 요구사항을 정확히 파악하기 위해 실제 개발될 소프트웨어의 **견본(시제품, Prototype)**을 만들어 최종 결과물을 예측하는 모형.
- 시제품은 사용자와 시스템 사이의 **인터페이스에 중점**을 둠.
- 개발 단계 안에서 유지보수가 이루어지며 별도의 유지보수 단계가 없어짐.
- 개발 순서: 요구 수집 → 빠른 설계 → 프로토타입 구축 → 고객 평가 → 프로토타입 조정 → 구현
- **장점**: 요구사항을 충실히 반영, 변경 용이. 미리 모형을 볼 수 있어 공동 참조 모델 제공.
- **단점**: 단기간 제작으로 비효율적 알고리즘 사용 가능성. 시제품을 완제품으로 오해하여 혼란 발생 가능.

**Giải thích (Vietnamese):**
Thay vì làm một mạch từ đầu đến cuối, mô hình nguyên mẫu tạo ra một bản "nháp" (prototype) nhanh chóng để khách hàng dùng thử và góp ý. Chủ yếu tập trung vào giao diện (UI/UX) để khách hàng hình dung được sản phẩm.

**Ví dụ (Example):**
Trước khi may một bộ vest thật (bằng vải đắt tiền), thợ may làm một bộ bằng vải nháp (prototype) cho khách mặc thử để xem form dáng đã chuẩn chưa, khách ưng ý rồi mới may vải thật.

**💡 Mẹo ghi nhớ (Mnemonics):**
**프**로토타입은 **미리보기(견본)**: Prototype = Bản dùng thử. Khách hàng xem trước rồi mới làm thật.

---

## 172. 소프트웨어 생명 주기 모형 - 나선형 모형 (Spiral Model / Mô hình xoắn ốc)
- 보헴(Boehm) 제안. 폭포수 모형과 프로토타입 모형의 장점에 **위험 분석(Risk Analysis)** 기능을 추가.
- 나선을 따라 돌 듯 점진적으로 완벽한 소프트웨어를 개발 (**점진적 모형**).
- 목적: 소프트웨어 개발 중 발생할 수 있는 **위험을 관리하고 최소화**.
- 개발 순서: 계획 및 정의(Planning) → **위험 분석(Risk Analysis)** → 공학적 개발(Engineering) → 고객 평가(Customer Evaluation)
- **장점**: 대규모 시스템에 적합 (현실적). 요구사항 추가/수정 용이. 유지보수 과정 불필요.
- **단점**: 위험성 평가에 크게 의존하여, 위험을 발견하지 못하면 문제 발생.

**Giải thích (Vietnamese):**
Mô hình xoắn ốc lặp đi lặp lại nhiều chu kỳ. Đặc trưng lớn nhất của nó là "Phân tích rủi ro" (Risk Analysis). Rất phù hợp cho các dự án quy mô lớn, phức tạp, ngân sách khổng lồ cần giảm thiểu rủi ro.

**Ví dụ (Example):**
Phát triển phần mềm cho tên lửa vũ trụ. Qua mỗi vòng xoắn ốc, team sẽ thêm tính năng và lập tức phân tích xem "có nguy cơ nổ tên lửa hay rò rỉ dữ liệu không?". Đảm bảo rủi ro ở mức 0 rồi mới xoắn tiếp.

**💡 Mẹo ghi nhớ (Mnemonics):**
**나위대** (나선형 - 위험분석 - 대규모): **나**선형 모형(Xoắn ốc) = **위**험 분석(Phân tích rủi ro) = **대**규모 프로젝트(Dự án lớn).
4 vòng lặp: **계위공고** (계획 - 위험 - 공학 - 고객).

---

## 173. 프로젝트 관리 (Project Management / Quản lý dự án)
- 주어진 기간 내 최소 비용으로 사용자를 만족시키는 시스템을 개발하기 위한 전반적인 활동.
- **효과적인 프로젝트 관리를 위한 3P (3대 요소)**:
  1. **사람 (People)**: 가장 기본이 되는 인적 자원.
  2. **문제 (Problem)**: 사용자 입장에서 문제를 분석하여 인식.
  3. **프로세스 (Process)**: 개발에 필요한 전체적인 작업 계획 및 구조 (Framework).
- **프로젝트 관리 대상**:
  - 계획 관리: 프로젝트 계획, 비용 산정, 일정 계획.
  - 품질 관리: 품질 통제, 품질 보증.
  - 위험 관리: 위험 식별, 위험 분석/평가.

**Giải thích (Vietnamese):**
Quản lý dự án là làm sao để làm ra phần mềm đúng hạn, rẻ nhất mà khách hàng vẫn hài lòng. Có 3 yếu tố cốt lõi (3P): Con người (ai làm?), Vấn đề (giải quyết cái gì?), và Quy trình (làm như thế nào?).

**Ví dụ (Example):**
Dự án game: People (lập trình viên, hoạ sĩ thiết kế), Problem (game bị giật lag, cần tối ưu), Process (Dùng Agile Scrum để chia sprint làm việc).

**💡 Mẹo ghi nhớ (Mnemonics):**
**3P**: **P**eople (Người) - **P**roblem (Vấn đề) - **P**rocess (Quy trình). Thiếu chữ P nào dự án cũng "Phá sản" (Phá).

---

## 174. 프로젝트 계획 수립 & 비용 결정 요소 (Project Planning & Cost Factors / Lập kế hoạch dự án & Các yếu tố chi phí)
- **소프트웨어 개발 영역 결정**: 프로젝트 계획 수립의 첫 번째 업무. 처리될 데이터, 기능, 성능, 제약조건, 인터페이스 등을 결정.
- **프로젝트 비용 결정 요소**:
  - **프로젝트 요소**: 제품의 복잡도, 시스템 크기, 요구 신뢰도.
  - **자원 요소**: 인적 자원, 하드웨어/소프트웨어 자원.
  - **생산성 요소**: 개발자 능력, 경험, 개발 기간.

**Giải thích (Vietnamese):**
Việc đầu tiên khi lập kế hoạch là xác định phạm vi (scope). Chi phí làm app đắt hay rẻ phụ thuộc vào 3 nhóm yếu tố: Bản thân dự án có phức tạp không? Tài nguyên cần thiết là gì? Lập trình viên có xịn không (năng suất)?

**💡 Mẹo ghi nhớ (Mnemonics):**
Chi phí phụ thuộc = **프자생** (프로젝트, 자원, 생산성).

---

## 175. 비용 산정 기법 - LOC 기법 (Lines Of Code / Kỹ thuật dòng mã lệnh)
- 소프트웨어 각 기능의 원시 코드 라인 수(LOC)의 비관치, 낙관치, 기대치를 측정하여 예측치를 구함.
- 측정이 용이하고 이해가 쉬워 가장 많이 사용됨.
- **산정 공식 (Dự đoán số dòng code)**: 
  예측치 = (낙관치 + 4 × 기대치 + 비관치) / 6
- **노력(인월, Person-Month)** = LOC / 1인당 월평균 생산 코드 라인 수 = 개발기간 × 투입인원.

**Giải thích (Vietnamese):**
Dự đoán chi phí dựa trên tổng số dòng code. Kỹ thuật này tính toán xem 1 người viết được bao nhiêu dòng code/tháng, từ đó suy ra cần bao nhiêu người và làm trong bao lâu (Person-Month). Công thức tính số dòng code kỳ vọng giống với ước lượng PERT.

**Ví dụ (Example):**
Làm web cần 6000 dòng code. Một Dev viết được 1000 dòng/tháng. Suy ra tốn 6 Người-Tháng (Person-Month). Nếu thuê 2 Dev thì tốn 3 tháng.

**💡 Mẹo ghi nhớ (Mnemonics):**
**LOC**: L = Line, O = Of, C = Code. **1 4 1 / 6**: 1 Lạc quan + 4 Kỳ vọng + 1 Bi quan chia 6.

---

## 176 - 177. 비용 산정 기법 - COCOMO 모형 (COnstructive COst MOdel / Kỹ thuật COCOMO)
- 보헴(Boehm)이 제안. 원시 프로그램 규모(LOC)에 의한 비용 산정 기법.
- 소프트웨어 개발 유형:
  - **조직형 (Organic Mode)**: 기관 내부 중·소규모, 5만 라인(50KDSI) 이하 (예: 사무/업무용).
  - **반분리형 (Semi-Detached Mode)**: 30만 라인(300KDSI) 이하 (예: 유틸리티, 트랜잭션 처리 시스템).
  - **내장형 (Embedded Mode)**: 초대형 규모, 30만 라인 이상 (예: 미사일 유도, 운영체제, 실시간 제어).
- **COCOMO 종류**:
  - **기본(Basic)**: 크기와 개발 유형만 이용.
  - **중간(Intermediate)**: 기본 + 제품/컴퓨터/개발자/프로젝트 특성 4가지 추가 반영.
  - **발전(Detailed)**: 개발 공정별로 노력을 산출하여 더 정확함.

**Giải thích (Vietnamese):**
COCOMO là mô hình tính phí dựa vào số dòng code nhưng phân loại theo quy mô dự án.
1. Organic: Nhỏ, nội bộ (<50k dòng).
2. Semi-detached: Vừa (<300k dòng).
3. Embedded: Rất lớn, nhúng vào phần cứng phức tạp như tên lửa (>300k dòng).

**Ví dụ (Example):**
- Organic: Viết tool điểm danh nhân sự cho cty.
- Embedded: Lập trình hệ thống điều khiển phanh ABS cho ô tô (cần cực kỳ phức tạp và chính xác).

**💡 Mẹo ghi nhớ (Mnemonics):**
**조반내** (Tổ - Bán - Nội): **조**직형(5만) - **반**분리형(30만) - **내**장형(30만 이상).

---

## 178. 프로젝트 일정 계획 (Project Scheduling / Lập lịch dự án)
- **브룩스(Brooks)의 법칙**: 프로젝트 진행 중에 새로운 인력을 투입할 경우 적응 기간과 부작용으로 일정이 더욱 지연됨. (Thêm người vào dự án đang trễ sẽ làm nó trễ hơn).
- **PERT (Program Evaluation and Review Technique)**:
  - 낙관치, 기대치, 비관치 3가지로 각 단계별 종료 시기를 결정.
  - 노드(작업)와 간선(예상시간)으로 구성.
- **CPM (Critical Path Method)**:
  - 노드(작업), 간선(전후 의존 관계).
  - 임계 경로(Critical Path)를 제공하여 프로젝트 최소 개발 기간을 결정함. 최장 경로가 임계 경로가 됨.

**Giải thích (Vietnamese):**
Khi lên lịch dự án, có quy luật Brooks nổi tiếng: "Thêm người vào dự án đang chậm tiến độ chỉ làm nó chậm hơn" (vì mất thời gian đào tạo người mới).
PERT và CPM là 2 biểu đồ mạng lưới giúp tìm ra đường găng (Critical Path) - chuỗi công việc dài nhất quyết định tổng thời gian dự án.

**💡 Mẹo ghi nhớ (Mnemonics):**
**Brooks**: "Chín người phụ nữ không thể sinh một đứa bé trong một tháng". Thêm người không có nghĩa là nhanh hơn!

---

## 179. 간트 차트 (Gantt Chart / Biểu đồ Gantt)
- 작업 일정을 **막대 도표(Bar Chart)**를 이용하여 표시하는 프로젝트 일정표. **시간선(Time-Line) 차트**라고도 함.
- 수평 막대 길이는 작업 기간을 나타냄.
- 중간 목표 미달성 이유와 예산 초과 등도 관리 가능. (단, 작업 간 의존성 파악은 CPM보다 약함).

**Giải thích (Vietnamese):**
Biểu đồ Gantt thể hiện các công việc bằng các thanh ngang (bar) chạy theo dòng thời gian. Rất trực quan để xem ai đang làm gì vào ngày nào, tiến độ ra sao.

---

## 180. 프로젝트 팀 구성 (Team Organization / Cấu trúc nhóm dự án)
- **분산형 팀 (민주주의식 팀 / Democratic Team)**:
  - 팀원 모두 의사 결정 참여. 장기 프로젝트에 적합. 이직률이 낮음.
  - 단점: 의사 결정 시간이 늦어지고 책임감이 분산될 수 있음. 의사소통 경로 수 = n(n-1)/2.
- **중앙 집중형 팀 (책임 프로그래머 팀 / Chief Programmer Team)**:
  - 한 관리자(책임 프로그래머)가 모든 의사 결정 권한과 책임을 가짐.
  - 의사 결정이 빠르고 소규모 문제에 적합.
  - 구성: 책임 프로그래머, 프로그래머, 프로그램 사서, 보조 프로그래머.
- **계층적 팀 (Hierarchical Team)**:
  - 분산형 + 중앙 집중형의 혼합. 초급 프로그래머들을 고급 프로그래머가 관리.

**Giải thích (Vietnamese):**
- Phân tán (Dân chủ): Mọi người cùng bàn bạc. Tốt cho dự án dài hạn nhưng họp hành mất thời gian.
- Tập trung (Chuyên tài): Một "siêu trình dịch" (Chief) quyết định hết, những người khác phụ việc. Nhanh nhưng phụ thuộc vào Chief.

---

## 181. 품질 표준 (Quality Standards / Tiêu chuẩn chất lượng phần mềm)
ISO/IEC 9126 등에서 말하는 소프트웨어 품질 특성:
1. **정확성 (Correctness)**: 사용자 요구 기능 충족.
2. **신뢰성 (Reliability)**: 오류 없이 정확/일관된 결과 수행.
3. **효율성 (Efficiency)**: 필요한 자원 소요 정도 (성능).
4. **무결성 (Integrity)**: 허용되지 않은 사용/변경 제어 (보안).
5. **사용용이성 (Usability)**: 배우고 사용하기 쉬운 정도.
6. **유지보수성 (Maintainability)**: 변경/오류 교정의 용이성.
7. **이식성 (Portability)**: 다양한 환경(하드웨어/OS)에서 운용 가능 정도.
8. **재사용성 (Reusability)**: 다른 목적으로 재사용 가능 여부.
9. **상호운용성 (Interoperability)**: 다른 소프트웨어와 정보 교환 능력.

**Giải thích (Vietnamese):**
Đây là các tiêu chí đánh giá phần mềm tốt. Ví dụ, phần mềm chạy nhanh là "Hiệu quả" (Efficiency), bảo mật chống hack là "Tính toàn vẹn" (Integrity), dễ cài trên cả Mac và Windows là "Tính di động/chuyển đổi" (Portability).

**💡 Mẹo ghi nhớ (Mnemonics):**
Chất lượng = **정신효무 사유이재상** (Đúng-Tin-Hiệu-Toàn Dùng-Bảo-Chuyển-Tái-Tương).

---

## 182. 품질 보증 / 정형 기술 검토 / 검토 회의 / 검열 (Quality Assurance & Reviews / Đảm bảo chất lượng & Đánh giá)
- **품질 보증 (QA)**: 소프트웨어가 요구사항과 일치하는지 확인하는 체계적인 작업.
- **정형 기술 검토 (FTR, Formal Technical Review)**: 소프트웨어 기술자들에 의해 수행되는 품질 보증 활동.
  - 지침: 제품 검토에만 집중, 의제 제한, 논쟁/반박 제한, 해결책(개선책) 논하지 않음, 참가자 수 제한 및 사전 준비.
- **검토 회의 (Walkthrough / Walkthrough)**:
  - 제품 개발자가 주최. 오류 조기 검출 목적 (해결책은 회의 후에). 사전 자료 배포.
- **검열 (Inspections / Inspection)**:
  - 검토 회의보다 더 공식적이고 발전된 형태. 다른 전문가가 코드/산출물을 꼼꼼히 심사하여 품질을 평가하고 개선.

**Giải thích (Vietnamese):**
- FTR (Đánh giá kỹ thuật chính thức): Là những cuộc họp để tìm lỗi phần mềm. **Lưu ý quan trọng**: Trong cuộc họp này CHỈ tìm lỗi, KHÔNG tranh cãi, KHÔNG bàn cách sửa lỗi (cách sửa sẽ bàn sau).
- Walkthrough: Tác giả tự trình bày code của mình cho team xem để tìm lỗi.
- Inspection: Người khác (thanh tra viên) sẽ soi xét code của bạn một cách rất nghiêm ngặt.

**💡 Mẹo ghi nhớ (Mnemonics):**
**FTR 원칙**: "문제만 찾고 해결책은 나중에!" (Chỉ tìm vấn đề, giải pháp tính sau!).

---

## 183. 위험 관리 (Risk Management / Quản lý rủi ro)
- 프로젝트 추진 과정에서 예상되는 돌발 상황을 미리 예상하고 대책을 수립하는 활동.
## 183. 위험 관리 절차 (Risk Management Procedure / Quy trình quản lý rủi ro) - Tiếp theo
- Yếu tố rủi ro tiêu biểu nhất là **사용자 요구 변경** (Sự thay đổi yêu cầu từ người dùng).
- **절차 (Quy trình)**:
  1. **위험 식별 (Nhận diện rủi ro)**: Nắm bắt các rủi ro có thể đoán trước.
  2. **위험 분석 및 평가 (Phân tích & Đánh giá)**: Lập bảng rủi ro (Risk Table) để phân tích xác suất xảy ra và sức ảnh hưởng (Risk Estimation).
  3. **위험 관리 계획 (Lập kế hoạch)**: Chuẩn bị đối sách phòng ngừa và tài liệu hóa.
     - *위험 회피 (Risk Avoidance)*: Chiến lược tốt nhất (Dự đoán và né tránh).
  4. **위험 감시 및 조치 (Giám sát & Xử lý)**:
     - *위험 감시 (Risk Monitoring)*: Liên tục theo dõi các dấu hiệu.
     - *비상 계획 (Contingency Plan)*: Kế hoạch dự phòng khi chiến lược né tránh thất bại.

**Giải thích (Vietnamese):**
Khách hàng liên tục thay đổi yêu cầu là rủi ro lớn nhất khi làm phần mềm. Để quản lý, trước tiên ta phải nhận diện được nó, rồi lập bảng đánh giá xem nếu xảy ra thì hậu quả là gì. Cách tốt nhất là "Né tránh" (Ví dụ: Chốt hợp đồng rõ ràng từ đầu để khách không đổi yêu cầu). Nếu vẫn xảy ra thì phải có kế hoạch dự phòng (Contingency Plan).

**💡 Mẹo ghi nhớ (Mnemonics):**
**식분계감** (Thức - Phân - Kế - Giám): 식별(Nhận diện) -> 분석(Phân tích) -> 계획(Lập kế hoạch) -> 감시(Giám sát).

---

## 184. 형상 관리 (SCM - Software Configuration Management / Quản lý cấu hình phần mềm)
- 소프트웨어 개발 과정에서 생산물을 확인하고 통제, **변경 상태를 기록하고 보관**하는 일련의 작업.
- 변경의 원인을 제어하고 적절히 변경되고 있는지 담당자에게 통보.
- 소프트웨어 생명 주기 **전 단계에 적용**되며 (유지보수 단계 포함), 방해 요인을 최소화하는 것이 목적.
- 형상 항목: 개발 문서, 소스 코드, 자료 구조, 유지보수 변경 사항 등.

**Giải thích (Vietnamese):**
SCM (Quản lý cấu hình) là việc theo dõi và kiểm soát mọi sự thay đổi của phần mềm (như dùng Git/GitHub). Ai đã sửa dòng code này? Sửa khi nào? Sửa tài liệu nào? Nó được áp dụng trong suốt vòng đời dự án để tránh xung đột và dễ dàng khôi phục khi có lỗi.

**Ví dụ (Example):**
Khi dùng Git để quản lý source code. Bạn commit một tính năng mới (theo dõi sự thay đổi), nếu code bị lỗi, bạn có thể dễ dàng revert (quay lại) phiên bản cũ. SCM chính là hệ thống quản lý các phiên bản này.

**💡 Mẹo ghi nhớ (Mnemonics):**
**형상관리 = 변경 통제 (Git)**: Nhắc đến 형상관리 là nhớ ngay đến việc theo dõi sự thay đổi (Change Control) trong suốt vòng đời.

---

## 185. 요구사항 분석 (Requirements Analysis / Phân tích yêu cầu)
- 소프트웨어 개발의 실질적인 첫 단계. 사용자의 요구를 이해하고 **문서화(명세화)**함.
- 분석 결과는 '설계 단계'의 기본 자료가 됨.
- **작업 과정**: 문제 인식 (면담, 설문조사) → 평가와 종합 (해결책 종합) → 모델 제작 (도식화, 이해하기 쉽게) → 문서화와 검토 (명세서 작성).
- **요구사항 분석가의 자질**: 소프트웨어 개발 경험, 사용자 환경 이해, 하드웨어/소프트웨어 기술 지식, **고객 관점(상대의 관점)**에서 문제 파악 능력.

**Giải thích (Vietnamese):**
Phân tích yêu cầu là bước đầu tiên để biết khách hàng thực sự muốn gì. Nhà phân tích phải có kinh nghiệm lập trình, hiểu biết hệ thống và đặc biệt là phải có "góc nhìn của khách hàng" để giải quyết đúng nỗi đau của họ.

---

## 186. 자료 흐름도 (DFD - Data Flow Diagram / Biểu đồ luồng dữ liệu)
- 자료의 흐름과 변환 과정을 도형 중심으로 기술. **버블(Bubble) 차트**라고도 함.
- 시스템의 범위를 표현하는 단계를 **배경도 (Level 0)**라고 함.
- **기호 (Ký hiệu)**:
  - **프로세스 (Process)**: `원(O)` - 자료를 변환시키는 처리 기능 (버블).
  - **자료 흐름 (Flow)**: `화살표(→)` - 자료의 이동.
  - **자료 저장소 (Data Store)**: `평행선(=)` - 파일, 데이터베이스.
  - **단말 (Terminator)**: `사각형(□)` - 정보의 생산자와 소비자 (외부 개체).

**Giải thích (Vietnamese):**
DFD vẽ ra cách dữ liệu chạy trong hệ thống. Ví dụ khi bạn mua hàng: Khách hàng (Hình vuông) -> Gửi yêu cầu mua (Mũi tên) -> Xử lý thanh toán (Hình tròn) -> Lưu vào Database (Đường song song). DFD còn gọi là Bubble Chart vì các Process được vẽ bằng hình tròn giống như bong bóng.

**💡 Mẹo ghi nhớ (Mnemonics):**
**프흐저단** (Process, Flow, Store, Terminator) / **원화평사** (Tròn, Mũi tên, Bình hành/Song song, Vuông).

---

## 187. 자료 사전 (DD - Data Dictionary / Từ điển dữ liệu)
- DFD에 있는 자료를 더 자세히 정의. 데이터를 설명하는 데이터이므로 **메타 데이터(Meta Data)**라고도 함.
- **표기 기호**:
  - `=` : 정의 (~로 구성되어 있다 / is composed of)
  + `+` : 연결 (그리고 / and)
  - `()` : 생략 가능 (Optional)
  - `[ | ]` : 선택 (또는 / or)
  - `{}` : 반복 (Iteration of)
  - `**` : 주석 (Comment)

**Giải thích (Vietnamese):**
Từ điển dữ liệu giải thích chi tiết các thành phần trong DFD. Ví dụ: `Hồ sơ = Tên + [ Nam | Nữ ] + ( Số điện thoại )`. Nghĩa là Hồ sơ gồm Tên, VÀ Giới tính (chọn Nam HOẶC Nữ), Số điện thoại (có ngoặc đơn nghĩa là có thể điền hoặc không).

**💡 Mẹo ghi nhớ (Mnemonics):**
- `()` Giống hình cái miệng ngậm lại -> Có thể không nói (Optional).
- `[ | ]` Dấu vách ngăn -> Phải chọn một trong hai.
- `{}` Dấu ngoặc nhọn móc nối tiếp -> Lặp đi lặp lại.

---

## 188. HIPO (Hierarchy plus Input-Process-Output)
- 입력, 처리, 출력의 기능을 나타내는 하향식 소프트웨어 개발 문서화 도구.
- **종류**:
  - **가시적 도표 (Visual Table of Contents)**: 전체적인 기능과 흐름을 보여주는 계층(Tree) 구조도.
  - **총체적 도표 (Overview Diagram)**: 입력, 처리, 출력에 대한 전반적 정보 제공.
  - **세부적 도표 (Detail Diagram)**: 기능을 상세히 기술.

**Giải thích (Vietnamese):**
HIPO là tài liệu thiết kế chia hệ thống theo cấu trúc từ trên xuống (Top-down). Gồm 3 loại biểu đồ: Tổng quan phân cấp (Tree), Biểu đồ chung (vẽ Input-Process-Output cơ bản), và Biểu đồ chi tiết.

**💡 Mẹo ghi nhớ (Mnemonics):**
**가총세** (Gia - Tổng - Tế): 가시적 (Trực quan/Phân cấp), 총체적 (Tổng quát), 세부적 (Chi tiết).

---

## 189. 구조적 설계의 주요 기본 원리 (Principles of Structured Design / Nguyên lý thiết kế có cấu trúc)
- **모듈화 (Modularity)**: 시스템을 모듈 단위로 나눔.
- **추상화 (Abstraction)**: 포괄적 개념 먼저 설계 후 세분화 (기능, 제어, 자료 추상화).
- **정보 은닉 (Information Hiding)**: 모듈 내부의 세부 정보를 감추어 다른 모듈이 변경하지 못하게 함 (유지보수 용이).
- **프로그램 구조 (Program Structure)**: 제어 계층 구조 (트리 형태).
  - 공유도(Fan-In): 나를 호출하는 상위 모듈 수.
  - 제어도(Fan-Out): 내가 호출하는 하위 모듈 수.

**Giải thích (Vietnamese):**
Khi thiết kế phần mềm, ta chia nhỏ thành các hàm/chức năng (Modularity). Dùng "Che giấu thông tin" (Information Hiding) như tính đóng gói (Encapsulation) trong OOP để các hàm không can thiệp sai vào dữ liệu của nhau.
- Fan-In (Đi vào): Có bao nhiêu hàm gọi đến mình. Fan-In cao là tốt vì tính tái sử dụng cao.
- Fan-Out (Đi ra): Mình gọi bao nhiêu hàm khác. Fan-Out cao nghĩa là hàm này quá phức tạp.

**💡 Mẹo ghi nhớ (Mnemonics):**
**모추정** (Mô - Trừu - Thông): **모**듈화(Modularity), **추**상화(Abstraction), **정**보 은닉(Information Hiding).

---

## 190. 바람직한 설계의 특징 (Good Design Characteristics / Đặc điểm của thiết kế tốt)
- 적당한 모듈 크기를 유지.
- **결합도(Coupling)는 약하게, 응집도(Cohesion)는 강하게 설계한다**.

**Giải thích (Vietnamese):**
Một thiết kế phần mềm chuẩn mực phải đảm bảo: "Mối liên kết giữa các module càng lỏng lẻo càng tốt (Low Coupling), nhưng sự gắn kết nhiệm vụ bên trong một module phải càng chặt chẽ càng tốt (High Cohesion)".

---

## 191. 결합도 (Coupling / Mức độ phụ thuộc)
- 모듈 간에 상호 의존하는 정도. 약할수록 독립성이 높고 품질이 좋음.
- **결합도가 약한 것부터 강한 순서 (Tốt -> Xấu)**:
  1. **자료 (Data)**: 파라미터로 단순 데이터(값)만 전달 (가장 좋음).
  2. **스탬프 (Stamp)**: 배열이나 레코드 등 자료 구조를 전달.
  3. **제어 (Control)**: 제어 신호(Flag)를 전달하여 상대 모듈의 흐름을 제어.
  4. **외부 (External)**: 외부에서 선언된 데이터를 참조.
  5. **공통 (Common)**: 전역 변수(공통 데이터 영역)를 여러 모듈이 사용.
  6. **내용 (Content)**: 다른 모듈의 내부 기능이나 변수를 직접 참조/수정 (가장 나쁨).

**Giải thích (Vietnamese):**
Coupling đánh giá mức độ "dính líu" giữa 2 module. Càng dính líu nhiều, khi sửa module này sẽ làm hỏng module kia.
Tốt nhất là Data (chỉ truyền tham trị như `int a`). Tệ nhất là Content (module A nhảy thẳng vào code của module B để sửa biến).

**💡 Mẹo ghi nhớ (Mnemonics):**
**자스제 외공내** (Tự - Tem - Chế - Ngoại - Công - Nội): 자료 (Data) -> 스탬프 (Stamp) -> 제어 (Control) -> 외부 (External) -> 공통 (Common) -> 내용 (Content). Từ Tốt đến Xấu.

---

## 192. 응집도 (Cohesion / Mức độ gắn kết)
- 모듈 안의 요소들이 서로 관련되어 있는 정도. 강할수록 독립성이 높고 품질이 좋음.
- **응집도가 약한 것부터 강한 순서 (Xấu -> Tốt)**:
  1. **우연적 (Coincidental)**: 아무 관련 없는 요소들이 우연히 모임 (가장 나쁨).
  2. **논리적 (Logical)**: 논리적으로 유사한 성격의 작업들을 모음.
  3. **시간적 (Temporal)**: 특정 시간에 같이 처리되는 기능들을 모음 (예: 초기화).
  4. **절차적 (Procedural)**: 기능들이 순차적으로 수행됨.
  5. **교환/통신적 (Communication)**: 동일한 입력/출력 데이터를 사용.
  6. **순차적 (Sequential)**: 앞 활동의 출력 데이터를 다음 활동의 입력 데이터로 사용.
  7. **기능적 (Functional)**: 내부 모든 요소가 단일 목적(기능)만을 위해 존재 (가장 좋음).

**Giải thích (Vietnamese):**
Cohesion đo lường sự tập trung của một module. Nếu một hàm vừa làm toán cộng, vừa in hóa đơn, vừa gửi email -> Quá nhiều việc không liên quan (Xấu). Hàm chỉ làm đúng một việc là "Tính tổng" -> Tuyệt vời (Functional).

**💡 Mẹo ghi nhớ (Mnemonics):**
**우논시절 교순기** (U - Luận - Thời - Tiết - Giao - Tuần - Kỹ): 우연 (Coincidental) -> 논리 (Logical) -> 시간 (Temporal) -> 절차 (Procedural) -> 교환 (Communication) -> 순차 (Sequential) -> 기능 (Functional). Từ Xấu đến Tốt.

---

## 193 - 194. 효과적인 모듈화 설계 방안 & N-S 차트 (Effective Modular Design & Nassi-Schneiderman Chart)
- **모듈화 방안**: 결합도를 줄이고 응집도를 높임 (Low Coupling, High Cohesion). 모듈 크기는 이해하기 쉽게 분해. 하나의 입구와 하나의 출구를 가짐.
- **N-S 차트**: 논리 기술에 중점을 둔 도형 (박스 다이어그램).
  - 순차, 선택, 반복 구조를 시각적으로 표현.
  - **GOTO나 화살표를 사용하지 않음**.
  - 읽기는 쉽지만 작성하기 어려움.

**Giải thích (Vietnamese):**
Biểu đồ N-S (Nassi-Schneiderman) là loại biểu đồ khối chữ nhật, không dùng mũi tên, không dùng GOTO. Cấu trúc lồng nhau rất dễ đọc logic nhưng vẽ ra thì khó.

---

## 195 - 197. 구현 및 구조적 프로그래밍, 제어 흐름도 (Implementation & Structured Programming)
- **구현(코딩)**: 설계 명세서를 컴퓨터가 알 수 있는 코드로 변환.
- **구조적 프로그래밍**: 순차(Sequence), 선택(Selection), 반복(Iteration)의 3가지 제어 구조만 사용하여 코딩 (Dijkstra 제안). 신뢰성 향상.
- **순환 복잡도 (Cyclomatic Complexity)**: 프로그램의 논리적 복잡도 척도.
  - V(G) = E - N + 2 (E: 화살표 수, N: 노드 수). 또는 닫힌 영역의 수 + 1.

**Giải thích (Vietnamese):**
Lập trình có cấu trúc chỉ dùng 3 luồng: Chạy tuần tự từ trên xuống (Sequence), Lệnh rẽ nhánh If/Else (Selection), và Vòng lặp For/While (Iteration). Độ phức tạp McCabe tính xem hàm có bao nhiêu đường đi (nhánh) độc lập.

**Ví dụ (Example):**
Nếu biểu đồ luồng có 5 Node (N=5) và 6 Cạnh/Mũi tên (E=6).
Độ phức tạp Cyclomatic V(G) = 6 - 5 + 2 = 3. Số 3 nghĩa là hàm này cần ít nhất 3 test case để phủ toàn bộ các đường đi.

---

## 196. 화이트 박스 테스트 (White Box Test / Kiểm thử Hộp trắng)
- 모듈의 **원시 코드(Source Code)를 오픈시킨 상태**에서 논리적인 모든 경로를 검사.
- 내부 구조, 제어 흐름, 논리 흐름(루프)을 직접 관찰하며 테스트.
- 조건의 참/거짓 경로를 적어도 한 번 이상 실행.
- 테스트 과정 **초기**에 적용됨.
- 종류: 기초 경로 검사 (Basic Path Testing), 조건 검사, 루프 검사, 데이터 흐름 검사.

**Giải thích (Vietnamese):**
Kiểm thử hộp trắng là bạn (thường là Dev) nhìn thấy toàn bộ source code và viết test case để đảm bảo mọi dòng code (if, else, vòng lặp) đều được chạy qua ít nhất 1 lần.

**💡 Mẹo ghi nhớ (Mnemonics):**
Hộp trắng trong suốt -> Nhìn thấu được code bên trong. Trọng tâm là "Logic đường đi" (경로).

---

## 198. 블랙 박스 테스트 (Black Box Test / Kiểm thử Hộp đen)
- **기능 검사**라고도 함. 내부 코드를 보지 않고, 소프트웨어의 인터페이스(입·출력)에서 기능이 완전히 작동하는지 입증.
- 테스트 과정 **후반부**에 적용됨.
- 종류:
  - **동치 분할 검사 (Equivalence Partitioning)**: 타당한 입력과 타당하지 않은 입력 자료의 갯수를 균등하게 나눠 테스트. (Ví dụ: Yêu cầu nhập từ 1-100. Test case: 50 (hợp lệ), 150 (không hợp lệ)).
  - **경계값 분석 (Boundary Value Analysis)**: 경계값에서 오류가 발생할 확률이 높음을 이용. (Ví dụ: Test case: 0, 1, 100, 101).
  - **원인-효과 그래프 (Cause-Effect Graphing)**: 입력(원인)과 출력(효과)의 관계 분석.
## 199. 검사 전략 (Testing Strategies / Chiến lược kiểm thử)
- **단위 검사 (Unit Testing)**: 코딩 후 최소 단위인 '모듈' 초점 검사 (화이트 박스 기법).
- **하향식 통합 검사 (Top-Down Integration)**: 상위 모듈 -> 하위 모듈 방향. 임시 시험용 모듈인 **스터브(Stub)** 필요.
- **상향식 통합 검사 (Bottom-Up Integration)**: 하위 모듈 -> 상위 모듈 방향. 제어 모듈과 종속 모듈 그룹인 **클러스터(Cluster)**와 드라이버(Driver) 필요. (Stub 불필요).
- **검증(확인) 검사 (Validation Testing)**: 요구사항 충족 여부 확인 (블랙 박스 기법).
  - **알파 검사 (Alpha Test)**: **개발자 환경(장소)**에서 사용자가 테스트 (통제된 환경).
  - **베타 검사 (Beta Test)**: **실제 사용자 환경**에서 여러 사용자가 테스트 (개발자 통제 없음).
- **시스템 검사 (System Test)**: 전체 시스템(하드웨어 포함)에서 완벽히 수행되는지 검사. (복구/보안/강도/성능 검사).

**Giải thích (Vietnamese):**
- Kiểm thử tích hợp từ trên xuống (Top-down) cần làm các module giả (Stub) để thay thế cho module con chưa code xong. Từ dưới lên (Bottom-up) cần nhóm (Cluster/Driver) để gọi module con.
- Alpha Test: Bạn mời khách hàng đến công ty bạn ngồi test app trước mặt bạn.
- Beta Test: Bạn tung app lên store cho người dùng tải về dùng thử và báo lỗi (bạn không ngồi cạnh họ).

**💡 Mẹo ghi nhớ (Mnemonics):**
**하스 상드** (Hạ - Stub, Thượng - Driver): **하**향식 = **스**터브(Stub). **상**향식 = 드라이버(Driver)/클러스터(Cluster).

---

## 200. 유지보수 (Maintenance / Bảo trì phần mềm)
- 개발 중 가장 많은 노력과 비용이 투입됨.
- **유형 (Phân loại)**:
  1. **수정(Corrective) 보수 (하자 보수)**: 검사 단계에서 못 찾은 '오류(버그) 수정'.
  2. **적응(Adaptive) 보수 (환경 적응)**: OS 변경, 하드웨어 변경 등 '환경 변화에 적응'하기 위한 수정.
  3. **완전화(Perfective) 보수 (기능 개선)**: 새로운 기능 추가, 성능 개선 (유지보수 중 가장 큰 비용 차지).
  4. **예방(Preventive) 보수**: 장래의 오류 발생에 대비하여 미리 예방.

**Giải thích (Vietnamese):**
- Corrective (Sửa lỗi): App bị crash, bạn phải vá lỗi.
- Adaptive (Thích ứng): Apple ra iOS mới, bạn update app để không bị lỗi màn hình tai thỏ.
- Perfective (Hoàn thiện): Thêm tính năng "Chat" vào app, cải tiến tốc độ tải (Chiếm nhiều ngân sách nhất).
- Preventive (Phòng ngừa): Refactor code để sau này dễ nâng cấp.

**💡 Mẹo ghi nhớ (Mnemonics):**
**수적완예** (Tu - Thích - Hoàn - Dự): **수**정, **적**응, **완**전, **예**방.

---

## 201. 외계인 코드 (Alien Code / Mã ngoài hành tinh)
- 아주 오래 전에 개발되어(보통 15년 전) 문서화가 제대로 되어 있지 않아 유지보수가 매우 어려운 프로그램.
- 해결책: 문서화(Documentation)를 철저히 해야 함.

**Giải thích (Vietnamese):**
Đó là những đoạn code từ "đời tống", người viết code đã nghỉ việc, code không có comment hay tài liệu giải thích. Người mới đọc vào không hiểu gì như ngôn ngữ ngoài hành tinh, không dám sửa vì sợ sập hệ thống.

---

## 202 - 203. 객체지향 기법 & 주요 원칙 (Object-Oriented Techniques & Principles / OOP)
- **개념**: 현실 세계의 개체(Entity)를 기계 부품(Object)처럼 만들어 조립식으로 소프트웨어 개발. 재사용/확장 용이.
- **구성 요소**:
  - **데이터 (Data/Attribute)**: 객체가 가진 정보 (속성, 상태).
  - **연산/메소드 (Method/Operation)**: 데이터를 처리하는 알고리즘/함수.
  - **클래스 (Class)**: 공통 속성/연산을 갖는 객체들의 집합 (틀, Type). 객체를 '인스턴스(Instance)'라고 함.
  - **메시지 (Message)**: 객체 간 상호작용 수단 (명령).
- **주요 기본 원칙**:
  1. **캡슐화 (Encapsulation)**: 데이터와 함수를 하나로 묶음. 재사용 용이, 결합도 낮아짐.
  2. **정보 은닉 (Information Hiding)**: 내부 정보를 숨기고 연산만을 통해 접근 허용 (Side Effect 최소화).
  3. **상속성 (Inheritance)**: 상위 클래스의 속성/연산을 하위 클래스가 물려받음. (다중 상속도 있음).
  4. **추상화 (Abstraction)**: 불필요한 부분 생략, 중요한 부분만 모델화.
  5. **다형성 (Polymorphism)**: 동일한 메시지(메소드명)에 대해 객체마다 다른 응답(기능)을 함.

**Giải thích (Vietnamese):**
OOP (Lập trình hướng đối tượng) giống như trò chơi xếp hình Lego.
- Class: Bản vẽ thiết kế chiếc xe.
- Object (Instance): Chiếc xe thật được lắp ráp.
- Tính đóng gói (Encapsulation): Gói gọn các bộ phận động cơ vào trong vỏ xe.
- Tính đa hình (Polymorphism): Cùng là lệnh "Kêu", con chó kêu "Gâu", con mèo kêu "Meo".

**💡 Mẹo ghi nhớ (Mnemonics):**
**캡정상추다** (Đóng - Ẩn - Kế - Trừu - Đa): 캡슐화, 정보 은닉, 상속성, 추상화, 다형성.

---

## 204 - 205. 객체지향 분석 및 럼바우 기법 (OO Analysis & Rumbaugh Method)
- **객체지향 분석**: 사용자의 요구사항을 분석하여 클래스(객체), 속성, 연산, 관계 등을 정의하는 작업.
- **분석 방법론**:
  - **Booch**: 미시적/거시적 개발 프로세스 모두 사용.
  - **Jacobson**: Use Case 강조.
  - **Coad/Yourdon**: E-R 다이어그램 사용.
  - **Wirfs-Brock**: 분석과 설계 간 구분 없음.
- **🌟 럼바우(Rumbaugh)의 분석 기법 (객체 모델링 기법, OMT)**:
  - 분석 순서: **객동기** (객체 -> 동적 -> 기능).
  1. **객체 모델링 (Object Modeling)**: 객체 식별, 구조 및 관계 규정 (객체 다이어그램 / 정보 모델링).
  2. **동적 모델링 (Dynamic Modeling)**: 시간 흐름에 따른 상태 변화, 제어 흐름 표현 (상태도).
  3. **기능 모델링 (Functional Modeling)**: 데이터 흐름을 중심으로 처리 과정 표현 (자료 흐름도, DFD).

**Giải thích (Vietnamese):**
Phương pháp phân tích của Rumbaugh là kinh điển nhất trong thi. Gồm 3 bước:
1. Object (Khách hàng, Tài khoản).
2. Dynamic (Tài khoản từ Đang mở -> Bị khóa khi nhập sai pass 3 lần).
3. Functional (Dữ liệu tiền chạy từ hệ thống ra ATM như thế nào).

**💡 Mẹo ghi nhớ (Mnemonics):**
**객동기** (Khách - Động - Cơ): **객**체(Object) -> **동**적(Dynamic) -> **기**능(Functional).

---

## 206 - 207. 객체지향 설계 및 프로그래밍 (OO Design & Programming)
- **설계 (OOD)**: 분석 모델을 설계 모델로 변환 (추상화, 정보 은닉, 상속 등 활용). 가장 중요한 것은 **모듈화**. 설계 명세서를 작성.
- **프로그래밍 (OOP)**: 현실 세계에 가까운 방식으로 프로그래밍. 유지보수/재사용성 향상.
  - 객체지향성 언어: Simula (최초), Smalltalk, C++, Java 등.

---

## 208. 소프트웨어의 재사용 (Software Reuse / Tái sử dụng phần mềm)
- 이미 개발된 소프트웨어 전체/일부를 다른 개발에 사용하는 것. 개발 시간/비용 단축, 품질 향상.
- **컴포넌트 (Component)**: 객체들의 모임으로 대규모 재사용 단위.
- 모듈 크기가 작고 일반적일수록 재사용률이 높음.
- 문제점: 표준화 부족, 공통 요소 발견의 어려움, 새 코드에 통합하기 어려움.

**Giải thích (Vietnamese):**
Đừng "phát minh lại cái bánh xe". Lấy những module, function đã chạy tốt ở dự án trước để ghép vào dự án này (ví dụ: dùng lại module đăng nhập bằng Google).

---

## 209. 소프트웨어 재공학 (Software Reengineering / Tái cấu trúc phần mềm)
- 기존 시스템을 수정 보완하거나 기능을 추가하여 성능을 향상 (예방 유지보수).
- 목적: 유지보수 비용 절감, 품질 향상, 소프트웨어 위기 해결.
- **주요 활동**:
  - **분석 (Analysis)**: 기존 명세서 확인.
  - **재구성/개조 (Restructuring)**: 기능은 그대로 두고 코드 구조만 향상 (Refactoring).
  - **역공학 (Reverse Engineering)**: 기존 코드를 분석하여 설계/명세서(문서)를 다시 뽑아내는 것 (복구). 가장 오래된 형태는 재문서화.
  - **이식 (Migration)**: 다른 OS나 하드웨어 환경으로 변환.

**Giải thích (Vietnamese):**
Reengineering là đập đi xây lại hoặc tu sửa lại nhà cũ cho hiện đại hơn.
- Restructuring: Cấu trúc lại bên trong nhà (mở rộng bếp, đập vách ngăn) nhưng nhìn bề ngoài vẫn là cái nhà đó.
- Reverse Engineering: Có một cái nhà cũ xây từ thời xưa không có bản vẽ. Nhìn vào cái nhà thực tế để vẽ lại bản vẽ kỹ thuật (Dịch ngược code thành tài liệu thiết kế).

**💡 Mẹo ghi nhớ (Mnemonics):**
**분재역이** (Phân - Tái - Nghịch - Di): 분석, 재구성, 역공학, 이식.

---

## 210. CASE (Computer-Aided Software Engineering)
- 소프트웨어 생명주기 전체 또는 일부를 **자동화하는 소프트웨어 도구**.
- 개발 기간 단축, 비용 절감, 품질 및 생산성 향상. 개발 주기의 표준화.
- **CASE 정보 저장소 (Repository)**: 개발 중 모아진 정보 보관 (현재의 Database 역할). 일관성 유지.
- **분류**:
  - 상위 (Upper) CASE: 요구 분석, 설계 단계 지원.
  - 하위 (Lower) CASE: 코드 작성, 테스트 지원.
  - 통합 (Integrated) CASE: 전체 과정 지원.

**Giải thích (Vietnamese):**
CASE là các phần mềm hỗ trợ kỹ sư làm phần mềm. Giống như Excel giúp kế toán tính toán nhanh hơn, CASE (như StarUML, Jira, Eclipse) giúp lập trình viên vẽ biểu đồ, quản lý task, sinh code tự động.

---

# 4과목 프로그래밍 언어 활용 (Phần 4: Ứng dụng ngôn ngữ lập trình)

## 070. 서버개발 프레임워크 (Server Development Framework)
- **모듈화 (Modularity)**: 캡슐화로 영향 최소화, 유지보수 용이.
- **재사용성 (Reusability)**: 반복 모듈 제공으로 생산성/품질 향상.
- **확장성 (Extensibility)**: 다형성 통한 인터페이스 확장.
- **제어 반전 (Inversion of Control, IoC)**: 프레임워크가 흐름을 제어하고 사용자(외부) 코드를 호출.

**Giải thích (Vietnamese):**
Framework (như Spring, Django) là một bộ khung có sẵn. Tính năng đặc biệt nhất của Framework là IoC (Đảo ngược quyền điều khiển): Thay vì bạn tự gọi thư viện (Library), thì Framework sẽ là người gọi code của bạn!

---

## 071. 보안 취약성 식별 (Security Vulnerability Identification / Lỗ hổng bảo mật)
- **버퍼 오버플로 (Buffer Overflow)**: 메모리를 다루는 데 오류 발생시켜 덮어쓰는 공격.
- **허상 포인터 (Dangling Pointer)**: 삭제된 객체를 가리키고 있는 포인터 (메모리 보안 위반).
- **FTP 바운스 공격**: FTP 프로토콜 구조 허점 이용.
- **SQL 삽입 (SQL Injection)**: 웹 입력창에 SQL 문법 삽입해 DB 데이터 유출/조작.
- **디렉토리 접근 공격 (Directory Traversal)**: 웹 루트 외 디렉토리 접근 (`../` 문자 사용).
- **포맷 스트링 버그**: `printf()` 등에서 검사되지 않은 입력 통한 공격.
- **코드 인젝션 (Code Injection)**: 유효하지 않은 실행 코드 주입.

**Giải thích (Vietnamese):**
- SQL Injection: Kẻ gian gõ `1' OR '1'='1` vào ô đăng nhập để lừa hệ thống cho phép truy cập.
- Buffer Overflow: Kẻ gian cố tình nhập 100 ký tự vào ô chỉ cho phép 10 ký tự, làm tràn bộ nhớ và sập chương trình.

---

## 072 - 073. 데이터 타입, 변수 및 연산자 (Data Types, Variables & Operators)
- **데이터 타입 (Data Types)**:
  - 정수형 (Integer): `int`, `short`, `long` (Ví dụ: 1, -1).
  - 부동 소수형 (Float Point): `float`, `double` (실수, 소수점) (Ví dụ: 3.14).
  - 문자형 (Character): `char` ('A').
  - 문자열 (String): `char` 배열, `string` ("ABC").
  - 논리형 (Boolean): 참/거짓 (True/False).
- **변수 작성 규칙 (Variable Naming Rules)**:
  - 영문자, 숫자, 밑줄(`_`) 사용 가능.
  - **숫자로 시작 불가**, 중간 공백 특수문자 불가, 예약어(`if`, `for` 등) 사용 불가.
- **연산자 (Operators)**:
  - 산술 (Arithmetic): `+`, `-`, `*`, `/` (몫), `%` (나머지).
  - 증감 (Increment/Decrement): `++` (1 증가), `--` (1 감소).
    - 전치 (`++A`): 연산 전 증가.
    - 후치 (`A++`): 연산 후 증가.
  - 관계 (Relational): `>`, `<`, `==` (같다), `!=` (다르다).
  - 논리 (Logical): `&&` (AND), `||` (OR), `!` (NOT).
  - 삼항 (Ternary): `(조건) ? (참) : (거짓);`
## 074. 데이터 입출력 (Data Input/Output)
- **표준 입력 함수 (C언어)**: `scanf("서식 문자열", &변수명);` (변수의 주소 `&`를 붙임).
- **표준 출력 함수 (C언어)**: `printf("서식 문자열", 변수);`
- **서식 문자열 유형 (Format Strings)**:
  - `%d`: 정수형 10진수 (Decimal)
  - `%f`: 실수형 (Float)
  - `%c`: 문자형 1개 (Character)
  - `%s`: 문자열 (String)
- **이스케이프 문자**: `\n` (줄바꿈), `\t` (탭), `\b` (백스페이스).
- **JAVA 입출력**: `System.out.println()` (출력 후 자동 개행), `System.out.print()` (개행 없음).
- **Python 입출력**: `print(문자열, end='')` (끝에 개행 대신 다른 문자 삽입).

**Giải thích (Vietnamese):**
Khi lập trình bằng C, bạn dùng `scanf` để nhận dữ liệu người dùng nhập (nhớ có dấu `&` trước tên biến) và `printf` để in ra màn hình. Dấu `%d` dùng cho số nguyên, `%f` cho số thập phân. Java dùng `System.out.println()`. Python thì ngắn gọn hơn chỉ cần `print()`.

---

## 075 - 077. 배열, 조건문, 반복문 (Arrays, Conditionals & Loops)
- **배열 (Array)**: `자료형 변수명[개수] = {초깃값};` (C/Java). 2차원 배열은 `변수명[행][열]`.
- **조건문 (if/switch)**:
  - C/Java: `if (조건) { ... } else if (조건) { ... } else { ... }`
  - Python: `if 조건:` -> `elif 조건:` -> `else:`
  - switch문 (C/Java): 식의 값에 따라 `case`를 찾아가며, `break;`가 없으면 아래 문장들도 계속 실행됨.
- **반복문 (for/while)**:
  - for문 (C/Java): `for (초기식; 조건식; 증감식) { ... }`
  - for문 (Python): `for 변수 in range(시작, 끝+1):`
  - while문: 조건이 참일 동안 반복.
  - do~while문 (C/Java): 조건과 상관없이 무조건 **최소 1번**은 실행하고 조건을 검사함.

**Giải thích (Vietnamese):**
- Trong Python, cấu trúc điều kiện là `if`, `elif` (viết tắt của else if) và `else`. Không cần ngoặc nhọn `{}` mà dùng thụt lề (indentation).
- `do~while` khác `while` ở chỗ: `do~while` sẽ làm việc trước rồi mới kiểm tra điều kiện sau, nên chắc chắn code bên trong được chạy ít nhất 1 lần.

---

## 078. 사용자 정의 함수와 클래스 (User Defined Functions & Classes)
- **접근 제어자 (JAVA Access Modifiers)**:
  1. `public`: 모든 접근 허용 (Bất cứ đâu cũng gọi được).
  2. `protected`: 같은 패키지 + 상속받은 자식 클래스만 허용.
  3. `default`: 같은 패키지(폴더) 내에서만 허용.
  4. `private`: 오직 해당 객체 내에서만 허용 (Bảo mật cao nhất).
- **클래스와 생성자 (Class & Constructor)**:
  - JAVA: 생성자 이름은 클래스 이름과 동일하며 반환값이 없음. `this` 키워드로 인스턴스 변수(필드)를 가리킴.
  - Python: `class` 키워드 사용. 생성자는 매직 메소드 `__init__(self, ...)`로 정의. `self`는 객체 자신을 참조(JAVA의 `this`와 유사).

---

## 079. 프로그래밍 언어의 종류 (Types of Programming Languages)
- **절차적 언어 (Procedural)**: 코드를 순차적인 함수(Procedure) 단위로 나누어 해결. (C, FORTRAN, ALGOL 등).
- **객체지향 언어 (Object-Oriented)**: 데이터와 메소드를 묶어 '객체'로 만듦 (캡슐화, 상속, 다형성 지원). (C++, JAVA 등). JAVA는 '가비지 컬렉터(Garbage Collector)'가 메모리를 자동 관리함.
- **스크립트 언어 (Scripting)**: 컴파일 없이 인터프리터 방식으로 바로 실행되는 언어. (Python, JavaScript, PHP, Bash 등).
  - PHP: 웹 서버용 스크립트. `@`를 쓰면 에러 무시.
  - JavaScript: 웹 브라우저 제어 (클래스와 프로토타입 기반).

**Giải thích (Vietnamese):**
- Ngôn ngữ thủ tục (như C) chạy từ trên xuống dưới, gọi các hàm.
- Ngôn ngữ OOP (như Java, C++) nhóm code thành các "Thực thể" (Object). Java có Garbage Collector tự động dọn dẹp RAM không dùng đến.
- Ngôn ngữ Script (Python, JS) không cần biên dịch ra file `.exe` mà chạy trực tiếp, rất linh hoạt.

---

## 080 - 081. 라이브러리와 예외처리 (Libraries & Exception Handling)
- **C언어 표준 라이브러리**:
  - `stdio.h`: 입출력 (`printf`, `scanf`).
  - `stdlib.h`: 자료형 변환 (`atoi`: char->int).
  - `string.h`: 문자열 처리 (`strlen`, `strcpy`).
  - `math.h`: 수학 함수 (`sqrt`: 제곱근).
- **예외처리 (Exception Handling)**:
  - JAVA: `try { 실행 } catch (예외객체 e) { 에러처리 } finally { 무조건 실행 }`
  - Python: `try: ... except 예외객체: ... finally: ...`
  - 주요 예외객체: `NullPointerException` (객체가 없을 때), `ZeroDivisionError` (0으로 나눌 때).

---

# Chapter 3. 응용 SW 기초 기술 활용 (Phần 3: Ứng dụng kỹ thuật cơ sở phần mềm)

## 082. 운영체제 기능 및 종류 (Operating System OS)
- **운영체제의 주요 프로그램**:
  - **제어 프로그램 (Control Program)**: 감시(Kernel), 작업 제어, 데이터 관리.
  - **처리 프로그램 (Processing Program)**: 언어 번역(컴파일러), 서비스, 문제 프로그램.
- **쉘(Shell)과 커널(Kernel)**:
  - **쉘 (Shell)**: 사용자의 명령어를 해석하여 커널로 전달 (사용자 인터페이스).
  - **커널 (Kernel)**: 핵심 모듈. 하드웨어/메모리/프로세스를 직접 제어 및 관리.
- **운영체제 종류**:
  - **Windows**: GUI, 선점형 멀티태스킹, PnP(자동 감지) 기능.
  - **Linux / Unix**: 오픈소스 (Linux), 트리 구조 파일 시스템. 시분할 시스템.
  - **Unix 파일 시스템 구조**: 부트 블록 -> 슈퍼 블록 (전체 정보) -> 아이노드(i-node) 블록 (파일 메타데이터) -> 데이터 블록 (실제 파일 내용).

**Giải thích (Vietnamese):**
OS giống như quản gia của máy tính.
- Kernel (Hạt nhân) là bộ não xử lý phần cứng. Shell (Vỏ) là cái dòng lệnh hoặc giao diện để con người nói chuyện với bộ não đó.
- Hệ thống tệp của UNIX chia làm 4 phần: Boot (chứa code khởi động) -> Super (Thông tin tổng quan) -> i-node (Lưu tên file, quyền truy cập...) -> Data (Nội dung file thực tế).

**💡 Mẹo ghi nhớ (Mnemonics):**
**제어 프로그램**: 감작데 (감시, 작업, 데이터). / **처리 프로그램**: 언서문 (언어, 서비스, 문제).

---

## 083. 메모리 관리 기법 - 배치 전략 (Memory Placement Strategies)
- **최초 적합 (First fit)**: 가장 처음 만나는 빈 공간에 할당 (빠름).
- **최적 적합 (Best fit)**: 자원 낭비(단편화)가 가장 적은 핏(딱 맞는) 공간에 할당.
- **최악 적합 (Worst fit)**: 단편화가 가장 큰(넓은) 공간에 할당 (남은 공간을 다시 쓰기 위해).

**Giải thích (Vietnamese):**
Khi một phần mềm cần RAM, OS sẽ nhét nó vào đâu?
- First fit: Thấy chỗ nào trống nhét vào luôn (Nhanh).
- Best fit: Tìm chỗ nào vừa khít nhất để nhét (Tiết kiệm chỗ).
- Worst fit: Cố tình nhét vào chỗ rộng nhất (Để chừa lại không gian rộng cho các app sau).

---

## 084. 페이지 교체 알고리즘 (Page Replacement Algorithms / Thuật toán thay thế trang nhớ)
- 메모리가 꽉 찼을 때 어떤 페이지를 내보낼지 결정.
- **FIFO (First In First Out)**: 가장 먼저 들어온 페이지를 교체.
- **OPT (Optimal)**: 앞으로 가장 오랫동안 사용되지 않을 페이지를 교체 (이론상 최적).
- **LRU (Least Recently Used)**: (과거 기준) 가장 오랫동안 사용되지 않은 페이지를 교체.
- **LFU (Least Frequently Used)**: 사용(참조) 횟수가 가장 적은 페이지 교체.
- **NUR (Not Used Recently)**: 최근에 사용하지 않은 페이지 교체 (참조 비트 사용).
- **지역성 (Locality)**: 프로세스가 특정 메모리 영역을 집중적으로 참조하는 현상.
  - 공간 지역성: 근처 메모리 참조 (배열).
  - 시간 지역성: 방금 참조한 곳 다시 참조 (루프, 변수).
- **스레싱 (Thrashing)**: 실제 CPU 연산보다 페이지 교체에 더 많은 시간이 소요되어 시스템 성능이 뚝 떨어지는 현상.

**Giải thích (Vietnamese):**
Khi RAM đầy, máy phải đẩy tạm dữ liệu ra ổ cứng.
- LRU: Đuổi cái nào lâu nhất không ai thèm đụng tới (Thường xuyên dùng nhất).
- LFU: Đuổi cái nào ít được gọi tên nhất.
- Locality: Chương trình có xu hướng dùng lại những dữ liệu gần nhau (Ví dụ chạy vòng lặp `for`).
- Thrashing: Tình trạng máy tính bị đơ, giật lag vì RAM quá đầy, máy mải mê swap dữ liệu ra vào ổ cứng mà không chịu tính toán xử lý.

---

## 085. 프로세스 및 스레드 (Process & Thread)
- **프로세스 상태 (Process States)**: 생성(Create) -> 준비(Ready) -> 실행(Running) -> 대기(Wait/Block) -> 종료(Exit).
- **상태 전이 (State Transitions)**:
  - **Dispatch**: 준비 -> 실행 (CPU 할당받음, 문맥교환 발생).
  - **Timeout (Timer Runout)**: 실행 -> 준비 (할당된 시간 초과).
  - **Block**: 실행 -> 대기 (I/O 작업 요청).
  - **Wake Up**: 대기 -> 준비 (I/O 작업 완료).
- **PCB (Process Control Block)**: OS가 프로세스를 관리하기 위해 유지하는 정보 블록 (상태, 식별자, 스택 정보 등).
- **문맥 교환 (Context Switch)**: CPU가 프로세스를 바꿀 때 현재 상태를 PCB에 저장하고 새 프로세스 상태를 불러오는 작업.
- **스레드 (Thread)**: 커널 수준(느리지만 안정적), 사용자 수준(빠르지만 불안정).

**Giải thích (Vietnamese):**
Process là một chương trình đang chạy.
Khi Process A đang chạy, hết thời gian (Timeout), OS sẽ cất trạng thái của A vào tờ giấy nhớ gọi là "PCB", sau đó gọi Process B lên chạy. Việc chuyển đổi này gọi là "Context Switch" (Chuyển đổi ngữ cảnh). Chuyển đổi càng nhiều máy càng chậm.

**💡 Mẹo ghi nhớ (Mnemonics):**
**디타블웨** (Dispatch, Timeout, Block, WakeUp): Chu trình chuyển trạng thái của Process.

---

## 086. 프로세스 스케줄링 (Process Scheduling)
- **선점형 (Preemptive)**: 운영체제가 CPU를 강제로 뺏을 수 있음. 빠르고 대화식 시스템에 유리하지만 오버헤드 발생. (RR, SRT, MLQ, MLFQ).
- **비선점형 (Non-Preemptive)**: 한 프로세스가 끝나야만 다음 프로세스가 CPU를 씀. 일괄처리에 적합. (FCFS, SJF, HRN).
  - **FCFS**: 먼저 온 놈이 먼저 (First Come First Serve).
  - **SJF**: 짧은 작업 먼저 (Shortest Job First). 긴 작업은 무한 대기(기아 상태) 발생 가능.
  - **HRN**: SJF의 단점(기아 상태) 보완. 우선순위 = (대기시간 + 서비스시간) / 서비스시간. 결과값이 큰 것부터 우선 처리!

**Giải thích (Vietnamese):**
Lập lịch cho CPU:
- Độc quyền (Non-Preemptive): Đang chạy thì không ai được cướp (Giống như đang đi vệ sinh, người khác phải đợi). Ví dụ: FCFS, SJF, HRN.
- Cướp quyền (Preemptive): Đang chạy nhưng có việc khẩn cấp (hoặc hết giờ) thì hệ thống đuổi ra cho người khác vào. Ví dụ: RR, SRT.
- Công thức HRN rất hay thi: `(Thời gian đợi + Thời gian xử lý) / Thời gian xử lý`. Việc đợi càng lâu ưu tiên càng cao.

---

## 교착상태 필요충분조건 1 - 상호배제 (Deadlock Conditions - Mutual Exclusion)
- **교착상태(Deadlock)**: 두 프로세스가 서로의 자원을 기다리며 멈춰버린 현상.
- **상호배제 알고리즘 (Mutual Exclusion)**: 한 번에 하나의 프로세스만 자원을 쓰게 함.
  - Dekker: 두 프로세스 간 Flag와 Turn 변수 사용.
  - Peterson: 두 프로세스 간 상대방에게 양보.
  - Lamport: 고유 번호(티켓) 부여, 번호순 진입.
  - Semaphore: 정수 변수(P연산, V연산)를 이용해 접근 통제.
## 086. 프로세스 스케줄링과 교착상태 (Process Scheduling & Deadlock) - 계속
- **교착상태(Deadlock) 4가지 필요충분조건**:
  1. **상호배제 (Mutual Exclusion)**: 한 번에 한 프로세스만 자원 사용.
  2. **점유와 대기 (Hold and Wait)**: 자원을 가진 채로 다른 자원을 기다림.
  3. **비선점 (Non-Preemption)**: 남의 자원을 강제로 뺏을 수 없음.
  4. **환형 대기 (Circular Wait)**: 꼬리에 꼬리를 물고 서로의 자원을 기다림.
- **교착상태 해결 방법 (Handling Deadlocks)**:
  - **예방 (Prevention)**: 4가지 조건 중 하나를 부정 (자원 낭비 심함).
  - **회피 (Avoidance)**: 발생 가능성을 피해 자원 할당 (예: **은행원 알고리즘**, 자원 할당 그래프).
  - **발견 (Detection)**: 발생을 허용하고 나중에 감시하여 발견.
  - **복구 (Recovery)**: 발견 후 프로세스를 종료하여 자원 회복 (기아 상태 주의).

**Giải thích (Vietnamese):**
Deadlock (Bế tắc) giống như kẹt xe ở ngã tư. Ai cũng tiến lên một chút (Chiếm giữ), không ai chịu lùi (Không thể cướp quyền), và chờ người kia nhường đường (Vòng tròn chờ đợi).
- Phòng ngừa (Prevention): Xây cầu vượt để không bao giờ kẹt xe (Tốn kém).
- Né tránh (Avoidance): Xem Google Maps, thấy đường đỏ (nguy cơ kẹt) thì không đi vào (Thuật toán Banker).
- Phục hồi (Recovery): Kẹt rồi thì gọi công an đến cẩu bớt 1 xe đi để thông đường.

**💡 Mẹo ghi nhớ (Mnemonics):**
Điều kiện: **상점비환** (Tương - Chiếm - Phi - Hoàn)
Giải quyết: **예회발복** (Dự - Tị - Phát - Phục).

---

## 087. 환경변수와 쉘 스크립트 명령어 (Environment Variables & Shell Scripts)
- **환경변수 명령어**:
  - `printenv`: 단일 변수 반환.
  - `env`: 환경 변수 출력/설정.
  - `set` / `setenv`: 변수 추가/업데이트.
  - `export`: 변수를 전역(Global) 변수로 변경 (export 안하면 현재 쉘에만 국한됨).
- **운영체제별 주요 명령어 (Windows / Unix(Linux))**:
  - 목록 보기: `dir` / `ls`
  - 복사: `copy` / `cp`
  - 삭제: `del` / `rm`
  - 이름 변경/이동: `ren`, `move` / `mv`
  - 폴더 생성: `md` / `mkdir`
  - 기타 Unix 명령어:
    - `chmod`: 권한 변경. / `chown`: 소유자 변경.
    - `cat`: 파일 내용 출력.
    - `grep`: 문자열(패턴) 검색 (Windows의 `find`).
    - `ps`: 프로세스 상태. / `kill`: 프로세스 종료.
    - `tar`: 파일 묶기/풀기. / `crontab`: 스케줄링.

**Giải thích (Vietnamese):**
- Lệnh `export` rất hay dùng trong Linux để set biến môi trường (Ví dụ: `export PATH=...`) để các chương trình khác cũng đọc được biến đó.
- Các lệnh Linux kinh điển: `ls` (list - liệt kê), `cp` (copy), `rm` (remove), `mv` (move), `mkdir` (make directory), `grep` (tìm text).

---

## 088. 인터넷 구성과 네트워크 - OSI 7계층 (OSI 7 Layer)
- **IEEE 802 표준**: 802.3 (Ethernet, 유선랜), 802.11 (무선랜, Wi-Fi).
- **OSI 7계층 (상위 계층부터)**:
  7. **응용 계층 (Application)**: 사용자 인터페이스. (HTTP, FTP, DNS) - 데이터 단위: Data.
  6. **표현 계층 (Presentation)**: 암호화, 압축, 포맷 변환. - 데이터 단위: Data.
  5. **세션 계층 (Session)**: 응용 프로그램 간 논리적 연결 생성/유지. - 데이터 단위: Data.
  4. **전송 계층 (Transport)**: 종단 간(End-to-End) 신뢰성 있는 전송. 포트 번호 사용. (TCP, UDP). 장비: L4 스위치. - 데이터 단위: Segment.
  3. **네트워크 계층 (Network)**: 경로 설정(Routing). IP 주소 사용. (IP, ICMP, ARP). 장비: 라우터, L3 스위치. - 데이터 단위: Packet.
  2. **데이터 링크 계층 (Data Link)**: 인접 노드 간 전송 제어, 오류/흐름 제어. MAC 주소 사용. (HDLC, PPP). 장비: 브리지, L2 스위치. - 데이터 단위: Frame.
  1. **물리 계층 (Physical)**: 전기적 신호 전송. 장비: 허브, 리피터. - 데이터 단위: Bit.

**Giải thích (Vietnamese):**
Mô hình OSI 7 lớp chia nhỏ quá trình gửi dữ liệu qua mạng.
Tầng 1 (Cáp mạng, dây điện), Tầng 2 (Truyền giữa 2 máy tính kề nhau qua địa chỉ MAC), Tầng 3 (Tìm đường đi trên mạng Internet qua IP), Tầng 4 (Đảm bảo gói tin không bị rớt qua TCP/UDP), Tầng 5-7 (Phần mềm xử lý hiển thị lên màn hình).

**💡 Mẹo ghi nhớ (Mnemonics):**
Tên 7 tầng từ dưới lên (1->7): **물데네 전세표응** (Vật - Dữ - Mạng - Truyền - Phiên - Biểu - Ứng).
Đơn vị dữ liệu (1->4): **비프패세** (Bit, Frame, Packet, Segment).

---

## 088. 인터넷 구성과 네트워크 - TCP vs UDP & 흐름/오류 제어
- **TCP (Transmission Control Protocol)**: 연결 지향, 신뢰성 높음, 흐름 및 오류 제어 지원. 속도는 느림.
- **UDP (User Datagram Protocol)**: 비연결 지향, 신뢰성 낮음(오류 복구 안함). 실시간 전송(스트리밍)에 유리하여 속도가 빠름.
- **TCP 흐름 제어 (Flow Control)**: 수신측이 처리할 수 있는 만큼만 보냄 (Window 크기 사용).
  - Stop and Wait: 1개 보내고 응답 기다림.
  - Sliding Window: 윈도우 크기만큼 한 번에 여러 개 보냄 (효율적).
- **TCP 오류 제어 (Error Control)**:
  - Go Back n: 오류 발생한 패킷부터 **그 이후의 모든 패킷** 재전송.
  - Selective Repeat: 오류가 발생한 **해당 패킷만** 골라서 재전송.

**Giải thích (Vietnamese):**
- TCP giống như gửi thư bảo đảm, phải có người ký nhận mới yên tâm. Chậm nhưng chắc.
- UDP giống như phát loa phóng thanh, cứ phát ra, ai nghe được thì nghe. Phù hợp gọi Video call (Rớt 1 hình cũng không sao, quan trọng là độ trễ thấp).
- Trượt cửa sổ (Sliding Window): Kỹ thuật gửi liên tục nhiều gói tin mà không cần đợi từng gói báo nhận.
- Go Back N: Bị lỗi gói số 3, hệ thống sẽ gửi lại từ gói 3, 4, 5... Selective Repeat: Lỗi gói 3 thì chỉ gửi lại đúng gói 3.

---

## 089. IP와 서브네팅, IPv4 vs IPv6 (IP & Subnetting)
- **IPv4 헤더 필드**: Version, Header Length, TOS, Total Length, TTL (수명), Source/Destination Address 등.
- **IPv4 클래스**:
  - Class A: `0.~` (거대 망)
  - Class B: `128.~` (중형 망)
  - Class C: `192.~` (소형 망)
- **IPv4 vs IPv6**:
  - 주소 길이: IPv4(32비트) -> **IPv6(128비트)** 확장.
  - IPv6 특징: 호스트 주소 자동 설정, 패킷 크기 제한 없음, 헤더 단순화, **보안(인증/무결성) 강화**, 플로 레이블링(QoS), 이동성 지원.
- **데이터 전송 방법**:
  - **유니캐스트 (Unicast)**: 1:1 통신.
  - **멀티캐스트 (Multicast)**: 1:N (특정 그룹).
  - **브로드캐스트 (Broadcast)**: 1:전체 (IPv4에서만 사용, 과부하 원인).
  - **애니캐스트 (Anycast)**: 1:가장 가까운 1개 노드 (IPv6에서 도입).

**Giải thích (Vietnamese):**
IPv4 sắp hết số (vì chỉ có 32 bit = khoảng 4 tỷ địa chỉ). Nên người ta sinh ra IPv6 (128 bit = số lượng vô hạn). IPv6 bảo mật tốt hơn, không cần cấu hình DHCP phức tạp (tự gán địa chỉ) và loại bỏ Broadcast để tránh nghẽn mạng.

**💡 Mẹo ghi nhớ (Mnemonics):**
Các kiểu truyền:
- Unicast = Nói chuyện riêng.
- Multicast = Nhắn tin vào group chat Zalo.
- Broadcast = Cầm loa hét cho cả trường nghe (Chỉ IPv4).
- Anycast = Gọi tổng đài, ai rảnh thì nhấc máy nghe trước (Chỉ IPv6).

---

## 추가: 응용 SW 기초 기술 (4과목 핵심 요약 1)

### 232. 배치 프로그램 (Batch Program)
- 대량의 데이터를 사용자 개입 없이 정해진 순서에 따라 **일괄적으로 처리**하는 방식.
- 야간 시간대 등 자원 소모가 적은 시간에 실행됨.
- **필수 요소 5가지**: 대용량, 자동화, 견고성, 안정성, 성능.

**Giải thích (Vietnamese):**
Chương trình Batch (xử lý hàng loạt) là loại phần mềm tự động chạy ngầm, thường vào ban đêm. Ví dụ: Cuối ngày ngân hàng tổng hợp lại toàn bộ giao dịch trong ngày, xử lý một lúc hàng triệu giao dịch mà không cần người bấm nút.

### 233 & 235. 데이터 타입 크기 (Data Type Sizes - C/C++ vs JAVA)
- **C/C++**: `char`(1바이트), `short`(2바이트), `int`(4바이트), `float`(4바이트), `double`(8바이트).
- **JAVA**: `byte`(1바이트), **`char`(2바이트, 유니코드 지원)**, `int`(4바이트), `boolean`(1바이트).

**Giải thích (Vietnamese):**
Lưu ý quan trọng: Trong C, `char` (kí tự) chiếm 1 byte. Nhưng trong Java, `char` chiếm 2 byte vì Java dùng bảng mã Unicode để hỗ trợ mọi ngôn ngữ trên thế giới (kể cả tiếng Hàn, tiếng Việt).

### 234. C언어의 구조체 (struct)
- 서로 다른 데이터 타입을 하나로 묶어 관리하는 사용자 정의 자료형. 배열(동일 타입)과의 차이점.
- (Ví dụ: Một `struct SinhVien` có thể chứa Tên(string), Tuổi(int), Điểm(float)).

### 236. Python 시퀀스 자료형
- 리스트(List): `[]` 변경 가능.
- 튜플(Tuple): `()` **변경 불가능(Immutable)**.
- (Ví dụ: Tuple dùng để lưu toạ độ GPS không bao giờ đổi).

### 238. 가비지 콜렉터 (Garbage Collector)
- 사용되지 않는 메모리를 자동으로 해제해주는 기능 (메모리 누수 방지). Java 등 현대 언어의 핵심.

### 239 - 244. 각종 연산자
- 산술(`%`, `++`), 관계(`==`, `!=`), 비트(`&`, `|`, `^`, `<<`), 논리(`&&`, `||`), 대입(`+=`), 조건 삼항연산자.
- `a += 1`은 `a = a + 1`과 같다.
- 비트 XOR(`^`): 두 비트가 다를 때만 1을 반환.
## 232. 배치 프로그램 (Batch Program)
- 대량의 데이터를 사용자 개입 없이 정해진 순서에 따라 **일괄적으로 처리**하는 방식.
- 야간 시간대 등 자원 소모가 적은 시간에 실행됨.
- **필수 요소 5가지**: 대용량, 자동화, 견고성(오류 시에도 중단 없이 기록/지속), 안정성, 성능.

**Giải thích (Vietnamese):**
Chương trình Batch (xử lý hàng loạt) tự động chạy ngầm để xử lý lượng lớn dữ liệu mà không cần con người can thiệp.
- Tính kiên cố (견고성): Lỡ có 1 dòng dữ liệu bị lỗi, chương trình không bị sập mà sẽ ghi log lại và chạy tiếp dòng khác.

**💡 Mẹo ghi nhớ (Mnemonics):**
**대자견안성** (Đại - Tự - Kiên - An - Tính): 대용량, 자동화, 견고성, 안정성, 성능.

---

## 233. C/C++의 데이터 타입 크기 (Data Type Sizes in C/C++)
- `char`: 1바이트 (문자 하나)
- `short`: 2바이트 (짧은 정수)
- `int` / `long`: 4바이트 (기본 정수)
- `long long`: 8바이트 (긴 정수)
- `float`: 4바이트 (실수)
- `double`: 8바이트 (정밀도 높은 실수)

**Giải thích (Vietnamese):**
Kích thước bộ nhớ các biến trong C/C++. Chữ cái (char) chiếm 1 byte. Số nguyên (int) chiếm 4 byte. Số thực (float) 4 byte, double (gấp đôi) là 8 byte.

---

## 234. C언어의 구조체 (struct in C)
- 서로 다른 데이터 유형을 가진 변수들을 하나로 묶어 관리하는 사용자 정의 자료형.
- 배열(Array)은 **동일한 자료형**만 모으지만, 구조체(Struct)는 **상이한 자료형**을 모을 수 있음.

**Giải thích (Vietnamese):**
Struct (Cấu trúc) dùng để gom nhóm nhiều biến khác kiểu lại với nhau. Ví dụ tạo kiểu `SinhVien` gồm tên (chuỗi) và tuổi (số). Trong khi Mảng (Array) chỉ được lưu cùng một kiểu (hoặc toàn chuỗi, hoặc toàn số).

---

## 235. JAVA의 데이터 타입 크기 (Data Type Sizes in JAVA)
- `byte`: 1바이트 (작은 숫자)
- `boolean`: 1바이트 (참/거짓)
- **`char`: 2바이트** (유니코드 지원으로 인해 C언어와 달리 2바이트를 차지함)
- `int`: 4바이트
- `long`: 8바이트 (C언어는 보통 4바이트지만 JAVA는 8바이트)
- `float`: 4바이트 / `double`: 8바이트

**Giải thích (Vietnamese):**
Java có 2 điểm khác biệt lớn với C: `char` chiếm 2 byte (để lưu bảng mã Unicode đa ngôn ngữ), và có kiểu `boolean` (chỉ lưu True/False).

---

## 236. Python의 시퀀스 자료형 (Sequence Data Types in Python)
- 여러 값이 연속적으로 이어진 데이터 구조.
- **리스트(List)**: `[]` 사용. 데이터의 추가/삭제/변경이 자유로움 (Mutable).
- **튜플(Tuple)**: `()` 사용. 한 번 생성하면 데이터의 변경(수정/삭제)이 **불가능함** (Immutable). 읽기 전용에 적합.
- **range**: 반복문에서 연속된 숫자를 생성할 때 사용.

**Giải thích (Vietnamese):**
List và Tuple đều dùng để lưu danh sách. Nhưng List có thể sửa được, còn Tuple thì "Bất di bất dịch" (không thể thêm/xoá/sửa sau khi tạo).

---

## 237. 변수명 작성 규칙 (Variable Naming Rules)
- 영문자, 숫자, 밑줄(`_`)의 조합만 가능.
- **첫 글자는 숫자로 시작할 수 없음** (예: `1a` 안됨).
- 공백이나 특수문자(`+`, `-`, `*`, `/`, `@` 등) 사용 금지.
- 예약어(`if`, `for`, `while` 등) 사용 금지.
- 대소문자 엄격히 구분.

**Giải thích (Vietnamese):**
Quy tắc đặt tên biến: Không được bắt đầu bằng số, không có khoảng trắng, không chứa ký tự đặc biệt (trừ dấu gạch dưới `_`), không dùng từ khoá của ngôn ngữ.

---

## 238. 가비지 콜렉터 (Garbage Collector)
- 더 이상 사용되지 않고 메모리를 점유하고 있는 변수/객체를 시스템이 **자동으로 해제**하여 자원을 회수하는 모듈.
- 메모리 누수(Memory Leak)를 방지. JAVA 등에서 사용됨.

**Giải thích (Vietnamese):**
"Người dọn rác" tự động. Bạn cứ việc tạo biến dùng, khi không dùng nữa, hệ thống sẽ tự động xoá nó khỏi RAM để giải phóng bộ nhớ. Trong C/C++ bạn phải tự dọn dẹp, nhưng Java/Python có tính năng này.

---

## 239 - 243. 연산자 (Operators)
- **산술 연산자**: 사칙연산, `%`(나머지), `++`/`--`(증감).
  - 전치(`++a`): 먼저 증가시키고 연산. 후치(`a++`): 연산 후 증가시킴.
- **관계 연산자**: `==`(같다), `!=`(다르다), `>`, `<`. C언어에서는 0 이외의 값을 참(True)으로 간주.
- **비트 연산자**: 비트 단위 연산. `&`(AND), `|`(OR), `^`(XOR: 서로 다를 때만 1), `~`(NOT). `<<`, `>>`(비트 이동).
- **논리 연산자**: `&&`(AND), `||`(OR), `!`(NOT).
- **대입 연산자**: `=`, `+=`, `-=` 등. `a += 1`은 `a = a + 1`과 동일.

---

## 244. 조건(삼항) 연산자 (Ternary Operator)
- 조건의 참/거짓에 따라 서로 다른 값을 반환.
- 형식: `조건 ? 참일때_값 : 거짓일때_값;`
- (예: `int max = (a > b) ? a : b;`)

**Giải thích (Vietnamese):**
Toán tử 3 ngôi giúp viết tắt câu lệnh if-else trên 1 dòng. Trả về giá trị 1 nếu điều kiện đúng, giá trị 2 nếu sai.

---

## 245. 연산자 우선순위 (Operator Precedence)
- 하나의 수식에 여러 연산자가 있을 때 계산되는 순서.
- 순위: **단항**(`!`, `++`, `~`) > **산술**(`*`, `/` > `+`, `-`) > **관계**(`>`, `==`) > **논리**(`&&` > `||`) > **대입**(`=`, `+=`).
- 괄호 `()`가 가장 우선.

**Giải thích (Vietnamese):**
Thứ tự ưu tiên tính toán: Ngoặc () -> Đơn nguyên (phủ định, tăng giảm) -> Nhân chia cộng trừ -> So sánh -> Logic (AND trước OR sau) -> Gán.

**💡 Mẹo ghi nhớ (Mnemonics):**
**단산관논대** (Đơn - Toán - Quan - Luận - Gán): 단항 -> 산술 -> 관계 -> 논리 -> 대입.

---

## 246 - 249. 입출력 함수와 포맷 (I/O Functions & Formats)
- **`scanf("서식문자열", &변수)`**: C언어 표준 입력. 변수명 앞에 주소 연산자 **`&`**를 반드시 붙여야 함.
- **`printf("서식문자열", 변수)`**: C언어 표준 출력. `&`를 붙이지 않음.
- **서식 문자열**:
  - `%d`: 10진수 정수 / `%f`: 실수 (예: `%8.2f`는 총 8자리, 소수점 2자리) / `%c`: 문자 1개 / `%s`: 문자열.
  - `%o`: 8진수 / `%x`: 16진수.
- **제어문자 (Escape Sequence)**:
  - `\n`: 줄바꿈 (New Line) / `\t`: 탭 (Tab) / `\b`: 백스페이스 / `\0`: 널 문자(문자열의 끝 표시).

**Giải thích (Vietnamese):**
Nhớ kĩ `scanf` phải có dấu `&` (địa chỉ) để nhét dữ liệu vào đúng chỗ trong RAM. `printf` thì không cần. Dấu `\0` (Null) cực kỳ quan trọng trong C để đánh dấu kết thúc một chuỗi (string).

---

## 250. JAVA에서의 표준 출력 (Standard Output in JAVA)
- `System.out.print()`: 형식 없이 그대로 출력 (줄바꿈 없음).
- `System.out.println()`: 출력 후 자동으로 줄바꿈(Enter) 수행.
- `System.out.printf()`: C언어처럼 서식 문자열(`%d` 등)을 사용하여 출력.
- 문자열과 변수를 섞어 쓸 때 `+` 연산자로 연결 가능.

---

## 251. 단순 if문 (Simple if Statement)
- 조건의 참/거짓에 따라 실행할 문장 결정.
- 문장이 두 개 이상이면 반드시 중괄호 `{ }`로 묶어야 함.
- C언어에서는 조건식 결과가 0이면 거짓(False), **0 이외의 모든 값은 참(True)**으로 간주.

---

## 252. 다중 if문 (Multiple if Statement)
- 처리할 조건이 여러 개일 때 `else if`를 사용해 순차적으로 판단.
- 위에서 조건이 참이면 해당 블록을 실행하고 빠져나옴 (아래 조건은 검사하지 않음).
- 모든 조건이 거짓일 때 마지막 `else`가 실행됨.

---

## 253. switch문 (switch Statement)
- 변수의 값에 따라 일치하는 `case` 문장을 실행하는 다분기 제어문.
## 254 - 257. 반복문과 제어 키워드 (Loops & Control Keywords)
- **for문**: 횟수가 정해진 반복(초기화, 조건검사, 증감식). 배열 순회에 주로 사용.
- **while문**: 조건이 참인 동안 반복(선행 판단). 조건이 항상 참이면 무한 루프 발생.
- **do~while문**: **최소 1번은 무조건 실행**한 후 조건을 검사(후행 판단).
- **break**: 현재 실행 중인 루프(블록)를 즉시 완전히 빠져나감.
- **continue**: 루프를 완전히 빠져나가지 않고, **다음 반복 회차로 건너뜀**.

**Giải thích (Vietnamese):**
- `for`: Biết trước số lần lặp (VD: đếm từ 1 đến 10).
- `while`: Lặp cho đến khi điều kiện sai (VD: lặp tới khi game over).
- `break`: Dừng cuộc chơi ngay lập tức, thoát ra ngoài.
- `continue`: Bỏ qua vòng lặp hiện tại, đi tới vòng lặp tiếp theo (VD: đếm từ 1 đến 10, nếu gặp số 5 thì `continue` -> in ra 1 2 3 4 6 7 8 9 10).

---

## 258 - 261. 배열과 문자열 (Arrays & Strings)
- **배열 (Array)**: **동일한 자료형**의 변수들을 연속된 메모리에 모아둔 것. `인덱스(첨자)`는 0부터 시작. 배열 이름 자체가 **첫 번째 요소의 시작 주소**를 의미.
- **2차원 배열**: 행과 열의 평면 구조 (예: `a[3][4]`는 3행 4열로 총 12개).
- **배열 초기화**: 선언과 동시에 값을 넣는 것. 크기를 생략해도 값의 개수만큼 자동 결정됨. 초기화되지 않은 빈칸은 자동으로 `0`으로 채워짐.
- **배열 형태의 문자열 (C언어)**: C언어는 문자열 자료형이 없어 `char` 배열을 사용. 문자열 끝에는 반드시 **널 문자(`\0`)**가 포함되어야 함 (글자수 + 1바이트 크기 필요).

**Giải thích (Vietnamese):**
Trong C, chuỗi "love" sẽ chiếm 5 ô nhớ (l, o, v, e, `\0`). Ký tự `\0` (Null) báo hiệu cho máy tính biết "đây là kết thúc của chuỗi".

---

## 262 - 263. 포인터 (Pointers)
- **포인터 (Pointer)**: 변수의 실제 **메모리 주소값**을 저장하는 특수 변수.
- `*` (간접 참조 연산자): 포인터가 가리키는 주소의 '값'.
- `&` (주소 연산자): 변수의 '주소'.
- **포인터와 배열**: 배열 이름은 포인터와 같음 (`배열명 == &배열명[0]`). 포인터 연산(`p+i`)으로 배열 요소에 접근 가능.

**Giải thích (Vietnamese):**
Pointer (Con trỏ) không lưu giá trị (như số 5), mà lưu "địa chỉ nhà" (ví dụ: nhà số 100A). 
`&a` là lấy địa chỉ nhà của a. `*p` là mở cửa vào nhà để lấy đồ (lấy giá trị).

---

## 264 - 274. 파이썬 문법 (Python Syntax & Basics)
- **기본 문법**: 자료형 선언 생략, 세미콜론(`;`) 불필요. 코드 블록은 중괄호 `{}` 대신 **콜론(`:`)과 들여쓰기(Indentation)**로 구분.
- **입출력**: `input()` (기본적으로 모두 문자열로 입력받음), `print()`. `sep`(분리 문자), `end`(종료 문자).
- **형변환 (Casting)**: `int()`(정수), `float()`(실수). 여러 개 입력 받을 땐 `map(int, input().split())` 사용.
- **자료형**:
  - **리스트 (List, `[]`)**: 수정/추가/삭제 자유로움 (Mutable). 서로 다른 타입 혼용 가능.
  - **딕셔너리 (Dictionary, `{}`)**: `Key:Value` 쌍으로 저장 (해시 맵). Key로 빠르게 검색.
  - **슬라이스 (Slice)**: `객체[시작:끝:증가값]`. 끝 번호는 제외됨 (n-1까지). 원본은 변경하지 않음.
- **제어문**: `if`, **`elif`** (else if 아님), `else`. `for i in range(시작, 끝)` 또는 `for i in 리스트`. `while`문.
- **클래스 (Class)**: `class` 키워드. 메소드(함수) 정의 시 첫 번째 매개변수로 반드시 **`self`**를 써야 함. 파이썬은 클래스 밖에서도 `def`로 독립된 함수를 만들 수 있음.

**Giải thích (Vietnamese):**
- Python dùng "thụt lề" (indentation) để phân chia các khối code thay vì `{}`.
- `input()` luôn trả về chuỗi (String). Nếu nhập số 5, nó hiểu là chữ "5". Phải bọc lại bằng `int(input())`.
- Dictionary giống như từ điển: tra chữ "Apple" (Key) ra "Quả táo" (Value).
- Cắt lát (Slicing): `a[1:4]` lấy các phần tử ở index 1, 2, 3 (không lấy 4).

---

## 275 - 278. 프로그래밍 언어의 종류 (Types of Programming Languages)
- **절차적 언어**: 실행 순서 중시. 
  - `COBOL` (사무용), `FORTRAN` (과학 기술 계산용), `C` (시스템 프로그래밍), `ALGOL`.
- **객체지향 언어**: 데이터+기능 캡슐화. 재사용성 높음.
  - `JAVA` (플랫폼 독립성, JVM), `C++` (C의 객체지향 확장), `Smalltalk` (최초 GUI, 순수 객체지향).
- **선언형 언어**: '무엇(What)'을 할지 기술 (함수형/논리형).
  - `LISP` (연결리스트, AI용), `PROLOG` (논리 추론, AI용), `Haskell` (순수 함수형), `XML` (구조화 문서).

---

## 279 - 280. 라이브러리 (Library)
- **라이브러리**: 자주 사용되는 함수/데이터를 모아 놓은 집합체 (개발 시간 단축, 코드 재사용).
- **C언어 표준 라이브러리 (Header Files)**:
  - `stdio.h`: 입출력 (`printf`, `scanf`)
  - `math.h`: 수학 연산 (`sqrt`, `pow`, `abs`)
  - `string.h`: 문자열 처리
  - `stdlib.h`: 유틸리티, 자료형 변환, 메모리 할당

**Giải thích (Vietnamese):**
Thư viện (Library) giống như siêu thị bán đồ làm sẵn. Bạn không cần tự viết code để tính căn bậc 2, chỉ cần gọi hàm `sqrt` trong thư viện `math.h` là xong.

---

## 281. 매시업과 SOA (SW Related Terms: Mashup & SOA)
- **매시업 (Mashup)**: 웹 서비스나 콘텐츠를 조합하여 **새로운 서비스를 만드는 기술** (예: 구글 지도 + 부동산 정보).
- **SOA (Service Oriented Architecture, 서비스 지향 아키텍처)**: 시스템을 **공유/재사용 가능한 서비스 단위**로 구축하는 구조. (계층: 표현, 업무 프로세스, 서비스 중간, 애플리케이션, 데이터 저장).

**Giải thích (Vietnamese):**
- Mashup: Lấy dữ liệu bản đồ của Google kết hợp với dữ liệu danh sách quán ăn để tạo ra app "Tìm quán ăn gần đây". (Trộn lẫn dữ liệu có sẵn để làm ra cái mới).

---

## 282. 운영체제의 정의 및 목적 (Definition & Purpose of OS)
- **운영체제(OS)**: 컴퓨터 자원(CPU, 메모리 등)을 효율적으로 관리하고 사용자에게 편리한 환경을 제공하는 소프트웨어 (Windows, Linux 등).
- 목적: 자원 관리, 편리한 인터페이스 제공, 가용성 극대화, 신뢰도 향상.
## 283 - 288. 운영체제 구성 및 UNIX 시스템 (OS & UNIX)
- **운영체제 구성**:
  - **제어 프로그램**: 감시(Supervisor, 핵심), 작업 제어, 데이터 관리.
  - **처리 프로그램**: 언어 번역(컴파일러), 서비스(유틸리티).
- **UNIX의 특징**: 대화식 운영체제, **C언어로 작성**되어 이식성이 높음. 트리(Tree) 구조의 파일 시스템.
  - **커널(Kernel)**: UNIX의 핵심. 하드웨어/메모리/프로세스 관리.
  - **쉘(Shell)**: 사용자의 명령어를 해석하여 커널에 전달하는 인터페이스.
- **파일 디스크립터 (File Descriptor)**: 시스템이 파일을 관리하기 위해 이름, 위치, 크기 등의 속성을 담아두는 제어 블록 (사용자가 직접 볼 수 없음).
- **UNIX 환경 변수**: `$HOME`(홈 디렉터리), `$PATH`(명령어 검색 경로), `$PWD`(현재 작업 폴더).
- **UNIX 명령어**: `chmod`(권한 변경), `fork`(프로세스 복제).

**Giải thích (Vietnamese):**
- Kernel là não bộ, Shell là lớp vỏ giao tiếp với người dùng.
- Lệnh `fork` trong Unix dùng để nhân bản một Process đang chạy thành một Process con mới.

---

## 289 - 296. 메모리 관리 및 가상 기억장치 (Memory Management)
- **배치 전략 (Placement)**: 최초 적합(First Fit, 빠름), 최적 적합(Best Fit, 단편화 최소), 최악 적합(Worst Fit, 큰 공간 남김).
- **페이징(Paging)**: 메모리를 **동일한 고정 크기**로 나눔. **내부 단편화** 발생 (빈 공간이 남아버림).
- **세그먼테이션(Segmentation)**: 논리적 의미(함수 등)에 따라 **가변 크기**로 나눔. **외부 단편화** 발생 (공간이 작아서 못 들어감).
- **페이지 크기**: 페이지가 작으면 내부 단편화는 줄지만, 맵 테이블이 커져 매핑 속도가 느려짐.
- **스래싱 (Thrashing)**: 빈번한 페이지 교체로 인해 시스템 처리량보다 교체 시간이 더 많아져 CPU 이용률이 급감하는 마비 상태.

**Giải thích (Vietnamese):**
- Paging (Phân trang): Cắt bánh thành các miếng bằng nhau. Điểm yếu: Ăn không hết 1 miếng sẽ dư thừa (Nội phân mảnh).
- Segmentation (Phân đoạn): Cắt bánh theo sức ăn của mỗi người (to nhỏ khác nhau). Điểm yếu: Chừa lại các khoảng trống lắt nhắt không ai nhét vừa (Ngoại phân mảnh).
- Thrashing: Máy quá tải, giật lag do mải lấy dữ liệu từ ổ cứng đắp vào RAM.

---

## 297 - 302. 프로세스와 스레드, 스케줄링 (Processes, Threads & Scheduling)
- **프로세스(Process)**: **PCB(Process Control Block)를 가진** 실행 중인 프로그램.
- **상태 전이**:
  - **Dispatch**: 준비(Ready) -> 실행(Run) (CPU 할당 받음).
  - **Timeout**: 실행(Run) -> 준비(Ready) (시간 초과).
  - **Wake Up**: 대기(Wait) -> 준비(Ready) (입출력 완료).
- **스레드(Thread)**: 프로세스 내의 독립적인 실행 흐름 (최소 작업 단위). 프로세스의 자원을 공유하여 병행성 증대 및 문맥 교환 오버헤드 감소.
- **비선점 스케줄링 (Non-Preemptive)**:
  - FCFS: 먼저 온 순서대로.
  - SJF: 실행 시간이 가장 짧은 것 먼저.
  - **HRN**: 대기 시간과 서비스 시간을 고려해 기아(Starvation) 현상 해결. 공식: **(대기시간 + 서비스시간) / 서비스시간** (값이 클수록 우선).

---

## 305 - 308. IP 주소 체계 (IPv4 vs IPv6)
- **IPv4**: 32비트 (8비트씩 4부분). 클래스 A~E로 나뉨.
- **IPv6**: 128비트 (16비트씩 8부분). 콜론(`:`)으로 구분, 16진수 사용. 
- **IPv6의 특징**: 무한대에 가까운 주소, 보안 강화, 패킷 크기 확장, PnP(자동 설정).
- **IPv6 전송 방식**: 유니캐스트(1:1), 멀티캐스트(1:N), 애니캐스트(가장 가까운 1:1).

**💡 Mẹo ghi nhớ (Mnemonics):**
IPv6 전송 방식 3총사: **유멀애** (Unicast, Multicast, Anycast). *Broadcast는 IPv4에만 있음!*

---

## 309 - 314. OSI 7계층과 네트워크 프로토콜 (OSI 7 Layers & Protocols)
- **응용 계층 (Application, 7계층)**: HTTP(웹), FTP(파일), SMTP(메일), DNS(도메인->IP 변환), SNMP(네트워크 관리).
- **전송 계층 (Transport, 4계층)**: 
  - **TCP**: 연결형, 신뢰성 보장, 양방향. 흐름 제어.
  - **UDP**: 비연결형, 신뢰성 낮음. 속도가 빨라 스트리밍에 유리.
- **인터넷/네트워크 계층 (Network, 3계층)**: 라우터 사용.
  - **IP**: 경로 설정.
  - **ICMP**: 오류 보고 및 제어.
  - **ARP**: IP 주소 -> MAC 주소 변환. (**RARP**는 반대).
- **데이터 링크/네트워크 액세스 계층 (Data Link, 2계층)**: Ethernet(CSMA/CD 방식), HDLC.

**Giải thích (Vietnamese):**
- **ARP**: Khi biết địa chỉ IP, dùng ARP để hỏi xem "Máy nào có IP này, cho xin địa chỉ MAC của card mạng (phần cứng)".
- **ICMP**: Lệnh `ping` hay dùng trên máy tính chính là chạy giao thức ICMP để kiểm tra mạng có thông không.

---

## 226 - 227. 데이터베이스 접속 기술 (Database Connectivity)
- **JDBC (Java DataBase Connectivity)**: **자바(Java)** 프로그램 내에서 데이터베이스(DBMS)에 접속하여 SQL 문을 실행하기 위한 표준 API. 운영체제에 독립적.
- **ODBC (Open DataBase Connectivity)**: 프로그래밍 **언어에 관계없이** (C, C++, VB 등) 다양한 DBMS에 접근할 수 있게 마이크로소프트가 만든 개방형 표준 API.

**Giải thích (Vietnamese):**
- JDBC: Dành riêng cho ngôn ngữ Java.
- ODBC: Mở (Open) cho mọi ngôn ngữ khác, dùng chung thông qua một "người quản lý tài xế" (Driver Manager) để dịch lệnh SQL gửi xuống Database.
