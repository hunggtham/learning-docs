# Gói phần mềm, phần mềm và thư viện dùng chung

> **Mạch đọc:** Đọc **Gói phần mềm, phần mềm và thư viện dùng chung** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Trình quản lý gói giải quyết vấn đề gì?** sang **Kho phần mềm và chỉ mục gói**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Một tệp thực thi không tồn tại độc lập với hệ thống. Nó có phiên bản, các phụ thuộc, cấu hình, thư viện dùng chung, chủ sở hữu và vòng đời cập nhật. **trình quản lý gói (package manager / 패키지 관리자)** tồn tại để biến việc cài phần mềm từ "chép vài tệp vào đâu đó" thành một trạng thái có siêu dữ liệu (metadata / 메타데이터) và đồ thị phụ thuộc có thể quản lý.

## Trình quản lý gói giải quyết vấn đề gì?

Nếu cài phần mềm thủ công, quản trị viên phải tự nhớ tệp nào được đặt ở đâu, thư viện nào cần có trước, phiên bản nào tương thích và làm sao gỡ hoặc nâng cấp. Hệ thống gói lưu siêu dữ liệu (metadata / 메타데이터) để quản lý các quan hệ đó.

Họ Debian/Ubuntu dùng gói `.deb` với hệ sinh thái `dpkg`/APT; họ RHEL dùng RPM với DNF/YUM.

```bash
cat /etc/os-release
```

Đây nên là một trong những bước đầu tiên để biết bản phân phối trước khi sao chép câu lệnh cài gói từ Internet.

## Kho phần mềm và chỉ mục gói

`apt update` không có nghĩa "nâng cấp Linux". Nó làm mới siêu dữ liệu (metadata / 메타데이터) về các gói từ những kho đã cấu hình:

```bash
sudo apt update
```

Sau đó `apt install` giải quyết quan hệ phụ thuộc và cài phiên bản ứng viên:

```bash
sudo apt install lsof
```

`apt upgrade` mới thực hiện nâng cấp các gói đã cài theo chính sách của bộ giải phụ thuộc.

Trên họ RHEL:

```bash
sudo dnf install lsof
sudo dnf upgrade
```

## Đồ thị phụ thuộc

Giả sử ứng dụng A cần thư viện B từ phiên bản X trở lên. Bộ giải phụ thuộc của trình quản lý gói (package manager / 패키지 관리자) cố tìm một tập phiên bản thỏa các ràng buộc. Đây cùng một lớp bài toán với việc giải phụ thuộc (dependency / 의존성) trong Maven, Gradle hoặc npm, nhưng nằm ở tầng gói của hệ điều hành.

Mối liên hệ quan trọng là cả phụ thuộc (dependency / 의존성) của dự án Java và phụ thuộc (dependency / 의존성) gói Linux đều quản lý đồ thị có hướng cùng ràng buộc phiên bản, nhưng phạm vi khác nhau. phụ thuộc (dependency / 의존성) Maven đi vào sản phẩm tạo ra (artifact / 산출물) hoặc classpath của ứng dụng; gói hệ điều hành có thể cài chương trình và thư viện dùng chung cho toàn hệ thống.

## Thư viện dùng chung

Tệp thực thi bản địa (native / 네이티브) có thể liên kết động với **thư viện dùng chung (shared library)**. Có thể xem các phụ thuộc bằng:

```bash
ldd /usr/bin/curl
```

Nếu chương trình thất bại vì thiếu dùng chung (shared / 공유) đối tượng (object / 객체), vấn đề không nhất thiết là tệp thực thi không tồn tại; bộ nạp động (dynamic loader) có thể không tìm được thư viện cần thiết.

Cần thận trọng khi dùng `ldd` với tệp nhị phân không đáng tin trên một số hệ thống hoặc cách triển khai. Trong bối cảnh bảo mật cao, nên ưu tiên tệp hệ thống đáng tin cậy hoặc công cụ kiểm tra an toàn hơn.

## `PATH` và cách shell tìm câu lệnh

Shell tìm tệp thực thi dựa trên `$PATH`:

```bash
command -v java
printf '%s\n' "$PATH" | tr ':' '\n'
```

Hai bản Java có thể cùng tồn tại trên máy; thứ tự trong `PATH` quyết định câu lệnh nào được shell chọn.

Để giải liên kết tượng trưng tới tệp thật:

```bash
readlink -f "$(command -v java)"
```

Đây là cách tốt để biết Java thực sự đang chạy từ đâu thay vì chỉ nhìn `JAVA_HOME`.

## Gói hệ thống và cài đặt thủ công

