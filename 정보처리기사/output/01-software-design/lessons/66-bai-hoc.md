# 5. Fan-In / Fan-Out (팬인 / 팬아웃)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **5. Fan-In / Fan-Out (팬인 / 팬아웃)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối fan-in/fan-out với coupling, dependency và change impact, để đo độ tập trung trách nhiệm trong thiết kế.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **5. Fan-In / Fan-Out (팬인 / 팬아웃)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **5. Fan-In / Fan-Out (팬인 / 팬아웃)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **6. N-S 차트 (Nassi-Schneiderman Chart)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **5. Fan-In / Fan-Out (팬인 / 팬아웃)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

Fan-In, Fan-Out

> **Chuyển mạch:** Ở chặng này của **5. Fan-In / Fan-Out (팬인 / 팬아웃)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **4. 응집도 (Cohesion - Độ gắn kết)**에서 만든 기준을 이어받아 **5. Fan-In / Fan-Out (팬인 / 팬아웃)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **5. Fan-In / Fan-Out (팬인 / 팬아웃)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Fan-In / Fan-Out (팬인 / 팬아웃)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **5. Fan-In / Fan-Out (팬인 / 팬아웃)**, **5. Fan-In / Fan-Out (팬인 / 팬아웃)** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 5. Fan-In / Fan-Out (팬인 / 팬아웃)

Từ **4. 응집도 (Cohesion - Độ gắn kết)**, ta đã có điểm tựa để bước vào **5. Fan-In / Fan-Out (팬인 / 팬아웃)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 66/69 trước khi đi vào chi tiết.

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

> **Bàn giao:** Sau **5. Fan-In / Fan-Out (팬인 / 팬아웃)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
