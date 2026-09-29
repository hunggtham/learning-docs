# 16. 소프트웨어 테스트 단계 (Software Testing Phases)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **16. 소프트웨어 테스트 단계 (Software Testing Phases)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **16. 소프트웨어 테스트 단계 (Software Testing Phases)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **17. 테스트 오라클 및 테스트 도구 (Test Oracle & Tools)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

소프트웨어, 테스트, 단계

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **15. 화이트박스 vs 블랙박스 테스트 (White-box vs Black-box Testing)**에서 만든 기준을 이어받아 **16. 소프트웨어 테스트 단계 (Software Testing Phases)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **16. 소프트웨어 테스트 단계 (Software Testing Phases)** và nối nó với **17. 테스트 오라클 및 테스트 도구 (Test Oracle & Tools)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 16. 소프트웨어 테스트 단계 (Software Testing Phases)

Sau khi đã đặt nền bằng **15. 화이트박스 vs 블랙박스 테스트 (White-box vs Black-box Testing)**, ta chuyển sang **16. 소프트웨어 테스트 단계 (Software Testing Phases)**. Đây là mắt xích 53/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **16. 소프트웨어 테스트 단계 (Software Testing Phases)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **단위 테스트 (Unit Test)**, **통합 테스트 (Integration Test)**, **인수 테스트 (Acceptance Test)**, **알파 테스트** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “16. 소프트웨어 테스트 단계 (Software Testing Phases)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* **단위 테스트 (Unit Test)**: 코딩 직후 최소 단위인 모듈/컴포넌트 테스트. (알고리즘 오류, 탈출구 없는 반복문 등 발견).
* **통합 테스트 (Integration Test)**:
  * 하향식 (Top-down): 상위에서 하위로 (스텁/Stub 사용).
  * 상향식 (Bottom-up): 하위에서 상위로 (드라이버/Driver 사용).
* **인수 테스트 (Acceptance Test)**: 사용자가 시스템을 수락하기 전 수행.
  * **알파 테스트**: 개발자 앞에서 사용자가 수행.
  * **베타 테스트 (Field Testing)**: 최종 사용자가 실제 환경에서 여러 사용자 앞에서 수행.
* **VI (Vietnamese) (Tiếng Việt):**
  * Unit Test: Kiểm thử từng module nhỏ (tìm lỗi thuật toán, lặp vô hạn).
  * Integration Test: Kiểm thử tích hợp. Top-down (từ trên xuống), Bottom-up (từ dưới lên).
  * Acceptance Test: Kiểm thử chấp nhận. Alpha (cùng dev), Beta (không có dev, real-world).
* **Example**: 게임 개발 후 회사 내부에서 해보는 것이 알파 테스트, 유저들에게 먼저 공개하는 것이 오픈 베타 테스트입니다.
* 💡 **Mẹo ghi nhớ**: Alpha = có người tạo ra (Dev) giám sát. Beta = thả ra tự nhiên cho User.

Ta có thể khép mục **16. 소프트웨어 테스트 단계 (Software Testing Phases)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **17. 테스트 오라클 및 테스트 도구 (Test Oracle & Tools)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.