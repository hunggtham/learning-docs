# 3. CAPM và thị trường hiệu quả: rủi ro nào được định giá?

Danh mục đã cho thấy diversification loại bớt rủi ro riêng lẻ. CAPM hỏi phần rủi ro còn lại được thị trường bù đắp thế nào; EMH hỏi thông tin đi vào giá nhanh đến đâu. Hai mô hình liên quan nhưng không đồng nhất: CAPM là quan hệ cân bằng giữa beta và expected return, còn EMH là mệnh đề về thông tin và khả năng kiếm excess return bền vững.

## 1. Từ CAL đến CAPM và CML

CAPM thêm hai giả định vào Markowitz: tồn tại tài sản vô rủi ro mà nhà đầu tư có thể vay/cho vay; thị trường hoàn hảo (**perfect market**) không có thuế và transaction cost, tài sản chia nhỏ vô hạn, giá công khai và nhà đầu tư không tự làm giá. Đây là thế giới chuẩn để suy ra quan hệ, không phải mô tả đầy đủ KRX hay bất kỳ thị trường hiện tại nào.

Khi mọi nhà đầu tư kết hợp tài sản vô rủi ro với cùng một **market portfolio**, CAL tiếp tuyến với efficient frontier trở thành **capital market line (CML)**:

\[
E(r_p)=r_f+\frac{E(r_m)-r_f}{\sigma_m}\sigma_p.
\]

Market portfolio chứa toàn bộ chứng khoán đang tồn tại, với tỷ trọng mỗi mã bằng giá trị thị trường của nó chia cho tổng giá trị thị trường. CML áp dụng cho các danh mục hiệu quả, đã đa dạng hóa; độ dốc là market risk premium trên một đơn vị tổng rủi ro.

Logic cân bằng của CML có ba bước. Mỗi nhà đầu tư trước hết chọn một risky portfolio trên efficient frontier; khi có risk-free asset, danh mục có slope cao nhất là danh mục đường tiếp tuyến, trở thành market portfolio (M). Cuối cùng, tổng hợp tỷ trọng của mọi nhà đầu tư buộc risky portfolio chung phải là (M); khác nhau chỉ ở tỷ trọng vay hoặc cho vay risk-free. Vì vậy market portfolio có tỷ trọng theo market value, không phải tỷ trọng bằng nhau.

### Worked check: CML cho cả expected return và covariance

Giả sử \(r_f=5\%\), \(E(r_m)=20\%\), \(\sigma_m=3\%\), còn danh mục \(P\) có \(\sigma_P=4\%\). Nếu \(P\) nằm trên CML, \(E(r_P)=5+(20-5)/3\times4=25\%\). Nếu thêm \(\rho_{P,m}=0,5\), covariance là \(\operatorname{Cov}(P,m)=0,5\times4\times3=6\) (đơn vị phần trăm bình phương). Hai phép tính trả lời hai câu hỏi khác nhau: CML nối tổng rủi ro với expected return của danh mục hiệu quả; covariance cho biết danh mục đó cùng chuyển động với market portfolio đến mức nào. Không được dùng covariance riêng lẻ để thay cho vị trí trên CML.

## 2. Beta và Security Market Line

Một cổ phiếu có thể có độ lệch chuẩn cao vì rủi ro riêng lẻ, nhưng nhà đầu tư có thể phân tán phần đó. Phần được định giá là mức cổ phiếu cùng chuyển động với market portfolio:

\[
\beta_i=\frac{\operatorname{Cov}(r_i,r_m)}{\operatorname{Var}(r_m)}.
\]

Từ đó **security market line (SML)** của CAPM là:

\[
E(r_i)=r_f+\beta_i\,[E(r_m)-r_f].
\]

Intercept là \(r_f\), slope là market risk premium. \(\beta_m=1\), beta của tài sản vô rủi ro bằng 0, và beta danh mục là trung bình có trọng số của beta cấu phần. Nếu A có beta 1,2 và B beta 1,5, tỷ trọng 40/60 cho beta danh mục 1,38.

CML dùng \(\sigma\) và dành cho danh mục hiệu quả; SML dùng \(\beta\) và áp dụng cả cho cổ phiếu riêng lẻ hoặc danh mục chưa đa dạng hóa. Đây là cặp dễ nhầm nhất trong phần CAPM. Khi tài sản nằm trên SML, expected return cao hơn mức beta yêu cầu và giá có xu hướng được mua lên; dưới SML, giá chịu áp lực bán. Trong ví dụ nguồn, \(r_f=5\%\), market return 10%, expected return cổ phiếu 12% cho beta \(\beta=(12-5)/(10-5)=1,4\).

