# 5. 관계 데이터 연산 및 정규화 (Phép toán quan hệ & Chuẩn hóa)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **5. 관계 데이터 연산 및 정규화 (Phép toán quan hệ & Chuẩn hóa)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối relational operations với algebra, join và normalization, để phép biến đổi dữ liệu đi cùng giảm dư thừa.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **5. 관계 데이터 연산 및 정규화 (Phép toán quan hệ & Chuẩn hóa)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **5. 관계 데이터 연산 및 정규화 (Phép toán quan hệ & Chuẩn hóa)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **6. SQL과 객체, 시스템 개념 (SQL, View, Catalog & Transaction)** khi chuyển sang phần tiếp theo.

Mục tiêu xác định phép toán quan hệ và normalization giảm dư thừa, anomaly và chi phí truy vấn ra sao; từ khóa khoanh vùng algebra, join và dependency.

## 핵심 키워드 (Từ khóa)

관계, 데이터, 연산, 정규화

Kiến thức liên kết đặt relational operations trên nền database structure; cách đọc tiếp theo giúp theo dõi dependency và hệ quả của biến đổi.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **4. 관계형 데이터베이스 구조 (Cấu trúc CSDL Quan hệ)**에서 만든 기준을 이어받아 **5. 관계 데이터 연산 및 정규화 (Phép toán quan hệ & Chuẩn hóa)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

Cách đọc đã đặt khung đối tượng–điều kiện–hệ quả; phần quan hệ và chuẩn hóa dùng khung đó để nối phép biến đổi với chất lượng dữ liệu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

Phần này khép lại bằng tiêu chí giảm dư thừa và giữ dependency; khi sang SQL hoặc transaction, hãy giữ lại hệ quả của schema đã chọn.

## 5. 관계 데이터 연산 및 정규화 (Phép toán quan hệ & Chuẩn hóa)

Từ **4. 관계형 데이터베이스 구조 (Cấu trúc CSDL Quan hệ)**, ta đã có điểm tựa để bước vào **5. 관계 데이터 연산 및 정규화 (Phép toán quan hệ & Chuẩn hóa)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 42/69 trước khi đi vào chi tiết.

Để đọc **5. 관계 데이터 연산 및 정규화 (Phép toán quan hệ & Chuẩn hóa)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **관계대수와 관계해석 (Đại số quan hệ & Giải tích quan hệ)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 관계대수와 관계해석 (Đại số quan hệ & Giải tích quan hệ)

Các ý ngay dưới **관계대수와 관계해석 (Đại số quan hệ & Giải tích quan hệ)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “관계대수와 관계해석 (Đại số quan hệ & Giải tích quan hệ)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **관계대수 (Relational Algebra):** 절차적 언어 (Procedural). 원하는 정보와 그 정보를 **어떻게** 유도하는지 기술. (Ngôn ngữ thủ tục: Chỉ ra 'Cái gì' và 'Làm thế nào').
- **관계해석 (Relational Calculus):** 비절차적 언어 (Non-procedural). 원하는 정보가 **무엇**인지 만을 정의. (Ngôn ngữ phi thủ tục: Chỉ ra 'Cái gì').

Các bullet của **관계대수와 관계해석 (Đại số quan hệ & Giải tích quan hệ)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **관계대수와 관계해석 (Đại số quan hệ & Giải tích quan hệ)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **순수 관계 연산자 4가지 (4 Phép toán quan hệ thuần túy)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **순수 관계 연산자 4가지 (4 Phép toán quan hệ thuần túy)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 순수 관계 연산자 4가지 (4 Phép toán quan hệ thuần túy)

Bây giờ ta đi vào nội dung của **순수 관계 연산자 4가지 (4 Phép toán quan hệ thuần túy)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “순수 관계 연산자 4가지 (4 Phép toán quan hệ thuần túy)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **Select (σ / 시그마):** 조건을 만족하는 행(튜플)을 구하는 수평 연산. (Chọn ra các hàng thỏa mãn điều kiện).
- **Project (π / 파이):** 제시된 열(속성)만을 추출하는 수직 연산. (Chọn ra các cột cần thiết).
- **Join (▷◁):** 공통 속성을 중심으로 2개의 릴레이션을 하나로 합침. (Kết nối 2 bảng).
- **Division (÷):** R의 속성이 S의 속성값을 모두 가진 튜플에서 S가 가진 속성을 제외하고 구하는 연산. (Phép chia: Lấy ra các giá trị của bảng R có mặt đầy đủ trong bảng S).

