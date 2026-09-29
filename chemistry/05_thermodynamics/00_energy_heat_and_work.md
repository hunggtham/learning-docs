# Năng lượng, nhiệt và công — nền tảng hạch toán của nhiệt động lực học

> **Mạch đọc:** Đọc **Năng lượng, nhiệt và công — nền tảng hạch toán của nhiệt động lực học** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **“Nhiệt là chất được chứa trong vật”** sang **“Temperature cao nghĩa total năng lượng (energy / 에너지) cao hơn mọi vật lạnh hơn”**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


> **Nhiệt động lực học (thermodynamics / 열역학)** nghiên cứu trạng thái năng lượng của hệ, cách năng lượng truyền qua ranh giới và những ràng buộc quyết định chiều biến đổi. Trong Hóa học, nhiệt động lực học trả lời “trạng thái nào thuận lợi?” và “năng lượng được phân bố ra sao?”, nhưng không tự cho biết quá trình xảy ra nhanh đến mức nào.

Chương này xây nền cho toàn bộ phần sau. Nếu các khái niệm **hệ, trạng thái, nội năng, nhiệt, công và định luật thứ nhất** chưa rõ, entropy và Gibbs sẽ rất dễ trở thành các công thức phải học thuộc.

# Chọn hệ trước khi viết phương trình

**Hệ (system / 계)** là phần thế giới ta chọn để phân tích. Phần còn lại là **môi trường (surroundings / 주위)**. Ranh giới giữa hai phần có thể là vật lý thật như thành bình hoặc chỉ là ranh giới tưởng tượng.

Cùng một thí nghiệm có thể được hạch toán khác nhau tùy hệ được chọn.

Ví dụ phản ứng trong bình chứa nước:

```text
chọn reaction mixture làm hệ
→ nước + calorimeter là môi trường

chọn toàn calorimeter làm hệ
→ cách viết q và boundary thay đổi
```

Định luật vật lý không đổi; chỉ bookkeeping thay đổi.

# Hệ mở, kín và cô lập

**Hệ mở (open system)** trao đổi cả vật chất và năng lượng.

**Hệ kín (closed system)** không trao đổi vật chất nhưng có thể trao đổi năng lượng.

**Hệ cô lập (isolated system)** lý tưởng không trao đổi cả vật chất lẫn năng lượng.

Phòng thí nghiệm thực chỉ gần đúng các loại này. Bình cách nhiệt vẫn mất một ít nhiệt; bình kín vẫn có thể truyền nhiệt qua thành.

Nhận biết mức xấp xỉ là một phần của modeling.

# Trạng thái nhiệt động

Một **trạng thái (thermodynamic state)** được xác định bằng các biến như:

\[
T,P,V,n_i
\]

và composition.

Một biến trạng thái chỉ cần biết giá trị hiện tại, không cần biết hệ đã đi đường nào để tới đó.

Các đại lượng như:

- nội năng \(U\);
- enthalpy \(H\);
- entropy \(S\);
- Gibbs free năng lượng (energy / 에너지) \(G\);

là **hàm trạng thái (state functions)**.

# Nội năng là gì?

**Nội năng (internal energy, \(U\) / 내부 에너지)** là tổng năng lượng vi mô thuộc các degree of freedom bên trong hệ.

Nó có thể bao gồm:

- chuyển động tịnh tiến;
- quay;
- dao động;
- electronic năng lượng (energy / 에너지);
- intermolecular interactions;
- chemical bonding;
- trong phạm vi rộng hơn, nuclear contributions.

Ta thường không đo absolute U. Điều quan trọng là:

\[
\Delta U=U_2-U_1
\]

Nhiệt động lực học được xây chủ yếu trên **chênh lệch trạng thái**, vì mốc zero tuyệt đối của nhiều dạng năng lượng không cần biết để dự đoán biến đổi.

# Nhiệt không phải năng lượng “nằm trong vật”

**Nhiệt (heat, \(q\) / 열)** là năng lượng truyền qua ranh giới (boundary / 경계) **do chênh lệch nhiệt độ**.

Khi hai vật có temperature khác nhau tiếp xúc, năng lượng (energy / 에너지) transfer từ hot tới cold được gọi là heat transfer cho tới khi thermal equilibrium thiết lập.

Sau khi năng lượng (energy / 에너지) đã vào hệ, ta không thể chỉ vào một subset molecules và nói “đây là nhiệt”. năng lượng (energy / 에너지) đã trở thành phần của nội bộ (internal / 내부) năng lượng (energy / 에너지) phân phối (distribution / 분포).

Vì vậy câu:

> vật chứa 500 J nhiệt

không chính xác bằng:

