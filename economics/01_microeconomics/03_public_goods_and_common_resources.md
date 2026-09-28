# Public Goods & Common Resources — Provision, free-riding và collective action

Public-goods analysis bắt đầu từ hai thuộc tính kỹ thuật của một good hoặc service: **rivalry** và **excludability**. Hai thuộc tính này quyết định liệu market price có thể dễ dàng phân bổ resource hay không, chứ không phải việc good đó do nhà nước hay tư nhân cung cấp.

Thuật ngữ public good (`공공재`) thường bị dùng sai để chỉ “thứ có ích cho công chúng”. Trong economics, một public good thuần túy là good **non-rival** và **non-excludable**. Một private company hoàn toàn có thể cung cấp public good; một government agency cũng có thể cung cấp private good.

## 1. Rivalry và excludability

Một good là **rival** khi consumption của một người làm giảm quantity hoặc quality còn lại cho người khác. Một sandwich là rival: một người ăn thì người khác không thể ăn cùng sandwich đó.

Một good là **non-rival** khi thêm một user có marginal resource cost rất thấp trong một capacity range. Một broadcast signal hoặc một công thức toán học có thể được nhiều người dùng đồng thời mà không bị “tiêu hao” theo cách của sandwich.

Một good là **excludable** khi provider có thể ngăn người không trả tiền sử dụng nó với chi phí hợp lý. Cinema seat là excludable; clean air trên một vùng rộng thường khó excludable.

Từ hai dimensions này xuất hiện bốn archetypes:

```text
Rival + Excludable        → private good
Non-rival + Excludable    → club/toll good
Rival + Non-excludable    → common-pool resource
Non-rival + Non-excludable→ public good
```

Đây là spectrum, không phải taxonomy tuyệt đối. Technology và institutions có thể thay đổi excludability hoặc congestion.

## 2. Vì sao public good tạo free-rider problem

Nếu một public good đã được cung cấp và không thể loại trừ người không trả, một individual có incentive khai thấp willingness to pay và hy vọng người khác finance good.

Đây là free-rider problem (`무임승차 문제`). Nếu nhiều người cùng hành xử như vậy, voluntary contribution có thể thấp hơn social value của good.

Vấn đề không phải consumer “xấu”. Nó là incentive structure: contribution của một cá nhân có private cost nhưng benefit của good được chia cho nhiều người.

## 3. Social demand cho public good khác private good

Với private good, individuals cạnh tranh cùng một unit, nên market demand thường cộng quantities theo chiều ngang tại mỗi price.

Với pure public good, mọi người consume cùng quantity `G`. Social marginal benefit là tổng willingness to pay của mọi người cho **cùng một unit**:

```text
SMB(G) = MB_1(G) + MB_2(G) + ... + MB_n(G)
```

Vì vậy demand được cộng theo chiều dọc.

Efficient provision thỏa Samuelson condition:

```text
Σ MRS_i = MRT
```

Trực giác: tổng marginal willingness to pay của các users phải bằng marginal social cost của việc cung cấp thêm một unit.

## 4. Vì sao pricing theo marginal cost có thể không finance được public good

Với non-rival good, marginal cost của thêm một user có thể gần zero. Nếu price được đặt bằng marginal cost cho mỗi user, revenue có thể không đủ cover fixed cost lớn của việc tạo good ban đầu.

Software, knowledge, digital infrastructure và broadcast content thường có structure:

```text
High fixed cost
Low marginal reproduction cost
```

Đây là reason economic organization có thể dùng subscription, bundling, advertising, donation, intellectual property hoặc tax finance thay vì simple per-unit marginal-cost pricing.

## 5. Public provision không đồng nghĩa public production

Government có thể finance good qua tax nhưng outsource production cho private contractor. Ngược lại, government-owned provider có thể charge user fee và cung cấp excludable service.

Cần tách ba câu hỏi:

```text
Who finances?
Who produces?
Who decides quantity/quality?
```

Ba answers có thể khác nhau. Confusion giữa chúng làm policy discussion trở nên mơ hồ.

## 6. Common-pool resources và tragedy of the commons

Common-pool resource (`공유자원`) là rival nhưng khó exclude. Fisheries, groundwater, grazing land hoặc congested open-access roads là examples điển hình.

Khi mỗi user nhận private benefit từ khai thác thêm nhưng phần depletion cost được chia cho cộng đồng, private extraction vượt social optimum.

Một simplified condition:

```text
Private user sees:
Marginal Private Benefit ≥ Private Extraction Cost

Society sees:
Marginal Social Benefit ≥ Extraction Cost + Marginal Depletion Cost
```

Nếu depletion externality không được internalize, resource có thể bị overuse.

## 7. “Tragedy” không phải kết quả tất yếu

Tragedy of the commons mô tả một incentive problem trong open-access regime, không chứng minh rằng mọi shared resource chắc chắn collapse.

Communities có thể phát triển monitoring, quotas, social norms, graduated sanctions và local governance để quản lý commons. Elinor Ostrom nổi tiếng vì chỉ ra nhiều institutional arrangements nằm giữa pure privatization và centralized state control.

Điểm reasoning quan trọng là không hỏi “public hay private?” trước, mà hỏi:

```text
Boundary của resource là gì?
Ai có quyền access?
Ai monitor?
Rule có phù hợp local information không?
Sanction có enforceable không?
```

## 8. Club goods và congestion

Club good là non-rival trong một capacity range nhưng excludable. Streaming subscription, private park hoặc software service có thể gần dạng này.

