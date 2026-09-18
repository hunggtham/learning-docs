# Ngôn ngữ, kính ngữ và những khái niệm quan hệ khó dịch

## Tiếng Hàn mã hoá quan hệ vào câu nói

Một trong những con đường nhanh nhất để hiểu văn hoá Hàn Quốc là quan sát cách tiếng Hàn bắt người nói lựa chọn quan hệ. Trong tiếng Anh, câu “Eat” có thể thêm “please” để lịch sự. Trong tiếng Hàn, động từ, đuôi câu, từ vựng và danh xưng có thể đổi theo quan hệ giữa người nói, người nghe và chủ thể.

**Kính ngữ (Honorifics / 높임말·존댓말)** không chỉ là “nói lịch sự”. Nó là hệ thống encode social relation vào grammar. `먹다` là “ăn”; `드시다` là từ kính ngữ cho hành động ăn của người cần được nâng; `먹어요`, `먹습니다`, `먹어` tạo các mức register khác nhau. Vì vậy người học không thể chọn một câu chỉ bằng semantic content; họ phải chọn cả social configuration.

## 존댓말, 반말 và speech levels

`존댓말` thường được hiểu là polite/honorific speech, còn `반말` là non-honorific/intimate speech. Tuy nhiên cặp này không hoàn toàn tương ứng với “formal vs informal”. Có ngôn ngữ thân mật vẫn lịch sự, và ngôn ngữ formal không nhất thiết thể hiện intimacy.

Việc chuyển từ 존댓말 sang 반말 thường mang ý nghĩa quan hệ: “chúng ta đã đủ gần để giảm social distance chưa?” Vì vậy câu `말 놓을까요?` — “chúng ta nói thoải mái hơn nhé?” — thực chất là một negotiation về relationship protocol.

Trong UI/UX, register cũng là vấn đề design. Một chatbot ngân hàng dùng 반말 có thể bị cảm nhận là xâm phạm khoảng cách; game character dùng 반말 có thể tạo personality thân thiện hoặc ngạo mạn. Localization vì vậy không thể chỉ dịch text literal; nó phải map relationship.

## 호칭: tên gọi là một phần của quan hệ

**Danh xưng (Forms of Address / 호칭)** như `선생님`, `팀장님`, `사장님`, `형`, `누나`, `언니`, `오빠` không chỉ “gọi người”. Chúng định nghĩa relationship model. Nhiều từ thân tộc được mở rộng sang quan hệ phi huyết thống, cho thấy logic gia đình được dùng làm metaphor xã hội.

Suffix `-님` có chức năng tôn kính. Trong công ty, một người có thể được gọi bằng chức vụ cộng `님`, ví dụ `팀장님`. Một số doanh nghiệp cố giảm hierarchy bằng cách gọi tên + `님` hoặc tên tiếng Anh. Nhưng như đã thấy ở chương trước, đổi address scheme không tự động đổi authority graph.

## 눈치: inference từ tín hiệu yếu

**눈치 (social perception / 눈치)** rất khó dịch bằng một từ. Nó là năng lực đọc bối cảnh, cảm xúc, quan hệ và expectation từ những tín hiệu không được nói trực tiếp. “Có 눈치” không chỉ là tinh ý; nó là khả năng inference trong môi trường mà nhiều thông tin xã hội được implicit.

Ta có thể liên hệ với Bayesian reasoning. Người quan sát có prior — hiểu biết trước về quan hệ và bối cảnh — rồi cập nhật khi thấy evidence: giọng nói ngắn hơn, silence kéo dài, ai đó không gắp đồ ăn, quản lý nhắc deadline gián tiếp. Trực giác có dạng:

```math
P(\text{meaning}\mid \text{signals, context})
\propto
P(\text{signals}\mid \text{meaning})P(\text{meaning})
```

Không ai thực sự tính xác suất, nhưng mental model này cho thấy 눈치 không phải “đọc suy nghĩ”; nó là inference dưới uncertainty.

Mặt tích cực của 눈치 là coordination tinh tế và sensitivity. Mặt tiêu cực xuất hiện khi tổ chức dựa quá nhiều vào implicit expectation: nhân viên phải đoán yêu cầu thay vì nhận specification rõ ràng. Trong Software Engineering, đây giống API undocumented: người lâu năm biết hidden contract, người mới dễ fail.

## 정: quan hệ tích luỹ theo thời gian

**정 (affective bond / 정)** cũng không có một bản dịch hoàn hảo. Nó chỉ cảm giác gắn bó, lưu luyến và trách nhiệm tình cảm hình thành qua thời gian chia sẻ. 정 không nhất thiết chỉ có trong quan hệ “thích nhau”. Hai người hay cãi nhau vẫn có thể nói đã có 정 sau nhiều năm.

