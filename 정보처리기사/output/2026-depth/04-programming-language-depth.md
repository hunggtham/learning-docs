# Môn 4 — 프로그래밍 언어 활용: Deep Dive 2026

> Môn 4 là vùng dễ mất điểm vì đề có thể chuyển nhanh giữa **máy chủ (server / 서버) program, programming ngôn ngữ (language / 언어), OS và mạng (network / 네트워크)**. Không nên học theo kiểu “tôi là nhà phát triển (developer / 개발자) nên chắc biết”. Phải luyện đọc mã (code / 코드), tính tay scheduling/page replacement/subnet và nhớ đúng thuật ngữ hệ thống.

## 1. 서버 프로그램 구현 — máy chủ (server / 서버) Program hiện thực (implementation / 구현)

### 1.1 Development môi trường (environment / 환경)

Development môi trường (environment / 환경) có thể gồm OS, JDK/thời gian chạy (runtime / 런타임), trình biên dịch (compiler / 컴파일러)/trình thông dịch (interpreter / 인터프리터), IDE, bản dựng (build / 빌드) công cụ (tool / 도구), khung phần mềm (framework / 프레임워크), DBMS, middleware, VCS và CI/CD công cụ (tool / 도구). Đề thường hỏi vai trò từng công cụ (tool / 도구), vì vậy cần phân category thay vì nhớ tên thương hiệu.

Trình biên dịch (compiler / 컴파일러) dịch nguồn (source / 소스) sang machine/intermediate mã (code / 코드) trước khi chạy theo mô hình truyền thống. trình thông dịch (interpreter / 인터프리터) thực thi/phân tích từng phần thời gian chạy (runtime / 런타임). JIT kết hợp bằng cách compile hot mã (code / 코드) trong thời gian chạy (runtime / 런타임).

Khung phần mềm (framework / 프레임워크) cung cấp skeleton/điều khiển (control / 제어) inversion; thư viện (library / 라이브러리) là mã (code / 코드) được ứng dụng (application / 애플리케이션) chủ động gọi. Đây là khác biệt cốt lõi: với khung phần mềm (framework / 프레임워크), luồng (flow / 흐름) điều khiển (control / 제어) thường được khung phần mềm (framework / 프레임워크) nắm giữ rồi gọi mã (code / 코드) của ứng dụng (application / 애플리케이션) theo vòng đời (lifecycle / 생명주기)/hook.

### 1.2 dùng chung (common / 공통) mô-đun (module / 모듈) và máy chủ (server / 서버) lô-gic (logic / 논리)

Máy chủ (server / 서버) program thường nhận yêu cầu (request / 요청), validate đầu vào (input / 입력), thực thi lô-gic nghiệp vụ (business logic / 비즈니스 로직), truy cập persistence/tài nguyên (resource / 자원), tạo phản hồi (response / 응답) và log/monitor lỗi (error / 오류). Layering giúp tách presentation/API, ứng dụng (application / 애플리케이션)/dịch vụ (service / 서비스), lĩnh vực (domain / 도메인) và hạ tầng (infrastructure / 인프라)/persistence.

Không phải mọi tầng (layer / 계층) đều bắt buộc trong mọi hệ thống (system / 시스템), nhưng đề lý thuyết thường đánh giá separation of concerns và mô-đun (module / 모듈) independence.

### 1.3 Batch Processing

Batch xử lý job theo tập dữ liệu và schedule, phù hợp khi không cần phản hồi (response / 응답) interactive tức thời. Online/giao dịch (transaction / 트랜잭션) processing xử lý yêu cầu (request / 요청) gần real-time. Batch lớn cần restartability, checkpoint, idempotency và lỗi (error / 오류) isolation để không phải chạy lại toàn bộ khi một phần thất bại.

## 2. 프로그래밍 언어 활용 — Programming ngôn ngữ (language / 언어) ứng dụng (application / 애플리케이션)

## 2.1 dùng chung (common / 공통) ngôn ngữ (language / 언어) concepts

