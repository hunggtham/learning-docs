# Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu học tập)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **권장 학습 순서 (Lộ trình đề xuất)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này dùng README làm bản đồ owner của toàn môn, rồi nối mục tiêu, lộ trình và từng bài học thành chuỗi khái niệm có thể kiểm chứng.

## 학습 목표 (Mục tiêu học tập)

Phần này đặt mục tiêu của bài, để người mới biết mình cần giải thích được điều gì trước khi đi vào thuật ngữ và ví dụ.

- 시험에서 사용하는 한국어 용어를 영어와 베트남어 뜻까지 함께 인식한다.
- 각 개념을 정의 → 구성요소/절차 → 비교 포인트 → 예시 순서로 설명할 수 있다.
- 앞에서 배운 개념과 뒤의 심화 개념을 연결하여 문제의 조건을 빠르게 해석한다.

> **Câu hỏi trung tâm:** Khi học môn này, người học không chỉ cần nhận ra thuật ngữ Hàn mà còn phải giải thích khái niệm đang giải quyết vấn đề nào, dựa trên điều kiện nào và được dùng để nối sang phần kiến thức nào tiếp theo.

> **Nối mạch:** Trong **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **권장 학습 순서 (Lộ trình đề xuất)** nối từ **학습 목표 (Mục tiêu học tập)** sang **101. 개념적 설계 (Conceptual Design)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 권장 학습 순서 (Lộ trình đề xuất)

Phần này là đường đi của bài giảng: đọc theo thứ tự để mỗi mục sau dùng lại hoặc mở rộng tiêu chí của mục trước.

1. 먼저 이 문서의 각 `##` 단원을 순서대로 읽는다.
2. 단원마다 **핵심 키워드**를 소리 내어 읽고, 한국어 원문과 베트남어 설명을 함께 확인한다.
3. 마지막에 `복습 체크리스트`를 점검한 뒤, 세부 lesson 파일에서 헷갈리는 부분을 다시 본다.

> **Nguồn:** tổng hợp từ các Markdown đã generate trong `raw_md/final`, được đối chiếu với các nguồn `raw` và `raw_md` cùng môn. Nội dung gốc được giữ lại; chỉ chuẩn hoá cấu trúc bài học.

> **Quy ước ngôn ngữ:** phần giải thích ưu tiên tiếng Việt; ở mọi lần xuất hiện, thuật ngữ đề thi dùng dạng `nghĩa Việt (English / 한국어)` để không phải quay lại tìm nghĩa.

> **Cách học:** học theo thứ tự các mục; với mỗi mục, xác định khái niệm → cơ chế/quy tắc → ví dụ → mẹo nhớ. Các mục lặp lại ở phần “심화” (nâng cao) dùng để nối kiến thức trước đó với dạng câu hỏi sâu hơn.

> **Mạch giảng:** mỗi mục mở bằng vị trí và mục đích học, đi qua phần giải thích của nguồn, rồi chốt bằng một câu bàn giao sang mục kế tiếp. Hãy đọc các câu nối như một phần của bài giảng: chúng cho biết vì sao kiến thức hiện tại cần thiết trước khi chuyển sang kiến thức sau.

---

> **Nối mạch:** Ở chặng này của **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **101. 개념적 설계 (Conceptual Design)** nối từ **권장 학습 순서 (Lộ trình đề xuất)** sang **102. 논리적 설계 (Logical Design / Data Modeling)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 101. 개념적 설계 (Conceptual Design)

Chúng ta bắt đầu mạch học bằng **101. 개념적 설계 (Conceptual Design)**. Trước khi đi vào từng thuật ngữ, hãy giữ câu hỏi trung tâm: phần kiến thức này giải quyết vấn đề gì và vì sao các khái niệm sau phải được đọc trong cùng một bối cảnh? Mục đích của mục 1/54 là tạo điểm tựa để những phần tiếp theo được hiểu theo quan hệ, không chỉ được ghi nhớ như danh sách.

Để đọc **101. 개념적 설계 (Conceptual Design)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “101. 개념적 설계 (Conceptual Design)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 정보의 구조를 얻기 위하여 현실 세계에 대한 인식을 추상적 개념으로 표현하는 과정이다.
- 개념 스키마 모델링과 트랜잭션 모델링을 병행 수행한다.
- **VI (Vietnamese) (Tiếng Việt):** Thiết kế khái niệm. Quá trình biểu diễn nhận thức về thế giới thực thành các khái niệm trừu tượng để có được cấu trúc thông tin. Thực hiện song song mô hình hóa lược đồ khái niệm và mô hình hóa giao dịch.
- **Example (Korean/Vietnamese):** 현실 세계의 '학생'과 '수업'을 E-R 다이어그램으로 그리는 것. / Vẽ sơ đồ E-R cho 'học sinh' và 'lớp học' trong thế giới thực.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Khái-Trừu (Khái niệm = Trừu tượng).

Như vậy, **101. 개념적 설계 (Conceptual Design)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **102. 논리적 설계 (Logical Design / Data Modeling)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **102. 논리적 설계 (Logical Design / Data Modeling)** nối từ **101. 개념적 설계 (Conceptual Design)** sang **103. 물리적 설계 (Physical Design)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 102. 논리적 설계 (Logical Design / Data Modeling)

Sau khi đã đặt nền bằng **101. 개념적 설계 (Conceptual Design)**, ta chuyển sang **102. 논리적 설계 (Logical Design / Data Modeling)**. Đây là mắt xích 2/54 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **102. 논리적 설계 (Logical Design / Data Modeling)** như một bài học cho người mới, hãy giữ câu hỏi: **ta dùng mô hình nào để biểu diễn đối tượng, quan hệ hoặc hành vi, và giới hạn của mỗi cách là gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “102. 논리적 설계 (Logical Design / Data Modeling)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 자료를 특정 DBMS가 지원하는 논리적 자료 구조로 변환(mapping)시키는 과정이다.
- **VI (Vietnamese) (Tiếng Việt):** Thiết kế logic (Mô hình hóa dữ liệu). Quá trình chuyển đổi (ánh xạ) dữ liệu thành cấu trúc dữ liệu logic được hỗ trợ bởi một DBMS cụ thể.
- **Example (Korean/Vietnamese):** E-R 다이어그램을 관계형 데이터베이스의 테이블 구조로 변환하는 것. / Chuyển đổi sơ đồ E-R thành cấu trúc bảng của cơ sở dữ liệu quan hệ.
- 💡 **Mẹo ghi nhớ:** Logic-Bảng (Thiết kế Logic = Chuyển đổi sang Bảng).

Ta có thể khép mục **102. 논리적 설계 (Logical Design / Data Modeling)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **103. 물리적 설계 (Physical Design)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **103. 물리적 설계 (Physical Design)** nối từ **102. 논리적 설계 (Logical Design / Data Modeling)** sang **163-167. 데이터베이스 설계 순서 (Database Design Process)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 103. 물리적 설계 (Physical Design)

Từ **102. 논리적 설계 (Logical Design / Data Modeling)**, ta đã có điểm tựa để bước vào **103. 물리적 설계 (Physical Design)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 3/54 trước khi đi vào chi tiết.

Để đọc **103. 물리적 설계 (Physical Design)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “103. 물리적 설계 (Physical Design)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 논리적 구조로 표현된 데이터를 물리적 구조의 데이터로 변환하는 과정이다.
- 데이터베이스 파일의 저장 구조 및 액세스 경로를 결정한다.
- **VI (Vietnamese) (Tiếng Việt):** Thiết kế vật lý. Quá trình chuyển đổi dữ liệu cấu trúc logic thành cấu trúc vật lý (lưu trữ ổ đĩa, đường dẫn truy cập).
- **Example (Korean/Vietnamese):** 테이블에 인덱스를 생성하여 검색 속도를 높이는 것. / Tạo chỉ mục (index) trên bảng để tăng tốc độ tìm kiếm.
- 💡 **Mẹo ghi nhớ:** Vật-Lưu (Thiết kế Vật lý = Cấu trúc Lưu trữ).

Điểm chốt của **103. 물리적 설계 (Physical Design)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **163-167. 데이터베이스 설계 순서 (Database Design Process)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **103. 물리적 설계 (Physical Design)** đặt đầu vào cho **163-167. 데이터베이스 설계 순서 (Database Design Process)**, rồi **11. 데이터베이스 설계 (Thiết kế cơ sở dữ liệu)** mở rộng hệ quả liên quan.

## 163-167. 데이터베이스 설계 순서 (Database Design Process)

Ở bước 4/54, **163-167. 데이터베이스 설계 순서 (Database Design Process)** xuất hiện như phần tiếp nối của **103. 물리적 설계 (Physical Design)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **163-167. 데이터베이스 설계 순서 (Database Design Process)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “163-167. 데이터베이스 설계 순서 (Database Design Process)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **요구 조건 분석 (Requirements Analysis):** 요구 조건 명세서 작성.
- **개념적 설계 (Conceptual Design - 164):** 개념 스키마, E-R 모델, DBMS 독립적.
- **논리적 설계 (Logical Design - 165):** 논리 스키마 설계, 매핑.
- **물리적 설계 (Physical Design - 166):** 물리적 구조 변환, 접근 경로, 저장 레코드 양식 결정.
- **구현 (Implementation):** DDL로 DB 생성.
- **VI (Vietnamese) (Tiếng Việt):** Quy trình thiết kế CSDL.
  - Phân tích yêu cầu -> Thiết kế Khái niệm (E-R) -> Thiết kế Logic (Bảng/Lược đồ logic) -> Thiết kế Vật lý (Lưu trữ) -> Triển khai (Code DDL).
- 💡 **Mẹo ghi nhớ:** Yêu-Khái-Lo-Vật-Cài (Yêu cầu -> Khái niệm -> Logic -> Vật lý -> Cài đặt).

Như vậy, **163-167. 데이터베이스 설계 순서 (Database Design Process)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **11. 데이터베이스 설계 (Thiết kế cơ sở dữ liệu)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **163-167. 데이터베이스 설계 순서 (Database Design Process)** cần kiểm chứng bằng **11. 데이터베이스 설계 (Thiết kế cơ sở dữ liệu)**, rồi **104. 데이터 모델에 표시할 요소 (Elements of Data Model)** mở rộng hệ quả liên quan.

## 11. 데이터베이스 설계 (Thiết kế cơ sở dữ liệu)

Sau khi đã đặt nền bằng **163-167. 데이터베이스 설계 순서 (Database Design Process)**, ta chuyển sang **11. 데이터베이스 설계 (Thiết kế cơ sở dữ liệu)**. Đây là mắt xích 5/54 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **11. 데이터베이스 설계 (Thiết kế cơ sở dữ liệu)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng là bằng chứng để so sánh các lựa chọn theo cùng tiêu chí, không phải danh sách cần học thuộc từng ô.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “11. 데이터베이스 설계 (Thiết kế cơ sở dữ liệu)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

| 단계 (Giai đoạn) | 설명 (Mô tả & Hoạt động) | Giải thích (VN) |
|---|---|---|
| **1. 요구조건 분석** | 목적 파악, 요구조건 식별 | Phân tích yêu cầu: Tìm hiểu người dùng cần gì. |
| **2. 개념적 설계** | 개념 스키마, E-R 다이어그램, 트랜잭션 모델링 | Thiết kế Khái niệm: Độc lập với DBMS. Vẽ biểu đồ ER (Thực thể - Mối quan hệ). |
| **3. 논리적 설계** | 논리적 자료구조, **정규화(Normalization)**, 트랜잭션 인터페이스 설계 | Thiết kế Logic: Chuyển đổi ER sang bảng (Table). **Thực hiện chuẩn hóa (Normalization)**. |
| **4. 물리적 설계** | 물리적 구조, 저장 레코드 양식, **접근 경로(Access Path)** | Thiết kế Vật lý: Định dạng file trên đĩa cứng, chọn kiểu dữ liệu thực tế, thiết lập cấu trúc lưu trữ và Index (Đường truy cập). |

> 💡 **Mẹo ghi nhớ:** **Yêu - Khái - Lo - Vật** (Yêu cầu -> Khái niệm -> Logic -> Vật lý). Dễ thi: Chuẩn hóa ở bước Logic, Access Path/Lưu trữ ở bước Vật lý.

test
---

Ta có thể khép mục **11. 데이터베이스 설계 (Thiết kế cơ sở dữ liệu)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **104. 데이터 모델에 표시할 요소 (Elements of Data Model)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **11. 데이터베이스 설계 (Thiết kế cơ sở dữ liệu)** đặt vấn đề; **104. 데이터 모델에 표시할 요소 (Elements of Data Model)** đối chiếu bằng chứng, rồi **168-172. 관계형 데이터 모델 및 E-R 모델 심화 (Relational & E-R Model Deep Dive)** mở rộng hệ quả hoặc giới hạn liên quan.

## 104. 데이터 모델에 표시할 요소 (Elements of Data Model)

Từ **11. 데이터베이스 설계 (Thiết kế cơ sở dữ liệu)**, ta đã có điểm tựa để bước vào **104. 데이터 모델에 표시할 요소 (Elements of Data Model)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 6/54 trước khi đi vào chi tiết.

Để đọc **104. 데이터 모델에 표시할 요소 (Elements of Data Model)** như một bài học cho người mới, hãy giữ câu hỏi: **ta dùng mô hình nào để biểu diễn đối tượng, quan hệ hoặc hành vi, và giới hạn của mỗi cách là gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “104. 데이터 모델에 표시할 요소 (Elements of Data Model)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **구조 (Structure):** 논리적으로 표현된 개체 타입들 간의 관계로 데이터 구조 및 정적 성질.
- **연산 (Operation):** 실제 데이터를 처리하는 작업 명세.
- **제약 조건 (Constraint):** 실제 데이터의 논리적인 제약 조건.
- **VI (Vietnamese) (Tiếng Việt):** Các yếu tố trong mô hình dữ liệu.
  - Cấu trúc: Mối quan hệ giữa các kiểu thực thể (tĩnh).
  - Phép toán: Đặc tả công việc xử lý dữ liệu (động).
  - Ràng buộc: Điều kiện giới hạn logic của dữ liệu.
- **Example (Korean/Vietnamese):** 구조: 학생 테이블, 연산: 정보 검색, 제약조건: 나이는 0 이상. / Cấu trúc: Bảng sinh viên, Phép toán: Tìm kiếm, Ràng buộc: Tuổi >= 0.
- 💡 **Mẹo ghi nhớ:** Cấu-Toán-Buộc (Cấu trúc, Toán tử, Ràng buộc).

Điểm chốt của **104. 데이터 모델에 표시할 요소 (Elements of Data Model)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **168-172. 관계형 데이터 모델 및 E-R 모델 심화 (Relational & E-R Model Deep Dive)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **168-172. 관계형 데이터 모델 및 E-R 모델 심화 (Relational & E-R Model Deep Dive)** nối từ **104. 데이터 모델에 표시할 요소 (Elements of Data Model)** sang **12. 관계형 데이터 모델과 릴레이션 (Mô hình dữ liệu quan hệ & Relation)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 168-172. 관계형 데이터 모델 및 E-R 모델 심화 (Relational & E-R Model Deep Dive)

Ở bước 7/54, **168-172. 관계형 데이터 모델 및 E-R 모델 심화 (Relational & E-R Model Deep Dive)** xuất hiện như phần tiếp nối của **104. 데이터 모델에 표시할 요소 (Elements of Data Model)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **168-172. 관계형 데이터 모델 및 E-R 모델 심화 (Relational & E-R Model Deep Dive)** như một bài học cho người mới, hãy giữ câu hỏi: **ta dùng mô hình nào để biểu diễn đối tượng, quan hệ hoặc hành vi, và giới hạn của mỗi cách là gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “168-172. 관계형 데이터 모델 및 E-R 모델 심화 (Relational & E-R Model Deep Dive)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **E-R 모델 (168-169):** 피터 첸 제안. 기본키 속성은 '밑줄 타원(Underlined Oval)', 복합 속성은 '복수 타원(Multiple Ovals)'. 1:1, 1:N, N:M 표현.
- **관계형 데이터 모델 (170):** 2차원 표(Table) 형태.
- **릴레이션 특징 (172):**
  - 똑같은 튜플 포함 불가 (튜플의 유일성).
  - 튜플 사이, 속성 사이 순서 없음.
  - 속성 이름은 유일, 속성 값은 중복 가능.
  - 원자값(Atomic)만 허용.
