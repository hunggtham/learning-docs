# Bash Scripting đáng tin cậy trên Linux

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Bash Scripting đáng tin cậy trên Linux**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Script được thực thi như thế nào?** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Exit status là hợp đồng của script** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối Bash scripting với input, exit status, concurrency và recovery, để script production có hợp đồng lỗi và đường lui rõ ràng.

Bash script thường bắt đầu rất nhỏ: vài câu lệnh để bản sao (copy / 복사) tệp (file / 파일), restart dịch vụ (service / 서비스) hoặc chạy backup. Nhưng ngay khi script được dùng trong môi trường vận hành (production / 운영 환경), chạy tự động bằng cron/systemd hoặc thao tác dữ liệu quan trọng, nó không còn là “một chuỗi command” nữa. Nó trở thành một chương trình cần quản lý đầu vào (input / 입력), lỗi (error / 오류), trạng thái trung gian, tính đồng thời (concurrency / 동시성) và khả năng phục hồi.

Mục tiêu của chương này không phải biến Bash thành ngôn ngữ cho mọi bài toán. Bash mạnh nhất khi dùng để **điều phối (orchestration)** các công cụ hệ thống đã có. Khi lô-gic (logic / 논리) dữ liệu, tính đồng thời (concurrency / 동시성) hoặc cấu trúc chương trình trở nên phức tạp, Python, Go hoặc một ngôn ngữ ứng dụng khác thường phù hợp hơn.

## Script được thực thi như thế nào?

Một tệp (file / 파일) shell script thường bắt đầu bằng **shebang**:

```bash
#!/usr/bin/env bash
```

Dòng này yêu cầu hệ điều hành dùng chương trình `bash` được tìm thấy qua `env`. Nếu môi trường yêu cầu đường dẫn tuyệt đối cố định, có thể dùng:

```bash
#!/bin/bash
```

Hai cách có ưu và nhược điểm khác nhau. `/usr/bin/env bash` linh hoạt hơn với môi trường có Bash ở vị trí khác, còn `/bin/bash` rõ ràng hơn khi cần kiểm soát thời gian chạy (runtime / 런타임) chính xác.

Sau khi cấp quyền thực thi:

```bash
chmod +x deploy.sh
./deploy.sh
```

Shell thực thi tệp (file / 파일) theo cú pháp Bash. Nếu chạy:

```bash
sh deploy.sh
```

thì script có thể được chạy bằng shell khác, làm các cú pháp riêng của Bash như arrays hoặc `[[ ... ]]` hoạt động khác hoặc lỗi. Vì vậy hãy phân biệt rõ script được viết cho POSIX `sh` hay cho Bash.

> **Nối mạch:** Trong **Bash Scripting đáng tin cậy trên Linux**, **Exit status là hợp đồng của script** nối từ **Script được thực thi như thế nào?** sang **set -euo pipefail: hữu ích nhưng không phải phép thuật**, vì cơ chế trước tạo đầu vào cho bước sau.

## Exit status là hợp đồng của script

Trong Unix, `0` thường biểu thị thành công, còn giá trị khác `0` biểu thị lỗi hoặc trạng thái đặc biệt.

```bash
cp source.conf target.conf
status=$?
echo "$status"
```

Một script môi trường vận hành (production / 운영 환경) nên trả về exit status có ý nghĩa để cron, systemd, CI/CD hoặc script cha biết nó đã thành công hay thất bại.

```bash
if ! cp "$src" "$dst"; then
  echo "Không thể copy file" >&2
  exit 1
fi
```

Không nên kết thúc script với `exit 0` một cách máy móc nếu các bước trước có thể đã thất bại mà chưa được kiểm tra.

> **Nối mạch:** Ở chặng này của **Bash Scripting đáng tin cậy trên Linux**, **set -euo pipefail: hữu ích nhưng không phải phép thuật** nối từ **Exit status là hợp đồng của script** sang **Quote biến gần như luôn là mặc định đúng**, vì cơ chế trước tạo đầu vào cho bước sau.

## `set -euo pipefail`: hữu ích nhưng không phải phép thuật

Một mẫu thường gặp là:

```bash
set -euo pipefail
```

`-e` yêu cầu shell thoát trong nhiều trường hợp command thất bại. `-u` xem việc dùng biến chưa được khai báo là lỗi. `pipefail` làm chuỗi xử lý (pipeline / 파이프라인) phản ánh lỗi ở command bên trong thay vì chỉ lấy trạng thái command cuối.

