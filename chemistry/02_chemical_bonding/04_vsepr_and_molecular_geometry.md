# VSEPR và hình học phân tử — từ miền electron tới hình dạng ba chiều

> **VSEPR — thuyết đẩy cặp electron lớp hóa trị (Valence Shell Electron Pair Repulsion / 원자가 전자쌍 반발 이론)** là mô hình hình học dùng số và kiểu **miền electron (electron domain)** quanh nguyên tử trung tâm để dự đoán cách các nguyên tử sắp xếp trong không gian. VSEPR không phải lý thuyết lượng tử đầy đủ, nhưng rất hữu ích để nối cấu trúc Lewis với hình dạng, độ phân cực và phản ứng hóa học.

Nếu chỉ biết công thức và connectivity, ta chưa biết phân tử dài, gấp khúc, phẳng hay ba chiều. Nhưng hình học quyết định vector dipole, khả năng tiếp cận reaction center, stereochemistry và molecular recognition. Vì thế geometry là một tầng thông tin độc lập cần được suy ra.

# Từ Lewis structure tới electron domains

Sau khi vẽ Lewis structure, ta đếm các miền mật độ electron quanh central atom.

Trong VSEPR cơ bản:

- một single bond = một domain;
- double hoặc triple bond vẫn được tính là một domain định hướng chính;
- một lone pair = một domain;
- electron độc thân đôi khi cần xử lý riêng và VSEPR kém tin cậy hơn.

Các domains sắp xếp sao cho giảm repulsion hiệu dụng.

# Các hình học miền electron cơ bản

| Số miền | Hình học miền electron | Góc lý tưởng |
|---:|---|---:|
| 2 | thẳng (linear) | 180° |
| 3 | tam giác phẳng (trigonal planar) | 120° |
| 4 | tứ diện (tetrahedral) | 109.5° |
| 5 | lưỡng tháp tam giác (trigonal bipyramidal) | 90°, 120°, 180° |
| 6 | bát diện (octahedral) | 90°, 180° |

Các góc này là reference geometries. Phân tử thật có thể lệch do lone pairs, multiple bonds, substituent size, electronegativity và electronic effects.

# Electron geometry khác molecular geometry

**Hình học miền electron (electron geometry)** tính cả bonding domains và lone pairs.

**Hình học phân tử (molecular geometry / 분자 기하)** chỉ mô tả positions của nuclei.

Ví dụ nước:

```text
2 O–H bonds
+ 2 lone pairs
= 4 domains
```

Electron geometry: tetrahedral.

Molecular geometry: bent.

Đây là distinction cơ bản cần giữ xuyên suốt.

# Ký hiệu AXE

Một notation hữu ích:

```text
A = central atom
X = bonded atoms/domains
E = lone pairs trên central atom
```

Ví dụ:

```text
CO2  → AX2      → linear
BF3  → AX3      → trigonal planar
CH4  → AX4      → tetrahedral
NH3  → AX3E     → trigonal pyramidal
H2O  → AX2E2    → bent
```

Notation này giúp tách electron-domain count khỏi tên molecule cụ thể.

# Vì sao lone pair làm góc bond nhỏ lại?

Lone pair density không bị chia sẻ với atom thứ hai nên thường tập trung gần central atom hơn và chiếm solid angle lớn hơn bonding domain.

Xu hướng repulsion thường viết:

\[
LP-LP>LP-BP>BP-BP
\]

Do đó:

```text
CH4  ≈ 109.5°
NH3  ≈ 107°
H2O  ≈ 104.5°
```

Không nên hiểu lone pair là “quả bóng vật lý lớn hơn”. Đây là mô tả hiệu dụng của electron-density distribution.

# Multiple bond không phải hai domain nhưng có repulsion mạnh hơn

Một C=O vẫn chủ yếu chiếm một hướng nên được tính một domain. Tuy nhiên electron density của multiple bond lớn hơn single bond, nên nó có thể đẩy các domains lân cận mạnh hơn và làm bond angles lệch.

Ví dụ formal trigonal-planar center có một double bond thường không có ba góc đúng 120°.

VSEPR vì thế cho **shape class** tốt hơn exact angle.

# Hai electron domains — linear

AX₂ như CO₂:

\[
O=C=O
\]

Hai domains đặt đối nhau 180°.

Do symmetry, two C=O bond dipoles cancel và CO₂ nonpolar dù từng bond polar.

Đây là ví dụ đầu tiên cho connection:

```text
Lewis → VSEPR geometry → vector dipoles → molecular polarity
```

# Ba electron domains

## AX₃ — trigonal planar

BF₃ có ba B–F domains và no lone pair trên B:

```text
planar
angles ≈120°
```

Molecule có symmetry cao nên net dipole gần 0 dù B–F bonds rất polar.

## AX₂E — bent

SO₂ thường được mô tả với ba electron domains quanh S, gồm two bonding regions + one lone-pair region.

Electron geometry trigonal planar nhưng molecular geometry bent.

