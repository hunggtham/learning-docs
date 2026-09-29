# COMMON PROMPT — Learning Docs

Áp dụng file này làm yêu cầu nền cho toàn bộ tài liệu học và mọi thay đổi nội dung trong repository.

## Nguyên tắc chung
Phần này là hợp đồng nền cho mọi prompt sinh tài liệu: trước khi viết chi tiết, hãy xác định người học, câu hỏi trung tâm và mối nối với phần trước.

- Luôn kiểm tra cấu trúc hiện tại, README, canonical files và internal links trước khi tạo hoặc sửa nội dung.
- Viết như một giảng viên đang dẫn người học đi qua một bài học hoàn chỉnh, không như báo cáo AI, danh sách ghi chú hoặc tập hợp các đoạn độc lập.
- Mỗi đơn vị giải thích phải có mạch nối hai đầu: phần đầu định vị người học dựa trên kiến thức nào, vì sao cần học và câu hỏi nào sẽ được giải quyết; phần cuối chốt điều vừa hình thành, nêu ranh giới hoặc điểm dễ nhầm và bàn giao rõ sang mục kế tiếp, mục liên quan hoặc owner canonical.
- Các section liền kề phải tạo thành một chuỗi suy luận: section trước mở ra nhu cầu/câu hỏi cho section sau, section sau nhắc lại điểm tựa vừa dùng. Câu nối phải nói quan hệ thật như phụ thuộc, mở rộng, đối chiếu, nguyên nhân–hệ quả hoặc ứng dụng; không dùng câu “xem tiếp” rỗng.
- Trong phần thân, đi theo logic phù hợp nội dung: đối tượng/mục tiêu → cơ chế hoặc ràng buộc → hệ quả → ví dụ/evidence hoặc bẫy dễ nhầm khi có căn cứ.
- Không được trả về một section chỉ có định nghĩa, bullet, bảng hoặc ví dụ mà thiếu câu giải thích và câu kết. Nếu section rất ngắn, gộp mạch mở–giải thích–chốt trong một đoạn tự nhiên thay vì bỏ qua các chức năng đó.
- Không coi việc chèn một câu chung trước và sau header là đã đạt contract. Phải viết lại mạch prose quanh nội dung thật của topic: câu mở phải nêu câu hỏi cụ thể, phần thân phải giải thích các bullet/bảng/công thức như bằng chứng, và câu chốt phải rút ra quan hệ hoặc ranh giới thật của topic.
- Nếu nội dung nguồn là danh sách, bảng hoặc công thức, luôn có prose dẫn vào để người mới biết cần đọc danh sách đó theo tiêu chí nào, và prose tổng hợp sau đó để biết các ý liên kết thành kết luận gì. Không để header rơi thẳng xuống bullet/bảng mà không có giải thích.
- Không bắt buộc dùng đúng các nhãn “Mục tiêu”, “Giải thích”, “Kết luận”; đây là contract về mạch reasoning, không phải template hình thức. Tuy vậy, nội dung tương ứng phải hiện diện trong prose của mọi section giảng dạy.
- Không rải cùng một boilerplate cho mọi topic. Giữ các liên kết đã có ý nghĩa và bổ sung đúng chỗ thiếu bằng thuật ngữ, quan hệ và phạm vi thật của topic.
- Giải thích theo luồng từ nền tảng đến nâng cao, đủ sâu để hiểu bản chất; ưu tiên understanding, reasoning, mechanism, first principles và connection giữa các concept hơn ghi nhớ máy móc.
- Nội dung phải liền mạch, tự nhiên, đủ ngữ cảnh; hạn chế bullet/table khi chúng làm đứt luồng đọc.
- Với thuật ngữ quan trọng, giữ hoặc note thuật ngữ tiếng Anh; khi phù hợp với ngữ cảnh Hàn Quốc, note thêm thuật ngữ tiếng Hàn và giải thích ngay tại chỗ.
- Ví dụ chỉ thêm khi giúp hiểu rõ hơn, phải đúng bản chất và không làm lệch nội dung chuyên môn.
- Có thể chia nhỏ, gộp hoặc tổ chức lại file/topic nếu giúp việc học và điều hướng tốt hơn, nhưng không làm mất nội dung cần thiết.
- Tôn trọng cấu trúc, naming, liên kết và style chung của repository; tránh duplicate content và file cô lập.
- Không cá nhân hóa nội dung học trừ khi được yêu cầu rõ ràng.

## Mạch học bắt buộc khi viết và review

Mỗi file/chapter là một đường đi có chủ đích. Khi mở đầu một mục lớn, phải trả lời ngắn gọn: người học cần biết gì trước, mục này giải quyết câu hỏi nào, và kết quả sẽ được dùng ở đâu. Khi kết thúc mục, phải trả lời: ta vừa có mental model/invariant nào, nó giới hạn ở đâu, và mục sau sẽ dùng, mở rộng hoặc đối chiếu nó như thế nào.

