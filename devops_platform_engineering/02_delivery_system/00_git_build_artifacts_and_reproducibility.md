# Từ nguồn (source / 소스) đến sản phẩm tạo ra (artifact / 산출물): Git, bản dựng (build / 빌드) và tính tái lập

> **Mạch đọc:** Đọc **Từ nguồn (source / 소스) đến sản phẩm tạo ra (artifact / 산출물): Git, bản dựng (build / 빌드) và tính tái lập** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. nguồn (source / 소스) điều khiển (control / 제어) là lịch sử thay đổi, không phải kho tệp (file / 파일)** sang **2. bản dựng (build / 빌드) là hàm biến đầu vào (input / 입력) thành đầu ra (output / 출력)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


## 1. nguồn (source / 소스) điều khiển (control / 제어) là lịch sử thay đổi, không phải kho tệp (file / 파일)

Git quan trọng với delivery vì nó tạo một đồ thị (graph / 그래프) các snapshot có định danh (identity / 식별자). lần ghi nhận (commit / 커밋) băm (hash / 해시) cho phép gắn một thay đổi với rà soát (review / 검토), kiểm thử (test / 테스트) kết quả (result / 결과), hiện vật bản dựng (build artifact / 빌드 산출물) và triển khai (deployment / 배포). Nếu môi trường vận hành (production / 운영 환경) đang chạy nhưng không thể trả lời “lần ghi nhận (commit / 커밋) nào sinh ra nhị phân (binary / 이진) này?”, traceability đã bị đứt.

Branch chiến lược (strategy / 전략) chỉ là một cơ chế quản lý concurrent thay đổi (change / 변경). Mục tiêu thật là giảm thời gian thay đổi sống ngoài nhánh chính và giảm batch kích thước (size / 크기). Nhánh tồn tại quá lâu làm tích hợp (integration / 통합) trở thành sự kiện lớn. Vì vậy trunk-based development thường phù hợp với continuous tích hợp (integration / 통합) khi nhóm (team / 팀) có kiểm thử (test / 테스트) và cờ tính năng (feature flag / 기능 플래그) đủ tốt. Nhưng quy tắc (rule / 규칙) không phải “không được branch”; quy tắc (rule / 규칙) là tích hợp (integration / 통합) phải thường xuyên và thay đổi phải nhỏ đủ để hiểu/quay lui (rollback / 롤백).

## 2. bản dựng (build / 빌드) là hàm biến đầu vào (input / 입력) thành đầu ra (output / 출력)

Mô hình tư duy (mental model / 사고 모델) đơn giản:

```text
artifact = build(source, dependencies, toolchain, configuration)
```

Nếu bất kỳ đầu vào (input / 입력) nào bị ẩn hoặc mutable, cùng lần ghi nhận (commit / 커밋) có thể tạo đầu ra (output / 출력) khác nhau. Ví dụ dùng phụ thuộc (dependency / 의존성) `latest`, download script không pin checksum hoặc bản dựng (build / 빌드) dựa vào gói (package / 패키지) registry trạng thái (state / 상태) hiện tại. Khi đó lần ghi nhận (commit / 커밋) băm (hash / 해시) không còn đủ để tái tạo sản phẩm tạo ra (artifact / 산출물).

Tính tái lập (reproducibility) không nhất thiết đòi bit-for-bit identical cho mọi hệ sinh thái, nhưng phải có đặc tả hợp đồng (contract / 계약) đủ mạnh: phụ thuộc (dependency / 의존성) phiên bản (version / 버전) khóa, toolchain phiên bản (version / 버전) xác định, bản dựng (build / 빌드) instruction versioned và environment-dependent giá trị (value / 값) không được bake ngẫu nhiên vào sản phẩm tạo ra (artifact / 산출물).

## 3. sản phẩm tạo ra (artifact / 산출물) phải bất biến sau khi phát hành

