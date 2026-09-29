# Môi trường vận hành (production / 운영 환경) troubleshooting: từ symptom đến bằng chứng (evidence / 증거) xuyên tầng

> **Mạch đọc:** Đọc **môi trường vận hành (production / 운영 환경) troubleshooting: từ symptom đến bằng chứng (evidence / 증거) xuyên tầng** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. Troubleshooting là bài toán giảm không gian giả thuyết** sang **2. Chuỗi tầng (layer / 계층) chuẩn**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


## 1. Troubleshooting là bài toán giảm không gian giả thuyết

Môi trường vận hành (production / 운영 환경) hệ thống (system / 시스템) có nhiều tầng (layer / 계층) nên đoán tool-first rất tốn thời gian. Quy trình tốt bắt đầu bằng symptom cụ thể, thời gian (time / 시간) cửa sổ (window / 윈도우) và phạm vi (scope / 범위) rồi dùng bằng chứng (evidence / 증거) để loại trừ từng lớp.

Hỏi trước: ai bị ảnh hưởng; tất cả yêu cầu (request / 요청) hay một region/tenant; bắt đầu lúc nào; có thay đổi gần đó không; thất bại (failure / 실패) là lỗi (error / 오류), độ trễ (latency / 지연 시간), stale dữ liệu (data / 데이터) hay sức chứa (capacity / 용량).

## 2. Chuỗi tầng (layer / 계층) chuẩn

Một đường suy luận thực dụng:

```text
user symptom
→ edge/DNS/TLS
→ routing/load balancer
→ service endpoint
→ pod/process/runtime
→ node/kernel resources
→ downstream dependency
→ data/consistency
→ recent change/control plane
```

Không phải sự cố (incident / 인시던트) nào đi hết chuỗi. Mục tiêu là tìm tầng (layer / 계층) đầu tiên nơi expected trạng thái (state / 상태) khác actual trạng thái (state / 상태).

## 3. thay đổi (change / 변경) correlation không bằng causation

Triển khai (deployment / 배포) ngay trước sự cố (incident / 인시던트) là suspect mạnh nhưng chưa phải chứng minh. Có thể traffic spike, phụ thuộc (dependency / 의존성) outage hoặc certificate expiry trùng thời điểm.

Dùng phiên bản (version / 버전) dimension/canary comparison để tăng confidence. Nếu chỉ pod phiên bản (version / 버전) mới lỗi còn cũ khỏe cùng nút (node / 노드)/traffic, bằng chứng (evidence / 증거) mạnh hơn chỉ nhìn timestamp.

## 4. Golden signals trước, detail sau

Bắt đầu traffic/tỷ lệ (rate / 비율), lỗi (error / 오류), độ trễ (latency / 지연 시간) và saturation phù hợp dịch vụ (service / 서비스). Sau đó drill down dimension: phiên bản (version / 버전), zone, endpoint, phụ thuộc (dependency / 의존성). Không mở 20 dashboard cùng lúc.

Nếu lỗi (error / 오류) tăng nhưng độ trễ (latency / 지연 시간) không tăng, có thể kiểm tra hợp lệ (validation / 검증)/cấu hình (config / 설정) nhanh thất bại (fail / 실패). Nếu độ trễ (latency / 지연 시간) tăng trước lỗi (error / 오류), có thể saturation/phụ thuộc (dependency / 의존성) hết thời gian chờ (timeout / 타임아웃). mẫu (pattern / 패턴) thời gian giúp định hướng.

## 5. CPU sự cố (incident / 인시던트)

CPU cao có thể là traffic tăng, hot vòng lặp (loop / 루프), GC, encryption/compression hoặc thử lại (retry / 재시도) storm. CPU thấp vẫn có độ trễ (latency / 지연 시간) nếu throttled quota, I/O wait hoặc downstream.

Kiểm tra demand và thông lượng (throughput / 처리량) trước khi quy mô (scale / 규모). Nếu thông lượng (throughput / 처리량) không tăng cùng CPU, mã (code / 코드)/đường dẫn (path / 경로) có thể kém hiệu quả. Nếu quy mô (scale / 규모) app làm DB pressure tăng, cần tìm bottleneck thật.

## 6. bộ nhớ (memory / 메모리) sự cố (incident / 인시던트)

Bộ nhớ (memory / 메모리) tăng tuyến tính theo thời gian gợi leak/bộ nhớ đệm (cache / 캐시) không bound; jump sau deploy gợi changed footprint; OOM theo tải (load / 로드) peak gợi sức chứa (capacity / 용량)/limit.

Trong bộ chứa (container / 컨테이너), phân biệt thời gian chạy (runtime / 런타임) vùng nhớ động (heap / 힙) và cgroup bộ nhớ (memory / 메모리). OOM sự kiện (event / 이벤트)/exit bằng chứng (evidence / 증거) quan trọng hơn giả định “Java vùng nhớ động (heap / 힙) còn thấp nên không thể OOM”.

## 7. mạng (network / 네트워크)/hết thời gian chờ (timeout / 타임아웃) sự cố (incident / 인시던트)

Tách DNS → TCP → TLS → HTTP. `timeout` có thể ở connect hoặc read. Proxy và ứng dụng (application / 애플리케이션) có hết thời gian chờ (timeout / 타임아웃) riêng. dấu vết (trace / 추적) cho biết hop nào chiếm thời gian.

Thử lại (retry / 재시도) storm thường làm đồ thị yêu cầu (request / 요청) outbound tăng nhanh hơn inbound. Đây là dấu hiệu amplification.

## 8. Kubernetes Pending/CrashLoop/NotReady

