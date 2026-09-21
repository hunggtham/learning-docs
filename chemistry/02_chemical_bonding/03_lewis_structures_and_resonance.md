# Cấu trúc Lewis và cộng hưởng — hạch toán electron trước khi đi sâu vào lượng tử

> **Cấu trúc Lewis (Lewis structure / 루이스 구조)** là mô hình hạch toán electron hóa trị. Nó giúp trả lời nhanh nguyên tử nào nối với nguyên tử nào, có bao nhiêu cặp electron liên kết, cặp electron không liên kết và điện tích hình thức. Lewis không phải ảnh chụp mật độ electron thật; nó là một lớp mô hình đơn giản hóa cực kỳ hữu ích trước khi chuyển sang VSEPR, liên kết hóa trị và obitan phân tử.

Nếu một người quên gần hết Hóa phổ thông, nên xem Lewis như **sổ kế toán electron**: trước khi hỏi phân tử có hình gì hay phản ứng ra sao, ta cần biết tổng electron hóa trị đã được phân bố nhất quán hay chưa.

# Bước 1 — đếm tổng electron hóa trị

Với phân tử trung hòa, cộng electron hóa trị của tất cả nguyên tử.

Với ion âm, cộng thêm electron theo độ lớn điện tích. Với ion dương, trừ electron.

Ví dụ \(CO_2\):

\[
4+2(6)=16\;e^-
\]

Ví dụ \(NO_3^-\):

\[
5+3(6)+1=24\;e^-
\]

Sai ngay bước đếm electron sẽ làm mọi bước sau sai, nên đây là checkpoint đầu tiên.

# Bước 2 — chọn khung nguyên tử

Nguyên tử ít âm điện hơn thường nằm ở trung tâm, ngoại trừ H gần như luôn ở đầu mút vì chỉ tạo một liên kết thông thường.

Ví dụ:

```text
CO2  → O–C–O
NH3  → H–N–H với H thứ ba gắn N
H2O  → H–O–H
```

Công thức phân tử không tự nói topology. Với cùng công thức có thể có nhiều constitutional isomers, vì vậy lựa chọn connectivity đôi khi cần kiến thức hóa học bổ sung.

# Bước 3 — tạo liên kết đơn và hoàn thiện shell đầu mút

Mỗi liên kết đơn dùng hai electron. Sau khi tạo skeleton, phân bố electron còn lại để các nguyên tử đầu mút đạt cấu hình bền hợp lý.

Với nguyên tố chu kỳ 2, quy tắc octet thường là guide tốt:

```text
C, N, O, F → thường hướng tới 8 electron valence quanh nguyên tử
H          → duet, tức 2 electron
```

Nhưng octet là heuristic, không phải nguyên lý lượng tử tuyệt đối.

# Bước 4 — xử lý electron còn lại ở nguyên tử trung tâm

Nếu sau khi hoàn thiện terminal atoms vẫn còn electron, đặt chúng lên central atom thành lone pairs.

Nếu central atom thiếu octet và terminal atom có lone pair phù hợp, một lone pair có thể được chuyển thành multiple bond.

Ví dụ CO₂ cuối cùng được biểu diễn:

```text
O=C=O
```

thay vì O–C–O với charge separation lớn.

# Điện tích hình thức — công cụ xếp hạng cấu trúc

**Điện tích hình thức (formal charge / 형식 전하)**:

\[
FC=V-N-\frac{B}{2}
\]

trong đó:

- \(V\): electron hóa trị của nguyên tử tự do;
- \(N\): electron không liên kết;
- \(B\): electron trong các liên kết.

Một cấu trúc thường hợp lý hơn khi:

- tổng formal charge đúng bằng charge tổng;
- độ lớn charge separation nhỏ;
- negative charge nằm trên atom electronegative hơn khi các lựa chọn khác tương đương.

Nhưng formal charge vẫn là bookkeeping convention. Nó không bằng partial charge thật từ electron density.

# Ví dụ: CO₂ và charge separation

Một cấu trúc cực đoan:

```text
⁻O–C≡O⁺
```

có thể thỏa electron count, nhưng tạo charge separation. Cấu trúc:

```text
O=C=O
```

có formal charges bằng 0 trên cả ba atoms và phù hợp hơn với symmetry cũng như bonding.

Điểm quan trọng là Lewis structure không chỉ được chọn bằng octet; formal charge và chemical plausibility cùng tham gia.

# Quy tắc octet và vì sao nó hữu ích

Nguyên tố chu kỳ 2 chỉ có valence shell gồm 2s và 2p, nên cấu hình closed-shell với tám electron quanh atom thường đặc biệt ổn định.

Đây là nguồn gốc hóa học của octet rule.

Tuy nhiên ba nhóm ngoại lệ phải được hiểu sớm.

## Hệ thiếu electron

\(BF_3\) có B chỉ được sáu electron trong cấu trúc Lewis đơn giản. Boron electron-deficient nên \(BF_3\) là Lewis acid mạnh và có thể nhận electron pair từ NH₃:

