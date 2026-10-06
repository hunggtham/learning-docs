# VFS, page bộ nhớ đệm (cache / 캐시) và writeback trong Linux

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **VFS, page bộ nhớ đệm (cache / 캐시) và writeback trong Linux**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Vì sao cần VFS?** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Các đối tượng quan trọng trong VFS** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối VFS với page cache và writeback để theo dõi cùng một lần đọc/ghi từ tên tệp đến lúc dữ liệu được ghi xuống thiết bị.

Các chương trước đã giải thích đường dẫn, inode, bộ mô tả tệp và journaling. Tuy nhiên, để hiểu đầy đủ việc “đọc một tệp (file / 파일)” hoặc “ghi một tệp (file / 파일)” trong Linux thực sự đi qua những lớp nào, cần thêm một tầng trung gian rất quan trọng: **VFS (Virtual file system)** và **page bộ nhớ đệm (cache / 캐시)**.

VFS giúp kernel cung cấp một giao diện tương đối thống nhất cho ext4, XFS, tmpfs, procfs, NFS và nhiều filesystem khác. Page bộ nhớ đệm (cache / 캐시) giúp hệ thống dùng RAM để tránh phải truy cập thiết bị lưu trữ ở mọi lần đọc/ghi. Khi ghép hai khái niệm này với cơ chế ghi ngược (writeback), ta có thể giải thích nhiều hiện tượng môi trường vận hành (production / 운영 환경) như: tệp (file / 파일) đã ghi nhưng chưa thực sự xuống disk, `free` thấp nhưng hệ thống vẫn khỏe, ghi burst nhanh lúc đầu rồi chậm dần, hoặc ứng dụng (application / 애플리케이션) độ trễ (latency / 지연 시간) tăng khi kernel phải flush dirty pages.

## Vì sao cần VFS?

Nếu mỗi ứng dụng phải biết ext4 dùng cấu trúc inode thế nào, XFS tổ chức siêu dữ liệu (metadata / 메타데이터) ra sao hoặc NFS gửi yêu cầu (request / 요청) qua mạng bằng giao thức gì, API thao tác tệp (file / 파일) sẽ cực kỳ phức tạp. Linux giải quyết bằng một lớp trừu tượng gọi là **VFS (Virtual File System / hệ thống tệp ảo)**.

Ứng dụng gọi các lời gọi hệ thống như:

```text
openat()
read()
write()
stat()
close()
```

Kernel nhận yêu cầu rồi đi qua VFS. Sau đó VFS gọi hiện thực (implementation / 구현) phù hợp của filesystem thật.

Có thể hình dung:

```text
application
   ↓
system call
   ↓
VFS
   ↓
ext4 / XFS / tmpfs / NFS / procfs / ...
   ↓
block layer hoặc network
```

VFS vì vậy không phải một filesystem lưu dữ liệu riêng. Nó là lớp giao diện và đối tượng chung để kernel thao tác nhiều filesystem theo cùng một mô hình.

> **Nối mạch:** Trong **VFS, page bộ nhớ đệm (cache / 캐시) và writeback trong Linux**, **Các đối tượng quan trọng trong VFS** nối từ **Vì sao cần VFS?** sang **Dentry bộ nhớ đệm (cache / 캐시) và vì sao đường dẫn (path / 경로) lookup có thể nhanh**, vì cơ chế trước tạo đầu vào cho bước sau.

## Các đối tượng quan trọng trong VFS

Để hiểu VFS, cần phân biệt vài đối tượng khái niệm:

- **superblock** đại diện cho một filesystem đã mount;
- **inode** đại diện siêu dữ liệu (metadata / 메타데이터) của một filesystem đối tượng (object / 객체);
- **dentry (directory entry cache)** đại diện quan hệ giữa tên trong thư mục và đối tượng (object / 객체);
- **tệp (file / 파일) đối tượng (object / 객체)** đại diện trạng thái của một tệp (file / 파일) đang được mở bởi tiến trình (process / 프로세스).

Một pathname như:

```text
/opt/app/config/application.yml
```

