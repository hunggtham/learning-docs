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

> **Chuyển mạch:** Trong **Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)**, **Trình quản lý gói (package manager / 패키지 관리자) quản lý nhiều hơn tệp (file / 파일)** nêu điều cần giải thích; **Gói (package / 패키지) cơ sở dữ liệu (database / 데이터베이스)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Trình quản lý gói (package manager / 패키지 관리자) tầng cao và tầng thấp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)**, **Gói (package / 패키지) cơ sở dữ liệu (database / 데이터베이스)** nêu điều cần giải thích; **Trình quản lý gói (package manager / 패키지 관리자) tầng cao và tầng thấp** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Repository là gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)**, **Repository là gì?** tiếp nhận điểm tựa từ **Trình quản lý gói (package manager / 패키지 관리자) tầng cao và tầng thấp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **apt update thực sự làm gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)**, **apt update thực sự làm gì?** tiếp nhận điểm tựa từ **Repository là gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Candidate phiên bản (version / 버전)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)**, **Candidate phiên bản (version / 버전)** tiếp nhận điểm tựa từ **apt update thực sự làm gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Pinning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)**, **Pinning** tiếp nhận điểm tựa từ **Candidate phiên bản (version / 버전)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hold gói (package / 패키지)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Pinning

APT pinning cho phép ưu tiên hoặc giữ phiên bản (version / 버전) theo repository/phiên bản (version / 버전) mẫu (pattern / 패턴).

Đây là công cụ mạnh nhưng có thể tạo phụ thuộc (dependency / 의존성) trạng thái (state / 상태) khó hiểu nếu dùng thiếu kiểm soát.

Môi trường vận hành (production / 운영 환경) pinning nên đi kèm documentation về lý do và thời điểm bỏ pin.

> **Chuyển mạch:** Trong **Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)**, **Hold gói (package / 패키지)** tiếp nhận điểm tựa từ **Pinning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **DNF versionlock** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hold gói (package / 패키지)

Debian-family có thể hold gói (package / 패키지):

```bash
sudo apt-mark hold package-name
apt-mark showhold
```

Hold giúp tránh auto-upgrade gói (package / 패키지) nhạy cảm, nhưng cũng có thể làm bảo mật (security / 보안) patch bị bỏ lỡ.

Hold là sự đánh đổi (trade-off / 트레이드오프), không phải trạng thái nên để vĩnh viễn mà không rà soát (review / 검토).

> **Chuyển mạch:** Ở chặng này của **Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)**, **DNF versionlock** tiếp nhận điểm tựa từ **Hold gói (package / 패키지)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phụ thuộc (dependency / 의존성) solver** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## DNF versionlock

RHEL-family có plugin/versionlock cơ chế (mechanism / 메커니즘) tùy phân phối (distribution / 분포)/phiên bản (version / 버전).

Mục tiêu tương tự: giữ gói (package / 패키지) ở một phiên bản (version / 버전) hoặc mẫu (pattern / 패턴) xác định.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)**, **Phụ thuộc (dependency / 의존성) solver** tiếp nhận điểm tựa từ **DNF versionlock** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phụ thuộc (dependency / 의존성) trực tiếp và gián tiếp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phụ thuộc (dependency / 의존성) solver

Một gói (package / 패키지) có thể yêu cầu:

```text
libA >= 2.0
libB < 5
```

Trình quản lý gói (package manager / 패키지 관리자) phải tìm tập versions thỏa các ràng buộc (constraints / 제약조건들).

Xung đột (conflict / 충돌) có thể xảy ra khi hai packages yêu cầu ranges không tương thích.

Đây là phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) bài toán (problem / 문제) giống Maven/Gradle/npm, nhưng phạm vi là operating-system trạng thái (state / 상태).

> **Chuyển mạch:** Trong **Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)**, **Phụ thuộc (dependency / 의존성) trực tiếp và gián tiếp** tiếp nhận điểm tựa từ **Phụ thuộc (dependency / 의존성) solver** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Recommended và suggested packages** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phụ thuộc (dependency / 의존성) trực tiếp và gián tiếp

Bạn có thể cài gói (package / 패키지) A, A kéo B, B kéo C.

Sau khi remove A, B/C có thể trở thành packages không còn cần thiết.

APT có:

```bash
sudo apt autoremove
```

Nhưng cần rà soát (review / 검토) kỹ trên môi trường vận hành (production / 운영 환경) vì gói (package / 패키지) được đánh dấu auto/manual không phải lúc nào cũng phản ánh nghiệp vụ (business / 비즈니스) phụ thuộc (dependency / 의존성) bạn mong muốn.