> hệ nhận 500 J dưới dạng nhiệt trong quá trình này.

# Công là năng lượng truyền có tổ chức

**Công (work, \(w\) / 일)** là năng lượng (energy / 에너지) transfer liên quan một generalized force tác dụng qua displacement/generalized coordinate.

Trong Hóa học thường gặp:

- công áp suất–thể tích;
- công điện;
- công bề mặt;
- công kéo/đàn hồi;
- công từ trường trong specialized các hệ thống (systems / 시스템들).

Nhiệt và công đều là **cách năng lượng (energy / 에너지) đi qua ranh giới (boundary / 경계)**, không phải trạng thái (state / 상태) properties.

# Định luật thứ nhất

Với quy ước dấu thường dùng trong Hóa học:

\[
\Delta U=q+w
\]

Trong đó:

```text
q > 0 → hệ nhận nhiệt
q < 0 → hệ tỏa nhiệt
w > 0 → môi trường làm công lên hệ
w < 0 → hệ làm công lên môi trường
```

Đây chỉ là conservation of năng lượng (energy / 에너지) viết cho hệ.

Nếu hệ mất 100 J nhiệt nhưng môi trường làm 40 J công lên hệ:

\[
\Delta U=-100+40=-60\;J
\]

Nội bộ (internal / 내부) năng lượng (energy / 에너지) giảm 60 J.

# Công giãn nở PV

Khi hệ giãn nở chống bên ngoài (external / 외부) pressure:

\[
w=-\int P_{ext}\,dV
\]

Nếu \(P_{ext}\) constant:

\[
w=-P_{ext}\Delta V
\]

Gas expansion có \(\Delta V>0\), nên \(w<0\): hệ truyền năng lượng (energy / 에너지) ra surroundings dưới dạng công việc (work / 작업).

Compression có \(\Delta V<0\), nên \(w>0\): surroundings làm công việc (work / 작업) lên hệ thống (system / 시스템).

# Vì sao dùng bên ngoài (external / 외부) pressure?

Mechanical công việc (work / 작업) ở ranh giới (boundary / 경계) phụ thuộc lực bên ngoài mà hệ thực sự đẩy chống lại.

Trong irreversible expansion, hệ thống (system / 시스템) pressure có thể không uniform hoặc không equal \(P_{ext}\). Vì vậy công việc (work / 작업) đường dẫn (path / 경로) được tính từ ranh giới (boundary / 경계) điều kiện (condition / 조건) thực tế, không phải chỉ từ initial/final pressures.

Đây là ví dụ đầu tiên cho việc công việc (work / 작업) là **path-dependent**.

# Free expansion

Nếu gas giãn vào vacuum:

\[
P_{ext}=0
\]

nên:

\[
w=0
\]

mặc dù volume tăng mạnh.

Nếu cùng initial/final states nhưng gas giãn reversible chống pressure gần bằng hệ thống (system / 시스템) pressure ở từng bước, magnitude công việc (work / 작업) có thể lớn hơn.

Cùng \(\Delta U\), nhưng q và w khác theo đường dẫn (path / 경로).

# Hàm trạng thái và đường dẫn (path / 경로) functions

Nếu đi từ A tới B:

\[
\Delta U_{A\to B}
\]

luôn giống nhau cho mọi đường dẫn (path / 경로).

Nhưng:

\[
q_{path1}\ne q_{path2}
\]

và:

\[
w_{path1}\ne w_{path2}
\]

trong general trường hợp (case / 사례).

Vì:

\[
q+w=\Delta U
\]

thay đổi công việc (work / 작업) đường dẫn (path / 경로) buộc heat exchange thay đổi tương ứng.

Đây là lý do ký hiệu vi phân thường viết:

\[
dU
\]

cho trạng thái (state / 상태) hàm (function / 함수), nhưng:

\[
\delta q,\;\delta w
\]

cho path-dependent transfers trong notation chặt chẽ.

# Quá trình thuận nghịch và không thuận nghịch

Một **quá trình thuận nghịch (reversible process)** là ideal limiting đường dẫn (path / 경로) đi qua chuỗi trạng thái infinitesimally close to equilibrium, có thể đảo chiều bằng perturbation vô cùng nhỏ mà không để lại net thay đổi (change / 변경) cho universe.

Không có tiến trình (process / 프로세스) thực hoàn toàn reversible; đây là tham chiếu (reference / 참조) đường dẫn (path / 경로).

Reversible expansion cho maximum công việc (work / 작업) đầu ra (output / 출력) giữa hai equilibrium states dưới điều kiện phù hợp.

Irreversibility xuất hiện từ:

- finite temperature gradients;
- friction;
- uncontrolled expansion;
- mixing;
- diffusion;
- chemical reaction with finite affinity.

Entropy môi trường vận hành (production / 운영 환경) ở chương sau định lượng hướng này.

# Nhiệt độ khác tổng năng lượng

Một cốc nước 90 °C có temperature cao hơn bồn nước 40 °C, nhưng bồn lớn có thể có total nội bộ (internal / 내부) năng lượng (energy / 에너지) lớn hơn rất nhiều.

Temperature là intensive variable phản ánh statistical năng lượng (energy / 에너지) phân phối (distribution / 분포) và equilibrium điều kiện (condition / 조건), không phải “lượng nhiệt chứa trong vật”.

# Định luật thứ không

Nếu A cân bằng nhiệt với B, và B cân bằng nhiệt với C, thì A cân bằng nhiệt với C.

**Định luật thứ không (zeroth law)** làm temperature trở thành đại lượng có thể so sánh transitive và tạo nền cho thermometer.

Thermometer hoạt động vì nó tiến tới thermal equilibrium với vật đo và có một thuộc tính (property / 속성) calibrated theo T.

# Nhiệt dung

**Nhiệt dung (heat capacity)** ở ràng buộc (constraint / 제약조건) cụ thể:

\[
C=\frac{\delta q}{dT}
\]

Ta thường phân biệt:

\[
C_V=\left(\frac{\partial U}{\partial T}\right)_V
\]

và:

\[
C_P=\left(\frac{\partial H}{\partial T}\right)_P
\]

trong các hệ phù hợp.

Với một mẫu đơn giản trong interval nhỏ:

\[
q=mc\Delta T
\]

với \(c\) là specific heat sức chứa (capacity / 용량).

# Vì sao Cp và Cv khác nhau?

Khi heating ở constant volume, hệ thống (system / 시스템) không làm PV expansion công việc (work / 작업).

Ở constant pressure, heating thường làm volume tăng và một phần năng lượng (energy / 에너지) đầu vào (input / 입력) liên quan expansion. Với ideal gas:

\[
C_P-C_V=R
\]

trên mol basis.

Đây là liên kết (connection / 연결) giữa microscopic năng lượng (energy / 에너지) lưu trữ (storage / 저장소) và macroscopic công việc (work / 작업).

# Equipartition — một trực giác thống kê

Trong classical limit, mỗi quadratic degree of freedom đóng góp average năng lượng (energy / 에너지) khoảng:

\[
\frac12k_BT
\]

per molecule.

Translational, rotational và vibrational modes vì thế ảnh hưởng heat sức chứa (capacity / 용량).

Nhưng quantum năng lượng (energy / 에너지) spacing làm một số modes “đóng băng” ở low temperature. Do đó heat sức chứa (capacity / 용량) thay đổi theo T và classical equipartition không đúng universal.

# Calorimetry

**Nhiệt lượng kế (calorimetry / 열량 측정법)** suy năng lượng (energy / 에너지) transfer từ temperature thay đổi (change / 변경) của một calibrated thermal mass.

Nếu calorimeter gần isolated:

\[
q_{reaction}+q_{calorimeter}=0
\]

và:

\[
q_{calorimeter}=C_{cal}\Delta T
\]

nên:

\[
q_{reaction}=-C_{cal}\Delta T
\]

Trong real experiment, cần tính cả vessel, solution, thermometer và heat mất mát (loss / 손실) nếu độ chính xác yêu cầu cao.

# Bomb calorimeter

Bomb calorimeter hoạt động gần constant volume.

Nếu only PV công việc (work / 작업) relevant:

\[
q_V=\Delta U
\]

Reaction xảy ra trong sealed rigid vessel, nên volume công việc (work / 작업) gần zero.

Đây là cách đo combustion internal-energy changes chính xác.

# Coffee-cup calorimeter

Calorimeter mở ở atmospheric pressure gần constant P.

Khi only PV công việc (work / 작업) relevant:

\[
q_P=\Delta H
\]

Do đó chemistry thường thích enthalpy vì lab reactions hay diễn ra gần constant pressure.

# Nhiệt lượng kế không đo “nhiệt của phân tử” trực tiếp

Ta đo temperature thay đổi (change / 변경) và dùng mô hình (model / 모델) heat sức chứa (capacity / 용량) để suy q.

Nếu heat sức chứa (capacity / 용량) thay đổi với temperature hoặc reaction không hoàn toàn, interpretation phải điều chỉnh.

Calorimetry luôn là một **inverse bài toán (problem / 문제)** từ observable \(\Delta T\) tới năng lượng (energy / 에너지) transfer.

# Open các hệ thống (systems / 시스템들) và enthalpy luồng (flow / 흐름)

