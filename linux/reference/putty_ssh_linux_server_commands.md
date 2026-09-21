# PuTTY / SSH Linux Server Command Cheat Sheet — Extended

> Dùng khi SSH vào Linux server bằng PuTTY, Terminal, iTerm, Windows Terminal...
>
> Phiên bản này ưu tiên **giải thích rõ option**, **mọi dòng đều có ví dụ**, và có thêm cột **Thực tế / Senior tips** để phục vụ debug production.

---

# 1. Navigation — Di chuyển trong server

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `pwd` | In ra **absolute path** của working directory hiện tại. Dùng để xác nhận mình đang đứng ở đâu trước khi copy/xoá/chỉnh file. | `pwd` | Trước `rm -rf`, `chmod -R`, `chown -R` nên chạy `pwd && ls -la` để tránh thao tác nhầm thư mục production. |
| `ls` | Liệt kê file/folder trong directory hiện tại. Mặc định không hiện file ẩn bắt đầu bằng `.`. | `ls` | Dùng nhanh khi chỉ cần nhìn tên file. Với server nên quen `ls -lah`. |
| `ls -l` | `-l` = **long format**: permission, owner, group, size, modified time, filename. | `ls -l /opt/app` | Rất hữu ích để check owner/permission trước khi kết luận app “không đọc được file”. |
| `ls -a` | `-a` = **all**, hiển thị cả hidden files như `.env`, `.bashrc`, `.git`. | `ls -a ~` | Khi app chạy khác terminal, thường cần kiểm tra hidden config như `.env`, `.profile`. |
| `ls -la` | Kết hợp long format + hidden files. | `ls -la /home/app` | Một trong các lệnh nên thuộc lòng. |
| `ls -lh` | `-h` = **human-readable**, hiển thị size dạng KB/MB/GB thay vì byte. | `ls -lh app.log` | Dùng để nhìn nhanh log có phình bất thường hay không. |
| `ls -ltr` | `-t` sort theo modified time; `-r` đảo thứ tự. Kết quả: file cũ ở trên, file mới nhất ở cuối. | `ls -ltr /var/log/app` | Rất tiện khi muốn nhìn file log vừa sinh ra gần nhất ở cuối terminal. |
| `ls -lt` | Sort theo modified time, **mới nhất ở đầu**. | `ls -lt /var/log | head` | Hay dùng để xem 10 file vừa thay đổi gần nhất. |
| `ls -lS` | `-S` sort theo file size giảm dần. | `ls -lhS /var/log` | Dùng để tìm nhanh file log lớn. |
| `cd /path` | Đổi working directory sang path chỉ định. | `cd /var/log/nginx` | Có thể gõ `cd /var/log/nginx && ls -lah` để đổi folder và xem ngay. |
| `cd ..` | Đi lên parent directory một cấp. | `cd ..` | `cd ../../..` giúp lùi nhiều cấp nhanh. |
| `cd ~` | Về home directory của user hiện tại. | `cd ~` | `~` thường là `/home/user` hoặc `/root`. |
| `cd /` | Về filesystem root `/`. | `cd /` | Khác với `~`; `/` là gốc toàn server. |
| `cd -` | Quay lại directory trước đó và in path ra màn hình. | `cd -` | Senior dùng rất nhiều khi chuyển qua lại giữa 2 folder deploy/log. |
| `tree` | Hiển thị cấu trúc folder theo dạng cây. Có thể chưa được cài mặc định. | `tree /opt/app` | Dùng khi cần hiểu nhanh layout project/config. |
| `tree -L 2` | `-L` giới hạn số level hiển thị, tránh output quá dài. | `tree -L 2 /opt/app` | Thường tốt hơn `tree` trên project lớn. |

---

# 2. File & Folder — Tạo / xoá / copy / move

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `touch file` | Tạo file rỗng nếu file chưa tồn tại; nếu đã tồn tại thì cập nhật modified time. | `touch app.log` | Có thể dùng để kiểm tra permission ghi: `touch /path/test && rm /path/test`. |
| `mkdir dir` | Tạo một directory. Lỗi nếu parent chưa tồn tại. | `mkdir backup` | Dùng `mkdir -p` gần như luôn an toàn hơn trong script. |
| `mkdir -p a/b/c` | `-p` tạo cả parent directories còn thiếu và không báo lỗi nếu directory đã tồn tại. | `mkdir -p /opt/app/log/archive` | Rất hay dùng trong deploy script/idempotent script. |
| `cp src dst` | Copy file từ source sang destination. Nếu destination tồn tại sẽ bị ghi đè. | `cp app.conf app.conf.bak` | Trước sửa config production nên `cp -a file file.$(date +%F_%H%M%S).bak`. |
| `cp -r src dst` | `-r` = recursive, copy directory và toàn bộ nội dung con. | `cp -r config/ backup/` | Với Linux server, `cp -a` thường tốt hơn `cp -r` vì giữ metadata. |
| `cp -p src dst` | `-p` bảo toàn mode, owner/group nếu có quyền, timestamps. | `cp -p nginx.conf nginx.conf.bak` | Dùng khi backup config cần giữ timestamp/permission. |
| `cp -a src dst` | `-a` = archive: recursive + preserve symlink, permission, ownership, timestamp. | `cp -a /opt/app /opt/app_backup` | Đây là lựa chọn “chuẩn senior” để backup cây folder trước deploy. |
| `cp -i src dst` | `-i` hỏi trước khi overwrite file tồn tại. | `cp -i app.conf /etc/app.conf` | Hữu ích khi thao tác tay production để tránh ghi đè nhầm. |
| `cp -v src dst` | `-v` hiển thị file đang được copy. | `cp -av config/ backup/` | `-av` thường dùng để vừa giữ metadata vừa thấy tiến trình. |
| `mv src dst` | Move file/folder hoặc rename nếu source/destination cùng filesystem. | `mv app.log app.log.old` | Rename gần như tức thì, thường dùng rotate tạm log/config. |
| `mv -i src dst` | Hỏi trước khi overwrite destination. | `mv -i new.conf app.conf` | Nên dùng khi thay file config thủ công. |
| `rm file` | Xoá file. Không đưa vào recycle bin. | `rm old.log` | Production: nên `ls -l old.log` trước khi xoá. |
| `rm -f file` | `-f` = force: không hỏi và không báo lỗi nếu file không tồn tại. | `rm -f /tmp/app.pid` | Hay dùng trong script cleanup; nguy hiểm khi kết hợp wildcard sai. |
| `rm -r dir` | `-r` xoá directory recursively. | `rm -r old_backup` | Với dữ liệu quan trọng có thể đổi tên trước rồi xoá sau. |
| `rm -rf dir` | Recursive + force. Xoá rất mạnh, không hỏi. | `rm -rf /tmp/app-cache` | Trước khi chạy: `pwd; printf '%q\n' /tmp/app-cache; ls -la /tmp/app-cache`. Không dùng biến rỗng kiểu `rm -rf "$DIR"/*` nếu chưa validate. |
| `rmdir dir` | Chỉ xoá directory rỗng. | `rmdir empty_dir` | An toàn hơn `rm -r` nếu muốn chắc chắn folder không chứa data. |
| `ln -s target link` | Tạo symbolic link trỏ từ `link` tới `target`. | `ln -s /opt/app/releases/20260907 /opt/app/current` | Pattern deploy hay dùng: release folder + symlink `current` để rollback nhanh. |
| `ln -sfn target link` | `-s` symlink, `-f` force, `-n` xử lý symlink destination như file. | `ln -sfn /opt/app/releases/v2 /opt/app/current` | Cập nhật symlink deploy gần như atomic. |
| `stat file` | Hiển thị inode, size, permission, owner, access/modify/change time. | `stat app.log` | Dùng để phân biệt `mtime`, `ctime`, `atime` khi debug file thay đổi. |
| `file name` | Dò loại file dựa trên content/header, không chỉ extension. | `file app.jar` | Hữu ích khi file `.txt` thực ra là binary/gzip hoặc script sai line ending. |

> ⚠️ `rm -rf` không có undo mặc định. Trên production, hãy ưu tiên kiểm tra path/biến trước khi xoá.

---

# 3. Xem nội dung file

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `cat file` | In toàn bộ nội dung file ra stdout. Phù hợp file nhỏ. | `cat application.yml` | Tránh `cat` file log vài GB vì terminal sẽ bị flood. |
| `cat -n file` | `-n` đánh số tất cả dòng. | `cat -n nginx.conf` | Hữu ích khi trao đổi “lỗi ở dòng 72”. |
| `less file` | Pager để xem file lớn; không load toàn bộ vào màn hình, có search/navigation. | `less app.log` | Với log lớn, đây là lựa chọn tốt hơn `cat`. |
| `less -N file` | `-N` hiển thị line number. | `less -N app.log` | Kết hợp `/Exception`, `n`, `N`, `G`. |
| `less +F file` | Mở file và follow giống `tail -f`; `Ctrl+C` để dừng follow và search. | `less +F app.log` | Workflow log rất mạnh: follow → `Ctrl+C` → `/ERROR` → `F` để follow tiếp. |
| `head file` | Hiển thị mặc định 10 dòng đầu. | `head app.log` | Dùng check header/config/version nhanh. |
| `head -n 50 file` | `-n 50` chỉ định số dòng đầu. | `head -n 50 application.yml` | Có thể viết `head -50 file` trên GNU. |
| `tail file` | Hiển thị mặc định 10 dòng cuối. | `tail app.log` | Dùng kiểm tra log mới nhất rất nhanh. |
| `tail -n 100 file` | Hiển thị 100 dòng cuối. | `tail -n 100 app.log` | Thường dùng 200/500/1000 dòng khi debug. |
| `tail -f file` | `-f` theo dõi file realtime khi có dữ liệu append. | `tail -f app.log` | `Ctrl+C` để dừng. |
| `tail -F file` | `-F` tương đương follow theo **filename** và retry; tiếp tục tốt hơn khi logrotate rename/recreate file. | `tail -F /var/log/app/app.log` | Production log rotate: thường chọn `-F` thay vì `-f`. |
| `tac file` | In file theo thứ tự dòng từ cuối lên đầu. | `tac app.log | less` | Hữu ích khi muốn đọc newest-first mà file không quá lớn. |
| `nl file` | In nội dung có line number; hỗ trợ format numbering tốt hơn `cat -n`. | `nl -ba app.conf` | `-ba` đánh số cả blank lines. |

