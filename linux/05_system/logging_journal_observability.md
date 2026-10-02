# Nhật ký, journal và khả năng quan sát hệ thống

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Nhật ký, journal và khả năng quan sát hệ thống**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Vì sao nhật ký tồn tại?** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Tệp nhật ký truyền thống** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối logging với journal và observability, để phân biệt log lưu trữ với tín hiệu dùng để suy luận trạng thái hệ thống.

Nhật ký (log) không phải toàn bộ sự thật của hệ thống. Nó chỉ là một **kênh quan sát (observation channel)** do kernel, trình quản lý dịch vụ hoặc ứng dụng chủ động tạo ra. Ứng dụng có thể bị treo mà không ghi thêm log; thiết bị lưu trữ có thể lỗi ở tầng kernel trong khi ứng dụng chỉ báo hết thời gian chờ (timeout / 타임아웃); gói tin mạng có thể bị loại bỏ trước khi yêu cầu tới được ứng dụng. Vì vậy **khả năng quan sát hệ thống (observability)** cần kết hợp nhật ký với số liệu đo (metrics), trạng thái tiến trình, socket, tài nguyên và mốc thời gian.

## Vì sao nhật ký tồn tại?

Hệ thống đang chạy thay đổi liên tục. Khi sự cố xảy ra, trạng thái tại thời điểm lỗi thường đã biến mất trước khi con người SSH vào máy. Nhật ký biến một phần sự kiện thành **bằng chứng tồn tại theo thời gian (persistent evidence)** để có thể dựng lại diễn biến.

Một bản ghi nhật ký hữu ích thường giúp trả lời: chuyện gì xảy ra, lúc nào, ở thành phần nào, yêu cầu hoặc tiến trình nào liên quan và kết quả ra sao. Dấu thời gian không có múi giờ hoặc `request ID` không được truyền xuyên các dịch vụ sẽ làm việc đối chiếu sự kiện khó hơn.

> **Chuyển mạch:** Trong **Nhật ký, journal và khả năng quan sát hệ thống**, **Tệp nhật ký truyền thống** tiếp nhận điểm tựa từ **Vì sao nhật ký tồn tại?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Journal của systemd** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tệp nhật ký truyền thống

Nhiều ứng dụng ghi nhật ký dưới `/var/log` hoặc thư mục riêng của ứng dụng:

```bash
ls -lh /var/log
less +F /var/log/myapp/app.log
```

`less +F` theo dõi tệp theo thời gian thực nhưng cho phép nhấn `Ctrl+C` để dừng theo dõi và tìm kiếm, sau đó nhấn `F` để tiếp tục.

`tail -F` khác `tail -f` ở chỗ phù hợp hơn khi tệp bị đổi tên hoặc tạo lại trong quá trình xoay vòng nhật ký:

```bash
tail -n 500 -F app.log
```

> **Chuyển mạch:** Ở chặng này của **Nhật ký, journal và khả năng quan sát hệ thống**, **Journal của systemd** tiếp nhận điểm tựa từ **Tệp nhật ký truyền thống** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **journalctl -xeu thực sự làm gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Journal của systemd

Trên hệ thống sử dụng systemd, `journald` thu thập nhật ký cùng siêu dữ liệu (metadata / 메타데이터) có cấu trúc từ nhiều nguồn.

```bash
journalctl -u app
```

Lọc theo thời gian:

```bash
journalctl -u app --since '2026-09-20 16:00' --until '2026-09-20 16:15'
```

Theo dõi liên tục:

```bash
journalctl -u app -f
```

Lấy 200 bản ghi gần nhất:

```bash
journalctl -u app -n 200 --no-pager
```

`-u` lọc theo đơn vị (unit / 단위), giúp tránh tìm kiếm toàn bộ journal khi ta đã biết phạm vi dịch vụ cần kiểm tra.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nhật ký, journal và khả năng quan sát hệ thống**, **journalctl -xeu thực sự làm gì?** tiếp nhận điểm tựa từ **Journal của systemd** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Xoay vòng nhật ký** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `journalctl -xeu` thực sự làm gì?

