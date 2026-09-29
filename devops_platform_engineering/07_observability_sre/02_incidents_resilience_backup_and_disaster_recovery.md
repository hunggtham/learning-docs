# Sự cố (incident / 인시던트), resilience, backup và disaster khôi phục (recovery / 복구)

> **Mạch đọc:** Đọc **sự cố (incident / 인시던트), resilience, backup và disaster khôi phục (recovery / 복구)** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. sự cố (incident / 인시던트) phản hồi (response / 응답) tối ưu khôi phục (recovery / 복구) trước nguyên nhân gốc (root cause / 근본 원인)** sang **2. Severity dựa trên impact**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


## 1. sự cố (incident / 인시던트) phản hồi (response / 응답) tối ưu khôi phục (recovery / 복구) trước nguyên nhân gốc (root cause / 근본 원인)

Trong sự cố có người dùng (user / 사용자) impact, hai mục tiêu khác nhau: phục hồi dịch vụ (service / 서비스) và hiểu nguyên nhân gốc. Chúng có thể trùng nhưng không luôn trùng. Restart, failover hoặc disable tính năng (feature / 기능) có thể phục hồi nhanh nhưng không giải thích nguyên nhân gốc (root cause / 근본 원인).

Sự cố (incident / 인시던트) tiến trình (process / 프로세스) tốt tách vai trò và thời gian. Stabilize trước; preserve bằng chứng (evidence / 증거) khi có thể; rồi investigation sâu sau khi impact giảm.

## 2. Severity dựa trên impact

Severity nên phản ánh phạm vi người dùng (user / 사용자)/nghiệp vụ (business / 비즈니스), mức mất dữ liệu, bảo mật (security / 보안) impact và thời gian, không phản ánh “bug có vẻ khó”. cơ sở dữ liệu (database / 데이터베이스) CPU 100% mà người dùng (user / 사용자) không bị ảnh hưởng có thể chưa là sự cố (incident / 인시던트) lớn; payment double-charge dù traffic nhỏ có thể rất nghiêm trọng.

Quy tắc (rule / 규칙) rõ giúp escalation nhất quán.

## 3. sự cố (incident / 인시던트) command giảm coordination chaos

Khi nhiều người cùng sửa môi trường vận hành (production / 운영 환경), nguy cơ hành động (action / 동작) xung đột (conflict / 충돌) tăng. sự cố (incident / 인시던트) commander điều phối priority/quyết định (decision / 결정); người vận hành thực hiện; communication role cập nhật stakeholder. nhóm (team / 팀) nhỏ có thể gộp role nhưng vẫn cần một đơn vị sở hữu (owner / 오너) quyết định rõ.

Timeline phải ghi sự kiện (event / 이벤트) và hành động (action / 동작): alert lúc nào, deploy nào trước đó, hành động (action / 동작) gì đã làm, chỉ số (metric / 지표) phản ứng ra sao. Timeline sau này là dữ liệu cho postmortem.

## 4. Mitigation có thể tăng blast radius

Trong sự cố (incident / 인시던트), “quy mô (scale / 규모) mọi thứ lên” hoặc “restart toàn bộ” dễ làm mất bằng chứng (evidence / 증거) và gây thundering herd. hành động (action / 동작) nên có hypothesis, expected kết quả (outcome / 결과) và quay lui (rollback / 롤백).

Ví dụ liên kết (connection / 연결) pool exhaustion do DB chậm: tăng replicas app có thể tăng tổng liên kết (connection / 연결) và làm DB tệ hơn. Mitigation hợp lý có thể là giảm tính đồng thời (concurrency / 동시성), shed tải (load / 로드) hoặc disable expensive đường dẫn (path / 경로).

## 5. Runbook phải là quyết định (decision / 결정) hỗ trợ (support / 지원)

Runbook tốt không chỉ ghi lệnh. Nó nêu symptom, điều kiện áp dụng, bằng chứng (evidence / 증거) cần kiểm tra, hành động (action / 동작), expected kết quả (result / 결과), nguy cơ và cách undo. Lệnh copy-paste không có ngữ cảnh (context / 맥락) có thể nguy hiểm hơn không có runbook.

Runbook nên được kiểm thử (test / 테스트) trong game day/sự cố (incident / 인시던트) thật và cập nhật khi giả định (assumption / 가정) đổi.

## 6. Postmortem tìm cơ chế, không tìm người để quy lỗi

“Engineer chạy nhầm command” là mô tả trigger, chưa phải nguyên nhân gốc (root cause / 근본 원인) đủ sâu. Hỏi vì sao một command có blast radius lớn, vì sao rà soát (review / 검토)/guardrail thiếu, vì sao môi trường vận hành (production / 운영 환경) credential cho phép, vì sao tín hiệu (signal / 신호) không cảnh báo sớm.

Blameless không nghĩa không có accountability. quyền sở hữu (ownership / 소유권) vẫn rõ, nhưng phân tích (analysis / 분석) tập trung hệ thống để thất bại (failure / 실패) tương tự khó tái diễn.

