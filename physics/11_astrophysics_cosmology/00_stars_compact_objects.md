# Vật lý sao, tiến hóa sao và các thiên thể đặc

## Thiên văn học trở thành vật lý bằng cách nào?

Phần lớn vật thể thiên văn không thể đưa vào phòng thí nghiệm. Ta chỉ nhận được các tín hiệu truyền đến Trái Đất như photon, tia vũ trụ, neutrino và sóng hấp dẫn, rồi dùng chúng để suy ngược trạng thái vật lý của nguồn.

Vật lý thiên văn (Astrophysics / 천체물리학) vì thế là một bài học lớn về suy luận: từ phổ, độ sáng, biến thiên theo thời gian, phân cực và chuyển động, ta có thể suy ra nhiệt độ, thành phần hóa học, vận tốc, khối lượng, từ trường và nhiều tính chất khác của vật thể ở rất xa.

## Ánh sáng là tín hiệu mang thông tin

Một vật gần vật đen (blackbody) có bước sóng cực đại liên hệ với nhiệt độ qua định luật Wien:

```math
\lambda_{max}T=b.
```

Công suất bức xạ trên một đơn vị diện tích tuân theo định luật Stefan–Boltzmann:

```math
j^\star=\sigma T^4.
```

Nếu một ngôi sao có bán kính `R` và gần đúng như vật đen:

```math
L=4\pi R^2\sigma T^4.
```

Thông lượng quan sát ở khoảng cách `d` là

```math
F=\frac{L}{4\pi d^2}.
```

Kết hợp phổ, độ sáng biểu kiến và khoảng cách cho phép suy ra nhiều tính chất của sao.

## Vạch quang phổ là “dấu vân tay” nguyên tử

Các vạch hấp thụ và phát xạ xuất hiện do chuyển mức lượng tử của nguyên tử hay ion. Mẫu vạch cho biết nguyên tố hóa học; độ dịch vạch cho thông tin về vận tốc qua hiệu ứng Doppler; độ rộng vạch chứa thông tin về nhiệt độ, va chạm hay chuyển động rối; tách vạch Zeeman có thể cho biết từ trường.

Vì vậy máy quang phổ gắn với kính thiên văn hoạt động như một “phòng thí nghiệm từ xa”. Vật lý lượng tử của nguyên tử cho phép ta đọc thành phần hóa học của một ngôi sao cách hàng nghìn năm ánh sáng.

## Sao cân bằng giữa hấp dẫn và áp suất

Một sao dãy chính không “cháy” theo phản ứng hóa học. Hấp dẫn kéo vật chất vào trong, còn gradient áp suất do plasma nóng và bức xạ tạo ra lực cân bằng hướng ra ngoài.

Cân bằng thủy tĩnh có dạng

```math
\frac{dP}{dr}=-\frac{G M(r)\rho(r)}{r^2}.
```

Khối lượng bên trong bán kính `r` thỏa

```math
\frac{dM}{dr}=4\pi r^2\rho(r).
```

Để mô tả đầy đủ cấu trúc sao còn cần phương trình sinh năng lượng từ phản ứng hạt nhân và phương trình vận chuyển năng lượng.

Một ngôi sao vì thế là một hệ plasma nhiệt động lực học tự hấp dẫn, không đơn giản là một “quả cầu lửa”.

## Nhiệt hạch và tuổi thọ của sao

Trong lõi sao, nhiệt độ và mật độ đủ lớn để các hạt nhân hydro có thể phản ứng nhờ cả chuyển động nhiệt lẫn xuyên hầm lượng tử (quantum tunneling). Phản ứng nhiệt hạch giải phóng năng lượng vì sản phẩm như heli có năng lượng liên kết trên nucleon lớn hơn trạng thái ban đầu.

Sao khối lượng lớn có nhiều nhiên liệu hơn nhưng độ sáng tăng rất nhanh theo khối lượng. Vì tốc độ tiêu thụ nhiên liệu tăng mạnh, chúng thường sống ngắn hơn các sao khối lượng nhỏ.

## Tiến hóa sao (stellar evolution)

Khi hydro trong lõi cạn dần, cấu trúc sao phải điều chỉnh. Sao khối lượng nhỏ và trung bình có thể trải qua pha sao khổng lồ đỏ rồi để lại sao lùn trắng. Sao khối lượng lớn có thể tổng hợp các nguyên tố nặng hơn cho đến khi lõi không còn thu được năng lượng từ nhiệt hạch hiệu quả, dẫn tới sụp đổ lõi và siêu tân tinh.

Phần còn lại có thể là sao neutron hoặc lỗ đen, tùy khối lượng và điều kiện tiến hóa. Đường tiến hóa thực tế còn phụ thuộc độ kim loại (metallicity), tốc độ quay, hệ sao đôi và mức mất khối lượng, nên không có một sơ đồ duy nhất áp dụng tuyệt đối cho mọi sao.

## Sao lùn trắng và áp suất suy biến electron

Áp suất suy biến electron (electron degeneracy pressure) xuất phát từ nguyên lý loại trừ Pauli, không cần nhiệt độ cao như áp suất khí lý tưởng. Khi electron bị nén vào thể tích nhỏ, chúng phải chiếm những trạng thái động lượng khác nhau, tạo áp suất lượng tử chống lại hấp dẫn.

Giới hạn Chandrasekhar cho thấy có một thang khối lượng tối đa mà áp suất suy biến electron có thể giữ sao lùn trắng ổn định. Khi khối lượng vượt quá miền này, các hiệu ứng tương đối tính và động lực học sụp đổ trở nên quan trọng.

## Sao neutron

Trong sụp đổ lõi, electron và proton có thể kết hợp tạo vật chất giàu neutron. Sao neutron có mật độ gần thang mật độ hạt nhân và được nâng đỡ bởi áp suất suy biến cùng các tương tác hạt nhân mạnh.

Pulsar là sao neutron quay nhanh và có từ trường mạnh. Bức xạ phát theo chùm quét qua không gian tạo tín hiệu tuần hoàn rất ổn định, khiến một số pulsar hoạt động như những “đồng hồ vũ trụ”.

## Lỗ đen và bồi tụ vật chất

Lỗ đen tự nó không cần phát ánh sáng, nhưng vật chất rơi vào có thể tạo đĩa bồi tụ rất nóng và phát bức xạ mạnh. Vì vậy các hệ đôi tia X và nhân thiên hà hoạt động có thể tiết lộ sự tồn tại của lỗ đen thông qua môi trường xung quanh.

Đối với lỗ đen Schwarzschild không quay, bán kính chân trời sự kiện là

```math
r_s=\frac{2GM}{c^2}.
```

Đây là một kết quả của thuyết tương đối rộng, không phải bán kính của một bề mặt vật chất rắn.

## Mô hình tư duy (Mental Model)

Một ngôi sao là hệ tự hấp dẫn trong đó hấp dẫn ép vật chất vào trong, áp suất chống lại sự nén, phản ứng hạt nhân cung cấp năng lượng và các cơ chế vận chuyển đưa năng lượng ra ngoài. Khi nhiên liệu, thành phần hay cơ chế tạo áp suất thay đổi, cấu trúc cân bằng của sao cũng thay đổi và dẫn đến tiến hóa sao.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Hấp dẫn và quỹ đạo](../01_mechanics/06_gravitation_orbits.md), [Nhiệt động lực học](../04_thermal_statistical/00_thermodynamics.md), [Vật lý hạt nhân](../09_atomic_nuclear_particle/01_nuclear_physics.md).

**Liên hệ tiếp:** [Thiên hà và vũ trụ học](01_galaxies_cosmology.md).
