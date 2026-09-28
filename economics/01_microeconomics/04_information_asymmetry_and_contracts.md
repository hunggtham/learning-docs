# Thông tin (information / 정보) Asymmetry & Contracts — Adverse selection, moral hazard và principal–tác nhân (agent / 에이전트)

> **Mạch đọc:** Đặt **thông tin (information / 정보) Asymmetry & Contracts — Adverse selection, moral hazard và principal–tác nhân (agent / 에이전트)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. Adverse selection: hidden kiểu (type / 타입) trước giao dịch** sang **2. Insurance thị trường (market / 시장) và selection**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

Thông tin (information / 정보) asymmetry (`정보 비대칭`) xuất hiện khi các bên trong một giao dịch (transaction / 트랜잭션) không có cùng thông tin liên quan đến chất lượng (quality / 품질), rủi ro (risk / 위험), effort hoặc kiểu (type / 타입). Khi thông tin ảnh hưởng payoff nhưng không thể quan sát hoặc verify hoàn hảo, price và đặc tả hợp đồng (contract / 계약) phải làm nhiều việc hơn là chỉ chuyển tiền: chúng còn phải **screen kiểu (type / 타입), tạo incentive và phân bổ rủi ro (risk / 위험)**.

Hai thất bại (failure / 실패) modes nền tảng là **adverse selection** và **moral hazard**. Chúng khác nhau về timing. Adverse selection là hidden thông tin (information / 정보) **trước khi đặc tả hợp đồng (contract / 계약)**; moral hazard là hidden hành động (action / 동작) hoặc hidden trạng thái (state / 상태) **sau khi đặc tả hợp đồng (contract / 계약)**.

## 1. Adverse selection: hidden kiểu (type / 타입) trước giao dịch

Giả sử seller biết chất lượng (quality / 품질) của sản phẩm nhưng buyer không biết. Nếu buyer chỉ nhìn average chất lượng (quality / 품질), họ chỉ willing to pay average giá trị (value / 값). Seller chất lượng (quality / 품질) cao thấy price đó quá thấp và rời thị trường (market / 시장); average chất lượng (quality / 품질) của phần còn lại giảm, khiến buyer tiếp tục hạ willingness to pay.

Đây là lô-gic (logic / 논리) “thị trường (market / 시장) for lemons” của George Akerlof. Vấn đề không phải mọi low-quality seller đều lừa đảo; chỉ cần chất lượng (quality / 품질) khó quan sát và participation quyết định (decision / 결정) phụ thuộc kiểu (type / 타입), composition của thị trường (market / 시장) đã có thể xấu đi.

Một vòng adverse selection có dạng:

```text
Buyer cannot observe type
→ price based on expected average quality
→ high-quality types exit
→ average quality falls
→ price falls further
```

Trong extreme trường hợp (case / 사례), thị trường (market / 시장) có thể unravel dù gains from trade tồn tại với full thông tin (information / 정보).

## 2. Insurance thị trường (market / 시장) và selection

Trong insurance, customer thường biết rủi ro (risk / 위험) của mình tốt hơn insurer ở một số dimensions. Nếu insurer phải charge một pooling premium cho mọi người, low-risk customers có thể thấy premium quá cao và giảm coverage, làm insured pool trở nên riskier.

Điều này không có nghĩa mọi insurance thị trường (market / 시장) tất yếu collapse. Insurer có thể dùng rủi ro (risk / 위험) classification, deductibles, waiting periods, group enrollment hoặc screening questions. Regulation cũng có thể bắt buộc community rating hoặc participation.

Chính sách (policy / 정책) sự đánh đổi (trade-off / 트레이드오프) xuất hiện vì screening theo rủi ro (risk / 위험) tăng actuarial accuracy nhưng có thể giảm redistribution và truy cập (access / 접근) của high-risk group.

## 3. Signaling: informed side tự chứng minh kiểu (type / 타입)

Signaling xảy ra khi bên có private thông tin (information / 정보) chọn một costly hành động (action / 동작) mà types khác nhau khó bắt chước ở cùng chi phí (cost / 비용).

Một tín hiệu (signal / 신호) chỉ hữu ích khi có **separating lô-gic (logic / 논리)**. Nếu cả high kiểu (type / 타입) và low kiểu (type / 타입) đều dễ dàng gửi cùng tín hiệu (signal / 신호), tín hiệu (signal / 신호) không reveal thông tin (information / 정보).