Phần mềm cài thủ công thường được đặt ở `/opt`, `/usr/local` hoặc đường dẫn riêng của ứng dụng. trình quản lý gói (package manager / 패키지 관리자) không tự biết những tệp đó. Vì vậy gỡ một gói không xóa phần mềm mà bạn từng giải nén thủ công vào `/opt`.

Ngược lại, nếu tự ghi đè một tệp thuộc quyền quản lý của trình quản lý gói (package manager / 패키지 관리자), lần nâng cấp tiếp theo có thể thay thế thay đổi đó.

## Phiên bản và khả năng tái tạo hệ thống

Chỉ ghi "cài nginx" chưa đủ để tái tạo một máy chủ nếu kho phần mềm hoặc phiên bản ứng viên thay đổi theo thời gian. Hạ tầng môi trường vận hành (production / 운영 환경) cần chính sách phiên bản, nguồn repository và quản lý cấu hình rõ ràng.

```bash
apt-cache policy nginx
rpm -q nginx
```

Công cụ cụ thể phụ thuộc bản phân phối.

## Cập nhật bảo mật

Cập nhật gói không chỉ thêm tính năng; nhiều bản vá bảo mật đi qua repository của bản phân phối. Tuy nhiên vá môi trường vận hành (production / 운영 환경) cần kiểm thử và quản lý thay đổi vì nâng thư viện có thể ảnh hưởng khả năng tương thích.

Không vá có rủi ro; vá không kiểm soát cũng có rủi ro. Vận hành bảo mật là quá trình cân bằng các đánh đổi dựa trên bằng chứng và mức độ ảnh hưởng.

## Lịch sử thay đổi gói

DNF cung cấp lịch sử giao dịch:

```bash
sudo dnf history
```

APT/dpkg thường có nhật ký trong `/var/log/apt` và `/var/log/dpkg.log`, tùy bản phân phối. Khi sự cố bắt đầu "sau tối qua", dòng thời gian thay đổi gói là một nguồn bằng chứng quan trọng.

## Bộ chứa (container / 컨테이너) thay đổi phạm vi gói như thế nào?

Ảnh bộ chứa (container / 컨테이너) thường đóng gói một hệ thống tệp không gian người dùng riêng nhưng vẫn sử dụng kernel của host. Gói được cài trong ảnh (image / 이미지)/bộ chứa (container / 컨테이너) không đồng nghĩa với gói được cài trên host. Điều này giảm một số xung đột phụ thuộc (dependency / 의존성) nhưng không loại bỏ việc quản lý lỗ hổng và phiên bản; vòng đời chỉ chuyển sang quá trình xây dựng và triển khai ảnh (image / 이미지).

## Mô hình tư duy (mental model / 사고 모델)

Trình quản lý gói (package manager / 패키지 관리자) là **trình quản lý trạng thái và phụ thuộc của phần mềm ở tầng hệ điều hành**. Đừng coi `apt install` chỉ là câu lệnh tải tệp; nó thay đổi trạng thái hệ thống dựa trên siêu dữ liệu (metadata / 메타데이터) repository, kết quả giải phụ thuộc (dependency / 의존성) và các script đi kèm gói.

## Những hiểu lầm phổ biến (Common Misconceptions)

**"`apt update` nâng cấp các gói."** Nó chủ yếu làm mới siêu dữ liệu (metadata / 메타데이터) của repository.

**"`command -v` không thấy nghĩa là phần mềm chưa cài."** Tệp thực thi có thể tồn tại nhưng không nằm trong `PATH`.

**"`JAVA_HOME` quyết định câu lệnh `java`."** Shell chủ yếu tìm `java` theo `PATH`; một số ứng dụng hoặc công cụ mới sử dụng `JAVA_HOME` theo cách riêng.

**"Cài bằng tar và bằng apt là giống nhau."** trình quản lý gói (package manager / 패키지 관리자) chỉ quản lý trạng thái và tệp nằm trong cơ sở dữ liệu gói của nó.

**"môi trường vận hành (production / 운영 환경) nên nâng cấp càng nhanh càng tốt."** Cần cân bằng độ khẩn cấp bảo mật với khả năng tương thích, kiểm thử và kiểm soát thay đổi.

## Kết nối kiến thức

Vòng đời gói phần mềm liên kết trực tiếp với [Bảo mật và gia cố hệ thống](./security_hardening.md), triển khai dịch vụ systemd và khả năng tái tạo môi trường vận hành (production / 운영 환경).

> **Bàn giao:** Sau **Kết nối kiến thức**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [backup restore disaster recovery](./backup_restore_disaster_recovery.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