- **VI (Vietnamese) (Tiếng Việt):** Mô hình E-R và Mô hình quan hệ.
  - E-R: Thuộc tính khóa chính có gạch chân, thuộc tính phức hợp có nhiều vòng bầu dục.
  - Đặc điểm quan hệ (Bảng): Hàng không trùng lặp (duy nhất), không quan trọng thứ tự hàng/cột, chỉ chứa giá trị nguyên tử.

Như vậy, **168-172. 관계형 데이터 모델 및 E-R 모델 심화 (Relational & E-R Model Deep Dive)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **12. 관계형 데이터 모델과 릴레이션 (Mô hình dữ liệu quan hệ & Relation)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **168-172. 관계형 데이터 모델 및 E-R 모델 심화 (Relational & E-R Model Deep Dive)** đặt vấn đề; **12. 관계형 데이터 모델과 릴레이션 (Mô hình dữ liệu quan hệ & Relation)** đối chiếu bằng chứng, rồi **13. 데이터 모델과 E-R 다이어그램 (Mô hình dữ liệu & Biểu đồ E-R)** mở rộng hệ quả hoặc giới hạn liên quan.

## 12. 관계형 데이터 모델과 릴레이션 (Mô hình dữ liệu quan hệ & Relation)

Sau khi đã đặt nền bằng **168-172. 관계형 데이터 모델 및 E-R 모델 심화 (Relational & E-R Model Deep Dive)**, ta chuyển sang **12. 관계형 데이터 모델과 릴레이션 (Mô hình dữ liệu quan hệ & Relation)**. Đây là mắt xích 8/54 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **12. 관계형 데이터 모델과 릴레이션 (Mô hình dữ liệu quan hệ & Relation)** như một bài học cho người mới, hãy giữ câu hỏi: **ta dùng mô hình nào để biểu diễn đối tượng, quan hệ hoặc hành vi, và giới hạn của mỗi cách là gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **12.1 릴레이션의 구조 (Cấu trúc Relation / Bảng)**. Hãy xác định **12.1 릴레이션의 구조 (Cấu trúc Relation / Bảng)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 12.1 릴레이션의 구조 (Cấu trúc Relation / Bảng)

Phần nguồn của **12.1 릴레이션의 구조 (Cấu trúc Relation / Bảng)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “12.1 릴레이션의 구조 (Cấu trúc Relation / Bảng)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **릴레이션 (Relation):** Bảng dữ liệu gồm hàng và cột.
- **튜플 (Tuple):** Hàng (Row / Record).
- **속성 (Attribute):** Cột (Column / Field).
- **차수 (Degree / 디그리):** Số lượng thuộc tính (Cột).
- **카디널리티 (Cardinality):** Số lượng 튜플 (Hàng).
- **도메인 (Domain):** Tập hợp các giá trị nguyên tử (Atomic) mà một thuộc tính có thể nhận.
- **인스턴스 (Instance):** Tập hợp các 튜플 tại một thời điểm (Dữ liệu thực tế).

> 💡 **Mẹo ghi nhớ:** **Car-Tu, De-At** (Cardinality = Tuple/Hàng, Degree = Attribute/Cột).

Với **12.1 릴레이션의 구조 (Cấu trúc Relation / Bảng)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **12.1 릴레이션의 구조 (Cấu trúc Relation / Bảng)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **12.2 릴레이션의 특징 (Đặc điểm của Relation)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **12.2 릴레이션의 특징 (Đặc điểm của Relation)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 12.2 릴레이션의 특징 (Đặc điểm của Relation)

Các ý ngay dưới **12.2 릴레이션의 특징 (Đặc điểm của Relation)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “12.2 릴레이션의 특징 (Đặc điểm của Relation)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **튜플의 유일성:** Không có 2 hàng nào giống hệt nhau.
- **튜플/속성의 무순서:** Thứ tự của các hàng và các cột **không quan trọng**.
- **원자값:** Mỗi ô (giao giữa hàng và cột) chỉ được chứa một giá trị duy nhất (không thể chia nhỏ).

---

Các bullet của **12.2 릴레이션의 특징 (Đặc điểm của Relation)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **12.2 릴레이션의 특징 (Đặc điểm của Relation)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **12. 관계형 데이터 모델과 릴레이션 (Mô hình dữ liệu quan hệ & Relation)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **13. 데이터 모델과 E-R 다이어그램 (Mô hình dữ liệu & Biểu đồ E-R)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **12. 관계형 데이터 모델과 릴레이션 (Mô hình dữ liệu quan hệ & Relation)** đặt vấn đề; **13. 데이터 모델과 E-R 다이어그램 (Mô hình dữ liệu & Biểu đồ E-R)** đối chiếu bằng chứng, rồi **105. E-R 다이어그램 (E-R Diagram)** mở rộng hệ quả hoặc giới hạn liên quan.

## 13. 데이터 모델과 E-R 다이어그램 (Mô hình dữ liệu & Biểu đồ E-R)

Từ **12. 관계형 데이터 모델과 릴레이션 (Mô hình dữ liệu quan hệ & Relation)**, ta đã có điểm tựa để bước vào **13. 데이터 모델과 E-R 다이어그램 (Mô hình dữ liệu & Biểu đồ E-R)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 9/54 trước khi đi vào chi tiết.

Để đọc **13. 데이터 모델과 E-R 다이어그램 (Mô hình dữ liệu & Biểu đồ E-R)** như một bài học cho người mới, hãy giữ câu hỏi: **ta dùng mô hình nào để biểu diễn đối tượng, quan hệ hoặc hành vi, và giới hạn của mỗi cách là gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng là bằng chứng để so sánh các lựa chọn theo cùng tiêu chí, không phải danh sách cần học thuộc từng ô.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **데이터 모델 구성 요소 (Thành phần mô hình dữ liệu)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 데이터 모델 구성 요소 (Thành phần mô hình dữ liệu)

Các ý ngay dưới **데이터 모델 구성 요소 (Thành phần mô hình dữ liệu)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “데이터 모델 구성 요소 (Thành phần mô hình dữ liệu)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개체 (Entity):** Đối tượng thực tế (ví dụ: Sinh viên, Môn học).
- **속성 (Attribute):** Đặc điểm của đối tượng (ví dụ: Mã SV, Tên).
- **관계 (Relationship):** Sự liên kết giữa các đối tượng (ví dụ: Đăng ký).
- *Lưu ý: 3 yếu tố cơ bản của mô hình là Cấu trúc (Structure), Phép toán (Operation), và Ràng buộc (Constraint).*

Các ý về **데이터 모델 구성 요소 (Thành phần mô hình dữ liệu)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **데이터 모델 구성 요소 (Thành phần mô hình dữ liệu)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **E-R 다이어그램 기호 (Ký hiệu biểu đồ E-R - Peter Chen)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **E-R 다이어그램 기호 (Ký hiệu biểu đồ E-R - Peter Chen)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### E-R 다이어그램 기호 (Ký hiệu biểu đồ E-R - Peter Chen)

Bây giờ ta đi vào nội dung của **E-R 다이어그램 기호 (Ký hiệu biểu đồ E-R - Peter Chen)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “E-R 다이어그램 기호 (Ký hiệu biểu đồ E-R - Peter Chen)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

| 기호 (Ký hiệu) | 의미 (Ý nghĩa) | Giải thích (VN) |
|---|---|---|
| **사각형 (Hình chữ nhật)** | 개체 (Entity) | Đối tượng thực thể. |
| **마름모 (Hình thoi)** | 관계 (Relationship) | Mối quan hệ giữa các thực thể (1:1, 1:N, N:M). |
| **타원 (Hình bầu dục)** | 속성 (Attribute) | Thuộc tính. |
| **밑줄 타원 (Bầu dục gạch dưới)** | 기본키 (Primary Key) | Thuộc tính Khóa chính. |
| **이중 타원 (Bầu dục kép)** | 다중 값 속성 (Multi-valued) | Thuộc tính đa trị (có thể chứa nhiều giá trị, vd: Số điện thoại). |
| **선 (Đường thẳng)** | 링크 (Link) | Đường nối kết. |

---

Bảng trong **E-R 다이어그램 기호 (Ký hiệu biểu đồ E-R - Peter Chen)** không phải danh sách rời. Hãy đọc theo từng cột để nhận ra tiêu chí so sánh, rồi tự diễn đạt bằng một câu: đối tượng nào khác nhau ở điểm nào và trong điều kiện nào sự khác biệt đó có ý nghĩa.

Điểm chốt của **E-R 다이어그램 기호 (Ký hiệu biểu đồ E-R - Peter Chen)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **13. 데이터 모델과 E-R 다이어그램 (Mô hình dữ liệu & Biểu đồ E-R)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **105. E-R 다이어그램 (E-R Diagram)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **13. 데이터 모델과 E-R 다이어그램 (Mô hình dữ liệu & Biểu đồ E-R)** đặt vấn đề; **105. E-R 다이어그램 (E-R Diagram)** đối chiếu bằng chứng, rồi **110-114. 키 (Keys)** mở rộng hệ quả hoặc giới hạn liên quan.

## 105. E-R 다이어그램 (E-R Diagram)

Ở bước 10/54, **105. E-R 다이어그램 (E-R Diagram)** xuất hiện như phần tiếp nối của **13. 데이터 모델과 E-R 다이어그램 (Mô hình dữ liệu & Biểu đồ E-R)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **105. E-R 다이어그램 (E-R Diagram)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “105. E-R 다이어그램 (E-R Diagram)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 사각형 (Rectangle): 개체 (Entity)
- 마름모 (Diamond): 관계 (Relationship)
- 타원 (Oval): 속성 (Attribute)
- 이중 타원 (Double Oval): 다중값 속성 (Multivalued Attribute)
- 선 (Line): 연결 (Link)
- **VI (Vietnamese) (Tiếng Việt):** Sơ đồ E-R. Hình chữ nhật (Thực thể), Hình thoi (Mối quan hệ), Hình bầu dục (Thuộc tính), Hình bầu dục kép (Thuộc tính đa trị).
- **Example:** 고객(사각형)이 상품(사각형)을 구매(마름모)한다. / Khách hàng (HCN) mua (Hình thoi) sản phẩm (HCN).

Như vậy, **105. E-R 다이어그램 (E-R Diagram)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **110-114. 키 (Keys)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **110-114. 키 (Keys)** nối từ **105. E-R 다이어그램 (E-R Diagram)** sang **173-177. 키와 무결성, 관계대수 요약 (Keys, Integrity, Relational Algebra)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 110-114. 키 (Keys)

Sau khi đã đặt nền bằng **105. E-R 다이어그램 (E-R Diagram)**, ta chuyển sang **110-114. 키 (Keys)**. Đây là mắt xích 11/54 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **110-114. 키 (Keys)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “110-114. 키 (Keys)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **후보키 (Candidate Key):** 튜플을 유일하게 식별하는 속성. 유일성과 최소성 만족.
- **기본키 (Primary Key):** 후보키 중 선정된 주키. 중복과 NULL 불가.
- **대체키 (Alternate Key):** 후보키 중 기본키를 제외한 나머지 (보조키).
- **슈퍼키 (Super Key):** 유일성은 만족하지만 최소성은 만족하지 못하는 속성 집합.
- **외래키 (Foreign Key):** 다른 릴레이션의 기본키를 참조하는 속성.
- **VI (Vietnamese) (Tiếng Việt):** Các loại khóa (Keys).
  - Candidate Key (Khóa ứng viên): Định danh duy nhất, thỏa mãn tính duy nhất và tính tối thiểu.
  - Primary Key (Khóa chính): Chọn từ khóa ứng viên, không trùng lặp, không NULL.
  - Alternate Key (Khóa thay thế): Các khóa ứng viên còn lại.
  - Super Key (Siêu khóa): Thỏa mãn tính duy nhất nhưng không tối thiểu.
  - Foreign Key (Khóa ngoại): Thuộc tính tham chiếu đến khóa chính của bảng khác.

Ta có thể khép mục **110-114. 키 (Keys)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **173-177. 키와 무결성, 관계대수 요약 (Keys, Integrity, Relational Algebra)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **173-177. 키와 무결성, 관계대수 요약 (Keys, Integrity, Relational Algebra)** nối từ **110-114. 키 (Keys)** sang **5. 스키마 (Schema - Lược đồ)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 173-177. 키와 무결성, 관계대수 요약 (Keys, Integrity, Relational Algebra)

Từ **110-114. 키 (Keys)**, ta đã có điểm tựa để bước vào **173-177. 키와 무결성, 관계대수 요약 (Keys, Integrity, Relational Algebra)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 12/54 trước khi đi vào chi tiết.

Để đọc **173-177. 키와 무결성, 관계대수 요약 (Keys, Integrity, Relational Algebra)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “173-177. 키와 무결성, 관계대수 요약 (Keys, Integrity, Relational Algebra)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

*Note: Includes duplicated points consolidated.*
- **도메인 무결성 (Domain Integrity):** 속성 값이 정의된 도메인에 속해야 함.
- **사용자 정의 무결성 (User-Defined Integrity):** 사용자가 정의한 제약 조건 만족.
- **순수 관계 연산자 (Pure Relational Operators):**
  - Select (σ): 수평 연산 (Horizontal) - 튜플 구함.
  - Project (π): 수직 연산 (Vertical) - 속성 구함.
  - Join (⋈) / Division (÷).
- **일반 집합 연산자 (Set Operators):** UNION (합집합), INTERSECTION (교집합), DIFFERENCE (차집합), CARTESIAN PRODUCT (교차곱).
- **VI (Vietnamese) (Tiếng Việt):** Các ràng buộc và Đại số quan hệ (nhắc lại).
  - Toàn vẹn miền (Domain): Giá trị phải nằm trong miền cho phép.
  - Select: Phép toán ngang (lọc hàng).
  - Project: Phép toán dọc (lọc cột).
  - Phép toán tập hợp: Hợp, Giao, Hiệu, Tích Đề-các.

Điểm chốt của **173-177. 키와 무결성, 관계대수 요약 (Keys, Integrity, Relational Algebra)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **5. 스키마 (Schema - Lược đồ)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **5. 스키마 (Schema - Lược đồ)** nối từ **173-177. 키와 무결성, 관계대수 요약 (Keys, Integrity, Relational Algebra)** sang **14. 키(Key)의 종류와 데이터베이스 무결성 (Các loại Khóa & Tính Toàn vẹn)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 5. 스키마 (Schema - Lược đồ)

Ở bước 13/54, **5. 스키마 (Schema - Lược đồ)** xuất hiện như phần tiếp nối của **173-177. 키와 무결성, 관계대수 요약 (Keys, Integrity, Relational Algebra)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **5. 스키마 (Schema - Lược đồ)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “5. 스키마 (Schema - Lược đồ)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **외부 스키마 (External Schema - Lược đồ ngoại):** 사용자나 개발자의 관점 (Góc nhìn người dùng). Nhiều lược đồ ngoại tồn tại cùng lúc (Mỗi người nhìn hệ thống một kiểu).
- **개념 스키마 (Conceptual Schema - Lược đồ khái niệm):** 조직 전체의 논리적 구조, 단 하나만 존재 (Cấu trúc logic của toàn bộ tổ chức, chỉ có 1). Quản lý quan hệ, quyền, bảo mật.
- **내부 스키마 (Internal Schema - Lược đồ nội):** 물리적 저장장치의 관점 (Góc nhìn lưu trữ vật lý). Tổ chức các bản ghi, chỉ mục trên ổ đĩa.

> 💡 **Mẹo ghi nhớ:** **Ngoại - Khái - Nội** (Người dùng (Ngoại) -> Thiết kế CSDL (Khái) -> Ổ cứng (Nội)).

---

Như vậy, **5. 스키마 (Schema - Lược đồ)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **14. 키(Key)의 종류와 데이터베이스 무결성 (Các loại Khóa & Tính Toàn vẹn)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **14. 키(Key)의 종류와 데이터베이스 무결성 (Các loại Khóa & Tính Toàn vẹn)** nối từ **5. 스키마 (Schema - Lược đồ)** sang **115. 무결성 (Integrity)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. 키(Key)의 종류와 데이터베이스 무결성 (Các loại Khóa & Tính Toàn vẹn)

