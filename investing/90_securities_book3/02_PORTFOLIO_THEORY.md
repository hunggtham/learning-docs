# 2. Lý thuyết danh mục: lợi ích của việc không đặt mọi rủi ro vào một chỗ

Phần thống kê đã cho ta kỳ vọng, phương sai và covariance. Markowitz dùng đúng ba ngôn ngữ đó để trả lời câu hỏi: nếu cùng một khoản vốn được chia cho nhiều tài sản, ta có thể đổi quan hệ giữa lợi suất kỳ vọng và rủi ro như thế nào? Câu trả lời không phải “đa dạng hóa luôn làm lợi suất tăng”, mà là **covariance thấp có thể làm tổng rủi ro nhỏ hơn trung bình rủi ro riêng lẻ**.

## 1. Markowitz và bộ giả định

**Danh mục (portfolio / 포트폴리오)** là một tập hợp tài sản. **Lý thuyết danh mục Markowitz (Markowitz portfolio theory / 마코위츠 포트폴리오 이론)** (1952) giả định nhà đầu tư hợp lý, có cùng phân phối dự báo về lợi suất tương lai (**homogeneous expectations / 동질적 예측**), chỉ quan tâm đến kỳ vọng và phương sai trong một kỳ đầu tư. Đây là mô hình hóa để suy luận, không phải mô tả đầy đủ hành vi thật: nhà đầu tư có thể khác nhau về thông tin, mục tiêu, thuế, thanh khoản và thời hạn.

Tiêu chí **trung bình–phương sai (mean–variance / 평균-분산 기준)** nói rằng nếu hai tài sản có cùng lợi suất kỳ vọng, chọn tài sản có rủi ro thấp hơn; nếu cùng rủi ro, chọn lợi suất kỳ vọng cao hơn. Các điểm còn lại tạo thành tập cơ hội; điểm không bị một điểm khác “lợi suất cao hơn và rủi ro thấp hơn” chi phối mới đáng xét. Phần biên còn lại là **biên hiệu quả (efficient frontier / 효율적 투자선)**.

## 2. Kỳ vọng và rủi ro của danh mục hai tài sản

Với tài sản A, B có trọng số \(w_A,w_B\) và \(w_A+w_B=1\):

\[
E(r_p)=w_AE(r_A)+w_BE(r_B).
\]

Nếu A có kỳ vọng 10%, B 20%, tỷ trọng 40/60 thì danh mục có kỳ vọng 16%. Phần này tuyến tính; điều khó nằm ở rủi ro:

Trong các công thức dưới đây, (w_i) là tỷ trọng vốn (không có đơn vị), (E(r_i)) là expected return theo cùng một kỳ và cùng scale (ví dụ 0,10 hoặc 10%, không trộn hai cách), (sigma_i) là độ lệch chuẩn cùng kỳ, (sigma_i^2) là phương sai và (\rho_{AB}) là hệ số tương quan trong [-1,1]. Công thức hai tài sản giả định các đại lượng này được ước lượng cho cùng horizon; nếu covariance/correlation thay đổi theo regime, kết quả tối ưu cũng thay đổi.

\[
\sigma_p^2=w_A^2\sigma_A^2+w_B^2\sigma_B^2
 +2w_Aw_B\operatorname{Cov}(r_A,r_B),
\]

hoặc:

\[
\sigma_p^2=w_A^2\sigma_A^2+w_B^2\sigma_B^2
 +2w_Aw_B\rho_{AB}\sigma_A\sigma_B.
\]

Khi \(\rho=+1\), hai tài sản đi cùng nhau và mức giảm rủi ro bị giới hạn. Khi \(\rho<+1\), hạng tử chéo nhỏ hơn, tạo **portfolio effect**. Với tương quan −1 trong điều kiện tỷ trọng phù hợp, rủi ro lý thuyết có thể bằng 0; trong thị trường thực, tương quan thay đổi và không nên xem đó là lời hứa.

### Ba trường hợp tương quan phải nhìn thấy trên hình

