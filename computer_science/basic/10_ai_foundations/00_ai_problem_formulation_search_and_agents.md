# Mô hình hóa bài toán AI, tìm kiếm và tác tử

> **Mạch đọc:** Đọc **Mô hình hóa bài toán AI, tìm kiếm và tác tử** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Mô hình tác tử** sang **Tìm kiếm trong không gian trạng thái**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


**Trí tuệ nhân tạo (Artificial Intelligence — AI / 인공지능)** rộng hơn học máy. Một cách nhìn nền tảng là xây dựng **tác tử (agent)** nhận quan sát từ môi trường, duy trì hoặc ước lượng trạng thái rồi chọn hành động để đạt mục tiêu trong điều kiện có bất định và giới hạn tài nguyên.

## Mô hình tác tử

Tác tử nhận **cảm nhận (percept)** từ môi trường và tạo hành động. **Tác tử hợp lý (rational agent)** chọn hành động được kỳ vọng đáp ứng tốt nhất thước đo hiệu quả dựa trên thông tin hiện có; điều này không đồng nghĩa với “thông minh giống con người”.

Môi trường có thể quan sát đầy đủ hoặc một phần, xác định hoặc ngẫu nhiên, theo từng phiên độc lập hoặc theo chuỗi, tĩnh hoặc động, rời rạc hoặc liên tục. Những đặc tính này ảnh hưởng trực tiếp đến họ thuật toán phù hợp.


> **Chuyển mạch:** Từ **Mô hình tác tử**, ta sang **Tìm kiếm trong không gian trạng thái** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Tìm kiếm trong không gian trạng thái

Nhiều bài toán AI có thể biểu diễn bằng trạng thái, hành động, mô hình chuyển trạng thái, trạng thái ban đầu và điều kiện mục tiêu.

Lập đường đi, giải câu đố, lập kế hoạch và tìm kiếm trong trò chơi đều có thể trở thành bài toán tìm kiếm đồ thị trên một **không gian trạng thái (state space)** thường không được tạo sẵn toàn bộ.

BFS tìm đường ngắn nhất theo số cạnh khi chi phí các cạnh bằng nhau; Dijkstra xử lý chi phí không âm; A* dùng **hàm heuristic** để hướng quá trình tìm kiếm về phía mục tiêu.


> **Chuyển mạch:** Từ **Tìm kiếm trong không gian trạng thái**, ta sang **Heuristic** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Heuristic

Heuristic `h(n)` ước lượng chi phí còn lại từ nút `n` tới mục tiêu. A* sử dụng:

\[
f(n)=g(n)+h(n)
\]

trong đó `g(n)` là chi phí đã đi từ điểm đầu tới `n`.

Nếu heuristic **chấp nhận được (admissible)**, tức không đánh giá cao hơn chi phí còn lại thực sự, A* có thể bảo đảm nghiệm tối ưu dưới các giả định phù hợp. Tính nhất quán (consistency) của heuristic giúp việc tìm kiếm trên đồ thị hoạt động ổn định hơn.

Heuristic tốt mã hóa kiến thức miền và giúp giảm số trạng thái phải khám phá.


> **Chuyển mạch:** Từ **Heuristic**, ta sang **Bùng nổ không gian tìm kiếm** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Bùng nổ không gian tìm kiếm

Nếu hệ số phân nhánh là `b` và độ sâu là `d`, số trạng thái có thể tăng gần `b^d`. Đây là **bùng nổ tổ hợp (combinatorial explosion)**; với BFS hoặc A*, bộ nhớ thường trở thành nút thắt trước cả CPU.

Vì vậy tìm kiếm trong AI liên hệ trực tiếp với lý thuyết độ phức tạp, thuật toán xấp xỉ và heuristic.


> **Chuyển mạch:** Từ **Bùng nổ không gian tìm kiếm**, ta sang **Tìm kiếm đối kháng** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Tìm kiếm đối kháng

Trò chơi hai người tổng bằng không có thể dùng **minimax**: một bên cố tối đa hóa giá trị, bên còn lại cố tối thiểu hóa. **Cắt tỉa alpha-beta (alpha-beta pruning)** loại những nhánh không thể ảnh hưởng đến quyết định cuối cùng.

