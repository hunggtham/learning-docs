# Bộ chứa (container / 컨테이너): ảnh (image / 이미지), thời gian chạy (runtime / 런타임), isolation và môi trường vận hành (production / 운영 환경) hành vi (behavior / 동작)

> **Mạch đọc:** Đọc **bộ chứa (container / 컨테이너): ảnh (image / 이미지), thời gian chạy (runtime / 런타임), isolation và môi trường vận hành (production / 운영 환경) hành vi (behavior / 동작)** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. bộ chứa (container / 컨테이너) không phải máy ảo nhỏ** sang **2. ảnh (image / 이미지) là filesystem + siêu dữ liệu (metadata / 메타데이터) bất biến theo tầng (layer / 계층)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


## 1. bộ chứa (container / 컨테이너) không phải máy ảo nhỏ

Bộ chứa (container / 컨테이너) trước hết là tiến trình (process / 프로세스) được kernel cô lập và giới hạn bằng các thành phần nguyên thủy (primitive / 기본 요소) của hệ điều hành. Nó dùng kernel của host thay vì mang kernel riêng như VM truyền thống. Namespaces quyết định tiến trình (process / 프로세스) nhìn thấy gì; cgroups quyết định tài nguyên (resource / 자원) account/điều khiển (control / 제어); capabilities và seccomp thu hẹp quyền kernel.

Cơ chế sâu đã có tại [containers, namespaces, cgroups, capabilities và seccomp](../../computer_science/03_operating_systems/advanced/06_containers_namespaces_cgroups_capabilities_and_seccomp.md). Chapter này tập trung cách các thành phần nguyên thủy (primitive / 기본 요소) đó biến thành ảnh (image / 이미지)/thời gian chạy (runtime / 런타임) workflow.

## 2. ảnh (image / 이미지) là filesystem + siêu dữ liệu (metadata / 메타데이터) bất biến theo tầng (layer / 계층)

Ảnh bộ chứa (container image / 컨테이너 이미지) thường gồm nhiều tầng (layer / 계층) content-addressed và siêu dữ liệu (metadata / 메타데이터) như command, môi trường (environment / 환경), người dùng (user / 사용자). ảnh (image / 이미지) không phải “snapshot của một máy chủ (server / 서버) đang chạy” theo nghĩa truyền thống; nó là gói (package / 패키지) để thời gian chạy (runtime / 런타임) tạo gốc (root / 루트) filesystem và tiến trình (process / 프로세스) môi trường (environment / 환경).

Layering giúp bộ nhớ đệm (cache / 캐시) và phân phối (distribution / 분포), nhưng cũng tạo hiểu nhầm. Xóa secret ở tầng (layer / 계층) sau không có nghĩa secret biến mất khỏi tầng (layer / 계층) cũ. Vì vậy credential không nên `COPY` vào bản dựng (build / 빌드) ngữ cảnh (context / 맥락)/ảnh (image / 이미지) rồi xóa. Multi-stage bản dựng (build / 빌드) giúp chỉ đưa đầu ra (output / 출력) cần thiết sang final ảnh (image / 이미지).

## 3. bộ chứa (container / 컨테이너) vòng đời (lifecycle / 생명주기) gắn với tiến trình (process / 프로세스) chính

Bộ chứa (container / 컨테이너) sống khi tiến trình (process / 프로세스) chính còn sống. Nếu tiến trình (process / 프로세스) chính thoát, bộ chứa (container / 컨테이너) hoàn thành dù child tiến trình (process / 프로세스) khác có thể từng được tạo. Vì vậy mẫu (pattern / 패턴) daemonize bên trong bộ chứa (container / 컨테이너) thường không cần thiết.

Tín hiệu (signal / 신호) handling đặc biệt quan trọng. thời gian chạy (runtime / 런타임)/orchestrator gửi tín hiệu (signal / 신호) cho tiến trình (process / 프로세스) chính khi stop. ứng dụng (application / 애플리케이션) phải nhận và shutdown theo deadline. Nếu dùng shell wrapper không `exec` tiến trình (process / 프로세스) thật, tín hiệu (signal / 신호) có thể dừng ở shell. điểm vào (entrypoint / 진입점) cần được hiểu như vòng đời (lifecycle / 생명주기) adapter chứ không chỉ script tiện lợi.

