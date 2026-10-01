# Năng lượng tự do Gibbs — tiêu chuẩn nhiệt động ở nhiệt độ và áp suất không đổi

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Năng lượng tự do Gibbs — tiêu chuẩn nhiệt động ở nhiệt độ và áp suất không đổi**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Vì sao cần một thế nhiệt động mới?** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Vi phân cơ bản của G** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

> **Năng lượng tự do Gibbs (Gibbs free energy, \(G\) / Gibbs 자유 에너지)** kết hợp enthalpy và entropy theo \(G=H-TS\). Ở nhiệt độ và áp suất không đổi, dấu của \(\Delta G\) cho tiêu chuẩn nhiệt động về chiều biến đổi tự diễn ra.

Một cách nhìn sâu hơn là: Gibbs free năng lượng (energy / 에너지) là **thế nhiệt động phù hợp với hóa học trong điều kiện nhiệt độ và áp suất được giữ gần cố định**, vì nó gói các đóng góp năng lượng và entropy vào một đại lượng duy nhất có thể tối thiểu hóa.

## Vì sao cần một thế nhiệt động mới?

Định luật thứ hai nói quá trình tự diễn ra làm entropy của vũ trụ tăng. Nhưng trong Hóa học, ta thường muốn chỉ tính các đại lượng của hệ thay vì luôn phải mô hình hóa môi trường.

Ở nhiệt độ và áp suất không đổi, biến thiên entropy của môi trường do truyền nhiệt gần bằng:

\[
\Delta S_{môi\ trường}=-\frac{\Delta H_{hệ}}{T}
\]

Theo định luật thứ hai:

\[
\Delta S_{vũ\ trụ}=\Delta S_{hệ}-\frac{\Delta H_{hệ}}{T}>0
\]

Nhân với `-T`:

\[
\Delta H-T\Delta S<0
\]

Đó chính là:

\[
\Delta G<0
\]

Vì vậy Gibbs free năng lượng (energy / 에너지) cho phép dùng **chỉ các đại lượng của hệ** để kiểm tra chiều tự phát trong điều kiện hóa học phổ biến.

> **Chuyển mạch:** Chọn G cho điều kiện T/P không đổi; vi phân của G cho biết các biến liên hợp, rồi dấu ΔG nối state change với hướng tự phát.

## Vi phân cơ bản của G

Từ:

\[
G=H-TS
\]

và với hệ một thành phần đơn giản:

\[
dH=TdS+VdP
\]

suy ra:

\[
dG=VdP-SdT
\]

Với hệ nhiều thành phần:

\[
dG=VdP-SdT+\sum_i\mu_i dn_i
\]

Trong đó \(\mu_i\) là **thế hóa học (chemical potential)** của cấu tử \(i\).

Phương trình này rất quan trọng vì nó cho thấy Gibbs free năng lượng (energy / 에너지) thay đổi theo ba loại biến:

- nhiệt độ;
- áp suất;
- thành phần hóa học.

> **Chuyển mạch:** Ở chặng này của **Năng lượng tự do Gibbs — tiêu chuẩn nhiệt động ở nhiệt độ và áp suất không đổi**, **Ý nghĩa của dấu ΔG** tiếp nhận điểm tựa từ **Vi phân cơ bản của G** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **G là tiêu chuẩn tối thiểu ở T và P không đổi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ý nghĩa của dấu ΔG

Nếu:

\[
\Delta G<0
\]

chiều thuận thuận lợi về mặt nhiệt động.

Nếu:

\[
\Delta G>0
\]

chiều thuận không tự diễn ra dưới các điều kiện đó; chiều nghịch thuận lợi hơn.

Nếu:

\[
\Delta G=0
\]

hệ ở trạng thái cân bằng dưới các ràng buộc đang xét.

“Tự diễn ra” không có nghĩa “xảy ra ngay lập tức”. Kim cương → graphite có thể thuận lợi về nhiệt động nhưng cực chậm vì hàng rào động học cao.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Năng lượng tự do Gibbs — tiêu chuẩn nhiệt động ở nhiệt độ và áp suất không đổi**, **G là tiêu chuẩn tối thiểu ở T và P không đổi** tiếp nhận điểm tựa từ **Ý nghĩa của dấu ΔG** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sự cạnh tranh giữa enthalpy và entropy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## G là tiêu chuẩn tối thiểu ở T và P không đổi

