# Bash Scripting đáng tin cậy trên Linux

Bash script thường bắt đầu rất nhỏ: vài câu lệnh để copy file, restart service hoặc chạy backup. Nhưng ngay khi script được dùng trong production, chạy tự động bằng cron/systemd hoặc thao tác dữ liệu quan trọng, nó không còn là “một chuỗi command” nữa. Nó trở thành một chương trình cần quản lý input, error, trạng thái trung gian, concurrency và khả năng phục hồi.

Mục tiêu của chương này không phải biến Bash thành ngôn ngữ cho mọi bài toán. Bash mạnh nhất khi dùng để **điều phối (orchestration)** các công cụ hệ thống đã có. Khi logic dữ liệu, concurrency hoặc cấu trúc chương trình trở nên phức tạp, Python, Go hoặc một ngôn ngữ ứng dụng khác thường phù hợp hơn.

## Script được thực thi như thế nào?

Một file shell script thường bắt đầu bằng **shebang**:

```bash
#!/usr/bin/env bash
```

Dòng này yêu cầu hệ điều hành dùng chương trình `bash` được tìm thấy qua `env`. Nếu môi trường yêu cầu đường dẫn tuyệt đối cố định, có thể dùng:

```bash
#!/bin/bash
```

Hai cách có ưu và nhược điểm khác nhau. `/usr/bin/env bash` linh hoạt hơn với môi trường có Bash ở vị trí khác, còn `/bin/bash` rõ ràng hơn khi cần kiểm soát runtime chính xác.

Sau khi cấp quyền thực thi:

```bash
chmod +x deploy.sh
./deploy.sh
```

Shell thực thi file theo cú pháp Bash. Nếu chạy:

```bash
sh deploy.sh
```

thì script có thể được chạy bằng shell khác, làm các cú pháp riêng của Bash như arrays hoặc `[[ ... ]]` hoạt động khác hoặc lỗi. Vì vậy hãy phân biệt rõ script được viết cho POSIX `sh` hay cho Bash.

## Exit status là hợp đồng của script

Trong Unix, `0` thường biểu thị thành công, còn giá trị khác `0` biểu thị lỗi hoặc trạng thái đặc biệt.

```bash
cp source.conf target.conf
status=$?
echo "$status"
```

Một script production nên trả về exit status có ý nghĩa để cron, systemd, CI/CD hoặc script cha biết nó đã thành công hay thất bại.

```bash
if ! cp "$src" "$dst"; then
  echo "Không thể copy file" >&2
  exit 1
fi
```

Không nên kết thúc script với `exit 0` một cách máy móc nếu các bước trước có thể đã thất bại mà chưa được kiểm tra.

## `set -euo pipefail`: hữu ích nhưng không phải phép thuật

Một mẫu thường gặp là:

```bash
set -euo pipefail
```

`-e` yêu cầu shell thoát trong nhiều trường hợp command thất bại. `-u` xem việc dùng biến chưa được khai báo là lỗi. `pipefail` làm pipeline phản ánh lỗi ở command bên trong thay vì chỉ lấy trạng thái command cuối.

Tuy nhiên `set -e` có nhiều ngoại lệ liên quan `if`, `&&`, `||`, subshell và command substitution. Vì vậy không nên hiểu nó là “mọi lỗi đều tự động được bắt”. Với các operation quan trọng, vẫn nên kiểm tra explicit:

```bash
if ! rsync -a --delete "$src/" "$dst/"; then
  echo "Đồng bộ thất bại" >&2
  exit 1
fi
```

## Quote biến gần như luôn là mặc định đúng

Giả sử:

```bash
DIR="/opt/My App"
```

Nếu viết:

```bash
cd $DIR
```

shell có thể tách thành hai argument. Viết:

```bash
cd "$DIR"
```

giữ giá trị thành một argument duy nhất.

Quy tắc thực dụng: **quote variable expansion trừ khi bạn chủ động muốn word splitting hoặc globbing**.

```bash
rm -rf "$TARGET_DIR"
```

Điều này đặc biệt quan trọng với destructive command. Tuy nhiên quote không thay thế việc validate biến.

## Validate input trước khi thao tác

Một script cleanup nguy hiểm:

