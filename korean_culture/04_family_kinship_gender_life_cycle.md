# Gia đình, họ tộc, giới và vòng đời

## Gia đình như một thiết chế chứ không chỉ là quan hệ tình cảm

Trong xã hội hiện đại, “gia đình” thường được hình dung trước hết là nơi của tình cảm riêng tư. Nhưng về mặt lịch sử, **gia đình (Family / 가족)** còn là một thiết chế phân phối tài sản, lao động, chăm sóc, giáo dục, danh dự và nghĩa vụ nghi lễ. Muốn hiểu gia đình Hàn Quốc, cần nhìn đồng thời hai lớp: logic gia tộc–Nho giáo của quá khứ và household nhỏ, đô thị, cá nhân hoá của hiện tại.

Trong Joseon, mô hình phụ hệ ngày càng mạnh, đặc biệt trong tầng lớp yangban. **Gia tộc phụ hệ (Patrilineal Kinship / 부계 혈연)** coi dòng họ theo nam giới là trục kế thừa tên họ, gia phả và nghi lễ tổ tiên. Tuy nhiên, không nên chiếu mô hình cuối Joseon ngược lên toàn bộ lịch sử. Ở những giai đoạn trước, quan hệ với gia đình bên mẹ và quyền thừa kế của nữ giới từng có vị trí đáng kể hơn.

Điểm quan trọng của **phụ thuộc đường đi lịch sử (Path Dependence / 경로 의존성)** là một thiết chế có thể mất cơ sở pháp lý nhưng vẫn để lại expectation. Luật, housing, employment và gender norm đã thay đổi sâu, nhưng ký ức về vai trò con trưởng, con dâu, “nhà chồng” hoặc người chủ trì nghi lễ vẫn có thể xuất hiện trong một số gia đình, đặc biệt ở các dịp lễ và tang.

## 가족, 가구, 세대: ba từ gần nhau nhưng không giống nhau

Trong tiếng Hàn, `가족` là **family**, nhấn mạnh quan hệ thân thuộc; `가구` là **household**, nhấn mạnh đơn vị cùng cư trú hoặc đơn vị thống kê; `세대` vừa có thể chỉ **generation** vừa xuất hiện trong nghĩa hộ/căn hộ tuỳ ngữ cảnh. Đây là khác biệt quan trọng khi đọc số liệu dân số.

Một người sống một mình có thể tạo `1인 가구`, nhưng không có nghĩa người đó “không có 가족”. Ngược lại, một `가족` có thể trải rộng qua nhiều household và nhiều thành phố. Khi xã hội chuyển từ co-residence sang networked family, contact qua KakaoTalk, chuyển tiền, chăm sóc định kỳ và về quê ngày lễ thay thế một phần việc sống chung.

Mental model:

```text
family network ≠ household address
```

Gia đình hiện đại ngày càng giống một network có các node sống tách biệt nhưng vẫn chia sẻ resource, care và obligation.

## Họ, 본관, 족보 và ý nghĩa của descent

Phần lớn họ Hàn Quốc ngắn, như `김`, `이`, `박`. Nhưng cùng họ không nhất thiết là cùng một dòng họ gần. **Bản quán (Ancestral Clan Origin / 본관)** chỉ địa phương hoặc nguồn gốc lịch sử của một dòng họ, ví dụ `김해 김씨`.

Đây là một ví dụ hay về identifier. Nếu chỉ dùng surname làm key, collision rất lớn. `본관` hoạt động gần như namespace hoặc composite key. Dĩ nhiên quan hệ huyết thống thực không thể suy ra đơn giản từ chuỗi tên, nhưng cấu trúc khái niệm giúp hiểu vì sao tên họ Hàn Quốc historically cần thêm metadata.

**Gia phả (Genealogy / 족보)** là record của dòng họ. Nó từng có chức năng xác định descent, marriage relation, status và memory. Từ góc nhìn information system, `족보` là một distributed database rất cũ: dữ liệu được copy, bổ sung và truyền qua thế hệ. Nhưng cũng như database lịch sử khác, record phản ánh người nào được system xem là đáng ghi; việc phụ nữ historically được biểu diễn như thế nào cũng phản ánh social structure của thời đại.

## 친가, 외가, 시가, 처가: family network có nhiều hướng

Một người có thể thuộc nhiều relational network cùng lúc. Một số từ quan trọng:

- `친가`: phía gia đình cha trong cách dùng truyền thống.
- `외가`: phía gia đình mẹ.
- `시가`: nhà chồng, nhìn từ người vợ.
- `처가`: nhà vợ, nhìn từ người chồng.
- `친정`: nhà cha mẹ ruột của người phụ nữ sau khi kết hôn trong cách dùng truyền thống.