Khi số users tăng, congestion hoặc server capacity có thể làm good trở nên rival tại margin. Vì vậy rivalry phụ thuộc scale.

Efficient pricing có thể cần hai phần:

```text
membership/access fee → cover fixed cost
usage/congestion price → reflect marginal capacity cost
```

## 9. Information goods, copyright và dynamic incentive

Knowledge và digital content có marginal reproduction cost rất thấp. Static efficiency gợi ý price gần zero để maximize access. Nhưng nếu creator không recover fixed development cost, incentive tạo content mới có thể giảm.

Intellectual property tạo temporary excludability để hỗ trợ innovation incentive, nhưng đồng thời hạn chế diffusion.

Đây là trade-off giữa:

```text
static allocative efficiency
vs.
dynamic innovation incentive
```

Không có một optimal copyright length hoặc patent scope suy ra trực tiếp chỉ từ “non-rival”. Cần evidence về R&D cost, substitution, spillovers và follow-on innovation.

## 10. Collective action và group size

Free-riding thường nghiêm trọng hơn khi group lớn, contribution khó quan sát và individual impact nhỏ. Nhưng group size không phải yếu tố duy nhất.

Repeated interaction, identity, selective incentives, social norms và punishment có thể duy trì cooperation.

Public-goods problem vì vậy nối trực tiếp sang game theory: một-shot incentive có thể dẫn tới under-contribution, trong khi repeated game hoặc mechanism design thay đổi equilibrium.

## 11. Tax finance và benefit principle

Một government có thể finance public good bằng broad tax. Nhưng tax itself gây incidence và distortion.

Benefit principle nói người hưởng lợi nên trả tương ứng benefit; ability-to-pay principle nói contribution nên phản ánh khả năng tài chính. Hai principles khác nhau về normative foundation.

Nếu beneficiary khó đo hoặc good tạo broad spillover, benefit pricing có thể infeasible. Nếu tax base distort behavior, broad financing cũng có cost.

## 12. Voting và public choice

Khi quantity public good được quyết định bằng politics, preference aggregation trở thành vấn đề riêng. Majority voting có thể chọn một level gần preference của median voter trong một số điều kiện single-peaked, nhưng result không generalize cho mọi multidimensional choice.

Political process cũng có information problem, concentrated interest và agenda-setting. Vì vậy “market failure” có thể chuyển thành “collective-choice problem”, không biến mất chỉ vì decision được public sector đảm nhận.

## 13. Mechanism design cho truthful revelation

Provider muốn biết willingness to pay, nhưng consumer có incentive understate để giảm contribution.

Mechanism design hỏi: có thể thiết kế rule khiến truthful revelation trở thành incentive-compatible hay không?

Vickrey–Clarke–Groves (VCG) mechanisms cho thấy trong một số settings có thể align private report với social choice, nhưng mechanism có practical limits về budget balance, complexity và strategic environment.

Điểm cốt lõi không phải nhớ tên mechanism mà hiểu problem:

```text
Efficient provision requires preference information
but agents may not want to reveal preferences truthfully
```

## 14. Public good khác merit good

Merit good là normative concept: society cho rằng người dân nên consume nhiều hơn mức họ tự chọn, ví dụ vì externality, paternalism hoặc distribution objective.

Public good là technical classification theo rivalry/excludability.

Education có thể có positive externality và merit-good argument nhưng classroom seat vẫn rival ở capacity margin và có thể excludable. Vì vậy không nên gọi toàn bộ education là pure public good.

## 15. Case reasoning: national defense, lighthouse, software

National defense thường gần public good vì protection trên territory non-rival trong broad range và khó exclude một resident riêng lẻ.

Lighthouse historically thường được dùng làm textbook example, nhưng real institutional history cho thấy lighthouse services có lúc được finance qua port dues hoặc bundled với excludable harbor services. Case này hữu ích để nhớ rằng excludability là institutional/technological, không chỉ “tự nhiên”.

Open-source software có thể non-rival và widely accessible, nhưng maintenance vẫn cần labor. Funding có thể đến từ sponsorship, dual licensing, enterprise service hoặc firms có complementary business model.

## 16. Failure modes thường gặp

Sai lầm thứ nhất là gọi mọi government service là public good.

Sai lầm thứ hai là coi non-rival nghĩa marginal cost luôn zero; server, congestion, support và security có thể làm marginal cost tăng.

Sai lầm thứ ba là nghĩ commons bắt buộc phải privatize hoặc nationalize. Institutional design có nhiều forms.

Sai lầm thứ tư là đánh giá digital goods chỉ bằng static access và bỏ qua dynamic creation incentive.

## 17. Mental model khi phân tích public-good problem

Khi gặp một resource hoặc service, hãy đi theo sequence:

1. Consumption có rival không? Ở capacity nào bắt đầu congestion?
2. Exclusion có technically và legally khả thi không? Cost bao nhiêu?
3. Fixed cost và marginal cost có structure thế nào?
4. Nếu non-excludable, free-rider incentive xuất hiện ở đâu?
5. Nếu rival nhưng open access, depletion/congestion externality nằm ở đâu?
6. Finance, production và governance có cần cùng một actor không?
7. Institution nào tận dụng local information và enforce rule tốt nhất?
8. Policy thay đổi static efficiency, distribution và dynamic incentive như thế nào?

Public goods cho thấy market có thể thiếu cơ chế reveal willingness to pay hoặc finance provision. Chapter tiếp theo đi vào một failure mode khác: ngay cả khi good excludable và rival bình thường, **information asymmetry (정보 비대칭)** vẫn có thể làm transaction thất bại hoặc contract méo mó.
