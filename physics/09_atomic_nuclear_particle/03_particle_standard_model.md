# Hạt cơ bản, Mô hình Chuẩn, đối xứng và trường lượng tử

## Mô hình Chuẩn mô tả những gì?

Mô hình Chuẩn (Standard Model / 표준 모형) mô tả ba tương tác cơ bản: điện từ, yếu và mạnh. Nó không cung cấp một lý thuyết lượng tử hoàn chỉnh của hấp dẫn.

Các fermion vật chất được chia thành quark và lepton, sắp thành ba thế hệ. Sáu quark là `up, down, charm, strange, top, bottom`. Sáu lepton gồm electron, muon, tau và ba neutrino tương ứng.

Các boson chuẩn (gauge boson) liên hệ với tương tác: photon cho điện từ, gluon cho tương tác mạnh, còn `W^\pm` và `Z` cho tương tác yếu. Boson Higgs liên hệ với trường Higgs và cơ chế tạo khối lượng trong lý thuyết điện yếu.

## Đối xứng chuẩn (gauge symmetry)

Cấu trúc đối xứng của Mô hình Chuẩn được viết

```math
SU(3)_C\times SU(2)_L\times U(1)_Y.
```

Không cần xem biểu thức này như một mã phải học thuộc. Ý tưởng quan trọng là: nếu ta yêu cầu một phép biến đổi nội tại có thể thay đổi theo từng điểm trong không-thời gian nhưng các dự đoán vật lý vẫn bất biến, đạo hàm thông thường không còn biến đổi đúng cách. Ta phải đưa vào trường chuẩn và đạo hàm hiệp biến (covariant derivative).

Theo cách này, tương tác giữa trường vật chất và boson chuẩn xuất hiện từ yêu cầu đối xứng cục bộ chứ không phải được gắn thêm tùy ý.

`SU(3)_C` là đối xứng của sắc động lực học lượng tử (Quantum Chromodynamics, QCD). `SU(2)_L\times U(1)_Y` tạo phần điện yếu. Sau phá vỡ đối xứng điện yếu, các tổ hợp trường vật lý tương ứng với photon, `W` và `Z`.

## Cơ chế Higgs

Trường Higgs có giá trị kỳ vọng chân không khác không. Khi đối xứng điện yếu bị phá vỡ tự phát, tương tác của trường Higgs với các trường chuẩn làm `W` và `Z` có khối lượng trong khi photon vẫn không khối lượng. Khối lượng fermion xuất hiện thông qua tương tác Yukawa với Higgs.

Tuy nhiên phần lớn khối lượng proton không đến trực tiếp từ khối lượng nghỉ của các quark hóa trị. Năng lượng động lực học QCD, trường gluon và tương tác giam hãm đóng góp phần lớn khối lượng–năng lượng của proton. Đây là ví dụ quan trọng cho việc khối lượng của vật thể composite không đơn giản bằng tổng khối lượng các thành phần cơ bản.

## QCD, điện tích màu và tự do tiệm cận

Quark mang điện tích màu (color charge), còn gluon cũng mang màu nên gluon có thể tự tương tác. Đây là khác biệt quan trọng so với photon, vốn không mang điện tích điện.

Ở năng lượng rất cao hay khoảng cách rất ngắn, hằng số ghép QCD giảm; hiện tượng này gọi là tự do tiệm cận (asymptotic freedom). Ở năng lượng thấp, tương tác mạnh lên và hiện tượng giam hãm (confinement) khiến quark không xuất hiện như hạt tự do cô lập.

Tán xạ không đàn hồi sâu cho thấy proton có cấu trúc parton. Trong va chạm năng lượng cao, quá trình cứng có thể tính bằng QCD nhiễu loạn, sau đó shower và hadron hóa biến parton mang màu thành các hadron trung hòa màu quan sát được trong detector.

## Tương tác yếu, tính thuận tay và phân rã beta

Tương tác yếu phân biệt thành phần thuận tay trái và phải của fermion, dẫn đến vi phạm đối xứng chẵn lẻ (parity violation).

Ở mức quark, một phân rã beta có thể được mô tả bằng việc quark loại down chuyển thành quark loại up thông qua boson `W`, sau đó `W` tạo lepton và neutrino hoặc phản neutrino phù hợp với các định luật bảo toàn.

## Dao động neutrino

Trạng thái flavor của neutrino không trùng hoàn toàn với trạng thái riêng khối lượng. Vì vậy neutrino tạo ra với một flavor có thể được phát hiện với flavor khác sau khi truyền một khoảng cách.