Những từ này cho thấy ngôn ngữ từng encode mạnh **orientation sau hôn nhân**. Tuy nhiên cách sống hiện đại ngày càng negotiated: khoảng cách tới nơi làm việc, childcare support, housing cost và quan hệ thực tế có thể quan trọng hơn mô hình “vợ theo nhà chồng”.

## 촌수: biến kinship thành cấu trúc có thể tính

**Độ thân tộc (Degree of Kinship / 촌수)** là cách biểu diễn mức quan hệ họ hàng. Nó hữu ích vì family network lớn cần một convention để xác định “xa/gần” không chỉ dựa vào cảm giác.

Cách hiểu trực giác là đếm số bước quan hệ giữa hai người qua ancestor/descendant edges. Parent–child là một bước; siblings đi từ một người lên cha/mẹ rồi xuống người kia, tạo hai bước. Trong graph theory, `촌수` gần với path length trong kinship graph.

Điểm quan trọng không phải thuộc lòng mọi họ hàng xa, mà hiểu vì sao Korean kinship vocabulary có độ phân giải cao: social obligation, inheritance, ritual và marriage historically phụ thuộc vào vị trí trong graph.

## 호칭 trong gia đình: relation quan trọng hơn tên riêng

Trong nhiều gia đình Hàn, gọi nhau bằng relation term như `어머니`, `아버지`, `형`, `누나`, `언니`, `오빠`, `삼촌`, `이모`, `고모` có thể tự nhiên hơn gọi tên. Sau hôn nhân, hệ thống xưng hô tiếp tục mở rộng với `시어머니`, `시아버지`, `장모님`, `장인어른` và nhiều term chi tiết khác.

Điều này cho thấy một principle xuyên suốt Korean culture: **role có thể được lexicalize**. Khi gọi ai đó bằng role, ta không chỉ identify người đó mà còn kích hoạt expectation của relationship.

Đọc sâu về cơ chế này tại [`03_language_honorifics_nunchi_jeong_face.md`](03_language_honorifics_nunchi_jeong_face.md).

## 제사: khi gia đình nối với người đã mất

**Nghi lễ tổ tiên (Ancestral Rite / 제사)** là một trong những nơi Nho giáo đi vào domestic life. Tùy gia đình, `제사` có thể chỉ nghi lễ ngày giỗ hoặc rộng hơn là các nghi thức tưởng nhớ tổ tiên. Bàn lễ, thứ tự hành lễ và vai trò người tham gia từng được chuẩn hoá mạnh theo lý tưởng Nho giáo.

Nhưng giá trị cốt lõi không chỉ là “cúng đồ ăn”. Nghi lễ thực hiện ít nhất ba chức năng. Thứ nhất, nó tái tạo collective memory: ai là tổ tiên, gia đình đến từ đâu. Thứ hai, nó tái tạo social structure: ai chủ trì, ai chuẩn bị, ai cúi lạy. Thứ ba, nó tạo synchronization: các thành viên ở xa trở về cùng thời điểm.

Chính vì nghi lễ phân phối workload không đều, đặc biệt historically lên phụ nữ và con dâu, nó cũng trở thành nơi tranh luận về gender equality. Nhiều gia đình hiện nay đơn giản hoá, đổi địa điểm, chia việc hoặc bỏ nghi lễ. Đây là ví dụ điển hình của **functional continuity**: meaning có thể được giữ trong khi implementation thay đổi.

## 결혼: hôn nhân giữa cá nhân và hai family networks

**Hôn nhân (Marriage / 결혼)** hiện nay về pháp lý là quan hệ giữa hai cá nhân, nhưng xã hội Hàn vẫn giữ nhiều dấu vết của việc hôn nhân kết nối hai family networks. Điều này thấy trong gặp mặt hai gia đình, phân chia chi phí, nghi thức cưới và cách gọi relatives sau hôn nhân.

`상견례` là buổi hai gia đình chính thức gặp nhau trước cưới. Trong nhiều trường hợp, nó đóng vai trò “handshake giữa hai network”: xác nhận relationship, thảo luận lịch trình và tạo first impression giữa những người sẽ tiếp tục gặp nhau.

`예물` và `예단` là các category quà/tài sản cưới mang historical meaning khác nhau. Mức độ thực hiện ngày nay biến thiên rất lớn; nhiều cặp giản lược hoặc bỏ vì cost và vì expectation bình đẳng hơn. Điều quan trọng là không học chúng như checklist bắt buộc, mà hiểu chúng như legacy của marriage exchange giữa households.