### Variable, phạm vi (scope / 범위), phạm vi tồn tại (lifetime scope / 수명 범위) là vùng mã nguồn (source code / 소스 코드) có thể truy cập identifier. thời gian tồn tại (lifetime / 수명) là khoảng thời gian đối tượng (object / 객체)/variable tồn tại trong thời gian chạy (runtime / 런타임). Hai khái niệm liên quan nhưng không đồng nhất.

Cục bộ (local / 로컬) variable thường có phạm vi (scope / 범위) hẹp; toàn cục (global / 전역)/static trạng thái (state / 상태) sống lâu hơn. Static cục bộ (local / 로컬) trong C có cục bộ (local / 로컬) phạm vi (scope / 범위) nhưng thời gian tồn tại (lifetime / 수명) kéo dài suốt tiến trình (process / 프로세스).

### Giá trị (value / 값) vs tham chiếu (reference / 참조) ngữ nghĩa (semantics / 의미론)

Giá trị (value / 값) ngữ nghĩa (semantics / 의미론) bản sao (copy / 복사) giá trị. tham chiếu (reference / 참조) ngữ nghĩa (semantics / 의미론) bản sao (copy / 복사) tham chiếu (reference / 참조) tới đối tượng (object / 객체) chung. Nhiều bug đề thi xuất phát từ việc hai biến cùng trỏ một đối tượng (object / 객체) mutable.

### Parameter Passing

Lời gọi (call / 호출) by giá trị (value / 값) truyền bản sao giá trị (value / 값). Nếu giá trị (value / 값) đó bản thân là pointer/tham chiếu (reference / 참조), hàm (function / 함수) nhận bản sao của pointer nhưng vẫn có thể mutate đối tượng (object / 객체) được trỏ tới. Đây là lý do Java được mô tả là pass-by-value, kể cả đối tượng (object / 객체) tham chiếu (reference / 참조).

## 3. C ngôn ngữ (language / 언어)

### 3.1 Pointer

Pointer lưu address. `&x` lấy địa chỉ x; `*p` dereference pointer p để truy cập giá trị (value / 값) tại address.

Ví dụ:

```c
int x = 10;
int *p = &x;
*p = 20;
```

Sau đó `x` là 20 vì `p` trỏ tới x.

Phải phân biệt:

- `p` = address.
- `*p` = giá trị (value / 값) tại address.
- `&p` = address của biến pointer p.

### 3.2 Pointer arithmetic

Nếu `p` là `int*`, `p + 1` trỏ tới phần tử int kế tiếp, tăng theo `sizeof(int)`, không chỉ tăng 1 byte về ngữ nghĩa (semantics / 의미론) C pointer arithmetic.

### 3.3 Array và Pointer

Trong nhiều expression, array name decay thành pointer tới phần tử đầu, nhưng array và pointer không hoàn toàn là cùng một kiểu (type / 타입)/thực thể (entity / 엔터티). `sizeof(array)` trong cùng phạm vi (scope / 범위) array thật có thể cho total array kích thước (size / 크기), trong khi `sizeof(pointer)` chỉ cho pointer kích thước (size / 크기).

### 3.4 String

C string là chuỗi (sequence / 시퀀스) char kết thúc bằng `\0`. `strlen` đếm ký tự trước null terminator, không tính `\0`. Buffer đủ chỗ phải tính thêm null terminator.

### 3.5 struct / union

`struct` cấp lưu trữ (storage / 저장소) cho các member (có padding/alignment). `union` cho các member dùng chung vùng lưu trữ (storage / 저장소); tại một thời điểm interpretation hợp lệ phụ thuộc member được ghi/đọc và quy tắc (rule / 규칙) ngôn ngữ.

### 3.6 Increment operators

`i++` trả giá trị (value / 값) cũ rồi increment như side tác động (effect / 효과) theo ngữ nghĩa (semantics / 의미론) expression; `++i` increment trước rồi giá trị (value / 값) expression là giá trị (value / 값) mới. Trong expression phức tạp, đừng đoán bằng trực giác; dấu vết (trace / 추적) chuỗi (sequence / 시퀀스) cẩn thận và tránh dựa vào mã (code / 코드) có undefined hành vi (behavior / 동작).

### 3.7 Recursion