Dao động neutrino nhạy với chênh lệch bình phương khối lượng `\Delta m^2`, năng lượng, khoảng cách và các góc trộn. Nó cho thấy neutrino có khối lượng khác không, vượt ra ngoài phiên bản tối giản ban đầu của Mô hình Chuẩn với neutrino không khối lượng.

## Sơ đồ Feynman không phải video quỹ đạo hạt

Sơ đồ Feynman (Feynman diagram) là công cụ tổ chức các số hạng trong khai triển nhiễu loạn của biên độ lượng tử. Các đường ngoài biểu diễn trạng thái vào và ra có thể quan sát, còn đường trong biểu diễn propagator trong phép tính.

Không nên đọc sơ đồ như một đoạn phim cho biết “hạt ảo thật sự bay theo đúng đường đó”. Xác suất vật lý được tính từ tổng kết hợp các biên độ rồi lấy bình phương độ lớn, bao gồm cả giao thoa giữa nhiều sơ đồ.

## Tiết diện, độ sáng va chạm và số sự kiện

Thí nghiệm hạt không chỉ hỏi một phản ứng có thể xảy ra hay không. Nó đo tiết diện (cross section) `\sigma`, độ rộng phân rã `\Gamma`, tỉ lệ nhánh và các phân bố động học.

Số sự kiện kỳ vọng có dạng

```math
N\approx \mathcal L_{\mathrm{int}}\,\sigma\,\epsilon,
```

trong đó `\mathcal L_{int}` là độ sáng tích phân và `\epsilon` là hiệu suất detector cùng quy trình chọn sự kiện.

Đây là nơi vật lý hạt nối trực tiếp với thống kê và khoa học dữ liệu: đáp ứng detector, nền sự kiện, hàm hợp lý (likelihood) và sai số hệ thống quyết định cách suy tham số vật lý từ dữ liệu va chạm.

## Trường lượng tử: hạt là kích thích của trường

Trong lý thuyết trường lượng tử (Quantum Field Theory, QFT / 양자장론), trường là đối tượng cơ bản. Hạt được hiểu là lượng tử kích thích của trường tương ứng. Photon là kích thích của trường điện từ; electron là kích thích của trường electron.

Khái niệm “hạt ảo” trong lý thuyết nhiễu loạn không nên được mô tả ngây thơ như hạt thật liên tục “xuất hiện rồi biến mất bằng cách mượn năng lượng”. Chúng là thành phần nội tại của phép tính và không phải hạt on-shell có thể quan sát trực tiếp.

## Quark và hadron

Proton và neutron không phải hạt cơ bản. Proton có nội dung quark hóa trị `uud`, neutron có `udd`, đồng thời bên trong còn có gluon và các cặp quark–phản quark biển.

Baryon chứa ba quark hóa trị, còn meson chứa một quark và một phản quark theo phân loại đơn giản. Do giam hãm màu, ta không tách được một quark tự do ở năng lượng thấp; va chạm năng lượng cao tạo jet và quá trình hadron hóa thay vì giải phóng quark cô lập.

## Phản vật chất

Mỗi hạt cơ bản có phản hạt tương ứng với cùng khối lượng nhưng các số lượng tử thích hợp đổi dấu, ví dụ điện tích điện. Khi vật chất và phản vật chất hủy nhau, năng lượng được chuyển thành các hạt khác sao cho các định luật bảo toàn vẫn được thỏa mãn.

Phản vật chất không có “khối lượng âm” trong vật lý chuẩn.

## Những gì Mô hình Chuẩn chưa giải thích

Mô hình Chuẩn cực kỳ thành công nhưng không phải lý thuyết của mọi thứ. Nó chưa chứa hấp dẫn lượng tử hoàn chỉnh; chưa xác định bản chất vật chất tối; không tự giải thích đầy đủ bất đối xứng vật chất–phản vật chất của vũ trụ; và nhiều khối lượng cùng hằng số ghép vẫn là tham số phải đo thực nghiệm.

Những giới hạn này không làm Mô hình Chuẩn “sai”. Chúng xác định miền mà mô hình đã được kiểm nghiệm rất tốt và những câu hỏi nơi cần vật lý mới.

## Mô hình tư duy (Mental Model)

Danh sách hạt chỉ là bề mặt của Mô hình Chuẩn. Cấu trúc sâu hơn nằm ở các trường lượng tử, đối xứng, cách đối xứng bị phá vỡ và những tương tác được phép giữa các trường.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Nền tảng lượng tử](../08_quantum/00_quantum_foundations.md), [Thuyết tương đối hẹp](../07_relativity/00_special_relativity.md).

**Liên hệ tiếp:** [Thiên hà và vũ trụ học](../11_astrophysics_cosmology/01_galaxies_cosmology.md).