Trước khi chạy hoặc đọc ví dụ dưới đây, hãy xác định câu hỏi vận hành mà nó trả lời, dữ liệu nào sẽ quan sát được và giới hạn của kết quả. Lệnh chỉ có ý nghĩa khi gắn với một giả thuyết về state của hệ thống.

```bash
journalctl -xeu nginx
```

`-u` chọn đơn vị (unit / 단위), `-e` đưa vị trí xem tới gần cuối journal, còn `-x` thêm phần giải thích cho một số mục có trong danh mục (catalog / 카탈로그). Câu lệnh này hữu ích khi dịch vụ không khởi động được, nhưng phần giải thích đi kèm không thay thế quá trình phân tích nguyên nhân gốc.

> **Chuyển mạch:** Trong **Nhật ký, journal và khả năng quan sát hệ thống**, **Xoay vòng nhật ký** tiếp nhận điểm tựa từ **journalctl -xeu thực sự làm gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Nhật ký có cấu trúc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Xoay vòng nhật ký

Nếu nhật ký chỉ nối thêm mãi, hệ thống tệp cuối cùng sẽ hết dung lượng. **Xoay vòng nhật ký (log rotation / 로그 로테이션)** đổi tệp cũ sang tên khác, có thể nén và xóa theo chính sách lưu giữ.

Các tệp sau xoay vòng thường có dạng:

```text
app.log
app.log.1
app.log.2.gz
```

Có thể tìm trực tiếp trong nhật ký đã nén mà không cần giải nén:

```bash
zgrep -Ein 'ERROR|Exception' app.log.2.gz
zless app.log.2.gz
```

Xoay vòng cần phối hợp với ứng dụng. Nếu tiến trình vẫn giữ tệp (file / 파일) descriptor tới `inode` cũ sau khi tệp bị đổi tên hoặc xóa và không mở lại nhật ký mới, dung lượng có thể không được giải phóng như mong đợi. `lsof +L1` giúp tìm các tệp đã mất tên nhưng vẫn còn được mở.

> **Chuyển mạch:** Ở chặng này của **Nhật ký, journal và khả năng quan sát hệ thống**, **Nhật ký có cấu trúc** tiếp nhận điểm tựa từ **Xoay vòng nhật ký** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đối chiếu sự kiện và request ID** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nhật ký có cấu trúc

Văn bản thuần dễ đọc nhưng khó phân tích ổn định khi định dạng thay đổi. **Nhật ký có cấu trúc (structured logging)** như JSON cung cấp các trường rõ ràng:

```json
{"ts":"2026-09-20T16:03:21+09:00","level":"ERROR","request_id":"abc123","service":"ekyc","message":"upstream timeout"}
```

Có thể truy vấn bằng `jq`:

```bash
jq 'select(.level == "ERROR") | {ts,request_id,message}' app.json.log
```

Cách tổ chức này có liên hệ với cơ sở dữ liệu và kỹ thuật dữ liệu: mỗi sự kiện trở thành một bản ghi có lược đồ thay vì một dòng văn bản mà người đọc phải đoán vị trí từng trường.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nhật ký, journal và khả năng quan sát hệ thống**, **Nhật ký có cấu trúc** đã nêu tiêu chí phân biệt, còn **Đối chiếu sự kiện và request ID** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Thời gian là một chiều dữ liệu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đối chiếu sự kiện và `request ID`

Trong hệ thống phân tán, một yêu cầu của người dùng có thể đi qua bộ cân bằng tải → API → dịch vụ → cơ sở dữ liệu. Hai sự kiện có dấu thời gian gần nhau chưa đủ chứng minh chúng thuộc cùng một yêu cầu. `Correlation ID` hoặc `trace ID` được truyền xuyên hệ thống giúp nối các bằng chứng lại với nhau.

