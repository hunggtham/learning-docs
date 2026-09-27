# 5. 소프트웨어 아키텍처 및 설계 (Kiến trúc và Thiết kế Phần mềm)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **5. 소프트웨어 아키텍처 및 설계 (Kiến trúc và Thiết kế Phần mềm)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

소프트웨어, 아키텍처, 설계

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 5. 소프트웨어 아키텍처 및 설계 (Kiến trúc và Thiết kế Phần mềm)

### 024. ISO/IEC 9126의 품질 특성 (Đặc tính chất lượng theo ISO/IEC 9126)
- 기능성 (Functionality): 요구사항을 정확하게 만족하는 기능을 제공하는지 여부를 나타냄. (Cung cấp chức năng thỏa mãn chính xác các yêu cầu không.)
- 신뢰성 (Reliability): 요구된 기능을 오류 없이 수행할 수 있는 정도를 나타냄. (Mức độ thực hiện chức năng yêu cầu mà không có lỗi.)
- 사용성 (Usability): 사용자가 쉽게 배우고 사용할 수 있는 정도를 나타냄. (Mức độ người dùng dễ dàng học và sử dụng.)
- 이식성 (Portability): 다른 환경에서도 얼마나 쉽게 적용할 수 있는지 정도를 나타냄. (Mức độ dễ dàng áp dụng trong các môi trường khác nhau.)
- **Ví dụ (Example):** App đang chạy trên Android, mang sang iOS chạy vẫn tốt mà không cần sửa nhiều -> Tính 이식성 (Portability) cao.

### 025. 소프트웨어 아키텍처의 설계 과정 (Quá trình thiết kế Kiến trúc phần mềm)
- 설계 목표 설정 (Thiết lập mục tiêu thiết kế) → 시스템 타입 결정 (Quyết định loại hệ thống) → 아키텍처 패턴 적용 (Áp dụng pattern kiến trúc) → 서브시스템 구체화 (Cụ thể hóa hệ thống con) → 검토 (Xem xét/Đánh giá).

### 026. 모듈화 (Modularization / Mô-đun hóa)
- 기능의 분리가 가능하여 인터페이스가 단순해진다. (Có thể phân tách các chức năng nên giao diện trở nên đơn giản.)
- 프로그램의 효율적인 관리가 가능하다. (Có thể quản lý chương trình một cách hiệu quả.)
- 오류의 파급 효과를 최소화할 수 있다. (Có thể giảm thiểu tác động lan truyền của lỗi.)
- 모듈의 크기를 너무 작게 나누면 개수가 많아져 모듈간의 통합 비용이 많이 들고, 너무 크게 나누면 개수가 적어 통합 비용은 적게 들지만 모듈 하나의 개발 비용이 많이 든다. (Nếu chia module quá nhỏ, số lượng nhiều, chi phí tích hợp sẽ cao. Nếu chia quá lớn, chi phí tích hợp ít nhưng chi phí phát triển 1 module lại cao.)
- **Ví dụ (Example):** Thay vì viết toàn bộ chức năng vào 1 file code, ta chia ra `login.py`, `payment.py`. Lỗi ở payment không làm sập login (giảm thiểu 파급 효과).

### 027. 추상화의 유형 (Các loại trừu tượng hóa)
- 과정 추상화 (Trừu tượng hóa quá trình)
- 데이터(자료) 추상화 (Trừu tượng hóa dữ liệu)
- 제어 추상화 (Trừu tượng hóa điều khiển)

### 028. 정보 은닉 (Information Hiding / Che giấu thông tin)
- 한 모듈 내부에 포함된 절차와 자료들의 정보가 감추어져 다른 모듈이 접근하거나 변경하지 못하도록 하는 기법이다. (Kỹ thuật che giấu thông tin về thủ tục và dữ liệu bên trong một module để các module khác không thể truy cập hoặc sửa đổi.)
- 모듈을 독립적으로 수행할 수 있다. (Có thể thực thi module một cách độc lập.)
- 수정, 시험, 유지보수가 용이하다. (Dễ dàng sửa đổi, kiểm thử, bảo trì.)
- 정보 은닉을 표기할 때 private의 의미는 은닉이다. (Khi ký hiệu che giấu thông tin, 'private' mang ý nghĩa là che giấu.)
- **Ví dụ (Example):** Trong OOP, khai báo các biến là `private` và chỉ cho phép truy cập qua `getter/setter`.

### 029. 파이프 - 필터 패턴 (Pipe-Filter Pattern)
- 시스템의 처리 결과물을 파이프를 통해 전달받아 처리한 후 그 결과물을 다시 파이프를 통해 다음 시스템으로 넘겨주는 패턴이다. (Pattern nhận kết quả xử lý qua Pipe, xử lý (Filter) rồi lại chuyển kết quả đó qua Pipe cho hệ thống tiếp theo.)
- 데이터 변환으로 인한 오버헤드가 발생한다. (Phát sinh overhead do chuyển đổi dữ liệu.)
- **Ví dụ (Example):** Câu lệnh trong Linux: `ls | grep "txt" | sort`. Ký tự `|` chính là Pipe, còn `grep`, `sort` là các Filter.

