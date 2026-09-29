# PuTTY / SSH Linux máy chủ (server / 서버) Command Cheat Sheet — Extended

> **Mạch đọc:** Đọc **PuTTY / SSH Linux máy chủ (server / 서버) Command Cheat Sheet — Extended** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Ví dụ cấp cao (senior / 시니어)** sang **Combo môi trường vận hành (production / 운영 환경)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


> Dùng khi SSH vào Linux máy chủ (server / 서버) bằng PuTTY, Terminal, iTerm, Windows Terminal...
>
> Phiên bản này ưu tiên **giải thích rõ option**, **mọi dòng đều có ví dụ**, và có thêm cột **Thực tế / cấp cao (senior / 시니어) tips** để phục vụ gỡ lỗi (debug / 디버그) môi trường vận hành (production / 운영 환경).

---

# 1. điều hướng (navigation / 내비게이션) — Di chuyển trong máy chủ (server / 서버)

Phần này chuyển khái niệm Linux thành thao tác hoặc bằng chứng có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu output với mô hình kernel, process, filesystem hoặc network đã học.

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `pwd` | In ra **absolute đường dẫn (path / 경로)** của working directory hiện tại. Dùng để xác nhận mình đang đứng ở đâu trước khi bản sao (copy / 복사)/xoá/chỉnh tệp (file / 파일). | `pwd` | Trước `rm -rf`, `chmod -R`, `chown -R` nên chạy `pwd && ls -la` để tránh thao tác nhầm thư mục môi trường vận hành (production / 운영 환경). |
| `ls` | Liệt kê tệp (file / 파일)/folder trong directory hiện tại. Mặc định không hiện tệp (file / 파일) ẩn bắt đầu bằng `.`. | `ls` | Dùng nhanh khi chỉ cần nhìn tên tệp (file / 파일). Với máy chủ (server / 서버) nên quen `ls -lah`. |
| `ls -l` | `-l` = **long format**: permission, đơn vị sở hữu (owner / 오너), group, kích thước (size / 크기), modified thời gian (time / 시간), filename. | `ls -l /opt/app` | Rất hữu ích để check đơn vị sở hữu (owner / 오너)/permission trước khi kết luận app “không đọc được tệp (file / 파일)”. |
| `ls -a` | `-a` = **all**, hiển thị cả hidden files như `.env`, `.bashrc`, `.git`. | `ls -a ~` | Khi app chạy khác terminal, thường cần kiểm tra hidden cấu hình (config / 설정) như `.env`, `.profile`. |
| `ls -la` | Kết hợp long format + hidden files. | `ls -la /home/app` | Một trong các lệnh nên thuộc lòng. |
| `ls -lh` | `-h` = **human-readable**, hiển thị kích thước (size / 크기) dạng KB/MB/GB thay vì byte. | `ls -lh app.log` | Dùng để nhìn nhanh log có phình bất thường hay không. |
| `ls -ltr` | `-t` sort theo modified thời gian (time / 시간); `-r` đảo thứ tự. Kết quả: tệp (file / 파일) cũ ở trên, tệp (file / 파일) mới nhất ở cuối. | `ls -ltr /var/log/app` | Rất tiện khi muốn nhìn tệp (file / 파일) log vừa sinh ra gần nhất ở cuối terminal. |
| `ls -lt` | Sort theo modified thời gian (time / 시간), **mới nhất ở đầu**. | `ls -lt /var/log | head` | Hay dùng để xem 10 tệp (file / 파일) vừa thay đổi gần nhất. |
| `ls -lS` | `-S` sort theo tệp (file / 파일) kích thước (size / 크기) giảm dần. | `ls -lhS /var/log` | Dùng để tìm nhanh tệp (file / 파일) log lớn. |
| `cd /path` | Đổi working directory sang đường dẫn (path / 경로) chỉ định. | `cd /var/log/nginx` | Có thể gõ `cd /var/log/nginx && ls -lah` để đổi folder và xem ngay. |
| `cd ..` | Đi lên parent directory một cấp. | `cd ..` | `cd ../../..` giúp lùi nhiều cấp nhanh. |
| `cd ~` | Về home directory của người dùng (user / 사용자) hiện tại. | `cd ~` | `~` thường là `/home/user` hoặc `/root`. |
| `cd /` | Về filesystem gốc (root / 루트) `/`. | `cd /` | Khác với `~`; `/` là gốc toàn máy chủ (server / 서버). |
| `cd -` | Quay lại directory trước đó và in đường dẫn (path / 경로) ra màn hình. | `cd -` | cấp cao (senior / 시니어) dùng rất nhiều khi chuyển qua lại giữa 2 folder deploy/log. |
| `tree` | Hiển thị cấu trúc folder theo dạng cây. Có thể chưa được cài mặc định. | `tree /opt/app` | Dùng khi cần hiểu nhanh bố cục (layout / 레이아웃) dự án (project / 프로젝트)/cấu hình (config / 설정). |
| `tree -L 2` | `-L` giới hạn số mức (level / 수준) hiển thị, tránh đầu ra (output / 출력) quá dài. | `tree -L 2 /opt/app` | Thường tốt hơn `tree` trên dự án (project / 프로젝트) lớn. |

---

# 2. tệp (file / 파일) & Folder — Tạo / xoá / bản sao (copy / 복사) / move

Phần này chuyển khái niệm Linux thành thao tác hoặc bằng chứng có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu output với mô hình kernel, process, filesystem hoặc network đã học.

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `touch file` | Tạo tệp (file / 파일) rỗng nếu tệp (file / 파일) chưa tồn tại; nếu đã tồn tại thì cập nhật modified thời gian (time / 시간). | `touch app.log` | Có thể dùng để kiểm tra permission ghi: `touch /path/test && rm /path/test`. |
| `mkdir dir` | Tạo một directory. Lỗi nếu parent chưa tồn tại. | `mkdir backup` | Dùng `mkdir -p` gần như luôn an toàn hơn trong script. |
| `mkdir -p a/b/c` | `-p` tạo cả parent directories còn thiếu và không báo lỗi nếu directory đã tồn tại. | `mkdir -p /opt/app/log/archive` | Rất hay dùng trong deploy script/idempotent script. |
| `cp src dst` | bản sao (copy / 복사) tệp (file / 파일) từ nguồn (source / 소스) sang destination. Nếu destination tồn tại sẽ bị ghi đè. | `cp app.conf app.conf.bak` | Trước sửa cấu hình (config / 설정) môi trường vận hành (production / 운영 환경) nên `cp -a file file.$(date +%F_%H%M%S).bak`. |
| `cp -r src dst` | `-r` = recursive, bản sao (copy / 복사) directory và toàn bộ nội dung con. | `cp -r config/ backup/` | Với Linux máy chủ (server / 서버), `cp -a` thường tốt hơn `cp -r` vì giữ siêu dữ liệu (metadata / 메타데이터). |
| `cp -p src dst` | `-p` bảo toàn chế độ (mode / 모드), đơn vị sở hữu (owner / 오너)/group nếu có quyền, timestamps. | `cp -p nginx.conf nginx.conf.bak` | Dùng khi backup cấu hình (config / 설정) cần giữ timestamp/permission. |
| `cp -a src dst` | `-a` = archive: recursive + preserve symlink, permission, quyền sở hữu (ownership / 소유권), timestamp. | `cp -a /opt/app /opt/app_backup` | Đây là lựa chọn “chuẩn cấp cao (senior / 시니어)” để backup cây folder trước deploy. |
| `cp -i src dst` | `-i` hỏi trước khi overwrite tệp (file / 파일) tồn tại. | `cp -i app.conf /etc/app.conf` | Hữu ích khi thao tác tay môi trường vận hành (production / 운영 환경) để tránh ghi đè nhầm. |
| `cp -v src dst` | `-v` hiển thị tệp (file / 파일) đang được bản sao (copy / 복사). | `cp -av config/ backup/` | `-av` thường dùng để vừa giữ siêu dữ liệu (metadata / 메타데이터) vừa thấy tiến trình. |
| `mv src dst` | Move tệp (file / 파일)/folder hoặc rename nếu nguồn (source / 소스)/destination cùng filesystem. | `mv app.log app.log.old` | Rename gần như tức thì, thường dùng rotate tạm log/cấu hình (config / 설정). |
| `mv -i src dst` | Hỏi trước khi overwrite destination. | `mv -i new.conf app.conf` | Nên dùng khi thay tệp (file / 파일) cấu hình (config / 설정) thủ công. |
| `rm file` | Xoá tệp (file / 파일). Không đưa vào recycle bin. | `rm old.log` | môi trường vận hành (production / 운영 환경): nên `ls -l old.log` trước khi xoá. |
| `rm -f file` | `-f` = force: không hỏi và không báo lỗi nếu tệp (file / 파일) không tồn tại. | `rm -f /tmp/app.pid` | Hay dùng trong script cleanup; nguy hiểm khi kết hợp wildcard sai. |
| `rm -r dir` | `-r` xoá directory recursively. | `rm -r old_backup` | Với dữ liệu quan trọng có thể đổi tên trước rồi xoá sau. |
| `rm -rf dir` | Recursive + force. Xoá rất mạnh, không hỏi. | `rm -rf /tmp/app-cache` | Trước khi chạy: `pwd; printf '%q\n' /tmp/app-cache; ls -la /tmp/app-cache`. Không dùng biến rỗng kiểu `rm -rf "$DIR"/*` nếu chưa validate. |
| `rmdir dir` | Chỉ xoá directory rỗng. | `rmdir empty_dir` | An toàn hơn `rm -r` nếu muốn chắc chắn folder không chứa dữ liệu (data / 데이터). |
| `ln -s target link` | Tạo symbolic link trỏ từ `link` tới `target`. | `ln -s /opt/app/releases/20260907 /opt/app/current` | mẫu (pattern / 패턴) deploy hay dùng: bản phát hành (release / 릴리스) folder + symlink `current` để quay lui (rollback / 롤백) nhanh. |
| `ln -sfn target link` | `-s` symlink, `-f` force, `-n` xử lý symlink destination như tệp (file / 파일). | `ln -sfn /opt/app/releases/v2 /opt/app/current` | Cập nhật symlink deploy gần như atomic. |
| `stat file` | Hiển thị inode, kích thước (size / 크기), permission, đơn vị sở hữu (owner / 오너), truy cập (access / 접근)/modify/thay đổi (change / 변경) thời gian (time / 시간). | `stat app.log` | Dùng để phân biệt `mtime`, `ctime`, `atime` khi gỡ lỗi (debug / 디버그) tệp (file / 파일) thay đổi. |
| `file name` | Dò loại tệp (file / 파일) dựa trên content/header, không chỉ extension. | `file app.jar` | Hữu ích khi tệp (file / 파일) `.txt` thực ra là nhị phân (binary / 이진)/gzip hoặc script sai line ending. |

> ⚠️ `rm -rf` không có undo mặc định. Trên môi trường vận hành (production / 운영 환경), hãy ưu tiên kiểm tra đường dẫn (path / 경로)/biến trước khi xoá.

---

# 3. Xem nội dung tệp (file / 파일)

Phần này chuyển khái niệm Linux thành thao tác hoặc bằng chứng có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu output với mô hình kernel, process, filesystem hoặc network đã học.

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `cat file` | In toàn bộ nội dung tệp (file / 파일) ra stdout. Phù hợp tệp (file / 파일) nhỏ. | `cat application.yml` | Tránh `cat` tệp (file / 파일) log vài GB vì terminal sẽ bị flood. |
| `cat -n file` | `-n` đánh số tất cả dòng. | `cat -n nginx.conf` | Hữu ích khi trao đổi “lỗi ở dòng 72”. |
| `less file` | Pager để xem tệp (file / 파일) lớn; không tải (load / 로드) toàn bộ vào màn hình, có tìm kiếm (search / 검색)/điều hướng (navigation / 내비게이션). | `less app.log` | Với log lớn, đây là lựa chọn tốt hơn `cat`. |
| `less -N file` | `-N` hiển thị line number. | `less -N app.log` | Kết hợp `/Exception`, `n`, `N`, `G`. |
| `less +F file` | Mở tệp (file / 파일) và follow giống `tail -f`; `Ctrl+C` để dừng follow và tìm kiếm (search / 검색). | `less +F app.log` | Workflow log rất mạnh: follow → `Ctrl+C` → `/ERROR` → `F` để follow tiếp. |
| `head file` | Hiển thị mặc định 10 dòng đầu. | `head app.log` | Dùng check header/cấu hình (config / 설정)/phiên bản (version / 버전) nhanh. |
| `head -n 50 file` | `-n 50` chỉ định số dòng đầu. | `head -n 50 application.yml` | Có thể viết `head -50 file` trên GNU. |
| `tail file` | Hiển thị mặc định 10 dòng cuối. | `tail app.log` | Dùng kiểm tra log mới nhất rất nhanh. |
| `tail -n 100 file` | Hiển thị 100 dòng cuối. | `tail -n 100 app.log` | Thường dùng 200/500/1000 dòng khi gỡ lỗi (debug / 디버그). |
| `tail -f file` | `-f` theo dõi tệp (file / 파일) realtime khi có dữ liệu append. | `tail -f app.log` | `Ctrl+C` để dừng. |
| `tail -F file` | `-F` tương đương follow theo **filename** và thử lại (retry / 재시도); tiếp tục tốt hơn khi logrotate rename/recreate tệp (file / 파일). | `tail -F /var/log/app/app.log` | môi trường vận hành (production / 운영 환경) log rotate: thường chọn `-F` thay vì `-f`. |
| `tac file` | In tệp (file / 파일) theo thứ tự dòng từ cuối lên đầu. | `tac app.log | less` | Hữu ích khi muốn đọc newest-first mà tệp (file / 파일) không quá lớn. |
| `nl file` | In nội dung có line number; hỗ trợ format numbering tốt hơn `cat -n`. | `nl -ba app.conf` | `-ba` đánh số cả blank lines. |

