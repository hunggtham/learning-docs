# Shell, Bash, pipe và chuyển hướng

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Shell, Bash, pipe và chuyển hướng**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Shell và terminal khác nhau** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Từ văn bản tới lệnh thực thi** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối shell, Bash, pipe và redirection với file descriptor và process, để thấy dữ liệu đi qua lệnh bằng cơ chế nào.

Shell không phải Linux kernel và cũng không chỉ là nơi nhập câu lệnh. **Trình vỏ lệnh (shell)** là một bộ thông dịch ngôn ngữ lệnh: nó đọc văn bản, phân tích cú pháp, mở rộng biến và mẫu tên tệp, thiết lập bộ mô tả tệp, khởi chạy chương trình, quản lý tác vụ và trả về mã thoát (exit status). Hiểu shell theo chuỗi xử lý này giúp tránh nhiều lỗi mà việc học thuộc câu lệnh không thể giải quyết.

## Shell và terminal khác nhau

Trình mô phỏng terminal như PuTTY, Windows Terminal hoặc iTerm cung cấp giao diện vào/ra. SSH tạo phiên làm việc từ xa. Shell như Bash, Zsh hoặc `sh` là chương trình chạy bên trong phiên đó và diễn giải câu lệnh người dùng nhập.

Có thể kiểm tra:

```bash
echo "$SHELL"
ps -p $$ -o pid,ppid,cmd
```

`$$` thường là `PID` của shell hiện tại.

> **Chuyển mạch:** Trong **Shell, Bash, pipe và chuyển hướng**, **Từ văn bản tới lệnh thực thi** tiếp nhận điểm tựa từ **Shell và terminal khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dấu nháy và tách từ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Từ văn bản tới lệnh thực thi

Khi nhập:

```bash
grep -i "$PATTERN" *.log > result.txt
```

shell không chuyển nguyên chuỗi này cho `grep`. Nó phải nhận diện cách đặt dấu nháy (quoting), mở rộng `$PATTERN`, mở rộng mẫu `*.log`, xử lý chuyển hướng rồi mới gọi chương trình thực thi với danh sách đối số cuối cùng.

Quy tắc mở rộng của shell có nhiều chi tiết, nhưng mô hình tư duy quan trọng là: **văn bản bạn gõ không nhất thiết giống danh sách đối số mà chương trình cuối cùng nhận được**.

> **Chuyển mạch:** Ở chặng này của **Shell, Bash, pipe và chuyển hướng**, **Dấu nháy và tách từ** tiếp nhận điểm tựa từ **Từ văn bản tới lệnh thực thi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Globbing không phải biểu thức chính quy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dấu nháy và tách từ

Giả sử:

```bash
DIR="/opt/My App"
```

Nếu chạy:

```bash
cd $DIR
```

shell có thể tách giá trị thành hai từ `/opt/My` và `App`. Viết:

```bash
cd "$DIR"
```

giữ toàn bộ giá trị thành một đối số.

Dấu nháy đơn ngăn hầu hết quá trình mở rộng:

```bash
echo '$HOME'
```

lệnh trên in nguyên `$HOME`. Dấu nháy kép vẫn cho phép mở rộng biến và thay thế kết quả lệnh:

```bash
echo "home=$HOME time=$(date)"
```

Một thói quen quan trọng là **đặt mở rộng biến trong dấu nháy kép**, trừ khi bạn thật sự muốn shell tách từ hoặc mở rộng mẫu tên tệp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Shell, Bash, pipe và chuyển hướng**, **Globbing không phải biểu thức chính quy** tiếp nhận điểm tựa từ **Dấu nháy và tách từ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mã thoát: giao diện biểu thị thành công hoặc thất bại** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Globbing không phải biểu thức chính quy

Mẫu shell:

```bash
ls *.log
```

được shell mở rộng thành danh sách tên tệp khớp trước khi `ls` chạy. `*` ở đây là **mẫu glob**, không phải biểu thức chính quy (regular expression / regex) `.*`.

