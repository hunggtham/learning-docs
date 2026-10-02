# 라이브러리 및 예외 처리 (Libraries and Exception Handling)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **라이브러리 및 예외 처리 (Libraries and Exception Handling)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Hãy phân biệt thư viện cung cấp hành vi có sẵn với exception biểu diễn đường lỗi, rồi nối chúng vào cách phục hồi của chương trình.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **라이브러리 및 예외 처리 (Libraries and Exception Handling)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **라이브러리 및 예외 처리 (Libraries and Exception Handling)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **운영체제 (OS: Operating System) 기초** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **라이브러리 및 예외 처리 (Libraries and Exception Handling)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

라이브러리, 예외, 처리

> **Chuyển mạch:** Ở chặng này của **라이브러리 및 예외 처리 (Libraries and Exception Handling)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **프로그래밍 언어의 분류 (Classification of Programming Languages)**에서 만든 기준을 이어받아 **라이브러리 및 예외 처리 (Libraries and Exception Handling)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **라이브러리 및 예외 처리 (Libraries and Exception Handling)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **라이브러리 및 예외 처리 (Libraries and Exception Handling)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **라이브러리 및 예외 처리 (Libraries and Exception Handling)**, **라이브러리 및 예외 처리 (Libraries and Exception Handling)** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 라이브러리 및 예외 처리 (Libraries and Exception Handling)

Ở bước 55/86, **라이브러리 및 예외 처리 (Libraries and Exception Handling)** xuất hiện như phần tiếp nối của **프로그래밍 언어의 분류 (Classification of Programming Languages)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **라이브러리 및 예외 처리 (Libraries and Exception Handling)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **1. 라이브러리 (Library)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **1. 라이브러리 (Library)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 1. 라이브러리 (Library)

Bây giờ ta đi vào nội dung của **1. 라이브러리 (Library)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “1. 라이브러리 (Library)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 자주 사용하는 함수나 데이터들을 미리 만들어 모아 놓은 집합체 (표준 라이브러리, 외부 라이브러리).
- **C언어 대표 표준 라이브러리**:
  - `stdio.h`: 입출력 (`printf`, `scanf`)
  - `math.h`: 수학 함수 (`sqrt`, `pow`)
  - `string.h`: 문자열 처리 (`strlen`, `strcpy`)
  - `stdlib.h`: 자료형 변환, 메모리 할당, 난수 (`atoi`, `malloc`, `rand`)
  - `time.h`: 시간 처리 (`time`)

Các bullet của **1. 라이브러리 (Library)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **1. 라이브러리 (Library)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. 예외 처리 (Exception Handling)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **2. 예외 처리 (Exception Handling)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 2. 예외 처리 (Exception Handling)

Phần nguồn của **2. 예외 처리 (Exception Handling)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “2. 예외 처리 (Exception Handling)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 프로그램의 정상적인 실행을 방해하는 조건이나 상태를 예외(Exception)라고 합니다.
- 예외 발생 시 비정상 종료를 막고 대비해 놓은 처리 루틴을 수행하는 것을 의미합니다.

> **Vietnamese Explanation**:
> Thư viện (Library) là nơi chứa các hàm viết sẵn để bạn gọi ra dùng (ví dụ nhập xuất, toán học). Xử lý ngoại lệ (Exception Handling) là việc bắt các lỗi có thể xảy ra trong lúc chạy (như chia cho 0, mất kết nối) để chương trình không bị sập ngang.

Các ý về **2. 예외 처리 (Exception Handling)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Điểm chốt của **2. 예외 처리 (Exception Handling)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Như vậy, **라이브러리 및 예외 처리 (Libraries and Exception Handling)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **운영체제 (OS: Operating System) 기초**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

> **Bàn giao:** Sau **라이브러리 및 예외 처리 (Libraries and Exception Handling)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