`Pending`: scheduler/lưu trữ (storage / 저장소)/ràng buộc (constraint / 제약조건). `ImagePullBackOff`: registry/name/auth/mạng (network / 네트워크). `CrashLoopBackOff`: tiến trình (process / 프로세스) start rồi thoát lặp; xem exit/log/cấu hình (config / 설정). `NotReady`: tiến trình (process / 프로세스) chạy nhưng readiness đặc tả hợp đồng (contract / 계약) thất bại (fail / 실패). OOMKilled: bộ nhớ (memory / 메모리) ranh giới (boundary / 경계)/bằng chứng (evidence / 증거).

Tên status là entry điểm (point / 지점), không phải nguyên nhân gốc (root cause / 근본 원인).

## 9. cơ sở dữ liệu (database / 데이터베이스) phụ thuộc (dependency / 의존성)

App độ trễ (latency / 지연 시간) tăng có thể do liên kết (connection / 연결) pool exhausted, slow truy vấn (query / 쿼리), tranh chấp khóa (lock contention / 잠금 경합) hoặc DB tài nguyên (resource / 자원) saturation. liên kết (connection / 연결) pool wait thời gian (time / 시간) khác truy vấn (query / 쿼리) thực thi (execution / 실행) thời gian (time / 시간). Nếu pool wait cao nhưng truy vấn (query / 쿼리) độ trễ (latency / 지연 시간) bình thường, có thể pool kích thước (size / 크기)/tính đồng thời (concurrency / 동시성)/leak.

Quy mô (scale / 규모) app replicas làm tổng pool lớn hơn nên phải tính DB max connections toàn hệ thống.

## 10. hàng đợi (queue / 큐)/backlog

Hàng đợi (queue / 큐) độ sâu (depth / 깊이) tăng vì producer nhanh hơn bên tiêu thụ (consumer / 소비자) hoặc bên tiêu thụ (consumer / 소비자) chậm/thất bại (fail / 실패). độ sâu (depth / 깊이) một mình không đủ; message age cho biết người dùng (user / 사용자) delay. Nếu autoscale bên tiêu thụ (consumer / 소비자) nhưng downstream DB bottleneck, thông lượng (throughput / 처리량) có thể không tăng.

Poison message có thể làm bên tiêu thụ (consumer / 소비자) thử lại (retry / 재시도) cùng item; cần dead-letter/idempotency chiến lược (strategy / 전략) theo lĩnh vực (domain / 도메인).

## 11. cấu hình (config / 설정)/secret thất bại (failure / 실패)

Cấu hình (config / 설정) thay đổi (change / 변경) có thể không tạo triển khai (deployment / 배포) sự kiện (event / 이벤트) nếu chỉnh ngoài chuỗi xử lý (pipeline / 파이프라인). Vì vậy cấu hình (config / 설정) revision cần telemetry. Secret rotation thất bại (failure / 실패) thường biểu hiện partial: instance restart mới dùng credential mới, instance cũ vẫn dùng old; khi old revoked mới bắt đầu thất bại (fail / 실패).

Luôn xác định effective cấu hình (config / 설정) trong tiến trình (process / 프로세스), không chỉ đối tượng (object / 객체)/cấu hình (config / 설정) store.

## 12. Certificate expiry

Cert sự cố (incident / 인시던트) có timestamp rất rõ nhưng có thể chỉ ảnh hưởng một máy khách (client / 클라이언트) trust store hoặc hostname. Kiểm tra chuỗi (chain / 사슬), SAN, expiry và trust đường dẫn (path / 경로). Alert expiry phải đủ sớm để rotation có thời gian, nhưng kiểm thử (test / 테스트) rotation mới là điều khiển (control / 제어) mạnh hơn alert.

## 13. Disk sự cố (incident / 인시던트)

Disk usage 100% có thể làm DB/log tác nhân (agent / 에이전트)/app thất bại (fail / 실패) dây chuyền. Kiểm tra khối (block / 블록), inode, deleted-open files và volume lớp (class / 클래스). Cleanup emergency phải tránh xóa bằng chứng (evidence / 증거)/dữ liệu (data / 데이터) cần khôi phục (recovery / 복구).

## 14. điều khiển (control / 제어) plane vs mặt phẳng dữ liệu (data plane / 데이터 플레인)

Kubernetes API hoặc cloud API lỗi không luôn nghĩa ứng dụng (application / 애플리케이션) traffic down. Ngược lại mặt phẳng dữ liệu (data plane / 데이터 플레인) có thể lỗi dù điều khiển (control / 제어) plane báo tài nguyên (resource / 자원) Healthy.

Xác định tầng (layer / 계층) trước hành động (action / 동작). Repeated deploy trong control-plane outage có thể tích hàng đợi (queue / 큐) thay đổi và gây burst khi hồi phục.

## 15. khôi phục (recovery / 복구) hành động (action / 동작) phải có expected tác động (effect / 효과)

Trước restart/quy mô (scale / 규모)/quay lui (rollback / 롤백), nói rõ: giả thuyết gì, chỉ số (metric / 지표) nào sẽ đổi nếu đúng, bao lâu đánh giá, cách undo. Trong sự cố (incident / 인시던트) nhanh có thể viết ngắn nhưng vẫn giữ discipline.

Điều này ngăn nhiều người làm hành động (action / 동작) đối nghịch và giúp timeline có ý nghĩa.

## 16. Preserve bằng chứng (evidence / 증거) và reproducibility

Nếu phải restart để recover, capture log/sự kiện (event / 이벤트)/cốt lõi (core / 핵심)/luồng thực thi (thread / 스레드) dump khi feasible. Sau đó tái tạo thất bại (failure / 실패) trong staging/kiểm thử tải (load test / 부하 테스트) từ sản phẩm tạo ra (artifact / 산출물)/cấu hình (config / 설정) tương ứng.