---

# 4. Edit tệp (file / 파일) — vi / vim / nano

Phần này chuyển khái niệm Linux thành thao tác hoặc bằng chứng có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu output với mô hình kernel, process, filesystem hoặc network đã học.

| Command / Key | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `vi file` | Mở tệp (file / 파일) bằng `vi` hoặc hiện thực (implementation / 구현) tương thích. | `vi /etc/nginx/nginx.conf` | Gần như máy chủ (server / 서버) Linux nào cũng có `vi`; nên biết tối thiểu save/tìm kiếm (search / 검색)/quit. |
| `vim file` | Mở Vim, thường có nhiều tính năng hơn vi. | `vim application.yml` | Có thể chưa được cài trên minimal máy chủ (server / 서버). |
| `nano file` | Editor đơn giản, command hiển thị dưới màn hình. | `nano app.conf` | Dễ dùng nhưng nhiều môi trường vận hành (production / 운영 환경) máy chủ (server / 서버) không cài. |
| `i` | Trong Vim: vào Insert chế độ (mode / 모드) trước cursor. | `i` | Nhấn `Esc` trước khi chạy command chế độ (mode / 모드). |
| `a` | Insert sau cursor. | `a` | Nhanh khi append ký tự sau vị trí hiện tại. |
| `o` | Tạo dòng mới bên dưới và vào Insert chế độ (mode / 모드). | `o` | Rất hay dùng khi thêm cấu hình (config / 설정) line. |
| `Esc` | Trở về Normal chế độ (mode / 모드). | `Esc` | Nếu “gõ gì cũng ra lệnh lạ”, nhấn `Esc` vài lần. |
| `:w` | ghi (write / 쓰기)/save tệp (file / 파일). | `:w` | Nếu permission denied, có thể thoát rồi mở bằng `sudoedit`. |
| `:q` | Quit nếu không có thay đổi chưa save. | `:q` | `:q!` để bỏ thay đổi. |
| `:wq` | Save rồi quit. | `:wq` | `ZZ` cũng save+quit trong normal chế độ (mode / 모드). |
| `:q!` | Force quit không save. | `:q!` | Dùng khi sửa nhầm. |
| `dd` | Delete/cut dòng hiện tại vào Vim register. | `dd` | `5dd` xoá 5 dòng. |
| `yy` | Yank/bản sao (copy / 복사) dòng hiện tại. | `yy` | `5yy` bản sao (copy / 복사) 5 dòng. |
| `p` | Paste sau cursor/dòng. | `p` | `P` paste trước. |
| `u` | Undo thay đổi gần nhất. | `u` | Có thể nhấn nhiều lần. |
| `Ctrl+r` | Redo trong Vim. | `Ctrl+r` | Khác với shell `Ctrl+R`. |
| `/text` | tìm kiếm (search / 검색) forward. | `/server.port` | `n` tiếp theo, `N` quay lại. |
| `:%s/old/new/g` | Substitute toàn bộ tệp (file / 파일); `%` = toàn tệp (file / 파일), `g` = mọi occurrence trên mỗi dòng. | `:%s/http:/https:/g` | Thêm `c`: `:%s/old/new/gc` để confirm từng replace. |
| `:set number` | Hiển thị line number. | `:set number` | `:set relativenumber` hữu ích khi điều hướng (navigation / 내비게이션). |
| `gg` | Đi đầu tệp (file / 파일). | `gg` | `G` xuống cuối tệp (file / 파일). |
| `10G` | Đi tới line 10. | `120G` | Hoặc `:120`. |
| `sudoedit file` | Mở tệp (file / 파일) cần quyền gốc (root / 루트) bằng editor người dùng (user / 사용자) rồi ghi lại an toàn qua sudo. | `sudoedit /etc/nginx/nginx.conf` | Thường tốt hơn chạy cả editor dưới quyền gốc (root / 루트). |

---

# 5. tìm kiếm (search / 검색) tệp (file / 파일) / folder — find

Phần này chuyển khái niệm Linux thành thao tác hoặc bằng chứng có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu output với mô hình kernel, process, filesystem hoặc network đã học.

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `find . -name "name"` | tìm kiếm (search / 검색) từ hiện tại (current / 현재) directory theo tên **case-sensitive**. | `find . -name "app.log"` | `.` nghĩa là bắt đầu từ hiện tại (current / 현재) directory. |
| `find . -iname "*.log"` | `-iname` không phân biệt hoa thường. | `find . -iname "*.LOG"` | Hữu ích khi extension không đồng nhất. |
| `find /path -type f` | `-type f` chỉ trả regular tệp (file / 파일). | `find /var/log -type f` | Thường kết hợp `-name`, `-mtime`, `-size`. |
| `find /path -type d` | `-type d` chỉ directory. | `find /opt -type d -name "logs"` | Dùng tìm folder trong cây (tree / 트리) lớn. |
| `find . -name "*.log"` | Wildcard `*` match chuỗi bất kỳ; quote mẫu (pattern / 패턴) để shell không expand trước. | `find . -name "*.log"` | Luôn quote `"*.log"` là thói quen tốt. |
| `find . -size +100M` | `+100M` = lớn hơn 100 MiB. `-100M` = nhỏ hơn. | `find /var/log -type f -size +100M` | Tìm log lớn trước khi disk full. |
| `find . -mtime -1` | Modified ít hơn 1×24h trước. | `find /opt/app -type f -mtime -1` | `-mmin -60` chính xác hơn cho “60 phút gần đây”. |
| `find . -mtime +30` | Modified hơn 30×24h trước. | `find /backup -type f -mtime +30` | Thường dùng cleanup backup/log cũ. |
| `find . -mmin -30` | Modified trong khoảng 30 phút gần đây. | `find /opt/app -type f -mmin -30` | Rất hữu ích khi muốn biết deploy vừa thay tệp (file / 파일) nào. |
| `find . -empty` | Tìm tệp (file / 파일) rỗng hoặc directory rỗng. | `find /tmp -empty` | Có thể kết hợp `-type f` để tránh directory. |
| `find ... -exec CMD {} \;` | Chạy command trên từng kết quả; `{}` là hiện tại (current / 현재) kết quả (result / 결과). | `find . -name "*.log" -exec ls -lh {} \;` | `{} +` hiệu quả hơn vì batch nhiều tệp (file / 파일) vào một command. |
| `find ... -delete` | Xoá trực tiếp kết quả tìm kiếm (search / 검색). | `find /tmp -type f -name "*.tmp" -mtime +7 -delete` | Luôn chạy cùng lệnh **không có `-delete` trước** để rà soát (review / 검토). |
| `which cmd` | Tìm executable sẽ được shell dùng theo `$PATH`. | `which java` | Tốt để check đang chạy Java nào. |
| `command -v cmd` | POSIX-friendly hơn `which`; trả đường dẫn (path / 경로)/alias/builtin. | `command -v java` | cấp cao (senior / 시니어) shell script thường ưu tiên `command -v`. |
| `whereis cmd` | Tìm nhị phân (binary / 이진)/nguồn (source / 소스)/man ở các location chuẩn. | `whereis java` | Không phải công cụ tìm kiếm (search / 검색) filesystem tổng quát. |

### Ví dụ cấp cao (senior / 시니어)

Phần này chuyển khái niệm Linux thành thao tác hoặc bằng chứng có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu output với mô hình kernel, process, filesystem hoặc network đã học.

```bash
find /var/log -type f -name "*.log" -size +500M -printf '%TY-%Tm-%Td %TH:%TM %10s %p\n'
```

Tìm tệp (file / 파일) log >500MB và in timestamp, kích thước (size / 크기), đường dẫn (path / 경로).

---

# 6. tìm kiếm (search / 검색) văn bản (text / 텍스트) — grep

Phần này chuyển khái niệm Linux thành thao tác hoặc bằng chứng có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu output với mô hình kernel, process, filesystem hoặc network đã học.

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `grep "text" file` | In các dòng chứa mẫu (pattern / 패턴). Mặc định mẫu (pattern / 패턴) là basic regex. | `grep "ERROR" app.log` | Quote mẫu (pattern / 패턴) nếu có không gian (space / 공간)/ký tự đặc biệt. |
| `grep -i` | Ignore trường hợp (case / 사례). | `grep -i "error" app.log` | Dùng khi log không nhất quán hoa/thường. |
| `grep -n` | In line number trước kết quả. | `grep -n "ERROR" app.log` | Rất hữu ích để mở lại bằng `less +123 app.log`. |
| `grep -v` | In các dòng **không match** mẫu (pattern / 패턴). | `grep -v "DEBUG" app.log` | Dùng loại noise khỏi log. |
| `grep -c` | Đếm số dòng match, không in nội dung. | `grep -c "ERROR" app.log` | Đếm lỗi nhanh; không phải số occurrences nếu một dòng có nhiều match. |
| `grep -r` | tìm kiếm (search / 검색) recursive trong folder. | `grep -r "DB_URL" /opt/app` | Thường dùng với `-n`. |
| `grep -R` | Recursive và follow symbolic links. | `grep -R "server.port" /opt/app` | Cẩn thận symlink vòng lặp (loop / 루프)/dự án (project / 프로젝트) lớn. |
| `grep -w` | Match whole word. | `grep -w "ERROR" app.log` | Không match `ERROR_CODE`. |
| `grep -F` | Fixed string, không interpret regex. | `grep -F "a[b]" file.txt` | Nhanh/an toàn khi tìm kiếm (search / 검색) literal có ký tự regex. |
| `grep -E` | Extended regex, hỗ trợ `|`, `+`, `?`, group thuận tiện. | `grep -E "ERROR|WARN|Exception" app.log` | Rất hay dùng cho nhiều từ khóa (keyword / 키워드). |
| `grep -A 5` | In 5 dòng **After** match. | `grep -A 5 "Exception" app.log` | Đọc dấu vết ngăn xếp (stack trace / 스택 트레이스) phía sau từ khóa (keyword / 키워드). |
| `grep -B 5` | In 5 dòng **Before** match. | `grep -B 5 "ERROR" app.log` | Xem yêu cầu (request / 요청)/ngữ cảnh (context / 맥락) trước lỗi. |
| `grep -C 5` | In 5 dòng trước + sau (**context**). | `grep -C 5 "ERROR" app.log` | Một trong option gỡ lỗi (debug / 디버그) log hữu ích nhất. |
| `grep -l` | Chỉ in tên tệp (file / 파일) có match. | `grep -rl "password" ./config` | Tìm tệp (file / 파일) nào chứa từ khóa (keyword / 키워드) mà không flood nội dung. |
| `grep -L` | Chỉ in tên tệp (file / 파일) **không** có match. | `grep -L "health" *.conf` | Dùng kiểm tra (audit / 감사) cấu hình (config / 설정) thiếu setting. |
| `grep -m 1` | Dừng sau N match trên mỗi tệp (file / 파일). | `grep -m 1 "Started" app.log` | Tìm first occurrence nhanh trên tệp (file / 파일) lớn. |
| `grep --color=auto` | Highlight match nếu terminal hỗ trợ. | `grep --color=auto -n "ERROR" app.log` | Nhiều distro alias sẵn `grep --color=auto`. |

### Combo môi trường vận hành (production / 운영 환경)

Phần này chuyển khái niệm Linux thành thao tác hoặc bằng chứng có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu output với mô hình kernel, process, filesystem hoặc network đã học.

```bash
grep -Ein -C 10 "ERROR|WARN|Exception|Caused by" app.log
```

```bash
tail -F app.log | grep --line-buffered -E "ERROR|Exception|timeout"
```

`--line-buffered` giúp đầu ra (output / 출력) chuỗi xử lý (pipeline / 파이프라인) realtime không bị buffer lâu.

---

# 7. Log — thao tác thường dùng

Phần này chuyển khái niệm Linux thành thao tác hoặc bằng chứng có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu output với mô hình kernel, process, filesystem hoặc network đã học.

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `tail -n 500 -F file` | Đọc 500 dòng cuối rồi tiếp tục follow theo filename. | `tail -n 500 -F app.log` | Đây là default tốt khi kiểm thử (test / 테스트) chức năng vừa bấm trên app. |
| `less +F file` | Follow trong `less`, có thể pause và tìm kiếm (search / 검색) ngay trong cùng công cụ (tool / 도구). | `less +F app.log` | `Ctrl+C` → `/keyword` → `n` → `F`. |
| `zgrep PATTERN file.gz` | tìm kiếm (search / 검색) trực tiếp trong gzip mà không cần extract. | `zgrep -in "ERROR" app.log.2.gz` | Cực hữu ích với rotated logs. |
| `zless file.gz` | Xem gzip bằng pager. | `zless access.log.3.gz` | tìm kiếm (search / 검색) `/text` như `less`. |
| `journalctl` | Xem log do systemd journal quản lý. | `journalctl` | Có thể cần sudo để xem đầy đủ. |
| `journalctl -u svc` | `-u` filter theo systemd đơn vị (unit / 단위). | `journalctl -u nginx.service` | Dùng đúng tên đơn vị (unit / 단위); có thể bỏ `.service`. |
| `journalctl -u svc -f` | Follow realtime journal của dịch vụ (service / 서비스). | `journalctl -u app -f` | Tương đương `tail -f` cho systemd. |
| `journalctl -u svc -n 200` | Chỉ 200 log entry gần nhất. | `journalctl -u app -n 200` | Nhanh hơn mở toàn journal. |
| `journalctl --since today` | Filter theo thời gian từ đầu ngày. | `journalctl -u app --since today` | Có thể dùng `"2026-09-07 09:00:00"`. |
| `journalctl --since "1 hour ago"` | Relative thời gian (time / 시간) filter. | `journalctl -u app --since "1 hour ago"` | Rất tiện sau sự cố (incident / 인시던트) mới xảy ra. |
| `journalctl --since ... --until ...` | Chọn khoảng thời gian cụ thể. | `journalctl -u app --since "18:00" --until "18:10"` | cấp cao (senior / 시니어) gỡ lỗi (debug / 디버그) sự cố (incident / 인시던트) thường khoanh đúng thời gian (time / 시간) cửa sổ (window / 윈도우) trước. |
| `journalctl -p err` | Filter theo priority lỗi (error / 오류) trở lên. | `journalctl -p err --since today` | Có thể dùng `warning`, `crit`. |
| `journalctl -xeu svc` | `-x` thêm giải thích, `-e` tới cuối, `-u` đơn vị (unit / 단위). | `journalctl -xeu nginx` | Rất hữu ích khi dịch vụ (service / 서비스) start thất bại (fail / 실패). |

