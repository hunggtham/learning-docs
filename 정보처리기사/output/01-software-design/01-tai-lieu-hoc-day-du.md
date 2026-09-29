# Môn 1 — 소프트웨어 설계 (Software Design) (Thiết kế phần mềm)

## 학습 목표 (Mục tiêu học tập)

Phần này đặt mục tiêu của bài, để người mới biết mình cần giải thích được điều gì trước khi đi vào thuật ngữ và ví dụ.

- 시험에서 사용하는 한국어 용어를 영어와 베트남어 뜻까지 함께 인식한다.
- 각 개념을 정의 → 구성요소/절차 → 비교 포인트 → 예시 순서로 설명할 수 있다.
- 앞에서 배운 개념과 뒤의 심화 개념을 연결하여 문제의 조건을 빠르게 해석한다.

> **Câu hỏi trung tâm:** Khi học môn này, người học không chỉ cần nhận ra thuật ngữ Hàn mà còn phải giải thích khái niệm đang giải quyết vấn đề nào, dựa trên điều kiện nào và được dùng để nối sang phần kiến thức nào tiếp theo.

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

## 소프트웨어 생명 주기 및 개발 방법론 (SDLC & Methodologies)

Chúng ta bắt đầu mạch học bằng **소프트웨어 생명 주기 및 개발 방법론 (SDLC & Methodologies)**. Trước khi đi vào từng thuật ngữ, hãy giữ câu hỏi trung tâm: phần kiến thức này giải quyết vấn đề gì và vì sao các khái niệm sau phải được đọc trong cùng một bối cảnh? Mục đích của mục 1/57 là tạo điểm tựa để những phần tiếp theo được hiểu theo quan hệ, không chỉ được ghi nhớ như danh sách.

Để đọc **소프트웨어 생명 주기 및 개발 방법론 (SDLC & Methodologies)** như một bài học cho người mới, hãy giữ câu hỏi: **một dự án đi qua những giai đoạn nào, mỗi mô hình phân bổ công việc và rủi ro ra sao?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các đoạn prose và thuật ngữ bên dưới cần được đọc như các bước trả lời cho câu hỏi đó.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Như vậy, **소프트웨어 생명 주기 및 개발 방법론 (SDLC & Methodologies)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **1. 소프트웨어 생명 주기 (SDLC - Software Development Life Cycle)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 1. 소프트웨어 생명 주기 (SDLC - Software Development Life Cycle)

Sau khi đã đặt nền bằng **소프트웨어 생명 주기 및 개발 방법론 (SDLC & Methodologies)**, ta chuyển sang **1. 소프트웨어 생명 주기 (SDLC - Software Development Life Cycle)**. Đây là mắt xích 2/57 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **1. 소프트웨어 생명 주기 (SDLC - Software Development Life Cycle)** như một bài học cho người mới, hãy giữ câu hỏi: **một dự án đi qua những giai đoạn nào, mỗi mô hình phân bổ công việc và rủi ro ra sao?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **개념**, **폭포수 모형 (Waterfall Model)**, **나선형 모형 (Spiral Model)**, **프로토타입 모형 (Prototype Model)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **개념**: Toàn bộ quá trình phát triển (Yêu cầu -> Thiết kế -> Code -> Test -> Bảo trì). Là tiêu chuẩn để quản lý dự án, chi phí, nhân lực.
- **폭포수 모형 (Waterfall Model)**:
  - Tuần tự (선형 순차적). Xong bước này mới qua bước khác. Không quay lại được.
  - Phù hợp dự án có yêu cầu rõ ràng, hệ thống nhà nước/ngân hàng. Tài liệu là trọng tâm.
- **나선형 모형 (Spiral Model)**:
  - Do Boehm đề xuất. Trọng tâm: Phân tích rủi ro (위험 분석).
  - Chu trình: Kế hoạch (계획) -> Phân tích rủi ro (위험) -> Phát triển (개발) -> Đánh giá (평가).
  - Phù hợp dự án lớn, rủi ro cao.
- **프로토타입 모형 (Prototype Model)**:
  - Làm bản nháp (시제품) trước khi phát triển thật. Phù hợp khi yêu cầu chưa rõ ràng.
- **V-모형 (V-Model)**:
  - Mỗi bước phát triển tương ứng với một bước Test (Ánh xạ Dev-Test). Yêu cầu chất lượng cực cao (Y tế, Hàng không).

Ta có thể khép mục **1. 소프트웨어 생명 주기 (SDLC - Software Development Life Cycle)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **1. 소프트웨어 공학 및 개발 방법론 (Kỹ nghệ phần mềm và Phương pháp luận phát triển)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 1. 소프트웨어 공학 및 개발 방법론 (Kỹ nghệ phần mềm và Phương pháp luận phát triển)

Từ **1. 소프트웨어 생명 주기 (SDLC - Software Development Life Cycle)**, ta đã có điểm tựa để bước vào **1. 소프트웨어 공학 및 개발 방법론 (Kỹ nghệ phần mềm và Phương pháp luận phát triển)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 3/57 trước khi đi vào chi tiết.

Để đọc **1. 소프트웨어 공학 및 개발 방법론 (Kỹ nghệ phần mềm và Phương pháp luận phát triển)** như một bài học cho người mới, hãy giữ câu hỏi: **một dự án đi qua những giai đoạn nào, mỗi mô hình phân bổ công việc và rủi ro ra sao?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **001. 소프트웨어 공학의 기본 원칙 (Nguyên tắc cơ bản của kỹ nghệ phần mềm)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 001. 소프트웨어 공학의 기본 원칙 (Nguyên tắc cơ bản của kỹ nghệ phần mềm)

Các ý ngay dưới **001. 소프트웨어 공학의 기본 원칙 (Nguyên tắc cơ bản của kỹ nghệ phần mềm)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- 현대적인 프로그래밍 기술을 계속적으로 적용해야 한다. (Phải liên tục áp dụng các kỹ thuật lập trình hiện đại.)
- 개발된 소프트웨어의 품질이 유지되도록 지속적으로 검증해야 한다. (Phải liên tục xác minh để duy trì chất lượng phần mềm đã phát triển.)
- 소프트웨어 개발 관련 사항 및 결과에 대한 명확한 기록을 유지해야 한다. (Phải lưu giữ hồ sơ rõ ràng về các vấn đề và kết quả liên quan đến phát triển phần mềm.)
- **Ví dụ (Example):** Áp dụng CI/CD (Continuous Integration/Continuous Deployment) để liên tục kiểm thử (검증) phần mềm mỗi khi có code mới.
- 💡 **Mẹo ghi nhớ (Mnemonic):** **HKK** (Hiện - Kiểm - Ký): **Hãy Kiểm Kê** (Kỹ thuật hiện đại - Kiểm chứng - Ghi chép).

Các ý về **001. 소프트웨어 공학의 기본 원칙 (Nguyên tắc cơ bản của kỹ nghệ phần mềm)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **001. 소프트웨어 공학의 기본 원칙 (Nguyên tắc cơ bản của kỹ nghệ phần mềm)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **002. 폭포수 모형 (Waterfall Model / Mô hình thác nước)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **002. 폭포수 모형 (Waterfall Model / Mô hình thác nước)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 002. 폭포수 모형 (Waterfall Model / Mô hình thác nước)

Bây giờ ta đi vào nội dung của **002. 폭포수 모형 (Waterfall Model / Mô hình thác nước)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 이전 단계로 돌아갈 수 없다는 전제하에 각 단계를 확실히 매듭짓고 다음 단계를 진행하는 개발 방법론이다. (Là phương pháp phát triển với tiền đề không thể quay lại giai đoạn trước, hoàn thành dứt điểm từng giai đoạn rồi mới tiến sang giai đoạn tiếp theo.)
- 고전적 생명 주기 모형이다. 보헴(Boehm)은 나선형 모형(Spiral Model)을 제안했다. (Là mô hình vòng đời cổ điển. Boehm là người đề xuất mô hình xoắn ốc.)
- 요구사항을 반영하기 어렵다. (Khó phản ánh/thay đổi yêu cầu.)
- **Ví dụ (Example):** Xây dựng một ngôi nhà, bạn không thể xây mái nhà khi chưa làm xong móng. (Phải theo tuần tự).
- 💡 **Mẹo ghi nhớ (Mnemonic):** Nước chảy từ trên xuống, không chảy ngược lại (이전 단계로 돌아갈 수 없음).

Các ý về **002. 폭포수 모형 (Waterfall Model / Mô hình thác nước)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Sau khi đọc **002. 폭포수 모형 (Waterfall Model / Mô hình thác nước)**, đừng bắt đầu lại từ số không. **003. 나선형 모형 (Spiral Model / Mô hình xoắn ốc)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **003. 나선형 모형 (Spiral Model / Mô hình xoắn ốc)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 003. 나선형 모형 (Spiral Model / Mô hình xoắn ốc)

Phần nguồn của **003. 나선형 모형 (Spiral Model / Mô hình xoắn ốc)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- 나선을 따라 돌듯이 점진적으로 완벽한 최종 소프트웨어를 개발하는 것이다. (Phát triển phần mềm cuối cùng hoàn hảo một cách tuần tự giống như quay theo hình xoắn ốc.)
- '계획 수립 → 위험 분석 → 개발 및 검증 → 고객 평가' 과정이 반복적으로 수행된다. (Quá trình 'Lập kế hoạch → Phân tích rủi ro → Phát triển & Kiểm chứng → Khách hàng đánh giá' được lặp đi lặp lại.)
- **Ví dụ (Example):** Phát triển một game lớn, ban đầu làm bản demo (1 vòng xoắn), đánh giá rủi ro, rồi mới phát triển thêm tính năng (vòng xoắn tiếp theo).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **KNKK** (Kế - Nguy - Khai - Khách): **Kế Nguy Khách Khóc** (Lập KH - Rủi ro - Phát triển - Khách hàng).

Các ý về **003. 나선형 모형 (Spiral Model / Mô hình xoắn ốc)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

**003. 나선형 모형 (Spiral Model / Mô hình xoắn ốc)** vừa cho ta cách đặt câu hỏi. Bây giờ **004. 애자일 모형의 주요 방법론 (Các phương pháp luận chính của mô hình Agile)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Đoạn **004. 애자일 모형의 주요 방법론 (Các phương pháp luận chính của mô hình Agile)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 004. 애자일 모형의 주요 방법론 (Các phương pháp luận chính của mô hình Agile)

Các ý ngay dưới **004. 애자일 모형의 주요 방법론 (Các phương pháp luận chính của mô hình Agile)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- 스크럼 (Scrum)
- XP (eXtreme Programming)
- 기능 중심 개발 (FDD; Feature Driven Development)
- 칸반 (Kanban)
- Lean
- **Ví dụ (Example):** Các công ty startup thường dùng Scrum để phát triển nhanh một ứng dụng, chia thành các Sprint ngắn 2 tuần.
- 💡 **Mẹo ghi nhớ (Mnemonic):** **SXFKL** (Scrum, XP, FDD, Kanban, Lean): **Sợ Xấu Phải Kiêng Luôn**.

Các ý về **004. 애자일 모형의 주요 방법론 (Các phương pháp luận chính của mô hình Agile)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **004. 애자일 모형의 주요 방법론 (Các phương pháp luận chính của mô hình Agile)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **005. 애자일 개발 4가지 핵심 가치 (4 Giá trị cốt lõi của phát triển Agile)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **005. 애자일 개발 4가지 핵심 가치 (4 Giá trị cốt lõi của phát triển Agile)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 005. 애자일 개발 4가지 핵심 가치 (4 Giá trị cốt lõi của phát triển Agile)

Bây giờ ta đi vào nội dung của **005. 애자일 개발 4가지 핵심 가치 (4 Giá trị cốt lõi của phát triển Agile)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 프로세스와 도구보다는 개인과 상호작용에 더 가치를 둔다. (Coi trọng cá nhân và sự tương tác hơn là quy trình và công cụ.)
- 방대한 문서보다는 실행되는 SW에 더 가치를 둔다. (Coi trọng phần mềm chạy được hơn là tài liệu đồ sộ.)
- 계약 협상보다는 고객과 협업에 더 가치를 둔다. (Coi trọng sự cộng tác với khách hàng hơn là đàm phán hợp đồng.)
- 계획을 따르기 보다는 변화에 반응하는 것에 더 가치를 둔다. (Coi trọng việc phản hồi với sự thay đổi hơn là bám sát kế hoạch.)
- **Ví dụ (Example):** Thay vì viết tài liệu 100 trang cho khách, nhóm Agile sẽ đưa cho khách một bản demo chạy được (실행되는 SW) để lấy ý kiến ngay.
- 💡 **Mẹo ghi nhớ (Mnemonic):** **CTKB** (Cá - Thực - Khách - Biến): **Cá Thực Khó Bắt** (Cá nhân - Thực thi - Khách hàng - Biến đổi).

Các ý về **005. 애자일 개발 4가지 핵심 가치 (4 Giá trị cốt lõi của phát triển Agile)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Sau khi đọc **005. 애자일 개발 4가지 핵심 가치 (4 Giá trị cốt lõi của phát triển Agile)**, đừng bắt đầu lại từ số không. **006. XP의 핵심 가치 (Giá trị cốt lõi của XP - eXtreme Programming)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **006. XP의 핵심 가치 (Giá trị cốt lõi của XP - eXtreme Programming)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 006. XP의 핵심 가치 (Giá trị cốt lõi của XP - eXtreme Programming)

Phần nguồn của **006. XP의 핵심 가치 (Giá trị cốt lõi của XP - eXtreme Programming)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- 의사소통 (Communication - Giao tiếp)
- 단순성 (Simplicity - Sự đơn giản)
- 용기 (Courage - Dũng cảm)
- 존중 (Respect - Tôn trọng)
- 피드백 (Feedback - Phản hồi)
- **Ví dụ (Example):** Developer có 'dũng cảm' (용기) để xóa những đoạn code cũ không cần thiết và viết lại cho 'đơn giản' (단순성).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **YĐDTP** (Ý - Đơn - Dũng - Tôn - Phản): **Ý Định Dũng Tướng Phàm**.

Các ý về **006. XP의 핵심 가치 (Giá trị cốt lõi của XP - eXtreme Programming)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Như vậy, **006. XP의 핵심 가치 (Giá trị cốt lõi của XP - eXtreme Programming)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Điểm chốt của **1. 소프트웨어 공학 및 개발 방법론 (Kỹ nghệ phần mềm và Phương pháp luận phát triển)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **2. 요구사항 개발 (Phát triển Yêu cầu)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 2. 요구사항 개발 (Phát triển Yêu cầu)

Ở bước 4/57, **2. 요구사항 개발 (Phát triển Yêu cầu)** xuất hiện như phần tiếp nối của **1. 소프트웨어 공학 및 개발 방법론 (Kỹ nghệ phần mềm và Phương pháp luận phát triển)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **2. 요구사항 개발 (Phát triển Yêu cầu)** như một bài học cho người mới, hãy giữ câu hỏi: **một nhu cầu nghiệp vụ được chuyển thành yêu cầu có thể kiểm tra và bàn giao như thế nào?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng cho ta tiêu chí đối chiếu, còn công thức cho ta quan hệ giữa các đại lượng; hãy dùng cả hai để kiểm tra cùng một kết luận.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **007. 주요 비기능 요구사항 (Các yêu cầu phi chức năng chính / Non-functional Requirements)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **007. 주요 비기능 요구사항 (Các yêu cầu phi chức năng chính / Non-functional Requirements)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 007. 주요 비기능 요구사항 (Các yêu cầu phi chức năng chính / Non-functional Requirements)

Bây giờ ta đi vào nội dung của **007. 주요 비기능 요구사항 (Các yêu cầu phi chức năng chính / Non-functional Requirements)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 성능 요구사항 (Yêu cầu hiệu năng)
- 보안 요구사항 (Yêu cầu bảo mật)
- 품질 요구사항 (Yêu cầu chất lượng)
- 제약사항 (Ràng buộc)
- 인터페이스 요구사항 (Yêu cầu giao diện)
- **Ví dụ (Example):** Chức năng đăng nhập là yêu cầu chức năng. Nhưng "Đăng nhập phải hoàn tất dưới 1 giây" là yêu cầu phi chức năng (hiệu năng - 성능).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **HBCRG** (Hiệu - Bảo - Chất - Ràng - Giao): **Học Bài Chăm Rồi Giỏi**.

Các ý về **007. 주요 비기능 요구사항 (Các yêu cầu phi chức năng chính / Non-functional Requirements)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **007. 주요 비기능 요구사항 (Các yêu cầu phi chức năng chính / Non-functional Requirements)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **008. 요구사항 개발 프로세스 (Quy trình phát triển yêu cầu)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **008. 요구사항 개발 프로세스 (Quy trình phát triển yêu cầu)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 008. 요구사항 개발 프로세스 (Quy trình phát triển yêu cầu)

Phần nguồn của **008. 요구사항 개발 프로세스 (Quy trình phát triển yêu cầu)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- 도출 (Elicitation - Khám phá/Rút ra) → 분석 (Analysis - Phân tích) → 명세 (Specification - Đặc tả) → 확인 (Validation - Xác nhận)
- **Ví dụ (Example):** Phỏng vấn user (도출), lọc ra các yêu cầu hợp lý (분석), viết tài liệu SRS (명세), nhờ user ký duyệt (확인).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **ĐPMX** (Đồ - Phân - Minh - Xác): **Đi Phượt Một Xe**.

Các ý về **008. 요구사항 개발 프로세스 (Quy trình phát triển yêu cầu)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Sau khi đọc **008. 요구사항 개발 프로세스 (Quy trình phát triển yêu cầu)**, đừng bắt đầu lại từ số không. **009. 요구사항 분석 (Phân tích yêu cầu / Requirements Analysis)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **009. 요구사항 분석 (Phân tích yêu cầu / Requirements Analysis)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 009. 요구사항 분석 (Phân tích yêu cầu / Requirements Analysis)

Các ý ngay dưới **009. 요구사항 분석 (Phân tích yêu cầu / Requirements Analysis)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- 개발 대상에 대한 사용자의 요구사항을 이해하고 문서화(명세화)하는 활동을 의미한다. (Hoạt động hiểu và tài liệu hóa (đặc tả) yêu cầu của người dùng về đối tượng cần phát triển.)
- 소프트웨어 개발의 실제적인 첫 단계이다. (Là bước thực tế đầu tiên của phát triển phần mềm.)
- 사용자 요구의 타당성을 조사하고 비용과 일정에 대한 제약을 설정한다. (Khảo sát tính hợp lý của yêu cầu người dùng và thiết lập các ràng buộc về chi phí, lịch trình.)
- 사용자의 요구를 정확하게 추출하여 목표를 정하고, 해결 방식을 결정한다. (Trích xuất chính xác yêu cầu của người dùng để đặt mục tiêu và quyết định cách giải quyết.)
- **Ví dụ (Example):** Khách hàng muốn "App chạy nhanh". Phân tích viên sẽ dịch thành "Thời gian phản hồi < 2s" và xem xét chi phí server có đủ đáp ứng không (비용/일정 제약).

Các ý về **009. 요구사항 분석 (Phân tích yêu cầu / Requirements Analysis)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

**009. 요구사항 분석 (Phân tích yêu cầu / Requirements Analysis)** vừa cho ta cách đặt câu hỏi. Bây giờ **010. 자료 흐름도 (DFD - Data Flow Diagram) 의 구성 요소** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Ở đoạn **010. 자료 흐름도 (DFD - Data Flow Diagram) 의 구성 요소**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 010. 자료 흐름도 (DFD - Data Flow Diagram) 의 구성 요소

Bây giờ ta đi vào nội dung của **010. 자료 흐름도 (DFD - Data Flow Diagram) 의 구성 요소**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 프로세스 (Process - Quy trình): Hình tròn / Hình bầu dục. (Ví dụ: 물품 확인 - Kiểm tra hàng hóa)
- 자료 흐름 (Data Flow - Luồng dữ liệu): Mũi tên. (Ví dụ: 물품 코드 - Mã hàng hóa)
- 자료 저장소 (Data Store - Kho lưu trữ dữ liệu): Hai đường thẳng song song. (Ví dụ: 물품대장 - Sổ hàng hóa)
- 단말 (Terminator - Điểm cuối/Tác nhân ngoài): Hình chữ nhật. (Ví dụ: 공장 - Nhà máy)
- 💡 **Mẹo ghi nhớ (Mnemonic):** **PFST** (Process, Flow, Store, Terminator): **Phải Phạt Sợ Tội**.

Các ý về **010. 자료 흐름도 (DFD - Data Flow Diagram) 의 구성 요소** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **010. 자료 흐름도 (DFD - Data Flow Diagram) 의 구성 요소** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **011. 자료 사전 (Data Dictionary) 의 표기 기호** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **011. 자료 사전 (Data Dictionary) 의 표기 기호**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 011. 자료 사전 (Data Dictionary) 의 표기 기호

Phần nguồn của **011. 자료 사전 (Data Dictionary) 의 표기 기호** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- `=`: 정의 (Định nghĩa - is composed of)
- `+`: 연결 (Kết nối/Và - and)
- `( )`: 생략 (Có thể bỏ qua/Tùy chọn - optional)
- `[ | ]`: 선택 (Lựa chọn [hoặc] - choose only one)
- `{ }`: 반복 (Lặp lại - iteration)
- `* *`: 설명 (Giải thích/Chú thích - comment)
- **Ví dụ (Example):** `Customer_Name = First_Name + (Middle_Name) + Last_Name`. Middle_Name nằm trong `( )` nghĩa là có thể không có (생략).
- 💡 **Mẹo ghi nhớ (Mnemonic):** `{ }` giống như vòng lặp trong code, nên là lặp lại (반복). `* *` giống comment `/* */` trong code.

Với **011. 자료 사전 (Data Dictionary) 의 표기 기호**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Sau khi đọc **011. 자료 사전 (Data Dictionary) 의 표기 기호**, đừng bắt đầu lại từ số không. **012. HIPO (Hierarchy plus Input-Process-Output)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **012. HIPO (Hierarchy plus Input-Process-Output)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 012. HIPO (Hierarchy plus Input-Process-Output)

Các ý ngay dưới **012. HIPO (Hierarchy plus Input-Process-Output)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- 하향식 소프트웨어 개발을 위한 문서화 도구이다. (Là công cụ tài liệu hóa cho phát triển phần mềm theo hướng từ trên xuống - Top-down.)
- 기호, 도표 등을 사용하므로 보기 쉽고 이해하기도 쉽다. (Sử dụng ký hiệu, biểu đồ nên dễ nhìn và dễ hiểu.)
- 기능과 자료의 의존 관계를 동시에 표현할 수 있다. (Có thể biểu diễn đồng thời mối quan hệ phụ thuộc giữa chức năng và dữ liệu.)
- **Ví dụ (Example):** Vẽ một sơ đồ cây bắt đầu từ Hệ thống chính (Quản lý trường học) rẽ nhánh xuống các chức năng con (Quản lý điểm, Quản lý sinh viên).

Các ý về **012. HIPO (Hierarchy plus Input-Process-Output)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Như vậy, **012. HIPO (Hierarchy plus Input-Process-Output)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Như vậy, **2. 요구사항 개발 (Phát triển Yêu cầu)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **9. 요구사항 및 시스템 파악 (Yêu cầu & Phân tích Hệ thống)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 9. 요구사항 및 시스템 파악 (Yêu cầu & Phân tích Hệ thống)

Sau khi đã đặt nền bằng **2. 요구사항 개발 (Phát triển Yêu cầu)**, ta chuyển sang **9. 요구사항 및 시스템 파악 (Yêu cầu & Phân tích Hệ thống)**. Đây là mắt xích 5/57 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **9. 요구사항 및 시스템 파악 (Yêu cầu & Phân tích Hệ thống)** như một bài học cho người mới, hãy giữ câu hỏi: **một nhu cầu nghiệp vụ được chuyển thành yêu cầu có thể kiểm tra và bàn giao như thế nào?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **요구사항 검증 방법 (Phương pháp xác minh yêu cầu)**. Hãy xác định **요구사항 검증 방법 (Phương pháp xác minh yêu cầu)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 요구사항 검증 방법 (Phương pháp xác minh yêu cầu)

Phần nguồn của **요구사항 검증 방법 (Phương pháp xác minh yêu cầu)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **동료검토 (Peer Review):** 작성자가 명세서 내용을 직접 설명하면서 결함을 발견함. (Tác giả trực tiếp giải thích tài liệu để đồng nghiệp tìm lỗi - Phi chính thức).
- **워크스루 (Walk Through):** 미리 배포한 명세서를 사전 검토한 후 결함을 발견함. (Phát tài liệu trước, sau đó họp để tìm lỗi - Phi chính thức).
- **인스펙션 (Inspection):** 작성자를 제외한 다른 검토 전문가들이 결함을 발견함. (Các chuyên gia khác (không phải tác giả) kiểm tra chặt chẽ để tìm lỗi - **Chính thức**).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **PWI** (Peer - Walk - Inspect): **Phát Web In**. Inspection là khắt khe và chính thức nhất (공식적).

Với **요구사항 검증 방법 (Phương pháp xác minh yêu cầu)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **요구사항 검증 방법 (Phương pháp xác minh yêu cầu)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **미들웨어 (Middleware)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **미들웨어 (Middleware)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 미들웨어 (Middleware)

Các ý ngay dưới **미들웨어 (Middleware)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- 분산 컴퓨팅 환경에서 서로 다른 기종 간을 연결한다. (Kết nối các nền tảng khác nhau trong môi trường điện toán phân tán).
- 운영체제와 응용 프로그램 사이에서 다양한 서비스를 제공한다. (Cung cấp các dịch vụ nằm giữa HĐH và Ứng dụng).
- 위치 투명성을 제공한다. (Cung cấp tính trong suốt về vị trí - User không cần biết server nằm đâu).
- 사용자가 미들웨어의 내부 동작을 확인하려면 별도의 응용 소프트웨어를 사용해야 한다.
- **종류 (Phân loại):** DB, RPC (Remote Procedure Call), MOM (Message Oriented Middleware), TP-Monitor (Transaction Processing Monitor), ORB (Object Request Broker), WAS (Web Application Server).

Các bullet của **미들웨어 (Middleware)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **미들웨어 (Middleware)**, đừng bắt đầu lại từ số không. **스크럼(Scrum) 상세 (Chi tiết về Scrum)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **스크럼(Scrum) 상세 (Chi tiết về Scrum)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 스크럼(Scrum) 상세 (Chi tiết về Scrum)

