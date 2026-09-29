# INFO PROCESSING ENGINEER CERT PROMPT — 정보처리기사 필기

Áp dụng prompt này sau COMMON_PROMPT.md khi tạo, kiểm tra hoặc sửa tài liệu
정보처리기사 필기. Mục tiêu là đưa bộ tài liệu lên chất lượng A/A+: đúng kiến
thức, bám cách hỏi của kỳ thi, dễ ôn lại, có nguồn và không làm mất format hiện
tại.

## 1. Phạm vi và cấu trúc chuẩn gốc (canonical / 정본)

Chuẩn gốc (canonical / 정본) đầu ra (output / 출력) là 정보처리기사/đầu ra (output / 출력)/. Giữ nguyên cấu trúc hiện tại:

- đầu ra (output / 출력)/README.md
- một folder cho mỗi môn;
- README.md của môn;
- 01-tai-lieu-hoc-day-du.md cho bài tổng hợp;
- lessons/NN-bai-hoc.md cho topic nhỏ.

Năm môn 필기 phải luôn được phân biệt rõ:

1. 소프트웨어 설계 — Software thiết kế (design / 설계)
2. 소프트웨어 개발 — Software Development
3. 데이터베이스 구축 — cơ sở dữ liệu (database / 데이터베이스) Construction
4. 프로그래밍 언어 활용 — Programming ngôn ngữ (language / 언어) ứng dụng (application / 애플리케이션)
5. 정보시스템 구축 관리 — thông tin (information / 정보) hệ thống (system / 시스템) Construction Management

Không gộp nội dung 실기 vào 필기 nếu người dùng chưa yêu cầu. Nếu thêm nội
dung thực hành sau này, tạo nhánh hoặc folder riêng và ghi rõ phạm vi.

## 2. Mục tiêu chất lượng A/A+

Một topic chỉ đạt chuẩn khi người học có thể:

1. nhận ra thuật ngữ tiếng Hàn trong đề;
2. nói được định nghĩa chính xác bằng tiếng Việt;
3. phân biệt được khái niệm gần nhất;
4. áp dụng được công thức, quy tắc, thuật toán hoặc mã (code / 코드);
5. giải thích được vì sao đáp án đúng và các đáp án khác sai;
6. tự ôn lại bằng một checklist hoặc câu hỏi ngắn.

Không đánh giá chất lượng chỉ bằng số lượng tệp (file / 파일). Ưu tiên tính đúng, tính nhất
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

    ### TẦNG A – ghi chú (note / 노트) NÉN (ÔN / ĐI THI)
    - 개념: định nghĩa ngắn, chính xác.
    - 핵심 키워드: từ khóa Hàn/Anh phải nhận diện.
    - 시험 포인트: điểm phân biệt hoặc điều kiện thường bị hỏi.
    - 주의/함정: phủ định, ngoại lệ, cặp dễ nhầm.
    - 한 문장 설명: câu chốt để tự nhớ.

    ### TẦNG B – ghi chú (note / 노트) 보충 (HIỂU SÂU)
    - cơ chế hoặc trình tự;
    - ví dụ đúng bản chất;
    - liên hệ với topic trước/sau;
    - giới hạn hoặc trường hợp không áp dụng.

    ### 복습 체크리스트
    - [ ] ...

Không thêm TẦNG B cho đủ hình thức. Không dùng cùng một đoạn boilerplate cho
선행·연결 개념 hoặc 읽는 방법 nếu topic đó có quan hệ và cách đọc riêng.

### Mạch nối của từng lesson

Mỗi lesson phải giúp người học biết mình đang đứng ở đâu trong chuỗi kiến thức:

- phần mở đầu nối topic với `선행·연결 개념` thật sự cần dùng, thuật ngữ hoặc câu hỏi đã mở ở lesson trước;
- phần giải thích đi theo `định nghĩa → cơ chế/quy tắc → điều kiện/ngoại lệ → ví dụ hoặc bẫy đề` khi phù hợp;
- phần kết thúc chốt điểm phân biệt và nói rõ lesson sau sẽ dùng, mở rộng hoặc đối chiếu điều gì.

Để câu nối có giá trị giảng dạy, mỗi lesson phải thể hiện đủ ba vế bằng thuật ngữ của chính topic:

1. **Từ đâu:** gọi tên kiến thức nền, điều kiện hoặc câu hỏi mà `선행·연결 개념` đã chuẩn bị; lesson đầu tiên phải nói rõ phạm vi và lý do bắt đầu từ đây.
2. **Đang giải quyết gì:** nêu câu hỏi trung tâm của lesson, rồi giải thích vì sao các bullet, bảng, công thức, đoạn mã hoặc ví dụ bên dưới cùng trả lời câu hỏi đó.
3. **Dùng đi đâu:** chốt mental model và điểm dễ nhầm, sau đó bàn giao sang lesson/subject/README cụ thể bằng quan hệ `kế thừa`, `mở rộng`, `đối chiếu`, `áp dụng` hoặc `nguyên nhân–hệ quả` khi nguồn cho phép.

