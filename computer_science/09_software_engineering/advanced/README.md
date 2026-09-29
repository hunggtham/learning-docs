# Advanced Kỹ nghệ phần mềm (software engineering / 소프트웨어 공학)

> **Mạch đọc:** Đọc **Advanced Kỹ nghệ phần mềm (software engineering / 소프트웨어 공학)** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **chuẩn gốc (canonical / 정본) chapters** sang **mô hình tư duy (mental models / 사고 모델들) cần đạt**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

Nhánh học (track / 트랙) này tập trung vào cách thay đổi môi trường vận hành (production / 운영 환경) hệ thống (system / 시스템) dưới bất định (uncertainty / 불확실성) mà không cần big-bang coordination. Không thêm chapter chỉ để bao phủ methodology hoặc chỉ số (metric / 지표) mới; ưu tiên quyết định (decision / 결정) ranh giới (boundary / 경계), tính tương thích (compatibility / 호환성), di chuyển (migration / 마이그레이션), xác minh (verification / 확인), bằng chứng (evidence / 증거) và economics của changeability.

## Chuẩn gốc (canonical / 정본) chapters

1. [Architecture decisions, evolution và socio-technical constraints](./00_architecture_decisions_evolution_and_socio_technical_constraints.md)
2. [Modular monolith vs services: boundary economics và migration](./01_modular_monolith_vs_services_boundary_economics.md)
3. [API/schema compatibility và evolutionary design](./02_api_schema_compatibility_and_evolutionary_design.md)
4. [Large-scale refactoring, strangler migration và branch-by-abstraction](./03_large_scale_refactoring_strangler_and_branch_by_abstraction.md)
5. [Test architecture: contract, mutation, property-based và production verification](./04_test_architecture_contract_mutation_property_and_production_verification.md)
6. [Deployment safety: canary, blue-green, feature flags và rollback limits](./05_deployment_safety_canary_blue_green_flags_and_rollback.md)
7. [Technical debt economics, engineering metrics và Goodhart's Law](./06_technical_debt_economics_metrics_and_goodhart.md)


> **Chuyển mạch:** Từ **chuẩn gốc (canonical / 정본) chapters**, ta sang **mô hình tư duy (mental models / 사고 모델들) cần đạt** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental models / 사고 모델들) cần đạt

Mỗi thay đổi phải được lập luận (reasoning / 추론) như một chuyển tiếp trạng thái (state transition / 상태 전이) có overlap cửa sổ (window / 윈도우):

```text
old world
→ mixed versions / partial rollout
→ migration state
→ new world
```

Bất biến (invariant / 불변식) quan trọng là hệ thống (system / 시스템) vẫn tương thích và quan sát được trong toàn bộ chuyển tiếp (transition / 전이), không chỉ ở trạng thái cuối.

Kiến trúc (architecture / 아키텍처) quyết định (decision / 결정) cần chỉ ra chất lượng (quality / 품질) attribute/sự đánh đổi (trade-off / 트레이드오프) nào được tối ưu, giả định (assumption / 가정) nào đang dựa vào và bằng chứng (evidence / 증거) nào sẽ cho biết quyết định (decision / 결정) không còn phù hợp. triển khai (deployment / 배포) chiến lược (strategy / 전략) phải nói rõ blast radius, quay lui (rollback / 롤백) limit, irreversible side tác động (effect / 효과) và guardrail nào quyết định tiếp tục hay dừng rollout.

Technical debt được nâng thành chuẩn gốc (canonical / 정본) chapter riêng vì nó có lập luận (reasoning / 추론) đường dẫn (path / 경로) về recurring thay đổi (change / 변경) chi phí (cost / 비용), option giá trị (value / 값), di chuyển (migration / 마이그레이션) timing, coordination/dữ liệu (data / 데이터)/kiểm thử (test / 테스트)/operational debt và chỉ số (metric / 지표) quản trị (governance / 거버넌스). Debt không được đánh giá bằng aesthetic hoặc một score tổng hợp; cần bằng chứng (evidence / 증거) về interest/rủi ro (risk / 위험) và trigger trả debt.