Với hệ kín ở nhiệt độ và áp suất không đổi, trạng thái cân bằng ổn định tương ứng với **cực tiểu Gibbs free năng lượng (energy / 에너지)** dưới các ràng buộc bảo toàn.

Điều này giải thích tại sao:

- phản ứng tiến cho tới khi \(\Delta_rG=0\);
- pha chuyển đổi cho tới khi chemical potential bằng nhau;
- chất khuếch tán từ vùng có chemical potential cao sang thấp.

Một nguyên lý duy nhất đứng sau nhiều hiện tượng tưởng như tách rời.

> **Chuyển mạch:** Trong **Năng lượng tự do Gibbs — tiêu chuẩn nhiệt động ở nhiệt độ và áp suất không đổi**, **Sự cạnh tranh giữa enthalpy và entropy** tiếp nhận điểm tựa từ **G là tiêu chuẩn tối thiểu ở T và P không đổi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Năng lượng tự do chuẩn của phản ứng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sự cạnh tranh giữa enthalpy và entropy

Từ:

\[
\Delta G=\Delta H-T\Delta S
\]

có thể thấy bốn trường hợp định tính.

Nếu `ΔH < 0` và `ΔS > 0`, quá trình thường thuận lợi ở mọi nhiệt độ trong mô hình đơn giản khi dấu không đổi.

Nếu `ΔH > 0` và `ΔS < 0`, quá trình thường không thuận lợi.

Nếu hai đóng góp cạnh tranh, nhiệt độ có thể làm dấu `ΔG` thay đổi.

Nóng chảy là ví dụ điển hình:

\[
\Delta H_{fus}>0
\]

và:

\[
\Delta S_{fus}>0
\]

Tại nhiệt độ nóng chảy cân bằng:

\[
\Delta G_{fus}=0
\]

nên gần đúng:

\[
T_m=\frac{\Delta H_{fus}}{\Delta S_{fus}}
\]

nếu các đại lượng thay đổi không đáng kể trong khoảng xét.

> **Chuyển mạch:** Ở chặng này của **Năng lượng tự do Gibbs — tiêu chuẩn nhiệt động ở nhiệt độ và áp suất không đổi**, **Năng lượng tự do chuẩn của phản ứng** tiếp nhận điểm tựa từ **Sự cạnh tranh giữa enthalpy và entropy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Điều kiện không chuẩn và thương số phản ứng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Năng lượng tự do chuẩn của phản ứng

Có thể tính:

\[
\Delta G_{rxn}^\circ=\sum_p\nu_p\Delta G_{f,p}^\circ-\sum_r\nu_r\Delta G_{f,r}^\circ
\]

Tương tự enthalpy, **năng lượng tự do tạo thành chuẩn (standard Gibbs free energy of formation)** có thể dùng như dữ liệu tra bảng.

Các giá trị này phụ thuộc trạng thái chuẩn và nhiệt độ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Năng lượng tự do Gibbs — tiêu chuẩn nhiệt động ở nhiệt độ và áp suất không đổi**, **Điều kiện không chuẩn và thương số phản ứng** tiếp nhận điểm tựa từ **Năng lượng tự do chuẩn của phản ứng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Liên hệ với hằng số cân bằng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Điều kiện không chuẩn và thương số phản ứng

Động lực thực tế phụ thuộc thành phần hiện tại của hệ:

\[
\Delta G=\Delta G^\circ+RT\ln Q
\]

Trong đó `Q` là **thương số phản ứng (reaction quotient)** được xây từ hoạt độ.

Điều này rất quan trọng: một phản ứng có `ΔG° > 0` vẫn có thể tiến theo chiều thuận nếu thành phần hiện tại làm `Q` đủ nhỏ.

Ngược lại, một phản ứng có `ΔG° < 0` có thể bị đẩy theo chiều nghịch nếu sản phẩm tích tụ quá nhiều.

