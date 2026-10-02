# Lưu trữ, thiết bị khối và hệ thống tệp

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Lưu trữ, thiết bị khối và hệ thống tệp**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Thiết bị khối là lớp trừu tượng gì?** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Phân vùng và volume** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối storage, block device và filesystem, để theo dõi dữ liệu từ ghi logic đến durability và phục hồi sau lỗi.

Khi `df -h` báo 100%, phản xạ phổ biến là tìm tệp lớn để xóa. Nhưng ngăn xếp lưu trữ (storage stack) của Linux có nhiều lớp: thiết bị khối vật lý hoặc ảo, phân vùng, ánh xạ volume, hệ thống tệp, vùng tên mount, tệp/`inode` và các tham chiếu đang mở. Hiểu từng lớp giúp phân biệt các tình huống như "hết dung lượng", "hết inode", "tệp đã xóa nhưng vẫn đang mở" hoặc "gắn sai filesystem".

## Thiết bị khối là lớp trừu tượng gì?

Ổ đĩa, SSD hoặc ổ đĩa ảo được kernel trình bày dưới dạng **thiết bị khối (block device / 블록 장치)**. Ứng dụng thông thường không đọc trực tiếp thiết bị khối thô; hệ thống tệp tổ chức các khối (block / 블록) thành tệp và thư mục.

```bash
lsblk
lsblk -f
```

`lsblk -f` giúp nhìn cây thiết bị, loại hệ thống tệp, UUID và các điểm gắn kết.

> **Chuyển mạch:** Trong **Lưu trữ, thiết bị khối và hệ thống tệp**, **Phân vùng và volume** tiếp nhận điểm tựa từ **Thiết bị khối là lớp trừu tượng gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hệ thống tệp và mount** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phân vùng và volume

Một ổ đĩa có thể được chia thành nhiều phân vùng. Hệ thống doanh nghiệp hoặc đám mây còn thường dùng LVM hay lớp ảo hóa lưu trữ để tách **volume lô-gic (logic / 논리) (logical volume)** khỏi bố trí ổ đĩa vật lý.

Mô hình LVM đơn giản:

```text
physical volume -> volume group -> logical volume -> filesystem -> mount point
```

Lớp trung gian này cho phép quản lý dung lượng linh hoạt hơn phân vùng cố định, nhưng cũng tạo thêm các bước cần kiểm tra khi mở rộng. Việc tăng kích thước ổ đĩa ảo trên cloud không có nghĩa hệ thống tệp tự động lớn lên theo.

> **Chuyển mạch:** Ở chặng này của **Lưu trữ, thiết bị khối và hệ thống tệp**, **Hệ thống tệp và mount** tiếp nhận điểm tựa từ **Phân vùng và volume** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **df đo gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hệ thống tệp và mount

Các hệ thống tệp như ext4 hoặc XFS quản lý phân bổ khối, siêu dữ liệu (metadata / 메타데이터) và vùng tên nội bộ. Để không gian người dùng truy cập, hệ thống tệp được **gắn (mount)** vào cây thư mục chung:

```bash
findmnt
findmnt /data
df -Th
```

`df -Th` cho biết loại filesystem và mức sử dụng. `findmnt` giúp trả lời một đường dẫn đang thuộc mount nào và nguồn lưu trữ nào.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lưu trữ, thiết bị khối và hệ thống tệp**, **df đo gì?** tiếp nhận điểm tựa từ **Hệ thống tệp và mount** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **du đo gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `df` đo gì?

`df` hỏi hệ thống tệp về dung lượng khối đã dùng và còn khả dụng:

```bash
df -h /var/log
```

Kết quả thường có tổng dung lượng, đã dùng, còn trống và tỷ lệ phần trăm. Nếu `/var/log` nằm trên một mount riêng, chỉ nhìn `df -h /` có thể bỏ sót vấn đề.

> **Chuyển mạch:** Trong **Lưu trữ, thiết bị khối và hệ thống tệp**, **du đo gì?** tiếp nhận điểm tựa từ **df đo gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tệp đã xóa nhưng vẫn đang mở** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `du` đo gì?

`du` duyệt các mục trong cây thư mục và cộng dung lượng của những đối tượng mà nó nhìn thấy:

```bash
sudo du -xhd1 /var 2>/dev/null | sort -hr
```

`-x` giữ việc duyệt trong cùng hệ thống tệp. Đây là chi tiết quan trọng nếu `/var` chứa một điểm gắn kết khác.

Nếu `df` báo dùng rất nhiều nhưng `du` không tìm thấy lượng dữ liệu tương ứng, nên nghĩ tới tệp đã xóa nhưng vẫn mở, hoặc phần dung lượng dành cho siêu dữ liệu (metadata / 메타데이터)/hệ thống tệp, trước khi kết luận công cụ đo sai.

> **Chuyển mạch:** Ở chặng này của **Lưu trữ, thiết bị khối và hệ thống tệp**, **Tệp đã xóa nhưng vẫn đang mở** tiếp nhận điểm tựa từ **du đo gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Inode** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tệp đã xóa nhưng vẫn đang mở

