# INFO PROCESSING ENGINEER CERT PROMPT — 정보처리기사 필기

Áp dụng prompt này sau COMMON_PROMPT.md khi tạo, kiểm tra hoặc sửa tài liệu
정보처리기사 필기. Mục tiêu là đưa bộ tài liệu lên chất lượng A/A+: đúng kiến
thức, bám cách hỏi của kỳ thi, dễ ôn lại, có nguồn và không làm mất format hiện
tại.

## 1. Phạm vi và cấu trúc canonical

Canonical output là 정보처리기사/output/. Giữ nguyên cấu trúc hiện tại:

- output/README.md
- một folder cho mỗi môn;
- README.md của môn;
- 01-tai-lieu-hoc-day-du.md cho bài tổng hợp;
- lessons/NN-bai-hoc.md cho topic nhỏ.

Năm môn 필기 phải luôn được phân biệt rõ:

1. 소프트웨어 설계 — Software Design
2. 소프트웨어 개발 — Software Development
3. 데이터베이스 구축 — Database Construction
4. 프로그래밍 언어 활용 — Programming Language Application
5. 정보시스템 구축 관리 — Information System Construction Management

Không gộp nội dung 실기 vào 필기 nếu người dùng chưa yêu cầu. Nếu thêm nội
dung thực hành sau này, tạo nhánh hoặc folder riêng và ghi rõ phạm vi.

## 2. Mục tiêu chất lượng A/A+

Một topic chỉ đạt chuẩn khi người học có thể:

1. nhận ra thuật ngữ tiếng Hàn trong đề;
2. nói được định nghĩa chính xác bằng tiếng Việt;
3. phân biệt được khái niệm gần nhất;
4. áp dụng được công thức, quy tắc, thuật toán hoặc code;
5. giải thích được vì sao đáp án đúng và các đáp án khác sai;
6. tự ôn lại bằng một checklist hoặc câu hỏi ngắn.

Không đánh giá chất lượng chỉ bằng số lượng file. Ưu tiên tính đúng, tính nhất
quán, độ phủ và khả năng truy hồi khi làm bài.

## 3. Format giải thích bắt buộc

Mỗi lesson giữ format hiện tại và có các phần sau:

    # Tên topic

    ## 학습 목표 (Mục tiêu)
    ## 핵심 키워드 (Từ khóa)
    ## 선행·연결 개념 (Kiến thức liên kết)
    ## 읽는 방법 (Cách đọc)

    ---

    ## Tên topic

    ### TẦNG A – NOTE NÉN (ÔN / ĐI THI)
    - 개념: định nghĩa ngắn, chính xác.
    - 핵심 키워드: từ khóa Hàn/Anh phải nhận diện.
    - 시험 포인트: điểm phân biệt hoặc điều kiện thường bị hỏi.
    - 주의/함정: phủ định, ngoại lệ, cặp dễ nhầm.
    - 한 문장 설명: câu chốt để tự nhớ.

    ### TẦNG B – NOTE 보충 (HIỂU SÂU)
    - cơ chế hoặc trình tự;
    - ví dụ đúng bản chất;
    - liên hệ với topic trước/sau;
    - giới hạn hoặc trường hợp không áp dụng.

    ### 복습 체크리스트
    - [ ] ...

Không thêm TẦNG B cho đủ hình thức. Không dùng cùng một đoạn boilerplate cho
선행·연결 개념 hoặc 읽는 방법 nếu topic đó có quan hệ và cách đọc riêng.

## 4. Quy tắc thuật ngữ và ngôn ngữ

- Giữ nguyên thuật ngữ Hàn dùng trong đề.
- Ghi English/acronym khi giúp nhận diện.
- Giải thích bằng tiếng Việt ngay sau thuật ngữ.
- Không dịch tên hàm, keyword code, công thức hoặc ký hiệu kỹ thuật.
- Với mỗi acronym, nêu full form lần đầu xuất hiện.
- Không dùng mnemonic thay cho định nghĩa chính thức.
- Mnemonic phải được kiểm tra lại thứ tự và không được tạo ra một fact mới.

Mẫu ưu tiên:

한국어 (English) — giải thích tiếng Việt

## 5. Phương pháp kiểm chứng nội dung

