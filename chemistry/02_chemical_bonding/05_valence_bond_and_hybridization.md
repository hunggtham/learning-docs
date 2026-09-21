# Lý thuyết liên kết hóa trị và lai hóa — mô hình các liên kết cục bộ trong không gian

> **Lý thuyết liên kết hóa trị (valence bond theory, VB / 원자가 결합 이론)** mô tả liên kết cộng hóa trị bằng sự chồng phủ của các obitan nguyên tử hoặc obitan đã được tổ hợp lại theo hướng phù hợp. **Lai hóa (hybridization / 혼성화)** là cách chọn một cơ sở obitan cục bộ thuận tiện để mô tả nhiều liên kết tương đương và hình học phân tử. Hai ý tưởng này rất mạnh trong hóa học hữu cơ, lập thể và reasoning về liên kết σ/π, nhưng chúng là **mô hình biểu diễn**, không phải những “cánh tay orbital” tồn tại độc lập trước khi phân tử hình thành.

# Vì sao cần một mô hình khác sau Lewis và VSEPR?

Lewis nói electron pair nào được hạch toán thành bond hoặc lone pair.

VSEPR nói electron domains sắp xếp theo geometry nào.

Nhưng hai mô hình trên chưa trả lời:

- orbital nào overlap để tạo bond;
- vì sao σ và π khác nhau;
- vì sao double bond hạn chế rotation;
- tại sao carbon tạo bốn bond tương đương;
- stereochemistry liên hệ orbital ra sao.

Valence-bond language lấp khoảng trống đó.

# Liên kết như sự chồng phủ orbital

Nếu hai orbital có symmetry phù hợp và electron spins có thể ghép đôi, sự chồng phủ có thể làm electron density tăng giữa hai nuclei và hạ năng lượng hệ.

Sự ổn định không đến từ “orbital chạm nhau” như hai vật rắn. Orbital là wavefunction; overlap nghĩa amplitudes của wavefunctions cùng tồn tại trong một vùng không gian và có thể tạo combination có năng lượng thấp hơn.

# Liên kết sigma

**Liên kết σ (sigma bond / 시그마 결합)** có electron density đối xứng gần quanh trục nối hai nuclei.

Nó có thể hình thành từ:

```text
s–s overlap
s–p overlap
p–p head-on overlap
hybrid–hybrid overlap
hybrid–s overlap
```

Vì density nằm quanh bond axis, rotation quanh một isolated single σ bond thường không phá overlap chính hoàn toàn. Điều này cho phép conformational rotation trong nhiều phân tử hữu cơ.

# Liên kết pi

**Liên kết π (pi bond / 파이 결합)** hình thành từ side-by-side overlap của orbitals, thường là p orbitals song song.

Electron density nằm ở hai phía của bond axis và có nodal plane chứa trục liên kết.

Nếu xoay một đầu quanh bond axis 90°, two p orbitals mất alignment và π overlap giảm mạnh. Vì vậy double bond có rotational barrier lớn và có thể tạo E/Z stereoisomers.

# Double và triple bond

Một C=C thường được mô tả:

```text
1 σ + 1 π
```

Một C≡C:

```text
1 σ + 2 π vuông góc nhau
```

Điều này giải thích vì sao multiple bond không chỉ là “nhiều thanh bond hơn”. σ và π có symmetry, overlap và phản ứng khác nhau.

# Bài toán methane và ý tưởng hybridization

Carbon ở trạng thái nguyên tử tự do có configuration đơn giản:

\[
2s^22p^2
\]

Nếu lấy nguyên xi các atomic orbitals, khó thấy ngay vì sao CH₄ có bốn C–H bonds gần tương đương theo tetrahedral geometry.

Ta có thể xây bốn tổ hợp tuyến tính từ one 2s + three 2p:

\[
sp^3
\]

Các **obitan lai sp³ (sp3 hybrid orbitals)** định hướng gần tetrahedral và mỗi orbital overlap với H 1s.

Đây là một change of basis toán học hữu ích cho localized bonding description.

