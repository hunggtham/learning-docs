# 소프트웨어 공학 (Software Engineering)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **소프트웨어 공학 (Software Engineering)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **소프트웨어 공학 (Software Engineering)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **071. 보안 취약성 식별 (Security Vulnerability Identification / Lỗ hổng bảo mật)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

소프트웨어, 공학

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **가상기억장치 및 페이지 교체 (Virtual Memory & Page Replacement)**에서 만든 기준을 이어받아 **소프트웨어 공학 (Software Engineering)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **소프트웨어 공학 (Software Engineering)** và nối nó với **071. 보안 취약성 식별 (Security Vulnerability Identification / Lỗ hổng bảo mật)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 소프트웨어 공학 (Software Engineering)

Sau khi đã đặt nền bằng **가상기억장치 및 페이지 교체 (Virtual Memory & Page Replacement)**, ta chuyển sang **소프트웨어 공학 (Software Engineering)**. Đây là mắt xích 56/78 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **소프트웨어 공학 (Software Engineering)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **모듈화 (Modularity)**, **재사용성 (Reusability)**, **확장성 (Extensibility)**, **제어 반전 (Inversion of Control, IoC)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

---

- **모듈화 (Modularity)**: 캡슐화로 영향 최소화, 유지보수 용이.
- **재사용성 (Reusability)**: 반복 모듈 제공으로 생산성/품질 향상.
- **확장성 (Extensibility)**: 다형성 통한 인터페이스 확장.
- **제어 반전 (Inversion of Control, IoC)**: 프레임워크가 흐름을 제어하고 사용자(외부) 코드를 호출.

**Giải thích (Vietnamese):**
Framework (như Spring, Django) là một bộ khung có sẵn. Tính năng đặc biệt nhất của Framework là IoC (Đảo ngược quyền điều khiển): Thay vì bạn tự gọi thư viện (Library), thì Framework sẽ là người gọi code của bạn!

---

Ta có thể khép mục **소프트웨어 공학 (Software Engineering)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **071. 보안 취약성 식별 (Security Vulnerability Identification / Lỗ hổng bảo mật)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.