Vì dipoles không triệt tiêu, SO₂ polar.

# Bốn electron domains

## AX₄ — tetrahedral

CH₄ có four equivalent directions.

Tetrahedral geometry maximizes angular separation trong 3D tốt hơn square planar cho bốn equivalent domains.

## AX₃E — trigonal pyramidal

NH₃ có one lone pair. Nitrogen nằm above plane của three H atoms.

Geometry này làm NH₃ có permanent dipole và lone pair accessible, liên quan trực tiếp tới Lewis basicity.

## AX₂E₂ — bent

H₂O bent và polar. Geometry cho phép water tạo hydrogen-bond network và có dielectric behavior rất khác một hypothetical linear H₂O molecule.

Hình học đơn giản ở mức VSEPR vì vậy lan tới physical properties của nước và biology.

# Năm electron domains — trigonal bipyramidal

Trigonal bipyramid có hai loại sites không tương đương:

- **axial**: ba tương tác 90° với equatorial domains;
- **equatorial**: hai tương tác 90° với axial domains.

Lone pair thường ưu tiên equatorial position vì ít 90° interactions hơn.

## AX₅ — trigonal bipyramidal

PF₅ là textbook example.

Axial P–F và equatorial P–F có local environments khác nhau, nên bond lengths có thể khác.

## AX₄E — seesaw

Một equatorial lone pair để lại four atomic positions tạo shape seesaw.

## AX₃E₂ — T-shaped

Hai lone pairs ưu tiên equatorial, còn three bonded atoms tạo T shape.

## AX₂E₃ — linear

Ba equatorial lone pairs để lại two axial bonds đối nhau, như XeF₂ trong simple VSEPR description.

# Sáu electron domains — octahedral

## AX₆ — octahedral

SF₆ có six equivalent directions trong ideal model.

## AX₅E — square pyramidal

Một lone pair removed khỏi octahedral vertex tạo square-pyramidal molecular geometry.

## AX₄E₂ — square planar

Hai lone pairs đặt trans để giảm repulsion, để lại four atoms trong một mặt phẳng vuông.

XeF₄ là main-group example.

Square planar cũng rất quan trọng trong d⁸ transition-metal complexes như Pt(II), nhưng ở đó ligand-field theory giải thích sâu hơn VSEPR.

# VSEPR với transition metals — biết lúc nào phải dừng dùng model

Transition-metal geometry phụ thuộc d-electron configuration, ligand-field splitting, steric effects và bonding orbital interactions.

Ví dụ four-coordinate complexes có thể tetrahedral hoặc square planar. Chỉ đếm domains kiểu main-group không đủ để dự đoán reliably.

Do đó VSEPR là một model có **domain of applicability**, không phải universal geometry engine.

# Molecular geometry và dipole moment

Net molecular dipole là vector sum:

\[
\vec\mu_{mol}=\sum_i\vec\mu_i
\]

với đóng góp từ bond polarization và electron distribution.

Ví dụ:

```text
CO2: polar bonds + linear symmetry → μ ≈ 0
BF3: polar bonds + trigonal symmetry → μ ≈ 0
H2O: polar bonds + bent shape → μ ≠ 0
NH3: polar bonds + pyramidal shape → μ ≠ 0
```

Chỉ biết electronegativity không đủ để kết luận molecule polar; geometry là phần còn lại của bài toán vector.

# Geometry và intermolecular forces

Molecular polarity ảnh hưởng:

- dipole–dipole attraction;
- solubility;
- boiling point trends;
- orientation at interfaces.

Geometry cũng xác định donor/acceptor positions cho hydrogen bonding.

Trong protein, placement ba chiều của carbonyl O, amide N–H và side-chain groups quyết định folding và recognition.

# Geometry và reaction mechanism

Một reaction center không chỉ cần electron-rich/electron-poor; reactant còn phải tiếp cận đúng direction.

Trong SN2 substitution, nucleophile ưu tiên **backside attack** đối diện leaving group vì orbital interaction với \(\sigma^*\) tốt nhất ở direction đó.

Kết quả là inversion of configuration.

Đây là ví dụ VSEPR/local geometry dẫn thẳng sang stereochemical mechanism.

# Geometry và orbital overlap

Shape dự đoán bởi VSEPR có thể được mô tả sâu hơn bằng localized orbitals hoặc MO theory.

Ví dụ tetrahedral geometry của carbon tương thích với bốn localized bonding directions có thể biểu diễn bằng sp³ hybrid basis.

Nhưng không nên đảo logic và nghĩ “sp³ tồn tại trước nên atom buộc phải tetrahedral”. Hybridization là representation của wavefunction phù hợp geometry.

# Geometry và symmetry

Symmetry giúp dự đoán:

- dipole cancellation;
- degeneracy;
- IR/Raman selection rules;
- equivalent atoms trong NMR;
- orbital combinations trong MO theory.

Ví dụ tetrahedral CH₄ có high symmetry nên all four C–H bonds equivalent trong ideal structure.