Bây giờ ta đi vào nội dung của **스크럼(Scrum) 상세 (Chi tiết về Scrum)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- **제품 책임자 (PO; Product Owner):** 요구사항을 작성하고 우선순위를 결정하는 주체. (Người đại diện khách hàng, tạo và quản lý thứ tự ưu tiên của Product Backlog).
- **스크럼 마스터 (SM; Scrum Master):** 스크럼 회의를 주관하고 장애 요소를 해결하는 가이드. (Người hướng dẫn, giải quyết khó khăn cho team, không phải là sếp quản lý).
- **개발팀 (Development Team):** 디자이너, 테스터 등 개발에 참여하는 모든 인원 (7~8명). (Nhóm đa chức năng trực tiếp làm ra sản phẩm).
- **제품 백로그 (Product Backlog):** 모든 요구사항(User Story) 목록. (Danh sách tổng tổng hợp mọi yêu cầu của sản phẩm).
- **스프린트 (Sprint):** 2~4주 주기의 실제 개발 과정. (Vòng lặp phát triển kéo dài 2-4 tuần).
- **일일 스크럼 (Daily Scrum):** 매일 15분, 서서 진행, 소멸 차트(Burn-down Chart) 사용. (Họp đứng 15 phút mỗi ngày cập nhật tiến độ, dùng Burn-down Chart).
- **스프린트 검토/회고 (Sprint Review/Retrospective):** 검토는 제품 시연, 회고는 프로세스 cải tiến. (Review = Demo sản phẩm; Retrospective = Rút kinh nghiệm quy trình).

Với **스크럼(Scrum) 상세 (Chi tiết về Scrum)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

**스크럼(Scrum) 상세 (Chi tiết về Scrum)** vừa cho ta cách đặt câu hỏi. Bây giờ **XP 주요 실천 방법 (Các kỹ thuật thực hành của XP)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Với **XP 주요 실천 방법 (Các kỹ thuật thực hành của XP)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### XP 주요 실천 방법 (Các kỹ thuật thực hành của XP)

Phần nguồn của **XP 주요 실천 방법 (Các kỹ thuật thực hành của XP)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **짝 프로그래밍 (Pair Programming):** 2 người cùng code trên 1 máy tính.
- **공동 코드 소유 (Collective Ownership):** Code là của chung, ai cũng có quyền sửa.
- **테스트 주도 개발 (TDD - Test-Driven Development):** Viết Test case trước, viết Code sau.
- **전체 팀 (Whole Team):** Khách hàng và team phát triển làm việc cùng nhau như 1 đội.
- **계속적인 통합 (Continuous Integration):** Tích hợp code liên tục (CI) ngay khi xong 1 task.
- **리팩토링 (Refactoring):** Cải thiện cấu trúc code mà không đổi chức năng bên ngoài.
- **소규모 릴리즈 (Small Releases):** Cập nhật/Phát hành các phiên bản nhỏ liên tục.

Các bullet của **XP 주요 실천 방법 (Các kỹ thuật thực hành của XP)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **XP 주요 실천 방법 (Các kỹ thuật thực hành của XP)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **현행 시스템 파악 (Phân tích hệ thống hiện tại)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **현행 시스템 파악 (Phân tích hệ thống hiện tại)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 현행 시스템 파악 (Phân tích hệ thống hiện tại)

Các ý ngay dưới **현행 시스템 파악 (Phân tích hệ thống hiện tại)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- 1단계: 시스템 구성, 기능, 인터페이스 파악. (Bước 1: Nắm bắt Cấu trúc, Chức năng, Interface).
- 2단계: 아키텍처 및 소프트웨어 구성 파악. (Bước 2: Nắm bắt Kiến trúc và Phần mềm).
- 3단계: 하드웨어 및 네트워크 구성 파악. (Bước 3: Nắm bắt Phần cứng và Mạng).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **KGI -> AS -> HN** (Kéo Ghế In -> Áo Sơ -> Hát Nhép) -> Giống như quy trình từ phần mềm đến phần cứng.

Các bullet của **현행 시스템 파악 (Phân tích hệ thống hiện tại)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **현행 시스템 파악 (Phân tích hệ thống hiện tại)**, đừng bắt đầu lại từ số không. **운영체제 (OS - Operating System)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **운영체제 (OS - Operating System)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 운영체제 (OS - Operating System)

Bây giờ ta đi vào nội dung của **운영체제 (OS - Operating System)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 컴퓨터 시스템의 자원들을 효율적으로 관리하며, 환경을 제공하는 소프트웨어이다. (Là phần mềm quản lý tài nguyên máy tính hiệu quả và cung cấp môi trường chạy ứng dụng).
- 고려사항 (Các yếu tố cần cân nhắc khi chọn): 가용성 (Tính sẵn sàng), 성능 (Hiệu năng), 기술 지원 (Hỗ trợ kỹ thuật), 주변 기기 (Thiết bị ngoại vi), 구축 비용 (Chi phí).

Các bullet của **운영체제 (OS - Operating System)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**운영체제 (OS - Operating System)** vừa cho ta cách đặt câu hỏi. Bây giờ **데이터베이스 관리 시스템 (DBMS)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Với **데이터베이스 관리 시스템 (DBMS)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 데이터베이스 관리 시스템 (DBMS)

Phần nguồn của **데이터베이스 관리 시스템 (DBMS)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- 사용자와 데이터베이스 사이에서 정보를 생성하고 관리해 주는 소프트웨어이다. (Phần mềm nằm giữa User và Database để quản lý dữ liệu - giải quyết vấn đề trùng lặp và phụ thuộc).
- 고려사항: 가용성, 성능, 기술 지원, 상호 호환성 (Tính tương thích), 구축 비용.

Các bullet của **데이터베이스 관리 시스템 (DBMS)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Với **데이터베이스 관리 시스템 (DBMS)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Ta có thể khép mục **9. 요구사항 및 시스템 파악 (Yêu cầu & Phân tích Hệ thống)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **10. 요구사항 심화 (Yêu cầu chuyên sâu)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 10. 요구사항 심화 (Yêu cầu chuyên sâu)

Từ **9. 요구사항 및 시스템 파악 (Yêu cầu & Phân tích Hệ thống)**, ta đã có điểm tựa để bước vào **10. 요구사항 심화 (Yêu cầu chuyên sâu)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 6/57 trước khi đi vào chi tiết.

Để đọc **10. 요구사항 심화 (Yêu cầu chuyên sâu)** như một bài học cho người mới, hãy giữ câu hỏi: **một nhu cầu nghiệp vụ được chuyển thành yêu cầu có thể kiểm tra và bàn giao như thế nào?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **요구사항의 유형 (Các loại yêu cầu)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 요구사항의 유형 (Các loại yêu cầu)

Các ý ngay dưới **요구사항의 유형 (Các loại yêu cầu)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- **기능 요구사항 (Functional Requirements):** 시스템이 무엇을 하는지, 어떤 기능을 하는지에 대한 사항. (Hệ thống làm gì, chức năng nào. Ví dụ: Phải có nút Lưu, phải tính toán được thuế).
- **비기능 요구사항 (Non-functional Requirements):** 성능 (Hiệu năng), 인터페이스 (Giao diện), 데이터 (Dữ liệu), 테스트 (Kiểm thử), 보안 (Bảo mật), 품질 (Chất lượng), 제약사항 (Ràng buộc), 프로젝트 관리/지원 (Quản lý dự án/Hỗ trợ). (Là các yêu cầu không trực tiếp là chức năng nhưng quyết định chất lượng hệ thống).
- **Ví dụ (Example):** Chức năng giỏ hàng là "기능" (Chức năng). Nhưng giỏ hàng phải load trong 0.5 giây là "성능" (Hiệu năng - Phi chức năng).

Các ý về **요구사항의 유형 (Các loại yêu cầu)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **요구사항의 유형 (Các loại yêu cầu)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **요구사항 도출 (Requirement Elicitation / Thu thập yêu cầu)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **요구사항 도출 (Requirement Elicitation / Thu thập yêu cầu)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 요구사항 도출 (Requirement Elicitation / Thu thập yêu cầu)

Bây giờ ta đi vào nội dung của **요구사항 도출 (Requirement Elicitation / Thu thập yêu cầu)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 기법 (Kỹ thuật): 청취와 인터뷰 (Lắng nghe & Phỏng vấn), 설문 (Khảo sát), 브레인스토밍 (Brainstorming), 워크샵 (Workshop), 프로토타이핑 (Prototyping), 유스케이스 (Use Case).

Các bullet của **요구사항 도출 (Requirement Elicitation / Thu thập yêu cầu)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **요구사항 도출 (Requirement Elicitation / Thu thập yêu cầu)**, đừng bắt đầu lại từ số không. **요구사항 명세 기법 (Kỹ thuật Đặc tả yêu cầu)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **요구사항 명세 기법 (Kỹ thuật Đặc tả yêu cầu)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 요구사항 명세 기법 (Kỹ thuật Đặc tả yêu cầu)

Phần nguồn của **요구사항 명세 기법 (Kỹ thuật Đặc tả yêu cầu)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **정형 명세 기법 (Formal Specification):** 수학적 기호, 정형화된 표기법 사용 (Dùng ký hiệu toán học). 정확하고 간결, 일관성 있음, 하지만 표기법이 어려워 사용자가 이해하기 어려움. (Chính xác, nhất quán nhưng khó hiểu với user). 종류: VDM, Z, Petri-net, CSP.
- **비정형 명세 기법 (Informal Specification):** 일반 명사, 동사 등의 자연어를 기반으로 서술 또는 다이어그램 작성. (Dùng ngôn ngữ tự nhiên/biểu đồ). 의사소통이 용이하지만 작성자에 따라 해석이 달라질 수 있음. (Dễ giao tiếp nhưng dễ gây hiểu nhầm). 종류: FSM, Decision Table, ER모델링, State Chart.
- 💡 **Mẹo ghi nhớ (Mnemonic):** **CTPT** (Chính-Toán-Phi-Tự) -> **Chăm Toán Phải Tốt** -> 정형 = 수학적 (Chính thức = Toán học), 비정형 = 자연어 (Phi chính thức = Tự nhiên).

Với **요구사항 명세 기법 (Kỹ thuật Đặc tả yêu cầu)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

**요구사항 명세 기법 (Kỹ thuật Đặc tả yêu cầu)** vừa cho ta cách đặt câu hỏi. Bây giờ **요구사항 분석을 위한 CASE 도구 (Công cụ CASE tự động hóa phân tích)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Đoạn **요구사항 분석을 위한 CASE 도구 (Công cụ CASE tự động hóa phân tích)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 요구사항 분석을 위한 CASE 도구 (Công cụ CASE tự động hóa phân tích)

Các ý ngay dưới **요구사항 분석을 위한 CASE 도구 (Công cụ CASE tự động hóa phân tích)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- **SADT:** SoftTech사 개발, 구조적 분석 및 설계 도구. (Công cụ phân tích cấu trúc của SoftTech).
- **SREM (RSL/REVS):** TRW사 개발, 실시간 처리 소프트웨어 요구사항 기술. (Công cụ cho hệ thống thời gian thực, dùng RSL và REVS).
- **PSL/PSA:** 미시간 대학 개발. (Phát triển bởi ĐH Michigan).
- **TAGS:** 개발 주기 전 과정에 이용할 수 있는 통합 자동화 도구. (Công cụ tích hợp toàn bộ vòng đời).

Các bullet của **요구사항 분석을 위한 CASE 도구 (Công cụ CASE tự động hóa phân tích)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Với **요구사항 분석을 위한 CASE 도구 (Công cụ CASE tự động hóa phân tích)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Điểm chốt của **10. 요구사항 심화 (Yêu cầu chuyên sâu)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **2. 요구사항 정의 (Requirements Definition)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 2. 요구사항 정의 (Requirements Definition)

Ở bước 7/57, **2. 요구사항 정의 (Requirements Definition)** xuất hiện như phần tiếp nối của **10. 요구사항 심화 (Yêu cầu chuyên sâu)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **2. 요구사항 정의 (Requirements Definition)** như một bài học cho người mới, hãy giữ câu hỏi: **một nhu cầu nghiệp vụ được chuyển thành yêu cầu có thể kiểm tra và bàn giao như thế nào?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **기능 요구사항 (Functional)**, **비기능 요구사항 (Non-Functional)**, **개발 프로세스 (Development Process)**, **명세 기법 (Specification Techniques)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **기능 요구사항 (Functional)**: Chức năng hệ thống phải có (Ví dụ: Đăng nhập).
- **비기능 요구사항 (Non-Functional)**: Hiệu năng, bảo mật, chất lượng, ràng buộc (Ví dụ: Phản hồi dưới 1s).
- **개발 프로세스 (Development Process)**:
  1. 도출 (Elicitation) -> 2. 분석 (Analysis) -> 3. 명세 (Specification) -> 4. 확인/검증 (Validation).
- 💡 **Mẹo ghi nhớ**: Đ/P/M/X (Elicitation, Analysis, Spec, Validation) -> **Đi Phượt Một Xe**
- **명세 기법 (Specification Techniques)**:
  - 정형 (Formal): Ký hiệu toán học (Toán học, VDM, Z-schema). Rõ ràng nhưng khó hiểu với user.
  - 비정형 (Informal): Ngôn ngữ tự nhiên (Natural language, FSM, ERD). Dễ hiểu nhưng có thể mơ hồ.

Như vậy, **2. 요구사항 정의 (Requirements Definition)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **3. 요구사항 분석기법 및 자동화 도구 (Analysis Techniques & CASE)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 3. 요구사항 분석기법 및 자동화 도구 (Analysis Techniques & CASE)

Sau khi đã đặt nền bằng **2. 요구사항 정의 (Requirements Definition)**, ta chuyển sang **3. 요구사항 분석기법 및 자동화 도구 (Analysis Techniques & CASE)**. Đây là mắt xích 8/57 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **3. 요구사항 분석기법 및 자동화 도구 (Analysis Techniques & CASE)** như một bài học cho người mới, hãy giữ câu hỏi: **một nhu cầu nghiệp vụ được chuyển thành yêu cầu có thể kiểm tra và bàn giao như thế nào?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng là bằng chứng để so sánh các lựa chọn theo cùng tiêu chí, không phải danh sách cần học thuộc từng ô. Trong khối này, **자료 흐름도 (DFD - Data Flow Diagram)**, **자료 사전 (DD - Data Dictionary)**, **CASE 도구 (CASE Tools)**, **HIPO (Hierarchical Input Process Output)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **자료 흐름도 (DFD - Data Flow Diagram)**:
  - 프로세스 (Process - Tròn), 자료 흐름 (Data Flow - Mũi tên), 자료 저장소 (Data Store - Đường thẳng), 단말 (Terminator - Vuông).
- **자료 사전 (DD - Data Dictionary)**:
  - `=`: Định nghĩa (is composed of)
  - `+`: Kết nối (and)
  - `( )`: Tùy chọn (Optional)
  - `[ | ]`: Lựa chọn (or)
  - `{ }`: Lặp lại (Iteration)
  - `**`: Ghi chú (Comment)
- **CASE 도구 (CASE Tools)**: SADT, SREM, PSL/PSA.
- **HIPO (Hierarchical Input Process Output)**: Phân tích Top-down (가시적 도표, 총체적 도표, 세부적 도표).

Ta có thể khép mục **3. 요구사항 분석기법 및 자동화 도구 (Analysis Techniques & CASE)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **1. 요구사항 개발 기법 (Requirements Elicitation Techniques)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 1. 요구사항 개발 기법 (Requirements Elicitation Techniques)

Từ **3. 요구사항 분석기법 및 자동화 도구 (Analysis Techniques & CASE)**, ta đã có điểm tựa để bước vào **1. 요구사항 개발 기법 (Requirements Elicitation Techniques)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 9/57 trước khi đi vào chi tiết.

Để đọc **1. 요구사항 개발 기법 (Requirements Elicitation Techniques)** như một bài học cho người mới, hãy giữ câu hỏi: **một nhu cầu nghiệp vụ được chuyển thành yêu cầu có thể kiểm tra và bàn giao như thế nào?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **도출 (Elicitation) 기법**, **인터뷰 (Interview)**, **브레인스토밍 (Brainstorming)**, **델파이 기법 (Delphi)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **도출 (Elicitation) 기법**:
  - **인터뷰 (Interview)**: Phỏng vấn.
  - **브레인스토밍 (Brainstorming)**: Công não ý tưởng (Không chỉ trích).
  - **델파이 기법 (Delphi)**: Hỏi ý kiến chuyên gia ẩn danh.
  - **프로토타이핑 (Prototyping)**: Làm mẫu thử.

Điểm chốt của **1. 요구사항 개발 기법 (Requirements Elicitation Techniques)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **12. 요구사항 (Requirements)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 12. 요구사항 (Requirements)

Ở bước 10/57, **12. 요구사항 (Requirements)** xuất hiện như phần tiếp nối của **1. 요구사항 개발 기법 (Requirements Elicitation Techniques)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **12. 요구사항 (Requirements)** như một bài học cho người mới, hãy giữ câu hỏi: **một nhu cầu nghiệp vụ được chuyển thành yêu cầu có thể kiểm tra và bàn giao như thế nào?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **요구사항 분석 (Requirements Analysis)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **요구사항 분석 (Requirements Analysis)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 요구사항 분석 (Requirements Analysis)

Bây giờ ta đi vào nội dung của **요구사항 분석 (Requirements Analysis)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

*   **분류 (Phân loại):** 기능적(Functional) / 비기능적(Non-functional)으로 조직화.
*   **절차 (Quy trình 5 bước):** 선별(목록 작성) -> 자료 준비 -> 분류(기능/비기능) -> 분석 및 수정 -> 전달 (Lọc -> Chuẩn bị -> Phân loại -> Phân tích/Sửa -> Truyền đạt).

Các bullet của **요구사항 분석 (Requirements Analysis)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **요구사항 분석 (Requirements Analysis)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **요구사항 검증 (Requirements Verification)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **요구사항 검증 (Requirements Verification)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 요구사항 검증 (Requirements Verification)

Phần nguồn của **요구사항 검증 (Requirements Verification)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

**설계 및 구현 전에 베이스라인(Baseline) 설정** (Xác minh trước khi thiết kế/code để chốt Baseline làm chuẩn).
*   **검증 방법 (Các phương pháp kiểm tra):**
    *   수작업: 동료검토(Peer Review), 워크스루(Walkthrough), 인스펙션(Inspection).
    *   **프로토타이핑 (Prototyping):** 견본 제작 (Làm bản mẫu dùng thử).
    *   **테스트 설계 (Test Design):** 테스트 케이스 생성 (Viết test case trước để xem có test được không).
    *   **CASE 도구:** 자동화 도구로 일관성 분석 (Dùng phần mềm check logic).

Các bullet của **요구사항 검증 (Requirements Verification)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **요구사항 검증 (Requirements Verification)**, đừng bắt đầu lại từ số không. **요구사항 품질 기준 7개 (7 Tiêu chí chất lượng)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **요구사항 품질 기준 7개 (7 Tiêu chí chất lượng)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 요구사항 품질 기준 7개 (7 Tiêu chí chất lượng)

Các ý ngay dưới **요구사항 품질 기준 7개 (7 Tiêu chí chất lượng)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

1.  **완전성 (Completeness):** 누락 없이 (Đầy đủ).
2.  **일관성 (Consistency):** 충돌 없이 (Nhất quán).
3.  **명확성 (Unambiguity):** 똑같이 이해되게 (Rõ ràng).
4.  **기능성 (Functionality):** '어떻게'보다 '무엇을(What)' (Tập trung vào tính năng "Làm gì" hơn là "Làm như thế nào").
5.  **검증 가능성 (Verifiability):** 테스트 가능 여부 (Có thể kiểm chứng/test được).
6.  **추적 가능성 (Traceability):** 설계서와 연결 (Có thể truy xuất).
7.  **변경 용이성 (Easily Changeable):** 수정 용이 (Dễ thay đổi).

---

Phần **요구사항 품질 기준 7개 (7 Tiêu chí chất lượng)** không có nhiều dữ liệu rời để tách nhỏ, vì vậy hãy giữ câu hỏi mục đích và tự chốt bằng một câu giải thích trước khi đi tiếp.

Như vậy, **요구사항 품질 기준 7개 (7 Tiêu chí chất lượng)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Như vậy, **12. 요구사항 (Requirements)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **A+ Deep Dive: 개발 모형 선택과 요구사항 검증**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## A+ Deep Dive: 개발 모형 선택과 요구사항 검증

Sau khi đã đặt nền bằng **12. 요구사항 (Requirements)**, ta chuyển sang **A+ Deep Dive: 개발 모형 선택과 요구사항 검증**. Đây là mắt xích 11/57 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **A+ Deep Dive: 개발 모형 선택과 요구사항 검증** như một bài học cho người mới, hãy giữ câu hỏi: **một nhu cầu nghiệp vụ được chuyển thành yêu cầu có thể kiểm tra và bàn giao như thế nào?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng là bằng chứng để so sánh các lựa chọn theo cùng tiêu chí, không phải danh sách cần học thuộc từng ô.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **1. 모형 선택 비교표**. Hãy xác định **1. 모형 선택 비교표** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 1. 모형 선택 비교표

Phần nguồn của **1. 모형 선택 비교표** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

| 모형 | 가장 강한 신호 | 변경 대응 | 시험 함정 |
|---|---|---|---|
| 폭포수 (Waterfall) | 요구사항이 안정적이고 단계 산출물이 명확함 | 낮음 | 순차적이라는 뜻이 곧 테스트가 없다는 뜻은 아님 |
| 프로토타입 (Prototype) | 사용자가 원하는 결과를 말로 확정하기 어려움 | 요구사항 확인에 유리 | 시제품을 그대로 운영 제품으로 착각하지 않음 |
| 나선형 (Spiral) | 대규모·고위험·불확실성이 큼 | 반복마다 위험 분석 | 보헴(Boehm)과 연결되는 모형은 나선형 |
| 애자일 (Agile) | 짧은 주기와 지속적인 고객 피드백 | 높음 | Agile은 단일 방법론이 아니라 가치와 원칙의 묶음 |

Bảng trong **1. 모형 선택 비교표** không phải danh sách rời. Hãy đọc theo từng cột để nhận ra tiêu chí so sánh, rồi tự diễn đạt bằng một câu: đối tượng nào khác nhau ở điểm nào và trong điều kiện nào sự khác biệt đó có ý nghĩa.

Ta vừa chốt **1. 모형 선택 비교표** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. 요구사항 검증 미니 트레이스** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **2. 요구사항 검증 미니 트레이스** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 2. 요구사항 검증 미니 트레이스

Các ý ngay dưới **2. 요구사항 검증 미니 트레이스** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

1. **완전성(Completeness)**: 모든 기능·제약이 빠짐없이 적혔는가?
2. **일관성(Consistency)**: 서로 모순되는 요구가 없는가?
3. **추적성(Traceability)**: 요구사항 ID가 설계·테스트 항목과 연결되는가?
4. **검증 가능성(Verifiability)**: `빠른 응답` 대신 `95% 요청을 2초 이내 처리`처럼 시험 가능한가?

> **시험 함정:** 검증(Verification)은 명세에 맞게 만들었는지, 확인(Validation)은 사용자의 실제 목적에 맞는지를 묻는다.

Phần **2. 요구사항 검증 미니 트레이스** không có nhiều dữ liệu rời để tách nhỏ, vì vậy hãy giữ câu hỏi mục đích và tự chốt bằng một câu giải thích trước khi đi tiếp.

Sau khi đọc **2. 요구사항 검증 미니 트레이스**, đừng bắt đầu lại từ số không. **자주 혼동하는 판별 포인트** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **자주 혼동하는 판별 포인트**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 자주 혼동하는 판별 포인트

Bây giờ ta đi vào nội dung của **자주 혼동하는 판별 포인트**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- **형상 관리 항목**은 소스 코드만이 아니라 요구사항·설계서·설치/운영 문서처럼 변경 이력을 추적해야 하는 산출물까지 포함한다. 개인 일정이나 예산 자체는 형상 항목이 아니다.
- **EAI Hybrid**는 Hub-and-Spoke와 Message Bus를 조합한다. 모든 애플리케이션을 직접 연결하는 Point-to-Point와 다르다.
- **N-S 차트**는 순차·선택·반복이라는 구조적 제어 흐름을 표현한다. 클래스 메모리 배치나 패킷 헤더를 표현하는 도구가 아니다.
- 내부 자료를 직접 참조하는 모듈은 **내용 결합도**가 강하다. 독립성을 높이려면 결합도는 낮추고 응집도는 높인다.

Các bullet của **자주 혼동하는 판별 포인트** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **자주 혼동하는 판별 포인트** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Ta có thể khép mục **A+ Deep Dive: 개발 모형 선택과 요구사항 검증** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **1. 현행 시스템 분석 (Current System Analysis)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 1. 현행 시스템 분석 (Current System Analysis)

Từ **A+ Deep Dive: 개발 모형 선택과 요구사항 검증**, ta đã có điểm tựa để bước vào **1. 현행 시스템 분석 (Current System Analysis)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 12/57 trước khi đi vào chi tiết.

Để đọc **1. 현행 시스템 분석 (Current System Analysis)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **플랫폼 성능 (Platform Performance)**, **운영체제 및 DBMS 고려사항 (OS & DBMS Considerations)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **플랫폼 성능 (Platform Performance)**:
  - 가용성 (Availability), 경과 시간 (Turnaround Time), 응답 시간 (Response Time), 사용률 (Utilization).
- **운영체제 및 DBMS 고려사항 (OS & DBMS Considerations)**:
  - 신뢰도 (Reliability), 성능 (Performance), 기술 지원 (Tech Support), 주변 기기 (Peripherals), 구축 비용 (Cost), 상호 호환성 (Compatibility).

Điểm chốt của **1. 현행 시스템 분석 (Current System Analysis)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **3. 현행 시스템 파악 (Understanding Current System)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 3. 현행 시스템 파악 (Understanding Current System)

