# Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Trình quản lý gói (package manager / 패키지 관리자) quản lý nhiều hơn tệp (file / 파일)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Gói (package / 패키지) cơ sở dữ liệu (database / 데이터베이스)** để đối chiếu nhận định với dữ liệu và nguồn. Mạch này nối package lifecycle với repository, dependency, signing và rollback, để cập nhật phần mềm được nhìn như một chuỗi cung ứng có kiểm soát.

Chương [Gói phần mềm, phần mềm và thư viện dùng chung](./packages_software_libraries.md) giải thích vai trò cơ bản của trình quản lý gói (package manager / 패키지 관리자). Chương này đi sâu vào cách repository, siêu dữ liệu (metadata / 메타데이터), phụ thuộc (dependency / 의존성) solver, signing, pinning, giao dịch (transaction / 트랜잭션) lịch sử (history / 이력) và quay lui (rollback / 롤백) liên kết với độ ổn định và bảo mật của môi trường vận hành (production / 운영 환경).

## Trình quản lý gói (package manager / 패키지 관리자) quản lý nhiều hơn tệp (file / 파일)

Một gói (package / 패키지) thường mang theo:

- siêu dữ liệu (metadata / 메타데이터);
- phiên bản (version / 버전);
- phụ thuộc (dependency / 의존성) declarations;
- quyền sở hữu (ownership / 소유권) của tệp (file / 파일);
- scripts chạy trước/sau install/remove;
- checksum/signature siêu dữ liệu (metadata / 메타데이터);
- cấu hình (configuration / 구성) ngữ nghĩa (semantics / 의미론);
- vòng đời (lifecycle / 생명주기) trạng thái (state / 상태) trong gói (package / 패키지) cơ sở dữ liệu (database / 데이터베이스).

Do đó:

```bash
apt install nginx
```

không chỉ là tải nhị phân (binary / 이진) rồi bản sao (copy / 복사) vào `/usr/bin`.

Package manager không chỉ chép file; nó duy trì metadata, dependency graph, version và trạng thái cài đặt. Vì vậy cần bắt đầu từ package database để biết hệ thống đang tin vào thông tin nào.

## Gói (package / 패키지) cơ sở dữ liệu (database / 데이터베이스)

Trên Debian-family, `dpkg` giữ cơ sở dữ liệu (database / 데이터베이스) cục bộ (local / 로컬) về packages đã cài.

Một số command:

```bash
dpkg -l
dpkg -L nginx
dpkg -S /usr/sbin/nginx
```

`dpkg -L` trả lời gói (package / 패키지) sở hữu những tệp (file / 파일) nào.

`dpkg -S` trả lời tệp (file / 파일) cụ thể thuộc gói (package / 패키지) nào.

Trên RPM-family:

```bash
rpm -qa
rpm -ql nginx
rpm -qf /usr/sbin/nginx
```

Kiến thức (knowledge / 지식) này rất hữu ích khi một tệp (file / 파일) hệ thống bị sửa thủ công và cần biết gói (package / 패키지) nào sẽ ghi đè nó khi upgrade.

Package database ghi version, dependency, checksum và trạng thái transaction của gói. Các package manager tầng cao và thấp đọc/biến đổi lớp metadata này theo những vai trò khác nhau.

## Trình quản lý gói (package manager / 패키지 관리자) tầng cao và tầng thấp

Trên Debian-family:

```text
APT
 ↓
dpkg
```

APT quản lý repository và phụ thuộc (dependency / 의존성) resolution; `dpkg` thao tác gói (package / 패키지) `.deb` và cơ sở dữ liệu (database / 데이터베이스) cục bộ (local / 로컬) ở tầng thấp hơn.

Tương tự, DNF nằm trên RPM ecosystem.

Khi install `.deb` trực tiếp bằng `dpkg -i`, phụ thuộc (dependency / 의존성) có thể chưa được giải quyết như khi dùng APT.

Tầng cao điều phối policy, dependency và transaction, còn tầng thấp thực hiện unpack/configure file cụ thể. Cả hai đều phụ thuộc repository để biết artifact nào có thể lấy và tin.

## Repository là gì?