---

# 4. Edit file — vi / vim / nano

| Command / Key | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `vi file` | Mở file bằng `vi` hoặc implementation tương thích. | `vi /etc/nginx/nginx.conf` | Gần như server Linux nào cũng có `vi`; nên biết tối thiểu save/search/quit. |
| `vim file` | Mở Vim, thường có nhiều tính năng hơn vi. | `vim application.yml` | Có thể chưa được cài trên minimal server. |
| `nano file` | Editor đơn giản, command hiển thị dưới màn hình. | `nano app.conf` | Dễ dùng nhưng nhiều production server không cài. |
| `i` | Trong Vim: vào Insert mode trước cursor. | `i` | Nhấn `Esc` trước khi chạy command mode. |
| `a` | Insert sau cursor. | `a` | Nhanh khi append ký tự sau vị trí hiện tại. |
| `o` | Tạo dòng mới bên dưới và vào Insert mode. | `o` | Rất hay dùng khi thêm config line. |
| `Esc` | Trở về Normal mode. | `Esc` | Nếu “gõ gì cũng ra lệnh lạ”, nhấn `Esc` vài lần. |
| `:w` | Write/save file. | `:w` | Nếu permission denied, có thể thoát rồi mở bằng `sudoedit`. |
| `:q` | Quit nếu không có thay đổi chưa save. | `:q` | `:q!` để bỏ thay đổi. |
| `:wq` | Save rồi quit. | `:wq` | `ZZ` cũng save+quit trong normal mode. |
| `:q!` | Force quit không save. | `:q!` | Dùng khi sửa nhầm. |
| `dd` | Delete/cut dòng hiện tại vào Vim register. | `dd` | `5dd` xoá 5 dòng. |
| `yy` | Yank/copy dòng hiện tại. | `yy` | `5yy` copy 5 dòng. |
| `p` | Paste sau cursor/dòng. | `p` | `P` paste trước. |
| `u` | Undo thay đổi gần nhất. | `u` | Có thể nhấn nhiều lần. |
| `Ctrl+r` | Redo trong Vim. | `Ctrl+r` | Khác với shell `Ctrl+R`. |
| `/text` | Search forward. | `/server.port` | `n` tiếp theo, `N` quay lại. |
| `:%s/old/new/g` | Substitute toàn bộ file; `%` = toàn file, `g` = mọi occurrence trên mỗi dòng. | `:%s/http:/https:/g` | Thêm `c`: `:%s/old/new/gc` để confirm từng replace. |
| `:set number` | Hiển thị line number. | `:set number` | `:set relativenumber` hữu ích khi navigation. |
| `gg` | Đi đầu file. | `gg` | `G` xuống cuối file. |
| `10G` | Đi tới line 10. | `120G` | Hoặc `:120`. |
| `sudoedit file` | Mở file cần quyền root bằng editor user rồi ghi lại an toàn qua sudo. | `sudoedit /etc/nginx/nginx.conf` | Thường tốt hơn chạy cả editor dưới quyền root. |

---

# 5. Search file / folder — find

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `find . -name "name"` | Search từ current directory theo tên **case-sensitive**. | `find . -name "app.log"` | `.` nghĩa là bắt đầu từ current directory. |
| `find . -iname "*.log"` | `-iname` không phân biệt hoa thường. | `find . -iname "*.LOG"` | Hữu ích khi extension không đồng nhất. |
| `find /path -type f` | `-type f` chỉ trả regular file. | `find /var/log -type f` | Thường kết hợp `-name`, `-mtime`, `-size`. |
| `find /path -type d` | `-type d` chỉ directory. | `find /opt -type d -name "logs"` | Dùng tìm folder trong tree lớn. |
| `find . -name "*.log"` | Wildcard `*` match chuỗi bất kỳ; quote pattern để shell không expand trước. | `find . -name "*.log"` | Luôn quote `"*.log"` là thói quen tốt. |
| `find . -size +100M` | `+100M` = lớn hơn 100 MiB. `-100M` = nhỏ hơn. | `find /var/log -type f -size +100M` | Tìm log lớn trước khi disk full. |
| `find . -mtime -1` | Modified ít hơn 1×24h trước. | `find /opt/app -type f -mtime -1` | `-mmin -60` chính xác hơn cho “60 phút gần đây”. |
| `find . -mtime +30` | Modified hơn 30×24h trước. | `find /backup -type f -mtime +30` | Thường dùng cleanup backup/log cũ. |
| `find . -mmin -30` | Modified trong khoảng 30 phút gần đây. | `find /opt/app -type f -mmin -30` | Rất hữu ích khi muốn biết deploy vừa thay file nào. |
| `find . -empty` | Tìm file rỗng hoặc directory rỗng. | `find /tmp -empty` | Có thể kết hợp `-type f` để tránh directory. |
| `find ... -exec CMD {} \;` | Chạy command trên từng kết quả; `{}` là current result. | `find . -name "*.log" -exec ls -lh {} \;` | `{} +` hiệu quả hơn vì batch nhiều file vào một command. |
| `find ... -delete` | Xoá trực tiếp kết quả search. | `find /tmp -type f -name "*.tmp" -mtime +7 -delete` | Luôn chạy cùng lệnh **không có `-delete` trước** để review. |
| `which cmd` | Tìm executable sẽ được shell dùng theo `$PATH`. | `which java` | Tốt để check đang chạy Java nào. |
| `command -v cmd` | POSIX-friendly hơn `which`; trả path/alias/builtin. | `command -v java` | Senior shell script thường ưu tiên `command -v`. |
| `whereis cmd` | Tìm binary/source/man ở các location chuẩn. | `whereis java` | Không phải công cụ search filesystem tổng quát. |

### Ví dụ senior

```bash
find /var/log -type f -name "*.log" -size +500M -printf '%TY-%Tm-%Td %TH:%TM %10s %p\n'
```

Tìm file log >500MB và in timestamp, size, path.

---

# 6. Search text — grep

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `grep "text" file` | In các dòng chứa pattern. Mặc định pattern là basic regex. | `grep "ERROR" app.log` | Quote pattern nếu có space/ký tự đặc biệt. |
| `grep -i` | Ignore case. | `grep -i "error" app.log` | Dùng khi log không nhất quán hoa/thường. |
| `grep -n` | In line number trước kết quả. | `grep -n "ERROR" app.log` | Rất hữu ích để mở lại bằng `less +123 app.log`. |
| `grep -v` | In các dòng **không match** pattern. | `grep -v "DEBUG" app.log` | Dùng loại noise khỏi log. |
| `grep -c` | Đếm số dòng match, không in nội dung. | `grep -c "ERROR" app.log` | Đếm lỗi nhanh; không phải số occurrences nếu một dòng có nhiều match. |
| `grep -r` | Search recursive trong folder. | `grep -r "DB_URL" /opt/app` | Thường dùng với `-n`. |
| `grep -R` | Recursive và follow symbolic links. | `grep -R "server.port" /opt/app` | Cẩn thận symlink loop/project lớn. |
| `grep -w` | Match whole word. | `grep -w "ERROR" app.log` | Không match `ERROR_CODE`. |
| `grep -F` | Fixed string, không interpret regex. | `grep -F "a[b]" file.txt` | Nhanh/an toàn khi search literal có ký tự regex. |
| `grep -E` | Extended regex, hỗ trợ `|`, `+`, `?`, group thuận tiện. | `grep -E "ERROR|WARN|Exception" app.log` | Rất hay dùng cho nhiều keyword. |
| `grep -A 5` | In 5 dòng **After** match. | `grep -A 5 "Exception" app.log` | Đọc stack trace phía sau keyword. |
| `grep -B 5` | In 5 dòng **Before** match. | `grep -B 5 "ERROR" app.log` | Xem request/context trước lỗi. |
| `grep -C 5` | In 5 dòng trước + sau (**Context**). | `grep -C 5 "ERROR" app.log` | Một trong option debug log hữu ích nhất. |
| `grep -l` | Chỉ in tên file có match. | `grep -rl "password" ./config` | Tìm file nào chứa keyword mà không flood nội dung. |
| `grep -L` | Chỉ in tên file **không** có match. | `grep -L "health" *.conf` | Dùng audit config thiếu setting. |
| `grep -m 1` | Dừng sau N match trên mỗi file. | `grep -m 1 "Started" app.log` | Tìm first occurrence nhanh trên file lớn. |
| `grep --color=auto` | Highlight match nếu terminal hỗ trợ. | `grep --color=auto -n "ERROR" app.log` | Nhiều distro alias sẵn `grep --color=auto`. |

### Combo production