Education có thể được mô hình hóa một phần như human-capital investment và một phần như labor-market tín hiệu (signal / 신호). Trong signaling mô hình (model / 모델) kinh điển, education có thể reveal productivity nếu high-productivity workers chịu education chi phí (cost / 비용) thấp hơn low-productivity workers.

Điều này không chứng minh education “chỉ là tín hiệu (signal / 신호)”. Empirical question là bao nhiêu return đến từ skill formation, selection và signaling trong từng ngữ cảnh (context / 맥락).

## 4. Screening: uninformed side thiết kế menu

Screening là mirror ảnh (image / 이미지) của signaling. Bên thiếu thông tin (information / 정보) đưa ra một menu contracts để các types tự chọn.

Insurance đặc tả hợp đồng (contract / 계약) có thể cho lựa chọn:

```text
High premium + low deductible
Low premium + high deductible
```

Nếu high-risk và low-risk customers đánh đổi premium với deductible khác nhau, menu có thể induce self-selection.

Thiết kế (design / 설계) cần thỏa incentive tính tương thích (compatibility / 호환성): mỗi kiểu (type / 타입) phải muốn chọn đặc tả hợp đồng (contract / 계약) dành cho mình hơn đặc tả hợp đồng (contract / 계약) của kiểu (type / 타입) khác.

## 5. Moral hazard: hidden hành động (action / 동작) sau đặc tả hợp đồng (contract / 계약)

Moral hazard xảy ra khi đặc tả hợp đồng (contract / 계약) thay đổi incentive sau khi được ký và một hành động (action / 동작) quan trọng khó quan sát hoặc verify.

Insurance giảm marginal chi phí (cost / 비용) của risky hành vi (behavior / 동작) hoặc care consumption đối với insured person; employment đặc tả hợp đồng (contract / 계약) có thể làm effort khó monitor; lender không kiểm soát hoàn hảo dự án (project / 프로젝트) rủi ro (risk / 위험) borrower chọn sau khi nhận vốn.

Lô-gic (logic / 논리) cơ bản:

```text
Protection / fixed payment increases
→ actor bears smaller share of marginal consequence
→ behavior may become less aligned with principal's objective
```

“Moral” ở đây là thuật ngữ lịch sử; economics không nhất thiết cáo buộc actor vô đạo đức. Đây là incentive phản hồi (response / 응답) dưới đặc tả hợp đồng (contract / 계약).

## 6. Deductible, copay và skin in the game

Insurance có thể giảm moral hazard bằng deductible hoặc copay. Khi insured vẫn chịu một phần marginal chi phí (cost / 비용), họ có incentive cân nhắc consumption/rủi ro (risk / 위험) kỹ hơn.

Nhưng chi phí (cost / 비용) sharing cũng giảm rủi ro (risk / 위험) protection, là mục tiêu cốt lõi của insurance. Optimal đặc tả hợp đồng (contract / 계약) cân bằng:

```text
Risk sharing
vs.
Incentive provision
```

Nếu household rất risk-averse nhưng hành vi (behavior / 동작) ít responsive, coverage rộng có thể tốt. Nếu hành vi (behavior / 동작) responsive mạnh và monitoring yếu, chi phí (cost / 비용) sharing có giá trị (value / 값) lớn hơn.

## 7. Principal–tác nhân (agent / 에이전트) bài toán (problem / 문제)

Principal–tác nhân (agent / 에이전트) bài toán (problem / 문제) xuất hiện khi principal giao tác vụ (task / 작업) cho tác nhân (agent / 에이전트) nhưng mục tiêu (objective / 목표) không hoàn toàn giống nhau và principal không quan sát đầy đủ hành động (action / 동작) hoặc thông tin (information / 정보) của tác nhân (agent / 에이전트).

Examples:

- shareholder và manager;
- employer và employee;
- patient và doctor;
- voter và politician;
- máy khách (client / 클라이언트) và contractor;
- lender và borrower.

Đặc tả hợp đồng (contract / 계약) cố gắng align payoff của tác nhân (agent / 에이전트) với mục tiêu (objective / 목표) của principal, nhưng hiệu năng (performance / 성능) measure thường imperfect.

## 8. Pay-for-performance và multitasking distortion

Nếu chỉ reward chỉ số (metric / 지표) dễ đo, tác nhân (agent / 에이전트) có thể tối ưu chỉ số (metric / 지표) thay vì mục tiêu (objective / 목표) thật. Giáo viên được trả chỉ theo kiểm thử (test / 테스트) score có incentive “teach to the kiểm thử (test / 테스트)”; salesperson theo revenue có thể discount quá mức; nhà phát triển (developer / 개발자) theo số ticket có thể chia nhỏ công việc (work / 작업) hoặc bỏ chất lượng (quality / 품질).