## 축의금: reciprocity được ghi nhớ qua thời gian

Trong đám cưới hiện đại, `축의금` — tiền mừng — là một cơ chế reciprocity. Người gửi không chỉ “mua bữa ăn”. Số tiền và việc có mặt có thể phản ánh relationship strength, precedent và chuẩn mực nhóm.

Vì nhiều quan hệ kéo dài qua nhiều sự kiện, người ta đôi khi giữ record để biết trước đây ai đã mừng bao nhiêu. Về mặt kinh tế học, đây gần với informal mutual-aid network hơn là transaction đơn lẻ.

Nếu A mừng cưới B hôm nay và nhiều năm sau B dự đám cưới con của A, exchange không cần cân bằng ngay lập tức. Đây là **reciprocity trong repeated game**, nơi memory và future interaction làm cooperation bền hơn.

## 폐백 và nghi thức sau lễ cưới

**Pyebaek (폐백)** là nghi lễ truyền thống thường được tích hợp sau lễ cưới hiện đại, trong đó cô dâu chú rể bày tỏ kính trọng với gia đình, đặc biệt phía nhà chồng trong hình thức lịch sử. Ngày nay cách tổ chức rất đa dạng và nhiều cặp không thực hiện.

Điểm học quan trọng là phân biệt giữa `wedding industry` và `family ritual`. Một lễ cưới ở wedding hall có thể rất standardized về slot thời gian, buffet và photo, trong khi pyebaek mang symbolic family layer riêng.

## 신혼집: housing trở thành một phần của marriage system

Tại Hàn Quốc, chuẩn bị nhà ở cho cặp mới cưới historically có thể gắn với expectation giữa hai gia đình. Trong xã hội giá nhà cao, `신혼집` không chỉ là câu chuyện romantic mà là bài toán financing, commute và intergenerational support.

Housing vì vậy nối trực tiếp với marriage timing. Nếu phải tích luỹ deposit lớn, lựa chọn kết hôn có thể bị delay; nếu cha mẹ hỗ trợ housing, inequality giữa households có thể được truyền qua thế hệ.

Đây là lý do chương family phải nối với [`24_economy_chaebol_housing_status_mobility.md`](24_economy_chaebol_housing_status_mobility.md).

## Gia đình hạt nhân, apartment society và 1인 가구

Công nghiệp hoá và đô thị hoá làm household Hàn Quốc nhỏ nhanh. Việc sống trong apartment gần nơi làm việc và trường học làm mô hình đại gia đình nhiều thế hệ khó duy trì như trước. Khi cả vợ chồng tham gia thị trường lao động, household economics cũng thay đổi.

**Gia đình hạt nhân (Nuclear Family / 핵가족)** từng là biểu tượng hiện đại hoá, nhưng hiện tại Hàn Quốc còn đi xa hơn với sự gia tăng hộ một người `1인 가구`.

Không nên giải thích xu hướng này bằng một nguyên nhân duy nhất như “người trẻ không muốn kết hôn”. Nó kết hợp già hoá, kết hôn muộn, ly hôn, widowhood, migration tới thành phố và lựa chọn sống độc lập.

Khi household size giảm, toàn bộ market adapts: package thực phẩm nhỏ, studio, delivery, convenience food, pet industry, self-service laundry và care service. Văn hoá gia đình vì vậy kết nối trực tiếp với product design và urban economics.

## 장남, 며느리 và sự thay đổi nghĩa vụ giới

**Con trưởng (Eldest Son / 장남)** historically có vai trò đặc biệt trong kế thừa và nghi lễ. **Con dâu (Daughter-in-law / 며느리)** thường gánh một phần lớn domestic ritual labor. Những expectation này đã suy yếu rõ, nhưng không biến mất đồng đều.

Điểm quan trọng là phân biệt descriptive với normative. Việc một tập quán từng phổ biến không có nghĩa nó là tiêu chuẩn nên duy trì. Xã hội Hàn hiện đại có tranh luận mạnh về division of care, career interruption, childcare và holiday labor.

**Career interruption / 경력단절** là thuật ngữ dùng khi sự nghiệp bị ngắt do sinh, chăm con hoặc care responsibility. Đây không chỉ là vấn đề cá nhân; nó là systems problem giữa work hours, childcare supply, school schedule, housing cost và gender norms.

## 맞벌이: dual-income household và bài toán time budget

`맞벌이` chỉ household trong đó cả hai vợ chồng cùng đi làm. Khi hai người đều có paid work nhưng domestic labour không giảm tương ứng, household gặp **time-budget constraint**.

