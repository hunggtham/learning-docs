# Dùng chung (common / 공통) PROMPT — học tập (learning / 학습) Docs

Áp dụng tệp (file / 파일) này làm yêu cầu nền cho toàn bộ tài liệu và thay đổi tiếp theo trong repository.

## Nguyên tắc chung

- Luôn kiểm tra cấu trúc hiện tại, README, chuẩn gốc (canonical / 정본) files và nội bộ (internal / 내부) links trước khi tạo hoặc sửa nội dung.
- Viết như một tài liệu học hoàn chỉnh để có thể đọc và hiểu trực tiếp, không phải ghi chú (note / 노트) hoặc bản tóm tắt rời rạc.
- Giải thích theo luồng từ nền tảng đến nâng cao, đủ sâu để hiểu bản chất; không dừng ở giải thích ngắn, nửa chừng hoặc chỉ nêu kết luận.
- Ưu tiên understanding, lập luận (reasoning / 추론), cơ chế (mechanism / 메커니즘), nguyên lý nền tảng (first principles / 제일 원리) và liên kết (connection / 연결) giữa các concept hơn ghi nhớ máy móc.
- Mỗi đơn vị giải thích phải có **mạch nối hai đầu**: ở phần đầu, định vị mục này dựa trên kiến thức nào và vì sao cần học nó; ở phần cuối, chốt điều vừa hình thành và bàn giao rõ sang mục tiếp theo, mục liên quan hoặc đơn vị sở hữu (owner / 오너) chuẩn gốc (canonical / 정본) khác. Câu nối phải nói quan hệ học tập thực tế (phụ thuộc, mở rộng, đối chiếu, nguyên nhân–hệ quả hoặc ứng dụng), không chỉ viết “xem tiếp”.
- Các section liền kề phải được viết như một chuỗi suy luận: kết thúc section trước phải tạo câu hỏi hoặc nhu cầu cho section sau, còn section sau phải nhắc lại điểm tựa vừa dùng. Có thể dùng câu kiểu “từ đây…”, “để hiểu vì sao…”, “sau khi đã phân biệt…”, nhưng phải thay đổi theo nội dung và không được rải cùng một boilerplate cho mọi topic.
- Phần mở đầu của một chapter/topic cần chỉ ra prerequisite, phạm vi và câu hỏi trung tâm; phần kết thúc cần có recap ngắn, ranh giới (boundary / 경계)/điểm dễ nhầm (nếu có) và một hướng đọc tiếp cụ thể. Khi section đứng độc lập về mặt tham chiếu, vẫn phải nói nó thuộc đơn vị sở hữu (owner / 오너) nào và được dùng trước/sau thao tác hoặc concept nào.
- Khi rà soát (review / 검토) tài liệu cũ, không chèn câu nối máy móc vào mọi heading. Trước hết kiểm tra mạch hiện có, giữ lại liên kết (connection / 연결) tốt, rồi bổ sung đúng chỗ thiếu bằng thuật ngữ và liên kết thật của topic; ưu tiên một đoạn nối có ý nghĩa hơn nhiều câu chung chung.
- Nội dung phải liền mạch, tự nhiên, đủ ngữ cảnh; hạn chế bullet/bảng (table / 테이블) khi chúng làm đứt luồng đọc.
- Prose phải ưu tiên tiếng Việt tự nhiên. Không dùng chuỗi từ khóa (keyword / 키워드) English/Hàn để thay cho câu giải thích; ở **mọi lần xuất hiện trong phần giải thích**, thuật ngữ chuyên môn phải được dịch sang tiếng Việt trước rồi ghi từ khóa (keyword / 키워드) English/Hàn ngay cạnh theo dạng `tiếng Việt (English / 한국어)`. Không rút gọn các lần sau thành chỉ tiếng Việt hoặc chỉ English/Hàn.
- Giữ nguyên tên API, mô-đun (module / 모듈), lớp (class / 클래스), phương thức (method / 메서드), command, identifier, giao thức (protocol / 프로토콜), tiêu chuẩn (standard / 표준), sản phẩm (product / 제품), tệp (file / 파일) đường dẫn (path / 경로) và mã (code / 코드); không tự dịch tên kỹ thuật thành tên giả. Với cụm khó dịch hoặc có nhiều nghĩa, giải thích nghĩa tiếng Việt trong câu trước rồi mới giữ original wording.
- Khi một đoạn có quá nhiều English/Hàn, viết lại mô hình tư duy (mental model / 사고 모델) bằng tiếng Việt và chỉ giữ các từ khóa (keyword / 키워드) cần tra cứu trong ngoặc. Không tạo bảng từ khóa (keyword / 키워드) dài nếu một paragraph dịch tự nhiên đã đủ; glossary chỉ làm đơn vị sở hữu (owner / 오너) tra cứu, không thay prose của chapter.
- Với thuật ngữ quan trọng, giữ hoặc ghi chú (note / 노트) thuật ngữ tiếng Anh; khi có liên hệ phù hợp với kiến thức/ngữ cảnh Hàn Quốc, ghi chú (note / 노트) thêm thuật ngữ tiếng Hàn. Giải thích ngay tại chỗ để người đọc không phải tự tra hoặc dịch thêm.
- Ví dụ chỉ thêm khi giúp hiểu rõ hơn, phải đúng bản chất và không làm lệch nội dung chuyên môn.
- Có thể chia nhỏ, gộp hoặc tổ chức lại tệp (file / 파일)/topic nếu giúp việc học và điều hướng tốt hơn, nhưng không làm mất nội dung cần thiết.
- Tôn trọng cấu trúc, naming, liên kết và style chung của repository; tránh duplicate content và tệp (file / 파일) cô lập.
- Không cá nhân hóa nội dung học theo người dùng trừ khi được yêu cầu rõ ràng.