Recursion cần cơ sở (base / 기반) trường hợp (case / 사례) và recursive step tiến về cơ sở (base / 기반) trường hợp (case / 사례). Mỗi lời gọi (call / 호출) thường tạo ngăn xếp (stack / 스택) frame; recursion sâu có thể ngăn xếp (stack / 스택) overflow.

## 4. Java

### 4.1 lớp (class / 클래스), đối tượng (object / 객체), Inheritance

Lớp (class / 클래스) định nghĩa kiểu (type / 타입)/hành vi (behavior / 동작); đối tượng (object / 객체) là instance thời gian chạy (runtime / 런타임). Inheritance tạo subtype quan hệ (relation / 관계). Java chỉ single inheritance cho lớp (class / 클래스) nhưng hỗ trợ nhiều giao diện (interface / 인터페이스).

### 4.2 Overloading vs Overriding

Overloading: cùng phương thức (method / 메서드) name, parameter danh sách (list / 목록) khác trong compile-time resolution. Return kiểu (type / 타입) đơn độc không đủ để overload.

Overriding: subclass cung cấp hiện thực (implementation / 구현) mới cho instance phương thức (method / 메서드) có signature tương thích; thời gian chạy (runtime / 런타임) động (dynamic / 동적) dispatch chọn phương thức (method / 메서드) theo actual đối tượng (object / 객체).

### 4.3 Polymorphism

```java
Animal a = new Dog();
a.sound();
```

Nếu `Dog` override `sound`, thời gian chạy (runtime / 런타임) gọi `Dog.sound()`. tham chiếu (reference / 참조) kiểu (type / 타입) `Animal` giới hạn member có thể truy cập compile-time; actual đối tượng (object / 객체) `Dog` quyết định overridden phương thức (method / 메서드) thời gian chạy (runtime / 런타임).

### 4.4 Abstract lớp (class / 클래스) vs giao diện (interface / 인터페이스)

Abstract lớp (class / 클래스) có thể giữ trạng thái (state / 상태), constructor và cả concrete/abstract phương thức (method / 메서드). giao diện (interface / 인터페이스) mô tả đặc tả hợp đồng (contract / 계약); Java hiện đại cho phép default/static/private phương thức (method / 메서드) tùy phiên bản (version / 버전), nhưng concept thi cơ bản vẫn là lớp trừu tượng (abstraction / 추상화) đặc tả hợp đồng (contract / 계약) và multiple giao diện (interface / 인터페이스) hiện thực (implementation / 구현).

### 4.5 Exception

Checked exception thường cần catch/declare compile-time; unchecked exception là RuntimeException hierarchy. `finally` thường dùng cleanup và được chạy trong luồng (flow / 흐름) bình thường/exception trừ một số termination đặc biệt.

### 4.6 String

Java String immutable. thao tác (operation / 연산) như concat tạo String mới về ngữ nghĩa (semantic / 의미적); StringBuilder mutable và phù hợp nhiều append trong vòng lặp (loop / 루프).

### 4.7 truy cập (access / 접근) modifier

`public`: rộng nhất. `private`: trong lớp (class / 클래스). `protected`: gói (package / 패키지) + subclass theo quy tắc (rule / 규칙) Java. Không modifier: package-private.

## 5. Python

### 5.1 đối tượng (object / 객체)/tham chiếu (reference / 참조) mô hình (model / 모델)

Python variable name bind tới đối tượng (object / 객체). Assignment không bản sao (copy / 복사) đối tượng (object / 객체) mặc định.

```python
a = [1, 2]
b = a
b.append(3)
```

Cả `a` và `b` cùng thấy danh sách (list / 목록) `[1,2,3]` vì cùng tham chiếu (reference / 참조) một danh sách (list / 목록) mutable.

### 5.2 Mutable vs Immutable

Danh sách (list / 목록), dict, set thường mutable. int, float, str, tuple thường immutable theo ngữ nghĩa (semantic / 의미적) cơ bản. Tuple có thể chứa mutable đối tượng (object / 객체); “tuple immutable” nghĩa cấu trúc tham chiếu (reference / 참조) của tuple không đổi, không bảo đảm mọi đối tượng (object / 객체) bên trong immutable.

### 5.3 Slicing