Repository chứa packages cùng siêu dữ liệu (metadata / 메타데이터) để trình quản lý gói (package manager / 패키지 관리자) biết:

- gói (package / 패키지) nào tồn tại;
- phiên bản (version / 버전) nào available;
- phụ thuộc (dependency / 의존성) gì;
- kiến trúc (architecture / 아키텍처) nào;
- checksum/signature gì.

Repository có thể là:

- official distro repository;
- vendor repository;
- nội bộ (internal / 내부) enterprise mirror;
- snapshot repository;
- testing/staging repository.

Repository là nguồn metadata và artifact có version, release channel và trust policy. `apt update` chủ yếu đồng bộ metadata; nó chưa tự cài hay nâng package.

## `apt update` thực sự làm gì?

`apt update` tải siêu dữ liệu (metadata / 메타데이터) repository về cục bộ (local / 로컬) bộ nhớ đệm (cache / 캐시).

Sau bước này trình quản lý gói (package manager / 패키지 관리자) biết candidate versions mới, nhưng chưa install chúng.

Do đó:

```bash
sudo apt update
apt list --upgradable
```

khác với:

```bash
sudo apt upgrade
```

`apt update` làm mới index để solver nhìn thấy version và dependency hiện tại. Từ index đó, candidate version được chọn dựa trên policy, pinning và trạng thái hệ thống.

## Candidate phiên bản (version / 버전)

Trình quản lý gói (package manager / 패키지 관리자) chọn **candidate phiên bản (version / 버전)** dựa trên repository priorities, kiến trúc (architecture / 아키텍처), pinning và phụ thuộc (dependency / 의존성) các ràng buộc (constraints / 제약조건들).

```bash
apt-cache policy nginx
```

có thể cho thấy:

```text
Installed: ...
Candidate: ...
Version table: ...
```

Nếu `apt install nginx` cài phiên bản (version / 버전) bất ngờ, hãy kiểm tra candidate và repository priority trước.

Candidate version là lựa chọn hiện tại của solver, không phải cam kết sẽ được cài. Pinning thêm trọng số hoặc ưu tiên để kiểm soát version/source, nhưng phải có lý do và thời hạn rõ.

## Pinning

APT pinning cho phép ưu tiên hoặc giữ phiên bản (version / 버전) theo repository/phiên bản (version / 버전) mẫu (pattern / 패턴).

Đây là công cụ mạnh nhưng có thể tạo phụ thuộc (dependency / 의존성) trạng thái (state / 상태) khó hiểu nếu dùng thiếu kiểm soát.

Môi trường vận hành (production / 운영 환경) pinning nên đi kèm documentation về lý do và thời điểm bỏ pin.

Pinning có thể giữ một nguồn hoặc version được ưu tiên; hold là chặn một package khỏi thay đổi tự động. Hai cơ chế khác nhau về phạm vi và dễ tạo drift nếu không được inventory.

## Hold gói (package / 패키지)

Debian-family có thể hold gói (package / 패키지):

```bash
sudo apt-mark hold package-name
apt-mark showhold
```

Hold giúp tránh auto-upgrade gói (package / 패키지) nhạy cảm, nhưng cũng có thể làm bảo mật (security / 보안) patch bị bỏ lỡ.

Hold là sự đánh đổi (trade-off / 트레이드오프), không phải trạng thái nên để vĩnh viễn mà không rà soát (review / 검토).

Hold giữ package khỏi transaction thông thường, còn DNF versionlock khóa các version được phép trong hệ sinh thái DNF. Sau policy version, solver vẫn phải giải dependency toàn graph.

## DNF versionlock

RHEL-family có plugin/versionlock cơ chế (mechanism / 메커니즘) tùy phân phối (distribution / 분포)/phiên bản (version / 버전).

Mục tiêu tương tự: giữ gói (package / 패키지) ở một phiên bản (version / 버전) hoặc mẫu (pattern / 패턴) xác định.

Versionlock giới hạn ứng viên nhưng không giải quyết xung đột dependency. Dependency solver cần tìm một tập version cùng tồn tại, và failure của nó phải được đọc như tín hiệu policy hoặc repository.

