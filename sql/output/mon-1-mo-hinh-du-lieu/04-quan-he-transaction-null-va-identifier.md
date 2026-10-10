# Quan hệ, Transaction, NULL và Identifier

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Quan hệ, transaction, NULL và identifier**. Route đi từ three-valued logic → key/NULL semantics → transaction boundaries → ACID/isolation → consistency and application behavior, để SQL semantics nối với trạng thái đồng thời.

> **Mục tiêu:** Quan hệ trong mô hình, ACID, NULL trong SQL và natural/surrogate key.

## Từ khóa cần nhớ (Keyword)

Phần giải thích dùng tiếng Việt trước. Ở mọi lần xuất hiện, thuật ngữ SQLD dùng dạng `nghĩa Việt (English / 한국어)` để vừa giữ mạch đọc vừa đối chiếu được từ khóa trong đề.

> **Nối mạch:** Từ **Từ khóa cần nhớ (Keyword)**, **Mạch tư duy (Logic học)** chuyển các thuật ngữ quan hệ, transaction, NULL và identifier thành những câu hỏi cần kiểm tra; **Mạch nối của bài học** sẽ liên kết chúng thành một chuỗi nguyên nhân–hệ quả.

## Mạch tư duy (Logic học)

Hãy xác định **đối tượng dữ liệu** trước, sau đó đọc **điều kiện**, **phạm vi dòng**, **thứ tự xử lý** và cuối cùng kiểm tra **kết quả mong đợi**. Với SQL, luôn phân biệt điều kiện lọc trước nhóm (`WHERE`) với điều kiện lọc sau nhóm (`HAVING`); đây là cầu nối để hiểu vì sao cùng một truy vấn có thể cho kết quả khác nhau.

> **Nối mạch:** Sau khi đặt câu hỏi logic cho các thuật ngữ, **Mạch nối của bài học** chỉ ra thứ tự đọc; từ đó chuyển sang **제2절 관계와 조인의 이해** để xem quan hệ và JOIN hiện thực hóa các tiêu chí ấy thế nào.

## Mạch nối của bài học

Bài này không đứng riêng: hãy nối **Quan hệ, Transaction, NULL và Identifier** với bài trước bằng đối tượng dữ liệu/điều kiện mà nó tái sử dụng, rồi dùng kết quả ở phần cuối để chọn bài kế tiếp trong cùng môn. Khi gặp một truy vấn mới, nói rõ nó đang mở rộng mô hình dữ liệu, thứ tự xử lý hay cách kiểm tra kết quả nào trước khi nhớ cú pháp.

> **Cách học:** Đọc phần khái niệm → tự chạy lại các ví dụ SQL → chốt lại mục **từ khóa (Keyword)**, bảng so sánh và phần ghi nhớ cuối bài.

---

Để học **Quan hệ, Transaction, NULL và Identifier** như một mạch suy luận, trước hết hãy giữ câu hỏi: **thay đổi nào tác động lên hàng dữ liệu, phạm vi nào bị ảnh hưởng và khi nào thay đổi được xác nhận?** Mục đích của bài là biến **Quan hệ trong mô hình, ACID, NULL trong SQL và natural/surrogate key** thành cách đọc có thể áp dụng.

Ta bắt đầu **Câu tổng kết tiếng Việt** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### Câu tổng kết tiếng Việt

Chuẩn hóa đi từ giá trị nguyên tử đến loại bỏ phụ thuộc bộ phận, phụ thuộc bắc cầu, phụ thuộc đa trị và phụ thuộc JOIN. Trước tiên phải chuẩn hóa đúng, sau đó mới đo hiệu năng và cân nhắc phi chuẩn hóa phần thật sự cần thiết.

Khi gom phần **Câu tổng kết tiếng Việt** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Câu tổng kết tiếng Việt**. Bây giờ chuyển sang **제2절 관계와 조인의 이해**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **제2절 관계와 조인의 이해** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** **Mạch nối của bài học** đã đặt thứ tự khái niệm; **제2절 관계와 조인의 이해** chuyển sang phạm vi quan hệ và JOIN, rồi mở thành **Phần 2: Quan hệ và JOIN** để đọc ví dụ theo truy vấn.

## 제2절 관계와 조인의 이해

Khi gom phần **제2절 관계와 조인의 이해** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **제2절 관계와 조인의 이해**. Bây giờ chuyển sang **Phần 2: Quan hệ và JOIN**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Phần 2: Quan hệ và JOIN** bằng câu hỏi: **ta đang kết hợp những tập hàng nào, cột nào làm cầu nối và điều kiện nối làm thay đổi kết quả ra sao?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** Từ khung **제2절 관계와 조인의 이해**, **Phần 2: Quan hệ và JOIN** đặt câu hỏi về bảng, khóa nối và kết quả; **1. 반정규화** sẽ cho thấy khi nào ta chủ động đổi mô hình để giảm chi phí JOIN.

## Phần 2: Quan hệ và JOIN

Ba hình này nối tiếp phần **반정규화 — Denormalization — Phi chuẩn hóa**, sau đó chuyển sang **관계 — Relationship — Quan hệ** và **조인 — JOIN — Kết nối bảng**.

---

Khi gom phần **Phần 2: Quan hệ và JOIN** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Phần 2: Quan hệ và JOIN**. Bây giờ chuyển sang **1. 반정규화**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **1. 반정규화** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** **Phần 2: Quan hệ và JOIN** cho thấy chi phí khi phải kết hợp bảng; **1. 반정규화** gọi tên quyết định thiết kế cho phép lặp hoặc gộp dữ liệu, rồi **1. Phi chuẩn hóa** giải thích quyết định ấy bằng tiếng Việt.

## 1. 반정규화

Khi gom phần **1. 반정규화** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **1. 반정규화**. Bây giờ chuyển sang **1. Phi chuẩn hóa**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **1. Phi chuẩn hóa** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** Sau khi phân biệt `반정규화` với mô hình chưa chuẩn hóa, **1. Phi chuẩn hóa** chuyển sang điều kiện, lợi ích và mặt trái; **2. Ví dụ 반정규화 trong hình** sẽ đặt nguyên tắc đó vào sơ đồ bảng.

## 1. Phi chuẩn hóa

Khi gom phần **1. Phi chuẩn hóa** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **1. Phi chuẩn hóa**. Bây giờ chuyển sang **1.1 반정규화의 khái niệm**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **1.1 반정규화의 khái niệm** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 1.1 반정규화의 khái niệm

**반정규화는 역정규화라고도 하며, 비정규화와는 다르다.**

**반정규화 còn được gọi là phi chuẩn hóa, nhưng không giống hoàn toàn với việc không chuẩn hóa.**

- `반정규화`: Denormalization, điều chỉnh có chủ đích mô hình đã chuẩn hóa.
- `비정규화`: Unnormalized, mô hình chưa được chuẩn hóa đầy đủ.

**반정규화는 데이터베이스 성능 향상을 위해 데이터 중복을 허용하고 조인을 줄이는 방법이다.**

**Phi chuẩn hóa là phương pháp cho phép trùng lặp dữ liệu và giảm JOIN nhằm cải thiện hiệu năng cơ sở dữ liệu.**

**반정규화는 정규화된 데이터 모델을 중복·통합·분리하여 시스템의 개발과 운영을 단순화하는 모델링 기법이다.**

**Phi chuẩn hóa là kỹ thuật điều chỉnh mô hình đã chuẩn hóa bằng cách thêm trùng lặp, gộp hoặc tách dữ liệu để đơn giản hóa việc phát triển và vận hành hệ thống.**

---

Khi gom phần **1.1 반정규화의 khái niệm** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **1.1 반정규화의 khái niệm**. Bây giờ chuyển sang **1.2 반정규화의 효과와 단점**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **1.2 반정규화의 효과와 단점** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 1.2 반정규화의 효과와 단점

**반정규화는 조회 속도를 향상시킬 수 있지만 데이터 모델의 유연성은 낮아질 수 있다.**

**Phi chuẩn hóa có thể tăng tốc độ truy vấn nhưng có thể làm giảm tính linh hoạt của mô hình dữ liệu.**

**반정규화를 하면 입력·수정·삭제 성능이 저하될 수 있다.**

**Khi phi chuẩn hóa, hiệu năng thêm, sửa và xóa dữ liệu có thể giảm.**

Lý do là cùng một thông tin có thể được lưu ở nhiều nơi, nên khi thay đổi phải cập nhật nhiều dòng hoặc nhiều bảng.

Ví dụ, nếu `부서명` được sao chép vào bảng `사원`, khi tên phòng ban thay đổi phải sửa nhiều dòng nhân viên.

---

Khi gom phần **1.2 반정규화의 효과와 단점** lại, ta không cần nhớ các dòng như những mảnh rời: ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **1.2 반정규화의 효과와 단점**. Bây giờ chuyển sang **1.3 Khi nào thực hiện 반정규화?**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **1.3 Khi nào thực hiện 반정규화?** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 1.3 Khi nào thực hiện 반정규화?

**정규화로 엔터티와 관계의 수가 많아져 조인으로 인한 성능 저하가 예상될 때 반정규화를 수행할 수 있다.**

**Có thể thực hiện phi chuẩn hóa khi việc chuẩn hóa làm tăng số Entity và quan hệ, khiến hiệu năng JOIN được dự đoán sẽ giảm.**

**정규화에 충실할수록 데이터의 종속성과 활용성은 향상되지만 수행 속도가 느려지는 경우 반정규화를 고려할 수 있다.**

**Nếu việc tuân thủ chuẩn hóa giúp tăng tính phụ thuộc và khả năng sử dụng dữ liệu nhưng làm tốc độ xử lý chậm, có thể cân nhắc phi chuẩn hóa.**

**대량의 범위를 자주 처리해야 하는 경우 반정규화를 고려할 수 있다.**

**Có thể cân nhắc phi chuẩn hóa khi thường xuyên phải xử lý một phạm vi dữ liệu lớn.**

**특정 범위의 데이터만 자주 처리하는 경우 반정규화를 고려할 수 있다.**

**Có thể cân nhắc phi chuẩn hóa khi thường xuyên chỉ xử lý một phạm vi dữ liệu cụ thể.**

**요약이나 집계 정보가 자주 요구되는 경우 반정규화를 고려할 수 있다.**

**Có thể cân nhắc phi chuẩn hóa khi thường xuyên cần thông tin tóm tắt hoặc tổng hợp.**

Ví dụ:

- Tổng doanh thu theo tháng.
- Số lượng nhân viên theo phòng ban.
- Số đơn hàng của từng khách hàng.
- Tổng điểm hoặc tổng số giao dịch.

**반정규화가 조회 성능 향상을 항상 보장하는 것은 아니다.**

**Phi chuẩn hóa không phải lúc nào cũng bảo đảm cải thiện hiệu năng truy vấn.**

Phải kiểm tra SQL thực tế, dữ liệu thực tế và Execution Plan trước khi quyết định.

---

Khi gom phần **1.3 Khi nào thực hiện 반정규화?** lại, ta không cần nhớ các dòng như những mảnh rời: ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **1.3 Khi nào thực hiện 반정규화?**. Bây giờ chuyển sang **2. Ví dụ 반정규화 trong hình**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **2. Ví dụ 반정규화 trong hình** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** **1. Phi chuẩn hóa** nêu đánh đổi giữa tốc độ đọc và chi phí cập nhật; **2. Ví dụ 반정규화 trong hình** minh họa đánh đổi ấy, sau đó **2. Ví dụ phi chuẩn hóa trong hình** diễn giải hình bằng dữ liệu cụ thể.