Tuy nhiên `set -e` có nhiều ngoại lệ liên quan `if`, `&&`, `||`, subshell và command substitution. Vì vậy không nên hiểu nó là “mọi lỗi đều tự động được bắt”. Với các thao tác (operation / 연산) quan trọng, vẫn nên kiểm tra tường minh (explicit / 명시적):

```bash
if ! rsync -a --delete "$src/" "$dst/"; then
  echo "Đồng bộ thất bại" >&2
  exit 1
fi
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **Bash Scripting đáng tin cậy trên Linux**, **Quote biến gần như luôn là mặc định đúng** nối từ **set -euo pipefail: hữu ích nhưng không phải phép thuật** sang **Validate đầu vào (input / 입력) trước khi thao tác**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Trong **Bash Scripting đáng tin cậy trên Linux**, **Validate đầu vào (input / 입력) trước khi thao tác** nối từ **Quote biến gần như luôn là mặc định đúng** sang **Parameter và giá trị mặc định**, vì cơ chế trước tạo đầu vào cho bước sau.

## Validate đầu vào (input / 입력) trước khi thao tác

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

Với script môi trường vận hành (production / 운영 환경), validate đường dẫn (path / 경로), tệp (file / 파일) tồn tại, quyền sở hữu (ownership / 소유권), disk không gian (space / 공간), dịch vụ (service / 서비스) trạng thái (state / 상태) và các điều kiện nghiệp vụ trước khi mutation.

> **Nối mạch:** Ở chặng này của **Bash Scripting đáng tin cậy trên Linux**, **Parameter và giá trị mặc định** nối từ **Validate đầu vào (input / 입력) trước khi thao tác** sang **Hàm và phạm vi biến**, vì cơ chế trước tạo đầu vào cho bước sau.

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

Cú pháp này rất hữu ích để thất bại (fail / 실패) sớm thay vì chạy nửa chừng rồi mới phát hiện cấu hình thiếu.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Bash Scripting đáng tin cậy trên Linux**, **Hàm và phạm vi biến** nối từ **Parameter và giá trị mặc định** sang **Arrays khi danh sách không nên được biểu diễn bằng chuỗi**, vì cơ chế trước tạo đầu vào cho bước sau.

## Hàm và phạm vi biến

Bash hỗ trợ functions:

```bash
log() {
  printf '%s %s\n' "$(date '+%F %T')" "$*"
}
```

Biến trong Bash mặc định không có khối (block / 블록) phạm vi (scope / 범위) như nhiều ngôn ngữ khác. Trong hàm (function / 함수), dùng `local` để giảm tác dụng phụ:

```bash
check_port() {
  local port="$1"
  ss -lnt | grep -q ":${port} "
}
```

Một hàm (function / 함수) tốt nên có trách nhiệm nhỏ, đầu vào (input / 입력) rõ ràng và exit status có ý nghĩa.

> **Nối mạch:** Trong **Bash Scripting đáng tin cậy trên Linux**, **Hàm và phạm vi biến** đặt đầu vào cho **Arrays khi danh sách không nên được biểu diễn bằng chuỗi**, rồi **Temporary tệp (file / 파일) và mktemp** mở rộng hệ quả hoặc giới hạn liên quan.

## Arrays khi danh sách không nên được biểu diễn bằng chuỗi

Sai lầm phổ biến là nhét danh sách đường dẫn (path / 경로) vào một string:

```bash
FILES="a.txt b file.txt c.txt"
```

Tên tệp (file / 파일) có khoảng trắng sẽ phá parsing. Bash array phù hợp hơn:

```bash
files=("a.txt" "b file.txt" "c.txt")

for file in "${files[@]}"; do
  printf '%s\n' "$file"