Một tiến trình có thể giữ `inode` sau khi tên đường dẫn đã bị `unlink`. Các khối (block / 블록) dữ liệu chưa thể được thu hồi cho tới khi tham chiếu đang mở cuối cùng được đóng.

```bash
sudo lsof +L1
```

Nếu thấy một tiến trình vẫn giữ nhật ký đã xóa có kích thước hàng chục GB, đóng hoặc khởi động lại đúng tiến trình có thể giải phóng dung lượng. Tuy nhiên cần hiểu cơ chế ghi và xoay vòng nhật ký của ứng dụng để vấn đề không lặp lại.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lưu trữ, thiết bị khối và hệ thống tệp**, **Inode** tiếp nhận điểm tựa từ **Tệp đã xóa nhưng vẫn đang mở** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tệp thưa (sparse file)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Inode

Hệ thống tệp cần các đối tượng siêu dữ liệu (metadata / 메타데이터). Rất nhiều tệp nhỏ có thể làm cạn tài nguyên `inode` trước khi dùng hết số byte lưu trữ:

```bash
df -i
```

Khi inode đạt 100%, thao tác tạo tệp có thể thất bại với `No space left on device` dù `df -h` vẫn cho thấy còn dung lượng.

> **Chuyển mạch:** Trong **Lưu trữ, thiết bị khối và hệ thống tệp**, **Tệp thưa (sparse file)** tiếp nhận điểm tựa từ **Inode** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bộ nhớ đệm trang và ghi dữ liệu xuống thiết bị** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tệp thưa (sparse file)

**Tệp thưa (sparse file)** có kích thước lô-gic (logic / 논리) lớn nhưng không cấp phát khối (block / 블록) cho mọi vùng toàn số 0. Vì vậy `ls -lh` và `du -h` có thể báo kích thước khác nhau.

```bash
ls -lh file
du -h file
```

`ls` thường hiển thị kích thước biểu kiến hoặc lô-gic (logic / 논리), còn `du` phản ánh các khối (block / 블록) thực tế được cấp phát theo quy tắc của công cụ và filesystem.

Đây là phản ví dụ quan trọng cho giả định rằng "kích thước tệp luôn bằng dung lượng đĩa đã dùng".

> **Chuyển mạch:** Ở chặng này của **Lưu trữ, thiết bị khối và hệ thống tệp**, **Tệp thưa (sparse file)** nêu điều cần giải thích; **Bộ nhớ đệm trang và ghi dữ liệu xuống thiết bị** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Tùy chọn mount** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bộ nhớ đệm trang và ghi dữ liệu xuống thiết bị

Linux dùng RAM làm **bộ nhớ đệm trang (page cache)** để tăng hiệu năng I/O. Khi ứng dụng ghi tệp, dữ liệu có thể nằm trong bộ nhớ trước khi được đẩy xuống thiết bị lưu trữ. `write()` trả thành công không luôn đồng nghĩa dữ liệu đã tồn tại bền vững sau mất điện.

Vì vậy tính bền vững của cơ sở dữ liệu phải quan tâm `fsync` và cam kết của tầng lưu trữ. Đây là mối liên hệ giữa quy tắc hệ thống tệp của hệ điều hành và tính bền vững (durability) trong ACID.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lưu trữ, thiết bị khối và hệ thống tệp**, **Bộ nhớ đệm trang và ghi dữ liệu xuống thiết bị** nêu điều cần giải thích; **Tùy chọn mount** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **/etc/fstab** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tùy chọn mount

Mount có các tùy chọn ảnh hưởng hành vi, bảo mật và hiệu năng như `ro`, `noexec` cùng nhiều thiết lập riêng của từng filesystem.

```bash
findmnt -o TARGET,SOURCE,FSTYPE,OPTIONS /data
```

Một tệp có bit thực thi nhưng nằm trên mount `noexec` vẫn có thể không chạy theo cách mong đợi. Vì vậy gỡ lỗi quyền truy cập không thể chỉ dừng ở `chmod`.

> **Chuyển mạch:** Trong **Lưu trữ, thiết bị khối và hệ thống tệp**, **/etc/fstab** tiếp nhận điểm tựa từ **Tùy chọn mount** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hệ thống tệp chỉ đọc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `/etc/fstab`

Cấu hình mount lâu dài thường nằm trong `/etc/fstab`. Một mục sai có thể ảnh hưởng quá trình khởi động. Trước khi thay đổi môi trường vận hành (production / 운영 환경), cần sao lưu và hiểu ý nghĩa UUID, thiết bị và điểm gắn kết.

```bash
cat /etc/fstab
findmnt --verify
```

Khả năng hỗ trợ `findmnt --verify` phụ thuộc phiên bản `util-linux`, nhưng đây là công cụ hữu ích để kiểm tra cấu hình.