Một anti-pattern phổ biến là dùng tag mutable như `app:latest` và push lại nội dung khác dưới cùng tag. Manifest nhìn không đổi nhưng tải công việc (workload / 워크로드) mới có thể chạy bytes khác. Điều này phá kiểm tra (audit / 감사) và quay lui (rollback / 롤백).

Tag thuận tiện cho con người, digest/content định danh (identity / 식별자) thuận tiện cho machine bất biến (invariant / 불변식). nền tảng (platform / 플랫폼) nên có cách promotion cùng một sản phẩm tạo ra (artifact / 산출물) digest từ kiểm thử (test / 테스트) sang staging rồi môi trường vận hành (production / 운영 환경). Không bản dựng (build / 빌드) lại nguồn (source / 소스) ở mỗi môi trường, vì bản dựng (build / 빌드) lại có nghĩa đưa thêm biến số vào đúng lúc cần tăng confidence.

## 4. cấu hình (configuration / 구성) khác sản phẩm tạo ra (artifact / 산출물)

Không phải mọi thứ đều nên đóng vào ảnh (image / 이미지)/gói (package / 패키지). mã (code / 코드) và thời gian chạy (runtime / 런타임) phụ thuộc (dependency / 의존성) ổn định thuộc sản phẩm tạo ra (artifact / 산출물). Environment-specific cấu hình (configuration / 구성), secret và endpoint thường nên được inject qua triển khai (deployment / 배포)/thời gian chạy (runtime / 런타임) giao diện (interface / 인터페이스). Ranh giới này cho phép cùng sản phẩm tạo ra (artifact / 산출물) chạy ở nhiều môi trường.

Tuy nhiên “externalize cấu hình (config / 설정)” không có nghĩa cấu hình (config / 설정) không cần versioning. Một sự cố (incident / 인시던트) do cấu hình (config / 설정) thay đổi (change / 변경) vẫn là thay đổi (change / 변경). môi trường vận hành (production / 운영 환경) cần biết mã (code / 코드) phiên bản (version / 버전) và cấu hình (config / 설정) phiên bản (version / 버전) nào kết hợp tại thời điểm thất bại (failure / 실패).

## 5. phụ thuộc (dependency / 의존성) pinning và cập nhật (update / 업데이트) chiến lược (strategy / 전략)

Khóa phụ thuộc (dependency / 의존성) giúp reproducibility nhưng tạo trách nhiệm cập nhật (update / 업데이트). Nếu pin mãi, bảo mật (security / 보안) patch và tính tương thích (compatibility / 호환성) improvement không vào được. Nếu luôn lấy newest, bản dựng (build / 빌드) trở nên không deterministic. Hệ thống tốt tách hai hành vi: bản dựng (build / 빌드) thường dùng phiên bản (version / 버전) đã pin; phụ thuộc (dependency / 의존성) cập nhật (update / 업데이트) là một thay đổi (change / 변경) tường minh (explicit / 명시적) qua bot hoặc pull yêu cầu (request / 요청), có kiểm thử (test / 테스트) và rà soát (review / 검토) như mã (code / 코드).

Với cơ sở (base / 기반) ảnh bộ chứa (container image / 컨테이너 이미지) cũng tương tự. `FROM ubuntu:latest` dễ dùng nhưng khó kiểm tra (audit / 감사). Pin digest tăng tính xác định; đồng thời cần automation định kỳ mở cập nhật (update / 업데이트) để cơ sở (base / 기반) ảnh (image / 이미지) không bị đóng băng.

## 6. bản dựng (build / 빌드) bộ nhớ đệm (cache / 캐시): tối ưu hóa (optimization / 최적화) có tính đúng đắn (correctness / 정확성) đặc tả hợp đồng (contract / 계약)

Bộ nhớ đệm (cache / 캐시) bản dựng (build / 빌드) giảm thời gian nhưng bộ nhớ đệm (cache / 캐시) key sai có thể tái sử dụng đầu ra (output / 출력) cũ khi đầu vào (input / 입력) đã đổi. Vì vậy bộ nhớ đệm (cache / 캐시) không chỉ là hiệu năng (performance / 성능) tính năng (feature / 기능); nó là tính đúng đắn (correctness / 정확성) bài toán (problem / 문제). bộ nhớ đệm (cache / 캐시) key phải đại diện mọi đầu vào (input / 입력) ảnh hưởng đầu ra (output / 출력).