Khung câu tham khảo (phải thay bằng nội dung thật, không sao chép nguyên mẫu): “Từ **[khái niệm nền]**, ta cần phân biệt **[câu hỏi/điểm thi]**; vì vậy lesson này dùng **[cơ chế hoặc tiêu chí]** để giải thích **[hệ quả]**. Khi đã nắm **[insight/boundary]**, người học có thể chuyển sang **[lesson hoặc nhu cầu kế tiếp]** để **[mục đích]**.” Với README, checklist và bảng tra cứu, câu nối phải chỉ rõ owner của khái niệm và đường quay lại lesson giảng giải; không dùng “xem tiếp” như một liên kết độc lập.

Ưu tiên các quan hệ thường gặp trong đề thi: dùng **kế thừa** khi lesson sau sử dụng cùng mô hình hoặc thuật ngữ của lesson trước; dùng **đối chiếu** khi cần phân biệt hai đáp án gần nhau; dùng **áp dụng** khi chuyển từ quy tắc sang đoạn mã, công thức hoặc tình huống; dùng **nguyên nhân–hệ quả** khi giải thích trạng thái, lỗi, 이상 현상 hoặc kết quả đầu ra. Câu nối phải nêu tiêu chí giúp người học chọn đúng đáp án, không chỉ nói rằng hai lesson “có liên quan”.

Khi review, bỏ qua một câu nối nếu câu đó không gọi tên ít nhất một khái niệm/điều kiện thật của lesson, không nêu quan hệ giữa hai phần, hoặc có thể dán nguyên xi vào mọi lesson. Nếu nguồn không đủ thông tin để chỉ tên phần sau, hãy bàn giao theo nhu cầu học tập được suy ra từ lesson và ghi rõ giới hạn thay vì bịa topic.

Áp dụng mạch này theo cấp heading trong lesson: tiêu đề `#` định vị topic và câu hỏi trung tâm; `##` nối topic với mục tiêu, từ khóa và kiến thức liên kết; `###`/`####` giải thích một khái niệm, cơ chế hoặc bẫy cụ thể rồi trả kết luận về `##` cha. Một heading con có bullet, bảng, công thức hoặc mã vẫn phải có câu hỏi cục bộ và câu nối với heading cha; không được coi cấp heading thấp là phần ghi chú rời.

Không bản sao (copy / 복사) một câu “tiếp theo là…” cho mọi bài. Với `README`, bảng tra cứu hoặc checklist, câu nối phải hướng người đọc về lesson/subject đơn vị sở hữu (owner / 오너) cụ thể; với đầu ra (output / 출력) được generate, sửa generator/nguồn (source / 소스) rồi regenerate thay vì sửa tay từng tệp (file / 파일).

## 4. Quy tắc thuật ngữ và ngôn ngữ
Phần “4. Quy tắc thuật ngữ và ngôn ngữ” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


- Giữ nguyên thuật ngữ Hàn dùng trong đề.
- Ghi English/acronym khi giúp nhận diện.
- Giải thích bằng tiếng Việt ngay sau thuật ngữ.
- Không dịch tên hàm, từ khóa (keyword / 키워드) mã (code / 코드), công thức hoặc ký hiệu kỹ thuật.
- Với mỗi acronym, nêu full form lần đầu xuất hiện.
- Không dùng mnemonic thay cho định nghĩa chính thức.
- Mnemonic phải được kiểm tra lại thứ tự và không được tạo ra một fact mới.

Mẫu ưu tiên:

한국어 (English) — giải thích tiếng Việt

## 5. Phương pháp kiểm chứng nội dung

Trước khi sửa hoặc thêm topic:

1. đọc README của gốc (root / 루트) và môn;
2. xác định nguồn (source / 소스) chuẩn gốc (canonical / 정본) và script generate;
3. đối chiếu ít nhất hai nguồn nội bộ nếu topic có số liệu, tác giả, chuẩn hoặc
   công thức;
4. đánh dấu mâu thuẫn thay vì tự hòa giải không có bằng chứng;
5. sau khi sửa nguồn (source / 소스), regenerate đầu ra (output / 출력) và kiểm tra diff.

Các thông tin phải kiểm chứng đặc biệt:

- tác giả và lịch sử mô hình;
- tên/phiên bản ISO và chuẩn kỹ thuật;
- công thức và đơn vị;
- đầu ra (output / 출력) của C/Java/Python/SQL;
- thứ tự thuật toán, trạng thái và điều kiện biên;
- các cặp phủ định như 옳은 것/옳지 않은 것, 상위/하위,
  논리적/물리적, 정적/동적.

