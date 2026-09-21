# Cấu hình electron

> **Cấu hình electron (electron configuration / 전자 배치)** mô tả cách các electron của một nguyên tử hoặc ion phân bố vào các obitan lượng tử có thể chiếm. Mục tiêu không phải học thuộc chuỗi `1s² 2s² 2p⁶...`, mà là hiểu vì sao cách sắp xếp electron quyết định tính tuần hoàn, liên kết hóa học và khả năng phản ứng của nguyên tố.

## Từ obitan đến nguyên tử nhiều electron

Ở nguyên tử hydrogen chỉ có một electron nên câu hỏi “electron nằm ở trạng thái nào?” tương đối trực tiếp. Với helium, carbon hay iron, ta phải giải quyết thêm hai vấn đề. Thứ nhất, electron là fermion nên không thể tùy ý chiếm cùng một trạng thái lượng tử. Thứ hai, electron đẩy nhau, vì vậy năng lượng của obitan trong nguyên tử nhiều electron không còn chỉ phụ thuộc số lượng tử chính `n`.

Cấu hình electron là cách Hóa học tổ chức bài toán nhiều electron thành một mô hình có thể sử dụng được.

Xem nền tảng: [Mô hình lượng tử của nguyên tử](./02_quantum_model_of_atom.md).

## Nguyên lý loại trừ Pauli

**Nguyên lý loại trừ Pauli (Pauli exclusion principle / 파울리 배타 원리)** phát biểu rằng không có hai electron trong cùng một nguyên tử có thể có cùng toàn bộ bốn số lượng tử.

Một obitan được xác định bởi `n`, `l` và `m_l`. Vì số lượng tử spin chỉ có hai giá trị `+1/2` và `-1/2`, mỗi obitan chứa tối đa hai electron và hai electron đó phải có spin đối nhau.

Do đó một phân lớp s chứa tối đa 2 electron, p chứa 6, d chứa 10 và f chứa 14:

\[
\text{sức chứa}=2(2l+1)
\]

Hệ số `2l+1` là số obitan trong phân lớp, còn hệ số 2 đến từ hai trạng thái spin.

## Nguyên lý Aufbau

**Nguyên lý Aufbau (Aufbau principle / 쌓음 원리)** nói rằng ở trạng thái cơ bản, electron có xu hướng chiếm các obitan năng lượng thấp trước rồi mới đến các obitan năng lượng cao hơn.

Thứ tự gần đúng thường dùng là:

```text
1s
2s 2p
3s 3p
4s 3d 4p
5s 4d 5p
6s 4f 5d 6p
7s 5f 6d 7p
```

Một quy tắc ghi nhớ phổ biến là quy tắc `n+l`: obitan có `n+l` nhỏ hơn thường có năng lượng thấp hơn; nếu bằng nhau, obitan có `n` nhỏ hơn thường được điền trước.

Tuy nhiên đây là **quy tắc sắp xếp gần đúng (approximate ordering rule)**, không phải định luật cơ bản tuyệt đối. Với nguyên tử nhiều electron, năng lượng obitan phụ thuộc che chắn, khả năng xuyên thấu và tương tác electron–electron. Đây là nguồn gốc của các trường hợp ngoại lệ.

## Quy tắc Hund