## 4. ảnh (image / 이미지) nhỏ không phải mục tiêu duy nhất

Giảm ảnh (image / 이미지) kích thước (size / 크기) cải thiện pull thời gian (time / 시간) và attack surface, nhưng ảnh (image / 이미지) tối thiểu đến mức không còn certificate CA, timezone dữ liệu (data / 데이터) hoặc diagnostic năng lực (capability / 역량) cần thiết có thể gây lỗi môi trường vận hành (production / 운영 환경) khó hiểu. Chọn cơ sở (base / 기반) ảnh (image / 이미지) dựa trên thời gian chạy (runtime / 런타임) yêu cầu (requirement / 요구사항), vulnerability surface, cập nhật (update / 업데이트) chính sách (policy / 정책) và operability.

Distroless phù hợp nhiều tải công việc (workload / 워크로드) nhưng debugging thường cần ephemeral/gỡ lỗi (debug / 디버그) bộ chứa (container / 컨테이너) hoặc công cụ (tool / 도구) ở nút (node / 노드); không nên vì thiếu `curl` mà cài một loạt gói (package / 패키지) trực tiếp vào môi trường vận hành (production / 운영 환경) bộ chứa (container / 컨테이너) lúc sự cố (incident / 인시던트).

## 5. Dockerfile là bản dựng (build / 빌드) đồ thị (graph / 그래프)

Đọc Dockerfile như một đồ thị (graph / 그래프) bộ nhớ đệm (cache / 캐시). Instruction nào phụ thuộc đầu vào (input / 입력) thường thay đổi nên đặt sau instruction ổn định nếu muốn reuse bộ nhớ đệm (cache / 캐시). Ví dụ với nút (node / 노드)/Java, phụ thuộc (dependency / 의존성) descriptor/lockfile có thể bản sao (copy / 복사) trước, resolve phụ thuộc (dependency / 의존성), rồi mới bản sao (copy / 복사) nguồn (source / 소스).

Tuy nhiên bộ nhớ đệm (cache / 캐시) tính đúng đắn (correctness / 정확성) ưu tiên speed. bản dựng (build / 빌드) argument, secret mount và nền tảng (platform / 플랫폼) mục tiêu (target / 대상) phải được dùng theo ngữ nghĩa (semantics / 의미론) đúng. Secret cho gói (package / 패키지) registry nên dùng bản dựng (build / 빌드) secret cơ chế (mechanism / 메커니즘) thay vì `ARG` hoặc `ENV` có nguy cơ lưu vào lịch sử (history / 이력)/tầng (layer / 계층).

## 6. gốc (root / 루트) inside bộ chứa (container / 컨테이너) vẫn là quyền đáng chú ý

“gốc (root / 루트) trong bộ chứa (container / 컨테이너)” không tự động bằng gốc (root / 루트) host, nhưng nếu bộ chứa (container / 컨테이너) escape vulnerability, mount nhạy cảm hoặc năng lực (capability / 역량) quá rộng thì impact tăng. môi trường vận hành (production / 운영 환경) default nên chạy non-root khi ứng dụng (application / 애플리케이션) không cần đặc quyền, drop năng lực (capability / 역량) không dùng, dùng read-only filesystem khi phù hợp và tránh mount host socket kiểu `/var/run/docker.sock` trừ khi hiểu rõ quyền tương đương control-plane mà nó trao.

Bộ chứa (container / 컨테이너) bảo mật (security / 보안) là defense in độ sâu (depth / 깊이), không dựa vào một không gian tên (namespace / 네임스페이스) ranh giới (boundary / 경계) duy nhất.

## 7. yêu cầu tài nguyên (resource request / 리소스 요청)/limit bắt đầu từ cgroup

Khi orchestrator đặt giới hạn bộ nhớ (memory limit / 메모리 제한), kernel/cgroup cuối cùng là nơi enforce. bộ nhớ (memory / 메모리) vượt ranh giới (boundary / 경계) có thể dẫn tới OOM kill. Giới hạn CPU (CPU limit / CPU 제한) thường dẫn tới throttling thay vì kill. Vì vậy thất bại (failure / 실패) mẫu (pattern / 패턴) khác nhau: bộ nhớ (memory / 메모리) issue có tiến trình (process / 프로세스) chết; CPU issue thường là độ trễ (latency / 지연 시간) tăng.