Sau khi đã đặt nền bằng **5. 스키마 (Schema - Lược đồ)**, ta chuyển sang **14. 키(Key)의 종류와 데이터베이스 무결성 (Các loại Khóa & Tính Toàn vẹn)**. Đây là mắt xích 14/54 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **14. 키(Key)의 종류와 데이터베이스 무결성 (Các loại Khóa & Tính Toàn vẹn)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng là bằng chứng để so sánh các lựa chọn theo cùng tiêu chí, không phải danh sách cần học thuộc từng ô.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **키(Key) 종류 (Các loại Khóa)**. Hãy xác định **키(Key) 종류 (Các loại Khóa)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 키(Key) 종류 (Các loại Khóa)

Phần nguồn của **키(Key) 종류 (Các loại Khóa)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “키(Key) 종류 (Các loại Khóa)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

| 종류 (Loại) | 설명 (Mô tả) | Tính chất (VN) |
|---|---|---|
| **슈퍼키 (Super Key)** | 튜플을 구별할 수 있는 속성 집합. | **Tính duy nhất (유일성).** |
| **후보키 (Candidate Key)** | 기본키가 될 수 있는 키 (유일성 + 최소성). | **Duy nhất + Tối thiểu (최소성).** (Không dư thừa thuộc tính). |
| **기본키 (Primary Key)** | 후보키 중 선택된 주키. NULL 불가. | Khóa chính. **Không được trùng, Không được NULL.** |
| **대체키 (Alternate Key)** | 기본키로 선택되지 못한 나머지 후보키. | Khóa thay thế (Khóa phụ). |
| **외래키 (Foreign Key)** | 다른 릴레이션의 기본키를 참조하는 속성. | Khóa ngoại. Dùng để liên kết 2 bảng. |

Bảng trong **키(Key) 종류 (Các loại Khóa)** không phải danh sách rời. Hãy đọc theo từng cột để nhận ra tiêu chí so sánh, rồi tự diễn đạt bằng một câu: đối tượng nào khác nhau ở điểm nào và trong điều kiện nào sự khác biệt đó có ý nghĩa.

Ta vừa chốt **키(Key) 종류 (Các loại Khóa)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **무결성 (Integrity - Tính toàn vẹn / chính xác)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **무결성 (Integrity - Tính toàn vẹn / chính xác)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 무결성 (Integrity - Tính toàn vẹn / chính xác)

Các ý ngay dưới **무결성 (Integrity - Tính toàn vẹn / chính xác)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “무결성 (Integrity - Tính toàn vẹn / chính xác)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개체 무결성 (Entity):** Khóa chính (Primary Key) không được trùng lặp và **không được NULL**.
- **참조 무결성 (Referential):** Khóa ngoại (Foreign Key) phải khớp với Khóa chính của bảng tham chiếu, hoặc có thể là NULL.
- **도메인 무결성 (Domain):** Giá trị phải nằm trong phạm vi định nghĩa (ví dụ: Giới tính chỉ là Nam/Nữ).
- **사용자 정의 무결성 (User-defined):** Phải thỏa mãn các điều kiện do người dùng tự định nghĩa.

---

Các ý về **무결성 (Integrity - Tính toàn vẹn / chính xác)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Điểm chốt của **무결성 (Integrity - Tính toàn vẹn / chính xác)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **14. 키(Key)의 종류와 데이터베이스 무결성 (Các loại Khóa & Tính Toàn vẹn)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **115. 무결성 (Integrity)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **115. 무결성 (Integrity)** nối từ **14. 키(Key)의 종류와 데이터베이스 무결성 (Các loại Khóa & Tính Toàn vẹn)** sang **116-121. 관계대수 (Relational Algebra)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 115. 무결성 (Integrity)

Từ **14. 키(Key)의 종류와 데이터베이스 무결성 (Các loại Khóa & Tính Toàn vẹn)**, ta đã có điểm tựa để bước vào **115. 무결성 (Integrity)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 15/54 trước khi đi vào chi tiết.

Để đọc **115. 무결성 (Integrity)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “115. 무결성 (Integrity)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개체 무결성 (Entity Integrity):** 기본키는 NULL값이나 중복값을 가질 수 없다.
- **참조 무결성 (Referential Integrity):** 외래키 값은 NULL이거나 참조 릴레이션의 기본키 값과 동일해야 한다.
- **VI (Vietnamese) (Tiếng Việt):** Tính toàn vẹn.
  - Toàn vẹn thực thể: Khóa chính không NULL và không trùng.
  - Toàn vẹn tham chiếu: Khóa ngoại phải là NULL hoặc khớp với khóa chính được tham chiếu.

Điểm chốt của **115. 무결성 (Integrity)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **116-121. 관계대수 (Relational Algebra)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **116-121. 관계대수 (Relational Algebra)** nối từ **115. 무결성 (Integrity)** sang **123-125. 정규화 (Normalization)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 116-121. 관계대수 (Relational Algebra)

Ở bước 16/54, **116-121. 관계대수 (Relational Algebra)** xuất hiện như phần tiếp nối của **115. 무결성 (Integrity)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **116-121. 관계대수 (Relational Algebra)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “116-121. 관계대수 (Relational Algebra)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 절차적인 언어 (Procedural Language). 질의에 대한 해를 구하기 위한 연산 순서 명시.
- **Select (σ):** 조건에 맞는 튜플 부분집합 추출 (행 추출).
- **Project (π):** 속성 리스트에 제시된 속성값 추출 (열 추출).
- **Join (⋈):** 두 릴레이션을 하나로 합침.
- **Division (÷):** 속성값을 모두 가진 튜플 추출.
- **교차곱 (Cartesian Product):** 두 릴레이션 튜플들의 모든 순서쌍. 카디널리티의 곱.
- **VI (Vietnamese) (Tiếng Việt):** Đại số quan hệ (Ngôn ngữ thủ tục).
  - Select (σ): Lọc hàng (hàng).
  - Project (π): Chọn cột (cột).
  - Join (⋈): Kết nối 2 bảng.
  - Division (÷): Chia quan hệ.

Như vậy, **116-121. 관계대수 (Relational Algebra)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **123-125. 정규화 (Normalization)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **123-125. 정규화 (Normalization)** nối từ **116-121. 관계대수 (Relational Algebra)** sang **179-182. 정규화와 이상 심화 (Normalization & Anomaly - Deep Dive)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 123-125. 정규화 (Normalization)

Sau khi đã đặt nền bằng **116-121. 관계대수 (Relational Algebra)**, ta chuyển sang **123-125. 정규화 (Normalization)**. Đây là mắt xích 17/54 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **123-125. 정규화 (Normalization)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “123-125. 정규화 (Normalization)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 데이터 중복을 배제하여 이상(Anomaly: 삽입, 삭제, 갱신 이상) 발생을 방지하는 과정. 논리적 설계 단계에서 수행.
- **1NF:** 도메인이 원자값 (Domain is Atomic).
- **2NF:** 부분적 함수 종속 제거 (Remove Partial Dependency).
- **3NF:** 이행적 함수 종속 제거 (Remove Transitive Dependency).
- **BCNF:** 결정자이면서 후보키가 아닌 것 제거.
- **4NF:** 다치 종속 제거 (Remove Multivalued Dependency).
- **5NF:** 조인 종속성 이용.
- **VI (Vietnamese) (Tiếng Việt):** Chuẩn hóa. Giảm thiểu dư thừa dữ liệu để ngăn ngừa dị thường (Anomaly).
- 💡 **Mẹo ghi nhớ:** Nguyên-Phần-Bắc-Quyết-Đa-Chung (Nguyên tử -> Từng phần -> Bắc cầu -> Quyết định -> Đa trị -> Chung).

Ta có thể khép mục **123-125. 정규화 (Normalization)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **179-182. 정규화와 이상 심화 (Normalization & Anomaly - Deep Dive)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **179-182. 정규화와 이상 심화 (Normalization & Anomaly - Deep Dive)** nối từ **123-125. 정규화 (Normalization)** sang **184-185. 반정규화 (Denormalization)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 179-182. 정규화와 이상 심화 (Normalization & Anomaly - Deep Dive)

Từ **123-125. 정규화 (Normalization)**, ta đã có điểm tựa để bước vào **179-182. 정규화와 이상 심화 (Normalization & Anomaly - Deep Dive)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 18/54 trước khi đi vào chi tiết.

Để đọc **179-182. 정규화와 이상 심화 (Normalization & Anomaly - Deep Dive)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “179-182. 정규화와 이상 심화 (Normalization & Anomaly - Deep Dive)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **정규화 목적 (180):** 데이터 중복 배제, 무결성 유지, 이상 발생 방지. 논리적 설계 단계 수행.
- **이상 (Anomaly - 181):**
  - 삽입 이상 (Insertion Anomaly): 원하지 않는 값까지 삽입해야 하는 현상.
  - 삭제 이상 (Deletion Anomaly): 의도치 않은 연쇄 삭제(Cascade).
  - 갱신 이상 (Update Anomaly): 일부만 갱신되어 정보 모순 발생.
- **정규화 단계 암기 요령 (182):** 두부이결다조 (도메인 원자값, 부분 함수 종속 제거, 이행적 함수 종속 제거, 결정자이면서 후보키 아닌 것 제거, 다치 종속 제거, 조인 종속).
- **VI (Vietnamese) (Tiếng Việt):** Chuẩn hóa và Dị thường dữ liệu (Sâu hơn).
  - Dị thường: Thêm (phải thêm dữ liệu không cần thiết), Xóa (bị mất dữ liệu liên quan), Sửa (cập nhật không đồng bộ gây mâu thuẫn).
  - Quy tắc ghi nhớ các chuẩn: Do-Bu-I-Gyeol-Da-Jo (Nguyên tử - Phần - Bắc cầu - Định thức - Đa trị - Kết nối).
- **Example:** 학번만 지우려다 이름과 학과 정보까지 다 지워지는 것이 '삭제 이상'. / Định xóa mã SV nhưng vô tình xóa luôn tên và khoa là 'Dị thường xóa'.

Điểm chốt của **179-182. 정규화와 이상 심화 (Normalization & Anomaly - Deep Dive)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **184-185. 반정규화 (Denormalization)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **184-185. 반정규화 (Denormalization)** nối từ **179-182. 정규화와 이상 심화 (Normalization & Anomaly - Deep Dive)** sang **16. 정규화(Normalization)와 이상 현상(Anomaly)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 184-185. 반정규화 (Denormalization)

Ở bước 19/54, **184-185. 반정규화 (Denormalization)** xuất hiện như phần tiếp nối của **179-182. 정규화와 이상 심화 (Normalization & Anomaly - Deep Dive)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **184-185. 반정규화 (Denormalization)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “184-185. 반정규화 (Denormalization)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 시스템 성능 향상을 위해 정규화 원칙을 의도적으로 위배 (통합, 중복, 분리).
- **방법:** 테이블 통합, 테이블 분할 (수평/수직 분할), 중복 테이블/속성 추가.
- **VI (Vietnamese) (Tiếng Việt):** Phi chuẩn hóa.
  - Cố tình phá vỡ quy tắc chuẩn hóa để tăng hiệu suất truy vấn.
  - Phương pháp: Gộp bảng, Chia bảng (ngang/dọc), Thêm cột/bảng dư thừa.
- **Example:** 조인(Join)을 피하기 위해 부서 테이블의 '부서명'을 사원 테이블에 중복 저장. / Thêm cột 'Tên phòng' vào bảng 'Nhân viên' để tránh phải Join.

Như vậy, **184-185. 반정규화 (Denormalization)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **16. 정규화(Normalization)와 이상 현상(Anomaly)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **16. 정규화(Normalization)와 이상 현상(Anomaly)** nối từ **184-185. 반정규화 (Denormalization)** sang **20. 쿼리 성능 최적화와 반정규화 (Tối ưu hóa Truy vấn và Phi chuẩn hóa)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 16. 정규화(Normalization)와 이상 현상(Anomaly)

Sau khi đã đặt nền bằng **184-185. 반정규화 (Denormalization)**, ta chuyển sang **16. 정규화(Normalization)와 이상 현상(Anomaly)**. Đây là mắt xích 20/54 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **16. 정규화(Normalization)와 이상 현상(Anomaly)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng là bằng chứng để so sánh các lựa chọn theo cùng tiêu chí, không phải danh sách cần học thuộc từng ô.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

**정규화 (Chuẩn hóa):** Quá trình chia nhỏ các bảng để giảm thiểu dư thừa dữ liệu và tránh các hiện tượng bất thường (이상 현상).

Ta bắt đầu phần nội dung bằng **이상 현상 (Anomaly - Bất thường)**. Hãy xác định **이상 현상 (Anomaly - Bất thường)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 이상 현상 (Anomaly - Bất thường)

Phần nguồn của **이상 현상 (Anomaly - Bất thường)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “이상 현상 (Anomaly - Bất thường)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **삽입 이상 (Insertion Anomaly):** Lỗi khi thêm dữ liệu (phải thêm các dữ liệu không mong muốn).
- **갱신 이상 (Update Anomaly):** Lỗi khi cập nhật (cập nhật thiếu sót dẫn đến dữ liệu không nhất quán).
- **삭제 이상 (Deletion Anomaly):** Lỗi 연쇄 삭제 (Xóa dây chuyền) (xóa một dữ liệu kéo theo mất luôn dữ liệu quan trọng khác).

Các bullet của **이상 현상 (Anomaly - Bất thường)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **이상 현상 (Anomaly - Bất thường)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **정규화 단계 (Các chuẩn - Bắt buộc học thuộc)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **정규화 단계 (Các chuẩn - Bắt buộc học thuộc)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 정규화 단계 (Các chuẩn - Bắt buộc học thuộc)

Các ý ngay dưới **정규화 단계 (Các chuẩn - Bắt buộc học thuộc)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “정규화 단계 (Các chuẩn - Bắt buộc học thuộc)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

| 정규형 (Chuẩn) | 조건 (Điều kiện để đạt được) | Mẹo ghi nhớ (VN) |
|---|---|---|
| **1NF** | **도**메인이 **원자값** (Mọi giá trị phải là Nguyên tử) | **도** (Do - Domain nguyên tử) |
| **2NF** | **부**분 함수 종속 제거 (Loại bỏ phụ thuộc hàm từng phần) | **부** (Bu - Bỏ phụ thuộc phần) |
| **3NF** | **이**행 함수 종속 제거 (Loại bỏ phụ thuộc hàm bắc cầu: A→B, B→C => A→C) | **이** (I - Loại bắc cầu / I-haeng) |
| **BCNF** | 모든 **결**정자가 후보키 (Tất cả yếu tố quyết định phải là Khóa ứng viên) | **결** (Gyeol - BCNF) |
| **4NF** | **다**치 종속 제거 (Loại bỏ phụ thuộc đa trị) | **다** (Da - Đa trị) |
| **5NF** | **조**인 종속 제거 (Loại bỏ phụ thuộc Join) | **조** (Jo - Join) |

> 💡 **Mẹo ghi nhớ:** **Đồ-Bếp-I-Kết-Đa-Giò** (Đô-main, Bếp-Phần, I-Bắc cầu, Kết-Quyết định, Đa trị, Giò-Chung).

---

Bảng trong **정규화 단계 (Các chuẩn - Bắt buộc học thuộc)** không phải danh sách rời. Hãy đọc theo từng cột để nhận ra tiêu chí so sánh, rồi tự diễn đạt bằng một câu: đối tượng nào khác nhau ở điểm nào và trong điều kiện nào sự khác biệt đó có ý nghĩa.

Điểm chốt của **정규화 단계 (Các chuẩn - Bắt buộc học thuộc)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **16. 정규화(Normalization)와 이상 현상(Anomaly)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **20. 쿼리 성능 최적화와 반정규화 (Tối ưu hóa Truy vấn và Phi chuẩn hóa)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **20. 쿼리 성능 최적화와 반정규화 (Tối ưu hóa Truy vấn và Phi chuẩn hóa)** nối từ **16. 정규화(Normalization)와 이상 현상(Anomaly)** sang **130-132. 트랜잭션 (Transaction)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 20. 쿼리 성능 최적화와 반정규화 (Tối ưu hóa Truy vấn và Phi chuẩn hóa)

Từ **16. 정규화(Normalization)와 이상 현상(Anomaly)**, ta đã có điểm tựa để bước vào **20. 쿼리 성능 최적화와 반정규화 (Tối ưu hóa Truy vấn và Phi chuẩn hóa)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 21/54 trước khi đi vào chi tiết.

