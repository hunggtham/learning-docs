# 9. 스키마 3계층 (Three-Schema Architecture)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **9. 스키마 3계층 (Three-Schema Architecture)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối three-schema architecture với external, conceptual và internal schema, để thay đổi storage không buộc đổi cách nhìn dữ liệu.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **9. 스키마 3계층 (Three-Schema Architecture)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **9. 스키마 3계층 (Three-Schema Architecture)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **14. 파레토 법칙 (Pareto Principle)** khi chuyển sang phần tiếp theo.

Mục tiêu phân biệt external, conceptual và internal schema theo lớp nhìn dữ liệu; từ khóa khoanh vùng mapping, independence và storage.

## 핵심 키워드 (Từ khóa)

스키마, 계층

Kiến thức liên kết đặt three-schema architecture trên nền interface contract và verification; cách đọc tiếp theo giúp theo dõi thay đổi ở lớp nào.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **26. 인터페이스 구현 검증 도구 (Interface Verification Tools)**에서 만든 기준을 이어받아 **9. 스키마 3계층 (Three-Schema Architecture)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

Cách đọc đã đặt khung đối tượng–điều kiện–hệ quả; phần schema dùng khung đó để nối view người dùng với mô hình và lưu trữ.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

Phần này khép lại bằng giá trị data independence và giới hạn mapping; khi sang Pareto, hãy chuyển từ kiến trúc dữ liệu sang cách ưu tiên nguyên nhân.

## 9. 스키마 3계층 (Three-Schema Architecture)

Sau khi đã đặt nền bằng **26. 인터페이스 구현 검증 도구 (Interface Verification Tools)**, ta chuyển sang **9. 스키마 3계층 (Three-Schema Architecture)**. Đây là mắt xích 71/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **9. 스키마 3계층 (Three-Schema Architecture)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **외부 스키마 (External Schema)**, **개념 스키마 (Conceptual Schema)**, **내부 스키마 (Internal Schema)**, **Example** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “9. 스키마 3계층 (Three-Schema Architecture)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* **외부 스키마 (External Schema)**: 사용자나 프로그래머 입장에서 필요한 논리적 구조.
* **개념 스키마 (Conceptual Schema)**: 전체적인 논리적 구조, 개체 간 관계/제약조건, 보안/무결성 규칙.
* **내부 스키마 (Internal Schema)**: 물리적 저장장치 입장에서 본 구조 (레코드 형식, 물리적 순서).
* **VI (Vietnamese) (Tiếng Việt):**
  * External: Góc nhìn của người dùng (User view).
  * Conceptual: Cấu trúc logic tổng thể, quan hệ, bảo mật.
  * Internal: Cấu trúc lưu trữ vật lý.
* **Example**: DB의 전체 테이블 구조는 개념 스키마, 사용자가 보는 뷰(View)는 외부 스키마, 파일 저장 방식은 내부 스키마.
* 💡 **Mẹo ghi nhớ**: Ngoài (Người dùng) - Giữa/Khái niệm (Tổng thể logic) - Trong (Lưu trữ vật lý).

Ta có thể khép mục **9. 스키마 3계층 (Three-Schema Architecture)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **14. 파레토 법칙 (Pareto Principle)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

> **Bàn giao:** Sau **9. 스키마 3계층 (Three-Schema Architecture)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