## Mạch học bắt buộc khi viết và rà soát (review / 검토)

Mỗi tệp (file / 파일)/chapter cần được đọc như một đường đi có chủ đích, không phải tập hợp các mục độc lập. Khi mở đầu một mục lớn, trả lời ngắn gọn ba câu hỏi: người học cần biết gì trước, mục này giải quyết câu hỏi nào, và kết quả sẽ được dùng ở đâu. Khi kết thúc mục, trả lời tiếp: ta vừa có mô hình tư duy (mental model / 사고 모델)/bất biến (invariant / 불변식) nào, nó giới hạn ở đâu, và mục sau sẽ dùng hoặc mở rộng nó như thế nào.

Với chuỗi section, áp dụng nhịp sau nhưng viết bằng ngôn ngữ tự nhiên của lĩnh vực (domain / 도메인):

1. **Định vị:** nối mục hiện tại với prerequisite hoặc câu hỏi được mở ra từ mục trước.
2. **Giải thích:** đi từ đối tượng (object / 객체)/goal → cơ chế (mechanism / 메커니즘)/ràng buộc (constraint / 제약조건) → consequence → example hoặc bằng chứng (evidence / 증거) khi cần.
3. **Bàn giao:** chốt insight, nêu ranh giới (boundary / 경계) hoặc cặp dễ nhầm, rồi dẫn sang section/đơn vị sở hữu (owner / 오너) tiếp theo bằng tên cụ thể và link nội bộ nếu có.

Không bắt buộc mọi mục phải có đúng ba đoạn hoặc dùng các nhãn trên. Đây là đặc tả hợp đồng (contract / 계약) về lập luận (reasoning / 추론), không phải template hình thức. Với glossary, chỉ mục (index / 인덱스), checklist, bảng tra cứu hoặc README, phần “bàn giao” có thể là cách dùng bảng, đơn vị sở hữu (owner / 오너) của khái niệm và đường quay lại chapter giải thích; không biến tài liệu tham chiếu thành prose dài không cần thiết.

Khi retrofit tài liệu cũ, ưu tiên các điểm gãy sau: mở đầu nhảy thẳng vào chi tiết mà không có prerequisite; section kết thúc đột ngột; concept được nhắc lại nhưng không chỉ ra quan hệ; link chỉ tồn tại ở mục lục mà không có câu giải thích vì sao nên đi theo link đó. Không sửa raw/imported capture trực tiếp; với đầu ra (output / 출력) generate, sửa nguồn (source / 소스) hoặc generator rồi regenerate.

## Quy ước ngôn ngữ và thuật ngữ

Người đọc phải có thể đọc phần giải thích chính bằng tiếng Việt mà không cần tự dịch lại một đoạn đầy từ khóa (keyword / 키워드). Ở mọi lần thuật ngữ chuyên môn xuất hiện trong prose, dùng mẫu:

```text
tiếng Việt (English / 한국어)
```

Lặp đủ bản dịch Việt và từ khóa (keyword / 키워드) English/Hàn ở từng lần xuất hiện để người đọc không phải quay lại tìm nghĩa. Nếu thật sự chưa có ánh xạ Hàn đáng tin cậy, tạm dùng `tiếng Việt (English)` và đánh dấu cần bổ sung thay vì đoán. Không dịch tên riêng của API, lớp (class / 클래스), command, giao thức (protocol / 프로토콜), tiêu chuẩn (standard / 표준), sản phẩm (product / 제품), tệp (file / 파일), identifier hay mã (code / 코드).

Khi rà soát (review / 검토) corpus cũ, tìm các câu trộn English/Hàn liên tiếp, heading chỉ có từ khóa (keyword / 키워드) và bảng từ khóa (keyword / 키워드) không có nghĩa Việt. Viết lại phần giải thích thành câu tiếng Việt; giữ original term cạnh bản dịch để tra cứu. Không sửa raw/provenance capture trực tiếp; với đầu ra (output / 출력) sinh tự động, cập nhật generator/nguồn (source / 소스) rồi regenerate.

## Branch & Git workflow

- `main` là trạng thái ổn định và chuẩn gốc (canonical / 정본).
- Thay đổi lớn hoặc theo từng topic nên thực hiện trên branch riêng; kiểm tra nội dung, links và lỗi trước khi merge.
- Không giữ branch/lần ghi nhận (commit / 커밋) dư thừa; sau khi merge, dọn các branch không còn cần thiết và giữ cấu trúc branch tối giản, rõ mục đích.

## Quy tắc kế thừa

Mọi yêu cầu mới sau này mặc định kế thừa tệp (file / 파일) này.

Yêu cầu mới chỉ bổ sung hoặc override đúng phạm vi được nói rõ; các nguyên tắc còn lại vẫn giữ nguyên.
