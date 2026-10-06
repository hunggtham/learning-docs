# 5. 소프트웨어 아키텍처 및 설계 (Kiến trúc và Thiết kế Phần mềm)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **5. 소프트웨어 아키텍처 및 설계 (Kiến trúc và Thiết kế Phần mềm)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối software architecture với boundary, component, quality attribute và trade-off, để thiết kế chịu được thay đổi.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **5. 소프트웨어 아키텍처 및 설계 (Kiến trúc và Thiết kế Phần mềm)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **5. 소프트웨어 아키텍처 및 설계 (Kiến trúc và Thiết kế Phần mềm)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **1. 소프트웨어 아키텍처 (Software Architecture)** khi chuyển sang phần tiếp theo.

> **Nối mạch:** Trong **5. 소프트웨어 아키텍처 및 설계 (Kiến trúc và Thiết kế Phần mềm)**, **핵심 키워드 (Từ khóa)** nối từ **학습 목표 (Mục tiêu)** sang **선행·연결 개념 (Kiến thức liên kết)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 핵심 키워드 (Từ khóa)

소프트웨어, 아키텍처, 설계

> **Nối mạch:** Ở chặng này của **5. 소프트웨어 아키텍처 및 설계 (Kiến trúc và Thiết kế Phần mềm)**, **핵심 키워드 (Từ khóa)** dẫn sang **선행·연결 개념 (Kiến thức liên kết)**, nơi tài liệu chuẩn và vị trí sở hữu được chỉ rõ để biết chỗ đào sâu tiếp; **읽는 방법 (Cách đọc)** mở rộng hệ quả liên quan.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **8. UI 및 UX, HCI (UI, UX, HCI)**에서 만든 기준을 이어받아 **5. 소프트웨어 아키텍처 및 설계 (Kiến trúc và Thiết kế Phần mềm)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Nối mạch:** Đặt trong câu hỏi lớn của **5. 소프트웨어 아키텍처 및 설계 (Kiến trúc và Thiết kế Phần mềm)**, **읽는 방법 (Cách đọc)** nối từ **선행·연결 개념 (Kiến thức liên kết)** sang **5. 소프트웨어 아키텍처 및 설계 (Kiến trúc và Thiết kế Phần mềm)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Nối mạch:** Trong **5. 소프트웨어 아키텍처 및 설계 (Kiến trúc và Thiết kế Phần mềm)**, **5. 소프트웨어 아키텍처 및 설계 (Kiến trúc và Thiết kế Phần mềm)** nối từ **읽는 방법 (Cách đọc)** sang phần giải thích tiếp theo, vì phần trước cung cấp điểm tựa cho chủ đề này.

## 5. 소프트웨어 아키텍처 및 설계 (Kiến trúc và Thiết kế Phần mềm)

Từ **8. UI 및 UX, HCI (UI, UX, HCI)**, ta đã có điểm tựa để bước vào **5. 소프트웨어 아키텍처 및 설계 (Kiến trúc và Thiết kế Phần mềm)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 24/69 trước khi đi vào chi tiết.

Để đọc **5. 소프트웨어 아키텍처 및 설계 (Kiến trúc và Thiết kế Phần mềm)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng là bằng chứng để so sánh các lựa chọn theo cùng tiêu chí, không phải danh sách cần học thuộc từng ô.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **024. ISO/IEC 9126의 품질 특성 (Đặc tính chất lượng theo ISO/IEC 9126)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 024. ISO/IEC 9126의 품질 특성 (Đặc tính chất lượng theo ISO/IEC 9126)