```bash
grep -Ein -C 10 "ERROR|WARN|Exception|Caused by" app.log
```

```bash
tail -F app.log | grep --line-buffered -E "ERROR|Exception|timeout"
```

`--line-buffered` giúp output pipeline realtime không bị buffer lâu.

---

# 7. Log — thao tác thường dùng

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `tail -n 500 -F file` | Đọc 500 dòng cuối rồi tiếp tục follow theo filename. | `tail -n 500 -F app.log` | Đây là default tốt khi test chức năng vừa bấm trên app. |
| `less +F file` | Follow trong `less`, có thể pause và search ngay trong cùng tool. | `less +F app.log` | `Ctrl+C` → `/keyword` → `n` → `F`. |
| `zgrep PATTERN file.gz` | Search trực tiếp trong gzip mà không cần extract. | `zgrep -in "ERROR" app.log.2.gz` | Cực hữu ích với rotated logs. |
| `zless file.gz` | Xem gzip bằng pager. | `zless access.log.3.gz` | Search `/text` như `less`. |
| `journalctl` | Xem log do systemd journal quản lý. | `journalctl` | Có thể cần sudo để xem đầy đủ. |
| `journalctl -u svc` | `-u` filter theo systemd unit. | `journalctl -u nginx.service` | Dùng đúng tên unit; có thể bỏ `.service`. |
| `journalctl -u svc -f` | Follow realtime journal của service. | `journalctl -u app -f` | Tương đương `tail -f` cho systemd. |
| `journalctl -u svc -n 200` | Chỉ 200 log entry gần nhất. | `journalctl -u app -n 200` | Nhanh hơn mở toàn journal. |
| `journalctl --since today` | Filter theo thời gian từ đầu ngày. | `journalctl -u app --since today` | Có thể dùng `"2026-09-07 09:00:00"`. |
| `journalctl --since "1 hour ago"` | Relative time filter. | `journalctl -u app --since "1 hour ago"` | Rất tiện sau incident mới xảy ra. |
| `journalctl --since ... --until ...` | Chọn khoảng thời gian cụ thể. | `journalctl -u app --since "18:00" --until "18:10"` | Senior debug incident thường khoanh đúng time window trước. |
| `journalctl -p err` | Filter theo priority error trở lên. | `journalctl -p err --since today` | Có thể dùng `warning`, `crit`. |
| `journalctl -xeu svc` | `-x` thêm giải thích, `-e` tới cuối, `-u` unit. | `journalctl -xeu nginx` | Rất hữu ích khi service start fail. |

---

# 8. Permission / Owner

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `ls -l` | Xem mode như `-rwxr-xr-x`, owner, group. | `ls -l deploy.sh` | Hãy đọc permission trước khi dùng `chmod 777`. |
| `chmod 755 file` | Owner `rwx`, group `r-x`, others `r-x`. | `chmod 755 deploy.sh` | Phù hợp executable/script phổ biến. |
| `chmod 644 file` | Owner `rw-`, group/others `r--`. | `chmod 644 application.yml` | Config không cần execute thường dùng 640/644 tuỳ security. |
| `chmod 600 file` | Chỉ owner đọc/ghi. | `chmod 600 ~/.ssh/id_rsa` | SSH private key thường bắt buộc permission chặt. |
| `chmod +x file` | Thêm execute bit theo rule umask/current class. | `chmod +x deploy.sh` | Kiểm tra shebang `#!/bin/bash` nếu script vẫn không chạy. |
| `chmod -x file` | Gỡ execute bit. | `chmod -x accidental.txt` | Dùng khi file không nên executable. |
| `chmod -R 755 dir` | Recursive mọi file/folder. | `chmod -R 755 /opt/app/bin` | Cẩn thận: ép file data thành executable. Senior thường dùng `find` để set dir/file riêng. |
| `find dir -type d -exec chmod 755 {} +` | Chỉ set permission directory. | `find /opt/app -type d -exec chmod 755 {} +` | Chuẩn hơn `chmod -R 755`. |
| `find dir -type f -exec chmod 644 {} +` | Chỉ set permission file. | `find /opt/app -type f -exec chmod 644 {} +` | Kết hợp với rule directory ở trên. |
| `chown user file` | Đổi owner user. | `sudo chown app app.log` | App permission lỗi rất thường do owner sai sau deploy bằng root. |
| `chown user:group file` | Đổi owner và group. | `sudo chown app:app application.yml` | Hay dùng cho app service account. |
| `chown -R user:group dir` | Recursive owner/group. | `sudo chown -R app:app /opt/app` | Review path kỹ trước khi recursive. |
| `umask` | Hiển thị mask ảnh hưởng permission mặc định khi tạo file/dir. | `umask` | `0022` thường tạo file 644, dir 755. |
| `namei -l /path/file` | Hiển thị permission của **mọi directory trên path**. | `namei -l /opt/app/config/app.yml` | Senior dùng khi file permission đúng nhưng app vẫn “Permission denied” do parent dir thiếu `x`. |

---

# 9. User / sudo

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `whoami` | In effective username. | `whoami` | Khi SSH qua account chung/sudo, luôn biết mình đang là ai. |
| `id` | In UID, primary GID và supplementary groups. | `id appuser` | Debug quyền group rất hữu ích. |
| `who` | Hiển thị session user đang login. | `who` | Có thể thấy terminal/remote session. |
| `w` | Giống `who` nhưng thêm uptime/load và command user đang chạy. | `w` | Hữu ích khi server nhiều admin cùng thao tác. |
| `sudo cmd` | Chạy một command với elevated privilege theo sudo policy. | `sudo systemctl restart nginx` | Ưu tiên sudo từng command hơn vào root shell lâu. |
| `sudo -i` | Mở login shell của root, load root environment. | `sudo -i` | Dùng cẩn thận; prompt root thường `#`. |
| `su - user` | Switch user và load login environment của user đó. | `sudo su - oracle` | `-` quan trọng vì load HOME/PATH/profile đúng user. |
| `sudo -u user cmd` | Chạy command dưới user khác mà không cần mở shell. | `sudo -u app java -version` | Rất hữu ích để tái hiện environment của service account. |
| `passwd` | Đổi password user hiện tại hoặc user khác nếu root. | `passwd` | Nhiều server enterprise disable password SSH và chỉ dùng key. |

---

# 10. Process

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `ps -ef` | `-e` tất cả process, `-f` full format gồm UID, PID, PPID, start time, command. | `ps -ef | grep java` | Classic trên Unix/Linux enterprise. |
| `ps aux` | BSD format: USER, PID, CPU, MEM, VSZ, RSS, STAT, command. | `ps aux --sort=-%mem | head` | Dễ sort CPU/RAM. |
| `pgrep name` | Tìm PID process theo tên/pattern. | `pgrep java` | Gọn hơn `ps | grep`. |
| `pgrep -af pattern` | `-a` full command line, `-f` match full command. | `pgrep -af 'java.*app.jar'` | Đây là cách sạch để tìm Java process cụ thể. |
| `pidof name` | Trả PID của program name. | `pidof nginx` | Hữu ích cho daemon đơn giản. |
| `top` | Monitor realtime CPU/RAM/process. | `top` | Trong top: `P` sort CPU, `M` sort memory, `1` per-CPU. |
| `top -p PID` | Chỉ monitor PID chỉ định. | `top -p 12345` | Tập trung vào app đang debug. |
| `kill PID` | Gửi SIGTERM (15) mặc định để process shutdown graceful. | `kill 12345` | Không cần viết `-15` nếu dùng mặc định. |
| `kill -15 PID` | Gửi SIGTERM explicit. | `kill -15 12345` | Cho app cơ hội flush data/close resources. |
| `kill -9 PID` | SIGKILL: kernel dừng ngay, process không cleanup được. | `kill -9 12345` | Chỉ dùng khi TERM không hiệu quả; không phải “cách chuẩn” để stop app. |
| `pkill pattern` | Gửi signal theo process name/pattern. | `pkill -15 java` | Nguy hiểm nếu có nhiều Java app; nên dùng pattern cụ thể. |
| `pkill -f pattern` | Match full command line. | `pkill -f 'app-name.jar'` | Kiểm tra `pgrep -af pattern` trước rồi mới `pkill`. |
| `pstree -p` | Hiển thị cây parent-child process kèm PID. | `pstree -p 1` | Debug process được sinh bởi service/script nào. |
| `ps -o ... -p PID` | Chọn các field cần xem. | `ps -p 1234 -o pid,ppid,user,%cpu,%mem,etime,lstart,cmd` | Senior thường dùng để lấy đúng metadata thay vì đọc `ps -ef` dài. |

---

# 11. Background jobs / nohup

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `cmd &` | Chạy process background của current shell. | `sleep 300 &` | Process vẫn có thể chịu SIGHUP khi SSH đóng tùy shell/config. |
| `nohup cmd &` | Ignore SIGHUP để process tiếp tục sau logout; mặc định output vào `nohup.out`. | `nohup java -jar app.jar > app.log 2>&1 &` | Trên app production hiện đại nên dùng systemd/container thay vì nohup nếu có thể. |
| `jobs` | Xem job của **current shell**, không phải toàn system. | `jobs -l` | `-l` thêm PID. |
| `fg %1` | Đưa job 1 về foreground. | `fg %1` | Job ID khác PID. |
| `bg %1` | Resume suspended job ở background. | `bg %1` | Thường dùng sau `Ctrl+Z`. |
| `Ctrl+Z` | Gửi SIGTSTP để suspend foreground job. | `Ctrl+Z` | Sau đó `bg` hoặc `fg`. |
| `disown %1` | Gỡ job khỏi shell job table, giúp tránh SIGHUP tùy shell. | `disown %1` | Không thay thế process supervisor thực thụ. |
| `echo $!` | PID của background command gần nhất. | `nohup ./run.sh & echo $!` | Hữu ích trong startup script đơn giản. |

