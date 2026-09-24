# Information Asymmetry & Contracts — Adverse selection, moral hazard và principal–agent

Information asymmetry (`정보 비대칭`) xuất hiện khi các bên trong một transaction không có cùng thông tin liên quan đến quality, risk, effort hoặc type. Khi thông tin ảnh hưởng payoff nhưng không thể quan sát hoặc verify hoàn hảo, price và contract phải làm nhiều việc hơn là chỉ chuyển tiền: chúng còn phải **screen type, tạo incentive và phân bổ risk**.

Hai failure modes nền tảng là **adverse selection** và **moral hazard**. Chúng khác nhau về timing. Adverse selection là hidden information **trước khi contract**; moral hazard là hidden action hoặc hidden state **sau khi contract**.

## 1. Adverse selection: hidden type trước giao dịch

Giả sử seller biết quality của sản phẩm nhưng buyer không biết. Nếu buyer chỉ nhìn average quality, họ chỉ willing to pay average value. Seller quality cao thấy price đó quá thấp và rời market; average quality của phần còn lại giảm, khiến buyer tiếp tục hạ willingness to pay.

Đây là logic “market for lemons” của George Akerlof. Vấn đề không phải mọi low-quality seller đều lừa đảo; chỉ cần quality khó quan sát và participation decision phụ thuộc type, composition của market đã có thể xấu đi.

Một vòng adverse selection có dạng:

```text
Buyer cannot observe type
→ price based on expected average quality
→ high-quality types exit
→ average quality falls
→ price falls further
```

Trong extreme case, market có thể unravel dù gains from trade tồn tại với full information.

## 2. Insurance market và selection

Trong insurance, customer thường biết risk của mình tốt hơn insurer ở một số dimensions. Nếu insurer phải charge một pooling premium cho mọi người, low-risk customers có thể thấy premium quá cao và giảm coverage, làm insured pool trở nên riskier.

Điều này không có nghĩa mọi insurance market tất yếu collapse. Insurer có thể dùng risk classification, deductibles, waiting periods, group enrollment hoặc screening questions. Regulation cũng có thể bắt buộc community rating hoặc participation.

Policy trade-off xuất hiện vì screening theo risk tăng actuarial accuracy nhưng có thể giảm redistribution và access của high-risk group.

## 3. Signaling: informed side tự chứng minh type

Signaling xảy ra khi bên có private information chọn một costly action mà types khác nhau khó bắt chước ở cùng cost.

Một signal chỉ hữu ích khi có **separating logic**. Nếu cả high type và low type đều dễ dàng gửi cùng signal, signal không reveal information.

Education có thể được mô hình hóa một phần như human-capital investment và một phần như labor-market signal. Trong signaling model kinh điển, education có thể reveal productivity nếu high-productivity workers chịu education cost thấp hơn low-productivity workers.

Điều này không chứng minh education “chỉ là signal”. Empirical question là bao nhiêu return đến từ skill formation, selection và signaling trong từng context.

## 4. Screening: uninformed side thiết kế menu

Screening là mirror image của signaling. Bên thiếu information đưa ra một menu contracts để các types tự chọn.

Insurance contract có thể cho lựa chọn:

```text
High premium + low deductible
Low premium + high deductible
```

Nếu high-risk và low-risk customers đánh đổi premium với deductible khác nhau, menu có thể induce self-selection.

Design cần thỏa incentive compatibility: mỗi type phải muốn chọn contract dành cho mình hơn contract của type khác.

## 5. Moral hazard: hidden action sau contract

Moral hazard xảy ra khi contract thay đổi incentive sau khi được ký và một action quan trọng khó quan sát hoặc verify.

Insurance giảm marginal cost của risky behavior hoặc care consumption đối với insured person; employment contract có thể làm effort khó monitor; lender không kiểm soát hoàn hảo project risk borrower chọn sau khi nhận vốn.

Logic cơ bản:

```text
Protection / fixed payment increases
→ actor bears smaller share of marginal consequence
→ behavior may become less aligned with principal's objective
```

“Moral” ở đây là thuật ngữ lịch sử; economics không nhất thiết cáo buộc actor vô đạo đức. Đây là incentive response dưới contract.

## 6. Deductible, copay và skin in the game

Insurance có thể giảm moral hazard bằng deductible hoặc copay. Khi insured vẫn chịu một phần marginal cost, họ có incentive cân nhắc consumption/risk kỹ hơn.

Nhưng cost sharing cũng giảm risk protection, là mục tiêu cốt lõi của insurance. Optimal contract cân bằng:

```text
Risk sharing
vs.
Incentive provision
```

