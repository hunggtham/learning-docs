# COMMON PROMPT — Learning Docs

Áp dụng file này làm yêu cầu nền cho toàn bộ tài liệu và thay đổi tiếp theo trong repository.

## Nguyên tắc chung

- Luôn kiểm tra cấu trúc hiện tại, README, canonical files và internal links trước khi tạo hoặc sửa nội dung.
- Viết như một tài liệu học hoàn chỉnh để có thể đọc và hiểu trực tiếp, không phải note hoặc bản tóm tắt rời rạc.
- Giải thích theo luồng từ nền tảng đến nâng cao, đủ sâu để hiểu bản chất; không dừng ở giải thích ngắn, nửa chừng hoặc chỉ nêu kết luận.
- Ưu tiên understanding, reasoning, mechanism, first principles và connection giữa các concept hơn ghi nhớ máy móc.
- Mỗi đơn vị giải thích phải có **mạch nối hai đầu**: ở phần đầu, định vị mục này dựa trên kiến thức nào và vì sao cần học nó; ở phần cuối, chốt điều vừa hình thành và bàn giao rõ sang mục tiếp theo, mục liên quan hoặc owner canonical khác. Câu nối phải nói quan hệ học tập thực tế (phụ thuộc, mở rộng, đối chiếu, nguyên nhân–hệ quả hoặc ứng dụng), không chỉ viết “xem tiếp”.
- Các section liền kề phải được viết như một chuỗi suy luận: kết thúc section trước phải tạo câu hỏi hoặc nhu cầu cho section sau, còn section sau phải nhắc lại điểm tựa vừa dùng. Có thể dùng câu kiểu “từ đây…”, “để hiểu vì sao…”, “sau khi đã phân biệt…”, nhưng phải thay đổi theo nội dung và không được rải cùng một boilerplate cho mọi topic.
- Phần mở đầu của một chapter/topic cần chỉ ra prerequisite, phạm vi và câu hỏi trung tâm; phần kết thúc cần có recap ngắn, boundary/điểm dễ nhầm (nếu có) và một hướng đọc tiếp cụ thể. Khi section đứng độc lập về mặt tham chiếu, vẫn phải nói nó thuộc owner nào và được dùng trước/sau thao tác hoặc concept nào.
- Khi review tài liệu cũ, không chèn câu nối máy móc vào mọi heading. Trước hết kiểm tra mạch hiện có, giữ lại connection tốt, rồi bổ sung đúng chỗ thiếu bằng thuật ngữ và liên kết thật của topic; ưu tiên một đoạn nối có ý nghĩa hơn nhiều câu chung chung.
- Nội dung phải liền mạch, tự nhiên, đủ ngữ cảnh; hạn chế bullet/table khi chúng làm đứt luồng đọc.
- Với thuật ngữ quan trọng, giữ hoặc note thuật ngữ tiếng Anh; khi có liên hệ phù hợp với kiến thức/ngữ cảnh Hàn Quốc, note thêm thuật ngữ tiếng Hàn. Giải thích ngay tại chỗ để người đọc không phải tự tra hoặc dịch thêm.
- Ví dụ chỉ thêm khi giúp hiểu rõ hơn, phải đúng bản chất và không làm lệch nội dung chuyên môn.
- Có thể chia nhỏ, gộp hoặc tổ chức lại file/topic nếu giúp việc học và điều hướng tốt hơn, nhưng không làm mất nội dung cần thiết.
- Tôn trọng cấu trúc, naming, liên kết và style chung của repository; tránh duplicate content và file cô lập.
- Không cá nhân hóa nội dung học theo người dùng trừ khi được yêu cầu rõ ràng.

## Mạch học bắt buộc khi viết và review

Mỗi file/chapter cần được đọc như một đường đi có chủ đích, không phải tập hợp các mục độc lập. Khi mở đầu một mục lớn, trả lời ngắn gọn ba câu hỏi: người học cần biết gì trước, mục này giải quyết câu hỏi nào, và kết quả sẽ được dùng ở đâu. Khi kết thúc mục, trả lời tiếp: ta vừa có mental model/invariant nào, nó giới hạn ở đâu, và mục sau sẽ dùng hoặc mở rộng nó như thế nào.

Với chuỗi section, áp dụng nhịp sau nhưng viết bằng ngôn ngữ tự nhiên của domain:

1. **Định vị:** nối mục hiện tại với prerequisite hoặc câu hỏi được mở ra từ mục trước.
2. **Giải thích:** đi từ object/goal → mechanism/constraint → consequence → example hoặc evidence khi cần.
3. **Bàn giao:** chốt insight, nêu boundary hoặc cặp dễ nhầm, rồi dẫn sang section/owner tiếp theo bằng tên cụ thể và link nội bộ nếu có.

Không bắt buộc mọi mục phải có đúng ba đoạn hoặc dùng các nhãn trên. Đây là contract về reasoning, không phải template hình thức. Với glossary, index, checklist, bảng tra cứu hoặc README, phần “bàn giao” có thể là cách dùng bảng, owner của khái niệm và đường quay lại chapter giải thích; không biến tài liệu tham chiếu thành prose dài không cần thiết.

Khi retrofit tài liệu cũ, ưu tiên các điểm gãy sau: mở đầu nhảy thẳng vào chi tiết mà không có prerequisite; section kết thúc đột ngột; concept được nhắc lại nhưng không chỉ ra quan hệ; link chỉ tồn tại ở mục lục mà không có câu giải thích vì sao nên đi theo link đó. Không sửa raw/imported capture trực tiếp; với output generate, sửa source hoặc generator rồi regenerate.

## Branch & Git workflow

- `main` là trạng thái ổn định và canonical.
- Thay đổi lớn hoặc theo từng topic nên thực hiện trên branch riêng; kiểm tra nội dung, links và lỗi trước khi merge.
- Không giữ branch/commit dư thừa; sau khi merge, dọn các branch không còn cần thiết và giữ cấu trúc branch tối giản, rõ mục đích.

## Quy tắc kế thừa

Mọi yêu cầu mới sau này mặc định kế thừa file này.

Yêu cầu mới chỉ bổ sung hoặc override đúng phạm vi được nói rõ; các nguyên tắc còn lại vẫn giữ nguyên.