---

# 12. systemd / service

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `systemctl status svc` | Xem active state, PID, recent log, exit code. | `systemctl status nginx` | Lệnh đầu tiên khi service có vấn đề. |
| `systemctl start svc` | Start service. | `sudo systemctl start nginx` | Sau đó verify bằng `status` + port + curl. |
| `systemctl stop svc` | Stop service. | `sudo systemctl stop nginx` | Xem `TimeoutStopSec` nếu service stop lâu. |
| `systemctl restart svc` | Stop rồi start lại. | `sudo systemctl restart app` | Restart gây downtime ngắn; config reload được thì ưu tiên reload. |
| `systemctl reload svc` | Yêu cầu service reload config mà không full restart, nếu service hỗ trợ. | `sudo systemctl reload nginx` | Nginx thường dùng reload sau `nginx -t`. |
| `systemctl enable svc` | Tạo enablement để service auto start theo target khi boot. | `sudo systemctl enable app` | `enable --now` vừa enable vừa start. |
| `systemctl disable svc` | Gỡ auto-start enablement. | `sudo systemctl disable app` | Không tự stop service đang chạy. |
| `systemctl is-active svc` | Trả `active`/`inactive` và exit code phù hợp script. | `systemctl is-active --quiet nginx && echo OK` | Tốt trong health/check script. |
| `systemctl is-enabled svc` | Kiểm tra auto-start state. | `systemctl is-enabled nginx` | Phân biệt “đang chạy” và “sẽ chạy sau reboot”. |
| `systemctl list-units --type=service` | List loaded service units. | `systemctl list-units --type=service --state=running` | Filter chỉ running service. |
| `systemctl daemon-reload` | Bắt systemd reload unit files sau khi sửa/tạo `.service`. | `sudo systemctl daemon-reload` | Không restart service tự động. |
| `systemctl cat svc` | Hiển thị unit file + drop-in config. | `systemctl cat app.service` | Senior dùng để biết config thực tế đang được systemd load. |
| `systemctl show svc` | In properties machine-readable-ish. | `systemctl show app -p MainPID -p ExecStart` | Hữu ích trong script/debug startup. |
| `systemctl reset-failed svc` | Reset failed state/counter. | `sudo systemctl reset-failed app` | Dùng sau khi xử lý lỗi `start-limit-hit`. |

---

# 13. Disk / Storage

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `df -h` | Filesystem usage; `-h` hiển thị size dễ đọc. | `df -h` | Check `%Use` của mount point, không chỉ tổng server. |
| `df -Th` | `-T` thêm filesystem type. | `df -Th /opt/app` | Hữu ích phân biệt ext4/xfs/nfs/tmpfs. |
| `du -sh dir` | `-s` summary, `-h` human-readable. | `du -sh /var/log` | Dùng để tìm folder gây đầy disk. |
| `du -sh *` | Size từng entry trong current folder. | `du -sh * | sort -h` | `sort -h` sort đúng KB/MB/GB. |
| `du -h --max-depth=1` | Hiện size theo level 1. | `du -h --max-depth=1 /var | sort -hr` | Rất hay dùng để drill-down disk usage. |
| `du -x` | Không đi sang filesystem/mount khác. | `du -xhd1 / | sort -hr` | Quan trọng khi `/` có mount NFS hoặc volume khác. |
| `lsblk` | Liệt kê block devices, partition, mountpoint. | `lsblk -f` | `-f` thêm filesystem/UUID. |
| `findmnt` | Hiển thị filesystem mount tree và source/target. | `findmnt /opt/app` | Dễ đọc hơn `mount`. |
| `mount` | Xem mount hoặc mount filesystem nếu có quyền. | `mount | grep '/data'` | Với production, thay đổi mount cần hiểu `/etc/fstab`. |
| `lsof +L1` | Tìm file đã bị delete nhưng process vẫn mở, nên disk chưa được giải phóng. | `sudo lsof +L1` | Đây là command “senior” cực hữu ích khi `df` đầy nhưng `du` không thấy. |
| `df -i` | Kiểm tra inode usage. | `df -i` | Disk có thể “full” vì hết inode dù còn GB trống. |

### Drill-down disk usage

```bash
sudo du -xhd1 / 2>/dev/null | sort -hr
```

Sau đó đi vào folder lớn và lặp lại.

---

# 14. Memory / CPU / System

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `free -h` | RAM total/used/free/shared/buff-cache/available. | `free -h` | Hãy nhìn `available`, không chỉ `free`; Linux dùng RAM làm cache. |
| `uptime` | Uptime, user count, load average 1/5/15 phút. | `uptime` | Load cao không đồng nghĩa CPU 100%; có thể do I/O wait. |
| `lscpu` | CPU architecture/topology/features. | `lscpu` | Check số socket/core/thread, virtualization. |
| `nproc` | Số processing units hiện available cho process. | `nproc` | So sánh load average với số CPU là một heuristic nhanh. |
| `uname -a` | Kernel name/release/architecture và host info. | `uname -a` | Dùng khi debug compatibility kernel/module. |
| `hostname` | Hostname hiện tại. | `hostname` | Rất quan trọng khi SSH nhiều server giống nhau. |
| `hostnamectl` | Hostname + OS/kernel/architecture. | `hostnamectl` | Một lệnh tóm tắt system khá tốt. |
| `cat /etc/os-release` | Distro và version. | `cat /etc/os-release` | Giúp chọn đúng apt/yum/dnf và docs. |
| `date` | Local server date/time. | `date '+%F %T %Z'` | Incident debugging phải check timezone server. |
| `timedatectl` | Timezone, NTP sync, RTC. | `timedatectl` | Clock lệch có thể gây JWT/TLS/log correlation lỗi. |
| `vmstat 1` | Snapshot CPU, runnable tasks, memory, paging, I/O mỗi 1 giây. | `vmstat 1 10` | Quan sát `r`, `si/so`, `wa` để phân biệt CPU/memory/I/O bottleneck. |
| `iostat -xz 1` | Extended disk I/O stats theo interval. | `iostat -xz 1 10` | Nhìn `%util`, `await`; cần package sysstat. |

---

# 15. Network

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `ip a` | Hiển thị interface, IP, state. | `ip a` | `ip` thay thế `ifconfig` trên Linux hiện đại. |
| `ip route` | Hiển thị routing table. | `ip route` | Check default gateway khi server ra ngoài không được. |
| `hostname -I` | In các IP của host. | `hostname -I` | Nhanh nhưng có thể trả nhiều IP/container interface. |
| `ping host` | Gửi ICMP echo request để test reachability/latency. | `ping -c 4 8.8.8.8` | Ping fail không chắc host chết vì firewall có thể block ICMP. |
| `ping -c 4 host` | `-c` giới hạn packet count rồi tự dừng. | `ping -c 4 google.com` | Phù hợp script/diagnostic ngắn. |
| `curl URL` | HTTP(S) client; mặc định in response body. | `curl http://localhost:8080/health` | Một trong lệnh quan trọng nhất để test app/backend. |
| `curl -I URL` | `-I` gửi HEAD và chỉ hiển thị response headers. | `curl -I https://example.com` | Không phải server nào cũng xử lý HEAD giống GET. |
| `curl -v URL` | Verbose: DNS/connect/TLS/request/response headers. | `curl -v https://api.example.com` | Debug proxy/TLS/header cực hữu ích. |
| `curl -sS URL` | `-s` silent progress, `-S` vẫn show error. | `curl -sS http://localhost:8080/health` | Tốt trong script. |
| `curl -f URL` | Fail với HTTP 4xx/5xx bằng non-zero exit code. | `curl -fsS http://localhost:8080/health` | Chuẩn health-check script: `curl -fsS`. |
| `curl -L URL` | Follow redirect 3xx. | `curl -L https://example.com/login` | Nếu chỉ `curl` thấy 301/302 mà browser chạy được, thử `-L`. |
| `curl -k URL` | Bỏ verify TLS certificate. | `curl -k https://localhost:8443` | Chỉ dùng debug; không phải fix cho cert lỗi. |
| `curl --connect-timeout 5` | Giới hạn thời gian connect. | `curl --connect-timeout 5 -fsS http://10.0.0.10:8080` | Tránh script treo lâu khi endpoint unreachable. |
| `wget URL` | Download file qua HTTP/HTTPS. | `wget https://example.com/app.tar.gz` | `wget -c` resume download. |
| `ss -lntp` | `-l` listening, `-n` numeric, `-t` TCP, `-p` process. | `sudo ss -lntp` | Thay thế `netstat`; command chuẩn để check listening port. |
| `ss -lunp` | Listening UDP + process. | `sudo ss -lunp` | DNS thường UDP/53. |
| `ss -antp` | Tất cả TCP socket, numeric, process. | `sudo ss -antp | grep ':8080'` | Có thể xem ESTAB/TIME-WAIT/CLOSE-WAIT. |
| `lsof -i :8080` | Liệt kê process/file descriptor liên quan port 8080. | `sudo lsof -nP -iTCP:8080 -sTCP:LISTEN` | `-nP` tránh DNS/service-name lookup, output nhanh và rõ port số. |
| `nc -vz host port` | Netcat: `-v` verbose, `-z` chỉ scan/connect không gửi data. | `nc -vz 10.0.0.10 8080` | Check TCP reachability nhanh hơn HTTP nếu app protocol khác. |
| `traceroute host` | Hiển thị hops trên đường route. | `traceroute 8.8.8.8` | Có thể bị firewall/filter nên không phải hop nào cũng trả lời. |
| `dig domain` | DNS query chi tiết. | `dig example.com A` | `dig +short example.com` cho output gọn. |
| `nslookup domain` | DNS lookup interactive/simple. | `nslookup example.com` | `dig` thường mạnh hơn nhưng `nslookup` phổ biến. |