Không phải sự cố (incident / 인시던트) nào tìm được single nguyên nhân gốc (root cause / 근본 원인). Có thể ghi nhân quả (causal / 인과적) factors và bất định (uncertainty / 불확실성) rõ ràng tốt hơn bịa một “nguyên nhân gốc (root cause / 근본 원인)” đơn giản.

## 17. cấp cao (senior / 시니어) ghi chú (note / 노트): troubleshooting giỏi là hiểu ranh giới (boundary / 경계)

Một operator cấp cao (senior / 시니어) không nhất thiết nhớ nhiều lệnh hơn; họ biết command nào trả lời câu hỏi nào, dữ liệu nằm ở tầng (layer / 계층) nào và khi nào lớp trừu tượng (abstraction / 추상화) bị rò.

Nền tảng (platform / 플랫폼) nên hỗ trợ drill-down từ dịch vụ (service / 서비스) danh mục (catalog / 카탈로그) → triển khai (deployment / 배포) → pod → nút (node / 노드) → dấu vết (trace / 추적)/log/chỉ số (metric / 지표) mà vẫn giữ quyền sở hữu (ownership / 소유권) và phiên bản (version / 버전) ngữ cảnh (context / 맥락). Đây là nơi nhà phát triển (developer / 개발자) experience và sự cố (incident / 인시던트) phản hồi (response / 응답) gặp nhau.

## 18. độ trễ (latency / 지연 시간) phải tách hàng đợi (queue / 큐) thời gian (time / 시간) và dịch vụ (service / 서비스) thời gian (time / 시간)

Một yêu cầu (request / 요청) chậm không có nghĩa mã (code / 코드) xử lý lô-gic nghiệp vụ (business logic / 비즈니스 로직) chậm. Tổng độ trễ (latency / 지연 시간) có thể gồm chờ liên kết (connection / 연결) pool, chờ luồng thực thi (thread / 스레드)/executor, chờ hàng đợi (queue / 큐), thời gian CPU thực thi, GC pause, mạng (network / 네트워크) và downstream.

Nếu ứng dụng (application / 애플리케이션) dấu vết (trace / 추적) chỉ đo từ lúc handler bắt đầu, thời gian yêu cầu (request / 요청) nằm chờ trước handler có thể biến mất khỏi dấu vết (trace / 추적). Vì vậy cần đặt instrumentation ở ranh giới (boundary / 경계) phù hợp và so client-observed độ trễ (latency / 지연 시간) với máy chủ (server / 서버) span. Khoảng chênh là clue cho proxy/mạng (network / 네트워크)/hàng đợi (queue / 큐)/scheduling.

Một hệ thống saturation thường biểu hiện dịch vụ (service / 서비스) thời gian (time / 시간) chưa tăng nhiều nhưng hàng đợi (queue / 큐) thời gian (time / 시간) tăng mạnh. quy mô (scale / 규모) đúng bottleneck hoặc shed tải (load / 로드) sẽ giảm hàng đợi (queue / 큐); tối ưu mã (code / 코드) handler trong trường hợp đó có thể không chạm nguyên nhân chính.

## 19. Coordinated omission có thể làm kiểm thử tải (load test / 부하 테스트) nói dối

Nếu tải (load / 로드) generator gửi yêu cầu (request / 요청) tiếp theo chỉ sau khi yêu cầu (request / 요청) trước hoàn thành, khi dịch vụ (service / 서비스) chậm nó tự động giảm arrival tỷ lệ (rate / 비율). Kết quả độ trễ (latency / 지연 시간) nhìn “đỡ xấu” đúng lúc môi trường vận hành (production / 운영 환경) thật sẽ tiếp tục nhận traffic và hàng đợi (queue / 큐) tăng.

Kiểm thử tải (load test / 부하 테스트) cần mô phỏng arrival mẫu (pattern / 패턴) thực tế đủ tốt và ghi nhận yêu cầu (request / 요청) đáng lẽ đã đến trong thời gian dịch vụ (service / 서비스) stall. Nếu không, thông lượng (throughput / 처리량)/độ trễ (latency / 지연 시간) benchmark có thể bỏ sót saturation cliff.

Điều cần nhớ không phải một công cụ (tool / 도구) benchmark cụ thể, mà là giả định (assumption / 가정) của tải công việc (workload / 워크로드) generator: closed-loop hay open-loop, tính đồng thời (concurrency / 동시성) cố định hay arrival tỷ lệ (rate / 비율) cố định, dữ liệu (data / 데이터)/bộ nhớ đệm (cache / 캐시) có đại diện môi trường vận hành (production / 운영 환경) không.

## 20. thất bại (failure / 실패) trường hợp (case / 사례): rollout tạo burst 502 dù Pod không crash

Giả sử mỗi rollout xuất hiện 502 trong 3–5 giây. Pod cũ nhận `SIGTERM` và đóng listener gần như ngay lập tức. Tuy nhiên endpoint/load-balancer propagation mất vài giây nên một phần yêu cầu (request / 요청) vẫn tuyến (route / 경로) tới Pod đang shutdown.

Bằng chứng (evidence / 증거): 502 tập trung đúng termination timestamp, tiến trình (process / 프로세스) exit mã (code / 코드) bình thường, không OOM, Pod mới Ready, ứng dụng (application / 애플리케이션) log Pod cũ có shutdown sự kiện (event / 이벤트) ngay trước liên kết (connection / 연결) reset. Đây không phải “Kubernetes không stable”; là termination/data-plane race.

Mitigation có thể gồm readiness/draining choreography và graceful shutdown để Pod ngừng nhận traffic trước khi listener biến mất, đồng thời giữ grace period đủ cho in-flight yêu cầu (request / 요청). Sau fix cần canary rollout và quan sát 5xx theo pod/phiên bản (version / 버전)/termination sự kiện (event / 이벤트).