Molecular geometry vì vậy là gateway tới group theory và spectroscopy.

# Axial/equatorial preference và steric size

Trong trigonal bipyramidal systems, lone pair không phải factor duy nhất. Bulky substituents cũng thường prefer equatorial positions vì có fewer 90° contacts.

VSEPR language có thể absorb một phần steric reasoning, nhưng electronic preferences và ligand-specific effects đôi khi vượt simple repulsion counting.

# Geometry có thể biến đổi động

Một molecule không phải sculpture cứng. Bonds vibrate, angles bend và conformations interconvert.

Một geometry label như “tetrahedral” thường nói equilibrium/average local arrangement, không có nghĩa atoms đứng im.

Trong fluxional molecules, exchange nhanh có thể làm NMR quan sát một average structure khác các snapshots tức thời.

# Berry pseudorotation

PF₅ derivatives có thể exchange axial/equatorial positions qua **Berry pseudorotation** mà không cần phá hoàn toàn molecular framework.

Đây là ví dụ cho việc geometry landscape có multiple conformations được nối bằng low-energy paths.

VSEPR cho static endpoints; kinetics cho interconversion giữa chúng.

# Lone pair stereochemical activity

Không phải mọi lone pair đều gây distortion giống nhau.

Ở heavy main-group elements, relativistic/electronic effects có thể làm lone pair ít stereochemically active hơn hoặc localization khác simple VSEPR picture.

Do đó “có lone pair = chắc chắn shape X với angle Y” là simplification.

# Hypervalent molecules và giới hạn electron-pair picture

PF₅, SF₆ và Xe compounds được mô tả hình học tốt bằng domain counting, nhưng bonding electron structure không nhất thiết tương ứng với localized two-center two-electron bonds mở rộng bằng d hybridization.

VSEPR có thể dự đoán shape đúng trong khi một giải thích orbital naïve lại sai.

Đây là bài học quan trọng: **một model có thể dự đoán một tầng hiện tượng tốt mà không phải là mô tả đầy đủ tầng sâu hơn**.

# Các bước giải một bài geometry

Một workflow đáng tin cậy:

```text
1. vẽ Lewis structure
2. xác định central atom
3. đếm electron domains
4. xác định electron geometry
5. xác định lone pairs
6. suy molecular geometry
7. dự đoán distortions định tính
8. cộng vector bond dipoles
9. kiểm tra VSEPR có phù hợp loại species hay không
```

Không nên nhảy thẳng từ formula sang shape nếu chưa accounting electron structure.

# Ví dụ tích hợp: SF₄

S có five electron domains: four S–F bonds + one lone pair.

Electron geometry:

```text
trigonal bipyramidal
```

Lone pair chọn equatorial site.

Remaining atoms tạo:

```text
seesaw geometry
```

Molecule không có symmetry đủ để bond dipoles triệt tiêu hoàn toàn, nên có net polarity.

Một ví dụ duy nhất nối Lewis → domain counting → site preference → molecular shape → polarity.

# Ví dụ tích hợp: XeF₄

Xe có six domains trong Lewis/VSEPR treatment:

```text
4 bonding + 2 lone pairs
```

Electron geometry octahedral.

Hai lone pairs đặt trans nhau.

Molecular geometry square planar.

Bốn Xe–F bond dipoles trong ideal square cancel nên molecule overall nonpolar.

# VSEPR không giải thích bond formation

VSEPR bắt đầu sau khi ta đã biết central atom, connectivity và electron domains. Nó không trả lời:

- vì sao bond hình thành;
- orbital energy ra sao;
- electron delocalized thế nào;
- excited states;
- magnetic properties.

Những câu hỏi đó cần VB/MO/quantum chemistry.

# Những hiểu lầm thường gặp

### “Lone pair là quả bóng lớn hơn bond pair”

Không. Đây là shorthand cho spatial electron density và repulsion hiệu dụng.

### “Double bond tính hai electron domains”

Không trong VSEPR cơ bản; nó là một directional domain nhưng thường repulsive hơn single bond.

### “VSEPR cho exact bond angles”

Không. Nó dự đoán geometry class và qualitative distortions.

### “Molecule không polar nếu có bonds giống nhau”

Không. Cần vector symmetry của toàn geometry.

### “VSEPR dùng tốt như nhau cho transition metals”

Không. Ligand-field/electronic structure thường quan trọng hơn.

## Mô hình tư duy

VSEPR là **bộ chuyển đổi từ electron bookkeeping sang spatial model**:

```text
Lewis electron domains
→ arrangement giảm crowding
→ positions của nuclei
→ symmetry
→ dipole / recognition / reactivity
```

Nó mạnh ở shape prediction, nhưng phải chuyển sang VB/MO khi câu hỏi trở thành “electron thực sự được tổ chức bằng orbital như thế nào?”.

Xem tiếp: [Lý thuyết liên kết hóa trị và lai hóa](./05_valence_bond_and_hybridization.md).