Các ý ngay dưới **024. ISO/IEC 9126의 품질 특성 (Đặc tính chất lượng theo ISO/IEC 9126)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “024. ISO/IEC 9126의 품질 특성 (Đặc tính chất lượng theo ISO/IEC 9126)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 기능성 (Functionality): 요구사항을 정확하게 만족하는 기능을 제공하는지 여부를 나타냄. (Cung cấp chức năng thỏa mãn chính xác các yêu cầu không.)
- 신뢰성 (Reliability): 요구된 기능을 오류 없이 수행할 수 있는 정도를 나타냄. (Mức độ thực hiện chức năng yêu cầu mà không có lỗi.)
- 사용성 (Usability): 사용자가 쉽게 배우고 사용할 수 있는 정도를 나타냄. (Mức độ người dùng dễ dàng học và sử dụng.)
- 이식성 (Portability): 다른 환경에서도 얼마나 쉽게 적용할 수 있는지 정도를 나타냄. (Mức độ dễ dàng áp dụng trong các môi trường khác nhau.)
- **Ví dụ (Example):** App đang chạy trên Android, mang sang iOS chạy vẫn tốt mà không cần sửa nhiều -> Tính 이식성 (Portability) cao.

Các ý về **024. ISO/IEC 9126의 품질 특성 (Đặc tính chất lượng theo ISO/IEC 9126)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **024. ISO/IEC 9126의 품질 특성 (Đặc tính chất lượng theo ISO/IEC 9126)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **025. 소프트웨어 아키텍처의 설계 과정 (Quá trình thiết kế Kiến trúc phần mềm)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **025. 소프트웨어 아키텍처의 설계 과정 (Quá trình thiết kế Kiến trúc phần mềm)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 025. 소프트웨어 아키텍처의 설계 과정 (Quá trình thiết kế Kiến trúc phần mềm)

Bây giờ ta đi vào nội dung của **025. 소프트웨어 아키텍처의 설계 과정 (Quá trình thiết kế Kiến trúc phần mềm)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “025. 소프트웨어 아키텍처의 설계 과정 (Quá trình thiết kế Kiến trúc phần mềm)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 설계 목표 설정 (Thiết lập mục tiêu thiết kế) → 시스템 타입 결정 (Quyết định loại hệ thống) → 아키텍처 패턴 적용 (Áp dụng pattern kiến trúc) → 서브시스템 구체화 (Cụ thể hóa hệ thống con) → 검토 (Xem xét/Đánh giá).

Các bullet của **025. 소프트웨어 아키텍처의 설계 과정 (Quá trình thiết kế Kiến trúc phần mềm)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **025. 소프트웨어 아키텍처의 설계 과정 (Quá trình thiết kế Kiến trúc phần mềm)**, đừng bắt đầu lại từ số không. **026. 모듈화 (Modularization / Mô-đun hóa)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **026. 모듈화 (Modularization / Mô-đun hóa)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 026. 모듈화 (Modularization / Mô-đun hóa)

Phần nguồn của **026. 모듈화 (Modularization / Mô-đun hóa)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “026. 모듈화 (Modularization / Mô-đun hóa)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 기능의 분리가 가능하여 인터페이스가 단순해진다. (Có thể phân tách các chức năng nên giao diện trở nên đơn giản.)
- 프로그램의 효율적인 관리가 가능하다. (Có thể quản lý chương trình một cách hiệu quả.)
- 오류의 파급 효과를 최소화할 수 있다. (Có thể giảm thiểu tác động lan truyền của lỗi.)
- 모듈의 크기를 너무 작게 나누면 개수가 많아져 모듈간의 통합 비용이 많이 들고, 너무 크게 나누면 개수가 적어 통합 비용은 적게 들지만 모듈 하나의 개발 비용이 많이 든다. (Nếu chia module quá nhỏ, số lượng nhiều, chi phí tích hợp sẽ cao. Nếu chia quá lớn, chi phí tích hợp ít nhưng chi phí phát triển 1 module lại cao.)
- **Ví dụ (Example):** Thay vì viết toàn bộ chức năng vào 1 file code, ta chia ra `login.py`, `payment.py`. Lỗi ở payment không làm sập login (giảm thiểu 파급 효과).

