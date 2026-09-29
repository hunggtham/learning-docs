# 120-2 ~ 126: 애플리케이션 테스트 이론 (Application Test Theory)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **120-2 ~ 126: 애플리케이션 테스트 이론 (Application Test Theory)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **120-2 ~ 126: 애플리케이션 테스트 이론 (Application Test Theory)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **127 ~ 129: 화이트박스 테스트 (White Box Test)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

애플리케이션, 테스트, 이론

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **105: 시각에 따른 테스트 (Verification vs Validation)**에서 만든 기준을 이어받아 **120-2 ~ 126: 애플리케이션 테스트 이론 (Application Test Theory)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **120-2 ~ 126: 애플리케이션 테스트 이론 (Application Test Theory)** và nối nó với **127 ~ 129: 화이트박스 테스트 (White Box Test)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 120-2 ~ 126: 애플리케이션 테스트 이론 (Application Test Theory)

Từ **105: 시각에 따른 테스트 (Verification vs Validation)**, ta đã có điểm tựa để bước vào **120-2 ~ 126: 애플리케이션 테스트 이론 (Application Test Theory)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 60/95 trước khi đi vào chi tiết.

Để đọc **120-2 ~ 126: 애플리케이션 테스트 이론 (Application Test Theory)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **테스트의 기본 원리 (Nguyên lý cơ bản)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 테스트의 기본 원리 (Nguyên lý cơ bản)

Các ý ngay dưới **테스트의 기본 원리 (Nguyên lý cơ bản)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- **완벽한 테스트 불가능:** Không thể khẳng định 100% hết bug.
- **파레토 법칙 (Pareto):** 80% bug nằm ở 20% code cốt lõi. (Đám mây lỗi).
- **살충제 패러독스 (Pesticide Paradox):** Test hoài 1 kịch bản sẽ bị "nhờn", phải liên tục thay đổi bộ test.
- **정황 의존 (Context):** Tùy thuộc ngữ cảnh (Web, Game) mà test khác nhau.

Các bullet của **테스트의 기본 원리 (Nguyên lý cơ bản)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **테스트의 기본 원리 (Nguyên lý cơ bản)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **테스트 분류 (Phân loại Test)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **테스트 분류 (Phân loại Test)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 테스트 분류 (Phân loại Test)

Bây giờ ta đi vào nội dung của **테스트 분류 (Phân loại Test)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

1. **실행 여부 (Theo việc có chạy code không):**
   - **정적 테스트 (Static):** Không chạy code. Đọc, review tài liệu (Walkthrough, Inspection).
   - **동적 테스트 (Dynamic):** Chạy code. (White box, Black box).
2. **테스트 기반 (Theo căn cứ Test):**
   - **명세 기반 (Specification):** Dựa vào tài liệu yêu cầu.
   - **구조 기반 (Structure):** Dựa vào luồng logic của code.
   - **경험 기반 (Experience):** Dựa vào kinh nghiệm tester (Đoán lỗi).
3. **목적 (Theo mục đích):**
   - **강도 (Stress):** Ép tải (Dồn dập bắt nó sập).
   - **회귀 (Regression):** Sửa code xong test lại xem có hỏng chỗ cũ không.
   - **회복 (Recovery):** Giả vờ ngắt điện xem app phục hồi data được không.
   - **병행 (Parallel):** Chạy app cũ và app mới cùng lúc để so kết quả.

- 💡 **Mẹo ghi nhớ (Mnemonics):** Inspection (Khám nghiệm) = Tĩnh (Static). Regression (Hồi quy) = Sửa xong test lại.

---

Với **테스트 분류 (Phân loại Test)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **테스트 분류 (Phân loại Test)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **120-2 ~ 126: 애플리케이션 테스트 이론 (Application Test Theory)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **127 ~ 129: 화이트박스 테스트 (White Box Test)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.