## 2. Ví dụ 반정규화 trong hình

Khi gom phần **2. Ví dụ 반정규화 trong hình** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **2. Ví dụ 반정규화 trong hình**. Bây giờ chuyển sang **2. Ví dụ phi chuẩn hóa trong hình**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **2. Ví dụ phi chuẩn hóa trong hình** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** Sau khi nhìn thấy ví dụ phi chuẩn hóa, **3. 관계** quay về khái niệm quan hệ để xác định các bảng được liên kết bằng thuộc tính nào và vì sao JOIN vẫn cần thiết.

## 2. Ví dụ phi chuẩn hóa trong hình

Trong hình có hai bảng đã được chuẩn hóa:

Khi gom phần **2. Ví dụ phi chuẩn hóa trong hình** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **2. Ví dụ phi chuẩn hóa trong hình**. Bây giờ chuyển sang **사원 테이블 — Bảng nhân viên**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **사원 테이블 — Bảng nhân viên** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 사원 테이블 — Bảng nhân viên

Phần này nối mạch SQL với “사원 테이블 — Bảng nhân viên”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

| 사번(PK) | 이름 | 부서번호 |
| --- | --- | --- |
| 2401 | 김지민 | 100 |
| 2402 | 이사원 | 101 |
| 2403 | 유현지 | 201 |

Khi gom phần **사원 테이블 — Bảng nhân viên** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **사원 테이블 — Bảng nhân viên**. Bây giờ chuyển sang **부서 테이블 — Bảng phòng ban**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **부서 테이블 — Bảng phòng ban** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 부서 테이블 — Bảng phòng ban

Phần này nối mạch SQL với “부서 테이블 — Bảng phòng ban”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

| 부서번호(PK) | 부서명 | 소재지 |
| --- | --- | --- |
| 100 | 영업부 | 서울 |
| 101 | 개발부 | 서울 |
| 201 | 생산부 | 부산 |

**사원 테이블의 부서번호와 부서 테이블의 부서번호가 같은 값을 가지므로 두 테이블을 연결할 수 있다.**

**Vì `부서번호` trong bảng nhân viên và `부서번호` trong bảng phòng ban có cùng giá trị nên có thể kết nối hai bảng.**

**부서번호가 두 테이블을 연결하는 JOIN KEY가 된다.**

**`부서번호` trở thành JOIN KEY kết nối hai bảng.**

Câu SQL tương ứng:

```sql
SELECT s.사번,
       s.이름,
       s.부서번호,
       d.부서명,
       d.소재지
FROM 사원 s
JOIN 부서 d
  ON s.부서번호 = d.부서번호;
```

Khi thực hiện truy vấn này, thông tin phòng ban được lấy bằng JOIN thay vì lưu lặp lại trong bảng nhân viên.

Nếu phi chuẩn hóa, có thể thêm `부서명` và `부서 위치` vào bảng `사원`.

```
사원(사번, 이름, 부서번호, 부서명, 부서위치)
```

Khi đó truy vấn đơn giản hơn, nhưng nếu tên phòng ban thay đổi thì nhiều dòng nhân viên cần được cập nhật.

---

Khi gom phần **부서 테이블 — Bảng phòng ban** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **부서 테이블 — Bảng phòng ban**. Bây giờ chuyển sang **3. 관계**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **3. 관계** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** **2. Ví dụ phi chuẩn hóa trong hình** cho thấy JOIN KEY và dữ liệu lặp thay đổi truy vấn ra sao; **3. 관계** khái quát lại quan hệ giữa thực thể, thuộc tính và hành động, rồi **3. Quan hệ** diễn giải cùng mạch bằng tiếng Việt.

## 3. 관계

Khi gom phần **3. 관계** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **3. 관계**. Bây giờ chuyển sang **3. Quan hệ**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **3. Quan hệ** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** Sau khi xác định quan hệ là liên kết có ngữ nghĩa giữa các thực thể, **4. 식별관계와 비식별관계** hỏi khóa cha có trở thành một phần định danh của khóa con hay không.

## 3. Quan hệ

Khi gom phần **3. Quan hệ** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **3. Quan hệ**. Bây giờ chuyển sang **3.1 관계의 정의**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **3.1 관계의 정의** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 3.1 관계의 정의

**관계는 엔터티의 인스턴스 사이에 존재하는 논리적인 연관성이다.**

**Quan hệ là sự liên kết logic tồn tại giữa các Instance của các Entity.**

Nói đơn giản:

- Entity là đối tượng hoặc chủ đề.
- Instance là một bản ghi cụ thể của Entity.
- Relationship là mối liên hệ giữa các bản ghi đó.

Ví dụ:

```
사원 Entity
부서 Entity
```

Một nhân viên cụ thể `김지민` thuộc một phòng ban cụ thể `영업부`.

Đây là quan hệ giữa một Instance của `사원` và một Instance của `부서`.

---

Khi gom phần **3.1 관계의 정의** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **3.1 관계의 정의**. Bây giờ chuyển sang **3.2 Quan hệ thông qua hành động**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **3.2 Quan hệ thông qua hành động** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 3.2 Quan hệ thông qua hành động

**관계는 엔터티 사이의 존재 관계와 행위 관계로 구분할 수 있다.**

**Quan hệ có thể được chia thành quan hệ tồn tại và quan hệ hành vi.**

Khi gom phần **3.2 Quan hệ thông qua hành động** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **3.2 Quan hệ thông qua hành động**. Bây giờ chuyển sang **존재 관계**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **존재 관계** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 존재 관계

**존재 관계는 한 엔터티가 다른 엔터티에 소속되는 관계이다.**

**Quan hệ tồn tại là quan hệ trong đó một Entity thuộc về một Entity khác.**

Ví dụ:

```
사원은 부서에 소속된다.
Nhân viên thuộc phòng ban.
```

Trong hình:

```
사원 ── 소속 ── 부서
```

Khi gom phần **존재 관계** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **존재 관계**. Bây giờ chuyển sang **행위 관계**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **행위 관계** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 행위 관계

**행위 관계는 어떤 행위를 통해 엔터티 사이에 발생하는 관계이다.**

**Quan hệ hành vi là quan hệ phát sinh giữa các Entity thông qua một hành động.**

Ví dụ:

```
고객이 주문한다.
Khách hàng đặt hàng.
```

Quan hệ `주문` phát sinh khi khách hàng thực hiện hành động đặt hàng.

---

Khi gom phần **행위 관계** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **행위 관계**. Bây giờ chuyển sang **4. 식별관계와 비식별관계**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **4. 식별관계와 비식별관계** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** **4. 식별관계와 비식별관계** nêu tên hai kiểu quan hệ; **4. Quan hệ định danh và không định danh** chuyển thành tiêu chí thiết kế: khóa con phụ thuộc định danh vào cha hay chỉ tham chiếu đến cha.

## 4. 식별관계와 비식별관계

Khi gom phần **4. 식별관계와 비식별관계** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **4. 식별관계와 비식별관계**. Bây giờ chuyển sang **4. Quan hệ định danh và không định danh**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **4. Quan hệ định danh và không định danh** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** Sau khi phân biệt khóa định danh và khóa tham chiếu, **5. 조인** dùng quan hệ đó làm điều kiện kết hợp các bảng để tạo kết quả truy vấn.

## 4. Quan hệ định danh và không định danh

Khi gom phần **4. Quan hệ định danh và không định danh** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **4. Quan hệ định danh và không định danh**. Bây giờ chuyển sang **4.1 식별관계**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **4.1 식별관계** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 4.1 식별관계

**부모의 식별자를 자식의 식별자에 포함하면 식별관계이다.**

**Nếu khóa định danh của cha được bao gồm trong khóa định danh của con thì đó là quan hệ định danh.**

Ví dụ:

```
부모 PK → 자식 PK
```

Trong quan hệ định danh, khóa của bảng cha trở thành một phần của PK bảng con.

Ví dụ:

```
주문(PK: 주문번호)
주문상세(PK: 주문번호 + 상품번호)
```

`주문번호` của bảng `주문` đồng thời tham gia vào PK của `주문상세`.

---

Khi gom phần **4.1 식별관계** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **4.1 식별관계**. Bây giờ chuyển sang **4.2 비식별관계**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **4.2 비식별관계** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 4.2 비식별관계

**부모의 식별자를 자식의 일반 속성으로 포함하면 비식별관계이다.**

**Nếu khóa định danh của cha chỉ được đưa vào bảng con với tư cách thuộc tính thường thì đó là quan hệ không định danh.**

Ví dụ:

```
부서(부서번호 PK)
사원(사번 PK, 부서번호 FK)
```

`부서번호` là PK của bảng `부서`, nhưng trong bảng `사원`, nó chỉ là FK chứ không tham gia vào PK.

---

Khi gom phần **4.2 비식별관계** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **4.2 비식별관계**. Bây giờ chuyển sang **5. 조인**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **5. 조인** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** **5. 조인** đặt thuật ngữ JOIN trong mạch quan hệ; **5. JOIN** trình bày cú pháp và hệ quả của việc ghép hàng bằng khóa chung.

## 5. 조인

Khi gom phần **5. 조인** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **5. 조인**. Bây giờ chuyển sang **5. JOIN**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **5. JOIN** bằng câu hỏi: **ta đang kết hợp những tập hàng nào, cột nào làm cầu nối và điều kiện nối làm thay đổi kết quả ra sao?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** Sau khi hiểu JOIN giữa các bảng khác nhau, **6. Self JOIN** áp dụng cùng nguyên tắc lên một bảng tự liên kết để đọc quan hệ phân cấp hoặc so sánh giữa các dòng.

## 5. JOIN

Khi gom phần **5. JOIN** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **5. JOIN**. Bây giờ chuyển sang **5.1 Khái niệm JOIN**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **5.1 Khái niệm JOIN** bằng câu hỏi: **ta đang kết hợp những tập hàng nào, cột nào làm cầu nối và điều kiện nối làm thay đổi kết quả ra sao?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 5.1 Khái niệm JOIN

**조인은 두 테이블의 공통 속성을 이용하여 데이터를 결합하는 것이다.**

**JOIN là việc kết hợp dữ liệu của hai bảng bằng thuộc tính chung.**

**조인에 사용되는 공통 속성을 조인 키 또는 JOIN KEY라고 한다.**

**Thuộc tính chung được sử dụng để JOIN gọi là Join Key hoặc JOIN KEY.**

Trong ví dụ:

```
사원.부서번호 = 부서.부서번호
```

`부서번호` là JOIN KEY.

---

Khi gom phần **5.1 Khái niệm JOIN** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **5.1 Khái niệm JOIN**. Bây giờ chuyển sang **5.2 JOIN trước và sau chuẩn hóa**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **5.2 JOIN trước và sau chuẩn hóa** bằng câu hỏi: **ta đang kết hợp những tập hàng nào, cột nào làm cầu nối và điều kiện nối làm thay đổi kết quả ra sao?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 5.2 JOIN trước và sau chuẩn hóa

Trước chuẩn hóa, bảng `사원` chứa cả:

```
사번, 이름, 부서번호, 부서명, 부서위치
```

Khi đó có thể truy vấn trực tiếp:

```sql
SELECT 사번, 이름, 부서명
FROM 사원
WHERE 사번 = '2401';
```

Sau chuẩn hóa, bảng `사원` chỉ chứa:

```
사번, 이름, 부서번호
```

Bảng `부서` chứa:

```
부서번호, 부서명, 부서위치
```

Muốn lấy thông tin đầy đủ phải JOIN:

```sql
SELECT a.사번,
       a.이름,
       b.부서명
FROM 사원 a,
     부서 b
WHERE a.부서번호 = b.부서번호
  AND a.사번 = '2401';
```

Hoặc viết theo ANSI JOIN:

```sql
SELECT a.사번,
       a.이름,
       b.부서명
FROM 사원 a
JOIN 부서 b
  ON a.부서번호 = b.부서번호
WHERE a.사번 = '2401';
```

**정규화 후에는 데이터의 독립성이 높아지지만 필요한 정보를 함께 조회하려면 조인이 필요하다.**

**Sau chuẩn hóa, tính độc lập của dữ liệu tăng lên nhưng cần JOIN khi muốn truy vấn các thông tin liên quan cùng lúc.**

---

Khi gom phần **5.2 JOIN trước và sau chuẩn hóa** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **5.2 JOIN trước và sau chuẩn hóa**. Bây giờ chuyển sang **6. Self JOIN**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **6. Self JOIN** bằng câu hỏi: **ta đang kết hợp những tập hàng nào, cột nào làm cầu nối và điều kiện nối làm thay đổi kết quả ra sao?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** **5. JOIN** đã xác định điều kiện ghép giữa các bảng; **6. Self JOIN** giữ nguyên cơ chế nhưng dùng hai bí danh cho cùng một bảng, rồi **6. Tự JOIN** giải thích tình huống ấy bằng tiếng Việt.

## 6. Self JOIN

Khi gom phần **6. Self JOIN** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **6. Self JOIN**. Bây giờ chuyển sang **6. Tự JOIN**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **6. Tự JOIN** bằng câu hỏi: **ta đang kết hợp những tập hàng nào, cột nào làm cầu nối và điều kiện nối làm thay đổi kết quả ra sao?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** Sau khi đọc self join như quan hệ giữa các dòng trong cùng bảng, **7. 상호 배타적 관계** chuyển sang điều kiện loại trừ: một thực thể phải thuộc một nhánh này hoặc nhánh kia.

## 6. Tự JOIN

Khi gom phần **6. Tự JOIN** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **6. Tự JOIN**. Bây giờ chuyển sang **6.1 관계형 데이터 모델**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **6.1 관계형 데이터 모델** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 6.1 관계형 데이터 모델

**관계형 데이터 모델에서 자기 자신끼리의 관계를 자기 자신과의 관계라고 한다.**

**Trong mô hình dữ liệu quan hệ, quan hệ giữa các bản ghi trong cùng một Entity gọi là quan hệ với chính nó.**

Một Entity có thể chứa quan hệ phân cấp giữa các Instance của chính Entity đó.

Ví dụ:

```
직원 → 상사
Nhân viên → Cấp trên
```

Cùng một bảng `직원`, nhưng một dòng có thể là cấp trên của dòng khác.

---

Khi gom phần **6.1 관계형 데이터 모델** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **6.1 관계형 데이터 모델**. Bây giờ chuyển sang **6.2 Ví dụ bảng nhân viên**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **6.2 Ví dụ bảng nhân viên** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 6.2 Ví dụ bảng nhân viên

Phần này nối mạch SQL với “6.2 Ví dụ bảng nhân viên”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

| 직원ID(PK) | 이름 | 상사ID |
| --- | --- | --- |
| 1 | 나사장 | NULL |
| 2 | 김철수 | 1 |
| 3 | 이지현 | 1 |
| 4 | 황수지 | 2 |
| 5 | 박현석 | 3 |

Ý nghĩa:

- `나사장` không có cấp trên nên `상사ID = NULL`.
- `김철수` có cấp trên là nhân viên `1`.
- `이지현` có cấp trên là nhân viên `1`.
- `황수지` có cấp trên là nhân viên `2`.
- `박현석` có cấp trên là nhân viên `3`.

**상사ID는 같은 직원 테이블의 직원ID를 참조한다.**

**`상사ID` tham chiếu đến `직원ID` trong chính bảng nhân viên.**

Đây là Self Referencing Foreign Key.

---

Khi gom phần **6.2 Ví dụ bảng nhân viên** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **6.2 Ví dụ bảng nhân viên**. Bây giờ chuyển sang **6.3 SQL Self JOIN**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **6.3 SQL Self JOIN** bằng câu hỏi: **ta đang kết hợp những tập hàng nào, cột nào làm cầu nối và điều kiện nối làm thay đổi kết quả ra sao?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 6.3 SQL Self JOIN

**어떤 직원의 상사 이름을 조회하려면 직원 테이블을 두 번 사용해야 한다.**

**Muốn truy vấn tên cấp trên của một nhân viên thì phải sử dụng bảng nhân viên hai lần.**

```sql
SELECT e.이름 AS 직원이름,
       m.이름 AS 상사이름
FROM 직원 e
LEFT JOIN 직원 m
  ON e.상사ID = m.직원ID;
```

Giải thích:

- `e`: bảng đại diện cho nhân viên.
- `m`: bảng đại diện cho cấp trên.
- `e.상사ID = m.직원ID`: cấp trên của nhân viên là nhân viên có ID tương ứng.

Kết quả:

| 직원이름 | 상사이름 |
| --- | --- |
| 나사장 | NULL |
| 김철수 | 나사장 |
| 이지현 | 나사장 |
| 황수지 | 김철수 |
| 박현석 | 이지현 |

**자기 자신을 두 개의 별칭으로 나누어 사용하는 조인을 셀프 조인이라고 한다.**

**JOIN một bảng với chính nó bằng hai bí danh khác nhau gọi là Self JOIN.**

---

Khi gom phần **6.3 SQL Self JOIN** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **6.3 SQL Self JOIN**. Bây giờ chuyển sang **7. 상호 배타적 관계**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **7. 상호 배타적 관계** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** **7. 상호 배타적 관계** nêu quan hệ mutually exclusive; **7. Quan hệ loại trừ lẫn nhau** chuyển nó thành dấu hiệu mô hình và điều kiện kiểm tra để tránh cho phép hai vai trò cùng tồn tại.

## 7. 상호 배타적 관계

Khi gom phần **7. 상호 배타적 관계** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **7. 상호 배타적 관계**. Bây giờ chuyển sang **7. Quan hệ loại trừ lẫn nhau**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **7. Quan hệ loại trừ lẫn nhau** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** Sau khi nắm điều kiện loại trừ và cấu trúc biểu diễn, **KẾT LUẬN GHI NHỚ CUỐI BÀI** gom lại các ranh giới giữa chuẩn hóa, quan hệ, JOIN và self join.

## 7. Quan hệ loại trừ lẫn nhau

Khi gom phần **7. Quan hệ loại trừ lẫn nhau** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **7. Quan hệ loại trừ lẫn nhau**. Bây giờ chuyển sang **7.1 Khái niệm**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **7.1 Khái niệm** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 7.1 Khái niệm

**상호 배타적 관계는 하나의 부모가 여러 자식 중 하나의 자식과만 관계를 가지는 것이다.**

**Quan hệ loại trừ lẫn nhau là quan hệ trong đó một bản ghi cha chỉ có quan hệ với một trong nhiều loại bản ghi con.**

Trong hình có:

```
개인고객
법인고객
주문
```

Một `주문` có thể thuộc về:

- Một `개인고객`, hoặc
- Một `법인고객`.

Nhưng không thể đồng thời thuộc về cả hai.

**주문은 개인고객 또는 법인고객 중 하나만 참조할 수 있다.**

**Một đơn hàng chỉ có thể tham chiếu đến một trong hai loại: khách hàng cá nhân hoặc khách hàng doanh nghiệp.**

---

Khi gom phần **7.1 Khái niệm** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **7.1 Khái niệm**. Bây giờ chuyển sang **7.2 Cấu trúc trong hình**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **7.2 Cấu trúc trong hình** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 7.2 Cấu trúc trong hình

Bảng `개인고객`:

```
고객번호
개인고객명
```

Bảng `법인고객`:

```
법인번호
법인명
```

Bảng `주문`:

```
주문번호
고객구분코드
개인/법인번호(FK)
```

`고객구분코드` dùng để phân biệt đơn hàng thuộc khách hàng cá nhân hay doanh nghiệp.

Ví dụ:

```
고객구분코드 = 개인
→ 개인고객번호를 참조

고객구분코드 = 법인
→ 법인번호를 참조
```

**고객구분코드에 따라 개인번호 또는 법인번호 중 하나만 유효하다.**

**Tùy vào mã loại khách hàng, chỉ số cá nhân hoặc số doanh nghiệp có hiệu lực.**

Đây chính là tính `Exclusive-OR`.

```
개인 OR 법인
Cá nhân HOẶC doanh nghiệp
```

Không phải:

```
개인 AND 법인
Cá nhân VÀ doanh nghiệp
```

---

Khi gom phần **7.2 Cấu trúc trong hình** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **7.2 Cấu trúc trong hình**. Bây giờ chuyển sang **KẾT LUẬN GHI NHỚ CUỐI BÀI**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **KẾT LUẬN GHI NHỚ CUỐI BÀI** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** **KẾT LUẬN GHI NHỚ CUỐI BÀI** chốt phần quan hệ và identifier; **제3절 모델이 표현하는 트랜잭션의 이해** chuyển cùng khung đối tượng–điều kiện–kết quả sang tính toàn vẹn của transaction.

## KẾT LUẬN GHI NHỚ CUỐI BÀI

Khi gom phần **KẾT LUẬN GHI NHỚ CUỐI BÀI** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **KẾT LUẬN GHI NHỚ CUỐI BÀI**. Bây giờ chuyển sang **1. 반정규화**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **1. 반정규화** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 1. 반정규화

**반정규화는 조회 성능을 위해 중복을 허용하고 JOIN을 줄이는 방법이다.**

**Phi chuẩn hóa là cách cho phép trùng lặp và giảm JOIN để cải thiện hiệu năng truy vấn.**

Nhưng phải nhớ:

```
조회 성능 ↑ 가능
입력/수정/삭제 성능 ↓ 가능
유연성 ↓ 가능
```

---

Khi gom phần **1. 반정규화** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **1. 반정규화**. Bây giờ chuyển sang **2. 관계**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **2. 관계** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 2. 관계

Phần này nối mạch SQL với “2. 관계”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

| 한국어 | English | Nghĩa |
| --- | --- | --- |
| 존재 관계 | Existence Relationship | Quan hệ tồn tại |
| 행위 관계 | Action Relationship | Quan hệ hành vi |
| 식별관계 | Identifying Relationship | Quan hệ định danh |
| 비식별관계 | Non-identifying Relationship | Quan hệ không định danh |
| 상호 배타적 관계 | Exclusive-OR Relationship | Quan hệ loại trừ lẫn nhau |

---

Khi gom phần **2. 관계** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **2. 관계**. Bây giờ chuyển sang **3. JOIN**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **3. JOIN** bằng câu hỏi: **ta đang kết hợp những tập hàng nào, cột nào làm cầu nối và điều kiện nối làm thay đổi kết quả ra sao?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 3. JOIN

**조인은 공통 속성인 JOIN KEY를 이용해 여러 테이블의 데이터를 결합하는 것이다.**

**JOIN là kết hợp dữ liệu của nhiều bảng bằng thuộc tính chung gọi là JOIN KEY.**

Ví dụ:

```sql
ON 사원.부서번호 = 부서.부서번호
```

---

Khi gom phần **3. JOIN** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **3. JOIN**. Bây giờ chuyển sang **4. Self JOIN**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **4. Self JOIN** bằng câu hỏi: **ta đang kết hợp những tập hàng nào, cột nào làm cầu nối và điều kiện nối làm thay đổi kết quả ra sao?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 4. Self JOIN

