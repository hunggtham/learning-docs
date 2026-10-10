# ERD, Entity, Attribute, Relationship và Identifier

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **ERD, entity, attribute, relationship và identifier**. Route đi từ entity boundary → attributes → relationship cardinality → identifiers/keys → relational schema, để sơ đồ phản ánh đúng quy tắc dữ liệu.

> **Mục tiêu:** Xây dựng ERD; phân loại entity/attribute/relationship; chọn và sử dụng identifier.

## Từ khóa cần nhớ (Keyword)

Phần giải thích dùng tiếng Việt trước. Ở mọi lần xuất hiện, thuật ngữ SQLD dùng dạng `nghĩa Việt (English / 한국어)` để vừa giữ mạch đọc vừa đối chiếu được từ khóa trong đề.

Từ khóa chỉ giúp định vị thuật ngữ; mạch tư duy cần biến chúng thành câu hỏi về thực thể, thuộc tính và quan hệ. Bước đầu là nối định nghĩa với cách người học kiểm tra mô hình.

## Mạch tư duy (Logic học)

Hãy xác định **đối tượng dữ liệu** trước, sau đó đọc **điều kiện**, **phạm vi dòng**, **thứ tự xử lý** và cuối cùng kiểm tra **kết quả mong đợi**. Với SQL, luôn phân biệt điều kiện lọc trước nhóm (`WHERE`) với điều kiện lọc sau nhóm (`HAVING`); đây là cầu nối để hiểu vì sao cùng một truy vấn có thể cho kết quả khác nhau.

Mạch tư duy giải thích cách đọc khái niệm, còn mạch nối biến cách đọc đó thành trình tự học và ra quyết định. Từ đây bài học đặt nền bằng các yếu tố của một mô hình dữ liệu tốt.

## Mạch nối của bài học

Bài này không đứng riêng: hãy nối **ERD, Entity, Attribute, Relationship và Identifier** với bài trước bằng đối tượng dữ liệu/điều kiện mà nó tái sử dụng, rồi dùng kết quả ở phần cuối để chọn bài kế tiếp trong cùng môn. Khi gặp một truy vấn mới, nói rõ nó đang mở rộng mô hình dữ liệu, thứ tự xử lý hay cách kiểm tra kết quả nào trước khi nhớ cú pháp.

> **Cách học:** Đọc phần khái niệm → tự chạy lại các ví dụ SQL → chốt lại mục **từ khóa (Keyword)**, bảng so sánh và phần ghi nhớ cuối bài.

---

Để học **ERD, Entity, Attribute, Relationship và Identifier** như một mạch suy luận, trước hết hãy giữ câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Mục đích của bài là biến **Xây dựng ERD; phân loại entity/attribute/relationship; chọn và sử dụng identifier** thành cách đọc có thể áp dụng.

Câu ghi nhớ quan trọng nhất:

> **현실 세계를 추상화·단순화하여 일정한 표기법으로 명확하게 표현하는 것**
>

> Là trừu tượng hóa và đơn giản hóa thế giới thực, sau đó biểu diễn nó rõ ràng bằng một hệ thống ký hiệu nhất định.
>

Công thức ghi nhớ:

```
추상화 = Bỏ chi tiết không cần thiết
단순화 = Biến thành cấu trúc dễ hiểu
명확화 = Loại bỏ sự mơ hồ
개념적 = Entity và nghiệp vụ
논리적 = Table, Key, Normalization
물리적 = Index và Storage
```

Ta bắt đầu **11. 좋은 데이터 모델의 요소** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Một mô hình tốt không chỉ có đủ entity mà còn phải rõ grain, rule và khả năng kiểm chứng. Khi các tiêu chí này đã rõ, cần biết stakeholder nào cung cấp hoặc xác nhận từng yêu cầu.

## 11. 좋은 데이터 모델의 요소

Khi gom phần **11. 좋은 데이터 모델의 요소** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **11. 좋은 데이터 모델의 요소**. Bây giờ chuyển sang **11.1. 완전성 - Tính đầy đủ**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **11.1. 완전성 - Tính đầy đủ** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 11.1. 완전성 - Tính đầy đủ

**완전성이란 업무에서 필요한 모든 데이터가 데이터 모델에 정의되어 있어야 한다는 의미이다.**

Tính đầy đủ nghĩa là tất cả dữ liệu cần thiết trong nghiệp vụ phải được định nghĩa trong mô hình dữ liệu.

**업무에 필요한 데이터가 모델에서 누락되면 시스템이 업무를 정확하게 처리할 수 없다.**

Nếu dữ liệu cần thiết cho nghiệp vụ bị thiếu trong mô hình thì hệ thống không thể xử lý nghiệp vụ chính xác.

Khi gom phần **11.1. 완전성 - Tính đầy đủ** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **11.1. 완전성 - Tính đầy đủ**. Bây giờ chuyển sang **Keyword: 완전성**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 완전성** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 완전성

**완전성은 필요한 데이터를 빠짐없이 모델에 포함하는 성질이다.**

Tính đầy đủ là đặc tính trong đó mọi dữ liệu cần thiết đều được đưa vào mô hình mà không bị bỏ sót.

Ví dụ nghiệp vụ bán hàng cần quản lý:

```
고객 - Khách hàng
상품 - Sản phẩm
주문 - Đơn hàng
결제 - Thanh toán
배송 - Giao hàng
```

Nếu mô hình chỉ có `CUSTOMER` và `PRODUCT` nhưng không có `ORDER`, hệ thống không thể lưu thông tin khách hàng đã mua sản phẩm nào.

Mô hình thiếu dữ liệu:

```
CUSTOMER
PRODUCT
```

Mô hình đầy đủ hơn:

```
CUSTOMER
PRODUCT
ORDERS
ORDER_ITEM
PAYMENT
DELIVERY
```

Khi gom phần **Keyword: 완전성** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 완전성**. Bây giờ chuyển sang **Cần phân biệt**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Cần phân biệt** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Cần phân biệt

**완전성은 데이터를 많이 넣는 것이 아니라 업무에 필요한 데이터를 빠짐없이 정의하는 것이다.**

Tính đầy đủ không có nghĩa là đưa thật nhiều dữ liệu vào, mà là định nghĩa đầy đủ những dữ liệu cần cho nghiệp vụ.

Không cần đưa vào các thông tin không liên quan chỉ để làm mô hình “đầy đủ” hơn.

---

Khi gom phần **Cần phân biệt** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Cần phân biệt**. Bây giờ chuyển sang **11.2. 중복배제 - Loại bỏ trùng lặp**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **11.2. 중복배제 - Loại bỏ trùng lặp** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 11.2. 중복배제 - Loại bỏ trùng lặp

**중복배제란 하나의 데이터베이스 안에서 동일한 사실이 한 번만 기록되도록 설계하는 것이다.**

Loại bỏ trùng lặp là thiết kế sao cho cùng một sự thật chỉ được ghi nhận một lần trong một database.

**동일한 데이터를 여러 테이블에 반복해서 저장하면 데이터 수정 시 불일치가 발생할 수 있다.**

Nếu lưu cùng một dữ liệu lặp lại ở nhiều bảng thì có thể phát sinh sự không nhất quán khi cập nhật.

Khi gom phần **11.2. 중복배제 - Loại bỏ trùng lặp** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **11.2. 중복배제 - Loại bỏ trùng lặp**. Bây giờ chuyển sang **Keyword: 중복배제**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 중복배제** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 중복배제

**중복배제는 동일한 의미를 가진 데이터를 여러 곳에 저장하지 않는 원칙이다.**

Loại bỏ trùng lặp là nguyên tắc không lưu dữ liệu có cùng ý nghĩa ở nhiều nơi.

Ví dụ không tốt:

```
CUSTOMER
--------
CUSTOMER_ID
CUSTOMER_NAME
ADDRESS

ORDERS
------
ORDER_ID
CUSTOMER_ID
CUSTOMER_NAME
ADDRESS
```

Ở đây, `CUSTOMER_NAME` và `ADDRESS` vừa nằm trong `CUSTOMER`, vừa nằm trong `ORDERS`.

Nếu khách hàng thay đổi địa chỉ:

```
CUSTOMER.ADDRESS = Seoul
ORDERS.ADDRESS   = Busan
```

thì dữ liệu bị mâu thuẫn.

Thiết kế tốt hơn:

```
CUSTOMER
--------
CUSTOMER_ID
CUSTOMER_NAME
ADDRESS

ORDERS
------
ORDER_ID
CUSTOMER_ID
```

`ORDERS` chỉ lưu `CUSTOMER_ID` và tham chiếu đến bảng `CUSTOMER`.

---

Khi gom phần **Keyword: 중복배제** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 중복배제**. Bây giờ chuyển sang **11.3. Trường hợp Foreign Key được phép lặp**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **11.3. Trường hợp Foreign Key được phép lặp** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 11.3. Trường hợp Foreign Key được phép lặp

Trong hình có ghi:

> FK는 필수불가결한 경우이다.
>

**외래키는 부모 테이블의 기본키 값을 자식 테이블에서 참조하기 위해 반복될 수 있다.**

Foreign Key có thể được lặp lại trong bảng con để tham chiếu đến Primary Key của bảng cha.

Khi gom phần **11.3. Trường hợp Foreign Key được phép lặp** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **11.3. Trường hợp Foreign Key được phép lặp**. Bây giờ chuyển sang **Keyword: FK**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: FK** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: FK

**FK(Foreign Key)는 다른 테이블의 기본키를 참조하여 테이블 간의 관계를 연결하는 컬럼이다.**

FK là cột tham chiếu đến Primary Key của bảng khác để liên kết các bảng với nhau.

Ví dụ:

```
CUSTOMER
--------
CUSTOMER_ID
CUSTOMER_NAME

ORDERS
------
ORDER_ID
CUSTOMER_ID
```

Dữ liệu:

```
CUSTOMER
CUSTOMER_ID | CUSTOMER_NAME
------------|--------------
C001        | Nguyễn Văn A

ORDERS
ORDER_ID | CUSTOMER_ID
---------|-----------
O001     | C001
O002     | C001
O003     | C001
```

`C001` xuất hiện nhiều lần trong `ORDERS`, nhưng đây không phải trùng lặp sai.

Lý do là một khách hàng có thể có nhiều đơn hàng:

```
CUSTOMER 1 : N ORDERS
```

Khi gom phần **Keyword: FK** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: FK**. Bây giờ chuyển sang **Điểm quan trọng**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Điểm quan trọng** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Điểm quan trọng

**외래키의 반복은 관계를 표현하기 위해 필요한 반복이므로 일반적인 중복과 구별해야 한다.**

Việc lặp Foreign Key là sự lặp cần thiết để biểu diễn quan hệ, vì vậy phải phân biệt nó với trùng lặp dữ liệu thông thường.

```
Thông tin khách hàng lặp lại ở nhiều bảng
→ Trùng lặp không cần thiết

CUSTOMER_ID lặp lại trong nhiều đơn hàng
→ Lặp cần thiết để biểu diễn quan hệ
```

---

Khi gom phần **Điểm quan trọng** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Điểm quan trọng**. Bây giờ chuyển sang **11.4. 업무규칙 - Quy tắc nghiệp vụ**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **11.4. 업무규칙 - Quy tắc nghiệp vụ** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 11.4. 업무규칙 - Quy tắc nghiệp vụ

**업무규칙이란 업무를 처리할 때 반드시 지켜야 하는 조건과 규칙이다.**

Quy tắc nghiệp vụ là các điều kiện và quy tắc bắt buộc phải tuân thủ khi xử lý nghiệp vụ.

**업무규칙은 데이터 모델에 표현되어야 하며 모든 사용자가 공유할 수 있어야 한다.**

Quy tắc nghiệp vụ phải được thể hiện trong mô hình dữ liệu và phải được cung cấp để mọi người dùng cùng chia sẻ.

Khi gom phần **11.4. 업무규칙 - Quy tắc nghiệp vụ** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **11.4. 업무규칙 - Quy tắc nghiệp vụ**. Bây giờ chuyển sang **Keyword: 업무규칙**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 업무규칙** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 업무규칙

**업무규칙은 데이터가 어떤 조건을 만족해야 하는지를 정의하는 업무상의 약속이다.**

Quy tắc nghiệp vụ là quy ước trong nghiệp vụ, định nghĩa dữ liệu phải thỏa mãn điều kiện nào.

Ví dụ:

```
Một nhân viên chỉ thuộc một phòng ban.
Một khách hàng có thể có nhiều đơn hàng.
Một đơn hàng phải thuộc về một khách hàng.
Giá sản phẩm không được nhỏ hơn 0.
Một đơn hàng phải có ít nhất một sản phẩm.
```

Các quy tắc này phải được phản ánh vào mô hình.

Ví dụ:

```
CREATE TABLE ORDERS (
    ORDER_ID NUMBER PRIMARY KEY,
    CUSTOMER_ID NUMBER NOT NULL,
    CONSTRAINT FK_ORDER_CUSTOMER
        FOREIGN KEY (CUSTOMER_ID)
        REFERENCES CUSTOMER(CUSTOMER_ID)
);
```

Trong đó:

- `PRIMARY KEY`: mỗi đơn hàng phải có mã duy nhất.
- `NOT NULL`: đơn hàng bắt buộc phải có khách hàng.
- `FOREIGN KEY`: khách hàng phải tồn tại trong bảng `CUSTOMER`.

Khi gom phần **Keyword: 업무규칙** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 업무규칙**. Bây giờ chuyển sang **Vì sao phải chia sẻ 업무규칙?**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Vì sao phải chia sẻ 업무규칙?** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Vì sao phải chia sẻ 업무규칙?

**업무규칙이 모델에 명확하게 표현되면 개발자, DBA, 현업 담당자가 동일한 기준으로 업무를 이해할 수 있다.**

Khi quy tắc nghiệp vụ được thể hiện rõ trong mô hình, nhà phát triển, DBA và người phụ trách nghiệp vụ có thể hiểu nghiệp vụ theo cùng một tiêu chuẩn.

Nếu quy tắc chỉ nằm trong suy nghĩ của một nhân viên, khi người đó nghỉ việc hoặc chuyển bộ phận thì kiến thức nghiệp vụ có thể bị mất.

---

Khi gom phần **Vì sao phải chia sẻ 업무규칙?** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Vì sao phải chia sẻ 업무규칙?**. Bây giờ chuyển sang **11.5. 데이터 재사용 - Tái sử dụng dữ liệu**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **11.5. 데이터 재사용 - Tái sử dụng dữ liệu** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 11.5. 데이터 재사용 - Tái sử dụng dữ liệu

**데이터 재사용이란 데이터를 통합성과 독립성의 관점에서 설계하여 여러 업무 영역에서 공통으로 사용하는 것이다.**

Tái sử dụng dữ liệu là thiết kế dữ liệu theo hướng tích hợp và độc lập để có thể sử dụng chung trong nhiều lĩnh vực nghiệp vụ.

**공통 데이터는 회사 전체의 관점에서 도출하고 여러 업무 영역에서 참조할 수 있도록 설계해야 한다.**

Dữ liệu dùng chung phải được xác định từ góc nhìn toàn công ty và thiết kế để nhiều lĩnh vực nghiệp vụ có thể tham chiếu.

Khi gom phần **11.5. 데이터 재사용 - Tái sử dụng dữ liệu** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **11.5. 데이터 재사용 - Tái sử dụng dữ liệu**. Bây giờ chuyển sang **Keyword: 데이터 재사용**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 데이터 재사용** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 데이터 재사용

**데이터 재사용은 같은 의미의 데이터를 업무별로 따로 만들지 않고 공통 데이터로 관리하는 것이다.**

Tái sử dụng dữ liệu là quản lý dữ liệu có cùng ý nghĩa như dữ liệu chung, thay vì tạo riêng cho từng nghiệp vụ.

Ví dụ không tốt:

```
Bộ phận bán hàng tự tạo CUSTOMER
Bộ phận thanh toán tự tạo CUSTOMER
Bộ phận giao hàng tự tạo CUSTOMER
```

Khi đó có thể xuất hiện ba cách quản lý khách hàng khác nhau.

Thiết kế tốt hơn:

```
CUSTOMER
--------
CUSTOMER_ID
CUSTOMER_NAME
PHONE
ADDRESS
```

Các hệ thống khác cùng tham chiếu bảng này:

```
Bán hàng      → CUSTOMER
Thanh toán    → CUSTOMER
Giao hàng     → CUSTOMER
Marketing     → CUSTOMER
```

Khi gom phần **Keyword: 데이터 재사용** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 데이터 재사용**. Bây giờ chuyển sang **Vì sao dữ liệu cần độc lập?**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Vì sao dữ liệu cần độc lập?** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Vì sao dữ liệu cần độc lập?

**데이터는 특정 프로그램에 종속되지 않고 여러 프로그램에서 활용될 수 있어야 한다.**

Dữ liệu không nên phụ thuộc vào một chương trình cụ thể mà phải có thể được sử dụng bởi nhiều chương trình.

Ví dụ thông tin khách hàng không nên chỉ được lưu bên trong chương trình bán hàng, vì chương trình thanh toán và giao hàng cũng cần sử dụng.

Khi gom phần **Vì sao dữ liệu cần độc lập?** lại, ta không cần nhớ các dòng như những mảnh rời: ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Vì sao dữ liệu cần độc lập?**. Bây giờ chuyển sang **Dòng quan trọng trong hình**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Dòng quan trọng trong hình** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Dòng quan trọng trong hình

> 파일시스템처럼 부서별로, 응용 프로그램별로 데이터를 따로 만들지 말라는 것
>

**부서별 또는 응용 프로그램별로 데이터를 따로 만들면 중복과 불일치가 증가한다.**

Nếu tạo dữ liệu riêng theo từng phòng ban hoặc từng chương trình thì sự trùng lặp và không nhất quán sẽ tăng lên.

---

Khi gom phần **Dòng quan trọng trong hình** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Dòng quan trọng trong hình**. Bây giờ chuyển sang **11.6. 의사소통 - Khả năng giao tiếp**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **11.6. 의사소통 - Khả năng giao tiếp** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 11.6. 의사소통 - Khả năng giao tiếp

**의사소통이란 업무규칙을 엔터티, 서브타입, 속성, 관계 등의 형태로 자세히 표현하는 것이다.**

Khả năng giao tiếp là biểu diễn quy tắc nghiệp vụ một cách chi tiết dưới dạng Entity, Subtype, Attribute và Relationship.

**모델을 본 관련자들이 동일한 의미로 이해하고 활용할 수 있어야 한다.**

Những người liên quan khi xem mô hình phải có thể hiểu và sử dụng nó với cùng một ý nghĩa.

Khi gom phần **11.6. 의사소통 - Khả năng giao tiếp** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **11.6. 의사소통 - Khả năng giao tiếp**. Bây giờ chuyển sang **Keyword: 의사소통**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 의사소통** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 의사소통

**의사소통은 데이터 모델을 통해 현업 담당자와 개발자가 같은 업무 내용을 공유하는 것이다.**

Khả năng giao tiếp là việc người phụ trách nghiệp vụ và nhà phát triển chia sẻ cùng một nội dung nghiệp vụ thông qua mô hình dữ liệu.

Ví dụ người phụ trách nghiệp vụ nói:

> Một khách hàng có thể có nhiều hợp đồng.
>

Trong mô hình cần biểu diễn:

```
CUSTOMER 1 ─── N CONTRACT
```

Nhờ đó:

- Người dùng hiểu quan hệ nghiệp vụ.
- Nhà phát triển hiểu cách tạo bảng.
- DBA hiểu khóa cần thiết.
- Tester hiểu điều kiện cần kiểm thử.

---

Khi gom phần **Keyword: 의사소통** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 의사소통**. Bây giờ chuyển sang **11.7. 통합성 - Tính tích hợp**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **11.7. 통합성 - Tính tích hợp** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 11.7. 통합성 - Tính tích hợp

**통합성이란 동일한 데이터는 조직 전체에서 한 번만 정의하고 다른 영역에서는 이를 참조하여 사용하는 것이다.**

Tính tích hợp là cùng một dữ liệu chỉ được định nghĩa một lần trong toàn tổ chức, các khu vực khác tham chiếu và sử dụng dữ liệu đó.

Khi gom phần **11.7. 통합성 - Tính tích hợp** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **11.7. 통합성 - Tính tích hợp**. Bây giờ chuyển sang **Keyword: 통합성**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 통합성** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 통합성

**통합성은 회사 전체가 공통 데이터를 하나의 기준으로 사용하는 성질이다.**

Tính tích hợp là đặc tính trong đó toàn công ty sử dụng dữ liệu chung theo một tiêu chuẩn duy nhất.

Ví dụ:

```
CUSTOMER_ID = C001
```

Mã khách hàng `C001` phải có cùng ý nghĩa trong:

- Hệ thống bán hàng.
- Hệ thống thanh toán.
- Hệ thống giao hàng.
- Hệ thống chăm sóc khách hàng.

Nếu mỗi hệ thống tự định nghĩa một mã khách hàng khác nhau thì việc đồng bộ dữ liệu sẽ khó khăn.

Khi gom phần **Keyword: 통합성** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 통합성**. Bây giờ chuyển sang **Phân biệt 중복배제 và 통합성**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Phân biệt 중복배제 và 통합성** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Phân biệt 중복배제 và 통합성

**중복배제는 동일한 데이터의 반복 저장을 방지하는 원칙이다.**

Loại bỏ trùng lặp là nguyên tắc ngăn việc lưu lặp cùng một dữ liệu.

**통합성은 조직 전체가 동일한 데이터를 하나의 기준으로 공유하는 원칙이다.**

Tính tích hợp là nguyên tắc toàn tổ chức chia sẻ cùng một dữ liệu theo một tiêu chuẩn.

Có thể ghi nhớ:

```
중복배제 = Không lưu lặp
통합성   = Toàn công ty dùng chung một định nghĩa
```

---

Khi gom phần **Phân biệt 중복배제 và 통합성** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Phân biệt 중복배제 và 통합성**. Bây giờ chuyển sang **12. 데이터 모델링의 이해관계자**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **12. 데이터 모델링의 이해관계자** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Stakeholder cung cấp ngữ nghĩa nghiệp vụ và các ngoại lệ mà schema không thể tự suy ra. Khi yêu cầu đã được gom lại, ERD trở thành bản đồ để biểu diễn và kiểm tra chúng.

## 12. 데이터 모델링의 이해관계자

Khi gom phần **12. 데이터 모델링의 이해관계자** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **12. 데이터 모델링의 이해관계자**. Bây giờ chuyển sang **12.1. Mô hình dữ liệu là sản phẩm cuối cùng**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **12.1. Mô hình dữ liệu là sản phẩm cuối cùng** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 12.1. Mô hình dữ liệu là sản phẩm cuối cùng

**데이터 모델은 대상 업무를 데이터 관점에서 분석하고 설계한 결과로 만들어지는 최종 산출물이다.**

Mô hình dữ liệu là sản phẩm cuối cùng được tạo ra sau khi phân tích và thiết kế nghiệp vụ dưới góc nhìn dữ liệu.

Khi gom phần **12.1. Mô hình dữ liệu là sản phẩm cuối cùng** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **12.1. Mô hình dữ liệu là sản phẩm cuối cùng**. Bây giờ chuyển sang **Keyword: 최종 산출물**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 최종 산출물** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 최종 산출물

**최종 산출물은 분석과 설계 과정을 거쳐 최종적으로 완성되어 프로젝트에서 사용하는 결과물이다.**

Sản phẩm cuối cùng là kết quả được hoàn thiện sau quá trình phân tích và thiết kế để sử dụng trong dự án.

Mô hình dữ liệu không chỉ là tài liệu tham khảo, mà còn là cơ sở cho:

- Thiết kế bảng.
- Viết SQL.
- Phát triển ứng dụng.
- Kiểm thử.
- Xây dựng báo cáo.
- Quản lý dữ liệu.

---

Khi gom phần **Keyword: 최종 산출물** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 최종 산출물**. Bây giờ chuyển sang **12.2. Các bên liên quan**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **12.2. Các bên liên quan** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 12.2. Các bên liên quan

Hình thể hiện bốn nhóm chính:

```
프로젝트 개발자 - Nhà phát triển dự án
DBA             - Quản trị cơ sở dữ liệu
현업 전문가      - Chuyên gia nghiệp vụ
전문 모델러      - Chuyên gia mô hình hóa dữ liệu
```

Ở giữa là:

```
데이터 모델링
```

Khi gom phần **12.2. Các bên liên quan** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **12.2. Các bên liên quan**. Bây giờ chuyển sang **1. 프로젝트 개발자**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **1. 프로젝트 개발자** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 1. 프로젝트 개발자

**프로젝트 개발자는 데이터 모델을 이해하고 필요하면 직접 작성할 수 있어야 한다.**

Nhà phát triển dự án phải hiểu mô hình dữ liệu và khi cần có thể trực tiếp viết mô hình.