---

# 16. Archive / Compress

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `tar -cvf x.tar dir/` | `c` create, `v` verbose, `f` archive filename. Không compress. | `tar -cvf backup.tar config/` | `v` có thể quá nhiều output với archive lớn. |
| `tar -xvf x.tar` | `x` extract, `v` verbose, `f` file. | `tar -xvf backup.tar` | Dùng `-C /dest` để extract vào destination cụ thể. |
| `tar -czvf x.tar.gz dir/` | `z` dùng gzip compression. | `tar -czvf app-backup.tar.gz /opt/app/config` | Backup config/log nhỏ rất phổ biến. |
| `tar -xzvf x.tar.gz` | Extract gzip-compressed tar. | `tar -xzvf app.tar.gz -C /opt/app` | Nên `tar -tzf` xem content trước nếu nguồn không quen. |
| `tar -tzf x.tar.gz` | `t` list content, không extract. | `tar -tzf app.tar.gz | less` | Review path để tránh extract ghi đè bất ngờ. |
| `gzip file` | Compress thành `file.gz` và mặc định xoá file gốc. | `gzip old.log` | `gzip -k` giữ file gốc nếu implementation hỗ trợ. |
| `gunzip file.gz` | Decompress gzip. | `gunzip app.log.gz` | Với log chỉ cần đọc, dùng `zless/zgrep` để khỏi extract. |
| `zip -r x.zip dir/` | `-r` recursive zip directory. | `zip -r config.zip config/` | Zip tiện cross-platform nhưng tar.gz phổ biến hơn trên Linux. |
| `unzip x.zip` | Extract zip. | `unzip app.zip -d /tmp/app` | `-l` để list trước. |

---

# 17. SSH

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `ssh user@host` | Mở encrypted remote shell qua SSH port mặc định 22. | `ssh app@10.0.0.10` | Verify host key fingerprint khi connect lần đầu. |
| `ssh -p PORT` | `-p` chỉ custom SSH port. | `ssh -p 2222 app@10.0.0.10` | SSH dùng lowercase `-p`; SCP dùng uppercase `-P`. |
| `ssh -i KEY` | Chỉ private key identity file. | `ssh -i ~/.ssh/prod.pem ubuntu@server` | Private key nên `chmod 600`. |
| `ssh -v` | Verbose connection/auth debugging. | `ssh -v user@host` | Thấy key nào được thử, auth method, config áp dụng. |
| `ssh -vvv` | Debug tối đa hơn. | `ssh -vvv user@host` | Dùng khi auth/proxy/jump host lỗi khó hiểu. |
| `ssh -J jump target` | ProxyJump qua bastion/jump host. | `ssh -J user@bastion app@10.0.1.20` | Senior thường cấu hình trong `~/.ssh/config` để gõ ngắn. |
| `ssh -L local:host:port` | Local port forwarding. | `ssh -L 15432:db.internal:5432 user@bastion` | Sau đó local app connect `localhost:15432` tới DB nội bộ. |
| `ssh -N` | Không chạy remote command, chỉ giữ connection/forward. | `ssh -N -L 8081:localhost:8080 user@server` | Chuẩn khi chỉ tạo tunnel. |
| `ssh -o ServerAliveInterval=60` | Gửi keepalive mỗi 60s. | `ssh -o ServerAliveInterval=60 user@host` | Giảm session chết do NAT/firewall idle timeout. |
| `exit` | Thoát remote shell/session. | `exit` | `Ctrl+D` gửi EOF và thường cũng logout. |

---

# 18. SCP / rsync

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `scp file user@host:/path/` | Copy local file lên remote qua SSH. | `scp app.jar app@server:/tmp/` | Với file lớn/đồng bộ lặp lại, `rsync` thường tốt hơn. |
| `scp user@host:/path/file .` | Copy remote file về current local dir. | `scp app@server:/var/log/app.log .` | Có thể dùng wildcard nhưng nhớ shell expansion/quote. |
| `scp -r dir user@host:/path/` | Recursive directory copy. | `scp -r config app@server:/tmp/` | Không tối ưu incremental như rsync. |
| `scp -P 2222` | Uppercase `-P` đặt SSH port. | `scp -P 2222 app.jar user@host:/tmp/` | Khác `ssh -p`. |
| `rsync -av src/ dst/` | `-a` archive preserve metadata; `-v` verbose. | `rsync -av ./config/ app@server:/opt/app/config/` | Dấu `/` cuối source rất quan trọng: `src/` = content, `src` = cả folder. |
| `rsync -z` | Compress data qua network. | `rsync -avz ./build/ app@server:/tmp/build/` | Trên LAN/file đã compressed có thể không lợi nhiều. |
| `rsync --progress` | Hiển thị tiến trình từng file. | `rsync -av --progress big.tar app@server:/tmp/` | `--info=progress2` cho tổng progress trên rsync mới. |
| `rsync --delete` | Xoá destination file không còn ở source để mirror. | `rsync -av --delete ./site/ server:/var/www/site/` | Rất nguy hiểm; luôn dry-run trước. |
| `rsync -n` / `--dry-run` | Chỉ mô phỏng thay đổi, không thực hiện. | `rsync -avhn --delete ./site/ server:/var/www/site/` | Senior gần như luôn dry-run trước `--delete`. |
| `rsync -e "ssh -p 2222"` | Chỉ custom SSH transport/options. | `rsync -av -e "ssh -p 2222" ./app/ user@host:/opt/app/` | Có thể thêm identity key trong chuỗi ssh. |

---

# 19. Text processing — wc / sort / cut / awk / sed

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `wc -l file` | Đếm số line. | `wc -l app.log` | Pipeline: `grep ERROR app.log | wc -l`. |
| `wc -w file` | Đếm word. | `wc -w notes.txt` | Ít dùng hơn trên server ops. |
| `sort file` | Sort lexical ascending. | `sort users.txt` | Thường pipe với `uniq`. |
| `sort -n` | Numeric sort. | `sort -n numbers.txt` | Không bị `"100"` đứng trước `"20"` như lexical. |
| `sort -r` | Reverse descending. | `sort -r names.txt` | Kết hợp `-n`/`-h`. |
| `sort -h` | Human numeric sort, hiểu K/M/G. | `du -sh * | sort -h` | Rất hữu ích cho disk usage. |
| `sort -u` | Sort và unique. | `sort -u ips.txt` | Tương tự `sort | uniq`. |
| `uniq -c` | Count số dòng trùng liên tiếp; thường phải sort trước. | `sort ips.txt | uniq -c | sort -nr` | Classic để tìm IP/request xuất hiện nhiều nhất. |
| `cut -d',' -f1` | `-d` delimiter, `-f` field index. | `cut -d',' -f1 users.csv` | Với CSV có quoted comma phức tạp, `cut` không phải parser đúng. |
| `awk '{print $1}'` | In field 1; awk mặc định split whitespace. | `ps -ef | awk '{print $2}'` | awk mạnh cho filter/aggregate column. |
| `awk -F,` | Chỉ field separator. | `awk -F, '{print $1,$3}' file.csv` | `BEGIN{FS=","}` tương đương kiểu script. |
| `sed 's/old/new/'` | Replace occurrence đầu tiên mỗi dòng trên stdout. | `sed 's/http:/https:/' app.conf` | Mặc định không sửa file gốc. |
| `sed 's/old/new/g'` | `g` replace mọi occurrence trên mỗi dòng. | `sed 's/foo/bar/g' file.txt` | Review output trước khi dùng `-i`. |
| `sed -i` | Edit file in-place. | `sed -i 's/foo/bar/g' app.conf` | Trên production nên backup: `sed -i.bak ...` nếu implementation hỗ trợ. |

### Senior log analytics bằng awk

Top status code:

```bash
awk '{print $9}' access.log | sort | uniq -c | sort -nr | head
```

Top client IP:

```bash
awk '{print $1}' access.log | sort | uniq -c | sort -nr | head -20
```

---

# 20. Pipe / Redirect

| Syntax | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `cmd1 \| cmd2` | Pipe stdout của cmd1 thành stdin của cmd2. | `ps -ef | grep java` | Đây là nền tảng để ghép Linux commands nhỏ thành workflow mạnh. |
| `>` | Redirect stdout và **ghi đè** file. | `echo "hello" > test.txt` | Cẩn thận với config/log quan trọng. |
| `>>` | Append stdout vào cuối file. | `echo "hello" >> test.txt` | Rất hay dùng ghi log thủ công/script. |
| `< file` | Lấy stdin từ file. | `wc -l < app.log` | Output chỉ là số, không kèm filename. |
| `2>` | Redirect stderr. File descriptor 2 = stderr. | `find / -name app.log 2>errors.txt` | Hữu ích tách lỗi permission. |
| `2>/dev/null` | Bỏ stderr. | `find / -name app.log 2>/dev/null` | Đừng lạm dụng khi đang debug vì sẽ che lỗi quan trọng. |
| `2>&1` | Redirect stderr tới cùng destination hiện tại của stdout. | `java -jar app.jar > app.log 2>&1` | Thứ tự redirect quan trọng. |
| `&>` | Bash shorthand redirect stdout+stderr. | `command &> output.log` | `>file 2>&1` portable hơn. |
| `tee file` | Copy stdin vừa ra terminal vừa ghi file. | `curl -v URL 2>&1 | tee curl-debug.log` | Rất hữu ích khi vừa muốn xem vừa lưu bằng chứng incident. |
| `tee -a file` | Append thay vì overwrite. | `echo test | tee -a run.log` | Với root file: `echo x | sudo tee /etc/file`. |

