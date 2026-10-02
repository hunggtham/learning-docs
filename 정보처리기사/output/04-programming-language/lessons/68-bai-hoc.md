# 210. CASE (Computer-Aided Software Engineering)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **210. CASE (Computer-Aided Software Engineering)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Hãy nối yêu cầu, mô hình hóa, sinh mã và kiểm thử với vai trò CASE trong việc giảm công việc thủ công.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **210. CASE (Computer-Aided Software Engineering)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **210. CASE (Computer-Aided Software Engineering)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **070. 서버개발 프레임워크 (Server Development Framework)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **210. CASE (Computer-Aided Software Engineering)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

CASE

> **Chuyển mạch:** Ở chặng này của **210. CASE (Computer-Aided Software Engineering)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **209. 소프트웨어 재공학 (Software Reengineering / Tái cấu trúc phần mềm)**에서 만든 기준을 이어받아 **210. CASE (Computer-Aided Software Engineering)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **210. CASE (Computer-Aided Software Engineering)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **210. CASE (Computer-Aided Software Engineering)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **210. CASE (Computer-Aided Software Engineering)**, **읽는 방법 (Cách đọc)** cho ta quy tắc; **210. CASE (Computer-Aided Software Engineering)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 210. CASE (Computer-Aided Software Engineering)

Sau khi đã đặt nền bằng **209. 소프트웨어 재공학 (Software Reengineering / Tái cấu trúc phần mềm)**, ta chuyển sang **210. CASE (Computer-Aided Software Engineering)**. Đây là mắt xích 68/91 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **210. CASE (Computer-Aided Software Engineering)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **CASE 정보 저장소 (Repository)**, **분류** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “210. CASE (Computer-Aided Software Engineering)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 소프트웨어 생명주기 전체 또는 일부를 **자동화하는 소프트웨어 도구**.
- 개발 기간 단축, 비용 절감, 품질 및 생산성 향상. 개발 주기의 표준화.
- **CASE 정보 저장소 (Repository)**: 개발 중 모아진 정보 보관 (현재의 Database 역할). 일관성 유지.
- **분류**:
  - 상위 (Upper) CASE: 요구 분석, 설계 단계 지원.
  - 하위 (Lower) CASE: 코드 작성, 테스트 지원.
  - 통합 (Integrated) CASE: 전체 과정 지원.

**Giải thích (Vietnamese):**
CASE là các phần mềm hỗ trợ kỹ sư làm phần mềm. Giống như Excel giúp kế toán tính toán nhanh hơn, CASE (như StarUML, Jira, Eclipse) giúp lập trình viên vẽ biểu đồ, quản lý task, sinh code tự động.

---

# 4과목 프로그래밍 언어 활용 (Phần 4: Ứng dụng ngôn ngữ lập trình)

Ta có thể khép mục **210. CASE (Computer-Aided Software Engineering)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **070. 서버개발 프레임워크 (Server Development Framework)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

> **Bàn giao:** Sau **210. CASE (Computer-Aided Software Engineering)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
