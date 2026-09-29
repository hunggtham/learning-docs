# 7. 설계 도구 및 모듈화 심화 (Công cụ thiết kế & Mô-đun hóa chuyên sâu)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **7. 설계 도구 및 모듈화 심화 (Công cụ thiết kế & Mô-đun hóa chuyên sâu)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **7. 설계 도구 및 모듈화 심화 (Công cụ thiết kế & Mô-đun hóa chuyên sâu)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **3. 모듈 (Module)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

설계, 도구, 모듈화, 심화

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **1. 객체지향 설계 5대 원칙 (SOLID)**에서 만든 기준을 이어받아 **7. 설계 도구 및 모듈화 심화 (Công cụ thiết kế & Mô-đun hóa chuyên sâu)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **7. 설계 도구 및 모듈화 심화 (Công cụ thiết kế & Mô-đun hóa chuyên sâu)** và nối nó với **3. 모듈 (Module)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 7. 설계 도구 및 모듈화 심화 (Công cụ thiết kế & Mô-đun hóa chuyên sâu)

Sau khi đã đặt nền bằng **1. 객체지향 설계 5대 원칙 (SOLID)**, ta chuyển sang **7. 설계 도구 및 모듈화 심화 (Công cụ thiết kế & Mô-đun hóa chuyên sâu)**. Đây là mắt xích 32/57 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **7. 설계 도구 및 모듈화 심화 (Công cụ thiết kế & Mô-đun hóa chuyên sâu)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **NS 차트 (Nassi-Shneiderman Chart)**. Hãy xác định **NS 차트 (Nassi-Shneiderman Chart)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### NS 차트 (Nassi-Shneiderman Chart)

Phần nguồn của **NS 차트 (Nassi-Shneiderman Chart)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- 논리의 기술에 중점을 둔 도형을 이용한 표현 방법이다. (Là phương pháp biểu diễn bằng hình khối, trọng tâm vào việc mô tả logic.)
- 연속, 선택 및 다중 선택, 반복 등의 제어 논리 구조를 표현한다. (Thể hiện cấu trúc logic điều khiển như tuần tự, lựa chọn (if-else), đa lựa chọn (switch), lặp lại (while/for).)
- GOTO나 화살표를 사용하지 않는다. (Không sử dụng lệnh GOTO hay mũi tên.)
- 시각적으로 명확히 식별하는 데 적합하다. (Thích hợp để nhận diện rõ ràng về mặt thị giác.)
- 이해하기 쉽고, 코드 변환이 용이하다. (Dễ hiểu và dễ chuyển đổi thành code.)
- **Ví dụ (Example):** Dùng các khối hình chữ nhật xếp chồng lên nhau để biểu diễn một hàm tính toán thay vì dùng sơ đồ khối (Flowchart) có mũi tên rườm rà.

Các ý về **NS 차트 (Nassi-Shneiderman Chart)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **NS 차트 (Nassi-Shneiderman Chart)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **재사용 (Reuse / Tái sử dụng)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **재사용 (Reuse / Tái sử dụng)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 재사용 (Reuse / Tái sử dụng)

Các ý ngay dưới **재사용 (Reuse / Tái sử dụng)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- 이미 개발된 기능을 새로운 시스템이나 기능 개발에 사용할 수 있는 정도를 의미한다. (Mức độ có thể sử dụng lại các chức năng đã phát triển cho hệ thống hoặc chức năng mới.)
- 재사용 규모에 따른 분류: 함수와 객체, 컴포넌트, 애플리케이션. (Phân loại theo quy mô: Hàm/Đối tượng, Component, Ứng dụng).

Các bullet của **재사용 (Reuse / Tái sử dụng)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **재사용 (Reuse / Tái sử dụng)**, đừng bắt đầu lại từ số không. **효과적인 모듈 설계 방안 (Phương án thiết kế module hiệu quả)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **효과적인 모듈 설계 방안 (Phương án thiết kế module hiệu quả)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 효과적인 모듈 설계 방안 (Phương án thiết kế module hiệu quả)

Bây giờ ta đi vào nội dung của **효과적인 모듈 설계 방안 (Phương án thiết kế module hiệu quả)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 결합도는 줄이고 응집도는 높인다. (Giảm độ kết dính (Coupling) và tăng độ gắn kết (Cohesion).)
- 복잡도와 중복성을 줄인다. (Giảm độ phức tạp và sự trùng lặp.)
- 일관성을 유지시킨다. (Duy trì tính nhất quán.)
- 모듈의 기능은 지나치게 제한적이어서는 안 된다. (Chức năng của module không nên quá hạn hẹp.)
- 유지보수가 용이해야 한다. (Phải dễ dàng bảo trì.)
- 💡 **Mẹo ghi nhớ (Mnemonic):** **CUTK** (Cao Ứng - Thấp Kết): **Cứ Ứng Thật Kỹ** -> 응집도 높게(Cohesion High), 결합도 낮게(Coupling Low).

Các bullet của **효과적인 모듈 설계 방안 (Phương án thiết kế module hiệu quả)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**효과적인 모듈 설계 방안 (Phương án thiết kế module hiệu quả)** vừa cho ta cách đặt câu hỏi. Bây giờ **주요 코드 (Các loại Code cơ bản)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Với **주요 코드 (Các loại Code cơ bản)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 주요 코드 (Các loại Code cơ bản)

Phần nguồn của **주요 코드 (Các loại Code cơ bản)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- 순차 코드 (Sequence Code): 일정 기준에 따라서 차례로 일련번호를 부여하는 방법. (Gắn số thứ tự liên tiếp theo một tiêu chuẩn định sẵn - VD: 001, 002, 003).
- 표의 숫자 코드 (Significant Digit Code): 코드화 대상 항목의 중량, 면적, 용량 등의 물리적 수치를 적용시키는 방법. (Sử dụng trực tiếp các chỉ số vật lý như trọng lượng, kích thước vào mã - VD: Tivi 50 inch thì mã là TV-50).

Các bullet của **주요 코드 (Các loại Code cơ bản)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Với **주요 코드 (Các loại Code cơ bản)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Ta có thể khép mục **7. 설계 도구 및 모듈화 심화 (Công cụ thiết kế & Mô-đun hóa chuyên sâu)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **3. 모듈 (Module)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.