Đây là multitasking bài toán (problem / 문제). Khi một dimension dễ đo và dimension khác khó đo, strong incentive trên chỉ số (metric / 지표) đầu có thể làm dimension sau xấu đi.

Vì vậy optimal incentive không phải lúc nào cũng “trả theo hiệu năng (performance / 성능) mạnh hơn”. Đôi khi fixed salary, nhóm (team / 팀) incentive, professional norm hoặc subjective evaluation giảm gaming.

## 9. Observable khác verifiable

Một fact có thể observable với các bên nhưng không verifiable bởi court hoặc third party. Hai engineers có thể biết ai effort nhiều hơn, nhưng đặc tả hợp đồng (contract / 계약) không thể enforce nếu bằng chứng (evidence / 증거) không đủ mục tiêu (objective / 목표).

Đặc tả hợp đồng (contract / 계약) lý thuyết (theory / 이론) vì vậy phân biệt:

```text
observable information
vs.
contractible/verifiable information
```

Nhiều incomplete contracts tồn tại không phải vì parties quên viết clause, mà vì future trạng thái (state / 상태) quá phức tạp hoặc không thể verify với chi phí hợp lý.

## 10. Incomplete contracts và residual điều khiển (control / 제어) rights

Khi không thể specify mọi future contingency, quyền sở hữu (ownership / 소유권) và điều khiển (control / 제어) rights trở nên quan trọng. Ai có quyền quyết định trong trạng thái chưa ghi rõ đặc tả hợp đồng (contract / 계약)?

Incomplete-contract lý thuyết (theory / 이론) phân tích residual rights of điều khiển (control / 제어). quyền sở hữu (ownership / 소유권) có thể khuyến khích investment vì đơn vị sở hữu (owner / 오너) giữ nhiều return từ relationship-specific investment, nhưng cũng có thể làm party khác underinvest nếu bargaining power giảm.

Điểm quan trọng là institution thiết kế (design / 설계) không chỉ là price. Quyền quyết định khi đặc tả hợp đồng (contract / 계약) im lặng cũng ảnh hưởng incentive.

## 11. Reputation như repeated-game solution

Trong one-shot giao dịch (transaction / 트랜잭션), seller có thể gain từ chất lượng (quality / 품질) thấp nếu buyer không kiểm tra được. Trong repeated relationship, reputation làm future profit phụ thuộc hiện tại (current / 현재) hành vi (behavior / 동작).

Nếu future nghiệp vụ (business / 비즈니스) có giá trị (value / 값) đủ lớn, seller có incentive duy trì chất lượng (quality / 품질).

Online rà soát (review / 검토), rating, certification và brand đều có thể giảm thông tin (information / 정보) asymmetry, nhưng chúng tạo tầng (layer / 계층) mới: fake rà soát (review / 검토), selection độ lệch (bias / 편향), nền tảng (platform / 플랫폼) manipulation và strategic reputation management.

## 12. Warranty và guarantee như tín hiệu (signal / 신호) + incentive

Warranty có hai vai trò.

Thứ nhất, seller chất lượng (quality / 품질) cao có thể offer warranty với expected repair chi phí (cost / 비용) thấp hơn low-quality seller, nên warranty trở thành tín hiệu (signal / 신호).

Thứ hai, warranty chuyển một phần thất bại (failure / 실패) chi phí (cost / 비용) về seller, tạo incentive cải thiện chất lượng (quality / 품질).

Nhưng broad warranty cũng có thể tăng bên tiêu thụ (consumer / 소비자) moral hazard nếu người dùng (user / 사용자) care giảm. Một đặc tả hợp đồng (contract / 계약) thực tế có thể đồng thời xử lý selection và incentive ở hai phía.

## 13. Certification, licensing và third-party xác minh (verification / 확인)

Third-party certification có thể tạo dùng chung (common / 공통) thông tin (information / 정보) tiêu chuẩn (standard / 표준) khi buyer không tự evaluate chất lượng (quality / 품질). Food an toàn (safety / 안전) inspection, accounting kiểm tra (audit / 감사), professional credential hoặc software bảo mật (security / 보안) certification đều dùng lô-gic (logic / 논리) này.

Nhưng certification có chi phí (cost / 비용) và capture rủi ro (risk / 위험). Nếu tiêu chuẩn (standard / 표준) quá thấp, nó không reveal chất lượng (quality / 품질); nếu quá cao, nó có thể tạo entry barrier không cần thiết.

