# Công sở Hàn Quốc: tổ chức, chức danh, báo cáo và quan hệ

## Công ty là nơi các lớp văn hoá va vào nhau

Workplace Hàn Quốc hiện đại là một laboratory đặc biệt: hierarchy Nho giáo, quản trị kiểu công nghiệp, luật lao động, multinational practice, agile software development và expectation của thế hệ trẻ cùng tồn tại. Vì vậy không có một “văn hoá công ty Hàn” duy nhất. Chaebol, startup, ngân hàng, game studio, công ty SI/SM và cơ quan nhà nước có architecture tổ chức rất khác.

Tuy vậy, một số khái niệm giúp đọc system.

## 직급, 직책, 연차: ba trục dễ nhầm

**Rank / 직급** là cấp bậc nhân sự; các tên truyền thống có thể gồm `사원`, `대리`, `과장`, `차장`, `부장`. Nhiều công ty đã thay đổi hoặc giản lược.

**Position/role / 직책** là vai trò quản lý như `팀장`, `파트장`, `본부장`. Một người có 직급 nhất định nhưng đảm nhiệm hoặc không đảm nhiệm 직책.

**Years of experience/tenure / 연차** có thể chỉ số năm đi làm hoặc năm trong tổ chức. Trong daily speech, `몇 년 차예요?` giúp định vị seniority nghề nghiệp.

Nếu coi organization như access-control system, `직급` giống grade, `직책` giống assigned role, còn `연차` giống historical metadata. Permission thực thường là function của cả ba.

Ngoài ra còn có **업무분장 (division of duties / phân công công việc)**. Đây là layer quan trọng vì một người có title cao chưa chắc là owner của task cụ thể. Trong project, câu hỏi `이 건 담당자가 누구예요?` thường quan trọng hơn việc nhìn chức vụ.

## 담당자, owner và khái niệm trách nhiệm

`담당자` là người phụ trách trực tiếp một việc. Trong team Hàn, nhiều communication xoay quanh việc xác định ai đang `담당` issue nào. Đây là cách biến organization chart thành operational ownership.

Một task tốt thường có bốn thuộc tính:

```text
담당자: ai chịu trách nhiệm xử lý
기한: khi nào cần xong
산출물: output cụ thể là gì
공유대상: ai cần được thông báo
```

Nếu thiếu một trong bốn, communication dễ trở thành “mọi người đều biết nhưng không ai thực sự sở hữu”.

`책임소재` nghĩa là locus of responsibility, thường xuất hiện khi có issue và organization cần biết ai chịu trách nhiệm ở layer nào. Khái niệm này có mặt tích cực là accountability, nhưng nếu bị lạm dụng thành blame-hunting thì team sẽ giấu lỗi thay vì report sớm.

## 보고: báo cáo như một protocol quản trị

**Reporting / 보고** có vai trò lớn trong nhiều tổ chức Hàn. Người nước ngoài đôi khi cảm thấy phải “báo cáo quá nhiều”, nhưng từ góc nhìn manager, report giảm uncertainty và tạo traceability.

Một report tốt trả lời: status hiện tại là gì, risk ở đâu, decision cần ai, next step là gì. Vấn đề nảy sinh khi report trở thành ritual phục vụ hierarchy thay vì information flow. Khi cùng dữ liệu phải format lại nhiều lần chỉ vì chain of command, coordination cost tăng.

Trong software team, có thể phân biệt **information pull** và **information push**. Dashboard cho phép manager pull status; daily report bắt engineer push. Nếu system observability tốt, nhu cầu status report thủ công có thể giảm.

## 보고 타이밍: báo sớm hay tự xử lý trước?

Một khác biệt văn hoá–tổ chức dễ gây conflict là **khi nào phải báo**. Một engineer có thể nghĩ “tôi xử lý xong rồi báo sẽ tốt hơn”; manager có thể nghĩ “issue ảnh hưởng release mà không báo ngay là risk”. Vì vậy report timing là một part của protocol.