---

# 8. Permission / đơn vị sở hữu (owner / 오너)

Phần này chuyển khái niệm Linux thành thao tác hoặc bằng chứng có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu output với mô hình kernel, process, filesystem hoặc network đã học.

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `ls -l` | Xem chế độ (mode / 모드) như `-rwxr-xr-x`, đơn vị sở hữu (owner / 오너), group. | `ls -l deploy.sh` | Hãy đọc permission trước khi dùng `chmod 777`. |
| `chmod 755 file` | đơn vị sở hữu (owner / 오너) `rwx`, group `r-x`, others `r-x`. | `chmod 755 deploy.sh` | Phù hợp executable/script phổ biến. |
| `chmod 644 file` | đơn vị sở hữu (owner / 오너) `rw-`, group/others `r--`. | `chmod 644 application.yml` | cấu hình (config / 설정) không cần execute thường dùng 640/644 tuỳ bảo mật (security / 보안). |
| `chmod 600 file` | Chỉ đơn vị sở hữu (owner / 오너) đọc/ghi. | `chmod 600 ~/.ssh/id_rsa` | SSH private key thường bắt buộc permission chặt. |
| `chmod +x file` | Thêm execute bit theo quy tắc (rule / 규칙) umask/hiện tại (current / 현재) lớp (class / 클래스). | `chmod +x deploy.sh` | Kiểm tra shebang `#!/bin/bash` nếu script vẫn không chạy. |
| `chmod -x file` | Gỡ execute bit. | `chmod -x accidental.txt` | Dùng khi tệp (file / 파일) không nên executable. |
| `chmod -R 755 dir` | Recursive mọi tệp (file / 파일)/folder. | `chmod -R 755 /opt/app/bin` | Cẩn thận: ép tệp (file / 파일) dữ liệu (data / 데이터) thành executable. cấp cao (senior / 시니어) thường dùng `find` để set dir/tệp (file / 파일) riêng. |
| `find dir -type d -exec chmod 755 {} +` | Chỉ set permission directory. | `find /opt/app -type d -exec chmod 755 {} +` | Chuẩn hơn `chmod -R 755`. |
| `find dir -type f -exec chmod 644 {} +` | Chỉ set permission tệp (file / 파일). | `find /opt/app -type f -exec chmod 644 {} +` | Kết hợp với quy tắc (rule / 규칙) directory ở trên. |
| `chown user file` | Đổi đơn vị sở hữu (owner / 오너) người dùng (user / 사용자). | `sudo chown app app.log` | App permission lỗi rất thường do đơn vị sở hữu (owner / 오너) sai sau deploy bằng gốc (root / 루트). |
| `chown user:group file` | Đổi đơn vị sở hữu (owner / 오너) và group. | `sudo chown app:app application.yml` | Hay dùng cho app dịch vụ (service / 서비스) account. |
| `chown -R user:group dir` | Recursive đơn vị sở hữu (owner / 오너)/group. | `sudo chown -R app:app /opt/app` | rà soát (review / 검토) đường dẫn (path / 경로) kỹ trước khi recursive. |
| `umask` | Hiển thị mask ảnh hưởng permission mặc định khi tạo tệp (file / 파일)/dir. | `umask` | `0022` thường tạo tệp (file / 파일) 644, dir 755. |
| `namei -l /path/file` | Hiển thị permission của **mọi directory trên đường dẫn (path / 경로)**. | `namei -l /opt/app/config/app.yml` | cấp cao (senior / 시니어) dùng khi tệp (file / 파일) permission đúng nhưng app vẫn “Permission denied” do parent dir thiếu `x`. |

---

# 9. người dùng (user / 사용자) / sudo

Phần này chuyển khái niệm Linux thành thao tác hoặc bằng chứng có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu output với mô hình kernel, process, filesystem hoặc network đã học.

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `whoami` | In effective username. | `whoami` | Khi SSH qua account chung/sudo, luôn biết mình đang là ai. |
| `id` | In UID, primary GID và supplementary groups. | `id appuser` | gỡ lỗi (debug / 디버그) quyền group rất hữu ích. |
| `who` | Hiển thị session người dùng (user / 사용자) đang login. | `who` | Có thể thấy terminal/remote session. |
| `w` | Giống `who` nhưng thêm uptime/tải (load / 로드) và command người dùng (user / 사용자) đang chạy. | `w` | Hữu ích khi máy chủ (server / 서버) nhiều admin cùng thao tác. |
| `sudo cmd` | Chạy một command với elevated privilege theo sudo chính sách (policy / 정책). | `sudo systemctl restart nginx` | Ưu tiên sudo từng command hơn vào gốc (root / 루트) shell lâu. |
| `sudo -i` | Mở login shell của gốc (root / 루트), tải (load / 로드) gốc (root / 루트) môi trường (environment / 환경). | `sudo -i` | Dùng cẩn thận; prompt gốc (root / 루트) thường `#`. |
| `su - user` | Switch người dùng (user / 사용자) và tải (load / 로드) login môi trường (environment / 환경) của người dùng (user / 사용자) đó. | `sudo su - oracle` | `-` quan trọng vì tải (load / 로드) HOME/đường dẫn (path / 경로)/profile đúng người dùng (user / 사용자). |
| `sudo -u user cmd` | Chạy command dưới người dùng (user / 사용자) khác mà không cần mở shell. | `sudo -u app java -version` | Rất hữu ích để tái hiện môi trường (environment / 환경) của dịch vụ (service / 서비스) account. |
| `passwd` | Đổi password người dùng (user / 사용자) hiện tại hoặc người dùng (user / 사용자) khác nếu gốc (root / 루트). | `passwd` | Nhiều máy chủ (server / 서버) enterprise disable password SSH và chỉ dùng key. |

---

# 10. tiến trình (process / 프로세스)

Phần này chuyển khái niệm Linux thành thao tác hoặc bằng chứng có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu output với mô hình kernel, process, filesystem hoặc network đã học.

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `ps -ef` | `-e` tất cả tiến trình (process / 프로세스), `-f` full format gồm UID, PID, PPID, start thời gian (time / 시간), command. | `ps -ef | grep java` | Classic trên Unix/Linux enterprise. |
| `ps aux` | BSD format: người dùng (user / 사용자), PID, CPU, MEM, VSZ, RSS, STAT, command. | `ps aux --sort=-%mem | head` | Dễ sort CPU/RAM. |
| `pgrep name` | Tìm PID tiến trình (process / 프로세스) theo tên/mẫu (pattern / 패턴). | `pgrep java` | Gọn hơn `ps | grep`. |
| `pgrep -af pattern` | `-a` full command line, `-f` match full command. | `pgrep -af 'java.*app.jar'` | Đây là cách sạch để tìm Java tiến trình (process / 프로세스) cụ thể. |
| `pidof name` | Trả PID của program name. | `pidof nginx` | Hữu ích cho daemon đơn giản. |
| `top` | Monitor realtime CPU/RAM/tiến trình (process / 프로세스). | `top` | Trong top: `P` sort CPU, `M` sort bộ nhớ (memory / 메모리), `1` per-CPU. |
| `top -p PID` | Chỉ monitor PID chỉ định. | `top -p 12345` | Tập trung vào app đang gỡ lỗi (debug / 디버그). |
| `kill PID` | Gửi SIGTERM (15) mặc định để tiến trình (process / 프로세스) shutdown graceful. | `kill 12345` | Không cần viết `-15` nếu dùng mặc định. |
| `kill -15 PID` | Gửi SIGTERM tường minh (explicit / 명시적). | `kill -15 12345` | Cho app cơ hội flush dữ liệu (data / 데이터)/close resources. |
| `kill -9 PID` | SIGKILL: kernel dừng ngay, tiến trình (process / 프로세스) không cleanup được. | `kill -9 12345` | Chỉ dùng khi TERM không hiệu quả; không phải “cách chuẩn” để stop app. |
| `pkill pattern` | Gửi tín hiệu (signal / 신호) theo tiến trình (process / 프로세스) name/mẫu (pattern / 패턴). | `pkill -15 java` | Nguy hiểm nếu có nhiều Java app; nên dùng mẫu (pattern / 패턴) cụ thể. |
| `pkill -f pattern` | Match full command line. | `pkill -f 'app-name.jar'` | Kiểm tra `pgrep -af pattern` trước rồi mới `pkill`. |
| `pstree -p` | Hiển thị cây parent-child tiến trình (process / 프로세스) kèm PID. | `pstree -p 1` | gỡ lỗi (debug / 디버그) tiến trình (process / 프로세스) được sinh bởi dịch vụ (service / 서비스)/script nào. |
| `ps -o ... -p PID` | Chọn các trường dữ liệu (field / 필드) cần xem. | `ps -p 1234 -o pid,ppid,user,%cpu,%mem,etime,lstart,cmd` | cấp cao (senior / 시니어) thường dùng để lấy đúng siêu dữ liệu (metadata / 메타데이터) thay vì đọc `ps -ef` dài. |

---

# 11. Background jobs / nohup

Đây là mục tra cứu thao tác. Hãy đọc câu hỏi vận hành trước, chọn lệnh phù hợp, rồi kiểm tra output và tác động phụ trước khi áp dụng trên server thật.

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `cmd &` | Chạy tiến trình (process / 프로세스) background của hiện tại (current / 현재) shell. | `sleep 300 &` | tiến trình (process / 프로세스) vẫn có thể chịu SIGHUP khi SSH đóng tùy shell/cấu hình (config / 설정). |
| `nohup cmd &` | Ignore SIGHUP để tiến trình (process / 프로세스) tiếp tục sau logout; mặc định đầu ra (output / 출력) vào `nohup.out`. | `nohup java -jar app.jar > app.log 2>&1 &` | Trên app môi trường vận hành (production / 운영 환경) hiện đại nên dùng systemd/bộ chứa (container / 컨테이너) thay vì nohup nếu có thể. |
| `jobs` | Xem job của **hiện tại (current / 현재) shell**, không phải toàn hệ thống (system / 시스템). | `jobs -l` | `-l` thêm PID. |
| `fg %1` | Đưa job 1 về foreground. | `fg %1` | Job ID khác PID. |
| `bg %1` | Resume suspended job ở background. | `bg %1` | Thường dùng sau `Ctrl+Z`. |
| `Ctrl+Z` | Gửi SIGTSTP để suspend foreground job. | `Ctrl+Z` | Sau đó `bg` hoặc `fg`. |
| `disown %1` | Gỡ job khỏi shell job bảng (table / 테이블), giúp tránh SIGHUP tùy shell. | `disown %1` | Không thay thế tiến trình (process / 프로세스) supervisor thực thụ. |
| `echo $!` | PID của background command gần nhất. | `nohup ./run.sh & echo $!` | Hữu ích trong startup script đơn giản. |

---

# 12. systemd / dịch vụ (service / 서비스)

Đây là mục tra cứu thao tác. Hãy đọc câu hỏi vận hành trước, chọn lệnh phù hợp, rồi kiểm tra output và tác động phụ trước khi áp dụng trên server thật.

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `systemctl status svc` | Xem active trạng thái (state / 상태), PID, recent log, exit mã (code / 코드). | `systemctl status nginx` | Lệnh đầu tiên khi dịch vụ (service / 서비스) có vấn đề. |
| `systemctl start svc` | Start dịch vụ (service / 서비스). | `sudo systemctl start nginx` | Sau đó verify bằng `status` + cổng (port / 포트) + curl. |
| `systemctl stop svc` | Stop dịch vụ (service / 서비스). | `sudo systemctl stop nginx` | Xem `TimeoutStopSec` nếu dịch vụ (service / 서비스) stop lâu. |
| `systemctl restart svc` | Stop rồi start lại. | `sudo systemctl restart app` | Restart gây downtime ngắn; cấu hình (config / 설정) reload được thì ưu tiên reload. |
| `systemctl reload svc` | Yêu cầu dịch vụ (service / 서비스) reload cấu hình (config / 설정) mà không full restart, nếu dịch vụ (service / 서비스) hỗ trợ. | `sudo systemctl reload nginx` | Nginx thường dùng reload sau `nginx -t`. |
| `systemctl enable svc` | Tạo enablement để dịch vụ (service / 서비스) auto start theo mục tiêu (target / 대상) khi boot. | `sudo systemctl enable app` | `enable --now` vừa enable vừa start. |
| `systemctl disable svc` | Gỡ auto-start enablement. | `sudo systemctl disable app` | Không tự stop dịch vụ (service / 서비스) đang chạy. |
| `systemctl is-active svc` | Trả `active`/`inactive` và exit mã (code / 코드) phù hợp script. | `systemctl is-active --quiet nginx && echo OK` | Tốt trong health/check script. |
| `systemctl is-enabled svc` | Kiểm tra auto-start trạng thái (state / 상태). | `systemctl is-enabled nginx` | Phân biệt “đang chạy” và “sẽ chạy sau reboot”. |
| `systemctl list-units --type=service` | danh sách (list / 목록) loaded dịch vụ (service / 서비스) units. | `systemctl list-units --type=service --state=running` | Filter chỉ running dịch vụ (service / 서비스). |
| `systemctl daemon-reload` | Bắt systemd reload đơn vị (unit / 단위) files sau khi sửa/tạo `.service`. | `sudo systemctl daemon-reload` | Không restart dịch vụ (service / 서비스) tự động. |
| `systemctl cat svc` | Hiển thị đơn vị (unit / 단위) tệp (file / 파일) + drop-in cấu hình (config / 설정). | `systemctl cat app.service` | cấp cao (senior / 시니어) dùng để biết cấu hình (config / 설정) thực tế đang được systemd tải (load / 로드). |
| `systemctl show svc` | In properties machine-readable-ish. | `systemctl show app -p MainPID -p ExecStart` | Hữu ích trong script/gỡ lỗi (debug / 디버그) startup. |
| `systemctl reset-failed svc` | Reset failed trạng thái (state / 상태)/counter. | `sudo systemctl reset-failed app` | Dùng sau khi xử lý lỗi `start-limit-hit`. |