## 21. thất bại (failure / 실패) trường hợp (case / 사례): Java vùng nhớ động (heap / 힙) chỉ 60% nhưng bộ chứa (container / 컨테이너) bị OOMKilled

Giả sử dashboard JVM cho vùng nhớ động (heap / 힙) 1,2 GiB trên max vùng nhớ động (heap / 힙) 2 GiB, trong khi Pod giới hạn bộ nhớ (memory limit / 메모리 제한) là 2 GiB và vẫn bị OOMKilled. vùng nhớ động (heap / 힙) chỉ số (metric / 지표) không bao gồm mọi bộ nhớ (memory / 메모리): metaspace, luồng thực thi (thread / 스레드) ngăn xếp (stack / 스택), direct buffer, bản địa (native / 네이티브) thư viện (library / 라이브러리), mmap/page bộ nhớ đệm (cache / 캐시) accounting tùy ngữ cảnh (context / 맥락) và thời gian chạy (runtime / 런타임) overhead đều có thể góp vào cgroup usage.

Bằng chứng (evidence / 증거) chuỗi (chain / 사슬) cần nối `lastState/exit`, cgroup/bộ chứa (container / 컨테이너) bộ nhớ (memory / 메모리) chỉ số (metric / 지표), nút (node / 노드) sự kiện (event / 이벤트) và JVM bản địa (native / 네이티브)/vùng nhớ động (heap / 힙) telemetry. Nếu cgroup usage chạm 2 GiB nhưng vùng nhớ động (heap / 힙) không chạm max, nguyên nhân là total tiến trình (process / 프로세스)/bộ chứa (container / 컨테이너) footprint vượt ranh giới (boundary / 경계), không phải vùng nhớ động (heap / 힙) OOM.

Fix có thể là giảm vùng nhớ động (heap / 힙) mục tiêu (target / 대상) để chừa bản địa (native / 네이티브) headroom, sửa direct-buffer/luồng thực thi (thread / 스레드) leak hoặc tăng limit sau sức chứa (capacity / 용량) rà soát (review / 검토). Chỉ đặt `-Xmx` bằng đúng bộ chứa (container / 컨테이너) limit là một anti-pattern vì giả định vùng nhớ động (heap / 힙) là toàn bộ bộ nhớ (memory / 메모리).

## 22. thất bại (failure / 실패) trường hợp (case / 사례): quy mô (scale / 규모) ứng dụng (application / 애플리케이션) làm outage cơ sở dữ liệu (database / 데이터베이스) nặng hơn

Traffic tăng làm độ trễ (latency / 지연 시간) app tăng. nhóm (team / 팀) quy mô (scale / 규모) từ 20 lên 100 replica. Mỗi replica có pool tối đa 50 liên kết (connection / 연결) nên theoretical liên kết (connection / 연결) demand tăng từ 1.000 lên 5.000, trong khi DB chỉ chịu khoảng 1.500 concurrent liên kết (connection / 연결) hữu ích. DB bắt đầu hàng đợi (queue / 큐)/khóa (lock / 잠금)/ngữ cảnh (context / 맥락) overhead, độ trễ (latency / 지연 시간) tăng thêm và thử lại (retry / 재시도) khuếch đại tải (load / 로드).

Bằng chứng (evidence / 증거) tốt là app replica count tăng trước DB liên kết (connection / 연결) saturation; thông lượng (throughput / 처리량) nghiệp vụ (business / 비즈니스) không tăng tương ứng; pool wait/truy vấn (query / 쿼리) độ trễ (latency / 지연 시간) và outbound thử lại (retry / 재시도) tăng. nguyên nhân gốc (root cause / 근본 원인) không phải “thiếu replica”, mà là bottleneck downstream và thiếu liên kết (connection / 연결)/tính đồng thời (concurrency / 동시성) ngân sách (budget / 예산) end-to-end.

Mitigation có thể giới hạn app tính đồng thời (concurrency / 동시성)/pool, shed tải (load / 로드), giảm thử lại (retry / 재시도) và quy mô (scale / 규모) DB nếu có headroom. Long-term fix là sức chứa (capacity / 용량) mô hình (model / 모델) nối autoscaling ứng dụng (application / 애플리케이션) với downstream ngân sách (budget / 예산).

## 23. thất bại (failure / 실패) trường hợp (case / 사례): cấu hình (config / 설정) store đúng nhưng tiến trình (process / 프로세스) vẫn dùng cấu hình (config / 설정) cũ

ConfigMap/secret manager cho thấy giá trị (value / 값) mới, nhưng một số instance vẫn hành vi (behavior / 동작) cũ. Có thể tiến trình (process / 프로세스) chỉ đọc cấu hình (config / 설정) lúc startup, volume sync có delay, reload hook thất bại (fail / 실패) hoặc liên kết (connection / 연결) đã mở bằng credential cũ.

Troubleshooting phải xác định **effective cấu hình (config / 설정)** của từng tiến trình (process / 프로세스)/phiên bản (version / 버전), không dừng ở nguồn chuẩn (source of truth / 정본). Nếu chỉ instance chưa restart lỗi, hypothesis mạnh là vòng đời (lifecycle / 생명주기)/reload. Nếu tất cả instance nhận tệp (file / 파일) mới nhưng hành vi (behavior / 동작) không đổi, xem ứng dụng (application / 애플리케이션) reload ngữ nghĩa (semantics / 의미론).

Nền tảng (platform / 플랫폼) nên expose cấu hình (config / 설정) revision trong telemetry/status để operator nối hành vi thời gian chạy (runtime behavior / 런타임 동작) với chính xác (exact / 정확한) cấu hình (config / 설정), giống sản phẩm tạo ra (artifact / 산출물) phiên bản (version / 버전).