Trong incident hoặc UAT, pattern hữu ích là:

```text
1. 발견: phát hiện issue
2. 영향도: ảnh hưởng tới đâu
3. 임시조치: đã làm gì tạm thời
4. 원인: đã biết root cause chưa
5. 다음 액션: ai làm gì tiếp
```

`선보고 후조치` — báo trước rồi xử lý — có thể phù hợp khi impact lớn hoặc cần approval. Nhưng technical emergency đôi khi phải `선조치 후보고` nếu delay gây thiệt hại. Điều quan trọng là team phải biết rule, không để engineer đoán bằng 눈치.

## 결재, 승인 và 합의

**Approval / 결재** là quy trình xin phê duyệt, thường qua hệ thống điện tử `전자결재`. Nó giúp compliance, budget control và accountability. Nhưng chain quá dài tăng decision latency.

`승인` cũng là approval, nhưng sắc thái có thể rộng hơn và không nhất thiết là formal document routing như `결재`. `합의` trong workflow có thể chỉ việc stakeholder liên quan đồng thuận trước khi final approver ký.

Một approval chain có thể trông như:

```text
작성자 → 검토자 → 합의자 → 결재권자
```

Nếu người học chỉ dịch tất cả thành “approve” sẽ bỏ mất architecture của process.

Little’s Law trong queueing theory nói rằng lượng work-in-progress liên quan arrival rate và time trong system. Dù không cần áp công thức máy móc, logic này hữu ích: nếu mọi request phải qua nhiều reviewer bận, queue sẽ tăng. “Văn hoá chậm” đôi khi không phải attitude mà là architecture của approval.

## 회의: cuộc họp và quyền nói

Trong team hierarchy mạnh, người junior có thể ít phản biện công khai hơn, đặc biệt khi chưa có trust. Điều này tạo **information loss**: người gần problem nhất biết bug nhưng signal bị attenuate trên đường lên management.

Các organization hiệu quả cố tạo psychological safety — **an toàn tâm lý / 심리적 안전감** — để disagreement về task không bị hiểu là disrespect cá nhân. Đây là nơi cultural literacy quan trọng: có thể giữ kính ngữ nhưng vẫn challenge assumption bằng evidence.

Ví dụ thay vì trực tiếp `그건 틀렸습니다` trong tình huống nhạy cảm, người nói có thể frame: `제가 확인한 로그에서는 다른 결과가 보여서요. 이 부분을 다시 확인해 보면 좋을 것 같습니다.` Nội dung kỹ thuật không yếu đi; delivery giảm face threat.

## 회의록, 정리 và “ai hiểu gì sau meeting?”

**Meeting minutes / 회의록** và từ `정리` rất quan trọng. Sau meeting, nhiều team dùng message kiểu:

```text
오늘 회의 내용 정리드립니다.
1. A 기능: 베트남팀 확인
2. B 이슈: 한국팀 수정
3. 재테스트: 금요일 오전
```

`정리하다` ở đây không chỉ là “sắp xếp”; nó là biến discussion thành shared state. Một meeting không có written summary dễ tạo nhiều version of truth.

Trong distributed systems, consensus đắt. Trong team người, meeting minutes là một low-cost consensus artifact.

## 공유: “share” không chỉ là gửi file

`공유드립니다`, `내용 공유 부탁드립니다`, `관련자에게 공유해 주세요` xuất hiện rất nhiều trong corporate Korean. `공유` có thể nghĩa gửi information để mọi stakeholder giữ cùng context.

Nhưng share quá rộng tạo notification overload. Good communication cần phân biệt:

- người phải action;
- người chỉ cần biết;
- người cần approve;
- người không cần nhận message.

Email CC, messenger mention và project tool đều là routing layer. Culture “share nhiều cho an toàn” có thể giảm blame risk nhưng tăng cognitive load.

## 인수인계: handover như chuyển state giữa người

