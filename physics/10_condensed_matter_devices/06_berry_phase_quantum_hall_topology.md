# Pha Berry, hiệu ứng Hall lượng tử và vật chất tô pô

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Berry phase, quantum Hall effect và topological matter**. Route đi từ band structure → adiabatic connection/Berry phase → Chern number → edge states/Hall response → disorder and protection, để topology nối hình học với quan sát vật lý.

## Vì sao topology cần nhiều hơn khái niệm band gap?

Lý thuyết dải giải thích rất nhiều về kim loại, bán dẫn và chất cách điện. Nhưng hai vật liệu đều có gap trong bulk vẫn có thể thuộc hai pha khác nhau theo cách không thể biến đổi liên tục từ pha này sang pha kia mà không đóng gap hoặc phá một đối xứng bảo vệ.

Sự khác biệt đó có thể được mã hóa bởi **bất biến tô pô (topological invariant / 위상 불변량)** của các trạng thái lượng tử trong không gian động lượng.

Để hiểu nguồn gốc của bất biến này, trước tiên cần hiểu pha hình học.

> **Chuyển mạch:** Trong **Pha Berry, hiệu ứng Hall lượng tử và vật chất tô pô**, **Tiến hóa đoạn nhiệt và pha Berry** tiếp nhận điểm tựa từ **Vì sao topology cần nhiều hơn khái niệm band gap?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Berry liên kết (connection / 연결) và Berry curvature** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tiến hóa đoạn nhiệt và pha Berry

Giả sử Hamiltonian phụ thuộc vào một tập tham số thay đổi chậm `\mathbf R`:

```math
H(\mathbf R)|n(\mathbf R)\rangle
=E_n(\mathbf R)|n(\mathbf R)\rangle.
```

Nếu hệ bắt đầu ở một trạng thái riêng không suy biến và tham số thay đổi đủ chậm so với gap năng lượng thích hợp, định lý đoạn nhiệt nói trạng thái sẽ gần như bám theo trạng thái riêng tức thời.

Sau một vòng kín trong không gian tham số, trạng thái nhận hai loại pha:

- pha động lực học do tích phân năng lượng theo thời gian;
- pha hình học phụ thuộc đường đi trong không gian tham số.

Pha hình học Berry là

```math
\gamma_n
=i\oint
\langle n(\mathbf R)|\nabla_{\mathbf R}n(\mathbf R)\rangle
\cdot d\mathbf R.
```

Pha của véc-tơ (vector / 벡터) riêng tại từng điểm có tự do gauge:

```math
|n\rangle
\to e^{i\alpha(\mathbf R)}|n\rangle.
```

Nhưng pha Berry quanh vòng kín, modulo `2\pi`, có nội dung vật lý gauge-invariant.

> **Chuyển mạch:** Ở chặng này của **Pha Berry, hiệu ứng Hall lượng tử và vật chất tô pô**, **Berry liên kết (connection / 연결) và Berry curvature** tiếp nhận điểm tựa từ **Tiến hóa đoạn nhiệt và pha Berry** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hình học của dải Bloch trong không gian k** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Berry liên kết (connection / 연결) và Berry curvature

Định nghĩa Berry liên kết (connection / 연결):

```math
\mathbf A_n(\mathbf R)
=i\langle n|\nabla_{\mathbf R}n\rangle.
```

Berry curvature là

```math
\mathbf\Omega_n
=\nabla_{\mathbf R}\times\mathbf A_n.
```

Bằng định lý Stokes,

```math
\gamma_n
=\int_S\mathbf\Omega_n\cdot d\mathbf S.
```

Cấu trúc này rất giống điện từ học:

- Berry liên kết (connection / 연결) tương tự thế vectơ;
- Berry curvature tương tự trường dữ liệu (field / 필드) strength;
- liên kết (connection / 연결) phụ thuộc gauge;
- các đại lượng tích phân phù hợp có nội dung gauge-invariant.

Không gian tham số ở đây có thể là không gian động lượng `\mathbf k`, hướng từ trường hoặc tập tham số điều khiển khác.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Pha Berry, hiệu ứng Hall lượng tử và vật chất tô pô**, **Hình học của dải Bloch trong không gian k** tiếp nhận điểm tựa từ **Berry liên kết (connection / 연결) và Berry curvature** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hiệu ứng Hall lượng tử nguyên** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hình học của dải Bloch trong không gian k

