# VSEPR và hình học phân tử — từ miền electron tới hình dạng ba chiều

> **Mạch đọc:** Đọc **VSEPR và hình học phân tử — từ miền electron tới hình dạng ba chiều** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **AX₃ — trigonal planar** sang **AX₂E — bent**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


> **VSEPR — thuyết đẩy cặp electron lớp hóa trị (Valence Shell Electron Pair Repulsion / 원자가 전자쌍 반발 이론)** là mô hình hình học dùng số và kiểu **miền electron (electron domain)** quanh nguyên tử trung tâm để dự đoán cách các nguyên tử sắp xếp trong không gian. VSEPR không phải lý thuyết lượng tử đầy đủ, nhưng rất hữu ích để nối cấu trúc Lewis với hình dạng, độ phân cực và phản ứng hóa học.

Nếu chỉ biết công thức và connectivity, ta chưa biết phân tử dài, gấp khúc, phẳng hay ba chiều. Nhưng hình học quyết định véc-tơ (vector / 벡터) dipole, khả năng tiếp cận reaction center, stereochemistry và molecular recognition. Vì thế hình học (geometry / 기하학) là một tầng thông tin độc lập cần được suy ra.

# Từ Lewis cấu trúc (structure / 구조) tới electron domains

Sau khi vẽ Lewis cấu trúc (structure / 구조), ta đếm các miền mật độ electron quanh central atom.

Trong VSEPR cơ bản:

- một single bond = một lĩnh vực (domain / 도메인);
- double hoặc triple bond vẫn được tính là một lĩnh vực (domain / 도메인) định hướng chính;
- một lone pair = một lĩnh vực (domain / 도메인);
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

Các góc này là tham chiếu (reference / 참조) geometries. Phân tử thật có thể lệch do lone pairs, multiple bonds, substituent kích thước (size / 크기), electronegativity và electronic effects.

# Electron hình học (geometry / 기하학) khác molecular hình học (geometry / 기하학)

**Hình học miền electron (electron geometry)** tính cả bonding domains và lone pairs.

**Hình học phân tử (molecular geometry / 분자 기하)** chỉ mô tả positions của nuclei.

Ví dụ nước:

```text
2 O–H bonds
+ 2 lone pairs
= 4 domains
```

Electron hình học (geometry / 기하학): tetrahedral.

Molecular hình học (geometry / 기하학): bent.

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

Lone pair density không bị chia sẻ với atom thứ hai nên thường tập trung gần central atom hơn và chiếm solid angle lớn hơn bonding lĩnh vực (domain / 도메인).

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

Không nên hiểu lone pair là “quả bóng vật lý lớn hơn”. Đây là mô tả hiệu dụng của electron-density phân phối (distribution / 분포).

# Multiple bond không phải hai lĩnh vực (domain / 도메인) nhưng có repulsion mạnh hơn

Một C=O vẫn chủ yếu chiếm một hướng nên được tính một lĩnh vực (domain / 도메인). Tuy nhiên electron density của multiple bond lớn hơn single bond, nên nó có thể đẩy các domains lân cận mạnh hơn và làm bond angles lệch.

Ví dụ formal trigonal-planar center có một double bond thường không có ba góc đúng 120°.

VSEPR vì thế cho **shape lớp (class / 클래스)** tốt hơn chính xác (exact / 정확한) angle.

# Hai electron domains — tuyến tính (linear / 선형)

AX₂ như CO₂:

\[
O=C=O
\]

Hai domains đặt đối nhau 180°.

Do symmetry, two C=O bond dipoles cancel và CO₂ nonpolar dù từng bond polar.

Đây là ví dụ đầu tiên cho liên kết (connection / 연결):

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

Electron hình học (geometry / 기하학) trigonal planar nhưng molecular hình học (geometry / 기하학) bent.

Vì dipoles không triệt tiêu, SO₂ polar.

# Bốn electron domains