> **Chuyển mạch:** Trong **Năng lượng tự do Gibbs — tiêu chuẩn nhiệt động ở nhiệt độ và áp suất không đổi**, **Liên hệ với hằng số cân bằng** tiếp nhận điểm tựa từ **Điều kiện không chuẩn và thương số phản ứng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thế hóa học — Gibbs free năng lượng (energy / 에너지) trên mỗi lượng chất vi phân** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Liên hệ với hằng số cân bằng

Tại cân bằng:

\[
\Delta G=0,\qquad Q=K
\]

nên:

\[
\Delta G^\circ=-RT\ln K
\]

Đây là cầu nối trực tiếp giữa nhiệt động lực học và hóa học cân bằng.

`K` lớn tương ứng \(\Delta G^\circ\) âm; `K` nhỏ tương ứng \(\Delta G^\circ\) dương.

Nhưng `K` không cho biết tốc độ phản ứng.

> **Chuyển mạch:** Ở chặng này của **Năng lượng tự do Gibbs — tiêu chuẩn nhiệt động ở nhiệt độ và áp suất không đổi**, **Thế hóa học — Gibbs free năng lượng (energy / 에너지) trên mỗi lượng chất vi phân** tiếp nhận điểm tựa từ **Liên hệ với hằng số cân bằng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vì sao chất khuếch tán?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thế hóa học — Gibbs free năng lượng (energy / 에너지) trên mỗi lượng chất vi phân

Trong hỗn hợp:

\[
\mu_i=\left(\frac{\partial G}{\partial n_i}\right)_{T,P,n_{j\ne i}}
\]

Chemical potential cho biết Gibbs free năng lượng (energy / 에너지) thay đổi bao nhiêu khi thêm một lượng rất nhỏ cấu tử \(i\) trong điều kiện các biến khác phù hợp được giữ cố định.

Với khí/dung dịch lý tưởng:

\[
\mu_i=\mu_i^\circ+RT\ln a_i
\]

Trong đó \(a_i\) là hoạt độ.

Đây là nền tảng của:

- khuếch tán;
- cân bằng pha;
- cân bằng hóa học;
- điện hóa;
- thẩm thấu.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Năng lượng tự do Gibbs — tiêu chuẩn nhiệt động ở nhiệt độ và áp suất không đổi**, **Vì sao chất khuếch tán?** tiếp nhận điểm tựa từ **Thế hóa học — Gibbs free năng lượng (energy / 에너지) trên mỗi lượng chất vi phân** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thế điện hóa** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vì sao chất khuếch tán?

Nói “chất đi từ nơi nồng độ cao tới thấp” chỉ đúng trong trường hợp đơn giản.

Động lực sâu hơn là độ dốc (gradient / 기울기) của **thế hóa học**.

Một species có thể di chuyển từ vùng nồng độ thấp sang cao nếu các tương tác hoặc điện trường làm chemical potential ở vùng nồng độ thấp cao hơn.

Trong hệ có điện tích, cần dùng **thế điện hóa (electrochemical potential)** thay vì chỉ chemical potential.

> **Chuyển mạch:** Trong **Năng lượng tự do Gibbs — tiêu chuẩn nhiệt động ở nhiệt độ và áp suất không đổi**, **Thế điện hóa** tiếp nhận điểm tựa từ **Vì sao chất khuếch tán?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Gibbs free năng lượng (energy / 에너지) và công hữu ích cực đại** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thế điện hóa

Với ion điện tích \(z_i\):

\[
\tilde\mu_i=\mu_i+z_iF\phi
\]

Trong đó \(\phi\) là điện thế.

Cân bằng điện hóa yêu cầu thế điện hóa bằng nhau giữa các vùng có thể trao đổi ion.

Khái niệm này đứng sau:

- phương trình Nernst;
- membrane potential;
- pin điện hóa;
- vận chuyển ion qua màng.

> **Chuyển mạch:** Ở chặng này của **Năng lượng tự do Gibbs — tiêu chuẩn nhiệt động ở nhiệt độ và áp suất không đổi**, **Gibbs free năng lượng (energy / 에너지) và công hữu ích cực đại** tiếp nhận điểm tựa từ **Thế điện hóa** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Gibbs và cân bằng pha** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Gibbs free năng lượng (energy / 에너지) và công hữu ích cực đại