**셀프 조인은 하나의 테이블을 서로 다른 별칭으로 두 번 사용하여 자기 자신과 JOIN하는 것이다.**

**Self JOIN là JOIN một bảng với chính nó bằng hai bí danh khác nhau.**

Ví dụ thường gặp:

- Nhân viên - cấp trên.
- Danh mục cha - danh mục con.
- Bình luận cha - bình luận trả lời.
- Cấu trúc thư mục.

---

Khi gom phần **4. Self JOIN** lại, ta không cần nhớ các dòng như những mảnh rời: ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **4. Self JOIN**. Bây giờ chuyển sang **5. Câu ghi nhớ cuối bài**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **5. Câu ghi nhớ cuối bài** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 5. Câu ghi nhớ cuối bài

Phần này nối mạch SQL với “5. Câu ghi nhớ cuối bài”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```
정규화하면 JOIN 증가
→ JOIN KEY로 테이블 연결
→ 같은 테이블끼리 연결하면 SELF JOIN
→ 여러 자식 중 하나만 연결하면 EXCLUSIVE-OR
```

**Chuẩn hóa làm tăng JOIN; các bảng được kết nối bằng JOIN KEY; cùng một bảng JOIN với chính nó là Self JOIN; chỉ được kết nối với một trong nhiều loại con là Exclusive-OR.**
---

Khi gom phần **5. Câu ghi nhớ cuối bài** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **5. Câu ghi nhớ cuối bài**. Bây giờ chuyển sang **제3절 모델이 표현하는 트랜잭션의 이해**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **제3절 모델이 표현하는 트랜잭션의 이해** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** Sau phần tổng kết quan hệ và identifier, **제3절 모델이 표현하는 트랜잭션의 이해** đặt transaction vào mô hình; **Phần 3 — Hiểu Transaction được biểu diễn trong mô hình dữ liệu** chuyển khái niệm đó thành các bước và điều kiện kiểm chứng.

## 제3절 모델이 표현하는 트랜잭션의 이해

Khi gom phần **제3절 모델이 표현하는 트랜잭션의 이해** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **제3절 모델이 표현하는 트랜잭션의 이해**. Bây giờ chuyển sang **Phần 3 — Hiểu Transaction được biểu diễn trong mô hình dữ liệu**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Phần 3 — Hiểu Transaction được biểu diễn trong mô hình dữ liệu** bằng câu hỏi: **thay đổi nào tác động lên hàng dữ liệu, phạm vi nào bị ảnh hưởng và khi nào thay đổi được xác nhận?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** **제3절 모델이 표현하는 트랜잭션의 이해** nêu phạm vi của transaction; **Phần 3 — Hiểu Transaction được biểu diễn trong mô hình dữ liệu** bắt đầu bằng nguyên tắc toàn bộ thao tác cùng thành công hoặc cùng bị hủy.

## Phần 3 — Hiểu Transaction được biểu diễn trong mô hình dữ liệu

Khi gom phần **Phần 3 — Hiểu Transaction được biểu diễn trong mô hình dữ liệu** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Phần 3 — Hiểu Transaction được biểu diễn trong mô hình dữ liệu**. Bây giờ chuyển sang **1. 트랜잭션(Transaction)이란?**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **1. 트랜잭션(Transaction)이란?** bằng câu hỏi: **thay đổi nào tác động lên hàng dữ liệu, phạm vi nào bị ảnh hưởng và khi nào thay đổi được xác nhận?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 1. 트랜잭션(Transaction)이란?

> **트랜잭션은 업무 처리를 위한 논리적인 작업 단위이다.**
Transaction là **một đơn vị công việc logic để xử lý một nghiệp vụ**.
>

Khi gom phần **1. 트랜잭션(Transaction)이란?** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **1. 트랜잭션(Transaction)이란?**. Bây giờ chuyển sang **Keyword: 트랜잭션 — Transaction — Giao dịch**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 트랜잭션 — Transaction — Giao dịch** bằng câu hỏi: **thay đổi nào tác động lên hàng dữ liệu, phạm vi nào bị ảnh hưởng và khi nào thay đổi được xác nhận?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 트랜잭션 — Transaction — Giao dịch

Điểm quan trọng nhất là đừng hiểu `Transaction = một câu SQL`.

Một transaction có thể chứa:

```sql
SELECT ...
UPDATE ...
INSERT ...
DELETE ...
```

Nhiều câu SQL có thể cùng phục vụ **một nghiệp vụ duy nhất**, nên chúng được gom lại thành **một transaction**.

Ví dụ nghiệp vụ:

> A chuyển 1 triệu won cho B.
>

Về mặt nghiệp vụ, đây là **một việc duy nhất**.

Nhưng DB phải thực hiện nhiều bước:

```
A → B chuyển 1 triệu

① Kiểm tra A có đủ tiền
② Trừ A 1 triệu
③ Cộng B 1 triệu
```

Có thể tưởng tượng SQL:

```sql
SELECT balance
FROM account
WHERE customer_id = 'A';

UPDATE account
SET balance = balance - 1000000
WHERE customer_id = 'A';

UPDATE account
SET balance = balance + 1000000
WHERE customer_id = 'B';

COMMIT;
```

Ba câu SQL khác nhau, nhưng xét về nghiệp vụ:

```
[      ONE TRANSACTION       ]

check A
   ↓
-1,000,000 A
   ↓
+1,000,000 B
   ↓
COMMIT
```

---

Khi gom phần **Keyword: 트랜잭션 — Transaction — Giao dịch** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 트랜잭션 — Transaction — Giao dịch**. Bây giờ chuyển sang **2. 트랜잭션은 모두 성공하거나 모두 취소되어야 한다**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **2. 트랜잭션은 모두 성공하거나 모두 취소되어야 한다** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** Sau nguyên tắc all-or-nothing ở **2. 트랜잭션은 모두 성공하거나 모두 취소되어야 한다**, **3. 왜 ERD에서 트랜잭션이 중요한가?** giải thích vì sao ranh giới transaction phải được phản ánh trong ERD.

## 2. 트랜잭션은 모두 성공하거나 모두 취소되어야 한다

> **하나의 트랜잭션에 속한 동작들은 모두 성공하거나, 모두 취소(UNDO)되어야 한다.**
Các thao tác thuộc cùng một transaction phải **hoặc thành công toàn bộ, hoặc bị hủy toàn bộ**.
>

Đây chính là:

Khi gom phần **2. 트랜잭션은 모두 성공하거나 모두 취소되어야 한다** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **2. 트랜잭션은 모두 성공하거나 모두 취소되어야 한다**. Bây giờ chuyển sang **All or Nothing**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **All or Nothing** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### All or Nothing

Ví dụ A có:

```
A = 5,000,000
B = 2,000,000
```

Chuyển 1 triệu:

```
A: 5M → 4M
B: 2M → 3M
```

Đúng.

Nhưng giả sử:

```
① A -1M     SUCCESS
② B +1M     ERROR
```

DB không được để:

```
A = 4M
B = 2M
```

vì 1 triệu đã “biến mất”.

Ngược lại cũng không được:

```
A = 5M
B = 3M
```

vì tiền tự nhiên xuất hiện.

Vì vậy:

```
① A -1M
② B +1M
      │
      ├── tất cả SUCCESS → COMMIT
      │
      └── có lỗi         → ROLLBACK
```

Khi gom phần **All or Nothing** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **All or Nothing**. Bây giờ chuyển sang **COMMIT**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

**COMMIT** là dữ liệu đầu vào của phép suy luận, không phải một khái niệm cần học tách khỏi truy vấn. Hãy đọc các cột và hàng để trả lời: **bảng này đang cung cấp những cột và hàng nào, khóa nào sẽ làm cầu nối, và dữ liệu thiếu sẽ ảnh hưởng kết quả ra sao?**

#### COMMIT

> **COMMIT은 트랜잭션의 변경사항을 확정한다.**
COMMIT xác nhận và làm cho các thay đổi của transaction được hoàn tất.
>

Khi gom phần **COMMIT** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **COMMIT**. Bây giờ chuyển sang **ROLLBACK**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

**ROLLBACK** là dữ liệu đầu vào của phép suy luận, không phải một khái niệm cần học tách khỏi truy vấn. Hãy đọc các cột và hàng để trả lời: **bảng này đang cung cấp những cột và hàng nào, khóa nào sẽ làm cầu nối, và dữ liệu thiếu sẽ ảnh hưởng kết quả ra sao?**

#### ROLLBACK

> **ROLLBACK은 트랜잭션에서 발생한 변경사항을 취소한다.**
ROLLBACK hủy các thay đổi xảy ra trong transaction.
>

Đây là ý trong ảnh:

> **부분 COMMIT 불가, 동시 COMMIT이나 ROLLBACK으로 처리**
Không được commit từng phần; toàn bộ nghiệp vụ phải được xử lý thống nhất bằng COMMIT hoặc ROLLBACK.
>

---

Khi gom phần **ROLLBACK** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **ROLLBACK**. Bây giờ chuyển sang **3. 왜 ERD에서 트랜잭션이 중요한가?**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **3. 왜 ERD에서 트랜잭션이 중요한가?** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** **3. 왜 ERD에서 트랜잭션이 중요한가?** nối tính nguyên tử với cấu trúc quan hệ; **Tại sao Transaction lại liên quan đến ERD?** diễn giải cùng câu hỏi để người học nhận ra boundary của nghiệp vụ.

## 3. 왜 ERD에서 트랜잭션이 중요한가?

Khi gom phần **3. 왜 ERD에서 트랜잭션이 중요한가?** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **3. 왜 ERD에서 트랜잭션이 중요한가?**. Bây giờ chuyển sang **Tại sao Transaction lại liên quan đến ERD?**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Tại sao Transaction lại liên quan đến ERD?** bằng câu hỏi: **thay đổi nào tác động lên hàng dữ liệu, phạm vi nào bị ảnh hưởng và khi nào thay đổi được xác nhận?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** Sau khi thấy transaction gắn với quan hệ nghiệp vụ, **4. 필수적 관계 vs 선택적 관계** hỏi một phía có bắt buộc phải tham gia hay có thể vắng mặt trong quan hệ đó.

## Tại sao Transaction lại liên quan đến ERD?

Đây là đoạn rất dễ đọc qua nhưng lại quan trọng trong SQLD.

> **두 엔터티의 관계가 서로 필수적일 때 하나의 트랜잭션을 형성한다.**
Khi quan hệ giữa hai entity mang tính bắt buộc với nhau trong nghiệp vụ, chúng có xu hướng cùng tham gia một transaction.
>

Ví dụ:

```
고객 ───── 주문
Customer    Order
```

Nếu nghiệp vụ yêu cầu một `주문` phải gắn với một `고객`, thì quan hệ đó mang tính bắt buộc ở phía tương ứng.

Ngược lại:

> **두 엔터티가 서로 독립적인 수행이 가능하다면 선택적 관계로 표현한다.**
Nếu nghiệp vụ của hai entity có thể diễn ra độc lập thì quan hệ có thể được biểu diễn dưới dạng optional.
>

---

Khi gom phần **Tại sao Transaction lại liên quan đến ERD?** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Tại sao Transaction lại liên quan đến ERD?**. Bây giờ chuyển sang **4. 필수적 관계 vs 선택적 관계**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **4. 필수적 관계 vs 선택적 관계** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** **4. 필수적 관계 vs 선택적 관계** xác định cardinality và participation; **5. IE와 Barker 표기법** chuyển các ràng buộc ấy thành ký pháp để đọc trực tiếp trên ERD.