## Phụ thuộc (dependency / 의존성) solver

Một gói (package / 패키지) có thể yêu cầu:

```text
libA >= 2.0
libB < 5
```

Trình quản lý gói (package manager / 패키지 관리자) phải tìm tập versions thỏa các ràng buộc (constraints / 제약조건들).

Xung đột (conflict / 충돌) có thể xảy ra khi hai packages yêu cầu ranges không tương thích.

Đây là phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) bài toán (problem / 문제) giống Maven/Gradle/npm, nhưng phạm vi là operating-system trạng thái (state / 상태).

Solver nhìn cả dependency trực tiếp và gián tiếp; một thay đổi nhỏ có thể kéo theo chain lớn. Inventory hai lớp này giúp đánh giá blast radius trước khi update.

## Phụ thuộc (dependency / 의존성) trực tiếp và gián tiếp

Bạn có thể cài gói (package / 패키지) A, A kéo B, B kéo C.

Sau khi remove A, B/C có thể trở thành packages không còn cần thiết.

APT có:

```bash
sudo apt autoremove
```

Nhưng cần rà soát (review / 검토) kỹ trên môi trường vận hành (production / 운영 환경) vì gói (package / 패키지) được đánh dấu auto/manual không phải lúc nào cũng phản ánh nghiệp vụ (business / 비즈니스) phụ thuộc (dependency / 의존성) bạn mong muốn.

Dependency trực tiếp là contract của package ứng dụng, còn dependency gián tiếp thường là nơi drift và surprise xuất hiện. Recommended/suggested packages thêm lựa chọn nhưng không luôn là runtime requirement.

## Recommended và suggested packages

Debian siêu dữ liệu (metadata / 메타데이터) có thể phân biệt phụ thuộc (dependency / 의존성) bắt buộc với recommended/suggested packages.

`--no-install-recommends` thường được dùng trong ảnh bộ chứa (container image / 컨테이너 이미지) để giảm kích thước:

```bash
apt-get install --no-install-recommends package
```

Nhưng ảnh (image / 이미지) nhỏ hơn có thể thiếu utility mà debugging cần. Đây là sự đánh đổi (trade-off / 트레이드오프) giữa minimal surface và operability.

Recommended và suggested packages có semantics khác nhau giữa policy/dialect và có thể làm footprint thay đổi. Trước khi cài, cần hiểu package scripts vì chúng có thể tạo side effect ngoài file payload.

## Gói (package / 패키지) scripts

Gói (package / 패키지) có thể chạy maintainer scripts như:

```text
preinst
postinst
prerm
postrm
```

Các script này có thể:

- tạo người dùng (user / 사용자);
- reload daemon;
- migrate cấu hình (config / 설정);
- cập nhật (update / 업데이트) bộ nhớ đệm (cache / 캐시);
- restart dịch vụ (service / 서비스).

Vì vậy gói (package / 패키지) install có thể tạo side tác động (effect / 효과) lớn hơn việc bản sao (copy / 복사) tệp (file / 파일).

Trên môi trường vận hành (production / 운영 환경), cần biết upgrade gói (package / 패키지) có tự restart dịch vụ (service / 서비스) không.

Package scripts can run during install, upgrade or removal and may mutate services, users, caches or databases. Configuration files are another boundary: payload ownership and local edits affect whether an update is safe.

## Cấu hình (configuration / 구성) files

Trình quản lý gói (package manager / 패키지 관리자) thường có ngữ nghĩa (semantics / 의미론) riêng cho cấu hình (config / 설정) files dưới `/etc`.

Khi gói (package / 패키지) upgrade và tệp (file / 파일) cấu hình (config / 설정) đã bị admin sửa, công cụ (tool / 도구) có thể hỏi giữ bản cục bộ (local / 로컬) hay dùng bản maintainer.

Trong unattended automation, xung đột (conflict / 충돌) này cần chính sách (policy / 정책) rõ; nếu không triển khai (deployment / 배포) có thể treo hoặc áp cấu hình (config / 설정) không mong muốn.

Configuration files carry local intent, so the package system must distinguish shipped defaults from administrator changes. Conffile ownership and three-way decisions determine whether an upgrade preserves or overwrites that intent.