# Hybrid orbitals là tổ hợp tuyến tính

Nếu \(\phi_s,\phi_{p_x},\phi_{p_y},\phi_{p_z}\) là atomic basis functions, một sp³ orbital có dạng khái niệm:

\[
\phi_{sp^3}=c_s\phi_s+c_x\phi_{p_x}+c_y\phi_{p_y}+c_z\phi_{p_z}
\]

Bốn combinations khác nhau chọn signs/coefficient để hướng về bốn tetrahedral directions.

Điểm cốt lõi: ta không tạo electron mới hay orbital mới vật lý từ hư không. Ta **biểu diễn cùng orbital space bằng một basis định hướng thuận tiện hơn**.

# sp³ — bốn hướng liên kết cục bộ

Ideal sp³ geometry:

\[
109.5^\circ
\]

CH₄ là example điển hình.

NH₃ và H₂O thường cũng được mô tả bằng localized sp³-like orbitals, nhưng lone-pair density làm angles và orbital characters khác ideal picture.

Do đó “sp³” không có nghĩa mọi orbital phải giống nhau chính xác trong molecule thật.

# sp² — mặt phẳng và một p orbital còn lại

One s + two p tạo three sp² hybrids trong một plane gần 120°.

Một p orbital không lai hóa còn vuông góc với plane.

Trong ethene:

```text
sp² orbitals → σ framework
unhybridized p → π bond
```

Mỗi carbon gần trigonal planar. Vì π overlap đòi p orbitals song song, rotation quanh C=C bị hạn chế.

# sp — linear và hai p orbitals còn lại

One s + one p tạo two sp hybrids đối nhau 180°.

Hai p orbitals còn lại vuông góc nhau và với bond axis.

Trong acetylene:

```text
sp–sp overlap → C–C σ
p–p overlap 1 → π
p–p overlap 2 → π
```

nên C≡C gần linear.

# S-character và tính chất hóa học

Trong simple hybrid model:

```text
sp   → 50% s
sp²  → 33% s
sp³  → 25% s
```

s orbital có density gần nucleus hơn p orbital. Vì thế orbital có nhiều s-character giữ electron density gần nucleus hơn.

Điều này giúp rationalize nhiều trends:

- C–H bond của sp carbon thường ngắn hơn sp²/sp³;
- carbanion trong sp orbital được ổn định hơn;
- terminal alkyne có acidity cao hơn alkene/alkane.

Ví dụ approximate acidity trend:

```text
HC≡CH  >  H2C=CH2  >  H3C–CH3
```

Hybridization ở đây nối structure với acid–base chemistry.

# Bent’s rule — hybridization không nhất thiết nguyên vẹn sp³/sp²

Các bonds quanh cùng central atom không nhất thiết có identical hybrid character.