Ở bước 13/57, **3. 현행 시스템 파악 (Understanding Current System)** xuất hiện như phần tiếp nối của **1. 현행 시스템 분석 (Current System Analysis)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **3. 현행 시스템 파악 (Understanding Current System)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **1단계**, **2단계**, **3단계** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **1단계**: 시스템 구성 (기간 업무/지원 업무), 기능 (계층형), 인터페이스 (Giao thức, loại liên kết).
- **2단계**: 아키텍처 구성 (Kiến trúc), 소프트웨어 구성 (Bản quyền - 라이선스).
- **3단계**: 하드웨어 구성 (Dự phòng - 이중화/Redundancy), 네트워크 구성 (Vị trí vật lý, mạng).

Như vậy, **3. 현행 시스템 파악 (Understanding Current System)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **3. 모델링 및 UML (Mô hình hóa và UML)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 3. 모델링 및 UML (Mô hình hóa và UML)

Sau khi đã đặt nền bằng **3. 현행 시스템 파악 (Understanding Current System)**, ta chuyển sang **3. 모델링 및 UML (Mô hình hóa và UML)**. Đây là mắt xích 14/57 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **3. 모델링 및 UML (Mô hình hóa và UML)** như một bài học cho người mới, hãy giữ câu hỏi: **ta dùng mô hình nào để biểu diễn đối tượng, quan hệ hoặc hành vi, và giới hạn của mỗi cách là gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **013. UML (Unified Modeling Language)**. Hãy xác định **013. UML (Unified Modeling Language)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 013. UML (Unified Modeling Language)

Phần nguồn của **013. UML (Unified Modeling Language)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- 시스템 개발자와 고객 또는 개발자 상호 간의 의사소통이 원활하게 이루어지도록 표준화한 대표적인 객체지향 모델링 언어이다. (Là ngôn ngữ mô hình hóa hướng đối tượng tiêu biểu được chuẩn hóa để việc giao tiếp giữa nhà phát triển hệ thống và khách hàng, hoặc giữa các nhà phát triển với nhau diễn ra suôn sẻ.)
- 구성 요소 (Components): 사물 (Things - Sự vật), 관계 (Relationships - Mối quan hệ), 다이어그램 (Diagram - Biểu đồ).
- **Ví dụ (Example):** Khi xây nhà cần bản vẽ thiết kế (Blueprint). Khi làm phần mềm, dùng UML làm bản vẽ thiết kế chung để ai cũng hiểu.
- 💡 **Mẹo ghi nhớ (Mnemonic):** **SQĐ** (Sự - Quan - Đa): **Sợ Quá Đi** (Sự vật - Quan hệ - Đa biểu đồ).

Các ý về **013. UML (Unified Modeling Language)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **013. UML (Unified Modeling Language)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **014. UML의 주요 관계 (Các mối quan hệ chính trong UML)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **014. UML의 주요 관계 (Các mối quan hệ chính trong UML)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 014. UML의 주요 관계 (Các mối quan hệ chính trong UML)

Các ý ngay dưới **014. UML의 주요 관계 (Các mối quan hệ chính trong UML)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- 일반화 (Generalization) 관계: 하나의 사물이 다른 사물에 비해 더 일반적인지 구체적인지를 표현. (Thể hiện một sự vật là tổng quát hay cụ thể hơn sự vật khác - kế thừa).
- 의존 (Dependency) 관계: 필요에 의해 서로에게 영향을 주는 짧은 시간 동안만 연관을 유지하는 관계를 표현. (Thể hiện mối quan hệ phụ thuộc ngắn hạn, ảnh hưởng lẫn nhau khi cần thiết).
- 실체화 (Realization) 관계: 사물이 할 수 있거나 해야 하는 기능으로 서로를 그룹화 할 수 있는 관계를 표현. (Thể hiện mối quan hệ hiện thực hóa chức năng mà sự vật có thể/phải làm - interface).
- **Ví dụ (Example):** Động vật -> Chó, Mèo là mối quan hệ '일반화' (Generalization).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **NYT** (Nhất - Ý - Thực): **Như Ý Thật** (Nhất quát - Ý tồn - Thực thể).

Các ý về **014. UML의 주요 관계 (Các mối quan hệ chính trong UML)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Sau khi đọc **014. UML의 주요 관계 (Các mối quan hệ chính trong UML)**, đừng bắt đầu lại từ số không. **015. 구조적(Structural) 다이어그램의 종류 (Các loại biểu đồ cấu trúc - Tĩnh)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **015. 구조적(Structural) 다이어그램의 종류 (Các loại biểu đồ cấu trúc - Tĩnh)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 015. 구조적(Structural) 다이어그램의 종류 (Các loại biểu đồ cấu trúc - Tĩnh)

Bây giờ ta đi vào nội dung của **015. 구조적(Structural) 다이어그램의 종류 (Các loại biểu đồ cấu trúc - Tĩnh)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 클래스 다이어그램 (Class Diagram)
- 객체 다이어그램 (Object Diagram)
- 컴포넌트 다이어그램 (Component Diagram)
- 배치 다이어그램 (Deployment Diagram)
- 복합체 구조 다이어그램 (Composite Structure Diagram)
- 패키지 다이어그램 (Package Diagram)
- **Ví dụ (Example):** Class Diagram thể hiện cấu trúc tĩnh của hệ thống, giống như sơ đồ tổ chức của một công ty.
- 💡 **Mẹo ghi nhớ (Mnemonic):** **LĐCBPG** (Lớp - Đối - Com - Bố - Phức - Gói): **Làm Được Có Bữa Phải Giỏi**. Các biểu đồ này thể hiện cấu trúc "Tĩnh" (정적).

Các ý về **015. 구조적(Structural) 다이어그램의 종류 (Các loại biểu đồ cấu trúc - Tĩnh)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

**015. 구조적(Structural) 다이어그램의 종류 (Các loại biểu đồ cấu trúc - Tĩnh)** vừa cho ta cách đặt câu hỏi. Bây giờ **016. 행위(Behavioral) 다이어그램의 종류 (Các loại biểu đồ hành vi - Động)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Với **016. 행위(Behavioral) 다이어그램의 종류 (Các loại biểu đồ hành vi - Động)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 016. 행위(Behavioral) 다이어그램의 종류 (Các loại biểu đồ hành vi - Động)

Phần nguồn của **016. 행위(Behavioral) 다이어그램의 종류 (Các loại biểu đồ hành vi - Động)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- 유스케이스 다이어그램 (Use Case Diagram)
- 순차 다이어그램 (Sequence Diagram)
- 커뮤니케이션 다이어그램 (Communication Diagram)
- 상태 다이어그램 (State Diagram)
- 활동 다이어그램 (Activity Diagram)
- 상호작용 개요 다이어그램 (Interaction Overview Diagram)
- 타이밍 다이어그램 (Timing Diagram)
- **Ví dụ (Example):** Sequence Diagram thể hiện trình tự thời gian gửi tin nhắn (메시지) giữa các đối tượng (hành vi động).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **UTCTHTT** (Use - Trình - Com - Trạng - Hoạt - Tương - Time): **Uống Trà Chiều Thấy Hay Thật Tuyệt**. Các biểu đồ này thể hiện đặc tính "Động" (동적).

Các ý về **016. 행위(Behavioral) 다이어그램의 종류 (Các loại biểu đồ hành vi - Động)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **016. 행위(Behavioral) 다이어그램의 종류 (Các loại biểu đồ hành vi - Động)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **017. 스테레오 타입 (Stereotype)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **017. 스테레오 타입 (Stereotype)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 017. 스테레오 타입 (Stereotype)

Các ý ngay dưới **017. 스테레오 타입 (Stereotype)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- UML에서 표현하는 기본 기능 외에 추가적인 기능을 표현하기 위해 사용한다. (Dùng để biểu diễn các chức năng bổ sung ngoài chức năng cơ bản trong UML.)
- 길러멧(Guilemet)이라고 부르는 겹화살괄호(`<< >>`) 사이에 표현할 형태를 기술한다. (Viết hình thái muốn biểu diễn giữa cặp dấu ngoặc nhọn kép `<< >>` gọi là Guilemet.)
- **Ví dụ (Example):** `<<include>>` hoặc `<<extend>>` trong Use Case Diagram.

Các ý về **017. 스테레오 타입 (Stereotype)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Sau khi đọc **017. 스테레오 타입 (Stereotype)**, đừng bắt đầu lại từ số không. **018. 유스케이스 다이어그램 - 액터(Actor) (Biểu đồ Use Case - Tác nhân)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **018. 유스케이스 다이어그램 - 액터(Actor) (Biểu đồ Use Case - Tác nhân)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 018. 유스케이스 다이어그램 - 액터(Actor) (Biểu đồ Use Case - Tác nhân)

Bây giờ ta đi vào nội dung của **018. 유스케이스 다이어그램 - 액터(Actor) (Biểu đồ Use Case - Tác nhân)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 시스템과 상호작용을 하는 모든 외부 요소로, 사람이나 외부 시스템을 의미한다. (Là tất cả các yếu tố bên ngoài tương tác với hệ thống, có nghĩa là con người hoặc hệ thống bên ngoài.)
- 주액터 (Primary Actor): 시스템을 사용함으로써 이득을 얻는 대상으로, 주로 사람이 해당함. (Đối tượng nhận được lợi ích khi dùng hệ thống, chủ yếu là con người - ví dụ: Khách hàng.)
- 부액터 (Secondary Actor): 주액터의 목적 달성을 위해 시스템에 서비스를 제공하는 외부 시스템으로, 조직이나 기관 등이 될 수 있음. (Hệ thống bên ngoài cung cấp dịch vụ cho hệ thống để đạt mục đích của Primary Actor - ví dụ: Cổng thanh toán ngân hàng.)

Các ý về **018. 유스케이스 다이어그램 - 액터(Actor) (Biểu đồ Use Case - Tác nhân)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

**018. 유스케이스 다이어그램 - 액터(Actor) (Biểu đồ Use Case - Tác nhân)** vừa cho ta cách đặt câu hỏi. Bây giờ **019. 순차(Sequence) 다이어그램의 구성 요소 (Thành phần của biểu đồ Sequence)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Với **019. 순차(Sequence) 다이어그램의 구성 요소 (Thành phần của biểu đồ Sequence)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 019. 순차(Sequence) 다이어그램의 구성 요소 (Thành phần của biểu đồ Sequence)

Phần nguồn của **019. 순차(Sequence) 다이어그램의 구성 요소 (Thành phần của biểu đồ Sequence)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- 액터 (Actor - Tác nhân)
- 객체 (Object - Đối tượng)
- 생명선 (Lifeline - Đường đời)
- 실행 상자 (Active Box - Hộp thực thi)
- 메시지 (Message - Thông điệp)
- **Ví dụ (Example):** Khi user (Actor) ấn nút mua hàng, một mũi tên (Message) sẽ được gửi đến Giỏ hàng (Object). Đường nét đứt sổ dọc xuống từ Giỏ hàng là 생명선 (Lifeline).

Các ý về **019. 순차(Sequence) 다이어그램의 구성 요소 (Thành phần của biểu đồ Sequence)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Với **019. 순차(Sequence) 다이어그램의 구성 요소 (Thành phần của biểu đồ Sequence)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Ta có thể khép mục **3. 모델링 및 UML (Mô hình hóa và UML)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **11. 모델링 및 다이어그램 심화 (Mô hình hóa & Biểu đồ chuyên sâu)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 11. 모델링 및 다이어그램 심화 (Mô hình hóa & Biểu đồ chuyên sâu)

Từ **3. 모델링 및 UML (Mô hình hóa và UML)**, ta đã có điểm tựa để bước vào **11. 모델링 및 다이어그램 심화 (Mô hình hóa & Biểu đồ chuyên sâu)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 15/57 trước khi đi vào chi tiết.

Để đọc **11. 모델링 및 다이어그램 심화 (Mô hình hóa & Biểu đồ chuyên sâu)** như một bài học cho người mới, hãy giữ câu hỏi: **ta dùng mô hình nào để biểu diễn đối tượng, quan hệ hoặc hành vi, và giới hạn của mỗi cách là gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **웹 애플리케이션 서버 (WAS - Web Application Server)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 웹 애플리케이션 서버 (WAS - Web Application Server)

Các ý ngay dưới **웹 애플리케이션 서버 (WAS - Web Application Server)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- 동적인 콘텐츠를 처리하기 위해 사용되는 미들웨어. (Middleware xử lý các nội dung web động thay vì web tĩnh).
- 종류: Tomcat, GlassFish, JBoss, Jetty, JEUS, Resin, WebLogic, WebSphere.

Các bullet của **웹 애플리케이션 서버 (WAS - Web Application Server)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **웹 애플리케이션 서버 (WAS - Web Application Server)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **자료 흐름도 (DFD) 표기법 차이 (Khác biệt ký hiệu DFD)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **자료 흐름도 (DFD) 표기법 차이 (Khác biệt ký hiệu DFD)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 자료 흐름도 (DFD) 표기법 차이 (Khác biệt ký hiệu DFD)

Bây giờ ta đi vào nội dung của **자료 흐름도 (DFD) 표기법 차이 (Khác biệt ký hiệu DFD)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- **Yourdon/DeMarco:** 프로세스를 원(원형)으로 표시. (Process là hình tròn).
- **Gane/Sarson:** 프로세스를 둥근 사각형으로 표시. (Process là hình chữ nhật bo góc).

Các bullet của **자료 흐름도 (DFD) 표기법 차이 (Khác biệt ký hiệu DFD)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **자료 흐름도 (DFD) 표기법 차이 (Khác biệt ký hiệu DFD)**, đừng bắt đầu lại từ số không. **HIPO Chart의 종류 (Các loại biểu đồ HIPO)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **HIPO Chart의 종류 (Các loại biểu đồ HIPO)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### HIPO Chart의 종류 (Các loại biểu đồ HIPO)

Phần nguồn của **HIPO Chart의 종류 (Các loại biểu đồ HIPO)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **가시적 도표 (Visual Table of Contents):** 시스템의 전체적인 기능과 흐름을 보여주는 계층(Tree) 구조도. (Cấu trúc cây tổng thể).
- **총체적 도표 (Overview Diagram):** 입력, 처리, 출력에 대한 전반적인 정보를 제공. (Cung cấp thông tin tổng quan I-P-O).
- **세부적 도표 (Detail Diagram):** 기본 요소들을 상세히 기술하는 도표. (Mô tả chi tiết các yếu tố cơ bản).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **GTT** (Gia - Tổng - Tế): **Giữ Trật Tự**.

Các bullet của **HIPO Chart의 종류 (Các loại biểu đồ HIPO)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**HIPO Chart의 종류 (Các loại biểu đồ HIPO)** vừa cho ta cách đặt câu hỏi. Bây giờ **클래스 다이어그램 심화 (Class Diagram chi tiết)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Đoạn **클래스 다이어그램 심화 (Class Diagram chi tiết)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 클래스 다이어그램 심화 (Class Diagram chi tiết)

Các ý ngay dưới **클래스 다이어그램 심화 (Class Diagram chi tiết)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- **클래스 (Class):** 3개의 구획으로 나뉨 (Chia làm 3 phần). 이름 (Tên class), 속성 (Attribute/Biến), 오퍼레이션 (Operation/Hàm, Phương thức).
- **관계 (Relationships) 심화:**
  - **연관 (Association):** 2개 이상의 사물이 서로 관련되어 있음 (Mũi tên ngang).
  - **집합 (Aggregation):** 하나의 사물이 다른 사물에 포함되어 있는 관계 (Hình thoi rỗng). (Ví dụ: Máy tính và Chuột - Mất máy tính chuột vẫn tồn tại).
  - **포함 (Composition):** 집합 관계의 특수한 형태, 포함하는 사물의 변화가 포함되는 사물에게 영향을 미치는 관계 (Hình thoi đặc). (Ví dụ: Tòa nhà và Căn phòng - Phá tòa nhà thì phòng cũng mất).

Các ý về **클래스 다이어그램 심화 (Class Diagram chi tiết)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **클래스 다이어그램 심화 (Class Diagram chi tiết)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **스테레오 타입 (Stereotype) 추가** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **스테레오 타입 (Stereotype) 추가**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 스테레오 타입 (Stereotype) 추가

Bây giờ ta đi vào nội dung của **스테레오 타입 (Stereotype) 추가**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- `<<include>>`: 연결된 다른 UML 요소에 대해 포함 관계. (Quan hệ Bắt buộc phải có - Bắt buộc thực hiện Use case kia).
- `<<extend>>`: 확장 관계. (Quan hệ Tùy chọn/Mở rộng - Có thể thực hiện hoặc không).
- `<<interface>>`: 인터페이스 정의. (Định nghĩa Interface).
- `<<exception>>`: 예외 정의. (Định nghĩa Ngoại lệ).
- `<<constructor>>`: 생성자 역할. (Đóng vai trò Hàm khởi tạo).

Các bullet của **스테레오 타입 (Stereotype) 추가** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **스테레오 타입 (Stereotype) 추가**, đừng bắt đầu lại từ số không. **순차 다이어그램 심화 (Sequence Diagram chi tiết)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **순차 다이어그램 심화 (Sequence Diagram chi tiết)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 순차 다이어그램 심화 (Sequence Diagram chi tiết)

Phần nguồn của **순차 다이어그램 심화 (Sequence Diagram chi tiết)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **생명선 (Lifeline):** 객체가 메모리에 존재하는 기간 (Đường nét đứt sổ dọc xuống).
- **실행 상자 (Active Box):** 객체가 메시지를 주고받으며 구동되고 있음을 표현 (Hình chữ nhật nằm trên đường sinh mệnh).

Các bullet của **순차 다이어그램 심화 (Sequence Diagram chi tiết)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**순차 다이어그램 심화 (Sequence Diagram chi tiết)** vừa cho ta cách đặt câu hỏi. Bây giờ **사용자 인터페이스(UI) 특성 (Đặc tính của UI)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Đoạn **사용자 인터페이스(UI) 특성 (Đặc tính của UI)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 사용자 인터페이스(UI) 특성 (Đặc tính của UI)

Các ý ngay dưới **사용자 인터페이스(UI) 특성 (Đặc tính của UI)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- 소프트웨어 영역 중 변경이 가장 많이 발생한다. (Là phần thường xuyên bị thay đổi nhất trong phần mềm).
- 최소한의 노력으로 원하는 결과를 얻을 수 있게 한다. (Giúp user đạt kết quả mong muốn với nỗ lực ít nhất).

Các bullet của **사용자 인터페이스(UI) 특성 (Đặc tính của UI)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Với **사용자 인터페이스(UI) 특성 (Đặc tính của UI)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Điểm chốt của **11. 모델링 및 다이어그램 심화 (Mô hình hóa & Biểu đồ chuyên sâu)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **4. UML (Unified Modeling Language)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 4. UML (Unified Modeling Language)

Ở bước 16/57, **4. UML (Unified Modeling Language)** xuất hiện như phần tiếp nối của **11. 모델링 및 다이어그램 심화 (Mô hình hóa & Biểu đồ chuyên sâu)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **4. UML (Unified Modeling Language)** như một bài học cho người mới, hãy giữ câu hỏi: **ta dùng mô hình nào để biểu diễn đối tượng, quan hệ hoặc hành vi, và giới hạn của mỗi cách là gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **개념**, **구성요소**, **관계 (Relationships)**, **다이어그램 (Diagrams)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **개념**: Ngôn ngữ mô hình hóa hướng đối tượng chuẩn.
- **구성요소**: 사물 (Things), 관계 (Relationships), 다이어그램 (Diagrams).
- **관계 (Relationships)**:
  - 연관 (Association), 의존 (Dependency), 집합 (Aggregation), 포함 (Composition), 일반화 (Generalization - Kế thừa), 실체화 (Realization - Interface).
- **다이어그램 (Diagrams)**:
  - **구조적/정적 (Structural/Static)**: Class, Object, Component, Deployment, Composite Structure, Package.
  - **행위적/동적 (Behavioral/Dynamic)**: Use Case, Sequence, Communication, State, Activity, Timing.
- 💡 **Mẹo ghi nhớ**:
  - 정적 다이어그램: 클/객/컴/배/복/패 (Class, Object, Component, Deployment, Composite, Package)
  - 동적 다이어그램: 유/순/커/상/활/타 (Use case, Sequence, Comm, State, Activity, Timing)

Như vậy, **4. UML (Unified Modeling Language)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **5. UML 구성요소 상세 (UML Components Detail)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 5. UML 구성요소 상세 (UML Components Detail)

Sau khi đã đặt nền bằng **4. UML (Unified Modeling Language)**, ta chuyển sang **5. UML 구성요소 상세 (UML Components Detail)**. Đây là mắt xích 17/57 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **5. UML 구성요소 상세 (UML Components Detail)** như một bài học cho người mới, hãy giữ câu hỏi: **ta dùng mô hình nào để biểu diễn đối tượng, quan hệ hoặc hành vi, và giới hạn của mỗi cách là gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **클래스 다이어그램 (Class Diagram)**, **유스케이스 다이어그램 (Use Case Diagram)**, **순차 다이어그램 (Sequence Diagram)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **클래스 다이어그램 (Class Diagram)**: Class Name, Attribute, Operation.
  - 접근 제어자 (Access Modifier): `+` (Public), `-` (Private), `#` (Protected), `~` (Package).
- **유스케이스 다이어그램 (Use Case Diagram)**: System, Use Case, Actor.
  - Quan hệ: `<<include>>` (Bắt buộc), `<<extend>>` (Tùy chọn), Generalization (Kế thừa).
- **순차 다이어그램 (Sequence Diagram)**: Object, Lifeline, Activation, Message, Self-Message.
  - Thể hiện sự tương tác theo thời gian.

Ta có thể khép mục **5. UML 구성요소 상세 (UML Components Detail)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **7. UML 심화 (Advanced UML)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 7. UML 심화 (Advanced UML)

Từ **5. UML 구성요소 상세 (UML Components Detail)**, ta đã có điểm tựa để bước vào **7. UML 심화 (Advanced UML)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 18/57 trước khi đi vào chi tiết.

Để đọc **7. UML 심화 (Advanced UML)** như một bài học cho người mới, hãy giữ câu hỏi: **ta dùng mô hình nào để biểu diễn đối tượng, quan hệ hoặc hành vi, và giới hạn của mỗi cách là gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **다이어그램 (Diagrams)**, **스테레오 타입 (Stereotype)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- Do OMG chuẩn hóa từ phương pháp của Rumbaugh, Booch, Jacobson.
- **다이어그램 (Diagrams)**:
  - 구조적 (Structural / Tĩnh): Class, Object, Component, Deployment, Composite, Package.
  - 행위적 (Behavioral / Động): Use Case, Sequence, Communication, State, Activity, Timing.
- **스테레오 타입 (Stereotype)**: Mở rộng UML bằng dấu `<< >>` (Guillemet). Ví dụ: `<<include>>`, `<<extend>>`.

Điểm chốt của **7. UML 심화 (Advanced UML)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **4. 사용자 인터페이스 (Giao diện người dùng - UI)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 4. 사용자 인터페이스 (Giao diện người dùng - UI)

Ở bước 19/57, **4. 사용자 인터페이스 (Giao diện người dùng - UI)** xuất hiện như phần tiếp nối của **7. UML 심화 (Advanced UML)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **4. 사용자 인터페이스 (Giao diện người dùng - UI)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **020. 사용자 인터페이스의 특징 (Đặc điểm của giao diện người dùng)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **020. 사용자 인터페이스의 특징 (Đặc điểm của giao diện người dùng)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 020. 사용자 인터페이스의 특징 (Đặc điểm của giao diện người dùng)

Bây giờ ta đi vào nội dung của **020. 사용자 인터페이스의 특징 (Đặc điểm của giao diện người dùng)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 사용자의 편리성과 가독성을 높여준다. (Tăng tính tiện lợi và khả năng đọc cho người dùng.)
- 작업 시간을 단축시킨다. (Rút ngắn thời gian làm việc.)
- 업무에 대한 이해도를 높여준다. (Tăng cường sự hiểu biết về công việc.)
- 사용자 중심으로 설계되어 있다. (Được thiết kế lấy người dùng làm trung tâm.)

Các bullet của **020. 사용자 인터페이스의 특징 (Đặc điểm của giao diện người dùng)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **020. 사용자 인터페이스의 특징 (Đặc điểm của giao diện người dùng)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **021. 사용자 인터페이스의 구분 (Phân loại giao diện người dùng)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **021. 사용자 인터페이스의 구분 (Phân loại giao diện người dùng)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 021. 사용자 인터페이스의 구분 (Phân loại giao diện người dùng)

Phần nguồn của **021. 사용자 인터페이스의 구분 (Phân loại giao diện người dùng)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- CLI (Command Line Interface): 명령과 출력이 텍스트 형태로 이뤄지는 인터페이스 (Giao diện mà lệnh và đầu ra đều dưới dạng văn bản - VD: CMD, Terminal).
- GUI (Graphical User Interface): 아이콘이나 메뉴를 마우스로 선택하여 작업을 수행하는 그래픽 환경의 인터페이스 (Giao diện môi trường đồ họa, dùng chuột chọn icon/menu - VD: Windows, MacOS).
- NUI (Natural User Interface): 사용자의 말이나 행동으로 기기를 조작하는 인터페이스 (Giao diện thao tác thiết bị bằng lời nói hoặc hành động của người dùng - VD: Siri, Kinect).

Các bullet của **021. 사용자 인터페이스의 구분 (Phân loại giao diện người dùng)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **021. 사용자 인터페이스의 구분 (Phân loại giao diện người dùng)**, đừng bắt đầu lại từ số không. **022. 사용자 인터페이스의 기본 원칙 (Nguyên tắc cơ bản của UI)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **022. 사용자 인터페이스의 기본 원칙 (Nguyên tắc cơ bản của UI)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 022. 사용자 인터페이스의 기본 원칙 (Nguyên tắc cơ bản của UI)

Các ý ngay dưới **022. 사용자 인터페이스의 기본 원칙 (Nguyên tắc cơ bản của UI)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- 직관성 (Tính trực quan): 누구나 쉽게 이해하고 사용할 수 있어야 한다. (Bất kỳ ai cũng có thể dễ dàng hiểu và sử dụng.)
- 유효성 (Tính hữu hiệu): 사용자의 목적을 정확하고 완벽하게 달성해야 한다. (Phải đạt được mục đích của người dùng một cách chính xác và hoàn hảo.)
- 학습성 (Tính học hỏi): 누구나 쉽게 배우고 익힐 수 있어야 한다. (Bất kỳ ai cũng có thể dễ dàng học và làm quen.)
- 유연성 (Tính linh hoạt): 요구사항을 최대한 수용하며, 실수를 방지. (Tính linh hoạt, tối đa hóa việc đáp ứng yêu cầu người dùng).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **THHN** (Trực - Hữu - Học - Nhu): **Trực Học Hằng Ngày**.