`a[start:stop:step]` stop là exclusive. Negative chỉ mục (index / 인덱스) đếm từ cuối. Cần luyện tay vì câu hỏi dễ hỏi đầu ra (output / 출력) ngắn.

### 5.4 hàm (function / 함수) argument

Python dùng object-sharing/call-by-object-reference terminology tùy giáo trình. Cách an toàn: hàm (function / 함수) nhận binding tới cùng đối tượng (object / 객체); mutate đối tượng (object / 객체) mutable có thể thấy bên ngoài, rebinding cục bộ (local / 로컬) name không tự đổi binding của caller.

### 5.5 Comprehension

Danh sách (list / 목록) comprehension rút gọn transform/filter. Ví dụ `[x*x for x in range(5) if x % 2 == 0]` → `[0,4,16]`.

### 5.6 Exception

`try/except/else/finally`: except xử lý lỗi (error / 오류), else chạy khi try không raise, finally dùng cleanup và chạy bất kể success/thất bại (failure / 실패) trong luồng (flow / 흐름) bình thường.

## 6. 운영체제 기초 활용 — Operating hệ thống (system / 시스템) Foundations

### 6.1 tiến trình (process / 프로세스) vs luồng thực thi (thread / 스레드)

Tiến trình (process / 프로세스) có address không gian (space / 공간)/tài nguyên (resource / 자원) ngữ cảnh (context / 맥락) riêng. luồng thực thi (thread / 스레드) là đơn vị thực thi (execution unit / 실행 유닛) trong tiến trình (process / 프로세스) và thường share address không gian (space / 공간)/resources với luồng thực thi (thread / 스레드) cùng tiến trình (process / 프로세스).

Ngữ cảnh (context / 맥락) switch giữa tiến trình (process / 프로세스) thường nặng hơn luồng thực thi (thread / 스레드), nhưng detail phụ thuộc OS. dùng chung (shared / 공유) bộ nhớ (memory / 메모리) giữa luồng thực thi (thread / 스레드) giúp communication nhanh nhưng tạo synchronization bài toán (problem / 문제).

### 6.2 tiến trình (process / 프로세스) trạng thái (state / 상태)

Các trạng thái (state / 상태) điển hình: New, Ready, Running, Waiting/Blocked, Terminated. Ready có CPU-ready nhưng đang chờ CPU. Blocked chờ sự kiện (event / 이벤트)/I/O, không chỉ chờ scheduler.

### 6.3 Scheduling

**FCFS** non-preemptive, đơn giản, có convoy tác động (effect / 효과). **SJF** chọn burst ngắn nhất, tối ưu average waiting thời gian (time / 시간) trong điều kiện biết burst nhưng có starvation. **SRTF** là preemptive form của SJF. **Round Robin** dùng thời gian (time / 시간) quantum, phù hợp time-sharing. **Priority Scheduling** chọn priority và có thể starvation; aging giảm starvation. **HRN** dùng phản hồi (response / 응답) ratio để cân bằng waiting/burst.

HRN phản hồi (response / 응답) ratio:

`(Waiting Time + Service Time) / Service Time`

### 6.4 Scheduling metrics

Turnaround thời gian (time / 시간) = Completion - Arrival. Waiting thời gian (time / 시간) = Turnaround - CPU Burst (trong bài đơn giản không I/O). phản hồi (response / 응답) thời gian (time / 시간) = First Run - Arrival.

Đề tính tay cần vẽ Gantt chart trước rồi mới tính chỉ số (metric / 지표).

### 6.5 Synchronization

Race điều kiện (condition / 조건) xảy ra khi kết quả (result / 결과) phụ thuộc timing interleaving. trọng yếu (critical / 중요) section là vùng truy cập dùng chung (shared / 공유) tài nguyên (resource / 자원) cần synchronization.

Mutex cung cấp mutual exclusion quyền sở hữu (ownership / 소유권). Semaphore là counter synchronization thành phần nguyên thủy (primitive / 기본 요소) có wait/tín hiệu (signal / 신호); nhị phân (binary / 이진) semaphore có thể giống mutex ở một số use trường hợp (case / 사례) nhưng ngữ nghĩa (semantics / 의미론) quyền sở hữu (ownership / 소유권) khác.

