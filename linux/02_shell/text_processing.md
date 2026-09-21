# Xử lý văn bản trên Linux

Máy chủ Linux tạo ra rất nhiều dữ liệu dạng văn bản: nhật ký, tệp cấu hình, danh sách tiến trình, đầu ra câu lệnh, dữ liệu gần giống CSV và các ảnh chụp chẩn đoán. Sức mạnh của shell không nằm ở từng tiện ích riêng lẻ mà ở khả năng đưa **luồng văn bản (text stream)** qua nhiều phép biến đổi nhỏ để trả lời một câu hỏi cụ thể.

## Bắt đầu từ câu hỏi, không bắt đầu từ câu lệnh

Giả sử môi trường production có `access.log`. Câu hỏi "máy chủ có lỗi không?" quá rộng. Có thể thu hẹp thành: trong 10 phút xảy ra sự cố, mã trạng thái HTTP nào tăng mạnh? IP nào tạo nhiều yêu cầu nhất? endpoint nào thường xuất hiện cùng phản hồi `500`? Khi câu hỏi đủ rõ, câu lệnh trở thành công cụ triển khai quá trình suy luận.

Một luồng xử lý văn bản tốt thường có dạng:

```text
dữ liệu thô -> chọn nguồn -> lọc -> biến đổi -> tổng hợp -> sắp xếp -> kiểm tra
```

## `grep`: chọn dòng theo mẫu

`grep` trả về các dòng khớp với mẫu:

```bash
grep 'ERROR' app.log
```

Không phân biệt chữ hoa/chữ thường và hiển thị số dòng:

```bash
grep -in 'timeout' app.log
```

Dùng biểu thức chính quy mở rộng để tìm nhiều mẫu:

```bash
grep -Ein 'ERROR|Exception|Caused by|timeout' app.log
```

Lấy thêm ngữ cảnh quanh dòng khớp:

```bash
grep -C 10 'NullPointerException' app.log
```

`-C 10` thường hữu ích hơn chỉ lấy dòng khớp vì dấu vết ngăn xếp (stack trace) và ngữ cảnh yêu cầu có thể nằm ở các dòng xung quanh.

Khi mẫu phải được hiểu đúng như chuỗi ký tự thông thường, `-F` tránh việc diễn giải theo regex:

```bash
grep -F 'a[b]' file.txt
```

## Regex không phải glob

`*.log` là mẫu glob phổ biến của shell. Biểu thức chính quy diễn đạt ý tưởng tương tự thường gần với `.*\.log`. Nhầm hai ngôn ngữ mẫu này dễ tạo ra lỗi khó nhận ra.

Ví dụ với regex mở rộng:

```bash
grep -E '^ERROR|^WARN' app.log
```

`^` neo vào đầu dòng, còn `|` biểu thị lựa chọn giữa các mẫu.

## `find`: truy vấn cây hệ thống tệp

`find` không chỉ tìm tên tệp; nó có thể truy vấn đối tượng theo loại, thời gian, kích thước và nhiều metadata khác:

```bash
find /var/log -type f -name '*.log' -size +500M
```

Tìm tệp thay đổi trong 30 phút gần đây:

```bash
find /opt/app -type f -mmin -30 -ls
```

Tìm theo mốc thời gian cụ thể:

```bash
find /opt/app -type f -newermt '2026-09-20 16:00'
```

Đây là công cụ điều tra sự cố rất mạnh cho câu hỏi như: "sau lần triển khai lúc 16:00, những tệp nào đã thay đổi?"

Trước thao tác có tính phá hủy, hãy quan sát kết quả trước:

```bash
find /backup -type f -mtime +30 -print
```

Chỉ sau khi kiểm tra mới cân nhắc thêm `-delete`. Tách **quan sát** khỏi **thay đổi trạng thái** giúp giảm rủi ro production.

## `sort` và `uniq`: từ sự kiện thành tần suất

