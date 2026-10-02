# Vật lý phân tử: liên kết, quay, dao động, orbital phân tử và quang phổ học

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Vật lý phân tử: liên kết, quay, dao động, orbital phân tử và quang phổ học**. Route đi từ nguyên tử → xấp xỉ Born–Oppenheimer → liên kết/orbital → quay và dao động → phổ phân tử, để cấu trúc nối với tín hiệu đo được.

## Từ nguyên tử đến phân tử

Một phân tử không chỉ là nhiều nguyên tử đứng gần nhau. Nó là một hệ lượng tử liên kết trong đó electron và hạt nhân cùng tạo ra trạng thái có năng lượng thấp hơn một số cấu hình nguyên tử tách rời.

Câu hỏi vật lý cốt lõi là: khi vị trí các hạt nhân thay đổi, Hamiltonian của electron thay đổi thế nào, và tổng năng lượng gồm năng lượng điện tử cùng lực đẩy hạt nhân–hạt nhân có đạt cực tiểu ở một hình học nào hay không.

Vật lý phân tử (Molecular Physics / 분자물리학) là cầu nối trực tiếp giữa cơ học lượng tử và hóa học. Liên kết hóa học, orbital phân tử và lai hóa đều là những ngôn ngữ khác nhau để tổ chức bài toán nhiều electron.

> **Chuyển mạch:** Trong **Vật lý phân tử: liên kết, quay, dao động, orbital phân tử và quang phổ học**, **Xấp xỉ Born–Oppenheimer** tiếp nhận điểm tựa từ **Từ nguyên tử đến phân tử** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đường cong thế năng và liên kết** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Xấp xỉ Born–Oppenheimer

Hạt nhân nặng hơn electron hàng nghìn lần, nên chuyển động hạt nhân thường chậm hơn chuyển động electron. Xấp xỉ Born–Oppenheimer (Born–Oppenheimer approximation / 보른-오펜하이머 근사) tận dụng sự tách thang thời gian này.

Ta tạm giữ vị trí các hạt nhân `R_A` gần như cố định rồi giải bài toán điện tử:

```math
H_{\mathrm{electronic}}(\{R_A\})\psi_e
=E_e(\{R_A\})\psi_e.
```

Năng lượng điện tử `E_e` cùng lực đẩy giữa các hạt nhân tạo thành một bề mặt thế năng (potential energy surface) cho chuyển động hạt nhân.

Xấp xỉ này không luôn đúng. Gần các điểm suy biến điện tử hoặc trong chuyển mức không đoạn nhiệt (nonadiabatic transition), chuyển động electron và hạt nhân có thể liên kết mạnh. Tuy nhiên nó giải thích vì sao các khái niệm như độ dài liên kết, góc liên kết và chế độ (mode / 모드) dao động có ý nghĩa rõ ràng.

> **Chuyển mạch:** Ở chặng này của **Vật lý phân tử: liên kết, quay, dao động, orbital phân tử và quang phổ học**, sau nội dung của **Xấp xỉ Born–Oppenheimer**, **Đường cong thế năng và liên kết** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Orbital liên kết và phản liên kết** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đường cong thế năng và liên kết

Với phân tử hai nguyên tử, tổng thế năng theo khoảng cách liên hạt nhân `R` thường có một cực tiểu. Ở `R` rất lớn, hai nguyên tử gần như độc lập. Khi tiến lại gần vừa phải, sự tái phân bố electron có thể hạ năng lượng. Nếu quá gần, lực đẩy hạt nhân–hạt nhân cùng chi phí động năng và nguyên lý Pauli làm năng lượng tăng mạnh.

Gần vị trí cân bằng `R_0`, khai triển Taylor cho

```math
V(R)\approx V(R_0)+\frac12k(R-R_0)^2+\cdots.
```

Số hạng tuyến tính biến mất tại cực tiểu. Vì vậy dao động nhỏ quanh cấu hình bền tự nhiên gần với dao động điều hòa. Đây là lý do mô hình dao động tử điều hòa xuất hiện rộng khắp vật lý, không chỉ vì nó dễ tính.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vật lý phân tử: liên kết, quay, dao động, orbital phân tử và quang phổ học**, **Orbital liên kết và phản liên kết** tiếp nhận điểm tựa từ **Đường cong thế năng và liên kết** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cộng hóa trị, ion và van der Waals** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Orbital liên kết và phản liên kết