> **Chuyển mạch:** Ở chặng này của **Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)**, **Recommended và suggested packages** tiếp nhận điểm tựa từ **Phụ thuộc (dependency / 의존성) trực tiếp và gián tiếp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Gói (package / 패키지) scripts** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Recommended và suggested packages

Debian siêu dữ liệu (metadata / 메타데이터) có thể phân biệt phụ thuộc (dependency / 의존성) bắt buộc với recommended/suggested packages.

`--no-install-recommends` thường được dùng trong ảnh bộ chứa (container image / 컨테이너 이미지) để giảm kích thước:

```bash
apt-get install --no-install-recommends package
```

Nhưng ảnh (image / 이미지) nhỏ hơn có thể thiếu utility mà debugging cần. Đây là sự đánh đổi (trade-off / 트레이드오프) giữa minimal surface và operability.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)**, **Gói (package / 패키지) scripts** tiếp nhận điểm tựa từ **Recommended và suggested packages** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cấu hình (configuration / 구성) files** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)**, **Cấu hình (configuration / 구성) files** tiếp nhận điểm tựa từ **Gói (package / 패키지) scripts** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Conffile quyền sở hữu (ownership / 소유권)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cấu hình (configuration / 구성) files

Trình quản lý gói (package manager / 패키지 관리자) thường có ngữ nghĩa (semantics / 의미론) riêng cho cấu hình (config / 설정) files dưới `/etc`.

Khi gói (package / 패키지) upgrade và tệp (file / 파일) cấu hình (config / 설정) đã bị admin sửa, công cụ (tool / 도구) có thể hỏi giữ bản cục bộ (local / 로컬) hay dùng bản maintainer.

Trong unattended automation, xung đột (conflict / 충돌) này cần chính sách (policy / 정책) rõ; nếu không triển khai (deployment / 배포) có thể treo hoặc áp cấu hình (config / 설정) không mong muốn.

> **Chuyển mạch:** Ở chặng này của **Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)**, sau nội dung của **Cấu hình (configuration / 구성) files**, **Conffile quyền sở hữu (ownership / 소유권)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Verify gói (package / 패키지) files** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Conffile quyền sở hữu (ownership / 소유권)

Trên Debian:

```bash
dpkg-query -W -f='${Conffiles}\n' package-name
```

có thể giúp xem cấu hình (config / 설정) files do gói (package / 패키지) quản lý.

Không nên coi toàn bộ `/etc` là “do trình quản lý gói (package manager / 패키지 관리자) sở hữu”; nhiều app/nội bộ (internal / 내부) configs được quản lý bằng cấu hình (configuration / 구성) management riêng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)**, **Verify gói (package / 패키지) files** tiếp nhận điểm tựa từ **Conffile quyền sở hữu (ownership / 소유권)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Repository signing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Verify gói (package / 패키지) files

RPM hỗ trợ verify:

```bash
rpm -V package-name
```

Đầu ra (output / 출력) cho biết một số thuộc tính tệp (file / 파일) khác với gói (package / 패키지) siêu dữ liệu (metadata / 메타데이터).

Điều này hữu ích khi nghi nhị phân (binary / 이진)/cấu hình (config / 설정) bị sửa thủ công.

Debian có thể dùng checksum siêu dữ liệu (metadata / 메타데이터) hoặc các công cụ (tool / 도구) bổ sung tùy gói (package / 패키지).

> **Chuyển mạch:** Trong **Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)**, **Repository signing** tiếp nhận điểm tựa từ **Verify gói (package / 패키지) files** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vì sao curl | sudo bash là rủi ro?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)**, **Vì sao curl | sudo bash là rủi ro?** tiếp nhận điểm tựa từ **Repository signing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Checksum khác signature** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)**, **Checksum khác signature** tiếp nhận điểm tựa từ **Vì sao curl | sudo bash là rủi ro?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Nội bộ (internal / 내부) mirror** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Checksum khác signature

Checksum như SHA-256 giúp phát hiện content thay đổi, nhưng nếu attacker có thể thay cả tệp (file / 파일) và checksum trên cùng website thì checksum không chứng minh provenance.

Digital signature dùng private/công khai (public / 공개) key trust mô hình (model / 모델) mạnh hơn khi key phân phối (distribution / 분포) an toàn.

> **Chuyển mạch:** Trong **Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)**, **Nội bộ (internal / 내부) mirror** tiếp nhận điểm tựa từ **Checksum khác signature** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Snapshot repository** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nội bộ (internal / 내부) mirror

Enterprise thường dùng repository mirror nội bộ để:

- kiểm soát versions;
- giảm bandwidth;
- giữ gói (package / 패키지) khi upstream xóa;
- quét vulnerability;
- triển khai theo wave;
- hỗ trợ môi trường không ra Internet trực tiếp.

Nhưng mirror phải được cập nhật và bảo vệ; mirror cũ có thể làm patching chậm.

> **Chuyển mạch:** Ở chặng này của **Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)**, **Snapshot repository** tiếp nhận điểm tựa từ **Nội bộ (internal / 내부) mirror** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Quay lui (rollback / 롤백) gói (package / 패키지) có đơn giản không?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)**, **Quay lui (rollback / 롤백) gói (package / 패키지) có đơn giản không?** tiếp nhận điểm tựa từ **Snapshot repository** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kernel gói (package / 패키지) và reboot** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quay lui (rollback / 롤백) gói (package / 패키지) có đơn giản không?

Downgrade nhị phân (binary / 이진) có thể không quay lui (rollback / 롤백):

- cơ sở dữ liệu (database / 데이터베이스) lược đồ (schema / 스키마);
- dữ liệu (data / 데이터) format;
- cấu hình (config / 설정) di chuyển (migration / 마이그레이션);
- systemd đơn vị (unit / 단위) hành vi (behavior / 동작);
- bộ nhớ đệm (cache / 캐시)/chỉ mục (index / 인덱스) di chuyển (migration / 마이그레이션).

Gói (package / 패키지) quay lui (rollback / 롤백) chỉ là một phần của ứng dụng (application / 애플리케이션) quay lui (rollback / 롤백).

> **Chuyển mạch:** Trong **Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)**, **Kernel gói (package / 패키지) và reboot** tiếp nhận điểm tựa từ **Quay lui (rollback / 롤백) gói (package / 패키지) có đơn giản không?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dùng chung (shared / 공유) thư viện (library / 라이브러리) upgrade và tiến trình (process / 프로세스) đang chạy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kernel gói (package / 패키지) và reboot

Cài kernel gói (package / 패키지) mới không có nghĩa kernel đang chạy đã đổi.

Kiểm tra:

```bash
uname -r
```

và packages installed.

Có thể có nhiều kernel versions trên disk; bootloader chọn kernel khi reboot.

Bảo mật (security / 보안) patch kernel thường cần reboot hoặc live patch cơ chế (mechanism / 메커니즘) nếu được hỗ trợ.

> **Chuyển mạch:** Ở chặng này của **Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)**, **Kernel gói (package / 패키지) và reboot** xác định đầu vào; **Dùng chung (shared / 공유) thư viện (library / 라이브러리) upgrade và tiến trình (process / 프로세스) đang chạy** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Restart sau gói (package / 패키지) cập nhật (update / 업데이트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (shared / 공유) thư viện (library / 라이브러리) upgrade và tiến trình (process / 프로세스) đang chạy

Nếu thư viện (library / 라이브러리) trên disk được nâng cấp, tiến trình (process / 프로세스) đang chạy thường vẫn dùng ánh xạ (mapping / 매핑)/thư viện (library / 라이브러리) đã tải (load / 로드) trước đó.

Do đó gói (package / 패키지) upgrade không chắc đã đưa bảo mật (security / 보안) fix vào tiến trình (process / 프로세스) cho tới khi tiến trình (process / 프로세스) restart.

Có công cụ (tool / 도구) trên một số distro giúp phát hiện processes dùng deleted/old libraries.

Ví dụ generic:

```bash
sudo lsof +L1
```

có thể thấy mapped deleted files trong một số trường hợp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)**, **Dùng chung (shared / 공유) thư viện (library / 라이브러리) upgrade và tiến trình (process / 프로세스) đang chạy** xác định đầu vào; **Restart sau gói (package / 패키지) cập nhật (update / 업데이트)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **glibc và cốt lõi (core / 핵심) libraries** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Restart sau gói (package / 패키지) cập nhật (update / 업데이트)

Cần biết thành phần (component / 컴포넌트) nào phải restart sau upgrade.

Có thể là:

- ứng dụng (application / 애플리케이션) dịch vụ (service / 서비스);
- SSH daemon;
- cơ sở dữ liệu (database / 데이터베이스);
- host reboot nếu kernel/glibc/cốt lõi (core / 핵심) thư viện (library / 라이브러리) thay đổi sâu.

Không restart mọi thứ một cách mù quáng; cần thay đổi (change / 변경) plan và availability chiến lược (strategy / 전략).

