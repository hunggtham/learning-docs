# Mobile Networks — từ sóng điện thoại tới Internet

Khi biểu tượng `5G` xuất hiện, phone không kết nối thẳng tới “Internet 5G”. Nó kết nối radio tới một cell site; traffic sau đó đi qua **mạng truy nhập vô tuyến (Radio Access Network, RAN / 무선접속망)**, transport network và **mạng lõi (core network / 코어망)** của operator trước khi tới Internet hoặc service khác.

## 1. Kiến trúc end-to-end

```text
Phone + SIM
   ↓ radio
Antenna / base station
   ↓
RAN
   ↓ fiber / microwave backhaul
Transport network
   ↓
Mobile core
   ├── authentication / subscriber data
   ├── mobility management
   ├── policy / charging
   └── user-plane gateway
            ↓
       Internet / IMS / private network
```

RAN giải quyết radio scheduling và handover ở edge. Core giải quyết identity, session, mobility, policy và đưa user traffic tới data network.

## 2. SIM thực sự làm gì?

SIM/eSIM chứa subscriber identity và secret material cho authentication. Network không đơn giản hỏi “số điện thoại là gì?” rồi cho vào. Phone và network thực hiện challenge-response để chứng minh subscriber hợp lệ mà không truyền secret key nguyên bản qua air interface.

Sau authentication, operator áp subscription profile: data plan, roaming, QoS, service permissions. Phone number là application-level identity quan trọng nhưng radio/network identity dùng nhiều identifier chuyên dụng hơn.

## 3. Một cell không có “tốc độ 1 Gbps cho từng người”

Radio spectrum là shared resource. Base station chia time/frequency/spatial resources cho active users. Marketing peak rate thường là theoretical aggregate trong điều kiện tốt; real throughput phụ thuộc:

```text
spectrum bandwidth
× spectral efficiency
× MIMO layers
× signal quality
÷ shared users
- protocol overhead
- backhaul/core congestion
```

Đứng gần antenna không bảo đảm nhanh nếu cell congested; signal đầy vạch nhưng backhaul nghẽn vẫn chậm.

## 4. Handover giữ cuộc gọi/data khi đang di chuyển

Phone liên tục đo serving cell và neighbor cells. Khi conditions phù hợp, network chuyển connection sang cell khác. Handover quá sớm tạo ping-pong; quá muộn làm radio link failure.

Trên KTX/highway ở Hàn Quốc hay cao tốc Bắc–Nam ở Việt Nam, mobility management khó hơn người đứng yên vì cell thay đổi nhanh và Doppler/radio conditions biến động.

## 5. 4G và 5G khác ở đâu?

4G LTE dùng Evolved Packet Core (EPC / 진화형 패킷 코어) và radio LTE. 5G New Radio (NR / 5G 신무선) có thể được triển khai hai cách lớn:

**5G NSA (Non-Standalone / 비단독모드)** dùng 5G radio nhưng vẫn dựa vào 4G core/control anchor ở nhiều architecture. Đây là cách triển khai nhanh vì tận dụng LTE infrastructure.

**5G SA (Standalone / 단독모드)** dùng 5G Core, cho phép architecture cloud-native hơn và mở đầy đủ hơn các capability như network slicing, low-latency/private-network integration tùy implementation.

```text
NSA
Phone → 4G control + 5G radio → 4G/EPC-centered core

SA
Phone → 5G NR → 5G Core → data network
```

Logo `5G` trên phone không tự cho biết deployment là NSA hay SA.

## 6. Hàn Quốc: dense mature mobile market

Hàn Quốc có ba mobile network operators lớn SK Telecom, KT và LG U+, cùng một MVNO ecosystem đáng kể. Dense urban fiber/backhaul và early 5G deployment giúp capacity cao ở nhiều đô thị. Đến 2026, policy/industry focus tiếp tục dịch từ coverage 5G ban đầu sang quality, 5G SA/core evolution, private 5G và AI/network automation.

**Nhà mạng ảo (Mobile Virtual Network Operator, MVNO / 알뜰폰)** không nhất thiết sở hữu radio network toàn quốc; họ mua wholesale capacity từ MNO rồi bán service riêng. Vì vậy số consumer brands lớn hơn số physical nationwide radio networks.

## 7. Việt Nam: 5G thương mại hóa trên ba mạng lớn

