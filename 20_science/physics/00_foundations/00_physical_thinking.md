# Tư duy Vật lý và First-Principles Thinking

## Vật lý thực sự nghiên cứu điều gì?

Vật lý (Physics / 물리학) nghiên cứu những quy luật tổng quát chi phối vật chất, năng lượng, không gian, thời gian và tương tác. Câu này nghe rất rộng, nhưng điểm quan trọng không nằm ở danh sách đối tượng. Điều làm Vật lý khác biệt là cách nó đặt câu hỏi: ta cố tìm một tập nhỏ các đại lượng có thể đo, xây dựng quan hệ toán học giữa chúng, rồi dùng quan hệ đó để dự đoán hiện tượng mới.

Nếu một quả bóng rơi, ta có thể mô tả bằng màu sắc, chất liệu, cảm giác khi cầm, tiếng va xuống đất, hay lịch sử của người ném. Vật lý không phủ nhận các đặc điểm đó; nó chỉ hỏi đặc điểm nào cần thiết để trả lời một câu hỏi cụ thể. Nếu câu hỏi là “quả bóng chạm đất sau bao lâu?”, màu sắc gần như không quan trọng, còn chiều cao ban đầu, vận tốc ban đầu và trường hấp dẫn thì quan trọng. Việc bỏ qua những gì không cần thiết chính là bước xây dựng mô hình (Model / 모형, 모델).

### Mô hình không phải hiện thực

Mô hình là một biểu diễn có chủ đích của hiện thực. Khi nói “coi vật là chất điểm”, ta không bảo rằng vật không có kích thước. Ta đang tuyên bố rằng kích thước của nó không ảnh hưởng đáng kể đến câu hỏi hiện tại. Khi coi “mặt phẳng không ma sát”, ta không nói ma sát không tồn tại; ta đang tạm loại một tương tác để nhìn rõ cấu trúc chính.

Đây là lý do cùng một vật có thể cần nhiều mô hình. Một chiếc ô tô trong bài toán đường đi có thể là chất điểm; trong bài toán lật xe phải có kích thước và tâm khối; trong bài toán khí động học phải có hình dạng bề mặt; trong bài toán động cơ lại phải đi xuống cấp phân tử và nhiệt động lực học.

> Một cách tốt để hiểu Vật lý là: mọi phương trình đều là một “hợp đồng”. Nó hứa mô tả thế giới chính xác trong một miền điều kiện nhất định, đổi lại ta phải tôn trọng các giả định của nó.

## Định luật vật lý và quan hệ nhân quả

Định luật vật lý (Physical Law / 물리 법칙) là một mô tả có tính khái quát cao được kiểm chứng thực nghiệm trong miền áp dụng của nó. “Định luật” không có nghĩa là chân lý siêu hình không thể thay đổi. Định luật Newton cực kỳ chính xác ở vận tốc thấp so với tốc độ ánh sáng và ở thang lớn hơn nguyên tử, nhưng cần thuyết tương đối và cơ học lượng tử khi vượt khỏi miền đó.

Điểm này giúp tránh một ngộ nhận phổ biến: lý thuyết mới không nhất thiết “xóa” lý thuyết cũ. Thường nó chứa lý thuyết cũ như một trường hợp giới hạn. Cơ học Newton xuất hiện từ thuyết tương đối khi `v \ll c`; quang hình học xuất hiện từ quang sóng khi bước sóng nhỏ hơn nhiều so với kích thước hệ.

## Từ hiện tượng đến phương trình

Một quy trình tư duy vật lý điển hình có thể được hình dung như sau:

```mermaid
flowchart LR
    A[Hiện tượng] --> B[Câu hỏi đo được]
    B --> C[Chọn đại lượng]
    C --> D[Đặt giả định]
    D --> E[Xây mô hình]
    E --> F[Suy ra hệ quả toán học]
    F --> G[Thí nghiệm / dữ liệu]
    G --> H{Phù hợp?}
    H -- Có --> I[Mở rộng / dự đoán]
    H -- Không --> D
```

Bước “đặt giả định” rất quan trọng. Mỗi lần bỏ qua lực cản không khí, coi dây không dãn, coi khí lý tưởng, coi ánh sáng là tia, ta đang thay thế hệ thật bằng một hệ dễ phân tích hơn. Nếu kết quả sai, câu hỏi đầu tiên không nên là “tính toán sai ở đâu?” mà còn phải là “mô hình có còn phù hợp không?”.

## Cấp độ mô tả và emergence

Vật lý thường hoạt động ở nhiều thang. Một phân tử nước tuân theo cơ học lượng tử, nhưng dòng nước trong ống được mô tả tốt bằng cơ học chất lưu. Nhiệt độ không phải thuộc tính của một hạt đơn lẻ; nó xuất hiện như đại lượng vĩ mô của một ensemble rất lớn các hạt.

Hiện tượng một quy luật vĩ mô xuất hiện từ tương tác vi mô được gọi là emergence (Emergence / 창발). Khái niệm này cũng quan trọng trong Computer Science, AI và hệ phức tạp: behavior cấp hệ thống có thể không được viết trực tiếp trong từng thành phần riêng lẻ.

## Mental Model

Vật lý không bắt đầu từ công thức mà từ việc chọn một phần của hiện thực, xác định đại lượng có thể đo, xây dựng mô hình và hỏi mô hình dự đoán được điều gì. Một mô hình tốt không cần chứa mọi chi tiết; nó cần giữ đúng những cấu trúc chi phối câu hỏi đang xét.

## Common Misconceptions

“Mô hình đơn giản là mô hình sai” là cách hiểu thiếu chính xác. Mọi theory đều có miền áp dụng; lý tưởng hóa là cách cô lập cơ chế quan trọng, miễn là ta biết assumption nào đã được dùng và khi nào assumption đó hỏng.

## Knowledge Connection

**Liên hệ tiếp:** [Phép đo, đơn vị và sai số](01_measurement_units_uncertainty.md), [Đối xứng và bảo toàn](04_symmetry_conservation_scale.md).
