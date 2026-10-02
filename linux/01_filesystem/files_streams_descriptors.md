# Tệp, luồng dữ liệu và bộ mô tả tệp

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Tệp, luồng dữ liệu và bộ mô tả tệp**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Vấn đề cần giải quyết** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Các luồng chuẩn** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối bộ mô tả tệp với luồng byte và các luồng chuẩn, giúp thấy cùng một giao diện I/O đang được tái sử dụng ra sao.

Nếu chương về hệ thống tệp trả lời câu hỏi một đường dẫn dẫn tới đối tượng như thế nào, chương này trả lời tiến trình **giữ và trao đổi dữ liệu với đối tượng đó bằng cách nào**. **Bộ mô tả tệp (file descriptor / 파일 디스크립터)** là một trong những lớp trừu tượng mạnh nhất của Unix/Linux vì nó cho phép tệp thông thường, terminal, pipe và socket cùng tham gia vào một mô hình vào/ra (I/O) tương đối thống nhất.

## Vấn đề cần giải quyết

Một tiến trình có thể cần đọc tệp cấu hình, ghi nhật ký, nhận dữ liệu bàn phím, gửi đầu ra ra terminal hoặc truyền byte qua kết nối TCP. Nếu mỗi loại tài nguyên có một giao diện hoàn toàn khác nhau, việc kết hợp câu lệnh trong shell và lập trình ứng dụng sẽ phức tạp hơn rất nhiều.

Linux cung cấp cho mỗi tiến trình một bảng các tệp (file / 파일) descriptor. tệp (file / 파일) descriptor thường là một số nguyên nhỏ và đóng vai trò như tay cầm (handle) dẫn tới một điểm cuối I/O đang mở.

> **Chuyển mạch:** Trong **Tệp, luồng dữ liệu và bộ mô tả tệp**, **Các luồng chuẩn** tiếp nhận điểm tựa từ **Vấn đề cần giải quyết** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chuyển hướng là thay đổi cách nối các luồng I/O** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

shell thiết lập lại tệp (file / 파일) descriptor trước khi chương trình chạy để `FD 1` trỏ tới `output.txt`. `echo` không cần có mã riêng cho tình huống "ghi vào tệp đầu ra (output / 출력).txt".

Đây là một ví dụ rõ về **tách biệt trách nhiệm (separation of concerns)**: chương trình tạo dữ liệu đầu ra, còn shell quyết định dữ liệu đó được chuyển tới đâu.

> **Chuyển mạch:** Ở chặng này của **Tệp, luồng dữ liệu và bộ mô tả tệp**, **Chuyển hướng là thay đổi cách nối các luồng I/O** tiếp nhận điểm tựa từ **Các luồng chuẩn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Pipe là gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chuyển hướng là thay đổi cách nối các luồng I/O

Phần này chuyển khái niệm Linux thành thao tác hoặc bằng chứng có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu output với mô hình kernel, process, filesystem hoặc network đã học.

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

Đây không phải cú pháp bí ẩn. Nó là thao tác thay đổi đồ thị kết nối của các tệp (file / 파일) descriptor.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tệp, luồng dữ liệu và bộ mô tả tệp**, **Pipe là gì?** tiếp nhận điểm tựa từ **Chuyển hướng là thay đổi cách nối các luồng I/O** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vì sao cần stderr riêng?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Vì vậy chuỗi xử lý (pipeline / 파이프라인) không đơn giản là "chạy lệnh đầu xong rồi sao chép toàn bộ văn bản sang lệnh sau". Với lượng dữ liệu đủ lớn, bên tạo dữ liệu và bên tiêu thụ có thể hoạt động đồng thời theo kiểu truyền dòng (streaming), đồng thời pipe buffer tạo ra cơ chế ép tốc độ ngược (backpressure) ở mức nhất định.

> **Chuyển mạch:** Trong **Tệp, luồng dữ liệu và bộ mô tả tệp**, **Vì sao cần stderr riêng?** tiếp nhận điểm tựa từ **Pipe là gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **/dev/null và /dev/zero** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vì sao cần `stderr` riêng?

Nếu dữ liệu bình thường và thông báo lỗi cùng đi qua `stdout`, chuỗi xử lý (pipeline / 파이프라인) xử lý dữ liệu sẽ bị lẫn nội dung chẩn đoán. `stderr` tạo một kênh riêng cho thông báo lỗi.

Ví dụ:

```bash
find / -name app.log 2>/dev/null
```

`stdout` vẫn chứa các đường dẫn tìm thấy, còn lỗi quyền truy cập trên `stderr` được chuyển vào `/dev/null`.