Với hai tài sản có \(\sigma_A=12\%\), \(\sigma_B=7\%\), khi \(\rho=+1\), danh mục nằm trên một đường thẳng và \(\sigma_p=|w_A\sigma_A+w_B\sigma_B|\): diversification hầu như không tạo thêm lợi ích. Khi \(\rho=0\), \(\sigma_p=\sqrt{w_A^2\sigma_A^2+w_B^2\sigma_B^2}\), đường cong lõm sang trái. Khi \(\rho=-1\), \(\sigma_p=|w_A\sigma_A-w_B\sigma_B|\), nên có thể chọn trọng số để triệt tiêu rủi ro lý thuyết. Ba trường hợp này không phải ba danh mục khác nhau; chúng là ba biên để thấy covariance thay đổi hình opportunity set ra sao.

Với n tài sản, lợi suất vẫn là tổng có trọng số; phương sai gồm tổng các phương sai riêng lẻ và toàn bộ các covariance từng cặp. Khi số tài sản tăng, phần rủi ro riêng lẻ giảm nhưng phần covariance chung còn lại. Vì thế “mua rất nhiều mã” không xóa được cú sốc kinh tế, lãi suất, lạm phát hay thị trường.

### Worked check: diversification có một mức sàn

Giả sử variance của một cổ phiếu gồm systematic variance 0,09 và idiosyncratic variance 0,04. Với danh mục đều gồm \(n\) cổ phiếu độc lập ở phần riêng lẻ, variance xấp xỉ

\[
\sigma_p^2=0,09+\frac{0,04}{n}.
\]

Một mã có variance 0,13, độ lệch chuẩn khoảng 36,1%; 25 mã có variance 0,0916, độ lệch chuẩn khoảng 30,3%; khi \(n\to\infty\), độ lệch chuẩn vẫn gần 30% vì systematic floor 0,09 còn nguyên. Đây là trực giác của đường cong nguồn: đoạn đầu giảm nhanh là idiosyncratic risk, phần phẳng còn lại là risk chung mà CAPM mới định giá.

## 3. Rủi ro hệ thống và rủi ro riêng lẻ

**Rủi ro phi hệ thống (unsystematic/idiosyncratic risk / 비체계적 위험)** đến từ một doanh nghiệp hoặc ngành riêng; đa dạng hóa có thể giảm nó. **Rủi ro hệ thống (systematic/market risk / 체계적 위험)** tác động đồng thời đến nhiều tài sản; đa dạng hóa trong cùng thị trường không loại bỏ được nó. Đường cong nguồn minh họa tổng rủi ro giảm nhanh rồi tiệm cận một mức sàn: phần giảm là idiosyncratic, phần sàn là systematic.

Đây là một boundary quan trọng: phân tán không đồng nghĩa an toàn tuyệt đối. Một danh mục gồm nhiều cổ phiếu ngân hàng vẫn có thể cùng chịu một cú sốc lãi suất; nhiều tài sản cùng phụ thuộc USD vẫn có thể cùng chịu funding shock. Vì vậy sau danh mục, CAPM sẽ đo phần rủi ro mà thị trường định giá bằng beta.

## 3A. Từ opportunity set đến minimum-variance portfolio

Với hai tài sản, thay \(w_B=1-w_A\) vào phương sai sẽ cho một hàm bậc hai theo \(w_A\). Điểm đáy của hàm đó là **danh mục phương sai tối thiểu (minimum-variance portfolio, MVP / 최소분산 포트폴리오)**, không nhất thiết là danh mục có lợi suất cao nhất. Với covariance viết theo correlation, trọng số MVP của A là:

\[
w_A^{MVP}=\frac{\sigma_B^2-\rho_{AB}\sigma_A\sigma_B}
{\sigma_A^2+\sigma_B^2-2\rho_{AB}\sigma_A\sigma_B},
\qquad w_B^{MVP}=1-w_A^{MVP}.
\]