không được xử lý như một chuỗi nguyên khối. Kernel resolve từng thành phần (component / 컴포넌트) trong không gian tên (namespace / 네임스페이스), sử dụng dentry bộ nhớ đệm (cache / 캐시) khi có thể, kiểm tra mount boundaries và cuối cùng tới inode/đối tượng (object / 객체) đích.

> **Nối mạch:** Ở chặng này của **VFS, page bộ nhớ đệm (cache / 캐시) và writeback trong Linux**, **Các đối tượng quan trọng trong VFS** đặt đầu vào cho **Dentry bộ nhớ đệm (cache / 캐시) và vì sao đường dẫn (path / 경로) lookup có thể nhanh**, rồi **Page bộ nhớ đệm (cache / 캐시) là gì?** mở rộng hệ quả hoặc giới hạn liên quan.

## Dentry bộ nhớ đệm (cache / 캐시) và vì sao đường dẫn (path / 경로) lookup có thể nhanh

Nếu mỗi lần `open()` đều phải đọc lại toàn bộ directory siêu dữ liệu (metadata / 메타데이터) từ disk, việc truy cập tệp (file / 파일) sẽ tốn kém. Linux giữ bộ nhớ đệm (cache / 캐시) cho pathname lookup gọi là **dentry bộ nhớ đệm (cache / 캐시) (dcache)**.

Điều này nghĩa là lần truy cập thứ hai vào một đường dẫn (path / 경로) thường có thể nhanh hơn vì một phần siêu dữ liệu (metadata / 메타데이터) cần cho việc phân giải tên đã ở RAM.

Nhưng dentry bộ nhớ đệm (cache / 캐시) không đảm bảo đối tượng (object / 객체) luôn còn tồn tại. không gian tên (namespace / 네임스페이스) có thể thay đổi do rename, unlink hoặc mount. Kernel phải duy trì tính hợp lệ của bộ nhớ đệm (cache / 캐시) theo ngữ nghĩa (semantics / 의미론) của filesystem.

> **Nối mạch:** Đặt trong câu hỏi lớn của **VFS, page bộ nhớ đệm (cache / 캐시) và writeback trong Linux**, **Dentry bộ nhớ đệm (cache / 캐시) và vì sao đường dẫn (path / 경로) lookup có thể nhanh** đặt đầu vào cho **Page bộ nhớ đệm (cache / 캐시) là gì?**, rồi **Page bộ nhớ đệm (cache / 캐시) và bộ nhớ của tiến trình (process / 프로세스) có phải hai thứ tách rời hoàn toàn?** mở rộng hệ quả hoặc giới hạn liên quan.

## Page bộ nhớ đệm (cache / 캐시) là gì?

**Page bộ nhớ đệm (cache / 캐시)** là vùng RAM được kernel dùng để giữ nội dung file-backed pages. Khi tiến trình (process / 프로세스) đọc tệp (file / 파일) thông qua buffered I/O, dữ liệu thường được lấy từ page bộ nhớ đệm (cache / 캐시) nếu đã có; nếu chưa có, kernel đọc từ lưu trữ (storage / 저장소) rồi đưa vào page bộ nhớ đệm (cache / 캐시).

Luồng đơn giản:

```text
read(fd)
   ↓
page cache có dữ liệu?
   ├─ có  → copy dữ liệu cho process
   └─ chưa → đọc từ storage → đặt vào page cache → trả cho process
```

Do đó RAM trống thấp không phải luôn xấu. Linux chủ động dùng RAM để giảm I/O.

> **Nối mạch:** Trong **VFS, page bộ nhớ đệm (cache / 캐시) và writeback trong Linux**, **Page bộ nhớ đệm (cache / 캐시) là gì?** đặt đầu vào cho **Page bộ nhớ đệm (cache / 캐시) và bộ nhớ của tiến trình (process / 프로세스) có phải hai thứ tách rời hoàn toàn?**, rồi **Buffered I/O và direct I/O** mở rộng hệ quả hoặc giới hạn liên quan.

## Page bộ nhớ đệm (cache / 캐시) và bộ nhớ của tiến trình (process / 프로세스) có phải hai thứ tách rời hoàn toàn?

Không. Một tệp (file / 파일) có thể được đọc bằng `read()` hoặc ánh xạ bằng `mmap()`. Trong cả hai trường hợp, page bộ nhớ đệm (cache / 캐시) có thể đóng vai trò backing cho dữ liệu file-backed.