```bash
rm -rf "$TARGET_DIR"/*
```

Nếu `TARGET_DIR` rỗng hoặc sai, hậu quả có thể lớn. Hãy kiểm tra precondition:

```bash
if [[ -z "${TARGET_DIR:-}" ]]; then
  echo "TARGET_DIR chưa được cấu hình" >&2
  exit 1
fi

if [[ "$TARGET_DIR" != /opt/app/cache/* ]]; then
  echo "Đường dẫn không nằm trong vùng cho phép: $TARGET_DIR" >&2
  exit 1
fi
```

Với script production, validate path, file tồn tại, ownership, disk space, service state và các điều kiện nghiệp vụ trước khi mutation.

## Parameter và giá trị mặc định

Argument vị trí:

```bash
script.sh prod 8080
```

trong script:

```bash
environment="$1"
port="$2"
```

Cách an toàn hơn khi argument có thể thiếu:

```bash
environment="${1:-dev}"
port="${2:-8080}"
```

`${VAR:-default}` dùng giá trị mặc định khi biến chưa có hoặc rỗng. `${VAR:?message}` buộc biến phải có:

```bash
: "${DEPLOY_DIR:?DEPLOY_DIR là bắt buộc}"
```

Cú pháp này rất hữu ích để fail sớm thay vì chạy nửa chừng rồi mới phát hiện cấu hình thiếu.

## Hàm và phạm vi biến

Bash hỗ trợ functions:

```bash
log() {
  printf '%s %s\n' "$(date '+%F %T')" "$*"
}
```

Biến trong Bash mặc định không có block scope như nhiều ngôn ngữ khác. Trong function, dùng `local` để giảm tác dụng phụ:

```bash
check_port() {
  local port="$1"
  ss -lnt | grep -q ":${port} "
}
```

Một function tốt nên có trách nhiệm nhỏ, input rõ ràng và exit status có ý nghĩa.

## Arrays khi danh sách không nên được biểu diễn bằng chuỗi

Sai lầm phổ biến là nhét danh sách path vào một string:

```bash
FILES="a.txt b file.txt c.txt"
```

Tên file có khoảng trắng sẽ phá parsing. Bash array phù hợp hơn:

```bash
files=("a.txt" "b file.txt" "c.txt")

for file in "${files[@]}"; do
  printf '%s\n' "$file"
done
```

Điểm quan trọng là `"${files[@]}"` giữ từng phần tử thành argument riêng.

## Temporary file và `mktemp`

Không nên tự tạo temp file kiểu:

```bash
/tmp/result.tmp
```

vì tên cố định có thể collision hoặc tạo vấn đề bảo mật. Dùng:

```bash
tmp_file=$(mktemp)
```

hoặc temp directory:

```bash
tmp_dir=$(mktemp -d)
```

Sau đó đăng ký cleanup bằng `trap`:

```bash
cleanup() {
  rm -rf "$tmp_dir"
}

trap cleanup EXIT
```

`trap` là một trong những công cụ quan trọng nhất để bảo đảm tài nguyên trung gian được dọn kể cả khi script lỗi giữa chừng.

## `trap` và xử lý signal

Có thể bắt một số signal để cleanup hoặc ghi log:

```bash
trap 'echo "Bị ngắt" >&2; exit 130' INT
trap 'echo "Nhận TERM" >&2; exit 143' TERM
```

Nhưng không thể catch `SIGKILL`. Script cũng không nên cố “nuốt” mọi signal nếu điều đó làm systemd hoặc operator không thể dừng nó đúng cách.

## Logging của script

Thay vì `echo` rời rạc, nên có format nhất quán:

```bash
log() {
  printf '%s [%s] %s\n' "$(date '+%F %T%z')" "$1" "$2"
}

log INFO "Bắt đầu deploy"
log ERROR "Health check thất bại" >&2
```

Nếu script chạy dưới systemd, stdout/stderr có thể được journald thu thập. Nếu chạy qua cron, hãy redirect hoặc thiết lập monitoring phù hợp.

Không log secret, token, password hoặc toàn bộ environment khi không cần thiết.

## Idempotency

Một script đáng tin cậy nên cố đạt cùng desired state dù chạy lại nhiều lần.