## 24. bằng chứng (evidence / 증거) ma trận (matrix / 행렬) giúp điều tra song song mà không hỗn loạn

Trong sự cố (incident / 인시던트) lớn, thay vì năm người cùng mở log, có thể chia hypothesis theo tầng (layer / 계층) với expected bằng chứng (evidence / 증거). Ví dụ một người kiểm tra thay đổi (change / 변경)/phiên bản (version / 버전), một người phụ thuộc (dependency / 의존성)/DB, một người nút (node / 노드)/tài nguyên (resource / 자원), một người traffic edge. Mỗi nhánh phải trả về kết luận có thể bác bỏ: “không thấy phiên bản (version / 버전) correlation”, “DB pool wait tăng từ 10 ms lên 900 ms”, không phải “DB có vẻ ổn”.

Sự cố (incident / 인시던트) commander sau đó cập nhật hypothesis cây (tree / 트리). Cách này tận dụng parallelism mà vẫn tránh hành động (action / 동작) xung đột (conflict / 충돌).

## 25. Mitigation thành công không chứng minh nguyên nhân gốc (root cause / 근본 원인)

Restart làm dịch vụ (service / 서비스) khỏe lại có thể do xóa leaked trạng thái (state / 상태), reset liên kết (connection / 연결), di chuyển Pod sang nút (node / 노드) khác hoặc đơn giản trùng lúc phụ thuộc (dependency / 의존성) hồi phục. “Restart fixed it” là observation, chưa phải explanation.

Sau khôi phục (recovery / 복구), cần hỏi trạng thái (state / 상태) nào đã bị reset và bằng chứng (evidence / 증거) nào phân biệt hypothesis. Nếu không còn bằng chứng (evidence / 증거), postmortem nên ghi bất định (uncertainty / 불확실성) và thêm instrumentation để lần sau phân biệt, thay vì gán nguyên nhân gốc (root cause / 근본 원인) giả chắc chắn.

## 26. môi trường vận hành (production / 운영 환경) debugging nên kết thúc bằng cải thiện hệ thống

Mỗi sự cố (incident / 인시던트) có ba loại đầu ra (output / 출력) tiềm năng: fix defect trực tiếp, tăng khả năng phát hiện/chẩn đoán, và giảm blast radius/khôi phục (recovery / 복구) thời gian (time / 시간). Ví dụ một bộ nhớ (memory / 메모리) leak cần mã (code / 코드) fix; thiếu cgroup chỉ số (metric / 지표) cần khả năng quan sát (observability / 관측 가능성) fix; rollout ồ ạt cần delivery guardrail.

Nếu chỉ sửa defect mà không cải thiện tín hiệu (signal / 신호) hoặc an toàn (safety / 안전) khi thất bại (failure / 실패) lớp (class / 클래스) có thể tái diễn, học tập (learning / 학습) vòng lặp (loop / 루프) chưa đóng. Troubleshooting là đầu vào (input / 입력) cho kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): thất bại (failure / 실패) lặp lại ở nhiều nhóm (team / 팀) nên được biến thành default, guardrail hoặc self-service diagnostic năng lực (capability / 역량).

## 27. Counterfactual tốt hơn narrative sau sự cố

Sau sự cố (incident / 인시던트) rất dễ kể một câu chuyện mượt: “deploy X làm độ trễ (latency / 지연 시간) tăng nên X là nguyên nhân”. nhân quả (causal / 인과적) confidence mạnh hơn khi có counterfactual: cohort không nhận X có khỏe không; quay lui (rollback / 롤백) X có đảo tín hiệu (signal / 신호) trong cùng traffic/phụ thuộc (dependency / 의존성) không; một zone/phiên bản (version / 버전) tương đương có hành vi (behavior / 동작) khác không.

Canary, phiên bản (version / 버전) dimension, tenant cohort và region split tạo natural experiment. Chúng không chứng minh tuyệt đối nhưng giúp phân biệt correlation với cơ chế (mechanism / 메커니즘).

Khi không có counterfactual, postmortem nên nói rõ bằng chứng (evidence / 증거) mức (level / 수준). Một hypothesis có timeline phù hợp nhưng chưa được reproduce khác với nguyên nhân gốc (root cause / 근본 원인) đã được isolation/reproduction xác nhận.

## 28. Nhiều vòng phản hồi (feedback loop / 피드백 루프) có thể tạo oscillation dù từng vòng lặp (loop / 루프) “đúng”

Môi trường vận hành (production / 운영 환경) hiện đại có HPA, cluster autoscaler, thử lại (retry / 재시도), circuit breaker, bộ cân bằng tải (load balancer / 로드 밸런서) health check, hàng đợi (queue / 큐) autoscaler và GitOps/controller cùng phản ứng với tín hiệu (signal / 신호). Nếu phản hồi (response / 응답) thời gian (time / 시간) và gain không được phối hợp, chúng có thể đẩy hệ thống qua lại.

Ví dụ độ trễ (latency / 지연 시간) tăng → HPA quy mô (scale / 규모) app → DB liên kết (connection / 연결) tăng → DB chậm hơn → thử lại (retry / 재시도) tăng → độ trễ (latency / 지연 시간) tăng thêm. Sau đó circuit breaker mở → tải (load / 로드) giảm → HPA quy mô (scale / 규모) down; breaker đóng → traffic dồn lại và chu kỳ lặp.