Với `mmap()`, tiến trình (process / 프로세스) nhìn thấy vùng địa chỉ ảo ánh xạ tới tệp (file / 파일). Khi truy cập một trang chưa có trong RAM, page fault có thể làm kernel đưa trang tương ứng từ tệp (file / 파일) vào page bộ nhớ đệm (cache / 캐시) rồi ánh xạ vào tiến trình (process / 프로세스).

Đây là lý do cơ sở dữ liệu (database / 데이터베이스) engine, thời gian chạy (runtime / 런타임) và hệ thống lưu trữ phải hiểu rõ mối quan hệ giữa page bộ nhớ đệm (cache / 캐시) của OS và bộ nhớ đệm (cache / 캐시) riêng của ứng dụng.

> **Nối mạch:** Ở chặng này của **VFS, page bộ nhớ đệm (cache / 캐시) và writeback trong Linux**, **Page bộ nhớ đệm (cache / 캐시) và bộ nhớ của tiến trình (process / 프로세스) có phải hai thứ tách rời hoàn toàn?** đặt đầu vào cho **Buffered I/O và direct I/O**, rồi **Ghi tệp (file / 파일): vì sao write() có thể trả về rất nhanh?** mở rộng hệ quả hoặc giới hạn liên quan.

## Buffered I/O và direct I/O

Phần lớn thao tác tệp (file / 파일) thông thường dùng **buffered I/O**, tức đi qua page bộ nhớ đệm (cache / 캐시).

Một số tải công việc (workload / 워크로드) có thể dùng **direct I/O** để giảm hoặc tránh page bộ nhớ đệm (cache / 캐시) cho các I/O nhất định. cơ sở dữ liệu (database / 데이터베이스) engine đôi khi dùng cách này để tự kiểm soát bộ nhớ đệm (cache / 캐시) và thứ tự (ordering / 순서) tốt hơn.

Direct I/O không tự động nhanh hơn. Nó giảm một số lớp bộ nhớ đệm (cache / 캐시) nhưng yêu cầu alignment và quản lý I/O cẩn thận. Nếu ứng dụng không có chiến lược bộ nhớ đệm (cache / 캐시) tốt, bỏ page bộ nhớ đệm (cache / 캐시) có thể làm hiệu năng tệ hơn.

> **Nối mạch:** Đặt trong câu hỏi lớn của **VFS, page bộ nhớ đệm (cache / 캐시) và writeback trong Linux**, **Ghi tệp (file / 파일): vì sao write() có thể trả về rất nhanh?** nối từ **Buffered I/O và direct I/O** sang **Dirty page là gì?**, vì cơ chế trước tạo đầu vào cho bước sau.

## Ghi tệp (file / 파일): vì sao `write()` có thể trả về rất nhanh?

Khi ứng dụng gọi:

```text
write(fd, buffer, size)
```

kernel thường có thể bản sao (copy / 복사) dữ liệu vào page bộ nhớ đệm (cache / 캐시), đánh dấu các trang là **dirty page**, rồi trả success trước khi lưu trữ (storage / 저장소) vật lý hoàn thành ghi.

Mô hình tư duy (mental model / 사고 모델):

```text
application write()
       ↓
RAM / page cache
       ↓
dirty pages
       ↓
writeback
       ↓
storage
```

Điều này giúp tăng thông lượng (throughput / 처리량) vì ứng dụng không phải chờ mỗi lần ghi (write / 쓰기) nhỏ xuống thiết bị.

> **Nối mạch:** Trong **VFS, page bộ nhớ đệm (cache / 캐시) và writeback trong Linux**, **Dirty page là gì?** nối từ **Ghi tệp (file / 파일): vì sao write() có thể trả về rất nhanh?** sang **Writeback diễn ra như thế nào?**, vì cơ chế trước tạo đầu vào cho bước sau.

## Dirty page là gì?

Một trang file-backed được gọi là **dirty** khi nội dung trong RAM mới hơn dữ liệu bền vững trên lưu trữ (storage / 저장소).

Có thể quan sát một số chỉ số hệ thống:

```bash
grep -E 'Dirty|Writeback' /proc/meminfo
```