Họ cần biết:

- Bảng nào được sử dụng.
- Cột nào là khóa.
- Bảng nào liên kết với nhau.
- Dữ liệu được thêm, sửa, xóa như thế nào.
- SQL nào cần sử dụng.

Khi gom phần **1. 프로젝트 개발자** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **1. 프로젝트 개발자**. Bây giờ chuyển sang **2. DBA**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **2. DBA** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 2. DBA

**DBA는 데이터베이스의 구축, 운영, 보안, 성능을 담당하는 전문가이다.**

DBA là chuyên gia phụ trách xây dựng, vận hành, bảo mật và hiệu năng của database.

DBA cần hiểu:

- Table.
- Index.
- Constraint.
- Storage.
- Backup.
- Performance.
- User và quyền truy cập.

Khi gom phần **2. DBA** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **2. DBA**. Bây giờ chuyển sang **3. 현업 전문가**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **3. 현업 전문가** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 3. 현업 전문가

**현업 전문가는 실제 업무의 규칙과 처리 과정을 가장 잘 알고 있는 사람이다.**

Chuyên gia nghiệp vụ là người hiểu rõ nhất các quy tắc và quy trình xử lý thực tế.

Ví dụ:

- Nhân viên kế toán hiểu quy tắc thanh toán.
- Nhân viên kho hiểu quy tắc nhập xuất kho.
- Nhân viên bán hàng hiểu quy trình đặt hàng.
- Nhân viên nhân sự hiểu quy tắc quản lý nhân viên.

Khi gom phần **3. 현업 전문가** lại, ta không cần nhớ các dòng như những mảnh rời: ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **3. 현업 전문가**. Bây giờ chuyển sang **4. 전문 모델러**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **4. 전문 모델러** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 4. 전문 모델러

**전문 모델러는 업무를 분석하고 데이터 구조와 데이터 간의 관계를 전문적으로 설계하는 사람이다.**

Chuyên gia mô hình hóa là người chuyên phân tích nghiệp vụ và thiết kế cấu trúc dữ liệu cùng các mối quan hệ giữa dữ liệu.

Khi gom phần **4. 전문 모델러** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **4. 전문 모델러**. Bây giờ chuyển sang **Hai câu quan trọng trong hình**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Hai câu quan trọng trong hình** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Hai câu quan trọng trong hình

**프로젝트에 참여하는 모든 사람은 데이터 모델링을 이해해야 한다.**

Tất cả những người tham gia dự án đều phải hiểu mô hình hóa dữ liệu.

**프로젝트 개발자와 전문 모델러는 데이터 모델을 직접 작성할 수 있어야 한다.**

Nhà phát triển dự án và chuyên gia mô hình hóa phải có khả năng trực tiếp viết mô hình dữ liệu.

---

Khi gom phần **Hai câu quan trọng trong hình** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Hai câu quan trọng trong hình**. Bây giờ chuyển sang **13. ERD là gì?**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **13. ERD là gì?** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

ERD biểu diễn entity, relationship và constraint, nhưng bản vẽ chỉ có giá trị khi được lập theo một quy trình nhất quán. Vì vậy bước kế tiếp là trình tự đi từ phạm vi nghiệp vụ đến mô hình.

## 13. ERD là gì?

Khi gom phần **13. ERD là gì?** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **13. ERD là gì?**. Bây giờ chuyển sang **13.1. Định nghĩa ERD**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **13.1. Định nghĩa ERD** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 13.1. Định nghĩa ERD

**ERD는 업무 분석에서 도출된 엔터티와 엔터티 간의 관계를 이해하기 쉽게 도식화한 다이어그램이다.**

ERD là sơ đồ biểu diễn các Entity được rút ra từ phân tích nghiệp vụ và mối quan hệ giữa các Entity một cách dễ hiểu.

**ERD는 데이터 흐름과 업무 프로세스 사이의 연관성을 표현하는 산출물이다.**

ERD là sản phẩm thể hiện mối liên hệ giữa luồng dữ liệu và quy trình nghiệp vụ.

Khi gom phần **13.1. Định nghĩa ERD** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **13.1. Định nghĩa ERD**. Bây giờ chuyển sang **Keyword: ERD**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: ERD** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: ERD

**ERD(Entity Relationship Diagram)는 엔터티, 속성, 관계를 그림으로 표현한 데이터 모델이다.**

ERD là mô hình dữ liệu biểu diễn Entity, Attribute và Relationship bằng hình ảnh.

ERD giúp trả lời:

- Có những Entity nào?
- Mỗi Entity có Attribute nào?
- Các Entity liên hệ ra sao?
- Quan hệ là 1:1, 1:N hay N:M?
- Quan hệ bắt buộc hay tùy chọn?
- Entity nào là cha, Entity nào là con?

---

Khi gom phần **Keyword: ERD** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: ERD**. Bây giờ chuyển sang **13.2. Nguồn gốc ERD**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **13.2. Nguồn gốc ERD** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 13.2. Nguồn gốc ERD

**1976년 Peter Chen이 Entity-Relationship Model이라는 표기법을 만들었다.**

Năm 1976, Peter Chen đã tạo ra phương pháp ký hiệu gọi là Entity-Relationship Model.

Khi gom phần **13.2. Nguồn gốc ERD** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **13.2. Nguồn gốc ERD**. Bây giờ chuyển sang **Keyword: Peter Chen**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: Peter Chen** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: Peter Chen

**Peter Chen은 엔터티와 관계를 이용하여 현실 세계를 데이터 모델로 표현하는 ER 모델을 제안한 인물이다.**

Peter Chen là người đề xuất mô hình ER, dùng Entity và Relationship để biểu diễn thế giới thực thành mô hình dữ liệu.

---

Khi gom phần **Keyword: Peter Chen** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: Peter Chen**. Bây giờ chuyển sang **14. Trình tự lập ERD**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **14. Trình tự lập ERD** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Trình tự lập ERD giúp tránh vẽ quan hệ trước khi biết entity và rule. Sau khi xác định các thành phần, cần thống nhất ký pháp để cardinality, optionality và key không bị hiểu khác nhau.

## 14. Trình tự lập ERD

Khi gom phần **14. Trình tự lập ERD** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **14. Trình tự lập ERD**. Bây giờ chuyển sang **14.1. Bước 1: Vẽ Entity**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **14.1. Bước 1: Vẽ Entity** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 14.1. Bước 1: Vẽ Entity

**첫 번째 단계는 업무에서 필요한 엔터티를 식별하고 그린다.**

Bước đầu tiên là xác định và vẽ các Entity cần thiết trong nghiệp vụ.

Ví dụ hệ thống bán hàng:

```
CUSTOMER
PRODUCT
ORDER
PAYMENT
```

Khi gom phần **14.1. Bước 1: Vẽ Entity** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **14.1. Bước 1: Vẽ Entity**. Bây giờ chuyển sang **Keyword: 식별**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 식별** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 식별

**식별은 업무에서 관리해야 할 대상을 찾아내는 것이다.**

Xác định là tìm ra những đối tượng cần được quản lý trong nghiệp vụ.

---

Khi gom phần **Keyword: 식별** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 식별**. Bây giờ chuyển sang **14.2. Bước 2: Sắp xếp Entity**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **14.2. Bước 2: Sắp xếp Entity** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 14.2. Bước 2: Sắp xếp Entity

**두 번째 단계는 엔터티를 관계가 잘 보이도록 적절하게 배치하는 것이다.**

Bước thứ hai là sắp xếp các Entity ở vị trí phù hợp để các mối quan hệ dễ quan sát.

**선이 서로 꼬이지 않도록 하고 가장 중요한 엔터티는 왼쪽 상단에 배치하는 것이 좋다.**

Nên tránh để các đường quan hệ bị chồng chéo và đặt Entity quan trọng nhất ở phía trên bên trái.

Khi gom phần **14.2. Bước 2: Sắp xếp Entity** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **14.2. Bước 2: Sắp xếp Entity**. Bây giờ chuyển sang **Keyword: 배치**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 배치** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 배치

**배치는 ERD의 가독성을 높이기 위해 엔터티의 위치를 정하는 작업이다.**

Sắp xếp là công việc quyết định vị trí của Entity để tăng khả năng đọc ERD.

Mục tiêu:

- Đường quan hệ không bị rối.
- Dễ theo dõi từ trái sang phải.
- Entity trung tâm được nhìn thấy rõ.
- Các nhóm nghiệp vụ được bố trí hợp lý.

---

Khi gom phần **Keyword: 배치** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 배치**. Bây giờ chuyển sang **14.3. Bước 3: Thiết lập quan hệ**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **14.3. Bước 3: Thiết lập quan hệ** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 14.3. Bước 3: Thiết lập quan hệ

**세 번째 단계는 엔터티 간의 업무 관계를 설정하는 것이다.**

Bước thứ ba là thiết lập quan hệ nghiệp vụ giữa các Entity.

**식별자 관계를 우선적으로 설정한다.**

Trước tiên nên thiết lập quan hệ định danh.

Khi gom phần **14.3. Bước 3: Thiết lập quan hệ** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **14.3. Bước 3: Thiết lập quan hệ**. Bây giờ chuyển sang **Keyword: 관계**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 관계** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 관계

**관계는 두 엔터티가 업무적으로 서로 어떻게 연결되어 있는지를 표현하는 것이다.**

Relationship biểu diễn hai Entity liên kết với nhau về mặt nghiệp vụ như thế nào.

Ví dụ:

```
CUSTOMER 1 ─── N ORDER
```

Nghĩa là một khách hàng có thể có nhiều đơn hàng.

---

Khi gom phần **Keyword: 관계** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 관계**. Bây giờ chuyển sang **14.4. 식별자 관계 - Quan hệ định danh**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **14.4. 식별자 관계 - Quan hệ định danh** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 14.4. 식별자 관계 - Quan hệ định danh

**식별자 관계는 부모 엔터티의 기본키가 자식 엔터티의 기본키 일부가 되는 관계이다.**

Quan hệ định danh là quan hệ trong đó Primary Key của Entity cha trở thành một phần Primary Key của Entity con.

Khi gom phần **14.4. 식별자 관계 - Quan hệ định danh** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **14.4. 식별자 관계 - Quan hệ định danh**. Bây giờ chuyển sang **Keyword: 식별자 관계**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 식별자 관계** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 식별자 관계

**식별자 관계에서는 부모의 PK가 자식에게 전달되어 자식의 식별자 구성에 포함된다.**

Trong quan hệ định danh, PK của cha được truyền sang con và được bao gồm trong cấu trúc định danh của con.

Ví dụ:

```
ORDER
-----
ORDER_ID PK

ORDER_ITEM
----------
ORDER_ID PK, FK
PRODUCT_ID PK, FK
QUANTITY
```

Ở đây:

```
ORDER_ITEM의 PK = ORDER_ID + PRODUCT_ID
```

`ORDER_ID` vừa là:

- Foreign Key tham chiếu `ORDER`.
- Một phần của Primary Key của `ORDER_ITEM`.

---

Khi gom phần **Keyword: 식별자 관계** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 식별자 관계**. Bây giờ chuyển sang **14.5. Tránh vòng lặp quan hệ**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **14.5. Tránh vòng lặp quan hệ** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 14.5. Tránh vòng lặp quan hệ

**가급적 순환 관계가 발생하지 않도록 관계를 설정해야 한다.**

Nên thiết lập quan hệ sao cho hạn chế phát sinh quan hệ vòng lặp.

Khi gom phần **14.5. Tránh vòng lặp quan hệ** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **14.5. Tránh vòng lặp quan hệ**. Bây giờ chuyển sang **Keyword: 순환 관계**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 순환 관계** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 순환 관계

**순환 관계는 엔터티 간의 연결이 고리처럼 다시 원래 엔터티로 돌아오는 관계이다.**

Quan hệ vòng lặp là quan hệ trong đó các Entity liên kết thành vòng và quay trở lại Entity ban đầu.

Ví dụ:

```
A → B → C → A
```

Quan hệ vòng có thể làm:

- Khó đọc ERD.
- Khó xác định thứ tự xử lý.
- Khó kiểm tra dữ liệu.
- Phức tạp khi thực hiện Insert hoặc Delete.

---

Khi gom phần **Keyword: 순환 관계** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 순환 관계**. Bây giờ chuyển sang **14.6. Bước 4: Đặt tên quan hệ**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **14.6. Bước 4: Đặt tên quan hệ** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 14.6. Bước 4: Đặt tên quan hệ

**네 번째 단계는 엔터티 간의 관계를 현재형 동사로 기술하는 것이다.**

Bước thứ tư là mô tả quan hệ giữa các Entity bằng động từ ở thì hiện tại.

**지나치게 포괄적인 단어보다 업무 의미가 분명한 관계명을 사용해야 한다.**

Nên sử dụng tên quan hệ thể hiện rõ ý nghĩa nghiệp vụ thay vì các từ quá bao quát.

Ví dụ trong hình:

```
주문한다 - Đặt hàng
철회한다 - Rút lại / hủy
수강한다 - Đăng ký học
```

Khi gom phần **14.6. Bước 4: Đặt tên quan hệ** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **14.6. Bước 4: Đặt tên quan hệ**. Bây giờ chuyển sang **Keyword: 관계명**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 관계명** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 관계명

**관계명은 두 엔터티 사이에서 어떤 업무 행위가 발생하는지를 나타내는 이름이다.**

Tên quan hệ là tên thể hiện hành động nghiệp vụ xảy ra giữa hai Entity.

Ví dụ:

```
CUSTOMER ── 주문한다 ── ORDER
STUDENT ── 수강한다 ── COURSE
CUSTOMER ── 결제한다 ── PAYMENT
```

Không nên dùng tên quá mơ hồ như:

```
관련된다 - Có liên quan
관리한다 - Quản lý
처리한다 - Xử lý
```

trừ khi nghiệp vụ thực sự không thể diễn đạt cụ thể hơn.

---

Khi gom phần **Keyword: 관계명** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 관계명**. Bây giờ chuyển sang **14.7. Bước 5: Ghi mức độ tham gia và Cardinality**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **14.7. Bước 5: Ghi mức độ tham gia và Cardinality** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 14.7. Bước 5: Ghi mức độ tham gia và Cardinality

**다섯 번째 단계는 관계의 참여도와 관계차수를 기술하는 것이다.**

Bước thứ năm là mô tả mức độ tham gia và số lượng trong quan hệ.

**관계차수는 한 엔터티의 인스턴스가 다른 엔터티의 인스턴스와 몇 개까지 연결될 수 있는지를 의미한다.**

Cardinality là số lượng Instance của một Entity có thể liên kết với Instance của Entity khác.

Khi gom phần **14.7. Bước 5: Ghi mức độ tham gia và Cardinality** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **14.7. Bước 5: Ghi mức độ tham gia và Cardinality**. Bây giờ chuyển sang **Keyword: 관계차수 또는 Cardinality**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 관계차수 또는 Cardinality** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 관계차수 또는 Cardinality

**Cardinality는 엔터티 간 관계의 수적 범위를 나타낸다.**

Cardinality biểu thị phạm vi số lượng của mối quan hệ giữa các Entity.

Ví dụ:

```
1 : 1
1 : N
N : M
```

Ý nghĩa:

- `1:1`: một đối tượng liên kết với một đối tượng.
- `1:N`: một đối tượng liên kết với nhiều đối tượng.
- `N:M`: nhiều đối tượng liên kết với nhiều đối tượng.

Trong ký pháp Chen, thường biểu diễn:

```
1 : N
```

Trong ký pháp IE/Crow’s Foot, dùng chân quạ để biểu diễn “nhiều”.

---

Khi gom phần **Keyword: 관계차수 또는 Cardinality** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 관계차수 또는 Cardinality**. Bây giờ chuyển sang **14.8. Bước 6: Ghi bắt buộc hoặc tùy chọn**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **14.8. Bước 6: Ghi bắt buộc hoặc tùy chọn** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 14.8. Bước 6: Ghi bắt buộc hoặc tùy chọn

**여섯 번째 단계는 관계에 반드시 참여해야 하는지 선택적으로 참여할 수 있는지를 기술하는 것이다.**

Bước thứ sáu là mô tả việc tham gia quan hệ là bắt buộc hay tùy chọn.

**필수 여부는 IE 표기법에서 원으로 표현할 수 있다.**

Tính bắt buộc có thể được biểu diễn bằng vòng tròn trong ký pháp IE.

Khi gom phần **14.8. Bước 6: Ghi bắt buộc hoặc tùy chọn** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **14.8. Bước 6: Ghi bắt buộc hoặc tùy chọn**. Bây giờ chuyển sang **Keyword: 필수 참여**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 필수 참여** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 필수 참여

**필수 참여는 해당 엔터티의 인스턴스가 관계에 반드시 참여해야 한다는 의미이다.**

Tham gia bắt buộc nghĩa là Instance của Entity đó bắt buộc phải tham gia vào quan hệ.

Ví dụ:

```
Mọi Order bắt buộc phải thuộc về một Customer.
```

Khi đó:

```
ORDERS.CUSTOMER_ID NOT NULL
```

Khi gom phần **Keyword: 필수 참여** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 필수 참여**. Bây giờ chuyển sang **Keyword: 선택 참여**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 선택 참여** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 선택 참여

**선택 참여는 해당 엔터티의 인스턴스가 관계에 참여하지 않아도 된다는 의미이다.**

Tham gia tùy chọn nghĩa là Instance của Entity có thể không tham gia vào quan hệ.

Ví dụ:

```
Một Customer có thể chưa từng tạo Order.
```

Khi đó phía `CUSTOMER` có thể có số lượng Order bằng 0.

---

Khi gom phần **Keyword: 선택 참여** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 선택 참여**. Bây giờ chuyển sang **15. ERD 표기법 - Các ký pháp ERD**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **15. ERD 표기법 - Các ký pháp ERD** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Ký pháp ERD là ngôn ngữ biểu diễn, không thay thế ngữ nghĩa nghiệp vụ. Khi đọc đúng đường nối và cardinality, ta mới có thể định nghĩa entity như một lớp đối tượng có identity riêng.

## 15. ERD 표기법 - Các ký pháp ERD

Khi gom phần **15. ERD 표기법 - Các ký pháp ERD** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **15. ERD 표기법 - Các ký pháp ERD**. Bây giờ chuyển sang **15.1. Chen notation**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **15.1. Chen notation** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 15.1. Chen notation

**Chen 표기법은 엔터티를 사각형, 관계를 마름모, 관계차수를 숫자로 표현한다.**

Ký pháp Chen biểu diễn Entity bằng hình chữ nhật, Relationship bằng hình thoi và Cardinality bằng con số.

Trong hình:

```
부서 1 ── 포함한다 ── N 직원
```

Nghĩa là:

```
Một phòng ban bao gồm nhiều nhân viên.
```

Tiếng Hàn:

**한 부서는 여러 직원을 포함할 수 있다.**

Một phòng ban có thể bao gồm nhiều nhân viên.

**한 직원은 하나의 부서에 소속될 수 있다.**

Một nhân viên có thể thuộc một phòng ban.

---

Khi gom phần **15.1. Chen notation** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **15.1. Chen notation**. Bây giờ chuyển sang **15.2. IE / Crow’s Foot notation**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **15.2. IE / Crow’s Foot notation** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 15.2. IE / Crow’s Foot notation

**IE 표기법은 관계의 다수성을 까마귀발 모양으로 표현한다.**

Ký pháp IE biểu diễn quan hệ nhiều bằng hình chân quạ.

**IE 표기법은 관계차수와 필수·선택 여부를 기호로 함께 표현할 수 있다.**

Ký pháp IE có thể đồng thời biểu diễn Cardinality và tính bắt buộc hoặc tùy chọn bằng các ký hiệu.

Các ký hiệu thường gặp:

```
|  = đúng một
O  = không hoặc một, tùy chọn
<  = nhiều
```

Ví dụ:

```
부서 |──── O< 직원
```

Có thể hiểu là:

- Một Department có thể có 0 hoặc nhiều Employee.
- Một Employee thuộc về một Department.

---

Khi gom phần **15.2. IE / Crow’s Foot notation** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **15.2. IE / Crow’s Foot notation**. Bây giờ chuyển sang **16. Entity là gì?**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **16. Entity là gì?** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Entity là thứ được quản lý hoặc cần phân biệt trong phạm vi nghiệp vụ; không phải mọi danh từ đều tự động thành bảng. Cách entity tồn tại trong thực tế là bước tiếp theo để kiểm tra ranh giới đó.

## 16. Entity là gì?

Khi gom phần **16. Entity là gì?** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **16. Entity là gì?**. Bây giờ chuyển sang **16.1. Định nghĩa**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **16.1. Định nghĩa** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 16.1. Định nghĩa

**엔터티는 업무에 필요하고 유용한 정보를 저장하고 관리하기 위한 집합이다.**

Entity là tập hợp dùng để lưu trữ và quản lý những thông tin cần thiết, hữu ích cho nghiệp vụ.

**엔터티는 인스턴스의 집합이다.**

Entity là tập hợp các Instance.

Khi gom phần **16.1. Định nghĩa** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **16.1. Định nghĩa**. Bây giờ chuyển sang **Keyword: Entity**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: Entity** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: Entity

**엔터티는 업무적으로 관리해야 할 대상이며 데이터베이스에서는 일반적으로 테이블로 구현된다.**

Entity là đối tượng cần được quản lý về mặt nghiệp vụ và thường được triển khai thành Table trong database.

Ví dụ:

```
CUSTOMER Entity
```

có thể chứa các Instance:

```
C001 - Nguyễn Văn A
C002 - Trần Văn B
C003 - Lê Văn C
```

Entity là khái niệm tập hợp:

```
CUSTOMER = {C001, C002, C003}
```

---

Khi gom phần **Keyword: Entity** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: Entity**. Bây giờ chuyển sang **16.2. Instance là gì?**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **16.2. Instance là gì?** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 16.2. Instance là gì?

**인스턴스는 엔터티에 실제로 존재하는 각각의 개별 데이터이다.**

Instance là từng dữ liệu riêng lẻ thực sự tồn tại trong Entity.

Khi gom phần **16.2. Instance là gì?** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **16.2. Instance là gì?**. Bây giờ chuyển sang **Keyword: Instance**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: Instance** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: Instance

**인스턴스는 데이터베이스 테이블의 한 행 또는 레코드에 해당한다.**

Instance tương ứng với một dòng hoặc một Record trong bảng database.

Ví dụ:

```
CUSTOMER
CUSTOMER_ID | CUSTOMER_NAME
------------|--------------
C001        | Nguyễn Văn A
C002        | Trần Văn B
```

Ở đây:

- `CUSTOMER` là Entity.
- `C001` là một Instance.
- `C002` là một Instance.

---

Khi gom phần **Keyword: Instance** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: Instance**. Bây giờ chuyển sang **17. Phân loại Entity theo hình thức tồn tại**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **17. Phân loại Entity theo hình thức tồn tại** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Phân loại entity theo hình thức tồn tại cho biết ta đang mô hình hóa người/vật, sự kiện hay khái niệm phụ thuộc. Phân loại theo thời điểm phát sinh bổ sung câu hỏi entity là ổn định hay được tạo theo giao dịch.

## 17. Phân loại Entity theo hình thức tồn tại

Hình chia Entity theo “유무형에 따른 분류”, nghĩa là phân loại theo việc có tồn tại dưới dạng vật chất hay không.

Gồm:

1. 유형 Entity - Tangible Entity.
2. 개념 Entity - Conceptual Entity.
3. 사건 Entity - Event Entity.

---

Khi gom phần **17. Phân loại Entity theo hình thức tồn tại** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **17. Phân loại Entity theo hình thức tồn tại**. Bây giờ chuyển sang **17.1. 유형 Entity - Entity hữu hình**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **17.1. 유형 Entity - Entity hữu hình** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 17.1. 유형 Entity - Entity hữu hình

**유형 엔터티는 물리적인 형태가 존재하고 안정적이며 지속적으로 활용되는 엔터티이다.**

Entity hữu hình là Entity có hình dạng vật lý, ổn định và được sử dụng lâu dài.

Ví dụ trong hình:

```
교수 - Giáo sư
강의실 - Phòng học
물품 - Hàng hóa
사원 - Nhân viên
```

Khi gom phần **17.1. 유형 Entity - Entity hữu hình** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **17.1. 유형 Entity - Entity hữu hình**. Bây giờ chuyển sang **Keyword: 유형 Entity**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 유형 Entity** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 유형 Entity

**유형 엔터티는 실제 세계에서 눈으로 확인하거나 물리적으로 존재하는 대상을 관리하는 엔터티이다.**

Entity hữu hình quản lý những đối tượng tồn tại vật lý trong thế giới thực, có thể quan sát hoặc nhận biết được.

Ví dụ:

```
EMPLOYEE
PRODUCT
CLASSROOM
PROFESSOR
```

Đặc điểm:

- Thường tồn tại ổn định.
- Có thể xác định bằng mã.
- Có thể quản lý vòng đời.
- Thường là Basic/Key Entity.

---

Khi gom phần **Keyword: 유형 Entity** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 유형 Entity**. Bây giờ chuyển sang **17.2. 개념 Entity - Entity khái niệm**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **17.2. 개념 Entity - Entity khái niệm** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 17.2. 개념 Entity - Entity khái niệm

**개념 엔터티는 물리적인 형태는 없지만 업무에서 관리해야 하는 개념적인 정보이다.**

Entity khái niệm không có hình dạng vật lý nhưng là thông tin khái niệm cần được quản lý trong nghiệp vụ.

Ví dụ trong hình:

```
수업 - Lớp học / Buổi học
보험상품 - Sản phẩm bảo hiểm
시스템 - Hệ thống
조직 - Tổ chức
```

Khi gom phần **17.2. 개념 Entity - Entity khái niệm** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **17.2. 개념 Entity - Entity khái niệm**. Bây giờ chuyển sang **Keyword: 개념 Entity**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 개념 Entity** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 개념 Entity

**개념 엔터티는 물리적으로 만질 수 없지만 업무 규칙과 관리 대상이 존재하는 엔터티이다.**

Entity khái niệm không thể cầm nắm về mặt vật lý nhưng có quy tắc nghiệp vụ và đối tượng quản lý rõ ràng.

Ví dụ:

```
DEPARTMENT
COURSE
INSURANCE_PRODUCT
SYSTEM
```

Một Department không phải là một vật thể đơn lẻ cần cầm nắm, nhưng vẫn là đối tượng nghiệp vụ cần quản lý.

---

Khi gom phần **Keyword: 개념 Entity** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 개념 Entity**. Bây giờ chuyển sang **17.3. 사건 Entity - Entity sự kiện**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **17.3. 사건 Entity - Entity sự kiện** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 17.3. 사건 Entity - Entity sự kiện

**사건 엔터티는 업무 수행 과정에서 발생하며 발생량이 비교적 많은 엔터티이다.**

Entity sự kiện phát sinh trong quá trình thực hiện nghiệp vụ và thường có số lượng phát sinh tương đối lớn.

Ví dụ trong hình:

```
수강신청 - Đăng ký môn học
주문 - Đơn hàng
입금 - Nộp tiền / Thanh toán
미납 - Chưa thanh toán
```

Khi gom phần **17.3. 사건 Entity - Entity sự kiện** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **17.3. 사건 Entity - Entity sự kiện**. Bây giờ chuyển sang **Keyword: 사건 Entity**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 사건 Entity** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 사건 Entity

**사건 엔터티는 업무가 실행될 때마다 새롭게 발생하는 거래 또는 활동을 저장하는 엔터티이다.**

Entity sự kiện lưu các giao dịch hoặc hoạt động phát sinh mới mỗi khi nghiệp vụ được thực hiện.

Ví dụ:

```
ORDER
PAYMENT
ENROLLMENT
PURCHASE
ATTENDANCE
```

Một khách hàng có thể đặt hàng nhiều lần, nên `ORDER` có thể phát sinh rất nhiều Instance.

---

Khi gom phần **Keyword: 사건 Entity** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 사건 Entity**. Bây giờ chuyển sang **17.4. Khi nào sự kiện là Relationship, khi nào là Entity?**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **17.4. Khi nào sự kiện là Relationship, khi nào là Entity?** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 17.4. Khi nào sự kiện là Relationship, khi nào là Entity?

**사건을 관계로 표현할지 엔터티로 표현할지는 그 사건이 관리해야 할 속성과 독립적인 데이터 집합을 가지는지에 따라 결정한다.**

Việc biểu diễn một sự kiện dưới dạng Relationship hay Entity phụ thuộc vào việc sự kiện đó có Attribute cần quản lý và có trở thành một tập dữ liệu độc lập hay không.

Ví dụ đơn giản:

```
STUDENT ── 수강한다 ── COURSE
```

Nếu chỉ cần biểu diễn việc sinh viên học môn học, có thể dùng Relationship.

Nhưng nếu cần lưu:

```
등록일
성적
출석률
수강상태
```

thì nên tạo Entity trung gian:

```
ENROLLMENT
----------
STUDENT_ID
COURSE_ID
ENROLL_DATE
GRADE
ATTENDANCE_RATE
STATUS
```

Khi gom phần **17.4. Khi nào sự kiện là Relationship, khi nào là Entity?** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **17.4. Khi nào sự kiện là Relationship, khi nào là Entity?**. Bây giờ chuyển sang **Cách hiểu**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Cách hiểu** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Cách hiểu

**관리해야 할 속성이 많으면 사건을 엔터티로 분리하는 것이 적절하다.**

Nếu sự kiện có nhiều Attribute cần quản lý thì nên tách nó thành Entity.

---

Khi gom phần **Cách hiểu** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Cách hiểu**. Bây giờ chuyển sang **17.5. Entity phụ thuộc**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **17.5. Entity phụ thuộc** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 17.5. Entity phụ thuộc

**사건 엔터티는 혼자 존재하기 어렵고 다른 엔터티에 의존하는 경우가 많다.**

Entity sự kiện thường khó tồn tại độc lập và phụ thuộc vào các Entity khác.

Ví dụ trong hình:

```
수강신청은 학생과 수업이 있어야 발생한다.
```

Đăng ký môn học chỉ có thể phát sinh khi tồn tại sinh viên và lớp học.

```
STUDENT + COURSE → ENROLLMENT
```

Khi gom phần **17.5. Entity phụ thuộc** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **17.5. Entity phụ thuộc**. Bây giờ chuyển sang **Keyword: 의존**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 의존** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 의존

**의존한다는 것은 다른 엔터티가 존재해야 해당 엔터티도 존재할 수 있다는 의미이다.**

Phụ thuộc nghĩa là Entity đó chỉ có thể tồn tại khi Entity khác tồn tại.

Ví dụ:

- Không thể có `ORDER_ITEM` nếu không có `ORDER`.
- Không thể có `ENROLLMENT` nếu không có `STUDENT`.
- Không thể có `PAYMENT` nếu không có giao dịch cần thanh toán.

---

Khi gom phần **Keyword: 의존** lại, ta không cần nhớ các dòng như những mảnh rời: ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 의존**. Bây giờ chuyển sang **18. Phân loại Entity theo thời điểm phát sinh**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **18. Phân loại Entity theo thời điểm phát sinh** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Entity có thể tồn tại thường trực, phát sinh theo sự kiện hoặc thay đổi theo kỳ; điều đó ảnh hưởng lifecycle và khóa. Đặt các loại cạnh nhau giúp nhìn ra quan hệ giữa chúng trong một sơ đồ chung.

## 18. Phân loại Entity theo thời điểm phát sinh

Hình chia thành:

```
기본/키 Entity
중심 Entity
행위 Entity
```

---

Khi gom phần **18. Phân loại Entity theo thời điểm phát sinh** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **18. Phân loại Entity theo thời điểm phát sinh**. Bây giờ chuyển sang **18.1. 기본/키 Entity - Basic hoặc Key Entity**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **18.1. 기본/키 Entity - Basic hoặc Key Entity** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 18.1. 기본/키 Entity - Basic hoặc Key Entity

**기본 엔터티는 업무에 본래 존재하며 독립적으로 생성되는 엔터티이다.**

Entity cơ bản là Entity vốn tồn tại trong nghiệp vụ và được tạo ra một cách độc lập.

**기본 엔터티는 다른 엔터티의 부모 역할을 하며 자신의 고유한 식별자를 가진다.**

Entity cơ bản đóng vai trò Entity cha của các Entity khác và có Identifier riêng.

Ví dụ trong hình:

```
사원 - Nhân viên
부서 - Phòng ban
고객 - Khách hàng
상품 - Sản phẩm
자재 - Vật tư
```

Khi gom phần **18.1. 기본/키 Entity - Basic hoặc Key Entity** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **18.1. 기본/키 Entity - Basic hoặc Key Entity**. Bây giờ chuyển sang **Keyword: 기본 Entity**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 기본 Entity** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 기본 Entity

**기본 엔터티는 다른 엔터티가 발생하기 전에 먼저 존재할 수 있는 엔터티이다.**

Entity cơ bản là Entity có thể tồn tại trước khi các Entity khác phát sinh.

Ví dụ:

```
CUSTOMER
PRODUCT
DEPARTMENT
EMPLOYEE
```

Trước khi có đơn hàng, phải có:

- Khách hàng.
- Sản phẩm.

---

Khi gom phần **Keyword: 기본 Entity** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 기본 Entity**. Bây giờ chuyển sang **18.2. 중심 Entity - Entity trung tâm**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **18.2. 중심 Entity - Entity trung tâm** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 18.2. 중심 Entity - Entity trung tâm

**중심 엔터티는 기본 엔터티로부터 발생하고 업무의 중심적인 역할을 하는 엔터티이다.**

Entity trung tâm phát sinh từ Entity cơ bản và đóng vai trò trung tâm trong nghiệp vụ.

Ví dụ trong hình:

```
접수 - Tiếp nhận
계약 - Hợp đồng
```

Ví dụ mở rộng:

```
CUSTOMER → ORDER
CUSTOMER → CONTRACT
```

Một khách hàng tồn tại trước, sau đó có thể phát sinh đơn hàng hoặc hợp đồng.

Khi gom phần **18.2. 중심 Entity - Entity trung tâm** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **18.2. 중심 Entity - Entity trung tâm**. Bây giờ chuyển sang **Keyword: 중심 Entity**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 중심 Entity** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 중심 Entity

**중심 엔터티는 업무 흐름에서 핵심적인 거래나 처리 대상을 나타낸다.**

Entity trung tâm biểu diễn giao dịch hoặc đối tượng xử lý cốt lõi trong luồng nghiệp vụ.

---

Khi gom phần **Keyword: 중심 Entity** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 중심 Entity**. Bây giờ chuyển sang **18.3. 행위 Entity - Entity hành vi**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **18.3. 행위 Entity - Entity hành vi** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 18.3. 행위 Entity - Entity hành vi

**행위 엔터티는 두 개 이상의 엔터티로부터 발생하고 업무 활동의 결과로 생성된다.**

Entity hành vi phát sinh từ hai hoặc nhiều Entity và được tạo ra như kết quả của hoạt động nghiệp vụ.

Ví dụ trong hình:

```
주문내역 - Chi tiết đơn hàng
계약진행 - Tiến hành hợp đồng
```

Ví dụ:

```
ORDER_ITEM
```

được tạo từ:

```
ORDER + PRODUCT
```

```
ORDER + PRODUCT → ORDER_ITEM
```

Khi gom phần **18.3. 행위 Entity - Entity hành vi** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **18.3. 행위 Entity - Entity hành vi**. Bây giờ chuyển sang **Keyword: 행위 Entity**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 행위 Entity** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 행위 Entity

**행위 엔터티는 업무가 실행된 결과를 저장하며 일반적으로 발생 빈도가 높다.**

Entity hành vi lưu kết quả của việc thực hiện nghiệp vụ và thường có tần suất phát sinh cao.

Ví dụ:

```
ORDER_ITEM
PAYMENT_HISTORY
ENROLLMENT
CONTRACT_PROCESS
DELIVERY_HISTORY
```

---

Khi gom phần **Keyword: 행위 Entity** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 행위 Entity**. Bây giờ chuyển sang **19. Sơ đồ quan hệ giữa các loại Entity**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **19. Sơ đồ quan hệ giữa các loại Entity** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Sơ đồ quan hệ giữa các loại entity gom các phân loại thành bức tranh tổng thể về ownership và dependency. Trước khi chuyển sang Attribute, cần chốt lại các keyword và ranh giới đã rút ra từ hai hình.

## 19. Sơ đồ quan hệ giữa các loại Entity

Phần này nối mạch SQL với “19. Sơ đồ quan hệ giữa các loại Entity”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```
기본/키 엔터티
      ↓
중심 엔터티
      ↓
행위 엔터티
```

Ví dụ trong hệ thống bán hàng:

```
CUSTOMER + PRODUCT
        ↓
      ORDER
        ↓
   ORDER_ITEM
```

Giải thích:

- `CUSTOMER` và `PRODUCT` là Basic/Key Entity.
- `ORDER` là Central Entity.
- `ORDER_ITEM` là Action Entity.

**기본 엔터티는 먼저 존재하고 중심 엔터티를 발생시키며 행위 엔터티는 업무 처리 결과로 생성된다.**

Basic Entity tồn tại trước, tạo ra Central Entity, còn Action Entity được tạo ra như kết quả xử lý nghiệp vụ.

---

Khi gom phần **19. Sơ đồ quan hệ giữa các loại Entity** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **19. Sơ đồ quan hệ giữa các loại Entity**. Bây giờ chuyển sang **20. Tổng hợp keyword của hai hình**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **20. Tổng hợp keyword của hai hình** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Tổng hợp hai hình chuyển danh sách phân loại thành vocabulary dùng chung cho ERD. Từ đây, Attribute được mở như một phần riêng vì thuộc tính chỉ có nghĩa khi gắn với entity và value.

## 20. Tổng hợp keyword của hai hình

Phần này nối mạch SQL với “20. Tổng hợp keyword của hai hình”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

| Keyword | Nghĩa tiếng Việt | Cách hiểu ngắn |
| --- | --- | --- |
| 완전성 | Tính đầy đủ | Không bỏ sót dữ liệu cần thiết |
| 중복배제 | Loại bỏ trùng lặp | Một sự thật chỉ ghi một nơi |
| 업무규칙 | Quy tắc nghiệp vụ | Điều kiện nghiệp vụ phải tuân thủ |
| 데이터 재사용 | Tái sử dụng dữ liệu | Dữ liệu chung dùng ở nhiều nơi |
| 의사소통 | Giao tiếp | Mọi bên hiểu mô hình cùng một nghĩa |
| 통합성 | Tính tích hợp | Toàn tổ chức dùng cùng định nghĩa |
| ERD | Sơ đồ quan hệ thực thể | Biểu diễn Entity và Relationship |
| 관계차수 | Cardinality | 1:1, 1:N, N:M |
| 참여도 | Mức độ tham gia | Bắt buộc hay tùy chọn |
| 식별자 관계 | Quan hệ định danh | PK của cha là một phần PK của con |
| 엔터티 | Entity | Tập hợp thông tin cần quản lý |
| 인스턴스 | Instance | Một dòng dữ liệu cụ thể |
| 유형 Entity | Entity hữu hình | Nhân viên, sản phẩm, phòng học |
| 개념 Entity | Entity khái niệm | Tổ chức, hệ thống, môn học |
| 사건 Entity | Entity sự kiện | Đơn hàng, thanh toán, đăng ký |
| 기본/키 Entity | Entity cơ bản | Khách hàng, sản phẩm, phòng ban |
| 중심 Entity | Entity trung tâm | Hợp đồng, tiếp nhận |
| 행위 Entity | Entity hành vi | Chi tiết đơn hàng, tiến hành hợp đồng |

Khi gom phần **20. Tổng hợp keyword của hai hình** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **20. Tổng hợp keyword của hai hình**. Bây giờ chuyển sang **Câu ghi nhớ cuối cùng**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Câu ghi nhớ cuối cùng** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### Câu ghi nhớ cuối cùng

**좋은 데이터 모델은 필요한 데이터를 빠짐없이 포함하고, 불필요한 중복을 제거하며, 업무규칙과 데이터 관계를 명확하게 표현해야 한다.**

Một mô hình dữ liệu tốt phải bao gồm đầy đủ dữ liệu cần thiết, loại bỏ trùng lặp không cần thiết và biểu diễn rõ quy tắc nghiệp vụ cùng quan hệ giữa dữ liệu.

**ERD는 이러한 데이터 모델을 엔터티, 관계, 관계차수, 참여도 등의 기호로 시각화한 산출물이다.**

ERD là sản phẩm trực quan hóa mô hình dữ liệu bằng các ký hiệu như Entity, Relationship, Cardinality và mức độ tham gia.

**엔터티는 업무 대상이며, 인스턴스는 그 엔터티에 실제로 저장된 각각의 데이터이다.**

Entity là đối tượng nghiệp vụ, còn Instance là từng dữ liệu thực tế được lưu trong Entity đó.

Khi gom phần **Câu ghi nhớ cuối cùng** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Câu ghi nhớ cuối cùng**. Bây giờ chuyển sang **제 3절 속성 - Phần 3: Attribute**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **제 3절 속성 - Phần 3: Attribute** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Phần Attribute bắt đầu từ việc phân biệt thuộc tính với entity và relationship. Sau khung khái niệm, định nghĩa Attribute sẽ đặt điều kiện để một đặc tính trở thành dữ liệu cần lưu.

## 제 3절 속성 - Phần 3: Attribute

Khi gom phần **제 3절 속성 - Phần 3: Attribute** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **제 3절 속성 - Phần 3: Attribute**. Bây giờ chuyển sang **1. 속성의 정의 - Định nghĩa Attribute**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **1. 속성의 정의 - Định nghĩa Attribute** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Attribute mô tả một khía cạnh của entity tại grain đã chọn, nhưng giá trị của nó phải có ngữ nghĩa và miền hợp lệ. Quan hệ giữa entity, instance, attribute và value giúp đặt từng giá trị vào đúng tầng.

## 1. 속성의 정의 - Định nghĩa Attribute

Khi gom phần **1. 속성의 정의 - Định nghĩa Attribute** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **1. 속성의 정의 - Định nghĩa Attribute**. Bây giờ chuyển sang **1.1. Định nghĩa trong tài liệu**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **1.1. Định nghĩa trong tài liệu** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 1.1. Định nghĩa trong tài liệu

**속성은 사물의 성질 또는 본질을 의미한다.**

Attribute có nghĩa là đặc tính hoặc bản chất của một sự vật.

**데이터 모델링에서 속성은 업무에서 필요한 인스턴스의 관리 대상 중 더 이상 분리되지 않는 최소 단위의 데이터이다.**

Trong mô hình hóa dữ liệu, Attribute là đơn vị dữ liệu nhỏ nhất không thể tiếp tục tách ra trong những thông tin của Instance mà nghiệp vụ cần quản lý.

Khi gom phần **1.1. Định nghĩa trong tài liệu** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **1.1. Định nghĩa trong tài liệu**. Bây giờ chuyển sang **Keyword: 속성(Attribute)**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 속성(Attribute)** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 속성(Attribute)

**속성은 엔터티를 설명하고 구체화하는 데이터 항목이다.**

Attribute là mục dữ liệu dùng để mô tả và cụ thể hóa một Entity.

Ví dụ Entity `학생`:

```
학생
- 학번
- 이름
- 전공
- 학점
```

Trong đó:

- `학생` là Entity.
- `학번`, `이름`, `전공`, `학점` là Attribute.
- Mỗi sinh viên cụ thể là một Instance.

Có thể hình dung:

```
Entity    = Học sinh / Sinh viên
Attribute = Mã số, tên, chuyên ngành, điểm
Instance  = 100번 홍길동 컴퓨터공학과 4.0
```

---

Khi gom phần **Keyword: 속성(Attribute)** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 속성(Attribute)**. Bây giờ chuyển sang **1.2. “Đơn vị dữ liệu nhỏ nhất” nghĩa là gì?**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **1.2. “Đơn vị dữ liệu nhỏ nhất” nghĩa là gì?** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 1.2. “Đơn vị dữ liệu nhỏ nhất” nghĩa là gì?

**속성은 업무적으로 의미가 있는 최소 단위까지 분리되어야 한다.**

Attribute phải được phân tách đến đơn vị nhỏ nhất có ý nghĩa đối với nghiệp vụ.

Khi gom phần **1.2. “Đơn vị dữ liệu nhỏ nhất” nghĩa là gì?** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **1.2. “Đơn vị dữ liệu nhỏ nhất” nghĩa là gì?**. Bây giờ chuyển sang **Ví dụ trong hình**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Ví dụ trong hình** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Ví dụ trong hình

Tài liệu ghi:

```
나이, 이름 등
```

Tuổi và tên là những Attribute riêng biệt.

Không nên gộp thành:

```
신상정보
```

vì `신상정보` chỉ là một khái niệm chung, chưa phải đơn vị dữ liệu nhỏ nhất.

Khi gom phần **Ví dụ trong hình** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Ví dụ trong hình**. Bây giờ chuyển sang **Ví dụ địa chỉ**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Ví dụ địa chỉ** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Ví dụ địa chỉ

**주소는 업무 목적에 따라 시, 구, 동, 번지 등으로 분리할 수 있다.**

Tùy mục đích nghiệp vụ, địa chỉ có thể được tách thành thành phố, quận, phường và số nhà.

Ví dụ:

```
주소 = 서울시 종로구 종로 1
```

Có thể tách thành:

```
시     = 서울시
구     = 종로구
도로명 = 종로
번지   = 1
```

Nhưng trong hình tài liệu ghi rằng không phải lúc nào thông tin cá nhân cũng bắt buộc phải tách thành Attribute riêng.

**업무에서 주소를 하나의 값으로만 사용한다면 주소를 하나의 속성으로 관리할 수 있다.**

Nếu nghiệp vụ chỉ sử dụng địa chỉ như một giá trị duy nhất thì có thể quản lý địa chỉ bằng một Attribute duy nhất.

Khi gom phần **Ví dụ địa chỉ** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Ví dụ địa chỉ**. Bây giờ chuyển sang **Cách quyết định có tách hay không**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Cách quyết định có tách hay không** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Cách quyết định có tách hay không

**속성의 분리 여부는 업무에서 해당 데이터를 어떻게 조회하고 관리하는지에 따라 결정한다.**

Việc có tách Attribute hay không phụ thuộc vào cách nghiệp vụ truy vấn và quản lý dữ liệu đó.

Nếu cần tìm:

```
WHERE CITY = '서울'
```

thì nên tách `CITY`.

Nếu chỉ cần hiển thị toàn bộ địa chỉ:

```
서울시 종로구 종로 1
```

thì có thể để thành một Attribute `ADDRESS`.

Khi gom phần **Cách quyết định có tách hay không** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Cách quyết định có tách hay không**. Bây giờ chuyển sang **Keyword: 최소 단위**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 최소 단위** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 최소 단위

**최소 단위란 더 이상 분리하지 않아도 업무적으로 독립된 의미를 유지하는 가장 작은 데이터 단위이다.**

Đơn vị nhỏ nhất là đơn vị dữ liệu nhỏ nhất vẫn giữ được ý nghĩa độc lập về mặt nghiệp vụ khi không tách thêm.

---

Khi gom phần **Keyword: 최소 단위** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 최소 단위**. Bây giờ chuyển sang **2. Quan hệ giữa Entity, Instance, Attribute và Attribute Value**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **2. Quan hệ giữa Entity, Instance, Attribute và Attribute Value** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Phân biệt entity, instance, attribute và attribute value ngăn việc biến một giá trị cụ thể thành cột hoặc bảng sai chỗ. Từ quan hệ đó, có thể rút ra các đặc điểm dùng để đánh giá chất lượng Attribute.

## 2. Quan hệ giữa Entity, Instance, Attribute và Attribute Value

Khi gom phần **2. Quan hệ giữa Entity, Instance, Attribute và Attribute Value** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **2. Quan hệ giữa Entity, Instance, Attribute và Attribute Value**. Bây giờ chuyển sang **2.1. Một Entity phải có Instance**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **2.1. Một Entity phải có Instance** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 2.1. Một Entity phải có Instance

**하나의 엔터티는 두 개 이상의 인스턴스 집합이어야 한다.**

Một Entity phải là tập hợp gồm từ hai Instance trở lên.

Khi gom phần **2.1. Một Entity phải có Instance** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **2.1. Một Entity phải có Instance**. Bây giờ chuyển sang **Keyword: Instance**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: Instance** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: Instance

**인스턴스는 엔터티에 실제로 저장된 각각의 개별 데이터이다.**

Instance là từng dữ liệu cụ thể được lưu trong Entity.

Ví dụ:

```
학생 Entity
```

có các Instance:

```
100번 학생
200번 학생
300번 학생
```

Biểu diễn dưới dạng bảng:

| 학번 | 이름 | 전공 | 학점 |
| --- | --- | --- | --- |
| 100 | 홍길동 | 컴퓨터공학과 | 4.0 |
| 200 | 정지희 | 화학공학과 | 3.8 |
| 300 | 김상민 | 물리학과 | 4.3 |

Ở đây:

- Bảng `학생` là Entity.
- Mỗi hàng là một Instance.
- Toàn bộ các hàng tạo thành tập hợp Instance của Entity.

Khi gom phần **Keyword: Instance** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: Instance**. Bây giờ chuyển sang **Lưu ý quan trọng**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Lưu ý quan trọng** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Lưu ý quan trọng

Trong tài liệu thi, câu “một Entity phải có từ hai Instance trở lên” thường được dùng để phân biệt Entity với một đối tượng đơn lẻ.

