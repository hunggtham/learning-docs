# Quá trình boot, kernel và initramfs

> **Mạch đọc:** Đọc **Quá trình boot, kernel và initramfs** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Từ khi bấm nút nguồn đến khi có shell** sang **Firmware: BIOS và UEFI**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

Khi một máy Linux “không boot được”, câu đó có thể mô tả lỗi ở nhiều lớp hoàn toàn khác nhau: firmware không tìm thấy boot thiết bị (device / 장치), bootloader không tải (load / 로드) được kernel, kernel không mount được gốc (root / 루트) filesystem, initramfs thiếu driver, hoặc PID 1 khởi động nhưng dịch vụ (service / 서비스) thiết yếu thất bại.

Muốn xử lý đúng cần hiểu **chuỗi khởi động (boot chain)** thay vì chỉ nhớ `systemctl`.

## Từ khi bấm nút nguồn đến khi có shell

Một mô hình đơn giản:

```text
Firmware (BIOS/UEFI)
        ↓
Bootloader
        ↓
Linux kernel
        ↓
initramfs / early userspace
        ↓
root filesystem thật
        ↓
PID 1 (thường là systemd)
        ↓
services / login / application
```

Mỗi lớp có responsibility riêng và có loại lỗi riêng.

## Firmware: BIOS và UEFI

Firmware chạy trước operating hệ thống (system / 시스템). Trên máy hiện đại thường là UEFI.

Firmware:

- khởi tạo phần cứng nền tảng;
- chọn boot mục tiêu (target / 대상);
- tải bootloader hoặc EFI executable.

Nếu disk không xuất hiện ở firmware mức (level / 수준) thì Linux kernel còn chưa được chạy. Khi đó chỉnh `/etc/fstab` hay `systemctl` không có tác dụng.

## Bootloader

Bootloader phổ biến trên Linux là GRUB.

Nhiệm vụ của bootloader là tìm và tải (load / 로드) kernel cùng initramfs vào bộ nhớ (memory / 메모리), sau đó truyền điều khiển (control / 제어) cho kernel.

Trên nhiều các hệ thống (systems / 시스템들) có thể xem cấu hình:

```bash
cat /etc/default/grub
```

Sau khi thay đổi, command regenerate phụ thuộc phân phối (distribution / 분포):

```bash
sudo update-grub
```

hoặc:

```bash
sudo grub2-mkconfig ...
```

Không sửa bootloader môi trường vận hành (production / 운영 환경) khi chưa có console/khôi phục (recovery / 복구) đường dẫn (path / 경로). Một lỗi nhỏ có thể làm host không boot từ xa được.

## Kernel ảnh (image / 이미지)

Kernel thường nằm dưới `/boot`:

```bash
ls -lh /boot
```

Có thể thấy:

```text
vmlinuz-...
initrd.img-...
config-...
System.map-...
```

`uname -r` cho biết kernel đang chạy:

```bash
uname -r
```

Điểm quan trọng: kernel tệp (file / 파일) đã được cài mới **không có nghĩa kernel mới đang chạy**. Nếu cập nhật (update / 업데이트) gói (package / 패키지) nhưng chưa reboot, `uname -r` vẫn có thể cho phiên bản (version / 버전) cũ.

## Kernel command line

Bootloader truyền parameters cho kernel.

Xem thời gian chạy (runtime / 런타임) command line:

```bash
cat /proc/cmdline
```

Có thể chứa gốc (root / 루트) thiết bị (device / 장치), console settings, cgroup options, crash kernel parameters hoặc gỡ lỗi (debug / 디버그) flags.

Đây là “effective trạng thái (state / 상태)” của boot hiện tại, không nhất thiết giống tệp (file / 파일) cấu hình (config / 설정) bạn vừa sửa nhưng chưa reboot.

## Vì sao cần initramfs?

Kernel cần mount gốc (root / 루트) filesystem để chạy userspace, nhưng để mount gốc (root / 루트) filesystem kernel có thể cần driver hoặc công cụ (tool / 도구) nằm… trên gốc (root / 루트) filesystem đó.

Đây là vấn đề vòng tròn.

**initramfs** là filesystem nhỏ được tải (load / 로드) vào RAM cùng kernel, chứa đủ driver và userspace công cụ (tool / 도구) để chuẩn bị gốc (root / 루트) filesystem thật.

Ví dụ cần:

- lưu trữ (storage / 저장소) driver;
- LVM;
- RAID;
- encryption setup;
- mạng (network / 네트워크) gốc (root / 루트);
- filesystem mô-đun (module / 모듈).

Sau khi gốc (root / 루트) thật sẵn sàng, hệ thống (system / 시스템) chuyển từ early userspace sang gốc (root / 루트) filesystem chính.