Để đọc **20. 쿼리 성능 최적화와 반정규화 (Tối ưu hóa Truy vấn và Phi chuẩn hóa)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **쿼리 성능 최적화 (Query Optimization)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 쿼리 성능 최적화 (Query Optimization)

Các ý ngay dưới **쿼리 성능 최적화 (Query Optimization)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Tối ưu hóa tốc độ chạy SQL thông qua **Optimizer (옵티마이저 - Bộ tối ưu)**.
- **RBO (Rule-Based Optimizer):** Tối ưu theo **규칙 (Quy tắc)** định sẵn. Phụ thuộc vào kinh nghiệm người lập trình.
- **CBO (Cost-Based Optimizer):** Tối ưu theo **비용 (Chi phí)** ước tính dựa trên thống kê dữ liệu. Rất thông minh và phổ biến hiện nay.
- **APM (Application Performance Management):** Công cụ giám sát hiệu suất ứng dụng.

Các bullet của **쿼리 성능 최적화 (Query Optimization)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **쿼리 성능 최적화 (Query Optimization)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **반정규화 (Denormalization - Phi chuẩn hóa)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **반정규화 (Denormalization - Phi chuẩn hóa)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 반정규화 (Denormalization - Phi chuẩn hóa)

Bây giờ ta đi vào nội dung của **반정규화 (Denormalization - Phi chuẩn hóa)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “반정규화 (Denormalization - Phi chuẩn hóa)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개념:** Cố tình phá vỡ chuẩn hóa (Gộp bảng, thêm dữ liệu trùng lặp).
- **목적:** Để **tăng hiệu suất truy vấn (조회 속도 향상)** khi thao tác JOIN quá nhiều.
- **단점:** Đánh đổi bằng sự **suy giảm tính nhất quán** (데이터 정합성 저하) và khó khăn khi cập nhật dữ liệu.

---

Các bullet của **반정규화 (Denormalization - Phi chuẩn hóa)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **반정규화 (Denormalization - Phi chuẩn hóa)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **20. 쿼리 성능 최적화와 반정규화 (Tối ưu hóa Truy vấn và Phi chuẩn hóa)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **130-132. 트랜잭션 (Transaction)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **130-132. 트랜잭션 (Transaction)** nối từ **20. 쿼리 성능 최적화와 반정규화 (Tối ưu hóa Truy vấn và Phi chuẩn hóa)** sang **187-189. 트랜잭션의 상태와 특성 (Transaction State & ACID)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 130-132. 트랜잭션 (Transaction)

Ở bước 22/54, **130-132. 트랜잭션 (Transaction)** xuất hiện như phần tiếp nối của **20. 쿼리 성능 최적화와 반정규화 (Tối ưu hóa Truy vấn và Phi chuẩn hóa)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **130-132. 트랜잭션 (Transaction)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “130-132. 트랜잭션 (Transaction)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 데이터베이스 상태를 변환시키는 논리적 작업의 단위.
- **ACID 특성:**
  - **Atomicity (원자성):** 모두 반영되거나(Commit) 전혀 반영되지 않아야 함(Rollback).
  - **Consistency (일관성):** 성공 시 일관성 있는 상태 유지.
  - **Isolation (독립성/격리성):** 다른 트랜잭션의 연산이 끼어들 수 없음.
  - **Durability (영속성):** 성공한 결과는 시스템 고장에도 영구 반영.
- **VI (Vietnamese) (Tiếng Việt):** Giao dịch (Transaction) & Tính chất ACID.
  - Atomicity (Tính nguyên tử): Tất cả hoặc không có gì.
  - Consistency (Tính nhất quán): Giữ trạng thái nhất quán.
  - Isolation (Tính độc lập): Không bị can thiệp bởi giao dịch khác.
  - Durability (Tính bền vững): Lưu trữ vĩnh viễn dù có lỗi hệ thống.

Như vậy, **130-132. 트랜잭션 (Transaction)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **187-189. 트랜잭션의 상태와 특성 (Transaction State & ACID)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **187-189. 트랜잭션의 상태와 특성 (Transaction State & ACID)** nối từ **130-132. 트랜잭션 (Transaction)** sang **9. 인덱스와 트랜잭션 (Index và Giao dịch)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 187-189. 트랜잭션의 상태와 특성 (Transaction State & ACID)

Sau khi đã đặt nền bằng **130-132. 트랜잭션 (Transaction)**, ta chuyển sang **187-189. 트랜잭션의 상태와 특성 (Transaction State & ACID)**. Đây là mắt xích 23/54 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **187-189. 트랜잭션의 상태와 특성 (Transaction State & ACID)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “187-189. 트랜잭션의 상태와 특성 (Transaction State & ACID)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **상태 (188):** 활동(Active) -> [부분 완료(Partially Committed) -> 완료(Committed)] 또는 [실패(Failed) -> 철회(Aborted/Rollback)].
- **특성 (189):** 원자성(Atomicity - 전부 또는 전무), 일관성(Consistency), 독립성(Isolation - 병행 중 간섭 불가), 영속성(Durability).
- **VI (Vietnamese) (Tiếng Việt):** Trạng thái và tính chất giao dịch.
  - Trạng thái: Đang chạy -> Hoàn thành một phần -> Commit HOẶC Lỗi -> Rollback.

Ta có thể khép mục **187-189. 트랜잭션의 상태와 특성 (Transaction State & ACID)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **9. 인덱스와 트랜잭션 (Index và Giao dịch)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **9. 인덱스와 트랜잭션 (Index và Giao dịch)** nối từ **187-189. 트랜잭션의 상태와 특성 (Transaction State & ACID)** sang **10. 트랜잭션 관리 기법 및 제어 (Quản lý và điều khiển giao dịch)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 9. 인덱스와 트랜잭션 (Index và Giao dịch)

Từ **187-189. 트랜잭션의 상태와 특성 (Transaction State & ACID)**, ta đã có điểm tựa để bước vào **9. 인덱스와 트랜잭션 (Index và Giao dịch)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 24/54 trước khi đi vào chi tiết.

Để đọc **9. 인덱스와 트랜잭션 (Index và Giao dịch)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng là bằng chứng để so sánh các lựa chọn theo cùng tiêu chí, không phải danh sách cần học thuộc từng ô.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **인덱스 (Index - Chỉ mục)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 인덱스 (Index - Chỉ mục)

Các ý ngay dưới **인덱스 (Index - Chỉ mục)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Dùng để tăng tốc độ tìm kiếm.
- **트리 기반 (Tree-based):** Thường dùng B-Tree, tốt cho tìm theo khoảng.
- **해시 (Hash):** Dùng Key-Value, truy cập nhanh và chi phí đồng đều, không tốt cho tìm khoảng.
- **비트맵 (Bitmap):** Dùng bit 0 và 1, phù hợp cho cột có ít giá trị khác biệt (Gender: M/F).
- **클러스터드 인덱스 (Clustered Index):** Dữ liệu thực sự được sắp xếp vật lý theo thứ tự Index. Rất tốt để tìm khoảng (Range search).

Các bullet của **인덱스 (Index - Chỉ mục)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **인덱스 (Index - Chỉ mục)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **트랜잭션 (Transaction - Giao dịch) - ACID** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **트랜잭션 (Transaction - Giao dịch) - ACID**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 트랜잭션 (Transaction - Giao dịch) - ACID

Bây giờ ta đi vào nội dung của **트랜잭션 (Transaction - Giao dịch) - ACID**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “트랜잭션 (Transaction - Giao dịch) - ACID” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

| 특징 (Đặc tính) | 설명 (Mô tả) | Ý nghĩa (VN) |
|---|---|---|
| **원자성 (Atomicity)** | All or Nothing (모두 반영되거나 전혀 반영되지 않음). | **Tính nguyên tử:** Chuyển tiền: hoặc cả 2 người cùng cập nhật, hoặc không ai thay đổi gì. Dùng Commit/Rollback. |
| **일관성 (Consistency)** | 일관적인 DB 상태 유지 (Trạng thái DB nhất quán). | **Tính nhất quán:** Dữ liệu sau giao dịch phải hợp lệ. |
| **고립성 (Isolation)** | 서로 간섭 불가 (Không can thiệp lẫn nhau). | **Tính cô lập:** Khi giao dịch A đang chạy, giao dịch B không thể nhảy vào làm sai lệch. |
| **영속성 (Durability)** | 영구적으로 결과 저장 (Lưu kết quả vĩnh viễn). | **Tính bền vững:** Sau khi COMMIT, dù sập nguồn dữ liệu vẫn tồn tại. |

> 💡 **Mẹo ghi nhớ:** **ACID** (Nguyên tử - Nhất quán - Cô lập - Bền vững).

---

Bảng trong **트랜잭션 (Transaction - Giao dịch) - ACID** không phải danh sách rời. Hãy đọc theo từng cột để nhận ra tiêu chí so sánh, rồi tự diễn đạt bằng một câu: đối tượng nào khác nhau ở điểm nào và trong điều kiện nào sự khác biệt đó có ý nghĩa.

Điểm chốt của **트랜잭션 (Transaction - Giao dịch) - ACID** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **9. 인덱스와 트랜잭션 (Index và Giao dịch)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **10. 트랜잭션 관리 기법 및 제어 (Quản lý và điều khiển giao dịch)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **10. 트랜잭션 관리 기법 및 제어 (Quản lý và điều khiển giao dịch)** nối từ **9. 인덱스와 트랜잭션 (Index và Giao dịch)** sang **143-145. SQL 분류 (SQL Categories)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. 트랜잭션 관리 기법 및 제어 (Quản lý và điều khiển giao dịch)

Ở bước 25/54, **10. 트랜잭션 관리 기법 및 제어 (Quản lý và điều khiển giao dịch)** xuất hiện như phần tiếp nối của **9. 인덱스와 트랜잭션 (Index và Giao dịch)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **10. 트랜잭션 관리 기법 및 제어 (Quản lý và điều khiển giao dịch)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **병행제어 기법 (Concurrency Control - Kiểm soát đồng thời)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **병행제어 기법 (Concurrency Control - Kiểm soát đồng thời)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 병행제어 기법 (Concurrency Control - Kiểm soát đồng thời)

Bây giờ ta đi vào nội dung của **병행제어 기법 (Concurrency Control - Kiểm soát đồng thời)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “병행제어 기법 (Concurrency Control - Kiểm soát đồng thời)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **로킹 (Locking):** Khóa tài nguyên để đảm bảo giao dịch chạy tuần tự (직렬화).
  - *Đơn vị khóa (Locking Unit):* Càng lớn (DB, Bảng) -> Ít Lock, Overhead nhỏ, Tính đồng thời giảm. Càng nhỏ (Bản ghi, Trường) -> Nhiều Lock, Overhead lớn, Tính đồng thời cao.
- **타임스탬프 (Time Stamping):** Gắn mốc thời gian để ưu tiên.
- **다중버전 동시제어 (MVCC):** Giữ nhiều phiên bản dữ liệu.
- **낙관적 병행제어 (Optimistic):** Cứ cho chạy đi, kết thúc mới kiểm tra lỗi (thích hợp môi trường ít xung đột).

Các bullet của **병행제어 기법 (Concurrency Control - Kiểm soát đồng thời)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **병행제어 기법 (Concurrency Control - Kiểm soát đồng thời)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **트랜잭션 상태 (Trạng thái giao dịch)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **트랜잭션 상태 (Trạng thái giao dịch)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 트랜잭션 상태 (Trạng thái giao dịch)

Phần nguồn của **트랜잭션 상태 (Trạng thái giao dịch)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “트랜잭션 상태 (Trạng thái giao dịch)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **활동 (Active):** Đang chạy.
- **부분 완료 (Partially Committed):** Đã chạy lệnh xong, chuẩn bị COMMIT nhưng chưa ghi lên đĩa.
- **완료 (Committed):** Thành công và lưu vĩnh viễn.
- **실패 (Failed):** Có lỗi xảy ra.
- **철회 (Aborted):** Bị hủy bỏ (Rollback).

Các bullet của **트랜잭션 상태 (Trạng thái giao dịch)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **트랜잭션 상태 (Trạng thái giao dịch)**, đừng bắt đầu lại từ số không. **데이터 사전 (Data Dictionary / System Catalog / Metadata)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **데이터 사전 (Data Dictionary / System Catalog / Metadata)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 데이터 사전 (Data Dictionary / System Catalog / Metadata)

Các ý ngay dưới **데이터 사전 (Data Dictionary / System Catalog / Metadata)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “데이터 사전 (Data Dictionary / System Catalog / Metadata)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- Lưu thông tin về các đối tượng (bảng, view, index...).
- DBMS tự động cập nhật, người dùng **chỉ được Read Only (조회만 가능)**.

---

Các bullet của **데이터 사전 (Data Dictionary / System Catalog / Metadata)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **데이터 사전 (Data Dictionary / System Catalog / Metadata)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Như vậy, **10. 트랜잭션 관리 기법 및 제어 (Quản lý và điều khiển giao dịch)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **143-145. SQL 분류 (SQL Categories)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **143-145. SQL 분류 (SQL Categories)** nối từ **10. 트랜잭션 관리 기법 및 제어 (Quản lý và điều khiển giao dịch)** sang **3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 143-145. SQL 분류 (SQL Categories)

Sau khi đã đặt nền bằng **10. 트랜잭션 관리 기법 및 제어 (Quản lý và điều khiển giao dịch)**, ta chuyển sang **143-145. SQL 분류 (SQL Categories)**. Đây là mắt xích 26/54 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **143-145. SQL 분류 (SQL Categories)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “143-145. SQL 분류 (SQL Categories)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **DDL (데이터 정의어):** CREATE, ALTER, DROP (스키마, 테이블 등 정의/변경/삭제).
- **DML (데이터 조작어):** SELECT, INSERT, DELETE, UPDATE (데이터 조회 및 변경).
- **DCL (데이터 제어어):** GRANT, REVOKE (권한 제어).
- **TCL (트랜잭션 제어어):** COMMIT, ROLLBACK, SAVEPOINT (트랜잭션 제어).
- **VI (Vietnamese) (Tiếng Việt):** Phân loại SQL.
  - DDL (Định nghĩa dữ liệu): CREATE, ALTER, DROP.
  - DML (Thao tác dữ liệu): SELECT, INSERT, DELETE, UPDATE.
  - DCL (Điều khiển dữ liệu): GRANT, REVOKE (điều khiển quyền).
  - TCL (Điều khiển giao dịch): COMMIT, ROLLBACK, SAVEPOINT (điều khiển giao dịch).

Ta có thể khép mục **143-145. SQL 분류 (SQL Categories)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **143-145. SQL 분류 (SQL Categories)** đặt vấn đề; **3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)** đối chiếu bằng chứng, rồi **4. SQL 문법의 종류 (Các loại cú pháp SQL)** mở rộng hệ quả hoặc giới hạn liên quan.

## 3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)

Từ **143-145. SQL 분류 (SQL Categories)**, ta đã có điểm tựa để bước vào **3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 27/54 trước khi đi vào chi tiết.

Để đọc **3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng là bằng chứng để so sánh các lựa chọn theo cùng tiêu chí, không phải danh sách cần học thuộc từng ô.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

| 종류 (Loại) | 설명 (Mô tả) | Ví dụ & Giải thích (VN) |
|---|---|---|
| **트리거 (Trigger)** | 테이블 이벤트(Insert, Update, Delete)에 반응해 **자동**으로 실행되는 작업. (Thực thi tự động khi có sự kiện). | _Ví dụ:_ Khi xóa 1 nhân viên khỏi bảng NhânViên, một trigger tự động lưu thông tin nhân viên đó vào bảng NhanVien_NghiViec (Audit log). |
| **프로시저 (Procedure)** | 어떤 행동을 수행하기 위한 일련의 작업 순서. (Một chuỗi các thao tác lưu sẵn để thực thi chung). | _Ví dụ:_ Một procedure `Tinh_Luong_Thang` chạy cuối tháng để tính lương cho toàn bộ công ty. |
| **사용자 정의 함수 (User-Defined Function)** | 단일 값으로 반환할 수 있도록 수행. (Hàm do người dùng định nghĩa, trả về một giá trị duy nhất). | _Ví dụ:_ Hàm `GET_AGE(ngay_sinh)` tự động tính và trả về tuổi. |

---