Một ngày chỉ có 24 giờ. Nếu thời gian đi làm `W`, commute `C`, childcare `K`, housework `H` và sleep `S` tăng, leisure `L` bị ép:

```math
24 = W + C + K + H + S + L
```

Không cần dùng phương trình để “tính gia đình”; nó chỉ cho thấy tại sao convenience service, delivery, daycare, grandparent care và outsourcing domestic work trở nên có giá trị trong xã hội dual-income.

## 조부모 육아: ông bà như care infrastructure

Ông bà có thể đóng vai trò lớn trong childcare, đặc biệt khi giờ làm việc của cha mẹ không khớp với giờ nhà trẻ/trường học. Đây là một dạng **intergenerational transfer** không chỉ bằng tiền mà bằng thời gian.

Nhưng care của ông bà cũng có cost: sức khoẻ, thời gian nghỉ hưu và conflict về parenting style. Vì vậy “ông bà giúp trông cháu” không chỉ là cultural warmth; nó có thể là response của family network trước institutional gap.

Đọc sâu hơn tại [`29_childhood_parenting_care_institutions.md`](29_childhood_parenting_care_institutions.md).

## 출산과 육아: sinh con như một bài toán hệ thống

Tỷ suất sinh thấp của Hàn Quốc thường được trình bày như “người Hàn không muốn có con”. Cách nói này quá đơn giản. Quyết định sinh con là optimization dưới nhiều constraint: housing, job security, opportunity cost nghề nghiệp, chi phí giáo dục, childcare, thời gian và expectation về parenting quality.

Nếu utility của một household phụ thuộc vào income `I`, housing `H`, career `C`, leisure `L`, childcare burden `B` và expected education cost `E`, quyết định không thể giải thích bằng một biến văn hoá duy nhất.

Điểm quan trọng là expectation về “parenting tốt” cũng có thể làm cost subjectively tăng. Nếu cha mẹ tin rằng phải cung cấp housing tốt, school district tốt, hagwon và nhiều enrichment activity mới là “đủ”, perceived minimum package của parenting tăng lên.

## 비혼, 만혼 và việc tách adulthood khỏi marriage

`비혼` thường chỉ lựa chọn không kết hôn hoặc không xem marriage là mục tiêu bắt buộc. `만혼` chỉ kết hôn muộn. Đây là hai khái niệm khác nhau: delay không đồng nghĩa rejection.

Trong life-course truyền thống, adulthood từng gắn mạnh với marriage và household formation. Trong hiện đại, một người có thể có nghề nghiệp ổn định, sống riêng, đầu tư và tạo social network mà không kết hôn. Điều này làm **adult identity** ít phụ thuộc vào marital status hơn trước.

## 이혼, 재혼 và family không còn một template duy nhất

Ly hôn `이혼`, tái hôn `재혼`, single-parent household, stepfamily và international family làm landscape gia đình đa dạng hơn. Khi family form đa dạng, school form, paperwork, inheritance, holiday planning và kinship vocabulary cũng phải adapt.

Đây là lý do dùng một hình ảnh “bố–mẹ–hai con” làm default cho mọi gia đình ngày càng thiếu chính xác. Cultural literacy tốt phải nhận ra family là category có nhiều implementation.

## 다문화가정: family và migration gặp nhau

`다문화가정` là label được dùng trong policy và public discourse cho một số gia đình có background quốc tế/migration. Nhưng label có thể quá rộng: một gia đình Việt–Hàn ở Seoul, gia đình Korean-Chinese, gia đình có cha/mẹ nhập tịch và con sinh tại Hàn có experience khác nhau.

Điểm quan trọng là con cái có thể xử lý nhiều language, identity và expectation cùng lúc. School, local community và family đóng vai trò trong việc language nào được duy trì, accent nào được đánh giá và “Koreanness” được định nghĩa ra sao.

Đọc thêm tại [`15_contemporary_change_demography_migration.md`](15_contemporary_change_demography_migration.md).

## 돌, 백일, 환갑 và lifecycle ritual

**Baek-il (100-day celebration / 백일)** và **Doljanchi (First-birthday celebration / 돌잔치)** historically mang trọng lượng trong bối cảnh infant mortality cao hơn. `돌잡이` cho trẻ chọn đồ vật mang tính dự đoán biểu tượng về tương lai, nay thường mang tính vui, photo và family memory hơn là niềm tin literal.

**Hwangap (60th-birthday cycle / 환갑)** historically quan trọng vì 60 năm hoàn thành một chu kỳ can-chi. Khi tuổi thọ tăng, cách tổ chức thay đổi; một số gia đình chuyển trọng tâm sang 70 hoặc 80 tuổi.

