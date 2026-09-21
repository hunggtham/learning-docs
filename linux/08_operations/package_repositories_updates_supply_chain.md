# Package lifecycle sâu hơn: repository, update, dependency và software supply chain

Chương [Gói phần mềm, phần mềm và thư viện dùng chung](./packages_software_libraries.md) giải thích vai trò cơ bản của package manager. Chương này đi sâu vào cách repository, metadata, dependency solver, signing, pinning, transaction history và rollback liên kết với độ ổn định và bảo mật của production.

## Package manager quản lý nhiều hơn file

Một package thường mang theo:

- metadata;
- version;
- dependency declarations;
- ownership của file;
- scripts chạy trước/sau install/remove;
- checksum/signature metadata;
- configuration semantics;
- lifecycle state trong package database.

Do đó:

```bash
apt install nginx
```

không chỉ là tải binary rồi copy vào `/usr/bin`.

## Package database

Trên Debian-family, `dpkg` giữ database local về packages đã cài.

Một số command:

```bash
dpkg -l
dpkg -L nginx
dpkg -S /usr/sbin/nginx
```

`dpkg -L` trả lời package sở hữu những file nào.

`dpkg -S` trả lời file cụ thể thuộc package nào.

Trên RPM-family:

```bash
rpm -qa
rpm -ql nginx
rpm -qf /usr/sbin/nginx
```

Knowledge này rất hữu ích khi một file hệ thống bị sửa thủ công và cần biết package nào sẽ ghi đè nó khi upgrade.

## Package manager tầng cao và tầng thấp

Trên Debian-family:

```text
APT
 ↓
dpkg
```

APT quản lý repository và dependency resolution; `dpkg` thao tác package `.deb` và database local ở tầng thấp hơn.

Tương tự, DNF nằm trên RPM ecosystem.

Khi install `.deb` trực tiếp bằng `dpkg -i`, dependency có thể chưa được giải quyết như khi dùng APT.

## Repository là gì?

Repository chứa packages cùng metadata để package manager biết:

- package nào tồn tại;
- version nào available;
- dependency gì;
- architecture nào;
- checksum/signature gì.

Repository có thể là:

- official distro repository;
- vendor repository;
- internal enterprise mirror;
- snapshot repository;
- testing/staging repository.

## `apt update` thực sự làm gì?

`apt update` tải metadata repository về local cache.

Sau bước này package manager biết candidate versions mới, nhưng chưa install chúng.

Do đó:

```bash
sudo apt update
apt list --upgradable
```

khác với:

```bash
sudo apt upgrade
```

## Candidate version

Package manager chọn **candidate version** dựa trên repository priorities, architecture, pinning và dependency constraints.

```bash
apt-cache policy nginx
```

có thể cho thấy:

```text
Installed: ...
Candidate: ...
Version table: ...
```

Nếu `apt install nginx` cài version bất ngờ, hãy kiểm tra candidate và repository priority trước.

## Pinning

APT pinning cho phép ưu tiên hoặc giữ version theo repository/version pattern.

Đây là công cụ mạnh nhưng có thể tạo dependency state khó hiểu nếu dùng thiếu kiểm soát.

Production pinning nên đi kèm documentation về lý do và thời điểm bỏ pin.

## Hold package

Debian-family có thể hold package:

```bash
sudo apt-mark hold package-name
apt-mark showhold
```

Hold giúp tránh auto-upgrade package nhạy cảm, nhưng cũng có thể làm security patch bị bỏ lỡ.

Hold là trade-off, không phải trạng thái nên để vĩnh viễn mà không review.

## DNF versionlock

RHEL-family có plugin/versionlock mechanism tùy distribution/version.

Mục tiêu tương tự: giữ package ở một version hoặc pattern xác định.

## Dependency solver

Một package có thể yêu cầu:

```text
libA >= 2.0
libB < 5
```

Package manager phải tìm tập versions thỏa constraints.