Xét hai orbital nguyên tử `\phi_A` và `\phi_B`. Tổ hợp đối xứng

```math
\psi_+\propto\phi_A+\phi_B
```

có thể làm tăng mật độ electron giữa hai hạt nhân và hạ năng lượng, tạo orbital liên kết (bonding orbital).

Tổ hợp phản đối xứng

```math
\psi_-\propto\phi_A-\phi_B
```

có nút giữa hai hạt nhân và thường có năng lượng cao hơn, tạo orbital phản liên kết (antibonding orbital).

Điều quan trọng là hiểu giao thoa của biên độ lượng tử làm thay đổi phân bố electron; phân bố đó lại thay đổi động năng và thế năng Coulomb. Liên kết hóa học vì thế liên hệ trực tiếp với chồng chập và giao thoa lượng tử.

Trong mô hình orbital phân tử đơn giản, bậc liên kết (bond order) có thể viết

```math
\text{bond order}=\frac{N_b-N_a}{2},
```

với `N_b` và `N_a` là số electron ở orbital liên kết và phản liên kết. Đây là công cụ hữu ích nhưng không phải định nghĩa duy nhất cho mọi hệ phân tử phức tạp.

> **Chuyển mạch:** Trong **Vật lý phân tử: liên kết, quay, dao động, orbital phân tử và quang phổ học**, **Cộng hóa trị, ion và van der Waals** tiếp nhận điểm tựa từ **Orbital liên kết và phản liên kết** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Trạng thái quay của phân tử** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cộng hóa trị, ion và van der Waals

Liên kết cộng hóa trị nhấn mạnh sự chia sẻ mật độ electron và trộn orbital. Liên kết ion nhấn mạnh chuyển điện tích và lực hút tĩnh điện giữa các ion. Trong phân tử thật, tính chất liên kết có thể nằm trên một phổ liên tục thay vì thuộc hoàn toàn một loại.

Ngoài liên kết hóa học mạnh còn có tương tác lưỡng cực–lưỡng cực, liên kết hydro và lực van der Waals. Lực phân tán London xuất hiện ngay cả giữa các nguyên tử hay phân tử không phân cực, vì thăng giáng lượng tử tức thời của điện tích tạo ra các lưỡng cực tương quan.

Điều này cho thấy “mômen lưỡng cực trung bình bằng không” không có nghĩa mọi thăng giáng tức thời đều bằng không.

> **Chuyển mạch:** Ở chặng này của **Vật lý phân tử: liên kết, quay, dao động, orbital phân tử và quang phổ học**, **Trạng thái quay của phân tử** tiếp nhận điểm tựa từ **Cộng hóa trị, ion và van der Waals** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Trạng thái dao động** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trạng thái quay của phân tử

Phân tử hai nguyên tử có thể được gần đúng như một rotor cứng. Năng lượng quay là

```math
E_J=\frac{\hbar^2}{2I}J(J+1),
```

với `J=0,1,2,...` và `I` là mômen quán tính.

Khoảng cách giữa các mức quay phụ thuộc vào `1/I`, nên quang phổ quay có thể dùng để suy ra mômen quán tính và từ đó suy ra độ dài liên kết.

Không phải mọi chuyển mức quay đều được phép. Quy tắc chọn phụ thuộc đối xứng phân tử và cách mômen lưỡng cực tương tác với trường điện từ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vật lý phân tử: liên kết, quay, dao động, orbital phân tử và quang phổ học**, **Trạng thái dao động** tiếp nhận điểm tựa từ **Trạng thái quay của phân tử** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chế độ (mode / 모드) chuẩn của phân tử nhiều nguyên tử** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trạng thái dao động

Trong xấp xỉ điều hòa, mức năng lượng dao động là

```math
E_v=\hbar\omega\left(v+\frac12\right),
```

với `v=0,1,2,...`.