## Conffile quyền sở hữu (ownership / 소유권)

Trên Debian:

```bash
dpkg-query -W -f='${Conffiles}\n' package-name
```

có thể giúp xem cấu hình (config / 설정) files do gói (package / 패키지) quản lý.

Không nên coi toàn bộ `/etc` là “do trình quản lý gói (package manager / 패키지 관리자) sở hữu”; nhiều app/nội bộ (internal / 내부) configs được quản lý bằng cấu hình (configuration / 구성) management riêng.

Conffile handling protects local configuration only when ownership and conflict decisions are visible. Verifying package files then checks what was installed, but it does not prove repository authenticity or runtime behavior.

## Verify gói (package / 패키지) files

RPM hỗ trợ verify:

```bash
rpm -V package-name
```

Đầu ra (output / 출력) cho biết một số thuộc tính tệp (file / 파일) khác với gói (package / 패키지) siêu dữ liệu (metadata / 메타데이터).

Điều này hữu ích khi nghi nhị phân (binary / 이진)/cấu hình (config / 설정) bị sửa thủ công.

Debian có thể dùng checksum siêu dữ liệu (metadata / 메타데이터) hoặc các công cụ (tool / 도구) bổ sung tùy gói (package / 패키지).

File verification can detect missing or modified payloads relative to package metadata. Repository signing establishes authenticity and integrity of metadata/artifacts before installation, a different link in the trust chain.

## Repository signing

Trình quản lý gói (package manager / 패키지 관리자) không nên tin gói (package / 패키지) chỉ vì tải qua HTTP/HTTPS. Repository signing giúp xác minh siêu dữ liệu (metadata / 메타데이터)/gói (package / 패키지) provenance bằng cryptographic trust chuỗi (chain / 사슬).

Trên hiện đại (modern / 현대적) Debian/Ubuntu, repository keys thường được cấu hình scoped bằng `signed-by=` thay vì bỏ mọi key vào toàn cục (global / 전역) trusted keyring.

Ví dụ conceptual:

```text
repository metadata
   ↓ signature verified by trusted key
package checksum
   ↓
package content
```

Repository signatures bind metadata to a trusted signing key and policy; bypassing that chain with `curl | sudo bash` gives a remote script direct privilege without equivalent review or transaction boundaries.

## Vì sao `curl | sudo bash` là rủi ro?

Mẫu (pattern / 패턴):

```bash
curl https://vendor.example/install.sh | sudo bash
```

cho remote content quyền gốc (root / 루트) ngay lập tức.

Nếu endpoint, CDN, DNS, vendor account hoặc script bị compromise, host cũng bị ảnh hưởng.

Cách an toàn hơn:

1. download;
2. verify nguồn (source / 소스)/signature/checksum;
3. inspect script;
4. execute với privilege tối thiểu cần thiết.

`curl | sudo bash` collapses download, interpretation and privileged execution into one opaque step. A checksum can detect bytes changed relative to a known digest, while a signature also authenticates who authorized those bytes.

## Checksum khác signature

Checksum như SHA-256 giúp phát hiện content thay đổi, nhưng nếu attacker có thể thay cả tệp (file / 파일) và checksum trên cùng website thì checksum không chứng minh provenance.

Digital signature dùng private/công khai (public / 공개) key trust mô hình (model / 모델) mạnh hơn khi key phân phối (distribution / 분포) an toàn.

Checksum proves content equality only if the digest came through a trusted channel; signature binds content or metadata to a key. Internal mirrors reduce external dependency but must preserve verification and provenance.

## Nội bộ (internal / 내부) mirror

Enterprise thường dùng repository mirror nội bộ để:

- kiểm soát versions;
- giảm bandwidth;
- giữ gói (package / 패키지) khi upstream xóa;
- quét vulnerability;
- triển khai theo wave;
- hỗ trợ môi trường không ra Internet trực tiếp.

Nhưng mirror phải được cập nhật và bảo vệ; mirror cũ có thể làm patching chậm.

An internal mirror centralizes availability and policy, but it can also become a single stale or compromised source. Snapshot repositories make the exact metadata/artifact set reproducible and support controlled rollback.