Bộ Khoa học và Công nghệ năm 2026 nêu Viettel, VNPT/VinaPhone và MobiFone là ba doanh nghiệp viễn thông lớn đã thương mại hóa 5G. Market đang ở giai đoạn mở rộng coverage/capacity nhanh, song song với chuyển đổi spectrum từ legacy generations sang 4G/5G.

Geography Việt Nam làm deployment khác Hàn Quốc: dense Hanoi/HCMC/industrial zones cho economics tốt của high-capacity cells; vùng núi, đảo và rural cần coverage-oriented design, tower sharing, lower-band spectrum và backhaul khác.

## 8. Hàn Quốc ↔ Việt Nam

| Câu hỏi | Hàn Quốc | Việt Nam |
|---|---|---|
| Major nationwide MNOs | SKT, KT, LG U+ | Viettel, VNPT/VinaPhone, MobiFone là ba operator 5G lớn |
| Market maturity | Very mature LTE/5G, dense traffic và MVNO market | 4G rất rộng; 5G commercial expansion đang tăng nhanh |
| Geography | Dense urbanized territory, easier fiber density per area | Long country, mountains/islands/rural zones làm coverage economics đa dạng hơn |
| 5G next step | SA/core evolution, private networks, quality/capacity | Expand 5G footprint, spectrum reuse, enterprise/private 5G và digital services |
| Backhaul | Dense fiber foundation | Fiber mạnh ở cities/industrial areas; remote areas có constraints lớn hơn |

## 9. Spectrum tại sao đắt?

Radio frequencies có propagation characteristics khác nhau và là scarce licensed resource. Low band đi xa/xuyên building tốt nhưng bandwidth hạn chế; mid-band cân bằng coverage/capacity; mmWave có bandwidth lớn nhưng range và blockage khó hơn.

```text
Low frequency
→ wider coverage, less capacity per MHz

Higher frequency
→ more bandwidth potential, smaller cells / harder propagation
```

Regulator cấp quyền sử dụng spectrum qua cơ chế quốc gia. Operator phải tối ưu spectrum portfolio cùng site density và capital expenditure.

## 10. Roaming hoạt động thế nào?

Khi subscriber Hàn Quốc sang Việt Nam, phone đăng ký vào visited network có roaming agreement. Visited network cung cấp radio access; home operator vẫn tham gia authentication/policy/billing theo architecture. Data có thể local breakout hoặc được routed qua home network tùy design/service.

```text
Korean SIM
→ Vietnamese visited RAN/core
→ roaming interconnect
→ home operator authentication/billing
→ Internet/service
```

Vì vậy roaming problem có thể nằm ở visited radio, roaming signaling, home-network policy hoặc billing profile.

## 11. Tại sao phone nóng và pin tụt khi sóng yếu?

Khi path loss cao, handset có thể tăng transmit power và search cells nhiều hơn. Radio retries, frequent handovers hoặc NSA dual connectivity cũng có thể tăng energy use. “Ít vạch sóng” không chỉ ảnh hưởng download; nó làm power-control loop thay đổi.

## 12. Failure modes

- Base station mất điện/backhaul → khu vực mất service.
- Core outage → nhiều cell vẫn phát sóng nhưng subscriber không tạo session.
- DNS/Internet gateway lỗi → signal bình thường nhưng app không truy cập Internet.
- Congestion → coverage tốt nhưng throughput thấp.
- Fiber cut → nhiều sites phía sau cùng bị ảnh hưởng.
- IMS issue → data có thể chạy nhưng voice/VoLTE/VoNR gặp lỗi.

Mental model:

```text
Mobile service
= spectrum
+ RAN
+ backhaul
+ core
+ interconnect
+ power
+ software
```

Đọc [internet](../internet/README.md) để theo packet sau khi rời mobile core; [semiconductors](../semiconductors/README.md) để hiểu modem/RF/baseband chips trong phone và base station.

## Nguồn chính thức tham chiếu

- Korea Ministry of Science and ICT — telecommunications/operator information: https://www.msit.go.kr/
- Vietnam Ministry of Science and Technology — 5G commercialization, 29 Mar 2026: https://mst.gov.vn/dot-pha-theo-nghi-quyet-57-thuong-mai-hoa-5g-thuc-day-phat-trien-kinh-te-so-theo-chieu-sau-197260329133308364.htm
- 3GPP — mobile standards: https://www.3gpp.org/