Ngay cả trạng thái cơ bản `v=0` vẫn có năng lượng điểm không `\frac12\hbar\omega`, nên hạt nhân không đứng yên tuyệt đối tại vị trí cân bằng.

Thế phân tử thật không hoàn toàn điều hòa. Khi kích thích tăng, khoảng cách mức thường thay đổi và cuối cùng phân tử có thể phân ly.

> **Chuyển mạch:** Trong **Vật lý phân tử: liên kết, quay, dao động, orbital phân tử và quang phổ học**, **Chế độ (mode / 모드) chuẩn của phân tử nhiều nguyên tử** tiếp nhận điểm tựa từ **Trạng thái dao động** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Quang phổ hồng ngoại và Raman** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chế độ (mode / 모드) chuẩn của phân tử nhiều nguyên tử

Một phân tử phi tuyến gồm `N` nguyên tử thường có `3N-6` bậc tự do dao động; phân tử tuyến tính có `3N-5`.

Mỗi chế độ (mode / 모드) chuẩn (normal mode / 정상 모드) là một mẫu dao động tập thể của nhiều nguyên tử. Về mặt toán học, các chế độ (mode / 모드) được tìm bằng cách chéo hóa ma trận Hessian có trọng số khối lượng của thế năng. Vì vậy đại số tuyến tính và bài toán trị riêng xuất hiện trực tiếp trong quang phổ phân tử.

> **Chuyển mạch:** Ở chặng này của **Vật lý phân tử: liên kết, quay, dao động, orbital phân tử và quang phổ học**, **Quang phổ hồng ngoại và Raman** tiếp nhận điểm tựa từ **Chế độ (mode / 모드) chuẩn của phân tử nhiều nguyên tử** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chuyển mức điện tử và huỳnh quang** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quang phổ hồng ngoại và Raman

Một chế độ (mode / 모드) dao động hấp thụ hồng ngoại mạnh khi dao động làm thay đổi mômen lưỡng cực điện của phân tử. Tán xạ Raman nhạy với sự thay đổi độ phân cực hóa (polarizability).

Vì hai cơ chế có quy tắc chọn khác nhau, phổ hồng ngoại và Raman bổ sung cho nhau khi xác định đối xứng, liên kết và cấu trúc phân tử.

Trong kỹ thuật và sinh học, các phương pháp này cho phép phân tích khí, vật liệu, protein hay chất ô nhiễm mà không cần phá mẫu. Trong công nghệ bán dẫn, Raman còn được dùng để khảo sát ứng suất và dao động mạng tinh thể.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vật lý phân tử: liên kết, quay, dao động, orbital phân tử và quang phổ học**, **Chuyển mức điện tử và huỳnh quang** tiếp nhận điểm tựa từ **Quang phổ hồng ngoại và Raman** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Va chạm phân tử và quãng đường tự do trung bình** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chuyển mức điện tử và huỳnh quang

Trạng thái điện tử kích thích thường có thang năng lượng lớn hơn trạng thái quay và dao động. Khi phân tử hấp thụ photon, chuyển mức điện tử có thể đi kèm thay đổi trạng thái dao động.

Nguyên lý Franck–Condon phản ánh việc hạt nhân nặng gần như không kịp dịch chuyển trong thời gian rất ngắn của một chuyển mức điện tử.

Sau khi hồi phục một phần năng lượng bằng các quá trình không bức xạ, phân tử có thể phát photon năng lượng thấp hơn photon hấp thụ. Sự chênh lệch này liên hệ với dịch Stokes (Stokes shift) và là nền tảng của nhiều kỹ thuật huỳnh quang.

> **Chuyển mạch:** Trong **Vật lý phân tử: liên kết, quay, dao động, orbital phân tử và quang phổ học**, **Va chạm phân tử và quãng đường tự do trung bình** tiếp nhận điểm tựa từ **Chuyển mức điện tử và huỳnh quang** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tính toán cấu trúc phân tử** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Va chạm phân tử và quãng đường tự do trung bình

Vật lý phân tử nối trực tiếp sang lý thuyết động học chất khí. Quãng đường tự do trung bình có bậc