## 4. 필수적 관계 vs 선택적 관계

Khi gom phần **4. 필수적 관계 vs 선택적 관계** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **4. 필수적 관계 vs 선택적 관계**. Bây giờ chuyển sang **필수적 관계 — Mandatory Relationship**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **필수적 관계 — Mandatory Relationship** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 필수적 관계 — Mandatory Relationship

> **관계가 반드시 존재해야 한다.**
Quan hệ bắt buộc phải tồn tại.
>

Ví dụ:

```
주문 → 고객
Order → Customer
```

Nếu quy tắc nghiệp vụ nói:

> 주문은 반드시 고객에게 속한다.
Mỗi đơn hàng bắt buộc phải thuộc về một khách hàng.
>

thì phía đó là mandatory.

---

Khi gom phần **필수적 관계 — Mandatory Relationship** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **필수적 관계 — Mandatory Relationship**. Bây giờ chuyển sang **선택적 관계 — Optional Relationship**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **선택적 관계 — Optional Relationship** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 선택적 관계 — Optional Relationship

> **관계가 없어도 엔터티 인스턴스가 존재할 수 있다.**
Một instance của entity vẫn có thể tồn tại dù chưa có quan hệ đó.
>

Ví dụ:

```
고객
Pham
```

Pham vừa đăng ký tài khoản nhưng chưa từng đặt hàng.

Vậy:

```
Customer → Order

0..N
```

Một customer có thể có:

```
0 order
1 order
N orders
```

---

Khi gom phần **선택적 관계 — Optional Relationship** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **선택적 관계 — Optional Relationship**. Bây giờ chuyển sang **5. IE와 Barker 표기법**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **5. IE와 Barker 표기법** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** Sau khi đọc quan hệ bắt buộc/tùy chọn bằng IE và Barker, **6. 트랜잭션의 특징 — ACID** quay lại hệ quả vận hành: dữ liệu phải giữ tính nguyên tử, nhất quán, cô lập và bền vững.

## 5. IE와 Barker 표기법

Ảnh của bạn nhấn mạnh sự khác nhau về ký hiệu.

Khi gom phần **5. IE와 Barker 표기법** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **5. IE와 Barker 표기법**. Bây giờ chuyển sang **IE 표기법**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **IE 표기법** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### IE 표기법

> **필수적 관계: 원 X**
Quan hệ bắt buộc: không có vòng tròn.
>

> **선택적 관계: 원 O**
Quan hệ optional: có vòng tròn `○`.
>

Có thể nhớ:

```
○ = zero allowed
```

Có vòng tròn nghĩa là:

```
0개도 가능
0 cũng được
→ optional
```

Khi gom phần **IE 표기법** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **IE 표기법**. Bây giờ chuyển sang **Barker 표기법**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Barker 표기법** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Barker 표기법

> **필수적 관계: 실선의 관계선**
Mandatory → đường liền.
>

> **선택적 관계: 점선의 관계선**
Optional → đường đứt.
>

Mẹo thi:

```
IE
○ → Optional

Barker
------  solid  → Mandatory
- - - - dashed → Optional
```

---

Khi gom phần **Barker 표기법** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Barker 표기법**. Bây giờ chuyển sang **6. 트랜잭션의 특징 — ACID**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **6. 트랜잭션의 특징 — ACID** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** **6. 트랜잭션의 특징 — ACID** nêu đủ bốn thuộc tính; **7. ② 일관성 Consistency — Tính nhất quán** đi sâu vào điều kiện trước và sau transaction để xác định dữ liệu vẫn hợp lệ.

## 6. 트랜잭션의 특징 — ACID

Ảnh tiếp theo đưa ra 4 thuộc tính cực kỳ quan trọng:

```
A → Atomicity
C → Consistency
I → Isolation
D → Durability
```

Đây chính là **ACID**.

---

Khi gom phần **6. 트랜잭션의 특징 — ACID** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **6. 트랜잭션의 특징 — ACID**. Bây giờ chuyển sang **① 원자성 Atomicity — Tính nguyên tử**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **① 원자성 Atomicity — Tính nguyên tử** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### ① 원자성 Atomicity — Tính nguyên tử

> **트랜잭션은 더 이상 분해가 불가능한 업무의 최소단위이다.**
Transaction được xem là đơn vị nghiệp vụ nhỏ nhất không thể chia nhỏ thêm khi xét tính hoàn thành.
>

> **전부 처리되거나 모두 처리되지 않아야 한다.**
Hoặc toàn bộ được thực hiện, hoặc toàn bộ không được thực hiện.
>

Chính là:

```
ALL OR NOTHING
```

Ví dụ:

```
A - 1M
B + 1M
```

Không được:

```
A -1M ✓
B +1M ✗
```

Mà phải:

```
✓ ✓ → COMMIT

hoặc

✗ → ROLLBACK toàn bộ
```

Khi gom phần **① 원자성 Atomicity — Tính nguyên tử** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **① 원자성 Atomicity — Tính nguyên tử**. Bây giờ chuyển sang **Keyword nhớ nhanh**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword nhớ nhanh** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword nhớ nhanh

Phần này nối mạch SQL với “Keyword nhớ nhanh”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```
Atomicity
= 원자성
= All or Nothing
= COMMIT / ROLLBACK
```

---

Khi gom phần **Keyword nhớ nhanh** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword nhớ nhanh**. Bây giờ chuyển sang **7. ② 일관성 Consistency — Tính nhất quán**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **7. ② 일관성 Consistency — Tính nhất quán** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** Từ consistency trong **6. 트랜잭션의 특징 — ACID**, **8. ③ 격리성 Isolation — Tính cô lập** chuyển sang câu hỏi các transaction đồng thời được phép nhìn thấy thay đổi của nhau đến mức nào.

## 7. ② 일관성 Consistency — Tính nhất quán

> **트랜잭션이 성공적으로 완료된 후에도 DB는 일관된 상태여야 한다.**
Sau khi transaction hoàn tất thành công, database vẫn phải ở trạng thái nhất quán.
>

Điểm cốt lõi:

```
DB hợp lệ
   ↓
Transaction
   ↓
DB vẫn hợp lệ
```

Ví dụ trước chuyển tiền:

```
A = 5M
B = 2M

Total = 7M
```

Sau:

```
A = 4M
B = 3M

Total = 7M
```

Các ràng buộc nghiệp vụ vẫn đúng.

Consistency không chỉ là tiền. Nó còn liên quan tới:

```
PK
FK
UNIQUE
CHECK
NOT NULL
Business Rule
```

Ví dụ:

```sql
CHECK (balance >= 0)
```

Nếu transaction khiến:

```
balance = -1,000,000
```

trong khi hệ thống cấm số dư âm, thì trạng thái DB không còn thỏa quy tắc.

Khi gom phần **7. ② 일관성 Consistency — Tính nhất quán** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **7. ② 일관성 Consistency — Tính nhất quán**. Bây giờ chuyển sang **Nhớ:**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Nhớ:** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Nhớ:

Phần này nối mạch SQL với “Nhớ:”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```
Consistency
= trước hợp lệ
→ transaction
→ sau vẫn hợp lệ
```

---

Khi gom phần **Nhớ:** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Nhớ:**. Bây giờ chuyển sang **8. ③ 격리성 Isolation — Tính cô lập**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **8. ③ 격리성 Isolation — Tính cô lập** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** **8. ③ 격리성 Isolation — Tính cô lập** kiểm soát tương tác khi đang chạy; **9. ④ 영속성 / 지속성 Durability — Tính bền vững** hỏi điều gì còn tồn tại sau commit và sự cố hệ thống.

## 8. ③ 격리성 Isolation — Tính cô lập

> **실행 중인 트랜잭션의 중간결과를 다른 트랜잭션이 접근할 수 없다.**
Transaction khác không được tùy ý nhìn thấy/kế thừa trạng thái trung gian chưa hoàn tất của transaction đang chạy.
>

Giả sử:

```
Transaction A

UPDATE balance - 1M
...
chưa COMMIT
```

Transaction B không nên dựa vào trạng thái chưa hoàn tất đó như thể nó đã được xác nhận.

Có thể hình dung:

```
T1: A -1M ---------------- COMMIT
         ↑
         │ trạng thái trung gian
         │
T2: không nên nhìn nó như dữ liệu đã hoàn tất
```

Đây là lý do xuất hiện các vấn đề concurrency như:

```
Dirty Read
Non-repeatable Read
Phantom Read
```

và các mức:

```
READ UNCOMMITTED
READ COMMITTED
REPEATABLE READ
SERIALIZABLE
```

SQLD ở đoạn này chủ yếu cần nhớ bản chất:

> **Isolation = các transaction đang chạy phải được cách ly thích hợp với nhau.**
>

---

Khi gom phần **8. ③ 격리성 Isolation — Tính cô lập** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **8. ③ 격리성 Isolation — Tính cô lập**. Bây giờ chuyển sang **9. ④ 영속성 / 지속성 Durability — Tính bền vững**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **9. ④ 영속성 / 지속성 Durability — Tính bền vững** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** Sau khi tách cô lập khỏi bền vững, **⭐ Tổng hợp ACID cực dễ nhớ** gom bốn thuộc tính theo câu hỏi: transaction làm trọn vẹn gì, giữ điều kiện nào, che thay đổi ra sao và ghi kết quả ở đâu.

## 9. ④ 영속성 / 지속성 Durability — Tính bền vững

> **트랜잭션이 성공적으로 완료되면 결과는 데이터베이스에 영속적으로 저장된다.**
Khi transaction đã hoàn tất thành công, kết quả phải được lưu bền vững trong database.
>

Tức là:

```
COMMIT 완료
    ↓
결과 유지
```

Ví dụ bạn chuyển tiền thành công.

Sau đó:

```
server restart
```

thì không được quay lại:

```
A = 5M
B = 2M
```

mà phải giữ:

```
A = 4M
B = 3M
```

---

Khi gom phần **9. ④ 영속성 / 지속성 Durability — Tính bền vững** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **9. ④ 영속성 / 지속성 Durability — Tính bền vững**. Bây giờ chuyển sang **⭐ Tổng hợp ACID cực dễ nhớ**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **⭐ Tổng hợp ACID cực dễ nhớ** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** **⭐ Tổng hợp ACID cực dễ nhớ** khép mô hình transaction; **제4절 NULL 속성의 이해** chuyển sang semantics của giá trị thiếu, nơi phép tính và điều kiện không còn giống giá trị thông thường.

## ⭐ Tổng hợp ACID cực dễ nhớ

Phần này nối mạch SQL với “⭐ Tổng hợp ACID cực dễ nhớ”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

| Korean | English | Ý chính |
| --- | --- | --- |
| 원자성 | Atomicity | All or Nothing |
| 일관성 | Consistency | Trước/sau đều hợp lệ |
| 격리성 | Isolation | Transaction không can thiệp trạng thái trung gian của nhau |
| 영속성 | Durability | COMMIT rồi thì phải được giữ |

Nhớ chuỗi:

```
Atomicity   → Có làm hết không?
Consistency → Kết quả có hợp lệ không?
Isolation   → Transaction khác có gây/nhìn thấy ảnh hưởng trung gian không?
Durability  → Commit rồi có giữ được không?
```

---

