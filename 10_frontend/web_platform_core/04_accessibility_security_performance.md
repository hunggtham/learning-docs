# Khả năng tiếp cận (accessibility / 접근성), bảo mật (security / 보안) và hiệu năng (performance / 성능) như tính đúng đắn (correctness / 정확성)

> **Mạch đọc:** Đặt **khả năng tiếp cận (accessibility / 접근성), bảo mật (security / 보안) và hiệu năng (performance / 성능) như tính đúng đắn (correctness / 정확성)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **khả năng tiếp cận (accessibility / 접근성)** sang **bảo mật (security / 보안)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

Ba concern này không phải checklist cuối sprint. Chúng là ràng buộc (constraint / 제약조건) của cùng
một nền tảng (platform / 플랫폼) đặc tả hợp đồng (contract / 계약): người dùng phải có thể hiểu/tương tác, dữ liệu không
được vượt trust ranh giới (boundary / 경계) sai, và công việc (work / 작업) phải nằm trong ngân sách (budget / 예산) có thể đo.

## Khả năng tiếp cận (accessibility / 접근성)

Bản địa (native / 네이티브) ngữ nghĩa (semantics / 의미론), accessible name, focus thứ tự (order / 순서), keyboard thao tác (operation / 연산), lỗi (error / 오류)
announcement, live region và reduced-motion preference tạo nên công khai (public / 공개) hành vi (behavior / 동작).
ARIA chỉ bổ sung khi bản địa (native / 네이티브) element không đủ; nó không sửa một document mô hình (model / 모델)
sai. Conditional rendering, portal, popup, WFrame, lazy loading và hydration
đều phải giữ ngữ nghĩa (semantics / 의미론) và focus restoration.


> **Chuyển mạch:** Từ **khả năng tiếp cận (accessibility / 접근성)**, ta sang **bảo mật (security / 보안)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Bảo mật (security / 보안)

Tách kiểm tra hợp lệ (validation / 검증), encoding, sanitization và authorization. URL/HTML/lưu trữ (storage / 저장소)/
`postMessage`/iframe/WebView cầu nối (bridge / 브리지) là untrusted đầu vào (input / 입력) cho tới khi ranh giới (boundary / 경계)
được xác định. XSS, CSRF, CORS, cookie/đơn vị từ (token / 토큰), CSP/Trusted Types và phụ thuộc (dependency / 의존성)
supply chuỗi (chain / 사슬) có dạng thất bại (failure mode / 실패 모드) khác nhau; UI kiểm tra hợp lệ (validation / 검증) không thay máy chủ (server / 서버) check.


> **Chuyển mạch:** Từ **bảo mật (security / 보안)**, ta sang **hiệu năng (performance / 성능)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Hiệu năng (performance / 성능)

Đo theo chuỗi nhân quả (causal chain / 인과 사슬): DNS/connect/phản hồi (response / 응답) → parse/script → style/bố cục (layout / 레이아웃)/paint
→ đầu vào (input / 입력) độ trễ (latency / 지연 시간) → bộ nhớ (memory / 메모리)/bundle/bộ nhớ đệm (cache / 캐시). dấu vết (trace / 추적) phải ghi trình duyệt (browser / 브라우저), bản dựng (build / 빌드) ID,
mạng (network / 네트워크) điều kiện (condition / 조건) và tải công việc (workload / 워크로드); ngân sách (budget / 예산) nên có guard ở kiểm thử (test / 테스트) hoặc bản phát hành (release / 릴리스) gate.

Các nhánh học (track / 트랙) hiện thực (implementation / 구현) cung cấp chi tiết: [HTML accessibility/security](../html/html_02_master_implementation_detailed.md),
[JavaScript production](../javascript/javascript_master_supplement_detailed.md),
[WebSquare accessibility](../websquare/09_forms_validation_i18n_accessibility.md)
và [WebSquare profiling](../websquare/24_event_semantics_performance_profiling.md).

> **Bàn giao:** Sau **hiệu năng (performance / 성능)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 web platform model](./00_web_platform_model.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
