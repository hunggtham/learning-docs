# 52. 소스 코드 최적화와 순환 복잡도 (Source Code Optimization & Cyclomatic Complexity)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **52. 소스 코드 최적화와 순환 복잡도 (Source Code Optimization & Cyclomatic Complexity)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **52. 소스 코드 최적화와 순환 복잡도 (Source Code Optimization & Cyclomatic Complexity)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **53. EAI와 ESB 심화 (EAI vs ESB)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

소스, 코드, 최적화와, 순환, 복잡도

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **51. 빅오 표기법 (Big-O Notation) 심화**에서 만든 기준을 이어받아 **52. 소스 코드 최적화와 순환 복잡도 (Source Code Optimization & Cyclomatic Complexity)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 52. 소스 코드 최적화와 순환 복잡도 (Source Code Optimization & Cyclomatic Complexity)

Sau khi đã đặt nền bằng **51. 빅오 표기법 (Big-O Notation) 심화**, ta chuyển sang **52. 소스 코드 최적화와 순환 복잡도 (Source Code Optimization & Cyclomatic Complexity)**. Đây là mắt xích 83/95 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **52. 소스 코드 최적화와 순환 복잡도 (Source Code Optimization & Cyclomatic Complexity)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **소스 코드 최적화**, **순환 복잡도 (McCabe's Cyclomatic Complexity)**, **소스 코드 품질 분석 도구 심화**, **정적 분석 도구** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

* **소스 코드 최적화**: 배제해야 할 '나쁜 코드(Bad Code - 스파게티 코드, 외계인 코드)'와 작성해야 할 '클린 코드(Clean Code - 가독성, 단순성, 의존성 배제, 중복성 최소화, 추상화)'가 있음.
* **순환 복잡도 (McCabe's Cyclomatic Complexity)**: 프로그램 논리의 복잡도를 측정.
  * 계산 방법: `V(G) = 화살표 수(E) - 노드 수(N) + 2` 또는 제어 흐름도의 닫힌 영역 수 + 1.
* **소스 코드 품질 분석 도구 심화**:
  * **정적 분석 도구**: pmd, cppcheck, SonarQube, checkstyle, ccm.
  * **동적 분석 도구**: Avalanche, Valgrind (메모리 누수, 스레드 결함 발견).
* **VI (Vietnamese) (Tiếng Việt):** Tối ưu mã nguồn & Độ phức tạp Cyclomatic (McCabe). 
  * Clean code > Bad code (Spaghetti/Alien).
  * V(G) = Cạnh(E) - Đỉnh(N) + 2. Số V(G) chính là số lượng test case cơ bản cần thiết.
  * Công cụ tĩnh (không chạy code): SonarQube. Động (chạy code tìm rò rỉ bộ nhớ): Valgrind.

Ta có thể khép mục **52. 소스 코드 최적화와 순환 복잡도 (Source Code Optimization & Cyclomatic Complexity)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **53. EAI와 ESB 심화 (EAI vs ESB)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.