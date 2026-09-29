# 09 — Warehouse, lake và lakehouse

> **Mạch đọc:** Đọc **09 — Warehouse, lake và lakehouse** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. Warehouse** sang **2. dữ liệu (data / 데이터) lake**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Warehouse, lake và lakehouse là các điểm khác nhau trên trục lưu trữ (storage / 저장소), lược đồ (schema / 스키마), giao dịch (transaction / 트랜잭션), quản trị (governance / 거버넌스) và compute. Không nên chọn bằng khẩu hiệu; hãy bắt đầu từ tải công việc (workload / 워크로드) và bất biến (invariant / 불변식) cần giữ.

## 1. Warehouse

Warehouse thường cung cấp danh mục (catalog / 카탈로그), SQL, tải công việc (workload / 워크로드) isolation, kiểm soát truy cập (access control / 접근 제어) và managed compute cùng các ngữ nghĩa (semantics / 의미론) phân tích tương đối chặt. Đổi lại chi phí, format và portability có thể bị gắn với nền tảng (platform / 플랫폼).

Điểm cần kiểm tra là truy vấn (query / 쿼리) isolation, tính đồng thời (concurrency / 동시성), ingestion độ trễ (latency / 지연 시간), historical correction và quyền truy cập—not chỉ benchmark scan.


> **Chuyển mạch:** Từ **1. Warehouse**, ta sang **2. dữ liệu (data / 데이터) lake** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 2. dữ liệu (data / 데이터) lake

Lake lưu tệp (file / 파일) linh hoạt trên đối tượng (object / 객체) lưu trữ (storage / 저장소), phù hợp raw bằng chứng (evidence / 증거), nhiều format và chi phí lưu trữ (storage / 저장소) thấp. Nếu thiếu lược đồ (schema / 스키마) discipline, quyền sở hữu (ownership / 소유권), chất lượng (quality / 품질) và danh mục (catalog / 카탈로그), lake nhanh chóng trở thành swamp: nhiều tệp (file / 파일) nhưng không biết tệp (file / 파일) nào đáng tin.

Đối tượng (object / 객체) lưu trữ (storage / 저장소) không cung cấp mọi ngữ nghĩa (semantics / 의미론) của filesystem. Rename có thể là bản sao (copy / 복사)+delete; listing có thể eventually consistent; nhiều writer có thể ghi cùng prefix. lần ghi nhận (commit / 커밋) giao thức (protocol / 프로토콜) phải được thiết kế rõ.


> **Chuyển mạch:** Từ **2. dữ liệu (data / 데이터) lake**, ta sang **3. Lakehouse và snapshot** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 3. Lakehouse và snapshot

Lakehouse thêm siêu dữ liệu (metadata / 메타데이터) tầng (layer / 계층) mô tả snapshot hợp lệ của các dữ liệu (data / 데이터) files. Một lần ghi nhận (commit / 커밋) thường gồm:

```text
read current snapshot → validate conflict → write new files → publish metadata pointer
```

Reader chỉ đọc tệp (file / 파일) thuộc snapshot đã lần ghi nhận (commit / 커밋). thời gian (time / 시간) travel là khả năng chọn snapshot cũ, không phải phép màu để phục hồi mọi dữ liệu nếu tệp (file / 파일) đã bị garbage-collect.


> **Chuyển mạch:** Từ **3. Lakehouse và snapshot**, ta sang **4. Compaction** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 4. Compaction

Streaming và micro-batch tạo small files. Compaction đọc nhiều tệp (file / 파일) nhỏ, rewrite thành tệp (file / 파일) lớn hơn và cập nhật siêu dữ liệu (metadata / 메타데이터). Compaction phải bảo đảm reader cũ vẫn đọc được snapshot của nó, reader mới thấy snapshot mới, và tệp (file / 파일) cũ chỉ bị xóa sau retention an toàn.

Compaction quá thường xuyên làm tăng ghi (write / 쓰기) amplification; quá muộn làm truy vấn (query / 쿼리) siêu dữ liệu (metadata / 메타데이터) và tác vụ (task / 작업) scheduling chậm. Trigger nên dựa trên tệp (file / 파일) count/kích thước (size / 크기), truy vấn (query / 쿼리) hành vi (behavior / 동작) và khôi phục (recovery / 복구) cửa sổ (window / 윈도우).


> **Chuyển mạch:** Từ **4. Compaction**, ta sang **5. Snapshot và lược đồ (schema / 스키마) evolution** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 5. Snapshot và lược đồ (schema / 스키마) evolution

Lược đồ (schema / 스키마) evolution cần tương thích với cả tệp (file / 파일) cũ, reader cũ và writer mới. Add nullable trường dữ liệu (field / 필드) thường dễ hơn rename/kiểu (type / 타입) narrowing. Nếu trường dữ liệu (field / 필드) định danh (identity / 식별자) chỉ dựa trên tên, rename có thể bị hiểu như drop+add.

Di chuyển (migration / 마이그레이션) an toàn thường dùng dual-read/dual-write hoặc versioned lược đồ (schema / 스키마), có tính tương thích (compatibility / 호환성) cửa sổ (window / 윈도우) và quay lui (rollback / 롤백) đường dẫn (path / 경로). Xóa column khỏi siêu dữ liệu (metadata / 메타데이터) không đồng nghĩa bytes đã biến mất; retention/privacy chính sách (policy / 정책) phải bao phủ cả tệp (file / 파일) cũ và snapshot cũ.