## AX₄ — tetrahedral

CH₄ có four equivalent directions.

Tetrahedral hình học (geometry / 기하학) maximizes angular separation trong 3D tốt hơn square planar cho bốn equivalent domains.

## AX₃E — trigonal pyramidal

NH₃ có one lone pair. Nitrogen nằm above plane của three H atoms.

Hình học (geometry / 기하학) này làm NH₃ có permanent dipole và lone pair accessible, liên quan trực tiếp tới Lewis basicity.

## AX₂E₂ — bent

H₂O bent và polar. hình học (geometry / 기하학) cho phép water tạo hydrogen-bond mạng (network / 네트워크) và có dielectric hành vi (behavior / 동작) rất khác một hypothetical tuyến tính (linear / 선형) H₂O molecule.

Hình học đơn giản ở mức VSEPR vì vậy lan tới vật lý (physical / 물리적) properties của nước và biology.

# Năm electron domains — trigonal bipyramidal

Trigonal bipyramid có hai loại sites không tương đương:

- **axial**: ba tương tác 90° với equatorial domains;
- **equatorial**: hai tương tác 90° với axial domains.

Lone pair thường ưu tiên equatorial position vì ít 90° interactions hơn.

## AX₅ — trigonal bipyramidal

PF₅ là textbook example.

Axial P–F và equatorial P–F có cục bộ (local / 로컬) environments khác nhau, nên bond lengths có thể khác.

## AX₄E — seesaw

Một equatorial lone pair để lại four atomic positions tạo shape seesaw.

## AX₃E₂ — T-shaped

Hai lone pairs ưu tiên equatorial, còn three bonded atoms tạo T shape.

## AX₂E₃ — tuyến tính (linear / 선형)

Ba equatorial lone pairs để lại two axial bonds đối nhau, như XeF₂ trong simple VSEPR description.

# Sáu electron domains — octahedral

## AX₆ — octahedral

SF₆ có six equivalent directions trong ideal mô hình (model / 모델).

## AX₅E — square pyramidal

Một lone pair removed khỏi octahedral vertex tạo square-pyramidal molecular hình học (geometry / 기하학).

## AX₄E₂ — square planar

Hai lone pairs đặt trans để giảm repulsion, để lại four atoms trong một mặt phẳng vuông.

XeF₄ là main-group example.

Square planar cũng rất quan trọng trong d⁸ transition-metal complexes như Pt(II), nhưng ở đó ligand-field lý thuyết (theory / 이론) giải thích sâu hơn VSEPR.

# VSEPR với chuyển tiếp (transition / 전이) metals — biết lúc nào phải dừng dùng mô hình (model / 모델)

Transition-metal hình học (geometry / 기하학) phụ thuộc d-electron cấu hình (configuration / 구성), ligand-field splitting, steric effects và bonding orbital interactions.

Ví dụ four-coordinate complexes có thể tetrahedral hoặc square planar. Chỉ đếm domains kiểu main-group không đủ để dự đoán reliably.

Do đó VSEPR là một mô hình (model / 모델) có **lĩnh vực (domain / 도메인) of applicability**, không phải universal hình học (geometry / 기하학) engine.

# Molecular hình học (geometry / 기하학) và dipole moment

Net molecular dipole là véc-tơ (vector / 벡터) sum:

\[
\vec\mu_{mol}=\sum_i\vec\mu_i
\]

với đóng góp từ bond polarization và electron phân phối (distribution / 분포).

Ví dụ:

```text
CO2: polar bonds + linear symmetry → μ ≈ 0
BF3: polar bonds + trigonal symmetry → μ ≈ 0
H2O: polar bonds + bent shape → μ ≠ 0
NH3: polar bonds + pyramidal shape → μ ≠ 0
```

Chỉ biết electronegativity không đủ để kết luận molecule polar; hình học (geometry / 기하학) là phần còn lại của bài toán véc-tơ (vector / 벡터).