Conflict có thể xảy ra khi hai packages yêu cầu ranges không tương thích.

Đây là dependency graph problem giống Maven/Gradle/npm, nhưng phạm vi là operating-system state.

## Dependency trực tiếp và gián tiếp

Bạn có thể cài package A, A kéo B, B kéo C.

Sau khi remove A, B/C có thể trở thành packages không còn cần thiết.

APT có:

```bash
sudo apt autoremove
```

Nhưng cần review kỹ trên production vì package được đánh dấu auto/manual không phải lúc nào cũng phản ánh business dependency bạn mong muốn.

## Recommended và suggested packages

Debian metadata có thể phân biệt dependency bắt buộc với recommended/suggested packages.

`--no-install-recommends` thường được dùng trong container image để giảm kích thước:

```bash
apt-get install --no-install-recommends package
```

Nhưng image nhỏ hơn có thể thiếu utility mà debugging cần. Đây là trade-off giữa minimal surface và operability.

## Package scripts

Package có thể chạy maintainer scripts như:

```text
preinst
postinst
prerm
postrm
```

Các script này có thể:

- tạo user;
- reload daemon;
- migrate config;
- update cache;
- restart service.

Vì vậy package install có thể tạo side effect lớn hơn việc copy file.

Trên production, cần biết upgrade package có tự restart service không.

## Configuration files

Package manager thường có semantics riêng cho config files dưới `/etc`.

Khi package upgrade và file config đã bị admin sửa, tool có thể hỏi giữ bản local hay dùng bản maintainer.

Trong unattended automation, conflict này cần policy rõ; nếu không deployment có thể treo hoặc áp config không mong muốn.

## Conffile ownership

Trên Debian:

```bash
dpkg-query -W -f='${Conffiles}\n' package-name
```

có thể giúp xem config files do package quản lý.

Không nên coi toàn bộ `/etc` là “do package manager sở hữu”; nhiều app/internal configs được quản lý bằng configuration management riêng.

## Verify package files

RPM hỗ trợ verify:

```bash
rpm -V package-name
```

Output cho biết một số thuộc tính file khác với package metadata.

Điều này hữu ích khi nghi binary/config bị sửa thủ công.

Debian có thể dùng checksum metadata hoặc các tool bổ sung tùy package.

## Repository signing

Package manager không nên tin package chỉ vì tải qua HTTP/HTTPS. Repository signing giúp xác minh metadata/package provenance bằng cryptographic trust chain.

Trên modern Debian/Ubuntu, repository keys thường được cấu hình scoped bằng `signed-by=` thay vì bỏ mọi key vào global trusted keyring.

Ví dụ conceptual:

```text
repository metadata
   ↓ signature verified by trusted key
package checksum
   ↓
package content
```

## Vì sao `curl | sudo bash` là rủi ro?

Pattern:

```bash
curl https://vendor.example/install.sh | sudo bash
```

cho remote content quyền root ngay lập tức.

Nếu endpoint, CDN, DNS, vendor account hoặc script bị compromise, host cũng bị ảnh hưởng.

Cách an toàn hơn:

1. download;
2. verify source/signature/checksum;
3. inspect script;
4. execute với privilege tối thiểu cần thiết.

## Checksum khác signature

Checksum như SHA-256 giúp phát hiện content thay đổi, nhưng nếu attacker có thể thay cả file và checksum trên cùng website thì checksum không chứng minh provenance.

Digital signature dùng private/public key trust model mạnh hơn khi key distribution an toàn.

## Internal mirror

Enterprise thường dùng repository mirror nội bộ để:

- kiểm soát versions;
- giảm bandwidth;
- giữ package khi upstream xóa;
- quét vulnerability;
- triển khai theo wave;
- hỗ trợ môi trường không ra Internet trực tiếp.

Nhưng mirror phải được cập nhật và bảo vệ; mirror cũ có thể làm patching chậm.