Tuy nhiên, trong database thực tế, một bảng mới tạo có thể chưa có dữ liệu:

```
CREATE TABLE STUDENT (...);
```

Lúc này bảng vẫn là Entity dù chưa có Instance. Vì vậy:

**시험에서는 엔터티를 인스턴스의 집합으로 이해하되, 실제 테이블은 인스턴스가 0개인 상태에서도 존재할 수 있다.**

Khi thi, hãy hiểu Entity là tập hợp các Instance, nhưng trong thực tế một Table vẫn có thể tồn tại khi chưa có Instance nào.

---

Khi gom phần **Lưu ý quan trọng** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Lưu ý quan trọng**. Bây giờ chuyển sang **2.2. Một Entity có từ hai Attribute trở lên**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **2.2. Một Entity có từ hai Attribute trở lên** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 2.2. Một Entity có từ hai Attribute trở lên

**하나의 엔터티는 두 개 이상의 속성을 가져야 한다.**

Một Entity phải có từ hai Attribute trở lên.

Ví dụ:

```
학생
- 학번
- 이름
- 전공
- 학점
```

Entity `학생` có bốn Attribute.

Nếu chỉ có một thuộc tính duy nhất thì thường chưa đủ để mô tả một Entity có ý nghĩa.

Khi gom phần **2.2. Một Entity có từ hai Attribute trở lên** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **2.2. Một Entity có từ hai Attribute trở lên**. Bây giờ chuyển sang **Keyword: Entity 구성**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: Entity 구성** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: Entity 구성

**엔터티의 구성은 엔터티, 속성, 인스턴스의 관계로 이해해야 한다.**

Cấu thành của Entity phải được hiểu thông qua quan hệ giữa Entity, Attribute và Instance.

```
Entity
 ├── Attribute 1
 ├── Attribute 2
 └── Attribute 3

Entity
 ├── Instance 1
 ├── Instance 2
 └── Instance 3
```

---

Khi gom phần **Keyword: Entity 구성** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: Entity 구성**. Bây giờ chuyển sang **2.3. Một Attribute có một Attribute Value**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **2.3. Một Attribute có một Attribute Value** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 2.3. Một Attribute có một Attribute Value

**하나의 속성은 하나의 속성값을 가져야 한다.**

Một Attribute phải có một Attribute Value.

Trong bảng:

```
학번 | 이름 | 전공 | 학점
100  | 홍길동 | 컴퓨터공학과 | 4.0
```

Mỗi ô chỉ có một giá trị:

```
학번 = 100
이름 = 홍길동
전공 = 컴퓨터공학과
학점 = 4.0
```

Khi gom phần **2.3. Một Attribute có một Attribute Value** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **2.3. Một Attribute có một Attribute Value**. Bây giờ chuyển sang **Ví dụ sai trong tài liệu**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Ví dụ sai trong tài liệu** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Ví dụ sai trong tài liệu

Phần này nối mạch SQL với “Ví dụ sai trong tài liệu”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```
나이 = 25, 370
```

Một ô không được chứa đồng thời hai giá trị `25` và `370`.

**한 속성값에 25와 370을 함께 저장하면 하나의 속성이 여러 값을 가지게 되므로 원자성이 깨진다.**

Nếu lưu đồng thời `25` và `370` trong một Attribute Value thì một Attribute có nhiều giá trị và tính nguyên tử bị phá vỡ.

Khi gom phần **Ví dụ sai trong tài liệu** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Ví dụ sai trong tài liệu**. Bây giờ chuyển sang **Keyword: 원자성(Atomicity)**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 원자성(Atomicity)** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 원자성(Atomicity)

**원자성은 하나의 속성값이 더 이상 분해할 수 없는 하나의 값이어야 한다는 의미이다.**

Tính nguyên tử nghĩa là mỗi Attribute Value phải là một giá trị duy nhất, không thể tiếp tục chia nhỏ trong phạm vi đó.

Ví dụ sai:

```
PHONE = 010-1111-1111, 010-2222-2222
```

Ví dụ đúng nếu chỉ quản lý một số điện thoại:

```
PHONE = 010-1111-1111
```

Nếu một người có nhiều số điện thoại, không nên nhét tất cả vào một ô. Có thể tạo bảng riêng:

```
STUDENT
-------
STUDENT_ID
STUDENT_NAME

STUDENT_PHONE
-------------
STUDENT_ID
PHONE
PHONE_TYPE
```

Hoặc tạo các cột riêng nếu số lượng loại điện thoại được cố định:

```
PHONE_HOME
PHONE_MOBILE
PHONE_WORK
```

Trong thiết kế quan hệ và chuẩn hóa, cách tạo bảng riêng thường linh hoạt hơn.

---

Khi gom phần **Keyword: 원자성(Atomicity)** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 원자성(Atomicity)**. Bây giờ chuyển sang **3. 속성의 특징 - Đặc điểm của Attribute**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **3. 속성의 특징 - Đặc điểm của Attribute** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Đặc điểm của Attribute gồm tính đơn trị, ổn định, phụ thuộc và khả năng suy diễn; các đặc điểm này quyết định lưu trực tiếp hay tính ra. Trước khi chọn kiểu dữ liệu, cần đặt tên nhất quán để schema dễ đọc và ít mơ hồ.

## 3. 속성의 특징 - Đặc điểm của Attribute

Khi gom phần **3. 속성의 특징 - Đặc điểm của Attribute** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **3. 속성의 특징 - Đặc điểm của Attribute**. Bây giờ chuyển sang **3.1. Attribute là thông tin cần quản lý trong nghiệp vụ**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **3.1. Attribute là thông tin cần quản lý trong nghiệp vụ** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 3.1. Attribute là thông tin cần quản lý trong nghiệp vụ

**속성은 해당 업무에서 필요하고 관리해야 하는 정보이다.**

Attribute là thông tin cần thiết và phải được quản lý trong nghiệp vụ tương ứng.

Khi gom phần **3.1. Attribute là thông tin cần quản lý trong nghiệp vụ** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **3.1. Attribute là thông tin cần quản lý trong nghiệp vụ**. Bây giờ chuyển sang **Keyword: 업무 필요성**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 업무 필요성** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 업무 필요성

**업무 필요성은 해당 데이터가 실제 업무 처리, 조회, 분석 또는 규칙에 사용되는지를 의미한다.**

Tính cần thiết đối với nghiệp vụ nghĩa là dữ liệu đó có được dùng trong xử lý, truy vấn, phân tích hoặc quy tắc nghiệp vụ hay không.

Ví dụ trong hệ thống nhân sự:

```
사원번호
사원명
입사일
부서코드
급여
```

đều là thông tin cần quản lý.

Nhưng:

```
Nhân viên thích uống cà phê gì
Màu áo nhân viên mặc hôm nay
```

có thể không phải Attribute cần thiết nếu không phục vụ nghiệp vụ.

---

Khi gom phần **Keyword: 업무 필요성** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 업무 필요성**. Bây giờ chuyển sang **3.2. Attribute phải phụ thuộc hàm vào Identifier**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **3.2. Attribute phải phụ thuộc hàm vào Identifier** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 3.2. Attribute phải phụ thuộc hàm vào Identifier

**속성은 정규화 이론에 근거하여 주식별자에 함수적으로 종속되어야 한다.**

Theo lý thuyết chuẩn hóa, Attribute phải phụ thuộc hàm vào khóa định danh chính.

Khi gom phần **3.2. Attribute phải phụ thuộc hàm vào Identifier** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **3.2. Attribute phải phụ thuộc hàm vào Identifier**. Bây giờ chuyển sang **Keyword: 주식별자**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 주식별자** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 주식별자

**주식별자는 엔터티의 각 인스턴스를 유일하게 식별하는 속성 또는 속성 집합이다.**

Khóa định danh chính là Attribute hoặc tập hợp Attribute dùng để xác định duy nhất mỗi Instance của Entity.

Ví dụ:

```
학생
- 학번 PK
- 이름
- 전공
- 학점
```

`학번` là khóa chính.

Khi biết:

```
학번 = 100
```

ta xác định được:

```
이름 = 홍길동
전공 = 컴퓨터공학과
학점 = 4.0
```

Biểu diễn phụ thuộc hàm:

```
학번 → 이름, 전공, 학점
```

Khi gom phần **Keyword: 주식별자** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 주식별자**. Bây giờ chuyển sang **Keyword: 함수적 종속**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 함수적 종속** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 함수적 종속

**함수적 종속은 어떤 속성값을 알면 다른 속성값을 유일하게 결정할 수 있는 관계이다.**

Phụ thuộc hàm là quan hệ trong đó biết giá trị của một Attribute thì có thể xác định duy nhất giá trị của Attribute khác.

Ví dụ:

```
학번 → 학생이름
```

Nhưng:

```
학생이름 → 학번
```

có thể không đúng vì có thể có nhiều người cùng tên.

---

Khi gom phần **Keyword: 함수적 종속** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 함수적 종속**. Bây giờ chuyển sang **3.3. Attribute được quyết định bởi Identifier**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **3.3. Attribute được quyết định bởi Identifier** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 3.3. Attribute được quyết định bởi Identifier

**주식별자가 결정되면 다른 속성의 값도 결정되어야 한다.**

Khi khóa định danh được xác định thì giá trị của các Attribute khác cũng phải được xác định.

Ví dụ:

```
학번 = 100
```

phải xác định được một sinh viên cụ thể.

Không nên có dữ liệu:

```
학번 | 이름
-----|-----
100  | 홍길동
100  | 김상민
```

nếu `학번` được định nghĩa là mã duy nhất của sinh viên.

---

Khi gom phần **3.3. Attribute được quyết định bởi Identifier** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **3.3. Attribute được quyết định bởi Identifier**. Bây giờ chuyển sang **3.4. Một Attribute chỉ có một giá trị**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **3.4. Một Attribute chỉ có một giá trị** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 3.4. Một Attribute chỉ có một giá trị

**하나의 속성은 하나의 값만 가져야 한다.**

Một Attribute chỉ được có một giá trị.

Đây là nguyên tắc đã giải thích ở trên, liên quan đến:

- Tính nguyên tử.
- Chuẩn hóa 1NF.
- Thiết kế bảng.
- Tránh nhóm lặp.

Ví dụ sai:

```
취미 = 독서, 영화감상, 여행
```

Nếu `취미` là một Attribute thì đang chứa nhiều giá trị.

Có thể xử lý:

```
STUDENT_HOBBY
-------------
STUDENT_ID
HOBBY
```

Dữ liệu:

| STUDENT_ID | HOBBY |
| --- | --- |
| 100 | 독서 |
| 100 | 영화감상 |
| 100 | 여행 |

---

Khi gom phần **3.4. Một Attribute chỉ có một giá trị** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **3.4. Một Attribute chỉ có một giá trị**. Bây giờ chuyển sang **4. 속성의 명명 - Đặt tên Attribute**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **4. 속성의 명명 - Đặt tên Attribute** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Đặt tên Attribute phải phản ánh ý nghĩa, grain và đơn vị đo, tránh tên chung như value hoặc status. Khi tên đã rõ, ký pháp Attribute giúp biểu diễn domain, optionality và các ràng buộc liên quan.

## 4. 속성의 명명 - Đặt tên Attribute

Khi gom phần **4. 속성의 명명 - Đặt tên Attribute** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **4. 속성의 명명 - Đặt tên Attribute**. Bây giờ chuyển sang **4.1. Sử dụng tên được dùng trong nghiệp vụ**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **4.1. Sử dụng tên được dùng trong nghiệp vụ** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 4.1. Sử dụng tên được dùng trong nghiệp vụ

**속성명은 해당 업무에서 실제로 사용하는 이름을 부여해야 한다.**

Tên Attribute phải sử dụng tên thực tế được dùng trong nghiệp vụ.

Khi gom phần **4.1. Sử dụng tên được dùng trong nghiệp vụ** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **4.1. Sử dụng tên được dùng trong nghiệp vụ**. Bây giờ chuyển sang **Keyword: 속성명**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 속성명** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 속성명

**속성명은 데이터가 무엇을 의미하는지 나타내는 이름이다.**

Tên Attribute là tên cho biết dữ liệu đó có ý nghĩa gì.

Ví dụ:

Không nên đặt:

```
COL_01
DATA_A
VALUE_1
```

Nên đặt:

```
STUDENT_ID
STUDENT_NAME
DEPARTMENT_CODE
HIRE_DATE
```

---

Khi gom phần **Keyword: 속성명** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 속성명**. Bây giờ chuyển sang **4.2. Hạn chế sử dụng từ viết tắt**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **4.2. Hạn chế sử dụng từ viết tắt** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 4.2. Hạn chế sử dụng từ viết tắt

**약어 사용은 가급적 피해야 한다.**

Nên hạn chế sử dụng từ viết tắt.

Ví dụ không tốt:

```
STU_NM
DEPT_CD
EMP_NO
```

Ví dụ rõ ràng hơn:

```
STUDENT_NAME
DEPARTMENT_CODE
EMPLOYEE_NUMBER
```

Tuy nhiên, trong thực tế một số từ viết tắt phổ biến vẫn được sử dụng:

```
ID
PK
FK
URL
```

Khi gom phần **4.2. Hạn chế sử dụng từ viết tắt** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **4.2. Hạn chế sử dụng từ viết tắt**. Bây giờ chuyển sang **Keyword: 약어**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 약어** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 약어

**약어는 긴 단어나 표현을 짧게 줄여서 사용하는 것이다.**

Từ viết tắt là cách rút ngắn một từ hoặc cụm từ dài.

Trong SQLD, ý chính của tài liệu là tên Attribute phải dễ hiểu đối với nhiều người, không nên phụ thuộc vào cách viết tắt cá nhân.

---

Khi gom phần **Keyword: 약어** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 약어**. Bây giờ chuyển sang **4.3. Dùng danh từ, tránh dùng câu mô tả**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **4.3. Dùng danh từ, tránh dùng câu mô tả** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 4.3. Dùng danh từ, tránh dùng câu mô tả

**서술식 속성명보다 명사형 속성명을 사용하는 것이 좋다.**

Nên sử dụng tên Attribute dạng danh từ thay vì tên Attribute dạng câu mô tả.

Ví dụ không tốt:

```
고객이름을 저장한다
주문한 날짜를 입력한다
```

Ví dụ tốt:

```
고객명
주문일자
```

Khi gom phần **4.3. Dùng danh từ, tránh dùng câu mô tả** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **4.3. Dùng danh từ, tránh dùng câu mô tả**. Bây giờ chuyển sang **Keyword: 명사형**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 명사형** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 명사형

**명사형 속성명은 데이터의 대상을 간결하게 나타내는 이름이다.**

Tên Attribute dạng danh từ là tên ngắn gọn thể hiện đối tượng của dữ liệu.

---

Khi gom phần **Keyword: 명사형** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 명사형**. Bây giờ chuyển sang **4.4. Tránh tên chứa công thức hoặc sở hữu**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **4.4. Tránh tên chứa công thức hoặc sở hữu** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 4.4. Tránh tên chứa công thức hoặc sở hữu

**속성명에는 수식이나 소유격 표현을 사용하지 않는 것이 좋다.**

Không nên sử dụng công thức hoặc cách biểu đạt sở hữu trong tên Attribute.

Ví dụ không tốt:

```
학생의 이름
상품의 가격
가격 × 수량
```

Ví dụ tốt:

```
학생명
상품가격
주문금액
```

Nếu là giá trị tính toán:

```
ORDER_AMOUNT = UNIT_PRICE * QUANTITY
```

thì tên Attribute nên thể hiện kết quả nghiệp vụ:

```
주문금액
```

---

Khi gom phần **4.4. Tránh tên chứa công thức hoặc sở hữu** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **4.4. Tránh tên chứa công thức hoặc sở hữu**. Bây giờ chuyển sang **4.5. Tên Attribute phải duy nhất trong toàn mô hình**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **4.5. Tên Attribute phải duy nhất trong toàn mô hình** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 4.5. Tên Attribute phải duy nhất trong toàn mô hình

**속성의 이름은 전체 데이터 모델에서 유일성을 확보해야 한다.**

Tên Attribute phải bảo đảm tính duy nhất trong toàn bộ mô hình dữ liệu.

Khi gom phần **4.5. Tên Attribute phải duy nhất trong toàn mô hình** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **4.5. Tên Attribute phải duy nhất trong toàn mô hình**. Bây giờ chuyển sang **Keyword: 유일성**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 유일성** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 유일성

**유일성은 서로 다른 속성이 같은 이름을 사용하지 않도록 하는 성질이다.**

Tính duy nhất là đặc tính trong đó các Attribute khác nhau không sử dụng cùng một tên gây nhầm lẫn.

Ví dụ trong hình:

Không nên dùng Attribute `이름` cho tất cả Entity:

```
교수 Entity → 이름
학생 Entity → 이름
```

Nên dùng:

```
교수 Entity → 교수명
학생 Entity → 학생명
```

Vì:

```
교수명 = Tên giáo sư
학생명 = Tên sinh viên
```

sẽ rõ nghĩa hơn `이름`.

Khi gom phần **Keyword: 유일성** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 유일성**. Bây giờ chuyển sang **Lưu ý**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Lưu ý** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Lưu ý

Trong mỗi bảng, tên cột đương nhiên không được trùng nhau. Nhưng tài liệu đang nhấn mạnh phạm vi rộng hơn: toàn bộ mô hình dữ liệu cần có cách đặt tên nhất quán và không gây mơ hồ.

---

Khi gom phần **Lưu ý** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Lưu ý**. Bây giờ chuyển sang **5. 속성의 표기법 - Ký pháp Attribute**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **5. 속성의 표기법 - Ký pháp Attribute** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Ký pháp làm rõ Attribute đang bắt buộc, khóa hay đa trị, nhưng implementation vẫn cần domain cụ thể. Domain xác định tập giá trị hợp lệ, kiểu dữ liệu và các giới hạn phải kiểm tra.

## 5. 속성의 표기법 - Ký pháp Attribute

Hình cho thấy hai cách biểu diễn:

1. IE 표기법.
2. Barker 표기법.

---

Khi gom phần **5. 속성의 표기법 - Ký pháp Attribute** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **5. 속성의 표기법 - Ký pháp Attribute**. Bây giờ chuyển sang **5.1. IE notation**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **5.1. IE notation** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 5.1. IE notation

**IE 표기법에서는 엔터티를 사각형으로 표현하고 내부에 속성명을 표시한다.**

Trong ký pháp IE, Entity được biểu diễn bằng hình chữ nhật và tên Attribute được ghi bên trong.

Ví dụ:

```
┌──────────────┐
│ 과목         │
├──────────────┤
│ 과목이름     │
│ 교재이름     │
│ 생성일자     │
└──────────────┘
```

Ở đây:

- `과목` là Entity.
- `과목이름`, `교재이름`, `생성일자` là Attribute.

---

Khi gom phần **5.1. IE notation** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **5.1. IE notation**. Bây giờ chuyển sang **5.2. Barker notation**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **5.2. Barker notation** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 5.2. Barker notation

**Barker 표기법에서는 속성의 종류를 기호로 구분하여 표현할 수 있다.**

Trong ký pháp Barker, loại Attribute có thể được phân biệt bằng ký hiệu.

Hình thể hiện:

```
과목
□ # 과목이름
□ ○ 교재이름
□ ○ 생성일자
```

Trong đó có thể hiểu:

- `#`: Identifier hoặc Primary Key.
- `○`: Attribute tùy chọn hoặc có thể NULL.
- Ký hiệu khác tùy theo quy ước của Barker notation.

Khi gom phần **5.2. Barker notation** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **5.2. Barker notation**. Bây giờ chuyển sang **Keyword: 표기법**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 표기법** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 표기법

**표기법은 데이터 모델의 구성 요소를 일정한 기호와 규칙으로 표현하는 방법이다.**

Ký pháp là phương pháp biểu diễn các thành phần của mô hình dữ liệu bằng các ký hiệu và quy tắc nhất định.

Điểm cần nhớ:

> Chen, IE/Crow’s Foot và Barker là các hệ thống ký hiệu khác nhau, nhưng đều biểu diễn cùng bản chất: Entity, Attribute và Relationship.
>

---

Khi gom phần **Keyword: 표기법** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 표기법**. Bây giờ chuyển sang **6. 속성의 도메인 - Domain của Attribute**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **6. 속성의 도메인 - Domain của Attribute** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Domain nối khái niệm nghiệp vụ với constraint triển khai như kiểu, range, format và nullability. Sau khi chốt domain, ta phân loại Attribute theo đặc tính để biết cách lưu và kiểm tra chúng.

## 6. 속성의 도메인 - Domain của Attribute

Khi gom phần **6. 속성의 도메인 - Domain của Attribute** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **6. 속성의 도메인 - Domain của Attribute**. Bây giờ chuyển sang **6.1. Định nghĩa**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **6.1. Định nghĩa** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 6.1. Định nghĩa

**도메인은 각 속성이 가질 수 있는 값의 범위이다.**

Domain là phạm vi các giá trị mà một Attribute có thể nhận.

**도메인은 속성의 데이터 타입, 길이, 제약조건 등을 지정한다.**

Domain xác định kiểu dữ liệu, độ dài và các ràng buộc của Attribute.

Khi gom phần **6.1. Định nghĩa** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **6.1. Định nghĩa**. Bây giờ chuyển sang **Keyword: 도메인(Domain)**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 도메인(Domain)** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 도메인(Domain)

**도메인은 특정 속성에 입력할 수 있는 값의 규칙과 범위를 정의한 것이다.**

Domain là tập hợp các quy tắc và phạm vi định nghĩa những giá trị có thể nhập vào một Attribute cụ thể.

---

Khi gom phần **Keyword: 도메인(Domain)** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 도메인(Domain)**. Bây giờ chuyển sang **6.2. Ví dụ về Domain trong hình**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **6.2. Ví dụ về Domain trong hình** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 6.2. Ví dụ về Domain trong hình

Khi gom phần **6.2. Ví dụ về Domain trong hình** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **6.2. Ví dụ về Domain trong hình**. Bây giờ chuyển sang **Địa chỉ**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Địa chỉ** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Địa chỉ

**주소 속성의 도메인은 길이가 20자리 이내인 문자열로 정의할 수 있다.**

Domain của Attribute địa chỉ có thể được định nghĩa là chuỗi ký tự có độ dài không quá 20 ký tự.

Ví dụ Oracle:

```
ADDRESS VARCHAR2(20)
```

Khi gom phần **Địa chỉ** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Địa chỉ**. Bây giờ chuyển sang **Điểm số**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Điểm số** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Điểm số

**학점 속성의 도메인은 0.0 이상 4.5 이하의 실수로 정의할 수 있다.**

Domain của Attribute điểm số có thể được định nghĩa là số thực từ 0.0 đến 4.5.

Ví dụ:

```
GPA NUMBER(2,1)
CHECK (GPA BETWEEN 0.0 AND 4.5)
```

Khi gom phần **Điểm số** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Điểm số**. Bây giờ chuyển sang **Keyword: 제약조건**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 제약조건** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 제약조건

**제약조건은 속성에 입력되는 값이 반드시 만족해야 하는 규칙이다.**

Constraint là quy tắc mà giá trị nhập vào Attribute bắt buộc phải thỏa mãn.

Ví dụ:

```
GPA NUMBER(2,1)
CHECK (GPA BETWEEN 0.0 AND 4.5)
```

Các giá trị hợp lệ:

```
0.0
3.8
4.5
```

Các giá trị không hợp lệ:

```
-1.0
5.0
10
```

---

Khi gom phần **Keyword: 제약조건** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 제약조건**. Bây giờ chuyển sang **7. Phân loại Attribute theo đặc tính**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **7. Phân loại Attribute theo đặc tính** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Phân loại theo đặc tính tách thuộc tính mô tả, định danh, dẫn xuất hoặc phụ thuộc thời gian. Một chiều khác là xem entity được cấu thành bởi Attribute đơn giản hay tổ hợp, để tránh flatten sai cấu trúc.

## 7. Phân loại Attribute theo đặc tính

Hình chia thành:

```
기본 속성
설계 속성
파생 속성
```

---

Khi gom phần **7. Phân loại Attribute theo đặc tính** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **7. Phân loại Attribute theo đặc tính**. Bây giờ chuyển sang **7.1. 기본 속성 - Basic Attribute**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **7.1. 기본 속성 - Basic Attribute** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 7.1. 기본 속성 - Basic Attribute

**기본 속성은 업무로부터 추출한 모든 속성이며 가장 일반적인 속성이다.**

Basic Attribute là tất cả các Attribute được trích xuất từ nghiệp vụ và là loại Attribute phổ biến nhất.

Ví dụ trong hình:

```
회원ID
이름
계좌번호
주문일자
원금
```

Khi gom phần **7.1. 기본 속성 - Basic Attribute** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **7.1. 기본 속성 - Basic Attribute**. Bây giờ chuyển sang **Keyword: 기본 속성**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 기본 속성** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 기본 속성

