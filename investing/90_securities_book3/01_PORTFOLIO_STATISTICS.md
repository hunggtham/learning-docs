# 1. Thống kê cho đầu tư: biến động phải được đo trước khi được quản trị

Sách 3 mở đầu bằng một điểm rất thực tế: giá trị doanh nghiệp phụ thuộc vào dòng tiền tương lai, nhưng dòng tiền ấy chưa biết chắc. Vì vậy người học cần một ngôn ngữ để mô tả điều đã biết, điều chưa chắc và mức độ phân tán của các kết quả. Chương này nối trực tiếp sang danh mục: nếu chưa phân biệt kỳ vọng, phương sai và tương quan, ta sẽ không hiểu vì sao ghép hai tài sản có thể làm rủi ro giảm.

## 1. Từ dữ liệu quan sát đến kỳ vọng

**Tổng thể (population / 모집단)** là toàn bộ dữ liệu mà ta quan tâm; **mẫu (sample / 표본)** là phần được quan sát vì thời gian hoặc chi phí có giới hạn. Khi kết quả được quyết định ngẫu nhiên, ta dùng **biến ngẫu nhiên (random variable / 확률변수)**. Phân phối xác suất ghép mỗi giá trị có thể xảy ra với xác suất của nó; tổng các xác suất phải bằng 1.

Với dữ liệu đã quan sát, **trung bình số học (arithmetic mean / 산술평균)** là:

\[
\bar x=\frac{x_1+\cdots+x_n}{n}.
\]

Với kết quả chưa biết nhưng có phân phối, **kỳ vọng (expected value / 기댓값)** là trung bình có trọng số:

\[
E(X)=\sum_i x_i p_i,
\]

hoặc với biến liên tục:

\[
E(X)=\int x f(x)\,dx.
\]

**Biến ngẫu nhiên rời rạc (discrete random variable / 이산확률변수)** có các giá trị đếm được; **biến ngẫu nhiên liên tục (continuous random variable / 연속확률변수)** có vô số giá trị trong một khoảng. Với biến liên tục, xác suất tại đúng một điểm thường bằng 0 nên ta tính xác suất trên khoảng, chẳng hạn \(P(a<X<b)=\int_a^b f(x)dx\). Ví dụ nguồn cho các giá trị 1, 2, 3, 4 với xác suất 0,2; 0,3; 0,3; 0,2, nên \(E(X)=2,5\). Điểm cần giữ là kỳ vọng không phải lời hứa rằng kết quả thực tế sẽ bằng 2,5; nó là tâm của phân phối dùng cho quyết định.

Khi dữ liệu là các mức tăng trưởng nối tiếp, trung bình số học không phải lúc nào cũng là đại lượng cần dùng. **Trung bình nhân (geometric mean / 기하평균)** của các mức return dương là \(\left(\prod_t(1+r_t)\right)^{1/T}-1\), phù hợp với tăng trưởng lũy kế; **trung bình điều hòa (harmonic mean / 조화평균)** là nghịch đảo của trung bình các nghịch đảo, phù hợp với một số bài toán tốc độ/giá trên một đơn vị. Dùng arithmetic mean cho return lũy kế sẽ phóng đại kết quả khi volatility lớn.

Ví dụ dễ thấy về harmonic mean: đi 60 km với tốc độ 30 km/h rồi quay lại 60 km với tốc độ 60 km/h. Vì hai chặng có cùng quãng đường, tốc độ trung bình đúng là harmonic mean \(2/(1/30+1/60)=40\) km/h, không phải arithmetic mean 45 km/h. Trong đầu tư, cùng logic xuất hiện khi lượng vốn mua được ở các mức giá khác nhau hoặc khi một tỷ lệ “trên mỗi đơn vị” được ghép qua nhiều kỳ; phải xác định đại lượng đang cộng là return, thời gian hay đơn vị trước khi chọn loại trung bình.

## 2. Độ phân tán: phương sai, độ lệch chuẩn và mẫu

**Độ lệch (deviation / 편차)** của quan sát là \(d_i=x_i-E(X)\). Trung bình các độ lệch bằng 0, nên muốn đo độ xa khỏi tâm ta bình phương chúng. **Phương sai (variance / 분산)** tổng thể và phương sai mẫu lần lượt là:

\[
\sigma^2=\frac{\sum_i(x_i-\mu)^2}{n},\qquad
s^2=\frac{\sum_i(x_i-\bar x)^2}{n-1}.
\]

