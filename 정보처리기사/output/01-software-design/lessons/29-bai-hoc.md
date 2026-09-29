# 15. 객체지향 및 모듈화 방법론 (Phương pháp luận OOP & Mô-đun hóa)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **15. 객체지향 및 모듈화 방법론 (Phương pháp luận OOP & Mô-đun hóa)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **15. 객체지향 및 모듈화 방법론 (Phương pháp luận OOP & Mô-đun hóa)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **2. 객체지향 (OOP - Object Oriented Programming)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

객체지향, 모듈화, 방법론

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **14. 객체지향 심화 (OOP chuyên sâu)**에서 만든 기준을 이어받아 **15. 객체지향 및 모듈화 방법론 (Phương pháp luận OOP & Mô-đun hóa)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **15. 객체지향 및 모듈화 방법론 (Phương pháp luận OOP & Mô-đun hóa)** và nối nó với **2. 객체지향 (OOP - Object Oriented Programming)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 15. 객체지향 및 모듈화 방법론 (Phương pháp luận OOP & Mô-đun hóa)

Sau khi đã đặt nền bằng **14. 객체지향 심화 (OOP chuyên sâu)**, ta chuyển sang **15. 객체지향 및 모듈화 방법론 (Phương pháp luận OOP & Mô-đun hóa)**. Đây là mắt xích 29/57 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **15. 객체지향 및 모듈화 방법론 (Phương pháp luận OOP & Mô-đun hóa)** như một bài học cho người mới, hãy giữ câu hỏi: **một dự án đi qua những giai đoạn nào, mỗi mô hình phân bổ công việc và rủi ro ra sao?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **객체지향 분석 방법론 종류 (Các phương pháp phân tích OOP)**. Hãy xác định **객체지향 분석 방법론 종류 (Các phương pháp phân tích OOP)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 객체지향 분석 방법론 종류 (Các phương pháp phân tích OOP)

Phần nguồn của **객체지향 분석 방법론 종류 (Các phương pháp phân tích OOP)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **Rumbaugh (럼바우):** 객체(Object), 동적(Dynamic), 기능(Functional) 모델로 나누어 분석. (Chia làm 3 mô hình).
- **Booch (부치):** 미시적(Micro) 개발과 거시적(Macro) 개발 프로세스 모두 사용. (Dùng cả quy trình vĩ mô và vi mô).
- **Jacobson (제이콥슨):** Use Case(유스케이스)를 강조. (Nhấn mạnh vào Use Case).
- **Coad와 Yourdon:** E-R 다이어그램 사용. (Dùng sơ đồ ER).
- **Wirfs-Brock:** 분석과 설계 간 구분이 없고 연속적으로 수행. (Không phân biệt rõ phân tích và thiết kế, làm liên tục).
- 💡 **Mẹo ghi nhớ (Mnemonic):** R-O, B-M, J-U, C-E, W-L -> **Ra Ôm Bạn Mới, Giữ Út, Cho Em Vui Lây** (Rumbaugh-Object, Booch-Micro, Jacobson-Use case, Coad-ER, Wirfs-Liên tục).

Các bullet của **객체지향 분석 방법론 종류 (Các phương pháp phân tích OOP)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **객체지향 분석 방법론 종류 (Các phương pháp phân tích OOP)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **공통 모듈 명세 기법 (Kỹ thuật đặc tả Module chung)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **공통 모듈 명세 기법 (Kỹ thuật đặc tả Module chung)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 공통 모듈 명세 기법 (Kỹ thuật đặc tả Module chung)

Các ý ngay dưới **공통 모듈 명세 기법 (Kỹ thuật đặc tả Module chung)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- **정확성 (Correctness):** 기능이 필요하다는 것을 알 수 있도록 정확히 작성. (Chính xác, biết rõ cần thiết).
- **명확성 (Clarity):** 중의적으로 해석되지 않도록 명확하게. (Rõ ràng, không hiểu 2 nghĩa).
- **완전성 (Completeness):** 구현에 필요한 모든 것을 기술. (Đầy đủ mọi thứ cần thiết).
- **일관성 (Consistency):** 기능들 간 상호 충돌이 발생하지 않도록. (Nhất quán, không xung đột).
- **추적성 (Traceability):** 요구사항 출처, 관련 시스템 등 관계 파악. (Có thể truy xuất nguồn gốc).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **CMHNT** (Chính - Minh - Hoàn - Nhất - Truy): **Chỉ Mong Học Nhất Trường**.

Các bullet của **공통 모듈 명세 기법 (Kỹ thuật đặc tả Module chung)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **공통 모듈 명세 기법 (Kỹ thuật đặc tả Module chung)**, đừng bắt đầu lại từ số không. **코드(Code)의 주요 기능 (Chức năng chính của Code)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **코드(Code)의 주요 기능 (Chức năng chính của Code)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 코드(Code)의 주요 기능 (Chức năng chính của Code)

Bây giờ ta đi vào nội dung của **코드(Code)의 주요 기능 (Chức năng chính của Code)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 식별 기능 (Nhận diện), 분류 기능 (Phân loại), 배열 기능 (Sắp xếp), 표준화 기능 (Chuẩn hóa), 간소화 기능 (Đơn giản hóa).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **TPBTG** (Thức - Phân - Bài - Tiêu - Giản): **Thích Phá Bài Thì Giảm**.

Các bullet của **코드(Code)의 주요 기능 (Chức năng chính của Code)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**코드(Code)의 주요 기능 (Chức năng chính của Code)** vừa cho ta cách đặt câu hỏi. Bây giờ **코드의 종류 심화 (Các loại Code chi tiết)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Với **코드의 종류 심화 (Các loại Code chi tiết)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 코드의 종류 심화 (Các loại Code chi tiết)

Phần nguồn của **코드의 종류 심화 (Các loại Code chi tiết)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **순차 코드 (Sequence Code):** 1, 2, 3... (Theo thứ tự).
- **블록 코드 (Block Code):** 공통성 있는 것끼리 블록으로 구분 (1000~1100: Phòng Nhân sự, 1101~1200: Phòng IT).
- **10진 코드 (Decimal Code):** 0~9 분할 반복 (Ví dụ: Mã phân loại sách thư viện Dewey).
- **그룹 분류 코드 (Group Classification):** 대/중/소 분류 (1-01-001).
- **연상 코드 (Mnemonic Code):** 명칭/약호와 관계있는 문자/숫자 (TV-40). (Gợi nhớ).
- **표의 숫자 코드 (Significant Digit):** 물리적 수치 적용 (120-720).
- **합성 코드 (Combined Code):** 2개 이상 코드 조합 (KE-711).

Các ý về **코드의 종류 심화 (Các loại Code chi tiết)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Với **코드의 종류 심화 (Các loại Code chi tiết)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Ta có thể khép mục **15. 객체지향 및 모듈화 방법론 (Phương pháp luận OOP & Mô-đun hóa)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **2. 객체지향 (OOP - Object Oriented Programming)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.