Các bullet của **022. 사용자 인터페이스의 기본 원칙 (Nguyên tắc cơ bản của UI)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**022. 사용자 인터페이스의 기본 원칙 (Nguyên tắc cơ bản của UI)** vừa cho ta cách đặt câu hỏi. Bây giờ **023. 목업 (Mockup)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Ở đoạn **023. 목업 (Mockup)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 023. 목업 (Mockup)

Bây giờ ta đi vào nội dung của **023. 목업 (Mockup)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 와이어프레임보다 좀 더 실제 화면과 유사하게 만든 정적인 형태의 모형이다. (Là mô hình dạng tĩnh, được làm giống với màn hình thực tế hơn so với Wireframe.)
- 시각적으로만 구성 요소를 배치하는 것으로 실제로 구현되지는 않는다. (Chỉ bố trí các thành phần về mặt thị giác chứ thực tế không hoạt động/code chưa chạy.)
- **Ví dụ (Example):** Dùng Figma vẽ ra một màn hình app đẹp long lanh, nhưng bấm vào các nút không có phản hồi logic gì, đó là Mockup.

Các ý về **023. 목업 (Mockup)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Với **023. 목업 (Mockup)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Như vậy, **4. 사용자 인터페이스 (Giao diện người dùng - UI)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **1. 사용자 인터페이스 (User Interface - UI)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 1. 사용자 인터페이스 (User Interface - UI)

Sau khi đã đặt nền bằng **4. 사용자 인터페이스 (Giao diện người dùng - UI)**, ta chuyển sang **1. 사용자 인터페이스 (User Interface - UI)**. Đây là mắt xích 20/57 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **1. 사용자 인터페이스 (User Interface - UI)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **UI 유형 (UI Types)**, **모바일 제스처 (Mobile Gestures)**, **UI 기본 원칙 (4 Principles)**, **직관성 (Intuitiveness)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **UI 유형 (UI Types)**:
  - CLI (Dòng lệnh), GUI (Đồ họa), NUI (Cử chỉ tự nhiên như chạm, vuốt), OUI (Hữu cơ).
  - **모바일 제스처 (Mobile Gestures)**: Tap (Chạm), Double Tap, Drag (Kéo), Pan (Di chuyển liên tục), Press (Nhấn giữ), Flick (Vuốt nhanh), Pinch (Phóng to/thu nhỏ bằng 2 ngón).
- **UI 기본 원칙 (4 Principles)**:
  - **직관성 (Intuitiveness)**: Dễ hiểu, trực quan.
  - **유효성 (Effectiveness)**: Đạt được mục tiêu của người dùng một cách chính xác và đầy đủ.
  - **학습성 (Learnability)**: Dễ học.
  - **유연성 (Flexibility)**: Linh hoạt, giảm thiểu lỗi.
  - 💡 **Mẹo ghi nhớ**: T/H/H/N -> **Trực Học Hằng Ngày**
- **UI 설계 도구 (UI Design Tools)**:
  - **와이어프레임 (Wireframe)**: Khung xương (Tĩnh).
  - **목업 (Mockup)**: Thiết kế tĩnh, giống thật nhất.
  - **스토리보드 (Storyboard)**: Bản hướng dẫn chi tiết, có luồng di chuyển.
  - **프로토타입 (Prototype)**: Mô hình động, có thể tương tác.

---

Ta có thể khép mục **1. 사용자 인터페이스 (User Interface - UI)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **12. UI 및 아키텍처 설계 심화 (Thiết kế UI & Kiến trúc chuyên sâu)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 12. UI 및 아키텍처 설계 심화 (Thiết kế UI & Kiến trúc chuyên sâu)

Từ **1. 사용자 인터페이스 (User Interface - UI)**, ta đã có điểm tựa để bước vào **12. UI 및 아키텍처 설계 심화 (Thiết kế UI & Kiến trúc chuyên sâu)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 21/57 trước khi đi vào chi tiết.

Để đọc **12. UI 및 아키텍처 설계 심화 (Thiết kế UI & Kiến trúc chuyên sâu)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **사용자 인터페이스(UI) 추가 유형 (Các loại UI bổ sung)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 사용자 인터페이스(UI) 추가 유형 (Các loại UI bổ sung)

Các ý ngay dưới **사용자 인터페이스(UI) 추가 유형 (Các loại UI bổ sung)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- **VUI (Voice User Interface):** 사람의 음성으로 기기를 조작하는 인터페이스. (Giao diện điều khiển bằng giọng nói - VD: Bixby, Alexa).
- **OUI (Organic User Interface):** 모든 사물과 사용자 간의 상호작용을 위한 인터페이스 (사물 인터넷, VR, AR, MR 등). (Giao diện hữu cơ, tương tác vật lý/thực tế ảo).

Các bullet của **사용자 인터페이스(UI) 추가 유형 (Các loại UI bổ sung)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **사용자 인터페이스(UI) 추가 유형 (Các loại UI bổ sung)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **사용자 인터페이스 설계 지침 (Hướng dẫn thiết kế UI)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **사용자 인터페이스 설계 지침 (Hướng dẫn thiết kế UI)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 사용자 인터페이스 설계 지침 (Hướng dẫn thiết kế UI)

Bây giờ ta đi vào nội dung của **사용자 인터페이스 설계 지침 (Hướng dẫn thiết kế UI)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- **사용자 중심 (User-centric):** 실사용자에 대한 이해가 바탕이 되어야 함. (Dựa trên sự hiểu biết về người dùng thực tế).
- **사용성 (Usability):** 설계 시 가장 우선적으로 고려해야 함. (Ưu tiên hàng đầu khi thiết kế - dễ hiểu, dễ dùng).
- **심미성 (Aesthetics):** 디자인적으로 완성도 높게 그래픽 요소 배치. (Bố trí đồ họa thẩm mỹ cao).
- **오류 발생 해결 (Error Recovery):** 오류 발생 시 쉽게 인지하고 해결할 수 있도록 설계. (Giúp user dễ nhận biết và khắc phục lỗi).

Các bullet của **사용자 인터페이스 설계 지침 (Hướng dẫn thiết kế UI)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **사용자 인터페이스 설계 지침 (Hướng dẫn thiết kế UI)**, đừng bắt đầu lại từ số không. **UI 설계 도구 심화 (Công cụ thiết kế UI chi tiết)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **UI 설계 도구 심화 (Công cụ thiết kế UI chi tiết)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### UI 설계 도구 심화 (Công cụ thiết kế UI chi tiết)

Phần nguồn của **UI 설계 도구 심화 (Công cụ thiết kế UI chi tiết)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **와이어프레임 (Wireframe):** 개략적인 레이아웃이나 뼈대 설계 (손그림, 스케치). (Khung xương, layout sơ lược).
- **목업 (Mockup):** 실제 화면과 유사하게 만든 정적인 형태의 모형. (Mô hình tĩnh giống thật nhưng không chạy được logic).
- **스토리보드 (Storyboard):** 와이어프레임 + 콘텐츠 설명 + 페이지 이동 흐름. 디자이너/개발자의 최종 참고 문서. (Tài liệu chi tiết nhất gồm wireframe + mô tả nội dung + luồng di chuyển).
- **프로토타입 (Prototype):** 인터랙션을 적용하여 실제 구현된 것처럼 테스트 가능한 동적인 모형. (Mô hình động có tương tác, test thử được).
- **유스케이스 (Use Case):** 사용자 측면의 요구사항 기술. (Mô tả yêu cầu chức năng từ góc nhìn người dùng).

Các bullet của **UI 설계 도구 심화 (Công cụ thiết kế UI chi tiết)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**UI 설계 도구 심화 (Công cụ thiết kế UI chi tiết)** vừa cho ta cách đặt câu hỏi. Bây giờ **UI 주요 요소 (Các thành phần UI)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Đoạn **UI 주요 요소 (Các thành phần UI)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### UI 주요 요소 (Các thành phần UI)

Các ý ngay dưới **UI 주요 요소 (Các thành phần UI)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- **체크 박스 (Check Box):** 1개 이상의 값을 선택할 수 있는 버튼. (Chọn nhiều - Multiple choice).
- **라디오 버튼 (Radio Button):** 여러 항목 중 하나만 선택할 수 있는 버튼. (Chọn 1 - Single choice).
- **텍스트 박스 (Text Box):** 데이터를 입력/수정하는 상자. (Hộp nhập văn bản).
- **콤보 상자 (Combo Box):** 목록에서 선택하거나 새로 입력할 수 있는 상자. (Dropdown list có thể gõ thêm text).
- **목록 상자 (List Box):** 목록만 표시하고 새로 입력할 수는 없는 상자. (Chỉ chọn từ list có sẵn, không được gõ).

Các bullet của **UI 주요 요소 (Các thành phần UI)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **UI 주요 요소 (Các thành phần UI)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **상위 설계와 하위 설계 (Thiết kế bậc cao và Bậc thấp)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **상위 설계와 하위 설계 (Thiết kế bậc cao và Bậc thấp)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 상위 설계와 하위 설계 (Thiết kế bậc cao và Bậc thấp)

Bây giờ ta đi vào nội dung của **상위 설계와 하위 설계 (Thiết kế bậc cao và Bậc thấp)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- **상위 설계 (High-level Design):** 아키텍처 설계, 예비 설계. 대상: 시스템 전체 구조 (DB, Interface). (Thiết kế tổng thể, kiến trúc).
- **하위 설계 (Low-level Design):** 모듈 설계, 상세 설계. 대상: 시스템 내부 구조, 컴포넌트, 알고리즘. (Thiết kế chi tiết module, thuật toán).

Các bullet của **상위 설계와 하위 설계 (Thiết kế bậc cao và Bậc thấp)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **상위 설계와 하위 설계 (Thiết kế bậc cao và Bậc thấp)**, đừng bắt đầu lại từ số không. **소프트웨어 아키텍처 품질 속성 (Thuộc tính chất lượng Kiến trúc)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **소프트웨어 아키텍처 품질 속성 (Thuộc tính chất lượng Kiến trúc)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 소프트웨어 아키텍처 품질 속성 (Thuộc tính chất lượng Kiến trúc)

Phần nguồn của **소프트웨어 아키텍처 품질 속성 (Thuộc tính chất lượng Kiến trúc)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **시스템 측면 (Hệ thống):** 성능, 보안, 가용성, 기능성. (Hiệu năng, bảo mật...).
- **비즈니스 측면 (Kinh doanh):** 시장 적시성 (Time-to-market), 비용과 혜택. (Thời điểm tung ra thị trường, chi phí).
- **아키텍처 측면 (Kiến trúc):** 개념적 무결성, 정확성, 완결성. (Tính toàn vẹn, chính xác).

Các bullet của **소프트웨어 아키텍처 품질 속성 (Thuộc tính chất lượng Kiến trúc)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**소프트웨어 아키텍처 품질 속성 (Thuộc tính chất lượng Kiến trúc)** vừa cho ta cách đặt câu hỏi. Bây giờ **협약(Contract)에 의한 설계 (Thiết kế theo hợp đồng)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Đoạn **협약(Contract)에 의한 설계 (Thiết kế theo hợp đồng)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 협약(Contract)에 의한 설계 (Thiết kế theo hợp đồng)

Các ý ngay dưới **협약(Contract)에 의한 설계 (Thiết kế theo hợp đồng)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- 컴포넌트의 정확한 인터페이스를 명세하는 방법. (Đặc tả chính xác interface của component).
- **선행 조건 (Precondition):** 오퍼레이션이 호출되기 전에 참이 되어야 할 조건. (Điều kiện bắt buộc trước khi chạy hàm).
- **결과 조건 (Postcondition):** 오퍼레이션이 수행된 후 만족되어야 할 조건. (Điều kiện phải đạt sau khi chạy hàm).
- **불변 조건 (Invariant):** 오퍼레이션이 실행되는 동안 항상 만족되어야 할 조건. (Điều kiện luôn đúng trong suốt quá trình chạy).

Các bullet của **협약(Contract)에 의한 설계 (Thiết kế theo hợp đồng)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Với **협약(Contract)에 의한 설계 (Thiết kế theo hợp đồng)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Điểm chốt của **12. UI 및 아키텍처 설계 심화 (Thiết kế UI & Kiến trúc chuyên sâu)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **5. 요구공학 (Requirements Engineering)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 5. 요구공학 (Requirements Engineering)

Ở bước 22/57, **5. 요구공학 (Requirements Engineering)** xuất hiện như phần tiếp nối của **12. UI 및 아키텍처 설계 심화 (Thiết kế UI & Kiến trúc chuyên sâu)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **5. 요구공학 (Requirements Engineering)** như một bài học cho người mới, hãy giữ câu hỏi: **một nhu cầu nghiệp vụ được chuyển thành yêu cầu có thể kiểm tra và bàn giao như thế nào?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **도출 (Elicitation)**, **분석 (Analysis)**, **명세 (Specification)**, **확인 (Validation)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **도출 (Elicitation)**: Lặp đi lặp lại trong suốt vòng đời (SDLC).
- **분석 (Analysis)**: Giải quyết xung đột (중재), dùng DFD, DD.
- **명세 (Specification)**: Viết tài liệu (Mini-Spec), đảm bảo tính truy xuất (추적성).
  - 정형 (Toán học, VDM) vs 비정형 (Ngôn ngữ tự nhiên, ERD).
- **확인 (Validation)**:
  - 확인 (Validation): Có đúng sản phẩm khách cần không? (Right product).
  - 검증 (Verification): Có làm đúng quy trình không? (Product right).
  - Cần quản lý cấu hình (형상 관리).

Như vậy, **5. 요구공학 (Requirements Engineering)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **8. UI 및 UX, HCI (UI, UX, HCI)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 8. UI 및 UX, HCI (UI, UX, HCI)

Sau khi đã đặt nền bằng **5. 요구공학 (Requirements Engineering)**, ta chuyển sang **8. UI 및 UX, HCI (UI, UX, HCI)**. Đây là mắt xích 23/57 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **8. UI 및 UX, HCI (UI, UX, HCI)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **UI 유형**, **UI 설계 도구**, **HCI (Human Computer Interaction)**, **UX (User Experience - Trải nghiệm người dùng)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **UI 유형**: CLI (Văn bản), GUI (Đồ họa), NUI (Tự nhiên - Giọng nói/Hành động), OUI (Hữu cơ - Gắn với đồ vật vật lý).
- **UI 설계 도구**: Wireframe (Khung xương), Mockup (Mô hình tĩnh giống thật), Storyboard (Kịch bản chi tiết), Prototype (Mô hình động tương tác).
- **HCI (Human Computer Interaction)**: Nghiên cứu tương tác người-máy tính để mang lại trải nghiệm tốt nhất (UX).
- **UX (User Experience - Trải nghiệm người dùng)**:
  - **주관성 (Subjectivity)**: Tính chủ quan.
  - **정황성 (Contextuality)**: Phụ thuộc vào hoàn cảnh (thời gian, địa điểm).
  - **총체성 (Holistic)**: Trải nghiệm tổng thể.
- **감성공학 (Affective Engineering)**: Khoa học kết hợp cảm xúc con người vào thiết kế (Dựa trên -> Thực hiện -> Ứng dụng).

Ta có thể khép mục **8. UI 및 UX, HCI (UI, UX, HCI)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **5. 소프트웨어 아키텍처 및 설계 (Kiến trúc và Thiết kế Phần mềm)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 5. 소프트웨어 아키텍처 및 설계 (Kiến trúc và Thiết kế Phần mềm)

Từ **8. UI 및 UX, HCI (UI, UX, HCI)**, ta đã có điểm tựa để bước vào **5. 소프트웨어 아키텍처 및 설계 (Kiến trúc và Thiết kế Phần mềm)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 24/57 trước khi đi vào chi tiết.

Để đọc **5. 소프트웨어 아키텍처 및 설계 (Kiến trúc và Thiết kế Phần mềm)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng là bằng chứng để so sánh các lựa chọn theo cùng tiêu chí, không phải danh sách cần học thuộc từng ô.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **024. ISO/IEC 9126의 품질 특성 (Đặc tính chất lượng theo ISO/IEC 9126)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 024. ISO/IEC 9126의 품질 특성 (Đặc tính chất lượng theo ISO/IEC 9126)

Các ý ngay dưới **024. ISO/IEC 9126의 품질 특성 (Đặc tính chất lượng theo ISO/IEC 9126)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- 기능성 (Functionality): 요구사항을 정확하게 만족하는 기능을 제공하는지 여부를 나타냄. (Cung cấp chức năng thỏa mãn chính xác các yêu cầu không.)
- 신뢰성 (Reliability): 요구된 기능을 오류 없이 수행할 수 있는 정도를 나타냄. (Mức độ thực hiện chức năng yêu cầu mà không có lỗi.)
- 사용성 (Usability): 사용자가 쉽게 배우고 사용할 수 있는 정도를 나타냄. (Mức độ người dùng dễ dàng học và sử dụng.)
- 이식성 (Portability): 다른 환경에서도 얼마나 쉽게 적용할 수 있는지 정도를 나타냄. (Mức độ dễ dàng áp dụng trong các môi trường khác nhau.)
- **Ví dụ (Example):** App đang chạy trên Android, mang sang iOS chạy vẫn tốt mà không cần sửa nhiều -> Tính 이식성 (Portability) cao.

Các ý về **024. ISO/IEC 9126의 품질 특성 (Đặc tính chất lượng theo ISO/IEC 9126)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **024. ISO/IEC 9126의 품질 특성 (Đặc tính chất lượng theo ISO/IEC 9126)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **025. 소프트웨어 아키텍처의 설계 과정 (Quá trình thiết kế Kiến trúc phần mềm)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **025. 소프트웨어 아키텍처의 설계 과정 (Quá trình thiết kế Kiến trúc phần mềm)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 025. 소프트웨어 아키텍처의 설계 과정 (Quá trình thiết kế Kiến trúc phần mềm)

Bây giờ ta đi vào nội dung của **025. 소프트웨어 아키텍처의 설계 과정 (Quá trình thiết kế Kiến trúc phần mềm)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 설계 목표 설정 (Thiết lập mục tiêu thiết kế) → 시스템 타입 결정 (Quyết định loại hệ thống) → 아키텍처 패턴 적용 (Áp dụng pattern kiến trúc) → 서브시스템 구체화 (Cụ thể hóa hệ thống con) → 검토 (Xem xét/Đánh giá).

Các bullet của **025. 소프트웨어 아키텍처의 설계 과정 (Quá trình thiết kế Kiến trúc phần mềm)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **025. 소프트웨어 아키텍처의 설계 과정 (Quá trình thiết kế Kiến trúc phần mềm)**, đừng bắt đầu lại từ số không. **026. 모듈화 (Modularization / Mô-đun hóa)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **026. 모듈화 (Modularization / Mô-đun hóa)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 026. 모듈화 (Modularization / Mô-đun hóa)

Phần nguồn của **026. 모듈화 (Modularization / Mô-đun hóa)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- 기능의 분리가 가능하여 인터페이스가 단순해진다. (Có thể phân tách các chức năng nên giao diện trở nên đơn giản.)
- 프로그램의 효율적인 관리가 가능하다. (Có thể quản lý chương trình một cách hiệu quả.)
- 오류의 파급 효과를 최소화할 수 있다. (Có thể giảm thiểu tác động lan truyền của lỗi.)
- 모듈의 크기를 너무 작게 나누면 개수가 많아져 모듈간의 통합 비용이 많이 들고, 너무 크게 나누면 개수가 적어 통합 비용은 적게 들지만 모듈 하나의 개발 비용이 많이 든다. (Nếu chia module quá nhỏ, số lượng nhiều, chi phí tích hợp sẽ cao. Nếu chia quá lớn, chi phí tích hợp ít nhưng chi phí phát triển 1 module lại cao.)
- **Ví dụ (Example):** Thay vì viết toàn bộ chức năng vào 1 file code, ta chia ra `login.py`, `payment.py`. Lỗi ở payment không làm sập login (giảm thiểu 파급 효과).

Các ý về **026. 모듈화 (Modularization / Mô-đun hóa)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

**026. 모듈화 (Modularization / Mô-đun hóa)** vừa cho ta cách đặt câu hỏi. Bây giờ **027. 추상화의 유형 (Các loại trừu tượng hóa)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Đoạn **027. 추상화의 유형 (Các loại trừu tượng hóa)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 027. 추상화의 유형 (Các loại trừu tượng hóa)

Các ý ngay dưới **027. 추상화의 유형 (Các loại trừu tượng hóa)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- 과정 추상화 (Trừu tượng hóa quá trình)
- 데이터(자료) 추상화 (Trừu tượng hóa dữ liệu)
- 제어 추상화 (Trừu tượng hóa điều khiển)

Các bullet của **027. 추상화의 유형 (Các loại trừu tượng hóa)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **027. 추상화의 유형 (Các loại trừu tượng hóa)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **028. 정보 은닉 (Information Hiding / Che giấu thông tin)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **028. 정보 은닉 (Information Hiding / Che giấu thông tin)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 028. 정보 은닉 (Information Hiding / Che giấu thông tin)

Bây giờ ta đi vào nội dung của **028. 정보 은닉 (Information Hiding / Che giấu thông tin)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 한 모듈 내부에 포함된 절차와 자료들의 정보가 감추어져 다른 모듈이 접근하거나 변경하지 못하도록 하는 기법이다. (Kỹ thuật che giấu thông tin về thủ tục và dữ liệu bên trong một module để các module khác không thể truy cập hoặc sửa đổi.)
- 모듈을 독립적으로 수행할 수 있다. (Có thể thực thi module một cách độc lập.)
- 수정, 시험, 유지보수가 용이하다. (Dễ dàng sửa đổi, kiểm thử, bảo trì.)
- 정보 은닉을 표기할 때 private의 의미는 은닉이다. (Khi ký hiệu che giấu thông tin, 'private' mang ý nghĩa là che giấu.)
- **Ví dụ (Example):** Trong OOP, khai báo các biến là `private` và chỉ cho phép truy cập qua `getter/setter`.

Các ý về **028. 정보 은닉 (Information Hiding / Che giấu thông tin)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Sau khi đọc **028. 정보 은닉 (Information Hiding / Che giấu thông tin)**, đừng bắt đầu lại từ số không. **029. 파이프 - 필터 패턴 (Pipe-Filter Pattern)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **029. 파이프 - 필터 패턴 (Pipe-Filter Pattern)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 029. 파이프 - 필터 패턴 (Pipe-Filter Pattern)

Phần nguồn của **029. 파이프 - 필터 패턴 (Pipe-Filter Pattern)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- 시스템의 처리 결과물을 파이프를 통해 전달받아 처리한 후 그 결과물을 다시 파이프를 통해 다음 시스템으로 넘겨주는 패턴이다. (Pattern nhận kết quả xử lý qua Pipe, xử lý (Filter) rồi lại chuyển kết quả đó qua Pipe cho hệ thống tiếp theo.)
- 데이터 변환으로 인한 오버헤드가 발생한다. (Phát sinh overhead do chuyển đổi dữ liệu.)
- **Ví dụ (Example):** Câu lệnh trong Linux: `ls | grep "txt" | sort`. Ký tự `|` chính là Pipe, còn `grep`, `sort` là các Filter.

Các ý về **029. 파이프 - 필터 패턴 (Pipe-Filter Pattern)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

**029. 파이프 - 필터 패턴 (Pipe-Filter Pattern)** vừa cho ta cách đặt câu hỏi. Bây giờ **030. MVC (Model-View-Controller) 패턴** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Đoạn **030. MVC (Model-View-Controller) 패턴** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 030. MVC (Model-View-Controller) 패턴

Các ý ngay dưới **030. MVC (Model-View-Controller) 패턴** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- 모델 (Model): 서브시스템의 핵심 기능과 데이터를 보관함. (Lưu trữ chức năng cốt lõi và dữ liệu - Logic nghiệp vụ.)
- 뷰 (View): 사용자에게 정보를 표시함. (Hiển thị thông tin cho người dùng - UI.)
- 컨트롤러 (Controller): 사용자로부터 입력된 변경 요청을 처리하기 위해 모델에게 명령을 보냄. (Xử lý yêu cầu thay đổi từ người dùng và gửi lệnh cho Model.)

Các bullet của **030. MVC (Model-View-Controller) 패턴** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **030. MVC (Model-View-Controller) 패턴** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **039. 모듈 (Module)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **039. 모듈 (Module)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 039. 모듈 (Module)

Bây giờ ta đi vào nội dung của **039. 모듈 (Module)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 모듈화를 통해 분리된 시스템의 각 기능들이다. (Là các chức năng của hệ thống được tách ra thông qua quá trình module hóa.)
- 단독으로 컴파일이 가능하다. (Có thể biên dịch độc lập.)
- 재사용 할 수 있다. (Có thể tái sử dụng.)
- 다른 모듈에서의 접근이 가능하다. (Các module khác có thể truy cập được.)

Các bullet của **039. 모듈 (Module)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **039. 모듈 (Module)**, đừng bắt đầu lại từ số không. **040 & 041. 결합도 (Coupling) 의 종류와 정도 (Các loại Độ kết dính / Mức độ từ Yếu → Mạnh)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **040 & 041. 결합도 (Coupling) 의 종류와 정도 (Các loại Độ kết dính / Mức độ từ Yếu → Mạnh)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 040 & 041. 결합도 (Coupling) 의 종류와 정도 (Các loại Độ kết dính / Mức độ từ Yếu → Mạnh)

Phần nguồn của **040 & 041. 결합도 (Coupling) 의 종류와 정도 (Các loại Độ kết dính / Mức độ từ Yếu → Mạnh)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- *Kết dính càng YẾU (약함) càng TỐT, càng MẠNH (강함) càng XẤU.*
- **자료 (Data) 결합도 (Yếu nhất - Tốt nhất):** 모듈 간의 인터페이스가 자료 요소로만 구성될 때. (Chỉ truyền dữ liệu đơn giản giữa các module).
- **스탬프 (Stamp) 결합도:** 배열이나 레코드 등의 자료 구조가 전달될 때. (Truyền cấu trúc dữ liệu như mảng, bản ghi).
- **제어 (Control) 결합도:** 제어 신호를 이용하여 통신하거나 제어 요소를 전달. (Truyền cờ điều khiển - control flag/signal).
- **외부 (External) 결합도:** 데이터(변수)를 외부의 다른 모듈에서 참조할 때. (Tham chiếu biến toàn cục bên ngoài).
- **공통 (Common) 결합도:** 공유되는 공통 데이터 영역을 여러 모듈이 사용할 때. (Nhiều module cùng dùng chung một vùng dữ liệu chung - global data).
- **내용 (Content) 결합도 (Mạnh nhất - Xấu nhất):** 한 모듈이 다른 모듈의 내부 기능 및 그 내부 자료를 직접 참조하거나 수정. (Module này trực tiếp can thiệp nội bộ module kia).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **TSCNCN** (Tư - Stamp - Chế - Ngoại - Công - Nội): **Tính Sao Cho Nhẹ Cả Người**. (Từ Tốt nhất -> Xấu nhất).

