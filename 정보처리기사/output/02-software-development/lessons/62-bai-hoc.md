# 105: 시각에 따른 테스트 (Verification vs Validation)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **105: 시각에 따른 테스트 (Verification vs Validation)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối verification với validation, để phân biệt xây đúng đặc tả với giải đúng nhu cầu.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **105: 시각에 따른 테스트 (Verification vs Validation)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **105: 시각에 따른 테스트 (Verification vs Validation)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **120-2 ~ 126: 애플리케이션 테스트 이론 (Application Test Theory)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **105: 시각에 따른 테스트 (Verification vs Validation)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

시각에, 따른, 테스트

> **Chuyển mạch:** Ở chặng này của **105: 시각에 따른 테스트 (Verification vs Validation)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **097-2: 테스트 프로세스 (Test Process - Quy trình kiểm thử)**에서 만든 기준을 이어받아 **105: 시각에 따른 테스트 (Verification vs Validation)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **105: 시각에 따른 테스트 (Verification vs Validation)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **105: 시각에 따른 테스트 (Verification vs Validation)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **105: 시각에 따른 테스트 (Verification vs Validation)**, **105: 시각에 따른 테스트 (Verification vs Validation)** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 105: 시각에 따른 테스트 (Verification vs Validation)

Sau khi đã đặt nền bằng **097-2: 테스트 프로세스 (Test Process - Quy trình kiểm thử)**, ta chuyển sang **105: 시각에 따른 테스트 (Verification vs Validation)**. Đây là mắt xích 62/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **105: 시각에 따른 테스트 (Verification vs Validation)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “105: 시각에 따른 테스트 (Verification vs Validation)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **검증 (Verification - Xác minh):** 개발자 시각 (Góc nhìn Dev). "Làm đúng thiết kế/mã code không?". (Are we building the product right?).
- **확인 (Validation - Thẩm định):** 사용자 시각 (Góc nhìn User). "Phần mềm này có đúng cái khách hàng cần không?". (Are we building the right product?).

- 💡 **Mẹo ghi nhớ (Mnemonics):** 검증 (Verification) = Code chuẩn chưa? (Dev). 확인 (Validation) = Khách ưng không? (User).

---

Ta có thể khép mục **105: 시각에 따른 테스트 (Verification vs Validation)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **120-2 ~ 126: 애플리케이션 테스트 이론 (Application Test Theory)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

> **Bàn giao:** Sau **105: 시각에 따른 테스트 (Verification vs Validation)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