Ở nhiệt độ và áp suất không đổi, độ giảm Gibbs free năng lượng (energy / 에너지) đặt giới hạn trên cho **công không phải công giãn nở (non-PV work)** thu được trong quá trình thuận nghịch:

\[
w_{nonPV,max}=-\Delta G
\]

Trong pin điện hóa:

\[
\Delta G=-nFE
\]

Điện áp pin vì vậy là một biểu hiện trực tiếp của chênh lệch Gibbs free năng lượng (energy / 에너지) trên mỗi mol electron chuyển.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Năng lượng tự do Gibbs — tiêu chuẩn nhiệt động ở nhiệt độ và áp suất không đổi**, **Gibbs và cân bằng pha** tiếp nhận điểm tựa từ **Gibbs free năng lượng (energy / 에너지) và công hữu ích cực đại** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **G theo thành phần và tính ổn định của hỗn hợp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Gibbs và cân bằng pha

Hai pha \(\alpha\) và \(\beta\) ở cân bằng khi chemical potential của mỗi cấu tử bằng nhau:

\[
\mu_i^\alpha=\mu_i^\beta
\]

Đối với một chất tinh khiết, nhiệt độ nóng chảy là điểm mà:

\[
\mu_{solid}=\mu_{liquid}
\]

Nếu nhiệt độ thấp hơn điểm nóng chảy, pha rắn có chemical potential thấp hơn. Nếu cao hơn, pha lỏng thấp hơn.

Đây là cách nhiệt động giải thích chuyển pha mà không cần dùng câu “chất thích ở pha nào”.

> **Chuyển mạch:** Trong **Năng lượng tự do Gibbs — tiêu chuẩn nhiệt động ở nhiệt độ và áp suất không đổi**, **G theo thành phần và tính ổn định của hỗn hợp** tiếp nhận điểm tựa từ **Gibbs và cân bằng pha** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Spinodal và nucleation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## G theo thành phần và tính ổn định của hỗn hợp

Với hỗn hợp hai thành phần, có thể vẽ Gibbs free năng lượng (energy / 에너지) mol theo composition.

Nếu đường cong `G(x)` lồi phù hợp, hỗn hợp đồng nhất có thể ổn định.

Nếu có vùng lõm thích hợp, hệ có thể giảm G bằng cách tách thành hai pha có composition khác nhau.

Đường tiếp tuyến chung (**common tangent construction**) cho compositions cân bằng của hai pha.

Đây là nền tảng nhiệt động của:

- phase diagram;
- miscibility gap;
- spinodal decomposition;
- alloy phase separation.

> **Chuyển mạch:** Ở chặng này của **Năng lượng tự do Gibbs — tiêu chuẩn nhiệt động ở nhiệt độ và áp suất không đổi**, **Spinodal và nucleation** tiếp nhận điểm tựa từ **G theo thành phần và tính ổn định của hỗn hợp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Gibbs–Duhem** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Spinodal và nucleation

Trong một số vùng composition, pha đồng nhất chỉ metastable và cần tạo mầm để tách pha.

Trong vùng spinodal, độ cong của G theo composition có thể âm:

\[
\frac{d^2G}{dx^2}<0
\]

khi đó dao động composition nhỏ có thể tự lớn lên mà không cần vượt nucleation barrier thông thường.

Khái niệm này nối Gibbs free năng lượng (energy / 에너지) với materials science và phase transformation kinetics.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Năng lượng tự do Gibbs — tiêu chuẩn nhiệt động ở nhiệt độ và áp suất không đổi**, **Gibbs–Duhem** tiếp nhận điểm tựa từ **Spinodal và nucleation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hoạt độ và dung dịch không lý tưởng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Gibbs–Duhem

Trong hỗn hợp, chemical potentials không thể thay đổi hoàn toàn độc lập.

Quan hệ Gibbs–Duhem ở T, P cố định:

\[
\sum_i n_i d\mu_i=0
\]

Điều này phản ánh rằng nếu composition thay đổi làm chemical potential của một cấu tử tăng, các cấu tử khác phải thay đổi liên quan để Gibbs năng lượng (energy / 에너지) toàn hệ vẫn nhất quán.

Nó là nền tảng của nhiều mô hình hoạt độ và thermodynamic consistency.