Nếu household rất risk-averse nhưng behavior ít responsive, coverage rộng có thể tốt. Nếu behavior responsive mạnh và monitoring yếu, cost sharing có value lớn hơn.

## 7. Principal–agent problem

Principal–agent problem xuất hiện khi principal giao task cho agent nhưng objective không hoàn toàn giống nhau và principal không quan sát đầy đủ action hoặc information của agent.

Examples:

- shareholder và manager;
- employer và employee;
- patient và doctor;
- voter và politician;
- client và contractor;
- lender và borrower.

Contract cố gắng align payoff của agent với objective của principal, nhưng performance measure thường imperfect.

## 8. Pay-for-performance và multitasking distortion

Nếu chỉ reward metric dễ đo, agent có thể tối ưu metric thay vì objective thật. Giáo viên được trả chỉ theo test score có incentive “teach to the test”; salesperson theo revenue có thể discount quá mức; developer theo số ticket có thể chia nhỏ work hoặc bỏ quality.

Đây là multitasking problem. Khi một dimension dễ đo và dimension khác khó đo, strong incentive trên metric đầu có thể làm dimension sau xấu đi.

Vì vậy optimal incentive không phải lúc nào cũng “trả theo performance mạnh hơn”. Đôi khi fixed salary, team incentive, professional norm hoặc subjective evaluation giảm gaming.

## 9. Observable khác verifiable

Một fact có thể observable với các bên nhưng không verifiable bởi court hoặc third party. Hai engineers có thể biết ai effort nhiều hơn, nhưng contract không thể enforce nếu evidence không đủ objective.

Contract theory vì vậy phân biệt:

```text
observable information
vs.
contractible/verifiable information
```

Nhiều incomplete contracts tồn tại không phải vì parties quên viết clause, mà vì future state quá phức tạp hoặc không thể verify với chi phí hợp lý.

## 10. Incomplete contracts và residual control rights

Khi không thể specify mọi future contingency, ownership và control rights trở nên quan trọng. Ai có quyền quyết định trong trạng thái chưa ghi rõ contract?

Incomplete-contract theory phân tích residual rights of control. Ownership có thể khuyến khích investment vì owner giữ nhiều return từ relationship-specific investment, nhưng cũng có thể làm party khác underinvest nếu bargaining power giảm.

Điểm quan trọng là institution design không chỉ là price. Quyền quyết định khi contract im lặng cũng ảnh hưởng incentive.

## 11. Reputation như repeated-game solution

Trong one-shot transaction, seller có thể gain từ quality thấp nếu buyer không kiểm tra được. Trong repeated relationship, reputation làm future profit phụ thuộc current behavior.

Nếu future business có value đủ lớn, seller có incentive duy trì quality.

Online review, rating, certification và brand đều có thể giảm information asymmetry, nhưng chúng tạo layer mới: fake review, selection bias, platform manipulation và strategic reputation management.

## 12. Warranty và guarantee như signal + incentive

Warranty có hai vai trò.

Thứ nhất, seller quality cao có thể offer warranty với expected repair cost thấp hơn low-quality seller, nên warranty trở thành signal.

Thứ hai, warranty chuyển một phần failure cost về seller, tạo incentive cải thiện quality.

Nhưng broad warranty cũng có thể tăng consumer moral hazard nếu user care giảm. Một contract thực tế có thể đồng thời xử lý selection và incentive ở hai phía.

## 13. Certification, licensing và third-party verification

Third-party certification có thể tạo common information standard khi buyer không tự evaluate quality. Food safety inspection, accounting audit, professional credential hoặc software security certification đều dùng logic này.

Nhưng certification có cost và capture risk. Nếu standard quá thấp, nó không reveal quality; nếu quá cao, nó có thể tạo entry barrier không cần thiết.

Vì vậy policy cần hỏi: hidden information cụ thể là gì, verification accuracy bao nhiêu và cost của false positive/false negative ra sao?

## 14. Credit market, collateral và rationing

Lender đối mặt cả adverse selection lẫn moral hazard. Interest rate cao có thể thu hút borrower riskier hoặc làm borrower chọn project riskier vì upside thuộc borrower trong khi downside một phần thuộc lender.

Do đó lender không nhất thiết clear market bằng tăng interest rate đến khi supply bằng demand. Có thể xuất hiện credit rationing: một số borrowers willing to pay rate cao vẫn không được vay.

Collateral giảm lender loss và có thể screen borrower, nhưng collateral requirement cũng tạo distribution effect vì household thiếu wealth bị hạn chế access dù project có productivity tốt.

## 15. Labor market và efficiency wage