## Khi initramfs có vấn đề

Triệu chứng có thể là emergency shell hoặc lỗi kiểu:

```text
Unable to find root device
ALERT! UUID=... does not exist
```

Điều tra cần hỏi:

- thiết bị (device / 장치) có xuất hiện không;
- UUID đúng không;
- driver có trong initramfs không;
- LVM/RAID/encryption có activate được không;
- gốc (root / 루트) filesystem có hỏng không.

Các công cụ (tool / 도구) thường dùng trong khôi phục (recovery / 복구):

```bash
lsblk -f
blkid
lvm pvscan
lvm vgscan
lvm lvscan
```

Tùy môi trường, command khác nhau.

## UUID và `/etc/fstab`

Mount bằng `/dev/sda1` có thể không ổn định khi thiết bị (device / 장치) enumeration thay đổi. UUID cung cấp định danh (identity / 식별자) ổn định hơn.

```bash
blkid
cat /etc/fstab
```

Một dòng `fstab` sai có thể làm boot vào emergency chế độ (mode / 모드) nếu mount được đánh dấu bắt buộc.

Các option như `nofail` hoặc systemd mount hành vi (behavior / 동작) có thể thay ngữ nghĩa (semantics / 의미론), nhưng không nên dùng để che lỗi lưu trữ (storage / 저장소) quan trọng.

## PID 1 xuất hiện khi nào?

Sau khi gốc (root / 루트) filesystem đã sẵn sàng, kernel chạy init tiến trình (process / 프로세스). Trên phần lớn phân phối (distribution / 분포) hiện đại:

```bash
ps -p 1 -o pid,comm,args
```

sẽ cho thấy `systemd`.

Từ đây boot chuyển từ kernel/early-userspace bài toán (problem / 문제) sang dịch vụ (service / 서비스)/phụ thuộc (dependency / 의존성) bài toán (problem / 문제).

## systemd boot giao dịch (transaction / 트랜잭션)

Systemd không đơn giản chạy mọi script theo thứ tự cố định. Nó xây phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) của units.

Một số targets thường gặp:

```text
local-fs.target
network.target
multi-user.target
graphical.target
```

Xem phụ thuộc (dependency / 의존성):

```bash
systemctl list-dependencies multi-user.target
```

Xem boot thời gian (time / 시간):

```bash
systemd-analyze
systemd-analyze blame
systemd-analyze critical-chain
```

### `systemd-analyze blame` cần được đọc cẩn thận

Một đơn vị (unit / 단위) có thời gian activate dài không nhất thiết là nguyên nhân gốc (root cause / 근본 원인) của boot chậm. Nó có thể chờ phụ thuộc (dependency / 의존성) hoặc chạy song song với đơn vị (unit / 단위) khác.

`critical-chain` thường hữu ích hơn để thấy đường phụ thuộc (dependency / 의존성) ảnh hưởng trực tiếp đến thời gian boot.

## Journal của boot hiện tại và boot trước

Trước khi chạy hoặc đọc ví dụ dưới đây, hãy xác định câu hỏi vận hành mà nó trả lời, dữ liệu nào sẽ quan sát được và giới hạn của kết quả. Lệnh chỉ có ý nghĩa khi gắn với một giả thuyết về state của hệ thống.

```bash
journalctl -b
```

`-b` lọc boot hiện tại.

Boot trước:

```bash
journalctl -b -1
```

Danh sách boots:

```bash
journalctl --list-boots
```

Đây là công cụ rất mạnh khi máy chủ (server / 서버) reboot bất ngờ: có thể xem phần cuối journal của boot trước.

```bash
journalctl -b -1 -e
```

## Reboot bất ngờ: bắt đầu từ đâu?

Không nên mặc định ứng dụng (application / 애플리케이션) đã gọi reboot.

Kiểm tra:

```bash
last -x | head -30
journalctl --list-boots
journalctl -b -1 -e
journalctl -k -b -1
```

Tìm các dấu hiệu:

- OOM;
- kernel panic;
- watchdog;
- power sự kiện (event / 이벤트);
- operator shutdown;
- cloud/hypervisor maintenance;
- filesystem/lưu trữ (storage / 저장소) errors.

Nếu log dừng đột ngột mà không có shutdown chuỗi (sequence / 시퀀스), power/hypervisor/kernel crash là giả thuyết đáng xem.

## Kernel panic

Kernel panic là thất bại (failure / 실패) nghiêm trọng khiến kernel không thể tiếp tục an toàn.

Một panic có thể do:

- kernel bug;
- driver;
- hardware thất bại (failure / 실패);
- corrupted bộ nhớ (memory / 메모리);
- filesystem/lưu trữ (storage / 저장소) đường dẫn (path / 경로);
- third-party mô-đun (module / 모듈).

Nếu host tự reboot sau panic, cục bộ (local / 로컬) logs có thể không còn đủ. môi trường vận hành (production / 운영 환경) các hệ thống (systems / 시스템들) quan trọng có thể cấu hình `kdump` để capture crash dump.

## Kdump

Kdump dùng một crash kernel nhỏ để ghi bộ nhớ (memory / 메모리) dump khi kernel chính panic.

Conceptual luồng (flow / 흐름):

```text
running kernel
    ↓ panic
reserved crash kernel
    ↓
write vmcore
    ↓
postmortem analysis
```

Đây là kỹ thuật sâu, thường cần distro-specific setup và đủ reserved bộ nhớ (memory / 메모리).

Không cần mọi ứng dụng (application / 애플리케이션) máy chủ (server / 서버) đều bật kdump, nhưng với kernel/hardware incidents khó tái hiện, nó có thể là bằng chứng (evidence / 증거) duy nhất.

## Kernel modules trong boot

Một driver có thể được build-in hoặc tải (load / 로드) như mô-đun (module / 모듈).

```bash
lsmod
modinfo <module>
```

Nếu gốc (root / 루트) lưu trữ (storage / 저장소) phụ thuộc mô-đun (module / 모듈) mà initramfs thiếu mô-đun (module / 모듈) đó, boot có thể thất bại (fail / 실패) trước khi gốc (root / 루트) filesystem sẵn sàng.

Sau thay đổi driver/kernel, initramfs đôi khi cần regenerate:

Ubuntu/Debian thường dùng:

```bash
sudo update-initramfs -u
```

RHEL-family thường dùng `dracut`.

Không chạy các lệnh này theo thói quen nếu chưa hiểu phân phối (distribution / 분포) và boot bố cục (layout / 레이아웃).

## Secure Boot

Trên UEFI các hệ thống (systems / 시스템들), Secure Boot có thể yêu cầu boot components/kernel modules được ký tin cậy.

Third-party kernel mô-đun (module / 모듈) không được ký đúng có thể không tải (load / 로드) dù tệp (file / 파일) tồn tại.

Khi driver “cài rồi nhưng không tải (load / 로드)”, Secure Boot là một tầng (layer / 계층) cần xem trên một số hosts.

## Boot và bộ chứa (container / 컨테이너) khác nhau

Bộ chứa (container / 컨테이너) thường không trải qua firmware → bootloader → kernel riêng. bộ chứa (container / 컨테이너) tiến trình (process / 프로세스) dùng host kernel và bắt đầu ở userspace không gian tên (namespace / 네임스페이스) của nó.

Đây là khác biệt nền tảng giữa bộ chứa (container / 컨테이너) và VM.

Virtual machine có virtual firmware/hardware và guest kernel riêng, nên có boot chuỗi (chain / 사슬) gần máy thật hơn.

## Mô hình tư duy xử lý boot thất bại (failure / 실패)

Đừng hỏi chung “Linux boot lỗi”. Hãy xác định **stage cuối cùng đã thành công**:

```text
Firmware thấy disk?
↓
Bootloader hiện menu/load kernel?
↓
Kernel chạy?
↓
Root device tìm thấy?
↓
Root filesystem mount được?
↓
PID 1 chạy?
↓
Target/services đạt trạng thái mong muốn?
```

Mỗi câu trả lời “có” loại bỏ một nhóm nguyên nhân phía trên.

## Những hiểu lầm phổ biến

**“systemd quản lý toàn bộ boot từ lúc bật nguồn.”** Không. Firmware, bootloader, kernel và initramfs xảy ra trước systemd.

**“Cài kernel mới nghĩa là đang chạy kernel mới.”** Chỉ sau reboot vào kernel đó mới đúng.

**“`fstab` chỉ ảnh hưởng mount sau khi login.”** Sai. Nó có thể ảnh hưởng boot và emergency chế độ (mode / 모드).

**“Boot chậm thì đơn vị (unit / 단위) đứng đầu `systemd-analyze blame` chắc chắn là thủ phạm.”** Không. Cần xem đường găng (critical path / 임계 경로) và phụ thuộc (dependency / 의존성).

**“bộ chứa (container / 컨테이너) boot giống VM.”** bộ chứa (container / 컨테이너) thường không boot kernel riêng.

Xem thêm: [systemd và services](./systemd_boot_services.md), [Storage và filesystem](../06_resources/storage_filesystems.md), [`/proc` và `/sys`](../00_foundations/proc_sysfs_kernel_interfaces.md).
