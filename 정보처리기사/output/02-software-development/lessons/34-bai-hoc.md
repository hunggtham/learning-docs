# 36. IDE (통합 개발 환경) 및 빌드 도구 (IDE & Build Tools)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **36. IDE (통합 개발 환경) 및 빌드 도구 (IDE & Build Tools)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **36. IDE (통합 개발 환경) 및 빌드 도구 (IDE & Build Tools)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **41. 빌드 자동화 도구 심화: Jenkins vs Gradle** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

IDE

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **10. 빌드 자동화 도구 (Build Automation Tools)**에서 만든 기준을 이어받아 **36. IDE (통합 개발 환경) 및 빌드 도구 (IDE & Build Tools)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **36. IDE (통합 개발 환경) 및 빌드 도구 (IDE & Build Tools)** và nối nó với **41. 빌드 자동화 도구 심화: Jenkins vs Gradle**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 36. IDE (통합 개발 환경) 및 빌드 도구 (IDE & Build Tools)

Ở bước 34/95, **36. IDE (통합 개발 환경) 및 빌드 도구 (IDE & Build Tools)** xuất hiện như phần tiếp nối của **10. 빌드 자동화 도구 (Build Automation Tools)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **36. IDE (통합 개발 환경) 및 빌드 도구 (IDE & Build Tools)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **IDE**, **기능**, **빌드 도구** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

* **IDE**: 코딩, 디버그, 컴파일, 배포 등 모든 작업을 하나의 프로그램에서 처리.
  * **기능**: 코딩(Coding), 컴파일(Compile), 디버깅(Debugging), 배포(Deployment).
* **빌드 도구**: 소스 코드를 실행 가능한 제품 소프트웨어로 변환(Ant, Maven, Gradle).
* **VI (Vietnamese) (Tiếng Việt):** Môi trường phát triển tích hợp (IDE - như Eclipse, VS Code). Chức năng: Code, Dịch, Gỡ lỗi, Triển khai.

Như vậy, **36. IDE (통합 개발 환경) 및 빌드 도구 (IDE & Build Tools)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **41. 빌드 자동화 도구 심화: Jenkins vs Gradle**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.