Ví dụ:

```text
Dirty:       120000 kB
Writeback:    16000 kB
```

`Dirty` cho biết lượng trang đang chờ ghi; `Writeback` cho biết lượng đang trong quá trình ghi xuống lưu trữ (storage / 저장소).

Một giá trị lớn không tự động là lỗi. Cần nhìn xu hướng, tốc độ ghi, độ trễ (latency / 지연 시간) và tải công việc (workload / 워크로드).

> **Nối mạch:** Ở chặng này của **VFS, page bộ nhớ đệm (cache / 캐시) và writeback trong Linux**, **Writeback diễn ra như thế nào?** nối từ **Dirty page là gì?** sang **Khi dirty bộ nhớ (memory / 메모리) quá nhiều thì chuyện gì xảy ra?**, vì cơ chế trước tạo đầu vào cho bước sau.

## Writeback diễn ra như thế nào?

Kernel có cơ chế nền để ghi dirty pages xuống lưu trữ (storage / 저장소). Việc ghi có thể được kích hoạt bởi:

- tuổi của dirty page;
- tỷ lệ dirty bộ nhớ (memory / 메모리) vượt ngưỡng;
- `fsync()` hoặc `sync()`;
- áp lực bộ nhớ;
- cơ chế writeback riêng của filesystem.

Các tham số như sau có thể tồn tại qua `sysctl`:

```bash
sysctl vm.dirty_ratio
sysctl vm.dirty_background_ratio
sysctl vm.dirty_expire_centisecs
sysctl vm.dirty_writeback_centisecs
```

Không nên thay đổi các giá trị này theo bài tuning chung trên Internet. Chúng ảnh hưởng cân bằng giữa thông lượng (throughput / 처리량), độ trễ (latency / 지연 시간) burst và lượng dữ liệu chưa xuống lưu trữ (storage / 저장소).

> **Nối mạch:** Đặt trong câu hỏi lớn của **VFS, page bộ nhớ đệm (cache / 캐시) và writeback trong Linux**, **Khi dirty bộ nhớ (memory / 메모리) quá nhiều thì chuyện gì xảy ra?** nối từ **Writeback diễn ra như thế nào?** sang **fsync() thay đổi điều gì?**, vì cơ chế trước tạo đầu vào cho bước sau.

## Khi dirty bộ nhớ (memory / 메모리) quá nhiều thì chuyện gì xảy ra?

Nếu tiến trình (process / 프로세스) ghi nhanh hơn lưu trữ (storage / 저장소) có thể hấp thụ, dirty pages tăng dần. Đến một mức, kernel có thể làm tiến trình (process / 프로세스) ghi bị throttled hoặc phải tham gia writeback.

Triệu chứng có thể là:

```text
lúc đầu write rất nhanh
→ dirty pages tăng
→ storage queue tăng
→ kernel bắt đầu writeback mạnh
→ application latency tăng
```

Đây là một ví dụ quan trọng cho thấy benchmark ngắn có thể gây hiểu nhầm. Một tải công việc (workload / 워크로드) ghi trong 5 giây có thể đo chủ yếu tốc độ RAM/page bộ nhớ đệm (cache / 캐시), không phản ánh sustained lưu trữ (storage / 저장소) thông lượng (throughput / 처리량).

> **Nối mạch:** Trong **VFS, page bộ nhớ đệm (cache / 캐시) và writeback trong Linux**, **fsync() thay đổi điều gì?** nối từ **Khi dirty bộ nhớ (memory / 메모리) quá nhiều thì chuyện gì xảy ra?** sang **fdatasync() và sự khác biệt khái niệm**, vì cơ chế trước tạo đầu vào cho bước sau.

## `fsync()` thay đổi điều gì?

`fsync(fd)` yêu cầu kernel đồng bộ dữ liệu và siêu dữ liệu (metadata / 메타데이터) cần thiết của tệp (file / 파일) theo ngữ nghĩa (semantics / 의미론) của hệ thống xuống lưu trữ (storage / 저장소).

Ứng dụng cần durability như cơ sở dữ liệu (database / 데이터베이스) thường không thể chỉ dựa vào `write()`.