Khi xử lý sự cố, không nên luôn loại bỏ `stderr` vì đó có thể là bằng chứng quan trọng. Có thể lưu hai luồng riêng:

```bash
find / -name app.log >results.txt 2>errors.txt
```

> **Chuyển mạch:** Ở chặng này của **Tệp, luồng dữ liệu và bộ mô tả tệp**, **/dev/null và /dev/zero** tiếp nhận điểm tựa từ **Vì sao cần stderr riêng?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bộ mô tả tệp đang mở và trạng thái tiến trình** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `/dev/null` và `/dev/zero`

`/dev/null` là một điểm cuối thiết bị bỏ mọi dữ liệu được ghi vào và trả về cuối luồng khi đọc. Nó hữu ích khi ta thực sự không cần một luồng đầu ra.

```bash
command >/dev/null 2>&1
```

`/dev/zero` trả về các byte bằng 0 khi đọc và có nhiều trường hợp sử dụng ở mức hệ thống. Hai đường dẫn này minh họa rằng vùng tên `/dev` chứa các đối tượng không phải tệp dữ liệu thông thường trên đĩa nhưng vẫn dùng giao diện I/O giống tệp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tệp, luồng dữ liệu và bộ mô tả tệp**, **Bộ mô tả tệp đang mở và trạng thái tiến trình** tiếp nhận điểm tựa từ **/dev/null và /dev/zero** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Rò rỉ bộ mô tả tệp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bộ mô tả tệp đang mở và trạng thái tiến trình

Có thể quan sát các tệp (file / 파일) descriptor của một tiến trình qua:

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

Khi ứng dụng báo `Too many open files`, vấn đề thường liên quan số tệp (file / 파일) descriptor hoặc giới hạn tài nguyên chứ không phải dung lượng đĩa.

```bash
cat /proc/12345/limits
```

Hãy kiểm tra mục `Max open files`.

> **Chuyển mạch:** Trong **Tệp, luồng dữ liệu và bộ mô tả tệp**, **Rò rỉ bộ mô tả tệp** tiếp nhận điểm tựa từ **Bộ mô tả tệp đang mở và trạng thái tiến trình** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bộ đệm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Rò rỉ bộ mô tả tệp

Nếu ứng dụng mở tệp hoặc socket nhưng không đóng đúng cách, số tệp (file / 파일) descriptor đang mở có thể tăng dần. Khi chạm giới hạn, những thao tác nhìn bề ngoài không liên quan cũng có thể thất bại vì tiến trình không thể tạo thêm descriptor.

Có thể bắt đầu điều tra bằng:

```bash
ls /proc/12345/fd | wc -l
lsof -p 12345 | head
```

Theo dõi số lượng theo thời gian hữu ích hơn một ảnh chụp tức thời. Nếu số FD tăng liên tục theo lưu lượng, cần kiểm tra vòng đời tài nguyên trong mã nguồn.

Mối liên hệ với Java rất rõ: `InputStream`, `OutputStream`, socket hoặc tài nguyên JDBC cuối cùng đều phụ thuộc vào tài nguyên của hệ điều hành. `try-with-resources` không chỉ là phong cách viết mã; nó giúp bảo đảm tài nguyên nền được giải phóng đúng vòng đời.

> **Chuyển mạch:** Ở chặng này của **Tệp, luồng dữ liệu và bộ mô tả tệp**, **Bộ đệm** tiếp nhận điểm tựa từ **Rò rỉ bộ mô tả tệp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vị trí đọc/ghi và trạng thái dùng chung** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bộ đệm

Khi chương trình gọi một hàm ghi ở tầng cao, dữ liệu không nhất thiết lập tức tới thiết bị lưu trữ hoặc mạng. Bộ đệm (buffering) có thể tồn tại ở ứng dụng, môi trường chạy, `libc`, bộ nhớ đệm trang của kernel, hệ thống tệp, bộ nhớ đệm thiết bị hoặc ngăn xếp mạng.

Vì vậy "đã gọi `write`" không đồng nghĩa với "byte đã được lưu bền vững trên thiết bị vật lý". Tính bền vững của cơ sở dữ liệu phải quan tâm tới `fsync` và quy tắc của hệ thống lưu trữ; nhật ký thời gian thực qua pipe đôi khi cần bộ đệm theo dòng.

Ví dụ:

```bash
tail -F app.log | grep --line-buffered ERROR
```