Các ý về **026. 모듈화 (Modularization / Mô-đun hóa)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

**026. 모듈화 (Modularization / Mô-đun hóa)** vừa cho ta cách đặt câu hỏi. Bây giờ **027. 추상화의 유형 (Các loại trừu tượng hóa)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Đoạn **027. 추상화의 유형 (Các loại trừu tượng hóa)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 027. 추상화의 유형 (Các loại trừu tượng hóa)

Các ý ngay dưới **027. 추상화의 유형 (Các loại trừu tượng hóa)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “027. 추상화의 유형 (Các loại trừu tượng hóa)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 과정 추상화 (Trừu tượng hóa quá trình)
- 데이터(자료) 추상화 (Trừu tượng hóa dữ liệu)
- 제어 추상화 (Trừu tượng hóa điều khiển)

Các bullet của **027. 추상화의 유형 (Các loại trừu tượng hóa)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **027. 추상화의 유형 (Các loại trừu tượng hóa)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **028. 정보 은닉 (Information Hiding / Che giấu thông tin)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **028. 정보 은닉 (Information Hiding / Che giấu thông tin)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 028. 정보 은닉 (Information Hiding / Che giấu thông tin)

Bây giờ ta đi vào nội dung của **028. 정보 은닉 (Information Hiding / Che giấu thông tin)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “028. 정보 은닉 (Information Hiding / Che giấu thông tin)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 한 모듈 내부에 포함된 절차와 자료들의 정보가 감추어져 다른 모듈이 접근하거나 변경하지 못하도록 하는 기법이다. (Kỹ thuật che giấu thông tin về thủ tục và dữ liệu bên trong một module để các module khác không thể truy cập hoặc sửa đổi.)
- 모듈을 독립적으로 수행할 수 있다. (Có thể thực thi module một cách độc lập.)
- 수정, 시험, 유지보수가 용이하다. (Dễ dàng sửa đổi, kiểm thử, bảo trì.)
- 정보 은닉을 표기할 때 private의 의미는 은닉이다. (Khi ký hiệu che giấu thông tin, 'private' mang ý nghĩa là che giấu.)
- **Ví dụ (Example):** Trong OOP, khai báo các biến là `private` và chỉ cho phép truy cập qua `getter/setter`.

Các ý về **028. 정보 은닉 (Information Hiding / Che giấu thông tin)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Sau khi đọc **028. 정보 은닉 (Information Hiding / Che giấu thông tin)**, đừng bắt đầu lại từ số không. **029. 파이프 - 필터 패턴 (Pipe-Filter Pattern)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **029. 파이프 - 필터 패턴 (Pipe-Filter Pattern)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 029. 파이프 - 필터 패턴 (Pipe-Filter Pattern)

Phần nguồn của **029. 파이프 - 필터 패턴 (Pipe-Filter Pattern)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “029. 파이프 - 필터 패턴 (Pipe-Filter Pattern)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 시스템의 처리 결과물을 파이프를 통해 전달받아 처리한 후 그 결과물을 다시 파이프를 통해 다음 시스템으로 넘겨주는 패턴이다. (Pattern nhận kết quả xử lý qua Pipe, xử lý (Filter) rồi lại chuyển kết quả đó qua Pipe cho hệ thống tiếp theo.)
- 데이터 변환으로 인한 오버헤드가 발생한다. (Phát sinh overhead do chuyển đổi dữ liệu.)
- **Ví dụ (Example):** Câu lệnh trong Linux: `ls | grep "txt" | sort`. Ký tự `|` chính là Pipe, còn `grep`, `sort` là các Filter.

Các ý về **029. 파이프 - 필터 패턴 (Pipe-Filter Pattern)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

**029. 파이프 - 필터 패턴 (Pipe-Filter Pattern)** vừa cho ta cách đặt câu hỏi. Bây giờ **030. MVC (Model-View-Controller) 패턴** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Đoạn **030. MVC (Model-View-Controller) 패턴** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 030. MVC (Model-View-Controller) 패턴