Trạng thái Bloch có dạng

```math
|\psi_{n\mathbf k}\rangle
=e^{i\mathbf k\cdot\mathbf r}
|u_{n\mathbf k}\rangle.
```

Phần tuần hoàn `|u_{n\mathbf k}\rangle` thay đổi theo `\mathbf k`. Chính sự biến đổi này tạo Berry liên kết (connection / 연결) và Berry curvature trong Brillouin zone.

Trong động lực bán cổ điển của wavepacket electron,

```math
\dot{\mathbf r}
=
\frac{1}{\hbar}\nabla_{\mathbf k}E_n
-
\dot{\mathbf k}\times\mathbf\Omega_n(\mathbf k).
```

Hạng thứ hai là vận tốc dị thường (anomalous velocity), có thể tạo đáp ứng ngang mà mô hình Drude đơn giản không có.

> **Chuyển mạch:** Trong **Pha Berry, hiệu ứng Hall lượng tử và vật chất tô pô**, **Hiệu ứng Hall lượng tử nguyên** tiếp nhận điểm tựa từ **Hình học của dải Bloch trong không gian k** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Số Chern là thuộc tính toàn cục** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hiệu ứng Hall lượng tử nguyên

Trong hệ electron 2D dưới từ trường vuông góc mạnh, chuyển động cyclotron bị lượng tử hóa thành các mức Landau.

Thực nghiệm cho độ dẫn Hall theo plateau:

```math
\sigma_{xy}
=\nu\frac{e^2}{h},
```

với `\nu` nguyên trong hiệu ứng Hall lượng tử nguyên.

Điểm sâu hơn Landau quantization là độ dẫn Hall có thể liên hệ với số Chern của các dải đã chiếm:

```math
C_n
=\frac{1}{2\pi}
\int_{BZ}\Omega_n(\mathbf k)\,d^2k.
```

Vì `C_n` là số nguyên, nhiễu nhỏ hoặc thay đổi tham số liên tục không dễ đổi giá trị này nếu bulk gap thích hợp vẫn mở.

Đây là nguồn gốc của độ bền đáng kinh ngạc của lượng tử hóa Hall.

> **Chuyển mạch:** Ở chặng này của **Pha Berry, hiệu ứng Hall lượng tử và vật chất tô pô**, **Số Chern là thuộc tính toàn cục** tiếp nhận điểm tựa từ **Hiệu ứng Hall lượng tử nguyên** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bulk–ranh giới (boundary / 경계) correspondence** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Số Chern là thuộc tính toàn cục

Topology không chỉ hỏi trạng thái tại một điểm `\mathbf k`. Nó hỏi các véc-tơ (vector / 벡터) riêng được nối với nhau trên toàn Brillouin zone như thế nào.

Tại từng vùng cục bộ, ta thường có thể chọn pha trạng thái trơn. Nhưng trên toàn không gian tham số, có thể không tồn tại một gauge trơn duy nhất ở mọi nơi.

Trở ngại toàn cục này được đo bằng bất biến tô pô.

Một trực giác đơn giản là winding number: một vòng có số lần quấn nguyên và biến dạng nhỏ không đổi số nguyên đó trừ khi đường đi qua singularity.

Trong band topology, đóng gap đóng vai trò như điểm singular cho phép bất biến đổi giá trị.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Pha Berry, hiệu ứng Hall lượng tử và vật chất tô pô**, **Số Chern là thuộc tính toàn cục** đã nêu tiêu chí phân biệt, còn **Bulk–ranh giới (boundary / 경계) correspondence** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Topological insulator và đối xứng đảo thời gian** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bulk–ranh giới (boundary / 경계) correspondence

Nếu hai vùng bulk có bất biến tô pô khác nhau, giao diện (interface / 인터페이스) giữa chúng phải giải quyết sự thay đổi bất biến.

Trong nhiều hệ, điều này buộc xuất hiện trạng thái biên nối các sector năng lượng.

Trong hiệu ứng Hall lượng tử, bulk có gap nhưng cạnh có kênh dẫn chiral. Trong trường hợp lý tưởng, kênh chỉ truyền theo một chiều nên backscattering đàn hồi bị hạn chế mạnh.

Đây là bulk–ranh giới (boundary / 경계) correspondence: topology của bulk quyết định sự tồn tại của chế độ (mode / 모드) biên.