> **Chuyển mạch:** Trong **Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)**, **glibc và cốt lõi (core / 핵심) libraries** tiếp nhận điểm tựa từ **Restart sau gói (package / 패키지) cập nhật (update / 업데이트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **CVE không tự động nghĩa host có thể bị khai thác** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## glibc và cốt lõi (core / 핵심) libraries

Nâng cốt lõi (core / 핵심) thư viện (library / 라이브러리) có phạm vi ảnh hưởng lớn vì nhiều processes phụ thuộc.

Running processes đã map old thư viện (library / 라이브러리) có thể tiếp tục chạy, nhưng tiến trình (process / 프로세스) mới sẽ tải (load / 로드) phiên bản (version / 버전) mới.

Trong một khoảng thời gian host có thể tồn tại mixed thời gian chạy (runtime / 런타임) trạng thái (state / 상태).

Đây là lý do reboot maintenance cửa sổ (window / 윈도우) đôi khi giúp đưa host về trạng thái đồng nhất sau large patch set.

> **Chuyển mạch:** Ở chặng này của **Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)**, **CVE không tự động nghĩa host có thể bị khai thác** tiếp nhận điểm tựa từ **glibc và cốt lõi (core / 핵심) libraries** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bảo mật (security / 보안) advisory** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## CVE không tự động nghĩa host có thể bị khai thác

Vulnerability scanner có thể báo gói (package / 패키지) phiên bản (version / 버전) gắn với CVE, nhưng distro đôi khi backport bảo mật (security / 보안) fix mà vẫn giữ upstream phiên bản (version / 버전) number gần cũ.

Cần xem distro bảo mật (security / 보안) advisory, gói (package / 패키지) bản phát hành (release / 릴리스) suffix và patch status.

Không chỉ so ngữ nghĩa (semantic / 의미적) phiên bản (version / 버전) với upstream rồi kết luận vulnerable.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)**, **Bảo mật (security / 보안) advisory** tiếp nhận điểm tựa từ **CVE không tự động nghĩa host có thể bị khai thác** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Unattended upgrade** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bảo mật (security / 보안) advisory

Các distro thường có advisory cơ sở dữ liệu (database / 데이터베이스) riêng.

Môi trường vận hành (production / 운영 환경) patching nên dựa trên:

- severity;
- exploitability;
- exposure;
- asset criticality;
- vendor/distro fix availability;
- regression rủi ro (risk / 위험).

> **Chuyển mạch:** Trong **Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)**, **Unattended upgrade** tiếp nhận điểm tựa từ **Bảo mật (security / 보안) advisory** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Immutable ảnh (image / 이미지) mô hình (model / 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)**, **Immutable ảnh (image / 이미지) mô hình (model / 모델)** tiếp nhận điểm tựa từ **Unattended upgrade** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **SBOM** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)**, **SBOM** tiếp nhận điểm tựa từ **Immutable ảnh (image / 이미지) mô hình (model / 모델)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Gói (package / 패키지) và ảnh bộ chứa (container image / 컨테이너 이미지)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## SBOM

**Software Bill of Materials (SBOM)** liệt kê components/dependencies trong sản phẩm tạo ra (artifact / 산출물) hoặc ảnh (image / 이미지).

SBOM hỗ trợ trả lời:

```text
“CVE này ảnh hưởng những host/image/application nào?”
```

Nó không tự động bảo đảm an toàn, nhưng tăng khả năng inventory và phản hồi (response / 응답).

> **Chuyển mạch:** Trong **Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)**, **Gói (package / 패키지) và ảnh bộ chứa (container image / 컨테이너 이미지)** tiếp nhận điểm tựa từ **SBOM** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Multi-stage bản dựng (build / 빌드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)**, **Multi-stage bản dựng (build / 빌드)** tiếp nhận điểm tựa từ **Gói (package / 패키지) và ảnh bộ chứa (container image / 컨테이너 이미지)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Gói (package / 패키지) bộ nhớ đệm (cache / 캐시) và disk usage** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Multi-stage bản dựng (build / 빌드)

Ảnh bộ chứa (container image / 컨테이너 이미지) có thể dùng bản dựng (build / 빌드) stage chứa trình biên dịch (compiler / 컴파일러) và thời gian chạy (runtime / 런타임) stage chỉ chứa artifacts cần thiết.

Điều này giảm attack surface và ảnh (image / 이미지) kích thước (size / 크기).

Nhưng debugging môi trường vận hành (production / 운영 환경) ảnh (image / 이미지) tối giản có thể khó hơn; cần khả năng quan sát (observability / 관측 가능성)/tooling chiến lược (strategy / 전략) khác.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)**, **Gói (package / 패키지) bộ nhớ đệm (cache / 캐시) và disk usage** tiếp nhận điểm tựa từ **Multi-stage bản dựng (build / 빌드)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Giao dịch (transaction / 트랜잭션) lịch sử (history / 이력)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Gói (package / 패키지) bộ nhớ đệm (cache / 캐시) và disk usage