## 7. hành động (action / 동작) item phải thay đổi hệ thống

Hành động (action / 동작) “cẩn thận hơn” gần như không tạo điều khiển (control / 제어) mới. hành động (action / 동작) tốt có đơn vị sở hữu (owner / 오너) và deadline, ví dụ thêm chính sách (policy / 정책) ngăn wildcard permission, thêm canary check, tự động expire certificate hoặc kiểm thử (test / 테스트) restore hàng quý.

Không nên tạo hàng chục hành động (action / 동작) low-value sau mỗi sự cố (incident / 인시던트). Ưu tiên thay đổi giảm xác suất hoặc blast radius của thất bại (failure / 실패) lớp (class / 클래스) quan trọng.

## 8. Resilience khác redundancy

Thêm replica tăng redundancy nhưng resilience còn gồm detection, failover, degradation, khôi phục (recovery / 복구) và học tập (learning / 학습). Ba replica cùng zone không chịu được zone thất bại (failure / 실패). Multi-zone nhưng cùng cơ sở dữ liệu (database / 데이터베이스) single điểm (point / 지점) vẫn chưa đủ.

Hãy vẽ miền lỗi (failure domain / 장애 도메인): tiến trình (process / 프로세스), pod, nút (node / 노드), rack/zone, region, điều khiển (control / 제어) plane, định danh (identity / 식별자) provider, DNS, registry, CI và human thao tác (operation / 연산). Availability end-to-end bị chi phối bởi phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프).

## 9. Backup không phải khôi phục (recovery / 복구)

Có tệp (file / 파일) backup chưa chứng minh khôi phục được. Backup có thể corrupt, thiếu key giải mã, không chứa giao dịch (transaction / 트랜잭션) log cần thiết hoặc restore mất quá lâu so với mục tiêu.

Khôi phục (recovery / 복구) kiểm thử (test / 테스트) phải thực sự tạo môi trường (environment / 환경), restore dữ liệu (data / 데이터), chạy consistency/nghiệp vụ (business / 비즈니스) kiểm tra hợp lệ (validation / 검증) và đo thời gian.

## 10. RPO và RTO

Khôi phục (recovery / 복구) điểm (point / 지점) mục tiêu (objective / 목표) (RPO) trả lời chấp nhận mất bao nhiêu dữ liệu theo thời gian. khôi phục (recovery / 복구) thời gian (time / 시간) mục tiêu (objective / 목표) (RTO) trả lời chấp nhận mất năng lực (capability / 역량) bao lâu.

Hai mục tiêu dẫn tới kiến trúc (architecture / 아키텍처) khác nhau. RPO gần zero có thể cần synchronous/continuous replication và giao dịch (transaction / 트랜잭션) ngữ nghĩa (semantics / 의미론) mạnh. RTO vài phút cần automation/failover khác RTO một ngày.

Không nên chọn RPO/RTO theo mong muốn kỹ thuật; nghiệp vụ (business / 비즈니스) impact phải quyết định.

## 11. Replication không thay backup

Replication sao chép cả thay đổi tốt và xấu. Nếu người dùng (user / 사용자) delete dữ liệu (data / 데이터) hoặc ransomware/corruption propagate, replica có thể hỏng giống primary. Backup point-in-time độc lập tạo khôi phục (recovery / 복구) option khác.

Ngược lại, backup mỗi ngày không cung cấp failover nhanh. Resilience thường cần cả replication và backup với mục tiêu khác nhau.

## 12. Disaster khôi phục (recovery / 복구) và điều khiển (control / 제어) plane phụ thuộc (dependency / 의존성)

DR plan phải xét cả phụ thuộc (dependency / 의존성) ngoài ứng dụng (application / 애플리케이션): DNS, IAM, KMS/key, sản phẩm tạo ra (artifact / 산출물) registry, secret store, mạng (network / 네트워크), IaC trạng thái (state / 상태) và CI/CD. Nếu restore cơ sở dữ liệu (database / 데이터베이스) ở region B nhưng encryption key/định danh (identity / 식별자) chính sách (policy / 정책) chỉ tồn tại region A, dữ liệu (data / 데이터) vẫn vô dụng.

Một lỗi phổ biến là DR document giả định công cụ (tool / 도구) dùng để restore vẫn khả dụng trong thảm họa. Cần kiểm tra bootstrap đường dẫn (path / 경로).

## 13. Game day và chaos experiment

Chaos kỹ thuật (engineering / 엔지니어링) có giá trị khi kiểm tra hypothesis cụ thể về resilience, không phải phá môi trường vận hành (production / 운영 환경) ngẫu nhiên. Ví dụ: “mất một nút (node / 노드) không làm SLO checkout vi phạm quá X phút”. Experiment cần steady-state chỉ số (metric / 지표), blast radius giới hạn, stop điều kiện (condition / 조건) và quay lui (rollback / 롤백).