Vì vậy chính sách (policy / 정책) cần hỏi: hidden thông tin (information / 정보) cụ thể là gì, xác minh (verification / 확인) accuracy bao nhiêu và chi phí (cost / 비용) của false positive/false negative ra sao?

## 14. Credit thị trường (market / 시장), collateral và rationing

Lender đối mặt cả adverse selection lẫn moral hazard. Interest tỷ lệ (rate / 비율) cao có thể thu hút borrower riskier hoặc làm borrower chọn dự án (project / 프로젝트) riskier vì upside thuộc borrower trong khi downside một phần thuộc lender.

Do đó lender không nhất thiết clear thị trường (market / 시장) bằng tăng interest tỷ lệ (rate / 비율) đến khi supply bằng demand. Có thể xuất hiện credit rationing: một số borrowers willing to pay tỷ lệ (rate / 비율) cao vẫn không được vay.

Collateral giảm lender mất mát (loss / 손실) và có thể screen borrower, nhưng collateral yêu cầu (requirement / 요구사항) cũng tạo phân phối (distribution / 분포) tác động (effect / 효과) vì household thiếu wealth bị hạn chế truy cập (access / 접근) dù dự án (project / 프로젝트) có productivity tốt.

## 15. Labor thị trường (market / 시장) và efficiency wage

Nếu worker effort khó monitor, firm có thể trả wage cao hơn market-clearing mức (level / 수준) để tăng chi phí (cost / 비용) của job mất mát (loss / 손실), giảm turnover hoặc thu hút applicant chất lượng (quality / 품질) cao hơn.

Efficiency wage các mô hình (models / 모델들) giải thích vì sao unemployment có thể tồn tại ngay cả khi workers willing to công việc (work / 작업) ở wage thấp hơn. Đây là một example cho việc thông tin (information / 정보)/incentive friction thay đổi simple supply-demand kết quả (result / 결과).

## 16. Healthcare và delegated expertise

Patient thường thiếu medical kiến thức (knowledge / 지식) nên doctor vừa cung cấp dịch vụ (service / 서비스) vừa tư vấn quantity/chất lượng (quality / 품질) cần dùng. Đây là agency relationship với asymmetric thông tin (information / 정보).

Fee-for-service có thể khuyến khích quantity; capitation có thể khuyến khích economize quá mức; salary giảm volume incentive nhưng có thể giảm effort ở một số margins.

Không payment hệ thống (system / 시스템) nào giải quyết hoàn toàn mọi incentive. thiết kế (design / 설계) thường kết hợp payment, chất lượng (quality / 품질) metrics, peer rà soát (review / 검토) và regulation.

## 17. thông tin (information / 정보) disclosure và limits của transparency

Một phản hồi (response / 응답) tự nhiên là bắt buộc disclosure. Nhưng disclosure chỉ hiệu quả khi users hiểu, chú ý và có khả năng hành động trên thông tin (information / 정보).

Nếu disclosure dài, technical hoặc quá nhiều, bounded attention làm tác động (effect / 효과) nhỏ. Firms cũng có thể strategically frame thông tin (information / 정보).

Do đó “more thông tin (information / 정보)” không tự động “better quyết định (decision / 결정)”. thông tin (information / 정보) thiết kế (design / 설계) cần quan tâm salience, comparability và quyết định (decision / 결정) ngữ cảnh (context / 맥락).

## 18. Bayesian updating và belief

Thông tin (information / 정보) problems thường cần lập luận (reasoning / 추론) theo xác suất (probability / 확률). Buyer bắt đầu với prior belief về kiểu (type / 타입), quan sát tín hiệu (signal / 신호) rồi cập nhật (update / 업데이트) posterior bằng Bayes quy tắc (rule / 규칙).

```text
Posterior ∝ Likelihood × Prior
```

Tín hiệu (signal / 신호) mạnh khi likelihood khác nhiều giữa types. Nếu cả types tạo tín hiệu (signal / 신호) với xác suất gần giống nhau, posterior ít thay đổi.

Đây là cầu nối (bridge / 브리지) trực tiếp sang xác suất (probability / 확률)/statistics và econometrics: thông tin (information / 정보) cấu trúc (structure / 구조) là một mô hình (model / 모델) về belief formation, còn dữ liệu (data / 데이터) giúp estimate likelihood và kiểm thử (test / 테스트) predictions.

## 19. Pooling, separating và semi-separating equilibrium

Trong signaling/screening các mô hình (models / 모델들), equilibrium có thể:

- **pooling**: nhiều types chọn cùng hành động (action / 동작)/đặc tả hợp đồng (contract / 계약) nên kiểu (type / 타입) không được reveal;
- **separating**: types chọn khác nhau và thông tin (information / 정보) được reveal;
- **semi-separating**: một số types mix hoặc overlap.

Không nên assume separating kết quả (outcome / 결과) chỉ vì có tín hiệu (signal / 신호). chi phí (cost / 비용) cấu trúc (structure / 구조) và beliefs ngoài equilibrium đường dẫn (path / 경로) quyết định equilibrium tồn tại và được sustain thế nào.

## 20. chính sách (policy / 정책) sự đánh đổi (trade-off / 트레이드오프): privacy vs thông tin (information / 정보) efficiency

More thông tin (information / 정보) có thể giảm adverse selection nhưng làm privacy giảm. Health/genetic dữ liệu (data / 데이터) giúp insurer price rủi ro (risk / 위험) chính xác hơn nhưng có thể làm rủi ro (risk / 위험) sharing yếu đi. Credit dữ liệu (data / 데이터) giảm default bất định (uncertainty / 불확실성) nhưng có thể tạo exclusion hoặc lỗi (error / 오류) persistence.

Đây là một xung đột (conflict / 충돌) giữa allocative thông tin (information / 정보) và xã hội (social / 사회적) objectives khác. Economics có thể map sự đánh đổi (trade-off / 트레이드오프), nhưng normative choice cần law, ethics và institutional ngữ cảnh (context / 맥락).

## 21. thất bại (failure / 실패) modes thường gặp

Sai lầm thứ nhất là gọi mọi bất định (uncertainty / 불확실성) là asymmetric thông tin (information / 정보). Nếu cả hai bên cùng không biết future trạng thái (state / 상태), đó là dùng chung (common / 공통) bất định (uncertainty / 불확실성) chứ chưa chắc thông tin (information / 정보) asymmetry.

Sai lầm thứ hai là nhầm adverse selection với moral hazard. Hãy hỏi hidden thông tin (information / 정보)/hành động (action / 동작) xuất hiện trước hay sau đặc tả hợp đồng (contract / 계약).

Sai lầm thứ ba là nghĩ incentive pay luôn cải thiện hiệu năng (performance / 성능). chỉ số (metric / 지표) distortion và risk-bearing có thể làm kết quả (outcome / 결과) xấu đi.

Sai lầm thứ tư là coi transparency là free solution và bỏ qua attention, comprehension, privacy và gaming.

## 22. mô hình tư duy (mental model / 사고 모델) cho thông tin (information / 정보) bài toán (problem / 문제)

Khi phân tích một thị trường (market / 시장) hoặc đặc tả hợp đồng (contract / 계약), hãy hỏi:

1. Ai biết điều gì mà bên kia không biết?
2. thông tin (information / 정보) là hidden kiểu (type / 타입), hidden hành động (action / 동작) hay hidden trạng thái (state / 상태)?
3. Timing: bài toán (problem / 문제) xuất hiện trước hay sau đặc tả hợp đồng (contract / 계약)?
4. Variable đó observable nhưng có verifiable không?
5. Price/đặc tả hợp đồng (contract / 계약) hiện tại tạo incentive nào?
6. Có tín hiệu (signal / 신호) hoặc menu nào khiến types tự reveal không?
7. đặc tả hợp đồng (contract / 계약) đang trade off rủi ro (risk / 위험) sharing với incentive ra sao?
8. chỉ số (metric / 지표) có thể bị gaming hoặc làm lệch multitask effort không?
9. Reputation, certification, collateral hoặc monitoring có giảm friction không?
10. chính sách (policy / 정책) tăng thông tin (information / 정보) nhưng có chi phí (cost / 비용) về privacy, exclusion hoặc administrative burden không?

Với chapter này, chuỗi microeconomics từ individual choice đến welfare và ba market-failure families đã hoàn chỉnh ở mức nền tảng. Bước kế tiếp là chuyển sang **thị trường (market / 시장) cấu trúc (structure / 구조) và game lý thuyết (theory / 이론)**, nơi payoff của một actor phụ thuộc trực tiếp vào hành động (action / 동작) của các actor khác và price-taking giả định (assumption / 가정) không còn đủ.

> **Bàn giao:** Sau **22. mô hình tư duy (mental model / 사고 모델) cho thông tin (information / 정보) bài toán (problem / 문제)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 consumer and producer theory](./00_consumer_and_producer_theory.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