Đừng đặt tài nguyên (resource / 자원) limit bằng cách bản sao (copy / 복사) con số giữa dịch vụ (service / 서비스). Cần đo working set, tính đồng thời (concurrency / 동시성), hành vi thời gian chạy (runtime behavior / 런타임 동작) và peak. Với JVM/managed thời gian chạy (runtime / 런타임), vùng nhớ động (heap / 힙) sizing phải tính cả bản địa (native / 네이티브) bộ nhớ (memory / 메모리) và bộ chứa (container / 컨테이너) awareness.

## 8. Writable tầng (layer / 계층) là ephemeral trạng thái (state / 상태)

Bộ chứa (container / 컨테이너) writable tầng (layer / 계층) thường không phải nơi lưu trạng thái (state / 상태) cần tồn tại sau reschedule. Log tệp (file / 파일), upload và cơ sở dữ liệu (database / 데이터베이스) dữ liệu (data / 데이터) nếu chỉ ở writable tầng (layer / 계층) có thể mất khi bộ chứa (container / 컨테이너) bị thay. Stateful dữ liệu (data / 데이터) phải đi qua volume/lưu trữ (storage / 저장소) đặc tả hợp đồng (contract / 계약) phù hợp.

“Stateless dịch vụ (service / 서비스)” không có nghĩa tiến trình (process / 프로세스) không có trạng thái (state / 상태); nó có bộ nhớ đệm (cache / 캐시), liên kết (connection / 연결) và in-flight yêu cầu (request / 요청). Nó nghĩa trạng thái (state / 상태) cần durable/authoritative không phụ thuộc định danh (identity / 식별자) của instance cụ thể.

## 9. Health check phải đo đúng ngữ nghĩa (semantics / 의미론)

Liveness trả lời “tiến trình (process / 프로세스) này còn có khả năng tự phục hồi hay cần restart?”. Readiness trả lời “instance này có nên nhận traffic lúc này không?”. Trộn hai ngữ nghĩa (semantics / 의미론) có thể tạo restart vòng lặp (loop / 루프) khi phụ thuộc (dependency / 의존성) tạm lỗi.

Ví dụ cơ sở dữ liệu (database / 데이터베이스) chậm không nhất thiết là lý do kill tiến trình (process / 프로세스). Nếu liveness phụ thuộc DB, outage DB có thể khiến hàng trăm pod restart cùng lúc, tăng tải (load / 로드) khi DB vừa hồi phục. Readiness có thể tạm đưa instance khỏi traffic; liveness nên tập trung deadlock/hang không tự hồi được.

## 10. Tag, digest và promotion

Ảnh (image / 이미지) tag là alias; digest là định danh (identity / 식별자) content. môi trường vận hành (production / 운영 환경) bản phát hành (release / 릴리스) nên có khả năng truy vết digest. Nếu manifest chỉ ghi tag mutable, rollout/restart ở hai thời điểm có thể lấy ảnh (image / 이미지) khác nhau.

Bản dựng (build / 빌드) một lần, ký/scanning siêu dữ liệu (metadata / 메타데이터) một lần, rồi promote digest là mẫu (pattern / 패턴) giúp giảm bất định (uncertainty / 불확실성).

## 11. gỡ lỗi (debug / 디버그) bộ chứa (container / 컨테이너) theo tầng (layer / 계층)

Khi bộ chứa (container / 컨테이너) thất bại (fail / 실패) start, xem ảnh (image / 이미지)/điểm vào (entrypoint / 진입점)/cấu hình (config / 설정) trước mạng (network / 네트워크). Khi chạy nhưng unhealthy, xem tiến trình (process / 프로세스), ports, probe và phụ thuộc (dependency / 의존성). Khi bị kill, xem exit mã (code / 코드), OOM/sự kiện (event / 이벤트) và tài nguyên (resource / 자원) pressure. Khi độ trễ (latency / 지연 시간) tăng, xem CPU throttling, bộ nhớ (memory / 메모리)/GC, I/O và mạng (network / 네트워크).

Bộ chứa (container / 컨테이너) không nên trở thành lớp trừu tượng (abstraction / 추상화) khiến operator quên Linux. Nó chỉ thêm một tầng (layer / 계층) packaging và isolation vào cùng mô hình thực thi (execution model / 실행 모델).

## 12. tầng (layer / 계층) bất biến không có nghĩa filesystem thời gian chạy (runtime / 런타임) bất biến

