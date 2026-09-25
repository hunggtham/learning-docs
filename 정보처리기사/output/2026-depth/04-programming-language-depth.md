# Môn 4 — 프로그래밍 언어 활용: Deep Dive 2026

> Môn 4 là vùng dễ mất điểm vì đề có thể chuyển nhanh giữa **server program, programming language, OS và network**. Không nên học theo kiểu “tôi là developer nên chắc biết”. Phải luyện đọc code, tính tay scheduling/page replacement/subnet và nhớ đúng thuật ngữ hệ thống.

## 1. 서버 프로그램 구현 — Server Program Implementation

### 1.1 Development Environment

Development environment có thể gồm OS, JDK/runtime, compiler/interpreter, IDE, build tool, framework, DBMS, middleware, VCS và CI/CD tool. Đề thường hỏi vai trò từng tool, vì vậy cần phân category thay vì nhớ tên thương hiệu.

Compiler dịch source sang machine/intermediate code trước khi chạy theo mô hình truyền thống. Interpreter thực thi/phân tích từng phần runtime. JIT kết hợp bằng cách compile hot code trong runtime.

Framework cung cấp skeleton/control inversion; library là code được application chủ động gọi. Đây là khác biệt cốt lõi: với framework, flow control thường được framework nắm giữ rồi gọi code của application theo lifecycle/hook.

### 1.2 Common Module và Server Logic

Server program thường nhận request, validate input, thực thi business logic, truy cập persistence/resource, tạo response và log/monitor error. Layering giúp tách presentation/API, application/service, domain và infrastructure/persistence.

Không phải mọi layer đều bắt buộc trong mọi system, nhưng đề lý thuyết thường đánh giá separation of concerns và module independence.

### 1.3 Batch Processing

Batch xử lý job theo tập dữ liệu và schedule, phù hợp khi không cần response interactive tức thời. Online/transaction processing xử lý request gần real-time. Batch lớn cần restartability, checkpoint, idempotency và error isolation để không phải chạy lại toàn bộ khi một phần thất bại.

## 2. 프로그래밍 언어 활용 — Programming Language Application

## 2.1 Common language concepts

### Variable, Scope, Lifetime

Scope là vùng source code có thể truy cập identifier. Lifetime là khoảng thời gian object/variable tồn tại trong runtime. Hai khái niệm liên quan nhưng không đồng nhất.

Local variable thường có scope hẹp; global/static state sống lâu hơn. Static local trong C có local scope nhưng lifetime kéo dài suốt process.

### Value vs Reference semantics

Value semantics copy giá trị. Reference semantics copy reference tới object chung. Nhiều bug đề thi xuất phát từ việc hai biến cùng trỏ một object mutable.

### Parameter Passing

Call by value truyền bản sao value. Nếu value đó bản thân là pointer/reference, function nhận bản sao của pointer nhưng vẫn có thể mutate object được trỏ tới. Đây là lý do Java được mô tả là pass-by-value, kể cả object reference.

## 3. C Language

### 3.1 Pointer

Pointer lưu address. `&x` lấy địa chỉ x; `*p` dereference pointer p để truy cập value tại address.

Ví dụ:

```c
int x = 10;
int *p = &x;
*p = 20;
```

Sau đó `x` là 20 vì `p` trỏ tới x.

Phải phân biệt:

- `p` = address.
- `*p` = value tại address.
- `&p` = address của biến pointer p.

### 3.2 Pointer arithmetic

Nếu `p` là `int*`, `p + 1` trỏ tới phần tử int kế tiếp, tăng theo `sizeof(int)`, không chỉ tăng 1 byte về semantics C pointer arithmetic.

### 3.3 Array và Pointer

Trong nhiều expression, array name decay thành pointer tới phần tử đầu, nhưng array và pointer không hoàn toàn là cùng một type/entity. `sizeof(array)` trong cùng scope array thật có thể cho total array size, trong khi `sizeof(pointer)` chỉ cho pointer size.

### 3.4 String

C string là sequence char kết thúc bằng `\0`. `strlen` đếm ký tự trước null terminator, không tính `\0`. Buffer đủ chỗ phải tính thêm null terminator.

### 3.5 struct / union

`struct` cấp storage cho các member (có padding/alignment). `union` cho các member dùng chung vùng storage; tại một thời điểm interpretation hợp lệ phụ thuộc member được ghi/đọc và rule ngôn ngữ.