Tuy nhiên `fsync()` có chi phí vì nó đưa độ trễ (latency / 지연 시간) của lưu trữ (storage / 저장소) vào đường găng (critical path / 임계 경로).

Do đó cơ sở dữ liệu (database / 데이터베이스) thường dùng kỹ thuật batching hoặc group lần ghi nhận (commit / 커밋) để nhiều giao dịch (transaction / 트랜잭션) cùng chia sẻ chi phí flush.

> **Nối mạch:** Ở chặng này của **VFS, page bộ nhớ đệm (cache / 캐시) và writeback trong Linux**, **fdatasync() và sự khác biệt khái niệm** nối từ **fsync() thay đổi điều gì?** sang **Atomicity, visibility và durability là ba khái niệm khác nhau**, vì cơ chế trước tạo đầu vào cho bước sau.

## `fdatasync()` và sự khác biệt khái niệm

`fdatasync()` tập trung vào dữ liệu và siêu dữ liệu (metadata / 메타데이터) cần thiết để đọc dữ liệu đúng, trong khi `fsync()` có thể có ngữ nghĩa (semantics / 의미론) rộng hơn về siêu dữ liệu (metadata / 메타데이터) tùy filesystem.

Điểm cần nhớ không phải thuộc API chi tiết, mà là: **có nhiều mức guarantee khác nhau giữa “đã bản sao (copy / 복사) vào RAM” và “đã bền vững trên lưu trữ (storage / 저장소)”**.

> **Nối mạch:** Đặt trong câu hỏi lớn của **VFS, page bộ nhớ đệm (cache / 캐시) và writeback trong Linux**, **Atomicity, visibility và durability là ba khái niệm khác nhau** nối từ **fdatasync() và sự khác biệt khái niệm** sang **Sao chép khi ghi (copy-on-write / 쓰기 시 복사) có làm page bộ nhớ đệm (cache / 캐시) biến mất không?**, vì cơ chế trước tạo đầu vào cho bước sau.

## Atomicity, visibility và durability là ba khái niệm khác nhau

Một thao tác có thể:

- atomic về không gian tên (namespace / 네임스페이스);
- visible ngay cho tiến trình (process / 프로세스) khác;
- nhưng chưa durable sau power mất mát (loss / 손실).

Ví dụ `rename()` trong cùng filesystem thường atomic về không gian tên (namespace / 네임스페이스), nhưng muốn bảo đảm trạng thái tồn tại sau crash có thể cần fsync tệp (file / 파일) và directory theo mẫu (pattern / 패턴) phù hợp.

Không nên đồng nhất “người đọc khác đã thấy tệp (file / 파일) mới” với “tệp (file / 파일) mới đã chắc chắn được ghi bền vững”.

> **Nối mạch:** Trong **VFS, page bộ nhớ đệm (cache / 캐시) và writeback trong Linux**, **Sao chép khi ghi (copy-on-write / 쓰기 시 복사) có làm page bộ nhớ đệm (cache / 캐시) biến mất không?** nối từ **Atomicity, visibility và durability là ba khái niệm khác nhau** sang **Read-ahead**, vì cơ chế trước tạo đầu vào cho bước sau.

## Sao chép khi ghi (copy-on-write / 쓰기 시 복사) có làm page bộ nhớ đệm (cache / 캐시) biến mất không?

Không. Filesystem dùng sao chép khi ghi (copy-on-write / 쓰기 시 복사) như Btrfs có chiến lược ghi siêu dữ liệu (metadata / 메타데이터)/dữ liệu (data / 데이터) khác, nhưng page bộ nhớ đệm (cache / 캐시) vẫn là một phần quan trọng của Linux I/O ngăn xếp (stack / 스택).

Sao chép khi ghi (copy-on-write / 쓰기 시 복사) thay đổi cách blocks được cập nhật và giúp snapshot/checksum ở mức filesystem, nhưng không loại bỏ khái niệm bộ nhớ đệm (cache / 캐시), writeback hoặc durability.

> **Nối mạch:** Ở chặng này của **VFS, page bộ nhớ đệm (cache / 캐시) và writeback trong Linux**, **Read-ahead** nối từ **Sao chép khi ghi (copy-on-write / 쓰기 시 복사) có làm page bộ nhớ đệm (cache / 캐시) biến mất không?** sang **Readahead quá lớn có thể gây tác dụng ngược**, vì cơ chế trước tạo đầu vào cho bước sau.