> **Chuyển mạch:** Trong **Pha Berry, hiệu ứng Hall lượng tử và vật chất tô pô**, **Bulk–ranh giới (boundary / 경계) correspondence** đã nêu tiêu chí phân biệt, còn **Topological insulator và đối xứng đảo thời gian** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Spin–orbit coupling: từ tương đối tính nguyên tử đến topology vật liệu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Topological insulator và đối xứng đảo thời gian

Không phải pha tô pô nào cũng cần từ trường ngoài.

Topological insulator 2D hoặc 3D có thể có bulk gap nhờ spin–orbit coupling và giữ đối xứng đảo thời gian. Bulk cách điện nhưng bề mặt hoặc cạnh chứa trạng thái dẫn được bảo vệ bởi symmetry.

“Được bảo vệ” không nghĩa không bao giờ tán xạ. Nó nghĩa một số cơ chế mở gap hoặc backscattering không thể xảy ra nếu symmetry bảo vệ và cấu trúc gap còn nguyên.

Tạp chất từ, tương tác, nhiệt độ, ghép giữa hai bề mặt hoặc đóng gap vẫn có thể phá hành vi lý tưởng.

> **Chuyển mạch:** Ở chặng này của **Pha Berry, hiệu ứng Hall lượng tử và vật chất tô pô**, **Spin–orbit coupling: từ tương đối tính nguyên tử đến topology vật liệu** tiếp nhận điểm tựa từ **Topological insulator và đối xứng đảo thời gian** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Pha Berry trong graphene** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Spin–orbit coupling: từ tương đối tính nguyên tử đến topology vật liệu

Spin–orbit coupling có nguồn gốc sâu từ hiệu chỉnh tương đối tính của electron trong điện trường nguyên tử.

Trong tinh thể, tương tác này có thể đảo thứ tự hoặc đặc trưng của các dải năng lượng. Khi xảy ra band inversion, hình học của hàm sóng Bloch có thể thay đổi và tạo pha tô pô.

Chuỗi kiến thức rất đẹp là

