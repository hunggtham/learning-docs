# 11. 데이터베이스 설계 (Thiết kế cơ sở dữ liệu)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **11. 데이터베이스 설계 (Thiết kế cơ sở dữ liệu)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối database design với requirements, logical model, physical model và governance, để mỗi quyết định có owner và tiêu chí kiểm tra.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **11. 데이터베이스 설계 (Thiết kế cơ sở dữ liệu)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **11. 데이터베이스 설계 (Thiết kế cơ sở dữ liệu)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **104. 데이터 모델에 표시할 요소 (Elements of Data Model)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **11. 데이터베이스 설계 (Thiết kế cơ sở dữ liệu)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

데이터베이스, 설계

> **Chuyển mạch:** Ở chặng này của **11. 데이터베이스 설계 (Thiết kế cơ sở dữ liệu)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **163-167. 데이터베이스 설계 순서 (Database Design Process)**에서 만든 기준을 이어받아 **11. 데이터베이스 설계 (Thiết kế cơ sở dữ liệu)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **11. 데이터베이스 설계 (Thiết kế cơ sở dữ liệu)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. 데이터베이스 설계 (Thiết kế cơ sở dữ liệu)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **11. 데이터베이스 설계 (Thiết kế cơ sở dữ liệu)**, **읽는 방법 (Cách đọc)** nêu điều cần giải thích; **11. 데이터베이스 설계 (Thiết kế cơ sở dữ liệu)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

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

> **Bàn giao:** Sau **11. 데이터베이스 설계 (Thiết kế cơ sở dữ liệu)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
