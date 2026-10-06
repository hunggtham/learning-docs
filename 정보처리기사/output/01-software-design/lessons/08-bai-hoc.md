# 3. 요구사항 분석기법 및 자동화 도구 (Analysis Techniques & CASE)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **3. 요구사항 분석기법 및 자동화 도구 (Analysis Techniques & CASE)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối requirements analysis với technique, automation và CASE, để nhu cầu được biến thành mô hình có thể kiểm chứng.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **3. 요구사항 분석기법 및 자동화 도구 (Analysis Techniques & CASE)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **3. 요구사항 분석기법 및 자동화 도구 (Analysis Techniques & CASE)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **1. 요구사항 개발 기법 (Requirements Elicitation Techniques)** khi chuyển sang phần tiếp theo.

> **Nối mạch:** Trong **3. 요구사항 분석기법 및 자동화 도구 (Analysis Techniques & CASE)**, **핵심 키워드 (Từ khóa)** nối từ **학습 목표 (Mục tiêu)** sang **선행·연결 개념 (Kiến thức liên kết)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 핵심 키워드 (Từ khóa)

요구사항, 분석기법, 자동화, 도구

> **Nối mạch:** Ở chặng này của **3. 요구사항 분석기법 및 자동화 도구 (Analysis Techniques & CASE)**, **핵심 키워드 (Từ khóa)** dẫn sang **선행·연결 개념 (Kiến thức liên kết)**, nơi tài liệu chuẩn và vị trí sở hữu được chỉ rõ để biết chỗ đào sâu tiếp; **읽는 방법 (Cách đọc)** mở rộng hệ quả liên quan.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **2. 요구사항 정의 (Requirements Definition)**에서 만든 기준을 이어받아 **3. 요구사항 분석기법 및 자동화 도구 (Analysis Techniques & CASE)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Nối mạch:** Đặt trong câu hỏi lớn của **3. 요구사항 분석기법 및 자동화 도구 (Analysis Techniques & CASE)**, **읽는 방법 (Cách đọc)** nối từ **선행·연결 개념 (Kiến thức liên kết)** sang **3. 요구사항 분석기법 및 자동화 도구 (Analysis Techniques & CASE)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Nối mạch:** Trong **3. 요구사항 분석기법 및 자동화 도구 (Analysis Techniques & CASE)**, **읽는 방법 (Cách đọc)** nêu quy tắc; **3. 요구사항 분석기법 및 자동화 도구 (Analysis Techniques & CASE)** thử quy tắc trong tình huống, rồi nối sang phần giải thích tiếp theo.

## 3. 요구사항 분석기법 및 자동화 도구 (Analysis Techniques & CASE)

Sau khi đã đặt nền bằng **2. 요구사항 정의 (Requirements Definition)**, ta chuyển sang **3. 요구사항 분석기법 및 자동화 도구 (Analysis Techniques & CASE)**. Đây là mắt xích 8/69 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **3. 요구사항 분석기법 및 자동화 도구 (Analysis Techniques & CASE)** như một bài học cho người mới, hãy giữ câu hỏi: **một nhu cầu nghiệp vụ được chuyển thành yêu cầu có thể kiểm tra và bàn giao như thế nào?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng là bằng chứng để so sánh các lựa chọn theo cùng tiêu chí, không phải danh sách cần học thuộc từng ô. Trong khối này, **자료 흐름도 (DFD - Data Flow Diagram)**, **자료 사전 (DD - Data Dictionary)**, **CASE 도구 (CASE Tools)**, **HIPO (Hierarchical Input Process Output)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “3. 요구사항 분석기법 및 자동화 도구 (Analysis Techniques & CASE)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

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

> **Bàn giao:** Sau **3. 요구사항 분석기법 및 자동화 도구 (Analysis Techniques & CASE)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