Các bullet của **040 & 041. 결합도 (Coupling) 의 종류와 정도 (Các loại Độ kết dính / Mức độ từ Yếu → Mạnh)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**040 & 041. 결합도 (Coupling) 의 종류와 정도 (Các loại Độ kết dính / Mức độ từ Yếu → Mạnh)** vừa cho ta cách đặt câu hỏi. Bây giờ **043. 주요 응집도 (Cohesion)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Đoạn **043. 주요 응집도 (Cohesion)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 043. 주요 응집도 (Cohesion)

Các ý ngay dưới **043. 주요 응집도 (Cohesion)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- *Độ gắn kết nội bộ. Gắn kết càng MẠNH càng TỐT.*
- **기능적 (Functional) 응집도 (Mạnh nhất - Tốt nhất):** Tất cả các yếu tố bên trong đều hướng tới giải quyết một chức năng duy nhất.
- **순차적 (Sequential) 응집도:** Kết quả đầu ra của hoạt động này là đầu vào của hoạt động kia.
- **통신적 (Communication) 응집도:** Các hoạt động cùng sử dụng chung một dữ liệu đầu vào/ra.
- **절차적 (Procedural) 응집도:** 모듈 안의 구성 요소들이 그 기능을 순차적으로 수행할 경우. (Thực hiện tuần tự theo quy trình nhưng có thể không cùng dữ liệu).
- **시간적 (Temporal) 응집도:** 특정 시간에 처리되는 몇 개의 기능을 모아 하나의 모듈로 작성. (Nhóm các chức năng cần thực hiện cùng một thời điểm, ví dụ: Module khởi tạo hệ thống).
- **논리적 (Logical) 응집도:** Các chức năng có cùng logic được nhóm lại.
- **우연적 (Coincidental) 응집도 (Yếu nhất - Xấu nhất):** 각 구성 요소들이 서로 관련 없는 요소로만 구성된 경우. (Nhóm các thành phần chẳng liên quan gì với nhau).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **KTTTTLN** (Kỳ - Thuận - Thông - Tiết - Thời - Luận - Ngẫu): **Không Thể Tin Thằng Trẻ Làm Ngốc**. (Từ Tốt nhất -> Xấu nhất).

Các ý về **043. 주요 응집도 (Cohesion)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **043. 주요 응집도 (Cohesion)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **044. 팬인(Fan-In) / 팬아웃(Fan-Out)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **044. 팬인(Fan-In) / 팬아웃(Fan-Out)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 044. 팬인(Fan-In) / 팬아웃(Fan-Out)

Bây giờ ta đi vào nội dung của **044. 팬인(Fan-In) / 팬아웃(Fan-Out)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 팬인 (Fan-In): 어떤 모듈을 제어(호출)하는 모듈의 수. (Số lượng các module gọi/điều khiển module đó -> Mũi tên TRỎ VÀO nó).
- 팬아웃 (Fan-Out): 어떤 모듈에 의해 제어(호출)되는 모듈의 수. (Số lượng các module mà module đó gọi/điều khiển -> Mũi tên TRỎ RA từ nó).
- **Nguyên tắc thiết kế tốt:** Fan-In phải CAO (được dùng lại nhiều), Fan-Out phải THẤP (ít phụ thuộc vào nhiều thằng khác).

Các bullet của **044. 팬인(Fan-In) / 팬아웃(Fan-Out)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **044. 팬인(Fan-In) / 팬아웃(Fan-Out)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **5. 소프트웨어 아키텍처 및 설계 (Kiến trúc và Thiết kế Phần mềm)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **13. 소프트웨어 품질 및 아키텍처 패턴 (Chất lượng SW & Mẫu Kiến trúc)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 13. 소프트웨어 품질 및 아키텍처 패턴 (Chất lượng SW & Mẫu Kiến trúc)

Ở bước 25/57, **13. 소프트웨어 품질 및 아키텍처 패턴 (Chất lượng SW & Mẫu Kiến trúc)** xuất hiện như phần tiếp nối của **5. 소프트웨어 아키텍처 및 설계 (Kiến trúc và Thiết kế Phần mềm)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **13. 소프트웨어 품질 및 아키텍처 패턴 (Chất lượng SW & Mẫu Kiến trúc)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **ISO/IEC 9126 하위 품질 특성 (Đặc tính con của ISO/IEC 9126)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **ISO/IEC 9126 하위 품질 특성 (Đặc tính con của ISO/IEC 9126)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### ISO/IEC 9126 하위 품질 특성 (Đặc tính con của ISO/IEC 9126)

Bây giờ ta đi vào nội dung của **ISO/IEC 9126 하위 품질 특성 (Đặc tính con của ISO/IEC 9126)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- *Đây là phần rất hay thi, cần ghi nhớ chi tiết.*
- **기능성 (Functionality):** 적절성 (Suitability), 정밀성 (Accuracy), 상호 운용성 (Interoperability), 보안성 (Security), 준수성 (Compliance).
- **신뢰성 (Reliability):** 성숙성 (Maturity), 고장 허용성 (Fault Tolerance), 회복성 (Recoverability).
- **사용성 (Usability):** 이해성 (Understandability), 학습성 (Learnability), 운용성 (Operability), 친밀성 (Attractiveness).
- **효율성 (Efficiency):** 시간 효율성 (Time Behaviour), 자원 효율성 (Resource Behaviour).
- **유지 보수성 (Maintainability):** 분석성 (Analyzability), 변경성 (Changeability), 안정성 (Stability), 시험성 (Testability).
- **이식성 (Portability):** 적용성 (Adaptability), 설치성 (Installability), 대체성 (Replaceability), 공존성 (Co-existence).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **KTSHDD** (Kỳ - Tín - Sử - Hiệu - Duy - Di): **Không Tin Sẽ Hư Dần Dần** (Tên 6 đặc tính chính).
  - 유지 보수성: **분변안시** (Phân - Biến - An - Thử).

Các bullet của **ISO/IEC 9126 하위 품질 특성 (Đặc tính con của ISO/IEC 9126)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **ISO/IEC 9126 하위 품질 특성 (Đặc tính con của ISO/IEC 9126)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **관련 품질 표준 (Các tiêu chuẩn ISO khác)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **관련 품질 표준 (Các tiêu chuẩn ISO khác)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 관련 품질 표준 (Các tiêu chuẩn ISO khác)

Phần nguồn của **관련 품질 표준 (Các tiêu chuẩn ISO khác)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **ISO/IEC 25010:** 2011년 9126을 개정한 최신 표준. (Bản cập nhật của 9126).
- **ISO/IEC 12119:** 테스트 절차를 포함한 품질 표준. (Bao gồm quy trình test).
- **ISO/IEC 14598:** 평가자별 제품 평가 활동 규정. (Quy định hoạt động đánh giá).

Các bullet của **관련 품질 표준 (Các tiêu chuẩn ISO khác)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **관련 품질 표준 (Các tiêu chuẩn ISO khác)**, đừng bắt đầu lại từ số không. **기타 아키텍처 패턴 (Các mẫu kiến trúc bổ sung)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **기타 아키텍처 패턴 (Các mẫu kiến trúc bổ sung)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 기타 아키텍처 패턴 (Các mẫu kiến trúc bổ sung)

Các ý ngay dưới **기타 아키텍처 패턴 (Các mẫu kiến trúc bổ sung)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- **마스터-슬레이브 패턴 (Master-Slave):** 마스터가 작업을 분할하고 슬레이브가 처리 결과를 돌려주는 패턴 (장애 허용 시스템, 병렬 컴퓨팅). (Master chia việc, Slave làm rồi trả kết quả -> Hệ thống tính toán song song).
- **브로커 패턴 (Broker):** 사용자가 요청하면 브로커가 적합한 컴포넌트를 연결해 줌 (분산 환경). (Môi giới kết nối User với Component phù hợp -> Hệ thống phân tán).
- **피어-투-피어 패턴 (Peer-To-Peer / P2P):** 각 피어가 클라이언트도 되고 서버도 됨. (Mỗi node vừa là Client vừa là Server).
- **이벤트-버스 패턴 (Event-Bus):** 소스가 이벤트를 발행(Publish)하면 리스너가 구독(Subscribe)하여 처리. (Mô hình Pub/Sub).
- **블랙보드 패턴 (Blackboard):** 모든 컴포넌트가 공유 데이터 저장소(블랙보드)에 접근 (음성 인식, 신호 해석). (Bảng đen dùng chung, các AI agents tự do truy cập -> Nhận diện giọng nói, xử lý tín hiệu).

Các bullet của **기타 아키텍처 패턴 (Các mẫu kiến trúc bổ sung)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **기타 아키텍처 패턴 (Các mẫu kiến trúc bổ sung)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Như vậy, **13. 소프트웨어 품질 및 아키텍처 패턴 (Chất lượng SW & Mẫu Kiến trúc)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **1. 소프트웨어 아키텍처 (Software Architecture)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 1. 소프트웨어 아키텍처 (Software Architecture)

Sau khi đã đặt nền bằng **13. 소프트웨어 품질 및 아키텍처 패턴 (Chất lượng SW & Mẫu Kiến trúc)**, ta chuyển sang **1. 소프트웨어 아키텍처 (Software Architecture)**. Đây là mắt xích 26/57 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **1. 소프트웨어 아키텍처 (Software Architecture)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **상위 설계 (High-level)**, **하위 설계 (Low-level)**, **아키텍처 패턴 (Architecture Patterns)**, **레이어 패턴 (Layers)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **상위 설계 (High-level)**: 아키텍처 (Architecture), 자료구조 (Data Structure), 인터페이스 (Interface).
- **하위 설계 (Low-level)**: 모듈 (Module), 프로시저 (Procedure).
- **아키텍처 패턴 (Architecture Patterns)**:
  - **레이어 패턴 (Layers)**: Chia thành các tầng (OSI 7 layer).
  - **클라이언트-서버 패턴 (Client-Server)**: Máy khách - Máy chủ.
  - **파이프-필터 패턴 (Pipe-Filter)**: Dữ liệu qua các bộ lọc liên tiếp (Ví dụ: Unix shell).
  - **MVC 패턴**: Model (Dữ liệu), View (Giao diện), Controller (Điều khiển).
  - **브로커 패턴 (Broker)**: Có môi giới ở giữa.
  - **마스터-슬레이브 (Master-Slave)**: Một chủ, nhiều tớ (Hệ thống thời gian thực).

Ta có thể khép mục **1. 소프트웨어 아키텍처 (Software Architecture)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **6. 객체지향 (Hướng Đối Tượng - OOP)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 6. 객체지향 (Hướng Đối Tượng - OOP)

Từ **1. 소프트웨어 아키텍처 (Software Architecture)**, ta đã có điểm tựa để bước vào **6. 객체지향 (Hướng Đối Tượng - OOP)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 27/57 trước khi đi vào chi tiết.

Để đọc **6. 객체지향 (Hướng Đối Tượng - OOP)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **031. 메시지 (Message)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 031. 메시지 (Message)

Các ý ngay dưới **031. 메시지 (Message)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- 객체에게 어떤 행위를 하도록 지시하는 명령 또는 요구사항이다. (Là lệnh hoặc yêu cầu chỉ thị cho đối tượng thực hiện một hành vi nào đó.)
- 객체들 간에 상호 작용을 하는 데 사용되는 수단이다. (Là phương tiện dùng để tương tác giữa các đối tượng.)

Các bullet của **031. 메시지 (Message)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **031. 메시지 (Message)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **032. 클래스 (Class)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **032. 클래스 (Class)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 032. 클래스 (Class)

Bây giờ ta đi vào nội dung của **032. 클래스 (Class)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 공통된 속성과 연산(행위)을 갖는 객체의 집합이다. (Là tập hợp các đối tượng có chung thuộc tính và phép toán (hành vi).)
- 클래스에 속한 각각의 객체를 인스턴스(Instance)라 한다. (Mỗi đối tượng thuộc một class được gọi là Thực thể - Instance).
- 객체지향 프로그램에서 데이터를 추상화하는 단위이다. (Là đơn vị trừu tượng hóa dữ liệu trong lập trình OOP.)

Các bullet của **032. 클래스 (Class)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **032. 클래스 (Class)**, đừng bắt đầu lại từ số không. **033. 캡슐화 (Encapsulation / Đóng gói)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **033. 캡슐화 (Encapsulation / Đóng gói)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 033. 캡슐화 (Encapsulation / Đóng gói)

Phần nguồn của **033. 캡슐화 (Encapsulation / Đóng gói)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- 데이터와 데이터를 처리하는 함수를 하나로 묶는 것을 의미한다. (Việc bó buộc dữ liệu và hàm xử lý dữ liệu đó thành một khối.)
- 외부 모듈의 변경으로 인한 파급 효과가 적다. (Giảm thiểu hiệu ứng lan truyền khi module bên ngoài thay đổi.)
- 인터페이스가 단순화된다. (Giao diện trở nên đơn giản.)
- 재사용이 용이하다. (Dễ dàng tái sử dụng.)
- **Ví dụ (Example):** Một viên thuốc nhộng (capsule) chứa nhiều bột thuốc bên trong, người dùng chỉ việc uống viên nhộng mà không cần biết tỷ lệ bột bên trong.

Các ý về **033. 캡슐화 (Encapsulation / Đóng gói)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

**033. 캡슐화 (Encapsulation / Đóng gói)** vừa cho ta cách đặt câu hỏi. Bây giờ **034. 상속 (Inheritance / Kế thừa)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Đoạn **034. 상속 (Inheritance / Kế thừa)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 034. 상속 (Inheritance / Kế thừa)

Các ý ngay dưới **034. 상속 (Inheritance / Kế thừa)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- 상위 클래스(부모 클래스)의 모든 속성과 연산을 하위 클래스(자식 클래스)가 물려받는 것이다. (Lớp con kế thừa toàn bộ thuộc tính và phương thức của lớp cha.)

Các bullet của **034. 상속 (Inheritance / Kế thừa)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **034. 상속 (Inheritance / Kế thừa)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **035. 다형성 (Polymorphism / Đa hình)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **035. 다형성 (Polymorphism / Đa hình)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 035. 다형성 (Polymorphism / Đa hình)

Bây giờ ta đi vào nội dung của **035. 다형성 (Polymorphism / Đa hình)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 오버로딩 (Overloading - Nạp chồng): 메소드의 이름은 같지만 인수를 받는 자료형과 개수를 달리하여 여러 기능을 정의할 수 있음. (Cùng tên hàm nhưng khác kiểu/số lượng tham số -> Định nghĩa nhiều chức năng).
- 오버라이딩 (Overriding - Ghi đè): 메소드의 이름은 같지만 메소드 안의 실행 코드를 달리하여 자식 클래스에서 재정의해서 사용할 수 있음. (Cùng tên hàm, định nghĩa lại nội dung code ở lớp con).
- **Ví dụ (Example):** Hàm `add(int a, int b)` và `add(float a, float b)` là Overloading. Lớp Mèo `speak()` kêu Meo, lớp Chó `speak()` kêu Gâu là Overriding.

Các ý về **035. 다형성 (Polymorphism / Đa hình)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Sau khi đọc **035. 다형성 (Polymorphism / Đa hình)**, đừng bắt đầu lại từ số không. **036. 객체지향 분석 방법론 - Coad와 Yourdon 방법** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **036. 객체지향 분석 방법론 - Coad와 Yourdon 방법**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 036. 객체지향 분석 방법론 - Coad와 Yourdon 방법

Phần nguồn của **036. 객체지향 분석 방법론 - Coad와 Yourdon 방법** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- E-R 다이어그램을 사용하여 객체의 행위를 모델링 한다. (Sử dụng biểu đồ E-R để mô hình hóa hành vi đối tượng.)
- 객체 식별, 구조 식별, 주제 정의, 속성과 인스턴스 연결 정의, 연산과 메시지 연결 정의 등의 과정으로 구성하는 기법이다. (Quy trình gồm: Nhận diện đối tượng, Nhận diện cấu trúc, Định nghĩa chủ đề, Định nghĩa thuộc tính/liên kết instance, Định nghĩa phép toán/thông điệp).

Các bullet của **036. 객체지향 분석 방법론 - Coad와 Yourdon 방법** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**036. 객체지향 분석 방법론 - Coad와 Yourdon 방법** vừa cho ta cách đặt câu hỏi. Bây giờ **037. 럼바우(Rumbaugh)의 분석 기법 (Kỹ thuật phân tích của Rumbaugh)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Đoạn **037. 럼바우(Rumbaugh)의 분석 기법 (Kỹ thuật phân tích của Rumbaugh)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 037. 럼바우(Rumbaugh)의 분석 기법 (Kỹ thuật phân tích của Rumbaugh)

Các ý ngay dưới **037. 럼바우(Rumbaugh)의 분석 기법 (Kỹ thuật phân tích của Rumbaugh)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- 객체(Object) 모델링: 정보 모델링이라고도 하며, 객체들 간의 관계를 규정하여 객체 다이어그램으로 표시하는 것. (Mô hình hóa đối tượng/thông tin: Xác định mối quan hệ giữa các đối tượng và hiển thị bằng Object Diagram).
- 동적(Dynamic) 모델링: 상태 다이어그램을 이용하여 객체들 간의 동적인 행위를 표현하는 모델링. (Mô hình hóa động: Thể hiện hành vi động giữa các đối tượng bằng State Diagram).
- 기능(Functional) 모델링: 자료 흐름도를 이용하여 자료 흐름을 표현한 모델링. (Mô hình hóa chức năng: Thể hiện luồng dữ liệu bằng DFD - Data Flow Diagram).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **KĐC** (Khách - Động - Cơ): **Không Đợi Chờ** (Khách thể - Động lực - Cơ năng). (O-D-F)

Các bullet của **037. 럼바우(Rumbaugh)의 분석 기법 (Kỹ thuật phân tích của Rumbaugh)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **037. 럼바우(Rumbaugh)의 분석 기법 (Kỹ thuật phân tích của Rumbaugh)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **038. 객체지향 설계 원칙 (SOLID 원칙) (Các nguyên tắc thiết kế OOP)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **038. 객체지향 설계 원칙 (SOLID 원칙) (Các nguyên tắc thiết kế OOP)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 038. 객체지향 설계 원칙 (SOLID 원칙) (Các nguyên tắc thiết kế OOP)

Bây giờ ta đi vào nội dung của **038. 객체지향 설계 원칙 (SOLID 원칙) (Các nguyên tắc thiết kế OOP)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 단일 책임 원칙 (SRP - Single Responsibility Principle): 객체는 단 하나의 책임만 가져야 한다는 원칙. (Mỗi đối tượng chỉ có MỘT trách nhiệm duy nhất.)
- 개방-폐쇄 원칙 (OCP - Open-Closed Principle): 기존의 코드를 변경하지 않고 기능을 추가할 수 있도록 설계해야 한다는 원칙. (Mở cho việc mở rộng, Đóng cho việc sửa đổi.)
- 리스코프 치환 원칙 (LSP - Liskov Substitution Principle): 자식 클래스는 최소한 자신의 부모 클래스에서 가능한 행위는 수행할 수 있어야 한다는 설계 원칙. (Lớp con có thể thay thế hoàn toàn lớp cha mà không làm hỏng logic.)
- 인터페이스 분리 원칙 (ISP - Interface Segregation Principle): 자신이 사용하지 않는 인터페이스와 의존 관계를 맺거나 영향을 받지 않아야 한다는 원칙. (Nên tách nhỏ Interface, không ép client implement những phương thức không dùng tới.)
- 의존 역전 원칙 (DIP - Dependency Inversion Principle): 추상성이 낮은 클래스보다 추상성이 높은 클래스와 의존 관계를 맺어야 한다는 원칙. (Module cấp cao không nên phụ thuộc module cấp thấp, cả 2 nên phụ thuộc vào abstraction/interface.)
- 💡 **Mẹo ghi nhớ (Mnemonic):** Tên các chữ cái đầu tiếng Anh tạo thành chữ **S-O-L-I-D**.

Các bullet của **038. 객체지향 설계 원칙 (SOLID 원칙) (Các nguyên tắc thiết kế OOP)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **038. 객체지향 설계 원칙 (SOLID 원칙) (Các nguyên tắc thiết kế OOP)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **6. 객체지향 (Hướng Đối Tượng - OOP)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **14. 객체지향 심화 (OOP chuyên sâu)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 14. 객체지향 심화 (OOP chuyên sâu)

Ở bước 28/57, **14. 객체지향 심화 (OOP chuyên sâu)** xuất hiện như phần tiếp nối của **6. 객체지향 (Hướng Đối Tượng - OOP)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **14. 객체지향 심화 (OOP chuyên sâu)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **다형성 (Polymorphism) 추가 설명** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **다형성 (Polymorphism) 추가 설명** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 다형성 (Polymorphism) 추가 설명

Bây giờ ta đi vào nội dung của **다형성 (Polymorphism) 추가 설명**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- **오버로딩 (Overloading):** 인수를 받는 자료형과 개수를 달리하여 여러 기능을 정의. (Cùng tên hàm, khác tham số).
- **오버라이딩 (Overriding / 메소드 재정의):** 상위 클래스의 메소드 안의 코드를 자식 클래스에서 재정의. (Lớp con định nghĩa lại hàm của lớp cha).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **Over-load** = Chở thêm đồ (Thêm tham số). **Over-ride** = Lái đè lên vết xe cũ (Ghi đè nội dung hàm).

Với **다형성 (Polymorphism) 추가 설명**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Với **다형성 (Polymorphism) 추가 설명**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Như vậy, **14. 객체지향 심화 (OOP chuyên sâu)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **15. 객체지향 및 모듈화 방법론 (Phương pháp luận OOP & Mô-đun hóa)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 15. 객체지향 및 모듈화 방법론 (Phương pháp luận OOP & Mô-đun hóa)

Sau khi đã đặt nền bằng **14. 객체지향 심화 (OOP chuyên sâu)**, ta chuyển sang **15. 객체지향 및 모듈화 방법론 (Phương pháp luận OOP & Mô-đun hóa)**. Đây là mắt xích 29/57 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **15. 객체지향 및 모듈화 방법론 (Phương pháp luận OOP & Mô-đun hóa)** như một bài học cho người mới, hãy giữ câu hỏi: **một dự án đi qua những giai đoạn nào, mỗi mô hình phân bổ công việc và rủi ro ra sao?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **객체지향 분석 방법론 종류 (Các phương pháp phân tích OOP)**. Hãy xác định **객체지향 분석 방법론 종류 (Các phương pháp phân tích OOP)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 객체지향 분석 방법론 종류 (Các phương pháp phân tích OOP)

Phần nguồn của **객체지향 분석 방법론 종류 (Các phương pháp phân tích OOP)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **Rumbaugh (럼바우):** 객체(Object), 동적(Dynamic), 기능(Functional) 모델로 나누어 분석. (Chia làm 3 mô hình).
- **Booch (부치):** 미시적(Micro) 개발과 거시적(Macro) 개발 프로세스 모두 사용. (Dùng cả quy trình vĩ mô và vi mô).
- **Jacobson (제이콥슨):** Use Case(유스케이스)를 강조. (Nhấn mạnh vào Use Case).
- **Coad와 Yourdon:** E-R 다이어그램 사용. (Dùng sơ đồ ER).
- **Wirfs-Brock:** 분석과 설계 간 구분이 없고 연속적으로 수행. (Không phân biệt rõ phân tích và thiết kế, làm liên tục).
- 💡 **Mẹo ghi nhớ (Mnemonic):** R-O, B-M, J-U, C-E, W-L -> **Ra Ôm Bạn Mới, Giữ Út, Cho Em Vui Lây** (Rumbaugh-Object, Booch-Micro, Jacobson-Use case, Coad-ER, Wirfs-Liên tục).

Các bullet của **객체지향 분석 방법론 종류 (Các phương pháp phân tích OOP)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **객체지향 분석 방법론 종류 (Các phương pháp phân tích OOP)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **공통 모듈 명세 기법 (Kỹ thuật đặc tả Module chung)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **공통 모듈 명세 기법 (Kỹ thuật đặc tả Module chung)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 공통 모듈 명세 기법 (Kỹ thuật đặc tả Module chung)

Các ý ngay dưới **공통 모듈 명세 기법 (Kỹ thuật đặc tả Module chung)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- **정확성 (Correctness):** 기능이 필요하다는 것을 알 수 있도록 정확히 작성. (Chính xác, biết rõ cần thiết).
- **명확성 (Clarity):** 중의적으로 해석되지 않도록 명확하게. (Rõ ràng, không hiểu 2 nghĩa).
- **완전성 (Completeness):** 구현에 필요한 모든 것을 기술. (Đầy đủ mọi thứ cần thiết).
- **일관성 (Consistency):** 기능들 간 상호 충돌이 발생하지 않도록. (Nhất quán, không xung đột).
- **추적성 (Traceability):** 요구사항 출처, 관련 시스템 등 관계 파악. (Có thể truy xuất nguồn gốc).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **CMHNT** (Chính - Minh - Hoàn - Nhất - Truy): **Chỉ Mong Học Nhất Trường**.

Các bullet của **공통 모듈 명세 기법 (Kỹ thuật đặc tả Module chung)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **공통 모듈 명세 기법 (Kỹ thuật đặc tả Module chung)**, đừng bắt đầu lại từ số không. **코드(Code)의 주요 기능 (Chức năng chính của Code)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **코드(Code)의 주요 기능 (Chức năng chính của Code)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 코드(Code)의 주요 기능 (Chức năng chính của Code)