Ví dụ với Dockerfile, bản sao (copy / 복사) lockfile và cài phụ thuộc (dependency / 의존성) trước khi bản sao (copy / 복사) toàn nguồn (source / 소스) giúp bộ nhớ đệm (cache / 캐시) phụ thuộc (dependency / 의존성) tầng (layer / 계층) hiệu quả. Nhưng nếu bản dựng (build / 빌드) phụ thuộc tệp (file / 파일) bị bỏ qua khỏi ngữ cảnh (context / 맥락) hoặc môi trường (environment / 환경) variable không nằm trong key, bộ nhớ đệm (cache / 캐시) có thể che lỗi. Khi nghi ngờ bản dựng (build / 빌드) inconsistency, thử clean bản dựng (build / 빌드) để phân biệt lỗi nguồn (source / 소스) với lỗi bộ nhớ đệm (cache / 캐시).

## 7. Provenance và software supply chuỗi (chain / 사슬)

Sản phẩm tạo ra (artifact / 산출물) môi trường vận hành (production / 운영 환경) nên có siêu dữ liệu (metadata / 메타데이터) trả lời: nguồn (source / 소스) repository nào, lần ghi nhận (commit / 커밋) nào, bản dựng (build / 빌드) workflow nào, builder định danh (identity / 식별자) nào, phụ thuộc (dependency / 의존성) nào và thời điểm nào. Provenance không tự động đảm bảo sản phẩm tạo ra (artifact / 산출물) an toàn; nó làm chuỗi bằng chứng có thể kiểm tra.

SBOM (Software Bill of Materials) mô tả thành phần (component / 컴포넌트) bên trong sản phẩm tạo ra (artifact / 산출물). SBOM hữu ích khi một vulnerability mới xuất hiện: thay vì scan mọi nguồn (source / 소스) bằng phỏng đoán, có thể tìm sản phẩm tạo ra (artifact / 산출물) nào chứa phiên bản (version / 버전) bị ảnh hưởng. Chapter bảo mật (security / 보안) sẽ nối provenance, signing và chính sách (policy / 정책) thành supply-chain điều khiển (control / 제어).

## 8. Một chuỗi xử lý (pipeline / 파이프라인) bản dựng (build / 빌드) có đặc tả hợp đồng (contract / 계약) rõ ràng

Một bản dựng (build / 빌드) chuỗi xử lý (pipeline / 파이프라인) tối thiểu nên tách xác minh (verification / 확인) và packaging. xác minh (verification / 확인) chứng minh nguồn (source / 소스) thay đổi (change / 변경) đạt quy tắc (rule / 규칙). Packaging tạo sản phẩm tạo ra (artifact / 산출물). Publish đưa sản phẩm tạo ra (artifact / 산출물) bất biến vào registry/repository. siêu dữ liệu (metadata / 메타데이터) nối sản phẩm tạo ra (artifact / 산출물) với lần ghi nhận (commit / 커밋) và bản dựng (build / 빌드) run.

Pseudo-flow:

```text
checkout exact commit
→ restore trusted cache
→ resolve pinned dependencies
→ compile/build
→ unit/static/security checks
→ package immutable artifact
→ generate metadata/SBOM
→ publish once
```

Không nhất thiết mọi check chạy trước packaging; tổ chức có thể tối ưu parallelism. Điều không nên mất là định danh (identity / 식별자) và promotion ngữ nghĩa (semantics / 의미론).

## 9. thất bại (failure / 실패) mẫu (pattern / 패턴)