---

# 21. History / Shell shortcuts

| Command / Key | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `history` | Hiển thị command history của shell. | `history | tail -50` | Có thể chứa sensitive command; tránh gõ password/token trực tiếp vào command line. |
| `history | grep text` | Search command đã dùng. | `history | grep ssh` | Nhanh để lấy lại command dài. |
| `!!` | Chạy lại command ngay trước đó. | `sudo !!` | Classic: quên sudo → `sudo !!`. |
| `!123` | Chạy lại history entry 123. | `!123` | Review `history` trước tránh chạy nhầm destructive command. |
| `Ctrl+R` | Reverse incremental search history. | `Ctrl+R`, gõ `journalctl` | Một trong keyboard shortcut tăng tốc nhất. |
| `Ctrl+A` | Đưa cursor về đầu command line. | `Ctrl+A` | Giống Home trong readline. |
| `Ctrl+E` | Đưa cursor về cuối line. | `Ctrl+E` | Giống End. |
| `Ctrl+U` | Xoá từ cursor về đầu line. | `Ctrl+U` | Nhanh hơn giữ Backspace. |
| `Ctrl+K` | Xoá từ cursor đến cuối line. | `Ctrl+K` | Dùng sửa suffix command dài. |
| `Ctrl+W` | Xoá word phía trước. | `Ctrl+W` | Command-line editing quan trọng. |
| `Ctrl+L` | Clear terminal screen. | `Ctrl+L` | Không xoá history. |
| `Tab` | Auto-complete path/command nếu shell hỗ trợ. | `cd /var/lo<Tab>` | Nhấn Tab 2 lần để xem candidates. |

---

# 22. Environment variables

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `env` | In environment của process shell hiện tại. | `env | sort` | Có thể chứa secret/token; cẩn thận khi paste log. |
| `printenv VAR` | In environment variable cụ thể. | `printenv JAVA_HOME` | Gọn hơn `env | grep`. |
| `echo "$PATH"` | Expand và in shell variable PATH. | `echo "$PATH" | tr ':' '\n'` | Tách PATH từng dòng để debug executable priority. |
| `export KEY=value` | Set và export biến cho child processes của current shell. | `export JAVA_HOME=/usr/lib/jvm/java-17` | Chỉ tồn tại trong session nếu không ghi vào profile/service config. |
| `unset KEY` | Xoá shell variable/environment variable. | `unset HTTP_PROXY` | Hữu ích khi proxy làm curl/app đi sai đường. |
| `source file` | Chạy file trong **current shell** để thay đổi environment hiện tại. | `source ~/.bashrc` | Khác `bash file` vì child shell không cập nhật parent shell. |
| `env KEY=value cmd` | Set variable chỉ cho một command. | `env JAVA_HOME=/opt/jdk21 ./run.sh` | Senior dùng để test không làm bẩn session environment. |

---

# 23. Java / JVM server

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `java -version` | Hiển thị runtime Java đang được gọi qua PATH. | `java -version` | Check cả `which java` và `readlink -f $(which java)` nếu version bất ngờ. |
| `which java` | Path executable được shell resolve. | `which java` | Có thể là symlink. |
| `readlink -f $(which java)` | Resolve symlink tới binary thật. | `readlink -f "$(command -v java)"` | Tìm chính xác JDK installation đang chạy. |
| `jar tf app.jar` | `t` list archive table, `f` jar file. | `jar tf app.jar | less` | Kiểm tra class/resource có nằm trong artifact hay không. |
| `java -jar app.jar` | Chạy executable JAR có Main-Class/launcher phù hợp. | `java -jar app.jar` | Production nên cấu hình heap/GC/logging rõ ràng. |
| `jps -lv` | Liệt kê JVM process có attach mechanism, kèm args. | `jps -lv` | Không phải JVM nào cũng hiện nếu user/permission khác. |
| `jstack PID` | Thread dump JVM. | `jstack 12345 > /tmp/jstack.$(date +%s).txt` | Khi app treo/high CPU, lấy 2-3 dump cách nhau vài giây để so thread. |
| `jcmd PID VM.command_line` | In JVM command line. | `jcmd 12345 VM.command_line` | `jcmd` hiện đại và đa năng hơn nhiều tool JDK cũ. |
| `jcmd PID VM.flags` | JVM flags thực tế. | `jcmd 12345 VM.flags` | Check heap/GC options thực sự đang áp dụng. |
| `jcmd PID GC.heap_info` | Heap summary. | `jcmd 12345 GC.heap_info` | Nhẹ hơn heap dump; phù hợp kiểm tra nhanh. |
| `jcmd PID Thread.print` | Thread dump qua jcmd. | `jcmd 12345 Thread.print > /tmp/thread.txt` | Có thể dùng thay `jstack`. |
| `jcmd PID GC.class_histogram` | Histogram class/object count. | `jcmd 12345 GC.class_histogram | head -50` | Có overhead; dùng thận trọng production tải cao. |

---

# 24. Package manager

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `apt update` | Refresh package index, không upgrade package. | `sudo apt update` | Nên chạy trước `apt install` trên Ubuntu/Debian nếu metadata cũ. |
| `apt upgrade` | Upgrade package có thể upgrade mà không remove package cần thiết theo apt rules. | `sudo apt upgrade` | Production cần change window; không upgrade bừa. |
| `apt install pkg` | Install package. | `sudo apt install tree` | Có thể `apt-cache policy pkg` xem candidate/source trước. |
| `apt remove pkg` | Remove package nhưng thường giữ config. | `sudo apt remove nginx` | `purge` mới xoá package config managed. |
| `apt purge pkg` | Remove package + config files do package manager quản lý. | `sudo apt purge nginx` | Không có nghĩa xoá toàn data app. |
| `dnf install pkg` | Install trên RHEL/Fedora/newer enterprise distros. | `sudo dnf install lsof` | RHEL 8/9 thường dùng dnf; `yum` có thể là compatibility wrapper. |
| `dnf history` | Xem transaction history. | `sudo dnf history` | Rất hữu ích biết package nào vừa được đổi. |
| `rpm -qa` | List RPM packages. | `rpm -qa | grep java` | Dùng audit installed package trên RHEL family. |

---

# 25. Date / Time

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `date` | In server local date/time. | `date` | Luôn check timezone khi đối chiếu log giữa nhiều system. |
| `date "+%Y-%m-%d %H:%M:%S"` | Custom output format. | `date "+%Y-%m-%d %H:%M:%S %Z"` | Hay dùng tạo timestamp backup filename. |
| `date -u` | In UTC. | `date -u` | API/cloud logs thường dùng UTC. |
| `timedatectl` | Timezone/NTP/system clock state. | `timedatectl status` | Nếu `System clock synchronized: no`, auth/token có thể lỗi theo time. |
| `find . -newermt` | Tìm file modified sau mốc thời gian. | `find . -type f -newermt "2026-09-07 18:00"` | Dễ hiểu hơn `mtime` khi incident có timestamp cụ thể. |

---

# 26. Cron

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `crontab -l` | List cron entries của user hiện tại. | `crontab -l` | Root/user khác có crontab khác nhau. |
| `crontab -e` | Edit user crontab bằng editor mặc định. | `crontab -e` | Cron environment PATH rất tối giản; dùng absolute path trong command. |
| `sudo crontab -l -u user` | Xem crontab user khác. | `sudo crontab -l -u app` | Khi job “không chạy”, check đúng user trước. |
| `0 2 * * * cmd` | Chạy mỗi ngày 02:00. | `0 2 * * * /opt/scripts/backup.sh >> /var/log/backup.log 2>&1` | Luôn redirect output và dùng path tuyệt đối để debug cron. |
| `*/5 * * * * cmd` | Chạy mỗi 5 phút. | `*/5 * * * * /opt/check.sh` | Tránh job nặng chạy chồng; cân nhắc lock/flock. |
| `flock` | Prevent concurrent cron run bằng file lock. | `*/5 * * * * flock -n /tmp/job.lock /opt/job.sh` | Senior tip quan trọng cho cron task có thể chạy lâu. |

---

# 27. Open files / file descriptors

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `lsof` | List open files; Linux coi socket/device cũng là file-like object. | `sudo lsof | head` | Output rất lớn; nên filter. |
| `lsof /path/file` | Process nào đang mở file. | `sudo lsof /var/log/app.log` | Biết process giữ file khi không delete/move được như mong đợi. |
| `lsof -i :PORT` | Process có socket trên port. | `sudo lsof -nP -i :8080` | `-nP` tránh name resolution làm chậm. |
| `lsof +L1` | File link count <1, thường là deleted nhưng vẫn open. | `sudo lsof +L1` | Giải thích trường hợp `df` đầy nhưng file đã “xoá”. |
| `ls /proc/PID/fd` | Liệt kê file descriptors của process. | `ls -l /proc/12345/fd | head` | Senior Linux debugging: `/proc` cung cấp rất nhiều runtime info. |
| `cat /proc/PID/limits` | Resource limits của process. | `cat /proc/12345/limits` | Check `Max open files` khi gặp “Too many open files”. |