Bắt đầu staging/lab không có nghĩa đủ; môi trường vận hành (production / 운영 환경) có traffic/dữ liệu (data / 데이터)/phụ thuộc (dependency / 의존성) khác. Nhưng môi trường vận hành (production / 운영 환경) experiment phải có maturity và guardrail tương ứng.

## 14. cấp cao (senior / 시니어) ghi chú (note / 노트): phục hồi là một sản phẩm (product / 제품) năng lực (capability / 역량)

Backup, failover và sự cố (incident / 인시던트) tiến trình (process / 프로세스) không nên là tài liệu tồn tại riêng. Chúng là năng lực (capability / 역량) cần phiên bản (version / 버전), kiểm thử (test / 테스트), quyền sở hữu (ownership / 소유권) và telemetry. Nếu khôi phục (recovery / 복구) chỉ được thử khi disaster thật xảy ra, đó không phải plan mà là hy vọng.

Một nền tảng (platform / 플랫폼) trưởng thành biến khôi phục (recovery / 복구) đường dẫn (path / 경로) thành workflow lặp lại: snapshot/backup tự động, restore drill, môi trường (environment / 환경) bootstrap bằng mã (code / 코드), truy cập (access / 접근) khẩn cấp được kiểm tra (audit / 감사) và communication template sẵn.

## 15. MTTR nên được phân rã để biết đang tối ưu phần nào

Một con số MTTR tổng hợp có thể che nhiều vấn đề khác nhau. Có thể tách timeline thành detection, triage/understanding, mitigation, repair và xác minh (verification / 확인). Hai sự cố (incident / 인시던트) cùng mất 60 phút nhưng một cái mất 50 phút mới phát hiện, cái kia phát hiện ngay nhưng quay lui (rollback / 롤백) không chạy được, cần cải tiến hoàn toàn khác nhau.

Một decomposition thực dụng:

```text
failure begins
→ detected
→ acknowledged / triaged
→ mitigation starts
→ user impact recovered
→ permanent repair
→ learning/action closed
```

Không nhất thiết mọi tổ chức phải dùng cùng tên chỉ số (metric / 지표). Điều quan trọng là timestamp có ngữ nghĩa (semantics / 의미론) rõ để tránh “MTTR giảm” chỉ vì đổi cách bắt đầu/kết thúc đồng hồ.

## 16. Backup consistency có nhiều mức

Snapshot lưu trữ (storage / 저장소) không tự động bảo đảm application-consistent trạng thái (state / 상태). Với cơ sở dữ liệu (database / 데이터베이스) đang ghi, snapshot crash-consistent có thể tương đương mất điện đột ngột: engine phải dựa WAL/journal/khôi phục (recovery / 복구) khi restore. Một số hệ thống cần quiesce, checkpoint hoặc coordination giữa nhiều volume/thành phần (component / 컴포넌트) để tạo backup nhất quán.

Nếu ứng dụng (application / 애플리케이션) có nhiều datastore, restore mỗi datastore về thời điểm khác nhau còn có thể vi phạm nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식) dù từng cơ sở dữ liệu (database / 데이터베이스) riêng lẻ đều hợp lệ. Ví dụ thứ tự (order / 순서) trạng thái (state / 상태) ở DB A đã lần ghi nhận (commit / 커밋) nhưng payment sự kiện (event / 이벤트) ở store B restore về trước đó.

Backup thiết kế (design / 설계) vì vậy phải xác định consistency ranh giới (boundary / 경계), không chỉ “snapshot đã success”. cơ sở dữ liệu (database / 데이터베이스) internals sâu hơn giữ ở chuẩn gốc (canonical / 정본) dữ liệu (data / 데이터) & Databases; DevOps cần bảo đảm restore workflow hiểu đặc tả ứng dụng (application contract / 애플리케이션 계약).

## 17. Point-in-time khôi phục (recovery / 복구) cần cả cơ sở (base / 기반) backup và log chuỗi (chain / 사슬) usable

Point-in-time khôi phục (recovery / 복구) thường dựa trên một cơ sở (base / 기반) snapshot/backup cộng chuỗi log/giao dịch (transaction / 트랜잭션) thay đổi (change / 변경) tới mốc cần phục hồi. Có backup full nhưng thiếu một đoạn log hoặc key giải mã có thể làm khôi phục (recovery / 복구) tới thời điểm mục tiêu bất khả thi.

Restore drill nên kiểm tra chuỗi (chain / 사슬) end-to-end, không chỉ danh sách (list / 목록) tệp (file / 파일) tồn tại. RPO thực tế được quyết định bởi log shipping/retention và mốc gần nhất có thể phục hồi thành công, không phải con số trong chính sách (policy / 정책) document.

## 18. DR bootstrap phải được xem như phụ thuộc (dependency / 의존성) closure