Price adjustment phải đọc theo chiều ngược: beta xác định required return; required return dùng để discount expected cash flow; discount rate và cash flow quyết định price; price mới lại thay đổi expected return. Nếu expected return hiện tại cao hơn SML, price có thể đang thấp so với cash flow dự kiến; buying làm price tăng và expected return giảm về SML. CAPM vì thế là mô hình cân bằng, không phải máy dự báo giá ngày mai.

Phân biệt **intrinsic value** và market price giúp nối CAPM với EMH. Nhà phân tích có thể ước lượng intrinsic value từ cash flow, risk và growth; market price là giá giao dịch hiện tại. Trong thị trường hiệu quả, giá không nhất thiết bằng đúng intrinsic value ở từng thời điểm, nhưng sai lệch có kỳ vọng bằng 0 sau khi xét thông tin, rủi ro và chi phí. Nếu tin rằng intrinsic value cao hơn market price, quyết định mua phải ghi rõ giả định nào chưa được thị trường phản ánh và cơ chế nào sẽ làm giá điều chỉnh; nếu không, “undervalued” chỉ là một con số DCF khác.

## 3. Thị trường hiệu quả và ba tập thông tin

Nguồn phân biệt ba loại hiệu quả: **allocative efficiency** (vốn được phân bổ tới nơi có năng suất phù hợp), **operational efficiency** (giao dịch vận hành với chi phí thấp) và **informational efficiency** (giá phản ánh thông tin). Learning edition tập trung loại thứ ba.

Một thị trường thông tin hiệu quả cần nhiều người tham gia độc lập theo đuổi lợi ích, thông tin mới lan truyền độc lập và giá điều chỉnh nhanh. “Giá phản ánh thông tin” nghĩa là khi thông tin công khai, giá thay đổi đủ và nhanh để về giá hợp lý; phản ứng chậm hoặc phản ứng quá mức rồi đảo chiều đều không phù hợp với dạng lý tưởng.

Ba dạng EMH là các tập thông tin lồng nhau:

| Dạng | Giá đã phản ánh | Hệ quả với chiến lược |
|---|---|---|
| Weak-form (약형) | giá và volume quá khứ | quy tắc kỹ thuật dựa trên lịch sử khó tạo excess return bền vững |
| Semi-strong (준강형) | toàn bộ thông tin công khai: báo cáo, công bố, chính sách | đọc thông tin công khai sau khi phát hành không đủ tạo lợi nhuận vượt trội bền vững |
| Strong-form (강형) | mọi thông tin, kể cả nội bộ | không ai có thể duy trì lợi nhuận từ thông tin độc quyền |

Strong-form là mệnh đề mạnh nhất và nguồn nhấn mạnh nó chưa được chứng minh thực nghiệm đầy đủ. EMH cũng không nói mọi người không bao giờ có lãi; nó nói không thể **dự đoán và duy trì** excess return chỉ từ tập thông tin tương ứng sau khi tính rủi ro và chi phí.

Ma trận kiểm định của nguồn có thể đọc như sau: weak-form xem autocorrelation, random walk và trading rule; semi-strong xem event window trước/sau công bố và abnormal return; strong-form xem insider, professional trader và fund performance. Mỗi test cần benchmark return, event date, transaction cost và kiểm soát multiple testing; nếu thiếu các điều kiện đó, “anomaly” có thể chỉ là artifact của data mining.

## 4. Kiểm định, anomaly và behavioral boundary

Weak-form được kiểm tra bằng autocorrelation, random walk và trading rules; semi-strong dùng event study quanh stock split, phát hành, thay đổi kế toán hoặc earnings announcement; strong-form xem giao dịch insider, professional traders và quỹ. Một công bố “doanh thu tăng 30% nhưng giá giảm” không tự chứng minh thị trường kém hiệu quả: nếu consensus đã kỳ vọng tăng 50%, tin 30% là negative surprise.

Nguồn ghi nhận các anomaly: long-horizon negative autocorrelation (winner/loser reversal), size effect, low-PER effect và January effect. Nhưng anomaly có thể phản ánh risk model sai, sample/data-mining, transaction cost, thuế hoặc hành vi chứ không tự động bác bỏ EMH. Phần “EMH sau đó” đưa behavioral finance vào boundary: heuristic, overconfidence, mental accounting, framing, representativeness, conservatism và disposition effect có thể tạo pattern có hệ thống; hành vi ấy làm giả định “mọi nhà đầu tư luôn rational” trở nên quá mạnh.

### Worked check: winner/loser reversal là source-state, không phải alpha hiện tại