---

# 28. xargs

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `xargs cmd` | Chuyển stdin thành arguments cho command. | `printf '%s\n' a b | xargs echo` | Hữu ích khi command không đọc stdin trực tiếp. |
| `xargs -0` | Input được phân cách bằng NUL, an toàn với space/newline trong filename. | `find . -type f -print0 | xargs -0 grep -n "ERROR"` | Pair chuẩn với `find -print0`. |
| `xargs -n N` | Giới hạn N arguments mỗi invocation. | `seq 1 10 | xargs -n 2 echo` | Hữu ích batch process. |
| `xargs -P N` | Chạy tối đa N process song song. | `cat hosts.txt | xargs -n1 -P4 ping -c1` | Có thể tăng tải mạnh; dùng cẩn thận production. |

---

# 29. Compare / checksum

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `diff file1 file2` | So sánh text line-by-line. | `diff old.conf new.conf` | Exit code 0=same, 1=different, >1=error. |
| `diff -u` | Unified diff có context, dễ đọc và dùng trong patch/review. | `diff -u app.conf.bak app.conf` | Đây là format quen thuộc của Git diff. |
| `cmp file1 file2` | So sánh byte-level, dừng tại khác biệt đầu. | `cmp app.jar app2.jar` | Nhanh check binary identical hay không. |
| `md5sum file` | Tính MD5 checksum. | `md5sum app.jar` | Không dùng MD5 cho security; dùng để compare integrity cơ bản. |
| `sha256sum file` | Tính SHA-256. | `sha256sum app.jar` | Phù hợp verify artifact checksum. |

---

# 30. Encoding / binary inspection

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `file file` | Guess file type. | `file script.sh` | Có thể báo “with CRLF line terminators” khi script Windows lỗi trên Linux. |
| `file -i file` | In MIME type và charset estimate. | `file -i data.csv` | Giúp debug UTF-8/EUC-KR/other encoding. |
| `xxd file` | Hex dump. | `xxd app.dat | head` | Nhìn BOM/header/magic bytes. |
| `hexdump -C file` | Canonical hex + ASCII. | `hexdump -C file.bin | head` | Tốt để tìm hidden CRLF/control chars. |
| `od -c file` | Character dump, escape non-printing chars. | `od -c script.sh | head` | Debug `\r` trong shell script. |

---

# 31. Advanced process / performance

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `ps -p PID -o ...` | Custom process columns. | `ps -p 12345 -o pid,ppid,nlwp,%cpu,%mem,rss,vsz,etime,cmd` | `nlwp` = thread count. |
| `pidstat -p PID 1` | CPU stats process theo interval 1s. | `pidstat -p 12345 1 10` | Cần sysstat; tốt hơn nhìn snapshot đơn lẻ. |
| `pidstat -t -p PID 1` | CPU per-thread. | `pidstat -t -p 12345 1` | Kết hợp Java thread dump để map high CPU thread. |
| `vmstat 1` | System-level CPU/memory/io quick sampling. | `vmstat 1 10` | `wa` cao → nghi I/O wait; `si/so` → swap activity. |
| `iostat -xz 1` | Extended storage device stats. | `iostat -xz 1 10` | `await` cao có thể chỉ ra storage latency. |
| `sar -u 1 10` | CPU statistics bằng sysstat. | `sar -u 1 10` | `sar` có thể xem historical metrics nếu sysstat collection bật. |
| `dmesg -T` | Kernel ring buffer với human-readable timestamp. | `sudo dmesg -T | tail -100` | Check OOM killer, disk errors, NIC/kernel events. |
| `journalctl -k` | Kernel logs qua journal. | `journalctl -k --since today` | Thường dễ filter time hơn dmesg. |

---

# 32. Network troubleshooting flow

| Step | Command | Ví dụ | Senior note |
|---|---|---|---|
| DNS | `dig` | `dig +short api.example.com` | Nếu IP sai, chưa cần debug app. |
| Route | `ip route get IP` | `ip route get 10.0.0.10` | Cho biết interface/gateway/source IP Linux sẽ dùng. |
| Reachability | `ping` | `ping -c 4 10.0.0.10` | Ping fail không kết luận TCP fail. |
| TCP | `nc -vz` | `nc -vz 10.0.0.10 443` | Phân biệt network/port với HTTP logic. |
| TLS/HTTP | `curl -v` | `curl -vk https://host:443/health` | `-k` chỉ debug cert; sau đó phải fix verify. |
| Listening local | `ss -lntp` | `sudo ss -lntp | grep ':8080'` | Nếu không listen local thì network ngoài không phải nguyên nhân chính. |
| DNS detail | `dig` | `dig api.example.com` | Check TTL/CNAME/A/AAAA. |
| Path | `traceroute` | `traceroute 10.0.0.10` | Có giới hạn vì firewall có thể drop probes. |

---

# 33. Server troubleshooting flow

| Step | Command | Ví dụ | Senior note |
|---|---|---|---|
| 1. Service state | `systemctl status` | `systemctl status app` | Xem exit code/MainPID/recent logs. |
| 2. Recent logs | `journalctl -u` | `journalctl -u app -n 300 --no-pager` | Khoanh lỗi trước restart. |
| 3. Process | `pgrep -af` | `pgrep -af 'java.*app'` | Xác nhận process thật sự tồn tại. |
| 4. Port | `ss` | `sudo ss -lntp | grep ':8080'` | Process sống chưa chắc app đã bind port. |
| 5. Local health | `curl -fsS` | `curl -fsS -v http://127.0.0.1:8080/health` | Tách vấn đề app khỏi LB/firewall/DNS. |
| 6. Resource | `free/df/top` | `free -h; df -h; top` | Check RAM/disk/CPU pressure. |
| 7. Kernel | `dmesg` | `dmesg -T | grep -i -E 'oom|killed|error'` | OOM killer có thể giết Java mà app log không kịp ghi. |
| 8. Config diff | `diff -u` | `diff -u app.conf.bak app.conf` | Incident sau deploy thường do config/artifact khác. |

---

# 34. Commands nên thuộc lòng

| Nhóm | Command | Ví dụ | Senior note |
|---|---|---|---|
| Navigation | `pwd`, `ls -lah`, `cd`, `cd -` | `pwd && ls -lah` | Luôn biết context trước khi thao tác. |
| File | `cp -a`, `mv`, `rm`, `mkdir -p` | `cp -a app.conf app.conf.bak` | Backup trước edit. |
| View | `less`, `tail -n 500 -F` | `less +F app.log` | Dùng less cho file lớn. |
| Search | `grep -Ein`, `find` | `grep -Ein -C5 "ERROR|Exception" app.log` | Context quanh lỗi quan trọng hơn keyword đơn. |
| Process | `pgrep -af`, `ps`, `top`, `kill` | `pgrep -af java` | Tránh `kill -9` như default. |
| Port | `ss`, `lsof` | `sudo ss -lntp | grep 8080` | `ss` là tool hiện đại. |
| HTTP | `curl -fsS -v` | `curl -fsS -v http://localhost:8080/health` | `-f` giúp script detect 4xx/5xx. |
| Disk | `df -h`, `du -xhd1`, `lsof +L1` | `du -xhd1 /var | sort -hr` | `lsof +L1` là kiến thức rất đáng nhớ. |
| Service | `systemctl`, `journalctl` | `journalctl -xeu app` | Pair chuẩn systemd debug. |
| SSH | `ssh`, `scp`, `rsync` | `ssh -J bastion app@private-host` | Jump host/tunnel là kỹ năng server thực tế. |

---

# 35. Combo thực tế / senior thường dùng

### 35.1 Tìm đúng Java process, tránh grep tự match

```bash
pgrep -af 'java.*app-name'
```

Hoặc:

```bash
ps -ef | grep '[j]ava'
```

### 35.2 Xem process nào listen port 8080

```bash
sudo ss -lntp | grep ':8080'
```

Chi tiết hơn:

```bash
sudo lsof -nP -iTCP:8080 -sTCP:LISTEN
```

### 35.3 Xem 500 dòng gần nhất rồi realtime

```bash
tail -n 500 -F app.log
```

### 35.4 Follow log nhưng chỉ giữ lỗi

```bash
tail -F app.log | grep --line-buffered -E 'ERROR|Exception|Caused by|timeout'
```

### 35.5 Search error kèm 10 dòng context

```bash
grep -Ein -C 10 'ERROR|WARN|Exception|Caused by' app.log
```

### 35.6 Tìm file vừa bị thay đổi trong 30 phút

```bash
find /opt/app -type f -mmin -30 -ls
```

### 35.7 Tìm folder chiếm disk lớn nhất

```bash
sudo du -xhd1 /var 2>/dev/null | sort -hr
```

### 35.8 Khi `df -h` đầy nhưng `du` không thấy

```bash
sudo lsof +L1
```

### 35.9 Test app local trước khi đổ lỗi network/LB

```bash
curl -fsS -v http://127.0.0.1:8080/health
```

### 35.10 Xem connection state của port

```bash
sudo ss -antp | grep ':8080'
```

Các state quan trọng:

- `LISTEN`: server đang listen.
- `ESTAB`: connection active.
- `TIME-WAIT`: connection đã close, kernel giữ tạm state.
- `CLOSE-WAIT`: peer đã đóng nhưng local process chưa close socket; quá nhiều có thể liên quan code/resource leak.
- `SYN-SENT`: client đã gửi SYN nhưng chưa nhận SYN-ACK.
- `SYN-RECV`: server nhận SYN và đang chờ handshake hoàn tất.

