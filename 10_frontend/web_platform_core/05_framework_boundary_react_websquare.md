# Framework boundary: React và WebSquare

Framework giúp tổ chức application state và rendering, nhưng không phải một
browser mới. Khi framework behavior khó hiểu, quay về ba câu hỏi: primitive
nào của browser đang được dùng; framework sở hữu identity/lifecycle/scheduling
nào; application contract nào cần test và telemetry.

## React

React quản lý component identity, render/reconciliation, state, Effects,
concurrency và các server/client boundary. Nó vẫn render DOM, dùng CSS, nhận
native events và chịu hydration/parser constraints. Debug nên kiểm tra DOM,
CSS, network và event timeline trước khi kết luận reconciliation là nguyên nhân.

## WebSquare

WebSquare thêm page/scope, WFrame, DataCollection, Submission, GridView và
runtime/build artifact contract trên nền HTML/JavaScript/XML. Scope destroy,
submission ordering, grid identity và engine version có thể tạo failure riêng;
không gộp chúng với browser lifecycle. XML source, runtime engine và W-Pack
artifact cần được trace như ba identity khác nhau.

## Framework placement checklist

Mỗi chapter framework nên chỉ rõ:

1. browser primitive và native semantics đang được dùng;
2. abstraction nào sở hữu state, subscription, cleanup, error và scheduling;
3. invariant nào được kiểm tra bằng test, accessibility check, profile,
   telemetry và deployed-artifact evidence.

Đọc tiếp [React index](../react/00_index.md) hoặc [WebSquare index](../websquare/README.md);
không dùng framework README để thay thế core platform mental model.
