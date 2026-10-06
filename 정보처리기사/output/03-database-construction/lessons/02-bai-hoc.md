# 102. 논리적 설계 (Logical Design / Data Modeling)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **102. 논리적 설계 (Logical Design / Data Modeling)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối logical design với entities, relationships và normalization, để mô hình dữ liệu phản ánh quy tắc nghiệp vụ trước khi chọn storage.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **102. 논리적 설계 (Logical Design / Data Modeling)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **102. 논리적 설계 (Logical Design / Data Modeling)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **103. 물리적 설계 (Physical Design)** khi chuyển sang phần tiếp theo.

> **Nối mạch:** Trong **102. 논리적 설계 (Logical Design / Data Modeling)**, **핵심 키워드 (Từ khóa)** nối từ **학습 목표 (Mục tiêu)** sang **선행·연결 개념 (Kiến thức liên kết)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 핵심 키워드 (Từ khóa)

논리적, 설계

> **Nối mạch:** Ở chặng này của **102. 논리적 설계 (Logical Design / Data Modeling)**, **핵심 키워드 (Từ khóa)** dẫn sang **선행·연결 개념 (Kiến thức liên kết)**, nơi tài liệu chuẩn và vị trí sở hữu được chỉ rõ để biết chỗ đào sâu tiếp; **읽는 방법 (Cách đọc)** mở rộng hệ quả liên quan.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **101. 개념적 설계 (Conceptual Design)**에서 만든 기준을 이어받아 **102. 논리적 설계 (Logical Design / Data Modeling)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Nối mạch:** Đặt trong câu hỏi lớn của **102. 논리적 설계 (Logical Design / Data Modeling)**, **읽는 방법 (Cách đọc)** nối từ **선행·연결 개념 (Kiến thức liên kết)** sang **102. 논리적 설계 (Logical Design / Data Modeling)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Nối mạch:** Trong **102. 논리적 설계 (Logical Design / Data Modeling)**, **102. 논리적 설계 (Logical Design / Data Modeling)** nối từ **읽는 방법 (Cách đọc)** sang phần giải thích tiếp theo, vì phần trước cung cấp điểm tựa cho chủ đề này.

## 102. 논리적 설계 (Logical Design / Data Modeling)

Sau khi đã đặt nền bằng **101. 개념적 설계 (Conceptual Design)**, ta chuyển sang **102. 논리적 설계 (Logical Design / Data Modeling)**. Đây là mắt xích 2/54 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **102. 논리적 설계 (Logical Design / Data Modeling)** như một bài học cho người mới, hãy giữ câu hỏi: **ta dùng mô hình nào để biểu diễn đối tượng, quan hệ hoặc hành vi, và giới hạn của mỗi cách là gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “102. 논리적 설계 (Logical Design / Data Modeling)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 자료를 특정 DBMS가 지원하는 논리적 자료 구조로 변환(mapping)시키는 과정이다.
- **VI (Vietnamese) (Tiếng Việt):** Thiết kế logic (Mô hình hóa dữ liệu). Quá trình chuyển đổi (ánh xạ) dữ liệu thành cấu trúc dữ liệu logic được hỗ trợ bởi một DBMS cụ thể.
- **Example (Korean/Vietnamese):** E-R 다이어그램을 관계형 데이터베이스의 테이블 구조로 변환하는 것. / Chuyển đổi sơ đồ E-R thành cấu trúc bảng của cơ sở dữ liệu quan hệ.
- 💡 **Mẹo ghi nhớ:** Logic-Bảng (Thiết kế Logic = Chuyển đổi sang Bảng).

Ta có thể khép mục **102. 논리적 설계 (Logical Design / Data Modeling)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **103. 물리적 설계 (Physical Design)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

> **Bàn giao:** Sau **102. 논리적 설계 (Logical Design / Data Modeling)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