```text
special relativity
→ atomic spin–orbit coupling
→ crystal bands
→ band inversion
→ topological material
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Pha Berry, hiệu ứng Hall lượng tử và vật chất tô pô**, **Pha Berry trong graphene** tiếp nhận điểm tựa từ **Spin–orbit coupling: từ tương đối tính nguyên tử đến topology vật liệu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dirac và Weyl semimetal** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Pha Berry trong graphene

Quanh điểm Dirac của graphene, quasiparticle có pseudospin texture. Khi đi quanh điểm Dirac trong không gian động lượng, trạng thái có thể tích lũy pha Berry gần `\pi`.

Pha này ảnh hưởng:

- cấu trúc mức Landau;
- dao động lượng tử;
- weak localization;
- đáp ứng vận chuyển.

Câu “electron graphene là hạt tương đối tính không khối lượng” chỉ là mô tả hiệu dụng năng lượng thấp. Electron cơ bản trong chân không vẫn có khối lượng nghỉ.

> **Chuyển mạch:** Trong **Pha Berry, hiệu ứng Hall lượng tử và vật chất tô pô**, **Dirac và Weyl semimetal** tiếp nhận điểm tựa từ **Pha Berry trong graphene** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lý thuyết hiện đại của phân cực điện** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dirac và Weyl semimetal

Nếu hai dải chạm nhau tại các điểm cô lập với dispersion gần tuyến tính, quasiparticle năng lượng thấp có thể tuân Hamiltonian Dirac hoặc Weyl hiệu dụng.

Một Weyl nút (node / 노드) hoạt động như nguồn hoặc hố của Berry curvature trong không gian động lượng và mang topological charge.

Trên bề mặt, có thể xuất hiện Fermi arc nối hình chiếu của các Weyl nút (node / 노드).

Đây là ví dụ pha tô pô khi bulk không có gap hoàn toàn.

> **Chuyển mạch:** Ở chặng này của **Pha Berry, hiệu ứng Hall lượng tử và vật chất tô pô**, **Lý thuyết hiện đại của phân cực điện** tiếp nhận điểm tựa từ **Dirac và Weyl semimetal** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bơm Thouless** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lý thuyết hiện đại của phân cực điện

Trong tinh thể tuần hoàn vô hạn, công thức đơn giản “tổng điện tích nhân vị trí” gặp vấn đề vì vị trí tuyệt đối của electron trong trạng thái Bloch không phải đại lượng đơn giản.

Thay đổi phân cực của vật rắn có thể được biểu diễn bằng pha Berry của các dải đã chiếm.

Điều này cho thấy pha Berry không chỉ xuất hiện trong các vật liệu “kỳ lạ”; nó còn tham gia mô tả một đại lượng quen thuộc như phân cực điện.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Pha Berry, hiệu ứng Hall lượng tử và vật chất tô pô**, **Bơm Thouless** tiếp nhận điểm tựa từ **Lý thuyết hiện đại của phân cực điện** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hiệu ứng Hall lượng tử phân số** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bơm Thouless

Xét một chất cách điện 1D có Hamiltonian biến đổi đoạn nhiệt qua một chu kỳ.

Động lượng tinh thể và tham số chu kỳ tạo một không gian tham số 2D hiệu dụng. Điện tích được bơm trong mỗi chu kỳ có thể liên hệ với số Chern.

Trong điều kiện lý tưởng, điện tích bơm bị lượng tử hóa.

Đây là ví dụ trực tiếp nối bất biến tô pô với đại lượng vận chuyển đo được.

> **Chuyển mạch:** Trong **Pha Berry, hiệu ứng Hall lượng tử và vật chất tô pô**, **Hiệu ứng Hall lượng tử phân số** tiếp nhận điểm tựa từ **Bơm Thouless** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Berry curvature và anomalous Hall tác động (effect / 효과)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hiệu ứng Hall lượng tử phân số

Ở tương tác mạnh và filling phân số, độ dẫn Hall nhận các giá trị phân số.

Không thể giải thích đầy đủ bằng dải một hạt và số Chern đơn giản. Hệ tạo trạng thái nhiều hạt tương quan mạnh với quasiparticle có điện tích phân số và thống kê bất thường.

Hiệu ứng Hall lượng tử phân số mở đường tới khái niệm **topological thứ tự (order / 순서)**, nơi phân loại pha không chỉ dựa trên phá vỡ đối xứng Landau.

> **Chuyển mạch:** Ở chặng này của **Pha Berry, hiệu ứng Hall lượng tử và vật chất tô pô**, **Berry curvature và anomalous Hall tác động (effect / 효과)** tiếp nhận điểm tựa từ **Hiệu ứng Hall lượng tử phân số** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tính topology bằng số** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Berry curvature và anomalous Hall tác động (effect / 효과)

Vật liệu sắt từ hoặc có spin–orbit coupling mạnh có thể có Hall phản hồi (response / 응답) ngay cả khi không có từ trường ngoài lớn.

Phần nội tại của anomalous Hall conductivity liên hệ với tích phân Berry curvature của các trạng thái đã chiếm.

Do đó hình học của hàm sóng lượng tử có thể tạo hệ quả vận chuyển vĩ mô trực tiếp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Pha Berry, hiệu ứng Hall lượng tử và vật chất tô pô**, **Tính topology bằng số** tiếp nhận điểm tựa từ **Berry curvature và anomalous Hall tác động (effect / 효과)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vì sao bất biến chỉ đổi khi gap đóng?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tính topology bằng số

Trong tính toán vật liệu, các véc-tơ (vector / 벡터) riêng Bloch được lấy trên một lưới `k` rời rạc.

Không thể đơn giản sai phân pha thô của eigenvector vì mỗi véc-tơ (vector / 벡터) riêng có pha tùy ý tại từng điểm `k`.

Các thuật toán tốt dùng overlap gauge-covariant, Wilson vòng lặp (loop / 루프) hoặc phương pháp tương đương để giữ bất biến gauge.

Đây là bài học quan trọng cho scientific computing: biểu diễn số phải tôn trọng đối xứng và bất biến của lý thuyết, nếu không kết quả có thể phụ thuộc quy ước tùy ý.

> **Chuyển mạch:** Trong **Pha Berry, hiệu ứng Hall lượng tử và vật chất tô pô**, **Vì sao bất biến chỉ đổi khi gap đóng?** tiếp nhận điểm tựa từ **Tính topology bằng số** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Điều kiện đoạn nhiệt và giới hạn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vì sao bất biến chỉ đổi khi gap đóng?

Giả sử Hamiltonian thay đổi trơn theo tham số `\lambda` và dải đã chiếm luôn cách dải chưa chiếm bởi gap hữu hạn.

Khi đó eigenstate có thể biến dạng trơn theo `\lambda`. Một số nguyên tô pô không thể thay đổi liên tục từ `0` sang `1`.

Để bất biến nhảy, cấu trúc toán học phải mất tính trơn hoặc trở nên singular. Trong band lý thuyết (theory / 이론), điều này thường xảy ra khi gap đóng tại chuyển pha tô pô.

Sau đó gap có thể mở lại với topology mới.

> **Chuyển mạch:** Ở chặng này của **Pha Berry, hiệu ứng Hall lượng tử và vật chất tô pô**, **Vì sao bất biến chỉ đổi khi gap đóng?** đã nêu tiêu chí phân biệt, còn **Điều kiện đoạn nhiệt và giới hạn** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Điều kiện đoạn nhiệt và giới hạn

Pha Berry đoạn nhiệt giả sử thay đổi tham số chậm so với thang thời gian đặt bởi gap tới các trạng thái khác. Nếu đi qua degeneracy hoặc thay đổi quá nhanh, chuyển tiếp (transition / 전이) giữa các dải có thể xảy ra và mô tả đoạn nhiệt đơn giản thất bại.

Bất biến band một hạt rất mạnh với hệ electron gần độc lập, nhưng tương tác mạnh có thể đòi hỏi topology nhiều hạt, Green hàm (function / 함수) hoặc các công cụ khác.

Topological protection cũng không loại bỏ mọi nguồn điện trở thực nghiệm.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Pha Berry, hiệu ứng Hall lượng tử và vật chất tô pô**, các dấu vết trong **Điều kiện đoạn nhiệt và giới hạn** được đọc cùng nhau ở **Mô hình tư duy (mental model / 사고 모델)** để rút ra mô hình, thay vì giữ chúng như những quan sát rời. Từ đây, **Những ngộ nhận thường gặp (Common Misconceptions)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Lý thuyết dải thông thường hỏi **năng lượng của trạng thái là bao nhiêu**. Band topology hỏi thêm **các hàm sóng được ghép với nhau toàn cục như thế nào trên không gian động lượng**.

```text
Bloch states
→ Berry connection
→ Berry curvature
→ integral over parameter space
→ topological invariant
→ robust bulk response / boundary states
```

Pha Berry là thông tin hình học; số Chern là thông tin toàn cục.

> **Chuyển mạch:** Trong **Pha Berry, hiệu ứng Hall lượng tử và vật chất tô pô**, **Những ngộ nhận thường gặp (Common Misconceptions)** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Topological protection nghĩa thiết bị không có điện trở”

Không. Contact, tán xạ không đàn hồi, nhiệt độ, kênh phụ và phá symmetry vẫn có thể gây điện trở.

### “Pha Berry chỉ là một pha động lực học khác”

Không. Pha động lực học phụ thuộc tích phân năng lượng theo thời gian; pha Berry phụ thuộc đường đi trong không gian tham số và hình học của trạng thái riêng.

### “Topology chỉ là toán trừu tượng không đo được”

Không. Lượng tử hóa Hall, trạng thái biên, dao động lượng tử và thay đổi phân cực là các hệ quả đo được.

### “Chỉ cần thấy Dirac cone là chắc chắn có pha tô pô”

Không. Cần xét symmetry, gap, cấu trúc toàn cục của các dải và bất biến thích hợp.

> **Chuyển mạch:** Ở chặng này của **Pha Berry, hiệu ứng Hall lượng tử và vật chất tô pô**, sau nội dung của **Những ngộ nhận thường gặp (Common Misconceptions)**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

**Nên hiểu trước:** [Tinh thể và dải Bloch](00_crystals_bands.md), [Đối xứng lượng tử và tích phân đường](../08_quantum/07_symmetry_operator_path_integral.md), [Thế gauge](../05_electromagnetism/06_potentials_gauge.md).

**Liên hệ tiếp:** [Vận chuyển và Hall](02_transport_magnetism_superconductivity.md), [Phonon và vật chất tô pô](04_phonons_defects_topological_matter.md), [Thống kê lượng tử](../08_quantum/05_identical_particles_quantum_statistics.md), [QFT và gauge](../09_atomic_nuclear_particle/05_quantum_fields_symmetry_interactions.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