Khi gom phần **⭐ Tổng hợp ACID cực dễ nhớ** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **⭐ Tổng hợp ACID cực dễ nhớ**. Bây giờ chuyển sang **제4절 NULL 속성의 이해**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **제4절 NULL 속성의 이해** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** Sau phần tổng hợp ACID, **제4절 NULL 속성의 이해** giới thiệu NULL như một trạng thái “chưa biết/không có giá trị”; **Phần 4 — NULL** sẽ đưa semantics đó vào truy vấn.

## 제4절 NULL 속성의 이해

Khi gom phần **제4절 NULL 속성의 이해** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **제4절 NULL 속성의 이해**. Bây giờ chuyển sang **Phần 4 — NULL**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Phần 4 — NULL** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** **Phần 4 — NULL** đã xác định NULL không phải chuỗi rỗng hay số 0; **11. NULL trong phép toán** kiểm tra cách trạng thái chưa biết lan qua toán tử và biểu thức.

## Phần 4 — NULL

Đây là phần **rất dễ bị gài trong SQLD**.

Khi gom phần **Phần 4 — NULL** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Phần 4 — NULL**. Bây giờ chuyển sang **10. NULL là gì?**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **10. NULL là gì?** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 10. NULL là gì?

> **NULL은 아직 정의되지 않은 값이다.**
NULL là giá trị **chưa được xác định / không biết / không tồn tại theo ngữ cảnh**, chứ không phải một giá trị thông thường.
>

Trong ảnh:

> **NULL은 0 또는 공백과 다르다.**
NULL khác `0` và khác chuỗi rỗng/khoảng trắng.
>

Đây là điểm bắt buộc phải nhớ:

```
NULL ≠ 0
NULL ≠ ' '
```

Về mặt khái niệm:

```
0
→ biết giá trị
→ giá trị chính xác là zero

NULL
→ không biết/chưa có giá trị
```

Ví dụ:

```
나이 = 0
```

nghĩa là biết tuổi bằng 0.

Nhưng:

```
나이 = NULL
```

nghĩa là:

> Không biết tuổi / chưa nhập tuổi.
>

---

Khi gom phần **10. NULL là gì?** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **10. NULL là gì?**. Bây giờ chuyển sang **11. NULL trong phép toán**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **11. NULL trong phép toán** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** Sau khi thấy NULL lan truyền trong biểu thức, **12. NVL và ISNULL** chuyển sang cách thay thế giá trị để biến kết quả chưa biết thành giá trị có thể trình bày hoặc tính tiếp.

## 11. NULL trong phép toán

> **NULL 값을 포함하는 연산의 결과값도 NULL 값이다.**
Phép toán có NULL thường cho kết quả NULL.
>

Ví dụ:

```sql
10 + NULL
```

→

```
NULL
```

Tại sao?

Bởi vì:

```
10 + một giá trị không biết
```

thì kết quả cũng:

```
không biết
```

Tương tự:

```
NULL + 100 → NULL
NULL - 10  → NULL
NULL * 2   → NULL
```

---

Khi gom phần **11. NULL trong phép toán** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **11. NULL trong phép toán**. Bây giờ chuyển sang **12. NVL và ISNULL**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **12. NVL và ISNULL** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** **12. NVL và ISNULL** cho phép đặt giá trị thay thế theo dialect; **13. NULL không được so sánh bằng =** quay lại nguyên tắc ba giá trị để giải thích vì sao `=` không thể tìm NULL.

## 12. NVL và ISNULL

Trong Oracle:

```sql
NVL(column, replacement)
```

Ví dụ:

```sql
NVL(C, 0)
```

> **컬럼 C의 NULL 값을 0으로 치환한다.**
Thay NULL trong cột C bằng 0.
>

Ví dụ:

```
C
----
10
NULL
20
```

```sql
SELECT NVL(C, 0)
```

→

```
10
0
20
```

Lưu ý SQLD thường xoay quanh Oracle, vì vậy hãy nhớ mạnh:

```sql
NVL()
```

`ISNULL()` phổ biến ở SQL Server.

---

Khi gom phần **12. NVL và ISNULL** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **12. NVL và ISNULL**. Bây giờ chuyển sang **13. NULL không được so sánh bằng =**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **13. NULL không được so sánh bằng =** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** Sau khi thấy `NULL = NULL` không cho kết quả TRUE, **14. NULL trong Aggregate Function** kiểm tra một ngữ cảnh khác: hàm tổng hợp bỏ qua hay giữ NULL trong phép tính.

## 13. NULL không được so sánh bằng =

Đây là câu cực quan trọng trong ảnh:

> **NULL과의 모든 비교(IS NULL 제외)는 알 수 없음(UNKNOWN)을 반환한다.**
Các phép so sánh thông thường với NULL trả về UNKNOWN, ngoại trừ kiểm tra `IS NULL`/`IS NOT NULL`.
>

Sai:

```sql
WHERE column = NULL
```

Đúng:

```sql
WHERE column IS NULL
```

Và:

```sql
WHERE column IS NOT NULL
```

---

Khi gom phần **13. NULL không được so sánh bằng =** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **13. NULL không được so sánh bằng =**. Bây giờ chuyển sang **Tại sao `NULL = NULL` không phải TRUE?**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Tại sao `NULL = NULL` không phải TRUE?** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### Tại sao `NULL = NULL` không phải TRUE?

Vì NULL nghĩa là:

```
unknown
```

Ví dụ:

```
A = NULL
B = NULL
```

Bạn không biết A.

Bạn cũng không biết B.

Không có nghĩa:

```
A = B
```

Ví dụ thực tế:

```
A tuổi = không biết
B tuổi = không biết
```

Không thể kết luận:

```
A và B bằng tuổi nhau
```

Do đó:

```sql
NULL = NULL
```

không trả về `TRUE`.

Trong logic SQL:

```
TRUE
FALSE
UNKNOWN
```

được gọi là **Three-Valued Logic — 3VL**.

---

Khi gom phần **Tại sao `NULL = NULL` không phải TRUE?** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Tại sao `NULL = NULL` không phải TRUE?**. Bây giờ chuyển sang **14. NULL trong Aggregate Function**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **14. NULL trong Aggregate Function** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** **14. NULL trong Aggregate Function** cho thấy mỗi hàm có quy tắc xử lý NULL riêng; **15. COUNT() khác COUNT(column)** tập trung vào khác biệt dễ thi nhất giữa đếm dòng và đếm giá trị không NULL.

## 14. NULL trong Aggregate Function

Ảnh có bảng:

```
컬럼1    컬럼2
10       20
20       NULL
```

Hãy tính.

Khi gom phần **14. NULL trong Aggregate Function** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **14. NULL trong Aggregate Function**. Bây giờ chuyển sang **COUNT(column)**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **COUNT(column)** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### COUNT(column)

Phần này nối mạch SQL với “COUNT(column)”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```sql
COUNT(column1)
```

→ `2`

```sql
COUNT(column2)
```

→ `1`

Vì:

> **COUNT(column)은 NULL을 제외한다.**
COUNT(column) bỏ qua NULL.
>

---

Khi gom phần **COUNT(column)** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **COUNT(column)**. Bây giờ chuyển sang **SUM**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

**SUM** là dữ liệu đầu vào của phép suy luận, không phải một khái niệm cần học tách khỏi truy vấn. Hãy đọc các cột và hàng để trả lời: **bảng này đang cung cấp những cột và hàng nào, khóa nào sẽ làm cầu nối, và dữ liệu thiếu sẽ ảnh hưởng kết quả ra sao?**

#### SUM

Phần này nối mạch SQL với “SUM”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```sql
SUM(column1)
= 10 + 20
= 30
```

```sql
SUM(column2)
= 20
```

NULL bị bỏ qua.

---

Khi gom phần **SUM** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **SUM**. Bây giờ chuyển sang **AVG**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

**AVG** là dữ liệu đầu vào của phép suy luận, không phải một khái niệm cần học tách khỏi truy vấn. Hãy đọc các cột và hàng để trả lời: **bảng này đang cung cấp những cột và hàng nào, khóa nào sẽ làm cầu nối, và dữ liệu thiếu sẽ ảnh hưởng kết quả ra sao?**

#### AVG

Đây là chỗ cực dễ sai.

```sql
AVG(column2)
```

không phải:

```
(20 + 0) / 2
= 10 ❌
```

Mà là:

```
20 / 1
= 20 ✓
```

Vì:

> **집계 함수에서 NULL은 0이 아니라 계산 대상에서 제외된다.**
Trong aggregate function, NULL không được xem là 0 mà bị loại khỏi tập tính toán.
>

---

Khi gom phần **AVG** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **AVG**. Bây giờ chuyển sang **15. COUNT(*) khác COUNT(column)**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **15. COUNT(*) khác COUNT(column)** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** Sau khi phân biệt `COUNT(*)` với `COUNT(column)`, **16. Nếu column là PK?** hỏi điều kiện nào khiến hai kết quả trùng nhau: cột khóa chính không chứa NULL.

## 15. COUNT(*) khác COUNT(column)

Phần này nối mạch SQL với “15. COUNT(*) khác COUNT(column)”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```sql
COUNT(*)
```

> **NULL 여부와 관계없이 행 자체를 센다.**
Đếm số dòng, bất kể trong dòng có NULL hay không.
>

Trong bảng:

```
row 1
row 2
```

→

```sql
COUNT(*) = 2
```

Nhưng:

```sql
COUNT(column2) = 1
```

Vì row thứ hai:

```
column2 = NULL
```

Do đó:

```
COUNT(*)       → đếm ROW
COUNT(column)  → đếm NON-NULL
```

Khi gom phần **15. COUNT(*) khác COUNT(column)** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **15. COUNT(*) khác COUNT(column)**. Bây giờ chuyển sang **⭐ Đây là một công thức SQLD rất đáng nhớ**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **⭐ Đây là một công thức SQLD rất đáng nhớ** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### ⭐ Đây là một công thức SQLD rất đáng nhớ

Phần này nối mạch SQL với “⭐ Đây là một công thức SQLD rất đáng nhớ”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```
COUNT(*) = 모든 행
COUNT(col) = NULL 제외
```

---

Khi gom phần **⭐ Đây là một công thức SQLD rất đáng nhớ** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **⭐ Đây là một công thức SQLD rất đáng nhớ**. Bây giờ chuyển sang **16. Nếu column là PK?**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **16. Nếu column là PK?** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** **16. Nếu column là PK?** dùng constraint để giải thích trường hợp đếm bằng nhau; **17. Trung bình trên toàn bộ số dòng** mở rộng câu hỏi sang mẫu số khi tính trung bình có NULL.

## 16. Nếu column là PK?

Ảnh ghi:

> **컬럼이 PK라면 NULL값 허용 X → 항상 COUNT(*) = COUNT(컬럼)**
Nếu column là PK thì không cho phép NULL, vì vậy COUNT(*) luôn bằng COUNT(column) trên bảng đó.
>

Vì:

```
PRIMARY KEY
= UNIQUE
+ NOT NULL
```

Cho nên:

```sql
COUNT(*)
```

và:

```sql
COUNT(pk_column)
```

sẽ bằng nhau.

---

Khi gom phần **16. Nếu column là PK?** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **16. Nếu column là PK?**. Bây giờ chuyển sang **17. Trung bình trên toàn bộ số dòng**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **17. Trung bình trên toàn bộ số dòng** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** Sau khi xác định mẫu số khi tính trung bình có NULL, **18. NULL의 ERD 표기법** chuyển sang cách biểu diễn khả năng vắng mặt của thuộc tính trong ERD.

## 17. Trung bình trên toàn bộ số dòng

Ảnh nhấn mạnh:

```
전체 행 개수에 대한 평균
= SUM(column) / COUNT(*)
```