Nhật ký thường là một chuỗi sự kiện. Để tìm giá trị xuất hiện nhiều nhất, mô hình kinh điển là: lấy trường cần quan tâm → sắp xếp → đếm → sắp xếp theo số lần.

Nếu cột đầu của access log là IP máy khách:

```bash
awk '{print $1}' access.log | sort | uniq -c | sort -nr | head -20
```

`uniq` chỉ gộp các dòng trùng nhau nằm liền kề, vì vậy bước `sort` trước đó rất quan trọng.

Mô hình này có quan hệ gần với truy vấn cơ sở dữ liệu:

```sql
SELECT ip, COUNT(*)
GROUP BY ip
ORDER BY COUNT(*) DESC
LIMIT 20
```

Pipeline của shell và SQL khác cú pháp nhưng cùng chia sẻ một cách suy luận dữ liệu: **chọn trường → nhóm → tổng hợp → sắp xếp**.

## `awk`: xử lý bản ghi và trường

`awk` mặc định coi mỗi dòng là một bản ghi (record) và tách trường theo khoảng trắng. Vì vậy:

```bash
awk '{print $1}' access.log
```

sẽ in trường đầu tiên.

Có thể lọc theo điều kiện:

```bash
awk '$9 >= 500 {print $1, $7, $9}' access.log
```

Nếu định dạng nhật ký quy định `$9` là mã trạng thái HTTP, câu lệnh trên chọn các lỗi phía máy chủ và in IP, đường dẫn cùng mã trạng thái.

`awk` cũng có thể tổng hợp dữ liệu:

```bash
awk '{count[$9]++} END {for (s in count) print s, count[s]}' access.log
```

`awk` thực chất là một ngôn ngữ lập trình nhỏ, không chỉ là công cụ in cột.

Tuy nhiên nhật ký thực tế có thể chứa trường trong dấu nháy, JSON hoặc stack trace nhiều dòng. Không nên giả định mọi dữ liệu đều tách được bằng khoảng trắng. Với nhật ký JSON, `jq` thường phù hợp hơn nếu có sẵn.

## `sed`: chỉnh sửa luồng văn bản

`sed` phù hợp với các phép biến đổi theo dòng:

```bash
sed 's/http:/https:/g' config.txt
```

Mặc định kết quả được in ra `stdout`, còn tệp gốc không thay đổi. Điều này cho phép kiểm tra trước:

```bash
sed 's/old/new/g' app.conf | less
```

Sau khi chắc chắn mới chỉnh trực tiếp, ví dụ:

```bash
sed -i.bak 's/old/new/g' app.conf
```

Sao lưu trước thay thế tự động đặc biệt quan trọng với cấu hình production.

## `cut`, `tr` và `paste`

Với định dạng có dấu phân cách đơn giản:

```bash
cut -d: -f1 /etc/passwd
```

lấy trường tên người dùng.

`tr` biến đổi ký tự:

```bash
echo "$PATH" | tr ':' '\n'
```

biến `PATH` thành từng dòng để dễ đọc.

Các công cụ này phù hợp với định dạng đơn giản. Với CSV thật sự có dấu phẩy trong trường được đặt dấu nháy, trường nhiều dòng hoặc quy tắc escape, nên dùng trình phân tích CSV đúng chuẩn thay vì ép `cut` xử lý một ngữ pháp mà nó không hiểu.

## `head`, `tail`, `less`: lấy mẫu và điều hướng dữ liệu

Không phải lúc nào cũng cần xử lý toàn bộ dữ liệu. Trước hết nên xem hình dạng của dữ liệu:

```bash
head -n 5 access.log
tail -n 20 access.log
less -N access.log
```

Một thói quen tốt ở mức vận hành nâng cao là xem mẫu trước để xác nhận định dạng rồi mới viết `awk '$9...'`. Nếu giả định về cấu trúc sai, pipeline vẫn có thể chạy đúng cú pháp nhưng trả về kết quả sai về ý nghĩa.

## Nhật ký đã nén

