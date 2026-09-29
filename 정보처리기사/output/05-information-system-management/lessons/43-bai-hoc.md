# 소프트웨어 재사용 및 재공학 활동 (Software Reuse & Reengineering Activities)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **소프트웨어 재사용 및 재공학 활동 (Software Reuse & Reengineering Activities)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **소프트웨어 재사용 및 재공학 활동 (Software Reuse & Reengineering Activities)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **CASE (Computer Aided Software Engineering)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

소프트웨어, 재사용, 재공학, 활동

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **5과목 정보시스템 구축 관리 (Information System Construction Management)**에서 만든 기준을 이어받아 **소프트웨어 재사용 및 재공학 활동 (Software Reuse & Reengineering Activities)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **소프트웨어 재사용 및 재공학 활동 (Software Reuse & Reengineering Activities)** và nối nó với **CASE (Computer Aided Software Engineering)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 소프트웨어 재사용 및 재공학 활동 (Software Reuse & Reengineering Activities)

Ở bước 43/61, **소프트웨어 재사용 및 재공학 활동 (Software Reuse & Reengineering Activities)** xuất hiện như phần tiếp nối của **5과목 정보시스템 구축 관리 (Information System Construction Management)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **소프트웨어 재사용 및 재공학 활동 (Software Reuse & Reengineering Activities)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **합성 중심 (Composition-Based)**, **생성 중심 (Generation-Based)**, **분석 (Analysis)**, **재구성 (Restructuring)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **1. 재사용 방법 (Reuse Methods)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **1. 재사용 방법 (Reuse Methods)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 1. 재사용 방법 (Reuse Methods)

Bây giờ ta đi vào nội dung của **1. 재사용 방법 (Reuse Methods)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- **합성 중심 (Composition-Based)**: 소프트웨어 부품(블록)을 만들어 끼워 맞추어 완성시키는 방법. (블록 구성 방법)
- **생성 중심 (Generation-Based)**: 추상화 형태의 명세를 구체화하여 프로그램을 만드는 방법. (패턴 구성 방법)

Các bullet của **1. 재사용 방법 (Reuse Methods)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **1. 재사용 방법 (Reuse Methods)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. 재공학 주요 활동 (Reengineering Activities)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **2. 재공학 주요 활동 (Reengineering Activities)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 2. 재공학 주요 활동 (Reengineering Activities)

Phần nguồn của **2. 재공학 주요 활동 (Reengineering Activities)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

기존 시스템을 개선하고 유지보수성을 높이는 활동입니다.
- **분석 (Analysis)**: 기존 명세서를 확인해 동작을 이해하고 대상을 선정.
- **재구성 (Restructuring)**: 외적인 동작은 유지하면서 코드 구조를 향상.
- **역공학 (Reverse Engineering)**: 기존 코드를 분석해 설계 정보나 구성 요소를 다시 추출(도출)해 내는 활동.
- **이식 (Migration)**: 다른 운영체제나 하드웨어 환경에서 사용할 수 있도록 변환.

Các bullet của **2. 재공학 주요 활동 (Reengineering Activities)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **2. 재공학 주요 활동 (Reengineering Activities)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Như vậy, **소프트웨어 재사용 및 재공학 활동 (Software Reuse & Reengineering Activities)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **CASE (Computer Aided Software Engineering)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.