### 6.6 Deadlock

Bốn điều kiện Coffman: Mutual Exclusion, Hold and Wait, No Preemption, Circular Wait. Phá ít nhất một điều kiện có thể prevent deadlock.

Banker's thuật toán (algorithm / 알고리즘) là ví dụ deadlock avoidance dựa safe trạng thái (state / 상태), không phải detection.

### 6.7 bộ nhớ (memory / 메모리) Management

Paging chia virtual bộ nhớ (memory / 메모리) thành fixed-size page và vật lý (physical / 물리적) bộ nhớ (memory / 메모리) thành frame. Segmentation chia theo logical segment variable-size.

Nội bộ (internal / 내부) fragmentation thường gắn fixed-size allocation; bên ngoài (external / 외부) fragmentation thường gắn variable-size contiguous allocation.

### 6.8 Virtual bộ nhớ (memory / 메모리)

Page fault xảy ra khi referenced page không ở bộ nhớ (memory / 메모리). OS phải tải (load / 로드) page từ backing store, có thể cần chọn victim page.

Page replacement:

- FIFO: thay page vào sớm nhất.
- LRU: thay page lâu nhất chưa dùng.
- Optimal: thay page sẽ được dùng xa nhất trong tương lai; dùng làm benchmark vì không thực tế biết future.
- LFU: dựa frequency, cần xử lý lịch sử (history / 이력)/tie.

Belady's Anomaly có thể xảy ra với FIFO: tăng frame nhưng page fault tăng. ngăn xếp (stack / 스택) algorithms như LRU/Optimal không có anomaly này theo thuộc tính (property / 속성) kinh điển.

### 6.9 Thrashing

Thrashing xảy ra khi hệ thống (system / 시스템) dành quá nhiều thời gian paging do working set không đủ frame. CPU utilization có thể giảm dù multiprogramming cao. Working-set/điều khiển (control / 제어) page-fault frequency là các approach liên quan.

### 6.10 tệp (file / 파일) hệ thống (system / 시스템)

Tệp (file / 파일) allocation chiến lược (strategy / 전략) có thể contiguous, linked, indexed. Contiguous nhanh sequential/random nhưng khó grow và bên ngoài (external / 외부) fragmentation. Linked dễ grow nhưng random truy cập (access / 접근) kém. Indexed dùng chỉ mục (index / 인덱스) khối (block / 블록) để trỏ dữ liệu (data / 데이터) khối (block / 블록).

## 7. 네트워크 기초 활용 — mạng (network / 네트워크) Foundations

### 7.1 OSI 7 Layers

1 vật lý (physical / 물리적) — bit/tín hiệu (signal / 신호)/media.
2 dữ liệu (data / 데이터) Link — frame, MAC, cục bộ (local / 로컬) link.
3 mạng (network / 네트워크) — packet, IP, routing.
4 vận chuyển (transport / 전송) — end-to-end vận chuyển (transport / 전송), TCP/UDP, cổng (port / 포트).
5 Session — session điều khiển (control / 제어).
6 Presentation — biểu diễn (representation / 표현)/encoding/encryption/compression concept.
7 ứng dụng (application / 애플리케이션) — giao thức (protocol / 프로토콜)/dịch vụ (service / 서비스) gần ứng dụng (application / 애플리케이션).

Trong Internet ngăn xếp (stack / 스택) thực tế, Session/Presentation thường không tách rõ như OSI tham chiếu (reference / 참조) mô hình (model / 모델).

### 7.2 TCP vs UDP

TCP connection-oriented, reliable byte stream, thứ tự (ordering / 순서), retransmission, luồng (flow / 흐름)/congestion điều khiển (control / 제어). UDP connectionless datagram, không bảo đảm delivery/thứ tự (order / 순서), overhead thấp hơn.

“UDP nhanh hơn” chỉ là shorthand. ứng dụng (application / 애플리케이션) có thể tự thêm độ tin cậy (reliability / 신뢰성) và chi phí (cost / 비용) khác; chọn giao thức (protocol / 프로토콜) dựa yêu cầu (requirement / 요구사항).

### 7.3 dùng chung (common / 공통) Protocols