Ví dụ nguồn dùng \(\sigma_A=12\%\), \(\sigma_B=7\%\), \(\rho=0,5\). Khi thay số vào công thức, \(w_A\) xấp xỉ 0,064 và \(w_B\) xấp xỉ 0,936; độ lệch chuẩn danh mục khoảng 6,97%, thấp hơn độ lệch chuẩn của cả hai cổ phiếu. (Nếu thấy tỷ trọng 0,64/0,36 trong bản nháp cũ, đó là lỗi đảo vị trí tử số, không phải kết quả của công thức.) Expected return phải tính tiếp từ hai expected return riêng lẻ; không thể suy ra chỉ từ hai độ lệch chuẩn. Đây là một phép kiểm tra cơ chế: lợi ích đến từ covariance chứ không phải vì một cổ phiếu “tốt hơn” theo mọi tiêu chí.

### Worked check: covariance mới quyết định điểm đáy

Với hai tài sản trên, covariance là \(0,5\times0,12\times0,07=0,0042\). Ở trọng số MVP, ba phần của phương sai lần lượt là \(w_A^2\sigma_A^2\), \(w_B^2\sigma_B^2\) và \(2w_Aw_B\operatorname{Cov}_{AB}\); cộng lại cho khoảng \(0,00485\), căn bậc hai là 6,97%. Nếu đặt \(\rho=1\), hạng tử chéo tăng và lợi ích phân tán gần như biến mất; nếu đặt \(\rho=-1\), công thức có thể tạo điểm triệt tiêu rủi ro trong mô hình. Đây là cách kiểm tra bằng số cho trực giác “correlation thấp quan trọng hơn việc chỉ đếm số mã”.

MVP là điểm thấp nhất của toàn opportunity set. Từ điểm đó đi lên theo các danh mục có expected return cao hơn tạo **efficient frontier**; các điểm nằm dưới hoặc bên phải frontier bị một điểm khác thống trị. Nhà đầu tư risk-averse chọn một điểm trên frontier theo utility curve, chứ không mặc định chọn MVP. Nếu cho phép short selling, borrowing và lending, hình dạng frontier và vùng tỷ trọng khả thi thay đổi; Sách 3 đang dùng giả định đơn giản nên cần ghi rõ boundary này.

### Ràng buộc biến frontier lý thuyết thành frontier có thể giao dịch

Frontier Markowitz không bị giới hạn bởi việc người học có thể tính trọng số âm. Trong thực tế, mandate có thể yêu cầu \(w_i\ge0\), tổng trọng số bằng 1, tối đa 10% một mã, hoặc không được dùng leverage. Khi nghiệm unconstrained cho \(w_A<0\), đó là tín hiệu mô hình muốn short A; nếu short bị cấm, nghiệm phải nằm trên biên \(w_A=0\), và minimum variance mới có thể cao hơn nghiệm lý thuyết. Tương tự, một danh mục có 130% cổ phiếu và −30% cash nằm trên CAL khi được vay, nhưng không khả thi với tài khoản không margin.

Vì vậy khi trình bày “efficient”, phải ghi rõ efficient trong **tập cơ hội nào**: universe nào, có short hay không, có transaction cost/thuế hay không, và constraint rebalancing ra sao. Hai nhà đầu tư có cùng expected returns và covariance vẫn có frontier khác nhau nếu mandate khác nhau.

## 4. Utility và thái độ với rủi ro

Chỉ tối đa hóa kỳ vọng có thể xếp ba khoản đầu tư có cùng kỳ vọng là như nhau dù phương sai rất khác. **Kỳ vọng hữu dụng (expected utility / 기대효용)** đưa thái độ với rủi ro vào quyết định. Với tài sản cuối kỳ \(W\), nhà đầu tư:

- **Ngại rủi ro (risk-averse / 위험회피형)** có utility tăng nhưng tăng chậm dần; tại cùng kỳ vọng, thích rủi ro thấp hơn.
- **Trung lập rủi ro (risk-neutral / 위험중립형)** có utility tuyến tính; chỉ nhìn kỳ vọng.
- **Ưa rủi ro (risk-seeking / 위험선호형)** có utility tăng nhanh dần; chấp nhận thêm rủi ro để đổi lấy cơ hội.

Đường cong bàng quan trong mặt phẳng expected return–risk nối các điểm có cùng utility. Mô hình đầu tư thông thường dùng risk aversion, nhưng đó là giả định cần nói rõ, không phải bản chất của mọi người.

### Worked check: cùng expected return, khác expected utility

