# Quá trình khởi động, systemd và dịch vụ

Một máy chủ cần chuyển từ trạng thái "máy vừa bật" sang trạng thái mà mạng đã sẵn sàng, hệ thống tệp đã được gắn, ứng dụng chạy đúng danh tính, nhật ký có nơi thu thập và các phụ thuộc được quản lý. Nếu chỉ dùng một chuỗi script shell không có mô hình phụ thuộc, việc khởi động và phục hồi dịch vụ sẽ nhanh chóng trở nên khó kiểm soát. Trên nhiều bản phân phối Linux hiện đại, **systemd** đảm nhiệm vai trò trình quản lý hệ thống và dịch vụ.

## Từ firmware tới không gian người dùng

Luồng khởi động (boot flow) thay đổi theo nền tảng, nhưng có thể hình dung:

```text
firmware -> bootloader -> Linux kernel -> early userspace/initramfs -> root filesystem -> PID 1 -> services/targets
```

Kernel khởi tạo phần cứng và các hệ thống con cần thiết rồi bắt đầu tiến trình `init` trong không gian người dùng. Với hệ thống sử dụng systemd, systemd trở thành `PID 1`.

```bash
ps -p 1 -o pid,comm,args
```

`PID 1` có quy tắc đặc biệt liên quan tới vòng đời hệ thống và việc thu nhận trạng thái của tiến trình con.

## Vì sao trình quản lý dịch vụ cần đồ thị phụ thuộc?

Cơ sở dữ liệu có thể cần hệ thống tệp và mạng trước khi khởi động. Ứng dụng có thể cần cơ sở dữ liệu nhưng không nên giải quyết bằng cách cố định `sleep 30`. Systemd mô tả các **đơn vị (unit)** và quan hệ giữa chúng theo thứ tự và phụ thuộc thay vì chỉ dựa vào thời gian chờ giả định.

Điểm quan trọng là **thứ tự (ordering)** và **yêu cầu phụ thuộc (requirement)** là hai khái niệm khác nhau. `After=` chỉ định thứ tự khi các unit cùng được đưa vào quá trình khởi động; nó không tự động kéo unit kia vào. `Requires=` và `Wants=` mô tả các mức quan hệ phụ thuộc khác nhau.

Vì vậy sao chép một unit file mà không hiểu các chỉ thị có thể tạo ra lỗi tranh chấp trong quá trình khởi động (boot race).

## Unit là gì?

Systemd quản lý nhiều loại unit như `.service`, `.socket`, `.timer`, `.mount`, `.target`... Dịch vụ chỉ là một loại trong số đó.

Xem nội dung unit:

```bash
systemctl cat app.service
```

Xem các thuộc tính đã được systemd phân giải:

```bash
systemctl show app.service -p MainPID -p User -p Group -p ExecStart
```

`systemctl cat` đặc biệt hữu ích vì nó hiển thị unit cùng các cấu hình bổ sung (drop-in) thực tế, tốt hơn việc đoán tệp nằm trong `/etc/systemd/system` hay `/usr/lib/systemd/system`.

## Vòng đời dịch vụ

Các câu lệnh quen thuộc:

```bash
sudo systemctl start app
sudo systemctl stop app
sudo systemctl restart app
sudo systemctl status app
```

`restart` là một thay đổi trạng thái lớn. Khi xảy ra sự cố, nếu điều kiện cho phép nên thu thập bằng chứng trước:

```bash
systemctl status app --no-pager
journalctl -u app -n 300 --no-pager
systemctl show app -p MainPID -p ExecMainStatus
```

Sau khi khởi động lại, trạng thái gây lỗi ban đầu có thể biến mất.

## `reload` khác `restart`

Nếu daemon hỗ trợ nạp lại cấu hình, `reload` yêu cầu tiến trình đang chạy đọc cấu hình mới mà không dừng rồi khởi động lại toàn bộ:

```bash
sudo nginx -t && sudo systemctl reload nginx
```

Ở đây `nginx -t` kiểm tra cấu hình trước; `&&` bảo đảm chỉ reload khi bước kiểm tra thành công.

Không phải dịch vụ nào cũng hỗ trợ reload. `systemctl reload app` không tự tạo ra khả năng này nếu bản thân ứng dụng không triển khai cơ chế nạp lại.

## `enable` khác `start`

```bash
systemctl is-active app
systemctl is-enabled app
```

`active` nói về trạng thái khi đang chạy hiện tại. `enabled` nói về quan hệ kích hoạt để unit có thể được khởi động theo mục tiêu boot. Một dịch vụ có thể đang hoạt động nhưng vẫn `disabled` nếu quản trị viên khởi động thủ công.

```bash
sudo systemctl enable --now app
```

thường vừa bật tự khởi động vừa khởi động ngay dịch vụ.

## Unit file và môi trường thực thi

Ví dụ đơn giản:

```ini
[Unit]
Description=Example Java service
After=network.target

[Service]
User=app
Group=app
WorkingDirectory=/opt/app
ExecStart=/usr/bin/java -jar /opt/app/app.jar
Restart=on-failure
Environment=SPRING_PROFILES_ACTIVE=prod

[Install]
WantedBy=multi-user.target
```

Điểm cần hiểu là dịch vụ không chạy bên trong phiên SSH tương tác của bạn. `PATH`, `JAVA_HOME`, thư mục làm việc hiện tại, `umask` và giới hạn tài nguyên có thể khác. Vì vậy tình huống "chạy tay được nhưng service không chạy" thường liên quan môi trường, danh tính hoặc đường dẫn.