Khi region chính mất, khôi phục (recovery / 복구) môi trường (environment / 환경) cần một tập tối thiểu phụ thuộc (dependency / 의존성) để có thể tự dựng phần còn lại. Nếu IaC trạng thái (state / 상태) backend, DNS admin, KMS key, định danh (identity / 식별자) provider và sản phẩm tạo ra (artifact / 산출물) registry đều chỉ truy cập được từ region đã mất, automation DR có thể không khởi động.

Hãy vẽ bootstrap đồ thị (graph / 그래프) và hỏi thành phần (component / 컴포넌트) nào cần tồn tại trước để tạo thành phần (component / 컴포넌트) sau. Một số control-plane asset cần replication/cross-region truy cập (access / 접근) độc lập với ứng dụng (application / 애플리케이션) dữ liệu (data / 데이터). khôi phục (recovery / 복구) plan tốt biết **thứ tự khởi động** chứ không chỉ danh sách tài nguyên (resource / 자원).

## 19. Failover cũng là một distributed-state thay đổi (change / 변경)

Chuyển traffic sang replica/region mới cần đảm bảo writer quyền sở hữu (ownership / 소유권). Nếu old primary chưa chắc đã chết mà new primary được mở ghi (write / 쓰기) không có fencing, split brain có thể xuất hiện. Đây là lý do lease/fencing/consensus là chuẩn gốc (canonical / 정본) phụ thuộc (dependency / 의존성) quan trọng cho HA.

Ở DevOps tầng (layer / 계층), runbook phải biết thất bại (failure / 실패) detector có bất định (uncertainty / 불확실성) và thao tác promote/failback có điều kiện (condition / 조건) nào. “Không ping được primary nên promote ngay” có thể nguy hiểm nếu mạng (network / 네트워크) partition chỉ tách operator khỏi primary nhưng primary vẫn phục vụ một phần traffic.

## 20. Failback thường khó hơn failover

Sau khi chạy ở DR region nhiều giờ, dữ liệu (data / 데이터)/trạng thái (state / 상태) mới đã sinh ở nơi dự phòng. Chuyển ngược không phải chỉ đổi DNS về. Cần đồng bộ dữ liệu (data / 데이터) direction, bảo đảm old primary đã catch up hoặc rebuild, kiểm tra phiên bản (version / 버전)/cấu hình (config / 설정) drift và staged traffic return.

Một DR plan chỉ mô tả failover mà không có failback/reconciliation để lại hệ thống ở trạng thái tạm kéo dài và tăng rủi ro (risk / 위험) cho sự cố (incident / 인시던트) tiếp theo.

## 21. Chaos experiment cần phân biệt hypothesis thất bại (failure / 실패) với experiment thất bại (failure / 실패)

Nếu experiment inject mạng (network / 네트워크) mất mát (loss / 손실) nhưng công cụ (tool / 도구) inject chỉ vào một subset khác dự kiến, kết quả không chứng minh hệ thống (system / 시스템) resilient. Experiment phải verify fault thực sự xảy ra, steady-state tín hiệu (signal / 신호) được đo đúng và stop điều kiện (condition / 조건) hoạt động.

Ví dụ hypothesis “mất một zone checkout vẫn đạt SLO”. Experiment cần chứng minh tải công việc (workload / 워크로드)/traffic của zone thật sự unavailable, không phải scheduler vô tình chưa đặt replica ở zone đó. Sau đó mới đọc SLO/người dùng (user / 사용자) impact.

## 22. cấp cao (senior / 시니어) walkthrough: backup hàng ngày nhưng RTO vẫn không đạt

Giả sử backup cơ sở dữ liệu (database / 데이터베이스) 500 GB chạy mỗi ngày thành công. Disaster thật cần restore sang region khác; tải backup mất 2 giờ, replay log 90 phút, provisioning mạng (network / 네트워크)/secret thêm 45 phút, kiểm tra hợp lệ (validation / 검증) 30 phút. Tổng khôi phục (recovery / 복구) hơn 4 giờ trong khi RTO nghiệp vụ (business / 비즈니스) là 60 phút.

Backup success tỷ lệ (rate / 비율) 100% không giải quyết mismatch này. Kiến trúc cần thay đổi: warm standby, snapshot locality, pre-provisioned sức chứa (capacity / 용량), faster restore đường dẫn (path / 경로) hoặc điều chỉnh RTO nếu chi phí (cost / 비용) không hợp lý.

Đây là ví dụ vì sao RTO là end-to-end năng lực (capability / 역량) chỉ số (metric / 지표), không phải thuộc tính của một backup job.

## 23. “dịch vụ (service / 서비스) đã lên lại” chưa phải khôi phục (recovery / 복구) complete

Một HTTP endpoint trả 200 sau failover chỉ chứng minh một phần dữ liệu (data / 데이터) đường dẫn (path / 경로) hoạt động. khôi phục (recovery / 복구) complete cần xác nhận nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식): ghi (write / 쓰기) mới có lần ghi nhận (commit / 커밋) đúng không, hàng đợi (queue / 큐) cũ có đang drain không, duplicate side tác động (effect / 효과) có xuất hiện không, read replica/bộ nhớ đệm (cache / 캐시) có stale quá mức không và background job có tiếp tục từ checkpoint hợp lệ không.