Trước khi sửa hoặc thêm topic:

1. đọc README của root và môn;
2. xác định source canonical và script generate;
3. đối chiếu ít nhất hai nguồn nội bộ nếu topic có số liệu, tác giả, chuẩn hoặc
   công thức;
4. đánh dấu mâu thuẫn thay vì tự hòa giải không có bằng chứng;
5. sau khi sửa source, regenerate output và kiểm tra diff.

Các thông tin phải kiểm chứng đặc biệt:

- tác giả và lịch sử mô hình;
- tên/phiên bản ISO và chuẩn kỹ thuật;
- công thức và đơn vị;
- output của C/Java/Python/SQL;
- thứ tự thuật toán, trạng thái và điều kiện biên;
- các cặp phủ định như 옳은 것/옳지 않은 것, 상위/하위,
  논리적/물리적, 정적/동적.

Không được để hai file trong cùng output giải thích trái nhau. Nếu cần giữ một
quy ước đặc thù của đề, ghi rõ đó là “quy ước đề thi” và tách khỏi fact tổng
quát.

## 6. Quy tắc theo dạng kiến thức

### Định nghĩa, mô hình và phương pháp

Phải có mục đích, thành phần, trình tự, đặc điểm nhận diện và điểm khác với mô
hình gần nhất.

### Công thức

Phải có ý nghĩa biến, đơn vị, công thức, ví dụ thay số và lỗi thường gặp.

### Thuật toán

Phải có input, state transition, điều kiện dừng, output, độ phức tạp và một
ví dụ trace ngắn nếu phù hợp.

### Code và SQL

Phải trace được giá trị biến hoặc kết quả truy vấn. Ghi rõ language/version nếu
khác nhau có thể làm thay đổi kết quả.

### Database

Ưu tiên khóa, phụ thuộc, chuẩn hóa, 이상 현상, SQL result, transaction, ACID,
index, view, trigger và procedure. Với câu hỏi SQL, nên cho schema nhỏ và kết
quả sau thực thi thay vì chỉ mô tả bằng lời.

### Network, OS và security

Luôn tách đối tượng, cơ chế, mục tiêu, dấu hiệu nhận biết và biện pháp phòng
chống. Không gom nhiều attack có tên gần nhau vào cùng một định nghĩa.

## 7. Kiểm soát trùng lặp và độ phủ

- Một khái niệm có một định nghĩa canonical; topic khác liên kết thay vì chép
  lại nguyên đoạn.
- Nếu một topic xuất hiện ở nhiều source, gộp thành nền tảng → mở rộng → bẫy
  đề, không tạo nhiều lesson gần như giống nhau.
- Ghi rõ topic nào là nền tảng, topic nào là 심화.
- Không để môn 5 có độ chi tiết thấp hơn bất thường so với bốn môn còn lại.
- Mỗi môn phải có README, full guide, lesson links và checklist nhất quán.

## 8. Quality gates trước khi hoàn tất

Chạy hoặc kiểm tra các điều sau:

- mọi link Markdown nội bộ đều tồn tại;
- không còn placeholder, OCR artifact, HTML marker hoặc heading hỏng;
- không có hai định nghĩa trái nhau cho cùng một thuật ngữ;
- công thức/code mẫu đã được kiểm tra bằng ví dụ tối thiểu;
- lesson giữ đúng tên file và numbering hiện tại;
- full guide và lesson không lệch chủ đề;
- output regenerate được từ source/script;
- thay đổi không làm lộ raw, raw_md, PDF hoặc tài liệu nguồn chưa được phép;
- web reader hiển thị được heading, list, code, table và link.

## 9. Mức ưu tiên sửa lỗi

- P0: lỗi kiến thức, công thức, output code/SQL, sai ranh giới môn, link hỏng.
- P1: thiếu topic quan trọng, thiếu phân biệt đề thi, trùng lặp gây nhầm,
  thiếu 필기/실기 scope.
- P2: boilerplate, wording, mnemonic, navigation và visual polish.

Khi có P0, phải sửa trước khi mở rộng thêm topic. Mỗi lần nâng cấp phải ghi
ngắn gọn đã sửa gì, kiểm tra bằng lệnh nào và còn giới hạn nào chưa xử lý.
