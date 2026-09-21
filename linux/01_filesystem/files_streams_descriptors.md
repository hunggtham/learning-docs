# Tệp, luồng dữ liệu và bộ mô tả tệp

Nếu chương về hệ thống tệp trả lời câu hỏi một đường dẫn dẫn tới đối tượng như thế nào, chương này trả lời tiến trình **giữ và trao đổi dữ liệu với đối tượng đó bằng cách nào**. **Bộ mô tả tệp (file descriptor / 파일 디스크립터)** là một trong những lớp trừu tượng mạnh nhất của Unix/Linux vì nó cho phép tệp thông thường, terminal, pipe và socket cùng tham gia vào một mô hình vào/ra (I/O) tương đối thống nhất.

## Vấn đề cần giải quyết

Một tiến trình có thể cần đọc tệp cấu hình, ghi nhật ký, nhận dữ liệu bàn phím, gửi đầu ra ra terminal hoặc truyền byte qua kết nối TCP. Nếu mỗi loại tài nguyên có một giao diện hoàn toàn khác nhau, việc kết hợp câu lệnh trong shell và lập trình ứng dụng sẽ phức tạp hơn rất nhiều.

Linux cung cấp cho mỗi tiến trình một bảng các file descriptor. File descriptor thường là một số nguyên nhỏ và đóng vai trò như tay cầm (handle) dẫn tới một điểm cuối I/O đang mở.

## Các luồng chuẩn

Khi shell khởi chạy một chương trình thông thường, chương trình thường nhận ba bộ mô tả chuẩn:

| FD | Tên | Ý nghĩa |
|---:|---|---|
| `0` | `stdin` | đầu vào chuẩn (standard input) |
| `1` | `stdout` | đầu ra chuẩn (standard output) |
| `2` | `stderr` | đầu ra lỗi chuẩn (standard error) |

Điểm quan trọng là chương trình không nhất thiết biết `stdout` đang đi đâu. Đích có thể là terminal, tệp hoặc pipe.

```bash
echo hello
```

Trong trường hợp bình thường, shell để `stdout` của `echo` trỏ tới terminal. Nhưng với:

```bash
echo hello > output.txt
```

shell thiết lập lại file descriptor trước khi chương trình chạy để `FD 1` trỏ tới `output.txt`. `echo` không cần có mã riêng cho tình huống "ghi vào tệp output.txt".

Đây là một ví dụ rõ về **tách biệt trách nhiệm (separation of concerns)**: chương trình tạo dữ liệu đầu ra, còn shell quyết định dữ liệu đó được chuyển tới đâu.

## Chuyển hướng là thay đổi cách nối các luồng I/O

```bash
command > out.log
```

`>` chuyển hướng `stdout` vào tệp.

```bash
command 2> error.log
```

`2>` chuyển hướng `stderr`.

```bash
command > all.log 2>&1
```

Trước tiên `FD 1` được nối tới `all.log`; sau đó `FD 2` được sao chép để trỏ tới cùng đích hiện tại của `FD 1`.

Thứ tự rất quan trọng. Shell xử lý chuyển hướng từ trái sang phải, vì vậy:

```bash
command 2>&1 > all.log
```

không nhất thiết tương đương. Khi `2>&1` xảy ra trước, `stderr` được nối tới đích mà `stdout` đang dùng **tại thời điểm đó**, thường là terminal; sau đó chỉ `stdout` mới chuyển sang tệp.

Đây không phải cú pháp bí ẩn. Nó là thao tác thay đổi đồ thị kết nối của các file descriptor.

## Pipe là gì?

**Đường ống (pipe)** là một kênh giao tiếp do kernel quản lý, có đầu ghi và đầu đọc. Biểu thức:

```bash
ps -ef | grep java
```

khiến shell tạo một pipe, nối `stdout` của `ps` vào đầu ghi và `stdin` của `grep` vào đầu đọc. Hai chương trình có thể chạy đồng thời và các byte được truyền qua bộ đệm của kernel.