Runbook nên có **exit criteria** rõ thay vì dựa vào cảm giác dashboard xanh. Ví dụ: lỗi (error / 오류) ngân sách (budget / 예산) burn về mức bình thường, backlog age giảm liên tục, payment reconciliation không có mismatch, replica lag dưới threshold và không còn traffic tới old writer.

Điều này ngăn sự cố (incident / 인시던트) bị đóng quá sớm rồi tái mở khi deferred công việc (work / 작업) bắt đầu gây hậu quả.

## 24. khôi phục (recovery / 복구) thường có một backlog phải xử lý sau khi sức chứa (capacity / 용량) trở lại

Trong outage, yêu cầu (request / 요청) có thể nằm trong hàng đợi (queue / 큐), máy khách (client / 클라이언트) thử lại (retry / 재시도), batch bị dồn và scheduled job bị miss. Khi phụ thuộc (dependency / 의존성) hồi phục, tất cả cùng quay lại tạo **khôi phục (recovery / 복구) tải (load / 로드)** lớn hơn steady-state traffic.

Nếu dịch vụ (service / 서비스) vừa đủ sức chứa (capacity / 용량) cho normal tải (load / 로드), mở toàn bộ producer ngay có thể tạo second outage. khôi phục (recovery / 복구) plan nên kiểm soát ramp-up, replay tỷ lệ (rate / 비율), thử lại (retry / 재시도) ngân sách (budget / 예산) và priority giữa realtime traffic với backlog.

Một hệ thống resilient không chỉ sống qua thất bại (failure / 실패); nó phải **hội tụ trở lại steady trạng thái (state / 상태) có kiểm soát**.

## 25. dữ liệu (data / 데이터) integrity xác minh (verification / 확인) phải tách khỏi hạ tầng (infrastructure / 인프라) health

Cơ sở dữ liệu (database / 데이터베이스) tiến trình (process / 프로세스) healthy và replication connected không chứng minh nghiệp vụ (business / 비즈니스) dữ liệu (data / 데이터) đúng sau restore/failover. Cần kiểm tra hợp lệ (validation / 검증) ở mức (level / 수준) phù hợp: row/count/checksum khi hữu ích, foreign/nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식), reconciliation với hệ thống bên ngoài (external system / 외부 시스템) hoặc sampled giao dịch (transaction / 트랜잭션) replay.

Ví dụ payment hệ thống (system / 시스템) có thể restore DB thành công nhưng mất một đoạn sự kiện (event / 이벤트) đã gửi sang provider trước RPO ranh giới (boundary / 경계). Khi đó cục bộ (local / 로컬) cơ sở dữ liệu (database / 데이터베이스) hợp lệ về lưu trữ (storage / 저장소) nhưng nghiệp vụ (business / 비즈니스) trạng thái (state / 상태) giữa hai hệ thống lệch.

Khôi phục (recovery / 복구) kiểm thử (test / 테스트) trưởng thành phải trả lời “bytes đọc được” và “nghiệp vụ (business / 비즈니스) trạng thái (state / 상태) nhất quán” như hai câu hỏi riêng.

## 26. Backup cần chống cả accidental deletion lẫn malicious destruction

Nếu attacker hoặc credential bị compromise có quyền xóa môi trường vận hành (production / 운영 환경) và xóa luôn backup, retention chỉ tồn tại trên giấy. Một số thất bại (failure / 실패) mô hình (model / 모델) cần immutable/WORM retention, account/credential ranh giới (boundary / 경계) riêng hoặc delayed deletion để backup không cùng blast radius với primary.

Cyber khôi phục (recovery / 복구) còn cần clean-room giả định (assumption / 가정): sản phẩm tạo ra (artifact / 산출물), định danh (identity / 식별자), secret và admin workstation nào còn đáng tin sau compromise? Restore hạ tầng (infrastructure / 인프라) từ backup nhưng dùng lại credential/bản dựng (build / 빌드) chuỗi xử lý (pipeline / 파이프라인) đã bị attacker kiểm soát có thể tái nhiễm hệ thống.

Vì vậy disaster khôi phục (recovery / 복구) và bảo mật (security / 보안) khôi phục (recovery / 복구) có overlap nhưng threat mô hình (model / 모델) khác nhau. DR do region outage giả định điều khiển (control / 제어) plane còn trustworthy; cyber khôi phục (recovery / 복구) có thể không cho phép giả định đó.

## 27. quyết định (decision / 결정) log quan trọng hơn timeline thuần sự kiện

Timeline nói “14:05 quy mô (scale / 규모) lên 50 replica”. quyết định (decision / 결정) log nên thêm: hypothesis nào dẫn tới hành động (action / 동작), bằng chứng (evidence / 증거) nào hỗ trợ, expected chỉ số (metric / 지표) nào phải đổi và điều kiện undo là gì.

