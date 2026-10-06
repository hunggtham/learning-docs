# Sách 1 — Hợp đồng tương lai và quyền chọn

[← Mục lục sách 1](./00-book1-index.md) · [Phần trước](./06-stock-market-trading.md) · [Phần tiếp theo](./08-securities-tax.md)

## 한국어 핵심어 — Từ khóa đọc nhanh

- `주가지수` — chỉ số giá cổ phiếu; `주가` là giá cổ phiếu, `지수` là chỉ số.
- `선물` / `옵션` — hợp đồng tương lai / quyền chọn; `선물` tạo nghĩa vụ,
  `옵션` tạo quyền nhưng không nhất thiết tạo nghĩa vụ cho bên mua.
- `기초자산` — tài sản cơ sở; hãy tìm xem hợp đồng đang dựa trên chỉ số, cổ
  phiếu hay tài sản nào.
- `콜옵션` / `풋옵션` — quyền chọn mua / bán; `콜` là quyền mua, `풋` là quyền
  bán trong ngữ cảnh quyền chọn.
- `증거금` / `레버리지` — ký quỹ / đòn bẩy; `증거금` là tiền bảo đảm thực hiện
  hợp đồng, không phải toàn bộ giá trị danh nghĩa.

Khi gặp `~을 만기일에 결제하다`, hãy đọc là “thanh toán ~ vào ngày đáo hạn”;
`만기` là đáo hạn và `결제` là thanh toán/quyết toán.

## 제7절 — 주가지수선물·옵션시장

Phái sinh chỉ số bắt đầu từ một câu hỏi khác với cổ phiếu: thay vì mua một rổ
cổ phiếu ngay hôm nay, nhà đầu tư có thể cam kết một mức giá cho giá trị của
cả rổ ở một thời điểm tương lai hay mua quyền lựa chọn mà không bắt buộc phải
thực hiện. Vì vậy, phần này luôn cần đọc cùng ba lớp: tài sản cơ sở, hợp đồng và
cơ chế ký quỹ/thanh toán.

### 1. KOSPI200 là tài sản cơ sở

KOSPI200 (`KOSPI200지수`) là chỉ số do sở giao dịch tính từ một nhóm cổ phiếu
niêm yết, với trọng số dựa trên giá trị vốn hóa thị trường. Công thức khái quát
thường gồm:

```text
KOSPI200 = tổng vốn hóa hiện tại của các cổ phiếu cấu thành
           ───────────────────────────────────────────────
           tổng vốn hóa tại thời điểm cơ sở
```

Chỉ số không phải số tiền nhà đầu tư có thể nhận khi mua “một đơn vị KOSPI200”.
Nó là thước đo tổng hợp để làm tài sản tham chiếu cho hợp đồng tương lai và
quyền chọn, đồng thời phản ánh biến động của một nhóm cổ phiếu thay vì một mã
riêng lẻ.

Danh mục cấu thành được rà soát định kỳ và có thể thay đổi bất thường khi cổ
phiếu bị hủy niêm yết, đưa vào diện quản lý, sáp nhập hoặc phát sinh sự kiện
khác. Các ngưỡng tỷ trọng, lịch thay đổi và quy tắc thay thế này là
quy tắc theo thời kỳ; khi dùng để định giá hoặc giao dịch thực tế phải kiểm tra
lại phương pháp tính hiện hành.

### 2. Hợp đồng tương lai chỉ số

#### 2.1. Cam kết giá giữa hai thời điểm

Hợp đồng tương lai chỉ số (`주가지수선물`) là cam kết mua hoặc bán giá trị quy
đổi của chỉ số vào một kỳ hạn xác định. Người mua kỳ vọng giá chỉ số/hợp đồng
tăng; người bán kỳ vọng giá giảm hoặc dùng vị thế bán để phòng hộ danh mục cổ
phiếu.