> **Chuyển mạch:** Từ **mô hình tư duy (mental models / 사고 모델들) cần đạt**, ta sang **hệ thống (system / 시스템) thiết kế (design / 설계) và Kỹ nghệ phần mềm (software engineering / 소프트웨어 공학) giao nhau ở changeability** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Hệ thống (system / 시스템) thiết kế (design / 설계) và Kỹ nghệ phần mềm (software engineering / 소프트웨어 공학) giao nhau ở changeability

Hệ thống (system / 시스템) thiết kế (design / 설계) nằm ở `08_software_systems` và các lĩnh vực (domain / 도메인) thời gian chạy (runtime / 런타임)/mạng (network / 네트워크)/cơ sở dữ liệu (database / 데이터베이스); Kỹ nghệ phần mềm (software engineering / 소프트웨어 공학) sở hữu câu hỏi **làm sao thay đổi thiết kế (design / 설계) đó an toàn và kinh tế theo thời gian**.

Zero-downtime cơ sở dữ liệu (database / 데이터베이스) di chuyển (migration / 마이그레이션), sự cố (incident / 인시던트) học tập (learning / 학습), technical debt, nhóm (team / 팀) quyền sở hữu (ownership / 소유권) và kiến trúc (architecture / 아키텍처) quản trị (governance / 거버넌스) được nối qua chuẩn gốc (canonical / 정본) chapters theo perspective evolution/quyết định (decision / 결정) thay vì tạo methodology danh mục (catalog / 카탈로그).


> **Chuyển mạch:** Từ **hệ thống (system / 시스템) thiết kế (design / 설계) và Kỹ nghệ phần mềm (software engineering / 소프트웨어 공학) giao nhau ở changeability**, ta sang **bằng chứng vận hành (production evidence / 운영 증거)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Bằng chứng vận hành (production evidence / 운영 증거)

Một thay đổi môi trường vận hành (production / 운영 환경) phải để lại bằng chứng (evidence / 증거) đủ để kiểm tra hypothesis: triển khai (deployment / 배포) phiên bản (version / 버전)/cohort, lỗi (error / 오류) và độ trễ (latency / 지연 시간) percentile, SLO burn, tính tương thích (compatibility / 호환성) failures, lược đồ (schema / 스키마)/dữ liệu (data / 데이터) di chuyển (migration / 마이그레이션) progress, quay lui (rollback / 롤백) feasibility, kiểm thử (test / 테스트) tín hiệu (signal / 신호), nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식), repeated thay đổi (change / 변경) amplification và operational toil.

Chỉ số (metric / 지표) chỉ có giá trị khi gắn với quyết định (decision / 결정). DORA-style tín hiệu (signal / 신호), kiểm thử (test / 테스트) coverage, triển khai (deployment / 배포) frequency, LOC hay ticket thông lượng (throughput / 처리량) không được dùng như proxy tuyệt đối cho kỹ thuật (engineering / 엔지니어링) chất lượng (quality / 품질) nếu không hiểu cơ chế (mechanism / 메커니즘) và Goodhart rủi ro (risk / 위험) phía sau.


> **Chuyển mạch:** Từ **bằng chứng vận hành (production evidence / 운영 증거)**, ta sang **Quy tắc mở rộng** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Quy tắc mở rộng

Ưu tiên deepen chapter hiện có khi gap thuộc kiến trúc (architecture / 아키텍처) ranh giới (boundary / 경계), tính tương thích (compatibility / 호환성), di chuyển (migration / 마이그레이션), xác minh (verification / 확인), triển khai (deployment / 배포) an toàn (safety / 안전) hoặc debt economics. Chỉ thêm conceptual đơn vị (unit / 단위) mới khi có bất biến (invariant / 불변식)/dạng thất bại (failure mode / 실패 모드) độc lập mà các chapter chuẩn gốc (canonical / 정본) không thể chứa tự nhiên.

> **Bàn giao:** Sau **Quy tắc mở rộng**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 architecture decisions evolution and socio technical constraints](./00_architecture_decisions_evolution_and_socio_technical_constraints.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