### 030. MVC (Model-View-Controller) 패턴
- 모델 (Model): 서브시스템의 핵심 기능과 데이터를 보관함. (Lưu trữ chức năng cốt lõi và dữ liệu - Logic nghiệp vụ.)
- 뷰 (View): 사용자에게 정보를 표시함. (Hiển thị thông tin cho người dùng - UI.)
- 컨트롤러 (Controller): 사용자로부터 입력된 변경 요청을 처리하기 위해 모델에게 명령을 보냄. (Xử lý yêu cầu thay đổi từ người dùng và gửi lệnh cho Model.)

### 039. 모듈 (Module)
- 모듈화를 통해 분리된 시스템의 각 기능들이다. (Là các chức năng của hệ thống được tách ra thông qua quá trình module hóa.)
- 단독으로 컴파일이 가능하다. (Có thể biên dịch độc lập.)
- 재사용 할 수 있다. (Có thể tái sử dụng.)
- 다른 모듈에서의 접근이 가능하다. (Các module khác có thể truy cập được.)

### 040 & 041. 결합도 (Coupling) 의 종류와 정도 (Các loại Độ kết dính / Mức độ từ Yếu → Mạnh)
- *Kết dính càng YẾU (약함) càng TỐT, càng MẠNH (강함) càng XẤU.*
- **자료 (Data) 결합도 (Yếu nhất - Tốt nhất):** 모듈 간의 인터페이스가 자료 요소로만 구성될 때. (Chỉ truyền dữ liệu đơn giản giữa các module).
- **스탬프 (Stamp) 결합도:** 배열이나 레코드 등의 자료 구조가 전달될 때. (Truyền cấu trúc dữ liệu như mảng, bản ghi).
- **제어 (Control) 결합도:** 제어 신호를 이용하여 통신하거나 제어 요소를 전달. (Truyền cờ điều khiển - control flag/signal).
- **외부 (External) 결합도:** 데이터(변수)를 외부의 다른 모듈에서 참조할 때. (Tham chiếu biến toàn cục bên ngoài).
- **공통 (Common) 결합도:** 공유되는 공통 데이터 영역을 여러 모듈이 사용할 때. (Nhiều module cùng dùng chung một vùng dữ liệu chung - global data).
- **내용 (Content) 결합도 (Mạnh nhất - Xấu nhất):** 한 모듈이 다른 모듈의 내부 기능 및 그 내부 자료를 직접 참조하거나 수정. (Module này trực tiếp can thiệp nội bộ module kia).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **TSCNCN** (Tư - Stamp - Chế - Ngoại - Công - Nội): **Tính Sao Cho Nhẹ Cả Người**. (Từ Tốt nhất -> Xấu nhất).

### 043. 주요 응집도 (Cohesion)
- *Độ gắn kết nội bộ. Gắn kết càng MẠNH càng TỐT.*
- **기능적 (Functional) 응집도 (Mạnh nhất - Tốt nhất):** Tất cả các yếu tố bên trong đều hướng tới giải quyết một chức năng duy nhất.
- **순차적 (Sequential) 응집도:** Kết quả đầu ra của hoạt động này là đầu vào của hoạt động kia.
- **통신적 (Communication) 응집도:** Các hoạt động cùng sử dụng chung một dữ liệu đầu vào/ra.
- **절차적 (Procedural) 응집도:** 모듈 안의 구성 요소들이 그 기능을 순차적으로 수행할 경우. (Thực hiện tuần tự theo quy trình nhưng có thể không cùng dữ liệu).
- **시간적 (Temporal) 응집도:** 특정 시간에 처리되는 몇 개의 기능을 모아 하나의 모듈로 작성. (Nhóm các chức năng cần thực hiện cùng một thời điểm, ví dụ: Module khởi tạo hệ thống).
- **논리적 (Logical) 응집도:** Các chức năng có cùng logic được nhóm lại.
- **우연적 (Coincidental) 응집도 (Yếu nhất - Xấu nhất):** 각 구성 요소들이 서로 관련 없는 요소로만 구성된 경우. (Nhóm các thành phần chẳng liên quan gì với nhau).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **KTTTTLN** (Kỳ - Thuận - Thông - Tiết - Thời - Luận - Ngẫu): **Không Thể Tin Thằng Trẻ Làm Ngốc**. (Từ Tốt nhất -> Xấu nhất).

### 044. 팬인(Fan-In) / 팬아웃(Fan-Out)
- 팬인 (Fan-In): 어떤 모듈을 제어(호출)하는 모듈의 수. (Số lượng các module gọi/điều khiển module đó -> Mũi tên TRỎ VÀO nó).
- 팬아웃 (Fan-Out): 어떤 모듈에 의해 제어(호출)되는 모듈의 수. (Số lượng các module mà module đó gọi/điều khiển -> Mũi tên TRỎ RA từ nó).
- **Nguyên tắc thiết kế tốt:** Fan-In phải CAO (được dùng lại nhiều), Fan-Out phải THẤP (ít phụ thuộc vào nhiều thằng khác).