Ảnh (image / 이미지) tầng (layer / 계층) là content-addressed và read-only khi thời gian chạy (runtime / 런타임) ghép filesystem, nhưng bộ chứa (container / 컨테이너) thường có thêm writable tầng (layer / 계층) phía trên. Khi tiến trình (process / 프로세스) sửa một tệp (file / 파일) vốn nằm trong lower tầng (layer / 계층), lưu trữ (storage / 저장소) driver có thể phải thực hiện copy-up trước khi ghi. Vì vậy một tải công việc (workload / 워크로드) ghi nhiều dữ liệu vào writable tầng (layer / 계층) có hành vi (behavior / 동작) I/O khác hẳn đọc ảnh (image / 이미지) bất biến.

Điều này giải thích hai môi trường vận hành (production / 운영 환경) mẫu (pattern / 패턴). Thứ nhất, ghi log dung lượng lớn vào filesystem bộ chứa (container / 컨테이너) có thể làm ephemeral lưu trữ (storage / 저장소) đầy dù ứng dụng (application / 애플리케이션) không lưu “nghiệp vụ (business / 비즈니스) dữ liệu (data / 데이터)”. Thứ hai, tải công việc (workload / 워크로드) write-heavy không nên mặc định dùng overlay writable tầng (layer / 계층) như durable lưu trữ (storage / 저장소) chỉ vì đường dẫn (path / 경로) nhìn giống filesystem bình thường.

Bộ chứa (container / 컨테이너) packaging và lưu trữ (storage / 저장소) durability là hai đặc tả hợp đồng (contract / 계약) khác nhau.

## 13. UID/GID và quyền tệp (file / 파일) phải được lập luận (reasoning / 추론) xuyên ảnh (image / 이미지)–thời gian chạy (runtime / 런타임)–volume

`USER 10001` trong ảnh (image / 이미지) chỉ chọn định danh (identity / 식별자) tiến trình (process / 프로세스) bên trong người dùng (user / 사용자) không gian tên (namespace / 네임스페이스)/thời gian chạy (runtime / 런타임) ngữ cảnh (context / 맥락). Khi mount volume, tệp (file / 파일) trên volume có đơn vị sở hữu (owner / 오너)/chế độ (mode / 모드) riêng. Một ảnh (image / 이미지) chạy tốt trên laptop có thể thất bại (fail / 실패) môi trường vận hành (production / 운영 환경) với `Permission denied` nếu volume được provision với UID/GID khác.

Không nên chữa bằng `chmod 777` hoặc quay lại gốc (root / 루트) theo phản xạ. Hãy xác định tiến trình (process / 프로세스) effective UID/GID, quyền sở hữu (ownership / 소유권) của mount, cơ chế `fsGroup`/thời gian chạy (runtime / 런타임) chính sách (policy / 정책) nếu có và ai chịu trách nhiệm initialize permission. dùng chung (shared / 공유) volume còn cần xét nhiều tiến trình (process / 프로세스) có cùng ánh xạ (mapping / 매핑) định danh (identity / 식별자) hay không.

Đây là ví dụ lớp trừu tượng (abstraction / 추상화) leak giữa ảnh (image / 이미지) siêu dữ liệu (metadata / 메타데이터) và filesystem authorization thực tế.

## 14. PID 1 có ngữ nghĩa (semantics / 의미론) khác tiến trình (process / 프로세스) bình thường

Trong Linux, PID 1 có vai trò đặc biệt đối với tín hiệu (signal / 신호) mặc định và reaping orphaned child. Nếu ứng dụng (application / 애플리케이션) hoặc shell wrapper trở thành PID 1 nhưng không xử lý child vòng đời (lifecycle / 생명주기), zombie tiến trình (process / 프로세스) có thể tích tụ trong tải công việc (workload / 워크로드) tạo nhiều subprocess.

Một init nhỏ có thể hữu ích khi ứng dụng (application / 애플리케이션) không làm tốt vai trò này, nhưng không nên thêm theo nghi thức. Trước hết cần biết tiến trình (process / 프로세스) cây (tree / 트리) thật, ai spawn child và ai phải `wait()` chúng.