Thông tin này giúp người đến sau không lặp lại hành động (action / 동작) đã thất bại và giúp postmortem phân biệt quyết định (decision / 결정) hợp lý với kết quả (outcome / 결과) xấu do bất định (uncertainty / 불확실성). sự cố (incident / 인시던트) rà soát (review / 검토) không nên dùng hindsight để kết luận mọi quyết định sai chỉ vì kết quả cuối xấu.

Một quyết định (decision / 결정) log tốt giữ ngữ cảnh (context / 맥락) của thời điểm ra quyết định — khi operator chưa biết những gì postmortem biết sau này.

## 28. Degraded chế độ (mode / 모드) cần entry và exit giao thức (protocol / 프로토콜)

Brownout/read-only chế độ (mode / 모드)/disable tính năng (feature / 기능) là mitigation mạnh, nhưng sau sự cố (incident / 인시던트) cần biết khi nào bật lại. Nếu khôi phục (recovery / 복구) vừa đủ mong manh mà mọi optional tải công việc (workload / 워크로드) được mở đồng thời, tải (load / 로드) có thể vượt sức chứa (capacity / 용량) lần nữa.

Degraded chế độ (mode / 모드) nên có phụ thuộc (dependency / 의존성) và exit criteria: cốt lõi (core / 핵심) SLO ổn trong bao lâu, backlog còn bao nhiêu, downstream headroom thế nào, bộ nhớ đệm (cache / 캐시) đã warm chưa, replica lag đã bắt kịp chưa. Re-enable từng năng lực (capability / 역량) theo staged thứ tự (order / 순서) thường an toàn hơn một switch “mọi thứ normal”.

Điều này biến graceful degradation từ emergency hack thành độ tin cậy (reliability / 신뢰성) năng lực (capability / 역량) có vòng đời (lifecycle / 생명주기).

## 29. khôi phục (recovery / 복구) automation phải có idempotency và resume ngữ nghĩa (semantics / 의미론)

DR workflow có thể thất bại (fail / 실패) ở bước 7/12 vì quota, permission hoặc phụ thuộc (dependency / 의존성) unavailable. Nếu run lại từ đầu tạo duplicate mạng (network / 네트워크)/cơ sở dữ liệu (database / 데이터베이스)/secret hoặc overwrite trạng thái (state / 상태) đã đúng, automation làm khôi phục (recovery / 복구) khó hơn.

Workflow nên giữ thao tác (operation / 연산) định danh (identity / 식별자)/checkpoint, đọc actual trạng thái (state / 상태) và tiếp tục từ phần chưa đạt bất biến (invariant / 불변식). Bước irreversible như promote writer, rotate key hoặc delete old tài nguyên (resource / 자원) cần guard/confirmation mạnh hơn bước create idempotent.

Khôi phục (recovery / 복구) automation là phân tán (distributed / 분산) workflow giống nền tảng (platform / 플랫폼) provisioning; nó cần partial-failure ngữ nghĩa (semantics / 의미론) chứ không chỉ shell script dài.

## 30. Game day phải đo cả human/control-plane đường dẫn (path / 경로)

Một resilience kiểm thử (test / 테스트) chỉ kill pod rồi quan sát autoscaler chưa kiểm tra khả năng organization phục hồi khi cần quyền khẩn cấp, dashboard, DNS admin, KMS, registry hoặc communication channel. Nhiều disaster thật làm mất cùng lúc một phần điều khiển (control / 제어) plane và con người bị stress/thời gian (time / 시간) pressure.

Game day trưởng thành có thể kiểm tra bootstrap truy cập (access / 접근), break-glass, quyết định (decision / 결정) quyền sở hữu (ownership / 소유권), runbook discoverability và communication cadence bên cạnh data-plane failover. Mục tiêu không phải diễn kịch sự cố (incident / 인시던트), mà là tìm phụ thuộc (dependency / 의존성) ẩn trong khôi phục (recovery / 복구) năng lực (capability / 역량).

Nếu mọi kiểm thử (test / 테스트) đều do đúng tác giả runbook thực hiện, chưa chứng minh tài liệu đủ cho người trực khác.

## 31. cấp cao (senior / 시니어) walkthrough: failover thành công rồi outage lần hai khi backlog được mở

Giả sử region A outage 20 phút. Region B failover thành công, realtime traffic ổn ở 60% sức chứa (capacity / 용량). Trong thời gian outage hàng đợi (queue / 큐) tích 2 triệu message. nhóm (team / 팀) thấy dashboard xanh và bật toàn bộ bên tiêu thụ (consumer / 소비자) ở tính đồng thời (concurrency / 동시성) cũ. bên tiêu thụ (consumer / 소비자) cùng lúc xử lý backlog, mở hàng nghìn DB liên kết (connection / 연결) và gọi bên ngoài (external / 외부) API; độ trễ (latency / 지연 시간) realtime tăng, thử lại (retry / 재시도) xuất hiện và dịch vụ (service / 서비스) lại vượt SLO.