HTTP/HTTPS: web ứng dụng (application / 애플리케이션) giao thức (protocol / 프로토콜). DNS: name resolution. DHCP: cấp mạng (network / 네트워크) cấu hình (configuration / 구성) động. FTP: tệp (file / 파일) transfer truyền thống. SMTP: gửi mail. POP3/IMAP: nhận/quản lý mail. SSH: secure remote shell. SNMP: mạng (network / 네트워크) management. NTP: thời gian (time / 시간) synchronization.

Cổng (port / 포트) number có thể được hỏi, nhưng nên học những cổng (port / 포트) nền tảng: HTTP 80, HTTPS 443, SSH 22, DNS 53, SMTP 25, FTP điều khiển (control / 제어) 21. Đừng dành quá nhiều thời gian thuộc mọi cổng (port / 포트) hiếm trước khi cốt lõi (core / 핵심) concept vững.

### 7.4 IPv4 và Subnet

IPv4 có 32 bit. Prefix `/n` dành n bit mạng (network / 네트워크), còn `32-n` bit host.

Số address trong subnet = `2^(32-n)`. Trong subnet truyền thống, usable host thường trừ mạng (network / 네트워크) và broadcast, ngoại trừ các special prefix/use trường hợp (case / 사례).

Ví dụ `/26`: còn 6 host bit → 64 address, thường 62 usable host.

Subnet mask `/26` = `255.255.255.192`, khối (block / 블록) kích thước (size / 크기) ở octet cuối = 64.

### 7.5 Routing

Static routing cấu hình thủ công. động (dynamic / 동적) routing dùng routing giao thức (protocol / 프로토콜).

Distance véc-tơ (vector / 벡터) chia sẻ distance/véc-tơ (vector / 벡터) với neighbor, ví dụ RIP truyền thống. Link trạng thái (state / 상태) xây topology map và chạy shortest-path thuật toán (algorithm / 알고리즘), ví dụ OSPF. BGP là path-vector/inter-domain routing giữa autonomous các hệ thống (systems / 시스템들).

### 7.6 LAN devices

Hub phát frame/bit ra nhiều cổng (port / 포트) và hoạt động đơn giản ở vật lý (physical / 물리적) tầng (layer / 계층) concept. Switch học MAC address và forward frame ở dữ liệu (data / 데이터) Link tầng (layer / 계층). Router tuyến (route / 경로) packet giữa mạng (network / 네트워크) ở mạng (network / 네트워크) tầng (layer / 계층).

### 7.7 ARP, ICMP

ARP map IPv4 address sang MAC trong cục bộ (local / 로컬) mạng (network / 네트워크). ICMP hỗ trợ điều khiển (control / 제어)/lỗi (error / 오류) diagnostics như ping concept. DNS không làm nhiệm vụ map IP sang MAC.

## 8. Cặp dễ nhầm

| Cặp | Điểm tách |
|---|---|
| khung phần mềm (framework / 프레임워크) vs thư viện (library / 라이브러리) | inversion of điều khiển (control / 제어) vs app chủ động gọi |
| phạm vi (scope / 범위) vs thời gian tồn tại (lifetime / 수명) | vùng truy cập tên vs thời gian đối tượng (object / 객체) tồn tại |
| Overloading vs Overriding | compile-time signature vs subtype hành vi thời gian chạy (runtime behavior / 런타임 동작) |
| giá trị (value / 값) vs tham chiếu (reference / 참조) ngữ nghĩa (semantics / 의미론) | bản sao (copy / 복사) giá trị (value / 값) vs alias cùng đối tượng (object / 객체) |
| tiến trình (process / 프로세스) vs luồng thực thi (thread / 스레드) | address không gian (space / 공간)/tài nguyên (resource / 자원) ngữ cảnh (context / 맥락) vs đơn vị thực thi (execution unit / 실행 유닛) share tiến trình (process / 프로세스) |
| Ready vs Blocked | chờ CPU vs chờ sự kiện (event / 이벤트)/I/O |
| SJF vs SRTF | non-preemptive vs preemptive |
| Paging vs Segmentation | fixed-size page/frame vs logical variable segment |
| nội bộ (internal / 내부) vs bên ngoài (external / 외부) fragmentation | lãng phí trong khối (block / 블록) vs lỗ trống giữa khối (block / 블록) |
| FIFO vs LRU | oldest loaded vs least recently used |
| TCP vs UDP | reliable liên kết (connection / 연결) stream vs connectionless datagram |
| Switch vs Router | MAC/L2 vs IP/L3 |
| DNS vs ARP | name→IP vs IPv4→MAC cục bộ (local / 로컬) |