Nếu “staging chạy, môi trường vận hành (production / 운영 환경) lỗi” dù mã (code / 코드) được cho là giống nhau, kiểm tra đầu tiên là sản phẩm tạo ra (artifact / 산출물) có thật sự giống nhau không. Nếu staging deploy bằng tag và môi trường vận hành (production / 운영 환경) pull lại tag vài giờ sau, có thể bytes đã khác. Nếu sản phẩm tạo ra (artifact / 산출물) giống, so cấu hình (config / 설정), secret phiên bản (version / 버전), bên ngoài (external / 외부) phụ thuộc (dependency / 의존성) và dữ liệu (data / 데이터)/lược đồ (schema / 스키마) tính tương thích (compatibility / 호환성).

Nếu “rebuild lần ghi nhận (commit / 커밋) cũ nhưng sản phẩm tạo ra (artifact / 산출물) khác”, kiểm tra phụ thuộc (dependency / 의존성) khóa (lock / 잠금), cơ sở (base / 기반) ảnh (image / 이미지), gói (package / 패키지) registry, bản dựng (build / 빌드) timestamp, generated mã (code / 코드) và toolchain. Đây là lý do reproducibility là prerequisite của debugging đáng tin cậy.

## 10. bất biến (invariant / 불변식) cần giữ

Một delivery hệ thống (system / 시스템) trưởng thành phải trả lời được: thay đổi nào sinh sản phẩm tạo ra (artifact / 산출물); sản phẩm tạo ra (artifact / 산출물) nào được deploy; sản phẩm tạo ra (artifact / 산출물) có bất biến không; đầu vào (input / 입력) bản dựng (build / 빌드) có được phiên bản (version / 버전) hóa không; ai/automation nào tạo sản phẩm tạo ra (artifact / 산출물); và cùng sản phẩm tạo ra (artifact / 산출물) có được promote xuyên môi trường không. Khi các câu trả lời này rõ, CI/CD phía sau mới có nền ổn định.

## 11. Reproducible bản dựng (build / 빌드) khác hermetic bản dựng (build / 빌드)

Hai khái niệm liên quan nhưng không giống nhau. bản dựng (build / 빌드) tái lập được (reproducible build) nhấn mạnh cùng đầu vào (input / 입력) cho đầu ra (output / 출력) tương đương theo đặc tả hợp đồng (contract / 계약). bản dựng (build / 빌드) kín (hermetic build) nhấn mạnh quá trình bản dựng (build / 빌드) chỉ được phép thấy những đầu vào (input / 입력) đã khai báo, thay vì vô tình đọc công cụ (tool / 도구), tệp (file / 파일), mạng (network / 네트워크) hoặc gói (package / 패키지) trạng thái (state / 상태) từ môi trường host.

Một bản dựng (build / 빌드) có thể cho kết quả giống nhau nhiều lần trong cùng runner nhưng vẫn không hermetic nếu nó âm thầm dùng JDK cài sẵn trong máy. Ngày runner được nâng cấp, đầu ra (output / 출력) hoặc hành vi (behavior / 동작) có thể đổi. Ngược lại, bản dựng (build / 빌드) hermetic nhưng sản phẩm tạo ra (artifact / 산출물) chứa timestamp ngẫu nhiên có thể chưa bit-for-bit reproducible.

Mô hình tư duy (mental model / 사고 모델) tốt là khai báo **đầu vào (input / 입력) closure**: nguồn (source / 소스), phụ thuộc (dependency / 의존성), toolchain, bản dựng (build / 빌드) quy tắc (rule / 규칙) và dữ liệu nào thực sự ảnh hưởng đầu ra (output / 출력). Càng ít đầu vào (input / 입력) ẩn, debugging và provenance càng đáng tin.

## 12. Reproducible không đồng nghĩa trusted

Một attacker kiểm soát bản dựng (build / 빌드) script hoàn toàn có thể tạo malware theo cách rất reproducible. Vì vậy tính đúng đắn (correctness / 정확성) và trust là hai trục khác nhau. Reproducibility giúp biết cùng đầu vào (input / 입력) tạo cùng đầu ra (output / 출력); provenance/attestation giúp biết đầu vào (input / 입력) và builder nào đã được dùng; authorization/chính sách (policy / 정책) quyết định có tin builder và nguồn (source / 소스) đó hay không.