Không được để hai tệp (file / 파일) trong cùng đầu ra (output / 출력) giải thích trái nhau. Nếu cần giữ một
quy ước đặc thù của đề, ghi rõ đó là “quy ước đề thi” và tách khỏi fact tổng
quát.

## 6. Quy tắc theo dạng kiến thức

### Định nghĩa, mô hình và phương pháp

Phải có mục đích, thành phần, trình tự, đặc điểm nhận diện và điểm khác với mô
hình gần nhất.

### Công thức

Phải có ý nghĩa biến, đơn vị, công thức, ví dụ thay số và lỗi thường gặp.

### Thuật toán

Phải có đầu vào (input / 입력), chuyển tiếp trạng thái (state transition / 상태 전이), điều kiện dừng, đầu ra (output / 출력), độ phức tạp và một
ví dụ dấu vết (trace / 추적) ngắn nếu phù hợp.

### Mã (code / 코드) và SQL

Phải dấu vết (trace / 추적) được giá trị biến hoặc kết quả truy vấn. Ghi rõ ngôn ngữ (language / 언어)/phiên bản (version / 버전) nếu
khác nhau có thể làm thay đổi kết quả.

### Cơ sở dữ liệu (database / 데이터베이스)

Ưu tiên khóa, phụ thuộc, chuẩn hóa, 이상 현상, SQL kết quả (result / 결과), giao dịch (transaction / 트랜잭션), ACID,
chỉ mục (index / 인덱스), view, trigger và procedure. Với câu hỏi SQL, nên cho lược đồ (schema / 스키마) nhỏ và kết
quả sau thực thi thay vì chỉ mô tả bằng lời.

### Mạng (network / 네트워크), OS và bảo mật (security / 보안)

Luôn tách đối tượng, cơ chế, mục tiêu, dấu hiệu nhận biết và biện pháp phòng
chống. Không gom nhiều attack có tên gần nhau vào cùng một định nghĩa.

## 7. Kiểm soát trùng lặp và độ phủ
Phần “7. Kiểm soát trùng lặp và độ phủ” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


- Một khái niệm có một định nghĩa chuẩn gốc (canonical / 정본); topic khác liên kết thay vì chép
  lại nguyên đoạn.
- Nếu một topic xuất hiện ở nhiều nguồn (source / 소스), gộp thành nền tảng → mở rộng → bẫy
  đề, không tạo nhiều lesson gần như giống nhau.
- Ghi rõ topic nào là nền tảng, topic nào là 심화.
- Không để môn 5 có độ chi tiết thấp hơn bất thường so với bốn môn còn lại.
- Mỗi môn phải có README, full guide, lesson links và checklist nhất quán.

## 8. chất lượng (quality / 품질) gates trước khi hoàn tất

Chạy hoặc kiểm tra các điều sau:

- mọi link Markdown nội bộ đều tồn tại;
- không còn placeholder, OCR sản phẩm tạo ra (artifact / 산출물), HTML marker hoặc heading hỏng;
- không có hai định nghĩa trái nhau cho cùng một thuật ngữ;
- công thức/mã (code / 코드) mẫu đã được kiểm tra bằng ví dụ tối thiểu;
- lesson giữ đúng tên tệp (file / 파일) và numbering hiện tại;
- full guide và lesson không lệch chủ đề;
- `output/COVERAGE_MATRIX.md` phản ánh đúng số lesson, nguồn (source / 소스) chuẩn gốc (canonical / 정본) và phạm vi rà soát của từng môn;
- đầu ra (output / 출력) regenerate được từ nguồn (source / 소스)/script;
- thay đổi không làm lộ raw, raw_md, PDF hoặc tài liệu nguồn chưa được phép;
- web reader hiển thị được heading, danh sách (list / 목록), mã (code / 코드), bảng (table / 테이블) và link.

## 9. Mức ưu tiên sửa lỗi
Phần “9. Mức ưu tiên sửa lỗi” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


- P0: lỗi kiến thức, công thức, đầu ra (output / 출력) mã (code / 코드)/SQL, sai ranh giới môn, link hỏng.
- P1: thiếu topic quan trọng, thiếu phân biệt đề thi, trùng lặp gây nhầm,
  thiếu 필기/실기 phạm vi (scope / 범위).
- P2: boilerplate, wording, mnemonic, điều hướng (navigation / 내비게이션) và visual polish.

Khi có P0, phải sửa trước khi mở rộng thêm topic. Mỗi lần nâng cấp phải ghi
ngắn gọn đã sửa gì, kiểm tra bằng lệnh nào và còn giới hạn nào chưa xử lý.