Đó là lý do khi dùng `find` nên đặt mẫu trong dấu nháy:

```bash
find . -name '*.log'
```

Nếu không đặt dấu nháy, shell hiện tại có thể mở rộng `*.log` trước, khiến `find` nhận danh sách đối số khác dự kiến.

> **Chuyển mạch:** Trong **Shell, Bash, pipe và chuyển hướng**, **Mã thoát: giao diện biểu thị thành công hoặc thất bại** tiếp nhận điểm tựa từ **Globbing không phải biểu thức chính quy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Pipe và trạng thái của chuỗi xử lý (pipeline / 파이프라인)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mã thoát: giao diện biểu thị thành công hoặc thất bại

Chương trình Unix trả về một số nguyên gọi là **mã thoát (exit status)**. Quy ước phổ biến là `0` biểu thị thành công, còn giá trị khác `0` biểu thị thất bại hoặc một điều kiện khác mà chương trình định nghĩa.

```bash
grep ERROR app.log
echo $?
```

`$?` là mã thoát của câu lệnh gần nhất.

Các toán tử shell dùng mã này để tạo luồng điều khiển:

```bash
nginx -t && sudo systemctl reload nginx
```

Lệnh reload chỉ chạy nếu kiểm tra cấu hình thành công.

```bash
curl -fsS http://localhost:8080/health || echo "health check failed"
```

Lệnh phía sau `||` chỉ chạy nếu `curl` thất bại. Đây là **luồng điều khiển (control flow)** chứ không chỉ là cách viết ngắn.

> **Chuyển mạch:** Ở chặng này của **Shell, Bash, pipe và chuyển hướng**, **Mã thoát: giao diện biểu thị thành công hoặc thất bại** xác định đầu vào; **Pipe và trạng thái của chuỗi xử lý (pipeline / 파이프라인)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Chuyển hướng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Pipe và trạng thái của chuỗi xử lý (pipeline / 파이프라인)

Trước khi chạy hoặc đọc ví dụ dưới đây, hãy xác định câu hỏi vận hành mà nó trả lời, dữ liệu nào sẽ quan sát được và giới hạn của kết quả. Lệnh chỉ có ý nghĩa khi gắn với một giả thuyết về state của hệ thống.

```bash
producer | filter | consumer
```

Shell nối các bộ mô tả tệp giữa nhiều tiến trình. Trong Bash mặc định, mã thoát của một chuỗi xử lý (pipeline / 파이프라인) thường là mã của câu lệnh cuối, vì vậy lỗi ở câu lệnh trước có thể bị che khuất.

Trong script nghiêm túc thường gặp:

```bash
set -o pipefail
```

Khi bật `pipefail`, chuỗi xử lý (pipeline / 파이프라인) có thể phản ánh lỗi của một thành phần trước thay vì chỉ dựa vào câu lệnh cuối. Cấu hình `set -euo pipefail` rất phổ biến nhưng cần hiểu rõ trước khi sao chép máy móc, vì `set -e` có nhiều trường hợp biên (edge case / 경계 사례) và có thể làm script kết thúc ở nơi người viết không dự kiến.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Shell, Bash, pipe và chuyển hướng**, **Pipe và trạng thái của chuỗi xử lý (pipeline / 파이프라인)** xác định đầu vào; **Chuyển hướng** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Biến shell và biến môi trường** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chuyển hướng

Sau khi hiểu [bộ mô tả tệp](../01_filesystem/files_streams_descriptors.md), cú pháp chuyển hướng có thể đọc như cách đấu nối các luồng I/O:

```bash
command >out.log 2>error.log
```

`stdout` đi vào `out.log`, còn `stderr` đi vào `error.log`.

```bash
command >>out.log 2>&1
```

`stdout` được ghi nối tiếp vào tệp, còn `stderr` được sao chép tới cùng đích.

Trong Bash:

```bash
command &>all.log
```

có thể chuyển cả `stdout` và `stderr`, nhưng cách `>file 2>&1` thường dễ gặp hơn trong nhiều môi trường shell khác nhau.

> **Chuyển mạch:** Trong **Shell, Bash, pipe và chuyển hướng**, **Biến shell và biến môi trường** tiếp nhận điểm tựa từ **Chuyển hướng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thay thế kết quả câu lệnh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Biến shell và biến môi trường

Biến shell tồn tại trong shell hiện tại:

```bash
NAME=app
```

Tiến trình con chỉ nhận biến đó qua môi trường nếu nó được xuất (export):

```bash
export NAME
```

hoặc có thể đặt biến chỉ cho một câu lệnh:

```bash
NAME=app ./run.sh
```

Điều này giải thích một lỗi kinh điển: chạy ứng dụng thủ công thì hoạt động nhưng dịch vụ systemd lại thất bại vì môi trường của shell tương tác không tự động được truyền vào trình quản lý dịch vụ.

> **Chuyển mạch:** Ở chặng này của **Shell, Bash, pipe và chuyển hướng**, **Thay thế kết quả câu lệnh** tiếp nhận điểm tựa từ **Biến shell và biến môi trường** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Gom nhóm lệnh và subshell** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thay thế kết quả câu lệnh

Phần này chuyển khái niệm Linux thành thao tác hoặc bằng chứng có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu output với mô hình kernel, process, filesystem hoặc network đã học.

```bash
backup="app.$(date +%F_%H%M%S).bak"
cp -a app.conf "$backup"
```

`$(...)` chạy câu lệnh bên trong và thay biểu thức bằng `stdout` của câu lệnh đó. Đây là một luồng dữ liệu từ chương trình quay trở lại biểu thức shell.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Shell, Bash, pipe và chuyển hướng**, **Gom nhóm lệnh và subshell** tiếp nhận điểm tựa từ **Thay thế kết quả câu lệnh** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hàm shell** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Gom nhóm lệnh và subshell

Dấu ngoặc tròn tạo **shell con (subshell)** trong nhiều ngữ cảnh:

```bash
(cd /var/log && grep ERROR app.log)
```

`cd` chỉ ảnh hưởng shell con; sau khi biểu thức kết thúc, shell hiện tại vẫn ở thư mục cũ.

Dấu ngoặc nhọn gom nhóm các lệnh trong shell hiện tại:

```bash
{ date; hostname; uptime; } > snapshot.txt
```

Toàn bộ đầu ra của nhóm được chuyển hướng chỉ một lần.

> **Chuyển mạch:** Trong **Shell, Bash, pipe và chuyển hướng**, **Hàm shell** tiếp nhận điểm tựa từ **Gom nhóm lệnh và subshell** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **xargs và xây dựng danh sách đối số** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hàm shell

Hàm shell giúp đóng gói một luồng công việc nhỏ:

```bash
check_app() {
  systemctl status app --no-pager
  ss -lntp | grep ':8080'
  curl -fsS http://127.0.0.1:8080/health
}
```

Khi lô-gic (logic / 논리) lớn, cần cấu trúc dữ liệu phức tạp, kiểm thử nghiêm túc hoặc xử lý đồng thời, một ngôn ngữ như Python hoặc Go thường phù hợp hơn. Shell mạnh nhất khi dùng để **điều phối (orchestration)** các công cụ hệ thống nhỏ.

> **Chuyển mạch:** Ở chặng này của **Shell, Bash, pipe và chuyển hướng**, **xargs và xây dựng danh sách đối số** tiếp nhận điểm tựa từ **Hàm shell** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Điều khiển tác vụ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `xargs` và xây dựng danh sách đối số

Pipe truyền byte qua `stdin`; không phải chương trình nào cũng hiểu dữ liệu `stdin` như danh sách đối số. `xargs` chuyển đầu vào thành các đối số cho một câu lệnh:

```bash
find . -type f -name '*.log' -print0 | xargs -0 grep -n ERROR
```

Cặp `-print0` và `-0` dùng ký tự NUL làm dấu phân cách, an toàn hơn với tên tệp chứa khoảng trắng hoặc xuống dòng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Shell, Bash, pipe và chuyển hướng**, **Điều khiển tác vụ** tiếp nhận điểm tựa từ **xargs và xây dựng danh sách đối số** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Điều khiển tác vụ

Shell tương tác quản lý các nhóm tiến trình chạy ở tiền cảnh và hậu cảnh. `Ctrl+Z` thường tạm dừng tác vụ tiền cảnh; `bg` tiếp tục nó ở hậu cảnh; `fg` đưa lại tiền cảnh; `jobs` hiển thị các tác vụ do shell hiện tại quản lý.

```bash
sleep 300 &
jobs -l
```

Đây là tiện ích dành cho phiên tương tác, không phải cơ chế giám sát tiến trình môi trường vận hành (production / 운영 환경). Dịch vụ chạy lâu dài nên được systemd hoặc một trình giám sát bộ chứa (container / 컨테이너) quản lý để có chính sách khởi động lại, nhật ký và vòng đời rõ ràng.

> **Chuyển mạch:** Trong **Shell, Bash, pipe và chuyển hướng**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Điều khiển tác vụ** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những hiểu lầm phổ biến (Common Misconceptions)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Có thể xem shell như một **bộ biên dịch điều phối nhỏ**. Nó biến văn bản thành danh sách đối số, môi trường, cách nối tệp (file / 파일) descriptor và các lần khởi chạy tiến trình. Khi câu lệnh cho kết quả bất ngờ, trước hết hãy hỏi shell đã biến văn bản ban đầu thành gì, rồi mới hỏi chương trình đích đã làm gì.

Một kỹ thuật gỡ lỗi script:

```bash
bash -x script.sh
```

`-x` hiển thị các câu lệnh sau quá trình mở rộng ở mức rất hữu ích, giúp quan sát luồng điều khiển thực tế.

> **Chuyển mạch:** Ở chặng này của **Shell, Bash, pipe và chuyển hướng**, **Những hiểu lầm phổ biến (Common Misconceptions)** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối sang chương tiếp theo** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu lầm phổ biến (Common Misconceptions)

**"Khoảng trắng chỉ để định dạng câu lệnh."** Khoảng trắng thường phân tách từ và đối số; dấu nháy thay đổi ý nghĩa này.

**"`*` là regex."** Trên dòng lệnh shell, nó thường là glob do shell xử lý.

**"Biến shell tự động có trong mọi tiến trình."** Chỉ biến môi trường đã được export mới được truyền cho tiến trình con.

**"`cmd1 | cmd2` nghĩa là cmd1 chạy xong rồi cmd2 mới bắt đầu."** Các tiến trình trong chuỗi xử lý (pipeline / 파이프라인) thường có thể chạy đồng thời và truyền dữ liệu theo luồng.

**"`nohup` là trình quản lý dịch vụ."** Nó chỉ giải quyết một phần vấn đề liên quan phiên làm việc và `SIGHUP`; nó không cung cấp đầy đủ cơ chế giám sát vòng đời dịch vụ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Shell, Bash, pipe và chuyển hướng**, **Kết nối sang chương tiếp theo** tiếp nhận điểm tựa từ **Những hiểu lầm phổ biến (Common Misconceptions)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối sang chương tiếp theo

Shell mạnh vì các công cụ Linux có giao diện văn bản và luồng dữ liệu dễ kết hợp. [Xử lý văn bản](./text_processing.md) giải thích cách `grep`, `find`, `sed`, `awk`, `sort` và `uniq` phối hợp để biến dữ liệu thô trên máy chủ thành bằng chứng có thể phân tích.

> **Bàn giao:** Sau **Kết nối sang chương tiếp theo**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