Bây giờ ta đi vào nội dung của **코드(Code)의 주요 기능 (Chức năng chính của Code)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 식별 기능 (Nhận diện), 분류 기능 (Phân loại), 배열 기능 (Sắp xếp), 표준화 기능 (Chuẩn hóa), 간소화 기능 (Đơn giản hóa).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **TPBTG** (Thức - Phân - Bài - Tiêu - Giản): **Thích Phá Bài Thì Giảm**.

Các bullet của **코드(Code)의 주요 기능 (Chức năng chính của Code)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**코드(Code)의 주요 기능 (Chức năng chính của Code)** vừa cho ta cách đặt câu hỏi. Bây giờ **코드의 종류 심화 (Các loại Code chi tiết)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Với **코드의 종류 심화 (Các loại Code chi tiết)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 코드의 종류 심화 (Các loại Code chi tiết)

Phần nguồn của **코드의 종류 심화 (Các loại Code chi tiết)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **순차 코드 (Sequence Code):** 1, 2, 3... (Theo thứ tự).
- **블록 코드 (Block Code):** 공통성 있는 것끼리 블록으로 구분 (1000~1100: Phòng Nhân sự, 1101~1200: Phòng IT).
- **10진 코드 (Decimal Code):** 0~9 분할 반복 (Ví dụ: Mã phân loại sách thư viện Dewey).
- **그룹 분류 코드 (Group Classification):** 대/중/소 분류 (1-01-001).
- **연상 코드 (Mnemonic Code):** 명칭/약호와 관계있는 문자/숫자 (TV-40). (Gợi nhớ).
- **표의 숫자 코드 (Significant Digit):** 물리적 수치 적용 (120-720).
- **합성 코드 (Combined Code):** 2개 이상 코드 조합 (KE-711).

Các ý về **코드의 종류 심화 (Các loại Code chi tiết)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Với **코드의 종류 심화 (Các loại Code chi tiết)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Ta có thể khép mục **15. 객체지향 및 모듈화 방법론 (Phương pháp luận OOP & Mô-đun hóa)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **2. 객체지향 (OOP - Object Oriented Programming)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 2. 객체지향 (OOP - Object Oriented Programming)

Từ **15. 객체지향 및 모듈화 방법론 (Phương pháp luận OOP & Mô-đun hóa)**, ta đã có điểm tựa để bước vào **2. 객체지향 (OOP - Object Oriented Programming)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 30/57 trước khi đi vào chi tiết.

Để đọc **2. 객체지향 (OOP - Object Oriented Programming)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **구성요소**, **객체지향 기법 (OOP Techniques)**, **캡슐화 (Encapsulation)**, **정보 은닉 (Information Hiding)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **구성요소**: 클래스 (Class), 객체 (Object), 메서드 (Method), 메시지 (Message), 인스턴스 (Instance), 속성 (Property).
- **객체지향 기법 (OOP Techniques)**:
  - **캡슐화 (Encapsulation)**: Đóng gói dữ liệu và phương thức, giảm kết dính (Coupling).
  - **정보 은닉 (Information Hiding)**: Giấu thông tin chi tiết.
  - **다형성 (Polymorphism)**: Đa hình (Overloading - Cùng tên khác tham số, Overriding - Ghi đè phương thức cha).
- **객체지향 설계 원칙 (SOLID)**:
  - **S (SRP)**: Đơn trách nhiệm (Một lớp một việc).
  - **O (OCP)**: Đóng-Mở (Mở rộng thì dễ, sửa đổi thì cấm).
  - **L (LSP)**: Thay thế Liskov (Lớp con thay thế được lớp cha).
  - **I (ISP)**: Phân tách Interface (Interface nhỏ gọn).
  - **D (DIP)**: Đảo ngược phụ thuộc (Phụ thuộc vào Interface, không phụ thuộc vào triển khai chi tiết).
- **분석 방법론 (OOA Methods)**:
  - **람바우 (Rumbaugh - OMT)**: 객체 모형 (Object) -> 동적 모형 (Dynamic) -> 기능 모형 (Functional - DFD).
  - 💡 **Mẹo ghi nhớ**: K/Đ/C -> **Không Đợi Chờ**

Điểm chốt của **2. 객체지향 (OOP - Object Oriented Programming)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **1. 객체지향 설계 5대 원칙 (SOLID)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 1. 객체지향 설계 5대 원칙 (SOLID)

Ở bước 31/57, **1. 객체지향 설계 5대 원칙 (SOLID)** xuất hiện như phần tiếp nối của **2. 객체지향 (OOP - Object Oriented Programming)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **1. 객체지향 설계 5대 원칙 (SOLID)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

**개념 (Khái niệm):** 시스템의 변경이나 확장에 유연하게 대응하기 위해 지켜야 할 5가지 원칙 (5 nguyên tắc thiết kế hướng đối tượng giúp hệ thống linh hoạt trước các thay đổi và mở rộng).

*   **SRP (Single Responsibility Principle - 단일 책임 원칙):**
    *   **Korean:** 객체는 '단 하나의 책임'만 가져야 함. 클래스를 수정해야 할 이유는 단 하나여야 함.
    *   **VI (Vietnamese) (Tiếng Việt):** Nguyên tắc Đơn trách nhiệm. Một đối tượng (hoặc lớp) chỉ nên có một trách nhiệm duy nhất. Lý do để sửa đổi một lớp chỉ nên có một.
    *   **Example:**
        *   *KR:* 보고서를 생성하는 클래스와 출력하는 클래스를 분리.
        *   *VN:* Tách biệt lớp tạo báo cáo và lớp in báo cáo, không để chung một lớp.
*   **OCP (Open-Closed Principle - 개방-폐쇄 원칙):**
    *   **Korean:** 기능 추가에는 열려(Open) 있어야 하고, 기존 코드 변경에는 닫혀(Closed) 있어야 함. 인터페이스로 캡슐화.
    *   **VI (Vietnamese) (Tiếng Việt):** Nguyên tắc Đóng - Mở. Mở rộng chức năng thì dễ dàng (Open), nhưng không được sửa đổi mã nguồn hiện tại (Closed). Thường dùng Interface để đóng gói.
    *   **Example:**
        *   *KR:* 결제 수단(카드, 페이 등)을 인터페이스로 구현하여 새로운 결제 수단 추가 시 기존 코드 수정 없이 확장.
        *   *VN:* Dùng Interface cho phương thức thanh toán, khi thêm phương thức mới (ví dụ: ví điện tử) thì không cần sửa mã cũ.
*   **LSP (Liskov Substitution Principle - 리스코프 치환 원칙):**
    *   **Korean:** 자식 클래스는 최소한 부모 클래스의 행위를 수행할 수 있어야 함. 부모의 의도를 훼손하지 않고 확장.
    *   **VI (Vietnamese) (Tiếng Việt):** Nguyên tắc Thay thế Liskov. Lớp con phải có thể thay thế lớp cha mà không làm hỏng tính đúng đắn của chương trình. Lớp con chỉ nên mở rộng, không làm sai lệch ý định của lớp cha.
    *   **Example:**
        *   *KR:* 새(Bird) 부모 클래스를 상속받은 펭귄(Penguin)이 날기(fly) 메서드를 가지면 LSP 위반.
        *   *VN:* Chim cánh cụt kế thừa từ lớp Chim, nhưng nếu gọi hàm bay() sẽ bị lỗi, vi phạm LSP. Cần thiết kế lại.
*   **ISP (Interface Segregation Principle - 인터페이스 분리 원칙):**
    *   **Korean:** 사용하지 않는 인터페이스에 의존하지 않도록 분리.
    *   **VI (Vietnamese) (Tiếng Việt):** Nguyên tắc Phân tách Interface. Không nên ép các lớp phụ thuộc vào những interface mà chúng không sử dụng. Hãy chia nhỏ interface khổng lồ thành các interface cụ thể.
    *   **Example:**
        *   *KR:* 복합기 인터페이스를 프린터, 스캐너, 팩스 인터페이스로 분리.
        *   *VN:* Tách interface của máy photocopy đa năng thành các interface riêng: In, Quét, Fax.
*   **DIP (Dependency Inversion Principle - 의존 역전 원칙):**
    *   **Korean:** 구체적인 클래스보다 추상화된 클래스(인터페이스)에 의존해야 함.
    *   **VI (Vietnamese) (Tiếng Việt):** Nguyên tắc Đảo ngược phụ thuộc. Các module cấp cao không nên phụ thuộc vào module cấp thấp, cả hai nên phụ thuộc vào abstractions (interface).
    *   **Example:**
        *   *KR:* 자동차가 스노우타이어(구체) 대신 타이어(추상) 인터페이스에 의존.
        *   *VN:* Lớp xe hơi phụ thuộc vào interface "Lốp xe" nói chung, thay vì phụ thuộc trực tiếp vào "Lốp đi tuyết".

💡 **Mẹo ghi nhớ (Mnemonics):** **SOLID** (S = Single, O = Open, L = Liskov, I = Interface, D = Dependency)

---

Như vậy, **1. 객체지향 설계 5대 원칙 (SOLID)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **7. 설계 도구 및 모듈화 심화 (Công cụ thiết kế & Mô-đun hóa chuyên sâu)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 7. 설계 도구 및 모듈화 심화 (Công cụ thiết kế & Mô-đun hóa chuyên sâu)

Sau khi đã đặt nền bằng **1. 객체지향 설계 5대 원칙 (SOLID)**, ta chuyển sang **7. 설계 도구 및 모듈화 심화 (Công cụ thiết kế & Mô-đun hóa chuyên sâu)**. Đây là mắt xích 32/57 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **7. 설계 도구 및 모듈화 심화 (Công cụ thiết kế & Mô-đun hóa chuyên sâu)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **NS 차트 (Nassi-Shneiderman Chart)**. Hãy xác định **NS 차트 (Nassi-Shneiderman Chart)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### NS 차트 (Nassi-Shneiderman Chart)

Phần nguồn của **NS 차트 (Nassi-Shneiderman Chart)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- 논리의 기술에 중점을 둔 도형을 이용한 표현 방법이다. (Là phương pháp biểu diễn bằng hình khối, trọng tâm vào việc mô tả logic.)
- 연속, 선택 및 다중 선택, 반복 등의 제어 논리 구조를 표현한다. (Thể hiện cấu trúc logic điều khiển như tuần tự, lựa chọn (if-else), đa lựa chọn (switch), lặp lại (while/for).)
- GOTO나 화살표를 사용하지 않는다. (Không sử dụng lệnh GOTO hay mũi tên.)
- 시각적으로 명확히 식별하는 데 적합하다. (Thích hợp để nhận diện rõ ràng về mặt thị giác.)
- 이해하기 쉽고, 코드 변환이 용이하다. (Dễ hiểu và dễ chuyển đổi thành code.)
- **Ví dụ (Example):** Dùng các khối hình chữ nhật xếp chồng lên nhau để biểu diễn một hàm tính toán thay vì dùng sơ đồ khối (Flowchart) có mũi tên rườm rà.

Các ý về **NS 차트 (Nassi-Shneiderman Chart)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **NS 차트 (Nassi-Shneiderman Chart)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **재사용 (Reuse / Tái sử dụng)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **재사용 (Reuse / Tái sử dụng)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 재사용 (Reuse / Tái sử dụng)

Các ý ngay dưới **재사용 (Reuse / Tái sử dụng)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- 이미 개발된 기능을 새로운 시스템이나 기능 개발에 사용할 수 있는 정도를 의미한다. (Mức độ có thể sử dụng lại các chức năng đã phát triển cho hệ thống hoặc chức năng mới.)
- 재사용 규모에 따른 분류: 함수와 객체, 컴포넌트, 애플리케이션. (Phân loại theo quy mô: Hàm/Đối tượng, Component, Ứng dụng).

Các bullet của **재사용 (Reuse / Tái sử dụng)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **재사용 (Reuse / Tái sử dụng)**, đừng bắt đầu lại từ số không. **효과적인 모듈 설계 방안 (Phương án thiết kế module hiệu quả)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **효과적인 모듈 설계 방안 (Phương án thiết kế module hiệu quả)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 효과적인 모듈 설계 방안 (Phương án thiết kế module hiệu quả)

Bây giờ ta đi vào nội dung của **효과적인 모듈 설계 방안 (Phương án thiết kế module hiệu quả)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 결합도는 줄이고 응집도는 높인다. (Giảm độ kết dính (Coupling) và tăng độ gắn kết (Cohesion).)
- 복잡도와 중복성을 줄인다. (Giảm độ phức tạp và sự trùng lặp.)
- 일관성을 유지시킨다. (Duy trì tính nhất quán.)
- 모듈의 기능은 지나치게 제한적이어서는 안 된다. (Chức năng của module không nên quá hạn hẹp.)
- 유지보수가 용이해야 한다. (Phải dễ dàng bảo trì.)
- 💡 **Mẹo ghi nhớ (Mnemonic):** **CUTK** (Cao Ứng - Thấp Kết): **Cứ Ứng Thật Kỹ** -> 응집도 높게(Cohesion High), 결합도 낮게(Coupling Low).

Các bullet của **효과적인 모듈 설계 방안 (Phương án thiết kế module hiệu quả)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**효과적인 모듈 설계 방안 (Phương án thiết kế module hiệu quả)** vừa cho ta cách đặt câu hỏi. Bây giờ **주요 코드 (Các loại Code cơ bản)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Với **주요 코드 (Các loại Code cơ bản)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 주요 코드 (Các loại Code cơ bản)

Phần nguồn của **주요 코드 (Các loại Code cơ bản)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- 순차 코드 (Sequence Code): 일정 기준에 따라서 차례로 일련번호를 부여하는 방법. (Gắn số thứ tự liên tiếp theo một tiêu chuẩn định sẵn - VD: 001, 002, 003).
- 표의 숫자 코드 (Significant Digit Code): 코드화 대상 항목의 중량, 면적, 용량 등의 물리적 수치를 적용시키는 방법. (Sử dụng trực tiếp các chỉ số vật lý như trọng lượng, kích thước vào mã - VD: Tivi 50 inch thì mã là TV-50).

Các bullet của **주요 코드 (Các loại Code cơ bản)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Với **주요 코드 (Các loại Code cơ bản)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Ta có thể khép mục **7. 설계 도구 및 모듈화 심화 (Công cụ thiết kế & Mô-đun hóa chuyên sâu)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **3. 모듈 (Module)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 3. 모듈 (Module)

Từ **7. 설계 도구 및 모듈화 심화 (Công cụ thiết kế & Mô-đun hóa chuyên sâu)**, ta đã có điểm tựa để bước vào **3. 모듈 (Module)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 33/57 trước khi đi vào chi tiết.

Để đọc **3. 모듈 (Module)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **결합도 (Coupling - Độ kết dính giữa các module)**, **응집도 (Cohesion - Độ gắn kết trong 1 module)**, **팬인 (Fan-In) / 팬아웃 (Fan-Out)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **결합도 (Coupling - Độ kết dính giữa các module)**: Càng thấp càng tốt.
  - 자료 (Data - Tốt nhất) < 스탬프 (Stamp) < 제어 (Control) < 외부 (External) < 공통 (Common) < 내용 (Content - Tệ nhất).
  - 💡 **Mẹo ghi nhớ**: T/S/C/N/C/N (Tốt -> Tệ) -> **Tính Sao Cho Nhẹ Cả Người**
- **응집도 (Cohesion - Độ gắn kết trong 1 module)**: Càng cao càng tốt.
  - 기능적 (Functional - Tốt nhất) > 순차적 (Sequential) > 통신적 (Communication) > 절차적 (Procedural) > 시간적 (Temporal) > 논리적 (Logical) > 우연적 (Coincidental - Tệ nhất).
  - 💡 **Mẹo ghi nhớ**: K/T/T/T/T/L/N (Tốt -> Tệ) -> **Không Thể Tin Thằng Trẻ Làm Ngốc**
- **팬인 (Fan-In) / 팬아웃 (Fan-Out)**:
  - Fan-in (Số module gọi nó): Cao thì tốt (tái sử dụng nhiều).
  - Fan-out (Số module nó gọi): Càng thấp càng tốt.

Điểm chốt của **3. 모듈 (Module)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **2. 모듈 (Module) & 독립성 (Independence)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 2. 모듈 (Module) & 독립성 (Independence)

Ở bước 34/57, **2. 모듈 (Module) & 독립성 (Independence)** xuất hiện như phần tiếp nối của **3. 모듈 (Module)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **2. 모듈 (Module) & 독립성 (Independence)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

**개념 (Khái niệm):** 시스템의 기능을 분리한 단위. 단독 컴파일과 재사용 가능 (Module là các đơn vị chức năng được phân tách của hệ thống, có thể biên dịch độc lập và tái sử dụng).

*   **기능적 독립성 (Functional Independence - Tính độc lập chức năng):**
    *   **Korean:** 각 모듈이 하나의 기능만을 수행하고 상호작용을 최소화하는 것. 결합도(Coupling)는 약하게(Weak), 응집도(Cohesion)는 강하게(Strong) 해야 함.
    *   **VI (Vietnamese) (Tiếng Việt):** Mỗi module chỉ thực hiện một chức năng và hạn chế tương tác với bên ngoài. Cần Độ phụ thuộc (Coupling) thấp và Độ gắn kết (Cohesion) cao. Kích thước module nên nhỏ gọn.
    *   **Example:**
        *   *KR:* 독립된 로그인 모듈은 다른 모듈 변경 시 영향을 받지 않음.
        *   *VN:* Module đăng nhập đứng độc lập, khi sửa giỏ hàng thì module đăng nhập không bị ảnh hưởng.

---

Như vậy, **2. 모듈 (Module) & 독립성 (Independence)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **7. 공통 모듈 (Common Module)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 7. 공통 모듈 (Common Module)

Sau khi đã đặt nền bằng **2. 모듈 (Module) & 독립성 (Independence)**, ta chuyển sang **7. 공통 모듈 (Common Module)**. Đây là mắt xích 35/57 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **7. 공통 모듈 (Common Module)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

**개념 (Khái niệm):** 여러 프로그램에서 공통적으로 사용할 수 있는 모듈 (Module dùng chung cho nhiều chương trình, ví dụ: Đăng nhập, tính toán).

*   **명세 기법 5가지 (5 nguyên tắc viết đặc tả module):**
    1.  **정확성 (Correctness):** 정확히 작성 (Chính xác).
    2.  **명확성 (Clarity):** 중의적이지 않게 (Rõ ràng, không mơ hồ).
    3.  **완전성 (Completeness):** 모든 것을 빠짐없이 (Đầy đủ).
    4.  **일관성 (Consistency):** 상호 충돌 없게 (Nhất quán).
    5.  **추적성 (Traceability):** 출처, 관계 추적 가능 (Có thể truy xuất nguồn gốc).
💡 **Mẹo ghi nhớ:** C-M-H-N-T (Chính-Rõ-Đủ-Nhất-Truy) -> **Chỉ Mong Học Nhất Trường**

---

Ta có thể khép mục **7. 공통 모듈 (Common Module)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **9. 효과적인 모듈 설계 방안 (Effective Module Design)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 9. 효과적인 모듈 설계 방안 (Effective Module Design)

Từ **7. 공통 모듈 (Common Module)**, ta đã có điểm tựa để bước vào **9. 효과적인 모듈 설계 방안 (Effective Module Design)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 36/57 trước khi đi vào chi tiết.

Để đọc **9. 효과적인 모듈 설계 방안 (Effective Module Design)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

*   **Korean:** 결합도↓, 응집도↑. 모듈의 영향 영역(Scope of Effect)이 제어 영역(Scope of Control) 안에 있어야 함. 단일 입구/단일 출구(Single Entry, Single Exit). 복잡도와 중복성 감소.
*   **VI (Vietnamese) (Tiếng Việt):** Coupling thấp, Cohesion cao. **Phạm vi ảnh hưởng (Scope of Effect) phải nằm TRONG Phạm vi kiểm soát (Scope of Control)** của module. Chỉ có 1 đầu vào và 1 đầu ra. Giảm độ phức tạp và dư thừa.
*   **Example:** Một hàm sắp xếp chỉ nên thay đổi mảng truyền vào nó (trong vùng kiểm soát), không nên vô tình thay đổi giao diện UI (vùng ảnh hưởng ngoài kiểm soát).

---

Điểm chốt của **9. 효과적인 모듈 설계 방안 (Effective Module Design)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **9. 소프트웨어 품질 특성 (ISO/IEC 9126)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 9. 소프트웨어 품질 특성 (ISO/IEC 9126)

Ở bước 37/57, **9. 소프트웨어 품질 특성 (ISO/IEC 9126)** xuất hiện như phần tiếp nối của **9. 효과적인 모듈 설계 방안 (Effective Module Design)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **9. 소프트웨어 품질 특성 (ISO/IEC 9126)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- 6 tiêu chuẩn chất lượng:
  1. **기능성 (Functionality - Chức năng)**: Bảo mật, Tương tác, Chính xác.
  2. **신뢰성 (Reliability - Độ tin cậy)**: Không lỗi, Phục hồi (회복성), Chịu lỗi (고장 허용성).
  3. **사용성 (Usability - Khả năng sử dụng)**: Dễ học, Dễ hiểu, Hấp dẫn.
  4. **효율성 (Efficiency - Hiệu quả)**: Thời gian phản hồi, Tiết kiệm tài nguyên.
  5. **유지 보수성 (Maintainability - Khả năng bảo trì)**: Dễ phân tích, Dễ thay đổi, Ổn định.
  6. **이식성 (Portability - Khả năng thay thế/di chuyển)**: Cài đặt dễ, Tương thích, Thay thế.

Như vậy, **9. 소프트웨어 품질 특성 (ISO/IEC 9126)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **8. 디자인 패턴 (Design Patterns)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 8. 디자인 패턴 (Design Patterns)

Sau khi đã đặt nền bằng **9. 소프트웨어 품질 특성 (ISO/IEC 9126)**, ta chuyển sang **8. 디자인 패턴 (Design Patterns)**. Đây là mắt xích 38/57 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **8. 디자인 패턴 (Design Patterns)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **디자인 패턴 (Design Pattern) 개요**. Hãy xác định **디자인 패턴 (Design Pattern) 개요** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 디자인 패턴 (Design Pattern) 개요

Phần nguồn của **디자인 패턴 (Design Pattern) 개요** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- 세부적인 구현 방안을 설계할 때 참조할 수 있는 전형적인 해결 방식 또는 예제를 의미한다. (Là những phương pháp giải quyết hoặc ví dụ điển hình có thể tham khảo khi thiết계 chi tiết phương án triển khai.)
- 3가지 유형 (3 Loại chính): 생성 패턴 (Creational), 구조 패턴 (Structural), 행위 패턴 (Behavioral).

Các ý về **디자인 패턴 (Design Pattern) 개요** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **디자인 패턴 (Design Pattern) 개요** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **생성 패턴 (Creational Pattern / Mẫu khởi tạo) - 5 loại** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **생성 패턴 (Creational Pattern / Mẫu khởi tạo) - 5 loại** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 생성 패턴 (Creational Pattern / Mẫu khởi tạo) - 5 loại

Các ý ngay dưới **생성 패턴 (Creational Pattern / Mẫu khởi tạo) - 5 loại** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- 객체 생성과 관련된 패턴. (Liên quan đến việc tạo đối tượng.)
- **빌더 (Builder):** 작게 분리된 인스턴스를 건축하듯이 조합하여 객체를 생성함. (Tạo đối tượng bằng cách lắp ráp các phần nhỏ như xây nhà.)
- **팩토리 메소드 (Factory Method):** 객체 생성을 서브 클래스에서 처리하도록 분리하여 캡슐화한 패턴으로, 가상 생성자(Virtual Constructor) 패턴이라고도 함. (Giao việc tạo đối tượng cho lớp con, còn gọi là Virtual Constructor).
- **프로토타입 (Prototype):** 원본 객체를 복제하는 방법으로 객체를 생성함. (Tạo đối tượng bằng cách copy/clone từ đối tượng gốc).
- **싱글톤 (Singleton):** 생성된 객체를 여러 프로세스가 동시에 참조할 수는 없음 (하나의 객체만 생성). (Đảm bảo chỉ có 1 instance duy nhất được tạo ra).
- **추상 팩토리 (Abstract Factory):** 서로 연관·의존하는 객체들의 그룹으로 생성하여 추상적으로 표현함. (Tạo ra một nhóm các đối tượng có liên quan với nhau thông qua interface).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **BFPSA** (Build - Fact - Pro - Sing - Ab): **Bạn Phải Phạt Sợ Ai**.

Các bullet của **생성 패턴 (Creational Pattern / Mẫu khởi tạo) - 5 loại** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **생성 패턴 (Creational Pattern / Mẫu khởi tạo) - 5 loại**, đừng bắt đầu lại từ số không. **구조 패턴 (Structural Pattern / Mẫu cấu trúc) - 7 loại** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **구조 패턴 (Structural Pattern / Mẫu cấu trúc) - 7 loại**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 구조 패턴 (Structural Pattern / Mẫu cấu trúc) - 7 loại

Bây giờ ta đi vào nội dung của **구조 패턴 (Structural Pattern / Mẫu cấu trúc) - 7 loại**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 클래스나 객체를 조합해 더 큰 구조를 만드는 패턴. (Kết hợp lớp/đối tượng thành cấu trúc lớn hơn).
- **어댑터 (Adapter):** 인터페이스를 다른 클래스가 재사용할 수 있도록 변환함. (Biến đổi interface để lớp khác dùng được, giống như cục sạc chuyển đổi điện).
- **브리지 (Bridge):** 서로가 독립적으로 확장할 수 있도록 구성함. (Tách phần trừu tượng và phần thực thi để cả 2 có thể phát triển độc lập).
- **컴포지트 (Composite):** 복합 객체와 단일 객체를 구분 없이 다루고자 할 때 사용함. (Xử lý đối tượng đơn lẻ và đối tượng phức hợp (nhóm) theo cùng một cách, cấu trúc cây).
- **데코레이터 (Decorator):** 부가적인 기능을 추가하기 위해 다른 객체들을 덧붙이는 방식으로 구현함. (Gắn thêm tính năng mới vào đối tượng có sẵn giống như trang trí).
- **퍼싸드 (Facade):** 복잡한 서브 클래스들을 피해 더 상위에 인터페이스를 구성함. (Tạo một interface cấp cao đơn giản để che giấu hệ thống con phức tạp bên dưới).
- **플라이웨이트 (Flyweight):** 가능한 한 인스턴스를 공유해서 사용함으로써 메모리를 절약하는 패턴. (Chia sẻ instance để tiết kiệm bộ nhớ, tái sử dụng những gì giống nhau).
- **프록시 (Proxy):** 접근이 어려운 객체와 여기에 연결하려는 객체 사이에서 인터페이스 역할을 수행하는 패턴. (Người đại diện, đứng giữa kiểm soát truy cập vào đối tượng thực).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **ABCDFFP** (Ad - Bri - Com - Dec - Fac - Fly - Pro): **Anh Bán Cơm Đĩa Phải Phạt Phi**.