## Snapshot repository

Nếu muốn reproducible host bản dựng (build / 빌드), repository “latest” không đủ.

Snapshot repository giữ trạng thái repository ở một thời điểm.

Ví dụ mô hình tư duy (mental model / 사고 모델):

```text
prod build ngày 2026-09-20
→ repository snapshot 2026-09-20
→ package versions cố định
```

Điều này giúp rebuild máy chủ (server / 서버) giống nhau hơn.

Snapshots make rollback inputs reproducible, but package rollback is not automatically safe: scripts, schemas, user data and external state may not be reversible. Kernel updates add a reboot boundary and a second booted state.

## Quay lui (rollback / 롤백) gói (package / 패키지) có đơn giản không?

Downgrade nhị phân (binary / 이진) có thể không quay lui (rollback / 롤백):

- cơ sở dữ liệu (database / 데이터베이스) lược đồ (schema / 스키마);
- dữ liệu (data / 데이터) format;
- cấu hình (config / 설정) di chuyển (migration / 마이그레이션);
- systemd đơn vị (unit / 단위) hành vi (behavior / 동작);
- bộ nhớ đệm (cache / 캐시)/chỉ mục (index / 인덱스) di chuyển (migration / 마이그레이션).

Gói (package / 패키지) quay lui (rollback / 롤백) chỉ là một phần của ứng dụng (application / 애플리케이션) quay lui (rollback / 롤백).

Kernel rollback can require selecting an older boot artifact and validating modules, initramfs and hardware behavior. Shared libraries create a different boundary: running processes may keep old mappings while new processes load new code.

## Kernel gói (package / 패키지) và reboot

Cài kernel gói (package / 패키지) mới không có nghĩa kernel đang chạy đã đổi.

Kiểm tra:

```bash
uname -r
```

và packages installed.

Có thể có nhiều kernel versions trên disk; bootloader chọn kernel khi reboot.

Bảo mật (security / 보안) patch kernel thường cần reboot hoặc live patch cơ chế (mechanism / 메커니즘) nếu được hỗ trợ.

Shared-library upgrades can leave a mixed process population, so package completion is not the same as runtime convergence. Restart policy determines when services actually begin using the patched library.

## Dùng chung (shared / 공유) thư viện (library / 라이브러리) upgrade và tiến trình (process / 프로세스) đang chạy

Nếu thư viện (library / 라이브러리) trên disk được nâng cấp, tiến trình (process / 프로세스) đang chạy thường vẫn dùng ánh xạ (mapping / 매핑)/thư viện (library / 라이브러리) đã tải (load / 로드) trước đó.

Do đó gói (package / 패키지) upgrade không chắc đã đưa bảo mật (security / 보안) fix vào tiến trình (process / 프로세스) cho tới khi tiến trình (process / 프로세스) restart.

Có công cụ (tool / 도구) trên một số distro giúp phát hiện processes dùng deleted/old libraries.

Ví dụ generic:

```bash
sudo lsof +L1
```

có thể thấy mapped deleted files trong một số trường hợp.

Restarting after an update must be driven by process/library state and service criticality, not a blanket reboot habit. glibc and other core libraries raise the blast radius and require especially explicit validation.

## Restart sau gói (package / 패키지) cập nhật (update / 업데이트)

Cần biết thành phần (component / 컴포넌트) nào phải restart sau upgrade.

Có thể là:

- ứng dụng (application / 애플리케이션) dịch vụ (service / 서비스);
- SSH daemon;
- cơ sở dữ liệu (database / 데이터베이스);
- host reboot nếu kernel/glibc/cốt lõi (core / 핵심) thư viện (library / 라이브러리) thay đổi sâu.

Không restart mọi thứ một cách mù quáng; cần thay đổi (change / 변경) plan và availability chiến lược (strategy / 전략).

Core-library updates can require coordinated service restarts, but restart scope should follow actual linkage and availability requirements. After runtime convergence, CVE assessment asks whether a published issue is exploitable in this host context.

## glibc và cốt lõi (core / 핵심) libraries