# Hình học (geometry / 기하학) và intermolecular forces

Molecular polarity ảnh hưởng:

- dipole–dipole attraction;
- solubility;
- boiling điểm (point / 지점) trends;
- orientation at interfaces.

Hình học (geometry / 기하학) cũng xác định donor/acceptor positions cho hydrogen bonding.

Trong protein, placement ba chiều của carbonyl O, amide N–H và side-chain groups quyết định folding và recognition.

# Hình học (geometry / 기하학) và reaction cơ chế (mechanism / 메커니즘)

Một reaction center không chỉ cần electron-rich/electron-poor; reactant còn phải tiếp cận đúng direction.

Trong SN2 substitution, nucleophile ưu tiên **backside attack** đối diện leaving group vì orbital tương tác (interaction / 상호작용) với \(\sigma^*\) tốt nhất ở direction đó.

Kết quả là inversion of cấu hình (configuration / 구성).

Đây là ví dụ VSEPR/cục bộ (local / 로컬) hình học (geometry / 기하학) dẫn thẳng sang stereochemical cơ chế (mechanism / 메커니즘).

# Hình học (geometry / 기하학) và orbital overlap

Shape dự đoán bởi VSEPR có thể được mô tả sâu hơn bằng localized orbitals hoặc MO lý thuyết (theory / 이론).

Ví dụ tetrahedral hình học (geometry / 기하학) của carbon tương thích với bốn localized bonding directions có thể biểu diễn bằng sp³ hybrid basis.

Nhưng không nên đảo lô-gic (logic / 논리) và nghĩ “sp³ tồn tại trước nên atom buộc phải tetrahedral”. Hybridization là biểu diễn (representation / 표현) của wavefunction phù hợp hình học (geometry / 기하학).

# Hình học (geometry / 기하학) và symmetry

Symmetry giúp dự đoán:

- dipole cancellation;
- degeneracy;
- IR/Raman selection rules;
- equivalent atoms trong NMR;
- orbital combinations trong MO lý thuyết (theory / 이론).

Ví dụ tetrahedral CH₄ có high symmetry nên all four C–H bonds equivalent trong ideal cấu trúc (structure / 구조).

Molecular hình học (geometry / 기하학) vì vậy là gateway tới group lý thuyết (theory / 이론) và spectroscopy.

# Axial/equatorial preference và steric kích thước (size / 크기)

Trong trigonal bipyramidal các hệ thống (systems / 시스템들), lone pair không phải factor duy nhất. Bulky substituents cũng thường prefer equatorial positions vì có fewer 90° contacts.

VSEPR ngôn ngữ (language / 언어) có thể absorb một phần steric lập luận (reasoning / 추론), nhưng electronic preferences và ligand-specific effects đôi khi vượt simple repulsion counting.

# Hình học (geometry / 기하학) có thể biến đổi động

Một molecule không phải sculpture cứng. Bonds vibrate, angles bend và conformations interconvert.

Một hình học (geometry / 기하학) label như “tetrahedral” thường nói equilibrium/average cục bộ (local / 로컬) arrangement, không có nghĩa atoms đứng im.

Trong fluxional molecules, exchange nhanh có thể làm NMR quan sát một average cấu trúc (structure / 구조) khác các snapshots tức thời.

# Berry pseudorotation

PF₅ derivatives có thể exchange axial/equatorial positions qua **Berry pseudorotation** mà không cần phá hoàn toàn molecular khung phần mềm (framework / 프레임워크).

Đây là ví dụ cho việc hình học (geometry / 기하학) landscape có multiple conformations được nối bằng low-energy paths.

VSEPR cho static endpoints; kinetics cho interconversion giữa chúng.

# Lone pair stereochemical activity

Không phải mọi lone pair đều gây distortion giống nhau.