---

# 13. Disk / lưu trữ (storage / 저장소)

Đây là mục tra cứu thao tác. Hãy đọc câu hỏi vận hành trước, chọn lệnh phù hợp, rồi kiểm tra output và tác động phụ trước khi áp dụng trên server thật.

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `df -h` | Filesystem usage; `-h` hiển thị kích thước (size / 크기) dễ đọc. | `df -h` | Check `%Use` của mount điểm (point / 지점), không chỉ tổng máy chủ (server / 서버). |
| `df -Th` | `-T` thêm filesystem kiểu (type / 타입). | `df -Th /opt/app` | Hữu ích phân biệt ext4/xfs/nfs/tmpfs. |
| `du -sh dir` | `-s` summary, `-h` human-readable. | `du -sh /var/log` | Dùng để tìm folder gây đầy disk. |
| `du -sh *` | kích thước (size / 크기) từng entry trong hiện tại (current / 현재) folder. | `du -sh * | sort -h` | `sort -h` sort đúng KB/MB/GB. |
| `du -h --max-depth=1` | Hiện kích thước (size / 크기) theo mức (level / 수준) 1. | `du -h --max-depth=1 /var | sort -hr` | Rất hay dùng để drill-down disk usage. |
| `du -x` | Không đi sang filesystem/mount khác. | `du -xhd1 / | sort -hr` | Quan trọng khi `/` có mount NFS hoặc volume khác. |
| `lsblk` | Liệt kê khối (block / 블록) devices, partition, mountpoint. | `lsblk -f` | `-f` thêm filesystem/UUID. |
| `findmnt` | Hiển thị filesystem mount cây (tree / 트리) và nguồn (source / 소스)/mục tiêu (target / 대상). | `findmnt /opt/app` | Dễ đọc hơn `mount`. |
| `mount` | Xem mount hoặc mount filesystem nếu có quyền. | `mount | grep '/data'` | Với môi trường vận hành (production / 운영 환경), thay đổi mount cần hiểu `/etc/fstab`. |
| `lsof +L1` | Tìm tệp (file / 파일) đã bị delete nhưng tiến trình (process / 프로세스) vẫn mở, nên disk chưa được giải phóng. | `sudo lsof +L1` | Đây là command “cấp cao (senior / 시니어)” cực hữu ích khi `df` đầy nhưng `du` không thấy. |
| `df -i` | Kiểm tra inode usage. | `df -i` | Disk có thể “full” vì hết inode dù còn GB trống. |

### Drill-down disk usage

Đây là mục tra cứu thao tác. Hãy đọc câu hỏi vận hành trước, chọn lệnh phù hợp, rồi kiểm tra output và tác động phụ trước khi áp dụng trên server thật.

```bash
sudo du -xhd1 / 2>/dev/null | sort -hr
```

Sau đó đi vào folder lớn và lặp lại.

---

# 14. bộ nhớ (memory / 메모리) / CPU / hệ thống (system / 시스템)

Đây là mục tra cứu thao tác. Hãy đọc câu hỏi vận hành trước, chọn lệnh phù hợp, rồi kiểm tra output và tác động phụ trước khi áp dụng trên server thật.

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `free -h` | RAM total/used/free/dùng chung (shared / 공유)/buff-cache/available. | `free -h` | Hãy nhìn `available`, không chỉ `free`; Linux dùng RAM làm bộ nhớ đệm (cache / 캐시). |
| `uptime` | Uptime, người dùng (user / 사용자) count, tải (load / 로드) average 1/5/15 phút. | `uptime` | tải (load / 로드) cao không đồng nghĩa CPU 100%; có thể do I/O wait. |
| `lscpu` | CPU kiến trúc (architecture / 아키텍처)/topology/features. | `lscpu` | Check số socket/cốt lõi (core / 핵심)/luồng thực thi (thread / 스레드), virtualization. |
| `nproc` | Số processing units hiện available cho tiến trình (process / 프로세스). | `nproc` | So sánh tải (load / 로드) average với số CPU là một heuristic nhanh. |
| `uname -a` | Kernel name/bản phát hành (release / 릴리스)/kiến trúc (architecture / 아키텍처) và host info. | `uname -a` | Dùng khi gỡ lỗi (debug / 디버그) tính tương thích (compatibility / 호환성) kernel/mô-đun (module / 모듈). |
| `hostname` | Hostname hiện tại. | `hostname` | Rất quan trọng khi SSH nhiều máy chủ (server / 서버) giống nhau. |
| `hostnamectl` | Hostname + OS/kernel/kiến trúc (architecture / 아키텍처). | `hostnamectl` | Một lệnh tóm tắt hệ thống (system / 시스템) khá tốt. |
| `cat /etc/os-release` | Distro và phiên bản (version / 버전). | `cat /etc/os-release` | Giúp chọn đúng apt/yum/dnf và docs. |
| `date` | cục bộ (local / 로컬) máy chủ (server / 서버) date/thời gian (time / 시간). | `date '+%F %T %Z'` | sự cố (incident / 인시던트) debugging phải check timezone máy chủ (server / 서버). |
| `timedatectl` | Timezone, NTP sync, RTC. | `timedatectl` | Clock lệch có thể gây JWT/TLS/log correlation lỗi. |
| `vmstat 1` | Snapshot CPU, runnable tasks, bộ nhớ (memory / 메모리), paging, I/O mỗi 1 giây. | `vmstat 1 10` | Quan sát `r`, `si/so`, `wa` để phân biệt CPU/bộ nhớ (memory / 메모리)/I/O bottleneck. |
| `iostat -xz 1` | Extended disk I/O stats theo interval. | `iostat -xz 1 10` | Nhìn `%util`, `await`; cần gói (package / 패키지) sysstat. |

---

# 15. mạng (network / 네트워크)

Đây là mục tra cứu thao tác. Hãy đọc câu hỏi vận hành trước, chọn lệnh phù hợp, rồi kiểm tra output và tác động phụ trước khi áp dụng trên server thật.

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `ip a` | Hiển thị giao diện (interface / 인터페이스), IP, trạng thái (state / 상태). | `ip a` | `ip` thay thế `ifconfig` trên Linux hiện đại. |
| `ip route` | Hiển thị routing bảng (table / 테이블). | `ip route` | Check default gateway khi máy chủ (server / 서버) ra ngoài không được. |
| `hostname -I` | In các IP của host. | `hostname -I` | Nhanh nhưng có thể trả nhiều IP/bộ chứa (container / 컨테이너) giao diện (interface / 인터페이스). |
| `ping host` | Gửi ICMP echo yêu cầu (request / 요청) để kiểm thử (test / 테스트) reachability/độ trễ (latency / 지연 시간). | `ping -c 4 8.8.8.8` | Ping thất bại (fail / 실패) không chắc host chết vì firewall có thể khối (block / 블록) ICMP. |
| `ping -c 4 host` | `-c` giới hạn packet count rồi tự dừng. | `ping -c 4 google.com` | Phù hợp script/diagnostic ngắn. |
| `curl URL` | HTTP(S) máy khách (client / 클라이언트); mặc định in phản hồi (response / 응답) body. | `curl http://localhost:8080/health` | Một trong lệnh quan trọng nhất để kiểm thử (test / 테스트) app/backend. |
| `curl -I URL` | `-I` gửi HEAD và chỉ hiển thị phản hồi (response / 응답) headers. | `curl -I https://example.com` | Không phải máy chủ (server / 서버) nào cũng xử lý HEAD giống GET. |
| `curl -v URL` | Verbose: DNS/connect/TLS/yêu cầu (request / 요청)/phản hồi (response / 응답) headers. | `curl -v https://api.example.com` | gỡ lỗi (debug / 디버그) proxy/TLS/header cực hữu ích. |
| `curl -sS URL` | `-s` silent progress, `-S` vẫn show lỗi (error / 오류). | `curl -sS http://localhost:8080/health` | Tốt trong script. |
| `curl -f URL` | thất bại (fail / 실패) với HTTP 4xx/5xx bằng non-zero exit mã (code / 코드). | `curl -fsS http://localhost:8080/health` | Chuẩn health-check script: `curl -fsS`. |
| `curl -L URL` | Follow redirect 3xx. | `curl -L https://example.com/login` | Nếu chỉ `curl` thấy 301/302 mà trình duyệt (browser / 브라우저) chạy được, thử `-L`. |
| `curl -k URL` | Bỏ verify TLS certificate. | `curl -k https://localhost:8443` | Chỉ dùng gỡ lỗi (debug / 디버그); không phải fix cho cert lỗi. |
| `curl --connect-timeout 5` | Giới hạn thời gian connect. | `curl --connect-timeout 5 -fsS http://10.0.0.10:8080` | Tránh script treo lâu khi endpoint unreachable. |
| `wget URL` | Download tệp (file / 파일) qua HTTP/HTTPS. | `wget https://example.com/app.tar.gz` | `wget -c` resume download. |
| `ss -lntp` | `-l` listening, `-n` numeric, `-t` TCP, `-p` tiến trình (process / 프로세스). | `sudo ss -lntp` | Thay thế `netstat`; command chuẩn để check listening cổng (port / 포트). |
| `ss -lunp` | Listening UDP + tiến trình (process / 프로세스). | `sudo ss -lunp` | DNS thường UDP/53. |
| `ss -antp` | Tất cả TCP socket, numeric, tiến trình (process / 프로세스). | `sudo ss -antp | grep ':8080'` | Có thể xem ESTAB/TIME-WAIT/CLOSE-WAIT. |
| `lsof -i :8080` | Liệt kê tiến trình (process / 프로세스)/tệp (file / 파일) descriptor liên quan cổng (port / 포트) 8080. | `sudo lsof -nP -iTCP:8080 -sTCP:LISTEN` | `-nP` tránh DNS/service-name lookup, đầu ra (output / 출력) nhanh và rõ cổng (port / 포트) số. |
| `nc -vz host port` | Netcat: `-v` verbose, `-z` chỉ scan/connect không gửi dữ liệu (data / 데이터). | `nc -vz 10.0.0.10 8080` | Check TCP reachability nhanh hơn HTTP nếu app giao thức (protocol / 프로토콜) khác. |
| `traceroute host` | Hiển thị hops trên đường tuyến (route / 경로). | `traceroute 8.8.8.8` | Có thể bị firewall/filter nên không phải hop nào cũng trả lời. |
| `dig domain` | DNS truy vấn (query / 쿼리) chi tiết. | `dig example.com A` | `dig +short example.com` cho đầu ra (output / 출력) gọn. |
| `nslookup domain` | DNS lookup interactive/simple. | `nslookup example.com` | `dig` thường mạnh hơn nhưng `nslookup` phổ biến. |

---

# 16. Archive / Compress

Đây là mục tra cứu thao tác. Hãy đọc câu hỏi vận hành trước, chọn lệnh phù hợp, rồi kiểm tra output và tác động phụ trước khi áp dụng trên server thật.

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `tar -cvf x.tar dir/` | `c` create, `v` verbose, `f` archive filename. Không compress. | `tar -cvf backup.tar config/` | `v` có thể quá nhiều đầu ra (output / 출력) với archive lớn. |
| `tar -xvf x.tar` | `x` extract, `v` verbose, `f` tệp (file / 파일). | `tar -xvf backup.tar` | Dùng `-C /dest` để extract vào destination cụ thể. |
| `tar -czvf x.tar.gz dir/` | `z` dùng gzip compression. | `tar -czvf app-backup.tar.gz /opt/app/config` | Backup cấu hình (config / 설정)/log nhỏ rất phổ biến. |
| `tar -xzvf x.tar.gz` | Extract gzip-compressed tar. | `tar -xzvf app.tar.gz -C /opt/app` | Nên `tar -tzf` xem content trước nếu nguồn không quen. |
| `tar -tzf x.tar.gz` | `t` danh sách (list / 목록) content, không extract. | `tar -tzf app.tar.gz | less` | rà soát (review / 검토) đường dẫn (path / 경로) để tránh extract ghi đè bất ngờ. |
| `gzip file` | Compress thành `file.gz` và mặc định xoá tệp (file / 파일) gốc. | `gzip old.log` | `gzip -k` giữ tệp (file / 파일) gốc nếu hiện thực (implementation / 구현) hỗ trợ. |
| `gunzip file.gz` | Decompress gzip. | `gunzip app.log.gz` | Với log chỉ cần đọc, dùng `zless/zgrep` để khỏi extract. |
| `zip -r x.zip dir/` | `-r` recursive zip directory. | `zip -r config.zip config/` | Zip tiện cross-platform nhưng tar.gz phổ biến hơn trên Linux. |
| `unzip x.zip` | Extract zip. | `unzip app.zip -d /tmp/app` | `-l` để danh sách (list / 목록) trước. |

