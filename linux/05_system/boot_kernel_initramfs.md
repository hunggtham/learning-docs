# Quá trình boot, kernel và initramfs

Khi một máy Linux “không boot được”, câu đó có thể mô tả lỗi ở nhiều lớp hoàn toàn khác nhau: firmware không tìm thấy boot device, bootloader không load được kernel, kernel không mount được root filesystem, initramfs thiếu driver, hoặc PID 1 khởi động nhưng service thiết yếu thất bại.

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

Firmware chạy trước operating system. Trên máy hiện đại thường là UEFI.

Firmware:

- khởi tạo phần cứng nền tảng;
- chọn boot target;
- tải bootloader hoặc EFI executable.

Nếu disk không xuất hiện ở firmware level thì Linux kernel còn chưa được chạy. Khi đó chỉnh `/etc/fstab` hay `systemctl` không có tác dụng.

## Bootloader

Bootloader phổ biến trên Linux là GRUB.

Nhiệm vụ của bootloader là tìm và load kernel cùng initramfs vào memory, sau đó truyền control cho kernel.

Trên nhiều systems có thể xem cấu hình:

```bash
cat /etc/default/grub
```

Sau khi thay đổi, command regenerate phụ thuộc distribution:

```bash
sudo update-grub
```

hoặc:

```bash
sudo grub2-mkconfig ...
```

Không sửa bootloader production khi chưa có console/recovery path. Một lỗi nhỏ có thể làm host không boot từ xa được.

## Kernel image

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

Điểm quan trọng: kernel file đã được cài mới **không có nghĩa kernel mới đang chạy**. Nếu update package nhưng chưa reboot, `uname -r` vẫn có thể cho version cũ.

## Kernel command line

Bootloader truyền parameters cho kernel.

Xem runtime command line:

```bash
cat /proc/cmdline
```

Có thể chứa root device, console settings, cgroup options, crash kernel parameters hoặc debug flags.

Đây là “effective state” của boot hiện tại, không nhất thiết giống file config bạn vừa sửa nhưng chưa reboot.

## Vì sao cần initramfs?

Kernel cần mount root filesystem để chạy userspace, nhưng để mount root filesystem kernel có thể cần driver hoặc tool nằm… trên root filesystem đó.

Đây là vấn đề vòng tròn.

**initramfs** là filesystem nhỏ được load vào RAM cùng kernel, chứa đủ driver và userspace tool để chuẩn bị root filesystem thật.

Ví dụ cần:

- storage driver;
- LVM;
- RAID;
- encryption setup;
- network root;
- filesystem module.

Sau khi root thật sẵn sàng, system chuyển từ early userspace sang root filesystem chính.

## Khi initramfs có vấn đề

Triệu chứng có thể là emergency shell hoặc lỗi kiểu:

```text
Unable to find root device
ALERT! UUID=... does not exist
```

Điều tra cần hỏi:

- device có xuất hiện không;
- UUID đúng không;
- driver có trong initramfs không;
- LVM/RAID/encryption có activate được không;
- root filesystem có hỏng không.

Các tool thường dùng trong recovery:

```bash
lsblk -f
blkid
lvm pvscan
lvm vgscan
lvm lvscan
```

Tùy môi trường, command khác nhau.

## UUID và `/etc/fstab`

Mount bằng `/dev/sda1` có thể không ổn định khi device enumeration thay đổi. UUID cung cấp identity ổn định hơn.

```bash
blkid
cat /etc/fstab
```

Một dòng `fstab` sai có thể làm boot vào emergency mode nếu mount được đánh dấu bắt buộc.

Các option như `nofail` hoặc systemd mount behavior có thể thay semantics, nhưng không nên dùng để che lỗi storage quan trọng.

## PID 1 xuất hiện khi nào?

Sau khi root filesystem đã sẵn sàng, kernel chạy init process. Trên phần lớn distribution hiện đại:

```bash
ps -p 1 -o pid,comm,args
```

sẽ cho thấy `systemd`.

Từ đây boot chuyển từ kernel/early-userspace problem sang service/dependency problem.

## systemd boot transaction