Nâng cốt lõi (core / 핵심) thư viện (library / 라이브러리) có phạm vi ảnh hưởng lớn vì nhiều processes phụ thuộc.

Running processes đã map old thư viện (library / 라이브러리) có thể tiếp tục chạy, nhưng tiến trình (process / 프로세스) mới sẽ tải (load / 로드) phiên bản (version / 버전) mới.

Trong một khoảng thời gian host có thể tồn tại mixed thời gian chạy (runtime / 런타임) trạng thái (state / 상태).

Đây là lý do reboot maintenance cửa sổ (window / 윈도우) đôi khi giúp đưa host về trạng thái đồng nhất sau large patch set.

glibc and other core libraries amplify the consequence of a bad update, yet a CVE score alone does not prove exploitability. Advisory interpretation must combine affected version, reachable configuration, exposure and available mitigations.

## CVE không tự động nghĩa host có thể bị khai thác

Vulnerability scanner có thể báo gói (package / 패키지) phiên bản (version / 버전) gắn với CVE, nhưng distro đôi khi backport bảo mật (security / 보안) fix mà vẫn giữ upstream phiên bản (version / 버전) number gần cũ.

Cần xem distro bảo mật (security / 보안) advisory, gói (package / 패키지) bản phát hành (release / 릴리스) suffix và patch status.

Không chỉ so ngữ nghĩa (semantic / 의미적) phiên bản (version / 버전) với upstream rồi kết luận vulnerable.

A CVE advisory is a risk signal with version and configuration conditions, not an automatic incident declaration. Unattended upgrades turn that signal into an automated lifecycle, so scope, timing and rollback evidence must be explicit.

## Bảo mật (security / 보안) advisory

Các distro thường có advisory cơ sở dữ liệu (database / 데이터베이스) riêng.

Môi trường vận hành (production / 운영 환경) patching nên dựa trên:

- severity;
- exploitability;
- exposure;
- asset criticality;
- vendor/distro fix availability;
- regression rủi ro (risk / 위험).

Unattended upgrades reduce patch lag but can change packages without a human at the moment of execution. Immutable images shift the control point earlier: build and test a complete artifact, then replace rather than mutate hosts in place.

## Unattended upgrade

Auto-update có thể tốt cho bảo mật (security / 보안) nhưng có rủi ro (risk / 위험) availability nếu gói (package / 패키지) restart dịch vụ (service / 서비스) hoặc có incompatible thay đổi (change / 변경).

Một số environments chọn:

```text
auto security updates
+ staged rollout
+ canary hosts
+ rollback/recovery plan
```

Thay vì bật auto-upgrade đồng loạt trên toàn fleet.

Immutable images improve repeatability only when the image build inputs and provenance are controlled. SBOM records the components inside the artifact so a new advisory can be mapped to affected images and rebuild scope.

## Immutable ảnh (image / 이미지) mô hình (model / 모델)

Thay vì patch host in-place, cloud/bộ chứa (container / 컨테이너) environments có thể rebuild ảnh (image / 이미지):

```text
base image mới
→ packages mới
→ test
→ deploy instances mới
→ drain instances cũ
```

Ưu điểm:

- reproducibility;
- quay lui (rollback / 롤백) dễ hơn;
- giảm cấu hình (configuration / 구성) drift.

Nhược điểm:

- cần ảnh (image / 이미지) chuỗi xử lý (pipeline / 파이프라인);
- patch khẩn cấp vẫn cần tốc độ bản dựng (build / 빌드)/deploy tốt.

SBOM connects component inventory to remediation, but it does not prove a component is safe or present at runtime. Container images add another packaging boundary where host packages, image layers and runtime mounts must be distinguished.

## SBOM

**Software Bill of Materials (SBOM)** liệt kê components/dependencies trong sản phẩm tạo ra (artifact / 산출물) hoặc ảnh (image / 이미지).

SBOM hỗ trợ trả lời:

```text
“CVE này ảnh hưởng những host/image/application nào?”
```

Nó không tự động bảo đảm an toàn, nhưng tăng khả năng inventory và phản hồi (response / 응답).

