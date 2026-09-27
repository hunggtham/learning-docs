# Rendering pipeline: parser đến pixels

Rendering là quá trình biến resource và state thành output quan sát được. DOM
không phải rendering tree, và framework component tree cũng không phải DOM.
Tách các tree này giúp tránh giải thích mọi vấn đề bằng “re-render”.

## Các boundary chính

1. HTML parser tạo DOM và có thể sửa source markup theo parsing rules.
2. CSS parser tạo CSSOM; cascade tính specified/computed/used values.
3. Browser hợp nhất DOM/CSSOM thành style và formatting/layout state.
4. Layout tính geometry; paint tạo display items; composite ghép layers thành
   frame. Một thay đổi có thể chỉ invalid paint hoặc lan ngược tới layout.

DOM tree có node không vẽ, còn pseudo-element hoặc anonymous box có thể xuất
   hiện trong formatting/paint model. Vì vậy `querySelector`, accessibility
   tree, layout box và compositor layer là các quan sát khác nhau.

## Invalidation và evidence

Script đọc layout sau khi mutate style có thể ép synchronous layout. Large DOM,
intrinsic sizing, font swap, selector matching và repeated measurement có thể
đẩy cost lên theo số node hoặc số lần render. `transform`/`opacity` thường giúp
tránh layout nhưng không làm mất memory, raster, upload hoặc compositor cost.

Kết luận phải dựa trên DevTools trace, Long Task, layout/paint timing, memory
và network evidence. Screenshot chỉ chứng minh kết quả hình ảnh, không chứng
minh causal cost. Xem [CSS track](../css/CSS_Beginner_to_Senior_2026.md) cho
cascade/layout detail và [JavaScript performance](../javascript/javascript_senior.md)
cho runtime profiling.

## SSR, hydration và framework

SSR tạo HTML trước; hydration gắn runtime behavior vào markup đã có. Parser,
DOM repair, nondeterministic data hoặc khác biệt environment có thể làm markup
không khớp. React reconciliation và WebSquare rendering có lifecycle riêng,
nhưng cuối cùng vẫn bị ràng buộc bởi DOM, CSS và browser scheduling.