Các ý ngay dưới **030. MVC (Model-View-Controller) 패턴** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “030. MVC (Model-View-Controller) 패턴” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 모델 (Model): 서브시스템의 핵심 기능과 데이터를 보관함. (Lưu trữ chức năng cốt lõi và dữ liệu - Logic nghiệp vụ.)
- 뷰 (View): 사용자에게 정보를 표시함. (Hiển thị thông tin cho người dùng - UI.)
- 컨트롤러 (Controller): 사용자로부터 입력된 변경 요청을 처리하기 위해 모델에게 명령을 보냄. (Xử lý yêu cầu thay đổi từ người dùng và gửi lệnh cho Model.)

Các bullet của **030. MVC (Model-View-Controller) 패턴** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **030. MVC (Model-View-Controller) 패턴** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **039. 모듈 (Module)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **039. 모듈 (Module)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 039. 모듈 (Module)

Bây giờ ta đi vào nội dung của **039. 모듈 (Module)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “039. 모듈 (Module)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 모듈화를 통해 분리된 시스템의 각 기능들이다. (Là các chức năng của hệ thống được tách ra thông qua quá trình module hóa.)
- 단독으로 컴파일이 가능하다. (Có thể biên dịch độc lập.)
- 재사용 할 수 있다. (Có thể tái sử dụng.)
- 다른 모듈에서의 접근이 가능하다. (Các module khác có thể truy cập được.)

Các bullet của **039. 모듈 (Module)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **039. 모듈 (Module)**, đừng bắt đầu lại từ số không. **040 & 041. 결합도 (Coupling) 의 종류와 정도 (Các loại Độ kết dính / Mức độ từ Yếu → Mạnh)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **040 & 041. 결합도 (Coupling) 의 종류와 정도 (Các loại Độ kết dính / Mức độ từ Yếu → Mạnh)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 040 & 041. 결합도 (Coupling) 의 종류와 정도 (Các loại Độ kết dính / Mức độ từ Yếu → Mạnh)

Phần nguồn của **040 & 041. 결합도 (Coupling) 의 종류와 정도 (Các loại Độ kết dính / Mức độ từ Yếu → Mạnh)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “040 & 041. 결합도 (Coupling) 의 종류와 정도 (Các loại Độ kết dính / Mức độ từ Yếu → Mạnh)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- *Kết dính càng YẾU (약함) càng TỐT, càng MẠNH (강함) càng XẤU.*
- **자료 (Data) 결합도 (Yếu nhất - Tốt nhất):** 모듈 간의 인터페이스가 자료 요소로만 구성될 때. (Chỉ truyền dữ liệu đơn giản giữa các module).
- **스탬프 (Stamp) 결합도:** 배열이나 레코드 등의 자료 구조가 전달될 때. (Truyền cấu trúc dữ liệu như mảng, bản ghi).
- **제어 (Control) 결합도:** 제어 신호를 이용하여 통신하거나 제어 요소를 전달. (Truyền cờ điều khiển - control flag/signal).
- **외부 (External) 결합도:** 데이터(변수)를 외부의 다른 모듈에서 참조할 때. (Tham chiếu biến toàn cục bên ngoài).
- **공통 (Common) 결합도:** 공유되는 공통 데이터 영역을 여러 모듈이 사용할 때. (Nhiều module cùng dùng chung một vùng dữ liệu chung - global data).
- **내용 (Content) 결합도 (Mạnh nhất - Xấu nhất):** 한 모듈이 다른 모듈의 내부 기능 및 그 내부 자료를 직접 참조하거나 수정. (Module này trực tiếp can thiệp nội bộ module kia).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **TSCNCN** (Tư - Stamp - Chế - Ngoại - Công - Nội): **Tính Sao Cho Nhẹ Cả Người**. (Từ Tốt nhất -> Xấu nhất).