Mô hình tư duy:

```text
ps stdout (FD 1) -> [pipe] -> grep stdin (FD 0)
```

Vì vậy pipeline không đơn giản là "chạy lệnh đầu xong rồi sao chép toàn bộ văn bản sang lệnh sau". Với lượng dữ liệu đủ lớn, bên tạo dữ liệu và bên tiêu thụ có thể hoạt động đồng thời theo kiểu truyền dòng (streaming), đồng thời pipe buffer tạo ra cơ chế ép tốc độ ngược (backpressure) ở mức nhất định.

## Vì sao cần `stderr` riêng?

Nếu dữ liệu bình thường và thông báo lỗi cùng đi qua `stdout`, pipeline xử lý dữ liệu sẽ bị lẫn nội dung chẩn đoán. `stderr` tạo một kênh riêng cho thông báo lỗi.

Ví dụ:

```bash
find / -name app.log 2>/dev/null
```

`stdout` vẫn chứa các đường dẫn tìm thấy, còn lỗi quyền truy cập trên `stderr` được chuyển vào `/dev/null`.

Khi xử lý sự cố, không nên luôn loại bỏ `stderr` vì đó có thể là bằng chứng quan trọng. Có thể lưu hai luồng riêng:

```bash
find / -name app.log >results.txt 2>errors.txt
```

## `/dev/null` và `/dev/zero`

`/dev/null` là một điểm cuối thiết bị bỏ mọi dữ liệu được ghi vào và trả về cuối luồng khi đọc. Nó hữu ích khi ta thực sự không cần một luồng đầu ra.

```bash
command >/dev/null 2>&1
```

`/dev/zero` trả về các byte bằng 0 khi đọc và có nhiều trường hợp sử dụng ở mức hệ thống. Hai đường dẫn này minh họa rằng vùng tên `/dev` chứa các đối tượng không phải tệp dữ liệu thông thường trên đĩa nhưng vẫn dùng giao diện I/O giống tệp.

## Bộ mô tả tệp đang mở và trạng thái tiến trình

Có thể quan sát các file descriptor của một tiến trình qua:

```bash
ls -l /proc/<PID>/fd
```

Với shell hiện tại:

```bash
ls -l /proc/$$/fd
```

Các mục ở đây cho biết từng FD đang trỏ tới terminal, pipe, socket hoặc tệp nào. `lsof` cung cấp cách nhìn dễ đọc hơn:

```bash
sudo lsof -p 12345
```

Khi ứng dụng báo `Too many open files`, vấn đề thường liên quan số file descriptor hoặc giới hạn tài nguyên chứ không phải dung lượng đĩa.

```bash
cat /proc/12345/limits
```

Hãy kiểm tra mục `Max open files`.

## Rò rỉ bộ mô tả tệp

Nếu ứng dụng mở tệp hoặc socket nhưng không đóng đúng cách, số file descriptor đang mở có thể tăng dần. Khi chạm giới hạn, những thao tác nhìn bề ngoài không liên quan cũng có thể thất bại vì tiến trình không thể tạo thêm descriptor.

Có thể bắt đầu điều tra bằng:

```bash
ls /proc/12345/fd | wc -l
lsof -p 12345 | head
```

Theo dõi số lượng theo thời gian hữu ích hơn một ảnh chụp tức thời. Nếu số FD tăng liên tục theo lưu lượng, cần kiểm tra vòng đời tài nguyên trong mã nguồn.

Mối liên hệ với Java rất rõ: `InputStream`, `OutputStream`, socket hoặc tài nguyên JDBC cuối cùng đều phụ thuộc vào tài nguyên của hệ điều hành. `try-with-resources` không chỉ là phong cách viết mã; nó giúp bảo đảm tài nguyên nền được giải phóng đúng vòng đời.

## Bộ đệm