Khi shutdown không hoạt động, kiểm tra tín hiệu (signal / 신호) thực sự tới PID nào và wrapper có dùng `exec` hay không. “Orchestrator đã gửi SIGTERM” chưa chứng minh nghiệp vụ (business / 비즈니스) tiến trình (process / 프로세스) nhận được SIGTERM.

## 15. bộ nhớ (memory / 메모리) trong bộ chứa (container / 컨테이너) là tổng footprint theo accounting ranh giới (boundary / 경계)

Vùng nhớ vùng nhớ động (heap / 힙) chỉ là một phần. bản địa (native / 네이티브) allocation, luồng thực thi (thread / 스레드) ngăn xếp (stack / 스택), JIT/mã (code / 코드) bộ nhớ đệm (cache / 캐시), mmap, dùng chung (shared / 공유) bộ nhớ (memory / 메모리) và page bộ nhớ đệm (cache / 캐시) accounting có thể góp vào cgroup bộ nhớ (memory / 메모리) tùy tải công việc (workload / 워크로드)/kernel/thời gian chạy (runtime / 런타임). Vì vậy đặt JVM `-Xmx` bằng đúng giới hạn bộ nhớ (memory limit / 메모리 제한) gần như không để headroom cho phần còn lại.

Một cách lập luận (reasoning / 추론) thực dụng là bắt đầu từ total cgroup usage rồi phân rã xuống thời gian chạy (runtime / 런타임) vùng nhớ động (heap / 힙)/bản địa (native / 네이티브) và kernel/file-backed hành vi (behavior / 동작). Nếu bộ chứa (container / 컨테이너) bị OOMKilled nhưng vùng nhớ động (heap / 힙) chưa đầy, đó không phải mâu thuẫn; hai chỉ số (metric / 지표) đang đo ranh giới (boundary / 경계) khác nhau.

CPU cũng tương tự. ứng dụng (application / 애플리케이션) có thể báo CPU utilization vừa phải nhưng cgroup có throttled thời gian (time / 시간) cao vì demand vượt quota theo từng period. Tail độ trễ (latency / 지연 시간) thường nhạy với throttling hơn average CPU chart.

## 16. ảnh (image / 이미지) kiến trúc (architecture / 아키텍처) và thời gian chạy (runtime / 런타임) kiến trúc (architecture / 아키텍처) phải tương thích

Một ảnh (image / 이미지) có thể được bản dựng (build / 빌드) cho `amd64`, `arm64` hoặc nhiều kiến trúc (architecture / 아키텍처) bằng manifest danh sách (list / 목록)/chỉ mục (index / 인덱스). Tag giống nhau không có nghĩa bytes executable giống nhau ở mọi nút (node / 노드); thời gian chạy (runtime / 런타임) chọn variant phù hợp kiến trúc (architecture / 아키텍처).

Điều này quan trọng khi bản dựng (build / 빌드) trên Apple Silicon nhưng môi trường vận hành (production / 운영 환경) dùng x86, hoặc cluster có nút (node / 노드) hỗn hợp. Emulation có thể làm bản dựng (build / 빌드)/kiểm thử (test / 테스트) “chạy được” nhưng khác hiệu năng (performance / 성능) hoặc bản địa (native / 네이티브) phụ thuộc (dependency / 의존성) hành vi (behavior / 동작) so với thực thi (execution / 실행) thật.

Bản phát hành (release / 릴리스) siêu dữ liệu (metadata / 메타데이터) nên giữ nền tảng (platform / 플랫폼)/kiến trúc (architecture / 아키텍처) định danh (identity / 식별자) khi nó ảnh hưởng sản phẩm tạo ra (artifact / 산출물). bản địa (native / 네이티브) thư viện (library / 라이브러리), JNI, Python wheel hoặc nhị phân (binary / 이진) downloaded trong bản dựng (build / 빌드) là các điểm dễ tạo mismatch.

## 17. Registry availability là phụ thuộc (dependency / 의존성) của scaling và khôi phục (recovery / 복구)

Tải công việc (workload / 워크로드) đang chạy có thể khỏe khi registry lỗi vì ảnh (image / 이미지) đã nằm trên nút (node / 노드). Nhưng scale-out, nút (node / 노드) replacement hoặc disaster khôi phục (recovery / 복구) cần pull ảnh (image / 이미지) mới. Vì vậy registry là phụ thuộc (dependency / 의존성) control-plane của sức chứa (capacity / 용량)/khôi phục (recovery / 복구) dù không nằm trên yêu cầu (request / 요청) dữ liệu (data / 데이터) đường dẫn (path / 경로) bình thường.