Khác với:

```sql
AVG(column)
```

Ví dụ:

```
20
NULL
```

Khi gom phần **17. Trung bình trên toàn bộ số dòng** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **17. Trung bình trên toàn bộ số dòng**. Bây giờ chuyển sang **AVG(column)**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **AVG(column)** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### AVG(column)

Phần này nối mạch SQL với “AVG(column)”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```
20 / 1
= 20
```

Khi gom phần **AVG(column)** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **AVG(column)**. Bây giờ chuyển sang **SUM(column)/COUNT(*)**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **SUM(column)/COUNT(*)** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### SUM(column)/COUNT(*)

Phần này nối mạch SQL với “SUM(column)/COUNT(*)”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```
20 / 2
= 10
```

Hai kết quả hoàn toàn khác nhau.

Đây là dạng bẫy SQLD rất phổ biến.

---

Khi gom phần **SUM(column)/COUNT(*)** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **SUM(column)/COUNT(*)**. Bây giờ chuyển sang **18. NULL의 ERD 표기법**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **18. NULL의 ERD 표기법** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** **18. NULL의 ERD 표기법** nối semantics giá trị thiếu với constraint trên mô hình; **제5절 본질식별자 vs 인조식별자** chuyển sang câu hỏi khóa định danh đến từ dữ liệu nghiệp vụ hay được tạo riêng.

## 18. NULL의 ERD 표기법

Ảnh nói:

Khi gom phần **18. NULL의 ERD 표기법** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **18. NULL의 ERD 표기법**. Bây giờ chuyển sang **IE**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **IE** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### IE

> **NULL 허용 여부 알 수 없음**
Không thể xác định trực tiếp việc attribute có cho phép NULL hay không từ cách biểu diễn attribute như trong hình.
>

Khi gom phần **IE** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **IE**. Bây giờ chuyển sang **Barker**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Barker** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Barker

> **속성 앞 동그라미 표시**
Dùng ký hiệu trước thuộc tính để biểu diễn tính optional.
>

Trong hình Barker:

```

Khi gom phần **Barker** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Barker**. Bây giờ chuyển sang **주문번호**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **주문번호** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

## 주문번호

○ 주문금액
○ 주문취소금액
```

Trong đó `#` liên quan đến identifier/key, còn `○` biểu thị thuộc tính optional.

---

Khi gom phần **주문번호** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **주문번호**. Bây giờ chuyển sang **제5절 본질식별자 vs 인조식별자**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **제5절 본질식별자 vs 인조식별자** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** Sau khi xác định NULL và ràng buộc trong ERD, **제5절 본질식별자 vs 인조식별자** đặt hai chiến lược định danh cạnh nhau; **19. 본질식별자 — Natural/Original Identifier** bắt đầu từ khóa có sẵn trong nghiệp vụ.

## 제5절 본질식별자 vs 인조식별자

Đây là phần tiếp nối trực tiếp kiến thức `식별자` bạn vừa học trước đó.

Khi gom phần **제5절 본질식별자 vs 인조식별자** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **제5절 본질식별자 vs 인조식별자**. Bây giờ chuyển sang **19. 본질식별자 — Natural/Original Identifier**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **19. 본질식별자 — Natural/Original Identifier** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** **19. 본질식별자 — Natural/Original Identifier** cho thấy khóa tự nhiên mang ý nghĩa nghiệp vụ; **20. 인조식별자 — Surrogate Key** đối chiếu với khóa sinh ra chỉ để định danh ổn định.

## 19. 본질식별자 — Natural/Original Identifier

Ảnh dùng:

> **원조(본질) 식별자**
Identifier được hình thành tự nhiên từ nghiệp vụ và cần thiết cho việc phân biệt dữ liệu.
>

Ví dụ:

```
학번
주민등록번호
사번
```

Tức là bản thân nghiệp vụ đã có nó.

Ví dụ:

```
학생

학번
----
20260001
20260002
```

Không phải vì DB cần PK nên ta mới nghĩ ra `학번`; nó vốn có ý nghĩa trong nghiệp vụ trường học.

Có thể liên hệ với thuật ngữ phổ biến:

```
본질식별자
≈ Natural Key / Business Key
```

---

Khi gom phần **19. 본질식별자 — Natural/Original Identifier** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **19. 본질식별자 — Natural/Original Identifier**. Bây giờ chuyển sang **20. 인조식별자 — Surrogate Key**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **20. 인조식별자 — Surrogate Key** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** Sau khi so sánh khóa tự nhiên với surrogate key, **21. Tại sao cần 인조식별자?** kiểm tra các lý do thực dụng: khóa nghiệp vụ dài, thay đổi hoặc khó bảo đảm duy nhất.

## 20. 인조식별자 — Surrogate Key

> **업무에는 존재하지 않지만 편의성을 위해 인위적으로 만든 식별자이다.**
Là identifier không tồn tại tự nhiên trong nghiệp vụ nhưng được tạo nhân tạo để thuận tiện cho hệ thống.
>

Ví dụ:

```
ORDER_DETAIL_ID
USER_ID
SEQ
AUTO_INCREMENT
IDENTITY
```

Ví dụ:

```
주문상세번호
-------------
1
2
3
4
```

`주문상세번호` có thể chẳng có ý nghĩa gì với khách hàng.

Nó chỉ giúp DB nói:

```
đây là row #1
đây là row #2
```

Đó chính là:

```
Surrogate Key
= 인조식별자
```

---

Khi gom phần **20. 인조식별자 — Surrogate Key** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **20. 인조식별자 — Surrogate Key**. Bây giờ chuyển sang **21. Tại sao cần 인조식별자?**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **21. Tại sao cần 인조식별자?** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** **21. Tại sao cần 인조식별자?** nêu vấn đề ổn định và đơn giản của định danh; **22. Giải pháp: 주문상세번호** đưa nguyên tắc ấy vào một khóa chi tiết đơn hàng cụ thể.

## 21. Tại sao cần 인조식별자?

Ảnh đưa ra ví dụ rất hay.

Ban đầu `주문이력` dùng:

```
PK = 주문번호 + 상품번호
```

Tức composite PK:

```
ORDER_ID + PRODUCT_ID
```

Ví dụ:

```
101 + c03
101 + c05
101 + c06
```

Đều khác nhau → OK.

Nhưng vài giờ sau khách thêm lại `c03`:

```
101 + c03
```

Ta có:

```
101 c03 ← lần đầu
101 c05
101 c06
101 c03 ← lần sau
```

PK:

```
(101, c03)
```

bị trùng.

→ `PRIMARY KEY violation`.

---

Khi gom phần **21. Tại sao cần 인조식별자?** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **21. Tại sao cần 인조식별자?**. Bây giờ chuyển sang **22. Giải pháp: 주문상세번호**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **22. Giải pháp: 주문상세번호** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** **22. Giải pháp: 주문상세번호** minh họa surrogate key bằng một định danh ổn định; **23. Nhưng 인조식별자 tạo ra một vấn đề lớn** kiểm tra cái giá phải trả khi khóa kỹ thuật che khuất ý nghĩa nghiệp vụ.

## 22. Giải pháp: 주문상세번호

Ta thêm:

```
주문상세번호
Order Detail ID
```

Ví dụ:

```
주문상세번호 | 주문번호 | 상품번호
---------------------------------
1            101       c03
2            101       c05
3            101       c06
4            101       c03
```

Bây giờ:

```
PK = 주문상세번호
```

nên:

```
1 ≠ 4
```

Hai row được phân biệt.

Đây chính là **인조식별자**.

Có thể sinh bằng Oracle Sequence:

```sql
주문상세번호_SEQ.NEXTVAL
```

Ví dụ:

```sql
INSERT INTO 주문이력
VALUES (주문상세번호_SEQ.NEXTVAL, '101', 'c03', 3, ...);
```

Sequence tự sinh:

```
1
2
3
4
...
```

---

Khi gom phần **22. Giải pháp: 주문상세번호** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **22. Giải pháp: 주문상세번호**. Bây giờ chuyển sang **23. Nhưng 인조식별자 tạo ra một vấn đề lớn**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **23. Nhưng 인조식별자 tạo ra một vấn đề lớn** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** Sau ví dụ 주문상세번호, **23. Nhưng 인조식별자 tạo ra một vấn đề lớn** chuyển từ lợi ích ổn định sang rủi ro song song: vẫn phải bảo toàn quy tắc duy nhất của dữ liệu nghiệp vụ.

## 23. Nhưng 인조식별자 tạo ra một vấn đề lớn

Đây là phần ảnh muốn bạn đặc biệt chú ý.

Khi:

```
PK = 주문상세번호
```

thì DB chỉ kiểm tra:

```
주문상세번호 unique?
```

Ví dụ:

```
ID | ORDER | PRODUCT
--------------------
1  | 101   | c03
2  | 101   | c05
3  | 101   | c06
4  | 101   | c03
```

Về PK:

```
1
2
3
4
```

→ tất cả unique.

Cho nên DB chấp nhận.

Nhưng nếu nghiệp vụ **không cho phép cùng một `(주문번호, 상품번호)` xuất hiện lặp lại**, thì surrogate PK đã che mất business uniqueness đó.

Đây là ý:

> **인조식별자만이 주식별자라 시스템 오류로 인한 중복 데이터의 입력을 막을 수 없다.**
Nếu chỉ dựa vào surrogate identifier làm primary identifier thì có thể không ngăn được duplicate theo business key.
>

---

Khi gom phần **23. Nhưng 인조식별자 tạo ra một vấn đề lớn** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **23. Nhưng 인조식별자 tạo ra một vấn đề lớn**. Bây giờ chuyển sang **24. Đây chính là nhược điểm quan trọng của 인조식별자**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **24. Đây chính là nhược điểm quan trọng của 인조식별자** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** **24. Đây chính là nhược điểm quan trọng của 인조식별자** chốt việc phải giữ business uniqueness; **25. 인조식별자 có thể làm tăng Index** theo dõi hệ quả vật lý khi mỗi quan hệ vẫn cần index theo khóa nghiệp vụ.

## 24. Đây chính là nhược điểm quan trọng của 인조식별자

Ảnh liệt kê:

> **중복 데이터 발생 가능성 → 데이터 품질 저하**
Có khả năng phát sinh dữ liệu trùng → giảm chất lượng dữ liệu.
>

Ví dụ:

```
ID | ORDER | PRODUCT
1  | 101   | C03
2  | 101   | C03
```

PK vẫn:

```
1 ≠ 2
```

→ DB nói OK.

Nhưng nghiệp vụ có thể nói:

```
101 + C03
```

không được duplicate.

Vậy cần thêm:

```sql
UNIQUE (ORDER_ID, PRODUCT_ID)
```

nếu business rule yêu cầu uniqueness.

---

Khi gom phần **24. Đây chính là nhược điểm quan trọng của 인조식별자** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **24. Đây chính là nhược điểm quan trọng của 인조식별자**. Bây giờ chuyển sang **25. 인조식별자 có thể làm tăng Index**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **25. 인조식별자 có thể làm tăng Index** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** Sau khi thấy surrogate key có thể làm tăng index, **26. Một vấn đề khác: Query vẫn phải dùng business columns** nhắc rằng truy vấn nghiệp vụ vẫn lọc theo thuộc tính có nghĩa, không chỉ theo khóa kỹ thuật.

## 25. 인조식별자 có thể làm tăng Index

Ảnh nói:

> **불필요한 인덱스 생성 → 저장 공간 낭비 및 DML 성능 저하**
Có thể phát sinh index bổ sung không cần thiết → tốn storage và giảm hiệu năng DML.
>