Container images may carry OS packages and application dependencies in layered form. Multi-stage builds reduce the final attack surface by separating build-time tools from the runtime artifact, but reproducibility still depends on pinned inputs.

## Gói (package / 패키지) và ảnh bộ chứa (container image / 컨테이너 이미지)

Ảnh bộ chứa (container image / 컨테이너 이미지) dùng trình quản lý gói (package manager / 패키지 관리자) lúc bản dựng (build / 빌드) nhưng thời gian chạy (runtime / 런타임) bộ chứa (container / 컨테이너) thường không nên cập nhật (update / 업데이트) packages thủ công.

Nếu chạy:

```bash
apt upgrade
```

bên trong running bộ chứa (container / 컨테이너) rồi bộ chứa (container / 컨테이너) bị recreate, thay đổi có thể mất.

Mẫu (pattern / 패턴) tốt hơn:

```text
Dockerfile update
→ build image mới
→ scan/test
→ deploy image mới
```

Multi-stage builds reduce unnecessary payload, while package caches trade speed for disk usage and stale or untrusted artifacts. Cache policy must define retention, provenance and eviction rather than treating cached bytes as neutral.

## Multi-stage bản dựng (build / 빌드)

Ảnh bộ chứa (container image / 컨테이너 이미지) có thể dùng bản dựng (build / 빌드) stage chứa trình biên dịch (compiler / 컴파일러) và thời gian chạy (runtime / 런타임) stage chỉ chứa artifacts cần thiết.

Điều này giảm attack surface và ảnh (image / 이미지) kích thước (size / 크기).

Nhưng debugging môi trường vận hành (production / 운영 환경) ảnh (image / 이미지) tối giản có thể khó hơn; cần khả năng quan sát (observability / 관측 가능성)/tooling chiến lược (strategy / 전략) khác.

Package caches can hide which artifact was fetched and consume enough disk to change upgrade behavior. Transaction history restores observability: it records requested changes, solver decisions and outcomes for audit or recovery.

## Gói (package / 패키지) bộ nhớ đệm (cache / 캐시) và disk usage

APT/DNF bộ nhớ đệm (cache / 캐시) có thể chiếm disk.

Ví dụ:

```bash
du -sh /var/cache/apt 2>/dev/null
```

Cleanup cần dùng package-manager-aware commands thay vì xóa random cơ sở dữ liệu (database / 데이터베이스) files.

Transaction history supports diagnosis but cannot replace a pre-upgrade check. Before production, validate disk, repository reachability, locks, service health, backups and a rollback path appropriate to the package change.

## Giao dịch (transaction / 트랜잭션) lịch sử (history / 이력)

DNF:

```bash
sudo dnf history
sudo dnf history info <ID>
```

APT:

```bash
less /var/log/apt/history.log
```

Dòng thời gian gói (package / 패키지) changes rất hữu ích khi sự cố (incident / 인시던트) bắt đầu sau maintenance cửa sổ (window / 윈도우).

Pre-upgrade checks reduce avoidable failure, but production still has unknown interactions. A service failure after patch should be analyzed as a timeline linking package transaction, config, process state and external dependencies.

## Kiểm tra trước upgrade môi trường vận hành (production / 운영 환경)

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

A post-patch service failure needs a bounded rollback or forward-fix decision, with evidence preserved before changing more state. Host A/host B comparison provides a natural control when one host remains healthy.

## Một trường hợp (case / 사례): dịch vụ (service / 서비스) thất bại (fail / 실패) sau patch

Giả sử sau OS patch, Java app thất bại (fail / 실패) với bản địa (native / 네이티브) thư viện (library / 라이브러리) lỗi (error / 오류).

Điều tra:

```bash
journalctl -u app
ldd /path/to/native.so
rpm -qa --last | head
# hoặc
cat /var/log/apt/history.log
```

Có thể gói (package / 패키지) cập nhật (update / 업데이트) đổi ABI hoặc thư viện (library / 라이브러리) đường dẫn (path / 경로).

Quay lui (rollback / 롤백) cần xem phụ thuộc (dependency / 의존성) và cấu hình (config / 설정)/dữ liệu (data / 데이터) tính tương thích (compatibility / 호환성), không chỉ downgrade một gói (package / 패키지) riêng lẻ.