**기본 속성은 업무에서 원래부터 관리해야 하는 사실을 저장하는 속성이다.**

Basic Attribute lưu những sự thật vốn cần được quản lý trong nghiệp vụ.

Ví dụ:

```
CUSTOMER_ID
CUSTOMER_NAME
ACCOUNT_NUMBER
ORDER_DATE
PRINCIPAL
```

Đây là những giá trị được thu thập hoặc phát sinh trực tiếp từ nghiệp vụ.

---

Khi gom phần **Keyword: 기본 속성** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 기본 속성**. Bây giờ chuyển sang **7.2. 설계 속성 - Designed Attribute**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **7.2. 설계 속성 - Designed Attribute** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 7.2. 설계 속성 - Designed Attribute

**설계 속성은 업무상 필요한 데이터 외에 데이터 모델링을 위해 새로 만들거나 변형하여 정의한 속성이다.**

Designed Attribute là Attribute được tạo mới hoặc biến đổi để phục vụ mô hình hóa dữ liệu, ngoài dữ liệu vốn cần thiết trong nghiệp vụ.

Khi gom phần **7.2. 설계 속성 - Designed Attribute** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **7.2. 설계 속성 - Designed Attribute**. Bây giờ chuyển sang **Keyword: 설계 속성**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 설계 속성** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 설계 속성

**설계 속성은 현실에 원래 존재하는 값을 그대로 저장한 것이 아니라 관리와 식별을 편리하게 하기 위해 설계자가 추가한 속성이다.**

Designed Attribute không nhất thiết là giá trị vốn tồn tại nguyên trạng trong thực tế, mà được nhà thiết kế thêm vào để quản lý và định danh thuận tiện hơn.

Ví dụ:

```
일련번호
주문번호
상품코드
지점코드
```

Một sản phẩm ngoài đời có thể không tự nhiên có `상품코드`, nhưng hệ thống tạo mã này để:

- Phân biệt sản phẩm.
- Tìm kiếm nhanh.
- Làm Primary Key.
- Liên kết với bảng khác.

Khi gom phần **Keyword: 설계 속성** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 설계 속성**. Bây giờ chuyển sang **Ví dụ**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Ví dụ** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Ví dụ

Phần này nối mạch SQL với “Ví dụ”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```
PRODUCT
-------
PRODUCT_CODE
PRODUCT_NAME
PRICE
```

`PRODUCT_CODE` thường là Designed Attribute.

---

Khi gom phần **Ví dụ** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Ví dụ**. Bây giờ chuyển sang **7.3. 설계 속성으로 만든 인조 식별자**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **7.3. 설계 속성으로 만든 인조 식별자** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 7.3. 설계 속성으로 만든 인조 식별자

**일련번호와 같은 설계 속성은 유일한 식별자를 만들기 위해 사용될 수 있다.**

Designed Attribute như số thứ tự có thể được sử dụng để tạo Identifier duy nhất.

Ví dụ:

```
ORDER_NUMBER
PRODUCT_CODE
BRANCH_CODE
```

Các mã này có thể không phải dữ liệu tự nhiên từ thế giới thực, mà là dữ liệu được thiết kế để hệ thống quản lý dễ hơn.

---

Khi gom phần **7.3. 설계 속성으로 만든 인조 식별자** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **7.3. 설계 속성으로 만든 인조 식별자**. Bây giờ chuyển sang **7.4. 파생 속성 - Derived Attribute**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **7.4. 파생 속성 - Derived Attribute** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 7.4. 파생 속성 - Derived Attribute

**파생 속성은 다른 속성들로부터 유도되거나 계산되어 생성되는 속성이다.**

Derived Attribute là Attribute được suy ra hoặc tính toán từ các Attribute khác.

**파생 속성은 다른 속성의 영향을 받아 발생하며 일반적으로 계산된 값을 저장한다.**

Derived Attribute phát sinh do ảnh hưởng của các Attribute khác và thường lưu giá trị đã được tính toán.

Ví dụ:

```
주문금액 = 단가 × 수량
총금액 = 각 상품 금액의 합계
평균점수 = 점수의 합계 ÷ 과목 수
```

Khi gom phần **7.4. 파생 속성 - Derived Attribute** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **7.4. 파생 속성 - Derived Attribute**. Bây giờ chuyển sang **Keyword: 파생 속성**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 파생 속성** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 파생 속성

**파생 속성은 원천 속성의 값이 변경되면 함께 변경될 수 있는 계산 결과 속성이다.**

Derived Attribute là Attribute kết quả tính toán có thể thay đổi khi giá trị của các Attribute nguồn thay đổi.

Ví dụ:

```
UNIT_PRICE = 100
QUANTITY   = 3

ORDER_AMOUNT = 300
```

`ORDER_AMOUNT` là Derived Attribute.

---

Khi gom phần **Keyword: 파생 속성** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 파생 속성**. Bây giờ chuyển sang **7.5. Có nên lưu Derived Attribute không?**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **7.5. Có nên lưu Derived Attribute không?** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 7.5. Có nên lưu Derived Attribute không?

**파생 속성은 조회 성능을 빠르게 하기 위해 원래 속성의 값을 계산하여 저장할 수 있다.**

Derived Attribute có thể được tính toán và lưu lại để tăng tốc độ truy vấn.

Ví dụ thay vì mỗi lần truy vấn đều tính:

```
SELECT UNIT_PRICE * QUANTITY
FROM ORDER_ITEM;
```

ta lưu sẵn:

```
ORDER_AMOUNT
```

Khi gom phần **7.5. Có nên lưu Derived Attribute không?** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **7.5. Có nên lưu Derived Attribute không?**. Bây giờ chuyển sang **Nhưng có rủi ro**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Nhưng có rủi ro** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Nhưng có rủi ro

**파생 속성은 원천 속성이 변경될 때 계산값도 함께 수정해야 하므로 관리 부담이 있다.**

Derived Attribute tạo ra gánh nặng quản lý vì khi Attribute nguồn thay đổi thì giá trị tính toán cũng phải được cập nhật.

Ví dụ:

```
UNIT_PRICE = 100
QUANTITY   = 3
ORDER_AMOUNT = 300
```

Nếu `QUANTITY` đổi thành `5` mà `ORDER_AMOUNT` không cập nhật thì:

```
ORDER_AMOUNT = 300  -- Sai
Thực tế phải là 500
```

Khi gom phần **Nhưng có rủi ro** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Nhưng có rủi ro**. Bây giờ chuyển sang **Câu ghi nhớ**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Câu ghi nhớ** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Câu ghi nhớ

**파생 속성은 조회에는 편리하지만 원천 데이터가 변경될 때 일관성을 관리해야 한다.**

Derived Attribute thuận tiện khi truy vấn nhưng phải quản lý tính nhất quán khi dữ liệu nguồn thay đổi.

---

Khi gom phần **Câu ghi nhớ** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Câu ghi nhớ**. Bây giờ chuyển sang **7.6. “가급적 적게 정의” nghĩa là gì?**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **7.6. “가급적 적게 정의” nghĩa là gì?** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 7.6. “가급적 적게 정의” nghĩa là gì?

**파생 속성은 데이터 일관성과 유지보수 문제 때문에 가급적 적게 정의하는 것이 좋다.**

Do có vấn đề về tính nhất quán và bảo trì, nên hạn chế định nghĩa Derived Attribute ở mức cần thiết.

Nhưng không có nghĩa là tuyệt đối không được dùng.

Có thể sử dụng khi:

- Truy vấn tính toán quá thường xuyên.
- Dữ liệu rất lớn.
- Cần tối ưu hiệu năng.
- Có cơ chế cập nhật tự động.
- Có thể bảo đảm giá trị không bị lệch.

---

Khi gom phần **7.6. “가급적 적게 정의” nghĩa là gì?** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **7.6. “가급적 적게 정의” nghĩa là gì?**. Bây giờ chuyển sang **8. Phân loại Attribute theo cách Entity được cấu thành**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **8. Phân loại Attribute theo cách Entity được cấu thành** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Attribute có thể cấu thành entity trực tiếp, lồng trong cấu trúc hoặc đại diện cho một nhóm giá trị; cách phân loại ảnh hưởng decomposition. Tiếp theo cần hỏi mỗi Attribute có một value hay nhiều value trong một instance.

## 8. Phân loại Attribute theo cách Entity được cấu thành

Hình chia Attribute thành:

```
PK 속성
FK 속성
일반 속성
```

---

Khi gom phần **8. Phân loại Attribute theo cách Entity được cấu thành** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **8. Phân loại Attribute theo cách Entity được cấu thành**. Bây giờ chuyển sang **8.1. PK Attribute**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **8.1. PK Attribute** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 8.1. PK Attribute

**기본키 속성은 엔터티의 인스턴스를 구별할 수 있는 속성이다.**

Primary Key Attribute là Attribute có thể phân biệt các Instance của Entity.

Khi gom phần **8.1. PK Attribute** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **8.1. PK Attribute**. Bây giờ chuyển sang **Keyword: 기본키(PK)**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 기본키(PK)** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 기본키(PK)

**기본키는 각 인스턴스를 유일하게 식별하고 NULL을 허용하지 않는 키이다.**

Primary Key là khóa xác định duy nhất mỗi Instance và không cho phép NULL.

Ví dụ:

```
사원
- 사원번호(PK)
- 사원명
- 우편번호
- 주소
- 전화번호
- 부서코드(FK)
```

`사원번호` là PK vì mỗi nhân viên có một mã riêng.

```
CREATE TABLE EMPLOYEE (
    EMPLOYEE_ID NUMBER PRIMARY KEY,
    EMPLOYEE_NAME VARCHAR2(100)
);
```

---

Khi gom phần **Keyword: 기본키(PK)** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 기본키(PK)**. Bây giờ chuyển sang **8.2. FK Attribute**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **8.2. FK Attribute** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 8.2. FK Attribute

**외래키 속성은 다른 엔터티와의 관계에서 포함된 속성이다.**

Foreign Key Attribute là Attribute được chứa trong quan hệ với Entity khác.

**외래키는 다른 테이블의 기본키를 참조하여 엔터티 간의 관계를 표현한다.**

Foreign Key tham chiếu Primary Key của bảng khác để biểu diễn quan hệ giữa các Entity.

Khi gom phần **8.2. FK Attribute** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **8.2. FK Attribute**. Bây giờ chuyển sang **Keyword: 외래키(FK)**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 외래키(FK)** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 외래키(FK)

**외래키는 자식 테이블에서 부모 테이블의 기본키를 참조하는 속성이다.**

Foreign Key là Attribute ở bảng con dùng để tham chiếu Primary Key của bảng cha.

Ví dụ:

```
DEPARTMENT
----------
DEPARTMENT_CODE PK

EMPLOYEE
--------
EMPLOYEE_ID PK
DEPARTMENT_CODE FK
```

`EMPLOYEE.DEPARTMENT_CODE` tham chiếu:

```
DEPARTMENT.DEPARTMENT_CODE
```

```
FOREIGN KEY (DEPARTMENT_CODE)
REFERENCES DEPARTMENT(DEPARTMENT_CODE)
```

---

Khi gom phần **Keyword: 외래키(FK)** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 외래키(FK)**. Bây giờ chuyển sang **8.3. 일반 속성 - General Attribute**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **8.3. 일반 속성 - General Attribute** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 8.3. 일반 속성 - General Attribute

**일반 속성은 기본키와 외래키에 포함되지 않는 일반적인 속성이다.**

General Attribute là Attribute thông thường không thuộc Primary Key hoặc Foreign Key.

Ví dụ:

```
EMPLOYEE
--------
EMPLOYEE_ID      PK
DEPARTMENT_CODE  FK
EMPLOYEE_NAME    일반 속성
PHONE            일반 속성
ADDRESS          일반 속성
```

---

Khi gom phần **8.3. 일반 속성 - General Attribute** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **8.3. 일반 속성 - General Attribute**. Bây giờ chuyển sang **9. Phân loại theo số lượng Attribute Value**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **9. Phân loại theo số lượng Attribute Value** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Số lượng Attribute Value quyết định cột đơn, bảng con hoặc quan hệ riêng khi chuyển sang relational schema. Sau cardinality theo value, khả năng phân tách cho biết một thuộc tính có nên tiếp tục tách thành thành phần nhỏ hơn.

## 9. Phân loại theo số lượng Attribute Value

Khi gom phần **9. Phân loại theo số lượng Attribute Value** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **9. Phân loại theo số lượng Attribute Value**. Bây giờ chuyển sang **9.1. Single Value Attribute**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **9.1. Single Value Attribute** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 9.1. Single Value Attribute

**단일값 속성은 하나의 속성이 하나의 값만 가지는 속성이다.**

Single Value Attribute là Attribute chỉ có một giá trị.

Ví dụ:

```
나이 = 25
이름 = 홍길동
```

Khi gom phần **9.1. Single Value Attribute** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **9.1. Single Value Attribute**. Bây giờ chuyển sang **Keyword: 단일값 속성**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 단일값 속성** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 단일값 속성

**단일값 속성은 하나의 인스턴스에 대해 하나의 값만 저장되는 속성이다.**

Single Value Attribute là Attribute mà mỗi Instance chỉ lưu một giá trị.

Ví dụ:

```
STUDENT_ID = 100
STUDENT_NAME = 홍길동
```

---

Khi gom phần **Keyword: 단일값 속성** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 단일값 속성**. Bây giờ chuyển sang **9.2. Multi Value Attribute**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **9.2. Multi Value Attribute** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 9.2. Multi Value Attribute

**다중값 속성은 하나의 속성이 여러 개의 값을 가지는 속성이다.**

Multi Value Attribute là Attribute có nhiều giá trị.

Ví dụ trong hình:

```
취미 = 독서, 여행, 영화감상
```

Khi gom phần **9.2. Multi Value Attribute** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **9.2. Multi Value Attribute**. Bây giờ chuyển sang **Keyword: 다중값 속성**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 다중값 속성** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 다중값 속성

**다중값 속성은 한 인스턴스에 대해 같은 종류의 값이 여러 개 존재하는 속성이다.**

Multi Value Attribute là Attribute trong đó một Instance có nhiều giá trị cùng loại.

Ví dụ:

```
학생 100의 취미:
- 독서
- 여행
- 영화감상
```

---

Khi gom phần **Keyword: 다중값 속성** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 다중값 속성**. Bây giờ chuyển sang **9.3. Vì sao Multi Value Attribute là vấn đề?**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **9.3. Vì sao Multi Value Attribute là vấn đề?** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 9.3. Vì sao Multi Value Attribute là vấn đề?

**다중값 속성은 하나의 속성이 하나의 속성값을 가져야 한다는 원칙을 위반한다.**

Multi Value Attribute vi phạm nguyên tắc một Attribute phải có một Attribute Value.

Ví dụ không nên:

```
STUDENT_ID | HOBBY
-----------|-----------------
100        | 독서, 여행, 영화
```

Vì gây khó khăn khi:

```
WHERE HOBBY = '여행'
```

Không thể truy vấn chính xác nếu nhiều giá trị được nhét vào một chuỗi.

Khi gom phần **9.3. Vì sao Multi Value Attribute là vấn đề?** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **9.3. Vì sao Multi Value Attribute là vấn đề?**. Bây giờ chuyển sang **Cách xử lý 1: Chuẩn hóa thành Entity riêng**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Cách xử lý 1: Chuẩn hóa thành Entity riêng** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Cách xử lý 1: Chuẩn hóa thành Entity riêng

**다중값 속성은 제1정규화를 적용하거나 별도의 엔터티로 분리해야 한다.**

Multi Value Attribute phải được xử lý bằng chuẩn hóa lần thứ nhất hoặc tách thành Entity riêng.

```
STUDENT
-------
STUDENT_ID
STUDENT_NAME

STUDENT_HOBBY
-------------
STUDENT_ID
HOBBY
```

Dữ liệu:

| STUDENT_ID | HOBBY |
| --- | --- |
| 100 | 독서 |
| 100 | 여행 |
| 100 | 영화감상 |

Khi gom phần **Cách xử lý 1: Chuẩn hóa thành Entity riêng** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Cách xử lý 1: Chuẩn hóa thành Entity riêng**. Bây giờ chuyển sang **Cách xử lý 2: Tạo Relationship**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Cách xử lý 2: Tạo Relationship** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Cách xử lý 2: Tạo Relationship

**분리한 엔터티는 원래 엔터티와 관계를 통해 연결해야 한다.**

Entity được tách ra phải được liên kết với Entity ban đầu thông qua Relationship.

```
STUDENT 1 ─── N STUDENT_HOBBY
```

---

Khi gom phần **Cách xử lý 2: Tạo Relationship** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Cách xử lý 2: Tạo Relationship**. Bây giờ chuyển sang **10. Phân loại theo khả năng phân tách**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **10. Phân loại theo khả năng phân tách** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Attribute decomposition làm rõ khi nào một field phức hợp nên tách thành nhiều thuộc tính hoặc entity phụ. Sau khi phân loại đủ các chiều, phần tổng hợp kiểm tra chúng có tạo thành mô hình nhất quán hay chưa.

## 10. Phân loại theo khả năng phân tách

Khi gom phần **10. Phân loại theo khả năng phân tách** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **10. Phân loại theo khả năng phân tách**. Bây giờ chuyển sang **10.1. Simple Attribute**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **10.1. Simple Attribute** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 10.1. Simple Attribute

**단순 속성은 다른 속성으로 더 이상 분해할 수 없는 속성이다.**

Simple Attribute là Attribute không thể tiếp tục phân tách thành các Attribute khác.

Ví dụ trong hình:

```
시
구
동
번지
이름
나이
```

Khi gom phần **10.1. Simple Attribute** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **10.1. Simple Attribute**. Bây giờ chuyển sang **Keyword: 단순 속성**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 단순 속성** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 단순 속성

**단순 속성은 업무적으로 더 이상 나눌 필요가 없는 하나의 기본적인 데이터 항목이다.**

Simple Attribute là một mục dữ liệu cơ bản không cần tách thêm về mặt nghiệp vụ.

Ví dụ:

```
나이 = 25
```

Thông thường không cần tách `25` thành các Attribute nhỏ hơn.

---

Khi gom phần **Keyword: 단순 속성** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 단순 속성**. Bây giờ chuyển sang **10.2. Composite Attribute**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **10.2. Composite Attribute** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 10.2. Composite Attribute

**복합 속성은 여러 개의 단순 속성으로 구성된 속성이다.**

Composite Attribute là Attribute được cấu thành từ nhiều Simple Attribute.

Ví dụ trong hình:

```
주소
├── 시
├── 구
├── 동
└── 번지
```

Khi gom phần **10.2. Composite Attribute** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **10.2. Composite Attribute**. Bây giờ chuyển sang **Keyword: 복합 속성**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 복합 속성** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 복합 속성

**복합 속성은 하나의 큰 의미를 가지지만 내부적으로 여러 세부 항목으로 나눌 수 있는 속성이다.**

Composite Attribute có một ý nghĩa lớn nhưng bên trong có thể chia thành nhiều mục chi tiết.

Ví dụ:

```
ADDRESS
├── CITY
├── DISTRICT
├── STREET
└── BUILDING_NUMBER
```

Khi gom phần **Keyword: 복합 속성** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 복합 속성**. Bây giờ chuyển sang **Có nên tách Composite Attribute không?**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Có nên tách Composite Attribute không?** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Có nên tách Composite Attribute không?

**복합 속성을 분리할지는 업무에서 각 하위 요소를 독립적으로 조회하거나 관리해야 하는지에 따라 결정한다.**

Việc có tách Composite Attribute hay không phụ thuộc vào việc nghiệp vụ có cần truy vấn hoặc quản lý từng thành phần con một cách độc lập hay không.

Nếu cần tìm tất cả sinh viên ở Seoul:

```
WHERE CITY = '서울'
```

thì nên tách `CITY`.

Nếu chỉ cần hiển thị toàn bộ địa chỉ, có thể lưu:

```
ADDRESS = 서울시 종로구 종로 1
```

---

Khi gom phần **Có nên tách Composite Attribute không?** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Có nên tách Composite Attribute không?**. Bây giờ chuyển sang **11. Tổng hợp toàn bộ nội dung trong hai hình**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **11. Tổng hợp toàn bộ nội dung trong hai hình** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Tổng hợp toàn bộ Attribute giúp đối chiếu domain, value cardinality và decomposition với các entity đã chọn. Khi chuyển sang Relationship, trọng tâm đổi từ “entity có gì” sang “entity liên hệ và phụ thuộc thế nào”.

## 11. Tổng hợp toàn bộ nội dung trong hai hình

**속성은 엔터티를 설명하는 최소 단위의 데이터이며 각 인스턴스에 대해 하나의 값을 가져야 한다.**

Attribute là đơn vị dữ liệu nhỏ nhất mô tả Entity và mỗi Instance phải có một giá trị tương ứng.

**속성은 주식별자에 함수적으로 종속되어야 하며 업무에 필요한 정보만 포함해야 한다.**

Attribute phải phụ thuộc hàm vào khóa định danh chính và chỉ bao gồm thông tin cần thiết cho nghiệp vụ.

**속성명은 업무에서 사용하는 명확한 명사형 이름으로 작성하고 전체 모델에서 유일하게 관리해야 한다.**

Tên Attribute phải được đặt bằng danh từ rõ ràng được sử dụng trong nghiệp vụ và được quản lý duy nhất trong toàn mô hình.

**도메인은 속성이 가질 수 있는 값의 범위와 데이터 타입, 길이, 제약조건을 정의한다.**

Domain định nghĩa phạm vi giá trị, kiểu dữ liệu, độ dài và ràng buộc mà Attribute có thể nhận.

**속성은 기본 속성, 설계 속성, 파생 속성으로 분류할 수 있다.**

Attribute có thể được phân loại thành Basic, Designed và Derived Attribute.

**속성은 PK 속성, FK 속성, 일반 속성으로도 분류할 수 있다.**

Attribute cũng có thể được phân loại thành PK, FK và General Attribute.

**속성값의 개수에 따라 단일값 속성과 다중값 속성으로 나눌 수 있다.**

Theo số lượng giá trị, Attribute được chia thành Single Value và Multi Value Attribute.

**분해 가능성에 따라 단순 속성과 복합 속성으로 나눌 수 있다.**

Theo khả năng phân tách, Attribute được chia thành Simple và Composite Attribute.

Khi gom phần **11. Tổng hợp toàn bộ nội dung trong hai hình** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **11. Tổng hợp toàn bộ nội dung trong hai hình**. Bây giờ chuyển sang **Sơ đồ ghi nhớ**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Sơ đồ ghi nhớ** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### Sơ đồ ghi nhớ

Phần này nối mạch SQL với “Sơ đồ ghi nhớ”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```
속성
├── 정의
│   ├── 사물의 성질
│   └── 업무상 관리하는 최소 데이터 단위
│
├── 특징
│   ├── 업무에 필요한 정보
│   ├── 주식별자에 함수적 종속
│   └── 하나의 속성은 하나의 값
│
├── 명명
│   ├── 업무 용어 사용
│   ├── 약어 지양
│   ├── 명사형 사용
│   └── 전체 모델에서 유일성 확보
│
├── 도메인
│   ├── 데이터 타입
│   ├── 길이
│   └── 제약조건
│
├── 특성 분류
│   ├── 기본 속성
│   ├── 설계 속성
│   └── 파생 속성
│
├── 구성 방식
│   ├── PK 속성
│   ├── FK 속성
│   └── 일반 속성
│
├── 값의 개수
│   ├── 단일값 속성
│   └── 다중값 속성
│
└── 분해 가능성
    ├── 단순 속성
    └── 복합 속성
```

Câu ghi nhớ quan trọng nhất:

> **속성은 업무에 필요한 최소 단위의 데이터이며, 주식별자에 함수적으로 종속되고 하나의 속성값만 가져야 한다.**
>

> Attribute là đơn vị dữ liệu nhỏ nhất cần thiết cho nghiệp vụ, phải phụ thuộc hàm vào khóa định danh chính và mỗi Attribute chỉ được có một Attribute Value.
>

---

Khi gom phần **Sơ đồ ghi nhớ** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Sơ đồ ghi nhớ**. Bây giờ chuyển sang **제 4절 관계 - Phần 4: Relationship**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **제 4절 관계 - Phần 4: Relationship** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Relationship là phần nối các entity trong phạm vi và thời điểm cụ thể, nên phải đọc cùng cardinality và optionality. Bước đầu của phần này là định nghĩa chính xác relationship thay vì chỉ nhìn đường nối trên hình.

## 제 4절 관계 - Phần 4: Relationship

Khi gom phần **제 4절 관계 - Phần 4: Relationship** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **제 4절 관계 - Phần 4: Relationship**. Bây giờ chuyển sang **1. 관계의 정의 - Định nghĩa Relationship**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **1. 관계의 정의 - Định nghĩa Relationship** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Định nghĩa Relationship xác định association có ý nghĩa gì và ở grain nào. Pairing tiếp theo làm rõ các entity tham gia, vai trò của từng phía và cách tránh quan hệ mơ hồ.