Runbook cần phân biệt “ứng dụng (application / 애플리케이션) đang phục vụ” với “cluster có khả năng tạo replica mới”. ảnh (image / 이미지) pull thất bại (failure / 실패) trong lúc nút (node / 노드) autoscale có thể biến traffic spike thành sức chứa (capacity / 용량) sự cố (incident / 인시던트).

Sản phẩm tạo ra (artifact / 산출물) retention cũng là khôi phục (recovery / 복구) đặc tả hợp đồng (contract / 계약). Nếu manifest quay lui (rollback / 롤백) trỏ digest đã bị garbage-collect khỏi registry, quay lui (rollback / 롤백) lô-gic (logic / 논리) đúng trên Git nhưng không thể materialize tải công việc (workload / 워크로드).

## 18. cấp cao (senior / 시니어) walkthrough: Pod khởi động chậm chỉ sau khi nút (node / 노드) mới được thêm

Giả sử Pod trên nút (node / 노드) cũ start trong 5 giây, nhưng Pod trên nút (node / 노드) mới mất 90 giây. ứng dụng (application / 애플리케이션) init log chỉ mất 4 giây. Phần còn lại nằm trước tiến trình (process / 프로세스) startup.

Chuỗi nhân quả (causal chain / 인과 사슬) nên kiểm tra ảnh (image / 이미지) pull kích thước (size / 크기)/tầng (layer / 계층) bộ nhớ đệm (cache / 캐시), registry độ trễ (latency / 지연 시간), nút (node / 노드) egress và volume/mạng (network / 네트워크) setup. Nếu nút (node / 노드) cũ đã bộ nhớ đệm (cache / 캐시) cơ sở (base / 기반) tầng (layer / 계층) còn nút (node / 노드) mới phải kéo ảnh (image / 이미지) 1,5 GiB qua constrained registry/NAT, ứng dụng (application / 애플리케이션) không phải bottleneck.

Mitigation có thể là giảm sản phẩm tạo ra (artifact / 산출물) kích thước (size / 크기) hợp lý, pre-pull cho tải công việc (workload / 워크로드) trọng yếu (critical / 중요), tăng registry/egress sức chứa (capacity / 용량) hoặc giữ warm sức chứa (capacity / 용량). Bài học không phải “ảnh (image / 이미지) càng nhỏ càng tốt”, mà là startup SLO phải tính cả phân phối (distribution / 분포) đường dẫn (path / 경로), không chỉ tiến trình (process / 프로세스) boot thời gian (time / 시간).

## 19. ảnh (image / 이미지) cấu hình (config / 설정) và thời gian chạy (runtime / 런타임) override tạo một precedence chuỗi (chain / 사슬)

Ảnh (image / 이미지) có thể khai báo `ENTRYPOINT`, `CMD`, `ENV`, người dùng (user / 사용자) và working directory, nhưng orchestrator/thời gian chạy (runtime / 런타임) có thể override một phần. Khi bộ chứa (container / 컨테이너) chạy khác cục bộ (local / 로컬), cần xác định **effective thời gian chạy (runtime / 런타임) cấu hình (config / 설정)**, không chỉ đọc Dockerfile.

Ví dụ ảnh (image / 이미지) có `ENTRYPOINT ["java", "-jar", "app.jar"]` nhưng triển khai (deployment / 배포) override command sai; hoặc ảnh (image / 이미지) `USER 10001` nhưng nền tảng (platform / 플랫폼) bảo mật (security / 보안) ngữ cảnh (context / 맥락) ép UID khác. Cả hai đều là legitimate composition nhưng nguồn (source / 소스) of hành vi (behavior / 동작) nằm ở nhiều tầng (layer / 계층).

Bản phát hành (release / 릴리스) siêu dữ liệu (metadata / 메타데이터) nên cho operator thấy ảnh (image / 이미지) digest cùng effective command/env/bảo mật (security / 보안) ngữ cảnh (context / 맥락) quan trọng. “ảnh (image / 이미지) đúng” chưa chứng minh tiến trình (process / 프로세스) được khởi động theo đặc tả hợp đồng (contract / 계약) mong muốn.

## 20. Init bộ chứa (container / 컨테이너) giải sequencing cục bộ, không biến phụ thuộc (dependency / 의존성) thành healthy