> **Chuyển mạch:** Từ **5. Snapshot và lược đồ (schema / 스키마) evolution**, ta sang **6. Partition và bố cục (layout / 레이아웃)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 6. Partition và bố cục (layout / 레이아웃)

Partition theo ngày hỗ trợ pruning và vòng đời (lifecycle / 생명주기) nhưng có thể tạo partition nhỏ khi volume thấp. Partition theo high-cardinality key tạo directory explosion. tệp (file / 파일) kích thước (size / 크기), row group, sort thứ tự (order / 순서) và clustering có thể quan trọng hơn số partition.

Bố cục (layout / 레이아웃) phải được đo bằng bytes scanned, files opened, tác vụ (task / 작업) count, compaction chi phí (cost / 비용) và truy vấn (query / 쿼리) độ trễ (latency / 지연 시간) trên tải công việc (workload / 워크로드) thật.


> **Chuyển mạch:** Từ **6. Partition và bố cục (layout / 레이아웃)**, ta sang **7. quyết định (decision / 결정) frame** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 7. quyết định (decision / 결정) frame

Chọn lưu trữ (storage / 저장소) bằng câu hỏi:

1. Raw bằng chứng (evidence / 증거) cần giữ và replay trong bao lâu?
2. bên tiêu thụ (consumer / 소비자) cần SQL ad-hoc, API độ trễ (latency / 지연 시간) hay batch scan?
3. Snapshot/giao dịch (transaction / 트랜잭션) ngữ nghĩa (semantics / 의미론) cần mạnh tới mức nào?
4. lược đồ (schema / 스키마) evolution và multi-writer xung đột (conflict / 충돌) được kiểm soát ra sao?
5. danh mục (catalog / 카탈로그), lineage, kiểm soát truy cập (access control / 접근 제어), deletion và chi phí (cost / 비용) quyền sở hữu (ownership / 소유권) thuộc về ai?

Đọc tiếp: [03 — Storage và formats](../03_storage_and_formats.md), [11 — Governance](../11_governance_lineage_security/README.md), [12 — Cost và capacity](../12_cost_performance_capacity/README.md).


> **Chuyển mạch:** Từ **7. quyết định (decision / 결정) frame**, ta sang **8. Snapshot isolation và xung đột (conflict / 충돌) detection** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 8. Snapshot isolation và xung đột (conflict / 충돌) detection

Hai writer có thể cùng đọc snapshot S0 rồi tạo S1a và S1b. siêu dữ liệu (metadata / 메타데이터) lần ghi nhận (commit / 커밋) phải quyết định:

```text
S0 + changes(a) → S1a
S0 + changes(b) → reject/merge → S2
```

Nếu lần ghi nhận (commit / 커밋) chỉ kiểm tra tệp (file / 파일) đường dẫn (path / 경로) mới mà bỏ qua logical overlap, hai writer có thể cùng sửa một partition và làm mất cập nhật (update / 업데이트). xung đột (conflict / 충돌) detection phải xét partition/key/phạm vi (range / 범위) mà thao tác (operation / 연산) đọc và ghi.


> **Chuyển mạch:** Từ **8. Snapshot isolation và xung đột (conflict / 충돌) detection**, ta sang **9. thời gian (time / 시간) travel, retention và GDPR-style delete** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 9. thời gian (time / 시간) travel, retention và GDPR-style delete

Thời gian (time / 시간) travel hữu ích cho kiểm tra (audit / 감사) và quay lui (rollback / 롤백) nhưng giữ snapshot cũ đồng nghĩa giữ bytes cũ. Retention chính sách (policy / 정책) cần đồng thời trả lời truy vấn (query / 쿼리) quay lui (rollback / 롤백), replay cửa sổ (window / 윈도우), backup cửa sổ (window / 윈도우) và deletion yêu cầu (requirement / 요구사항).

Khi cần xóa một subject, phải xác định dữ liệu (data / 데이터) files, snapshots, manifests, materialized views, caches và downstream exports nào chứa bản ghi (record / 레코드). Rewriting tệp (file / 파일) để redact có thể phá snapshot lineage; do đó deletion job cần tạo bằng chứng (evidence / 증거) về phiên bản (version / 버전) trước/sau và xác nhận các bản bản sao (copy / 복사) đã hết retention.


> **Chuyển mạch:** Từ **9. thời gian (time / 시간) travel, retention và GDPR-style delete**, ta sang **10. bảng (table / 테이블) maintenance đặc tả hợp đồng (contract / 계약)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 10. bảng (table / 테이블) maintenance đặc tả hợp đồng (contract / 계약)

Compaction, clustering, vacuum/garbage collection và statistics refresh là các workflow có phụ thuộc (dependency / 의존성) với reader/writer. Mỗi maintenance tác vụ (task / 작업) cần:

1. đầu vào (input / 입력) snapshot và tệp (file / 파일) set;
2. đầu ra (output / 출력) snapshot/manifest;
3. xung đột (conflict / 충돌) chính sách (policy / 정책) với concurrent writer;
4. retention deadline của tệp (file / 파일) cũ;
5. tính đúng đắn (correctness / 정확성) check trước publish;
6. quay lui (rollback / 롤백) hoặc restore đường dẫn (path / 경로).

Maintenance không nên chạy như cron vô danh; nó là một dữ liệu (data / 데이터) sản phẩm (product / 제품) thao tác (operation / 연산) có đơn vị sở hữu (owner / 오너) và ngân sách (budget / 예산).

> **Bàn giao:** Sau **10. bảng (table / 테이블) maintenance đặc tả hợp đồng (contract / 계약)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp.