Trong một nhóm obitan suy biến, chẳng hạn ba obitan p, electron sẽ điền đơn lẻ vào các obitan với spin song song trước khi ghép đôi. Đây là **quy tắc Hund (Hund's rule / 훈트 규칙)**.

Ví dụ carbon có sáu electron:

```text
1s  ↑↓
2s  ↑↓
2p  ↑   ↑   _
```

chứ không ưu tiên:

```text
2p  ↑↓  _   _
```

Lý do sâu hơn không đơn giản là “electron ghét ở chung”. Sự kết hợp giữa lực đẩy electron–electron và **ổn định trao đổi (exchange stabilization)** khiến cách phân bố electron độc thân trên các obitan suy biến thường có năng lượng thấp hơn.

## Cách viết cấu hình electron

Oxygen có số hiệu nguyên tử 8, nên nguyên tử trung hòa có 8 electron:

\[
1s^2\,2s^2\,2p^4
\]

Có thể dùng **cách viết rút gọn theo khí hiếm (noble-gas shorthand)**:

\[
[He]\,2s^2\,2p^4
\]

Iron, `Z=26`:

\[
[Ar]\,4s^2\,3d^6
\]

Việc đặt `4s` trước `3d` trong ký hiệu phản ánh thứ tự điền gần đúng, nhưng không nên suy diễn rằng `4s` luôn thấp năng lượng hơn `3d` trong mọi ion hoặc mọi trạng thái.

## Thứ tự điền và thứ tự ion hóa không giống nhau

Ở nguyên tử kim loại chuyển tiếp trung hòa, `4s` thường được điền trước `3d`. Nhưng khi tạo cation, electron `4s` thường bị loại trước electron `3d`.

Ví dụ:

\[
Fe: [Ar]4s^2 3d^6
\]

\[
Fe^{2+}: [Ar]3d^6
\]

Điều này không mâu thuẫn nếu ta nhớ rằng năng lượng obitan thay đổi khi số electron chiếm và điện tích hạt nhân hiệu dụng thay đổi. “Thứ tự obitan” không phải một bảng cố định độc lập với trạng thái của nguyên tử.

## Ngoại lệ: chromium và copper

Theo quy tắc Aufbau đơn giản, chromium có thể được dự đoán là:

\[
[Ar]4s^2 3d^4
\]

nhưng cấu hình trạng thái cơ bản quan sát được gần với:

\[
[Ar]4s^1 3d^5
\]

Copper tương tự:

\[
[Ar]4s^1 3d^{10}
\]

thay vì `[Ar]4s²3d⁹`.

Không nên giải thích ngoại lệ chỉ bằng câu “phân lớp bán bão hòa và bão hòa hoàn toàn bền hơn”. Đó chỉ là quy tắc ghi nhớ. Nguồn gốc thực sự liên quan đến chênh lệch năng lượng rất nhỏ giữa `4s` và `3d`, tương quan electron, hiệu ứng trao đổi và tổng năng lượng của toàn nguyên tử.

## Electron hóa trị

**Electron hóa trị (valence electrons / 원자가 전자)** là các electron quan trọng nhất đối với liên kết và phản ứng hóa học. Với các nguyên tố nhóm chính, chúng thường là electron ở lớp có `n` lớn nhất.

Ví dụ sulfur:

\[
[Ne]3s^2 3p^4
\]

có 6 electron hóa trị trong mô hình thông thường của nguyên tố nhóm chính.

Khái niệm này giúp giải thích vì sao các nguyên tố trong cùng một nhóm của bảng tuần hoàn có hóa học tương tự: chúng có mẫu cấu hình electron hóa trị giống nhau.

## Electron lõi và hiệu ứng che chắn

Các electron nằm sâu bên trong gọi là **electron lõi (core electrons)**. Trong nhiều phản ứng thông thường chúng ít thay đổi hơn electron hóa trị.

Electron lõi che chắn một phần điện tích dương của hạt nhân đối với electron ngoài. Vì vậy electron ngoài cùng cảm nhận **điện tích hạt nhân hiệu dụng (effective nuclear charge)** nhỏ hơn `Z`.

Khi đi từ trái sang phải trong một chu kỳ, điện tích hạt nhân tăng nhanh hơn mức che chắn giữa các electron cùng lớp. Đây là bước nối trực tiếp sang các xu hướng tuần hoàn.

## Tính thuận từ và nghịch từ

Cấu hình electron cho phép dự đoán hành vi từ.

Một tiểu phần có một hay nhiều electron độc thân thường **thuận từ (paramagnetic / 상자성)** và bị hút vào từ trường. Nếu tất cả electron đều ghép đôi, tiểu phần thường **nghịch từ (diamagnetic / 반자성)**.

Ví dụ nguyên tử oxygen `2p⁴` có hai electron độc thân theo quy tắc Hund nên thuận từ.

Phân tử `O2` cũng thuận từ, nhưng cấu trúc Lewis đơn giản không giải thích được. Lý thuyết obitan phân tử sẽ giải thích điều đó ở phần liên kết.

## Cấu hình electron và bảng tuần hoàn

Bảng tuần hoàn không chỉ là danh sách nguyên tố. Các khối của bảng phản ánh phân lớp đang được điền:

- khối s tương ứng với việc điền phân lớp s;
- khối p tương ứng với phân lớp p;
- khối d tương ứng với kim loại chuyển tiếp;
- khối f tương ứng với lanthanide và actinide.

Đây là lý do bảng tuần hoàn có hình dạng không phải một hình chữ nhật đồng đều.

## Ion và cấu hình giống khí hiếm

Nhiều nguyên tử nhóm chính tạo ion có cấu hình electron gần khí hiếm, nhưng cần hiểu đây là **mẫu quan sát (pattern)** chứ không phải “mục tiêu” có ý thức của nguyên tử.

Sodium:

\[
Na:[Ne]3s^1
\]

mất một electron:

\[
Na^+:[Ne]
\]

Chlorine:

\[
Cl:[Ne]3s^2 3p^5
\]

nhận một electron:

\[
Cl^-:[Ar]
\]

Sự hình thành ion thực tế phải được đánh giá bằng tổng năng lượng của toàn quá trình, bao gồm năng lượng ion hóa, ái lực electron, năng lượng mạng hoặc năng lượng solvat hóa. Không phải cứ “đạt octet” là tự động thuận lợi.

## Trạng thái cơ bản và trạng thái kích thích

Cấu hình electron thường được viết cho **trạng thái cơ bản (ground state / 바닥 상태)**, tức trạng thái năng lượng thấp nhất. Nếu hấp thụ năng lượng, electron có thể được kích thích lên obitan năng lượng cao hơn, tạo **trạng thái kích thích (excited state / 들뜬 상태)**.

Khi electron trở về mức thấp hơn, chênh lệch năng lượng có thể phát photon:

\[
\Delta E=h\nu
\]

Đây là liên hệ trực tiếp giữa cấu hình electron và quang phổ nguyên tử.

## Các hiểu lầm thường gặp

### “Electron thật sự xếp thành từng tầng giống các vòng tròn trong hình”

Không. Lớp và phân lớp là cấu trúc trạng thái lượng tử, không phải các lớp vật liệu hình cầu cứng.

### “4s luôn thấp hơn 3d”

Không. Thứ tự năng lượng phụ thuộc nguyên tử, ion và số electron đang chiếm.

### “Quy tắc octet là luật cơ bản của tự nhiên”

Không. Quy tắc octet là một **quy tắc kinh nghiệm (heuristic)** rất hữu ích cho nhiều hợp chất nhóm chính, nhưng có nhiều ngoại lệ và không thay thế lập luận năng lượng.

### “Electron ghép đôi vì hai electron hút nhau”

Electron cùng điện tích nên đẩy nhau. Ghép đôi xảy ra khi tổng năng lượng của việc ghép vào obitan thấp vẫn thuận lợi hơn việc đưa electron lên trạng thái khác có năng lượng cao hơn.

## Mô hình tư duy

Cấu hình electron là lời giải gần đúng cho một bài toán tối ưu năng lượng có ràng buộc:

- obitan năng lượng thấp được ưu tiên;
- Pauli giới hạn số electron trong mỗi trạng thái;
- Hund chi phối cách phân bố trong các obitan suy biến;
- tương tác electron–electron tạo che chắn, hiệu ứng trao đổi và ngoại lệ.

Nếu hiểu cấu hình electron theo cách này, bảng tuần hoàn trở thành kết quả tự nhiên thay vì một bảng cần học thuộc.

Xem tiếp: [Bảng tuần hoàn và các xu hướng tuần hoàn](./04_periodic_table_and_periodic_trends.md).