> **Chuyển mạch:** Ở chặng này của **Lưu trữ, thiết bị khối và hệ thống tệp**, **Hệ thống tệp chỉ đọc** tiếp nhận điểm tựa từ **/etc/fstab** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hiệu năng I/O** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hệ thống tệp chỉ đọc

Filesystem có thể được gắn ở chế độ chỉ đọc do cấu hình hoặc bị kernel chuyển sang trạng thái chỉ đọc sau lỗi nghiêm trọng, tùy loại hệ thống tệp và tình huống. Khi đó ứng dụng có thể báo lỗi ghi dù các bit quyền nhìn vẫn đúng.

```bash
findmnt -o TARGET,OPTIONS /path
journalctl -k --since today
```

Nhật ký kernel có thể chứa lỗi I/O hoặc filesystem trong khi ứng dụng chỉ biểu hiện bằng một lỗi ghi chung chung.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lưu trữ, thiết bị khối và hệ thống tệp**, **Hiệu năng I/O** tiếp nhận điểm tựa từ **Hệ thống tệp chỉ đọc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy về LVM** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hiệu năng I/O

Dung lượng và độ trễ là hai chiều hoàn toàn khác nhau. Thiết bị còn nhiều chỗ trống vẫn có thể bị bão hòa hoặc phản hồi chậm.

```bash
iostat -xz 1 10
```

Các số liệu như `await`, hàng đợi và mức sử dụng cần được hiểu trong bối cảnh thiết bị và khối lượng công việc; không nên áp một ngưỡng duy nhất cho mọi loại lưu trữ. Với lưu trữ mạng hoặc cloud, giới hạn dịch vụ như IOPS và thông lượng (throughput / 처리량) càng quan trọng.

> **Chuyển mạch:** Trong **Lưu trữ, thiết bị khối và hệ thống tệp**, **Mô hình tư duy về LVM** gom các mảnh từ **Hiệu năng I/O** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy về LVM

LVM thêm một lớp ánh xạ gián tiếp: hệ thống tệp không nhất thiết nằm trực tiếp trên phân vùng vật lý. Khi cần tăng dung lượng, luồng có thể là mở rộng ổ đĩa bên dưới → PV → LV → hệ thống tệp, nhưng câu lệnh chính xác phụ thuộc topology và filesystem đang dùng.

Không nên sao chép `lvextend`, `resize2fs` hoặc `xfs_growfs` trước khi xác định cấu trúc bằng:

```bash
lsblk
pvs
vgs
lvs
findmnt
```

> **Chuyển mạch:** Ở chặng này của **Lưu trữ, thiết bị khối và hệ thống tệp**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Mô hình tư duy về LVM** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những hiểu lầm phổ biến (Common Misconceptions)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Khi xử lý sự cố lưu trữ, hãy đi từ vùng tên xuống lớp vật lý:

```text
đường dẫn
 -> điểm mount
 -> hệ thống tệp
 -> logical volume / phân vùng
 -> thiết bị khối
 -> hệ thống lưu trữ bên dưới
```

Đồng thời cần theo dõi các tham chiếu đang mở (`lsof`), dung lượng `inode` và độ trễ I/O. Từ "disk" trong giao tiếp hàng ngày thường đang gộp nhiều lớp khác nhau.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lưu trữ, thiết bị khối và hệ thống tệp**, **Những hiểu lầm phổ biến (Common Misconceptions)** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu lầm phổ biến (Common Misconceptions)

**"`df` và `du` phải cho số giống nhau."** Hai công cụ đo theo cơ chế khác nhau.

**"Xóa tệp lớn luôn giải phóng dung lượng ngay."** Không nếu tệp còn được tiến trình giữ mở.

**"`No space left` luôn nghĩa là hết GB."** Có thể hệ thống đã hết inode.

**"Kích thước từ `ls` bằng dung lượng thực tế đã cấp phát."** Sparse tệp (file / 파일) là phản ví dụ rõ ràng.

**"Ổ còn trống nghĩa là lưu trữ khỏe."** Độ trễ, IOPS hoặc thông lượng (throughput / 처리량) vẫn có thể là nút thắt.

**"Tăng virtual disk thì filesystem tự tăng."** Có thể còn các lớp phân vùng, LVM và filesystem phải mở rộng riêng.

> **Chuyển mạch:** Trong **Lưu trữ, thiết bị khối và hệ thống tệp**, **Kết nối kiến thức** tiếp nhận điểm tựa từ **Những hiểu lầm phổ biến (Common Misconceptions)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối kiến thức

Lưu trữ gắn chặt với [Hệ thống tệp và inode](../01_filesystem/filesystem_paths_inodes_links.md), [Bộ nhớ](./memory_virtual_memory.md) thông qua page bộ nhớ đệm (cache / 캐시) và [Xử lý sự cố production](../09_production/production_troubleshooting.md) khi áp lực lưu trữ làm dịch vụ thất bại theo cách gián tiếp.

> **Bàn giao:** Sau **Kết nối kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