## Read-ahead

Khi kernel nhận thấy tiến trình (process / 프로세스) đọc tuần tự, nó có thể đọc trước các khối (block / 블록) kế tiếp vào page bộ nhớ đệm (cache / 캐시). Cơ chế này gọi là **read-ahead**.

Điều này làm sequential scan nhanh hơn vì I/O được gom và chuỗi xử lý (pipeline / 파이프라인) trước.

Nhưng random truy cập (access / 접근) không hưởng lợi giống vậy. Đây là lý do sequential thông lượng (throughput / 처리량) và random IOPS là hai đặc tính rất khác nhau của lưu trữ (storage / 저장소).

> **Nối mạch:** Đặt trong câu hỏi lớn của **VFS, page bộ nhớ đệm (cache / 캐시) và writeback trong Linux**, **Readahead quá lớn có thể gây tác dụng ngược** nối từ **Read-ahead** sang **dropcaches và vì sao không nên dùng để “tối ưu” môi trường vận hành (production / 운영 환경)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Readahead quá lớn có thể gây tác dụng ngược

Nếu tải công việc (workload / 워크로드) đọc ngẫu nhiên nhưng kernel đoán thành tuần tự, read-ahead có thể kéo vào RAM những dữ liệu không dùng tới, gây bộ nhớ đệm (cache / 캐시) pollution và I/O thừa.

Tuning chỉ nên làm khi có đo lường cụ thể.

> **Nối mạch:** Trong **VFS, page bộ nhớ đệm (cache / 캐시) và writeback trong Linux**, **dropcaches và vì sao không nên dùng để “tối ưu” môi trường vận hành (production / 운영 환경)** nối từ **Readahead quá lớn có thể gây tác dụng ngược** sang **Page bộ nhớ đệm (cache / 캐시) và bộ chứa (container / 컨테이너)**, vì cơ chế trước tạo đầu vào cho bước sau.

## `drop_caches` và vì sao không nên dùng để “tối ưu” môi trường vận hành (production / 운영 환경)

Linux cho phép yêu cầu kernel thu hồi một số bộ nhớ đệm (cache / 캐시):

```bash
sync
echo 3 | sudo tee /proc/sys/vm/drop_caches
```

Lệnh này đôi khi hữu ích trong benchmark kiểm soát, nhưng không phải cách “giải phóng RAM” định kỳ cho môi trường vận hành (production / 운영 환경).

Xóa page bộ nhớ đệm (cache / 캐시) có thể làm lần đọc tiếp theo phải quay lại lưu trữ (storage / 저장소) và tăng độ trễ (latency / 지연 시간) mạnh.

> **Nối mạch:** Ở chặng này của **VFS, page bộ nhớ đệm (cache / 캐시) và writeback trong Linux**, **Page bộ nhớ đệm (cache / 캐시) và bộ chứa (container / 컨테이너)** nối từ **dropcaches và vì sao không nên dùng để “tối ưu” môi trường vận hành (production / 운영 환경)** sang **Page bộ nhớ đệm (cache / 캐시) và Java**, vì cơ chế trước tạo đầu vào cho bước sau.

## Page bộ nhớ đệm (cache / 캐시) và bộ chứa (container / 컨테이너)

Bộ chứa (container / 컨테이너) chia sẻ host kernel, nên page bộ nhớ đệm (cache / 캐시) là tài nguyên host-level theo ngữ nghĩa (semantics / 의미론) kernel, dù accounting trong cgroup có thể phân bổ chi phí bộ nhớ (memory / 메모리) theo điều khiển (control / 제어) group.

Hai bộ chứa (container / 컨테이너) đọc cùng một tệp (file / 파일) backing có thể trong một số tình huống tận dụng bộ nhớ đệm (cache / 캐시) chung ở kernel tầng (layer / 계층).

Điều này cũng làm bộ nhớ (memory / 메모리) accounting phức tạp hơn việc chỉ nhìn RSS của từng tiến trình (process / 프로세스).