Các bullet của **040 & 041. 결합도 (Coupling) 의 종류와 정도 (Các loại Độ kết dính / Mức độ từ Yếu → Mạnh)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**040 & 041. 결합도 (Coupling) 의 종류와 정도 (Các loại Độ kết dính / Mức độ từ Yếu → Mạnh)** vừa cho ta cách đặt câu hỏi. Bây giờ **043. 주요 응집도 (Cohesion)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Đoạn **043. 주요 응집도 (Cohesion)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 043. 주요 응집도 (Cohesion)

Các ý ngay dưới **043. 주요 응집도 (Cohesion)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “043. 주요 응집도 (Cohesion)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- *Độ gắn kết nội bộ. Gắn kết càng MẠNH càng TỐT.*
- **기능적 (Functional) 응집도 (Mạnh nhất - Tốt nhất):** Tất cả các yếu tố bên trong đều hướng tới giải quyết một chức năng duy nhất.
- **순차적 (Sequential) 응집도:** Kết quả đầu ra của hoạt động này là đầu vào của hoạt động kia.
- **통신적 (Communication) 응집도:** Các hoạt động cùng sử dụng chung một dữ liệu đầu vào/ra.
- **절차적 (Procedural) 응집도:** 모듈 안의 구성 요소들이 그 기능을 순차적으로 수행할 경우. (Thực hiện tuần tự theo quy trình nhưng có thể không cùng dữ liệu).
- **시간적 (Temporal) 응집도:** 특정 시간에 처리되는 몇 개의 기능을 모아 하나의 모듈로 작성. (Nhóm các chức năng cần thực hiện cùng một thời điểm, ví dụ: Module khởi tạo hệ thống).
- **논리적 (Logical) 응집도:** Các chức năng có cùng logic được nhóm lại.
- **우연적 (Coincidental) 응집도 (Yếu nhất - Xấu nhất):** 각 구성 요소들이 서로 관련 없는 요소로만 구성된 경우. (Nhóm các thành phần chẳng liên quan gì với nhau).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **KTTTTLN** (Kỳ - Thuận - Thông - Tiết - Thời - Luận - Ngẫu): **Không Thể Tin Thằng Trẻ Làm Ngốc**. (Từ Tốt nhất -> Xấu nhất).

Các ý về **043. 주요 응집도 (Cohesion)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **043. 주요 응집도 (Cohesion)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **044. 팬인(Fan-In) / 팬아웃(Fan-Out)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **044. 팬인(Fan-In) / 팬아웃(Fan-Out)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 044. 팬인(Fan-In) / 팬아웃(Fan-Out)

Bây giờ ta đi vào nội dung của **044. 팬인(Fan-In) / 팬아웃(Fan-Out)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “044. 팬인(Fan-In) / 팬아웃(Fan-Out)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 팬인 (Fan-In): 어떤 모듈을 제어(호출)하는 모듈의 수. (Số lượng các module gọi/điều khiển module đó -> Mũi tên TRỎ VÀO nó).
- 팬아웃 (Fan-Out): 어떤 모듈에 의해 제어(호출)되는 모듈의 수. (Số lượng các module mà module đó gọi/điều khiển -> Mũi tên TRỎ RA từ nó).
- **Nguyên tắc thiết kế tốt:** Fan-In phải CAO (được dùng lại nhiều), Fan-Out phải THẤP (ít phụ thuộc vào nhiều thằng khác).

Các bullet của **044. 팬인(Fan-In) / 팬아웃(Fan-Out)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **044. 팬인(Fan-In) / 팬아웃(Fan-Out)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **5. 소프트웨어 아키텍처 및 설계 (Kiến trúc và Thiết kế Phần mềm)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **1. 소프트웨어 아키텍처 (Software Architecture)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

> **Bàn giao:** Sau **5. 소프트웨어 아키텍처 및 설계 (Kiến trúc và Thiết kế Phần mềm)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
