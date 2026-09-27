# Web Platform: model, boundaries và invariant

Web Platform không chỉ là tập API của browser. Nó là hợp đồng giữa resource
được tải, parser tạo ra tree, runtime thực thi script, renderer tạo ra pixels,
input tạo ra events và security model giới hạn dữ liệu nào được phép đi qua
boundary nào.

## Từ resource đến behavior

Một màn hình thật thường có chuỗi causal như sau:

```text
URL/navigation
→ response và resource graph
→ HTML/CSS parse
→ DOM/CSSOM + style state
→ layout/paint/composite
→ input/event
→ JavaScript và async work
→ state/data update
→ render invalidation
```

Đây là graph có thể quay lại, không phải danh sách bước tuyến tính. Font load,
resize, stylesheet mới, network response hoặc state update có thể invalid một
phần tree và kích hoạt lại work. Vì vậy câu hỏi debug tốt là “boundary nào
đổi state và evidence nào chứng minh nó?” thay vì chỉ hỏi “component nào lỗi?”.

## Ba lớp cần tách

**Primitive của platform** gồm HTML semantics, DOM identity, CSS cascade,
event dispatch, URL/fetch, storage, timers, accessibility tree và origin
policy. **Framework semantics** thêm component/page identity, lifecycle,
subscription, scheduling và rendering abstraction. **Application contract**
định nghĩa business state, server authorization, error meaning và release
artifact. Một framework không thể biến dữ liệu không đáng tin thành trusted data
chỉ bằng type hoặc component boundary.

## Invariant cấp domain

- Mỗi resource, request, DOM node, component/page instance và async operation
  có identity và lifetime rõ ràng.
- State có một source of truth; derived view, cache và optimistic projection
  không được âm thầm trở thành canonical state.
- Kết quả cũ không được ghi đè intent mới; cancellation hoặc generation check
  phải bảo vệ stale response.
- Semantics, keyboard/focus và accessible name là behavior công khai, không
  phải polish chỉ kiểm tra khi gần release.
- Dữ liệu từ URL, DOM, storage, message, iframe, WebView bridge và backend đều
  phải có trust boundary trước khi đi vào sink hoặc side effect.
- Performance claim phải có trace/metric/profile; không suy ra từ một CSS
  property hoặc cảm giác “nhanh hơn”.

Các chapter tiếp theo triển khai những invariant này ở runtime, renderer,
interaction/network và production constraints.