`--line-buffered` yêu cầu GNU `grep` đẩy đầu ra theo từng dòng để giảm độ trễ trong chuỗi xử lý (pipeline / 파이프라인) truyền dòng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tệp, luồng dữ liệu và bộ mô tả tệp**, **Vị trí đọc/ghi và trạng thái dùng chung** tiếp nhận điểm tựa từ **Bộ đệm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Socket cũng được biểu diễn bằng tệp (file / 파일) descriptor** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vị trí đọc/ghi và trạng thái dùng chung

Đối tượng tệp đã mở trong kernel có trạng thái như vị trí hiện tại (current offset). Khi tiến trình đọc tuần tự, vị trí này tiến lên. Các descriptor có thể được sao chép và trong một số trường hợp chia sẻ trạng thái tệp đang mở bên dưới. Vì vậy tệp (file / 파일) descriptor không chỉ là "số thứ tự tệp"; nó là một tay cầm tới trạng thái mà kernel đang duy trì.

> **Chuyển mạch:** Trong **Tệp, luồng dữ liệu và bộ mô tả tệp**, **Socket cũng được biểu diễn bằng tệp (file / 파일) descriptor** tiếp nhận điểm tựa từ **Vị trí đọc/ghi và trạng thái dùng chung** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Socket cũng được biểu diễn bằng tệp (file / 파일) descriptor

Khi máy chủ tạo socket, thực hiện `bind`, `listen` và `accept`, mỗi kết nối thường được ứng dụng nhìn thông qua một tệp (file / 파일) descriptor. Công cụ như:

```bash
sudo lsof -nP -iTCP:8080
```

kết nối góc nhìn tiến trình với góc nhìn mạng. Phần này được giải thích sâu hơn tại [Mạng, DNS, socket và cổng](../07_networking/networking_dns_sockets_ports.md).

> **Chuyển mạch:** Ở chặng này của **Tệp, luồng dữ liệu và bộ mô tả tệp**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Socket cũng được biểu diễn bằng tệp (file / 파일) descriptor** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những hiểu lầm phổ biến (Common Misconceptions)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Hãy hình dung mỗi tiến trình có một **bảng các ổ cắm I/O**. Số descriptor là nhãn của ổ cắm; đối tượng phía sau có thể là terminal, tệp, pipe hoặc socket. Chuyển hướng và pipe không sửa lô-gic (logic / 논리) nghiệp vụ của chương trình; shell chỉ đấu lại các ổ cắm trước khi chương trình chạy.

Mô hình này giúp hiểu cú pháp shell mà không cần học thuộc từng ký hiệu như những quy tắc rời rạc.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tệp, luồng dữ liệu và bộ mô tả tệp**, **Những hiểu lầm phổ biến (Common Misconceptions)** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Từ tệp (file / 파일) descriptor tới shell** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu lầm phổ biến (Common Misconceptions)

**"`stdout` nghĩa là màn hình."** `stdout` chỉ là descriptor số 1. Terminal là đích mặc định phổ biến chứ không phải bản chất của `stdout`.

**"Pipe là một tệp tạm."** Pipe ẩn danh là đối tượng giao tiếp do kernel quản lý, không phải tệp lưu trữ lâu dài.

**"Chuyển hướng chỉ là sao chép văn bản."** Shell thiết lập tệp (file / 파일) descriptor để chương trình sử dụng; bản chất là thay đổi cách nối I/O.

**"Đưa tiến trình xuống nền thì đóng terminal vẫn chắc chắn chạy."** Tiến trình có thể nhận `SIGHUP` hoặc mất tài nguyên gắn với terminal. Với dịch vụ lâu dài trong môi trường vận hành (production / 운영 환경), trình quản lý dịch vụ ổn định hơn `nohup`.

> **Chuyển mạch:** Trong **Tệp, luồng dữ liệu và bộ mô tả tệp**, **Từ tệp (file / 파일) descriptor tới shell** tiếp nhận điểm tựa từ **Những hiểu lầm phổ biến (Common Misconceptions)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Từ tệp (file / 파일) descriptor tới shell

Khi đã hiểu file descriptor, các ký hiệu `|`, `>`, `>>`, `2>`, `2>&1` trở thành hệ quả tự nhiên của mô hình I/O. Chương tiếp theo [Shell, Bash, pipe và chuyển hướng](../02_shell/shell_bash_pipes_redirection.md) mở rộng từ việc nối I/O sang cách phân tích lệnh, mở rộng biểu thức, mã thoát và kết hợp câu lệnh.

> **Bàn giao:** Sau **Từ tệp (file / 파일) descriptor tới shell**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