Điểm chốt của **3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **4. SQL 문법의 종류 (Các loại cú pháp SQL)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)** đặt vấn đề; **4. SQL 문법의 종류 (Các loại cú pháp SQL)** đối chiếu bằng chứng, rồi **A+ Deep Dive: SQL 결과를 행 단위로 추적하기** mở rộng hệ quả hoặc giới hạn liên quan.

## 4. SQL 문법의 종류 (Các loại cú pháp SQL)

Ở bước 28/54, **4. SQL 문법의 종류 (Các loại cú pháp SQL)** xuất hiện như phần tiếp nối của **3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **4. SQL 문법의 종류 (Các loại cú pháp SQL)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng là bằng chứng để so sánh các lựa chọn theo cùng tiêu chí, không phải danh sách cần học thuộc từng ô.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “4. SQL 문법의 종류 (Các loại cú pháp SQL)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

| 종류 (Loại) | 명령어 (Lệnh) | 설명 & 역할 (Mô tả & Vai trò) | Giải thích (VN) |
|---|---|---|---|
| **DDL** (Data Definition Language) | CREATE, ALTER, DROP, TRUNCATE | 데이터베이스를 **정의**하는 언어, 구조 결정. (Ngôn ngữ định nghĩa dữ liệu - Cấu trúc). | Dùng để Tạo (CREATE), Sửa (ALTER), Xóa hoàn toàn (DROP), hoặc Xóa trắng (TRUNCATE) bảng. Giống như việc xây/đập một ngôi nhà. |
| **DML** (Data Manipulation Language) | SELECT, INSERT, UPDATE, DELETE | 저장된 자료를 조회, 삽입, 수정, 삭제. (Ngôn ngữ thao tác dữ liệu - Nội dung). | Dùng để Thêm, Sửa, Xóa, Lấy dữ liệu bên trong bảng. Giống như việc sắp xếp đồ đạc trong nhà. |
| **DCL** (Data Control Language) | GRANT, REVOKE | 데이터 보안과 권한 제어. (Ngôn ngữ điều khiển dữ liệu - Quyền). | Dùng để cấp quyền hoặc thu hồi quyền. |
| **TCL** (Transaction Control Language) | COMMIT, ROLLBACK, SAVEPOINT | 트랜잭션의 확정, 취소, 부분 복귀. (Ngôn ngữ điều khiển giao dịch). | Dùng để xác nhận, hoàn tác hoặc đặt điểm khôi phục giao dịch. |

> 💡 **Mẹo ghi nhớ:**
> DDL: **CADT** (Create, Alter, Drop, Truncate - "Cắt" cấu trúc).
> DML: **SUDI** (Select, Update, Delete, Insert - "Sửa đi" dữ liệu).
> DCL: **GR** (Grant, Revoke - "Gác quyền"). TCL: **CRS** (Commit, Rollback, Savepoint - "Chốt/Rút/Save").

---

Như vậy, **4. SQL 문법의 종류 (Các loại cú pháp SQL)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **A+ Deep Dive: SQL 결과를 행 단위로 추적하기**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **A+ Deep Dive: SQL 결과를 행 단위로 추적하기** nối từ **4. SQL 문법의 종류 (Các loại cú pháp SQL)** sang **150-155. 데이터 조작어 (DML) 확장 및 조건 연산자**, vì cơ chế trước tạo đầu vào cho bước sau.

## A+ Deep Dive: SQL 결과를 행 단위로 추적하기

Sau khi đã đặt nền bằng **4. SQL 문법의 종류 (Các loại cú pháp SQL)**, ta chuyển sang **A+ Deep Dive: SQL 결과를 행 단위로 추적하기**. Đây là mắt xích 29/54 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **A+ Deep Dive: SQL 결과를 행 단위로 추적하기** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng là bằng chứng để so sánh các lựa chọn theo cùng tiêu chí, không phải danh sách cần học thuộc từng ô.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **1. 샘플 스키마와 데이터**. Hãy xác định **1. 샘플 스키마와 데이터** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 1. 샘플 스키마와 데이터

Phần nguồn của **1. 샘플 스키마와 데이터** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “1. 샘플 스키마와 데이터” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

```sql
CREATE TABLE sales (
  dept CHAR(1), amount INT
);
INSERT INTO sales VALUES ('A', 120), ('A', 80), ('B', 90), ('B', 40);
```

Phần **1. 샘플 스키마와 데이터** không có nhiều dữ liệu rời để tách nhỏ, vì vậy hãy giữ câu hỏi mục đích và tự chốt bằng một câu giải thích trước khi đi tiếp.

Ta vừa chốt **1. 샘플 스키마와 데이터** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. WHERE와 HAVING의 순서** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **2. WHERE와 HAVING의 순서** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 2. WHERE와 HAVING의 순서

Các ý ngay dưới **2. WHERE와 HAVING의 순서** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “2. WHERE와 HAVING의 순서” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

```sql
SELECT dept, SUM(amount) AS total
FROM sales
WHERE amount >= 80
GROUP BY dept
HAVING SUM(amount) >= 150
ORDER BY total DESC;
```

행 필터를 먼저 적용하면 `(A,120)`, `(A,80)`, `(B,90)`만 남는다. 그룹별 합계는
`A=200`, `B=90`이므로 `HAVING`을 통과하는 최종 결과는 `A | 200` 한 행이다.

- `WHERE`: 그룹화 **전** 개별 행을 제거.
- `GROUP BY`: 같은 키를 그룹으로 묶고 집계.
- `HAVING`: 그룹화 **후** 집계 결과를 제거.
- `ORDER BY`: 최종 결과의 표시 순서를 정함. 명시하지 않으면 순서를 가정하지 않는다.

> **시험 함정:** 집계 함수 조건을 `WHERE`에 넣지 않고 `HAVING`에 둔다. 별칭(alias)은 구현/문맥에 따라 `WHERE`에서 바로 사용할 수 없으므로 원래 표현식을 확인한다.

Các bullet của **2. WHERE와 HAVING의 순서** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **2. WHERE와 HAVING의 순서**, đừng bắt đầu lại từ số không. **자주 혼동하는 판별 포인트** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **자주 혼동하는 판별 포인트**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 자주 혼동하는 판별 포인트

Bây giờ ta đi vào nội dung của **자주 혼동하는 판별 포인트**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “자주 혼동하는 판별 포인트” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `GRANT`/`REVOKE`는 권한을 다루는 **DCL**, `COMMIT`/`ROLLBACK`/`SAVEPOINT`는 트랜잭션을 다루는 **TCL**이다.
- 로킹 단위를 작게 하면 동시성·공유도는 커지지만 잠금 관리 오버헤드도 증가한다. 작은 단위가 교착상태를 자동으로 제거하지는 않는다.
- 2NF는 부분 함수 종속, 3NF는 이행 함수 종속, BCNF는 모든 결정자가 후보키여야 한다는 조건으로 구별한다.
- 뷰는 보안·논리적 독립성에 활용할 수 있지만, 갱신 가능 여부는 정의 방식과 제약에 따라 달라지고 일반적으로 독립 인덱스를 갖지 않는다.

Các bullet của **자주 혼동하는 판별 포인트** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **자주 혼동하는 판별 포인트** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Ta có thể khép mục **A+ Deep Dive: SQL 결과를 행 단위로 추적하기** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **150-155. 데이터 조작어 (DML) 확장 및 조건 연산자**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **150-155. 데이터 조작어 (DML) 확장 및 조건 연산자** nối từ **A+ Deep Dive: SQL 결과를 행 단위로 추적하기** sang **193. 뷰 (View)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 150-155. 데이터 조작어 (DML) 확장 및 조건 연산자

Từ **A+ Deep Dive: SQL 결과를 행 단위로 추적하기**, ta đã có điểm tựa để bước vào **150-155. 데이터 조작어 (DML) 확장 및 조건 연산자**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 30/54 trước khi đi vào chi tiết.

Để đọc **150-155. 데이터 조작어 (DML) 확장 및 조건 연산자** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng cho ta tiêu chí đối chiếu, còn công thức cho ta quan hệ giữa các đại lượng; hãy dùng cả hai để kiểm tra cùng một kết luận.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “150-155. 데이터 조작어 (DML) 확장 및 조건 연산자” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **DELETE (150):** 튜플을 삭제. `DELETE FROM 테이블명 [WHERE 조건];`
- **UPDATE (151):** 튜플 내용 변경. `UPDATE 테이블명 SET 속성명 = 데이터 [WHERE 조건];`
- **SELECT (152, 153):** 데이터 검색. `SELECT [DISTINCT] 속성명 FROM 테이블명 [WHERE] [GROUP BY] [HAVING] [ORDER BY ASC|DESC];`
- **LIKE (154):** 문자 패턴 일치 검색.
  - `%`: 모든 문자
  - `_`: 문자 하나
  - `#`: 숫자 하나
- **BETWEEN (155):** 두 숫자 사이의 값 검색.
- **VI (Vietnamese) (Tiếng Việt):** Mở rộng DML và toán tử điều kiện.
  - DELETE: Xóa dữ liệu (hàng).
  - UPDATE: Cập nhật dữ liệu.
  - SELECT: Truy vấn dữ liệu (DISTINCT: Loại bỏ trùng lặp).
  - LIKE: Tìm kiếm theo mẫu ký tự. `%` đại diện cho chuỗi, `_` đại diện 1 ký tự, `#` đại diện 1 số.
  - BETWEEN: Trong khoảng giá trị.
- **Example:** `SELECT * FROM 학생 WHERE 이름 LIKE '김%';` / Tìm tất cả sinh viên có tên bắt đầu bằng họ 'Kim' (김).

Điểm chốt của **150-155. 데이터 조작어 (DML) 확장 및 조건 연산자** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **193. 뷰 (View)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **193. 뷰 (View)** nối từ **150-155. 데이터 조작어 (DML) 확장 및 조건 연산자** sang **8. 서브쿼리와 뷰 (Truy vấn con và View)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 193. 뷰 (View)

Ở bước 31/54, **193. 뷰 (View)** xuất hiện như phần tiếp nối của **150-155. 데이터 조작어 (DML) 확장 및 조건 연산자**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **193. 뷰 (View)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “193. 뷰 (View)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 기본 테이블로부터 유도된 가상 테이블 (물리적 구현 X).
- 장점: 논리적 데이터 독립성, 보안 강화. 단점: 인덱스 불가, 뷰 정의 변경 불가, 갱신 제약.
- **VI (Vietnamese) (Tiếng Việt):** Khung nhìn (View). Bảng ảo. Ưu điểm: Độc lập dữ liệu, bảo mật. Nhược điểm: Không có index độc lập, khó cập nhật.

Như vậy, **193. 뷰 (View)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **8. 서브쿼리와 뷰 (Truy vấn con và View)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **8. 서브쿼리와 뷰 (Truy vấn con và View)** nối từ **193. 뷰 (View)** sang **191-192. 인덱스 (Index)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 8. 서브쿼리와 뷰 (Truy vấn con và View)

Sau khi đã đặt nền bằng **193. 뷰 (View)**, ta chuyển sang **8. 서브쿼리와 뷰 (Truy vấn con và View)**. Đây là mắt xích 32/54 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **8. 서브쿼리와 뷰 (Truy vấn con và View)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **서브쿼리 (Subquery)**. Hãy xác định **서브쿼리 (Subquery)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 서브쿼리 (Subquery)

Phần nguồn của **서브쿼리 (Subquery)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “서브쿼리 (Subquery)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **단일 행 서브쿼리 (Single-row Subquery):** Trả về 1 dòng. Dùng toán tử `=`, `>`, `<`.
- **다중 행 서브쿼리 (Multi-row Subquery):** Trả về nhiều dòng. Dùng `IN`, `ANY`, `ALL`.
- **인라인 뷰 (Inline View):** Subquery nằm trong mệnh đề `FROM`, tạo thành bảng ảo tạm thời.

Các bullet của **서브쿼리 (Subquery)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **서브쿼리 (Subquery)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **뷰 (VIEW - Bảng ảo)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **뷰 (VIEW - Bảng ảo)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 뷰 (VIEW - Bảng ảo)

Các ý ngay dưới **뷰 (VIEW - Bảng ảo)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “뷰 (VIEW - Bảng ảo)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `CREATE VIEW 뷰명 AS (SELECT문);`
- `DROP VIEW 뷰명;`
- **장점 (Ưu điểm):** Bảo mật (chỉ cho xem cột cần thiết), Đơn giản hóa truy vấn phức tạp, Đảm bảo tính toàn vẹn dữ liệu.
- **단점 (Nhược điểm):** Không thể sửa đổi cấu trúc dễ dàng, cơ bản là Read Only, **Không thể gắn Index (인덱스 불가능)**.

---

Các bullet của **뷰 (VIEW - Bảng ảo)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **뷰 (VIEW - Bảng ảo)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **8. 서브쿼리와 뷰 (Truy vấn con và View)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **191-192. 인덱스 (Index)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **191-192. 인덱스 (Index)** nối từ **8. 서브쿼리와 뷰 (Truy vấn con và View)** sang **136-137. 분산 데이터베이스 (Distributed DB)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 191-192. 인덱스 (Index)

Từ **8. 서브쿼리와 뷰 (Truy vấn con và View)**, ta đã có điểm tựa để bước vào **191-192. 인덱스 (Index)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 33/54 trước khi đi vào chi tiết.

Để đọc **191-192. 인덱스 (Index)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “191-192. 인덱스 (Index)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 데이터 접근을 빠르게 하기 위한 <키 값, 포인터> 구조. DDL로 제어. 트리 기반(B+ 트리), 비트맵, 함수 기반, 도메인 인덱스 등.
- **VI (Vietnamese) (Tiếng Việt):** Chỉ mục (Index). Cấu trúc <Khóa, Con trỏ> giúp truy cập nhanh. Sử dụng B+ Tree, Bitmap...

Điểm chốt của **191-192. 인덱스 (Index)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **136-137. 분산 데이터베이스 (Distributed DB)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **136-137. 분산 데이터베이스 (Distributed DB)** nối từ **191-192. 인덱스 (Index)** sang **195-196. 분산 데이터베이스 목표 (Distributed DB Goals)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 136-137. 분산 데이터베이스 (Distributed DB)

Ở bước 34/54, **136-137. 분산 데이터베이스 (Distributed DB)** xuất hiện như phần tiếp nối của **191-192. 인덱스 (Index)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **136-137. 분산 데이터베이스 (Distributed DB)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “136-137. 분산 데이터베이스 (Distributed DB)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 논리적으로는 하나이나 물리적으로 분산된 데이터베이스.
- **목표 (Goals):** 위치 투명성 (Location), 중복 투명성 (Replication), 병행 투명성 (Concurrency), 장애 투명성 (Failure).
- **VI (Vietnamese) (Tiếng Việt):** Cơ sở dữ liệu phân tán. Tính trong suốt về: Vị trí, Nhân bản, Đồng thời, Lỗi.

Như vậy, **136-137. 분산 데이터베이스 (Distributed DB)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **195-196. 분산 데이터베이스 목표 (Distributed DB Goals)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **195-196. 분산 데이터베이스 목표 (Distributed DB Goals)** nối từ **136-137. 분산 데이터베이스 (Distributed DB)** sang **197. 분산 데이터베이스의 장단점 (Distributed DB Pros/Cons)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 195-196. 분산 데이터베이스 목표 (Distributed DB Goals)

Sau khi đã đặt nền bằng **136-137. 분산 데이터베이스 (Distributed DB)**, ta chuyển sang **195-196. 분산 데이터베이스 목표 (Distributed DB Goals)**. Đây là mắt xích 35/54 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **195-196. 분산 데이터베이스 목표 (Distributed DB Goals)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “195-196. 분산 데이터베이스 목표 (Distributed DB Goals)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 위치 투명성(Location), 중복 투명성(Replication), 병행 투명성(Concurrency), 장애 투명성(Failure).
- **VI (Vietnamese) (Tiếng Việt):** Mục tiêu CSDL phân tán (Tính trong suốt về: vị trí, nhân bản, đồng thời, sự cố).

Ta có thể khép mục **195-196. 분산 데이터베이스 목표 (Distributed DB Goals)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **197. 분산 데이터베이스의 장단점 (Distributed DB Pros/Cons)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **197. 분산 데이터베이스의 장단점 (Distributed DB Pros/Cons)** nối từ **195-196. 분산 데이터베이스 목표 (Distributed DB Goals)** sang **17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 197. 분산 데이터베이스의 장단점 (Distributed DB Pros/Cons)