Ở heavy main-group elements, relativistic/electronic effects có thể làm lone pair ít stereochemically active hơn hoặc localization khác simple VSEPR picture.

Do đó “có lone pair = chắc chắn shape X với angle Y” là simplification.

# Hypervalent molecules và giới hạn electron-pair picture

PF₅, SF₆ và Xe compounds được mô tả hình học tốt bằng lĩnh vực (domain / 도메인) counting, nhưng bonding electron cấu trúc (structure / 구조) không nhất thiết tương ứng với localized two-center two-electron bonds mở rộng bằng d hybridization.

VSEPR có thể dự đoán shape đúng trong khi một giải thích orbital naïve lại sai.

Đây là bài học quan trọng: **một mô hình (model / 모델) có thể dự đoán một tầng hiện tượng tốt mà không phải là mô tả đầy đủ tầng sâu hơn**.

# Các bước giải một bài hình học (geometry / 기하학)

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

Không nên nhảy thẳng từ formula sang shape nếu chưa accounting electron cấu trúc (structure / 구조).

# Ví dụ tích hợp: SF₄

S có five electron domains: four S–F bonds + one lone pair.

Electron hình học (geometry / 기하학):

```text
trigonal bipyramidal
```

Lone pair chọn equatorial site.

Remaining atoms tạo:

```text
seesaw geometry
```

Molecule không có symmetry đủ để bond dipoles triệt tiêu hoàn toàn, nên có net polarity.

Một ví dụ duy nhất nối Lewis → lĩnh vực (domain / 도메인) counting → site preference → molecular shape → polarity.

# Ví dụ tích hợp: XeF₄

Xe có six domains trong Lewis/VSEPR treatment:

```text
4 bonding + 2 lone pairs
```

Electron hình học (geometry / 기하학) octahedral.

Hai lone pairs đặt trans nhau.

Molecular hình học (geometry / 기하학) square planar.

Bốn Xe–F bond dipoles trong ideal square cancel nên molecule overall nonpolar.

# VSEPR không giải thích bond formation

VSEPR bắt đầu sau khi ta đã biết central atom, connectivity và electron domains. Nó không trả lời:

- vì sao bond hình thành;
- orbital năng lượng (energy / 에너지) ra sao;
- electron delocalized thế nào;
- excited states;
- magnetic properties.

Những câu hỏi đó cần VB/MO/quantum chemistry.

# Những hiểu lầm thường gặp

### “Lone pair là quả bóng lớn hơn bond pair”

Không. Đây là shorthand cho spatial electron density và repulsion hiệu dụng.

### “Double bond tính hai electron domains”

Không trong VSEPR cơ bản; nó là một directional lĩnh vực (domain / 도메인) nhưng thường repulsive hơn single bond.

### “VSEPR cho chính xác (exact / 정확한) bond angles”

Không. Nó dự đoán hình học (geometry / 기하학) lớp (class / 클래스) và qualitative distortions.

### “Molecule không polar nếu có bonds giống nhau”

Không. Cần véc-tơ (vector / 벡터) symmetry của toàn hình học (geometry / 기하학).

### “VSEPR dùng tốt như nhau cho chuyển tiếp (transition / 전이) metals”

Không. Ligand-field/electronic cấu trúc (structure / 구조) thường quan trọng hơn.

## Mô hình tư duy

VSEPR là **bộ chuyển đổi từ electron bookkeeping sang spatial mô hình (model / 모델)**:

```text
Lewis electron domains
→ arrangement giảm crowding
→ positions của nuclei
→ symmetry
→ dipole / recognition / reactivity
```

Nó mạnh ở shape prediction, nhưng phải chuyển sang VB/MO khi câu hỏi trở thành “electron thực sự được tổ chức bằng orbital như thế nào?”.

Xem tiếp: [Lý thuyết liên kết hóa trị và lai hóa](./05_valence_bond_and_hybridization.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 why atoms bond](./00_why_atoms_bond.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