Các bullet của **구조 패턴 (Structural Pattern / Mẫu cấu trúc) - 7 loại** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**구조 패턴 (Structural Pattern / Mẫu cấu trúc) - 7 loại** vừa cho ta cách đặt câu hỏi. Bây giờ **행위 패턴 (Behavioral Pattern / Mẫu hành vi) - 11 loại** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Với **행위 패턴 (Behavioral Pattern / Mẫu hành vi) - 11 loại**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 행위 패턴 (Behavioral Pattern / Mẫu hành vi) - 11 loại

Phần nguồn của **행위 패턴 (Behavioral Pattern / Mẫu hành vi) - 11 loại** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- 객체 간의 상호작용이나 책임 분배에 대한 패턴. (Giao tiếp và phân bổ trách nhiệm giữa các đối tượng).
- **책임 연쇄 (Chain of Responsibility):** 요청을 한 객체가 처리하지 못하면 다음 객체로 넘어가는 형태. (Xử lý dây chuyền, ai làm được thì làm, không thì chuyển người tiếp theo).
- **커맨드 (Command):** 재이용하거나 취소할 수 있도록 요청에 필요한 정보를 저장함. (Đóng gói yêu cầu thành đối tượng, dễ dàng undo/redo).
- **인터프리터 (Interpreter):** 언어에 문법 표현을 정의함. (Định nghĩa ngữ pháp cho ngôn ngữ).
- **반복자 (Iterator):** 접근이 잦은 객체에 대해 동일한 인터페이스를 사용하도록 함. (Duyệt qua các phần tử của tập hợp mà không cần biết cấu trúc bên trong).
- **중재자 (Mediator):** 복잡한 상호 작용을 캡슐화하여 객체로 정의함. (Làm trung gian liên lạc giữa các đối tượng để giảm sự phụ thuộc chéo).
- **메멘토 (Memento):** 객체를 해당 시점의 상태로 돌릴 수 있는 기능을 제공, C + Z와 같은 되돌리기 기능을 개발할 때 주로 이용함. (Lưu trạng thái để khôi phục/Undo).
- **옵서버 (Observer):** 객체에 상속되어 있는 다른 객체들에게 변화된 상태를 전달함. (Một đối tượng thay đổi trạng thái, các đối tượng đăng ký theo dõi sẽ được thông báo - VD: Đăng ký kênh YouTube).
- **상태 (State):** 객체의 상태에 따라 동일한 동작을 다르게 처리해야 할 때 사용함. (Thay đổi hành vi khi trạng thái đối tượng thay đổi).
- **전략 (Strategy):** 동일한 계열의 알고리즘들을 상호 교환할 수 있게 정의함. (Đóng gói thuật toán để có thể thay đổi linh hoạt lúc runtime).
- **템플릿 메소드 (Template Method):** 하위 클래스에서 세부 처리를 구체화함. (Lớp cha định nghĩa khung thuật toán, lớp con implement chi tiết).
- **방문자 (Visitor):** 처리 기능을 분리하여 별도의 클래스로 구성함. (Tách logic xử lý khỏi cấu trúc dữ liệu, đối tượng Visitor đi "thăm" các phần tử để xử lý).

Các bullet của **행위 패턴 (Behavioral Pattern / Mẫu hành vi) - 11 loại** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Với **행위 패턴 (Behavioral Pattern / Mẫu hành vi) - 11 loại**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Ta có thể khép mục **8. 디자인 패턴 (Design Patterns)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **16. 디자인 패턴 심화 (Design Patterns chuyên sâu)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 16. 디자인 패턴 심화 (Design Patterns chuyên sâu)

Từ **8. 디자인 패턴 (Design Patterns)**, ta đã có điểm tựa để bước vào **16. 디자인 패턴 심화 (Design Patterns chuyên sâu)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 39/57 trước khi đi vào chi tiết.

Để đọc **16. 디자인 패턴 심화 (Design Patterns chuyên sâu)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **디자인 패턴 사용의 장·단점 (Ưu/Nhược điểm của Design Pattern)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 디자인 패턴 사용의 장·단점 (Ưu/Nhược điểm của Design Pattern)

Các ý ngay dưới **디자인 패턴 사용의 장·단점 (Ưu/Nhược điểm của Design Pattern)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- **장점 (Ưu điểm):** 범용적 코딩 스타일(구조 파악 용이), 생산성 향상, 개발 시간/비용 절약, 의사소통 원활, 유연한 대처 가능. (Dễ đọc code, tăng năng suất, tiết kiệm chi phí, dễ giao tiếp, dễ đối phó thay đổi).
- **단점 (Nhược điểm):** 초기 투자 비용 부담, 다른 기반(비객체지향)에는 부적합. (Tốn kém thời gian học ban đầu, không hợp cho mô hình không hướng đối tượng).

Các bullet của **디자인 패턴 사용의 장·단점 (Ưu/Nhược điểm của Design Pattern)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **디자인 패턴 사용의 장·단점 (Ưu/Nhược điểm của Design Pattern)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **디자인 패턴 - 23종 세부 특징 (23 Mẫu Design Pattern GoF)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **디자인 패턴 - 23종 세부 특징 (23 Mẫu Design Pattern GoF)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 디자인 패턴 - 23종 세부 특징 (23 Mẫu Design Pattern GoF)

Bây giờ ta đi vào nội dung của **디자인 패턴 - 23종 세부 특징 (23 Mẫu Design Pattern GoF)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- *(Tham khảo lại Mục 8 để biết tên gọi, dưới đây là các đặc điểm từ khóa thường ra thi)*
- **생성 패턴 (5개):**
  - **Abstract Factory:** 인터페이스를 통해 구체적인 클래스에 의존하지 않고 객체 생성. (Tạo đối tượng qua Interface mà không phụ thuộc Class cụ thể).
  - **Builder:** 생성 과정과 표현 방법을 분리. (Tách rời quá trình tạo và cách biểu diễn).
  - **Factory Method:** 상위 클래스는 인터페이스만 정의, 실제 생성은 서브 클래스가. (Lớp cha định nghĩa Interface, lớp con thực sự tạo).
  - **Prototype:** 비용이 큰 경우 복제하여 생성. (Clone khi chi phí tạo mới quá lớn).
  - **Singleton:** 인스턴스가 하나뿐임을 보장. (Đảm bảo chỉ có 1 instance).
- **구조 패턴 (7개):**
  - **Adapter:** 호환성이 없는 클래스들의 인터페이스 변환. (Chuyển đổi interface không tương thích).
  - **Bridge:** 기능(추상층)과 구현(구현부)을 분리. (Tách rời chức năng và phần thực thi).
  - **Composite:** 트리 구조로 구성. (Cấu trúc cây).
  - **Decorator:** 능동적으로 기능들을 확장(덧붙임). (Chủ động mở rộng/thêm tính năng).
  - **Facade:** 통합 인터페이스 제공(Wrapper 객체). (Cung cấp interface tổng hợp).
  - **Flyweight:** 다수의 유사 객체 공유 (메모리 절약). (Chia sẻ nhiều đối tượng giống nhau để tiết kiệm RAM).
  - **Proxy:** 네트워크 연결, 메모리 대용량 객체 접근 등 (인터페이스 역할). (Làm đại diện kết nối mạng, tải đối tượng lớn).

Các bullet của **디자인 패턴 - 23종 세부 특징 (23 Mẫu Design Pattern GoF)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **디자인 패턴 - 23종 세부 특징 (23 Mẫu Design Pattern GoF)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **16. 디자인 패턴 심화 (Design Patterns chuyên sâu)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **4. 디자인 패턴 (Design Patterns - GoF)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 4. 디자인 패턴 (Design Patterns - GoF)

Ở bước 40/57, **4. 디자인 패턴 (Design Patterns - GoF)** xuất hiện như phần tiếp nối của **16. 디자인 패턴 심화 (Design Patterns chuyên sâu)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **4. 디자인 패턴 (Design Patterns - GoF)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **생성 패턴 (Creational - 5)**, **구조 패턴 (Structural - 7)**, **행위 패턴 (Behavioral - 11)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **생성 패턴 (Creational - 5)**: Abstract Factory, Builder, Factory Method, Prototype, Singleton. (Tạo đối tượng)
- **구조 패턴 (Structural - 7)**: Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy. (Cấu trúc, ghép nối)
- **행위 패턴 (Behavioral - 11)**: Strategy, Mediator, Command, Observer, State, Iterator, Visitor, Chain of Responsibility, Interpreter, Memento, Template Method. (Hành vi, tương tác)

---

Như vậy, **4. 디자인 패턴 (Design Patterns - GoF)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **11. 디자인 패턴 (Design Pattern)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 11. 디자인 패턴 (Design Pattern)

Sau khi đã đặt nền bằng **4. 디자인 패턴 (Design Patterns - GoF)**, ta chuyển sang **11. 디자인 패턴 (Design Pattern)**. Đây là mắt xích 41/57 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **11. 디자인 패턴 (Design Pattern)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

**개념 (Khái niệm):** 설계 시 참조할 수 있는 전형적인 해결 방식 (Các mẫu giải pháp tiêu chuẩn dùng tham khảo khi thiết kế phần mềm). GoF (Gang of Four)가 23개로 체계화.
💡 **Mẹo ghi nhớ:** "바퀴를 다시 발명하지 마라 (Don't reinvent the wheel)" - Đừng phát minh lại bánh xe, hãy dùng các mẫu đã được kiểm chứng.

*   **장단점 (Ưu & Nhược điểm):**
    *   장점: 구조 파악 용이, 의사소통 원활, 생산성 향상 (Dễ nắm cấu trúc, giao tiếp tốt, tăng năng suất).
    *   단점: **초기 투자 비용 부담**, 객체지향 전용 (Tốn chi phí/thời gian học ban đầu, chỉ hợp với Hướng đối tượng).

Ta bắt đầu phần nội dung bằng **11.1 생성 패턴 (Creational - 5개)**. Hãy xác định **11.1 생성 패턴 (Creational - 5개)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 11.1 생성 패턴 (Creational - 5개)

Phần nguồn của **11.1 생성 패턴 (Creational - 5개)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

객체 생성 캡슐화 (Đóng gói quá trình tạo đối tượng).
1.  **추상 팩토리 (Abstract Factory):** 연관된 객체 그룹 생성 (Tạo nhóm đối tượng liên quan).
2.  **빌더 (Builder):** 생성 과정과 표현 방법 분리 (Tách quá trình xây dựng và biểu diễn).
3.  **팩토리 메소드 (Factory Method):** 객체 생성을 서브 클래스에 위임, 가상 생성자 (Giao việc tạo đối tượng cho lớp con).
4.  **프로토타입 (Prototype):** 원본 객체 복제 (Nhân bản đối tượng nguyên mẫu Clone).
5.  **싱글톤 (Singleton):** 인스턴스가 하나뿐임을 보장 (Đảm bảo chỉ có 1 instance duy nhất).

Phần **11.1 생성 패턴 (Creational - 5개)** không có nhiều dữ liệu rời để tách nhỏ, vì vậy hãy giữ câu hỏi mục đích và tự chốt bằng một câu giải thích trước khi đi tiếp.

Ta vừa chốt **11.1 생성 패턴 (Creational - 5개)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **11.2 구조 패턴 (Structural - 7개)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **11.2 구조 패턴 (Structural - 7개)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 11.2 구조 패턴 (Structural - 7개)

Các ý ngay dưới **11.2 구조 패턴 (Structural - 7개)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

객체 조합으로 더 큰 구조 생성 (Kết hợp đối tượng thành cấu trúc lớn hơn).
1.  **어댑터 (Adapter):** 호환 안 되는 인터페이스 변환 (Chuyển đổi interface không tương thích).
2.  **브리지 (Bridge):** 구현과 추상층 분리 (Tách biệt phần triển khai và phần trừu tượng).
3.  **컴포지트 (Composite):** 트리 구조, 단일/복합 객체 동일하게 다룸 (Cấu trúc cây, xử lý đối tượng đơn và phức như nhau).
4.  **데코레이터 (Decorator):** 동적으로 기능 덧붙임 (Thêm chức năng linh hoạt bằng cách bọc đối tượng).
5.  **퍼싸드 (Facade):** 복잡한 서브 시스템 위에 통합 인터페이스(Wrapper) 제공 (Tạo mặt tiền/giao diện chung đơn giản cho hệ thống phức tạp).
6.  **플라이웨이트 (Flyweight):** 인스턴스 공유로 메모리 절약 (Chia sẻ đối tượng để tiết kiệm bộ nhớ).
7.  **프록시 (Proxy):** 접근 어려운 객체를 대리 수행 (Đại diện/ủy quyền truy cập cho đối tượng khác).

Phần **11.2 구조 패턴 (Structural - 7개)** không có nhiều dữ liệu rời để tách nhỏ, vì vậy hãy giữ câu hỏi mục đích và tự chốt bằng một câu giải thích trước khi đi tiếp.

Sau khi đọc **11.2 구조 패턴 (Structural - 7개)**, đừng bắt đầu lại từ số không. **11.3 행위 패턴 (Behavioral - 11개)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **11.3 행위 패턴 (Behavioral - 11개)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 11.3 행위 패턴 (Behavioral - 11개)

Bây giờ ta đi vào nội dung của **11.3 행위 패턴 (Behavioral - 11개)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

객체 간 상호작용 및 책임 분배 (Tương tác và phân chia trách nhiệm giữa các đối tượng).
1.  **책임 연쇄 (Chain of Responsibility):** 고리를 따라 책임 넘김 (Truyền yêu cầu theo chuỗi xử lý).
2.  **커맨드 (Command):** 요청을 객체로 캡슐화 (로그, Undo) (Đóng gói yêu cầu thành đối tượng, tiện cho Undo/Log).
3.  **인터프리터 (Interpreter):** 언어 문법 정의 (Định nghĩa cú pháp ngôn ngữ).
4.  **반복자 (Iterator):** 내부 노출 없이 순차 접근 (Truy cập tuần tự không lộ cấu trúc).
5.  **중재자 (Mediator):** 복잡한 상호작용을 통제/지시 (Điều phối viên trung gian để giảm phụ thuộc chéo).
6.  **메멘토 (Memento):** 상태 스냅샷 저장/복원 (Lưu trạng thái để Undo/Khôi phục).
7.  **옵서버 (Observer):** 상태 변화를 구독자에게 전파 (Publish/Subscribe, thông báo khi có thay đổi).
8.  **상태 (State):** 상태에 따라 다른 동작 (Hành vi thay đổi theo trạng thái).
9.  **전략 (Strategy):** 알고리즘 캡슐화하여 교체 가능 (Đóng gói thuật toán, dễ dàng hoán đổi).
10. **템플릿 메소드 (Template Method):** 상위가 골격, 하위가 세부 구현 (Lớp cha tạo khung, lớp con điền chi tiết).
11. **방문자 (Visitor):** 처리 기능을 분리하여 방문 수행 (Tách logic xử lý ra khỏi cấu trúc dữ liệu, đi "thăm" từng phần tử).

---

Phần **11.3 행위 패턴 (Behavioral - 11개)** không có nhiều dữ liệu rời để tách nhỏ, vì vậy hãy giữ câu hỏi mục đích và tự chốt bằng một câu giải thích trước khi đi tiếp.

Như vậy, **11.3 행위 패턴 (Behavioral - 11개)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Ta có thể khép mục **11. 디자인 패턴 (Design Pattern)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **2. 인터페이스 검토 및 연계 기술 (Interface Review & Tech)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 2. 인터페이스 검토 및 연계 기술 (Interface Review & Tech)

Từ **11. 디자인 패턴 (Design Pattern)**, ta đã có điểm tựa để bước vào **2. 인터페이스 검토 및 연계 기술 (Interface Review & Tech)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 42/57 trước khi đi vào chi tiết.

Để đọc **2. 인터페이스 검토 및 연계 기술 (Interface Review & Tech)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **정형 기술 검토 (FTR - Formal Technical Review)**, **동료검토 (Peer Review)**, **워크 스루 (Walk Through)**, **인스펙션 (Inspection)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **정형 기술 검토 (FTR - Formal Technical Review)**:
  - **동료검토 (Peer Review)**: Tác giả tự giải thích tài liệu, đồng nghiệp tìm lỗi.
  - **워크 스루 (Walk Through)**: Gửi tài liệu trước, họp review ngắn để tìm lỗi nhanh.
  - **인스펙션 (Inspection)**: Chuyên gia khác (không phải tác giả) kiểm tra chặt chẽ để tìm lỗi.
  - 💡 **Mẹo ghi nhớ**: 동료(Tự thuyết trình) / 워크스루(Họp ngắn) / 인스펙션(Chuyên gia chém).
- **연계 기술 (Connection Tech)**:
  - DB Link, API, Socket (Cấp phát cổng), JDBC.
- **미들웨어 (Middleware)**: Phần mềm trung gian kết nối các hệ thống khác biệt.
  - **TP Monitor**: Giám sát Transaction (Giao dịch).
  - **MOM (Message-Oriented)**: Bất đồng bộ (비동기), dùng hàng đợi tin nhắn (메시지 큐).
  - **ORB (Object Request Broker)**: Hướng đối tượng, chuẩn CORBA.
  - **WAS (Web Application Server)**: Xử lý nội dung web động (동적인 콘텐츠).

---

Điểm chốt của **2. 인터페이스 검토 및 연계 기술 (Interface Review & Tech)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **13. 시스템 연계 및 인터페이스 (System Interface & Integration)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 13. 시스템 연계 및 인터페이스 (System Interface & Integration)

Ở bước 43/57, **13. 시스템 연계 및 인터페이스 (System Interface & Integration)** xuất hiện như phần tiếp nối của **2. 인터페이스 검토 및 연계 기술 (Interface Review & Tech)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **13. 시스템 연계 및 인터페이스 (System Interface & Integration)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **13.1 시스템 연계 기술 (Các công nghệ liên kết hệ thống)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **13.1 시스템 연계 기술 (Các công nghệ liên kết hệ thống)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 13.1 시스템 연계 기술 (Các công nghệ liên kết hệ thống)

Bây giờ ta đi vào nội dung của **13.1 시스템 연계 기술 (Các công nghệ liên kết hệ thống)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

1.  **DB Link:** DB 객체 이용 (Kết nối trực tiếp qua DB Link).
2.  **API/Open API:** 프로그램 인터페이스 (Mở cổng API để ứng dụng khác gọi).
3.  **EAI (연계 솔루션):** 중계 서버/클라이언트 사용 (Dùng máy chủ trung gian Enterprise Application Integration).
4.  **Socket:** 포트 할당하여 연결 (Mở port mạng Socket để truyền dữ liệu).
5.  **Web Service:** WSDL, UDDI, SOAP 프로토콜 사용 (Dịch vụ web dùng giao thức chuẩn XML/SOAP).

Phần **13.1 시스템 연계 기술 (Các công nghệ liên kết hệ thống)** không có nhiều dữ liệu rời để tách nhỏ, vì vậy hãy giữ câu hỏi mục đích và tự chốt bằng một câu giải thích trước khi đi tiếp.

Ta vừa chốt **13.1 시스템 연계 기술 (Các công nghệ liên kết hệ thống)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **13.2 인터페이스 통신 & 처리 유형 (Loại giao tiếp & xử lý)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **13.2 인터페이스 통신 & 처리 유형 (Loại giao tiếp & xử lý)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 13.2 인터페이스 통신 & 처리 유형 (Loại giao tiếp & xử lý)

Phần nguồn của **13.2 인터페이스 통신 & 처리 유형 (Loại giao tiếp & xử lý)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

*   **통신 유형 (Loại Giao tiếp):**
    *   **단방향 (Unidirectional):** 응답 없음 (Chỉ gửi, không cần phản hồi).
    *   **동기 (Synchronous):** 응답 대기 (Gửi và đợi phản hồi).
    *   **비동기 (Asynchronous):** 다른 작업 수행 (Gửi xong làm việc khác, trả lời sau).
*   **처리 유형 (Loại Xử lý):**
    *   **실시간 (Real-time):** 즉시 처리 (Xử lý ngay lập tức).
    *   **지연 처리 (Deferred):** 비용 절감을 위해 모아서 처리 (Trì hoãn xử lý để tiết kiệm chi phí).
    *   **배치 (Batch):** 대용량 일괄 처리 (Gom dữ liệu lớn xử lý 1 lần).

Các bullet của **13.2 인터페이스 통신 & 처리 유형 (Loại giao tiếp & xử lý)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **13.2 인터페이스 통신 & 처리 유형 (Loại giao tiếp & xử lý)**, đừng bắt đầu lại từ số không. **13.3 명세화 (Specification)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **13.3 명세화 (Specification)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 13.3 명세화 (Specification)

Các ý ngay dưới **13.3 명세화 (Specification)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

*   **송수신 데이터 명세화:** 데이터 필드명, 타입, 사이즈, **암호화 여부** 정의 (Đặc tả dữ liệu: Tên trường, Kiểu, Kích thước, và có Cần Mã hóa không).
*   **오류 식별 및 처리 방안 명세화:** 오류 코드, 메시지, 해결 방법 정의 (Đặc tả lỗi: Mã lỗi, Thông báo, Cách xử lý để dễ vận hành).

---

Các bullet của **13.3 명세화 (Specification)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **13.3 명세화 (Specification)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Như vậy, **13. 시스템 연계 및 인터페이스 (System Interface & Integration)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **17. 시스템 연계 및 미들웨어 (Liên kết hệ thống & Middleware)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 17. 시스템 연계 및 미들웨어 (Liên kết hệ thống & Middleware)

Sau khi đã đặt nền bằng **13. 시스템 연계 및 인터페이스 (System Interface & Integration)**, ta chuyển sang **17. 시스템 연계 및 미들웨어 (Liên kết hệ thống & Middleware)**. Đây là mắt xích 44/57 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **17. 시스템 연계 및 미들웨어 (Liên kết hệ thống & Middleware)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **요구사항 검증 방법 추가 (Các phương pháp kiểm chứng yêu cầu bổ sung)**. Hãy xác định **요구사항 검증 방법 추가 (Các phương pháp kiểm chứng yêu cầu bổ sung)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 요구사항 검증 방법 추가 (Các phương pháp kiểm chứng yêu cầu bổ sung)

Phần nguồn của **요구사항 검증 방법 추가 (Các phương pháp kiểm chứng yêu cầu bổ sung)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **요구사항 검토 (Requirements Review):** 동료검토, 워크스루, 인스펙션. (Review thủ công bởi người).
- **프로토타이핑 (Prototyping):** 견본품을 만들어 최종 결과물을 예측. (Làm bản nháp/prototype để dự đoán kết quả).
- **테스트 설계 (Test Design):** 요구사항이 현실적으로 테스트 가능한지 검토 (Test Case 생성). (Tạo Test Case để xem yêu cầu có khả thi không).
- **CASE 도구 활용 (CASE Tools):** 일관성 분석(Consistency Analysis)을 통해 요구사항 변경사항 추적 및 분석. (Dùng tool để phân tích tính nhất quán).

Các bullet của **요구사항 검증 방법 추가 (Các phương pháp kiểm chứng yêu cầu bổ sung)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **요구사항 검증 방법 추가 (Các phương pháp kiểm chứng yêu cầu bổ sung)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **시스템 연계 기술 (Các công nghệ liên kết hệ thống)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **시스템 연계 기술 (Các công nghệ liên kết hệ thống)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 시스템 연계 기술 (Các công nghệ liên kết hệ thống)

Các ý ngay dưới **시스템 연계 기술 (Các công nghệ liên kết hệ thống)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- **DB Link:** DB에서 제공하는 DB Link 객체를 이용. (Dùng trực tiếp link kết nối của DB).
- **API / Open API:** 송신 시스템의 DB에서 데이터를 읽어와 제공하는 프로그램. (Giao diện lập trình ứng dụng mở).
- **연계 솔루션:** EAI 서버와 송·수신 시스템에 설치되는 클라이언트(Client)를 이용. (Giải pháp dùng EAI Server).
- **Socket:** 통신을 위한 소켓을 생성하여 포트를 할당하고 클라이언트와 연결. (Tạo socket và cấp phát port để giao tiếp mạng).
- **Web Service:** WSDL, UDDI, SOAP 프로토콜을 이용. (Dịch vụ web dùng chuẩn SOAP/WSDL).

Các bullet của **시스템 연계 기술 (Các công nghệ liên kết hệ thống)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **시스템 연계 기술 (Các công nghệ liên kết hệ thống)**, đừng bắt đầu lại từ số không. **연계 매커니즘 구성요소 (Thành phần cơ chế liên kết)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **연계 매커니즘 구성요소 (Thành phần cơ chế liên kết)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 연계 매커니즘 구성요소 (Thành phần cơ chế liên kết)

Bây giờ ta đi vào nội dung của **연계 매커니즘 구성요소 (Thành phần cơ chế liên kết)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- **송신 시스템 (Sender System):** 데이터를 전송 형식에 맞게 변환하여 송신. (Hệ thống gửi, chuyển đổi dữ liệu ra định dạng chuẩn).
- **수신 시스템 (Receiver System):** 수신한 데이터를 시스템에 맞게 변환하여 반영. (Hệ thống nhận, chuyển đổi dữ liệu chuẩn vào DB).
- **연계 서버 (Integration Server):** 송수신 현황을 모니터링. (Server trung gian giám sát quá trình truyền dữ liệu).

Các bullet của **연계 매커니즘 구성요소 (Thành phần cơ chế liên kết)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**연계 매커니즘 구성요소 (Thành phần cơ chế liên kết)** vừa cho ta cách đặt câu hỏi. Bây giờ **미들웨어(Middleware) 상세 (Chi tiết Middleware)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Với **미들웨어(Middleware) 상세 (Chi tiết Middleware)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 미들웨어(Middleware) 상세 (Chi tiết Middleware)