Từ **195-196. 분산 데이터베이스 목표 (Distributed DB Goals)**, ta đã có điểm tựa để bước vào **197. 분산 데이터베이스의 장단점 (Distributed DB Pros/Cons)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 36/54 trước khi đi vào chi tiết.

Để đọc **197. 분산 데이터베이스의 장단점 (Distributed DB Pros/Cons)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “197. 분산 데이터베이스의 장단점 (Distributed DB Pros/Cons)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **장점:** 지역 자치성, 자료 공유성 향상, 시스템 성능 및 신뢰성/가용성 향상.
- **단점:** 설계 및 소프트웨어 개발 어려움, 처리 비용 및 잠재적 오류 증가.
- **VI (Vietnamese) (Tiếng Việt):** Ưu nhược điểm của CSDL phân tán.
  - Ưu điểm: Độc lập cục bộ, tăng chia sẻ, tin cậy cao, dễ mở rộng.

---

- **반입 전략:** 요구 반입, 예상 반입.
- **배치 전략:** 최초 적합(First Fit), 최적 적합(Best Fit), 최악 적합(Worst Fit).
- **단편화 (Fragmentation):** 내부 단편화(남는 공간), 외부 단편화(들어갈 수 없는 작은 공간). 통합/압축으로 해결.
- **가상 기억장치 (Virtual Memory):** 페이징(동일 크기 분할, 내부 단편화 발생), 세그먼테이션(논리적 크기 분할, 외부 단편화 발생).
- **페이지 교체 알고리즘:** FIFO(먼저 들어온 것 교체), LRU(최근에 가장 오랫동안 사용 안 한 것 교체), LFU(사용 빈도 가장 적은 것 교체).
- **국부성 (Locality):** 시간 구역성(반복문, 스택), 공간 구역성(배열 순회).
- **스래싱 (Thrashing):** 페이지 부재가 너무 잦아 시스템 성능 저하. 워킹 셋(Working Set)으로 방지.
- **VI (Vietnamese) (Tiếng Việt):** Quản lý bộ nhớ.
  - Phân mảnh: Nội vi (còn dư), Ngoại vi (không đủ chỗ).
  - Bộ nhớ ảo: Phân trang (Paging - kích thước bằng nhau) và Phân đoạn (Segmentation - theo logic).
  - Thuật toán thay trang: FIFO, LRU, LFU. Thrashing xảy ra khi lỗi trang quá nhiều.

Điểm chốt của **197. 분산 데이터베이스의 장단점 (Distributed DB Pros/Cons)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)** nối từ **197. 분산 데이터베이스의 장단점 (Distributed DB Pros/Cons)** sang **18. 파티셔닝과 암호화 (Phân vùng và Mã hóa)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)

Ở bước 37/54, **17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)** xuất hiện như phần tiếp nối của **197. 분산 데이터베이스의 장단점 (Distributed DB Pros/Cons)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **스토리지 (Storage - Thiết bị lưu trữ)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **스토리지 (Storage - Thiết bị lưu trữ)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 스토리지 (Storage - Thiết bị lưu trữ)

Bây giờ ta đi vào nội dung của **스토리지 (Storage - Thiết bị lưu trữ)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “스토리지 (Storage - Thiết bị lưu trữ)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **DAS (Direct Attached Storage):** Kết nối trực tiếp bằng cáp. Nhanh, an toàn nhưng khó mở rộng.
- **NAS (Network Attached Storage):** Kết nối qua mạng (Network-based, File-level). Mềm dẻo nhưng có thể nghẽn mạng.
- **SAN (Storage Area Network):** Dùng cáp quang (Fiber Channel), tốc độ cực cao, đắt tiền.
- **SDS (Software-defined Storage):** Quản lý toàn bộ tài nguyên lưu trữ bằng phần mềm (Ảo hóa lưu trữ).

Các bullet của **스토리지 (Storage - Thiết bị lưu trữ)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **스토리지 (Storage - Thiết bị lưu trữ)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **분산 데이터베이스 (Distributed Database - CSDL Phân tán)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **분산 데이터베이스 (Distributed Database - CSDL Phân tán)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 분산 데이터베이스 (Distributed Database - CSDL Phân tán)

Phần nguồn của **분산 데이터베이스 (Distributed Database - CSDL Phân tán)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Dữ liệu phân bố ở nhiều nơi (máy chủ khác nhau) nhưng người dùng cảm giác như đang dùng 1 CSDL duy nhất.
- **장점 (Ưu điểm):** Đáng tin cậy, dễ mở rộng, tính tự trị khu vực cao.
- **단점 (Nhược điểm):** Thiết kế khó, chi phí cao, bảo mật phức tạp.

**4대 투명성 (4 Đặc tính Trong suốt - Transparency):**
1. **위치 투명성 (Location):** Người dùng không cần biết dữ liệu nằm ở máy chủ nào.
2. **중복(복제) 투명성 (Replication):** Không cần biết dữ liệu được nhân bản ra sao.
3. **병행 투명성 (Concurrency):** Nhiều người truy cập cùng lúc vẫn không bị lỗi kết quả.
4. **장애 투명성 (Failure):** Một Node chết, toàn hệ thống vẫn hoạt động bình thường.

---

Các bullet của **분산 데이터베이스 (Distributed Database - CSDL Phân tán)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **분산 데이터베이스 (Distributed Database - CSDL Phân tán)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Như vậy, **17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **18. 파티셔닝과 암호화 (Phân vùng và Mã hóa)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **18. 파티셔닝과 암호화 (Phân vùng và Mã hóa)** nối từ **17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)** sang **19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18. 파티셔닝과 암호화 (Phân vùng và Mã hóa)

Sau khi đã đặt nền bằng **17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)**, ta chuyển sang **18. 파티셔닝과 암호화 (Phân vùng và Mã hóa)**. Đây là mắt xích 38/54 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **18. 파티셔닝과 암호화 (Phân vùng và Mã hóa)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **파티셔닝 (Partitioning)**. Hãy xác định **파티셔닝 (Partitioning)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 파티셔닝 (Partitioning)

Phần nguồn của **파티셔닝 (Partitioning)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Chia các bảng lớn thành các phần nhỏ (Partition) để dễ quản lý và tăng hiệu suất.
- **범위 분할 (Range):** Phân chia theo khoảng (VD: Tháng 1, Tháng 2).
- **해시 분할 (Hash):** Dùng hàm băm để chia đều. Dữ liệu phân bố đều nhưng khó tìm theo khoảng.
- **목록 분할 (List):** Phân chia theo danh sách giá trị (VD: Nước: VN, KR, US).
- **조합 분할 (Composite):** Kết hợp các phương pháp trên.
- **라운드 로빈 (Round Robin):** Chia xoay vòng đều nhau tuần tự (Không cần khóa).

Các bullet của **파티셔닝 (Partitioning)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **파티셔닝 (Partitioning)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **데이터베이스 암호화 (Mã hóa CSDL)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **데이터베이스 암호화 (Mã hóa CSDL)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 데이터베이스 암호화 (Mã hóa CSDL)

Các ý ngay dưới **데이터베이스 암호화 (Mã hóa CSDL)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “데이터베이스 암호화 (Mã hóa CSDL)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **암호화 (Encryption):** Biến 평문 (Plaintext - Văn bản gốc) thành 암호문 (Ciphertext - Bản mã).
- **복호화 (Decryption):** Giải mã từ Ciphertext về Plaintext.
- **키 (Key):** Chìa khóa dùng để mã hóa và giải mã.
---

Các bullet của **데이터베이스 암호화 (Mã hóa CSDL)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **데이터베이스 암호화 (Mã hóa CSDL)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **18. 파티셔닝과 암호화 (Phân vùng và Mã hóa)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)** nối từ **18. 파티셔닝과 암호화 (Phân vùng và Mã hóa)** sang **106-107. 튜플(Tuple)과 속성(Attribute)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)

Từ **18. 파티셔닝과 암호화 (Phân vùng và Mã hóa)**, ta đã có điểm tựa để bước vào **19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 39/54 trước khi đi vào chi tiết.

Để đọc **19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng cho ta tiêu chí đối chiếu, còn công thức cho ta quan hệ giữa các đại lượng; hãy dùng cả hai để kiểm tra cùng một kết luận.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **개인키 암호 방식 (Private Key / Symmetric Key - Mã hóa Khóa đối xứng)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 개인키 암호 방식 (Private Key / Symmetric Key - Mã hóa Khóa đối xứng)

Các ý ngay dưới **개인키 암호 방식 (Private Key / Symmetric Key - Mã hóa Khóa đối xứng)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “개인키 암호 방식 (Private Key / Symmetric Key - Mã hóa Khóa đối xứng)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개념 (Khái niệm):** Dùng **CÙNG MỘT KHÓA** để mã hóa và giải mã (단일키 - Khóa đơn).
- **장점 (Ưu điểm):** Tốc độ xử lý cực kỳ nhanh.
- **단점 (Nhược điểm):** Khó phân phối và quản lý khóa khi có quá nhiều người dùng.
- **종류 (Thuật toán tiêu biểu):** DES, AES, SEED, ARIA. (Chia làm 2 dạng: Block - theo khối, Stream - theo luồng bit).

> 💡 **Mẹo ghi nhớ:** **Đối-Cá-Nhanh-Khó** (Khóa Đối xứng = Khóa Cá nhân = Nhanh = Khó quản lý khóa).

Với **개인키 암호 방식 (Private Key / Symmetric Key - Mã hóa Khóa đối xứng)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **개인키 암호 방식 (Private Key / Symmetric Key - Mã hóa Khóa đối xứng)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **접근통제 기술 (Access Control - Kỹ thuật kiểm soát truy cập)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **접근통제 기술 (Access Control - Kỹ thuật kiểm soát truy cập)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 접근통제 기술 (Access Control - Kỹ thuật kiểm soát truy cập)

Bây giờ ta đi vào nội dung của **접근통제 기술 (Access Control - Kỹ thuật kiểm soát truy cập)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “접근통제 기술 (Access Control - Kỹ thuật kiểm soát truy cập)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

| 종류 (Loại) | 기준 (Tiêu chí) | 특징 (Đặc điểm VN) |
|---|---|---|
| **DAC (임의 접근통제)** | 소유자 (Chủ sở hữu) | Chủ dữ liệu tự do cấp/thu quyền (GRANT/REVOKE). |
| **MAC (강제 접근통제)** | 보안 등급 (Mức độ bảo mật) | Hệ thống ép buộc dựa trên cấp độ bảo mật (VD: Top Secret). |
| **RBAC (역할기반 접근통제)** | 역할 (Vai trò) | Quyền gắn với chức vụ (VD: Manager, Staff). Đổi chức vụ = tự đổi quyền. |

Khi đọc **접근통제 기술 (Access Control - Kỹ thuật kiểm soát truy cập)**, hãy tách hai lớp: bảng giúp đối chiếu các loại hoặc tiêu chí, còn công thức cần được đọc theo biến, đơn vị và quan hệ giữa các đại lượng. Cách tách này giúp ta hiểu cơ chế trước khi ghi nhớ ký hiệu.

Sau khi đọc **접근통제 기술 (Access Control - Kỹ thuật kiểm soát truy cập)**, đừng bắt đầu lại từ số không. **MAC 보안 모델 (Các mô hình bảo mật của MAC)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **MAC 보안 모델 (Các mô hình bảo mật của MAC)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### MAC 보안 모델 (Các mô hình bảo mật của MAC)

Phần nguồn của **MAC 보안 모델 (Các mô hình bảo mật của MAC)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “MAC 보안 모델 (Các mô hình bảo mật của MAC)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **벨-라파듈라 (Bell-LaPadula):** Tập trung vào **기밀성 (Tính Bảo mật / Kín đáo)** (Quân đội). Không đọc lên trên, Không ghi xuống dưới.
- **비바 (Biba):** Tập trung vào **무결성 (Tính Toàn vẹn)**. Ngăn chặn việc sửa đổi trái phép.
- **클락-윌슨 (Clark-Wilson):** Dành cho thương mại, chỉ cho phép sửa qua phần mềm được ủy quyền.
- **만리장성 (Chinese Wall):** Tránh xung đột lợi ích (người xem hồ sơ công ty A thì không được xem của đối thủ B).

---

Các bullet của **MAC 보안 모델 (Các mô hình bảo mật của MAC)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **MAC 보안 모델 (Các mô hình bảo mật của MAC)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Điểm chốt của **19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **106-107. 튜플(Tuple)과 속성(Attribute)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **106-107. 튜플(Tuple)과 속성(Attribute)** nối từ **19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)** sang **108. 도메인 (Domain)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 106-107. 튜플(Tuple)과 속성(Attribute)

Ở bước 40/54, **106-107. 튜플(Tuple)과 속성(Attribute)** xuất hiện như phần tiếp nối của **19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **106-107. 튜플(Tuple)과 속성(Attribute)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “106-107. 튜플(Tuple)과 속성(Attribute)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **튜플 (Tuple):** 릴레이션을 구성하는 행(Row). 튜플의 수 = 카디널리티 (Cardinality).
- **속성 (Attribute):** 데이터베이스를 구성하는 가장 작은 논리적 단위. 열(Column). 속성의 수 = 디그리 (Degree).
- **VI (Vietnamese) (Tiếng Việt):** Tuple (Hàng) và Attribute (Cột).
  - Tuple: Hàng. Số hàng = Cardinality.
  - Attribute: Cột, đơn vị logic nhỏ nhất. Số cột = Degree.
- **Example:** 학생 테이블의 '홍길동' 데이터 한 줄이 튜플, '이름', '학번' 열이 속성. / Một dòng dữ liệu 'Hong Gil-dong' là Tuple, các cột 'Tên', 'Mã SV' là Attribute.
- 💡 **Mẹo ghi nhớ:** Tu-Car (Tuple = Cardinality), At-De (Attribute = Degree).

Như vậy, **106-107. 튜플(Tuple)과 속성(Attribute)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **108. 도메인 (Domain)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **108. 도메인 (Domain)** nối từ **106-107. 튜플(Tuple)과 속성(Attribute)** sang **178. 관계해석 (Relational Calculus)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 108. 도메인 (Domain)

Sau khi đã đặt nền bằng **106-107. 튜플(Tuple)과 속성(Attribute)**, ta chuyển sang **108. 도메인 (Domain)**. Đây là mắt xích 41/54 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **108. 도메인 (Domain)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “108. 도메인 (Domain)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 하나의 애트리뷰트가 취할 수 있는 같은 타입의 원자(Atomic) 값들의 집합.
- **VI (Vietnamese) (Tiếng Việt):** Miền giá trị. Tập hợp các giá trị nguyên tử (không thể chia nhỏ) cùng kiểu mà một thuộc tính có thể nhận.
- **Example:** '성별' 속성의 도메인은 {남, 여}. / Miền giá trị của thuộc tính 'Giới tính' là {Nam, Nữ}.

Ta có thể khép mục **108. 도메인 (Domain)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **178. 관계해석 (Relational Calculus)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **178. 관계해석 (Relational Calculus)** nối từ **108. 도메인 (Domain)** sang **183. 함수적 종속과 이행적 종속 (Functional & Transitive Dependency)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 178. 관계해석 (Relational Calculus)

Từ **108. 도메인 (Domain)**, ta đã có điểm tựa để bước vào **178. 관계해석 (Relational Calculus)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 42/54 trước khi đi vào chi tiết.

Để đọc **178. 관계해석 (Relational Calculus)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “178. 관계해석 (Relational Calculus)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- E.F. Codd가 제안, 비절차적(원하는 정보가 무엇인지만 정의) 특성.
- 튜플 관계해석과 도메인 관계해석으로 나뉨. 관계대수와 능력 동등.
- **VI (Vietnamese) (Tiếng Việt):** Giải tích quan hệ (Relational Calculus).
  - Do E.F. Codd đề xuất. Tính phi thủ tục (chỉ cần biết 'là gì' thay vì 'làm thế nào').
  - Có sức mạnh tính toán tương đương đại số quan hệ.

Điểm chốt của **178. 관계해석 (Relational Calculus)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **183. 함수적 종속과 이행적 종속 (Functional & Transitive Dependency)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **183. 함수적 종속과 이행적 종속 (Functional & Transitive Dependency)** nối từ **178. 관계해석 (Relational Calculus)** sang **186. 시스템 카탈로그 (System Catalog)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 183. 함수적 종속과 이행적 종속 (Functional & Transitive Dependency)

