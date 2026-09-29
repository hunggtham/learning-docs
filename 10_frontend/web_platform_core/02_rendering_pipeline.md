# Rendering chuỗi xử lý (pipeline / 파이프라인): parser đến pixels

> **Mạch đọc:** Đặt **Rendering chuỗi xử lý (pipeline / 파이프라인): parser đến pixels** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Các ranh giới (boundary / 경계) chính** sang **vô hiệu hóa (invalidation / 무효화) và bằng chứng (evidence / 증거)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Rendering là quá trình biến tài nguyên (resource / 자원) và trạng thái (state / 상태) thành đầu ra (output / 출력) quan sát được. DOM
không phải rendering cây (tree / 트리), và khung phần mềm (framework / 프레임워크) thành phần (component / 컴포넌트) cây (tree / 트리) cũng không phải DOM.
Tách các cây (tree / 트리) này giúp tránh giải thích mọi vấn đề bằng “re-render”.

## Các ranh giới (boundary / 경계) chính

1. HTML parser tạo DOM và có thể sửa nguồn (source / 소스) markup theo parsing rules.
2. CSS parser tạo CSSOM; cascade tính specified/computed/used values.
3. trình duyệt (browser / 브라우저) hợp nhất DOM/CSSOM thành style và formatting/bố cục (layout / 레이아웃) trạng thái (state / 상태).
4. bố cục (layout / 레이아웃) tính hình học (geometry / 기하학); paint tạo display items; composite ghép layers thành
   frame. Một thay đổi có thể chỉ invalid paint hoặc lan ngược tới bố cục (layout / 레이아웃).

DOM cây (tree / 트리) có nút (node / 노드) không vẽ, còn pseudo-element hoặc anonymous box có thể xuất
   hiện trong formatting/paint mô hình (model / 모델). Vì vậy `querySelector`, cây khả năng tiếp cận (accessibility tree / 접근성 트리), bố cục (layout / 레이아웃) box và compositor tầng (layer / 계층) là các quan sát khác nhau.


> **Chuyển mạch:** Từ **Các ranh giới (boundary / 경계) chính**, ta sang **vô hiệu hóa (invalidation / 무효화) và bằng chứng (evidence / 증거)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Vô hiệu hóa (invalidation / 무효화) và bằng chứng (evidence / 증거)

Script đọc bố cục (layout / 레이아웃) sau khi mutate style có thể ép synchronous bố cục (layout / 레이아웃). Large DOM,
định cỡ nội tại (intrinsic sizing / 내재 크기 결정), font swap, selector matching và repeated đo lường (measurement / 측정) có thể
đẩy chi phí (cost / 비용) lên theo số nút (node / 노드) hoặc số lần kết xuất (render / 렌더링). `transform`/`opacity` thường giúp
tránh bố cục (layout / 레이아웃) nhưng không làm mất bộ nhớ (memory / 메모리), raster, upload hoặc compositor chi phí (cost / 비용).

Kết luận phải dựa trên DevTools dấu vết (trace / 추적), Long tác vụ (task / 작업), bố cục (layout / 레이아웃)/paint timing, bộ nhớ (memory / 메모리)
và mạng (network / 네트워크) bằng chứng (evidence / 증거). Screenshot chỉ chứng minh kết quả hình ảnh, không chứng
minh nhân quả (causal / 인과적) chi phí (cost / 비용). Xem [CSS track](../css/CSS_Beginner_to_Senior_2026.md) cho
cascade/bố cục (layout / 레이아웃) detail và [JavaScript performance](../javascript/javascript_senior.md)
cho thời gian chạy (runtime / 런타임) profiling.


> **Chuyển mạch:** Từ **vô hiệu hóa (invalidation / 무효화) và bằng chứng (evidence / 증거)**, ta sang **SSR, hydration và khung phần mềm (framework / 프레임워크)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## SSR, hydration và khung phần mềm (framework / 프레임워크)

SSR tạo HTML trước; hydration gắn hành vi thời gian chạy (runtime behavior / 런타임 동작) vào markup đã có. Parser,
DOM repair, nondeterministic dữ liệu (data / 데이터) hoặc khác biệt môi trường (environment / 환경) có thể làm markup
không khớp. React reconciliation và WebSquare rendering có vòng đời (lifecycle / 생명주기) riêng,
nhưng cuối cùng vẫn bị ràng buộc bởi DOM, CSS và trình duyệt (browser / 브라우저) scheduling.

> **Bàn giao:** Sau **SSR, hydration và khung phần mềm (framework / 프레임워크)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 web platform model](./00_web_platform_model.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