## 1. 관계의 정의 - Định nghĩa Relationship

Khi gom phần **1. 관계의 정의 - Định nghĩa Relationship** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **1. 관계의 정의 - Định nghĩa Relationship**. Bây giờ chuyển sang **1.1. Định nghĩa trong tài liệu**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **1.1. Định nghĩa trong tài liệu** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 1.1. Định nghĩa trong tài liệu

**관계는 엔터티의 인스턴스 사이에 논리적인 연관성이 존재하거나 행위로서 서로에게 연관성이 부여된 상태이다.**

Relationship là trạng thái trong đó giữa các Instance của Entity tồn tại sự liên quan về mặt logic hoặc sự liên quan được tạo ra thông qua một hành động.

Khi gom phần **1.1. Định nghĩa trong tài liệu** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **1.1. Định nghĩa trong tài liệu**. Bây giờ chuyển sang **Keyword: 관계(Relationship)**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 관계(Relationship)** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 관계(Relationship)

**관계는 두 개 이상의 엔터티가 업무적으로 어떻게 연결되는지를 나타내는 데이터 모델의 구성 요소이다.**

Relationship là thành phần của mô hình dữ liệu biểu diễn từ hai Entity trở lên liên kết với nhau về mặt nghiệp vụ như thế nào.

Ví dụ trong hình:

```
[강사] ── 가르친다 ── [수강생]
```

Nghĩa là:

```
Giảng viên dạy học viên.
```

Ở đây:

- `강사` là Entity.
- `수강생` là Entity.
- `강사1`, `강사2` là các Instance của `강사`.
- `학생1`, `학생2` là các Instance của `수강생`.
- `가르친다` là Relationship.

---

Khi gom phần **Keyword: 관계(Relationship)** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 관계(Relationship)**. Bây giờ chuyển sang **1.2. Relationship ở cấp Entity và Instance**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **1.2. Relationship ở cấp Entity và Instance** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 1.2. Relationship ở cấp Entity và Instance

**엔터티 간의 관계는 실제로는 각 엔터티에 속한 인스턴스 간의 관계로 구성된다.**

Relationship giữa các Entity thực chất được cấu thành từ Relationship giữa các Instance thuộc những Entity đó.

Ví dụ:

```
강사 Entity
- 강사1
- 강사2

수강생 Entity
- 학생1
- 학생2
```

Các mối quan hệ thực tế:

```
강사1 ── 가르친다 ── 학생1
강사1 ── 가르친다 ── 학생2
강사2 ── 가르친다 ── 학생2
```

Như vậy, không phải toàn bộ giảng viên đều nhất thiết dạy toàn bộ học viên. Quan hệ phải được xác định ở cấp từng Instance.

Khi gom phần **1.2. Relationship ở cấp Entity và Instance** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **1.2. Relationship ở cấp Entity và Instance**. Bây giờ chuyển sang **Keyword: Instance Relationship**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: Instance Relationship** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: Instance Relationship

**인스턴스 관계는 실제 데이터 행과 행 사이에 존재하는 구체적인 관계이다.**

Instance Relationship là mối quan hệ cụ thể tồn tại giữa các dòng dữ liệu thực tế.

---

Khi gom phần **Keyword: Instance Relationship** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: Instance Relationship**. Bây giờ chuyển sang **2. 관계의 페어링 - Pairing của Relationship**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **2. 관계의 페어링 - Pairing của Relationship** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Pairing cho biết relationship là unary, binary hay n-ary và mỗi phía đóng vai trò gì. Sau khi xác định cặp hoặc nhóm tham gia, cần phân loại relationship theo semantics nghiệp vụ.

## 2. 관계의 페어링 - Pairing của Relationship

Khi gom phần **2. 관계의 페어링 - Pairing của Relationship** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **2. 관계의 페어링 - Pairing của Relationship**. Bây giờ chuyển sang **2.1. Định nghĩa Pairing**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **2.1. Định nghĩa Pairing** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 2.1. Định nghĩa Pairing

**페어링은 하나의 엔터티 안에서 인스턴스가 개별적으로 관계를 가지는 것이다.**

Pairing là việc mỗi Instance trong một Entity có Relationship riêng với Instance của Entity khác.

Ví dụ trong hình:

```
강사 Entity
- 강사1
- 강사2

수강생 Entity
- 학생1
- 학생2
```

Một khả năng Pairing:

```
강사1 - 학생1
강사1 - 학생2
강사2 - 학생2
```

Khi gom phần **2.1. Định nghĩa Pairing** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **2.1. Định nghĩa Pairing**. Bây giờ chuyển sang **Keyword: 페어링(Pairing)**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 페어링(Pairing)** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 페어링(Pairing)

**페어링은 어떤 인스턴스가 어떤 다른 인스턴스와 연결되는지를 나타내는 조합이다.**

Pairing là tổ hợp cho biết Instance nào được liên kết với Instance nào.

---

Khi gom phần **Keyword: 페어링(Pairing)** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 페어링(Pairing)**. Bây giờ chuyển sang **2.2. Quan hệ và tập hợp Pairing**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **2.2. Quan hệ và tập hợp Pairing** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 2.2. Quan hệ và tập hợp Pairing

**관계는 여러 개의 페어링을 논리적으로 표현한 것이다.**

Relationship là cách biểu diễn logic của nhiều Pairing.

Ví dụ:

```
강사1 - 학생1
강사1 - 학생2
강사2 - 학생2
```

Ba Pairing này hợp lại tạo thành Relationship:

```
강사는 수강생을 가르친다.
```

Khi gom phần **2.2. Quan hệ và tập hợp Pairing** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **2.2. Quan hệ và tập hợp Pairing**. Bây giờ chuyển sang **Keyword: 관계 집합**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 관계 집합** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 관계 집합

**관계 집합은 동일한 업무 의미를 가진 여러 인스턴스 관계의 집합이다.**

Relationship Set là tập hợp nhiều Instance Relationship có cùng ý nghĩa nghiệp vụ.

Có thể ghi nhớ:

```
Entity   = Tập hợp Instance
Relationship = Tập hợp Pairing
```

Tài liệu cũng so sánh:

**엔터티가 인스턴스의 집합이라면 관계는 페어링의 집합이다.**

Nếu Entity là tập hợp các Instance thì Relationship là tập hợp các Pairing.

---

Khi gom phần **Keyword: 관계 집합** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 관계 집합**. Bây giờ chuyển sang **3. Phân loại Relationship**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **3. Phân loại Relationship** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Phân loại Relationship giúp tách quan hệ sở hữu, tham chiếu, giao dịch hoặc phụ thuộc. Một ranh giới quan trọng là relationship do sự tồn tại của entity hay do một hành động tạo ra.

## 3. Phân loại Relationship

Tài liệu phân loại Relationship dựa trên mục đích liên kết:

```
존재에 의한 관계
행위에 의한 관계
```

Nghĩa là:

1. Relationship do sự tồn tại.
2. Relationship do hành động.

---

Khi gom phần **3. Phân loại Relationship** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **3. Phân loại Relationship**. Bây giờ chuyển sang **4. 존재에 의한 관계 - Relationship do sự tồn tại**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **4. 존재에 의한 관계 - Relationship do sự tồn tại** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Relationship do sự tồn tại mô tả dependency khi một entity sống phụ thuộc entity khác, còn relationship do hành động gắn với event hoặc nghiệp vụ xảy ra. Phân biệt này ảnh hưởng thời điểm tạo row và khóa ngoại.

## 4. 존재에 의한 관계 - Relationship do sự tồn tại

Khi gom phần **4. 존재에 의한 관계 - Relationship do sự tồn tại** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **4. 존재에 의한 관계 - Relationship do sự tồn tại**. Bây giờ chuyển sang **4.1. Nội dung trong tài liệu**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **4.1. Nội dung trong tài liệu** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 4.1. Nội dung trong tài liệu

**존재에 의한 관계는 하나의 엔터티가 다른 엔터티에 항상 속해 있는 관계이다.**

Relationship do sự tồn tại là quan hệ trong đó một Entity luôn thuộc về Entity khác.

**각 엔터티는 독립적으로 존재할 수 있다.**

Mỗi Entity có thể tồn tại độc lập.

Trong hình:

```
[부서] ── 소속한다 ── [사원]
```

Một nhân viên thuộc về một phòng ban.

Khi gom phần **4.1. Nội dung trong tài liệu** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **4.1. Nội dung trong tài liệu**. Bây giờ chuyển sang **Keyword: 존재에 의한 관계**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 존재에 의한 관계** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 존재에 의한 관계

**존재 관계는 어떤 행위가 발생하지 않아도 엔터티의 존재 사실만으로 성립하는 관계이다.**

Relationship tồn tại là quan hệ được hình thành chỉ bởi sự tồn tại của Entity, không cần có một hành động cụ thể xảy ra.

Ví dụ:

```
EMPLOYEE thuộc DEPARTMENT.
```

Quan hệ này tồn tại vì nhân viên được tổ chức phân vào phòng ban, không nhất thiết phải có một giao dịch cụ thể như đặt hàng hay thanh toán.

---

Khi gom phần **Keyword: 존재에 의한 관계** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 존재에 의한 관계**. Bây giờ chuyển sang **4.2. Đặc điểm của Relationship do sự tồn tại**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **4.2. Đặc điểm của Relationship do sự tồn tại** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 4.2. Đặc điểm của Relationship do sự tồn tại

**존재 관계에서는 관련된 엔터티들이 각각 독립적으로 존재할 수 있다.**

Trong Relationship tồn tại, các Entity liên quan có thể tồn tại độc lập.

Ví dụ:

```
DEPARTMENT
EMPLOYEE
```

- Một phòng ban có thể tồn tại dù hiện tại chưa có nhân viên.
- Một nhân viên có thể được tạo ra trước khi được phân vào phòng ban, tùy theo quy tắc nghiệp vụ.

Khi gom phần **4.2. Đặc điểm của Relationship do sự tồn tại** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **4.2. Đặc điểm của Relationship do sự tồn tại**. Bây giờ chuyển sang **Lưu ý**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Lưu ý** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Lưu ý

Nếu nghiệp vụ quy định nhân viên bắt buộc phải thuộc một phòng ban thì quan hệ vẫn là Relationship tồn tại, nhưng phía nhân viên có thể là quan hệ bắt buộc.

---

Khi gom phần **Lưu ý** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Lưu ý**. Bây giờ chuyển sang **4.3. Biểu diễn trong UML**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **4.3. Biểu diễn trong UML** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 4.3. Biểu diễn trong UML

**UML에서는 존재에 의한 관계를 연관관계라고 표현하고 실선으로 표시한다.**

Trong UML, Relationship do sự tồn tại được biểu diễn là Association và dùng đường liền.

Khi gom phần **4.3. Biểu diễn trong UML** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **4.3. Biểu diễn trong UML**. Bây giờ chuyển sang **Keyword: 연관관계(Association)**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 연관관계(Association)** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 연관관계(Association)

**연관관계는 두 클래스 또는 엔터티가 구조적으로 연결되어 있음을 표현하는 관계이다.**

Association là quan hệ biểu diễn việc hai Class hoặc Entity được liên kết với nhau về mặt cấu trúc.

Ví dụ:

```
Department ───── Employee
```

Đường liền cho biết hai đối tượng có mối liên hệ ổn định.

---

Khi gom phần **Keyword: 연관관계(Association)** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 연관관계(Association)**. Bây giờ chuyển sang **4.4. Biểu diễn trong Source Code**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **4.4. Biểu diễn trong Source Code** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 4.4. Biểu diễn trong Source Code

**연관관계는 소스코드에서 멤버변수로 선언하여 사용할 수 있다.**

Association có thể được sử dụng trong mã nguồn bằng cách khai báo dưới dạng Member Variable.

Ví dụ Java:

```
class Employee {
    Department department;
}
```

Ở đây:

- `Employee` có biến thành viên `department`.
- Điều này thể hiện nhân viên liên kết với phòng ban.

Hoặc:

```
class Department {
    List<Employee> employees;
}
```

Điều này thể hiện một phòng ban có danh sách nhân viên.

Khi gom phần **4.4. Biểu diễn trong Source Code** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **4.4. Biểu diễn trong Source Code**. Bây giờ chuyển sang **Keyword: 멤버변수(Member Variable)**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 멤버변수(Member Variable)** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 멤버변수(Member Variable)

**멤버변수는 클래스 내부에 선언되어 객체의 상태나 다른 객체와의 연결을 저장하는 변수이다.**

Member Variable là biến được khai báo bên trong Class để lưu trạng thái của đối tượng hoặc kết nối với đối tượng khác.

---

Khi gom phần **Keyword: 멤버변수(Member Variable)** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 멤버변수(Member Variable)**. Bây giờ chuyển sang **5. 행위에 의한 관계 - Relationship do hành động**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **5. 행위에 의한 관계 - Relationship do hành động** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Relationship do hành động thường tạo dữ liệu giao dịch hoặc history, nên cardinality và thời gian phải được kiểm tra riêng. Sau semantics, ký pháp Relationship cho biết cách biểu diễn các constraint đó trên ERD.

## 5. 행위에 의한 관계 - Relationship do hành động

Khi gom phần **5. 행위에 의한 관계 - Relationship do hành động** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **5. 행위에 의한 관계 - Relationship do hành động**. Bây giờ chuyển sang **5.1. Nội dung trong tài liệu**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **5.1. Nội dung trong tài liệu** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 5.1. Nội dung trong tài liệu

**행위에 의한 관계는 특정한 행위가 발생하여 엔터티 간의 관계가 만들어지는 것이다.**

Relationship do hành động là quan hệ được tạo ra do một hành động cụ thể xảy ra giữa các Entity.

**혼자서는 존재할 수 없는 엔터티인 사건 엔터티와 관련되는 경우가 많다.**

Nó thường liên quan đến Event Entity, là Entity không thể tồn tại độc lập.

Ví dụ trong hình:

```
고객 김철수 ── 주문한다 ── 주문 CTA024
```

Đơn hàng `CTA024` được tạo ra thông qua hành động đặt hàng của khách hàng Kim Cheol-su.

Khi gom phần **5.1. Nội dung trong tài liệu** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **5.1. Nội dung trong tài liệu**. Bây giờ chuyển sang **Keyword: 행위에 의한 관계**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 행위에 의한 관계** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 행위에 의한 관계

**행위 관계는 업무 활동이나 거래가 발생한 결과로 만들어지는 관계이다.**

Relationship hành động là quan hệ được tạo ra như kết quả của một hoạt động nghiệp vụ hoặc giao dịch.

Ví dụ:

```
Khách hàng đặt hàng.
Sinh viên đăng ký môn học.
Nhân viên lập hợp đồng.
Khách hàng thanh toán.
```

---

Khi gom phần **Keyword: 행위에 의한 관계** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 행위에 의한 관계**. Bây giờ chuyển sang **5.2. Event Entity thường không tồn tại độc lập**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **5.2. Event Entity thường không tồn tại độc lập** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 5.2. Event Entity thường không tồn tại độc lập

**사건 엔터티는 다른 엔터티가 존재하고 특정 행위가 발생해야 생성될 수 있다.**

Event Entity chỉ có thể được tạo ra khi các Entity khác tồn tại và một hành động cụ thể xảy ra.

Ví dụ:

```
CUSTOMER + 주문 행위 → ORDER
STUDENT + COURSE + 수강 행위 → ENROLLMENT
```

Không thể có:

```
ORDER
```

nếu không có khách hàng và hành động đặt hàng.

Không thể có:

```
ENROLLMENT
```

nếu không có sinh viên, môn học và hành động đăng ký.

Khi gom phần **5.2. Event Entity thường không tồn tại độc lập** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **5.2. Event Entity thường không tồn tại độc lập**. Bây giờ chuyển sang **Keyword: 사건 엔터티(Event Entity)**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 사건 엔터티(Event Entity)** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 사건 엔터티(Event Entity)

**사건 엔터티는 업무가 수행될 때마다 발생하는 거래나 사건을 저장하는 엔터티이다.**

Event Entity lưu giao dịch hoặc sự kiện phát sinh mỗi khi nghiệp vụ được thực hiện.

Ví dụ:

```
ORDER
PAYMENT
ENROLLMENT
CONTRACT
DELIVERY
```

---

Khi gom phần **Keyword: 사건 엔터티(Event Entity)** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 사건 엔터티(Event Entity)**. Bây giờ chuyển sang **5.3. Biểu diễn trong UML**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **5.3. Biểu diễn trong UML** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 5.3. Biểu diễn trong UML

**UML에서는 행위에 의한 관계를 의존관계로 표현하고 점선으로 표시한다.**

Trong UML, Relationship do hành động được biểu diễn là Dependency và dùng đường nét đứt.

Khi gom phần **5.3. Biểu diễn trong UML** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **5.3. Biểu diễn trong UML**. Bây giờ chuyển sang **Keyword: 의존관계(Dependency)**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 의존관계(Dependency)** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 의존관계(Dependency)

**의존관계는 한 객체의 변화나 행위가 다른 객체에 영향을 주는 관계이다.**

Dependency là quan hệ trong đó sự thay đổi hoặc hành động của một đối tượng ảnh hưởng đến đối tượng khác.

Ví dụ:

```
Customer ─ ─ ─ ─ > Order
```

Ý nghĩa:

- `Order` phụ thuộc vào hành động của `Customer`.
- Khi khách hàng thực hiện hành động đặt hàng thì Order được tạo ra.

---

Khi gom phần **Keyword: 의존관계(Dependency)** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 의존관계(Dependency)**. Bây giờ chuyển sang **5.4. Biểu diễn trong Operation**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **5.4. Biểu diễn trong Operation** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 5.4. Biểu diễn trong Operation

**의존관계는 오퍼레이션에서 파라미터 등으로 이용할 수 있다.**

Dependency có thể được sử dụng dưới dạng Parameter trong Operation.

Ví dụ:

```
class Customer {
    void order(Product product) {
        // tạo Order
    }
}
```

Ở đây:

- Phương thức `order()` là một Operation.
- `Product product` là Parameter.
- Hành động của Customer có thể tạo ra hoặc tác động đến Order.

Khi gom phần **5.4. Biểu diễn trong Operation** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **5.4. Biểu diễn trong Operation**. Bây giờ chuyển sang **Keyword: 오퍼레이션(Operation)**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 오퍼레이션(Operation)** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 오퍼레이션(Operation)

**오퍼레이션은 객체가 수행할 수 있는 동작이나 기능이다.**

Operation là hành động hoặc chức năng mà một đối tượng có thể thực hiện.

---

Khi gom phần **Keyword: 오퍼레이션(Operation)** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 오퍼레이션(Operation)**. Bây giờ chuyển sang **5.5. Ví dụ trong tài liệu**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **5.5. Ví dụ trong tài liệu** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 5.5. Ví dụ trong tài liệu

**주문 CTA024는 김철수의 주문이라는 행위를 통해 생성된다.**

Đơn hàng `CTA024` được tạo ra thông qua hành động đặt hàng của Kim Cheol-su.

Chuỗi nghiệp vụ:

```
김철수 고객 존재
        ↓
주문 행위 발생
        ↓
주문 CTA024 생성
```

Khi gom phần **5.5. Ví dụ trong tài liệu** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **5.5. Ví dụ trong tài liệu**. Bây giờ chuyển sang **Lưu ý quan trọng trong ERD**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Lưu ý quan trọng trong ERD** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Lưu ý quan trọng trong ERD

**ERD에서는 UML과 달리 존재 관계와 행위 관계를 별도의 기호로 구분하지 않고 표현한다.**

Trong ERD, khác với UML, Relationship tồn tại và Relationship hành động thường không được phân biệt bằng các ký hiệu riêng.

Nghĩa là trong ERD:

- Không nhất thiết dùng đường liền cho Relationship tồn tại.
- Không nhất thiết dùng đường nét đứt cho Relationship hành động.
- ERD tập trung vào quan hệ dữ liệu và lực lượng quan hệ.

---

---

Khi gom phần **Lưu ý quan trọng trong ERD** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Lưu ý quan trọng trong ERD**. Bây giờ chuyển sang **6. 관계의 표기법 - Cách biểu diễn Relationship**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **6. 관계의 표기법 - Cách biểu diễn Relationship** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Cách biểu diễn Relationship phải làm rõ cardinality, optionality, identifying và hướng phụ thuộc. Relationship Check dùng các câu hỏi kiểm chứng để phát hiện đường nối thiếu, thừa hoặc không phù hợp với rule.

## 6. 관계의 표기법 - Cách biểu diễn Relationship

Khi gom phần **6. 관계의 표기법 - Cách biểu diễn Relationship** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **6. 관계의 표기법 - Cách biểu diễn Relationship**. Bây giờ chuyển sang **6.1. 관계명 - Tên Relationship**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **6.1. 관계명 - Tên Relationship** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 6.1. 관계명 - Tên Relationship

**관계명은 엔터티 간의 관계를 설명하는 이름이다.**

Relationship Name là tên mô tả quan hệ giữa các Entity.

**관계명은 애매한 동사를 피하고 현재형으로 표현해야 한다.**

Tên Relationship phải tránh động từ mơ hồ và được viết ở thì hiện tại.

Khi gom phần **6.1. 관계명 - Tên Relationship** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **6.1. 관계명 - Tên Relationship**. Bây giờ chuyển sang **Ví dụ**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Ví dụ** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Ví dụ

Tốt:

```
주문한다
소속된다
포함한다
수강한다
```

Không nên dùng từ quá mơ hồ:

```
관리한다
관련된다
처리한다
관계된다
```

Khi gom phần **Ví dụ** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Ví dụ**. Bây giờ chuyển sang **Keyword: 관계명**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 관계명** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 관계명

**관계명은 두 엔터티 사이에서 어떤 업무가 진행되는지 명확히 보여주는 동사이다.**

Relationship Name là động từ cho thấy rõ nghiệp vụ nào diễn ra giữa hai Entity.

Ví dụ:

```
CUSTOMER ── 주문한다 ── ORDER
STUDENT ── 수강한다 ── COURSE
EMPLOYEE ── 소속된다 ── DEPARTMENT
```

---

Khi gom phần **Keyword: 관계명** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 관계명**. Bây giờ chuyển sang **6.2. Quan hệ phải đọc được từ cả hai phía**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **6.2. Quan hệ phải đọc được từ cả hai phía** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 6.2. Quan hệ phải đọc được từ cả hai phía

**관계명은 기준 엔터티와 대상 엔터티 양쪽에서 자연스럽게 읽혀야 한다.**

Relationship Name phải có thể đọc tự nhiên từ cả phía Entity nguồn và Entity đích.

Ví dụ:

```
CUSTOMER ── 주문한다 ── ORDER
```

Đọc từ phía Customer:

```
Khách hàng đặt hàng.
```

Đọc từ phía Order:

```
Đơn hàng được đặt bởi khách hàng.
```

---

Khi gom phần **6.2. Quan hệ phải đọc được từ cả hai phía** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **6.2. Quan hệ phải đọc được từ cả hai phía**. Bây giờ chuyển sang **6.3. 관계차수 - Cardinality**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **6.3. 관계차수 - Cardinality** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 6.3. 관계차수 - Cardinality

**관계차수는 각 관계에 참여할 수 있는 인스턴스의 수이다.**

Cardinality là số lượng Instance có thể tham gia vào mỗi Relationship.

Trong hình:

```
1:N
1:1
M:N
```

Khi gom phần **6.3. 관계차수 - Cardinality** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **6.3. 관계차수 - Cardinality**. Bây giờ chuyển sang **Keyword: 관계차수(Cardinality)**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 관계차수(Cardinality)** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 관계차수(Cardinality)

**관계차수는 한 인스턴스가 상대 엔터티의 몇 개 인스턴스와 연결될 수 있는지를 나타낸다.**

Cardinality cho biết một Instance có thể liên kết với bao nhiêu Instance của Entity đối diện.

Ví dụ:

Khi gom phần **Keyword: 관계차수(Cardinality)** lại, ta không cần nhớ các dòng như những mảnh rời: ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 관계차수(Cardinality)**. Bây giờ chuyển sang **1:1**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **1:1** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 1:1

Phần này nối mạch SQL với “1:1”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```
PERSON 1 ─── 1 PASSPORT
```

Một người có một hộ chiếu và một hộ chiếu thuộc về một người.

Khi gom phần **1:1** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **1:1**. Bây giờ chuyển sang **1:N**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **1:N** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 1:N

Phần này nối mạch SQL với “1:N”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```
DEPARTMENT 1 ─── N EMPLOYEE
```

Một phòng ban có nhiều nhân viên.

Khi gom phần **1:N** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **1:N**. Bây giờ chuyển sang **M:N**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **M:N** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### M:N