### 3.6 Increment operators

`i++` trả value cũ rồi increment như side effect theo semantics expression; `++i` increment trước rồi value expression là value mới. Trong expression phức tạp, đừng đoán bằng trực giác; trace sequence cẩn thận và tránh dựa vào code có undefined behavior.

### 3.7 Recursion

Recursion cần base case và recursive step tiến về base case. Mỗi call thường tạo stack frame; recursion sâu có thể stack overflow.

## 4. Java

### 4.1 Class, Object, Inheritance

Class định nghĩa type/behavior; object là instance runtime. Inheritance tạo subtype relation. Java chỉ single inheritance cho class nhưng hỗ trợ nhiều interface.

### 4.2 Overloading vs Overriding

Overloading: cùng method name, parameter list khác trong compile-time resolution. Return type đơn độc không đủ để overload.

Overriding: subclass cung cấp implementation mới cho instance method có signature tương thích; runtime dynamic dispatch chọn method theo actual object.

### 4.3 Polymorphism

```java
Animal a = new Dog();
a.sound();
```

Nếu `Dog` override `sound`, runtime gọi `Dog.sound()`. Reference type `Animal` giới hạn member có thể truy cập compile-time; actual object `Dog` quyết định overridden method runtime.

### 4.4 Abstract class vs Interface

Abstract class có thể giữ state, constructor và cả concrete/abstract method. Interface mô tả contract; Java hiện đại cho phép default/static/private method tùy version, nhưng concept thi cơ bản vẫn là abstraction contract và multiple interface implementation.

### 4.5 Exception

Checked exception thường cần catch/declare compile-time; unchecked exception là RuntimeException hierarchy. `finally` thường dùng cleanup và được chạy trong flow bình thường/exception trừ một số termination đặc biệt.

### 4.6 String

Java String immutable. Operation như concat tạo String mới về semantic; StringBuilder mutable và phù hợp nhiều append trong loop.

### 4.7 Access modifier

`public`: rộng nhất. `private`: trong class. `protected`: package + subclass theo rule Java. Không modifier: package-private.

## 5. Python

### 5.1 Object/reference model

Python variable name bind tới object. Assignment không copy object mặc định.

```python
a = [1, 2]
b = a
b.append(3)
```

Cả `a` và `b` cùng thấy list `[1,2,3]` vì cùng reference một list mutable.

### 5.2 Mutable vs Immutable

List, dict, set thường mutable. int, float, str, tuple thường immutable theo semantic cơ bản. Tuple có thể chứa mutable object; “tuple immutable” nghĩa cấu trúc reference của tuple không đổi, không bảo đảm mọi object bên trong immutable.

### 5.3 Slicing

`a[start:stop:step]` stop là exclusive. Negative index đếm từ cuối. Cần luyện tay vì câu hỏi dễ hỏi output ngắn.

### 5.4 Function argument

Python dùng object-sharing/call-by-object-reference terminology tùy giáo trình. Cách an toàn: function nhận binding tới cùng object; mutate object mutable có thể thấy bên ngoài, rebinding local name không tự đổi binding của caller.

### 5.5 Comprehension

List comprehension rút gọn transform/filter. Ví dụ `[x*x for x in range(5) if x % 2 == 0]` → `[0,4,16]`.

### 5.6 Exception

`try/except/else/finally`: except xử lý error, else chạy khi try không raise, finally dùng cleanup và chạy bất kể success/failure trong flow bình thường.

## 6. 운영체제 기초 활용 — Operating System Foundations

### 6.1 Process vs Thread

Process có address space/resource context riêng. Thread là execution unit trong process và thường share address space/resources với thread cùng process.

Context switch giữa process thường nặng hơn thread, nhưng detail phụ thuộc OS. Shared memory giữa thread giúp communication nhanh nhưng tạo synchronization problem.

### 6.2 Process State

Các state điển hình: New, Ready, Running, Waiting/Blocked, Terminated. Ready có CPU-ready nhưng đang chờ CPU. Blocked chờ event/I/O, không chỉ chờ scheduler.

### 6.3 Scheduling

**FCFS** non-preemptive, đơn giản, có convoy effect. **SJF** chọn burst ngắn nhất, tối ưu average waiting time trong điều kiện biết burst nhưng có starvation. **SRTF** là preemptive form của SJF. **Round Robin** dùng time quantum, phù hợp time-sharing. **Priority Scheduling** chọn priority và có thể starvation; aging giảm starvation. **HRN** dùng response ratio để cân bằng waiting/burst.