Khi chỉ số (metric / 지표) dao động tuần hoàn, đừng chỉ gỡ lỗi (debug / 디버그) thành phần (component / 컴포넌트) riêng. Hãy vẽ vòng lặp (loop / 루프): **tín hiệu (signal / 신호) nào kích hành động (action / 동작) nào, delay bao lâu, hành động (action / 동작) thay tài nguyên (resource / 자원)/tải (load / 로드) gì, vòng lặp (loop / 루프) khác quan sát tín hiệu (signal / 신호) gì**. Oscillation thường là thuộc tính (property / 속성) của tương tác (interaction / 상호작용), không phải một controller đơn độc.

## 29. máy khách (client / 클라이언트) hết thời gian chờ (timeout / 타임아웃) không có nghĩa máy chủ (server / 서버) đã dừng công việc (work / 작업)

Một yêu cầu (request / 요청) hết thời gian chờ (timeout / 타임아웃) ở máy khách (client / 클라이언트)/proxy có thể vẫn tiếp tục chạy trong máy chủ (server / 서버) hoặc downstream nếu cancellation không propagate. máy khách (client / 클라이언트) thử lại (retry / 재시도) sau hết thời gian chờ (timeout / 타임아웃) có thể tạo hai thao tác (operation / 연산) đồng thời. Với ghi (write / 쓰기) không idempotent, đây là đường tới duplicate side tác động (effect / 효과).

Bằng chứng (evidence / 증거) cần so máy khách (client / 클라이언트) hết thời gian chờ (timeout / 타임아웃) timestamp với máy chủ (server / 서버) dấu vết (trace / 추적) và downstream thao tác (operation / 연산). Nếu máy chủ (server / 서버) hoàn thành sau khi máy khách (client / 클라이언트) đã bỏ, độ trễ (latency / 지연 시간)/lỗi (error / 오류) dashboard phía máy khách (client / 클라이언트) và máy chủ (server / 서버) có thể kể hai câu chuyện khác nhau.

Deadline propagation, cancellation và idempotency key là độ tin cậy (reliability / 신뢰성) cơ chế (mechanism / 메커니즘). Troubleshooting phải hỏi “công việc (work / 작업) đã bị hủy thật chưa?” thay vì đồng nhất hết thời gian chờ (timeout / 타임아웃) với thất bại (failure / 실패) kết thúc.

## 30. Partial thất bại (failure / 실패) nên được cắt theo cohort trước khi nhìn toàn cục (global / 전역) average

Một sự cố (incident / 인시던트) có thể chỉ ảnh hưởng nút (node / 노드) ảnh (image / 이미지) mới, AZ cụ thể, tenant tier, certificate chuỗi (chain / 사슬) cũ, IPv6 đường dẫn (path / 경로), trình duyệt (browser / 브라우저) phiên bản (version / 버전) hoặc shard dữ liệu. toàn cục (global / 전역) lỗi (error / 오류) 2% có thể là 100% thất bại (failure / 실패) của một cohort nhỏ.

Dimension hữu ích nhất thường là dimension gần thất bại (failure / 실패) ranh giới (boundary / 경계): phiên bản (version / 버전), zone, nút (node / 노드) pool, mục tiêu (target / 대상) phụ thuộc (dependency / 의존성), cấu hình (config / 설정) revision, định danh (identity / 식별자) principal, shard/partition. High-cardinality không có nghĩa phải chỉ mục (index / 인덱스) mọi thứ vô hạn; cần chọn dimension có khả năng phân biệt hypothesis.

Câu hỏi cấp cao (senior / 시니어) là: **những yêu cầu (request / 요청) thất bại (fail / 실패) có điểm chung nào mà yêu cầu (request / 요청) thành công không có?** Đây thường là đường ngắn nhất tới isolation ranh giới (boundary / 경계).

## 31. khôi phục (recovery / 복구) storm là một thất bại (failure / 실패) phase riêng

Khi phụ thuộc (dependency / 의존성) hoặc điều khiển (control / 제어) plane hồi phục, hệ thống chưa chắc ổn ngay. Backlog, thử lại (retry / 재시도) hàng đợi (queue / 큐), reconnect, trượt bộ nhớ đệm (cache miss / 캐시 미스), ảnh (image / 이미지) pull, leader election và pod restart có thể đồng loạt tạo tải (load / 로드) lớn hơn steady trạng thái (state / 상태) trước outage.

Nếu operator thấy phụ thuộc (dependency / 의존성) “đã xanh” nhưng độ trễ (latency / 지연 시간) tiếp tục xấu, hãy kiểm tra khôi phục (recovery / 복구) tải công việc (workload / 워크로드): hàng đợi (queue / 큐) age đang drain ra sao, reconnect tỷ lệ (rate / 비율), bộ nhớ đệm (cache / 캐시) hit, DB liên kết (connection / 연결) churn, controller backlog và nút (node / 노드) provisioning.

Khôi phục (recovery / 복구) cần throttling/ramp-up giống startup. Mở toàn bộ traffic ngay khi health check xanh có thể tạo second outage.

## 32. Brownout cần được phân biệt với silent data-quality thất bại (failure / 실패)

Graceful degradation có chủ đích có thể trả stale bộ nhớ đệm (cache / 캐시), bỏ recommendation hoặc defer non-critical công việc (work / 작업). Nhưng nếu telemetry chỉ nhìn HTTP 200, brownout và nghiệp vụ (business / 비즈니스) tính đúng đắn (correctness / 정확성) thất bại (failure / 실패) có thể bị che.

Degradation chế độ (mode / 모드) phải có tường minh (explicit / 명시적) tín hiệu (signal / 신호): tính năng (feature / 기능) disabled, dữ liệu (data / 데이터) freshness, fallback ratio, stale age hoặc chất lượng (quality / 품질) tier. SLO có thể cho cốt lõi (core / 핵심) availability xanh trong khi sản phẩm (product / 제품) chất lượng (quality / 품질) giảm; dashboard phải cho operator biết đây là intentional degraded chế độ (mode / 모드) hay unknown thất bại (failure / 실패).