```bash
mkdir -p /opt/app/releases
```

là idempotent hơn việc giả định directory chưa tồn tại.

Trong deploy, thay vì “copy rồi hy vọng”, có thể so checksum hoặc version:

```bash
sha256sum app.jar
```

Một migration hoặc business command có side effect không phải lúc nào cũng idempotent; khi đó cần marker, transaction hoặc cơ chế cấp ứng dụng phù hợp.

## Concurrency và `flock`

Nếu cron chạy job mỗi 5 phút nhưng job có lúc mất 8 phút, hai instance có thể overlap.

```bash
flock -n /run/app-maintenance.lock /opt/scripts/maintenance.sh
```

`-n` không chờ nếu lock đang được giữ. Đây là giải pháp phù hợp cho single-host automation. Với nhiều host, cần distributed coordination khác.

## Atomic update

Ghi trực tiếp vào file config có thể để lại file nửa vời nếu process bị ngắt. Pattern tốt hơn là tạo file mới, validate rồi rename:

```bash
tmp=$(mktemp)
generate_config > "$tmp"
validate_config "$tmp"
mv "$tmp" /opt/app/application.yml
```

Rename trong cùng filesystem thường atomic ở namespace level. Pattern này giảm thời gian hệ thống nhìn thấy trạng thái trung gian.

## `shellcheck`

`ShellCheck` là static analyzer cho shell script. Nó phát hiện nhiều lỗi về quoting, unused variables, word splitting và portability.

```bash
shellcheck deploy.sh
```

Không nên coi output của tool là luật tuyệt đối, nhưng nó giúp bắt các lỗi shell rất phổ biến trước production.

## Debug script

Bash có tracing:

```bash
bash -x script.sh
```

hoặc trong script:

```bash
set -x
```

Nhưng `set -x` có thể in secret nằm trong arguments hoặc variables. Không bật tracing bừa bãi trong production logs.

Có thể thay `PS4` để trace có timestamp/line number khi cần điều tra sâu:

```bash
export PS4='+ ${BASH_SOURCE}:${LINENO}: '
```

## Khi nào nên bỏ Bash?

Nếu script cần parse JSON phức tạp, quản lý cấu trúc dữ liệu lớn, retry policy nhiều nhánh, HTTP workflow lớn, concurrency hoặc test suite sâu, Bash thường bắt đầu trở nên khó kiểm soát.

Một dấu hiệu quan trọng là khi phần lớn code không còn là gọi system tools mà trở thành logic ứng dụng. Khi đó Python/Go/Java có type/data structure/testing tốt hơn, còn Bash chỉ nên giữ vai trò entrypoint hoặc glue code.

## Mô hình tư duy (Mental Model)

Một Bash script production nên được nhìn như một **state transition program**:

```text
input + current system state
        ↓
validate preconditions
        ↓
perform controlled mutations
        ↓
verify postconditions
        ↓
return meaningful exit status
```

Script tốt không chỉ “chạy command”. Nó chứng minh rằng điều kiện trước đúng, thay đổi state có chủ đích, và kiểm tra rằng desired state thực sự đạt được.

## Những hiểu lầm phổ biến

**“Có `set -e` là mọi lỗi đều được xử lý.”** Không. Bash có nhiều ngữ cảnh khiến `-e` không hoạt động như người mới dự đoán.

**“Quote biến chỉ cần khi có khoảng trắng.”** Quote còn ngăn glob expansion và word splitting ngoài ý muốn.

**“Cron chạy được nghĩa script đáng tin.”** Cron chỉ lập lịch; locking, timeout, idempotency, logging và error handling vẫn là trách nhiệm của script/system design.

**“Bash viết được thì nên dùng Bash.”** Khả năng viết được không đồng nghĩa Bash là công cụ có maintainability tốt nhất.

## Kết nối kiến thức

Chương này nối trực tiếp với [Shell, Bash, Pipes và Redirection](./shell_bash_pipes_redirection.md), [Scheduling và Automation](../08_operations/scheduling_automation.md), [systemd và Services](../05_system/systemd_boot_services.md), và [Production Troubleshooting](../09_production/production_troubleshooting.md).