Chuỗi lập luận (reasoning / 추론) nên là:

```text
identity của source/change
→ identity và isolation của builder
→ declared inputs
→ artifact digest
→ provenance/attestation
→ policy cho phép promotion/deploy hay không
```

Nếu chỉ scan sản phẩm tạo ra (artifact / 산출물) cuối cùng mà không kiểm soát builder, một compromised runner có thể chèn mã (code / 코드) sau kiểm thử (test / 테스트). Nếu chỉ tin builder nhưng phụ thuộc (dependency / 의존성) không pin, bản dựng (build / 빌드) vẫn có đầu vào (input / 입력) ngoài dự kiến.

## 13. bộ nhớ đệm (cache / 캐시) là trust ranh giới (boundary / 경계), không chỉ hiệu năng (performance / 성능) tính năng (feature / 기능)

Dùng chung (shared / 공유) bộ nhớ đệm (cache / 캐시) có thể làm tăng tốc đáng kể, nhưng nếu key collision hoặc writer không đáng tin có thể ghi đầu ra (output / 출력) độc hại vào bộ nhớ đệm (cache / 캐시), job khác sẽ consume mà không chạy lại bước tạo đầu ra (output / 출력). Với bộ nhớ đệm (cache / 캐시) chứa gói (package / 패키지), compiled đối tượng (object / 객체) hoặc Docker tầng (layer / 계층), cần biết ai được ghi, key có bao phủ đầu vào (input / 입력) quan trọng không và bộ nhớ đệm (cache / 캐시) có được phân tách theo trust mức (level / 수준) hay repository hay không.

Pull yêu cầu (request / 요청) từ fork/untrusted nguồn (source / 소스) đặc biệt cần cẩn thận. Một mẫu (pattern / 패턴) an toàn là cho job không tin cậy đọc bộ nhớ đệm (cache / 캐시) phù hợp nhưng không ghi vào bộ nhớ đệm (cache / 캐시) dùng bởi trusted bản phát hành (release / 릴리스) job, hoặc dùng không gian tên (namespace / 네임스페이스)/bộ nhớ đệm (cache / 캐시) key tách biệt. Chi tiết phụ thuộc CI hệ thống (system / 시스템) nhưng bất biến (invariant / 불변식) không đổi: **đầu ra (output / 출력) từ trust lĩnh vực (domain / 도메인) thấp không được trở thành đầu vào (input / 입력) ngầm của trust lĩnh vực (domain / 도메인) cao**.

## 14. Attestation là statement có subject và predicate

Attestation có thể hiểu đơn giản là một statement được một định danh (identity / 식별자) ký/xác nhận về một subject. Subject thường là sản phẩm tạo ra (artifact / 산출물) digest; predicate có thể mô tả provenance, kiểm thử (test / 테스트) kết quả (result / 결과) hoặc chính sách (policy / 정책) fact. Điều quan trọng là không đánh đồng “có signature” với “nội dung statement đúng và đủ”.

Verifier phải kiểm tra ít nhất: subject có đúng digest đang deploy không; signer/builder có nằm trong trust chính sách (policy / 정책) không; statement kiểu (type / 타입) có đúng điều đang cần chứng minh không; và định danh (identity / 식별자)/key có còn hợp lệ theo vòng đời (lifecycle / 생명주기) hiện tại không.

Nhờ đó promotion có thể chuyển từ “chuỗi xử lý (pipeline / 파이프라인) trước đã xanh” sang một đặc tả hợp đồng (contract / 계약) machine-verifiable: sản phẩm tạo ra (artifact / 산출물) D chỉ được vào môi trường vận hành (production / 운영 환경) nếu có provenance từ trusted builder, nguồn (source / 소스) revision được rà soát (review / 검토) theo chính sách (policy / 정책) và các xác minh (verification / 확인) cần thiết gắn đúng với D.