Troubleshooting không nên “fix” brownout ngay nếu nó đang bảo vệ cốt lõi (core / 핵심) luồng (flow / 흐름). Trước hết xác nhận trigger, protected bất biến (invariant / 불변식) và điều kiện thoát chế độ (mode / 모드).

## 33. Clock và sự kiện (event / 이벤트) thứ tự (ordering / 순서) có thể làm timeline đánh lừa

Log từ nhiều host/dịch vụ (service / 서비스) có thể lệch clock, batch trước khi ship hoặc ghi timestamp ở thời điểm khác nhau. dấu vết (trace / 추적) span cũng có sampling/clock giả định (assumption / 가정). Vì vậy thứ tự hiển thị không luôn bằng nhân quả (causal / 인과적) thứ tự (order / 순서) tuyệt đối.

Khi vài giây quyết định hypothesis, ưu tiên correlation ID/dấu vết (trace / 추적) parent, chuỗi (sequence / 시퀀스)/phiên bản (version / 버전), triển khai (deployment / 배포) sự kiện (event / 이벤트) từ nguồn chuẩn (source of truth / 정본) và monotonic duration trong cùng tiến trình (process / 프로세스) hơn việc so raw wall-clock timestamp giữa host.

NTP/clock health vẫn quan trọng, nhưng sự cố (incident / 인시던트) phân tích (analysis / 분석) nên biết bất định (uncertainty / 불확실성) của timeline thay vì suy luận causality từ chênh 200 ms không đáng tin.

## 34. Negative bằng chứng (evidence / 증거) có giá trị nếu biết detector đáng tin tới đâu

“Không có log lỗi (error / 오류)” chỉ loại trừ hypothesis nếu đường đi mã (code path / 코드 경로) chắc chắn phải log và log chuỗi xử lý (pipeline / 파이프라인) không mất dữ liệu. “Không thấy CPU cao” chỉ hữu ích nếu chỉ số (metric / 지표) resolution bắt được spike và đúng cgroup/nút (node / 노드). Absence of bằng chứng (evidence / 증거) không tự động là bằng chứng (evidence / 증거) of absence.

Mỗi tín hiệu (signal / 신호) có detection ranh giới (boundary / 경계): sampling, retention, scrape interval, dropped log, missing label hoặc instrumentation gap. cấp cao (senior / 시니어) debugging luôn hỏi **nếu hypothesis đúng, detector này có chắc nhìn thấy không?**

Khi detector yếu, kết luận đúng là “chưa quan sát được”, không phải “đã loại trừ”. Điều này giúp hypothesis cây (tree / 트리) trung thực hơn và thường chỉ ra khả năng quan sát (observability / 관측 가능성) debt cần sửa sau sự cố (incident / 인시던트).

## 35. nhân quả (causal / 인과적) đồ thị (graph / 그래프) tốt hơn một timeline phẳng khi nhiều yếu tố tương tác

Timeline chỉ nói sự kiện nào xảy ra trước sau. nhân quả (causal / 인과적) đồ thị (graph / 그래프) cố gắng biểu diễn phụ thuộc (dependency / 의존성): traffic tăng làm hàng đợi (queue / 큐) tăng; hàng đợi (queue / 큐) tăng làm độ trễ (latency / 지연 시간) tăng; hết thời gian chờ (timeout / 타임아웃) làm thử lại (retry / 재시도) tăng; thử lại (retry / 재시도) lại làm traffic downstream tăng. Một nút (node / 노드) có thể vừa là hậu quả của cause trước vừa trở thành cause của thất bại (failure / 실패) tiếp theo.

Khi sự cố (incident / 인시던트) phức tạp, hãy vẽ arrow “A có thể làm B bằng cơ chế (mechanism / 메커니즘) nào?” thay vì chỉ liệt kê timestamp. Nếu không mô tả được cơ chế (mechanism / 메커니즘) nối hai sự kiện (event / 이벤트), correlation cần được giữ ở mức hypothesis.

Nhân quả (causal / 인과적) đồ thị (graph / 그래프) cũng giúp phân biệt trigger, amplifier và latent điều kiện (condition / 조건). Bad deploy có thể là trigger, thử lại (retry / 재시도) chính sách (policy / 정책) là amplifier, còn thiếu admission điều khiển (control / 제어) là điều kiện khiến blast radius lớn.

## 36. Intervention tạo bằng chứng (evidence / 증거) mạnh nhưng đồng thời làm hệ thống (system / 시스템) thay đổi

Quay lui (rollback / 롤백), quy mô (scale / 규모), disable tính năng (feature / 기능) hoặc restart vừa là mitigation vừa là experiment. Nếu quay lui (rollback / 롤백) làm lỗi (error / 오류) giảm, confidence vào thay đổi (change / 변경) tăng — nhưng traffic, bộ nhớ đệm (cache / 캐시), phụ thuộc (dependency / 의존성) hoặc autoscaler cũng có thể đổi cùng lúc.

Một intervention hữu ích nên thay ít biến nhất có thể trong giới hạn sự cố (incident / 인시던트) an toàn (safety / 안전) và ghi rõ expected tác động (effect / 효과). Khi có thể, dùng cohort nhỏ/canary thay vì toàn fleet để giữ comparison group. Khi người dùng (user / 사용자) impact buộc phải hành động mạnh, ưu tiên khôi phục (recovery / 복구) nhưng đừng overclaim nhân quả (causal / 인과적) certainty sau đó.

Môi trường vận hành (production / 운영 환경) không phải laboratory sạch. Discipline nằm ở việc biết intervention nào đã phá counterfactual nào.

