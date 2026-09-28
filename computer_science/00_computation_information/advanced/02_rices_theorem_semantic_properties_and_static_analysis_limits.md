# Định lý Rice, thuộc tính ngữ nghĩa và giới hạn của phân tích tĩnh

> **Mạch đọc:** Đặt **Định lý Rice, thuộc tính ngữ nghĩa và giới hạn của phân tích tĩnh** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Cú pháp và ngữ nghĩa** sang **Định lý Rice**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Lập trình viên thường muốn công cụ trả lời các câu như “chương trình này có bao giờ crash không?”, “hàm này có luôn trả kết quả đúng không?” hoặc “đoạn mã này có thể làm lộ secret không?”. **Phân tích tĩnh (static analysis)** có thể trả lời nhiều câu hữu ích, nhưng với chương trình tổng quát tồn tại giới hạn lý thuyết sâu hơn vấn đề hiệu năng của công cụ.

## Cú pháp và ngữ nghĩa

**Thuộc tính cú pháp (syntactic property)** nhìn vào hình dạng chương trình: có dùng API X không, AST có mẫu Y không. **Thuộc tính ngữ nghĩa (semantic property)** nói về hành vi mà chương trình thực hiện: có kết thúc không, có thể trả một giá trị cụ thể không, hai chương trình có tính cùng một hàm hay không.

Suy luận ngữ nghĩa mạnh hơn nhưng cũng khó hơn vì có thể phải xét quá trình thực thi không có giới hạn hữu hạn biết trước.


> **Chuyển mạch:** Từ **Cú pháp và ngữ nghĩa**, ta sang **Định lý Rice** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Định lý Rice

Trực giác của **định lý Rice (Rice's theorem)** là: mọi thuộc tính ngữ nghĩa không tầm thường của các hàm tính được từng phần đều không thể quyết định trong trường hợp tổng quát. “Không tầm thường” nghĩa là thuộc tính đúng với một số hàm tính được và sai với một số hàm khác.

Điều này không nói bộ phân tích vô dụng. Nó nói không thể có một thuật toán vừa luôn kết thúc vừa luôn trả lời chính xác cho mọi chương trình về mọi thuộc tính ngữ nghĩa thuộc loại đó.


> **Chuyển mạch:** Từ **Định lý Rice**, ta sang **Liên hệ với bài toán dừng** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Liên hệ với bài toán dừng

Nhiều chứng minh bất khả thi dùng **phép quy giảm (reduction)** từ bài toán dừng. Nếu tồn tại bộ phân tích hoàn hảo cho thuộc tính P, ta có thể xây một chương trình đặc biệt để dùng bộ phân tích đó quyết định bài toán dừng, mâu thuẫn với tính không quyết định được đã biết.

Reduction vì vậy là kỹ thuật chuyển giới hạn từ bài toán A sang B bằng lập luận “nếu giải được B thì cũng giải được A”.


> **Chuyển mạch:** Từ **Liên hệ với bài toán dừng**, ta sang **Tính âm thanh và tính đầy đủ** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Tính âm thanh và tính đầy đủ

Bộ phân tích tĩnh thường phải đánh đổi. Một bộ phân tích **không bỏ sót theo mô hình (sound)** cố không bỏ qua lỗi thuộc phạm vi đã mô hình hóa nhưng có thể báo dương tính giả. Một bộ phân tích **đầy đủ (complete)** trong một bối cảnh có thể tránh một số báo sai nhưng phải bỏ bớt trường hợp hoặc chỉ áp dụng cho ngôn ngữ bị giới hạn.

Công cụ bảo mật thường ưu tiên không bỏ sót ở thuộc tính quan trọng; lint trong IDE có thể ưu tiên tỷ lệ tín hiệu/nhiễu để lập trình viên không bỏ qua quá nhiều cảnh báo.


> **Chuyển mạch:** Từ **Tính âm thanh và tính đầy đủ**, ta sang **Diễn giải trừu tượng** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Diễn giải trừu tượng

**Diễn giải trừu tượng (abstract interpretation)** thay không gian trạng thái cụ thể có thể vô hạn bằng một miền trừu tượng nhỏ hơn rồi tính điểm cố định. Ví dụ thay mọi số nguyên bằng ba lớp `{âm, không, dương}`.

Trừu tượng hóa làm mất thông tin nhưng khiến bài toán phân tích trở nên khả thi. Dương tính giả thường xuất hiện vì nhiều trạng thái cụ thể khác nhau bị gộp thành cùng một trạng thái trừu tượng.


> **Chuyển mạch:** Từ **Diễn giải trừu tượng**, ta sang **Giới hạn sức biểu đạt để lấy lại khả năng quyết định** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Giới hạn sức biểu đạt để lấy lại khả năng quyết định

Giao thức hữu hạn trạng thái, kiểm tra mô hình có giới hạn, ngôn ngữ toàn phần hoặc ngôn ngữ truy vấn bị hạn chế có thể cung cấp bảo đảm mạnh hơn chính vì sức biểu đạt đã bị giới hạn.

Đây là nguyên lý lặp lại trong khoa học máy tính: mô hình yếu hơn đôi khi hữu ích hơn vì ta có thể chứng minh được nhiều điều hơn về nó.


> **Chuyển mạch:** Từ **Giới hạn sức biểu đạt để lấy lại khả năng quyết định**, ta sang **AI phân tích mã không xóa giới hạn lý thuyết** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## AI phân tích mã không xóa giới hạn lý thuyết

ML hoặc LLM có thể dự đoán lỗi dựa trên mẫu đã học, nhưng không biến một thuộc tính không quyết định được thành một chứng minh quyết định được. Dự đoán xác suất và bảo đảm hình thức là hai loại bằng chứng khác nhau.


> **Chuyển mạch:** Từ **AI phân tích mã không xóa giới hạn lý thuyết**, ta sang **Mô hình tư duy** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy

> Phân tích tĩnh luôn đứng giữa sức biểu đạt, độ chính xác và chi phí để bảo đảm kết thúc. Tính không quyết định được không bảo ta ngừng phân tích; nó buộc ta phải chọn rõ mức trừu tượng, phạm vi giới hạn và loại bảo đảm muốn có.

> **Bàn giao:** Sau **Mô hình tư duy**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 formal models reductions and computability](./00_formal_models_reductions_and_computability.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
