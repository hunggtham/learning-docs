# Tâm lý học học tập và thiết kế thói quen

Học hiệu quả không chỉ là đưa thông tin vào đầu. Một hệ thống học tốt phải giải quyết ít nhất bốn bài toán: mã hóa (encoding), lưu giữ (retention), truy hồi (retrieval) và chuyển giao (transfer). Nếu chỉ đọc lại nhiều lần, người học có thể tăng cảm giác quen thuộc mà không tăng đáng kể khả năng tự truy hồi khi cần.

## Retrieval practice

Luyện truy hồi (retrieval practice) là cố gắng lấy thông tin từ trí nhớ thay vì chỉ xem lại. Ví dụ, sau khi học một concept, đóng tài liệu và tự trả lời: “concept này giải quyết vấn đề gì?”, “mechanism là gì?”, “khi nào không áp dụng được?”.

Retrieval có hai vai trò: đo xem mình thực sự biết gì và làm memory trace dễ truy cập hơn. Điều quan trọng là retrieval cần feedback; nếu người học nhớ sai mà không sửa, lỗi có thể được củng cố.

## Spacing

Lặp lại cách quãng (spacing) phân phối các lần học theo thời gian. Việc phải “khôi phục” memory sau một khoảng quên vừa phải tạo effort có ích hơn việc lặp ngay khi thông tin còn rất tươi.

Spacing không có một lịch duy nhất tối ưu cho mọi nội dung. Khoảng cách phụ thuộc độ khó, thời gian đến kỳ thi và mức retention cần giữ.

## Interleaving

Xen kẽ (interleaving) trộn các dạng bài hoặc concept gần nhau để buộc người học phân biệt khi nào dùng phương pháp nào. Nó thường khó chịu hơn blocked practice vì performance tức thời có thể thấp hơn, nhưng chính việc phải chọn strategy có thể hỗ trợ transfer.

## Elaborative explanation

Giải thích bằng lời của mình giúp nối kiến thức mới với prior knowledge. Nhưng “giải thích dài” không đồng nghĩa “hiểu sâu”. Một explanation tốt cần trả lời causal/mechanistic question, không chỉ đổi từ của definition.

Ví dụ khi học database index, thay vì ghi “index giúp truy vấn nhanh hơn”, hãy giải thích cấu trúc nào được tạo, lookup path thay đổi ra sao, chi phí write tăng thế nào và khi nào full scan vẫn hợp lý.

## Illusion of competence

Cảm giác quen (familiarity) rất dễ bị nhầm với mastery. Highlight, reread và xem solution tạo cảm giác “mình biết”, nhưng recognition task dễ hơn recall/generation task.

Một test đơn giản: nếu bỏ tài liệu đi, bạn có thể tự dựng lại cấu trúc hay giải một problem mới không?

## Transfer

Chuyển giao (transfer) là khả năng dùng kiến thức trong context mới. Transfer khó vì người học thường mã hóa kiến thức gắn chặt với surface features của ví dụ ban đầu.

Để tăng transfer, nên:

- học nhiều ví dụ có cấu trúc sâu giống nhau nhưng bề mặt khác nhau;
- so sánh hai case để tìm invariant;
- giải thích vì sao một strategy áp dụng được;
- luyện chọn strategy, không chỉ thực thi strategy đã được chỉ sẵn.

## Habit: cue, response và reward

Thói quen (habit) hình thành khi một behavior được lặp trong context tương đối ổn định đến mức cue bắt đầu kích hoạt response với ít deliberation hơn.

Mental model đơn giản:

```text
Cue / context
     ↓
Response
     ↓
Outcome / reward
     ↓
Association mạnh dần qua lặp lại
```

Điều này giải thích tại sao chỉ đặt goal “tôi sẽ học mỗi tối” thường yếu. Một plan tốt xác định cue: “sau khi rửa bát lúc 21:00, tôi mở bàn học và làm 10 phút retrieval trước”.

## Implementation intention

Ý định thực thi (implementation intention) có dạng:

```text
Nếu X xảy ra → tôi sẽ làm Y.
```

Nó giảm số decision cần thực hiện tại thời điểm hành động. Ví dụ: “Nếu tôi muốn nằm xuống sau khi về nhà, tôi sẽ tắm trước và ngồi ở bàn 10 phút rồi mới quyết định có nghỉ hay không.”

## Environment design

Self-control hiệu quả thường xảy ra trước temptation. Nếu điện thoại nằm ngay cạnh bàn, mỗi notification tạo attentional capture và switching cost. Environment design có thể giảm số lần phải dùng inhibition.

Các intervention nhỏ:

- đặt phone ngoài tầm tay;
- chặn notification không cần thiết;
- chuẩn bị tài liệu từ trước;
- mở sẵn task đầu tiên;
- dùng website blocker cho time block cụ thể.

## Motivation và action

Motivation không phải nhiên liệu ổn định. Nếu một system chỉ hoạt động khi “có hứng”, nó dễ đổ vỡ.

Phân biệt:

- **motivation problem**: biết phải làm gì nhưng reward quá xa;
- **clarity problem**: task mơ hồ;
- **skill problem**: chưa biết cách làm;
- **capacity problem**: quá mệt, thiếu ngủ, overload;
- **avoidance problem**: task gắn với fear/shame.

Mỗi cơ chế cần intervention khác nhau.

## Thiết kế session học

Một session có thể theo flow:

```text
1. Recall kiến thức cũ không nhìn tài liệu
2. Học concept mới theo causal structure
3. Làm ví dụ có feedback
4. Làm một problem biến thể
5. Ghi câu hỏi chưa giải quyết
6. Lên lịch retrieval tiếp theo
```

## Ứng dụng với lập trình

Trong programming, đọc code không đủ. Durable learning cần generation và debugging.

Ví dụ khi học Java Stream:

- tự viết pipeline từ yêu cầu;
- dự đoán output trước khi chạy;
- giải thích laziness;
- so sánh `map`, `flatMap`, `filter`, `reduce`;
- tạo edge case;
- debug một pipeline sai.

Đó là retrieval + discrimination + transfer.

## Common misconceptions

**“Học nhiều giờ = học tốt.”** Thời lượng không nói lên cognitive operation đang diễn ra.

**“Quên nghĩa là học thất bại.”** Một mức forgetting trước retrieval có thể tạo desirable difficulty.

**“Habit cần 21 ngày.”** Không có một con số cố định cho mọi behavior và context.

**“Kỷ luật mạnh thì không cần thiết kế môi trường.”** Ngược lại, environment design thường làm self-control rẻ hơn.

## Knowledge connections

Xem thêm [[../02_learning_and_cognition/01_memory]], [[../02_learning_and_cognition/09_learning_transfer_forgetting_and_durable_knowledge]], [[../02_learning_and_cognition/04_cognitive_biases_and_metacognition]], [[../03_human_development_and_person/02_motivation_and_emotion]] và [[../03_human_development_and_person/09_self_concept_identity_and_self_regulation]].