# 핵심 040: 애플리케이션 테스트 원리 및 종류 (Test Principles & Types)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **핵심 040: 애플리케이션 테스트 원리 및 종류 (Test Principles & Types)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **핵심 040: 애플리케이션 테스트 원리 및 종류 (Test Principles & Types)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **핵심 041: 테스트 케이스 / 시나리오 / 오라클 (Test Case/Scenario/Oracle)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

핵심, 애플리케이션, 테스트, 원리, 종류

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **49. 테스트 하네스 구성 요소 (Test Harness Components)**에서 만든 기준을 이어받아 **핵심 040: 애플리케이션 테스트 원리 및 종류 (Test Principles & Types)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 핵심 040: 애플리케이션 테스트 원리 및 종류 (Test Principles & Types)

Sau khi đã đặt nền bằng **49. 테스트 하네스 구성 요소 (Test Harness Components)**, ta chuyển sang **핵심 040: 애플리케이션 테스트 원리 및 종류 (Test Principles & Types)**. Đây là mắt xích 53/95 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **핵심 040: 애플리케이션 테스트 원리 및 종류 (Test Principles & Types)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **테스트의 기본 원리 (Các nguyên lý cơ bản)**. Hãy xác định **테스트의 기본 원리 (Các nguyên lý cơ bản)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 테스트의 기본 원리 (Các nguyên lý cơ bản)

Phần nguồn của **테스트의 기본 원리 (Các nguyên lý cơ bản)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **완벽한 테스팅은 불가능:** Không bao giờ test ra 100% không còn lỗi.
- **결함 집중 (Defect Clustering):** Lỗi thường tập trung ở 20% các module cốt lõi (Quy tắc Pareto 80/20).
- **살충제 패러독스 (Pesticide Paradox):** Nghịch lý thuốc trừ sâu. Dùng mãi một bài test thì không tìm ra lỗi mới. Cần liên tục thay đổi bộ test.
- **정황 의존성 (Context Dependency):** Tùy bối cảnh (web, app, game) mà cách test phải khác nhau.
- **오류-부재의 궤변 (Absence of Errors Fallacy):** App không có lỗi nhưng không đúng ý khách hàng thì vẫn là rác.

Các bullet của **테스트의 기본 원리 (Các nguyên lý cơ bản)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **테스트의 기본 원리 (Các nguyên lý cơ bản)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **정적 테스트 vs 동적 테스트 (Static vs Dynamic Test)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **정적 테스트 vs 동적 테스트 (Static vs Dynamic Test)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 정적 테스트 vs 동적 테스트 (Static vs Dynamic Test)

Các ý ngay dưới **정적 테스트 vs 동적 테스트 (Static vs Dynamic Test)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- **정적 테스트 (Static):** Không chạy code. Đọc và review code/tài liệu. (Walkthrough, Inspection, Review). Phát hiện lỗi sớm, tiết kiệm tiền.
- **동적 테스트 (Dynamic):** Phải chạy chương trình. Gồm Black Box và White Box testing.

- 💡 **Mẹo ghi nhớ (Mnemonics):** Thuốc trừ sâu (Pesticide) = Cần thay mới bộ Test. Đám mây lỗi (Clustering) = 20% code gây ra 80% lỗi.

---

Với **정적 테스트 vs 동적 테스트 (Static vs Dynamic Test)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **정적 테스트 vs 동적 테스트 (Static vs Dynamic Test)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **핵심 040: 애플리케이션 테스트 원리 및 종류 (Test Principles & Types)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **핵심 041: 테스트 케이스 / 시나리오 / 오라클 (Test Case/Scenario/Oracle)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.