HRN response ratio:

`(Waiting Time + Service Time) / Service Time`

### 6.4 Scheduling metrics

Turnaround Time = Completion - Arrival. Waiting Time = Turnaround - CPU Burst (trong bài đơn giản không I/O). Response Time = First Run - Arrival.

Đề tính tay cần vẽ Gantt chart trước rồi mới tính metric.

### 6.5 Synchronization

Race condition xảy ra khi result phụ thuộc timing interleaving. Critical section là vùng truy cập shared resource cần synchronization.

Mutex cung cấp mutual exclusion ownership. Semaphore là counter synchronization primitive có wait/signal; binary semaphore có thể giống mutex ở một số use case nhưng semantics ownership khác.

### 6.6 Deadlock

Bốn điều kiện Coffman: Mutual Exclusion, Hold and Wait, No Preemption, Circular Wait. Phá ít nhất một điều kiện có thể prevent deadlock.

Banker's Algorithm là ví dụ deadlock avoidance dựa safe state, không phải detection.

### 6.7 Memory Management

Paging chia virtual memory thành fixed-size page và physical memory thành frame. Segmentation chia theo logical segment variable-size.

Internal fragmentation thường gắn fixed-size allocation; external fragmentation thường gắn variable-size contiguous allocation.

### 6.8 Virtual Memory

Page fault xảy ra khi referenced page không ở memory. OS phải load page từ backing store, có thể cần chọn victim page.

Page replacement:

- FIFO: thay page vào sớm nhất.
- LRU: thay page lâu nhất chưa dùng.
- Optimal: thay page sẽ được dùng xa nhất trong tương lai; dùng làm benchmark vì không thực tế biết future.
- LFU: dựa frequency, cần xử lý history/tie.

Belady's Anomaly có thể xảy ra với FIFO: tăng frame nhưng page fault tăng. Stack algorithms như LRU/Optimal không có anomaly này theo property kinh điển.

### 6.9 Thrashing

Thrashing xảy ra khi system dành quá nhiều thời gian paging do working set không đủ frame. CPU utilization có thể giảm dù multiprogramming cao. Working-set/control page-fault frequency là các approach liên quan.

### 6.10 File System

File allocation strategy có thể contiguous, linked, indexed. Contiguous nhanh sequential/random nhưng khó grow và external fragmentation. Linked dễ grow nhưng random access kém. Indexed dùng index block để trỏ data block.

## 7. 네트워크 기초 활용 — Network Foundations

### 7.1 OSI 7 Layers

1 Physical — bit/signal/media.  
2 Data Link — frame, MAC, local link.  
3 Network — packet, IP, routing.  
4 Transport — end-to-end transport, TCP/UDP, port.  
5 Session — session control.  
6 Presentation — representation/encoding/encryption/compression concept.  
7 Application — protocol/service gần application.

Trong Internet stack thực tế, Session/Presentation thường không tách rõ như OSI reference model.

### 7.2 TCP vs UDP

TCP connection-oriented, reliable byte stream, ordering, retransmission, flow/congestion control. UDP connectionless datagram, không bảo đảm delivery/order, overhead thấp hơn.

“UDP nhanh hơn” chỉ là shorthand. Application có thể tự thêm reliability và cost khác; chọn protocol dựa requirement.

### 7.3 Common Protocols

HTTP/HTTPS: web application protocol. DNS: name resolution. DHCP: cấp network configuration động. FTP: file transfer truyền thống. SMTP: gửi mail. POP3/IMAP: nhận/quản lý mail. SSH: secure remote shell. SNMP: network management. NTP: time synchronization.

Port number có thể được hỏi, nhưng nên học những port nền tảng: HTTP 80, HTTPS 443, SSH 22, DNS 53, SMTP 25, FTP control 21. Đừng dành quá nhiều thời gian thuộc mọi port hiếm trước khi core concept vững.

### 7.4 IPv4 và Subnet

IPv4 có 32 bit. Prefix `/n` dành n bit network, còn `32-n` bit host.

Số address trong subnet = `2^(32-n)`. Trong subnet truyền thống, usable host thường trừ network và broadcast, ngoại trừ các special prefix/use case.

Ví dụ `/26`: còn 6 host bit → 64 address, thường 62 usable host.

