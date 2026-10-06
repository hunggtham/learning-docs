# 6. 구조적 분석 도구 (Structured Analysis Tools)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **6. 구조적 분석 도구 (Structured Analysis Tools)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối structured analysis với data flow, process và decomposition, để yêu cầu được tách thành mô hình kiểm chứng.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **6. 구조적 분석 도구 (Structured Analysis Tools)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **6. 구조적 분석 도구 (Structured Analysis Tools)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **10. 소프트웨어 설계 원리 (Software Design Principles)** khi chuyển sang phần tiếp theo.

> **Nối mạch:** Trong **6. 구조적 분석 도구 (Structured Analysis Tools)**, **핵심 키워드 (Từ khóa)** nối từ **학습 목표 (Mục tiêu)** sang **선행·연결 개념 (Kiến thức liên kết)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 핵심 키워드 (Từ khóa)

구조적, 분석, 도구

> **Nối mạch:** Ở chặng này của **6. 구조적 분석 도구 (Structured Analysis Tools)**, **핵심 키워드 (Từ khóa)** dẫn sang **선행·연결 개념 (Kiến thức liên kết)**, nơi tài liệu chuẩn và vị trí sở hữu được chỉ rõ để biết chỗ đào sâu tiếp; **읽는 방법 (Cách đọc)** mở rộng hệ quả liên quan.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **4. 운영 환경 구축 고려사항 (Operation Environment Considerations)**에서 만든 기준을 이어받아 **6. 구조적 분석 도구 (Structured Analysis Tools)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Nối mạch:** Đặt trong câu hỏi lớn của **6. 구조적 분석 도구 (Structured Analysis Tools)**, **읽는 방법 (Cách đọc)** nối từ **선행·연결 개념 (Kiến thức liên kết)** sang **6. 구조적 분석 도구 (Structured Analysis Tools)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Nối mạch:** Trong **6. 구조적 분석 도구 (Structured Analysis Tools)**, **6. 구조적 분석 도구 (Structured Analysis Tools)** nối từ **읽는 방법 (Cách đọc)** sang phần giải thích tiếp theo, vì phần trước cung cấp điểm tựa cho chủ đề này.

## 6. 구조적 분석 도구 (Structured Analysis Tools)

Sau khi đã đặt nền bằng **4. 운영 환경 구축 고려사항 (Operation Environment Considerations)**, ta chuyển sang **6. 구조적 분석 도구 (Structured Analysis Tools)**. Đây là mắt xích 62/69 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **6. 구조적 분석 도구 (Structured Analysis Tools)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng là bằng chứng để so sánh các lựa chọn theo cùng tiêu chí, không phải danh sách cần học thuộc từng ô. Trong khối này, **DFD (Biểu đồ luồng dữ liệu)**, **DD (Từ điển dữ liệu)**, **HIPO** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “6. 구조적 분석 도구 (Structured Analysis Tools)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

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

> **Bàn giao:** Sau **6. 구조적 분석 도구 (Structured Analysis Tools)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