Không nên hiểu “mua hợp đồng” là sở hữu toàn bộ cổ phiếu cấu thành. Hợp đồng tạo
ra vị thế phải trả hoặc nhận phần chênh lệch theo giá thanh toán; giá trị danh
nghĩa được khuếch đại bởi hệ số nhân, trong khi nhà đầu tư chỉ nộp ký quỹ ban
đầu. Đó là nguồn gốc của đòn bẩy và cũng là lý do lỗ có thể tăng nhanh hơn số
tiền đã nộp.

#### 2.2. Kỳ hạn và giao dịch chênh lệch

Các tháng đáo hạn được chia thành kỳ hạn cơ bản và kỳ hạn niêm yết bổ sung.
Giao dịch chênh lệch (`선물스프레드`) đồng thời mua một tháng và bán một tháng
khác, với giá giao dịch là chênh lệch giữa hai kỳ hạn:

```text
spread = giá kỳ hạn xa − giá kỳ hạn gần
```

Nếu mua spread, nhà đầu tư mua kỳ hạn gần và bán kỳ hạn xa theo quy ước của
nguồn; nếu bán spread thì làm ngược lại. Vị thế spread vì thế không đơn giản là
“tăng” hay “giảm” chỉ số: nó là kỳ vọng về việc khoảng cách giữa hai kỳ hạn sẽ
mở rộng hay thu hẹp.

Khi hợp đồng được khớp, giao dịch được ghi nhận theo cùng số lượng ở hai kỳ hạn
và giá của kỳ hạn xa được suy ra từ giá kỳ hạn gần cộng với spread. Ví dụ minh
Ví dụ minh họa dùng spread 3 điểm: nếu kỳ hạn gần khớp ở 210 điểm thì kỳ hạn xa
khớp ở 213 điểm. Con số chỉ minh họa cơ chế; không phải dự báo giá.

#### 2.3. Ngày giao dịch, thanh toán và quy mô hợp đồng

Các khái niệm cần tách:

- **ngày giao dịch cuối:** ngày cuối cùng hợp đồng còn được giao dịch;
- **ngày bắt đầu giao dịch:** ngày hợp đồng mới được đưa vào hệ thống;
- **ngày thanh toán cuối:** ngày dùng giá thanh toán để hoàn tất nghĩa vụ;
- **đơn vị hợp đồng:** một hợp đồng, không phải một cổ phiếu;
- **hệ số nhân:** quy đổi một điểm chỉ số thành một số tiền.

Giá trị danh nghĩa được tính bằng:

```text
giá trị hợp đồng = điểm chỉ số × hệ số nhân
```

Ví dụ minh họa: nếu chỉ số là 100 điểm và hệ số nhân là 25 triệu đồng
cho mỗi điểm, một hợp đồng có giá trị danh nghĩa 2,5 tỷ đồng. Đây là giá trị
quy đổi để tính lời/lỗ, không phải số tiền phải trả toàn bộ khi mở vị thế.

Đơn vị yết giá, khối lượng lệnh tối đa, giờ giao dịch và các tháng đáo hạn đều là
snapshot. Phần bền vững cần nhớ là: hợp đồng có ngày đáo hạn,
được đánh giá lại theo giá thanh toán, và thường được thanh toán bằng chênh lệch
thay vì giao một rổ cổ phiếu.

#### 2.4. Giá tham chiếu, biên giá và gián đoạn giao dịch

Giá tham chiếu thường lấy từ giá lý thuyết hoặc giá thanh toán trước đó, tùy
thời điểm của hợp đồng. Biên giá theo tầng giới hạn mức dao động trong ngày; cơ
chế ngắt mạch dừng giao dịch khi biến động quá lớn, rồi mở lại bằng khớp một giá.