**Quy tắc Bent (Bent's rule)** nói gần đúng rằng atomic s-character có xu hướng tập trung vào bonds hướng tới substituents electropositive hơn, còn p-character nhiều hơn hướng tới electronegative substituents.

Vì thế real localized orbitals thường có hybridization không phải integer labels hoàn hảo như sp² hoặc sp³.

Các nhãn sp/sp²/sp³ là shorthand hữu ích, không phải quantum numbers.

# Lone pairs và hybridization

Lone pair có thể chiếm localized orbital với s/p character khác bonding orbitals.

Trong amines, geometry gần pyramidal thường được mô tả sp³-like. Nhưng trong amides, lone pair trên N conjugate với carbonyl π system nên N gần planar.

Điều này dẫn tới partial C–N double-bond character và restricted rotation.

Do đó không nên gán hybridization chỉ bằng cách đếm four groups; resonance/conjugation có thể thay orbital organization.

# Conjugation đòi orbital alignment

Trong một conjugated system:

```text
p–p–p–p continuous overlap
```

cho phép π electrons delocalize trên nhiều atoms.

Nếu một atom trở thành strongly pyramidal và p orbital mất alignment, conjugation giảm.

Đây là lý do planarity thường được ưu tiên trong amides, allylic systems và aromatic rings.

# Hyperconjugation

**Siêu liên hợp (hyperconjugation)** là delocalization giữa một σ bond, thường C–H/C–C, và orbital lân cận như empty p hoặc π*.

Ví dụ carbocation được stabilize khi adjacent σ bonds có thể donate density vào empty p orbital.

Hyperconjugation giúp giải thích:

- carbocation stability;
- alkene substitution trends;
- conformational effects;
- some bond length changes.

Localized VB language vì thế không có nghĩa electron hoàn toàn bị khóa trong từng bond.

# Resonance trong valence-bond theory

Valence-bond theory có thể dùng nhiều localized structures và combine chúng thành wavefunction tốt hơn.

Lewis resonance contributors là một phiên bản định tính của ý tưởng này.

Benzene có thể được mô tả bằng superposition của nhiều VB structures thay vì một Kekulé form duy nhất.

Do đó “VB = localized, MO = delocalized” là simplification. VB hiện đại cũng mô tả delocalization thông qua resonance giữa localized configurations.

# Orbital phase và phản ứng

Overlap phụ thuộc phase/sign của wavefunctions, không chỉ geometry.

Constructive overlap tạo bonding interaction; destructive overlap tạo node/antibonding character.

Trong organic reaction mechanisms, orientation của filled orbital với acceptor orbital quyết định stereoelectronic preference.

# SN2 — backside attack từ orbital perspective

Trong SN2, nucleophile lone pair donate vào \(\sigma^*\) orbital của C–leaving-group bond.

\(\sigma^*\) có lobe phù hợp ở backside của carbon, nên nucleophile tiếp cận từ phía đối diện leaving group.

Kết quả:

```text
backside attack
→ transition state gần trigonal-bipyramidal arrangement
→ inversion of configuration
```

Đây là ví dụ mạnh cho việc geometry mechanism xuất phát từ donor–acceptor orbital interaction.

# E2 — anti-periplanar requirement

Trong E2 elimination, C–H bond đang bị phá và C–leaving-group bond cần alignment để electron flow hiệu quả vào forming π bond.

Geometry anti-periplanar thường tối ưu overlap.

Vì vậy conformational analysis của cyclohexane có thể dự đoán E2 reactivity: leaving group và β-H thường cần trans-diaxial arrangement.

Hybrid/orbital thinking nối trực tiếp molecular geometry với product outcome.

# Carbonyl — π và π* tạo electrophilicity

C=O gồm σ framework và π interaction. Vì O electronegative hơn, occupied π orbital và unoccupied π* không phân bố đối xứng.

LUMO-like π* có coefficient đáng kể trên carbon, tạo acceptor site cho nucleophile.

Nucleophile attack thường xảy ra theo một angle không hoàn toàn 90° với carbonyl plane, thường được mô tả bởi **Bürgi–Dunitz trajectory**.

Đây là example advanced cho stereoelectronic control.

# Hybridization và geometry không phải nguyên nhân–kết quả đơn chiều

Textbook thường viết:

```text
carbon sp3 → tetrahedral
```

Một cách chính xác hơn:

```text
electronic Hamiltonian + nuclear positions
→ molecular wavefunction/geometry
→ localized orbital analysis có thể biểu diễn bằng sp3-like basis
```

Hybridization là một language mô tả geometry/bonding, không phải force bí ẩn làm atom chọn shape.

# Promotion energy và “carbon kích electron lên p”

Cách giải thích cổ điển nói carbon “promote” one 2s electron lên 2p rồi hybridize.

Hình ảnh này có giá trị mnemonic nhưng không nên hiểu như một sequence vật lý riêng biệt:

```text
atom promote trước
→ hybridize
→ rồi bond
```

Molecule hình thành như một toàn hệ lượng tử; energy gained from bonding được xét cùng mọi rearrangements electronic.

# Hypervalent main-group compounds

Cách dạy cũ dùng sp³d/sp³d² hybrids chứa d orbitals cho PF₅/SF₆.

Electronic-structure calculations cho thấy contribution của central-atom d orbitals thường không tương xứng với literal expanded-hybrid picture.

Models như **three-center four-electron bonding (3c–4e)**, ionic resonance và MO delocalization thường phù hợp hơn.

Vì vậy:

```text
sp3d, sp3d2
```

có thể giữ như geometry mnemonic trong contexts nhập môn, nhưng không nên coi là literal bonding mechanism.

# Three-center four-electron bond

Trong simple 3c–4e picture, ba atomic orbitals combine thành:

- bonding MO;
- approximately nonbonding MO;
- antibonding MO.

Bốn electrons fill bonding + nonbonding levels, tạo two equivalent partial bonds trên three centers.

I₃⁻ và XeF₂ là examples phù hợp để vượt khỏi localized two-center bond picture.

# Localized orbitals từ MO wavefunction

Ngay cả khi quantum chemistry tính canonical MOs delocalized, các occupied orbitals có thể được transform bằng unitary transformation thành **localized molecular orbitals** mà không thay tổng wavefunction determinant.

Các schemes như Boys hoặc Pipek–Mezey localization tạo orbitals giống bond/lone-pair picture.

Điều này cho thấy localized VB-like và delocalized MO-like descriptions có thể là những coordinate systems khác nhau trên cùng electronic state.

# Bond order không hoàn toàn là số bond Lewis

Trong localized description, ta nói single/double/triple. Nhưng bond order thực có thể được estimate bằng nhiều definitions: Wiberg, Mayer, MO occupancy...

Các giá trị có thể không nguyên và phụ thuộc analysis method.

Do đó “bond order 1.3” không phải mâu thuẫn; nó phản ánh partial/delocalized bonding.

# Hybridization và spectroscopy

s-character ảnh hưởng NMR chemical shifts, coupling, core-level energies và vibrational frequencies gián tiếp qua geometry/bond strength.

Spectroscopy vì vậy cung cấp evidence để kiểm tra localized bonding picture, không chỉ là một kỹ thuật nhận diện độc lập.

# Hybridization trong materials

Carbon allotropes minh họa mạnh:

```text
diamond → sp3-like tetrahedral network
planar graphene → sp2-like σ network + delocalized π system
carbyne-like chains → sp-like local picture
```

Khác local orbital organization tạo khác biệt lớn về hardness, dimensionality và electronic transport.

# Khi nào nên dùng VB/hybridization?

Model này đặc biệt hữu ích khi câu hỏi liên quan:

- local σ/π bonding;
- molecular geometry;
- stereochemistry;
- conformational restrictions;
- donor–acceptor orbital orientation;
- organic mechanisms.

Nên chuyển sang MO/quantum methods khi cần:

- global delocalization;
- magnetism;
- excited states;
- spectroscopy;
- near-degenerate electronic states;
- band structure.

# Những hiểu lầm thường gặp

### “Hybridization là một sự kiện xảy ra trước bonding”

Không. Đó là representation/basis transformation hữu ích của molecular electronic structure.

### “sp³ nghĩa exact 25% s trên mọi orbital”

Chỉ đúng trong idealized symmetric construction. Real molecules có thể rehybridize.

### “Mọi molecule phải gán hybridization”

Không. Nhiều systems được mô tả tốt hơn bằng MO theory.

### “sp³d chứng minh d orbital tạo hypervalent bonds”

Không phải interpretation hiện đại đáng tin cậy mặc định.

### “Single bond luôn quay tự do”

Không. Conjugation, steric effects và ring constraints có thể tạo rotational barriers lớn.

## Mô hình tư duy

Valence-bond language nhìn molecule như **mạng tương tác orbital cục bộ có directionality**:

```text
atomic/orbital basis
→ localized hybrid directions
→ σ / π overlap
→ stereoelectronic constraints
→ geometry và reactivity
```

Hybridization là coordinate system rất hữu ích cho local chemistry, còn MO theory mở rộng sang electron states của toàn molecule.

Xem tiếp: [Lý thuyết obitan phân tử](./06_molecular_orbital_theory.md).