Ví dụ:

```
PK:
ORDER_DETAIL_ID
```

DB thường cần index phục vụ PK/unique constraint.

Nhưng thực tế query thường:

```sql
WHERE ORDER_ID = ?
AND PRODUCT_ID = ?
```

thì có thể lại cần index:

```
(ORDER_ID, PRODUCT_ID)
```

Kết quả:

```
Index 1 → ORDER_DETAIL_ID
Index 2 → ORDER_ID + PRODUCT_ID
```

Trong khi nếu thiết kế phù hợp khác đi, có trường hợp có thể giảm một phần index.

Mỗi index bổ sung làm DML như:

```sql
INSERT
UPDATE
DELETE
```

tốn thêm chi phí vì DB không chỉ sửa table mà còn phải duy trì index.

---

Khi gom phần **25. 인조식별자 có thể làm tăng Index** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **25. 인조식별자 có thể làm tăng Index**. Bây giờ chuyển sang **26. Một vấn đề khác: Query vẫn phải dùng business columns**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **26. Một vấn đề khác: Query vẫn phải dùng business columns** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** **26. Một vấn đề khác: Query vẫn phải dùng business columns** cân bằng lại lợi ích và chi phí; **27. 인조식별자의 장점 — Ưu điểm** tổng hợp những trường hợp khóa kỹ thuật vẫn giúp mô hình ổn định hơn.

## 26. Một vấn đề khác: Query vẫn phải dùng business columns

Ảnh nói rất đúng:

> **검색할 때 결국 주문번호와 상품번호를 기반으로 WHERE절을 작성하게 된다.**
Khi tìm kiếm dữ liệu, cuối cùng ta vẫn thường viết WHERE dựa trên 주문번호 và 상품번호.
>

Ví dụ người dùng không biết:

```
ORDER_DETAIL_ID = 473928
```

Họ biết:

```
Order = 101
Product = C03
```

Vì vậy ứng dụng lại query:

```sql
SELECT *
FROM 주문이력
WHERE 주문번호 = '101'
AND 상품번호 = 'C03';
```

Chứ không phải lúc nào cũng:

```sql
WHERE 주문상세번호 = 473928;
```

Đây là lý do surrogate key **không tự động thay thế business key về mặt nghiệp vụ**.

---

Khi gom phần **26. Một vấn đề khác: Query vẫn phải dùng business columns** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **26. Một vấn đề khác: Query vẫn phải dùng business columns**. Bây giờ chuyển sang **27. 인조식별자의 장점 — Ưu điểm**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **27. 인조식별자의 장점 — Ưu điểm** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** Sau khi cân bằng ưu điểm của surrogate key với business columns, **28. Nhưng tại sao ảnh nói “꼭 필요한 경우에만”?** đặt ra nguyên tắc dùng có điều kiện: chỉ thêm khóa kỹ thuật khi lợi ích ổn định vượt chi phí và rủi ro.

## 27. 인조식별자의 장점 — Ưu điểm

Ảnh cũng nói rõ:

> **시퀀스나 키 제약조건 등을 통해 주식별자를 생성할 수 있어 개발의 편의성이 향상된다.**
Có thể tạo primary identifier dễ dàng bằng sequence/key mechanism, giúp việc phát triển thuận tiện hơn.
>

Ví dụ thay vì PK:

```
customer_id
+ product_id
+ date
+ version
```

rất dài, ta dùng:

```
ID
----
10001
10002
10003
```

Foreign key cũng đơn giản.

Thay vì child table phải giữ:

```
customer_id
product_id
date
version
```

có thể chỉ giữ:

```
parent_id
```

→ code dễ hơn
→ JOIN đơn giản hơn
→ FK nhỏ hơn
→ developer dễ quản lý hơn.

Ảnh tóm lại:

```
시간 ↓
비용 ↓
```

---

Khi gom phần **27. 인조식별자의 장점 — Ưu điểm** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **27. 인조식별자의 장점 — Ưu điểm**. Bây giờ chuyển sang **28. Nhưng tại sao ảnh nói “꼭 필요한 경우에만”?**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **28. Nhưng tại sao ảnh nói “꼭 필요한 경우에만”?** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** **28. Nhưng tại sao ảnh nói “꼭 필요한 경우에만”?** chốt tiêu chí lựa chọn có điều kiện; **29. Nối toàn bộ phần này với kiến thức Key trước đó** liên hệ surrogate key với primary key, candidate key và business key đã học.

## 28. Nhưng tại sao ảnh nói “꼭 필요한 경우에만”?

> **개발 편의성을 높여주나 단점도 존재하니 꼭 필요한 경우에만 사용하는 것이 바람직하다.**
Surrogate identifier giúp phát triển thuận tiện nhưng cũng có nhược điểm, vì vậy cần dùng khi phù hợp chứ không phải cứ thấy composite key là thay ngay.
>

Điểm thi quan trọng là:

```
인조식별자 = luôn tốt ❌

본질식별자 = luôn tốt ❌
```

Phải xem **business rule + uniqueness + query pattern + integrity + performance**.

---

Khi gom phần **28. Nhưng tại sao ảnh nói “꼭 필요한 경우에만”?** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **28. Nhưng tại sao ảnh nói “꼭 필요한 경우에만”?**. Bây giờ chuyển sang **29. Nối toàn bộ phần này với kiến thức Key trước đó**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **29. Nối toàn bộ phần này với kiến thức Key trước đó** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** Sau khi nối quyết định dùng surrogate key với các khái niệm khóa, **30. Bức tranh tổng thể của 5 ảnh** đặt toàn bộ quan hệ, NULL và identifier vào một sơ đồ đối chiếu duy nhất.

## 29. Nối toàn bộ phần này với kiến thức Key trước đó

Bạn có thể ghép với cây Key đã học:

```
Super Key
│
└── Candidate Key
      │
      ├── Primary Key
      │
      └── Alternate Key
```

Nhưng:

```
본질식별자 / 인조식별자
```

là **một góc phân loại khác**.

Ví dụ:

```
EMPLOYEE

EMP_ID       ← surrogate
EMAIL        ← natural/business identifier
SSN          ← natural identifier
```

Có thể thiết kế:

```
PK = EMP_ID
UNIQUE = EMAIL
```

Vậy:

```
EMP_ID
→ 인조식별자
→ Primary Key

EMAIL
→ 본질식별자
→ Candidate Key / Alternate Key
```

Điểm này rất quan trọng: **Primary Key không đồng nghĩa với Natural Key.**

---

Khi gom phần **29. Nối toàn bộ phần này với kiến thức Key trước đó** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **29. Nối toàn bộ phần này với kiến thức Key trước đó**. Bây giờ chuyển sang **30. Bức tranh tổng thể của 5 ảnh**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **30. Bức tranh tổng thể của 5 ảnh** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** **30. Bức tranh tổng thể của 5 ảnh** giúp nhìn các lựa chọn cạnh nhau theo cùng tiêu chí; **⭐ NOTE ÔN SQLD — Phần cần thuộc** rút thành các câu kiểm tra ngắn trước khi ôn thi.

## 30. Bức tranh tổng thể của 5 ảnh

Bây giờ hãy nối chúng thành một logic duy nhất.

```
                DATABASE MODEL
                      │
        ┌─────────────┼─────────────┐
        ↓             ↓             ↓
   Transaction       NULL       Identifier
        │             │             │
        ↓             ↓             ↓
      ACID        Unknown      본질 / 인조
        │                           │
   ┌────┼────┐                      ├─ Natural
   ↓    ↓    ↓                      │
   A C  I    D                      └─ Surrogate
```

Khi gom phần **30. Bức tranh tổng thể của 5 ảnh** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **30. Bức tranh tổng thể của 5 ảnh**. Bây giờ chuyển sang **Transaction trả lời:**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Transaction trả lời:** bằng câu hỏi: **thay đổi nào tác động lên hàng dữ liệu, phạm vi nào bị ảnh hưởng và khi nào thay đổi được xác nhận?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Transaction trả lời:

Phần này nối mạch SQL với “Transaction trả lời:”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```
Một nghiệp vụ phải được xử lý như thế nào?
```

→ All or Nothing.

Khi gom phần **Transaction trả lời:** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Transaction trả lời:**. Bây giờ chuyển sang **ACID trả lời:**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **ACID trả lời:** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### ACID trả lời:

Phần này nối mạch SQL với “ACID trả lời:”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```
Transaction phải đảm bảo những tính chất gì?
```

→ Atomicity / Consistency / Isolation / Durability.

Khi gom phần **ACID trả lời:** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **ACID trả lời:**. Bây giờ chuyển sang **NULL trả lời:**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **NULL trả lời:** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### NULL trả lời:

Phần này nối mạch SQL với “NULL trả lời:”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```
DB biểu diễn giá trị chưa biết/chưa có thế nào?
```

→ NULL.

Khi gom phần **NULL trả lời:** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **NULL trả lời:**. Bây giờ chuyển sang **Identifier trả lời:**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Identifier trả lời:** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Identifier trả lời:

Phần này nối mạch SQL với “Identifier trả lời:”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```
Làm thế nào phân biệt từng instance/row?
```

→ Identifier.

Khi gom phần **Identifier trả lời:** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Identifier trả lời:**. Bây giờ chuyển sang **Natural vs Surrogate trả lời:**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Natural vs Surrogate trả lời:** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Natural vs Surrogate trả lời:

Phần này nối mạch SQL với “Natural vs Surrogate trả lời:”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```
Identifier đó đến từ nghiệp vụ
hay do hệ thống tạo?
```

→ 본질식별자 vs 인조식별자.

---

Khi gom phần **Natural vs Surrogate trả lời:** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Natural vs Surrogate trả lời:**. Bây giờ chuyển sang **⭐ NOTE ÔN SQLD — Phần cần thuộc**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **⭐ NOTE ÔN SQLD — Phần cần thuộc** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Nối mạch:** Sau phần ghi nhớ, tài liệu đã khép vòng từ quan hệ và JOIN qua transaction, NULL đến identifier; khi ôn, hãy luôn kiểm tra đối tượng, điều kiện và hệ quả thay vì học các nhãn riêng lẻ.

## ⭐ NOTE ÔN SQLD — Phần cần thuộc

Phần này nối mạch SQL với “⭐ NOTE ÔN SQLD — Phần cần thuộc”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```
[TRANSACTION]

트랜잭션
= 업무 처리를 위한 논리적 작업 단위
= Logical Unit of Work

Atomicity
= All or Nothing

Consistency
= DB의 일관성 유지

Isolation
= 다른 Transaction의 중간 결과 접근 제한

Durability
= COMMIT된 결과는 지속적으로 유지
```

```
[NULL]

NULL
≠ 0
≠ blank
= unknown / undefined / absence

NULL + number → NULL

NULL = NULL → UNKNOWN
NULL IS NULL → TRUE

COUNT(*)   → 모든 행
COUNT(col) → NULL 제외

SUM/AVG/MAX/MIN

Khi gom phần **⭐ NOTE ÔN SQLD — Phần cần thuộc** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Như vậy, **⭐ NOTE ÔN SQLD — Phần cần thuộc** đã được đặt trong quan hệ giữa đầu vào, quy tắc xử lý và kết quả. Khi ôn lại, hãy tự diễn đạt ranh giới của nó rồi dùng ranh giới đó làm điểm nối sang bài tiếp theo.

> **Bàn giao:** Sau **⭐ NOTE ÔN SQLD — Phần cần thuộc**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