Với chuỗi section, áp dụng nhịp sau bằng ngôn ngữ tự nhiên của domain:

1. **Định vị:** nối mục hiện tại với prerequisite hoặc câu hỏi được mở ra từ mục trước.
2. **Giải thích:** đi từ object/goal → mechanism/constraint → consequence → example hoặc evidence khi cần.
3. **Bàn giao:** chốt insight, nêu boundary hoặc cặp dễ nhầm, rồi dẫn sang section/owner tiếp theo bằng tên cụ thể nếu biết.

Mỗi header chỉ là nhãn điều hướng; không được giải thích header như một khái niệm độc lập nếu phần bên dưới đang dạy một chuỗi khái niệm. Hãy đọc toàn bộ khối dưới header để xác định một câu hỏi chung, các bước suy luận và kết luận. Một lesson hoàn chỉnh phải giống một buổi giảng ngắn cho người mới: bối cảnh → câu hỏi → giải thích có liên kết → ví dụ/evidence → chốt → lý do chuyển tiếp.

Glossary, index, checklist và bảng tra cứu thuần tham chiếu có thể ngắn hơn, nhưng vẫn phải nói rõ cách dùng, owner của khái niệm và đường quay lại phần giảng giải; không được dùng ngoại lệ này cho section đang dạy kiến thức.

## Câu liên kết bắt buộc giữa các phần

Câu liên kết phải giúp người mới hiểu hướng suy luận, không chỉ báo rằng tài liệu đang chuyển sang header khác. Vì vậy, mỗi section giảng dạy phải có đủ ba mối nối sau:

1. **Mối nối đi vào:** nhắc đúng khái niệm, điều kiện hoặc câu hỏi từ phần trước (nếu có), rồi nói section hiện tại dùng điểm tựa đó để giải quyết câu hỏi nào.
2. **Mối nối trong section:** giải thích vì sao các định nghĩa, bullet, bảng, công thức hoặc ví dụ được đặt cạnh nhau; phải chỉ ra quan hệ như kế thừa, mở rộng, đối chiếu, áp dụng hoặc nguyên nhân–hệ quả.
3. **Mối nối đi ra:** chốt insight và boundary của section, rồi nói rõ kết luận đó sẽ được dùng, mở rộng hoặc kiểm tra ở section/chunk/owner nào tiếp theo.

Có thể dùng các khung câu sau rồi thay bằng thuật ngữ thật của topic:

- “Từ **[điểm tựa ở phần trước]**, ta có tiêu chí **[X]**; phần này dùng tiêu chí đó để giải quyết **[câu hỏi cụ thể]**.”
- “Các ý dưới đây không phải danh sách rời: hãy đọc chúng theo **[tiêu chí/quan hệ]**, vì điều đó giải thích **[hệ quả hoặc điểm phân biệt]**.”
- “Điểm chốt là **[invariant/mental model]**; vì **[ranh giới hoặc ngoại lệ]**, phần tiếp theo cần xem **[tên hoặc nhu cầu cụ thể]**.”

Không dùng riêng các câu “tiếp theo”, “xem tiếp”, “như trên”, “phần này trình bày…” nếu chúng không nêu khái niệm trước, câu hỏi hiện tại hoặc nhu cầu kế tiếp. Không bịa quan hệ chỉ để đủ mẫu; nếu SOURCE không cho biết section kế tiếp, hãy bàn giao theo nhu cầu học tập được chứng minh trong chính section đó và đánh dấu phần chưa chắc chắn khi cần. Khi review, phải đọc câu nối cùng đoạn nội dung mà nó nối: một câu chung chung đặt trước header không được tính là liên kết.

Khi retrofit tài liệu cũ, ưu tiên các điểm gãy: mở đầu nhảy thẳng vào chi tiết mà không có prerequisite; section kết thúc đột ngột; concept được nhắc lại nhưng không chỉ ra quan hệ; link chỉ tồn tại ở mục lục mà không có lý do học tập để đi theo link. Với output generate, sửa source hoặc generator rồi regenerate thay vì sửa tay từng file.

## Branch & Git workflow
Phần này chuyển hợp đồng nội dung thành quy trình cập nhật an toàn, để việc tái sinh và kiểm tra tài liệu không làm mất thay đổi liên quan.

- `main` là trạng thái ổn định và canonical.
- Thay đổi lớn hoặc theo từng topic nên thực hiện trên branch riêng; kiểm tra nội dung, links và lỗi trước khi merge.
- Không giữ branch/commit dư thừa; sau khi merge, dọn các branch không còn cần thiết và giữ cấu trúc branch tối giản, rõ mục đích.

## Quy tắc kế thừa

Mọi prompt chuyên môn và yêu cầu mới mặc định kế thừa contract này. Prompt chuyên môn chỉ được bổ sung hoặc siết chặt phạm vi; không được làm yếu yêu cầu về mạch mở đầu–giải thích–kết thúc–bàn giao.