## 15. bản dựng (build / 빌드) siêu dữ liệu (metadata / 메타데이터) phải sống cùng sản phẩm tạo ra (artifact / 산출물) định danh (identity / 식별자)

Log CI thường bị retention ngắn hoặc khó tìm. siêu dữ liệu (metadata / 메타데이터) quan trọng cho môi trường vận hành (production / 운영 환경) không nên chỉ nằm trong một chuỗi xử lý (pipeline / 파이프라인) run URL. sản phẩm tạo ra (artifact / 산출물) danh mục (catalog / 카탈로그)/registry nên cho phép lần từ digest tới nguồn (source / 소스) revision, builder, SBOM, provenance và bản phát hành (release / 릴리스) lịch sử (history / 이력).

Điều này đặc biệt hữu ích trong sự cố (incident / 인시던트) hoặc vulnerability phản hồi (response / 응답). Khi có CVE mới, câu hỏi không còn là “repo nào có phụ thuộc (dependency / 의존성) này?” mà là “sản phẩm tạo ra (artifact / 산출물) nào đang hoặc từng chạy môi trường vận hành (production / 운영 환경) chứa thành phần (component / 컴포넌트) bị ảnh hưởng, được bản dựng (build / 빌드) từ revision nào, và có replacement nào đã verify?”.

## 16. cấp cao (senior / 시니어) ghi chú (note / 노트): promotion là chuyển trust, không phải bản sao (copy / 복사) bytes

Khi sản phẩm tạo ra (artifact / 산출물) D đi từ staging sang môi trường vận hành (production / 운영 환경), bytes không nên đổi. Thứ thay đổi là **mức bằng chứng (evidence / 증거) và authorization** gắn với D. Staging có thể chứng minh tích hợp (integration / 통합) hành vi (behavior / 동작); canary môi trường vận hành (production / 운영 환경) thêm bằng chứng (evidence / 증거) từ traffic thật; approval nếu cần xác nhận rủi ro (risk / 위험)/nghiệp vụ (business / 비즈니스) quyết định (decision / 결정).

Nhìn như vậy giúp tránh anti-pattern “rebuild cho môi trường vận hành (production / 운영 환경) để sạch hơn”. Rebuild tạo subject mới và reset một phần bằng chứng (evidence / 증거). Một delivery hệ thống (system / 시스템) mạnh giữ sản phẩm tạo ra (artifact / 산출물) định danh (identity / 식별자) ổn định rồi tích lũy bằng chứng (evidence / 증거) quanh định danh (identity / 식별자) đó.

## 17. Nondeterminism có thể đến từ những đầu vào (input / 입력) tưởng như vô hại

Timestamp bản dựng (build / 빌드), timezone, locale, filesystem iteration thứ tự (order / 순서), random seed, generated archive siêu dữ liệu (metadata / 메타데이터) hoặc absolute workspace đường dẫn (path / 경로) đều có thể làm đầu ra (output / 출력) bytes khác dù nguồn (source / 소스)/phụ thuộc (dependency / 의존성) giống nhau. Không phải mọi khác biệt byte đều ảnh hưởng hành vi (behavior / 동작), nhưng chúng làm content digest và nhị phân (binary / 이진) comparison khó dùng hơn.

Reproducibility công việc (work / 작업) vì vậy cần xác định **equivalence đặc tả hợp đồng (contract / 계약)**. Với sản phẩm tạo ra (artifact / 산출물) ký theo digest, bit-for-bit determinism có giá trị cao. Với một số gói (package / 패키지), có thể chấp nhận siêu dữ liệu (metadata / 메타데이터) khác nếu executable ngữ nghĩa (semantics / 의미론) giống, nhưng phải biết phần nào được normalize và phần nào không.

Không nên xóa siêu dữ liệu (metadata / 메타데이터) phục vụ traceability chỉ để đạt digest giống nhau. Mục tiêu là loại nondeterminism không có chủ đích, không phải làm sản phẩm tạo ra (artifact / 산출물) mất provenance.