\[
BF_3+NH_3\rightarrow F_3B\leftarrow NH_3
\]

Ngoại lệ octet ở đây trực tiếp giải thích reactivity.

## Species có số electron lẻ

\(NO\) có tổng electron valence lẻ nên không thể ghép tất cả thành pairs.

Các **gốc tự do (radicals / 라디칼)** thường có electron độc thân và có chemistry rất khác closed-shell molecules.

## Hệ siêu hóa trị

Các species như \(PF_5\), \(SF_6\), \(XeF_4\) không nên được giải thích đơn giản bằng câu “nguyên tử trung tâm dùng d orbital để mở rộng octet”.

Mô tả hiện đại thường dùng bonding đa tâm, ionic resonance contributors và MO delocalization. Lewis expanded-octet drawings vẫn hữu ích cho bookkeeping nhưng không phải literal orbital picture.

# Cộng hưởng — khi một hình Lewis không đủ

Nếu nhiều Lewis structures có cùng skeleton nhưng khác vị trí electron, ta có **cấu trúc cộng hưởng (resonance contributors / 공명 구조)**.

Ví dụ nitrate:

```text
 O            O⁻           O⁻
 ||            |            |
N–O⁻   ↔    O=N–O⁻  ↔   O⁻–N=O
 |
O⁻
```

Ba contributors tương đương về symmetry.

Phân tử thật **không nhảy qua lại** giữa ba hình. Electron density thật delocalized trên toàn nhóm \(NO_3^-\).

# Resonance hybrid và dữ liệu thực nghiệm

Nếu một contributor với N=O và hai N–O đơn là literal structure, ta kỳ vọng một bond ngắn khác hai bond dài.

Thực nghiệm cho ba N–O gần tương đương. Điều này phù hợp **lai cộng hưởng (resonance hybrid)**, trong đó bond order được phân bố trên nhiều liên kết.

Resonance vì thế không chỉ là cách vẽ đẹp hơn; nó giải thích bond length, charge distribution và stability.

# Bậc liên kết trung bình

Với carbonate \(CO_3^{2-}\), một double-bond contribution được chia cho ba C–O tương đương. Average bond order gần:

\[
BO\approx\frac{4}{3}
\]

Con số này không nghĩa có “1.333 thanh liên kết”. Nó mô tả tính chất trung gian của electron density và correlation với bond length/strength.

# Contributors không đóng góp bằng nhau trong mọi hệ

Nếu resonance contributors không tương đương, chúng có weight khác nhau.

Contributor thường quan trọng hơn khi:

- atoms đạt shell hợp lý;
- formal charge nhỏ;
- negative charge ở atom electronegative hơn;
- charge separation ít hơn;
- bonding phù hợp hơn với known chemistry.

Ví dụ amide có neutral contributor và charge-separated contributor:

```text
O=C–N  ↔  ⁻O–C=N⁺
```

Contributor thứ hai không dominant nhưng đủ quan trọng để làm C–N có partial double-bond character.

# Resonance giải thích hình học của amide

Do electron pair trên N delocalize vào carbonyl, C–N bond của amide ngắn hơn single C–N bình thường và rotation bị hạn chế.

Điều này làm peptide bond trong protein gần phẳng.

Một ý tưởng Lewis/resonance cơ bản vì thế nối trực tiếp tới cấu trúc protein trong sinh học.

# Conjugation — resonance mở rộng trên nhiều atoms

Khi các p orbitals liền kề có thể overlap, electron π có thể delocalize trên chuỗi dài.

Ví dụ allyl cation:

```text
CH2=CH–CH2⁺ ↔ ⁺CH2–CH=CH2
```

Positive charge không nằm cố định trên một carbon.

Trong conjugated polymer, delocalization mở rộng làm HOMO–LUMO gap giảm và tạo optical/electronic properties hữu ích.

Đây là cầu nối Lewis resonance → MO theory → organic electronics.

# Aromaticity không chỉ là “rất nhiều resonance”

Benzene thường được vẽ bằng hai Kekulé structures, nhưng aromatic stabilization sâu hơn simple averaging of double bonds.

Một cyclic, planar, conjugated π system có electron count phù hợp có thể có electronic stabilization đặc biệt. MO theory mô tả điều này tốt hơn Lewis.

Lewis contributors vẫn hữu ích để nhìn electron movement, nhưng không nên dùng chúng làm toàn bộ lý thuyết aromaticity.

# Curved arrows — Lewis structures trở thành ngôn ngữ cơ chế

Trong organic mechanisms, **mũi tên cong (curved arrow)** mô tả sự dịch chuyển của một electron pair từ electron-rich region tới electron-poor region.

Ví dụ nucleophile tấn công carbonyl:

```text
lone pair → carbonyl carbon
π(C=O) → oxygen
```

Mũi tên **không mô tả atom bay theo đường cong**. Nó hạch toán electron redistribution giữa Lewis structures trước và sau elementary step.