Failover cơ chế (mechanism / 메커니즘) ban đầu đúng. thất bại (failure / 실패) thứ hai đến từ thiếu recovery-rate điều khiển (control / 제어). Mitigation tốt là ưu tiên realtime đường dẫn (path / 경로), throttle replay, tăng bên tiêu thụ (consumer / 소비자) dần theo downstream headroom và theo dõi hàng đợi (queue / 큐) age thay vì chỉ hàng đợi (queue / 큐) độ sâu (depth / 깊이).

Bài học cuối cùng: **khôi phục (recovery / 복구) là một chuyển tiếp trạng thái (state transition / 상태 전이) cần sức chứa (capacity / 용량) ngân sách (budget / 예산), sequencing và bằng chứng (evidence / 증거) riêng**, không phải khoảnh khắc hạ tầng (infrastructure / 인프라) chuyển từ đỏ sang xanh.

## 32. khôi phục (recovery / 복구) đồ thị (graph / 그래프) phải mô tả phụ thuộc (dependency / 의존성) thứ tự (ordering / 순서) và năng lực (capability / 역량) tối thiểu

Danh sách “khởi động A, B, C” không đủ nếu phụ thuộc (dependency / 의존성) giữa chúng thay đổi theo chế độ (mode / 모드). Ví dụ ứng dụng (application / 애플리케이션) cần DNS để gọi cơ sở dữ liệu (database / 데이터베이스), DNS automation lại cần định danh (identity / 식별자), định danh (identity / 식별자) dịch vụ (service / 서비스) cần KMS, còn KMS chính sách (policy / 정책) được deploy từ điều khiển (control / 제어) plane đang hỏng. khôi phục (recovery / 복구) phải tìm một **phụ thuộc (dependency / 의존성) closure tối thiểu** có thể tự đứng lên trước, rồi mới mở rộng năng lực (capability / 역량).

Một cách lập luận (reasoning / 추론) là vẽ đồ thị (graph / 그래프) theo năng lực (capability / 역량) thay vì tên máy chủ (server / 서버): `break-glass identity → key/decrypt → artifact + state access → network/DNS tối thiểu → writer/data path → observability → background workload`. Mỗi cạnh phải trả lời phụ thuộc (dependency / 의존성) có thật sự bắt buộc ở khôi phục (recovery / 복구) chế độ (mode / 모드) hay có thể bypass/degrade an toàn.

Runbook tốt vì vậy không chỉ có thứ tự (order / 순서) mà còn có **precondition** và **proof** cho từng bước. Nếu bước “promote cơ sở dữ liệu (database / 데이터베이스)” yêu cầu fencing old writer, bằng chứng (evidence / 증거) fencing phải tồn tại trước khi hành động (action / 동작) tiếp theo được phép chạy.

## 33. bằng chứng (evidence / 증거) survivability là một yêu cầu (requirement / 요구사항) của resilience

Sự cố (incident / 인시던트) lớn có thể làm mất chính hệ thống dùng để điều tra: log backend ở cùng region, dashboard phụ thuộc SSO đang outage, triển khai (deployment / 배포) lịch sử (history / 이력) chỉ có trong CI điều khiển (control / 제어) plane hoặc kiểm tra (audit / 감사) trail nằm trên cơ sở dữ liệu (database / 데이터베이스) vừa corrupt. Khi đó hệ thống có thể phục hồi chậm không phải vì thiếu operator skill mà vì bằng chứng cùng miền lỗi (failure domain / 장애 도메인) với tải công việc (workload / 워크로드).

Trọng yếu (critical / 중요) bằng chứng (evidence / 증거) cần được phân loại theo câu hỏi khôi phục (recovery / 복구): ai đã thay đổi gì, sản phẩm tạo ra (artifact / 산출물)/cấu hình (config / 설정) nào đang chạy, writer nào có quyền sở hữu (ownership / 소유권), backup nào usable, yêu cầu (request / 요청)/nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식) nào đang thất bại (fail / 실패). Một phần bằng chứng (evidence / 증거) có thể cần replication hoặc retention ở miền lỗi (failure domain / 장애 도메인) độc lập; phần khác cần export/snapshot trước destructive mitigation.

Không phải mọi telemetry phải sống qua disaster. bất biến (invariant / 불변식) là **minimum diagnostic and khôi phục (recovery / 복구) bằng chứng (evidence / 증거)** phải còn truy cập được bằng bootstrap định danh (identity / 식별자)/đường dẫn (path / 경로) đã thiết kế, nếu không runbook đang giả định sensor tồn tại khi cần nhất.

## 34. khôi phục (recovery / 복구) điều khiển (control / 제어) plane và serving mặt phẳng dữ liệu (data plane / 데이터 플레인) có thể khỏe theo thứ tự khác nhau