> **Chuyển mạch:** Trong **Năng lượng tự do Gibbs — tiêu chuẩn nhiệt động ở nhiệt độ và áp suất không đổi**, **Hoạt độ và dung dịch không lý tưởng** tiếp nhận điểm tựa từ **Gibbs–Duhem** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Liên hệ với áp suất thẩm thấu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hoạt độ và dung dịch không lý tưởng

Với dung dịch thật:

\[
\mu_i=\mu_i^\circ+RT\ln a_i
\]

và:

\[
a_i=\gamma_i x_i
\]

hoặc dạng phù hợp với chuẩn nồng độ khác.

\(\gamma_i\) là **hệ số hoạt độ (activity coefficient)** mô tả độ lệch khỏi ideality.

Nếu tương tác A–B khác mạnh A–A/B–B, Gibbs mixing không còn chỉ là entropy trộn lý tưởng.

Đây là nguồn của:

- azeotrope;
- phase separation;
- activity correction;
- salt effects.

> **Chuyển mạch:** Ở chặng này của **Năng lượng tự do Gibbs — tiêu chuẩn nhiệt động ở nhiệt độ và áp suất không đổi**, **Liên hệ với áp suất thẩm thấu** tiếp nhận điểm tựa từ **Hoạt độ và dung dịch không lý tưởng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Liên hệ với hóa sinh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Liên hệ với áp suất thẩm thấu

Thẩm thấu cũng có thể hiểu từ chemical potential của dung môi.

Chất tan làm chemical potential của dung môi giảm. Dung môi tinh khiết có xu hướng đi qua màng bán thấm về phía dung dịch cho tới khi chênh lệch áp suất bù chênh chemical potential.

Với dung dịch loãng lý tưởng:

\[
\pi\approx iCRT
\]

Đây không phải một định luật tách biệt; nó là hệ quả của cân bằng chemical potential.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Năng lượng tự do Gibbs — tiêu chuẩn nhiệt động ở nhiệt độ và áp suất không đổi**, **Liên hệ với hóa sinh** tiếp nhận điểm tựa từ **Liên hệ với áp suất thẩm thấu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Nồng độ trong tế bào làm ΔG khác ΔG°'** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Liên hệ với hóa sinh

Tế bào thúc đẩy những quá trình không thuận lợi bằng **ghép cặp phản ứng (reaction coupling)** với phản ứng thuận lợi mạnh như thủy phân ATP.

Điều kiện là tổng Gibbs free năng lượng (energy / 에너지):

\[
\Delta G_{total}=\sum_i\Delta G_i
\]

phải âm.

ATP không “giải phóng năng lượng vì phá một liên kết cao năng”. Phá liên kết luôn cần năng lượng; sự thuận lợi của thủy phân đến từ chênh lệch toàn bộ trạng thái chất phản ứng và sản phẩm, gồm:

- cộng hưởng;
- solvat hóa;
- giảm repulsion;
- entropy.

> **Chuyển mạch:** Trong **Năng lượng tự do Gibbs — tiêu chuẩn nhiệt động ở nhiệt độ và áp suất không đổi**, **Nồng độ trong tế bào làm ΔG khác ΔG°'** tiếp nhận điểm tựa từ **Liên hệ với hóa sinh** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Gibbs free năng lượng (energy / 에너지) và reaction coordinate** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nồng độ trong tế bào làm ΔG khác ΔG°'

Trong sinh hóa, trạng thái chuẩn biến đổi thường dùng `ΔG°'` với pH quy ước.

Nhưng trong tế bào:

\[
\Delta G=\Delta G^{\circ'}+RT\ln Q
\]

Do ATP/ADP/Pi không ở nồng độ chuẩn, Gibbs free năng lượng (energy / 에너지) thủy phân ATP trong tế bào có thể âm hơn đáng kể so với giá trị chuẩn.

Điều này cho thấy **nồng độ thật là một phần của năng lượng khả dụng**.

> **Chuyển mạch:** Ở chặng này của **Năng lượng tự do Gibbs — tiêu chuẩn nhiệt động ở nhiệt độ và áp suất không đổi**, **Gibbs free năng lượng (energy / 에너지) và reaction coordinate** tiếp nhận điểm tựa từ **Nồng độ trong tế bào làm ΔG khác ΔG°'** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Gibbs free năng lượng (energy / 에너지) khác hàng rào hoạt hóa** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Gibbs free năng lượng (energy / 에너지) và reaction coordinate

Nếu mô tả phản ứng bằng tọa độ tiến triển \(\xi\):

\[
\left(\frac{\partial G}{\partial \xi}\right)_{T,P}=\Delta_rG
\]

Nếu:

\[
\Delta_rG<0
\]

G giảm khi phản ứng tiến thuận.

Nếu:

\[
\Delta_rG>0
\]

G giảm khi phản ứng đi nghịch.

Tại cân bằng:

\[
\Delta_rG=0
\]

Đây là cách hình học rất trực quan để nối reaction quotient với minimization của G.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Năng lượng tự do Gibbs — tiêu chuẩn nhiệt động ở nhiệt độ và áp suất không đổi**, **Gibbs free năng lượng (energy / 에너지) khác hàng rào hoạt hóa** tiếp nhận điểm tựa từ **Gibbs free năng lượng (energy / 에너지) và reaction coordinate** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Nhiệt độ làm Gibbs thay đổi như thế nào?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Gibbs free năng lượng (energy / 에너지) khác hàng rào hoạt hóa

Trên sơ đồ phản ứng có hai loại độ cao:

- chênh lệch giữa đầu và cuối → \(\Delta G\);
- chênh lệch từ trạng thái đầu tới chuyển tiếp (transition / 전이) trạng thái (state / 상태) → \(\Delta G^\ddagger\).

`ΔG` quyết định hướng thermodynamic.

`ΔG‡` quyết định tốc độ theo transition-state lý thuyết (theory / 이론).

Một phản ứng có thể:

```text
ΔG rất âm
nhưng ΔG‡ rất lớn
→ thuận lợi nhưng chậm
```

Đây là phân biệt quan trọng nhất giữa thermodynamics và kinetics.

> **Chuyển mạch:** Trong **Năng lượng tự do Gibbs — tiêu chuẩn nhiệt động ở nhiệt độ và áp suất không đổi**, **Nhiệt độ làm Gibbs thay đổi như thế nào?** tiếp nhận điểm tựa từ **Gibbs free năng lượng (energy / 에너지) khác hàng rào hoạt hóa** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Áp suất làm Gibbs thay đổi như thế nào?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nhiệt độ làm Gibbs thay đổi như thế nào?

Từ:

\[
\left(\frac{\partial G}{\partial T}\right)_P=-S
\]

G giảm theo nhiệt độ với độ dốc bằng âm entropy.

Pha có entropy cao hơn có đường G giảm nhanh hơn khi T tăng. Đây là cách hình học để hiểu tại sao liquid có thể trở nên ổn định hơn solid ở nhiệt độ cao.

> **Chuyển mạch:** Ở chặng này của **Năng lượng tự do Gibbs — tiêu chuẩn nhiệt động ở nhiệt độ và áp suất không đổi**, **Áp suất làm Gibbs thay đổi như thế nào?** tiếp nhận điểm tựa từ **Nhiệt độ làm Gibbs thay đổi như thế nào?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phương trình Clapeyron** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Áp suất làm Gibbs thay đổi như thế nào?

Từ:

\[
\left(\frac{\partial G}{\partial P}\right)_T=V
\]

Pha có thể tích mol lớn hơn có G tăng nhanh hơn khi áp suất tăng.

Do đó áp suất cao thường ưu tiên pha có thể tích nhỏ hơn, dù chi tiết còn phụ thuộc cấu trúc.

Đây là cơ sở trực giác cho ảnh hưởng áp suất lên chuyển pha.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Năng lượng tự do Gibbs — tiêu chuẩn nhiệt động ở nhiệt độ và áp suất không đổi**, **Phương trình Clapeyron** tiếp nhận điểm tựa từ **Áp suất làm Gibbs thay đổi như thế nào?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Năng lượng tự do và khả năng sinh công** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phương trình Clapeyron

Từ điều kiện cân bằng hai pha có thể suy ra:

\[
\frac{dP}{dT}=\frac{\Delta S}{\Delta V}=\frac{\Delta H}{T\Delta V}
\]

Đây là **phương trình Clapeyron** mô tả độ dốc đường cân bằng pha trên giản đồ P–T.

Với vaporization và giả định khí lý tưởng, nó dẫn tới phương trình Clausius–Clapeyron gần đúng.

> **Chuyển mạch:** Trong **Năng lượng tự do Gibbs — tiêu chuẩn nhiệt động ở nhiệt độ và áp suất không đổi**, **Năng lượng tự do và khả năng sinh công** tiếp nhận điểm tựa từ **Phương trình Clapeyron** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Liên hệ với exergy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Năng lượng tự do và khả năng sinh công

Gibbs free năng lượng (energy / 에너지) không phải “năng lượng tự do nằm sẵn trong phân tử”.

Nó là một thế nhiệt động cho biết mức công không-PV tối đa có thể trích ra **nếu quá trình diễn ra thuận nghịch ở T, P xác định**.

Trong quá trình thật không thuận nghịch, công thực tế luôn nhỏ hơn giới hạn này.

> **Chuyển mạch:** Ở chặng này của **Năng lượng tự do Gibbs — tiêu chuẩn nhiệt động ở nhiệt độ và áp suất không đổi**, **Liên hệ với exergy** tiếp nhận điểm tựa từ **Năng lượng tự do và khả năng sinh công** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Các hiểu lầm thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Liên hệ với exergy

**Khả năng sinh công (exergy)** mở rộng ý tưởng này bằng cách so trạng thái hệ với môi trường tham chiếu.

Gibbs free năng lượng (energy / 에너지) đặc biệt liên quan tới chemical exergy trong hệ ở T/P môi trường cố định.

Trong kỹ thuật, mất exergy gắn với entropy generation và irreversibility.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Năng lượng tự do Gibbs — tiêu chuẩn nhiệt động ở nhiệt độ và áp suất không đổi**, **Các hiểu lầm thường gặp** tiếp nhận điểm tựa từ **Liên hệ với exergy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Các hiểu lầm thường gặp

### “ΔG âm nghĩa là phản ứng nhanh”

Sai. Hàng rào hoạt hóa thuộc động học hóa học.

### “ΔG° chính là ΔG thực tế”

Chỉ đúng khi hệ ở các điều kiện trạng thái chuẩn thích hợp. Trong điều kiện thực, thành phần và hoạt độ làm `ΔG` thay đổi.

### “Năng lượng tự do là phần năng lượng hoàn toàn tự do”

Không. Đây là một thế nhiệt động có định nghĩa chính xác, không phải một kho năng lượng thông thường.

### “Khi ΔG = 0 thì mọi phản ứng dừng hẳn”

Không. Ở cân bằng động, forward và reverse reaction vẫn diễn ra nhưng tốc độ ròng bằng 0.

### “Chemical potential chỉ là nồng độ”

Không. Nó phụ thuộc composition, tương tác, áp suất, nhiệt độ và với ion còn có điện thế.

### “Pha ổn định là pha có enthalpy thấp nhất”

Không nhất thiết. Ở nhiệt độ hữu hạn, entropy đóng góp qua `-TS`, nên pha có enthalpy cao hơn vẫn có thể có G thấp hơn.

> **Chuyển mạch:** Trong **Năng lượng tự do Gibbs — tiêu chuẩn nhiệt động ở nhiệt độ và áp suất không đổi**, **Mô hình tư duy** gom các mảnh từ **Các hiểu lầm thường gặp** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

Năng lượng tự do Gibbs giống **địa hình nhiệt động của hệ ở nhiệt độ và áp suất không đổi**. Reaction, diffusion và phase chuyển tiếp (transition / 전이) đều có thể hiểu như quá trình hệ tìm đường giảm G. Chemical potential là độ dốc cục bộ của địa hình đối với từng species; equilibrium là trạng thái không còn hướng nào làm G giảm dưới các ràng buộc hiện có. Kinetics quyết định hệ có đi được xuống địa hình đó nhanh hay bị mắc sau một hàng rào cao.

Xem tiếp: [Nhiệt động lực học hóa học](./04_chemical_thermodynamics.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