## Snapshot repository

Nếu muốn reproducible host build, repository “latest” không đủ.

Snapshot repository giữ trạng thái repository ở một thời điểm.

Ví dụ mental model:

```text
prod build ngày 2026-09-20
→ repository snapshot 2026-09-20
→ package versions cố định
```

Điều này giúp rebuild server giống nhau hơn.

## Rollback package có đơn giản không?

Downgrade binary có thể không rollback:

- database schema;
- data format;
- config migration;
- systemd unit behavior;
- cache/index migration.

Package rollback chỉ là một phần của application rollback.

## Kernel package và reboot

Cài kernel package mới không có nghĩa kernel đang chạy đã đổi.

Kiểm tra:

```bash
uname -r
```

và packages installed.

Có thể có nhiều kernel versions trên disk; bootloader chọn kernel khi reboot.

Security patch kernel thường cần reboot hoặc live patch mechanism nếu được hỗ trợ.

## Shared library upgrade và process đang chạy

Nếu library trên disk được nâng cấp, process đang chạy thường vẫn dùng mapping/library đã load trước đó.

Do đó package upgrade không chắc đã đưa security fix vào process cho tới khi process restart.

Có tool trên một số distro giúp phát hiện processes dùng deleted/old libraries.

Ví dụ generic:

```bash
sudo lsof +L1
```

có thể thấy mapped deleted files trong một số trường hợp.

## Restart sau package update

Cần biết component nào phải restart sau upgrade.

Có thể là:

- application service;
- SSH daemon;
- database;
- host reboot nếu kernel/glibc/core library thay đổi sâu.

Không restart mọi thứ một cách mù quáng; cần change plan và availability strategy.

## glibc và core libraries

Nâng core library có phạm vi ảnh hưởng lớn vì nhiều processes phụ thuộc.

Running processes đã map old library có thể tiếp tục chạy, nhưng process mới sẽ load version mới.

Trong một khoảng thời gian host có thể tồn tại mixed runtime state.

Đây là lý do reboot maintenance window đôi khi giúp đưa host về trạng thái đồng nhất sau large patch set.

## CVE không tự động nghĩa host có thể bị khai thác

Vulnerability scanner có thể báo package version gắn với CVE, nhưng distro đôi khi backport security fix mà vẫn giữ upstream version number gần cũ.

Cần xem distro security advisory, package release suffix và patch status.

Không chỉ so semantic version với upstream rồi kết luận vulnerable.

## Security advisory

Các distro thường có advisory database riêng.

Production patching nên dựa trên:

- severity;
- exploitability;
- exposure;
- asset criticality;
- vendor/distro fix availability;
- regression risk.

## Unattended upgrade

Auto-update có thể tốt cho security nhưng có risk availability nếu package restart service hoặc có incompatible change.

Một số environments chọn:

```text
auto security updates
+ staged rollout
+ canary hosts
+ rollback/recovery plan
```

Thay vì bật auto-upgrade đồng loạt trên toàn fleet.

## Immutable image model

Thay vì patch host in-place, cloud/container environments có thể rebuild image:

```text
base image mới
→ packages mới
→ test
→ deploy instances mới
→ drain instances cũ
```

Ưu điểm:

- reproducibility;
- rollback dễ hơn;
- giảm configuration drift.

Nhược điểm:

- cần image pipeline;
- patch khẩn cấp vẫn cần tốc độ build/deploy tốt.

## SBOM

**Software Bill of Materials (SBOM)** liệt kê components/dependencies trong artifact hoặc image.

SBOM hỗ trợ trả lời:

```text
“CVE này ảnh hưởng những host/image/application nào?”
```

Nó không tự động bảo đảm an toàn, nhưng tăng khả năng inventory và response.

## Package và container image

Container image dùng package manager lúc build nhưng runtime container thường không nên update packages thủ công.

Nếu chạy:

```bash
apt upgrade
```

bên trong running container rồi container bị recreate, thay đổi có thể mất.

Pattern tốt hơn:

```text
Dockerfile update
→ build image mới
→ scan/test
→ deploy image mới
```

## Multi-stage build

Container image có thể dùng build stage chứa compiler và runtime stage chỉ chứa artifacts cần thiết.

Điều này giảm attack surface và image size.

Nhưng debugging production image tối giản có thể khó hơn; cần observability/tooling strategy khác.

## Package cache và disk usage

APT/DNF cache có thể chiếm disk.

Ví dụ:

```bash
du -sh /var/cache/apt 2>/dev/null
```

Cleanup cần dùng package-manager-aware commands thay vì xóa random database files.

## Transaction history

DNF:

```bash
sudo dnf history
sudo dnf history info <ID>
```

APT:

```bash
less /var/log/apt/history.log
```

Dòng thời gian package changes rất hữu ích khi incident bắt đầu sau maintenance window.

## Kiểm tra trước upgrade production

Một workflow tốt:

```text
inventory current versions
→ refresh metadata
→ xem candidate updates
→ đọc advisory/changelog quan trọng
→ test staging/canary
→ backup/rollback readiness
→ apply
→ restart/reboot nếu cần
→ verify application health
```

Không chỉ chạy `apt upgrade -y` rồi coi như hoàn tất.

## Một case: service fail sau patch

Giả sử sau OS patch, Java app fail với native library error.

Điều tra:

```bash
journalctl -u app
ldd /path/to/native.so
rpm -qa --last | head
# hoặc
cat /var/log/apt/history.log
```

Có thể package update đổi ABI hoặc library path.

Rollback cần xem dependency và config/data compatibility, không chỉ downgrade một package riêng lẻ.

## Một case: host A lỗi, host B khỏe

So sánh package versions:

```bash
# Debian-like
dpkg-query -W > /tmp/packages.txt

# RPM-like
rpm -qa | sort > /tmp/packages.txt
```

Sau đó diff giữa hosts.

Nếu app artifact/config giống nhau nhưng package set khác, OS drift trở thành hypothesis mạnh.

## Configuration drift

In-place server tồn tại lâu có thể tích lũy:

- package versions khác nhau;
- manual edits;
- old repositories;
- disabled services;
- stale symlinks.

Infrastructure-as-code hoặc immutable image giảm drift bằng cách tái tạo thay vì sửa host mãi mãi.

## Mô hình tư duy

Package lifecycle có thể nhìn thành:

```text
trusted repository
    ↓
metadata + signature
    ↓
dependency resolution
    ↓
package transaction
    ↓
files + scripts + config
    ↓
running processes
    ↓
verification / restart / reboot
```

Một update chỉ hoàn tất khi runtime state đã thực sự dùng code mới và application health được xác minh.

## Những hiểu lầm phổ biến

**“Cài package mới nghĩa process đang chạy đã dùng version mới.”** Không; process có thể vẫn giữ binary/library mapping cũ.

**“HTTPS đủ để tin package.”** Repository signing và provenance vẫn quan trọng.

**“Checksum chứng minh file đến từ vendor.”** Checksum chỉ mạnh nếu nguồn checksum cũng được trust độc lập.

**“Downgrade package luôn rollback được.”** Data/config/schema migration có thể không tương thích ngược.

**“Version upstream thấp hơn nghĩa chắc chắn còn CVE.”** Distro có thể backport patch.

**“Auto-update luôn tốt hơn manual.”** Cần cân bằng security speed và availability/change control.

## Kết nối kiến thức

Đọc [ELF và dynamic linking](./elf_dynamic_linking.md) để hiểu tác động của shared library upgrade, [Deployment và rollback](./deployment_release_rollback.md) để hiểu release lifecycle, và [Security hardening](./security_hardening.md) để đặt patching vào threat model tổng thể.