Comparing a failed host with a healthy peer can separate package change from shared dependency or workload effects, but only if versions, traffic and configuration are comparable. Configuration drift is the next boundary to inventory.

## Một trường hợp (case / 사례): host A lỗi, host B khỏe

So sánh gói (package / 패키지) versions:

```bash
# Debian-like
dpkg-query -W > /tmp/packages.txt

# RPM-like
rpm -qa | sort > /tmp/packages.txt
```

Sau đó diff giữa hosts.

Nếu app sản phẩm tạo ra (artifact / 산출물)/cấu hình (config / 설정) giống nhau nhưng gói (package / 패키지) set khác, OS drift trở thành hypothesis mạnh.

Configuration drift explains why nominally identical hosts can react differently to the same update. The mental model should therefore follow package metadata, trust chain, transaction, runtime state and evidence of convergence.

## Cấu hình (configuration / 구성) drift

In-place máy chủ (server / 서버) tồn tại lâu có thể tích lũy:

- gói (package / 패키지) versions khác nhau;
- manual edits;
- old repositories;
- disabled services;
- stale symlinks.

Infrastructure-as-code hoặc immutable ảnh (image / 이미지) giảm drift bằng cách tái tạo thay vì sửa host mãi mãi.

Mô hình tư duy tốt nối package identity → verified source → dependency solve → transaction → runtime restart → observed health. Những hiểu lầm phổ biến thường bỏ qua một mắt xích và gọi package installation là hoàn tất.

## Mô hình tư duy

Gói (package / 패키지) vòng đời (lifecycle / 생명주기) có thể nhìn thành:

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

Một cập nhật (update / 업데이트) chỉ hoàn tất khi thời gian chạy (runtime / 런타임) trạng thái (state / 상태) đã thực sự dùng mã (code / 코드) mới và ứng dụng (application / 애플리케이션) health được xác minh.

Misconceptions như checksum = signature, CVE = exploit, rollback = undo hay image = reproducibility đều làm sai boundary của supply chain. Sửa chúng giúp nối bài với provenance, SBOM và operational recovery.

## Những hiểu lầm phổ biến

**“Cài gói (package / 패키지) mới nghĩa tiến trình (process / 프로세스) đang chạy đã dùng phiên bản (version / 버전) mới.”** Không; tiến trình (process / 프로세스) có thể vẫn giữ nhị phân (binary / 이진)/thư viện (library / 라이브러리) ánh xạ (mapping / 매핑) cũ.

**“HTTPS đủ để tin gói (package / 패키지).”** Repository signing và provenance vẫn quan trọng.

**“Checksum chứng minh tệp (file / 파일) đến từ vendor.”** Checksum chỉ mạnh nếu nguồn checksum cũng được trust độc lập.

**“Downgrade gói (package / 패키지) luôn quay lui (rollback / 롤백) được.”** dữ liệu (data / 데이터)/cấu hình (config / 설정)/lược đồ (schema / 스키마) di chuyển (migration / 마이그레이션) có thể không tương thích ngược.

**“phiên bản (version / 버전) upstream thấp hơn nghĩa chắc chắn còn CVE.”** Distro có thể backport patch.

**“Auto-update luôn tốt hơn manual.”** Cần cân bằng bảo mật (security / 보안) speed và availability/thay đổi (change / 변경) điều khiển (control / 제어).

Package repositories nối metadata, trust, lifecycle và runtime operations thành một supply chain có thể audit. Kết luận chỉ đáng tin khi nêu rõ artifact, nguồn tin, state sau update và giới hạn rollback.

## Kết nối kiến thức

Đọc [ELF và dynamic linking](./elf_dynamic_linking.md) để hiểu tác động của dùng chung (shared / 공유) thư viện (library / 라이브러리) upgrade, [Deployment và rollback](./deployment_release_rollback.md) để hiểu bản phát hành (release / 릴리스) vòng đời (lifecycle / 생명주기), và [Security hardening](./security_hardening.md) để đặt patching vào threat mô hình (model / 모델) tổng thể.

> **Bàn giao:** Sau **Kết nối kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