```math
\ell\sim\frac{1}{\sqrt2\,n\sigma},
```

trong đó `n` là mật độ số hạt và `\sigma` là tiết diện va chạm (collision cross section).

Tiết diện không đơn giản bằng diện tích hình học của phân tử. Nó phụ thuộc năng lượng, thế tương tác và tán xạ lượng tử.

Khi `\ell` nhỏ hơn nhiều kích thước hệ, mô hình chất lưu liên tục thường phù hợp. Khi `\ell` cùng bậc hoặc lớn hơn kích thước hệ, như trong chân không cao hay tầng khí quyển trên, mô tả động học phân tử trở nên cần thiết.

> **Chuyển mạch:** Ở chặng này của **Vật lý phân tử: liên kết, quay, dao động, orbital phân tử và quang phổ học**, **Tính toán cấu trúc phân tử** tiếp nhận điểm tựa từ **Va chạm phân tử và quãng đường tự do trung bình** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tính toán cấu trúc phân tử

Với phân tử nhiều electron, phương trình Schrödinger chính xác gần như không thể giải giải tích. Hóa học lượng tử dùng các phương pháp xấp xỉ như Hartree–Fock, lý thuyết phiếm hàm mật độ (Density Functional Theory, DFT), tương tác cấu hình và coupled-cluster.

Chi phí tính toán tăng rất nhanh theo kích thước hệ, nên lựa chọn mô hình vật lý và thuật toán luôn đi cùng nhau. Mô phỏng phân tử có thể dùng trường lực cổ điển, động lực học phân tử, phương pháp ab initio hoặc mô hình lai QM/MM tùy câu hỏi cần trả lời.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vật lý phân tử: liên kết, quay, dao động, orbital phân tử và quang phổ học**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Tính toán cấu trúc phân tử** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những ngộ nhận thường gặp (Common Misconceptions)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Phân tử là một hệ lượng tử có cấu trúc phân tầng. Electron tạo bề mặt thế năng; hạt nhân chuyển động trên bề mặt đó; gần hình học bền, chuyển động quay và dao động được lượng tử hóa; bức xạ điện từ đọc các chênh lệch mức năng lượng thành phổ.

Cùng một “cảnh quan năng lượng” giải thích hình học phân tử, độ bền liên kết, phổ và nhiều đường phản ứng hóa học.

> **Chuyển mạch:** Trong **Vật lý phân tử: liên kết, quay, dao động, orbital phân tử và quang phổ học**, **Những ngộ nhận thường gặp (Common Misconceptions)** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Liên kết hóa học chỉ là electron nằm giữa hai nguyên tử”

Không đủ. Năng lượng liên kết là kết quả của động năng electron, lực hút electron–hạt nhân, lực đẩy electron–electron và hạt nhân–hạt nhân, cùng hiệu ứng trao đổi và tương quan lượng tử.

### “Phân tử có một hình dạng cứng tuyệt đối”

Không. Hạt nhân luôn có dao động điểm không và chuyển động nhiệt. Hình học phân tử thường là cấu hình cân bằng hoặc cấu trúc trung bình của một hệ lượng tử động.

### “Vạch phổ chỉ cho biết màu”

Không. Tần số vạch cho chênh lệch năng lượng, còn mẫu vạch và cường độ có thể cho mômen quán tính, độ cứng liên kết, đối xứng và cấu trúc điện tử.

> **Chuyển mạch:** Ở chặng này của **Vật lý phân tử: liên kết, quay, dao động, orbital phân tử và quang phổ học**, sau nội dung của **Những ngộ nhận thường gặp (Common Misconceptions)**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

**Nên hiểu trước:** [Vật lý nguyên tử](00_atomic_physics.md), [Các hệ lượng tử](../08_quantum/01_quantum_systems.md), [Mômen động lượng và spin](../08_quantum/02_angular_momentum_spin.md).

**Liên hệ tiếp:** [Cơ học thống kê](../04_thermal_statistical/01_entropy_statistical_mechanics.md), [Quang học sóng](../06_optics/01_wave_optics.md), [Tinh thể và dải năng lượng](../10_condensed_matter_devices/00_crystals_bands.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