## 18. Build-time mạng (network / 네트워크) là phụ thuộc (dependency / 의존성) môi trường vận hành (production / 운영 환경) gián tiếp

Một bản dựng (build / 빌드) cho phép download tùy ý từ Internet có hidden phụ thuộc (dependency / 의존성) vào DNS, gói (package / 패키지) registry, mirror, certificate chuỗi (chain / 사슬) và nội dung remote tại thời điểm bản dựng (build / 빌드). Lockfile có thể pin phiên bản (version / 버전) nhưng nếu registry cho phép sản phẩm tạo ra (artifact / 산출물) cùng phiên bản (version / 버전) bị thay hoặc script tải nhị phân (binary / 이진) ngoài trình quản lý gói (package manager / 패키지 관리자), reproducibility vẫn yếu.

Một hướng mạnh hơn là dùng trusted mirror/proxy, checksum/content digest, phụ thuộc (dependency / 의존성) bộ nhớ đệm (cache / 캐시) có quyền sở hữu (ownership / 소유권) và chính sách (policy / 정책) rõ. Với hermetic bản dựng (build / 빌드) nghiêm ngặt, mạng (network / 네트워크) có thể bị tắt sau khi declared đầu vào (input / 입력) đã được materialize.

Điểm cốt lõi là phân biệt **resolution** với **bản dựng (build / 빌드) thực thi (execution / 실행)**. phụ thuộc (dependency / 의존성) cập nhật (update / 업데이트)/resolution có thể cần mạng (network / 네트워크); bản dựng (build / 빌드) của revision đã khóa nên càng ít phụ thuộc remote mutable trạng thái (state / 상태) càng tốt.

## 19. Rebuild độc lập là một kỹ thuật kiểm chứng, không chỉ disaster khôi phục (recovery / 복구)

Nếu hai builder độc lập nhận cùng declared inputs và tạo sản phẩm tạo ra (artifact / 산출물) tương đương, confidence tăng rằng đầu ra (output / 출력) không phụ thuộc runner hidden trạng thái (state / 상태). Trong supply-chain bảo mật (security / 보안), independent rebuild còn giúp phát hiện một builder bị compromise nếu đầu ra (output / 출력) lệch bất ngờ.

Không phải mọi nhóm (team / 팀) cần hệ thống reproducible-build cấp distro. Nhưng với sản phẩm tạo ra (artifact / 산출물) trọng yếu (critical / 중요), có thể dùng periodic clean-room rebuild hoặc rebuild khi sự cố (incident / 인시던트) để kiểm tra hidden đầu vào (input / 입력)/bộ nhớ đệm (cache / 캐시) contamination.

Nếu rebuild chỉ pass khi dùng lại cùng bộ nhớ đệm (cache / 캐시)/runner ảnh (image / 이미지) cũ, đó là tín hiệu (signal / 신호) rằng đầu vào (input / 입력) closure chưa thật sự được kiểm soát.

## 20. sản phẩm tạo ra (artifact / 산출물) phải mang định danh (identity / 식별자) của nền tảng (platform / 플랫폼) mục tiêu (target / 대상) khi mục tiêu (target / 대상) ảnh hưởng bytes

Cùng nguồn (source / 소스) có thể bản dựng (build / 빌드) cho `linux/amd64`, `linux/arm64`, GPU thời gian chạy (runtime / 런타임) khác hoặc libc khác. Gọi tất cả là “phiên bản (version / 버전) 1.2.3” mà không giữ nền tảng (platform / 플랫폼) dimension có thể làm triển khai (deployment / 배포) lấy sản phẩm tạo ra (artifact / 산출물) không tương thích hoặc khiến vulnerability inventory sai.