### 35.11 Backup config có timestamp trước sửa

```bash
cp -a application.yml "application.yml.$(date +%F_%H%M%S).bak"
```

### 35.12 Compare config trước/sau

```bash
diff -u application.yml.bak application.yml
```

### 35.13 Validate nginx trước reload

```bash
sudo nginx -t && sudo systemctl reload nginx
```

### 35.14 Restart và xem log ngay

```bash
sudo systemctl restart app && sudo journalctl -u app -n 100 -f
```

### 35.15 Dry-run rsync trước khi mirror/delete

```bash
rsync -avhn --delete ./build/ app@server:/opt/app/
```

Nếu output đúng mới chạy thật:

```bash
rsync -avh --delete ./build/ app@server:/opt/app/
```

### 35.16 Tìm process high memory

```bash
ps aux --sort=-%mem | head -20
```

### 35.17 Tìm process high CPU

```bash
ps aux --sort=-%cpu | head -20
```

### 35.18 Xem resource của một PID

```bash
ps -p 12345 -o pid,ppid,user,%cpu,%mem,rss,vsz,nlwp,etime,lstart,cmd
```

### 35.19 Check process resource limits

```bash
cat /proc/12345/limits
```

### 35.20 Check OOM killer

```bash
sudo dmesg -T | grep -i -E 'out of memory|oom|killed process'
```

hoặc:

```bash
sudo journalctl -k | grep -i -E 'oom|killed process'
```

---

# 36. Shell operators cần hiểu

| Ký hiệu | Ý nghĩa | Ví dụ | Senior note |
|---|---|---|---|
| `.` | Current directory. | `find . -name "*.log"` | Trong shell `source file` cũng có thể viết `. file`. |
| `..` | Parent directory. | `cd ..` | Có thể chain `../../..`. |
| `~` | Home directory. | `cd ~/.ssh` | `~user` có thể chỉ home của user khác. |
| `*` | Glob match 0+ ký tự. | `ls *.log` | Shell expand trước command; quote khi muốn pattern tới `find/grep`. |
| `?` | Glob match đúng 1 ký tự. | `ls app?.log` | Không giống regex `?`. |
| `$VAR` | Variable expansion. | `echo "$HOME"` | Quote `"$VAR"` để tránh word splitting/globbing. |
| `$(cmd)` | Command substitution. | `echo "Now: $(date)"` | Modern và dễ nest hơn backticks. |
| `'text'` | Single quote: gần như literal, không expand `$VAR`. | `echo '$HOME'` | Output literal `$HOME`. |
| `"text"` | Double quote: giữ whitespace nhưng vẫn expand variable/substitution. | `echo "$HOME"` | Default tốt khi dùng variable path. |
| `\` | Escape ký tự đặc biệt hoặc line continuation. | `echo \$HOME` | Trong shell script dài dùng `\` nối dòng. |
| `;` | Chạy command sau bất kể trước success/fail. | `date; hostname` | Khác `&&`. |
| `&&` | Chỉ chạy command sau nếu trước exit code 0. | `nginx -t && systemctl reload nginx` | Pattern production an toàn. |
| `||` | Chỉ chạy command sau nếu trước fail. | `curl -fsS URL || echo "health failed"` | Có thể dùng fallback/error handling. |
| `&` | Background process. | `sleep 100 &` | `$!` lấy PID gần nhất. |
| `|` | Pipe stdout. | `journalctl -u app | grep ERROR` | stderr không tự đi qua pipe trừ khi redirect. |

---

# 37. Safety checklist production

| Trước khi... | Check | Ví dụ | Senior note |
|---|---|---|---|
| Xoá recursive | path + content | `pwd; ls -la "$DIR"` | Validate biến không rỗng trước `rm -rf`. |
| Restart service | config + impact | `nginx -t` | Nếu hỗ trợ reload thì không restart full. |
| Kill process | PID + command | `ps -fp "$PID"` | PID có thể đã được reuse; verify command. |
| Chown/chmod recursive | tree/path | `find /opt/app -maxdepth 2 -ls | head` | Permission nên dir/file khác nhau. |
| Rsync delete | dry-run | `rsync -avhn --delete ...` | Đọc toàn bộ output trước chạy thật. |
| Edit config | backup | `cp -a file file.$(date +%F_%H%M%S).bak` | Sau edit dùng `diff -u`. |
| Cleanup log | list first | `find ... -mtime +30 -print` | Chỉ thêm `-delete` sau review. |

---

# 38. Learning order

| Level | Học | Mục tiêu |
|---|---|---|
| 1 | `pwd`, `ls`, `cd` | Không bị lạc trong filesystem. |
| 2 | `cat`, `less`, `head`, `tail` | Đọc config/log. |
| 3 | `cp`, `mv`, `rm`, `mkdir`, `touch` | Quản lý file/folder. |
| 4 | `grep`, `find` | Tìm text/file nhanh. |
| 5 | Vim tối thiểu | Có thể sửa config trên mọi server. |
| 6 | pipe + redirect | Ghép command và lưu/filter output. |
| 7 | `ps`, `pgrep`, `top`, `kill` | Quản lý process. |
| 8 | `df`, `du`, `free`, `vmstat` | Check resource. |
| 9 | `ss`, `lsof`, `curl`, `dig`, `nc` | Debug network/port/API. |
| 10 | `systemctl`, `journalctl` | Debug service chuẩn systemd. |
| 11 | tar/gzip | Backup/deploy artifact. |
| 12 | ssh/scp/rsync | Remote operations. |
| 13 | awk/sed/xargs | Xử lý dữ liệu/log nâng cao. |
| 14 | `/proc`, `lsof +L1`, `dmesg`, `pidstat`, `iostat` | Troubleshooting cấp senior. |

---

# 39. Quick Cheat Sheet — nên thuộc lòng

| Tình huống | Command | Ví dụ | Senior note |
|---|---|---|---|
| Đang ở đâu | `pwd` | `pwd` | Check trước destructive operation. |
| Xem file | `ls -lah` | `ls -lah /opt/app` | Có hidden + size human-readable. |
| Xem log | `less +F` | `less +F app.log` | Follow và search trong cùng tool. |
| Search lỗi | `grep -Ein -C` | `grep -Ein -C5 'ERROR|Exception' app.log` | Kèm context. |
| Tìm file | `find` | `find . -type f -name "*.yml"` | Quote wildcard. |
| Process | `pgrep -af` | `pgrep -af java` | Sạch hơn grep. |
| Port | `ss -lntp` | `sudo ss -lntp | grep ':8080'` | Chuẩn Linux hiện đại. |
| Health | `curl -fsS -v` | `curl -fsS -v http://127.0.0.1:8080/health` | Local test trước network ngoài. |
| Disk | `df -h` | `df -h` | Check mount full. |
| Drill disk | `du -xhd1` | `du -xhd1 /var | sort -hr` | Không cross filesystem. |
| Deleted-open file | `lsof +L1` | `sudo lsof +L1` | Giải thích disk không được free. |
| RAM | `free -h` | `free -h` | Nhìn `available`. |
| Service | `systemctl status` | `systemctl status app` | First-line debug. |
| Service log | `journalctl -xeu` | `journalctl -xeu app` | Start failure cực hữu ích. |
| Backup file | `cp -a` | `cp -a app.conf app.conf.bak` | Giữ metadata. |
| Compare | `diff -u` | `diff -u old.conf new.conf` | Review thay đổi. |
| SSH debug | `ssh -vvv` | `ssh -vvv user@host` | Auth/connect troubleshooting. |
| Transfer | `rsync -avhn` | `rsync -avhn --delete src/ host:/dst/` | Dry-run trước delete. |
| Kernel/OOM | `dmesg -T` | `dmesg -T | grep -i oom` | App “tự chết” có thể do OOM killer. |

---

# 40. Checklist debug nhanh cho Java/Web server

```bash
# 1) Service có chạy không?
systemctl status app

# 2) Log vừa rồi có gì?
journalctl -u app -n 300 --no-pager

# 3) Java process có thật sự tồn tại?
pgrep -af 'java.*app'

# 4) Có listen port không?
sudo ss -lntp | grep ':8080'

# 5) Local endpoint có trả lời?
curl -fsS -v http://127.0.0.1:8080/health

# 6) Server có thiếu resource?
free -h
df -h
uptime

# 7) Folder nào ăn disk?
sudo du -xhd1 /var 2>/dev/null | sort -hr

# 8) Có file deleted nhưng process giữ không?
sudo lsof +L1

# 9) Kernel có OOM kill app không?
sudo dmesg -T | grep -i -E 'oom|killed process|out of memory'

# 10) Config vừa thay gì?
diff -u application.yml.bak application.yml
```

---

## Ghi nhớ quan trọng

- Không cần “học thuộc mọi option” của Linux command. Hãy học **option phổ biến + biết đọc `man`/`--help`**.
- Khi không nhớ option:

```bash
command --help
```

hoặc:

```bash
man command
```

Ví dụ:

```bash
man find
man grep
man rsync
```

- Senior không phải người nhớ nhiều command nhất, mà là người:
  - hiểu `stdin/stdout/stderr`, exit code và pipe;
  - biết khoanh vùng lỗi theo **service → process → port → local endpoint → network → resource → kernel**;
  - luôn kiểm tra trước destructive operation;
  - biết lấy bằng chứng trước khi restart/xoá/kill làm mất trạng thái lỗi.