Hệ thống còn có cơ chế dừng giao dịch tự nguyện khi quyền chọn/tương lai hoặc
hệ thống giao dịch cổ phiếu gặp sự cố kéo dài, và cơ chế Sidecar tạm thời hạn
chế hiệu lực của lệnh khi giá hợp đồng tương lai biến động mạnh. Các tỷ lệ 8%,
15%, 20%, thời lượng tạm dừng và giờ áp dụng chỉ là số liệu của ấn bản này.

### 3. Quyền chọn chỉ số

Quyền chọn (`주가지수옵션`) tạo quyền, không tạo nghĩa vụ bắt buộc, cho người mua:

- **call:** quyền mua theo giá thực hiện;
- **put:** quyền bán theo giá thực hiện.

Người mua trả **phí quyền chọn (premium)** để có quyền đó. Người bán nhận phí
nhưng gánh nghĩa vụ nếu người mua thực hiện. Vì vậy, mất mát tối đa của người
mua thường bị giới hạn ở phí đã trả, trong khi người bán cần quản lý ký quỹ và
rủi ro nghĩa vụ.

Kỳ hạn, ngày giao dịch cuối, ngày thanh toán cuối, tháng niêm yết và giá thực
hiện phải được đọc cùng nhau. Giá thực hiện là mức tham chiếu để xác định quyền
có giá trị; premium là giá thị trường của chính quyền đó. Không được đồng nhất
hai loại giá này.

Một số biến số vận hành cần theo dõi:

- quyền chọn được gắn với KOSPI200;
- kỳ hạn thanh toán và tháng niêm yết được quy định theo lịch;
- đơn vị giao dịch là một hợp đồng;
- biên giá được mở rộng theo các tầng;
- giao dịch có thể bị dừng khi thị trường cơ sở hoặc hệ thống gặp điều kiện đặc
  biệt.

Các con số về bước giá, hạn mức lệnh, thời gian và khoảng cách giá thực hiện là
quy tắc lịch sử. Khi phân tích quyền chọn, điều quan trọng hơn là theo dõi quan
hệ giữa giá cơ sở, giá thực hiện, thời gian còn lại, premium và biến động kỳ
vọng.

### 4. ELW và các loại chứng quyền gắn với cổ phiếu

ELW (`Equity Linked Warrant`) là chứng khoán do một tổ chức phát hành, cho phép
nhà đầu tư mua (`call`) hoặc bán (`put`) tài sản cơ sở theo giá thực hiện trước
định. ELW được giao dịch trên thị trường cổ phiếu, nên nhà đầu tư có thể tham
gia với số tiền nhỏ hơn so với mua trực tiếp toàn bộ tài sản cơ sở.

Điểm khác biệt quan trọng so với quyền chọn niêm yết:

| Khía cạnh | ELW | Quyền chọn cổ phiếu/chỉ số |
|---|---|---|
| Bên phát hành | tổ chức được phép phát hành | đối tác trong hệ thống quyền chọn |
| Nơi giao dịch | thị trường cổ phiếu | thị trường quyền chọn |
| Tài sản cơ sở | cổ phiếu hoặc chỉ số đủ điều kiện | danh mục tài sản được quy tắc quyền chọn quy định |
| Thanh khoản | thường có nhà cung cấp thanh khoản (`LP`) | phụ thuộc cung–cầu của sổ lệnh |
| Rủi ro tín dụng | gắn với khả năng thực hiện của tổ chức phát hành | gắn với cơ chế thanh toán bù trừ |

Chứng quyền do công ty phát hành (`Company Warrant`) cho người sở hữu quyền mua
cổ phiếu mới của chính công ty khi thực hiện. Chứng quyền có bảo đảm
(`Covered Warrant`) thường do công ty chứng khoán phát hành để cung cấp một
công cụ quản lý danh mục, không phải để huy động vốn cho công ty cơ sở. Hai
loại này khác ELW ở chủ thể phát hành và dòng tiền khi quyền được thực hiện.