Cultural meaning phụ thuộc baseline. Một ritual từng đánh dấu survival có thể đổi thành celebration khi demographic regime thay đổi.

## 장례: tang lễ và cộng đồng hiện diện

Tang lễ Hàn Quốc hiện đại thường diễn ra ở **funeral hall / 장례식장**, nhiều nơi nằm trong bệnh viện. Người đến viếng cúi chào, bày tỏ chia buồn và đưa `부의금`. Tang lễ thường là nơi social network của người mất và gia đình hiện rõ.

Việc đồng nghiệp, bạn học cũ hoặc đối tác tới tang không đơn giản là formal etiquette; nó thể hiện rằng quan hệ không chỉ tồn tại trong task hiện tại. `경조사` — các việc vui/buồn lớn của đời người — tạo một layer reciprocity nối workplace và family life.

Nhịp sống đô thị và dịch vụ tang lễ chuyên nghiệp hoá làm nghi thức ngày càng standardized, nhưng mức tôn giáo, cách cúi lạy và thời gian ở lại vẫn có thể khác theo gia đình.

## 노부모 부양: elder care trong xã hội già hoá

**Phụng dưỡng cha mẹ già / 노부모 부양** từng dựa mạnh vào family. Khi family size giảm, con cái sống xa và phụ nữ tham gia labour market nhiều hơn, mô hình care này chịu pressure.

Care gồm nhiều loại resource: tiền, thời gian, đưa đi bệnh viện, quản lý thuốc, nấu ăn và companionship. Nếu chỉ đo monetary transfer, ta bỏ qua invisible labour.

Đây là một trong những nơi tension giữa `효` như norm đạo đức và state welfare/care institution hiện đại xuất hiện rõ nhất.

## 반려동물 và household mới

`반려동물` — companion animal — ngày càng được nói như một thành viên household thay vì chỉ “pet”. Việc dùng từ `반려` cho thấy language cũng update theo relationship model mới.

Pet industry, pet-friendly housing, animal hospital và memorial service mở rộng khi one-person household và smaller family tăng. Không nên nói pet “thay thế con cái” một cách đơn giản; nhưng rõ ràng household resources và emotional attachment đang được phân phối theo những form mới.

## Knowledge Connection: family như một welfare system

Trước khi nhà nước phúc lợi phát triển, gia đình thường đóng vai trò insurance network: người trẻ chăm người già, gia đình hỗ trợ thất nghiệp, tài sản truyền giữa thế hệ. Khi family size giảm và người già sống lâu hơn, load trên mỗi edge trong family network tăng.

Nếu một thế hệ có ít con hơn, cùng một lượng elder care được chia cho ít người hơn. Đây là một bài toán network capacity. Chính vì vậy ageing và household change không chỉ là demographic statistics; chúng gây áp lực lên pension, healthcare, housing và workplace.

## Knowledge Connection: family như hệ thống phân phối rủi ro

Ta có thể nhìn family như một informal risk-pooling system. Một member mất việc, ốm hoặc cần deposit nhà ở có thể nhận hỗ trợ từ parents/siblings. Nhưng risk pooling chỉ hoạt động khi network còn capacity.

Nếu nhiều member cùng chịu shock — housing cost cao, elder care, childcare — family network có thể không absorb nổi. Khi đó demand chuyển sang state welfare, insurance và market service.

## Mental Model

> Gia đình Hàn Quốc nên được hiểu như một hệ thống đang chuyển từ **kinship-based institution** sang **negotiated household + distributed family network**. Nhiều symbol và nghi lễ cũ vẫn tồn tại, nhưng ai làm, ai trả tiền, ai chăm sóc, ai sống với ai và ai có quyền quyết định đang được thương lượng lại.

## Common Misconceptions

“Người Hàn sống cùng bố mẹ đến khi cưới” không còn mô tả đủ thực tế; housing cost, region, gender và income tạo khác biệt lớn.

“Đám cưới Hàn chỉ là show hình thức” bỏ qua chức năng network và reciprocity.

“Gia đình Nho giáo luôn giống nhau qua lịch sử” sai vì cấu trúc thừa kế, vai trò phụ nữ và mức độ patrilineality thay đổi theo thời kỳ.

“1인 가구 nghĩa là cô lập khỏi gia đình” sai; household address và family network là hai layer khác nhau.

“Hiếu thảo đồng nghĩa con cái phải tự chăm cha mẹ tại nhà” là cách diễn giải quá hẹp; elder care hiện đại được phân phối giữa family, healthcare, welfare và market service.