Trong hệ thống (system / 시스템) có mass luồng (flow / 흐름), vật chất mang theo nội bộ (internal / 내부) năng lượng (energy / 에너지) và PV luồng (flow / 흐름) công việc (work / 작업). Điều này làm **enthalpy** xuất hiện tự nhiên trong steady-flow năng lượng (energy / 에너지) balances.

Một simplified steady-flow balance:

\[
\dot Q-\dot W_s
+\sum_{in}\dot n_i h_i
-\sum_{out}\dot n_i h_i=0
\]

khi bỏ kinetic/potential changes.

Đây là cầu nối từ basic thermodynamics sang chemical kỹ thuật (engineering / 엔지니어링).

# Năng lượng (energy / 에너지) conservation không cho direction

First law cho phép cả:

```text
hot → cold
```

và hypothetical:

```text
cold → hot
```

nếu chỉ yêu cầu total năng lượng (energy / 에너지) conserved.

Nhưng tự nhiên chỉ tự xảy ra theo một direction nếu không có bên ngoài (external / 외부) công việc (work / 작업).

Direction cần **second law và entropy**.

Vì vậy first law là necessary nhưng không sufficient để dự đoán spontaneity.

# Năng lượng (energy / 에너지) trong chemical bonds — tránh câu “bond chứa năng lượng” quá đơn giản

Một bond bền là một trạng thái có năng lượng (energy / 에너지) thấp hơn separated fragments theo tham chiếu (reference / 참조) phù hợp.

Phá bond cần năng lượng (energy / 에너지).

Reaction tỏa nhiệt khi năng lượng (energy / 에너지) giải phóng từ forming new interactions lớn hơn năng lượng (energy / 에너지) cần để phá old interactions và reorganize hệ thống (system / 시스템).

Do đó câu:

> phá bond giải phóng năng lượng

thường sai nếu nói về isolated bond cleavage.

# Biology — ATP và năng lượng (energy / 에너지) transfer

ATP hydrolysis thuận lợi không phải vì “phá phosphate bond giải phóng năng lượng (energy / 에너지)”. Breaking bond itself requires năng lượng (energy / 에너지).

Net reaction favorable do combination của:

- products resonance stabilization;
- electrostatic relief;
- hydration/solvation;
- entropy;
- concentrations in cell.

Biochemistry vẫn tuân cùng first-law bookkeeping như combustion hoặc electrochemistry.

# Battery — chemical năng lượng (energy / 에너지) thành electrical công việc (work / 작업)

Trong electrochemical cell, năng lượng (energy / 에너지) có thể qua ranh giới (boundary / 경계) dưới dạng electrical công việc (work / 작업) thay vì chỉ heat/PV công việc (work / 작업).

Ở reversible conditions, maximum non-PV công việc (work / 작업) liên hệ Gibbs free năng lượng (energy / 에너지):

\[
w_{elec,max}=-\Delta G
\]

Điều này sẽ được phát triển ở electrochemistry.

# Những hiểu lầm thường gặp

### “Nhiệt là chất được chứa trong vật”

Không. Nhiệt là chế độ (mode / 모드) of năng lượng (energy / 에너지) transfer do temperature difference.

### “Temperature cao nghĩa total năng lượng (energy / 에너지) cao hơn mọi vật lạnh hơn”

Không. Total năng lượng (energy / 에너지) còn phụ thuộc amount và degrees of freedom.

### “q và w là trạng thái (state / 상태) functions”

Không. Chúng phụ thuộc đường dẫn (path / 경로).

### “Expansion luôn làm công việc (work / 작업) như nhau nếu ΔV giống nhau”

Không. công việc (work / 작업) phụ thuộc external-pressure đường dẫn (path / 경로).

### “Conservation of năng lượng (energy / 에너지) cho biết tiến trình (process / 프로세스) tự xảy ra chiều nào”

Không. Cần second law.

## Mô hình tư duy

Hãy xem thermodynamics đầu tiên như một **ledger có ranh giới (boundary / 경계) rõ ràng**:

```text
trạng thái hệ → U
energy qua boundary vì ΔT → q
energy qua boundary do generalized force → w
conservation → ΔU = q + w
```

Sau đó enthalpy, entropy và Gibbs không thay ledger này; chúng xây thêm các trạng thái (state / 상태) functions phù hợp với những các ràng buộc (constraints / 제약조건들) khác nhau để trả lời những câu hỏi khó hơn.

Xem tiếp: [Enthalpy và nhiệt hóa học](./01_enthalpy_and_thermochemistry.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 enthalpy and thermochemistry](./01_enthalpy_and_thermochemistry.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