LP giữ vai trò đưa giá mua/bán để hỗ trợ thanh khoản. Nhà cung cấp thanh khoản
không thể xóa rủi ro giá, rủi ro phát hành hoặc rủi ro cấu trúc; họ chỉ giúp nhà
đầu tư có khả năng tìm thấy đối ứng trong điều kiện quy tắc cho phép.

### 5. Đọc các chỉ số của ELW

Các chỉ số này giúp so sánh quyền chọn có giá và thời hạn khác nhau.
Chúng là công cụ đọc cấu trúc, không phải tín hiệu mua bán độc lập.

#### 5.1. Premium

Premium đo phần giá ELW cao hơn hoặc thấp hơn giá trị nội tại so với tài sản cơ
sở. Công thức được biểu diễn theo phần trăm:

```text
premium = (giá ELW − giá trị nội tại) / giá tài sản cơ sở × 100
```

Premium dương có thể phản ánh thời gian còn lại, biến động kỳ vọng, chi phí vốn
hoặc điều kiện thanh khoản. Vì vậy, premium thấp không tự động có nghĩa là rẻ.

#### 5.2. Điểm hòa vốn và CFP

Điểm hòa vốn của call và put được xác định bằng cách cộng hoặc trừ giá thực hiện
với phần giá ELW đã quy đổi theo tỷ lệ chuyển đổi:

```text
call break-even = giá thực hiện + (giá ELW / tỷ lệ chuyển đổi)
put  break-even = giá thực hiện − (giá ELW / tỷ lệ chuyển đổi)
```

CFP (`Capital Fulcrum Point`) là mức tăng trưởng kỳ vọng hằng năm của tài sản cơ
sở khiến lợi suất đến ngày đáo hạn của tài sản cơ sở và ELW cân bằng theo công
thức trên. Nó hữu ích để so sánh các ELW có ngày đáo hạn khác nhau, nhưng
phụ thuộc mạnh vào giả định giá hiện tại, giá thực hiện và thời gian còn lại.

#### 5.3. Parity, gearing và effective gearing

- **Parity:** so sánh giá tài sản cơ sở với giá thực hiện; parity trên 100 cho
  thấy có giá trị nội tại, còn dưới 100 cho thấy chưa có giá trị nội tại theo
  cách trình bày này.
- **Gearing:** cho biết mua ELW thay thế trực tiếp tài sản cơ sở với quy mô vốn
  nhỏ hơn bao nhiêu lần:

  ```text
  gearing = giá tài sản cơ sở / (giá ELW × tỷ lệ chuyển đổi)
  ```

- **Effective gearing:** kết hợp gearing với delta để ước lượng mức nhạy của
  ELW trước một biến động nhỏ của tài sản cơ sở:

  ```text
  effective gearing = gearing × delta
  ```

Đòn bẩy chỉ nói về độ nhạy phần trăm, không nói rằng lợi nhuận sẽ tăng theo
đúng tỷ lệ đó. Thời gian hao mòn, biến động, chênh lệch mua–bán, khả năng thực
hiện của bên phát hành và điều chỉnh tỷ lệ chuyển đổi đều có thể làm kết quả
khác xa ví dụ tĩnh.

### 6. Hợp đồng tương lai và quyền chọn cổ phiếu riêng lẻ

Hợp đồng tương lai cổ phiếu (`개별주식선물`) và quyền chọn cổ phiếu riêng lẻ dùng
một mã cổ phiếu làm tài sản cơ sở. Việc chọn cổ phiếu thường dựa trên quy mô, số cổ
đông, thanh khoản và dữ liệu tài chính đủ để hình thành thị trường phái sinh.

Cơ chế đọc vẫn giống chỉ số:

```text
tài sản cơ sở → hợp đồng/kỳ hạn → hệ số nhân và đơn vị giao dịch
→ ký quỹ/thanh toán → biên giá và ngắt mạch
```