---

# 17. SSH

Đây là mục tra cứu thao tác. Hãy đọc câu hỏi vận hành trước, chọn lệnh phù hợp, rồi kiểm tra output và tác động phụ trước khi áp dụng trên server thật.

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `ssh user@host` | Mở encrypted remote shell qua SSH cổng (port / 포트) mặc định 22. | `ssh app@10.0.0.10` | Verify host key fingerprint khi connect lần đầu. |
| `ssh -p PORT` | `-p` chỉ custom SSH cổng (port / 포트). | `ssh -p 2222 app@10.0.0.10` | SSH dùng lowercase `-p`; SCP dùng uppercase `-P`. |
| `ssh -i KEY` | Chỉ private key định danh (identity / 식별자) tệp (file / 파일). | `ssh -i ~/.ssh/prod.pem ubuntu@server` | Private key nên `chmod 600`. |
| `ssh -v` | Verbose liên kết (connection / 연결)/auth debugging. | `ssh -v user@host` | Thấy key nào được thử, auth phương thức (method / 메서드), cấu hình (config / 설정) áp dụng. |
| `ssh -vvv` | gỡ lỗi (debug / 디버그) tối đa hơn. | `ssh -vvv user@host` | Dùng khi auth/proxy/jump host lỗi khó hiểu. |
| `ssh -J jump target` | ProxyJump qua bastion/jump host. | `ssh -J user@bastion app@10.0.1.20` | cấp cao (senior / 시니어) thường cấu hình trong `~/.ssh/config` để gõ ngắn. |
| `ssh -L local:host:port` | cục bộ (local / 로컬) cổng (port / 포트) forwarding. | `ssh -L 15432:db.internal:5432 user@bastion` | Sau đó cục bộ (local / 로컬) app connect `localhost:15432` tới DB nội bộ. |
| `ssh -N` | Không chạy remote command, chỉ giữ liên kết (connection / 연결)/forward. | `ssh -N -L 8081:localhost:8080 user@server` | Chuẩn khi chỉ tạo tunnel. |
| `ssh -o ServerAliveInterval=60` | Gửi keepalive mỗi 60s. | `ssh -o ServerAliveInterval=60 user@host` | Giảm session chết do NAT/firewall idle hết thời gian chờ (timeout / 타임아웃). |
| `exit` | Thoát remote shell/session. | `exit` | `Ctrl+D` gửi EOF và thường cũng logout. |

---

# 18. SCP / rsync

Đây là mục tra cứu thao tác. Hãy đọc câu hỏi vận hành trước, chọn lệnh phù hợp, rồi kiểm tra output và tác động phụ trước khi áp dụng trên server thật.

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `scp file user@host:/path/` | bản sao (copy / 복사) cục bộ (local / 로컬) tệp (file / 파일) lên remote qua SSH. | `scp app.jar app@server:/tmp/` | Với tệp (file / 파일) lớn/đồng bộ lặp lại, `rsync` thường tốt hơn. |
| `scp user@host:/path/file .` | bản sao (copy / 복사) remote tệp (file / 파일) về hiện tại (current / 현재) cục bộ (local / 로컬) dir. | `scp app@server:/var/log/app.log .` | Có thể dùng wildcard nhưng nhớ shell expansion/quote. |
| `scp -r dir user@host:/path/` | Recursive directory bản sao (copy / 복사). | `scp -r config app@server:/tmp/` | Không tối ưu incremental như rsync. |
| `scp -P 2222` | Uppercase `-P` đặt SSH cổng (port / 포트). | `scp -P 2222 app.jar user@host:/tmp/` | Khác `ssh -p`. |
| `rsync -av src/ dst/` | `-a` archive preserve siêu dữ liệu (metadata / 메타데이터); `-v` verbose. | `rsync -av ./config/ app@server:/opt/app/config/` | Dấu `/` cuối nguồn (source / 소스) rất quan trọng: `src/` = content, `src` = cả folder. |
| `rsync -z` | Compress dữ liệu (data / 데이터) qua mạng (network / 네트워크). | `rsync -avz ./build/ app@server:/tmp/build/` | Trên LAN/tệp (file / 파일) đã compressed có thể không lợi nhiều. |
| `rsync --progress` | Hiển thị tiến trình từng tệp (file / 파일). | `rsync -av --progress big.tar app@server:/tmp/` | `--info=progress2` cho tổng progress trên rsync mới. |
| `rsync --delete` | Xoá destination tệp (file / 파일) không còn ở nguồn (source / 소스) để mirror. | `rsync -av --delete ./site/ server:/var/www/site/` | Rất nguy hiểm; luôn dry-run trước. |
| `rsync -n` / `--dry-run` | Chỉ mô phỏng thay đổi, không thực hiện. | `rsync -avhn --delete ./site/ server:/var/www/site/` | cấp cao (senior / 시니어) gần như luôn dry-run trước `--delete`. |
| `rsync -e "ssh -p 2222"` | Chỉ custom SSH vận chuyển (transport / 전송)/options. | `rsync -av -e "ssh -p 2222" ./app/ user@host:/opt/app/` | Có thể thêm định danh (identity / 식별자) key trong chuỗi ssh. |

---

# 19. văn bản (text / 텍스트) processing — wc / sort / cut / awk / sed

Đây là mục tra cứu thao tác. Hãy đọc câu hỏi vận hành trước, chọn lệnh phù hợp, rồi kiểm tra output và tác động phụ trước khi áp dụng trên server thật.

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `wc -l file` | Đếm số line. | `wc -l app.log` | chuỗi xử lý (pipeline / 파이프라인): `grep ERROR app.log | wc -l`. |
| `wc -w file` | Đếm word. | `wc -w notes.txt` | Ít dùng hơn trên máy chủ (server / 서버) ops. |
| `sort file` | Sort lexical ascending. | `sort users.txt` | Thường pipe với `uniq`. |
| `sort -n` | Numeric sort. | `sort -n numbers.txt` | Không bị `"100"` đứng trước `"20"` như lexical. |
| `sort -r` | Reverse descending. | `sort -r names.txt` | Kết hợp `-n`/`-h`. |
| `sort -h` | Human numeric sort, hiểu K/M/G. | `du -sh * | sort -h` | Rất hữu ích cho disk usage. |
| `sort -u` | Sort và unique. | `sort -u ips.txt` | Tương tự `sort | uniq`. |
| `uniq -c` | Count số dòng trùng liên tiếp; thường phải sort trước. | `sort ips.txt | uniq -c | sort -nr` | Classic để tìm IP/yêu cầu (request / 요청) xuất hiện nhiều nhất. |
| `cut -d',' -f1` | `-d` delimiter, `-f` trường dữ liệu (field / 필드) chỉ mục (index / 인덱스). | `cut -d',' -f1 users.csv` | Với CSV có quoted comma phức tạp, `cut` không phải parser đúng. |
| `awk '{print $1}'` | In trường dữ liệu (field / 필드) 1; awk mặc định split whitespace. | `ps -ef | awk '{print $2}'` | awk mạnh cho filter/aggregate column. |
| `awk -F,` | Chỉ trường dữ liệu (field / 필드) separator. | `awk -F, '{print $1,$3}' file.csv` | `BEGIN{FS=","}` tương đương kiểu script. |
| `sed 's/old/new/'` | Replace occurrence đầu tiên mỗi dòng trên stdout. | `sed 's/http:/https:/' app.conf` | Mặc định không sửa tệp (file / 파일) gốc. |
| `sed 's/old/new/g'` | `g` replace mọi occurrence trên mỗi dòng. | `sed 's/foo/bar/g' file.txt` | rà soát (review / 검토) đầu ra (output / 출력) trước khi dùng `-i`. |
| `sed -i` | Edit tệp (file / 파일) in-place. | `sed -i 's/foo/bar/g' app.conf` | Trên môi trường vận hành (production / 운영 환경) nên backup: `sed -i.bak ...` nếu hiện thực (implementation / 구현) hỗ trợ. |

### Cấp cao (senior / 시니어) log analytics bằng awk

Top status mã (code / 코드):

```bash
awk '{print $9}' access.log | sort | uniq -c | sort -nr | head
```

Top máy khách (client / 클라이언트) IP:

```bash
awk '{print $1}' access.log | sort | uniq -c | sort -nr | head -20
```

---

# 20. Pipe / Redirect

Đây là mục tra cứu thao tác. Hãy đọc câu hỏi vận hành trước, chọn lệnh phù hợp, rồi kiểm tra output và tác động phụ trước khi áp dụng trên server thật.

| Syntax | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `cmd1 \| cmd2` | Pipe stdout của cmd1 thành stdin của cmd2. | `ps -ef | grep java` | Đây là nền tảng để ghép Linux commands nhỏ thành workflow mạnh. |
| `>` | Redirect stdout và **ghi đè** tệp (file / 파일). | `echo "hello" > test.txt` | Cẩn thận với cấu hình (config / 설정)/log quan trọng. |
| `>>` | Append stdout vào cuối tệp (file / 파일). | `echo "hello" >> test.txt` | Rất hay dùng ghi log thủ công/script. |
| `< file` | Lấy stdin từ tệp (file / 파일). | `wc -l < app.log` | đầu ra (output / 출력) chỉ là số, không kèm filename. |
| `2>` | Redirect stderr. tệp (file / 파일) descriptor 2 = stderr. | `find / -name app.log 2>errors.txt` | Hữu ích tách lỗi permission. |
| `2>/dev/null` | Bỏ stderr. | `find / -name app.log 2>/dev/null` | Đừng lạm dụng khi đang gỡ lỗi (debug / 디버그) vì sẽ che lỗi quan trọng. |
| `2>&1` | Redirect stderr tới cùng destination hiện tại của stdout. | `java -jar app.jar > app.log 2>&1` | Thứ tự redirect quan trọng. |
| `&>` | Bash shorthand redirect stdout+stderr. | `command &> output.log` | `>file 2>&1` portable hơn. |
| `tee file` | bản sao (copy / 복사) stdin vừa ra terminal vừa ghi tệp (file / 파일). | `curl -v URL 2>&1 | tee curl-debug.log` | Rất hữu ích khi vừa muốn xem vừa lưu bằng chứng sự cố (incident / 인시던트). |
| `tee -a file` | Append thay vì overwrite. | `echo test | tee -a run.log` | Với gốc (root / 루트) tệp (file / 파일): `echo x | sudo tee /etc/file`. |

---

# 21. lịch sử (history / 이력) / Shell shortcuts

Đây là mục tra cứu thao tác. Hãy đọc câu hỏi vận hành trước, chọn lệnh phù hợp, rồi kiểm tra output và tác động phụ trước khi áp dụng trên server thật.

| Command / Key | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `history` | Hiển thị command lịch sử (history / 이력) của shell. | `history | tail -50` | Có thể chứa sensitive command; tránh gõ password/đơn vị từ (token / 토큰) trực tiếp vào command line. |
| `history | grep text` | tìm kiếm (search / 검색) command đã dùng. | `history | grep ssh` | Nhanh để lấy lại command dài. |
| `!!` | Chạy lại command ngay trước đó. | `sudo !!` | Classic: quên sudo → `sudo !!`. |
| `!123` | Chạy lại lịch sử (history / 이력) entry 123. | `!123` | rà soát (review / 검토) `history` trước tránh chạy nhầm destructive command. |
| `Ctrl+R` | Reverse incremental tìm kiếm (search / 검색) lịch sử (history / 이력). | `Ctrl+R`, gõ `journalctl` | Một trong keyboard shortcut tăng tốc nhất. |
| `Ctrl+A` | Đưa cursor về đầu command line. | `Ctrl+A` | Giống Home trong readline. |
| `Ctrl+E` | Đưa cursor về cuối line. | `Ctrl+E` | Giống End. |
| `Ctrl+U` | Xoá từ cursor về đầu line. | `Ctrl+U` | Nhanh hơn giữ Backspace. |
| `Ctrl+K` | Xoá từ cursor đến cuối line. | `Ctrl+K` | Dùng sửa suffix command dài. |
| `Ctrl+W` | Xoá word phía trước. | `Ctrl+W` | Command-line editing quan trọng. |
| `Ctrl+L` | Clear terminal screen. | `Ctrl+L` | Không xoá lịch sử (history / 이력). |
| `Tab` | Auto-complete đường dẫn (path / 경로)/command nếu shell hỗ trợ. | `cd /var/lo<Tab>` | Nhấn Tab 2 lần để xem candidates. |

---

# 22. môi trường (environment / 환경) variables