Init bộ chứa (container / 컨테이너) có thể chuẩn bị tệp (file / 파일), permissions hoặc chờ một prerequisite trước khi main bộ chứa (container / 컨테이너) start. Nhưng dùng vòng lặp (loop / 루프) `until curl database` để “đảm bảo DB sẵn sàng” có thể tạo coupling và startup storm khi phụ thuộc (dependency / 의존성) outage.

Phụ thuộc (dependency / 의존성) availability thường là thời gian chạy (runtime / 런타임) concern cần thử lại (retry / 재시도)/backoff/degradation, không phải điều kiện phải đúng một lần ở startup. Nếu 500 Pod cùng init-poll phụ thuộc (dependency / 의존성) mỗi giây khi phụ thuộc (dependency / 의존성) hồi, chính init lô-gic (logic / 논리) có thể tạo thundering herd.

Dùng init bộ chứa (container / 컨테이너) khi có finite setup công việc (work / 작업) với completion ngữ nghĩa (semantics / 의미론) rõ; không biến nó thành supervisor của mọi bên ngoài (external / 외부) dịch vụ (service / 서비스).

## 21. Startup tài nguyên (resource / 자원) spike khác steady-state usage

Một dịch vụ (service / 서비스) có thể cần CPU/bộ nhớ (memory / 메모리) cao lúc JIT, tải (load / 로드) mô hình (model / 모델), decompress dữ liệu (data / 데이터) hoặc warm bộ nhớ đệm (cache / 캐시) rồi giảm đáng kể khi steady trạng thái (state / 상태). Nếu tài nguyên (resource / 자원) chính sách (policy / 정책) chỉ dựa average môi trường vận hành (production / 운영 환경), bộ chứa (container / 컨테이너) có thể bị throttled/OOM đúng lúc startup và không bao giờ Ready.

Ngược lại cấp limit theo startup peak cho toàn thời gian có thể lãng phí sức chứa (capacity / 용량). nền tảng (platform / 플랫폼) cần hiểu tải công việc (workload / 워크로드) lớp (class / 클래스): có thể precompute sản phẩm tạo ra (artifact / 산출물), lazy-load, dùng startup probe, giữ headroom hoặc tách initialization khỏi serving đường dẫn (path / 경로).

Startup SLO là composition của ảnh (image / 이미지) phân phối (distribution / 분포) + thời gian chạy (runtime / 런타임) setup + ứng dụng (application / 애플리케이션) initialization + readiness, không chỉ “main tiến trình (process / 프로세스) đã spawn”.

## 22. Read-only gốc (root / 루트) filesystem cần tường minh (explicit / 명시적) writable paths

Chạy gốc (root / 루트) filesystem read-only giảm một lớp mutation/attack surface nhưng ứng dụng (application / 애플리케이션) vẫn có thể cần `/tmp`, bộ nhớ đệm (cache / 캐시) hoặc generated tệp (file / 파일). Nếu không mô hình (model / 모델) writable đường dẫn (path / 경로), tải công việc (workload / 워크로드) chỉ thất bại (fail / 실패) khi mã (code / 코드) chạm filesystem ở môi trường vận hành (production / 운영 환경).

Mẫu (pattern / 패턴) tốt là xác định đường dẫn (path / 경로) nào thật sự cần ghi, mount `tmpfs`/ephemeral volume hoặc durable volume theo ngữ nghĩa (semantics / 의미론), rồi giữ phần còn lại read-only. Điều này biến filesystem mutation thành đặc tả hợp đồng (contract / 계약) có thể rà soát (review / 검토).

Không nên bỏ read-only chỉ vì một thư viện (library / 라이브러리) viết temp tệp (file / 파일) mặc định; trước hết xác định dữ liệu (data / 데이터) đó cần thời gian tồn tại (lifetime / 수명)/kích thước (size / 크기)/bảo mật (security / 보안) nào và cung cấp đúng lưu trữ (storage / 저장소) ranh giới (boundary / 경계).

## 23. bộ chứa (container / 컨테이너) restart che trạng thái (state / 상태) cục bộ nhưng không sửa bên ngoài (external / 외부) side tác động (effect / 효과)