Mẫu số \(n-1\) phản ánh việc trung bình mẫu đã được ước lượng từ chính dữ liệu; không được đổi n và n−1 tùy tiện. **Độ lệch chuẩn (standard deviation / 표준편차)** là căn bậc hai của phương sai, cùng đơn vị với dữ liệu và vì vậy dễ diễn giải hơn. Trong bài tỷ suất sinh lợi 12 tháng của nguồn, trung bình là −1,8%, tổng bình phương độ lệch là 835,74 và vì đây là mẫu nên \(s^2=835,74/11=75,98\), \(s≈8,72\%\).

Rủi ro trong quyển này được đo như độ biến thiên quanh kỳ vọng. Cách đo đối xứng này coi cả kết quả thấp hơn lẫn cao hơn kỳ vọng là “rủi ro”; đó là giới hạn quan trọng khi ta chỉ quan tâm downside risk. Khi sang danh mục, ta sẽ thấy một phần biến thiên riêng lẻ có thể triệt tiêu, nhưng không phải mọi biến thiên đều triệt tiêu được.

Nếu câu hỏi chỉ là “kết quả có thấp hơn mức mục tiêu không?”, có thể dùng **downside deviation** thay vì phạt cả những kết quả cao. Với target \(MAR\), một dạng semivariance là

\[
\sigma_-^2=\frac{1}{n}\sum_{t=1}^n\min(r_t-MAR,0)^2.
\]

Ví dụ return là −10%, 0%, 8% và 20%, với \(MAR=0\). Phương sai thông thường bình phương cả bốn độ lệch quanh mean; downside measure chỉ giữ −10% và 0%, vì hai kỳ dương không làm nhà đầu tư hụt mục tiêu. Đây không phải “cách đo đúng hơn” trong mọi tình huống: downside deviation phụ thuộc target, còn standard deviation hữu ích khi mô hình mean–variance cần cả hai phía. Điều quan trọng là không dùng một thước đo rồi quên câu hỏi mà nó trả lời.

## 3. Hai biến cùng chuyển động: scatterplot, covariance và correlation

Hãy vẽ **biểu đồ phân tán (scatterplot / 산포도)** trước khi tính số: mỗi điểm là một cặp \((x_i,y_i)\), giúp thấy quan hệ tăng, giảm hay không có hướng. **Hiệp phương sai (covariance / 공분산)** đo hai biến cùng lệch khỏi trung bình như thế nào:

\[
\operatorname{Cov}(X,Y)=E[(X-E(X))(Y-E(Y))].
\]

Covariance dương khi hai biến thường đi cùng hướng, âm khi đi ngược hướng, nhưng độ lớn phụ thuộc đơn vị đo nên khó so sánh giữa các cặp. **Hệ số tương quan (correlation coefficient / 상관계수)** chuẩn hóa nó:

\[
\rho_{XY}=\frac{\operatorname{Cov}(X,Y)}{\sigma_X\sigma_Y},\qquad -1\le\rho\le1.
\]

\(|\rho|\) gần 1 nghĩa là quan hệ tuyến tính chặt; dấu cho biết hướng. \(\rho≈0\) chỉ nói không có quan hệ tuyến tính rõ, không chứng minh hai biến độc lập hay quan hệ nhân quả. Đây là ranh giới cần nhớ khi đọc “tương quan” trong nghiên cứu đầu tư.

## 4. Biến đổi tuyến tính và hồi quy

Nếu \(Y=aX+b\), thì:

\[
E(Y)=aE(X)+b,\qquad V(Y)=a^2V(X),\qquad \sigma_Y=|a|\sigma_X.
\]

**Chuẩn hóa/tiêu chuẩn hóa (normalization/standardization / 정규화·표준화)** \(Z=(X-\mu)/\sigma\) đưa kỳ vọng về 0 và độ lệch chuẩn về 1. Với hai biến đổi \(U=aX+b\), \(V=cY+d\), hiệp phương sai là \(\operatorname{Cov}(U,V)=ac\operatorname{Cov}(X,Y)\). Khi ghép hai biến thành \(Z=aX+bY\):

\[
V(Z)=a^2\sigma_X^2+b^2\sigma_Y^2+2ab\operatorname{Cov}(X,Y).
\]

### Worked check: biến đổi tuyến tính không chỉ đổi mean