> **Nối mạch:** Đặt trong câu hỏi lớn của **VFS, page bộ nhớ đệm (cache / 캐시) và writeback trong Linux**, **Page bộ nhớ đệm (cache / 캐시) và Java** nối từ **Page bộ nhớ đệm (cache / 캐시) và bộ chứa (container / 컨테이너)** sang **Quan sát thực tế**, vì cơ chế trước tạo đầu vào cho bước sau.

## Page bộ nhớ đệm (cache / 캐시) và Java

Java ứng dụng (application / 애플리케이션) thường đọc JAR, cấu hình (config / 설정), static resources và log thông qua filesystem. Khi đọc lại dữ liệu, page bộ nhớ đệm (cache / 캐시) có thể làm I/O nhanh hơn.

Một JVM có vùng nhớ động (heap / 힙) ổn định nhưng host bộ nhớ (memory / 메모리) “used” tăng không nhất thiết là leak; page bộ nhớ đệm (cache / 캐시) có thể tăng do tải công việc (workload / 워크로드) đọc tệp (file / 파일).

Ngược lại, khi bộ nhớ (memory / 메모리) pressure cao, kernel reclaim page bộ nhớ đệm (cache / 캐시) và ứng dụng (application / 애플리케이션) có thể thấy I/O độ trễ (latency / 지연 시간) tăng vì bộ nhớ đệm (cache / 캐시) hit tỷ lệ (rate / 비율) giảm.

> **Nối mạch:** Trong **VFS, page bộ nhớ đệm (cache / 캐시) và writeback trong Linux**, **Quan sát thực tế** nối từ **Page bộ nhớ đệm (cache / 캐시) và Java** sang **Một trường hợp (case / 사례) môi trường vận hành (production / 운영 환경): log burst làm API chậm**, vì cơ chế trước tạo đầu vào cho bước sau.

## Quan sát thực tế

Một bộ công cụ cơ bản:

```bash
free -h
grep -E 'Cached|Dirty|Writeback' /proc/meminfo
vmstat 1
iostat -xz 1
pidstat -d 1
```

Nếu cần xem tiến trình (process / 프로세스) đang đọc/ghi tệp (file / 파일) nào:

```bash
sudo lsof -p <PID>
```

Nếu muốn nhìn lời gọi hệ thống (system call / 시스템 호출) I/O:

```bash
sudo strace -p <PID> -e trace=read,write,pread64,pwrite64,fsync,fdatasync
```

`strace` có overhead, nên chỉ dùng có mục tiêu và trong khoảng thời gian cần thiết.

> **Nối mạch:** Ở chặng này của **VFS, page bộ nhớ đệm (cache / 캐시) và writeback trong Linux**, **Quan sát thực tế** nêu quy tắc; **Một trường hợp (case / 사례) môi trường vận hành (production / 운영 환경): log burst làm API chậm** thử quy tắc trong tình huống, rồi **Một trường hợp (case / 사례) khác: deploy xong lần đầu chậm, lần sau nhanh** mở rộng hệ quả.

## Một trường hợp (case / 사례) môi trường vận hành (production / 운영 환경): log burst làm API chậm

Giả sử Java dịch vụ (service / 서비스) bình thường nhưng một lỗi upstream gây thử lại (retry / 재시도) liên tục và tạo log lớn.

Chuỗi nhân quả có thể là:

```text
upstream lỗi
→ retry storm
→ log write rate tăng mạnh
→ dirty pages tăng
→ writeback mạnh
→ storage queue dài
→ fsync hoặc metadata I/O chậm
→ application threads chờ I/O
→ API latency tăng
```

Nếu chỉ nhìn CPU có thể thấy CPU vẫn thấp và kết luận sai rằng máy chủ (server / 서버) còn khỏe.

Cần correlate log tỷ lệ (rate / 비율), `Dirty`, `iostat`, luồng thực thi (thread / 스레드) trạng thái (state / 상태) và ứng dụng (application / 애플리케이션) độ trễ (latency / 지연 시간).