Điểm khác là rủi ro tập trung vào một doanh nghiệp. Sự kiện chia tách, cổ tức,
phát hành thêm, hủy niêm yết hoặc thay đổi vốn có thể làm thay đổi giá tham
chiếu, hệ số điều chỉnh và điều kiện giao dịch. Vì vậy, một mức giá phái sinh
không thể được đọc tách khỏi lịch sự kiện của cổ phiếu cơ sở.

### 7. Công thức payoff và ký quỹ cần tự tính

Với `S_T` là giá tài sản cơ sở tại đáo hạn, `K` là giá thực hiện, `P` là
premium và `M` là hệ số nhân, có thể dựng payoff cơ bản:

```text
long call: max(S_T − K, 0) × M − P × M
long put : max(K − S_T, 0) × M − P × M
futures long: (giá thanh toán cuối − giá vào vị thế) × M
futures short: (giá vào vị thế − giá thanh toán cuối) × M
```

Đây là lợi/lỗ trước phí và điều chỉnh, dùng để kiểm tra hướng biến động. Ký quỹ
không phải chi phí mua toàn bộ tài sản; nó là khoản bảo đảm cho nghĩa vụ có thể
phát sinh. Nếu giá đi ngược vị thế, khoản lỗ được tính lại theo giá thanh toán và
có thể phát sinh yêu cầu nộp thêm.

#### 7.1. Vòng đời ký quỹ và thanh toán của một vị thế

Hãy đọc ký quỹ như một chuỗi trạng thái, không phải một khoản “phí mua hợp đồng”:

```text
mở vị thế
→ nộp ký quỹ ban đầu trên giá trị danh nghĩa
→ định giá lại theo giá thanh toán trong ngày
→ lãi được ghi có / lỗ bị trừ khỏi tài khoản
→ nếu số dư xuống dưới mức duy trì: nộp bổ sung hoặc giảm vị thế
→ đóng vị thế hoặc thanh toán cuối kỳ
```

| Trạng thái | Điều xảy ra | Câu hỏi cần kiểm tra |
|---|---|---|
| Ký quỹ ban đầu (`위탁증거금`) | đặt một phần tiền/tài sản bảo đảm để mở vị thế | tỷ lệ được tính trên giá trị danh nghĩa hay theo mô hình rủi ro nào? |
| Đánh giá lại hàng ngày (`일일정산`) | lời/lỗ được chuyển vào tài khoản theo giá thanh toán | giá thanh toán được xác định lúc nào và khác giá giao dịch cuối ra sao? |
| Ký quỹ duy trì (`유지증거금`) | số dư tối thiểu để tiếp tục giữ vị thế | khi nào phát sinh `추가증거금` và ai có quyền đóng cưỡng bức? |
| Đáo hạn/thanh toán cuối | nghĩa vụ được tất toán theo giá/điều kiện cuối kỳ | hợp đồng thanh toán bằng tiền hay có cơ chế giao tài sản? |

Ví dụ, một hợp đồng có giá trị danh nghĩa 1 tỷ nhưng chỉ yêu cầu ký quỹ 100 triệu
không có nghĩa rủi ro tối đa là 100 triệu. Nếu giá cơ sở giảm đủ mạnh, lỗ được
ghi nhận theo giá trị danh nghĩa và có thể vượt số tiền ban đầu. Ký quỹ chỉ là
điều kiện để duy trì vị thế; nó không phải giới hạn trách nhiệm.

Các tỷ lệ ký quỹ, ngưỡng duy trì, thời điểm gọi bổ sung và quy tắc cưỡng chế là
thông số theo sản phẩm/thời kỳ. Khi dùng thực tế, phải đọc quy chế của sở và công
ty chứng khoán, không lấy ví dụ 1 tỷ/100 triệu làm tỷ lệ hiện hành.

### 8. Cùng một hợp đồng, ba mục đích kinh tế