```bash
grep -F 'request_id=abc123' app.log
```

Khả năng quan sát tốt phải được thiết kế từ kiến trúc ứng dụng; không thể hoàn toàn bổ sung về sau chỉ bằng các câu lệnh Linux.

> **Chuyển mạch:** Trong **Nhật ký, journal và khả năng quan sát hệ thống**, **Đối chiếu sự kiện và request ID** đã nêu tiêu chí phân biệt, còn **Thời gian là một chiều dữ liệu** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Nhật ký, số liệu đo và dấu vết phân tán** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thời gian là một chiều dữ liệu

Điều tra sự cố nên xác định khoảng thời gian trước. Nếu người dùng báo lỗi lúc 16:05 KST nhưng nhật ký máy chủ dùng UTC, tìm sai múi giờ có thể dẫn tới kết luận nhầm rằng "không có lỗi".

```bash
date '+%F %T %Z'
date -u
timedatectl
```

Đồng bộ thời gian bằng NTP cũng quan trọng với TLS, thời hạn đơn vị từ (token / 토큰) và việc đối chiếu sự kiện giữa nhiều máy chủ.

> **Chuyển mạch:** Ở chặng này của **Nhật ký, journal và khả năng quan sát hệ thống**, **Thời gian là một chiều dữ liệu** nêu điều cần giải thích; **Nhật ký, số liệu đo và dấu vết phân tán** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Nhật ký của kernel** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nhật ký, số liệu đo và dấu vết phân tán

Ba khái niệm thường gặp là:

- **nhật ký (logs)** — các bản ghi sự kiện rời rạc;
- **số liệu đo (metrics)** — các đại lượng số theo thời gian như CPU, tốc độ yêu cầu hoặc percentile độ trễ;
- **dấu vết (traces)** — đường đi của một yêu cầu qua nhiều thành phần và span trong hệ thống phân tán.

Không loại nào thay thế hoàn toàn loại còn lại. CPU tăng đột biến có thể được chỉ số (metric / 지표) phát hiện nhanh; log giải thích sự kiện trong ứng dụng; dấu vết (trace / 추적) cho thấy độ trễ tập trung ở dịch vụ nào.

Các công cụ dòng lệnh Linux như `vmstat`, `iostat`, `ss`, `pidstat` cung cấp quan sát cục bộ, còn môi trường vận hành (production / 운영 환경) thường gửi metrics và traces tới hệ thống tập trung để lưu giữ và phân tích lâu dài.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nhật ký, journal và khả năng quan sát hệ thống**, **Nhật ký của kernel** tiếp nhận điểm tựa từ **Nhật ký, số liệu đo và dấu vết phân tán** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thu thập bằng chứng trước khi can thiệp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nhật ký của kernel

Nhật ký ứng dụng không nhìn thấy mọi loại thất bại. Kernel có thể ghi nhận OOM, lỗi hệ thống tệp, thiết bị hoặc mạng:

```bash
dmesg -T | tail -100
journalctl -k --since today
```

Tìm dấu hiệu OOM:

```bash
journalctl -k | grep -i -E 'oom|out of memory|killed process'
```

Nếu tiến trình Java "tự biến mất" mà nhật ký ứng dụng không cho thấy quá trình dừng có kiểm soát, nhật ký kernel là một lớp bắt buộc phải kiểm tra.

> **Chuyển mạch:** Trong **Nhật ký, journal và khả năng quan sát hệ thống**, **Nhật ký của kernel** nêu điều cần giải thích; **Thu thập bằng chứng trước khi can thiệp** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Tỷ lệ tín hiệu trên nhiễu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thu thập bằng chứng trước khi can thiệp

Trước khi khởi động lại một dịch vụ đang lỗi, nếu tình huống cho phép, nên chụp lại trạng thái:

```bash
date
systemctl status app --no-pager
journalctl -u app -n 300 --no-pager
pgrep -af 'java.*app'
ss -antp
free -h
df -h
```