Thứ tự xét nước đi tốt có thể làm cắt tỉa hiệu quả hơn nhưng không thay đổi kết quả minimax. Với trò chơi có không gian quá lớn, hệ thống còn cần hàm đánh giá heuristic, giới hạn độ sâu, Monte Carlo cây (tree / 트리) tìm kiếm (search / 검색) hoặc chính sách/hàm giá trị được học.


> **Chuyển mạch:** Từ **Tìm kiếm đối kháng**, ta sang **Lập kế hoạch** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Lập kế hoạch

**Lập kế hoạch (planning)** khác tìm đường đơn giản khi hành động có điều kiện tiên quyết và hiệu ứng, còn mục tiêu có thể là tập điều kiện lô-gic (logic / 논리). Lập kế hoạch cổ điển có thể tìm kiếm trong không gian trạng thái hoặc không gian kế hoạch.

Robot và bài toán thế giới thực bổ sung bất định, trạng thái/hành động liên tục và khả năng quan sát không đầy đủ.


> **Chuyển mạch:** Từ **Lập kế hoạch**, ta sang **Độ hữu dụng và bất định** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Độ hữu dụng và bất định

Khi kết quả mang tính ngẫu nhiên, câu hỏi “có đạt mục tiêu hay không” thường quá đơn giản. **Độ hữu dụng kỳ vọng (expected utility)** kết hợp xác suất với mức ưu tiên, lợi ích hoặc chi phí. Lý thuyết quyết định nối suy luận xác suất với lựa chọn hành động.


> **Chuyển mạch:** Từ **Độ hữu dụng và bất định**, ta sang **Liên hệ với học tăng cường** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Liên hệ với học tăng cường

**Học tăng cường (Reinforcement Learning — RL)** xem tác tử tương tác với môi trường và học **chính sách (policy / 정책)** từ phần thưởng thay vì được cung cấp đầy đủ mô hình chuyển trạng thái. Các khái niệm trạng thái, hành động, phần thưởng và chính sách vẫn sử dụng cùng mô hình tác tử.

Học máy và RL có thể được đào sâu trong thư viện riêng; ở đây trọng tâm là cầu nối khái niệm.


> **Chuyển mạch:** Từ **Liên hệ với học tăng cường**, ta sang **Những hiểu lầm thường gặp** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Những hiểu lầm thường gặp

**“AI = mạng nơ-ron.”** Tìm kiếm, lô-gic (logic / 논리), lập kế hoạch, suy luận xác suất và tối ưu hóa đều là nền tảng quan trọng của AI.

**“Heuristic chỉ là mẹo không có lý thuyết.”** Nhiều thuật toán tìm kiếm heuristic có bảo đảm hình thức khi heuristic thỏa các thuộc tính nhất định.

**“Tác tử hợp lý luôn tạo kết quả tốt nhất trong thực tế.”** Nó chỉ chọn hành động tốt nhất theo mô hình, thông tin và mục tiêu hiện có; bất định hoặc mô hình sai vẫn có thể dẫn tới kết quả xấu.


> **Chuyển mạch:** Từ **Những hiểu lầm thường gặp**, ta sang **Mô hình tư duy** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy

> AI bắt đầu bằng việc hình thức hóa chuỗi **cảm nhận → trạng thái hoặc niềm tin → hành động → mục tiêu**. Thuật toán chỉ có ý nghĩa sau khi cách biểu diễn bài toán đã rõ.


> **Chuyển mạch:** Từ **Mô hình tư duy**, ta sang **Kết nối** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Kết nối

Xem [thuật toán đồ thị](../01_algorithms_data_structures/06_graphs_and_graph_algorithms.md), [độ phức tạp](../01_algorithms_data_structures/11_complexity_reductions_and_np.md), [xác suất](../../../mathematics/06_probability_statistics/01_probability_foundations.md) và [nền tảng học máy](./02_machine_learning_foundations.md).

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 knowledge reasoning and probabilistic inference](./01_knowledge_reasoning_and_probabilistic_inference.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