> **Nối mạch:** Đặt trong câu hỏi lớn của **VFS, page bộ nhớ đệm (cache / 캐시) và writeback trong Linux**, **Một trường hợp (case / 사례) môi trường vận hành (production / 운영 환경): log burst làm API chậm** nêu quy tắc; **Một trường hợp (case / 사례) khác: deploy xong lần đầu chậm, lần sau nhanh** thử quy tắc trong tình huống, rồi **Mô hình tư duy** mở rộng hệ quả.

## Một trường hợp (case / 사례) khác: deploy xong lần đầu chậm, lần sau nhanh

Sau reboot hoặc deploy sang host mới, page bộ nhớ đệm (cache / 캐시) còn lạnh. Lần đầu đọc JAR/cấu hình (config / 설정)/static files phải lấy từ lưu trữ (storage / 저장소). Sau đó các pages ở bộ nhớ đệm (cache / 캐시) nên lần truy cập kế tiếp nhanh hơn.

Đây là **bộ nhớ đệm (cache / 캐시) warming** tự nhiên.

Một benchmark cần kiểm soát bộ nhớ đệm (cache / 캐시) trạng thái (state / 상태) nếu muốn so lưu trữ (storage / 저장소) thay vì đo bộ nhớ đệm (cache / 캐시).

> **Nối mạch:** Trong **VFS, page bộ nhớ đệm (cache / 캐시) và writeback trong Linux**, **Một trường hợp (case / 사례) khác: deploy xong lần đầu chậm, lần sau nhanh** nêu quy tắc; **Mô hình tư duy** thử quy tắc trong tình huống, rồi **Những hiểu lầm phổ biến** mở rộng hệ quả.

## Mô hình tư duy

Có thể hình dung I/O tệp (file / 파일) thông thường như:

```text
pathname
  ↓
VFS / dentry / inode
  ↓
page cache
  ↓
filesystem implementation
  ↓
block layer
  ↓
device / network storage
```

Khi đọc, page bộ nhớ đệm (cache / 캐시) cố tránh đi xuống các lớp dưới. Khi ghi, page bộ nhớ đệm (cache / 캐시) cho phép tách thời điểm ứng dụng ghi với thời điểm lưu trữ (storage / 저장소) thực sự hoàn thành.

> **Nối mạch:** Ở chặng này của **VFS, page bộ nhớ đệm (cache / 캐시) và writeback trong Linux**, **Những hiểu lầm phổ biến** tổng hợp từ **Mô hình tư duy** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối kiến thức** mở rộng hệ quả hoặc giới hạn liên quan.

## Những hiểu lầm phổ biến

**“`write()` trả về nghĩa dữ liệu đã nằm trên disk.”** Không nhất thiết; dữ liệu có thể mới ở page bộ nhớ đệm (cache / 캐시).

**“RAM dùng cho bộ nhớ đệm (cache / 캐시) là RAM bị lãng phí.”** Ngược lại, bộ nhớ đệm (cache / 캐시) giúp giảm I/O và có thể được reclaim.

**“`drop_caches` giúp môi trường vận hành (production / 운영 환경) nhanh hơn.”** Thường làm mất dữ liệu bộ nhớ đệm (cache / 캐시) hữu ích và tăng độ trễ (latency / 지연 시간) lần đọc sau.

**“Benchmark ghi 2 giây phản ánh tốc độ SSD.”** Có thể chủ yếu phản ánh page bộ nhớ đệm (cache / 캐시) nếu chưa buộc flush.

**“Atomic rename đồng nghĩa dữ liệu durable.”** Atomicity và durability là hai guarantee khác nhau.

> **Nối mạch:** Đặt trong câu hỏi lớn của **VFS, page bộ nhớ đệm (cache / 캐시) và writeback trong Linux**, **Kết nối kiến thức** nối từ **Những hiểu lầm phổ biến** sang  Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Kết nối kiến thức

Đọc thêm [Journaling, tính nhất quán và mount](./journaling_consistency_mounts.md) để hiểu durability sau crash, [I/O performance](../06_resources/io_performance.md) để hiểu hàng đợi (queue / 큐)/độ trễ (latency / 지연 시간), và [Bộ nhớ ảo](../06_resources/memory_virtual_memory.md) để nối page bộ nhớ đệm (cache / 캐시) với bộ nhớ (memory / 메모리) reclaim.

> **Bàn giao:** Sau **Kết nối kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