Ở bước 43/54, **183. 함수적 종속과 이행적 종속 (Functional & Transitive Dependency)** xuất hiện như phần tiếp nối của **178. 관계해석 (Relational Calculus)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **183. 함수적 종속과 이행적 종속 (Functional & Transitive Dependency)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “183. 함수적 종속과 이행적 종속 (Functional & Transitive Dependency)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **함수적 종속 (Functional Dependency):** X -> Y (X가 결정되면 Y가 결정됨).
- **이행적 종속 (Transitive Dependency):** A -> B, B -> C 일 때 A -> C 인 관계.
- **VI (Vietnamese) (Tiếng Việt):** Phụ thuộc hàm và Phụ thuộc bắc cầu.

Như vậy, **183. 함수적 종속과 이행적 종속 (Functional & Transitive Dependency)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **186. 시스템 카탈로그 (System Catalog)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **186. 시스템 카탈로그 (System Catalog)** nối từ **183. 함수적 종속과 이행적 종속 (Functional & Transitive Dependency)** sang **190. CRUD 분석**, vì cơ chế trước tạo đầu vào cho bước sau.

## 186. 시스템 카탈로그 (System Catalog)

Sau khi đã đặt nền bằng **183. 함수적 종속과 이행적 종속 (Functional & Transitive Dependency)**, ta chuyển sang **186. 시스템 카탈로그 (System Catalog)**. Đây là mắt xích 44/54 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **186. 시스템 카탈로그 (System Catalog)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “186. 시스템 카탈로그 (System Catalog)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- DBMS의 객체(테이블, 뷰 등) 정보를 포함하는 시스템 데이터베이스. (데이터 사전, 메타 데이터)
- 사용자가 조회는 가능하나 직접 갱신(INSERT/UPDATE/DELETE)은 불가 (시스템 자동 갱신).
- **VI (Vietnamese) (Tiếng Việt):** Danh mục hệ thống (System Catalog / Data Dictionary).
  - Chứa thông tin (metadata) về các đối tượng trong DB.
  - Người dùng có thể xem (SELECT) nhưng KHÔNG thể sửa đổi trực tiếp.

Ta có thể khép mục **186. 시스템 카탈로그 (System Catalog)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **190. CRUD 분석**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **190. CRUD 분석** nối từ **186. 시스템 카탈로그 (System Catalog)** sang **194. 파티션 (Partition)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 190. CRUD 분석

Từ **186. 시스템 카탈로그 (System Catalog)**, ta đã có điểm tựa để bước vào **190. CRUD 분석**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 45/54 trước khi đi vào chi tiết.

Để đọc **190. CRUD 분석** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “190. CRUD 분석” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- Create, Read, Update, Delete 연산의 매트릭스 분석으로 데이터 양 유추.
- **VI (Vietnamese) (Tiếng Việt):** Phân tích ma trận CRUD (Tạo, Đọc, Sửa, Xóa).

Điểm chốt của **190. CRUD 분석** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **194. 파티션 (Partition)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **194. 파티션 (Partition)** nối từ **190. CRUD 분석** sang **148-154. 파일 시스템과 디렉터리, 보안 (File System & Security)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 194. 파티션 (Partition)

Ở bước 46/54, **194. 파티션 (Partition)** xuất hiện như phần tiếp nối của **190. CRUD 분석**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **194. 파티션 (Partition)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “194. 파티션 (Partition)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 대용량 테이블/인덱스를 작은 논리적 단위로 분할.
- 종류: 범위(Range - 예: 월별), 해시(Hash), 조합(Composite), 목록(List), 라운드 로빈(Round Robin).
- **VI (Vietnamese) (Tiếng Việt):** Phân vùng dữ liệu (Partition). Chia bảng lớn thành phần nhỏ: theo Khoảng (Range), Băm (Hash), Danh sách (List)...

Như vậy, **194. 파티션 (Partition)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **148-154. 파일 시스템과 디렉터리, 보안 (File System & Security)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **148-154. 파일 시스템과 디렉터리, 보안 (File System & Security)** nối từ **194. 파티션 (Partition)** sang **1. UNIX 파일 시스템의 구조 (Cấu trúc hệ thống tệp UNIX)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 148-154. 파일 시스템과 디렉터리, 보안 (File System & Security)

Sau khi đã đặt nền bằng **194. 파티션 (Partition)**, ta chuyển sang **148-154. 파일 시스템과 디렉터리, 보안 (File System & Security)**. Đây là mắt xích 47/54 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **148-154. 파일 시스템과 디렉터리, 보안 (File System & Security)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “148-154. 파일 시스템과 디렉터리, 보안 (File System & Security)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **순차 파일 (Sequential File):** 연속 기록 (자기 테이프). 접근 느림.
- **색인 순차 파일 (Indexed Sequential File):** 순차 + 색인(포인터). (기본, 색인, 오버플로 영역).
- **직접 파일 (Direct File):** 해싱 함수로 물리적 주소 직접 계산. 접근 빠름.
- **디렉터리 구조:** 1단계, 2단계, 트리, 비순환 그래프(공유 허용), 일반적인 그래프(순환 허용).
- **보안 기법:** 접근 제어 행렬, 전역 테이블, 접근 제어 리스트, 권한 리스트.
- **VI (Vietnamese) (Tiếng Việt):** Hệ thống file & Bảo mật.
  - Cấu trúc file: Tuần tự, Tuần tự có chỉ mục, Trực tiếp (hashing).
  - Cấu trúc thư mục: Cây, Đồ thị không chu trình (cho phép chia sẻ).

# 3과목 데이터베이스 구축 (Phần 3: Xây dựng Cơ sở dữ liệu) - Phần 1

> [!NOTE]
> Mặc dù đây là nội dung môn 3 (CSDL), có một số kiến thức hệ điều hành UNIX còn sót lại từ phần trước.

Ta có thể khép mục **148-154. 파일 시스템과 디렉터리, 보안 (File System & Security)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **1. UNIX 파일 시스템의 구조 (Cấu trúc hệ thống tệp UNIX)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **1. UNIX 파일 시스템의 구조 (Cấu trúc hệ thống tệp UNIX)** nối từ **148-154. 파일 시스템과 디렉터리, 보안 (File System & Security)** sang **2. UNIX의 주요 명령어 (Các lệnh UNIX chính)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 1. UNIX 파일 시스템의 구조 (Cấu trúc hệ thống tệp UNIX)

Từ **148-154. 파일 시스템과 디렉터리, 보안 (File System & Security)**, ta đã có điểm tựa để bước vào **1. UNIX 파일 시스템의 구조 (Cấu trúc hệ thống tệp UNIX)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 48/54 trước khi đi vào chi tiết.

Để đọc **1. UNIX 파일 시스템의 구조 (Cấu trúc hệ thống tệp UNIX)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “1. UNIX 파일 시스템의 구조 (Cấu trúc hệ thống tệp UNIX)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **부트 블록 (Boot Block - Khối khởi động):**
  - 부팅 시 필요한 코드를 저장하고 있는 블록.
  - _Giải thích VN:_ Khối lưu trữ mã cần thiết khi khởi động máy.
  - _Ví dụ:_ MBR (Master Boot Record) trong Windows, nhưng ở UNIX nó nằm ở Boot Block, chứa bootloader để nạp hệ điều hành.

- **슈퍼 블록 (Super Block - Siêu khối):**
  - 전체 파일 시스템에 대한 정보를 저장. 사용 가능한 I-node, 사용 가능한 디스크 블록의 개수 등을 포함.
  - _Giải thích VN:_ Chứa thông tin về toàn bộ hệ thống tệp: số lượng I-node trống, các khối đĩa trống. Mỗi hệ thống tệp có Super Block riêng.
  - _Ví dụ:_ Giống như mục lục tổng quát của một thư viện cho biết thư viện có bao nhiêu kệ sách và bao nhiêu sách chưa được mượn.

- **I-node 블록 (I-node Block - Khối I-node):**
  - 각 파일이나 디렉터리에 대한 모든 정보를 저장. (소유자 UID/GID, 파일 크기, 타입, 생성/변경 시기, 권한, 데이터 블록 시작 주소 등).
  - _Giải thích VN:_ Lưu trữ siêu dữ liệu (metadata) của tệp (chủ sở hữu, kích thước, quyền, địa chỉ bắt đầu của dữ liệu, thời gian tạo/sửa).
  - _Ví dụ:_ I-node giống như thẻ căn cước (ID card) của tệp, mọi thông tin quản lý đều nằm ở đây trừ tên tệp và nội dung thực sự.

- **데이터 블록 (Data Block - Khối dữ liệu):**
  - 실제 파일에 대한 데이터가 저장된 블록.
  - _Giải thích VN:_ Nơi lưu trữ nội dung thực tế của tệp hoặc danh sách các thư mục con.
  - _Ví dụ:_ Các trang sách chứa nội dung chữ bên trong thư viện.

> 💡 **Mẹo ghi nhớ (Mnemonics):**
> Thứ tự các khối: **B**oot -> **S**uper -> **I**-node -> **D**ata (**BSID** - Bác Sĩ I-node Dễ thương).

---

Điểm chốt của **1. UNIX 파일 시스템의 구조 (Cấu trúc hệ thống tệp UNIX)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **2. UNIX의 주요 명령어 (Các lệnh UNIX chính)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **2. UNIX의 주요 명령어 (Các lệnh UNIX chính)** nối từ **1. UNIX 파일 시스템의 구조 (Cấu trúc hệ thống tệp UNIX)** sang **6. DDL, DML, DCL 상세 (Chi tiết DDL, DML, DCL)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 2. UNIX의 주요 명령어 (Các lệnh UNIX chính)

Ở bước 49/54, **2. UNIX의 주요 명령어 (Các lệnh UNIX chính)** xuất hiện như phần tiếp nối của **1. UNIX 파일 시스템의 구조 (Cấu trúc hệ thống tệp UNIX)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **2. UNIX의 주요 명령어 (Các lệnh UNIX chính)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng là bằng chứng để so sánh các lựa chọn theo cùng tiêu chí, không phải danh sách cần học thuộc từng ô.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “2. UNIX의 주요 명령어 (Các lệnh UNIX chính)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

| 명령어 (Command) | 의미 (Ý nghĩa) | Giải thích & Ví dụ (VN) |
|---|---|---|
| `fork` | 새로운 프로세스 생성 (Tạo tiến trình con/nhân bản tiến trình). | Giống như phân thân. Ví dụ: Tiến trình cha gọi `fork` tạo ra một tiến trình con y hệt để làm việc song song. |
| `exec` | 새로운 프로세스 수행 (Thực thi tiến trình mới). | Thay thế tiến trình hiện tại bằng tiến trình mới. Ví dụ: Dùng `exec` để mở chương trình máy tính (calculator). |
| `&` | 백그라운드 처리 (Chạy nền). | Đặt ở cuối lệnh. Ví dụ: `find / -name test.txt &` (Tìm kiếm ngầm, cho phép gõ tiếp lệnh khác). |
| `wait` | 하위 프로세스 종료 대기 (Đợi tiến trình con kết thúc). | Ví dụ: Tiến trình cha đứng đợi (wait) tiến trình con hoàn thành công việc mới tiếp tục. |
| `exit` | 프로세스 수행 종료 (Kết thúc tiến trình). | Ví dụ: Gõ `exit` để đóng terminal. |
| `cat` | 파일 내용 표시 (Hiển thị nội dung tệp, giống `TYPE` trong DOS). | Ví dụ: `cat file.txt` (In nội dung file.txt ra màn hình). |
| `chmod` | 파일 권한 지정 (Thay đổi quyền truy cập tệp). | Ví dụ: `chmod 777 file.sh` (Cấp toàn quyền đọc, ghi, chạy). |
| `chown` | 소유자 변경 (Thay đổi chủ sở hữu). | Ví dụ: `chown root file.txt` (Đổi chủ tệp thành root). |
| `mount` | 파일 시스템 마운팅 (Gắn hệ thống tệp). | Ví dụ: Cắm USB vào và dùng `mount` để hệ thống nhận diện nội dung USB. |
| `mkfs` | 파일 시스템 생성 (Tạo hệ thống tệp). | Format ổ đĩa. Ví dụ: `mkfs.ext4 /dev/sda1`. |
| `chdir` / `cd` | 디렉터리 위치 변경 (Thay đổi thư mục). | Ví dụ: `cd /home`. |
| `fsck` | 파일 시스템 검사 및 보수 (Kiểm tra và sửa lỗi hệ thống tệp). | Giống chkdsk trong Windows. Ví dụ: `fsck /dev/sda1`. |
| `rmdir` | 디렉터리 삭제 (Xóa thư mục rỗng). | Ví dụ: `rmdir empty_folder`. |
| `ls` | 파일 목록 확인 (Xem danh sách tệp). | Ví dụ: `ls -l` (Xem danh sách chi tiết). |
| `getpid` / `getppid` | 자신의 / 부모 프로세스 ID 획득 (Lấy PID / Parent PID). | ID tiến trình để quản lý (vd: dùng kill để tắt). |
| `cp` / `mv` / `rm`| 복사 (Copy) / 이동 및 이름 변경 (Move/Rename) / 삭제 (Remove). | `cp a.txt b.txt`, `mv old.txt new.txt`, `rm a.txt`. |
| `finger` | 사용자 정보 표시 (Hiển thị thông tin người dùng). | Xem ai đang đăng nhập vào hệ thống. |

---

# CHAPTER 01 SQL 응용 (Ứng dụng SQL)

Như vậy, **2. UNIX의 주요 명령어 (Các lệnh UNIX chính)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **6. DDL, DML, DCL 상세 (Chi tiết DDL, DML, DCL)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **6. DDL, DML, DCL 상세 (Chi tiết DDL, DML, DCL)** nối từ **2. UNIX의 주요 명령어 (Các lệnh UNIX chính)** sang **7. 집합연산자 및 조인 (Toán tử tập hợp và JOIN)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 6. DDL, DML, DCL 상세 (Chi tiết DDL, DML, DCL)

Sau khi đã đặt nền bằng **2. UNIX의 주요 명령어 (Các lệnh UNIX chính)**, ta chuyển sang **6. DDL, DML, DCL 상세 (Chi tiết DDL, DML, DCL)**. Đây là mắt xích 50/54 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **6. DDL, DML, DCL 상세 (Chi tiết DDL, DML, DCL)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng cho ta tiêu chí đối chiếu, còn công thức cho ta quan hệ giữa các đại lượng; hãy dùng cả hai để kiểm tra cùng một kết luận.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **6.1 DDL 문법 (Cú pháp DDL)**. Hãy xác định **6.1 DDL 문법 (Cú pháp DDL)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 6.1 DDL 문법 (Cú pháp DDL)

Phần nguồn của **6.1 DDL 문법 (Cú pháp DDL)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “6.1 DDL 문법 (Cú pháp DDL)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `CREATE TABLE`: Tạo bảng. Các ràng buộc: `PRIMARY KEY` (Khóa chính), `FOREIGN KEY` (Khóa ngoại), `UNIQUE` (Duy nhất), `CONSTRAINT` (Điều kiện), `CHECK` (Kiểm tra), `DEFAULT` (Mặc định), `NOT NULL` (Không được rỗng).
- `ALTER TABLE`:
  - `ADD` (Thêm cột): `ALTER TABLE table_name ADD col_name datatype;`
  - `MODIFY` (Sửa kiểu/ràng buộc cột): `ALTER TABLE table_name MODIFY col_name datatype;`
  - `DROP` (Xóa cột): `ALTER TABLE table_name DROP col_name;`
  - `RENAME COLUMN`: Đổi tên cột.
- `DROP TABLE` [CASCADE | RESTRICT]: Xóa bảng. CASCADE (xóa luôn đối tượng phụ thuộc), RESTRICT (không xóa nếu đang bị tham chiếu).
- `TRUNCATE TABLE`: Xóa nhanh toàn bộ dữ liệu, giữ lại cấu trúc, **không thể ROLLBACK**.

Các bullet của **6.1 DDL 문법 (Cú pháp DDL)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **6.1 DDL 문법 (Cú pháp DDL)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **6.2 DCL 문법 (Cú pháp DCL)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **6.2 DCL 문법 (Cú pháp DCL)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 6.2 DCL 문법 (Cú pháp DCL)