Một dịch vụ (service / 서비스) đang phục vụ người dùng (user / 사용자) có thể vẫn chạy trong khi điều khiển (control / 제어) plane deploy/cấu hình (config / 설정)/định danh (identity / 식별자) management bị hỏng. Ngược lại điều khiển (control / 제어) plane có thể hồi trước nhưng mặt phẳng dữ liệu (data plane / 데이터 플레인) còn stale, thiếu sức chứa (capacity / 용량) hoặc chưa có writer hợp lệ. Vì vậy trạng thái “nền tảng (platform / 플랫폼) xanh” và “nghiệp vụ (business / 비즈니스) năng lực (capability / 역량) xanh” phải được đo riêng.

Trong khôi phục (recovery / 복구), không nên mở mutation hàng loạt chỉ vì portal/API quản trị đã trả 200. Trước hết cần xác minh controller có trạng thái (state / 상태) đủ mới, bên ngoài (external / 외부) world đã reconcile, data-plane bất biến (invariant / 불변식) đúng và thao tác (operation / 연산) mới không tạo duplicate/orphan. Tương tự, mặt phẳng dữ liệu (data plane / 데이터 플레인) đang sống không có nghĩa có thể trì hoãn vô hạn khôi phục (recovery / 복구) điều khiển (control / 제어) plane nếu certificate/secret/lease sắp hết hạn.

Mô hình tư duy (mental model / 사고 모델) là hai trục: **serving continuity** và **management/khôi phục (recovery / 복구) năng lực (capability / 역량)**. Resilience trưởng thành biết degraded chế độ (mode / 모드) nào giữ được trục thứ nhất trong lúc khôi phục trục thứ hai.

## 35. khôi phục (recovery / 복구) xác minh (verification / 확인) phải kiểm tra negative không gian (space / 공간), không chỉ happy tín hiệu (signal / 신호)

Sau failover, việc thấy yêu cầu (request / 요청) thành công là bằng chứng (evidence / 증거) cần thiết nhưng chưa đủ. Cần hỏi những điều **không được phép còn xảy ra**: còn ghi (write / 쓰기) tới old primary không, còn traffic vào region bị cô lập không, bên tiêu thụ (consumer / 소비자) cũ có tiếp tục phát side tác động (effect / 효과) không, credential bị revoke có còn dùng được không, hàng đợi (queue / 큐) poison có tiếp tục thử lại (retry / 재시도) vô hạn không.

Negative-space check giúp bắt split brain và zombie tải công việc (workload / 워크로드) mà dashboard success-rate có thể che. bằng chứng (evidence / 증거) thường đến từ writer lease/fencing trạng thái (state / 상태), truy cập (access / 접근) log theo region/phiên bản (version / 버전), kiểm tra (audit / 감사) auth, hàng đợi (queue / 큐) attempt và reconciliation mismatch.

Exit criteria tốt gồm cả positive bất biến (invariant / 불변식) lẫn forbidden trạng thái (state / 상태). khôi phục (recovery / 복구) chỉ hoàn tất khi hệ thống vừa làm được điều cần làm vừa **không còn làm những điều nguy hiểm của topology cũ**.

## 36. khôi phục (recovery / 복구) debt xuất hiện khi trạng thái tạm trở thành trạng thái lâu dài

Sau sự cố (incident / 인시던트), nhóm (team / 팀) có thể giữ sức chứa (capacity / 용량) gấp đôi, bypass chính sách (policy / 정책), dùng break-glass credential, disable autoscaler, pin traffic một region hoặc để tính năng (feature / 기능) ở degraded chế độ (mode / 모드). Những hành động (action / 동작) này hợp lý để phục hồi nhưng tạo **khôi phục (recovery / 복구) debt** nếu không có đơn vị sở hữu (owner / 오너)/expiry.

Debt nguy hiểm vì nó thay giả định (assumption / 가정) cho sự cố (incident / 인시던트) tiếp theo: sức chứa (capacity / 용량) tưởng còn nhưng thực ra đang dành cho workaround; chính sách (policy / 정책) bị bypass nên authority rộng hơn; failover lần sau không còn region sạch; manual tuyến (route / 경로) bị quên trong nguồn chuẩn (source of truth / 정본). Vì vậy stabilization phải tạo inventory cho temporary exception và plan hội tụ trở lại supported steady trạng thái (state / 상태).

Post-incident closure nên xác nhận workaround đã được remove hoặc được chuyển thành thiết kế (design / 설계) chính thức có kiểm thử (test / 테스트)/SLO/quyền sở hữu (ownership / 소유권). “người dùng (user / 사용자) hết lỗi” là mốc mitigation; “temporary khôi phục (recovery / 복구) trạng thái (state / 상태) đã được thu hồi” mới là một phần của khôi phục (recovery / 복구) completion.

> **Bàn giao:** Sau **36. khôi phục (recovery / 복구) debt xuất hiện khi trạng thái tạm trở thành trạng thái lâu dài**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 observability telemetry and evidence driven debugging](./00_observability_telemetry_and_evidence_driven_debugging.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