Có thể hình dung 정 như state được tích luỹ qua repeated interactions. Một transaction đơn lẻ không tạo 정 mạnh. Những bữa ăn, giúp đỡ nhỏ, sống cùng khu phố, làm chung dự án và vượt qua khó khăn tạo history. Trong database terms, relationship không phải current row mà là event log.

Nhưng cần tránh romanticize. 정 có thể làm quan hệ ấm hơn, đồng thời khiến boundary khó thiết lập: “vì đã có tình nghĩa nên khó từ chối”.

## 체면: khuôn mặt xã hội

**Thể diện (Face / 체면)** là hình ảnh xã hội mà cá nhân muốn duy trì trước người khác. Khái niệm face không chỉ có ở Hàn Quốc; sociolinguistics và anthropology dùng nó rộng rãi. Trong môi trường coi trọng harmony, việc sửa sai công khai có thể gây chi phí face lớn hơn sửa riêng.

Vì vậy, một câu feedback rất thẳng trước cả team có thể truyền information chính xác nhưng gây social loss không cần thiết. Người giao tiếp giỏi tối ưu hai mục tiêu cùng lúc: **information accuracy** và **relationship preservation**.

Đây là multi-objective optimization. Không có một scalar đơn giản. Nếu quá tối ưu “giữ mặt”, vấn đề không được nói. Nếu chỉ tối ưu “nói thật ngay”, trust có thể giảm. Kỹ năng là chọn channel, timing và wording sao cho cả hai objective đủ tốt.

## 한: từ lịch sử đến cảm xúc tập thể

**한 (Han / 한)** thường được mô tả bằng những từ như nỗi uất, đau, tiếc, khát vọng chưa giải toả. Đây là một khái niệm được dùng nhiều trong văn học và diễn giải về lịch sử Hàn Quốc, nhưng không nên xem nó là “gene cảm xúc của người Hàn”. Ý nghĩa của 한 đã được kiến tạo và tranh luận qua nghệ thuật, lịch sử thuộc địa, chia cắt, chiến tranh và nationalism.

Một cách an toàn là dùng 한 khi phân tích một tác phẩm hoặc discourse cụ thể, thay vì gán nó cho toàn bộ dân tộc.

## 고생, 수고 và giá trị của nỗ lực

`고생` liên quan đến hardship, vất vả; `수고` liên quan đến effort/công lao. Các câu `고생했어요`, `수고하셨습니다` rất phổ biến vì chúng recognize effort chứ không chỉ outcome. Trong môi trường công việc, lời này đánh dấu rằng quá trình tiêu tốn sức lực được nhìn thấy.

Nó kết nối với lịch sử phát triển nhanh nhưng không nên suy ra rằng suffering luôn được ca ngợi. Thế hệ trẻ cũng phê phán văn hoá overwork và “chịu khổ mới trưởng thành”.

## High-context communication

Hàn Quốc thường được mô tả là **high-context culture / 고맥락 문화**, nghĩa là một phần meaning dựa nhiều vào bối cảnh chung, quan hệ và implicit cues. Đây là continuum chứ không phải nhãn cố định. Trong technical incident, người Hàn vẫn cần log và specification explicit; trong tình huống nhạy cảm giữa người quen, implication có thể quan trọng hơn.

Đối với người làm IT, bài học thực dụng là phân biệt **social context** với **technical requirement**. Đừng dùng 눈치 để thay acceptance criteria. Một team cross-cultural tốt nên explicit hoá deadline, owner và definition of done, đồng thời giữ politeness trong delivery.

## Mental Model

> Tiếng Hàn không chỉ truyền “nội dung”; nó truyền luôn một phần cấu trúc quan hệ. 눈치 là bộ giải mã context; 정 là history tích luỹ trong quan hệ; 체면 là constraint về cách xử lý thông tin nhạy cảm. Ba khái niệm này cùng giải thích vì sao cùng một câu đúng về mặt logic có thể vẫn sai về mặt xã hội.

## Common Misconceptions

`눈치` không đồng nghĩa với sợ hãi hay phục tùng. Một người có 눈치 tốt có thể nhận ra chính xác lúc cần phản biện.

`정` không phải “người Hàn tốt bụng”. Nó mô tả bond quan hệ, có cả lợi ích và cost.

`반말` không tự động là bất lịch sự. Giữa bạn thân hoặc khi đã thống nhất relationship, nó là register tự nhiên.

“Người Hàn không nói thẳng” cũng quá đơn giản. Mức trực tiếp thay đổi mạnh theo thế hệ, vùng, công ty, domain và mức độ rủi ro của vấn đề.