Do đó nắm Lewis tốt là prerequisite trực tiếp của reaction mechanisms.

# Formal charge khác partial charge

Trong carbonyl \(C=O\), Lewis neutral structure có formal charge 0 trên C và O, nhưng oxygen vẫn có partial negative charge còn carbon partial positive vì electronegativity khác nhau.

Vì vậy:

```text
formal charge → bookkeeping integer
partial charge → electron-density polarization
oxidation state → ionic bookkeeping for redox
```

Ba khái niệm trả lời ba câu hỏi khác nhau.

# Formal charge khác oxidation state

Với CO, formal-charge assignment và oxidation-state assignment khác vì chúng dùng rule phân electron khác nhau.

Formal charge chia bonding electrons equally.

Oxidation state gán toàn bộ bonding electrons cho atom electronegative hơn.

Không nên dùng oxidation state để chọn resonance contributor hay dùng formal charge để cân bằng redox một cách máy móc.

# Lewis acid và Lewis base

Lewis structure làm lộ rõ lone pair và electron-deficient center.

**Lewis base** cho electron pair.

**Lewis acid** nhận electron pair.

Ví dụ:

\[
NH_3+BF_3\rightarrow H_3N\to BF_3
\]

Nhìn lone pair trên N và empty acceptor capacity ở B giúp dự đoán reaction trước cả khi học orbital chi tiết.

# Lewis structure và VSEPR

Sau khi xây Lewis structure, đếm electron domains quanh central atom để chuyển sang hình học.

Ví dụ H₂O:

```text
2 O–H bonds + 2 lone pairs = 4 electron domains
```

→ electron geometry tetrahedral
→ molecular geometry bent.

Do đó Lewis là prerequisite trực tiếp của VSEPR.

# Lewis structure và hybridization

Lewis/VSEPR cho local coordination. Hybridization là một cách xây localized orbitals phù hợp geometry đó.

Nhưng không nên reasoning ngược kiểu:

```text
sp3 vì sách nói sp3 → nên geometry tetrahedral
```

Tốt hơn:

```text
electron structure + geometry quan sát
→ localized orbital model sp3 là representation hữu ích
```

# Lewis structure và MO theory

Lewis mạnh ở:

- connectivity;
- electron count;
- localized charges;
- reaction arrows.

MO mạnh hơn ở:

- delocalization;
- magnetism;
- excited states;
- spectroscopy;
- band formation.

Hai mô hình không “đánh nhau”; chúng dùng mức abstraction khác nhau.

# Một quy trình giải Lewis đáng tin cậy

Khi gặp species mới:

```text
1. đếm tổng valence electrons
2. xác định skeleton
3. tạo single bonds
4. hoàn thiện terminal shells
5. phân electron còn lại lên center
6. tạo multiple bonds nếu hợp lý
7. tính formal charges
8. tìm resonance contributors
9. kiểm tra electron count + total charge
10. hỏi model Lewis có giới hạn gì với species này
```

Bước 10 rất quan trọng: radical, electron-deficient, hypervalent và transition-metal species thường cần model cao hơn.

# Ví dụ tích hợp: nitrite NO₂⁻

Tổng valence electrons:

\[
5+2(6)+1=18
\]

Skeleton:

```text
O–N–O
```

Sau electron bookkeeping, hai contributors chính:

```text
O=N–O⁻ ↔ ⁻O–N=O
```

Hai N–O tương đương trung bình, bond order gần 1.5.

N còn một lone pair, nên quanh N có ba electron domains. VSEPR dự đoán electron geometry gần trigonal planar và molecular geometry bent.

Một bài Lewis vì thế tự nhiên dẫn sang geometry chứ không kết thúc ở chấm electron.

# Những hiểu lầm thường gặp

### “Đạt octet là đủ để structure đúng”

Không. Còn formal charge, electronegativity, connectivity và experimental constraints.

### “Resonance contributors là các phân tử luân phiên tồn tại”

Không. Chúng là nhiều representations của một electron state delocalized.

### “Formal charge là charge thật trên atom”

Không. Nó là bookkeeping model.

### “Expanded octet nghĩa central atom dùng d orbital mạnh”

Không phải giải thích mặc định hiện đại cho main-group hypervalency.

### “Lewis structure giải thích từ tính và màu”

Thường không. Cần MO/electronic-state models.

## Mô hình tư duy

Lewis theory nên được xem như **compiler frontend của cấu trúc hóa học**:

```text
formula + electron count
→ connectivity
→ localized electron bookkeeping
→ formal charge / resonance
→ geometry / reactivity hypotheses
```

Sau đó VSEPR, VB và MO cung cấp các lớp mô hình sâu hơn cho hình học, orbital và electron delocalization.

Xem tiếp: [VSEPR và hình học phân tử](./04_vsepr_and_molecular_geometry.md), [Liên kết hóa trị và lai hóa](./05_valence_bond_and_hybridization.md), [MO theory](./06_molecular_orbital_theory.md).