Nên dùng đường dẫn tuyệt đối và khai báo rõ các biến môi trường thật sự cần thiết.

## `daemon-reload`

Sau khi thay đổi unit file hoặc cấu hình drop-in:

```bash
sudo systemctl daemon-reload
```

systemd sẽ nạp lại định nghĩa các unit. Lệnh này **không tự khởi động lại ứng dụng**. Nếu tiến trình đang chạy cần dùng cấu hình mới, hành động tiếp theo phụ thuộc vào loại thay đổi.

## Chính sách khởi động lại

`Restart=on-failure` có thể giúp dịch vụ phục hồi sau lỗi tạm thời, nhưng vòng lặp khởi động lại liên tục cũng có thể che nguyên nhân gốc và tạo thêm tải. Systemd có cơ chế giới hạn tần suất khởi động. Sau khi sửa nguyên nhân, có thể cần:

```bash
sudo systemctl reset-failed app
```

Không nên coi `reset-failed` là cách sửa lỗi; nó chỉ đặt lại trạng thái thất bại và bộ đếm liên quan trong trình quản lý.

## Dừng dịch vụ có kiểm soát

Khi dừng dịch vụ, systemd gửi signal theo cấu hình, thường bắt đầu bằng `SIGTERM`. Ứng dụng cần xử lý quá trình dừng đúng cách để ngừng nhận lưu lượng mới, hoàn tất hoặc hủy công việc an toàn, ghi nốt trạng thái cần thiết và đóng tài nguyên.

Nếu ứng dụng không dừng trong khoảng thời gian cho phép, trình quản lý có thể chuyển sang biện pháp mạnh hơn. Xem thêm [Tiến trình, luồng, tín hiệu và tác vụ](../04_process/processes_threads_signals_jobs.md).

## Target

**Target unit** dùng để nhóm và đồng bộ trạng thái hệ thống, có vai trò gần với khái niệm runlevel cũ nhưng dựa trên đồ thị phụ thuộc. `multi-user.target` thường đại diện trạng thái nhiều người dùng không có giao diện đồ họa; `graphical.target` kéo thêm môi trường đồ họa khi có.

```bash
systemctl get-default
systemctl list-dependencies multi-user.target
```

## Kích hoạt bằng socket và bộ hẹn giờ

Systemd có thể quản lý socket unit và chỉ khởi động dịch vụ khi lưu lượng tới, hoặc dùng timer unit thay cho `cron` trong nhiều tình huống. Điều này cho thấy systemd không chỉ là công cụ để "restart service", mà là trình quản lý vòng đời và quan hệ phụ thuộc của hệ thống.

Bộ hẹn giờ được trình bày thêm tại [Lập lịch và tự động hóa](../08_operations/scheduling_automation.md).

## Xử lý khi dịch vụ không khởi động được

Một chuỗi quan sát tốt:

```bash
systemctl status app --no-pager
journalctl -xeu app
systemctl cat app
systemctl show app -p User -p Group -p WorkingDirectory -p ExecStart
```

Sau đó kiểm tra đường dẫn, quyền, môi trường, chương trình thực thi và các phụ thuộc dựa trên lỗi cụ thể.

Nếu Java không được tìm thấy khi chạy dưới systemd nhưng lại chạy được trong SSH shell, hãy kiểm tra `ExecStart` và đường dẫn tuyệt đối thay vì thêm `PATH` ngẫu nhiên.

## Mô hình tư duy (Mental Model)

Systemd là **trình giám sát tiến trình có hiểu quan hệ phụ thuộc và trình quản lý trạng thái hệ thống**. Unit file là mô tả khai báo về cách tài nguyên hoặc dịch vụ tham gia vào đồ thị hệ thống; `systemctl` là công cụ khách để yêu cầu systemd thay đổi hoặc báo cáo trạng thái.

## Những hiểu lầm phổ biến (Common Misconceptions)

**"`enable` = `start`."** `enable` chủ yếu ảnh hưởng việc kích hoạt theo boot/phụ thuộc; `start` tác động tới trạng thái chạy hiện tại.

**"`restart` là bước gỡ lỗi đầu tiên."** Khởi động lại là can thiệp làm mất một phần bằng chứng; nên quan sát trước khi thay đổi nếu có thể.

**"Dịch vụ có môi trường giống SSH shell."** Không. Trình quản lý dịch vụ tạo ngữ cảnh thực thi riêng.

**"`After=network.target` nghĩa là Internet hoặc DNS chắc chắn đã sẵn sàng."** Quan hệ thứ tự của target không chứng minh phụ thuộc mạng ở mức ứng dụng đã khỏe mạnh.

**"`systemctl status` chứa toàn bộ nhật ký."** Nó chỉ hiển thị một phần ngữ cảnh gần đây; dùng `journalctl` để truy vấn sâu hơn.

## Kết nối kiến thức

Systemd tạo ra ranh giới vòng đời cho dịch vụ. [Nhật ký và khả năng quan sát](./logging_journal_observability.md) giải thích cách journal gắn sự kiện với unit. Các giới hạn tài nguyên và chỉ thị bảo mật của systemd cũng liên kết trực tiếp với các chương về bộ nhớ, tiến trình và gia cố hệ thống.