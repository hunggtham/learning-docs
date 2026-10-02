# 245. 연산자 우선순위 (Operator Precedence)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **245. 연산자 우선순위 (Operator Precedence)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối operator precedence với parsing, associativity và evaluation order, để biểu thức không đổi nghĩa.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **245. 연산자 우선순위 (Operator Precedence)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **245. 연산자 우선순위 (Operator Precedence)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **입출력 (Input/Output)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **245. 연산자 우선순위 (Operator Precedence)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

연산자, 우선순위

> **Chuyển mạch:** Ở chặng này của **245. 연산자 우선순위 (Operator Precedence)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **244. 조건(삼항) 연산자 (Ternary Operator)**에서 만든 기준을 이어받아 **245. 연산자 우선순위 (Operator Precedence)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **245. 연산자 우선순위 (Operator Precedence)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **245. 연산자 우선순위 (Operator Precedence)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **245. 연산자 우선순위 (Operator Precedence)**, **245. 연산자 우선순위 (Operator Precedence)** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 245. 연산자 우선순위 (Operator Precedence)

Từ **244. 조건(삼항) 연산자 (Ternary Operator)**, ta đã có điểm tựa để bước vào **245. 연산자 우선순위 (Operator Precedence)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 12/91 trước khi đi vào chi tiết.

Để đọc **245. 연산자 우선순위 (Operator Precedence)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng là bằng chứng để so sánh các lựa chọn theo cùng tiêu chí, không phải danh sách cần học thuộc từng ô.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “245. 연산자 우선순위 (Operator Precedence)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 하나의 수식에 여러 연산자가 있을 때 계산되는 순서.
- 순위: **단항**(`!`, `++`, `~`) > **산술**(`*`, `/` > `+`, `-`) > **관계**(`>`, `==`) > **논리**(`&&` > `||`) > **대입**(`=`, `+=`).
- 괄호 `()`가 가장 우선.

**Giải thích (Vietnamese):**
Thứ tự ưu tiên tính toán: Ngoặc () -> Đơn nguyên (phủ định, tăng giảm) -> Nhân chia cộng trừ -> So sánh -> Logic (AND trước OR sau) -> Gán.

**💡 Mẹo ghi nhớ (Mnemonics):**
**단산관논대** (Đơn - Toán - Quan - Luận - Gán): 단항 -> 산술 -> 관계 -> 논리 -> 대입.

---

Điểm chốt của **245. 연산자 우선순위 (Operator Precedence)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **입출력 (Input/Output)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

> **Bàn giao:** Sau **245. 연산자 우선순위 (Operator Precedence)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