Sản phẩm tạo ra (artifact / 산출물) định danh (identity / 식별자) nên đủ để phân biệt mục tiêu (target / 대상) quan trọng, đồng thời bản phát hành (release / 릴리스) siêu dữ liệu (metadata / 메타데이터) có thể gom nhiều variant dưới một logical phiên bản (version / 버전). bộ chứa (container / 컨테이너) manifest chỉ mục (index / 인덱스) là một ví dụ: logical ảnh (image / 이미지) tham chiếu (reference / 참조) có nhiều digest con theo kiến trúc (architecture / 아키텍처).

Traceability môi trường vận hành (production / 운영 환경) phải đi tới digest/variant thực sự chạy, không dừng ở marketing phiên bản (version / 버전)/tag.

## 21. Generated mã (code / 코드) và trình biên dịch (compiler / 컴파일러) flag là nguồn (source / 소스) theo nghĩa delivery

Một repository có thể chứa lược đồ (schema / 스키마)/IDL rồi generate máy khách (client / 클라이언트)/máy chủ (server / 서버) mã (code / 코드) trong bản dựng (build / 빌드). Nếu generator phiên bản (version / 버전) hoặc flag thay đổi, đầu ra (output / 출력) thay đổi dù handwritten nguồn (source / 소스) không đổi. Tương tự trình biên dịch (compiler / 컴파일러) tối ưu hóa (optimization / 최적화), tính năng (feature / 기능) toggle compile-time hoặc bản dựng (build / 빌드) profile có thể làm hành vi (behavior / 동작) khác.

Vì vậy “nguồn (source / 소스) revision” trong provenance cần đi cùng bản dựng (build / 빌드) recipe/toolchain. Nếu generated đầu ra (output / 출력) được lần ghi nhận (commit / 커밋), repository phải có chính sách (policy / 정책) tránh nguồn (source / 소스) và generated tệp (file / 파일) drift. Nếu generate lúc bản dựng (build / 빌드), generator phải nằm trong declared đầu vào (input / 입력) closure.

Điều quan trọng không phải lần ghi nhận (commit / 커밋) generated mã (code / 코드) hay không; điều quan trọng là có **một authority rõ** cho đầu ra (output / 출력) và có thể tái tạo nó.

## 22. cấp cao (senior / 시니어) walkthrough: cùng lần ghi nhận (commit / 커밋) nhưng môi trường vận hành (production / 운영 환경) nhị phân (binary / 이진) khác staging

Giả sử staging và môi trường vận hành (production / 운영 환경) đều ghi lần ghi nhận (commit / 커밋) `abc123`, nhưng checksum nhị phân (binary / 이진) khác. Staging được bản dựng (build / 빌드) tuần trước trên runner ảnh (image / 이미지) JDK 21.0.4; môi trường vận hành (production / 운영 환경) chuỗi xử lý (pipeline / 파이프라인) rebuild hôm nay sau khi runner ảnh (image / 이미지) tự động lên 21.0.5 và một code-generation plugin lấy `latest`.

Lần ghi nhận (commit / 커밋) định danh (identity / 식별자) đúng nhưng bản dựng (build / 빌드) đầu vào (input / 입력) closure khác. Điều tra phải so toolchain/provenance/phụ thuộc (dependency / 의존성) resolution, không so nguồn (source / 소스) diff. Corrective hành động (action / 동작) là bản dựng (build / 빌드) một sản phẩm tạo ra (artifact / 산출물) bất biến từ chính xác (exact / 정확한) declared inputs rồi promote cùng digest, thay vì dùng lần ghi nhận (commit / 커밋) SHA như thể nó là sản phẩm tạo ra (artifact / 산출물) định danh (identity / 식별자).

Bài học là `commit → artifact` là một hàm chỉ đáng tin khi đầu vào (input / 입력) ngoài lần ghi nhận (commit / 커밋) được kiểm soát và được ghi lại.

> **Bàn giao:** Sau **22. cấp cao (senior / 시니어) walkthrough: cùng lần ghi nhận (commit / 커밋) nhưng môi trường vận hành (production / 운영 환경) nhị phân (binary / 이진) khác staging**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 ci cd change flow and safe delivery](./01_ci_cd_change_flow_and_safe_delivery.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