Các ý ngay dưới **6.2 DCL 문법 (Cú pháp DCL)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “6.2 DCL 문법 (Cú pháp DCL)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `GRANT 권한 ON 테이블 TO 사용자 [WITH GRANT OPTION];` (Cấp quyền. WITH GRANT OPTION: cho phép người đó cấp quyền tiếp cho người khác).
- `REVOKE 권한 ON 테이블 FROM 사용자 [CASCADE CONSTRAINTS];` (Thu hồi quyền. CASCADE: thu hồi luôn quyền mà người này đã cấp cho người khác).

Các bullet của **6.2 DCL 문법 (Cú pháp DCL)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **6.2 DCL 문법 (Cú pháp DCL)**, đừng bắt đầu lại từ số không. **6.3 TCL 문법 (Cú pháp TCL)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **6.3 TCL 문법 (Cú pháp TCL)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 6.3 TCL 문법 (Cú pháp TCL)

Bây giờ ta đi vào nội dung của **6.3 TCL 문법 (Cú pháp TCL)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “6.3 TCL 문법 (Cú pháp TCL)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `COMMIT`: Lưu vĩnh viễn giao dịch (Transaction) thành công.
- `ROLLBACK`: Hủy bỏ giao dịch bị lỗi, quay về trạng thái cũ.
- `SAVEPOINT`: Đặt điểm lưu để Rollback về điểm đó thay vì toàn bộ.

Các bullet của **6.3 TCL 문법 (Cú pháp TCL)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**6.3 TCL 문법 (Cú pháp TCL)** vừa cho ta cách đặt câu hỏi. Bây giờ **6.3 DML 문법 (Cú pháp DML)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Với **6.3 DML 문법 (Cú pháp DML)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 6.3 DML 문법 (Cú pháp DML)

Phần nguồn của **6.3 DML 문법 (Cú pháp DML)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “6.3 DML 문법 (Cú pháp DML)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `SELECT [DISTINCT] 속성명 FROM 테이블 WHERE 조건 GROUP BY 속성명 HAVING 조건 ORDER BY 속성명 [ASC|DESC];`
  - `DISTINCT`: Loại bỏ dòng trùng lặp.
  - `GROUP BY`: Nhóm dữ liệu (ROLLUP, CUBE để tính tổng phụ).
  - `HAVING`: Điều kiện cho nhóm (GROUP BY).
- **집계 함수 (Hàm tập hợp):** `COUNT`, `SUM`, `AVG`, `MAX`, `MIN`, `STDDEV` (độ lệch chuẩn), `VARIANCE` (phương sai).
- **순위 함수 (Hàm xếp hạng):** `RANK` (bỏ qua số hạng: 1, 1, 3), `DENSE_RANK` (không bỏ qua: 1, 1, 2), `ROW_NUMBER` (đánh số thứ tự: 1, 2, 3).
- **WHERE 연산자 (Toán tử điều kiện):** `LIKE '%'` (Nhiều ký tự), `LIKE '_'` (1 ký tự), `BETWEEN A AND B`, `IN()`, `IS NULL`.
- `UPDATE 테이블 SET 속성 = 데이터 WHERE 조건;` (Sửa dữ liệu).
- `DELETE FROM 테이블 WHERE 조건;` (Xóa dữ liệu, có thể ROLLBACK).
- `INSERT INTO 테이블 (속성) VALUES (데이터);` (Thêm dữ liệu).

---

Với **6.3 DML 문법 (Cú pháp DML)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Với **6.3 DML 문법 (Cú pháp DML)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Ta có thể khép mục **6. DDL, DML, DCL 상세 (Chi tiết DDL, DML, DCL)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **7. 집합연산자 및 조인 (Toán tử tập hợp và JOIN)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **7. 집합연산자 및 조인 (Toán tử tập hợp và JOIN)** nối từ **6. DDL, DML, DCL 상세 (Chi tiết DDL, DML, DCL)** sang **15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7. 집합연산자 및 조인 (Toán tử tập hợp và JOIN)

Từ **6. DDL, DML, DCL 상세 (Chi tiết DDL, DML, DCL)**, ta đã có điểm tựa để bước vào **7. 집합연산자 및 조인 (Toán tử tập hợp và JOIN)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 51/54 trước khi đi vào chi tiết.

Để đọc **7. 집합연산자 및 조인 (Toán tử tập hợp và JOIN)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **INNER JOIN**, **OUTER JOIN (LEFT, RIGHT, FULL)**, **SELF JOIN**, **CROSS JOIN** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **집합 연산자 (Toán tử tập hợp)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 집합 연산자 (Toán tử tập hợp)

Các ý ngay dưới **집합 연산자 (Toán tử tập hợp)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “집합 연산자 (Toán tử tập hợp)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `UNION`: Hợp (Loại bỏ trùng lặp).
- `UNION ALL`: Hợp tất cả (Giữ nguyên trùng lặp).
- `INTERSECT`: Giao (Chỉ lấy phần chung).
- `MINUS` / `EXCEPT`: Hiệu (Lấy bảng 1 trừ đi các dòng có trong bảng 2).

Các bullet của **집합 연산자 (Toán tử tập hợp)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **집합 연산자 (Toán tử tập hợp)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **조인 (JOIN)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **조인 (JOIN)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 조인 (JOIN)

Bây giờ ta đi vào nội dung của **조인 (JOIN)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “조인 (JOIN)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **INNER JOIN**: Lấy các dòng có dữ liệu khớp nhau (Giao). `SELECT * FROM A INNER JOIN B ON A.id = B.id;`
- **OUTER JOIN (LEFT, RIGHT, FULL)**: Lấy cả dữ liệu không khớp. Bên thiếu dữ liệu sẽ điền NULL.
  - Cú pháp Oracle (+): `WHERE A.id = B.id(+)` (Đây là LEFT OUTER JOIN vì dấu (+) nằm ở bảng B, tức là bảng B thiếu cũng không sao).
- **SELF JOIN**: Bảng tự JOIN với chính nó. (Dùng `AS` để tạo bí danh).
- **CROSS JOIN**: Tích Đề-các (Cartesian product), bắt cặp tất cả các dòng của 2 bảng.

---

Với **조인 (JOIN)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **조인 (JOIN)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **7. 집합연산자 및 조인 (Toán tử tập hợp và JOIN)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

> **Nối mạch:** Ở chặng này của **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **7. 집합연산자 및 조인 (Toán tử tập hợp và JOIN)** đặt vấn đề; **15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)** đối chiếu bằng chứng, rồi **21. 데이터 전환 및 정제 (Chuyển đổi dữ liệu - ETL)** mở rộng hệ quả hoặc giới hạn liên quan.

## 15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)

Ở bước 52/54, **15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)** xuất hiện như phần tiếp nối của **7. 집합연산자 및 조인 (Toán tử tập hợp và JOIN)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng cho ta tiêu chí đối chiếu, còn công thức cho ta quan hệ giữa các đại lượng; hãy dùng cả hai để kiểm tra cùng một kết luận.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **일반 집합 연산자 (Toán tử tập hợp cơ bản)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **일반 집합 연산자 (Toán tử tập hợp cơ bản)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 일반 집합 연산자 (Toán tử tập hợp cơ bản)

Bây giờ ta đi vào nội dung của **일반 집합 연산자 (Toán tử tập hợp cơ bản)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “일반 집합 연산자 (Toán tử tập hợp cơ bản)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **합집합 (UNION, ∪):** Hợp (lấy tất cả, bỏ trùng lặp).
- **교집합 (INTERSECTION, ∩):** Giao (lấy phần chung).
- **차집합 (DIFFERENCE, —):** Hiệu (R - S: có trong R nhưng không có trong S).
- **교차곱 (CARTESIAN PRODUCT, Х):** Tích Đề-các (kết hợp tất cả các dòng của 2 bảng).

Các bullet của **일반 집합 연산자 (Toán tử tập hợp cơ bản)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **일반 집합 연산자 (Toán tử tập hợp cơ bản)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **순수 관계 연산자 (Toán tử quan hệ thuần túy)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **순수 관계 연산자 (Toán tử quan hệ thuần túy)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 순수 관계 연산자 (Toán tử quan hệ thuần túy)

Phần nguồn của **순수 관계 연산자 (Toán tử quan hệ thuần túy)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “순수 관계 연산자 (Toán tử quan hệ thuần túy)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

| 연산자 (Toán tử) | 기호 (Ký hiệu) | 설명 (Mô tả) |
|---|---|---|
| **Select (선택)** | **σ (Sigma)** | Lấy các **Hàng (Tuple)** thỏa mãn điều kiện (Phép toán nằm ngang - 수평). |
| **Project (추출)** | **π (Pi)** | Lấy các **Cột (Attribute)** được chỉ định, loại bỏ trùng lặp (Phép toán dọc - 수직). |
| **Join (조인)** | **⋈ (Bowtie)** | Kết hợp 2 bảng dựa trên thuộc tính chung. |
| **Division (나누기)** | **÷ (Divide)** | Trả về các 튜플 của bảng R mà khớp với tất cả giá trị thuộc tính của bảng S. |

> 💡 **Mẹo ghi nhớ:** **Se-Hàng, Pro-Cột** (Select = Hàng/Tuple, Project = Cột/Attribute).

---

Khi đọc **순수 관계 연산자 (Toán tử quan hệ thuần túy)**, hãy tách hai lớp: bảng giúp đối chiếu các loại hoặc tiêu chí, còn công thức cần được đọc theo biến, đơn vị và quan hệ giữa các đại lượng. Cách tách này giúp ta hiểu cơ chế trước khi ghi nhớ ký hiệu.

Điểm chốt của **순수 관계 연산자 (Toán tử quan hệ thuần túy)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Như vậy, **15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **21. 데이터 전환 및 정제 (Chuyển đổi dữ liệu - ETL)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)** đặt vấn đề; **21. 데이터 전환 및 정제 (Chuyển đổi dữ liệu - ETL)** đối chiếu bằng chứng, rồi **22. 기타 주요 개념 (Các khái niệm quan trọng khác)** mở rộng hệ quả hoặc giới hạn liên quan.

## 21. 데이터 전환 및 정제 (Chuyển đổi dữ liệu - ETL)

Sau khi đã đặt nền bằng **15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)**, ta chuyển sang **21. 데이터 전환 및 정제 (Chuyển đổi dữ liệu - ETL)**. Đây là mắt xích 53/54 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **21. 데이터 전환 및 정제 (Chuyển đổi dữ liệu - ETL)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **데이터 전환 (Data Migration - Di chuyển dữ liệu)**. Hãy xác định **데이터 전환 (Data Migration - Di chuyển dữ liệu)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 데이터 전환 (Data Migration - Di chuyển dữ liệu)

Phần nguồn của **데이터 전환 (Data Migration - Di chuyển dữ liệu)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Là quá trình chuyển dữ liệu từ hệ thống cũ sang hệ thống mới.
- **ETL 3 bước:**
  1. **E**xtraction (추출): Trích xuất từ nguồn.
  2. **T**ransformation (변환): Biến đổi cho phù hợp chuẩn mới.
  3. **L**oad (적재): Nạp vào hệ thống đích.

Các bullet của **데이터 전환 (Data Migration - Di chuyển dữ liệu)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **데이터 전환 (Data Migration - Di chuyển dữ liệu)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **오류 데이터 정제 (Error Data Cleansing)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **오류 데이터 정제 (Error Data Cleansing)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 오류 데이터 정제 (Error Data Cleansing)

Các ý ngay dưới **오류 데이터 정제 (Error Data Cleansing)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Quản lý trạng thái lỗi trong quá trình chuyển đổi:
- **Open (Mở):** Phát hiện lỗi, chưa phân tích.
- **Assigned (Đã giao):** Giao cho lập trình viên sửa.
- **Fixed (Đã sửa):** Đã sửa xong.
- **Closed (Đóng):** Đã test lại và xác nhận bình thường.
- **Deferred (Trì hoãn):** Quyết định chưa sửa lúc này (hoặc không phải lỗi).

---

Các bullet của **오류 데이터 정제 (Error Data Cleansing)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **오류 데이터 정제 (Error Data Cleansing)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **21. 데이터 전환 및 정제 (Chuyển đổi dữ liệu - ETL)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **22. 기타 주요 개념 (Các khái niệm quan trọng khác)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

> **Nối mạch:** Trong **Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)**, **21. 데이터 전환 및 정제 (Chuyển đổi dữ liệu - ETL)** đặt vấn đề; **22. 기타 주요 개념 (Các khái niệm quan trọng khác)** đối chiếu bằng chứng, rồi nối sang phần giải thích tiếp theo.

## 22. 기타 주요 개념 (Các khái niệm quan trọng khác)

Từ **21. 데이터 전환 및 정제 (Chuyển đổi dữ liệu - ETL)**, ta đã có điểm tựa để bước vào **22. 기타 주요 개념 (Các khái niệm quan trọng khác)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 54/54 trước khi đi vào chi tiết.

Để đọc **22. 기타 주요 개념 (Các khái niệm quan trọng khác)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **CRUD 분석 (Phân tích CRUD)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### CRUD 분석 (Phân tích CRUD)

Các ý ngay dưới **CRUD 분석 (Phân tích CRUD)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “CRUD 분석 (Phân tích CRUD)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- Tạo ma trận (Matrix) giữa **Process (Tiến trình)** và **Table (Bảng)**.
- Đánh dấu **C**reate, **R**ead, **U**pdate, **D**elete để xem bảng nào bị thao tác nhiều/ít, phát hiện bảng bị bỏ sót (ít nhất mỗi bảng phải có 1 thao tác).

Các bullet của **CRUD 분석 (Phân tích CRUD)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **CRUD 분석 (Phân tích CRUD)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **MyBatis (프레임워크)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **MyBatis (프레임워크)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### MyBatis (프레임워크)

Bây giờ ta đi vào nội dung của **MyBatis (프레임워크)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “MyBatis (프레임워크)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- Khung làm việc (Framework) giúp đơn giản hóa JDBC trong Java.
- **Đặc điểm:** Tách mã SQL ra khỏi mã Java (lưu trong file XML hoặc Annotation), thân thiện với lập trình viên SQL.

Các bullet của **MyBatis (프레임워크)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **MyBatis (프레임워크)**, đừng bắt đầu lại từ số không. **시스템 카탈로그 (System Catalog)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **시스템 카탈로그 (System Catalog)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 시스템 카탈로그 (System Catalog)

Phần nguồn của **시스템 카탈로그 (System Catalog)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “시스템 카탈로그 (System Catalog)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **Định nghĩa:** CSDL đặc biệt chứa "dữ liệu về dữ liệu" (Metadata / Data Dictionary).
- **Đặc điểm:** Chỉ có hệ thống (DBMS) mới được quyền cập nhật (Tự động cập nhật). Người dùng chỉ có quyền **SELECT (Đọc)**.

Các bullet của **시스템 카탈로그 (System Catalog)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**시스템 카탈로그 (System Catalog)** vừa cho ta cách đặt câu hỏi. Bây giờ **연산자 우선순위 (Thứ tự ưu tiên toán tử trong SQL)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Đoạn **연산자 우선순위 (Thứ tự ưu tiên toán tử trong SQL)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 연산자 우선순위 (Thứ tự ưu tiên toán tử trong SQL)

Các ý ngay dưới **연산자 우선순위 (Thứ tự ưu tiên toán tử trong SQL)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “연산자 우선순위 (Thứ tự ưu tiên toán tử trong SQL)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 산술 연산자 (Toán học: `* / + -`) **>** 관계 연산자 (So sánh: `< > = !=`) **>** 논리 연산자 (Logic: `NOT > AND > OR`).

> 💡 **Mẹo ghi nhớ:** **Toán - Quan - Lo** (Toán học - Quan hệ - Logic). Nhân chia trước, cộng trừ sau, rồi đến so sánh, cuối cùng là AND/OR.

Với **연산자 우선순위 (Thứ tự ưu tiên toán tử trong SQL)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Với **연산자 우선순위 (Thứ tự ưu tiên toán tử trong SQL)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Khép lại **22. 기타 주요 개념 (Các khái niệm quan trọng khác)**, điều cần giữ lại là mối quan hệ giữa mục đích, cơ chế và điểm giới hạn của các khái niệm trong nguồn. Khi ôn lại, hãy tự giải thích chúng bằng một câu hoàn chỉnh rồi đối chiếu với các điểm dễ nhầm trước khi chuyển sang bài tổng hợp của môn.

> **Bàn giao:** Sau **22. 기타 주요 개념 (Các khái niệm quan trọng khác)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