Cơ chế xoay vòng nhật ký thường tạo tệp `.gz`. Không cần giải nén chỉ để tìm kiếm:

```bash
zgrep -Ein 'ERROR|Exception' app.log.2.gz
zless app.log.2.gz
```

Cách này giảm thao tác không cần thiết và giữ thư mục làm việc sạch hơn.

## `tee`: vừa quan sát vừa lưu bằng chứng

```bash
curl -v https://service.example 2>&1 | tee curl-debug.txt
```

Đầu ra vẫn xuất hiện trên terminal đồng thời được ghi vào tệp. Khi xử lý sự cố, việc lưu bằng chứng trước và sau thay đổi giúp so sánh trạng thái có cơ sở hơn.

## Dữ liệu phân cách bằng NUL và tên tệp an toàn

Tên tệp trên Unix có thể chứa khoảng trắng và thậm chí ký tự xuống dòng. Pipeline dựa hoàn toàn vào newline có thể sai với các tên bất thường. `find` và `xargs` hỗ trợ ký tự NUL làm dấu phân cách:

```bash
find . -type f -name '*.log' -print0 | xargs -0 grep -n 'ERROR'
```

Đây là kiến thức nâng cao không phải vì cú pháp phức tạp, mà vì nó tôn trọng mô hình dữ liệu thật thay vì giả định tên tệp luôn "đẹp".

## Hiệu năng: lọc sớm và thu hẹp phạm vi

Tìm kiếm toàn bộ `/` khi chỉ cần `/opt/app` vừa chậm vừa tạo nhiều lỗi quyền không liên quan. Một truy vấn điều tra sự cố tốt nên thu hẹp thời gian, đường dẫn và mẫu càng sớm càng tốt.

Thay vì:

```bash
grep -R ERROR /
```

hãy xác định nguồn nhật ký và khoảng thời gian:

```bash
journalctl -u app --since '16:00' --until '16:15' | grep -E 'ERROR|Exception'
```

Phạm vi tốt không chỉ làm câu lệnh chạy nhanh hơn mà còn giảm lượng bằng chứng không liên quan, từ đó làm quá trình suy luận chính xác hơn.

## Mô hình tư duy (Mental Model)

Có thể xem xử lý văn bản trên dòng lệnh như một **bộ máy truy vấn (query engine)** được tách thành nhiều toán tử nhỏ. Mỗi bước nên có trách nhiệm rõ: chọn nguồn, lọc, biến đổi, tổng hợp hoặc trình bày. Khi kết quả sai, hãy kiểm tra từng bước thay vì nhìn toàn pipeline như một câu thần chú.

## Những hiểu lầm phổ biến (Common Misconceptions)

**"`grep` dùng để tìm tệp."** `grep` chủ yếu tìm nội dung; `find` truy vấn các mục trong hệ thống tệp. Hai công cụ thường được kết hợp.

**"`uniq` tự tìm mọi dòng trùng."** Nó chỉ xử lý các dòng trùng nằm liền kề; thường cần `sort` trước.

**"Trường số 9 của `awk` luôn là mã HTTP."** Chỉ đúng với định dạng nhật ký cụ thể. Luôn xác minh cấu trúc dữ liệu.

**"`sed -i` nhanh nên có thể dùng ngay."** Xem trước kết quả biến đổi giúp tránh chỉnh sửa hàng loạt sai.

**"Đầu ra câu lệnh luôn là dữ liệu có cấu trúc ổn định."** Đầu ra dành cho con người có thể thay đổi theo phiên bản hoặc locale. Script production nên ưu tiên giao diện đọc bằng máy khi công cụ có hỗ trợ.

## Kết nối kiến thức

Xử lý văn bản là cầu nối giữa shell và khả năng quan sát hệ thống (observability). Khi chuyển sang [Nhật ký và khả năng quan sát](../05_system/logging_journal_observability.md), các mẫu lọc và tổng hợp này sẽ được dùng để xây dựng giả thuyết từ dữ liệu thay vì chỉ "tail rồi nhìn".