Không thể suy ra mục đích của một vị thế chỉ từ việc nhà đầu tư mua hay bán. Cùng
là hợp đồng tương lai chỉ số, vị thế có thể dùng để giảm rủi ro, chấp nhận rủi ro
để tìm lợi nhuận, hoặc khai thác chênh lệch giữa hai giá. Hãy đọc theo **tài sản
đang được bảo vệ**, **nguồn lợi nhuận kỳ vọng** và **rủi ro còn lại**:

| Mục đích | Cấu trúc minh họa | Lợi nhuận/rủi ro cần theo dõi |
|---|---|---|
| `헤지` — phòng hộ | đang nắm cổ phiếu, bán futures chỉ số; hoặc mua put | giảm tác động khi thị trường giảm nhưng tạo basis risk: danh mục không biến động y hệt chỉ số, cùng với chi phí premium/ký quỹ |
| `투기` — đầu cơ | mua futures khi kỳ vọng chỉ số tăng; mua call khi muốn giới hạn lỗ ở premium | đòn bẩy làm lời/lỗ thay đổi nhanh; với futures, lỗ không bị giới hạn ở số tiền ký quỹ ban đầu |
| `차익거래`/spread — kinh doanh chênh lệch | mua tài sản hoặc kỳ hạn rẻ hơn đồng thời bán vị thế liên quan đắt hơn | lợi nhuận kỳ vọng đến từ hội tụ giá, nhưng vẫn có chi phí vốn, thanh khoản, thời điểm thanh toán và rủi ro basis |

Ví dụ: danh mục cổ phiếu có beta gần 1 so với KOSPI200 có thể bán futures để
giảm rủi ro thị trường chung. Nếu chỉ số giảm nhưng các cổ phiếu trong danh mục
giảm ít hơn, vị thế futures có thể tạo lãi nhưng cũng làm mất một phần lợi nhuận
khi thị trường hồi phục. Đây là **phòng hộ không hoàn hảo**, không phải cách xóa
toàn bộ rủi ro.

Với spread giữa hai tháng đáo hạn, câu hỏi đúng không phải “chỉ số sẽ tăng hay
giảm?” mà là “chi phí vốn, cổ tức kỳ vọng và thời gian còn lại khiến khoảng cách
giữa hai hợp đồng thay đổi thế nào?”. Cách đặt câu hỏi này nối phần công thức
với cơ chế định giá, thay vì biến phái sinh thành một dự đoán hướng đơn giản.

### 9. Bảng đọc nhanh chỉ số ELW

| Chỉ số | Câu hỏi nó trả lời | Cạm bẫy |
|---|---|---|
| Premium | giá ELW đang cao hơn giá trị nội tại bao nhiêu? | premium thấp không tự động là rẻ |
| Break-even | giá cơ sở nào mới bù được giá thực hiện và tiền mua ELW? | phải đổi theo tỷ lệ chuyển đổi |
| Parity | quyền đã có giá trị nội tại chưa? | không phản ánh đầy đủ giá trị thời gian |
| Gearing | với cùng vốn, mức tiếp xúc danh nghĩa lớn hơn bao nhiêu? | đòn bẩy khuếch đại cả lỗ |
| Effective gearing | giá ELW nhạy thế nào trước biến động nhỏ của tài sản cơ sở? | delta và thanh khoản thay đổi theo thời gian |

### 10. Kiểm tra hiểu phần phái sinh

1. Nếu KOSPI200 tăng nhưng premium quyền chọn giảm, những biến nào ngoài giá cơ
   sở có thể giải thích hiện tượng đó?
2. Vì sao người mua call bị giới hạn lỗ ở premium trong mô hình cơ bản, còn người
   bán call phải quản lý ký quỹ?
3. Hãy tính payoff long call với `S_T = 230`, `K = 220`, `M = 1`, `P = 4`, rồi
   giải thích vì sao giá trị danh nghĩa không bằng số tiền premium.