Raw ghi nhận một nghiên cứu trong nước: nhóm cổ phiếu có kết quả thấp trong ba năm trước (losers) đạt 47% trong ba năm sau, còn nhóm winners đạt −8%. Nếu hai con số được đo cùng cách, chênh lệch reversal là \(47-(-8)=55\) điểm phần trăm trong giai đoạn nghiên cứu. Đây là một observation lịch sử của nguồn, không phải lợi suất năm hóa hay dự báo hiện tại. Muốn biến nó thành chiến lược có thể kiểm định, phải nêu rõ formation window, holding window, cách xử lý dividend/delisting, benchmark, phí giao dịch, thuế và liệu kết quả còn tồn tại ngoài mẫu hay không. Nếu không, ta chỉ biết một anomaly được báo cáo, chưa biết có alpha sau chi phí.

Một test EMH còn phải chống ba bias dữ liệu. **Survivorship bias** loại các quỹ hoặc doanh nghiệp đã biến mất nên làm hiệu quả lịch sử trông cao hơn; **look-ahead bias** dùng thông tin chỉ được biết sau ngày giao dịch; **p-hacking/multiple testing** thử đủ quy tắc rồi chỉ báo cáo quy tắc có kết quả tốt. Cách kiểm soát là khóa ngày công bố, dùng out-of-sample/holdout period, benchmark trước chi phí và ghi lại toàn bộ số lần thử. Một anomaly không tái lập ngoài mẫu là giả thuyết nghiên cứu, không phải alpha đã xác nhận.

### Worked check: headline tốt nhưng surprise xấu

Giả sử doanh thu năm trước là 100. Thị trường đã kỳ vọng doanh thu năm nay là 150, tức tăng 50%, nhưng công ty chỉ công bố 130, tức tăng 30%. Tin công bố có vẻ tích cực nếu chỉ so với năm trước, nhưng **surprise** so với consensus là \(130-150=-20\), nên giá giảm vẫn phù hợp với semi-strong EMH: giá đã phản ánh kỳ vọng 150 trước ngày công bố và chỉ điều chỉnh theo phần thông tin mới. Muốn kiểm định, không được chỉ nhìn dấu của giá; phải khóa timestamp công bố, chọn benchmark, tính abnormal return quanh event window và kiểm tra chi phí giao dịch cùng các tin đồng thời.

## 5. Quản lý danh mục dưới EMH

Ngay cả khi thị trường hiệu quả, portfolio manager vẫn quyết định mức risk phù hợp với khách hàng, diversification, thuế, transaction costs và benchmark. Active management cố tìm mispricing; passive management chấp nhận giá thị trường và tái tạo market portfolio bằng index fund. Không được suy ra rằng EMH làm mọi hoạt động đầu tư vô nghĩa; nó chỉ chuyển câu hỏi từ “tôi có dự báo tốt hơn không?” sang “exposure, chi phí và mục tiêu của tôi có phù hợp không?”.

Source-question test cần phân biệt đúng weak/semi-strong/strong, CML/SML, beta market bằng 1, risk-free beta bằng 0, và nhận diện vì sao event study khác autocorrelation. Mental model bàn giao sang bài kế tiếp: sau khi biết expected return hợp lý theo risk, ta cần đo xem danh mục đã tạo ra thành quả gì sau chi phí và so với benchmark ra sao.

Một kiểm tra số: nếu cổ phiếu có β=0,5, (r_f=6\%), market premium 8%, CAPM yêu cầu 10%; forecast return 14% chỉ đáng giao dịch khi forecast cash flow, estimation error và trading cost đủ đáng tin. Vì vậy lesson valuation tiếp theo không phải phần phụ: SML nói required return, còn DCF biến required return và cash flow thành value.

### Worked check: từ beta đến abnormal return

Giả sử trong ngày công bố, market return là 1%, cổ phiếu có \(\beta=1,2\) và \(r_f\) ngày đó gần 0. CAPM/market model cho expected return khoảng 1,2%. Nếu cổ phiếu thực tế tăng 3%, abnormal return sơ bộ là 1,8% trước khi điều chỉnh event window, bid–ask spread và các tin khác. Một event study không dừng ở phép trừ này: phải ước lượng beta trên estimation window trước sự kiện, chọn benchmark, kiểm tra nhiều ngày trước/sau và xem abnormal return có bền hay chỉ là một quan sát. Đây là lý do “giá tăng sau tin” chưa đủ để bác bỏ semi-strong EMH.

Beta cũng không phải nhãn “tốt” hay “xấu”. Beta 1,5 làm required return cao hơn market nếu risk premium dương; nó chỉ nói exposure với cú sốc thị trường lớn hơn. Một doanh nghiệp có beta thấp vẫn có thể rủi ro vì leverage, thanh khoản hoặc default risk mà CAPM đơn nhân không mô tả đầy đủ.