Với Java dùng CPU cao hoặc bị treo, có thể cần lấy luồng thực thi (thread / 스레드) dump trước khi restart. Khởi động lại có thể phục hồi dịch vụ nhưng đồng thời làm mất bằng chứng khi đang chạy.

Đây là khác biệt giữa **phục hồi dịch vụ (recovery)** và **phân tích nguyên nhân gốc (root-cause analysis)**. Hai mục tiêu có liên quan nhưng không giống nhau.

> **Chuyển mạch:** Ở chặng này của **Nhật ký, journal và khả năng quan sát hệ thống**, **Thu thập bằng chứng trước khi can thiệp** nêu điều cần giải thích; **Tỷ lệ tín hiệu trên nhiễu** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tỷ lệ tín hiệu trên nhiễu

Nhiều log hơn không tự động tạo khả năng quan sát (observability / 관측 가능성) tốt hơn. gỡ lỗi (debug / 디버그) quá dày có thể làm tăng chi phí lưu trữ, làm tìm kiếm chậm và che khuất sự kiện quan trọng. Thiết kế nhật ký cần mức log có ý nghĩa, lấy mẫu hoặc giới hạn tốc độ khi phù hợp và chính sách lưu giữ rõ ràng.

Không nên ghi bí mật, truy cập (access / 접근) đơn vị từ (token / 토큰), mật khẩu hoặc dữ liệu cá nhân không cần thiết vào log. Khả năng quan sát cũng là một phần của thiết kế bảo mật và quyền riêng tư.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nhật ký, journal và khả năng quan sát hệ thống**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Tỷ lệ tín hiệu trên nhiễu** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những hiểu lầm phổ biến (Common Misconceptions)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Hãy coi một sự cố như sự kiện đã xảy ra trong hệ thống nhiều lớp. Mỗi nguồn quan sát giống một camera nhìn từ một góc khác. Nhật ký ứng dụng không phải camera toàn cảnh. Nhiệm vụ là **đối chiếu các bằng chứng độc lập theo thời gian và theo giả thuyết nhân quả**.

> **Chuyển mạch:** Trong **Nhật ký, journal và khả năng quan sát hệ thống**, **Những hiểu lầm phổ biến (Common Misconceptions)** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu lầm phổ biến (Common Misconceptions)

**"Không có lỗi (error / 오류) log nghĩa là không có lỗi."** Thất bại có thể nằm ở kernel, mạng, phụ thuộc hoặc mã nguồn không ghi nhật ký đúng.

**"Restart xong hết lỗi nghĩa là nguyên nhân là dịch vụ cần restart."** Restart chỉ thay đổi trạng thái; nó chưa chứng minh nguyên nhân.

**"`tail -f` chính là khả năng quan sát (observability / 관측 가능성)."** Nó chỉ là một cách xem log thời gian thực, không có tổng hợp, đối chiếu hoặc ngữ cảnh tài nguyên.

**"Hai log có cùng thời gian nghĩa là có quan hệ nhân quả."** Cần thêm danh tính và ngữ cảnh như yêu cầu (request / 요청) ID, dấu vết (trace / 추적) ID và kiến trúc luồng xử lý.

**"Log càng chi tiết càng tốt."** Nhiễu, chi phí và rủi ro lộ dữ liệu nhạy cảm cũng tăng theo.

> **Chuyển mạch:** Ở chặng này của **Nhật ký, journal và khả năng quan sát hệ thống**, **Kết nối kiến thức** tiếp nhận điểm tựa từ **Những hiểu lầm phổ biến (Common Misconceptions)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối kiến thức

Chương [Xử lý sự cố production](../09_production/production_troubleshooting.md) dùng observability như một lớp bằng chứng. Các chương về CPU, bộ nhớ, lưu trữ và mạng cung cấp những nguồn quan sát ngoài nhật ký ứng dụng để tránh nhìn sự cố qua một kênh duy nhất.

> **Bàn giao:** Sau **Kết nối kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