Khi chương trình gọi một hàm ghi ở tầng cao, dữ liệu không nhất thiết lập tức tới thiết bị lưu trữ hoặc mạng. Bộ đệm (buffering) có thể tồn tại ở ứng dụng, môi trường chạy, `libc`, bộ nhớ đệm trang của kernel, hệ thống tệp, bộ nhớ đệm thiết bị hoặc ngăn xếp mạng.

Vì vậy "đã gọi `write`" không đồng nghĩa với "byte đã được lưu bền vững trên thiết bị vật lý". Tính bền vững của cơ sở dữ liệu phải quan tâm tới `fsync` và quy tắc của hệ thống lưu trữ; nhật ký thời gian thực qua pipe đôi khi cần bộ đệm theo dòng.

Ví dụ:

```bash
tail -F app.log | grep --line-buffered ERROR
```

`--line-buffered` yêu cầu GNU `grep` đẩy đầu ra theo từng dòng để giảm độ trễ trong pipeline truyền dòng.

## Vị trí đọc/ghi và trạng thái dùng chung

Đối tượng tệp đã mở trong kernel có trạng thái như vị trí hiện tại (current offset). Khi tiến trình đọc tuần tự, vị trí này tiến lên. Các descriptor có thể được sao chép và trong một số trường hợp chia sẻ trạng thái tệp đang mở bên dưới. Vì vậy file descriptor không chỉ là "số thứ tự tệp"; nó là một tay cầm tới trạng thái mà kernel đang duy trì.

## Socket cũng được biểu diễn bằng file descriptor

Khi máy chủ tạo socket, thực hiện `bind`, `listen` và `accept`, mỗi kết nối thường được ứng dụng nhìn thông qua một file descriptor. Công cụ như:

```bash
sudo lsof -nP -iTCP:8080
```

kết nối góc nhìn tiến trình với góc nhìn mạng. Phần này được giải thích sâu hơn tại [Mạng, DNS, socket và cổng](../07_networking/networking_dns_sockets_ports.md).

## Mô hình tư duy (Mental Model)

Hãy hình dung mỗi tiến trình có một **bảng các ổ cắm I/O**. Số descriptor là nhãn của ổ cắm; đối tượng phía sau có thể là terminal, tệp, pipe hoặc socket. Chuyển hướng và pipe không sửa logic nghiệp vụ của chương trình; shell chỉ đấu lại các ổ cắm trước khi chương trình chạy.

Mô hình này giúp hiểu cú pháp shell mà không cần học thuộc từng ký hiệu như những quy tắc rời rạc.

## Những hiểu lầm phổ biến (Common Misconceptions)

**"`stdout` nghĩa là màn hình."** `stdout` chỉ là descriptor số 1. Terminal là đích mặc định phổ biến chứ không phải bản chất của `stdout`.

**"Pipe là một tệp tạm."** Pipe ẩn danh là đối tượng giao tiếp do kernel quản lý, không phải tệp lưu trữ lâu dài.

**"Chuyển hướng chỉ là sao chép văn bản."** Shell thiết lập file descriptor để chương trình sử dụng; bản chất là thay đổi cách nối I/O.

**"Đưa tiến trình xuống nền thì đóng terminal vẫn chắc chắn chạy."** Tiến trình có thể nhận `SIGHUP` hoặc mất tài nguyên gắn với terminal. Với dịch vụ lâu dài trong production, trình quản lý dịch vụ ổn định hơn `nohup`.

## Từ file descriptor tới shell

Khi đã hiểu file descriptor, các ký hiệu `|`, `>`, `>>`, `2>`, `2>&1` trở thành hệ quả tự nhiên của mô hình I/O. Chương tiếp theo [Shell, Bash, pipe và chuyển hướng](../02_shell/shell_bash_pipes_redirection.md) mở rộng từ việc nối I/O sang cách phân tích lệnh, mở rộng biểu thức, mã thoát và kết hợp câu lệnh.