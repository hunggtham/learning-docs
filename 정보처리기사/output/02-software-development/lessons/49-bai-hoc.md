# 46. 애플리케이션 테스트 프로세스 (Test Process)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **46. 애플리케이션 테스트 프로세스 (Test Process)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **46. 애플리케이션 테스트 프로세스 (Test Process)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **47. 테스트 오라클의 종류 (Types of Test Oracles)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

애플리케이션, 테스트, 프로세스

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **45. V-모델 (V-Model) 기반 애플리케이션 테스트 단계**에서 만든 기준을 이어받아 **46. 애플리케이션 테스트 프로세스 (Test Process)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **46. 애플리케이션 테스트 프로세스 (Test Process)** và nối nó với **47. 테스트 오라클의 종류 (Types of Test Oracles)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 46. 애플리케이션 테스트 프로세스 (Test Process)

Ở bước 49/95, **46. 애플리케이션 테스트 프로세스 (Test Process)** xuất hiện như phần tiếp nối của **45. V-모델 (V-Model) 기반 애플리케이션 테스트 단계**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **46. 애플리케이션 테스트 프로세스 (Test Process)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **순서**, **결함 (Fault/Defect)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

* **순서**: 계획(Plan) → 분석 및 디자인(Analysis & Design) → 케이스 및 시나리오 작성 → 수행(Execution) → 결과 평가 및 리포팅 → 결함 추적 및 관리.
* **결함 (Fault/Defect)**: 설계와 다르게 동작하거나 예상 결과와 일치하지 않는 부분.
* **VI (Vietnamese) (Tiếng Việt):** Quy trình kiểm thử: Lập kế hoạch -> Phân tích -> Viết kịch bản -> Chạy -> Đánh giá -> Theo dõi lỗi (Defect Tracking). Lỗi (Defect) là sự sai lệch giữa kết quả thực tế và mong đợi.

Như vậy, **46. 애플리케이션 테스트 프로세스 (Test Process)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **47. 테스트 오라클의 종류 (Types of Test Oracles)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.