Giả sử return \(X\) có mean 5% và độ lệch chuẩn 10%, còn \(Y=2X+1\) (đơn vị phần trăm). Khi đó \(E(Y)=2\times5+1=11\%\), \(\sigma_Y=|2|\times10=20\%\), và \(\operatorname{Cov}(X,Y)=2\operatorname{Var}(X)\). Hệ số dương làm biến động tăng gấp đôi; nếu hệ số âm, hướng chuyển động đảo và covariance đổi dấu. Đây là cùng phép toán đứng sau leverage, beta và việc quy đổi exposure: thay đổi notional không chỉ nhân expected return mà còn nhân risk và covariance.

Chính hạng tử covariance này là cầu nối sang công thức rủi ro danh mục.

**Hồi quy (regression / 회귀분석)** dùng **biến độc lập (independent variable / 독립변수)** để dự báo **biến phụ thuộc (dependent variable / 종속변수)**. Hồi quy đơn có dạng \(Y=\alpha+\beta X+\varepsilon\); \(\varepsilon\) là **phần dư (residual / 잔차)** giữa giá trị thật và giá trị dự báo. **Phương pháp bình phương tối thiểu (least squares / 최소자승법)** chọn \(\alpha,\beta\) để tổng \(\varepsilon_i^2\) nhỏ nhất:

\[
\hat\beta=\frac{\sum_i(X_i-\bar X)(Y_i-\bar Y)}{\sum_i(X_i-\bar X)^2},
\qquad \hat\alpha=\bar Y-\hat\beta\bar X.
\]

Ví dụ quảng cáo–doanh thu trong nguồn cho \(\hat\beta=0,6\), \(\hat\alpha=2,2\), tức mô hình mẫu là \(\hat Y=2,2+0,6X\). Đây là công cụ dự báo tuyến tính, không phải bằng chứng rằng quảng cáo là nguyên nhân duy nhất của doanh thu.

Hồi quy còn có ba ranh giới: correlation không chứng minh causal effect; residual không được tự động xem là noise không có cấu trúc; và mô hình \(Y=\alpha+\beta X\) chỉ hợp lý khi quan hệ gần tuyến tính trong vùng dữ liệu. Khi chuyển sang beta trong CAPM, ta dùng covariance/variance theo logic hồi quy nhưng không nên nhầm beta là nguyên nhân của return.

### Worked check: cùng dữ liệu, đổi mẫu số là đổi câu hỏi

Giả sử ba return của tài sản A là 10%, −5% và 15%, còn B là 5%, 0% và 10%. Trung bình A là 6,67% và B là 5%. Nếu coi đây là **toàn bộ tổng thể**, phương sai A dùng mẫu số 3; nếu coi đây là **mẫu** để ước lượng các kỳ tương lai, phương sai dùng mẫu số 2. Với cách mẫu, covariance của A và B là khoảng 50 (đơn vị phần trăm bình phương), correlation khoảng 0,96: hai tài sản gần như đi cùng chiều trong tập dữ liệu này. Con số đó không đủ để kết luận tương lai; nó chỉ cho biết vì sao khi đưa hai tài sản vào cùng danh mục, hạng tử covariance có thể làm rủi ro tăng thay vì giảm.

Quy trình đọc một bảng return nên là: (1) xác định đơn vị và tần suất; (2) chọn tổng thể hay mẫu; (3) tính mean; (4) tính deviation và variance; (5) kiểm tra covariance/correlation; (6) chỉ sau đó mới đưa kết quả vào beta hoặc portfolio variance. Bỏ qua bước đầu thường tạo ra kết quả “đúng phép tính” nhưng sai câu hỏi.

## 5. Tự kiểm tra theo câu hỏi nguồn

Người học phải tính được trung bình và độ lệch chuẩn của một con xúc xắc, kỳ vọng của trò chơi xác suất, tổng sinh lợi qua nhiều tháng, correlation từ covariance và hai độ dốc hồi quy. Khi làm, hãy ghi rõ dữ liệu là tổng thể hay mẫu và kiểm tra đơn vị. Nếu đã có các đại lượng này, phần kế tiếp dùng chúng để chứng minh diversification: **expected return là trung bình có trọng số, còn portfolio risk có thêm covariance**.

Phần công thức danh mục chuyên sâu hơn nằm trong [Risk measurement & portfolio analytics](../01_foundations/04_RISK_MEASUREMENT_PORTFOLIO_ANALYTICS_AND_DECISION_RULES.md); file này chỉ giữ nền thống kê mà Sách 3 cần để đọc mạch tiếp.