APT/DNF bộ nhớ đệm (cache / 캐시) có thể chiếm disk.

Ví dụ:

```bash
du -sh /var/cache/apt 2>/dev/null
```

Cleanup cần dùng package-manager-aware commands thay vì xóa random cơ sở dữ liệu (database / 데이터베이스) files.

> **Chuyển mạch:** Trong **Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)**, **Giao dịch (transaction / 트랜잭션) lịch sử (history / 이력)** tiếp nhận điểm tựa từ **Gói (package / 패키지) bộ nhớ đệm (cache / 캐시) và disk usage** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kiểm tra trước upgrade môi trường vận hành (production / 운영 환경)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)**, **Kiểm tra trước upgrade môi trường vận hành (production / 운영 환경)** tiếp nhận điểm tựa từ **Giao dịch (transaction / 트랜잭션) lịch sử (history / 이력)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Một trường hợp (case / 사례): dịch vụ (service / 서비스) thất bại (fail / 실패) sau patch** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)**, **Kiểm tra trước upgrade môi trường vận hành (production / 운영 환경)** cho ta quy tắc; **Một trường hợp (case / 사례): dịch vụ (service / 서비스) thất bại (fail / 실패) sau patch** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Một trường hợp (case / 사례): host A lỗi, host B khỏe** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)**, **Một trường hợp (case / 사례): dịch vụ (service / 서비스) thất bại (fail / 실패) sau patch** cho ta quy tắc; **Một trường hợp (case / 사례): host A lỗi, host B khỏe** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Cấu hình (configuration / 구성) drift** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)**, **Một trường hợp (case / 사례): host A lỗi, host B khỏe** cho ta quy tắc; **Cấu hình (configuration / 구성) drift** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cấu hình (configuration / 구성) drift

In-place máy chủ (server / 서버) tồn tại lâu có thể tích lũy:

- gói (package / 패키지) versions khác nhau;
- manual edits;
- old repositories;
- disabled services;
- stale symlinks.

Infrastructure-as-code hoặc immutable ảnh (image / 이미지) giảm drift bằng cách tái tạo thay vì sửa host mãi mãi.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)**, **Mô hình tư duy** gom các mảnh từ **Cấu hình (configuration / 구성) drift** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những hiểu lầm phổ biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)**, **Những hiểu lầm phổ biến** gom các mảnh từ **Mô hình tư duy** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu lầm phổ biến

**“Cài gói (package / 패키지) mới nghĩa tiến trình (process / 프로세스) đang chạy đã dùng phiên bản (version / 버전) mới.”** Không; tiến trình (process / 프로세스) có thể vẫn giữ nhị phân (binary / 이진)/thư viện (library / 라이브러리) ánh xạ (mapping / 매핑) cũ.

**“HTTPS đủ để tin gói (package / 패키지).”** Repository signing và provenance vẫn quan trọng.

**“Checksum chứng minh tệp (file / 파일) đến từ vendor.”** Checksum chỉ mạnh nếu nguồn checksum cũng được trust độc lập.

**“Downgrade gói (package / 패키지) luôn quay lui (rollback / 롤백) được.”** dữ liệu (data / 데이터)/cấu hình (config / 설정)/lược đồ (schema / 스키마) di chuyển (migration / 마이그레이션) có thể không tương thích ngược.

**“phiên bản (version / 버전) upstream thấp hơn nghĩa chắc chắn còn CVE.”** Distro có thể backport patch.

**“Auto-update luôn tốt hơn manual.”** Cần cân bằng bảo mật (security / 보안) speed và availability/thay đổi (change / 변경) điều khiển (control / 제어).

> **Chuyển mạch:** Ở chặng này của **Gói (package / 패키지) vòng đời (lifecycle / 생명주기) sâu hơn: repository, cập nhật (update / 업데이트), phụ thuộc (dependency / 의존성) và software supply chuỗi (chain / 사슬)**, **Kết nối kiến thức** tiếp nhận điểm tựa từ **Những hiểu lầm phổ biến** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối kiến thức

Đọc [ELF và dynamic linking](./elf_dynamic_linking.md) để hiểu tác động của dùng chung (shared / 공유) thư viện (library / 라이브러리) upgrade, [Deployment và rollback](./deployment_release_rollback.md) để hiểu bản phát hành (release / 릴리스) vòng đời (lifecycle / 생명주기), và [Security hardening](./security_hardening.md) để đặt patching vào threat mô hình (model / 모델) tổng thể.

> **Bàn giao:** Sau **Kết nối kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