done
```

Điểm quan trọng là `"${files[@]}"` giữ từng phần tử thành argument riêng.

> **Nối mạch:** Ở chặng này của **Bash Scripting đáng tin cậy trên Linux**, **Arrays khi danh sách không nên được biểu diễn bằng chuỗi** đặt đầu vào cho **Temporary tệp (file / 파일) và mktemp**, rồi **trap và xử lý tín hiệu (signal / 신호)** mở rộng hệ quả hoặc giới hạn liên quan.

## Temporary tệp (file / 파일) và `mktemp`

Không nên tự tạo temp tệp (file / 파일) kiểu:

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

> **Nối mạch:** Đặt trong câu hỏi lớn của **Bash Scripting đáng tin cậy trên Linux**, **trap và xử lý tín hiệu (signal / 신호)** nối từ **Temporary tệp (file / 파일) và mktemp** sang **Logging của script**, vì cơ chế trước tạo đầu vào cho bước sau.

## `trap` và xử lý tín hiệu (signal / 신호)

Có thể bắt một số tín hiệu (signal / 신호) để cleanup hoặc ghi log:

```bash
trap 'echo "Bị ngắt" >&2; exit 130' INT
trap 'echo "Nhận TERM" >&2; exit 143' TERM
```

Nhưng không thể catch `SIGKILL`. Script cũng không nên cố “nuốt” mọi tín hiệu (signal / 신호) nếu điều đó làm systemd hoặc operator không thể dừng nó đúng cách.

> **Nối mạch:** Trong **Bash Scripting đáng tin cậy trên Linux**, **Logging của script** nối từ **trap và xử lý tín hiệu (signal / 신호)** sang **Idempotency**, vì cơ chế trước tạo đầu vào cho bước sau.

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

Không log secret, đơn vị từ (token / 토큰), password hoặc toàn bộ môi trường (environment / 환경) khi không cần thiết.

> **Nối mạch:** Ở chặng này của **Bash Scripting đáng tin cậy trên Linux**, **Idempotency** nối từ **Logging của script** sang **Tính đồng thời (concurrency / 동시성) và flock**, vì cơ chế trước tạo đầu vào cho bước sau.

## Idempotency

Một script đáng tin cậy nên cố đạt cùng desired trạng thái (state / 상태) dù chạy lại nhiều lần.

```bash
mkdir -p /opt/app/releases
```

là idempotent hơn việc giả định directory chưa tồn tại.

Trong deploy, thay vì “bản sao (copy / 복사) rồi hy vọng”, có thể so checksum hoặc phiên bản (version / 버전):

```bash
sha256sum app.jar
```

Một di chuyển (migration / 마이그레이션) hoặc nghiệp vụ (business / 비즈니스) command có side tác động (effect / 효과) không phải lúc nào cũng idempotent; khi đó cần marker, giao dịch (transaction / 트랜잭션) hoặc cơ chế cấp ứng dụng phù hợp.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Bash Scripting đáng tin cậy trên Linux**, **Tính đồng thời (concurrency / 동시성) và flock** nối từ **Idempotency** sang **Atomic cập nhật (update / 업데이트)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Tính đồng thời (concurrency / 동시성) và `flock`

Nếu cron chạy job mỗi 5 phút nhưng job có lúc mất 8 phút, hai instance có thể overlap.

```bash
flock -n /run/app-maintenance.lock /opt/scripts/maintenance.sh
```

`-n` không chờ nếu khóa (lock / 잠금) đang được giữ. Đây là giải pháp phù hợp cho single-host automation. Với nhiều host, cần phân tán (distributed / 분산) coordination khác.

> **Nối mạch:** Trong **Bash Scripting đáng tin cậy trên Linux**, **Atomic cập nhật (update / 업데이트)** nối từ **Tính đồng thời (concurrency / 동시성) và flock** sang **shellcheck**, vì cơ chế trước tạo đầu vào cho bước sau.

## Atomic cập nhật (update / 업데이트)

Ghi trực tiếp vào tệp (file / 파일) cấu hình (config / 설정) có thể để lại tệp (file / 파일) nửa vời nếu tiến trình (process / 프로세스) bị ngắt. mẫu (pattern / 패턴) tốt hơn là tạo tệp (file / 파일) mới, validate rồi rename:

```bash
tmp=$(mktemp)
generate_config > "$tmp"
validate_config "$tmp"
mv "$tmp" /opt/app/application.yml
```

Rename trong cùng filesystem thường atomic ở không gian tên (namespace / 네임스페이스) mức (level / 수준). mẫu (pattern / 패턴) này giảm thời gian hệ thống nhìn thấy trạng thái trung gian.

> **Nối mạch:** Ở chặng này của **Bash Scripting đáng tin cậy trên Linux**, **shellcheck** nối từ **Atomic cập nhật (update / 업데이트)** sang **Gỡ lỗi (debug / 디버그) script**, vì cơ chế trước tạo đầu vào cho bước sau.

## `shellcheck`

`ShellCheck` là static analyzer cho shell script. Nó phát hiện nhiều lỗi về quoting, unused variables, word splitting và portability.

```bash
shellcheck deploy.sh
```

Không nên coi đầu ra (output / 출력) của công cụ (tool / 도구) là luật tuyệt đối, nhưng nó giúp bắt các lỗi shell rất phổ biến trước môi trường vận hành (production / 운영 환경).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Bash Scripting đáng tin cậy trên Linux**, **Gỡ lỗi (debug / 디버그) script** nối từ **shellcheck** sang **Khi nào nên bỏ Bash?**, vì cơ chế trước tạo đầu vào cho bước sau.

## Gỡ lỗi (debug / 디버그) script

Bash có tracing:

```bash
bash -x script.sh
```

hoặc trong script:

```bash
set -x
```

Nhưng `set -x` có thể in secret nằm trong arguments hoặc variables. Không bật tracing bừa bãi trong môi trường vận hành (production / 운영 환경) logs.

Có thể thay `PS4` để dấu vết (trace / 추적) có timestamp/line number khi cần điều tra sâu:

```bash
export PS4='+ ${BASH_SOURCE}:${LINENO}: '
```

> **Nối mạch:** Trong **Bash Scripting đáng tin cậy trên Linux**, **Khi nào nên bỏ Bash?** nối từ **Gỡ lỗi (debug / 디버그) script** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Khi nào nên bỏ Bash?

Nếu script cần parse JSON phức tạp, quản lý cấu trúc dữ liệu lớn, thử lại (retry / 재시도) chính sách (policy / 정책) nhiều nhánh, HTTP workflow lớn, tính đồng thời (concurrency / 동시성) hoặc bộ kiểm thử (test suite / 테스트 스위트) sâu, Bash thường bắt đầu trở nên khó kiểm soát.

Một dấu hiệu quan trọng là khi phần lớn mã (code / 코드) không còn là gọi hệ thống (system / 시스템) tools mà trở thành lô-gic (logic / 논리) ứng dụng. Khi đó Python/Go/Java có kiểu (type / 타입)/cấu trúc dữ liệu (data structure / 자료구조)/testing tốt hơn, còn Bash chỉ nên giữ vai trò điểm vào (entrypoint / 진입점) hoặc glue mã (code / 코드).

> **Nối mạch:** Ở chặng này của **Bash Scripting đáng tin cậy trên Linux**, **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Khi nào nên bỏ Bash?** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những hiểu lầm phổ biến** mở rộng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

Một Bash script môi trường vận hành (production / 운영 환경) nên được nhìn như một **chuyển tiếp trạng thái (state transition / 상태 전이) program**:

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

Script tốt không chỉ “chạy command”. Nó chứng minh rằng điều kiện trước đúng, thay đổi trạng thái (state / 상태) có chủ đích, và kiểm tra rằng desired trạng thái (state / 상태) thực sự đạt được.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Bash Scripting đáng tin cậy trên Linux**, **Những hiểu lầm phổ biến** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối kiến thức** mở rộng hệ quả hoặc giới hạn liên quan.

## Những hiểu lầm phổ biến

**“Có `set -e` là mọi lỗi đều được xử lý.”** Không. Bash có nhiều ngữ cảnh khiến `-e` không hoạt động như người mới dự đoán.

**“Quote biến chỉ cần khi có khoảng trắng.”** Quote còn ngăn glob expansion và word splitting ngoài ý muốn.

**“Cron chạy được nghĩa script đáng tin.”** Cron chỉ lập lịch; locking, hết thời gian chờ (timeout / 타임아웃), idempotency, logging và lỗi (error / 오류) handling vẫn là trách nhiệm của script/hệ thống (system / 시스템) thiết kế (design / 설계).

**“Bash viết được thì nên dùng Bash.”** Khả năng viết được không đồng nghĩa Bash là công cụ có maintainability tốt nhất.

> **Nối mạch:** Trong **Bash Scripting đáng tin cậy trên Linux**, **Kết nối kiến thức** nối từ **Những hiểu lầm phổ biến** sang  Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Kết nối kiến thức

Chương này nối trực tiếp với [Shell, Bash, Pipes và Redirection](./shell_bash_pipes_redirection.md), [Scheduling và Automation](../08_operations/scheduling_automation.md), [systemd và Services](../05_system/systemd_boot_services.md), và [Production Troubleshooting](../09_production/production_troubleshooting.md).

> **Bàn giao:** Sau **Kết nối kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