Phần này nối mạch SQL với “M:N”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```
STUDENT M ─── N COURSE
```

Một sinh viên học nhiều môn và một môn có nhiều sinh viên.

Trong database quan hệ, quan hệ M:N thường cần bảng trung gian:

```
ENROLLMENT
----------
STUDENT_ID
COURSE_ID
```

---

Khi gom phần **M:N** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **M:N**. Bây giờ chuyển sang **6.4. Quan hệ tùy chọn hoặc bắt buộc**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **6.4. Quan hệ tùy chọn hoặc bắt buộc** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 6.4. Quan hệ tùy chọn hoặc bắt buộc

**관계선택사양은 관계에 반드시 참여해야 하는지 선택적으로 참여할 수 있는지를 나타낸다.**

Tính tùy chọn của Relationship cho biết việc tham gia quan hệ là bắt buộc hay có thể tùy chọn.

Trong hình:

```
필수참여관계: |
선택참여관계: O
```

Khi gom phần **6.4. Quan hệ tùy chọn hoặc bắt buộc** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **6.4. Quan hệ tùy chọn hoặc bắt buộc**. Bây giờ chuyển sang **Keyword: 필수참여관계**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 필수참여관계** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 필수참여관계

**필수참여관계는 해당 엔터티의 인스턴스가 관계에 반드시 참여해야 하는 관계이다.**

Relationship bắt buộc là quan hệ trong đó Instance của Entity bắt buộc phải tham gia.

Ví dụ:

```
Mọi Employee bắt buộc phải thuộc một Department.
```

Khi đó:

```
EMPLOYEE.DEPARTMENT_ID NOT NULL
```

Khi gom phần **Keyword: 필수참여관계** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 필수참여관계**. Bây giờ chuyển sang **Keyword: 선택참여관계**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 선택참여관계** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 선택참여관계

**선택참여관계는 해당 엔터티의 인스턴스가 관계에 참여하지 않아도 되는 관계이다.**

Relationship tùy chọn là quan hệ trong đó Instance của Entity có thể không tham gia.

Ví dụ:

```
Một Department có thể chưa có Employee.
Một Customer có thể chưa tạo Order.
```

---

Khi gom phần **Keyword: 선택참여관계** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 선택참여관계**. Bây giờ chuyển sang **7. Relationship Check - Kiểm tra Relationship**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **7. Relationship Check - Kiểm tra Relationship** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Relationship Check nối bản vẽ với kiểm tra nghiệp vụ: mỗi quan hệ phải có lý do, grain và miền tham gia. Từ đây cần phân biệt quan hệ định danh và không định danh vì chúng dẫn tới cách đặt khóa khác nhau.

## 7. Relationship Check - Kiểm tra Relationship

Tài liệu đưa ra bốn tiêu chí tự rà soát.

Khi gom phần **7. Relationship Check - Kiểm tra Relationship** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **7. Relationship Check - Kiểm tra Relationship**. Bây giờ chuyển sang **7.1. Có quy tắc liên quan giữa hai Entity không?**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **7.1. Có quy tắc liên quan giữa hai Entity không?** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 7.1. Có quy tắc liên quan giữa hai Entity không?

**두 엔터티 사이에 업무적으로 관심 있는 연관 규칙이 존재하는지 확인해야 한다.**

Phải kiểm tra xem giữa hai Entity có tồn tại quy tắc liên quan được quan tâm về mặt nghiệp vụ hay không.

Ví dụ:

```
CUSTOMER và ORDER
```

Có quy tắc:

```
Khách hàng tạo đơn hàng.
```

Nếu hai Entity hoàn toàn không có liên hệ nghiệp vụ thì không nên tạo Relationship chỉ vì chúng cùng nằm trong một hệ thống.

---

Khi gom phần **7.1. Có quy tắc liên quan giữa hai Entity không?** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **7.1. Có quy tắc liên quan giữa hai Entity không?**. Bây giờ chuyển sang **7.2. Có phát sinh sự kết hợp thông tin giữa hai Entity không?**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **7.2. Có phát sinh sự kết hợp thông tin giữa hai Entity không?** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 7.2. Có phát sinh sự kết hợp thông tin giữa hai Entity không?

**두 엔터티의 인스턴스가 결합되어 새로운 업무 정보를 만들어내는지 확인해야 한다.**

Phải kiểm tra xem các Instance của hai Entity có kết hợp với nhau để tạo ra thông tin nghiệp vụ mới hay không.

Ví dụ:

```
STUDENT + COURSE → ENROLLMENT
```

Khi sinh viên đăng ký môn học, một thông tin mới phát sinh:

```
학생번호
과목코드
수강년도
성적
```

---

Khi gom phần **7.2. Có phát sinh sự kết hợp thông tin giữa hai Entity không?** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **7.2. Có phát sinh sự kết hợp thông tin giữa hai Entity không?**. Bây giờ chuyển sang **7.3. Quy tắc liên kết có được mô tả trong tài liệu nghiệp vụ không?**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **7.3. Quy tắc liên kết có được mô tả trong tài liệu nghiệp vụ không?** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 7.3. Quy tắc liên kết có được mô tả trong tài liệu nghiệp vụ không?

**업무기술서나 장표에 엔터티 간의 관계 연결 규칙이 서술되어 있는지 확인해야 한다.**

Phải kiểm tra xem quy tắc liên kết giữa các Entity có được mô tả trong tài liệu nghiệp vụ hay không.

Khi gom phần **7.3. Quy tắc liên kết có được mô tả trong tài liệu nghiệp vụ không?** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **7.3. Quy tắc liên kết có được mô tả trong tài liệu nghiệp vụ không?**. Bây giờ chuyển sang **Keyword: 업무기술서**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 업무기술서** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 업무기술서

**업무기술서는 업무의 처리 절차와 규칙을 문서로 정리한 자료이다.**

Tài liệu nghiệp vụ là tài liệu ghi lại quy trình xử lý và quy tắc nghiệp vụ.

Các tài liệu cần kiểm tra:

- Tài liệu yêu cầu.
- Tài liệu phân tích.
- Quy trình nghiệp vụ.
- Biểu mẫu.
- Tài liệu đặc tả.
- Tài liệu màn hình.
- Tài liệu giao diện.

---

Khi gom phần **Keyword: 업무기술서** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 업무기술서**. Bây giờ chuyển sang **7.4. Có động từ mô tả Relationship không?**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **7.4. Có động từ mô tả Relationship không?** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 7.4. Có động từ mô tả Relationship không?

**업무기술서나 장표에 관계 연결을 가능하게 하는 동사가 있는지 확인해야 한다.**

Phải kiểm tra xem trong tài liệu nghiệp vụ có động từ cho phép mô tả Relationship hay không.

Ví dụ:

```
Khách hàng đặt hàng.
Nhân viên thuộc phòng ban.
Sinh viên đăng ký môn học.
Phòng ban bao gồm nhân viên.
```

Các động từ:

```
주문한다
소속된다
수강한다
포함한다
```

giúp xác định Relationship.

---

Khi gom phần **7.4. Có động từ mô tả Relationship không?** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **7.4. Có động từ mô tả Relationship không?**. Bây giờ chuyển sang **8. Quan hệ định danh và không định danh**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **8. Quan hệ định danh và không định danh** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Quan hệ định danh đưa khóa của parent vào identity của child; quan hệ không định danh giữ identity độc lập và chỉ tham chiếu parent. Trước khi chọn kiểu cụ thể, cần xem non-identifying relationship vận hành ra sao trong schema.

## 8. Quan hệ định danh và không định danh

Đây là phần quan trọng vì liên quan trực tiếp đến Primary Key, Foreign Key và Strong Entity/Weak Entity.

---

Khi gom phần **8. Quan hệ định danh và không định danh** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **8. Quan hệ định danh và không định danh**. Bây giờ chuyển sang **8.1. 식별자 관계 - Identifying Relationship**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **8.1. 식별자 관계 - Identifying Relationship** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 8.1. 식별자 관계 - Identifying Relationship

**식별자 관계에서는 자식 엔터티의 주식별자에 부모 엔터티의 주식별자가 포함된다.**

Trong Identifying Relationship, Primary Key của Entity cha được bao gồm trong Primary Key của Entity con.

**부모 엔터티가 반드시 먼저 생성되어야 자식 엔터티가 생성될 수 있다.**

Entity cha bắt buộc phải được tạo trước thì Entity con mới có thể được tạo.

Khi gom phần **8.1. 식별자 관계 - Identifying Relationship** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **8.1. 식별자 관계 - Identifying Relationship**. Bây giờ chuyển sang **Ví dụ trong hình**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Ví dụ trong hình** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Ví dụ trong hình

Phần này nối mạch SQL với “Ví dụ trong hình”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```
학생
----
학번 PK

수강
----
과목코드
수강년도
학번 FK
평점
```

Nếu `수강` là Entity con và `학번` được đưa vào Primary Key của nó:

```
수강 PK = 학번 + 과목코드 + 수강년도
```

thì đây là Identifying Relationship.

Khi gom phần **Ví dụ trong hình** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Ví dụ trong hình**. Bây giờ chuyển sang **Keyword: 식별자 관계**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 식별자 관계** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 식별자 관계

**식별자 관계는 부모의 주식별자가 자식의 주식별자 역할까지 수행하는 강한 관계이다.**

Identifying Relationship là quan hệ mạnh, trong đó Primary Key của cha đồng thời đóng vai trò trong Primary Key của con.

---

Khi gom phần **Keyword: 식별자 관계** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 식별자 관계**. Bây giờ chuyển sang **8.2. Đặc điểm của Identifying Relationship**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **8.2. Đặc điểm của Identifying Relationship** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 8.2. Đặc điểm của Identifying Relationship

**식별자 관계에서는 부모 엔터티 없이는 자식 엔터티가 생성될 수 없다.**

Trong Identifying Relationship, Entity con không thể được tạo nếu không có Entity cha.

Ví dụ:

```
STUDENT + COURSE → ENROLLMENT
```

Nếu `ENROLLMENT` dùng `STUDENT_ID` trong Primary Key, thì không thể tạo đăng ký môn học nếu không có sinh viên.

Khi gom phần **8.2. Đặc điểm của Identifying Relationship** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **8.2. Đặc điểm của Identifying Relationship**. Bây giờ chuyển sang **Ví dụ khóa**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Ví dụ khóa** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Ví dụ khóa

Phần này nối mạch SQL với “Ví dụ khóa”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```
ENROLLMENT
----------
STUDENT_ID PK, FK
COURSE_ID  PK, FK
GRADE
```

Ở đây:

- `STUDENT_ID` là FK tham chiếu `STUDENT`.
- `STUDENT_ID` đồng thời là một phần PK của `ENROLLMENT`.
- `COURSE_ID` cũng là một phần PK.

---

Khi gom phần **Ví dụ khóa** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Ví dụ khóa**. Bây giờ chuyển sang **8.3. Strong Entity và Weak Entity**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **8.3. Strong Entity và Weak Entity** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 8.3. Strong Entity và Weak Entity

**식별자 관계에서 부모 엔터티는 Strong Entity이고 자식 엔터티는 Weak Entity로 볼 수 있다.**

Trong Identifying Relationship, Entity cha có thể được xem là Strong Entity và Entity con là Weak Entity.

**Weak Entity는 부모 엔터티 없이는 독립적으로 존재하기 어렵다.**

Weak Entity khó có thể tồn tại độc lập nếu không có Entity cha.

Khi gom phần **8.3. Strong Entity và Weak Entity** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **8.3. Strong Entity và Weak Entity**. Bây giờ chuyển sang **Keyword: Strong Entity**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: Strong Entity** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: Strong Entity

**Strong Entity는 독립적인 주식별자를 가지고 다른 엔터티에 의존하지 않고 존재할 수 있는 엔터티이다.**

Strong Entity là Entity có Primary Key độc lập và có thể tồn tại mà không phụ thuộc vào Entity khác.

Ví dụ:

```
STUDENT
CUSTOMER
DEPARTMENT
```

Khi gom phần **Keyword: Strong Entity** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: Strong Entity**. Bây giờ chuyển sang **Keyword: Weak Entity**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: Weak Entity** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: Weak Entity

**Weak Entity는 부모 엔터티의 식별자나 존재에 의존하여 생성되고 관리되는 엔터티이다.**

Weak Entity là Entity được tạo và quản lý phụ thuộc vào Identifier hoặc sự tồn tại của Entity cha.

Ví dụ:

```
ORDER_ITEM
ENROLLMENT
```

---

Khi gom phần **Keyword: Weak Entity** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: Weak Entity**. Bây giờ chuyển sang **8.4. Khi nào cần giảm quan hệ định danh?**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **8.4. Khi nào cần giảm quan hệ định danh?** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 8.4. Khi nào cần giảm quan hệ định danh?

Tài liệu ghi rằng có thể giảm thiểu Identifying Relationship trong một số trường hợp:

**SQL 문의 조인 관계를 최소화해야 하는 경우 식별자 관계를 줄일 수 있다.**

Khi cần giảm thiểu quan hệ Join trong câu SQL, có thể giảm số lượng Identifying Relationship.

**부모와 자식이 식별자를 공유하면 부모의 PK가 자식의 PK 구성에 포함되어 구조가 복잡해질 수 있다.**

Nếu cha và con chia sẻ Identifier thì PK của cha được đưa vào cấu trúc PK của con, khiến cấu trúc có thể trở nên phức tạp.

Mục tiêu là:

- Giảm độ phức tạp của SQL.
- Giảm số lượng cột trong khóa ghép.
- Giúp phát triển và bảo trì dễ hơn.
- Tránh chuỗi khóa quá dài.

---

Khi gom phần **8.4. Khi nào cần giảm quan hệ định danh?** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **8.4. Khi nào cần giảm quan hệ định danh?**. Bây giờ chuyển sang **9. 비식별자 관계 - Non-identifying Relationship**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **9. 비식별자 관계 - Non-identifying Relationship** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Quan hệ không định danh giữ khóa chính của child tách khỏi khóa parent, nhưng vẫn cần foreign key để bảo toàn referential integrity. Từ trường hợp này, phần Identifier mở rộng câu hỏi: identity của entity được xác lập bằng gì.

## 9. 비식별자 관계 - Non-identifying Relationship

Khi gom phần **9. 비식별자 관계 - Non-identifying Relationship** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **9. 비식별자 관계 - Non-identifying Relationship**. Bây giờ chuyển sang **9.1. Định nghĩa**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **9.1. Định nghĩa** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 9.1. Định nghĩa

**비식별자 관계에서는 부모의 주식별자가 자식 엔터티의 일반 속성으로 상속된다.**

Trong Non-identifying Relationship, Primary Key của cha được kế thừa thành General Attribute của Entity con.

**비식별자 관계에서는 부모 엔터티 없이도 자식 엔터티가 생성될 수 있다.**

Trong Non-identifying Relationship, Entity con có thể được tạo mà không cần Entity cha.

Khi gom phần **9.1. Định nghĩa** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **9.1. Định nghĩa**. Bây giờ chuyển sang **Ví dụ**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Ví dụ** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Ví dụ

Phần này nối mạch SQL với “Ví dụ”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```
DEPARTMENT
----------
DEPARTMENT_ID PK

EMPLOYEE
--------
EMPLOYEE_ID PK
DEPARTMENT_ID FK
```

Ở đây:

- `EMPLOYEE_ID` là PK độc lập của Employee.
- `DEPARTMENT_ID` chỉ là FK.
- `DEPARTMENT_ID` không tham gia vào PK của Employee.

Đây là Non-identifying Relationship.

---

Khi gom phần **Ví dụ** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Ví dụ**. Bây giờ chuyển sang **9.2. So sánh hai loại Relationship**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **9.2. So sánh hai loại Relationship** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 9.2. So sánh hai loại Relationship

Phần này nối mạch SQL với “9.2. So sánh hai loại Relationship”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

| Nội dung | 식별자 관계 | 비식별자 관계 |
| --- | --- | --- |
| Tên tiếng Việt | Identifying Relationship | Non-identifying Relationship |
| PK của cha | Là một phần PK của con | Chỉ là Attribute/FK của con |
| Quan hệ | Mạnh | Yếu hơn |
| Entity con | Phụ thuộc vào cha | Có thể tồn tại độc lập hơn |
| UML | Thường là quan hệ phụ thuộc mạnh | Thường là quan hệ liên kết yếu hơn |
| Ký pháp | Đường liền | Đường nét đứt |
| Ví dụ | `ORDER_ITEM` | `EMPLOYEE - DEPARTMENT` |

---

Khi gom phần **9.2. So sánh hai loại Relationship** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **9.2. So sánh hai loại Relationship**. Bây giờ chuyển sang **9.3. Khi nào dùng Non-identifying Relationship?**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **9.3. Khi nào dùng Non-identifying Relationship?** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 9.3. Khi nào dùng Non-identifying Relationship?

Tài liệu nêu các trường hợp:

Khi gom phần **9.3. Khi nào dùng Non-identifying Relationship?** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **9.3. Khi nào dùng Non-identifying Relationship?**. Bây giờ chuyển sang **1. Entity con cần khóa riêng**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **1. Entity con cần khóa riêng** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 1. Entity con cần khóa riêng

**자식 엔터티가 독립적인 주식별자를 설정해야 하는 경우 비식별자 관계를 사용할 수 있다.**

Có thể dùng Non-identifying Relationship khi Entity con cần thiết lập Primary Key độc lập.

Ví dụ:

```
EMPLOYEE_ID PK
DEPARTMENT_ID FK
```

Khi gom phần **1. Entity con cần khóa riêng** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **1. Entity con cần khóa riêng**. Bây giờ chuyển sang **2. Quan hệ cha-con tương đối yếu**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **2. Quan hệ cha-con tương đối yếu** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 2. Quan hệ cha-con tương đối yếu

**부모와 자식 엔터티 간의 관계가 약한 경우 비식별자 관계를 사용할 수 있다.**

Có thể dùng Non-identifying Relationship khi quan hệ giữa cha và con tương đối yếu.

Ví dụ nhân viên có thể được tạo trước, sau đó mới được phân vào phòng ban.

Khi gom phần **2. Quan hệ cha-con tương đối yếu** lại, ta không cần nhớ các dòng như những mảnh rời: ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **2. Quan hệ cha-con tương đối yếu**. Bây giờ chuyển sang **3. Cha bị xóa trước con**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **3. Cha bị xóa trước con** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 3. Cha bị xóa trước con

**부모 엔터티의 인스턴스가 자식 엔터티보다 먼저 삭제될 수 있는 경우 비식별자 관계를 고려할 수 있다.**

Có thể cân nhắc Non-identifying Relationship khi Instance của cha có thể bị xóa trước Instance của con.

Lưu ý: trong database thực tế, việc xóa cha trước con còn phụ thuộc vào Foreign Key, `ON DELETE CASCADE`, `ON DELETE SET NULL` và quy tắc nghiệp vụ.

Khi gom phần **3. Cha bị xóa trước con** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **3. Cha bị xóa trước con**. Bây giờ chuyển sang **4. Cần đơn giản hóa PK**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **4. Cần đơn giản hóa PK** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 4. Cần đơn giản hóa PK

**PK 속성의 단순화가 필요한 경우 비식별자 관계를 사용하여 복합키를 줄일 수 있다.**

Khi cần đơn giản hóa Primary Key, có thể dùng Non-identifying Relationship để giảm khóa ghép.

---

Khi gom phần **4. Cần đơn giản hóa PK** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **4. Cần đơn giản hóa PK**. Bây giờ chuyển sang **10. 식별자 - Khái niệm Identifier**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **10. 식별자 - Khái niệm Identifier** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Identifier là thuộc tính hoặc tập thuộc tính phân biệt một instance trong đúng phạm vi entity. Sau khái niệm, cần kiểm tra các đặc điểm như ổn định, tối thiểu, duy nhất và phù hợp lifecycle.

## 10. 식별자 - Khái niệm Identifier

Khi gom phần **10. 식별자 - Khái niệm Identifier** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **10. 식별자 - Khái niệm Identifier**. Bây giờ chuyển sang **10.1. Định nghĩa**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **10.1. Định nghĩa** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 10.1. Định nghĩa

**식별자는 하나의 엔터티에 구성되어 있는 여러 개의 속성 중 엔터티를 대표하고 각각의 인스턴스를 구분 가능하게 만들어 주는 대표 속성이다.**

Identifier là Attribute đại diện cho Entity trong số nhiều Attribute của Entity và giúp phân biệt từng Instance.

**하나의 엔터티에는 반드시 하나의 유일한 식별자가 존재해야 한다.**

Một Entity nhất định phải có một Identifier duy nhất.

Khi gom phần **10.1. Định nghĩa** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **10.1. Định nghĩa**. Bây giờ chuyển sang **Keyword: 식별자(Identifier)**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 식별자(Identifier)** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 식별자(Identifier)

**식별자는 엔터티 내부의 각 인스턴스를 유일하게 구분하는 속성 또는 속성의 조합이다.**

Identifier là một Attribute hoặc tổ hợp Attribute dùng để phân biệt duy nhất từng Instance bên trong Entity.

Ví dụ:

```
STUDENT
-------
STUDENT_ID
STUDENT_NAME
MAJOR
GPA
```

`STUDENT_ID` là Identifier vì mỗi sinh viên có một mã riêng.

---

Khi gom phần **Keyword: 식별자(Identifier)** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 식별자(Identifier)**. Bây giờ chuyển sang **10.2. Identifier và Key khác nhau thế nào?**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **10.2. Identifier và Key khác nhau thế nào?** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 10.2. Identifier và Key khác nhau thế nào?

Tài liệu phân biệt:

**식별자는 논리 데이터 모델링 단계에서 사용하는 용어이다.**

Identifier là thuật ngữ được sử dụng ở giai đoạn mô hình hóa dữ liệu logic.

**키는 데이터베이스 테이블에 접근하기 위한 매개체로서 물리 데이터 모델링 단계에서 사용하는 용어이다.**

Key là phương tiện truy cập bảng database, được sử dụng ở giai đoạn mô hình hóa dữ liệu vật lý.

Khi gom phần **10.2. Identifier và Key khác nhau thế nào?** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **10.2. Identifier và Key khác nhau thế nào?**. Bây giờ chuyển sang **Keyword: Identifier**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: Identifier** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: Identifier

**식별자는 업무와 논리 모델의 관점에서 엔터티를 구분하는 개념이다.**

Identifier là khái niệm phân biệt Entity dưới góc nhìn nghiệp vụ và mô hình logic.

Khi gom phần **Keyword: Identifier** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: Identifier**. Bây giờ chuyển sang **Keyword: Key**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: Key** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: Key

**키는 실제 데이터베이스 테이블에서 행을 식별하거나 테이블 간의 관계를 연결하는 구현 수단이다.**

Key là phương tiện triển khai trong database thực tế để xác định dòng hoặc liên kết các bảng.

Ví dụ:

```
Logical model:
학생의 식별자 = 학번

Physical database:
STUDENT_ID PRIMARY KEY
```

Trong thực tế hai khái niệm thường được dùng gần như tương đương, nhưng khi thi SQLD cần nhớ sự khác nhau về cấp độ mô hình.

---

Khi gom phần **Keyword: Key** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: Key**. Bây giờ chuyển sang **11. Đặc điểm của Identifier**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **11. Đặc điểm của Identifier** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Một Identifier tốt phải duy nhất, tối thiểu, ổn định và không phụ thuộc dữ liệu dễ đổi. Các tiêu chí đó dẫn tới nhiều cách phân loại Identifier theo nguồn gốc và vai trò trong mô hình.

## 11. Đặc điểm của Identifier

Khi gom phần **11. Đặc điểm của Identifier** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **11. Đặc điểm của Identifier**. Bây giờ chuyển sang **11.1. 유일성 - Tính duy nhất**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **11.1. 유일성 - Tính duy nhất** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 11.1. 유일성 - Tính duy nhất

**주식별자에 의해 엔터티 내의 모든 인스턴스를 유일하게 구분할 수 있어야 한다.**

Dựa vào Primary Identifier phải có thể phân biệt duy nhất tất cả Instance trong Entity.

Khi gom phần **11.1. 유일성 - Tính duy nhất** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **11.1. 유일성 - Tính duy nhất**. Bây giờ chuyển sang **Keyword: 유일성**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 유일성** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 유일성

**유일성은 동일한 식별자 값을 가진 두 개의 인스턴스가 존재할 수 없다는 의미이다.**

Tính duy nhất nghĩa là không thể tồn tại hai Instance có cùng giá trị Identifier.

Ví dụ:

```
STUDENT_ID
100
200
300
```

Không thể có:

```
STUDENT_ID
100
100
```

nếu `STUDENT_ID` là Primary Key.

---

Khi gom phần **Keyword: 유일성** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 유일성**. Bây giờ chuyển sang **11.2. 최소성 - Tính tối thiểu**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **11.2. 최소성 - Tính tối thiểu** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 11.2. 최소성 - Tính tối thiểu