Đây là mục tra cứu thao tác. Hãy đọc câu hỏi vận hành trước, chọn lệnh phù hợp, rồi kiểm tra output và tác động phụ trước khi áp dụng trên server thật.

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `env` | In môi trường (environment / 환경) của tiến trình (process / 프로세스) shell hiện tại. | `env | sort` | Có thể chứa secret/đơn vị từ (token / 토큰); cẩn thận khi paste log. |
| `printenv VAR` | In môi trường (environment / 환경) variable cụ thể. | `printenv JAVA_HOME` | Gọn hơn `env | grep`. |
| `echo "$PATH"` | Expand và in shell variable đường dẫn (path / 경로). | `echo "$PATH" | tr ':' '\n'` | Tách đường dẫn (path / 경로) từng dòng để gỡ lỗi (debug / 디버그) executable priority. |
| `export KEY=value` | Set và export biến cho child processes của hiện tại (current / 현재) shell. | `export JAVA_HOME=/usr/lib/jvm/java-17` | Chỉ tồn tại trong session nếu không ghi vào profile/dịch vụ (service / 서비스) cấu hình (config / 설정). |
| `unset KEY` | Xoá shell variable/môi trường (environment / 환경) variable. | `unset HTTP_PROXY` | Hữu ích khi proxy làm curl/app đi sai đường. |
| `source file` | Chạy tệp (file / 파일) trong **hiện tại (current / 현재) shell** để thay đổi môi trường (environment / 환경) hiện tại. | `source ~/.bashrc` | Khác `bash file` vì child shell không cập nhật parent shell. |
| `env KEY=value cmd` | Set variable chỉ cho một command. | `env JAVA_HOME=/opt/jdk21 ./run.sh` | cấp cao (senior / 시니어) dùng để kiểm thử (test / 테스트) không làm bẩn session môi trường (environment / 환경). |

---

# 23. Java / JVM máy chủ (server / 서버)

Đây là mục tra cứu thao tác. Hãy đọc câu hỏi vận hành trước, chọn lệnh phù hợp, rồi kiểm tra output và tác động phụ trước khi áp dụng trên server thật.

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `java -version` | Hiển thị thời gian chạy (runtime / 런타임) Java đang được gọi qua đường dẫn (path / 경로). | `java -version` | Check cả `which java` và `readlink -f $(which java)` nếu phiên bản (version / 버전) bất ngờ. |
| `which java` | đường dẫn (path / 경로) executable được shell resolve. | `which java` | Có thể là symlink. |
| `readlink -f $(which java)` | Resolve symlink tới nhị phân (binary / 이진) thật. | `readlink -f "$(command -v java)"` | Tìm chính xác JDK installation đang chạy. |
| `jar tf app.jar` | `t` danh sách (list / 목록) archive bảng (table / 테이블), `f` jar tệp (file / 파일). | `jar tf app.jar | less` | Kiểm tra lớp (class / 클래스)/tài nguyên (resource / 자원) có nằm trong sản phẩm tạo ra (artifact / 산출물) hay không. |
| `java -jar app.jar` | Chạy executable JAR có Main-Class/launcher phù hợp. | `java -jar app.jar` | môi trường vận hành (production / 운영 환경) nên cấu hình vùng nhớ động (heap / 힙)/GC/logging rõ ràng. |
| `jps -lv` | Liệt kê JVM tiến trình (process / 프로세스) có attach cơ chế (mechanism / 메커니즘), kèm args. | `jps -lv` | Không phải JVM nào cũng hiện nếu người dùng (user / 사용자)/permission khác. |
| `jstack PID` | luồng thực thi (thread / 스레드) dump JVM. | `jstack 12345 > /tmp/jstack.$(date +%s).txt` | Khi app treo/high CPU, lấy 2-3 dump cách nhau vài giây để so luồng thực thi (thread / 스레드). |
| `jcmd PID VM.command_line` | In JVM command line. | `jcmd 12345 VM.command_line` | `jcmd` hiện đại và đa năng hơn nhiều công cụ (tool / 도구) JDK cũ. |
| `jcmd PID VM.flags` | JVM flags thực tế. | `jcmd 12345 VM.flags` | Check vùng nhớ động (heap / 힙)/GC options thực sự đang áp dụng. |
| `jcmd PID GC.heap_info` | vùng nhớ động (heap / 힙) summary. | `jcmd 12345 GC.heap_info` | Nhẹ hơn vùng nhớ động (heap / 힙) dump; phù hợp kiểm tra nhanh. |
| `jcmd PID Thread.print` | luồng thực thi (thread / 스레드) dump qua jcmd. | `jcmd 12345 Thread.print > /tmp/thread.txt` | Có thể dùng thay `jstack`. |
| `jcmd PID GC.class_histogram` | Histogram lớp (class / 클래스)/đối tượng (object / 객체) count. | `jcmd 12345 GC.class_histogram | head -50` | Có overhead; dùng thận trọng môi trường vận hành (production / 운영 환경) tải cao. |

---

# 24. trình quản lý gói (package manager / 패키지 관리자)

Đây là mục tra cứu thao tác. Hãy đọc câu hỏi vận hành trước, chọn lệnh phù hợp, rồi kiểm tra output và tác động phụ trước khi áp dụng trên server thật.

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `apt update` | Refresh gói (package / 패키지) chỉ mục (index / 인덱스), không upgrade gói (package / 패키지). | `sudo apt update` | Nên chạy trước `apt install` trên Ubuntu/Debian nếu siêu dữ liệu (metadata / 메타데이터) cũ. |
| `apt upgrade` | Upgrade gói (package / 패키지) có thể upgrade mà không remove gói (package / 패키지) cần thiết theo apt rules. | `sudo apt upgrade` | môi trường vận hành (production / 운영 환경) cần thay đổi (change / 변경) cửa sổ (window / 윈도우); không upgrade bừa. |
| `apt install pkg` | Install gói (package / 패키지). | `sudo apt install tree` | Có thể `apt-cache policy pkg` xem candidate/nguồn (source / 소스) trước. |
| `apt remove pkg` | Remove gói (package / 패키지) nhưng thường giữ cấu hình (config / 설정). | `sudo apt remove nginx` | `purge` mới xoá gói (package / 패키지) cấu hình (config / 설정) managed. |
| `apt purge pkg` | Remove gói (package / 패키지) + cấu hình (config / 설정) files do trình quản lý gói (package manager / 패키지 관리자) quản lý. | `sudo apt purge nginx` | Không có nghĩa xoá toàn dữ liệu (data / 데이터) app. |
| `dnf install pkg` | Install trên RHEL/Fedora/newer enterprise distros. | `sudo dnf install lsof` | RHEL 8/9 thường dùng dnf; `yum` có thể là tính tương thích (compatibility / 호환성) wrapper. |
| `dnf history` | Xem giao dịch (transaction / 트랜잭션) lịch sử (history / 이력). | `sudo dnf history` | Rất hữu ích biết gói (package / 패키지) nào vừa được đổi. |
| `rpm -qa` | danh sách (list / 목록) RPM packages. | `rpm -qa | grep java` | Dùng kiểm tra (audit / 감사) installed gói (package / 패키지) trên RHEL family. |

---

# 25. Date / thời gian (time / 시간)

Đây là mục tra cứu thao tác. Hãy đọc câu hỏi vận hành trước, chọn lệnh phù hợp, rồi kiểm tra output và tác động phụ trước khi áp dụng trên server thật.

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `date` | In máy chủ (server / 서버) cục bộ (local / 로컬) date/thời gian (time / 시간). | `date` | Luôn check timezone khi đối chiếu log giữa nhiều hệ thống (system / 시스템). |
| `date "+%Y-%m-%d %H:%M:%S"` | Custom đầu ra (output / 출력) format. | `date "+%Y-%m-%d %H:%M:%S %Z"` | Hay dùng tạo timestamp backup filename. |
| `date -u` | In UTC. | `date -u` | API/cloud logs thường dùng UTC. |
| `timedatectl` | Timezone/NTP/hệ thống (system / 시스템) clock trạng thái (state / 상태). | `timedatectl status` | Nếu `System clock synchronized: no`, auth/đơn vị từ (token / 토큰) có thể lỗi theo thời gian (time / 시간). |
| `find . -newermt` | Tìm tệp (file / 파일) modified sau mốc thời gian. | `find . -type f -newermt "2026-09-07 18:00"` | Dễ hiểu hơn `mtime` khi sự cố (incident / 인시던트) có timestamp cụ thể. |

---

# 26. Cron

Đây là mục tra cứu thao tác. Hãy đọc câu hỏi vận hành trước, chọn lệnh phù hợp, rồi kiểm tra output và tác động phụ trước khi áp dụng trên server thật.

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `crontab -l` | danh sách (list / 목록) cron entries của người dùng (user / 사용자) hiện tại. | `crontab -l` | gốc (root / 루트)/người dùng (user / 사용자) khác có crontab khác nhau. |
| `crontab -e` | Edit người dùng (user / 사용자) crontab bằng editor mặc định. | `crontab -e` | Cron môi trường (environment / 환경) đường dẫn (path / 경로) rất tối giản; dùng absolute đường dẫn (path / 경로) trong command. |
| `sudo crontab -l -u user` | Xem crontab người dùng (user / 사용자) khác. | `sudo crontab -l -u app` | Khi job “không chạy”, check đúng người dùng (user / 사용자) trước. |
| `0 2 * * * cmd` | Chạy mỗi ngày 02:00. | `0 2 * * * /opt/scripts/backup.sh >> /var/log/backup.log 2>&1` | Luôn redirect đầu ra (output / 출력) và dùng đường dẫn (path / 경로) tuyệt đối để gỡ lỗi (debug / 디버그) cron. |
| `*/5 * * * * cmd` | Chạy mỗi 5 phút. | `*/5 * * * * /opt/check.sh` | Tránh job nặng chạy chồng; cân nhắc khóa (lock / 잠금)/flock. |
| `flock` | Prevent concurrent cron run bằng tệp (file / 파일) khóa (lock / 잠금). | `*/5 * * * * flock -n /tmp/job.lock /opt/job.sh` | cấp cao (senior / 시니어) tip quan trọng cho cron tác vụ (task / 작업) có thể chạy lâu. |

---

# 27. Open files / tệp (file / 파일) descriptors

Đây là mục tra cứu thao tác. Hãy đọc câu hỏi vận hành trước, chọn lệnh phù hợp, rồi kiểm tra output và tác động phụ trước khi áp dụng trên server thật.

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `lsof` | danh sách (list / 목록) open files; Linux coi socket/thiết bị (device / 장치) cũng là file-like đối tượng (object / 객체). | `sudo lsof | head` | đầu ra (output / 출력) rất lớn; nên filter. |
| `lsof /path/file` | tiến trình (process / 프로세스) nào đang mở tệp (file / 파일). | `sudo lsof /var/log/app.log` | Biết tiến trình (process / 프로세스) giữ tệp (file / 파일) khi không delete/move được như mong đợi. |
| `lsof -i :PORT` | tiến trình (process / 프로세스) có socket trên cổng (port / 포트). | `sudo lsof -nP -i :8080` | `-nP` tránh name resolution làm chậm. |
| `lsof +L1` | tệp (file / 파일) link count <1, thường là deleted nhưng vẫn open. | `sudo lsof +L1` | Giải thích trường hợp `df` đầy nhưng tệp (file / 파일) đã “xoá”. |
| `ls /proc/PID/fd` | Liệt kê tệp (file / 파일) descriptors của tiến trình (process / 프로세스). | `ls -l /proc/12345/fd | head` | cấp cao (senior / 시니어) Linux debugging: `/proc` cung cấp rất nhiều thời gian chạy (runtime / 런타임) info. |
| `cat /proc/PID/limits` | tài nguyên (resource / 자원) limits của tiến trình (process / 프로세스). | `cat /proc/12345/limits` | Check `Max open files` khi gặp “Too many open files”. |

---

# 28. xargs

Đây là mục tra cứu thao tác. Hãy đọc câu hỏi vận hành trước, chọn lệnh phù hợp, rồi kiểm tra output và tác động phụ trước khi áp dụng trên server thật.

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `xargs cmd` | Chuyển stdin thành arguments cho command. | `printf '%s\n' a b | xargs echo` | Hữu ích khi command không đọc stdin trực tiếp. |
| `xargs -0` | đầu vào (input / 입력) được phân cách bằng NUL, an toàn với không gian (space / 공간)/newline trong filename. | `find . -type f -print0 | xargs -0 grep -n "ERROR"` | Pair chuẩn với `find -print0`. |
| `xargs -n N` | Giới hạn N arguments mỗi invocation. | `seq 1 10 | xargs -n 2 echo` | Hữu ích batch tiến trình (process / 프로세스). |
| `xargs -P N` | Chạy tối đa N tiến trình (process / 프로세스) song song. | `cat hosts.txt | xargs -n1 -P4 ping -c1` | Có thể tăng tải mạnh; dùng cẩn thận môi trường vận hành (production / 운영 환경). |

---

# 29. Compare / checksum

Đây là mục tra cứu thao tác. Hãy đọc câu hỏi vận hành trước, chọn lệnh phù hợp, rồi kiểm tra output và tác động phụ trước khi áp dụng trên server thật.

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `diff file1 file2` | So sánh văn bản (text / 텍스트) line-by-line. | `diff old.conf new.conf` | Exit mã (code / 코드) 0=same, 1=different, >1=lỗi (error / 오류). |
| `diff -u` | Unified diff có ngữ cảnh (context / 맥락), dễ đọc và dùng trong patch/rà soát (review / 검토). | `diff -u app.conf.bak app.conf` | Đây là format quen thuộc của Git diff. |
| `cmp file1 file2` | So sánh byte-level, dừng tại khác biệt đầu. | `cmp app.jar app2.jar` | Nhanh check nhị phân (binary / 이진) identical hay không. |
| `md5sum file` | Tính MD5 checksum. | `md5sum app.jar` | Không dùng MD5 cho bảo mật (security / 보안); dùng để compare integrity cơ bản. |
| `sha256sum file` | Tính SHA-256. | `sha256sum app.jar` | Phù hợp verify sản phẩm tạo ra (artifact / 산출물) checksum. |

---

# 30. Encoding / nhị phân (binary / 이진) inspection