## 37. sự cố (incident / 인시던트) state-change discipline ngăn operator tự tạo race

Trong sự cố (incident / 인시던트) lớn, nhiều người cùng quy mô (scale / 규모), patch cấu hình (config / 설정), restart và quay lui (rollback / 롤백) có thể làm actual trạng thái (state / 상태) thay đổi nhanh hơn khả năng quan sát. bằng chứng (evidence / 증거) thu ở phút 10 có thể không còn mô tả trạng thái (state / 상태) sau hành động (action / 동작) phút 11.

Nên có một đơn vị sở hữu (owner / 오너) cho mutation đường dẫn (path / 경로) hoặc ít nhất serialized log: hành động (action / 동작) nào, mục tiêu (target / 대상)/revision nào, ai thực hiện, expected tác động (effect / 효과), timestamp và quay lui (rollback / 롤백) điều kiện (condition / 조건). Read-only investigation có thể parallel; trạng thái (state / 상태) mutation cần coordination mạnh hơn.

Điều này đặc biệt quan trọng với controller/GitOps: manual patch có thể bị reconcile ngược, tạo cảm giác hệ thống (system / 시스템) “tự thay đổi” trong khi hai actor đang tranh quyền sở hữu (ownership / 소유권).

## 38. Detector coverage nên được xem như bản đồ, không phải danh sách dashboard

Một organization thường biết rõ các thất bại (failure / 실패) đã instrument nhưng ít biết vùng mù. Có thể lập coverage map theo thất bại (failure / 실패) lớp (class / 클래스): edge reachability, nghiệp vụ (business / 비즈니스) tính đúng đắn (correctness / 정확성), phụ thuộc (dependency / 의존성) độ trễ (latency / 지연 시간), tài nguyên (resource / 자원) pressure, dữ liệu (data / 데이터) freshness, hàng đợi (queue / 큐) age, control-plane convergence và bảo mật (security / 보안) authorization.

Với mỗi lớp (class / 클래스), hỏi sensor nằm ở đâu, sampling/freshness ra sao, thất bại (failure / 실패) nào sensor không nhìn thấy và tín hiệu (signal / 신호) mất thì có được phát hiện không. Coverage map không cần hoàn hảo; mục tiêu là biết “unknown unknown” nào đang hoàn toàn phụ thuộc complaint của người dùng (user / 사용자).

Sự cố (incident / 인시던트) mới phát hiện vùng mù nên tạo khả năng quan sát (observability / 관측 가능성) hành động (action / 동작) cụ thể, không chỉ thêm dashboard chung chung.

## 39. Fault injection chỉ tạo bằng chứng (evidence / 증거) nếu experiment có điều khiển (control / 제어) và xác minh (verification / 확인)

Inject 500 ms mạng (network / 네트워크) delay rồi thấy độ trễ (latency / 지연 시간) tăng không dạy nhiều nếu không xác nhận delay thật sự đi vào đường dẫn (path / 경로) nào, cohort nào bị ảnh hưởng và điều khiển (control / 제어) cohort nào không bị inject.

Một experiment tốt định nghĩa hypothesis, fault ranh giới (boundary / 경계), steady-state chỉ số (metric / 지표), stop điều kiện (condition / 조건), điều khiển (control / 제어)/comparison group và bằng chứng (evidence / 증거) chứng minh injection đã hoạt động. Nếu công cụ (tool / 도구) báo “fault injected” nhưng packet đường dẫn (path / 경로) thực không qua mục tiêu (target / 대상) đó, kết luận resilience là vô nghĩa.

Fault injection có giá trị nhất khi kiểm tra một bất biến (invariant / 불변식) cụ thể, ví dụ “mất một replica không làm checkout burn ngân sách (budget / 예산) > X”, không phải khi chỉ cố tạo chaos cho giống môi trường vận hành (production / 운영 환경).

## 40. cấp cao (senior / 시니어) walkthrough: restart giúp ngay nhưng nguyên nhân gốc (root cause / 근본 원인) vẫn chưa rõ

Giả sử dịch vụ (service / 서비스) độ trễ (latency / 지연 시간) tăng dần, restart toàn replica làm độ trễ (latency / 지연 시간) trở lại bình thường. Có ít nhất vài hypothesis: bộ nhớ (memory / 메모리)/bộ nhớ đệm (cache / 캐시) leak, liên kết (connection / 연결) pool trạng thái (state / 상태) xấu, luồng thực thi (thread / 스레드) starvation, DNS/liên kết (connection / 연결) refresh hoặc tải công việc (workload / 워크로드) được reschedule khỏi nút (node / 노드) lỗi.

Restart đã reset nhiều trạng thái (state / 상태) cùng lúc nên intervention có độ phân giải thấp. Sau sự cố (incident / 인시던트), hãy tìm cohort/tiến trình (process / 프로세스) bằng chứng (evidence / 증거) còn giữ được, thử targeted restart hoặc reproduction trong môi trường (environment / 환경) kiểm soát, và bổ sung chỉ số (metric / 지표) cho trạng thái (state / 상태) nghi ngờ.

Kết luận trưởng thành là: **restart chứng minh thất bại (failure / 실패) phụ thuộc một trạng thái (state / 상태) đã bị reset, nhưng chưa xác định trạng thái (state / 상태) nào**. Giữ bất định (uncertainty / 불확실성) chính xác tốt hơn gán nhãn “bộ nhớ (memory / 메모리) leak” chỉ vì restart có hiệu quả.

> **Bàn giao:** Sau **40. cấp cao (senior / 시니어) walkthrough: restart giúp ngay nhưng nguyên nhân gốc (root cause / 근본 원인) vẫn chưa rõ**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp.