Các bullet của **순수 관계 연산자 4가지 (4 Phép toán quan hệ thuần túy)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **순수 관계 연산자 4가지 (4 Phép toán quan hệ thuần túy)**, đừng bắt đầu lại từ số không. **이상(Anomaly) 현상 (Hiện tượng Dị thường dữ liệu)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **이상(Anomaly) 현상 (Hiện tượng Dị thường dữ liệu)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 이상(Anomaly) 현상 (Hiện tượng Dị thường dữ liệu)

Phần nguồn của **이상(Anomaly) 현상 (Hiện tượng Dị thường dữ liệu)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “이상(Anomaly) 현상 (Hiện tượng Dị thường dữ liệu)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 정규화를 거치지 않아 데이터가 중복될 때 발생하는 예기치 못한 현상. (Lỗi xảy ra do dữ liệu trùng lặp khi chưa chuẩn hóa).
- **삽입 이상 (Insertion):** 원하지 않는 값까지 억지로 삽입해야 하는 현상. (Khi thêm dữ liệu phải thêm cả dữ liệu không mong muốn do bắt buộc).
- **삭제 이상 (Deletion):** 한 튜플을 삭제할 때 의도와 상관없는 값까지 연쇄 삭제되는 현상. (Xóa 1 thông tin kéo theo mất luôn thông tin khác).
- **갱신 이상 (Update):** 일부 정보만 갱신되어 정보의 모순이 생기는 현상. (Cập nhật thiếu sót gây ra mâu thuẫn dữ liệu).

Các bullet của **이상(Anomaly) 현상 (Hiện tượng Dị thường dữ liệu)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**이상(Anomaly) 현상 (Hiện tượng Dị thường dữ liệu)** vừa cho ta cách đặt câu hỏi. Bây giờ **정규화(Normalization) 과정과 암기법 (Quy trình chuẩn hóa)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Đoạn **정규화(Normalization) 과정과 암기법 (Quy trình chuẩn hóa)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 정규화(Normalization) 과정과 암기법 (Quy trình chuẩn hóa)

Các ý ngay dưới **정규화(Normalization) 과정과 암기법 (Quy trình chuẩn hóa)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “정규화(Normalization) 과정과 암기법 (Quy trình chuẩn hóa)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 잘못 설계된 스키마를 쪼개어 바람직하게 만드는 논리적 설계 단계. (Chia nhỏ bảng để tối ưu dữ liệu).
- **1NF:** 도메인이 원자값 (Mỗi ô chỉ có 1 giá trị duy nhất).
- **2NF:** 부분적 함수 종속 제거 (Loại bỏ phụ thuộc hàm từng phần).
- **3NF:** 이행적 함수 종속 제거 (Loại bỏ phụ thuộc hàm bắc cầu A->B->C).
- **BCNF:** 결정자이면서 후보키가 아닌 것 제거 (Mọi yếu tố quyết định đều phải là khóa ứng viên).
- **4NF:** 다치 종속 제거 (Loại bỏ phụ thuộc đa trị).
- **5NF:** 조인 종속성 이용 (Dùng phụ thuộc Join).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **DBIGDJ** (Do-Bu-I-Gyul-Da-Jo): **Đi Bộ Ít Giúp Đỡ Jo** -> Do (Domain), Bu (부분), I (이행), Gyul (결정자), Da (다치), Jo (조인).

Các bullet của **정규화(Normalization) 과정과 암기법 (Quy trình chuẩn hóa)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Với **정규화(Normalization) 과정과 암기법 (Quy trình chuẩn hóa)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Điểm chốt của **5. 관계 데이터 연산 및 정규화 (Phép toán quan hệ & Chuẩn hóa)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **6. SQL과 객체, 시스템 개념 (SQL, View, Catalog & Transaction)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

> **Bàn giao:** Sau **5. 관계 데이터 연산 및 정규화 (Phép toán quan hệ & Chuẩn hóa)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