Đây là mục tra cứu thao tác. Hãy đọc câu hỏi vận hành trước, chọn lệnh phù hợp, rồi kiểm tra output và tác động phụ trước khi áp dụng trên server thật.

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `file file` | Guess tệp (file / 파일) kiểu (type / 타입). | `file script.sh` | Có thể báo “with CRLF line terminators” khi script Windows lỗi trên Linux. |
| `file -i file` | In MIME kiểu (type / 타입) và charset estimate. | `file -i data.csv` | Giúp gỡ lỗi (debug / 디버그) UTF-8/EUC-KR/other encoding. |
| `xxd file` | Hex dump. | `xxd app.dat | head` | Nhìn BOM/header/magic bytes. |
| `hexdump -C file` | chuẩn gốc (canonical / 정본) hex + ASCII. | `hexdump -C file.bin | head` | Tốt để tìm hidden CRLF/điều khiển (control / 제어) chars. |
| `od -c file` | Character dump, escape non-printing chars. | `od -c script.sh | head` | gỡ lỗi (debug / 디버그) `\r` trong shell script. |

---

# 31. Advanced tiến trình (process / 프로세스) / hiệu năng (performance / 성능)

Đây là mục tra cứu thao tác. Hãy đọc câu hỏi vận hành trước, chọn lệnh phù hợp, rồi kiểm tra output và tác động phụ trước khi áp dụng trên server thật.

| Command | Ý nghĩa / Option | Ví dụ | Thực tế / Senior tips |
|---|---|---|---|
| `ps -p PID -o ...` | Custom tiến trình (process / 프로세스) columns. | `ps -p 12345 -o pid,ppid,nlwp,%cpu,%mem,rss,vsz,etime,cmd` | `nlwp` = luồng thực thi (thread / 스레드) count. |
| `pidstat -p PID 1` | CPU stats tiến trình (process / 프로세스) theo interval 1s. | `pidstat -p 12345 1 10` | Cần sysstat; tốt hơn nhìn snapshot đơn lẻ. |
| `pidstat -t -p PID 1` | CPU per-thread. | `pidstat -t -p 12345 1` | Kết hợp Java luồng thực thi (thread / 스레드) dump để map high CPU luồng thực thi (thread / 스레드). |
| `vmstat 1` | System-level CPU/bộ nhớ (memory / 메모리)/io quick sampling. | `vmstat 1 10` | `wa` cao → nghi I/O wait; `si/so` → swap activity. |
| `iostat -xz 1` | Extended lưu trữ (storage / 저장소) thiết bị (device / 장치) stats. | `iostat -xz 1 10` | `await` cao có thể chỉ ra lưu trữ (storage / 저장소) độ trễ (latency / 지연 시간). |
| `sar -u 1 10` | CPU statistics bằng sysstat. | `sar -u 1 10` | `sar` có thể xem historical metrics nếu sysstat collection bật. |
| `dmesg -T` | Kernel ring buffer với human-readable timestamp. | `sudo dmesg -T | tail -100` | Check OOM killer, disk errors, NIC/kernel events. |
| `journalctl -k` | Kernel logs qua journal. | `journalctl -k --since today` | Thường dễ filter thời gian (time / 시간) hơn dmesg. |

---

# 32. mạng (network / 네트워크) troubleshooting luồng (flow / 흐름)

Đây là mục tra cứu thao tác. Hãy đọc câu hỏi vận hành trước, chọn lệnh phù hợp, rồi kiểm tra output và tác động phụ trước khi áp dụng trên server thật.

| Step | Command | Ví dụ | Senior note |
|---|---|---|---|
| DNS | `dig` | `dig +short api.example.com` | Nếu IP sai, chưa cần gỡ lỗi (debug / 디버그) app. |
| tuyến (route / 경로) | `ip route get IP` | `ip route get 10.0.0.10` | Cho biết giao diện (interface / 인터페이스)/gateway/nguồn (source / 소스) IP Linux sẽ dùng. |
| Reachability | `ping` | `ping -c 4 10.0.0.10` | Ping thất bại (fail / 실패) không kết luận TCP thất bại (fail / 실패). |
| TCP | `nc -vz` | `nc -vz 10.0.0.10 443` | Phân biệt mạng (network / 네트워크)/cổng (port / 포트) với HTTP lô-gic (logic / 논리). |
| TLS/HTTP | `curl -v` | `curl -vk https://host:443/health` | `-k` chỉ gỡ lỗi (debug / 디버그) cert; sau đó phải fix verify. |
| Listening cục bộ (local / 로컬) | `ss -lntp` | `sudo ss -lntp | grep ':8080'` | Nếu không listen cục bộ (local / 로컬) thì mạng (network / 네트워크) ngoài không phải nguyên nhân chính. |
| DNS detail | `dig` | `dig api.example.com` | Check TTL/CNAME/A/AAAA. |
| đường dẫn (path / 경로) | `traceroute` | `traceroute 10.0.0.10` | Có giới hạn vì firewall có thể drop probes. |

---

# 33. máy chủ (server / 서버) troubleshooting luồng (flow / 흐름)

Đây là mục tra cứu thao tác. Hãy đọc câu hỏi vận hành trước, chọn lệnh phù hợp, rồi kiểm tra output và tác động phụ trước khi áp dụng trên server thật.

| Step | Command | Ví dụ | Senior note |
|---|---|---|---|
| 1. dịch vụ (service / 서비스) trạng thái (state / 상태) | `systemctl status` | `systemctl status app` | Xem exit mã (code / 코드)/MainPID/recent logs. |
| 2. Recent logs | `journalctl -u` | `journalctl -u app -n 300 --no-pager` | Khoanh lỗi trước restart. |
| 3. tiến trình (process / 프로세스) | `pgrep -af` | `pgrep -af 'java.*app'` | Xác nhận tiến trình (process / 프로세스) thật sự tồn tại. |
| 4. cổng (port / 포트) | `ss` | `sudo ss -lntp | grep ':8080'` | tiến trình (process / 프로세스) sống chưa chắc app đã bind cổng (port / 포트). |
| 5. cục bộ (local / 로컬) health | `curl -fsS` | `curl -fsS -v http://127.0.0.1:8080/health` | Tách vấn đề app khỏi LB/firewall/DNS. |
| 6. tài nguyên (resource / 자원) | `free/df/top` | `free -h; df -h; top` | Check RAM/disk/CPU pressure. |
| 7. Kernel | `dmesg` | `dmesg -T | grep -i -E 'oom|killed|error'` | OOM killer có thể giết Java mà app log không kịp ghi. |
| 8. cấu hình (config / 설정) diff | `diff -u` | `diff -u app.conf.bak app.conf` | sự cố (incident / 인시던트) sau deploy thường do cấu hình (config / 설정)/sản phẩm tạo ra (artifact / 산출물) khác. |

---

# 34. Commands nên thuộc lòng

Đây là mục tra cứu thao tác. Hãy đọc câu hỏi vận hành trước, chọn lệnh phù hợp, rồi kiểm tra output và tác động phụ trước khi áp dụng trên server thật.

| Nhóm | Command | Ví dụ | Senior note |
|---|---|---|---|
| điều hướng (navigation / 내비게이션) | `pwd`, `ls -lah`, `cd`, `cd -` | `pwd && ls -lah` | Luôn biết ngữ cảnh (context / 맥락) trước khi thao tác. |
| tệp (file / 파일) | `cp -a`, `mv`, `rm`, `mkdir -p` | `cp -a app.conf app.conf.bak` | Backup trước edit. |
| View | `less`, `tail -n 500 -F` | `less +F app.log` | Dùng less cho tệp (file / 파일) lớn. |
| tìm kiếm (search / 검색) | `grep -Ein`, `find` | `grep -Ein -C5 "ERROR|Exception" app.log` | ngữ cảnh (context / 맥락) quanh lỗi quan trọng hơn từ khóa (keyword / 키워드) đơn. |
| tiến trình (process / 프로세스) | `pgrep -af`, `ps`, `top`, `kill` | `pgrep -af java` | Tránh `kill -9` như default. |
| cổng (port / 포트) | `ss`, `lsof` | `sudo ss -lntp | grep 8080` | `ss` là công cụ (tool / 도구) hiện đại. |
| HTTP | `curl -fsS -v` | `curl -fsS -v http://localhost:8080/health` | `-f` giúp script detect 4xx/5xx. |
| Disk | `df -h`, `du -xhd1`, `lsof +L1` | `du -xhd1 /var | sort -hr` | `lsof +L1` là kiến thức rất đáng nhớ. |
| dịch vụ (service / 서비스) | `systemctl`, `journalctl` | `journalctl -xeu app` | Pair chuẩn systemd gỡ lỗi (debug / 디버그). |
| SSH | `ssh`, `scp`, `rsync` | `ssh -J bastion app@private-host` | Jump host/tunnel là kỹ năng máy chủ (server / 서버) thực tế. |

---

# 35. Combo thực tế / cấp cao (senior / 시니어) thường dùng

### 35.1 Tìm đúng Java tiến trình (process / 프로세스), tránh grep tự match

Đây là mục tra cứu thao tác. Hãy đọc câu hỏi vận hành trước, chọn lệnh phù hợp, rồi kiểm tra output và tác động phụ trước khi áp dụng trên server thật.

```bash
pgrep -af 'java.*app-name'
```

Hoặc:

```bash
ps -ef | grep '[j]ava'
```

### 35.2 Xem tiến trình (process / 프로세스) nào listen cổng (port / 포트) 8080

Đây là mục tra cứu thao tác. Hãy đọc câu hỏi vận hành trước, chọn lệnh phù hợp, rồi kiểm tra output và tác động phụ trước khi áp dụng trên server thật.

```bash
sudo ss -lntp | grep ':8080'
```

Chi tiết hơn:

```bash
sudo lsof -nP -iTCP:8080 -sTCP:LISTEN
```

### 35.3 Xem 500 dòng gần nhất rồi realtime

Đây là mục tra cứu thao tác. Hãy đọc câu hỏi vận hành trước, chọn lệnh phù hợp, rồi kiểm tra output và tác động phụ trước khi áp dụng trên server thật.

```bash
tail -n 500 -F app.log
```

### 35.4 Follow log nhưng chỉ giữ lỗi

Đây là mục tra cứu thao tác. Hãy đọc câu hỏi vận hành trước, chọn lệnh phù hợp, rồi kiểm tra output và tác động phụ trước khi áp dụng trên server thật.

```bash
tail -F app.log | grep --line-buffered -E 'ERROR|Exception|Caused by|timeout'
```

### 35.5 tìm kiếm (search / 검색) lỗi (error / 오류) kèm 10 dòng ngữ cảnh (context / 맥락)

Đây là mục tra cứu thao tác. Hãy đọc câu hỏi vận hành trước, chọn lệnh phù hợp, rồi kiểm tra output và tác động phụ trước khi áp dụng trên server thật.

```bash
grep -Ein -C 10 'ERROR|WARN|Exception|Caused by' app.log
```

### 35.6 Tìm tệp (file / 파일) vừa bị thay đổi trong 30 phút

Đây là mục tra cứu thao tác. Hãy đọc câu hỏi vận hành trước, chọn lệnh phù hợp, rồi kiểm tra output và tác động phụ trước khi áp dụng trên server thật.

```bash
find /opt/app -type f -mmin -30 -ls
```

### 35.7 Tìm folder chiếm disk lớn nhất

Đây là mục tra cứu thao tác. Hãy đọc câu hỏi vận hành trước, chọn lệnh phù hợp, rồi kiểm tra output và tác động phụ trước khi áp dụng trên server thật.

```bash
sudo du -xhd1 /var 2>/dev/null | sort -hr
```

### 35.8 Khi `df -h` đầy nhưng `du` không thấy

Đây là mục tra cứu thao tác. Hãy đọc câu hỏi vận hành trước, chọn lệnh phù hợp, rồi kiểm tra output và tác động phụ trước khi áp dụng trên server thật.

```bash
sudo lsof +L1
```

### 35.9 kiểm thử (test / 테스트) app cục bộ (local / 로컬) trước khi đổ lỗi mạng (network / 네트워크)/LB

Đây là mục tra cứu thao tác. Hãy đọc câu hỏi vận hành trước, chọn lệnh phù hợp, rồi kiểm tra output và tác động phụ trước khi áp dụng trên server thật.

```bash
curl -fsS -v http://127.0.0.1:8080/health
```

### 35.10 Xem liên kết (connection / 연결) trạng thái (state / 상태) của cổng (port / 포트)

Đây là mục tra cứu thao tác. Hãy đọc câu hỏi vận hành trước, chọn lệnh phù hợp, rồi kiểm tra output và tác động phụ trước khi áp dụng trên server thật.

```bash
sudo ss -antp | grep ':8080'
```

Các trạng thái (state / 상태) quan trọng:

- `LISTEN`: máy chủ (server / 서버) đang listen.
- `ESTAB`: liên kết (connection / 연결) active.
- `TIME-WAIT`: liên kết (connection / 연결) đã close, kernel giữ tạm trạng thái (state / 상태).
- `CLOSE-WAIT`: peer đã đóng nhưng cục bộ (local / 로컬) tiến trình (process / 프로세스) chưa close socket; quá nhiều có thể liên quan mã (code / 코드)/tài nguyên (resource / 자원) leak.
- `SYN-SENT`: máy khách (client / 클라이언트) đã gửi SYN nhưng chưa nhận SYN-ACK.
- `SYN-RECV`: máy chủ (server / 서버) nhận SYN và đang chờ handshake hoàn tất.

### 35.11 Backup cấu hình (config / 설정) có timestamp trước sửa

Đây là mục tra cứu thao tác. Hãy đọc câu hỏi vận hành trước, chọn lệnh phù hợp, rồi kiểm tra output và tác động phụ trước khi áp dụng trên server thật.