Restart tạo tiến trình (process / 프로세스)/gốc (root / 루트) writable trạng thái (state / 상태) mới, nên có thể chữa deadlock, bộ nhớ (memory / 메모리) leak tạm thời hoặc corrupted cục bộ (local / 로컬) bộ nhớ đệm (cache / 캐시). Nhưng giao dịch (transaction / 트랜잭션) đã gửi tới cơ sở dữ liệu (database / 데이터베이스)/payment, message đã publish hoặc khóa (lock / 잠금) bên ngoài (external / 외부) vẫn tồn tại.

Vì vậy “restart sạch” chỉ đúng cho trạng thái (state / 상태) nằm trong instance. Runbook phải biết thao tác (operation / 연산) nào có side tác động (effect / 효과) ngoài bộ chứa (container / 컨테이너) và idempotency/khôi phục (recovery / 복구) của chúng. Nếu thử lại (retry / 재시도) yêu cầu (request / 요청) sau restart mà không có nghiệp vụ (business / 비즈니스) idempotency, khôi phục (recovery / 복구) có thể tạo duplicate tác động (effect / 효과).

Bộ chứa (container / 컨테이너) replaceability là hạ tầng (infrastructure / 인프라) thuộc tính (property / 속성); nghiệp vụ (business / 비즈니스) statelessness là thuộc tính (property / 속성) khác.

## 24. ảnh (image / 이미지) pull chính sách (policy / 정책) và bộ nhớ đệm (cache / 캐시) tạo consistency sự đánh đổi (trade-off / 트레이드오프)

Nút (node / 노드) bộ nhớ đệm (cache / 캐시) giúp startup nhanh và giảm registry tải (load / 로드). Nhưng nếu triển khai (deployment / 배포) dùng mutable tag, hành vi (behavior / 동작) có thể phụ thuộc nút (node / 노드) đã bộ nhớ đệm (cache / 캐시) bytes nào và pull chính sách (policy / 정책) ra sao. Hai Pod cùng tag có khả năng chạy digest khác nếu workflow cho phép tag bị overwrite.

Pin digest loại bỏ ambiguity này: bộ nhớ đệm (cache / 캐시) chỉ là tối ưu hóa (optimization / 최적화) cho cùng content định danh (identity / 식별자). Với immutable digest, nút (node / 노드) bộ nhớ đệm (cache / 캐시) cũ không làm phiên bản (version / 버전) stale; thời gian chạy (runtime / 런타임) biết chính xác content cần có.

Đây là lý do sản phẩm tạo ra (artifact / 산출물) immutability làm nhiều operational bài toán (problem / 문제) đơn giản hơn, không chỉ supply-chain bảo mật (security / 보안).

## 25. cấp cao (senior / 시니어) walkthrough: chỉ Pod mới restart bị lỗi sau secret/cấu hình (config / 설정) thay đổi (change / 변경)

Giả sử fleet cũ vẫn khỏe, nhưng mọi Pod reschedule mới đều thất bại (fail / 실패) startup. ảnh (image / 이미지) digest giống nhau. Investigation cho thấy thời gian chạy (runtime / 런타임) inject môi trường (environment / 환경) variable/secret revision mới; tiến trình (process / 프로세스) cũ chưa restart nên vẫn giữ effective cấu hình (config / 설정) cũ.

Nhân quả (causal / 인과적) dimension là **instance birth thời gian (time / 시간)/cấu hình (config / 설정) revision**, không phải ảnh (image / 이미지) phiên bản (version / 버전). Nếu operator chỉ quay lui (rollback / 롤백) ảnh (image / 이미지), thất bại (failure / 실패) vẫn tiếp tục vì cấu hình (config / 설정) nguồn (source / 소스) không đổi.

Nền tảng (platform / 플랫폼) nên expose sản phẩm tạo ra (artifact / 산출물) digest + cấu hình (config / 설정)/secret revision + startup timestamp để cohort mới/cũ dễ phân biệt. môi trường vận hành (production / 운영 환경) định danh (identity / 식별자) của một instance là composition của sản phẩm tạo ra (artifact / 산출물) và thời gian chạy (runtime / 런타임) inputs, không chỉ ảnh bộ chứa (container image / 컨테이너 이미지).

> **Bàn giao:** Sau **25. cấp cao (senior / 시니어) walkthrough: chỉ Pod mới restart bị lỗi sau secret/cấu hình (config / 설정) thay đổi (change / 변경)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp.