**최소성은 하나의 속성으로 충분히 식별할 수 있다면 다른 속성을 추가하지 않는 것이다.**

Tính tối thiểu là không thêm Attribute khác nếu một Attribute đã đủ để xác định Instance.

Ví dụ:

```
STUDENT_ID
```

đã đủ xác định sinh viên thì không cần tạo:

```
STUDENT_ID + STUDENT_NAME + PHONE
```

làm khóa.

Khi gom phần **11.2. 최소성 - Tính tối thiểu** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **11.2. 최소성 - Tính tối thiểu**. Bây giờ chuyển sang **Keyword: 최소성**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 최소성** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 최소성

**최소성은 식별자에 필요한 최소한의 속성만 포함하는 성질이다.**

Tính tối thiểu là đặc tính trong đó Identifier chỉ bao gồm những Attribute tối thiểu cần thiết.

Ví dụ:

```
{STUDENT_ID}
```

tốt hơn:

```
{STUDENT_ID, STUDENT_NAME, MAJOR, PHONE}
```

nếu chỉ `STUDENT_ID` đã duy nhất.

---

Khi gom phần **Keyword: 최소성** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 최소성**. Bây giờ chuyển sang **11.3. 불변성 - Tính bất biến**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **11.3. 불변성 - Tính bất biến** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 11.3. 불변성 - Tính bất biến

**주식별자가 한 번 특정 엔터티에 지정되면 그 식별자의 값은 변경되면 안 된다.**

Khi một Primary Identifier đã được gán cho một Entity cụ thể thì giá trị Identifier đó không nên thay đổi.

Khi gom phần **11.3. 불변성 - Tính bất biến** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **11.3. 불변성 - Tính bất biến**. Bây giờ chuyển sang **Keyword: 불변성**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 불변성** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 불변성

**불변성은 식별자가 한 번 정해진 후 계속 동일하게 유지되어야 한다는 성질이다.**

Tính bất biến là đặc tính trong đó Identifier phải tiếp tục được giữ nguyên sau khi đã được xác định.

Ví dụ không tốt:

```
STUDENT_ID = 100
```

Sau đó đổi thành:

```
STUDENT_ID = 999
```

Việc này có thể làm hỏng:

- Foreign Key ở bảng khác.
- Lịch sử dữ liệu.
- Báo cáo.
- Log.
- Quan hệ tham chiếu.

---

Khi gom phần **Keyword: 불변성** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 불변성**. Bây giờ chuyển sang **11.4. 존재성 - Tính tồn tại**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **11.4. 존재성 - Tính tồn tại** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 11.4. 존재성 - Tính tồn tại

**주식별자가 지정되면 반드시 데이터 값이 존재해야 하며 NULL을 허용하지 않는다.**

Khi đã chỉ định Primary Identifier thì giá trị dữ liệu bắt buộc phải tồn tại và không được phép là NULL.

Khi gom phần **11.4. 존재성 - Tính tồn tại** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **11.4. 존재성 - Tính tồn tại**. Bây giờ chuyển sang **Keyword: 존재성**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Keyword: 존재성** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Keyword: 존재성

**존재성은 식별자가 모든 인스턴스에 반드시 부여되어 있어야 한다는 의미이다.**

Tính tồn tại nghĩa là mọi Instance bắt buộc phải được gán Identifier.

Ví dụ:

```
STUDENT_ID NUMBER PRIMARY KEY
```

Primary Key trong Oracle có các đặc tính:

- Không được NULL.
- Không được trùng.
- Dùng xác định dòng.

---

Khi gom phần **Keyword: 존재성** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Keyword: 존재성**. Bây giờ chuyển sang **12. Phân loại Identifier**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **12. Phân loại Identifier** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Phân loại Identifier giúp tách tự nhiên/nghiệp vụ với nhân tạo/kỹ thuật, đơn với ghép và ổn định với biến động. Tiếp theo cần phân biệt primary identifier với secondary identifier trong cùng entity.

## 12. Phân loại Identifier

Tài liệu phân loại theo nhiều tiêu chí.

Khi gom phần **12. Phân loại Identifier** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **12. Phân loại Identifier**. Bây giờ chuyển sang **12.1. Theo tính đại diện**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **12.1. Theo tính đại diện** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 12.1. Theo tính đại diện

Phần này nối mạch SQL với “12.1. Theo tính đại diện”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```
주식별자 - Primary Key
보조식별자 - Candidate Key
```

Khi gom phần **12.1. Theo tính đại diện** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **12.1. Theo tính đại diện**. Bây giờ chuyển sang **12.2. Theo cách tạo ra**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **12.2. Theo cách tạo ra** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 12.2. Theo cách tạo ra

Phần này nối mạch SQL với “12.2. Theo cách tạo ra”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```
내부식별자 - Internal Identifier
외부식별자 - Foreign Key
```

Khi gom phần **12.2. Theo cách tạo ra** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **12.2. Theo cách tạo ra**. Bây giờ chuyển sang **12.3. Theo số lượng Attribute**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **12.3. Theo số lượng Attribute** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 12.3. Theo số lượng Attribute

Phần này nối mạch SQL với “12.3. Theo số lượng Attribute”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```
단일식별자 - Single Identifier
복합식별자 - Composite Identifier
```

Khi gom phần **12.3. Theo số lượng Attribute** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **12.3. Theo số lượng Attribute**. Bây giờ chuyển sang **12.4. Theo nguồn gốc**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **12.4. Theo nguồn gốc** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 12.4. Theo nguồn gốc

Phần này nối mạch SQL với “12.4. Theo nguồn gốc”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```
본질식별자 - Natural Identifier
인조식별자 - Artificial Identifier
```

---

Khi gom phần **12.4. Theo nguồn gốc** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **12.4. Theo nguồn gốc**. Bây giờ chuyển sang **13. 주식별자 và 보조식별자**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **13. 주식별자 và 보조식별자** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Primary identifier là lựa chọn chính để định danh instance; secondary identifier vẫn hữu ích cho tra cứu hoặc kiểm tra duy nhất. Các loại key trong schema triển khai là cách cụ thể hóa những vai trò này.

## 13. 주식별자 và 보조식별자

Khi gom phần **13. 주식별자 và 보조식별자** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **13. 주식별자 và 보조식별자**. Bây giờ chuyển sang **13.1. 주식별자 - Primary Identifier**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **13.1. 주식별자 - Primary Identifier** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 13.1. 주식별자 - Primary Identifier

**주식별자는 엔터티의 인스턴스를 유일하게 식별하기 위해 선택된 대표 식별자이다.**

Primary Identifier là Identifier đại diện được chọn để xác định duy nhất các Instance của Entity.

Trong database:

```
주식별자 → Primary Key
```

---

Khi gom phần **13.1. 주식별자 - Primary Identifier** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **13.1. 주식별자 - Primary Identifier**. Bây giờ chuyển sang **13.2. 보조식별자 - Candidate Identifier**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **13.2. 보조식별자 - Candidate Identifier** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 13.2. 보조식별자 - Candidate Identifier

**보조식별자는 엔터티 내에서 각 인스턴스를 구분할 수 있지만 대표성을 갖지 못하여 참조관계 연결이 불가능한 식별자이다.**

Candidate Identifier có thể phân biệt từng Instance trong Entity nhưng không được chọn làm đại diện nên không dùng để thiết lập quan hệ tham chiếu theo cách chính.

Tài liệu gọi là:

```
후보 키(Candidate Key)
```

Khi gom phần **13.2. 보조식별자 - Candidate Identifier** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **13.2. 보조식별자 - Candidate Identifier**. Bây giờ chuyển sang **Lưu ý thuật ngữ**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Lưu ý thuật ngữ** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Lưu ý thuật ngữ

Trong lý thuyết database:

- Candidate Key là khóa có tính duy nhất và tối thiểu.
- Một Candidate Key được chọn làm Primary Key.
- Các Candidate Key còn lại thường được gọi là Alternate Key.

Tài liệu sử dụng cách gọi `보조식별자` trong ngữ cảnh phân loại Identifier.

---

Khi gom phần **Lưu ý thuật ngữ** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Lưu ý thuật ngữ**. Bây giờ chuyển sang **14. Các loại Key**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **14. Các loại Key** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Key có thể là candidate, primary, alternate, foreign hoặc composite; mỗi loại có constraint và hệ quả join khác nhau. Khi chọn primary identifier, cần cân bằng ổn định, độ ngắn, khả năng truyền qua quan hệ và chi phí triển khai.

## 14. Các loại Key

Khi gom phần **14. Các loại Key** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **14. Các loại Key**. Bây giờ chuyển sang **14.1. Candidate Key**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **14.1. Candidate Key** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 14.1. Candidate Key

**후보 키는 테이블에서 각 행을 유일하게 식별할 수 있는 속성들의 집합이다.**

Candidate Key là tập hợp các Attribute có thể xác định duy nhất mỗi dòng trong bảng.

**후보 키는 유일성과 최소성을 동시에 만족해야 한다.**

Candidate Key phải đồng thời thỏa mãn tính duy nhất và tính tối thiểu.

Ví dụ:

```
STUDENT
-------
STUDENT_ID
RESIDENT_NUMBER
EMAIL
STUDENT_NAME
```

Nếu `STUDENT_ID`, `RESIDENT_NUMBER` và `EMAIL` đều duy nhất, có thể có ba Candidate Key:

```
{STUDENT_ID}
{RESIDENT_NUMBER}
{EMAIL}
```

---

Khi gom phần **14.1. Candidate Key** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **14.1. Candidate Key**. Bây giờ chuyển sang **14.2. Primary Key**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **14.2. Primary Key** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 14.2. Primary Key

**기본키는 후보 키 중에서 엔터티를 대표하는 키로 선택된 키이다.**

Primary Key là Candidate Key được chọn làm khóa đại diện cho Entity.

Ví dụ:

```
Primary Key = STUDENT_ID
```

Các Candidate Key còn lại có thể trở thành Alternate Key.

---

Khi gom phần **14.2. Primary Key** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **14.2. Primary Key**. Bây giờ chuyển sang **14.3. Super Key**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **14.3. Super Key** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 14.3. Super Key

**슈퍼 키는 유일성은 만족하지만 최소성은 만족하지 못하는 키이다.**

Super Key thỏa mãn tính duy nhất nhưng không thỏa mãn tính tối thiểu.

Ví dụ:

```
{STUDENT_ID}
{STUDENT_ID, STUDENT_NAME}
{STUDENT_ID, STUDENT_NAME, MAJOR}
```

Nếu `STUDENT_ID` đã đủ xác định duy nhất, thì các tổ hợp có thêm Attribute vẫn là Super Key nhưng không phải Candidate Key vì không tối thiểu.

Khi gom phần **14.3. Super Key** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **14.3. Super Key**. Bây giờ chuyển sang **Quan hệ giữa các Key**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Quan hệ giữa các Key** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Quan hệ giữa các Key

Phần này nối mạch SQL với “Quan hệ giữa các Key”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```
Super Key
├── Candidate Key
│   ├── Primary Key
│   └── Alternate Key
```

---

Khi gom phần **Quan hệ giữa các Key** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Quan hệ giữa các Key**. Bây giờ chuyển sang **14.4. Alternate Key**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **14.4. Alternate Key** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 14.4. Alternate Key

**대체 키는 후보 키 중에서 기본키로 선택된 키를 제외하고 남은 키이다.**

Alternate Key là Candidate Key còn lại sau khi loại Candidate Key đã được chọn làm Primary Key.

Ví dụ:

```
Candidate Keys:
- STUDENT_ID
- EMAIL
- RESIDENT_NUMBER

Primary Key:
- STUDENT_ID

Alternate Keys:
- EMAIL
- RESIDENT_NUMBER
```

---

Khi gom phần **14.4. Alternate Key** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **14.4. Alternate Key**. Bây giờ chuyển sang **15. Tiêu chí lựa chọn Primary Identifier**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **15. Tiêu chí lựa chọn Primary Identifier** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Tiêu chí chọn primary identifier nối quyết định mô hình với index, foreign key và lifecycle của row. Sau đó cần so sánh trực tiếp identifying/non-identifying relationship để thấy khóa ảnh hưởng cấu trúc child thế nào.

## 15. Tiêu chí lựa chọn Primary Identifier

Khi gom phần **15. Tiêu chí lựa chọn Primary Identifier** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **15. Tiêu chí lựa chọn Primary Identifier**. Bây giờ chuyển sang **15.1. Chọn Attribute được sử dụng thường xuyên**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **15.1. Chọn Attribute được sử dụng thường xuyên** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 15.1. Chọn Attribute được sử dụng thường xuyên

**해당 업무에서 자주 이용되는 속성을 주식별자로 선택하는 것이 좋다.**

Nên chọn Attribute được sử dụng thường xuyên trong nghiệp vụ làm Primary Identifier.

Ví dụ:

```
CUSTOMER_ID
```

được dùng thường xuyên để:

- Tìm khách hàng.
- Liên kết đơn hàng.
- Liên kết thanh toán.
- Tra cứu lịch sử.

---

Khi gom phần **15.1. Chọn Attribute được sử dụng thường xuyên** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **15.1. Chọn Attribute được sử dụng thường xuyên**. Bây giờ chuyển sang **15.2. Chọn giá trị ít thay đổi**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **15.2. Chọn giá trị ít thay đổi** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 15.2. Chọn giá trị ít thay đổi

**주식별자는 업무에서 자주 변경되지 않는 값을 선택해야 한다.**

Primary Identifier phải là giá trị ít bị thay đổi trong nghiệp vụ.

Không nên chọn:

```
주소
전화번호
부서명
```

vì các giá trị này có thể thay đổi.

Nên chọn:

```
EMPLOYEE_ID
CUSTOMER_ID
PRODUCT_CODE
```

nếu chúng được duy trì ổn định.

---

Khi gom phần **15.2. Chọn giá trị ít thay đổi** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **15.2. Chọn giá trị ít thay đổi**. Bây giờ chuyển sang **15.3. Tránh tên hoặc nội dung mô tả**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **15.3. Tránh tên hoặc nội dung mô tả** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 15.3. Tránh tên hoặc nội dung mô tả

**이름이나 내역처럼 서술형으로 표현되는 속성은 가급적 주식별자로 사용하지 않는 것이 좋다.**

Nên hạn chế sử dụng Attribute mô tả như tên hoặc nội dung làm Primary Identifier.

Ví dụ không tốt:

```
STUDENT_NAME
PRODUCT_NAME
DEPARTMENT_NAME
```

Lý do:

- Tên có thể trùng.
- Tên có thể thay đổi.
- Tên có thể dài.
- So sánh chuỗi tốn chi phí hơn mã số.

---

Khi gom phần **15.3. Tránh tên hoặc nội dung mô tả** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **15.3. Tránh tên hoặc nội dung mô tả**. Bây giờ chuyển sang **15.4. Hạn chế số lượng Attribute trong Composite Key**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **15.4. Hạn chế số lượng Attribute trong Composite Key** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 15.4. Hạn chế số lượng Attribute trong Composite Key

**복합 식별자를 구성할 때 너무 많은 속성을 포함하지 않는 것이 좋다.**

Khi tạo Composite Identifier, không nên bao gồm quá nhiều Attribute.

Ví dụ không tốt:

```
STUDENT_ID
COURSE_ID
YEAR
SEMESTER
DEPARTMENT_CODE
PROFESSOR_ID
CLASSROOM_CODE
```

Một khóa ghép quá dài sẽ:

- Khó đọc.
- Khó Join.
- Tăng độ phức tạp SQL.
- Làm khóa ngoại ở bảng con dài theo.
- Khó phát triển và bảo trì.

---

Khi gom phần **15.4. Hạn chế số lượng Attribute trong Composite Key** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **15.4. Hạn chế số lượng Attribute trong Composite Key**. Bây giờ chuyển sang **16. 식별자 관계 và 비식별자 관계: So sánh trọng tâm**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **16. 식별자 관계 và 비식별자 관계: So sánh trọng tâm** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

So sánh hai loại quan hệ cho thấy việc đưa parent key vào child identity là quyết định về ownership, không chỉ là ký pháp. Sơ đồ tổng hợp cuối hình sẽ kiểm tra các quyết định entity, attribute, relationship và identifier có nhất quán cùng nhau không.

## 16. 식별자 관계 và 비식별자 관계: So sánh trọng tâm

Phần này nối mạch SQL với “16. 식별자 관계 và 비식별자 관계: So sánh trọng tâm”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

| Tiêu chí | 식별자 관계 | 비식별자 관계 |
| --- | --- | --- |
| PK cha | Được kế thừa vào PK con | Không thuộc PK con |
| FK cha | Vừa là FK vừa là một phần PK | Chỉ là FK |
| Entity con | Phụ thuộc mạnh vào cha | Có thể độc lập hơn |
| Strong/Weak | Cha Strong, con Weak | Quan hệ yếu hơn |
| Ký pháp | Đường liền | Đường nét đứt |
| Mục tiêu | Thể hiện phụ thuộc định danh | Giảm phức tạp khóa |
| Ví dụ | `STUDENT - ENROLLMENT` | `DEPARTMENT - EMPLOYEE` |

Khi gom phần **16. 식별자 관계 và 비식별자 관계: So sánh trọng tâm** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **16. 식별자 관계 và 비식별자 관계: So sánh trọng tâm**. Bây giờ chuyển sang **Cách ghi nhớ**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Cách ghi nhớ** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Cách ghi nhớ

Phần này nối mạch SQL với “Cách ghi nhớ”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```
식별자 관계:
Cha cho con mượn Identifier để tạo PK.

비식별자 관계:
Con có Identifier riêng, cha chỉ cung cấp FK.
```

---

Khi gom phần **Cách ghi nhớ** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Cách ghi nhớ**. Bây giờ chuyển sang **17. Phân tích sơ đồ tổng hợp cuối hình**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **17. Phân tích sơ đồ tổng hợp cuối hình** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Phân tích sơ đồ tổng hợp cần lần lượt kiểm tra grain, cardinality, optionality, domain, key và đường phụ thuộc. Khi các lớp đã khớp, phần kết luận có thể cô đọng thành checklist áp dụng cho mô hình mới.

## 17. Phân tích sơ đồ tổng hợp cuối hình

Trong sơ đồ cuối:

```
부서
- 부서번호

사원
- 사번
- 주민등록번호
- 부서번호

교육이력
- 사번(FK)
- 수강일자

구매신청
- 주문번호
- 사번(FK)
- 주문일자
```

Khi gom phần **17. Phân tích sơ đồ tổng hợp cuối hình** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **17. Phân tích sơ đồ tổng hợp cuối hình**. Bây giờ chuyển sang **17.1. Department**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **17.1. Department** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 17.1. Department

**부서번호는 부서 엔터티의 주식별자이면서 내부식별자, 단일식별자, 원조식별자이다.**

`DEPARTMENT_ID` là Primary Identifier, Internal Identifier, Single Identifier và Natural Identifier của Entity Department.

Giải thích:

- `부서번호` là PK.
- Nó được tạo bên trong hệ thống.
- Chỉ một Attribute cũng đủ xác định phòng ban.
- Nó có thể là mã nghiệp vụ tự nhiên.

Khi gom phần **17.1. Department** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **17.1. Department**. Bây giờ chuyển sang **17.2. Employee**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **17.2. Employee** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 17.2. Employee

**사번은 사원 엔터티의 주식별자이며 주민등록번호는 보조식별자로 볼 수 있다.**

`EMPLOYEE_ID` là Primary Identifier của Employee, còn số đăng ký cư trú có thể là Candidate/Alternate Identifier.

**부서번호는 부서 엔터티에서 물려받은 외부식별자이다.**

`DEPARTMENT_ID` là External Identifier được kế thừa từ Entity Department.

Khi gom phần **17.2. Employee** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **17.2. Employee**. Bây giờ chuyển sang **17.3. Education History**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **17.3. Education History** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 17.3. Education History

**교육이력의 사번은 사원 엔터티를 참조하는 외래키이다.**

`EMPLOYEE_ID` trong Education History là Foreign Key tham chiếu đến Employee.

Nếu `교육이력` dùng:

```
사번 + 수강일자
```

làm khóa thì có thể là Composite Identifier.

Khi gom phần **17.3. Education History** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **17.3. Education History**. Bây giờ chuyển sang **17.4. Purchase Request**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **17.4. Purchase Request** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 17.4. Purchase Request

**구매신청의 주문번호는 인조식별자로 사용될 수 있다.**

`ORDER_NUMBER` của Purchase Request có thể được sử dụng làm Artificial Identifier.

**사번과 주문일자와 순번을 결합하여 주문번호를 만들 수도 있다.**

Có thể kết hợp Employee ID, ngày đặt hàng và số thứ tự để tạo Order Number.

Ví dụ:

```
주문번호 = 사번 + 주문일자 + 순번
```

Đây là Composite Artificial Identifier nếu được hệ thống tạo ra thay vì lấy từ bản chất nghiệp vụ.

---

Khi gom phần **17.4. Purchase Request** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **17.4. Purchase Request**. Bây giờ chuyển sang **KẾT LUẬN GHI NHỚ CUỐI BÀI**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **KẾT LUẬN GHI NHỚ CUỐI BÀI** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

KẾT LUẬN GHI NHỚ nên giữ ranh giới giữa ngữ nghĩa nghiệp vụ, ERD và schema triển khai: một đường nối đúng hình chưa đủ nếu key hoặc cardinality sai. Checklist cuối cùng là kiểm tra identity, dependency, normalization và constraint trước khi tạo bảng.

## KẾT LUẬN GHI NHỚ CUỐI BÀI

Khi gom phần **KẾT LUẬN GHI NHỚ CUỐI BÀI** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **KẾT LUẬN GHI NHỚ CUỐI BÀI**. Bây giờ chuyển sang **1. Bản chất của Relationship**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **1. Bản chất của Relationship** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 1. Bản chất của Relationship

**관계는 엔터티 인스턴스 사이의 논리적 연관성 또는 업무 행위로 만들어지는 연결이다.**

Relationship là sự liên kết được tạo ra bởi mối liên quan logic hoặc hành động nghiệp vụ giữa các Instance của Entity.

```
Entity = Tập hợp Instance
Relationship = Tập hợp Pairing
```

---

Khi gom phần **1. Bản chất của Relationship** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **1. Bản chất của Relationship**. Bây giờ chuyển sang **2. Hai loại Relationship chính**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **2. Hai loại Relationship chính** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 2. Hai loại Relationship chính

Phần này nối mạch SQL với “2. Hai loại Relationship chính”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

| 한국어 | Tiếng Việt | Đặc điểm |
| --- | --- | --- |
| 존재에 의한 관계 | Relationship do sự tồn tại | Các Entity có thể tồn tại độc lập |
| 행위에 의한 관계 | Relationship do hành động | Quan hệ phát sinh do một hành động nghiệp vụ |

```
존재 관계 = Thuộc về / liên kết do tồn tại
행위 관계 = Được tạo ra do hành động
```

---

Khi gom phần **2. Hai loại Relationship chính** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **2. Hai loại Relationship chính**. Bây giờ chuyển sang **3. Quan hệ trong UML**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **3. Quan hệ trong UML** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 3. Quan hệ trong UML

Phần này nối mạch SQL với “3. Quan hệ trong UML”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

| Quan hệ | Ký pháp UML | Ý nghĩa |
| --- | --- | --- |
| 연관관계 | Đường liền | Association |
| 의존관계 | Đường nét đứt | Dependency |

Lưu ý:

**ERD에서는 UML과 달리 존재 관계와 행위 관계를 반드시 별도의 선으로 구분하지 않는다.**

Trong ERD, khác với UML, Relationship tồn tại và Relationship hành động không nhất thiết phải dùng loại đường riêng để phân biệt.

---

Khi gom phần **3. Quan hệ trong UML** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **3. Quan hệ trong UML**. Bây giờ chuyển sang **4. Các thành phần cần ghi trên Relationship**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **4. Các thành phần cần ghi trên Relationship** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 4. Các thành phần cần ghi trên Relationship

Phần này nối mạch SQL với “4. Các thành phần cần ghi trên Relationship”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```
관계명        = Tên quan hệ
관계차수      = Cardinality
관계선택사양  = Bắt buộc hoặc tùy chọn
```

Ví dụ:

```
DEPARTMENT 1 ─── N EMPLOYEE
```

Có thể đọc:

```
Một Department có nhiều Employee.
Một Employee thuộc một Department.
```

---

Khi gom phần **4. Các thành phần cần ghi trên Relationship** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Như vậy, **4. Các thành phần cần ghi trên Relationship** đã được đặt trong quan hệ giữa đầu vào, quy tắc xử lý và kết quả. Khi ôn lại, hãy tự diễn đạt ranh giới của nó rồi dùng ranh giới đó làm điểm nối sang bài tiếp theo.

> **Bàn giao:** Sau **KẾT LUẬN GHI NHỚ CUỐI BÀI**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