**Handover / 인수인계** là quá trình chuyển công việc khi đổi owner, nghỉ phép, chuyển team hoặc nghỉ việc. Một handover tốt không chỉ có danh sách task; nó phải truyền cả hidden state:

```text
현재 상태
미해결 이슈
주요 연락처
정기 일정
접근 권한
주의사항
과거 의사결정 이유
```

Nếu chỉ truyền file mà không truyền reason behind decision, người mới nhận task có code nhưng mất context. Đây là organizational knowledge-loss problem.

## 회식: ăn uống như hạ tầng quan hệ

**Company dinner / 회식** historically là nơi đồng nghiệp tạo bond ngoài formal office. Vì high-context work dựa nhiều vào trust, shared meal giúp tăng bandwidth của quan hệ. Trong một số tổ chức, information và mentorship từng diễn ra ở đây.

Nhưng 회식 cũng có cost: thời gian cá nhân, alcohol pressure, exclusion của người chăm con hoặc không uống. Vì vậy norm đang thay đổi: lunch gathering, voluntary attendance, earlier end time và non-alcoholic format phổ biến hơn ở nhiều nơi.

Điều cần tránh là đồng nhất “회식 = ép uống”. Có môi trường như vậy, nhưng không phải definition của 회식.

## 술자리 etiquette và quyền từ chối

Tập quán truyền thống thường gồm rót rượu cho người khác bằng hai tay, người trẻ quay mặt khi uống trước người lớn tuổi, không tự đổ đầy ly trong một số context. Những ritual này encode respect.

Tuy nhiên, workplace hiện đại chịu luật, compliance và thay đổi norm. Việc ép uống không nên được hợp thức hoá bằng “văn hoá Hàn”. Cultural knowledge dùng để hiểu signal, không phải để xoá boundary cá nhân.

## 야근, 연차 và availability culture

**Overtime / 야근** từng gắn với giai đoạn growth-oriented management và competition cao. Có nơi “ngồi lại lâu” trở thành signal của commitment ngay cả khi productivity không tăng. Đây là classic proxy failure: presence được dùng thay cho output vì output khó đo.

Trong knowledge work, productivity không tuyến tính với time. Sau fatigue threshold, error rate tăng. Với programming, một giờ debug lúc tỉnh táo có thể giá trị hơn ba giờ code lúc kiệt sức.

`연차` còn có nghĩa **ngày nghỉ phép năm** ngoài nghĩa số năm kinh nghiệm, nên context rất quan trọng. `연차를 쓰다` nghĩa dùng ngày phép. Ở team tốt, leave là resource được plan; ở team thiếu người, employee có thể cảm thấy phải nhìn workload của đồng đội trước khi nghỉ.

Đây là một ví dụ của informal constraint: quyền pháp lý có thể tồn tại, nhưng social cost perceived vẫn ảnh hưởng behavior.

## 정규직, 계약직, 파견, 협력사: employment status ảnh hưởng experience

Không phải mọi người trong cùng office có cùng organizational position. Có thể có:

- `정규직`: nhân viên regular;
- `계약직`: contract employee;
- `파견`: dispatched worker;
- `협력사`: nhân sự của vendor/partner company;
- `프리랜서`: freelancer.

Hai người ngồi cạnh nhau có thể làm cùng project nhưng quyền access, benefit, evaluation và job security khác nhau. Vì vậy “văn hoá công ty” phải đọc cùng employment structure.

Trong IT/SI project, relationship `원청–협력사` hoặc client–vendor có thể tạo power asymmetry. Đây là nơi `갑–을` vocabulary xuất hiện, nhưng không nên mặc định mọi hợp tác đều abuse. Mấu chốt là ai kiểm soát budget, acceptance và renewal.

## SI, SM và project culture trong IT Hàn Quốc

Trong IT Hàn, `SI (System Integration)` thường chỉ project xây hệ thống mới, còn `SM (System Management/Maintenance)` liên quan vận hành, bảo trì và cải tiến hệ thống hiện có. Culture công việc khác nhau:

SI thường xoay quanh milestone, requirement, UAT, release và deadline project. SM nhấn mạnh incident, change request, operation continuity và long-term knowledge.

Các từ hay gặp:

- `요구사항`: requirement;
- `개발`: development;
- `테스트`: test;
- `검수`: acceptance/inspection;
- `오픈`: go-live;
- `장애`: incident/outage;
- `유지보수`: maintenance;
- `상주`: làm onsite dài hạn tại client.

Culture high-context dễ làm requirement nằm trong conversation thay vì ticket. Vì vậy project đa quốc gia cần biến oral agreement thành artifact rõ ràng.

## 메신저 và email: 확인, 회신, 전달

Corporate Korean có nhiều phrase tưởng giống nhau nhưng chức năng khác:

- `확인 부탁드립니다`: xin kiểm tra/xác nhận;
- `회신 부탁드립니다`: xin phản hồi;
- `전달드립니다`: chuyển thông tin/tài liệu;
- `공유드립니다`: chia sẻ để cùng nắm;
- `참고 부탁드립니다`: xin tham khảo;
- `검토 부탁드립니다`: xin review về nội dung/chất lượng.

Một response chỉ `네` có thể acknowledge nhưng chưa hoàn tất action. Vì vậy với task quan trọng, nên explicit output: `확인 후 3시까지 회신드리겠습니다.`

## 꼰대: phê phán authority lỗi thời

**Kkondae / 꼰대** là từ phổ biến để chỉ người áp đặt kinh nghiệm, tuổi hoặc địa vị theo cách giáo điều lên người khác. Từ này quan trọng vì nó là evidence rằng hierarchy đang được internal critique.

Một “꼰대” không chỉ là người lớn tuổi. Một người trẻ cũng có thể bị gọi như vậy nếu mindset là “tôi đã trải qua nên anh phải chịu giống tôi”. Core problem là dùng seniority làm substitute cho reasoning.

## MZ세대 và giới hạn của label thế hệ

`MZ세대` ghép Millennials và Generation Z, từng rất phổ biến trong media và corporate discourse. Nhưng hai cohort này trải qua technology và labour market khác nhau, nên label quá rộng dễ mất explanatory power.

Thay vì nói “MZ không thích hierarchy”, nên hỏi cụ thể: họ kỳ vọng transparency về evaluation không? muốn work-life boundary? thích title phẳng? phản ứng thế nào với unpaid social obligation? Những variable này đo được hơn.

## Knowledge Connection: organization như information network

Một công ty tồn tại để coordinate information và action. Hierarchy là routing topology. Nếu mọi message phải đi qua manager, topology giống tree. Tree dễ control nhưng dễ bottleneck. Cross-functional squad thêm lateral edges giúp information đi nhanh hơn nhưng cần rule rõ để tránh conflict.

Văn hoá công sở vì vậy có thể phân tích như network design: authority, information, incentive và trust là các channel khác nhau.

## Mental Model

> Đừng hỏi “công ty Hàn có hierarchy không?” Hãy hỏi hierarchy nằm ở layer nào: title, salary, approval, speaking order, evaluation, contract status hay knowledge. Một công ty có thể phẳng ở cách xưng hô nhưng vẫn tập trung quyền budget; hoặc có title truyền thống nhưng technical decision lại rất evidence-driven.

## Common Misconceptions

“Mọi công ty Hàn đều bắt buộc 회식” sai.

“Cấp dưới không được phản biện” là overgeneralization; cách phản biện và mức psychological safety mới là biến quan trọng.

“Ở lại muộn nghĩa là chăm chỉ” là một cultural signal từng tồn tại ở nhiều nơi nhưng không phải thước đo productivity đáng tin.

“`네` nghĩa là task đã hoàn tất” sai; nhiều khi chỉ là acknowledgement.

“Cùng ngồi một văn phòng nghĩa là cùng status” cũng sai; contract type và vendor relationship có thể tạo khác biệt lớn.