Subnet mask `/26` = `255.255.255.192`, block size ở octet cuối = 64.

### 7.5 Routing

Static routing cấu hình thủ công. Dynamic routing dùng routing protocol.

Distance Vector chia sẻ distance/vector với neighbor, ví dụ RIP truyền thống. Link State xây topology map và chạy shortest-path algorithm, ví dụ OSPF. BGP là path-vector/inter-domain routing giữa autonomous systems.

### 7.6 LAN devices

Hub phát frame/bit ra nhiều port và hoạt động đơn giản ở physical layer concept. Switch học MAC address và forward frame ở Data Link layer. Router route packet giữa network ở Network layer.

### 7.7 ARP, ICMP

ARP map IPv4 address sang MAC trong local network. ICMP hỗ trợ control/error diagnostics như ping concept. DNS không làm nhiệm vụ map IP sang MAC.

## 8. Cặp dễ nhầm

| Cặp | Điểm tách |
|---|---|
| Framework vs Library | inversion of control vs app chủ động gọi |
| Scope vs Lifetime | vùng truy cập tên vs thời gian object tồn tại |
| Overloading vs Overriding | compile-time signature vs subtype runtime behavior |
| Value vs Reference semantics | copy value vs alias cùng object |
| Process vs Thread | address space/resource context vs execution unit share process |
| Ready vs Blocked | chờ CPU vs chờ event/I/O |
| SJF vs SRTF | non-preemptive vs preemptive |
| Paging vs Segmentation | fixed-size page/frame vs logical variable segment |
| Internal vs External fragmentation | lãng phí trong block vs lỗ trống giữa block |
| FIFO vs LRU | oldest loaded vs least recently used |
| TCP vs UDP | reliable connection stream vs connectionless datagram |
| Switch vs Router | MAC/L2 vs IP/L3 |
| DNS vs ARP | name→IP vs IPv4→MAC local |

## 9. Procedural drills

### Drill 1 — C Pointer

```c
int x = 5;
int *p = &x;
(*p)++;
printf("%d", x);
```

Tự trace output và giải thích từng bước.

### Drill 2 — Java Polymorphism

Cho `Parent p = new Child();`, Child override `run()`. Khi gọi `p.run()` method nào chạy? Nếu field `name` được khai báo ở cả Parent và Child thì field access có semantics giống method dispatch không?

### Drill 3 — Python alias

```python
a = [1, 2]
b = a
b = b + [3]
```

Sau đó a và b là gì? So sánh với `b.append(3)`.

### Drill 4 — Round Robin

Ba process tới time 0 với burst P1=5, P2=3, P3=1, quantum=2. Vẽ Gantt chart và tính completion/waiting time.

### Drill 5 — Page replacement

Reference string `1 2 3 1 4 2 5 1 2 3 4 5`, 3 frame. Tính page fault cho FIFO và LRU.

### Drill 6 — Deadlock

Giải thích tại sao chỉ có Mutual Exclusion + Hold and Wait chưa đủ kết luận deadlock nếu chưa có No Preemption và Circular Wait.

### Drill 7 — Subnet

`192.168.10.130/26`: tìm network address, broadcast address và usable host range.

### Drill 8 — OSI

Một switch xử lý MAC address, router xử lý IP route, TCP dùng port. Map ba thao tác này vào OSI layer.

## 10. 과락 방지 checklist — Môn 4

Phải tự làm được:

- phân loại compiler/interpreter/JIT, framework/library, build/runtime tool;
- trace C pointer/array/string và operator cơ bản;
- phân biệt Java overloading/overriding/polymorphism/interface/abstract class;
- trace Python mutable/reference/slicing/comprehension;
- phân biệt scope/lifetime và value/reference behavior;
- vẽ process state và giải scheduling FCFS/SJF/SRTF/RR/Priority/HRN;
- tính turnaround/waiting/response time;
- giải synchronization, semaphore/mutex và deadlock;
- phân biệt paging/segmentation, fragmentation, virtual memory;
- tính FIFO/LRU/Optimal page replacement bài ngắn;
- giải OSI/TCP-IP, TCP/UDP, protocol và network device;
- tính subnet IPv4;
- phân biệt routing concept, ARP/DNS/ICMP.

Môn 4 phải luyện bằng giấy. Chỉ đọc code và công thức sẽ tạo false confidence.