Nếu worker effort khó monitor, firm có thể trả wage cao hơn market-clearing level để tăng cost của job loss, giảm turnover hoặc thu hút applicant quality cao hơn.

Efficiency wage models giải thích vì sao unemployment có thể tồn tại ngay cả khi workers willing to work ở wage thấp hơn. Đây là một example cho việc information/incentive friction thay đổi simple supply-demand result.

## 16. Healthcare và delegated expertise

Patient thường thiếu medical knowledge nên doctor vừa cung cấp service vừa tư vấn quantity/quality cần dùng. Đây là agency relationship với asymmetric information.

Fee-for-service có thể khuyến khích quantity; capitation có thể khuyến khích economize quá mức; salary giảm volume incentive nhưng có thể giảm effort ở một số margins.

Không payment system nào giải quyết hoàn toàn mọi incentive. Design thường kết hợp payment, quality metrics, peer review và regulation.

## 17. Information disclosure và limits của transparency

Một response tự nhiên là bắt buộc disclosure. Nhưng disclosure chỉ hiệu quả khi users hiểu, chú ý và có khả năng hành động trên information.

Nếu disclosure dài, technical hoặc quá nhiều, bounded attention làm effect nhỏ. Firms cũng có thể strategically frame information.

Do đó “more information” không tự động “better decision”. Information design cần quan tâm salience, comparability và decision context.

## 18. Bayesian updating và belief

Information problems thường cần reasoning theo probability. Buyer bắt đầu với prior belief về type, quan sát signal rồi update posterior bằng Bayes rule.

```text
Posterior ∝ Likelihood × Prior
```

Signal mạnh khi likelihood khác nhiều giữa types. Nếu cả types tạo signal với xác suất gần giống nhau, posterior ít thay đổi.

Đây là bridge trực tiếp sang probability/statistics và econometrics: information structure là một model về belief formation, còn data giúp estimate likelihood và test predictions.

## 19. Pooling, separating và semi-separating equilibrium

Trong signaling/screening models, equilibrium có thể:

- **pooling**: nhiều types chọn cùng action/contract nên type không được reveal;
- **separating**: types chọn khác nhau và information được reveal;
- **semi-separating**: một số types mix hoặc overlap.

Không nên assume separating outcome chỉ vì có signal. Cost structure và beliefs ngoài equilibrium path quyết định equilibrium tồn tại và được sustain thế nào.

## 20. Policy trade-off: privacy vs information efficiency

More information có thể giảm adverse selection nhưng làm privacy giảm. Health/genetic data giúp insurer price risk chính xác hơn nhưng có thể làm risk sharing yếu đi. Credit data giảm default uncertainty nhưng có thể tạo exclusion hoặc error persistence.

Đây là một conflict giữa allocative information và social objectives khác. Economics có thể map trade-off, nhưng normative choice cần law, ethics và institutional context.

## 21. Failure modes thường gặp

Sai lầm thứ nhất là gọi mọi uncertainty là asymmetric information. Nếu cả hai bên cùng không biết future state, đó là common uncertainty chứ chưa chắc information asymmetry.

Sai lầm thứ hai là nhầm adverse selection với moral hazard. Hãy hỏi hidden information/action xuất hiện trước hay sau contract.

Sai lầm thứ ba là nghĩ incentive pay luôn cải thiện performance. Metric distortion và risk-bearing có thể làm outcome xấu đi.

Sai lầm thứ tư là coi transparency là free solution và bỏ qua attention, comprehension, privacy và gaming.

## 22. Mental model cho information problem

Khi phân tích một market hoặc contract, hãy hỏi:

1. Ai biết điều gì mà bên kia không biết?
2. Information là hidden type, hidden action hay hidden state?
3. Timing: problem xuất hiện trước hay sau contract?
4. Variable đó observable nhưng có verifiable không?
5. Price/contract hiện tại tạo incentive nào?
6. Có signal hoặc menu nào khiến types tự reveal không?
7. Contract đang trade off risk sharing với incentive ra sao?
8. Metric có thể bị gaming hoặc làm lệch multitask effort không?
9. Reputation, certification, collateral hoặc monitoring có giảm friction không?
10. Policy tăng information nhưng có cost về privacy, exclusion hoặc administrative burden không?

Với chapter này, chuỗi microeconomics từ individual choice đến welfare và ba market-failure families đã hoàn chỉnh ở mức nền tảng. Bước kế tiếp là chuyển sang **market structure và game theory**, nơi payoff của một actor phụ thuộc trực tiếp vào action của các actor khác và price-taking assumption không còn đủ.