## 9. Procedural drills

### Drill 1 — C Pointer

```c
int x = 5;
int *p = &x;
(*p)++;
printf("%d", x);
```

Tự dấu vết (trace / 추적) đầu ra (output / 출력) và giải thích từng bước.

### Drill 2 — Java Polymorphism

Cho `Parent p = new Child();`, Child override `run()`. Khi gọi `p.run()` phương thức (method / 메서드) nào chạy? Nếu trường dữ liệu (field / 필드) `name` được khai báo ở cả Parent và Child thì trường dữ liệu (field / 필드) truy cập (access / 접근) có ngữ nghĩa (semantics / 의미론) giống phương thức (method / 메서드) dispatch không?

### Drill 3 — Python alias

```python
a = [1, 2]
b = a
b = b + [3]
```

Sau đó a và b là gì? So sánh với `b.append(3)`.

### Drill 4 — Round Robin

Ba tiến trình (process / 프로세스) tới thời gian (time / 시간) 0 với burst P1=5, P2=3, P3=1, quantum=2. Vẽ Gantt chart và tính completion/waiting thời gian (time / 시간).

### Drill 5 — Page replacement

Tham chiếu (reference / 참조) string `1 2 3 1 4 2 5 1 2 3 4 5`, 3 frame. Tính page fault cho FIFO và LRU.

### Drill 6 — Deadlock

Giải thích tại sao chỉ có Mutual Exclusion + Hold and Wait chưa đủ kết luận deadlock nếu chưa có No Preemption và Circular Wait.

### Drill 7 — Subnet

`192.168.10.130/26`: tìm mạng (network / 네트워크) address, broadcast address và usable host phạm vi (range / 범위).

### Drill 8 — OSI

Một switch xử lý MAC address, router xử lý IP tuyến (route / 경로), TCP dùng cổng (port / 포트). Map ba thao tác này vào OSI tầng (layer / 계층).

## 10. 과락 방지 checklist — Môn 4

Phải tự làm được:

- phân loại trình biên dịch (compiler / 컴파일러)/trình thông dịch (interpreter / 인터프리터)/JIT, khung phần mềm (framework / 프레임워크)/thư viện (library / 라이브러리), bản dựng (build / 빌드)/thời gian chạy (runtime / 런타임) công cụ (tool / 도구);
- dấu vết (trace / 추적) C pointer/array/string và operator cơ bản;
- phân biệt Java overloading/overriding/polymorphism/giao diện (interface / 인터페이스)/abstract lớp (class / 클래스);
- dấu vết (trace / 추적) Python mutable/tham chiếu (reference / 참조)/slicing/comprehension;
- phân biệt phạm vi (scope / 범위)/thời gian tồn tại (lifetime / 수명) và giá trị (value / 값)/tham chiếu (reference / 참조) hành vi (behavior / 동작);
- vẽ tiến trình (process / 프로세스) trạng thái (state / 상태) và giải scheduling FCFS/SJF/SRTF/RR/Priority/HRN;
- tính turnaround/waiting/phản hồi (response / 응답) thời gian (time / 시간);
- giải synchronization, semaphore/mutex và deadlock;
- phân biệt paging/segmentation, fragmentation, virtual bộ nhớ (memory / 메모리);
- tính FIFO/LRU/Optimal page replacement bài ngắn;
- giải OSI/TCP-IP, TCP/UDP, giao thức (protocol / 프로토콜) và mạng (network / 네트워크) thiết bị (device / 장치);
- tính subnet IPv4;
- phân biệt routing concept, ARP/DNS/ICMP.

Môn 4 phải luyện bằng giấy. Chỉ đọc mã (code / 코드) và công thức sẽ tạo false confidence.
