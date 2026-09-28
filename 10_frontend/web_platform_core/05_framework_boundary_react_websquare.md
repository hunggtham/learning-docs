# Khung phần mềm (framework / 프레임워크) ranh giới (boundary / 경계): React và WebSquare

> **Mạch đọc:** Đặt **khung phần mềm (framework / 프레임워크) ranh giới (boundary / 경계): React và WebSquare** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **React** sang **WebSquare**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

Khung phần mềm (framework / 프레임워크) giúp tổ chức ứng dụng (application / 애플리케이션) trạng thái (state / 상태) và rendering, nhưng không phải một
trình duyệt (browser / 브라우저) mới. Khi khung phần mềm (framework / 프레임워크) hành vi (behavior / 동작) khó hiểu, quay về ba câu hỏi: thành phần nguyên thủy (primitive / 기본 요소)
nào của trình duyệt (browser / 브라우저) đang được dùng; khung phần mềm (framework / 프레임워크) sở hữu định danh (identity / 식별자)/vòng đời (lifecycle / 생명주기)/scheduling
nào; đặc tả ứng dụng (application contract / 애플리케이션 계약) nào cần kiểm thử (test / 테스트) và telemetry.

## React

React quản lý thành phần (component / 컴포넌트) định danh (identity / 식별자), kết xuất (render / 렌더링)/reconciliation, trạng thái (state / 상태), Effects,
tính đồng thời (concurrency / 동시성) và các máy chủ (server / 서버)/máy khách (client / 클라이언트) ranh giới (boundary / 경계). Nó vẫn kết xuất (render / 렌더링) DOM, dùng CSS, nhận
bản địa (native / 네이티브) events và chịu hydration/parser các ràng buộc (constraints / 제약조건들). gỡ lỗi (debug / 디버그) nên kiểm tra DOM,
CSS, mạng (network / 네트워크) và sự kiện (event / 이벤트) timeline trước khi kết luận reconciliation là nguyên nhân.


> **Chuyển mạch:** Từ **React**, ta sang **WebSquare** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## WebSquare

WebSquare thêm page/phạm vi (scope / 범위), WFrame, DataCollection, Submission, GridView và
thời gian chạy (runtime / 런타임)/hiện vật bản dựng (build artifact / 빌드 산출물) đặc tả hợp đồng (contract / 계약) trên nền HTML/JavaScript/XML. phạm vi (scope / 범위) destroy,
submission thứ tự (ordering / 순서), grid định danh (identity / 식별자) và engine phiên bản (version / 버전) có thể tạo thất bại (failure / 실패) riêng;
không gộp chúng với trình duyệt (browser / 브라우저) vòng đời (lifecycle / 생명주기). XML nguồn (source / 소스), thời gian chạy (runtime / 런타임) engine và W-Pack
sản phẩm tạo ra (artifact / 산출물) cần được dấu vết (trace / 추적) như ba định danh (identity / 식별자) khác nhau.


> **Chuyển mạch:** Từ **WebSquare**, ta sang **khung phần mềm (framework / 프레임워크) placement checklist** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Khung phần mềm (framework / 프레임워크) placement checklist

Mỗi chapter khung phần mềm (framework / 프레임워크) nên chỉ rõ:

1. trình duyệt (browser / 브라우저) thành phần nguyên thủy (primitive / 기본 요소) và bản địa (native / 네이티브) ngữ nghĩa (semantics / 의미론) đang được dùng;
2. lớp trừu tượng (abstraction / 추상화) nào sở hữu trạng thái (state / 상태), subscription, cleanup, lỗi (error / 오류) và scheduling;
3. bất biến (invariant / 불변식) nào được kiểm tra bằng kiểm thử (test / 테스트), khả năng tiếp cận (accessibility / 접근성) check, profile,
   telemetry và deployed-artifact bằng chứng (evidence / 증거).

Đọc tiếp [React index](../react/00_index.md) hoặc [WebSquare index](../websquare/README.md);
không dùng khung phần mềm (framework / 프레임워크) README để thay thế cốt lõi (core / 핵심) nền tảng (platform / 플랫폼) mô hình tư duy (mental model / 사고 모델).

> **Bàn giao:** Sau **khung phần mềm (framework / 프레임워크) placement checklist**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 web platform model](./00_web_platform_model.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