Systemd không đơn giản chạy mọi script theo thứ tự cố định. Nó xây dependency graph của units.

Một số targets thường gặp:

```text
local-fs.target
network.target
multi-user.target
graphical.target
```

Xem dependency:

```bash
systemctl list-dependencies multi-user.target
```

Xem boot time:

```bash
systemd-analyze
systemd-analyze blame
systemd-analyze critical-chain
```

### `systemd-analyze blame` cần được đọc cẩn thận

Một unit có thời gian activate dài không nhất thiết là root cause của boot chậm. Nó có thể chờ dependency hoặc chạy song song với unit khác.

`critical-chain` thường hữu ích hơn để thấy đường dependency ảnh hưởng trực tiếp đến thời gian boot.

## Journal của boot hiện tại và boot trước

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

Đây là công cụ rất mạnh khi server reboot bất ngờ: có thể xem phần cuối journal của boot trước.

```bash
journalctl -b -1 -e
```

## Reboot bất ngờ: bắt đầu từ đâu?

Không nên mặc định application đã gọi reboot.

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
- power event;
- operator shutdown;
- cloud/hypervisor maintenance;
- filesystem/storage errors.

Nếu log dừng đột ngột mà không có shutdown sequence, power/hypervisor/kernel crash là giả thuyết đáng xem.

## Kernel panic

Kernel panic là failure nghiêm trọng khiến kernel không thể tiếp tục an toàn.

Một panic có thể do:

- kernel bug;
- driver;
- hardware failure;
- corrupted memory;
- filesystem/storage path;
- third-party module.

Nếu host tự reboot sau panic, local logs có thể không còn đủ. Production systems quan trọng có thể cấu hình `kdump` để capture crash dump.

## Kdump

Kdump dùng một crash kernel nhỏ để ghi memory dump khi kernel chính panic.

Conceptual flow:

```text
running kernel
    ↓ panic
reserved crash kernel
    ↓
write vmcore
    ↓
postmortem analysis
```

Đây là kỹ thuật sâu, thường cần distro-specific setup và đủ reserved memory.

Không cần mọi application server đều bật kdump, nhưng với kernel/hardware incidents khó tái hiện, nó có thể là evidence duy nhất.

## Kernel modules trong boot

Một driver có thể được build-in hoặc load như module.

```bash
lsmod
modinfo <module>
```

Nếu root storage phụ thuộc module mà initramfs thiếu module đó, boot có thể fail trước khi root filesystem sẵn sàng.

Sau thay đổi driver/kernel, initramfs đôi khi cần regenerate:

Ubuntu/Debian thường dùng:

```bash
sudo update-initramfs -u
```

RHEL-family thường dùng `dracut`.

Không chạy các lệnh này theo thói quen nếu chưa hiểu distribution và boot layout.

## Secure Boot

Trên UEFI systems, Secure Boot có thể yêu cầu boot components/kernel modules được ký tin cậy.

Third-party kernel module không được ký đúng có thể không load dù file tồn tại.

Khi driver “cài rồi nhưng không load”, Secure Boot là một layer cần xem trên một số hosts.

## Boot và container khác nhau

Container thường không trải qua firmware → bootloader → kernel riêng. Container process dùng host kernel và bắt đầu ở userspace namespace của nó.

Đây là khác biệt nền tảng giữa container và VM.

Virtual machine có virtual firmware/hardware và guest kernel riêng, nên có boot chain gần máy thật hơn.

## Mô hình tư duy xử lý boot failure

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

**“`fstab` chỉ ảnh hưởng mount sau khi login.”** Sai. Nó có thể ảnh hưởng boot và emergency mode.

**“Boot chậm thì unit đứng đầu `systemd-analyze blame` chắc chắn là thủ phạm.”** Không. Cần xem critical path và dependency.

**“Container boot giống VM.”** Container thường không boot kernel riêng.

Xem thêm: [systemd và services](./systemd_boot_services.md), [Storage và filesystem](../06_resources/storage_filesystems.md), [`/proc` và `/sys`](../00_foundations/proc_sysfs_kernel_interfaces.md).