```bash
cp -a application.yml "application.yml.$(date +%F_%H%M%S).bak"
```

### 35.12 Compare cấu hình (config / 설정) trước/sau

Đây là mục tra cứu thao tác. Hãy đọc câu hỏi vận hành trước, chọn lệnh phù hợp, rồi kiểm tra output và tác động phụ trước khi áp dụng trên server thật.

```bash
diff -u application.yml.bak application.yml
```

### 35.13 Validate nginx trước reload

Đây là mục tra cứu thao tác. Hãy đọc câu hỏi vận hành trước, chọn lệnh phù hợp, rồi kiểm tra output và tác động phụ trước khi áp dụng trên server thật.

```bash
sudo nginx -t && sudo systemctl reload nginx
```

### 35.14 Restart và xem log ngay

Đây là mục tra cứu thao tác. Hãy đọc câu hỏi vận hành trước, chọn lệnh phù hợp, rồi kiểm tra output và tác động phụ trước khi áp dụng trên server thật.

```bash
sudo systemctl restart app && sudo journalctl -u app -n 100 -f
```

### 35.15 Dry-run rsync trước khi mirror/delete

Đây là mục tra cứu thao tác. Hãy đọc câu hỏi vận hành trước, chọn lệnh phù hợp, rồi kiểm tra output và tác động phụ trước khi áp dụng trên server thật.

```bash
rsync -avhn --delete ./build/ app@server:/opt/app/
```

Nếu đầu ra (output / 출력) đúng mới chạy thật:

```bash
rsync -avh --delete ./build/ app@server:/opt/app/
```

### 35.16 Tìm tiến trình (process / 프로세스) high bộ nhớ (memory / 메모리)

Đây là mục tra cứu thao tác. Hãy đọc câu hỏi vận hành trước, chọn lệnh phù hợp, rồi kiểm tra output và tác động phụ trước khi áp dụng trên server thật.

```bash
ps aux --sort=-%mem | head -20
```

### 35.17 Tìm tiến trình (process / 프로세스) high CPU

Đây là mục tra cứu thao tác. Hãy đọc câu hỏi vận hành trước, chọn lệnh phù hợp, rồi kiểm tra output và tác động phụ trước khi áp dụng trên server thật.

```bash
ps aux --sort=-%cpu | head -20
```

### 35.18 Xem tài nguyên (resource / 자원) của một PID

Mục này dùng để kiểm tra resource mà một PID đang giữ. Hãy xác định PID đúng trước, rồi đối chiếu giới hạn, file mở và mức sử dụng với triệu chứng đang điều tra.

```bash
ps -p 12345 -o pid,ppid,user,%cpu,%mem,rss,vsz,nlwp,etime,lstart,cmd
```

### 35.19 Check tiến trình (process / 프로세스) tài nguyên (resource / 자원) limits

Resource limit giải thích vì sao một process có thể bị chặn dù host còn tài nguyên. Hãy đọc limit cùng workload và error log thay vì kết luận từ một con số đơn lẻ.

```bash
cat /proc/12345/limits
```

### 35.20 Check OOM killer

OOM killer là bằng chứng hệ thống đã không thể cấp phát memory theo yêu cầu. Kiểm tra log, cgroup và process bị chọn để phân biệt thiếu RAM, leak và giới hạn cấu hình.

```bash
sudo dmesg -T | grep -i -E 'out of memory|oom|killed process'
```

hoặc:

```bash
sudo journalctl -k | grep -i -E 'oom|killed process'
```

---

# 36. Shell operators cần hiểu

Các operator thay đổi cách shell nối lệnh, truyền stream và xử lý lỗi. Hãy đọc chúng theo exit status và thứ tự đánh giá trước khi ghép thành script production.

| Ký hiệu | Ý nghĩa | Ví dụ | Senior note |
|---|---|---|---|
| `.` | hiện tại (current / 현재) directory. | `find . -name "*.log"` | Trong shell `source file` cũng có thể viết `. file`. |
| `..` | Parent directory. | `cd ..` | Có thể chuỗi (chain / 사슬) `../../..`. |
| `~` | Home directory. | `cd ~/.ssh` | `~user` có thể chỉ home của người dùng (user / 사용자) khác. |
| `*` | Glob match 0+ ký tự. | `ls *.log` | Shell expand trước command; quote khi muốn mẫu (pattern / 패턴) tới `find/grep`. |
| `?` | Glob match đúng 1 ký tự. | `ls app?.log` | Không giống regex `?`. |
| `$VAR` | Variable expansion. | `echo "$HOME"` | Quote `"$VAR"` để tránh word splitting/globbing. |
| `$(cmd)` | Command substitution. | `echo "Now: $(date)"` | hiện đại (modern / 현대적) và dễ nest hơn backticks. |
| `'text'` | Single quote: gần như literal, không expand `$VAR`. | `echo '$HOME'` | đầu ra (output / 출력) literal `$HOME`. |
| `"text"` | Double quote: giữ whitespace nhưng vẫn expand variable/substitution. | `echo "$HOME"` | Default tốt khi dùng variable đường dẫn (path / 경로). |
| `\` | Escape ký tự đặc biệt hoặc line continuation. | `echo \$HOME` | Trong shell script dài dùng `\` nối dòng. |
| `;` | Chạy command sau bất kể trước success/thất bại (fail / 실패). | `date; hostname` | Khác `&&`. |
| `&&` | Chỉ chạy command sau nếu trước exit mã (code / 코드) 0. | `nginx -t && systemctl reload nginx` | mẫu (pattern / 패턴) môi trường vận hành (production / 운영 환경) an toàn. |
| `||` | Chỉ chạy command sau nếu trước thất bại (fail / 실패). | `curl -fsS URL || echo "health failed"` | Có thể dùng fallback/lỗi (error / 오류) handling. |
| `&` | Background tiến trình (process / 프로세스). | `sleep 100 &` | `$!` lấy PID gần nhất. |
| `|` | Pipe stdout. | `journalctl -u app | grep ERROR` | stderr không tự đi qua pipe trừ khi redirect. |

---

# 37. an toàn (safety / 안전) checklist môi trường vận hành (production / 운영 환경)

Checklist này là cổng kiểm tra trước thao tác có thể làm thay đổi server. Hãy xác định scope, backup, dry-run, rollback và bằng chứng sau lệnh trước khi thực thi.

| Trước khi... | Check | Ví dụ | Senior note |
|---|---|---|---|
| Xoá recursive | đường dẫn (path / 경로) + content | `pwd; ls -la "$DIR"` | Validate biến không rỗng trước `rm -rf`. |
| Restart dịch vụ (service / 서비스) | cấu hình (config / 설정) + impact | `nginx -t` | Nếu hỗ trợ reload thì không restart full. |
| Kill tiến trình (process / 프로세스) | PID + command | `ps -fp "$PID"` | PID có thể đã được reuse; verify command. |
| Chown/chmod recursive | cây (tree / 트리)/đường dẫn (path / 경로) | `find /opt/app -maxdepth 2 -ls | head` | Permission nên dir/tệp (file / 파일) khác nhau. |
| Rsync delete | dry-run | `rsync -avhn --delete ...` | Đọc toàn bộ đầu ra (output / 출력) trước chạy thật. |
| Edit cấu hình (config / 설정) | backup | `cp -a file file.$(date +%F_%H%M%S).bak` | Sau edit dùng `diff -u`. |
| Cleanup log | danh sách (list / 목록) first | `find ... -mtime +30 -print` | Chỉ thêm `-delete` sau rà soát (review / 검토). |

---

# 38. học tập (learning / 학습) thứ tự (order / 순서)

Thứ tự học này đi từ filesystem, process và network tới production troubleshooting. Đi theo dependency giúp mỗi lệnh tra cứu có một mental model để giải thích output.

| Level | Học | Mục tiêu |
|---|---|---|
| 1 | `pwd`, `ls`, `cd` | Không bị lạc trong filesystem. |
| 2 | `cat`, `less`, `head`, `tail` | Đọc cấu hình (config / 설정)/log. |
| 3 | `cp`, `mv`, `rm`, `mkdir`, `touch` | Quản lý tệp (file / 파일)/folder. |
| 4 | `grep`, `find` | Tìm văn bản (text / 텍스트)/tệp (file / 파일) nhanh. |
| 5 | Vim tối thiểu | Có thể sửa cấu hình (config / 설정) trên mọi máy chủ (server / 서버). |
| 6 | pipe + redirect | Ghép command và lưu/filter đầu ra (output / 출력). |
| 7 | `ps`, `pgrep`, `top`, `kill` | Quản lý tiến trình (process / 프로세스). |
| 8 | `df`, `du`, `free`, `vmstat` | Check tài nguyên (resource / 자원). |
| 9 | `ss`, `lsof`, `curl`, `dig`, `nc` | gỡ lỗi (debug / 디버그) mạng (network / 네트워크)/cổng (port / 포트)/API. |
| 10 | `systemctl`, `journalctl` | gỡ lỗi (debug / 디버그) dịch vụ (service / 서비스) chuẩn systemd. |
| 11 | tar/gzip | Backup/deploy sản phẩm tạo ra (artifact / 산출물). |
| 12 | ssh/scp/rsync | Remote operations. |
| 13 | awk/sed/xargs | Xử lý dữ liệu/log nâng cao. |
| 14 | `/proc`, `lsof +L1`, `dmesg`, `pidstat`, `iostat` | Troubleshooting cấp cấp cao (senior / 시니어). |

---

# 39. Quick Cheat Sheet — nên thuộc lòng

Cheat sheet chỉ nên dùng sau khi đã hiểu cơ chế và rủi ro của lệnh. Hãy chọn lệnh theo câu hỏi, kiểm tra target và tránh chạy chuỗi không hiểu trên máy thật.

| Tình huống | Command | Ví dụ | Senior note |
|---|---|---|---|
| Đang ở đâu | `pwd` | `pwd` | Check trước destructive thao tác (operation / 연산). |
| Xem tệp (file / 파일) | `ls -lah` | `ls -lah /opt/app` | Có hidden + kích thước (size / 크기) human-readable. |
| Xem log | `less +F` | `less +F app.log` | Follow và tìm kiếm (search / 검색) trong cùng công cụ (tool / 도구). |
| tìm kiếm (search / 검색) lỗi | `grep -Ein -C` | `grep -Ein -C5 'ERROR|Exception' app.log` | Kèm ngữ cảnh (context / 맥락). |
| Tìm tệp (file / 파일) | `find` | `find . -type f -name "*.yml"` | Quote wildcard. |
| tiến trình (process / 프로세스) | `pgrep -af` | `pgrep -af java` | Sạch hơn grep. |
| cổng (port / 포트) | `ss -lntp` | `sudo ss -lntp | grep ':8080'` | Chuẩn Linux hiện đại. |
| Health | `curl -fsS -v` | `curl -fsS -v http://127.0.0.1:8080/health` | cục bộ (local / 로컬) kiểm thử (test / 테스트) trước mạng (network / 네트워크) ngoài. |
| Disk | `df -h` | `df -h` | Check mount full. |
| Drill disk | `du -xhd1` | `du -xhd1 /var | sort -hr` | Không cross filesystem. |
| Deleted-open tệp (file / 파일) | `lsof +L1` | `sudo lsof +L1` | Giải thích disk không được free. |
| RAM | `free -h` | `free -h` | Nhìn `available`. |
| dịch vụ (service / 서비스) | `systemctl status` | `systemctl status app` | First-line gỡ lỗi (debug / 디버그). |
| dịch vụ (service / 서비스) log | `journalctl -xeu` | `journalctl -xeu app` | Start thất bại (failure / 실패) cực hữu ích. |
| Backup tệp (file / 파일) | `cp -a` | `cp -a app.conf app.conf.bak` | Giữ siêu dữ liệu (metadata / 메타데이터). |
| Compare | `diff -u` | `diff -u old.conf new.conf` | rà soát (review / 검토) thay đổi. |
| SSH gỡ lỗi (debug / 디버그) | `ssh -vvv` | `ssh -vvv user@host` | Auth/connect troubleshooting. |
| Transfer | `rsync -avhn` | `rsync -avhn --delete src/ host:/dst/` | Dry-run trước delete. |
| Kernel/OOM | `dmesg -T` | `dmesg -T | grep -i oom` | App “tự chết” có thể do OOM killer. |

---

# 40. Checklist gỡ lỗi (debug / 디버그) nhanh cho Java/Web máy chủ (server / 서버)

Checklist debug bắt đầu từ process, port, log và dependency rồi mới kiểm tra JVM hoặc web layer. Mục tiêu là khoanh boundary bằng evidence, không thử lệnh ngẫu nhiên.

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

Phần chốt nhắc lại nguyên tắc an toàn khi dùng tài liệu tra cứu: hiểu mục tiêu, xác nhận target, giữ bằng chứng và có đường rollback. Đó là điều biến một danh sách lệnh thành kỹ năng vận hành.

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

- cấp cao (senior / 시니어) không phải người nhớ nhiều command nhất, mà là người:
  - hiểu `stdin/stdout/stderr`, exit mã (code / 코드) và pipe;
  - biết khoanh vùng lỗi theo **dịch vụ (service / 서비스) → tiến trình (process / 프로세스) → cổng (port / 포트) → cục bộ (local / 로컬) endpoint → mạng (network / 네트워크) → tài nguyên (resource / 자원) → kernel**;
  - luôn kiểm tra trước destructive thao tác (operation / 연산);
  - biết lấy bằng chứng trước khi restart/xoá/kill làm mất trạng thái lỗi.

> **Bàn giao:** Sau **Ghi nhớ quan trọng**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp.
