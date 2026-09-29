# 핵심 039: 소프트웨어 품질 관련 국제 표준 (Software Quality Standards)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **핵심 039: 소프트웨어 품질 관련 국제 표준 (Software Quality Standards)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **핵심 039: 소프트웨어 품질 관련 국제 표준 (Software Quality Standards)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **핵심 클린 코드 작성 원칙 (Clean Code Principles)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

핵심, 소프트웨어, 품질, 관련, 국제, 표준

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)**에서 만든 기준을 이어받아 **핵심 039: 소프트웨어 품질 관련 국제 표준 (Software Quality Standards)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **핵심 039: 소프트웨어 품질 관련 국제 표준 (Software Quality Standards)** và nối nó với **핵심 클린 코드 작성 원칙 (Clean Code Principles)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 핵심 039: 소프트웨어 품질 관련 국제 표준 (Software Quality Standards)

Sau khi đã đặt nền bằng **핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)**, ta chuyển sang **핵심 039: 소프트웨어 품질 관련 국제 표준 (Software Quality Standards)**. Đây là mắt xích 89/95 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **핵심 039: 소프트웨어 품질 관련 국제 표준 (Software Quality Standards)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **ISO/IEC 9126:** Đánh giá chất lượng phần mềm gồm 6 đặc tính: **기신사효유이**
  - **기**능성 (Functionality): Đáp ứng đúng yêu cầu.
  - **신**뢰성 (Reliability): Chạy ổn định, không lỗi, chịu lỗi tốt.
  - **사**용성 (Usability): Dễ hiểu, dễ học, dễ dùng.
  - **효**율성 (Efficiency): Tốn ít tài nguyên, chạy nhanh.
  - **유**지 보수성 (Maintainability): Dễ sửa chữa, bảo trì, phân tích.
  - **이**식성 (Portability): Dễ cài đặt, dễ chuyển sang môi trường/máy khác.
- **ISO/IEC 14598:** Tiêu chuẩn đánh giá quá trình mua/phát triển.
- **ISO/IEC 12119:** Tiêu chuẩn cho gói phần mềm thương mại.
- **ISO/IEC 25000 (SQuaRE):** Tích hợp tất cả các tiêu chuẩn 9126, 14598, 12119.

- **Vietnamese Explanation:** ISO 9126 là kinh điển nhất, bạn phải nhớ 6 chữ cái đầu của 6 đặc tính. Nếu phần mềm khó dùng => Kém "Sử dụng tính". Nếu đổi máy tính mà không chạy được => Kém "Di thực tính" (Portability).
- 💡 **Mẹo ghi nhớ (Mnemonics):** 6 Đặc tính của 9126: "Chức Tín Dùng Hiệu Bảo Di" (Chức năng - Đáng tin - Dễ dùng - Hiệu quả - Bảo trì - Di động). ISO 25000 = Chuẩn xịn nhất tổng hợp tất cả.

---

Ta có thể khép mục **핵심 039: 소프트웨어 품질 관련 국제 표준 (Software Quality Standards)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **핵심 클린 코드 작성 원칙 (Clean Code Principles)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.