Phần nguồn của **미들웨어(Middleware) 상세 (Chi tiết Middleware)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- 운영체제와 응용 프로그램 사이에서 다양한 서비스를 제공.
- **DB (DataBase):** 2-Tier 아키텍처에 주로 사용, 클라이언트와 원격 DB를 연결. (Kết nối Client-DB).
- **RPC (Remote Procedure Call):** 원격 프로시저를 로컬 프로시저처럼 호출. (Gọi hàm từ xa như gọi hàm cục bộ).
- **MOM (Message Oriented Middleware):** 비동기형 메시지 전달 (이기종 분산 데이터 시스템). (Truyền tin nhắn bất đồng bộ).
- **TP-Monitor (Transaction Processing Monitor):** 온라인 트랜잭션 처리 및 감시 (항공기/철도 예약). (Quản lý giao dịch online tốc độ cao).
- **ORB (Object Request Broker):** CORBA 표준 스펙을 구현한 객체 지향 미들웨어. (Middleware hướng đối tượng chuẩn CORBA).
- **WAS (Web Application Server):** 동적인 콘텐츠를 처리하는 미들웨어. (Xử lý web động).

---

# 3과목: 데이터베이스 (Phần 3: Cơ sở dữ liệu)

Phần **3과목: 데이터베이스 (Phần 3: Cơ sở dữ liệu)** cần được đọc như một bước trong bài giảng: trước hết xác định mục đích, sau đó nối các ý bên dưới với điều kiện và hệ quả trước khi ghi nhớ từng dòng.
*(Lưu ý: Tùy theo chương trình, Database có thể thuộc Subject 1 hoặc 3. Dưới đây là kiến thức cốt lõi về DB)*

---

Các bullet của **미들웨어(Middleware) 상세 (Chi tiết Middleware)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Với **미들웨어(Middleware) 상세 (Chi tiết Middleware)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Ta có thể khép mục **17. 시스템 연계 및 미들웨어 (Liên kết hệ thống & Middleware)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **14. 미들웨어 (Middleware)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 14. 미들웨어 (Middleware)

Từ **17. 시스템 연계 및 미들웨어 (Liên kết hệ thống & Middleware)**, ta đã có điểm tựa để bước vào **14. 미들웨어 (Middleware)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 45/57 trước khi đi vào chi tiết.

Để đọc **14. 미들웨어 (Middleware)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

**개념 (Khái niệm):** 운영체제와 응용 프로그램 사이의 중재자 (Phần mềm trung gian đứng giữa OS và Ứng dụng).
💡 **Mẹo ghi nhớ 미들웨어:** DB, RPC, MOM, TP-Monitor, ORB, WAS

1.  **DB 미들웨어:** 2-Tier 원격 연결 (ODBC, IDAPI, Glue). (Kết nối CSDL 2 lớp).
2.  **RPC (Remote Procedure Call):** 원격을 로컬처럼 호출 (Entera, ONC/RPC). (Gọi hàm từ xa như gọi hàm cục bộ).
3.  **MOM (Message Oriented Middleware):** 비동기 메시지, 데이터 동기 (IBM MQ, JMS). (Truyền tin nhắn bất đồng bộ, đồng bộ dữ liệu hệ thống khác nền tảng).
4.  **TP-Monitor (Transaction Processing):** 항공/철도 예약, 빠른 응답/트랜잭션 감시 (tuxedo, tmax). (Giám sát giao dịch, đảm bảo tốc độ phản hồi nhanh cho đặt vé).
5.  **ORB (Object Request Broker):** 객체 지향, CORBA 표준 (Orbix). (Môi giới yêu cầu đối tượng, chuẩn CORBA).
6.  **WAS (Web Application Server):** 동적 콘텐츠, 웹 환경 핵심(Java/EJB) (WebLogic, WebSphere). (Xử lý nội dung web động, tác vụ doanh nghiệp quan trọng).
    *   *Example:* Apache là Web Server (tĩnh), còn WebLogic/Tomcat là WAS (động).

*   **솔루션 식별 & 명세서 작성:** 아키텍처 구성 정보, 구매 내역 확인 -> 제약사항 확인 (Xác định Middleware dựa trên kiến trúc và hóa đơn mua sắm -> Kiểm tra các hạn chế / constraints).

Điểm chốt của **14. 미들웨어 (Middleware)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **6. 애자일 방법론 (Agile Methodology)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 6. 애자일 방법론 (Agile Methodology)

Ở bước 46/57, **6. 애자일 방법론 (Agile Methodology)** xuất hiện như phần tiếp nối của **14. 미들웨어 (Middleware)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **6. 애자일 방법론 (Agile Methodology)** như một bài học cho người mới, hãy giữ câu hỏi: **một dự án đi qua những giai đoạn nào, mỗi mô hình phân bổ công việc và rủi ro ra sao?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **개념**, **4대 핵심 가치 (4 Core Values)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **개념**: Linh hoạt, phản hồi liên tục.
- **4대 핵심 가치 (4 Core Values)**:
  1. Cá nhân và tương tác (개인과의 상호작용) > Quy trình và công cụ.
  2. Phần mềm chạy được (실행되는 소프트웨어) > Tài liệu.
  3. Hợp tác với khách hàng (고객과의 협력) > Đàm phán hợp đồng.
  4. Phản hồi với sự thay đổi (변화에 유연하게 대응) > Tuân thủ kế hoạch.

Như vậy, **6. 애자일 방법론 (Agile Methodology)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **7. 스크럼(Scrum) 및 XP(eXtreme Programming)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 7. 스크럼(Scrum) 및 XP(eXtreme Programming)

Sau khi đã đặt nền bằng **6. 애자일 방법론 (Agile Methodology)**, ta chuyển sang **7. 스크럼(Scrum) 및 XP(eXtreme Programming)**. Đây là mắt xích 47/57 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **7. 스크럼(Scrum) 및 XP(eXtreme Programming)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **스크럼 (Scrum)**, **용어**, **프로세스**, **XP (eXtreme Programming)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **스크럼 (Scrum)**: Quản lý dự án Agile theo nhóm.
  - **용어**: 제품 백로그 (Product Backlog - Yêu cầu tổng), 스프린트 (Sprint - Chu kỳ 2-4 tuần), 속도 (Velocity), 번 다운 차트 (Burn Down Chart - Biểu đồ tiến độ), PO (Product Owner), SM (Scrum Master).
  - **프로세스**: Backlog -> Sprint Planning -> Sprint Execution (Daily Scrum) -> Sprint Review (Đánh giá) -> Sprint Retrospective (Hồi tưởng/Cải tiến).
- **XP (eXtreme Programming)**: Tối ưu hóa phát triển phần mềm cùng khách hàng.
  - **핵심 가치 (5 Core Values)**: 의사소통 (Communication), 단순성 (Simplicity), 용기 (Courage), 존중 (Respect), 피드백 (Feedback).
  - 💡 **Mẹo ghi nhớ**: Y/Đ/D/T/P -> **Ý Định Dũng Tướng Phàm**
  - **기본 원리 (Principles)**: Pair Programming, CI (Tích hợp liên tục), TDD (Test-Driven Development), Refactoring (Tái cấu trúc mã), 40-Hour Work.

---

Ta có thể khép mục **7. 스크럼(Scrum) 및 XP(eXtreme Programming)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **2. 스크럼 및 XP 추가 개념 (Advanced Scrum & XP)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 2. 스크럼 및 XP 추가 개념 (Advanced Scrum & XP)

Từ **7. 스크럼(Scrum) 및 XP(eXtreme Programming)**, ta đã có điểm tựa để bước vào **2. 스크럼 및 XP 추가 개념 (Advanced Scrum & XP)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 48/57 trước khi đi vào chi tiết.

Để đọc **2. 스크럼 및 XP 추가 개념 (Advanced Scrum & XP)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **스크럼 프로세스 (Scrum Process)**, **일일 스크럼 (Daily Scrum)**, **스프린트 검토 (Sprint Review)**, **스프린트 회고 (Sprint Retrospective)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **스크럼 프로세스 (Scrum Process)**:
  - **일일 스크럼 (Daily Scrum)**: Họp đứng 15 phút. Cập nhật tiến độ lên Burn-down Chart (Biểu đồ tiêu hao).
  - **스프린트 검토 (Sprint Review)**: Demo sản phẩm cho khách hàng xem có đúng ý không.
  - **스프린트 회고 (Sprint Retrospective)**: Nội bộ team họp để rút kinh nghiệm, cải tiến quy trình.
- **XP 기법 상세 (XP Details)**:
  - **사용자 스토리 (User Story)**: Kịch bản do khách hàng viết (đơn vị chức năng), có thể chứa Test Case.
  - **릴리즈 계획 (Release Planning)**: Kế hoạch phát hành từng phần sản phẩm (v1.0, v1.1).
  - **스파이크 (Spike)**: Chương trình nhỏ, code thử nghiệm nhanh để kiểm tra tính khả thi của công nghệ nhằm giảm rủi ro (기술적 위험 감소). Code này có thể bị vứt đi sau khi test.

Điểm chốt của **2. 스크럼 및 XP 추가 개념 (Advanced Scrum & XP)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **4. 운영 환경 구축 고려사항 (Operation Environment Considerations)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 4. 운영 환경 구축 고려사항 (Operation Environment Considerations)

Ở bước 49/57, **4. 운영 환경 구축 고려사항 (Operation Environment Considerations)** xuất hiện như phần tiếp nối của **2. 스크럼 및 XP 추가 개념 (Advanced Scrum & XP)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **4. 운영 환경 구축 고려사항 (Operation Environment Considerations)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **WAS (Web Application Server)**, **오픈 소스 (Open Source)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **운영체제 (OS)** & **DBMS**: 가용성 (Availability), 성능 (Performance), 기술 지원 (Tech Support), 구축 비용 (Cost).
  - OS có thêm: 주변 기기 (Thiết bị ngoại vi).
  - DBMS có thêm: 상호 호환성 (Khả năng tương thích - JDBC/ODBC).
- **WAS (Web Application Server)**: Xử lý nội dung động. Có thêm **가비지 컬렉션 (GC - Dọn rác)**.
- **오픈 소스 (Open Source)**: Cần chú ý 라이선스 (Bản quyền), 사용자 수 (Số lượng người dùng), 기술의 지속 가능성 (Khả năng duy trì công nghệ).

Như vậy, **4. 운영 환경 구축 고려사항 (Operation Environment Considerations)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **6. 구조적 분석 도구 (Structured Analysis Tools)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 6. 구조적 분석 도구 (Structured Analysis Tools)

Sau khi đã đặt nền bằng **4. 운영 환경 구축 고려사항 (Operation Environment Considerations)**, ta chuyển sang **6. 구조적 분석 도구 (Structured Analysis Tools)**. Đây là mắt xích 50/57 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **6. 구조적 분석 도구 (Structured Analysis Tools)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng là bằng chứng để so sánh các lựa chọn theo cùng tiêu chí, không phải danh sách cần học thuộc từng ô. Trong khối này, **DFD (Biểu đồ luồng dữ liệu)**, **DD (Từ điển dữ liệu)**, **HIPO** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- Phân tích Top-down (하향식), dùng biểu đồ (도형).
- **DFD (Biểu đồ luồng dữ liệu)**: Process (Tròn), Flow (Mũi tên), Data Store (Vạch ngang), Terminator (Vuông).
- **DD (Từ điển dữ liệu)**:
  - `=`: Định nghĩa
  - `+`: Nối
  - `( )`: Tùy chọn (Optional)
  - `[ | ]`: Chọn 1 trong các (Or)
  - `{ }`: Lặp (Iteration)
  - `* *`: Chú thích
- **HIPO**: Biểu đồ phân cấp (가시적, 총체적, 세부적).

Ta có thể khép mục **6. 구조적 분석 도구 (Structured Analysis Tools)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **10. 소프트웨어 설계 원리 (Software Design Principles)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 10. 소프트웨어 설계 원리 (Software Design Principles)

Từ **6. 구조적 분석 도구 (Structured Analysis Tools)**, ta đã có điểm tựa để bước vào **10. 소프트웨어 설계 원리 (Software Design Principles)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 51/57 trước khi đi vào chi tiết.

Để đọc **10. 소프트웨어 설계 원리 (Software Design Principles)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **모듈화 (Modularity)**, **추상화 (Abstraction)**, **단계적 분해 (Stepwise Refinement)**, **정보 은닉 (Information Hiding)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **모듈화 (Modularity)**:
  - Module quá nhỏ -> Chi phí tích hợp (Integration Cost) tăng.
  - Module quá lớn -> Chi phí phát triển từng module (Development Cost) tăng.
- **추상화 (Abstraction)**: 3 loại (과정 - Quá trình, 데이터 - Dữ liệu, 제어 - Điều khiển).
- **단계적 분해 (Stepwise Refinement)**: Đi từ trên xuống (Top-down).
- **정보 은닉 (Information Hiding)**: Giấu thông tin để giảm phụ thuộc.
- **시스템 타입 (System Types)**:
  - **대화형 (Interactive)**: Tương tác (VD: Web bán hàng).
  - **이벤트 중심 (Event-driven)**: Dựa trên sự kiện (VD: Chuông báo cháy).
  - **변환형 (Transformational)**: Biến đổi dữ liệu (VD: Trình biên dịch - Compiler).
  - **객체 영속형 (Object Persistence)**: Lưu trữ lâu dài (VD: Database Server).

Điểm chốt của **10. 소프트웨어 설계 원리 (Software Design Principles)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **3. 결합도 (Coupling - Độ phụ thuộc)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 3. 결합도 (Coupling - Độ phụ thuộc)

Ở bước 52/57, **3. 결합도 (Coupling - Độ phụ thuộc)** xuất hiện như phần tiếp nối của **10. 소프트웨어 설계 원리 (Software Design Principles)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **3. 결합도 (Coupling - Độ phụ thuộc)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

**개념 (Khái niệm):** 모듈 간의 의존성 정도 (Mức độ phụ thuộc giữa các module với nhau). **낮을수록 좋음 (Càng thấp càng tốt).**

순서 (Từ Tốt nhất đến Xấu nhất): **자료(Data) -> 스탬프(Stamp) -> 제어(Control) -> 외부(External) -> 공통(Common) -> 내용(Content)**
💡 **Mẹo ghi nhớ:** T-S-C-N-C-N (Data-Stamp-Control-External-Common-Content) -> **Tính Sao Cho Nhẹ Cả Người**

1.  **자료 결합도 (Data Coupling) - TỐT NHẤT:**
    *   **Korean:** 파라미터(자료 요소)만 전달.
    *   **VI (Vietnamese) (Tiếng Việt):** Chỉ truyền tham số dữ liệu cần thiết.
    *   **Example:** `sum(a, b)` truyền đúng 2 số a, b.
2.  **스탬프 결합도 (Stamp Coupling):**
    *   **Korean:** 배열/레코드 등 자료구조가 전달됨.
    *   **VI (Vietnamese) (Tiếng Việt):** Truyền toàn bộ cấu trúc dữ liệu (mảng, đối tượng) nhưng chỉ dùng 1 phần.
    *   **Example:** Truyền đối tượng `User` nhưng chỉ dùng `User.name`.
3.  **제어 결합도 (Control Coupling):**
    *   **Korean:** 제어 신호(Flag)를 전달하여 모듈 흐름 제어.
    *   **VI (Vietnamese) (Tiếng Việt):** Truyền cờ điều khiển (flag, boolean) can thiệp vào logic của module khác.
    *   **Example:** Truyền `isExpress=true` để quyết định cách xử lý.
4.  **외부 결합도 (External Coupling):**
    *   **Korean:** 외부 변수/데이터 참조.
    *   **VI (Vietnamese) (Tiếng Việt):** Cùng phụ thuộc vào dữ liệu / file / thiết bị bên ngoài.
    *   **Example:** Hai module dùng chung một file `config.txt`.
5.  **공통 결합도 (Common Coupling):**
    *   **Korean:** 공통 데이터 영역(전역 변수) 공유.
    *   **VI (Vietnamese) (Tiếng Việt):** Nhiều module dùng chung biến toàn cục (global variables).
    *   **Example:** Sử dụng `public static int totalCount` chung.
6.  **내용 결합도 (Content Coupling) - XẤU NHẤT:**
    *   **Korean:** 내부 기능/자료 직접 참조. 스파게티 코드.
    *   **VI (Vietnamese) (Tiếng Việt):** Truy cập, sửa đổi trực tiếp dữ liệu/logic nội bộ của module khác.
    *   **Example:** `moduleB.internalValue = 10` từ module A.

---

Như vậy, **3. 결합도 (Coupling - Độ phụ thuộc)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **4. 응집도 (Cohesion - Độ gắn kết)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 4. 응집도 (Cohesion - Độ gắn kết)

Sau khi đã đặt nền bằng **3. 결합도 (Coupling - Độ phụ thuộc)**, ta chuyển sang **4. 응집도 (Cohesion - Độ gắn kết)**. Đây là mắt xích 53/57 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **4. 응집도 (Cohesion - Độ gắn kết)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

**개념 (Khái niệm):** 모듈 내부 요소들이 서로 밀접하게 관련되어 있는 정도 (Mức độ liên quan chặt chẽ của các thành phần BÊN TRONG 1 module). **강할수록 좋음 (Càng cao càng tốt).**

순서 (Từ Tốt nhất đến Xấu nhất): **기능(Functional) -> 순차(Sequential) -> 교환(Communication) -> 절차(Procedural) -> 시간(Temporal) -> 논리(Logical) -> 우연(Coincidental)**
💡 **Mẹo ghi nhớ:** K-S-K-C-S-N-U (Kì-Sun-Kiều-Chul-Shi-Non-U) -> **Không Tin Kiều Chỉ Sợ Người Ù**

1.  **기능적 응집도 (Functional):**
    *   **Korean:** 단일 문제와 연관되어 수행. (Tốt nhất)
    *   **VI (Vietnamese) (Tiếng Việt):** Mọi thành phần trong module cùng giải quyết MỘT bài toán duy nhất.
2.  **순차적 응집도 (Sequential):**
    *   **Korean:** 출력 데이터가 다음 활동의 입력 데이터로 사용됨.
    *   **VI (Vietnamese) (Tiếng Việt):** Đầu ra của bước này là đầu vào của bước kia (trong cùng module).
3.  **교환(통신)적 응집도 (Communication):**
    *   **Korean:** 동일한 입출력을 사용하여 서로 다른 기능 수행.
    *   **VI (Vietnamese) (Tiếng Việt):** Các chức năng khác nhau dùng chung một tập dữ liệu đầu vào / đầu ra.
4.  **절차적 응집도 (Procedural):**
    *   **Korean:** 기능들을 순차적으로 수행.
    *   **VI (Vietnamese) (Tiếng Việt):** Các phần tử được thực hiện theo trình tự thời gian / kịch bản nhất định.
5.  **시간적 응집도 (Temporal):**
    *   **Korean:** 특정 시간에 처리되는 기능들을 모음.
    *   **VI (Vietnamese) (Tiếng Việt):** Gom các tác vụ xảy ra cùng một thời điểm (VD: khối khởi tạo hệ thống Init).
6.  **논리적 응집도 (Logical):**
    *   **Korean:** 유사한 성격/형태로 분류되는 요소들을 모음.
    *   **VI (Vietnamese) (Tiếng Việt):** Gom các hàm có tính chất logic giống nhau (VD: Hàm in các loại báo cáo, mặc dù báo cáo khác nhau).
7.  **우연적 응집도 (Coincidental) - XẤU NHẤT:**
    *   **Korean:** 아무 관련 없이 구성됨.
    *   **VI (Vietnamese) (Tiếng Việt):** Các phần tử gom lại ngẫu nhiên, không liên quan gì nhau.

---

Ta có thể khép mục **4. 응집도 (Cohesion - Độ gắn kết)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **5. Fan-In / Fan-Out (팬인 / 팬아웃)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 5. Fan-In / Fan-Out (팬인 / 팬아웃)

Từ **4. 응집도 (Cohesion - Độ gắn kết)**, ta đã có điểm tựa để bước vào **5. Fan-In / Fan-Out (팬인 / 팬아웃)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 54/57 trước khi đi vào chi tiết.

Để đọc **5. Fan-In / Fan-Out (팬인 / 팬아웃)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

**개념 (Khái niệm):** 모듈 간의 호출 관계를 나타내는 지표 (Chỉ số thể hiện mức độ gọi lẫn nhau giữa các module).

*   **Fan-In (들어옴 / Đi vào):**
    *   **Korean:** 나를 호출하는 모듈 수. **높게(High)** 설계하는 것이 재사용성 측면에서 좋음. (단, 단일 장애점 주의)
    *   **VI (Vietnamese) (Tiếng Việt):** Số lượng module gọi đến module hiện tại. Fan-In CAO là tốt vì chứng tỏ module được tái sử dụng nhiều, nhưng cần cẩn thận vì nó là trung tâm (Single Point of Failure).
*   **Fan-Out (나감 / Đi ra):**
    *   **Korean:** 내가 호출하는 모듈 수. **낮게(Low)** 설계하여 단순화해야 함.
    *   **VI (Vietnamese) (Tiếng Việt):** Số lượng module mà module hiện tại gọi. Fan-Out THẤP là tốt, tránh việc module phụ thuộc vào quá nhiều nơi khác.

💡 **Mẹo ghi nhớ:** Fan-In = Gọi VÀO tôi (High is good) / Fan-Out = Tôi gọi RA (Low is good).

---

Điểm chốt của **5. Fan-In / Fan-Out (팬인 / 팬아웃)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **6. N-S 차트 (Nassi-Schneiderman Chart)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

---

## 6. N-S 차트 (Nassi-Schneiderman Chart)

Ở bước 55/57, **6. N-S 차트 (Nassi-Schneiderman Chart)** xuất hiện như phần tiếp nối của **5. Fan-In / Fan-Out (팬인 / 팬아웃)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **6. N-S 차트 (Nassi-Schneiderman Chart)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

**개념 (Khái niệm):** 논리 기술 중점의 박스 다이어그램 (Biểu đồ dạng hộp tập trung mô tả logic).

*   **Korean:** GOTO나 화살표를 사용하지 않음. 단일 입구/단일 출구. Box Diagram, Chapin Chart라고도 부름. 순차, 선택, 반복 논리 구조 시각화.
*   **VI (Vietnamese) (Tiếng Việt):** Đặc điểm quan trọng nhất: **KHÔNG DÙNG GOTO và KHÔNG CÓ MŨI TÊN**. Có một lối vào và một lối ra duy nhất. Còn gọi là Box Diagram hoặc Chapin Chart. Gồm 3 cấu trúc: Tuần tự, Lựa chọn (If-else), Lặp (Loop). Dễ chuyển sang code nhưng khó vẽ.

---

Như vậy, **6. N-S 차트 (Nassi-Schneiderman Chart)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **8. 재사용 (Reuse)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

---

## 8. 재사용 (Reuse)

Sau khi đã đặt nền bằng **6. N-S 차트 (Nassi-Schneiderman Chart)**, ta chuyển sang **8. 재사용 (Reuse)**. Đây là mắt xích 56/57 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **8. 재사용 (Reuse)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

**개념 (Khái niệm):** 기존 기능을 최적화하여 다시 쓰는 것 (Tái sử dụng chức năng để tiết kiệm thời gian và chi phí).

*   **Korean:** 결합도는 낮고 응집도는 높아야 함.
*   **VI (Vietnamese) (Tiếng Việt):** Yêu cầu: Độ phụ thuộc (Coupling) THẤP và Độ gắn kết (Cohesion) CAO.
*   **분류 (Phân loại):**
    *   **함수와 객체 (Function & Object):** 소스 코드 단위 (Mức mã nguồn / Class).
    *   **컴포넌트 (Component):** 인터페이스 통신 (Mức Interface, không sửa code gốc).
    *   **애플리케이션 (Application):** 시스템 전체 (Mức ứng dụng hoàn chỉnh).

---

Ta có thể khép mục **8. 재사용 (Reuse)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **10. 코드 (Code) 개요 & 종류**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

---

## 10. 코드 (Code) 개요 & 종류

Từ **8. 재사용 (Reuse)**, ta đã có điểm tựa để bước vào **10. 코드 (Code) 개요 & 종류**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 57/57 trước khi đi vào chi tiết.

Để đọc **10. 코드 (Code) 개요 & 종류** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

**개념 (Khái niệm):** 데이터를 식별, 분류, 배열하기 위해 사용하는 기호 (Ký hiệu dùng để nhận dạng, phân loại và sắp xếp dữ liệu).

*   **기능 (Chức năng):** 식별(Nhận dạng), 분류(Phân loại), 배열(Sắp xếp), 표준화(Chuẩn hóa), 간소화(Đơn giản hóa).
*   **종류 (Các loại Code):**
    1.  **순차 코드 (Sequential):** 발생 순서대로 일련번호 부여 (Đánh số thứ tự 1, 2, 3...).
    2.  **블록 코드 (Block):** 공통성 있는 항목을 블록으로 묶음 (Phân khối theo nhóm chung).
    3.  **10진 코드 (Decimal):** 0~9까지 10진 분할 반복, 도서분류 (Phân loại thập phân như sách thư viện).
    4.  **그룹 분류 코드 (Group Classification):** 대/중/소분류 (Phân nhóm lớn/vừa/nhỏ như 1-01-001).
    5.  **연상 코드 (Mnemonic):** 명칭이나 약호와 관계있는 기호 (Mã gợi nhớ, ví dụ: TV-40 cho Tivi 40 inch).
    6.  **표의 숫자 코드 (Significant Digit):** 물리적 수치를 직접 적용 (Dùng kích thước vật lý làm mã).
    7.  **합성 코드 (Combined):** 2개 이상 조합 (Kết hợp nhiều mã).

*   **코드 부여 체계 (Code Assignment System):**
    *   **Korean:** 이름만으로 개체의 용도와 적용 범위를 알 수 있게 상세 명시 (자릿수, 구분자).
    *   **VI (Vietnamese) (Tiếng Việt):** Hệ thống đánh mã sao cho nhìn vào tên mã là biết ngay công dụng và phạm vi (cần nêu rõ số chữ số, dấu phân cách).
    *   **Example:** 연도(00) + 학과(00) + 개인번호(000) -> 2401001.

---

Khép lại **10. 코드 (Code) 개요 & 종류**, điều cần giữ lại là mối quan hệ giữa mục đích, cơ chế và điểm giới hạn của các khái niệm trong nguồn. Khi ôn lại, hãy tự giải thích chúng bằng một câu hoàn chỉnh rồi đối chiếu với các điểm dễ nhầm trước khi chuyển sang bài tổng hợp của môn.