Giả sử phương án A chắc chắn đem lại 30, còn phương án B đem lại 10 hoặc 50 với xác suất 50/50. Cả hai đều có expected return 30. Với nhà đầu tư risk-averse có \(U(W)=\sqrt W\), utility của A là \(\sqrt{30}\approx5,477\), còn B là \((\sqrt{10}+\sqrt{50})/2\approx5,117\); A được chọn dù expected return bằng nhau. Nhà đầu tư risk-neutral với \(U(W)=W\) sẽ indifferent. Nếu dùng utility lồi như \(U(W)=W^2\), B có expected utility cao hơn và phù hợp risk-seeking. Bài toán cho thấy “tối đa hóa expected return” chỉ là một lựa chọn utility đặc biệt, không phải kết luận trung lập.

### Worked check: ba phương án cùng mean, khác phân phối

Raw dùng ba phương án có expected return đều bằng 30: A nhận 20 hoặc 40 với xác suất 50/50; B nhận 10, 20 hoặc 70 với xác suất 25/50/25; C nhận 20, 30 hoặc 40 với xác suất 25/50/25. Variance tương ứng khoảng 100, 550 và 50. Nếu wealth ban đầu là 100 và nhà đầu tư dùng \(U(W)=\sqrt W\), expected utility xấp xỉ A = 11,393, B = 11,359, C = 11,398, nên C được chọn dù mean bằng nhau. Risk-neutral vẫn indifferent; risk-seeking có thể thích B vì phân phối rộng hơn. Đây là lý do utility phải được nêu cùng phân phối kết quả, không chỉ cùng expected return.

## 5. Vô rủi ro và đường phân bổ vốn

**Tài sản vô rủi ro (risk-free asset / 무위험자산)** có lợi suất thực hiện đúng bằng lợi suất kỳ vọng, nên phương sai bằng 0. Ghép tài sản vô rủi ro với tài sản rủi ro có kỳ vọng \(E(r_A)\), độ lệch chuẩn \(\sigma_A\), tỷ trọng tài sản rủi ro \(w_A\):

\[
E(r_p)=r_f+w_A[E(r_A)-r_f],\qquad
\sigma_p=w_A\sigma_A.
\]

Suy ra **đường phân bổ vốn (capital allocation line, CAL / 자본배분선)**:

\[
E(r_p)=r_f+\frac{E(r_A)-r_f}{\sigma_A}\sigma_p.
\]

Độ dốc là risk-reward ratio: phần bù rủi ro trên một đơn vị độ lệch chuẩn. Ở đây (r_f), (E(r_A)) và (E(r_p)) phải cùng kỳ/đơn vị; (sigma_A,sigma_p) là độ lệch chuẩn cùng kỳ. Quan hệ tuyến tính này dựa trên giả định có thể vay/cho vay ở (r_f) và scale exposure bằng tỷ trọng; khi borrowing rate khác lending rate, leverage bị giới hạn hoặc có chi phí giao dịch, CAL thực tế không còn là một đường thẳng duy nhất. Khi A được thay bằng market portfolio tối ưu, CAL trở thành **capital market line**, sẽ học ở bài CAPM.

## 6. Bài tập nguồn và bàn giao

Source questions yêu cầu tính return gồm dividend và capital gain, phân loại risk attitude, tính expected return của danh mục, dùng correlation để tính variance, nhận diện systematic risk và giải thích vì sao tăng số mã không làm risk về 0. Để tự kiểm tra, người học nên viết công thức trước, xác định trọng số và dấu của covariance rồi mới bấm số.

Mental model cần giữ lại là: **lợi suất danh mục là trung bình có trọng số; rủi ro danh mục là hàm của cả variance và covariance; efficient frontier là kết quả của việc loại các danh mục bị chi phối**. Phần CAPM tiếp theo hỏi thị trường định giá phần rủi ro còn lại này ra sao.

Khi cần đi sâu vào allocation, rebalancing và portfolio construction hiện đại, hãy quay về [Portfolio risk, allocation and behavior](../01_foundations/02_PORTFOLIO_RISK_ALLOCATION_AND_BEHAVIOR.md); lesson này giữ phần Markowitz vào đúng dependency của Sách 3.
