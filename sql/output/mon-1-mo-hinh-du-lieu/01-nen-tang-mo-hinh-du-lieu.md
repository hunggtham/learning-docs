# Nền tảng mô hình hóa dữ liệu

## I. 데이터 모델링의 이해

## 1. 데이터 모델링이란 무엇인가?

### 1.1. Định nghĩa

**데이터 모델링은 복잡한 현실 세계를 추상화하고 단순화하여 일정한 표기법으로 명확하게 표현하는 과정이다.**

Mô hình hóa dữ liệu là quá trình trừu tượng hóa và đơn giản hóa thế giới thực phức tạp, sau đó biểu diễn nó một cách rõ ràng bằng một hệ thống ký hiệu nhất định.

#### Keyword: 데이터 모델링

**데이터 모델링은 업무에서 필요한 데이터를 분석하고 데이터 간의 관계를 정의하여 데이터베이스 구조로 표현하는 작업이다.**

Mô hình hóa dữ liệu là công việc phân tích dữ liệu cần thiết trong nghiệp vụ, xác định mối quan hệ giữa các dữ liệu và biểu diễn chúng thành cấu trúc cơ sở dữ liệu.

Nói đơn giản hơn:

> Mô hình hóa dữ liệu là biến hoạt động ngoài đời thực thành bảng, cột, khóa và quan hệ trong database.
>

Ví dụ, trong thế giới thực:

```
Một khách hàng đặt nhiều đơn hàng.
Một đơn hàng có nhiều sản phẩm.
Một sản phẩm có thể xuất hiện trong nhiều đơn hàng.
```

Khi mô hình hóa, ta chuyển thành:

```
CUSTOMER 1 ─── N ORDER
ORDER    1 ─── N ORDER_ITEM
PRODUCT  1 ─── N ORDER_ITEM
```

---

### 1.2. 현실 세계 - Thế giới thực

**현실 세계는 사람, 상품, 주문, 결제, 직원과 같은 실제 업무 대상과 업무 활동이 존재하는 세계이다.**

Thế giới thực là nơi tồn tại các đối tượng và hoạt động nghiệp vụ như con người, sản phẩm, đơn hàng, thanh toán và nhân viên.

#### Keyword: 현실 세계

**현실 세계에는 정보가 많고 서로 복잡하게 연결되어 있기 때문에 데이터베이스에 그대로 저장하기 어렵다.**

Vì thế giới thực có rất nhiều thông tin và các thông tin liên kết phức tạp với nhau nên không thể lưu nguyên trạng vào database.

Ví dụ một cửa hàng có:

- Khách hàng.
- Sản phẩm.
- Nhân viên.
- Đơn hàng.
- Thanh toán.
- Kho hàng.
- Giao hàng.
- Khuyến mãi.

Nếu ghi lại mọi chi tiết của cửa hàng thì dữ liệu sẽ rất phức tạp, vì vậy cần chọn lọc.

---

### 1.3. 추상화 - Trừu tượng hóa

**추상화란 현실 세계의 모든 세부 정보를 표현하지 않고 업무에 필요한 핵심 정보만 선택하여 표현하는 것이다.**

Trừu tượng hóa là không biểu diễn tất cả chi tiết của thế giới thực mà chỉ chọn và biểu diễn những thông tin cốt lõi cần cho nghiệp vụ.

#### Keyword: 추상화

**추상화의 핵심은 불필요한 세부 사항을 제거하고 중요한 본질만 남기는 것이다.**

Bản chất của trừu tượng hóa là loại bỏ các chi tiết không cần thiết và chỉ giữ lại bản chất quan trọng.

Ví dụ trong hệ thống quản lý nhân viên, ta cần:

```
EMPLOYEE_ID
EMPLOYEE_NAME
DEPARTMENT_ID
HIRE_DATE
SALARY
```

Nhưng có thể không cần lưu:

```
Màu áo nhân viên mặc hôm nay
Món ăn nhân viên thích
Phương tiện nhân viên dùng để đi làm
```

Những thông tin này tồn tại trong thực tế nhưng không cần thiết cho mục tiêu quản lý nhân sự.

#### Cách hiểu dễ nhớ

```
추상화 = Bỏ chi tiết phụ, giữ bản chất chính
```

---

### 1.4. 단순화 - Đơn giản hóa

**단순화란 복잡한 현실을 제한된 규칙과 표현 방식으로 간결하게 나타내는 것이다.**

Đơn giản hóa là biểu diễn thế giới thực phức tạp bằng các quy tắc và phương thức biểu diễn giới hạn, ngắn gọn hơn.

#### Keyword: 단순화

**단순화는 복잡한 업무를 엔터티, 속성, 관계와 같은 일정한 구조로 정리하는 것이다.**

Đơn giản hóa là sắp xếp nghiệp vụ phức tạp thành các cấu trúc nhất định như Entity, Attribute và Relationship.

Ví dụ câu nghiệp vụ dài:

> Một khách hàng có thể đặt nhiều đơn hàng và mỗi đơn hàng có thể chứa nhiều sản phẩm.
>

Được đơn giản hóa thành:

```
CUSTOMER 1 : N ORDER
ORDER 1 : N ORDER_ITEM
PRODUCT 1 : N ORDER_ITEM
```

Hoặc thành các bảng:

```
CUSTOMER
ORDER
ORDER_ITEM
PRODUCT
```

#### Cách hiểu dễ nhớ

```
단순화 = Biến câu chuyện nghiệp vụ phức tạp thành cấu trúc dễ nhìn
```

---

### 1.5. 명확화 - Làm rõ

**명확화란 업무 규칙과 데이터 간의 관계에서 애매모호함을 제거하고 정확하게 표현하는 것이다.**

Làm rõ là loại bỏ sự mơ hồ trong quy tắc nghiệp vụ và mối quan hệ giữa các dữ liệu, sau đó biểu diễn chúng một cách chính xác.

#### Keyword: 명확화

**명확화의 목적은 서로 다른 사람이 같은 업무를 hiểu theo cùng một cách.**

Mục đích của làm rõ là bảo đảm những người khác nhau hiểu cùng một nghiệp vụ theo cùng một cách.

Ví dụ câu mơ hồ:

> Một nhân viên có thể làm việc tại một số phòng ban.
>

Câu này chưa rõ:

- Một nhân viên thuộc một phòng ban hay nhiều phòng ban?
- Có bắt buộc phải thuộc phòng ban không?
- Một phòng ban có thể có bao nhiêu nhân viên?
- Khi nhân viên chuyển phòng ban thì xử lý thế nào?

Mô hình rõ ràng hơn:

```
DEPARTMENT 1 ─── N EMPLOYEE
```

Điều này có nghĩa:

- Một phòng ban có thể có nhiều nhân viên.
- Một nhân viên thuộc một phòng ban.
- `EMPLOYEE.DEPARTMENT_ID` có thể là Foreign Key.

#### Cách hiểu dễ nhớ

```
명확화 = Không để người đọc phải đoán
```

---

## 2. Mục đích của 데이터 모델링

**데이터 모델링은 데이터베이스를 구축하기 위한 분석과 설계의 과정이다.**

Mô hình hóa dữ liệu là quá trình phân tích và thiết kế để xây dựng cơ sở dữ liệu.

#### Keyword: 분석 - Phân tích

**분석은 업무에서 어떤 데이터가 필요하고 그 데이터가 어떻게 사용되는지 파악하는 과정이다.**

Phân tích là quá trình xác định nghiệp vụ cần dữ liệu nào và dữ liệu đó được sử dụng như thế nào.

#### Keyword: 설계 - Thiết kế

**설계는 분석한 결과를 바탕으로 엔터티, 속성, 관계, 키와 같은 데이터베이스 구조를 결정하는 과정이다.**

Thiết kế là quá trình quyết định cấu trúc database như Entity, Attribute, Relationship và Key dựa trên kết quả phân tích.

Quy trình tổng quát:

```
Phân tích nghiệp vụ
→ Xác định Entity
→ Xác định Attribute
→ Xác định Relationship
→ Xác định Key
→ Chuẩn hóa
→ Thiết kế bảng
→ Tạo database
```

---

## 3. Đặc điểm của mô hình hóa dữ liệu

Tài liệu nêu ba đặc điểm chính:

```
추상화
단순화
명확화
```

### 3.1. 추상화

**추상화는 현실 세계를 일정한 형식에 맞추어 간략하게 표현하는 것이다.**

Trừu tượng hóa là biểu diễn thế giới thực một cách ngắn gọn theo một hình thức nhất định.

#### Giải thích lại keyword

**추상화에서는 현실의 모든 요소를 저장하지 않고 시스템 목적에 필요한 요소만 선택한다.**

Trong trừu tượng hóa, ta không lưu tất cả yếu tố của thế giới thực mà chỉ chọn những yếu tố cần cho mục tiêu của hệ thống.

---

### 3.2. 단순화

**단순화는 약속된 규약과 제한된 언어를 사용하여 업무 내용을 간결하게 표현하는 것이다.**

Đơn giản hóa là biểu diễn nội dung nghiệp vụ một cách ngắn gọn bằng các quy ước và ngôn ngữ giới hạn đã thống nhất.

#### Giải thích lại keyword

**단순화는 복잡한 업무를 테이블, 컬럼, 키와 같은 데이터베이스 구성 요소로 변환하는 것이다.**

Đơn giản hóa là chuyển nghiệp vụ phức tạp thành các thành phần database như bảng, cột và khóa.

---

### 3.3. 명확화

**명확화는 애매한 업무 규칙을 제거하고 데이터와 데이터의 관계를 정확하게 정의하는 것이다.**

Làm rõ là loại bỏ các quy tắc nghiệp vụ mơ hồ và định nghĩa chính xác quan hệ giữa các dữ liệu.

#### Giải thích lại keyword

**명확화가 이루어지면 개발자와 사용자가 동일한 업무 규칙을 이해할 수 있다.**

Khi việc làm rõ được thực hiện, nhà phát triển và người dùng có thể hiểu cùng một quy tắc nghiệp vụ.

#### Bảng đối chiếu 3 đặc trưng mô hình hóa & Cạm bẫy thuật ngữ đề thi

| Đặc trưng chuẩn (ĐÚNG) | Ý nghĩa nghiệp vụ | Thuật ngữ gây nhiễu đề thi (SAI) | Lý do sai |
| :--- | :--- | :--- | :--- |
| **추상화 (Abstraction)** | Lược bỏ chi tiết vụn vặt, chỉ giữ lại bản chất cốt lõi | **구체화 (Concretization)** | Mô hình hóa không ghi lại toàn bộ chi tiết cụ thể của đời thực |
| **단순화 (Simplification)** | Biểu diễn quy tắc phức tạp bằng ký pháp chuẩn hóa, dễ hiểu | **복잡화 (Complication)** | Mục tiêu mô hình là giảm độ phức tạp, không làm rắc rối thêm |
| **명확화 (Clarity)** | Triệt tiêu sự mơ hồ, bảo đảm mọi người hiểu duy nhất 1 nghĩa | **일반화 (Generalization)** | Đề thi hay đưa 일반화 để đánh lừa vì nghe có vẻ hợp lý nhưng không thuộc 3 đặc trưng |

---

## 4. Các góc nhìn của mô hình hóa

Tài liệu chia thành ba góc nhìn:

```
데이터 관점
프로세스 관점
데이터와 프로세스의 상관관점
```

---

### 4.1. 데이터 관점 - Góc nhìn dữ liệu

**데이터 관점은 “무엇이 필요한가?”에 관심을 두는 관점이다.**

Góc nhìn dữ liệu quan tâm đến câu hỏi: “Cần những dữ liệu gì?”

**데이터 관점에서는 업무와 데이터의 관계, 데이터와 데이터의 관계를 모델링한다.**

Ở góc nhìn dữ liệu, ta mô hình hóa quan hệ giữa nghiệp vụ và dữ liệu, cũng như quan hệ giữa dữ liệu với dữ liệu.

#### Keyword: 데이터 관점

**데이터 관점은 시스템에서 관리해야 할 엔터티, 속성, 관계를 파악하는 관점이다.**

Góc nhìn dữ liệu là góc nhìn xác định các Entity, Attribute và Relationship cần được quản lý trong hệ thống.

Ví dụ:

```
CUSTOMER
PRODUCT
ORDER
PAYMENT
```

Câu hỏi của góc nhìn dữ liệu:

- Hệ thống cần quản lý đối tượng nào?
- Mỗi đối tượng có thuộc tính gì?
- Các đối tượng liên quan với nhau thế nào?
- Dữ liệu nào là khóa chính?
- Dữ liệu nào là khóa ngoại?

---

### 4.2. 프로세스 관점 - Góc nhìn quy trình

**프로세스 관점은 “어떤 절차와 순서로 업무가 이루어지는가?”에 관심을 두는 관점이다.**

Góc nhìn quy trình quan tâm đến câu hỏi: “Nghiệp vụ được thực hiện theo thủ tục và trình tự nào?”

**프로세스 관점에서는 업무가 실제로 수행되는 과정과 수행되어야 하는 작업을 모델링한다.**

Ở góc nhìn quy trình, ta mô hình hóa công việc đang được thực hiện và công việc cần phải thực hiện.

#### Keyword: 프로세스 관점

**프로세스 관점은 업무의 시작부터 종료까지의 흐름과 처리 순서를 분석하는 것이다.**

Góc nhìn quy trình là phân tích luồng và thứ tự xử lý từ khi nghiệp vụ bắt đầu đến khi kết thúc.

Ví dụ quy trình mua hàng:

```
Sản phẩm được chọn
→ Tạo đơn hàng
→ Kiểm tra tồn kho
→ Thanh toán
→ Đóng gói
→ Giao hàng
→ Hoàn tất
```

---

### 4.3. 데이터와 프로세스의 상관관점

**상호작용 관점은 업무 처리 방법에 따라 데이터가 어떻게 생성되고 변경되는지를 분석하는 관점이다.**

Góc nhìn tương tác phân tích dữ liệu được tạo ra và thay đổi như thế nào tùy theo cách xử lý nghiệp vụ.

#### Keyword: 상호작용

**상호작용은 프로세스가 데이터를 사용하고 데이터가 다시 프로세스의 결과로 변경되는 관계이다.**

Tương tác là mối quan hệ trong đó quy trình sử dụng dữ liệu và dữ liệu lại thay đổi do kết quả của quy trình.

Ví dụ:

| Quy trình | Tác động đến dữ liệu |
| --- | --- |
| Tạo đơn hàng | INSERT vào `ORDERS` |
| Thêm sản phẩm | INSERT vào `ORDER_ITEM` |
| Thanh toán | INSERT vào `PAYMENT` |
| Giao hàng | UPDATE trạng thái đơn |
| Hủy đơn | UPDATE trạng thái, hoàn kho |

#### Cách ghi nhớ

```
데이터 관점 = What?
프로세스 관점 = How?
상호작용 관점 = How làm thay đổi What?
```

---

## 5. Tầm quan trọng của mô hình hóa dữ liệu

**데이터 모델링의 중요성은 파급효과, 간결한 표현, 데이터 품질 유지에 있다.**

Tầm quan trọng của mô hình hóa dữ liệu nằm ở ảnh hưởng lan tỏa, khả năng biểu diễn ngắn gọn và duy trì chất lượng dữ liệu.

---

### 5.1. 파급효과 - Ảnh hưởng lan tỏa

**데이터 모델은 애플리케이션, 보고서, 분석 시스템과 연결되므로 변경의 파급효과가 크다.**

Mô hình dữ liệu liên kết với ứng dụng, báo cáo và hệ thống phân tích nên một thay đổi có thể tạo ra ảnh hưởng lan tỏa lớn.

#### Keyword: 파급효과

**파급효과란 한 부분의 변경이나 오류가 다른 여러 부분으로 퍼지는 영향이다.**

Ảnh hưởng lan tỏa là việc một thay đổi hoặc lỗi ở một phần lan sang nhiều phần khác.

Ví dụ nếu thiết kế sai quan hệ khách hàng và đơn hàng:

- Lịch sử mua hàng sai.
- Báo cáo doanh thu sai.
- Tính điểm thành viên sai.
- Gửi khuyến mãi sai.
- Phân tích khách hàng sai.

---

### 5.2. 간결한 표현 - Biểu diễn ngắn gọn

**데이터 모델링은 복잡한 업무를 엔터티와 관계로 표현하여 이해하기 쉽게 만든다.**

Mô hình hóa dữ liệu biểu diễn nghiệp vụ phức tạp bằng Entity và Relationship, từ đó làm cho nó dễ hiểu hơn.

#### Keyword: 간결한 표현

**간결한 표현은 긴 업무 설명을 짧고 구조화된 모델로 나타내는 것이다.**

Biểu diễn ngắn gọn là chuyển phần mô tả nghiệp vụ dài thành một mô hình ngắn gọn và có cấu trúc.

Ví dụ:

```
CUSTOMER 1 ─── N ORDER
```

Có thể thay thế cho câu:

> Một khách hàng có thể tạo nhiều đơn hàng, và mỗi đơn hàng thuộc về một khách hàng.
>

---

### 5.3. 데이터 품질 유지 - Duy trì chất lượng dữ liệu

**좋은 데이터 모델은 데이터 중복과 불일치를 줄이고 데이터의 정확성과 일관성을 유지한다.**

Một mô hình dữ liệu tốt làm giảm sự trùng lặp và không nhất quán, đồng thời duy trì tính chính xác và nhất quán của dữ liệu.

#### Keyword: 데이터 품질

**데이터 품질은 데이터가 정확하고 일관되며 완전하고 최신 상태인 정도를 의미한다.**

Chất lượng dữ liệu là mức độ dữ liệu chính xác, nhất quán, đầy đủ và được cập nhật.

---

## 6. Ba vấn đề cần tránh

### 6.1. 중복 - Trùng lặp

**중복은 동일한 정보가 여러 장소에 반복해서 저장되는 현상이다.**

Trùng lặp là hiện tượng cùng một thông tin được lưu lặp lại ở nhiều nơi.

Ví dụ thiết kế không tốt:

```
ORDER
-----
ORDER_ID
CUSTOMER_ID
CUSTOMER_NAME

PAYMENT
-------
PAYMENT_ID
ORDER_ID
CUSTOMER_ID
CUSTOMER_NAME
```

`CUSTOMER_NAME` bị lưu ở nhiều bảng.

#### Keyword: 중복

**불필요한 중복은 저장 공간을 낭비하고 데이터 수정 시 오류를 발생시킨다.**

Sự trùng lặp không cần thiết làm lãng phí dung lượng và gây lỗi khi cập nhật dữ liệu.

Ví dụ khách hàng đổi tên nhưng:

```
CUSTOMER.CUSTOMER_NAME = Nguyễn Văn B
ORDER.CUSTOMER_NAME    = Nguyễn Văn A
```

Khi đó dữ liệu không còn thống nhất.

---

### 6.2. 비유연성 - Không linh hoạt

**비유연성은 작은 업무 변경에도 데이터 모델을 자주 수정해야 하는 문제이다.**

Không linh hoạt là vấn đề phải thường xuyên sửa mô hình dữ liệu ngay cả khi nghiệp vụ chỉ thay đổi nhỏ.

#### Keyword: 비유연성

**데이터의 정의와 데이터 사용 프로세스가 강하게 결합되면 비유연성이 증가한다.**

Khi định nghĩa dữ liệu và quy trình sử dụng dữ liệu bị gắn chặt với nhau, tính không linh hoạt sẽ tăng lên.

Thiết kế không linh hoạt:

```
EMPLOYEE
--------
EMPLOYEE_ID
SALES_2024
SALES_2025
SALES_2026
```

Mỗi năm lại phải thêm một cột mới.

Thiết kế linh hoạt:

```
EMPLOYEE_SALES
-------------
EMPLOYEE_ID
SALES_YEAR
SALES_AMOUNT
```

Khi có năm mới, chỉ cần thêm dòng dữ liệu.

---

### 6.3. 비일관성 - Không nhất quán

**비일관성은 서로 관련된 데이터가 서로 다른 값을 가지는 현상이다.**

Không nhất quán là hiện tượng các dữ liệu có liên quan nhưng lại chứa những giá trị khác nhau.

#### Keyword: 비일관성

**데이터 간의 관계와 무결성 규칙이 명확하지 않으면 비일관성이 발생한다.**

Nếu quan hệ giữa các dữ liệu và quy tắc toàn vẹn không rõ ràng thì sẽ phát sinh sự không nhất quán.

Ví dụ:

```
ORDERS.CUSTOMER_ID = 9999
```

nhưng trong bảng `CUSTOMER` không tồn tại khách hàng `9999`.

Cách ngăn chặn:

```sql
FOREIGN KEY (CUSTOMER_ID)
REFERENCES CUSTOMER(CUSTOMER_ID)
```

---

## 7. Ba giai đoạn mô hình hóa dữ liệu

**데이터 모델링은 개념적 모델링, 논리적 모델링, 물리적 모델링의 3단계로 진행된다.**

Mô hình hóa dữ liệu được tiến hành qua ba giai đoạn: mô hình hóa khái niệm, logic và vật lý.

```
개념적 모델링
→ 논리적 모델링
→ 물리적 모델링
```

---

### 7.1. 개념적 모델링 - Mô hình hóa khái niệm

**개념적 모델링은 업무 중심적이고 포괄적인 수준에서 핵심 엔터티와 관계를 도출하는 단계이다.**

Mô hình hóa khái niệm là giai đoạn trích xuất các Entity và Relationship cốt lõi ở mức độ bao quát, tập trung vào nghiệp vụ.

**개념적 모델링은 세 단계 중 추상화 수준이 가장 높다.**

Mô hình hóa khái niệm có mức độ trừu tượng cao nhất trong ba giai đoạn.

#### Keyword: 개념적 모델링

**개념적 모델링에서는 특정 DBMS나 실제 컬럼의 데이터 타입보다 업무의 본질을 먼저 정의한다.**

Trong mô hình hóa khái niệm, ta xác định bản chất nghiệp vụ trước, thay vì quan tâm đến DBMS cụ thể hay kiểu dữ liệu của cột.

Ví dụ:

```
CUSTOMER
ORDER
PRODUCT
PAYMENT
```

Ở giai đoạn này chưa cần viết:

```sql
CUSTOMER_ID NUMBER(10)
CUSTOMER_NAME VARCHAR2(100)
```

#### Đặc điểm ghi nhớ

```
개념적 = 업무와 핵심 Entity
```

---

### 7.2. 논리적 모델링 - Mô hình hóa logic

**논리적 모델링은 엔터티를 테이블로 변환하고 키, 속성, 관계를 정의하는 단계이다.**

Mô hình hóa logic là giai đoạn chuyển Entity thành bảng và xác định Key, Attribute, Relationship.

**논리적 모델링에서는 정규화를 적용하여 데이터의 중복과 불일치를 줄인다.**

Trong mô hình hóa logic, ta áp dụng chuẩn hóa để giảm trùng lặp và không nhất quán dữ liệu.

#### Keyword: 논리적 모델링

**논리적 모델링은 업무 개념을 관계형 데이터베이스가 이해할 수 있는 논리적 구조로 변환하는 과정이다.**

Mô hình hóa logic là quá trình chuyển khái niệm nghiệp vụ thành cấu trúc logic mà cơ sở dữ liệu quan hệ có thể hiểu.

Ví dụ:

```
Entity: Customer
→ Table: CUSTOMER

Attribute:
- Customer ID
- Customer Name

Key:
- Primary Key: CUSTOMER_ID
```

#### Đặc điểm ghi nhớ

```
논리적 = 테이블, 키, 속성, 관계, 정규화
```

---

### 7.3. 물리적 모델링 - Mô hình hóa vật lý

**물리적 모델링은 특정 DBMS의 특성에 맞게 인덱스와 저장 방식 등을 설계하는 단계이다.**

Mô hình hóa vật lý là giai đoạn thiết kế Index, phương thức lưu trữ và các yếu tố khác phù hợp với đặc điểm của DBMS cụ thể.

**물리적 모델링에서는 데이터 타입, 인덱스, 파티션, 테이블스페이스와 같은 실제 구현 요소를 고려한다.**

Trong mô hình hóa vật lý, ta xem xét các yếu tố triển khai thực tế như kiểu dữ liệu, Index, Partition và Tablespace.

#### Keyword: 물리적 모델링

**물리적 모델링은 논리적 모델을 실제 DBMS에서 성능과 저장 효율을 고려하여 구현하는 과정이다.**

Mô hình hóa vật lý là quá trình triển khai mô hình logic trong DBMS thực tế, có cân nhắc đến hiệu năng và hiệu quả lưu trữ.

Ví dụ Oracle:

```sql
CREATE TABLE CUSTOMER (
    CUSTOMER_ID NUMBER(10),
    CUSTOMER_NAME VARCHAR2(100)
);

CREATE INDEX IDX_CUSTOMER_NAME
ON CUSTOMER(CUSTOMER_NAME);
```

#### Đặc điểm ghi nhớ

```
물리적 = DBMS, 데이터 타입, 인덱스, 저장
```

---

## 8. So sánh ba cấp độ

| 한국어 | Tiếng Việt | Keyword chính |
| --- | --- | --- |
| 개념적 모델링 | Mô hình khái niệm | 업무, Entity, ERD |
| 논리적 모델링 | Mô hình logic | Table, Key, Attribute, Relationship, Normalization |
| 물리적 모델링 | Mô hình vật lý | DBMS, Data Type, Index, Storage |

Câu ghi nhớ:

**개념적 모델링은 업무와 엔터티를 중심으로 한다.**

Mô hình hóa khái niệm tập trung vào nghiệp vụ và Entity.

**논리적 모델링은 테이블과 정규화를 중심으로 한다.**

Mô hình hóa logic tập trung vào bảng và chuẩn hóa.

**물리적 모델링은 인덱스와 저장 방식을 중심으로 한다.**

Mô hình hóa vật lý tập trung vào Index và phương thức lưu trữ.

---

## 8.1. Ba yếu tố cấu thành của mô hình hóa dữ liệu (데이터 모델링의 3대 요소)

Mô hình hóa dữ liệu phân rã thế giới thực thành 3 yếu tố cấu thành cốt lõi:

1. **Things (어떤 것 / 대상):** Đối tượng nghiệp vụ mà hệ thống cần quản lý (ví dụ: Sinh viên, Khách hàng, Sản phẩm).
2. **Attributes (성격 / 특성):** Các tính chất, đặc điểm mô tả đối tượng đó (ví dụ: Tên, Mã số, Đơn giá).
3. **Relationships (연관 / 관계):** Mối liên kết, tương tác qua lại giữa các đối tượng (ví dụ: Sinh viên "đăng ký" Môn học, Khách hàng "đặt" Đơn hàng).

#### Bảng đối chiếu khái niệm Tập hợp (복수·집합 개념) vs Cá thể (개별·단수 개념)

Đây là bảng kiến thức then chốt thường xuyên xuất hiện trong các câu hỏi phân loại của kỳ thi SQLD:

| Yếu tố cấu thành | Khái niệm Tập hợp (복수/집합 개념) - Type/Class | Khái niệm Cá thể (개별/단수 개념) - Instance/Occurrence |
| :--- | :--- | :--- |
| **Đối tượng (Things)** | **엔터티 타입 (Entity Type)** hoặc **엔터티 (Entity)** | **엔터티 인스턴스 (Instance)** hoặc **어커런스 (Occurrence)** |
| **Mối liên hệ (Relationships)** | **관계 (Relationship)** | **페어링 (Pairing)** |
| **Đặc tính (Attributes)** | **속성 (Attribute)** | **속성값 (Attribute Value)** |

> [!IMPORTANT]
> **Điểm thi cốt lõi (핵심 출제 포인트):**
> - **관계 (Relationship):** Là tập hợp của tất cả các mối liên hệ giữa các thực thể ở mức độ lớp (Class/Type).
> - **페어링 (Pairing):** Là mối liên hệ cụ thể giữa một cá thể (Instance) này với một cá thể (Instance) khác.
> - *Ví dụ:* "Khách hàng mua Hàng hóa" là **관계 (Relationship)**. "Khách hàng Nguyễn Văn A mua Điện thoại iPhone 16 lúc 10:00" là **페어링 (Pairing)**.

---

## 8.2. Sáu yếu tố của một mô hình dữ liệu tốt (좋은 데이터 모델의 요소)

Theo giáo trình chuẩn SQLD (K-Data), một mô hình dữ liệu được đánh giá là xuất sắc khi đáp ứng đủ 6 tiêu chí:

| Tiêu chí (Hàn / Việt) | Định nghĩa chuẩn K-Data | Hậu quả nếu vi phạm |
| :--- | :--- | :--- |
| **완전성 (Completeness / Tính toàn diện)** | Định nghĩa đầy đủ tất cả dữ liệu cần thiết để vận hành nghiệp vụ. | Hệ thống thiếu dữ liệu xử lý, nghiệp vụ bị tắc nghẽn hoặc sai lệch. |
| **중복 배제 (Non-redundancy / Loại bỏ trùng lặp)** | Một sự thật chỉ được lưu duy nhất một lần trong toàn bộ CSDL (ngoại trừ Foreign Key). | Dẫn đến dị thường cập nhật (Update Anomaly), dữ liệu mâu thuẫn giữa các bảng. |
| **업무 규칙 (Business Rules / Phản ánh quy tắc)** | Mọi ràng buộc nghiệp vụ (Not Null, Unique, Check, Cardinality) phải được mô hình hóa rõ ràng. | Dữ liệu rác lọt vào CSDL, người dùng vi phạm quy trình vận hành. |
| **데이터 재사용 (Data Reusability / Khả năng tái sử dụng)** | Dữ liệu được tổ chức độc lập để nhiều ứng dụng và phòng ban có thể tái sử dụng lâu dài. | Dữ liệu bị cô lập theo từng ứng dụng (như thời File System), chi phí tích hợp cao. |
| **의사소통 (Communication / Ngôn ngữ giao tiếp)** | Đóng vai trò là ngôn ngữ trao đổi chung, thống nhất giữa Business, Developer và DBA. | Lập trình viên hiểu sai nghiệp vụ, xây dựng tính năng không đúng yêu cầu. |
| **통합성 (Integration / Tính tích hợp toàn cục)** | Cùng một dữ liệu chỉ được định nghĩa một lần trên quy mô toàn doanh nghiệp. | Phát sinh các bảng "đảo dữ liệu" (Data Silo) rời rạc, khó tổng hợp báo cáo. |

---

## 9. Kiến trúc 3 tầng lược đồ ANSI/SPARC (ANSI/SPARC 3단계 스키마 구조)

Để đảm bảo tính độc lập dữ liệu và che giấu sự phức tạp của việc lưu trữ vật lý đối với người dùng, tổ chức ANSI/X3/SPARC đã chuẩn hóa kiến trúc cơ sở dữ liệu thành **3 tầng lược đồ (3단계 스키마 구조)**:

### 9.1. 외부 스키마 (External Schema) — Góc nhìn người dùng (사용자 관점)
- **Khái niệm:** Là tầng mô tả khung nhìn dữ liệu của từng cá nhân, nhóm người dùng hoặc một chương trình ứng dụng cụ thể (**View / 사용자 뷰**).
- **Đặc trưng:**
  - Mỗi nhóm người dùng (ví dụ: nhân viên bán hàng, kế toán, quản trị viên) chỉ nhìn thấy và thao tác trên phần dữ liệu liên quan trực tiếp đến nghiệp vụ của mình.
  - Một cơ sở dữ liệu có thể có **nhiều 외부 스키마** khác nhau cùng tồn tại.
  - Được định nghĩa thông qua các View (Khung nhìn) hoặc giao diện truy vấn trong ứng dụng.

### 9.2. 개념 스키마 (Conceptual Schema) — Góc nhìn tổng thể toàn cục (통합 관점)
- **Khái niệm:** Là tầng mô tả cấu trúc logic toàn diện của toàn bộ cơ sở dữ liệu của một tổ chức (**Toàn bộ Entity, Attribute, Relationship, Ràng buộc nghiệp vụ và Phân quyền**).
- **Đặc trưng:**
  - Đóng vai trò là bức tranh tổng hợp hợp nhất tất cả các góc nhìn bên ngoài thành một thể thống nhất độc lập với DBMS vật lý cụ thể.
  - Mỗi hệ thống cơ sở dữ liệu chỉ có **duy nhất 1 개념 스키마** đại diện cho toàn bộ tổ chức.
  - Chính là sản phẩm đầu ra hoàn chỉnh của giai đoạn **Mô hình hóa dữ liệu logic (논리적 데이터 모델링)**.

### 9.3. 내부 스키마 (Internal Schema) — Góc nhìn lưu trữ vật lý (물리적 저장 관점)
- **Khái niệm:** Là tầng mô tả cách thức dữ liệu thực sự được tổ chức và lưu trữ vật lý trên các thiết bị đĩa cứng (**Storage Structures, Data Types, Block Sizes, Indices, Hashing**).
- **Đặc trưng:**
  - Phản ánh chi tiết việc cấp phát bộ nhớ, cấu trúc tệp tin, đường dẫn truy cập (Access Paths) và chỉ mục Index nhằm tối ưu hóa hiệu năng I/O.
  - Mỗi cơ sở dữ liệu chỉ có **duy nhất 1 내부 스키마**.
  - Chính là sản phẩm đầu ra của giai đoạn **Mô hình hóa dữ liệu vật lý (물리적 데이터 모델링)**.

---

### 9.4. Cơ chế ánh xạ 2 tầng (2단계 사상 - Mapping)

Mối liên kết giữa 3 tầng lược đồ được duy trì thông qua 2 cơ chế ánh xạ độc lập nhằm bảo đảm tính độc lập dữ liệu:

1. **외부/개념 사상 (External / Conceptual Mapping — 논리적 사상 / Ánh xạ logic):**
   - Ánh xạ giữa từng góc nhìn người dùng (외부 스키마) và lược đồ logic toàn cục (개념 스키마).
   - Xác định xem dữ liệu hiển thị trên ứng dụng tương ứng với bảng và cột nào trong cấu trúc toàn hệ thống.
   - **Mang lại Tính độc lập dữ liệu logic (논리적 데이터 독립성).**

2. **개념/내부 사상 (Conceptual / Internal Mapping — 물리적 사상 / Ánh xạ vật lý):**
   - Ánh xạ giữa lược đồ logic toàn cục (개념 스키마) và cấu trúc lưu trữ trên đĩa cứng (내부 스키마).
   - Xác định bảng logic được lưu trữ trong tệp nào, trên tablespace nào, và sử dụng những Index vật lý nào.
   - **Mang lại Tính độc lập dữ liệu vật lý (물리적 데이터 독립성).**

---

## 10. Tính độc lập của dữ liệu (데이터 독립성 - Data Independence)

**데이터 독립성이란 하위 단계의 데이터 구조가 변경되어도 상위 단계의 구조나 응용 프로그램이 영향을 받지 않는 성질이다.**

Tính độc lập dữ liệu là đặc tính trong đó cấu trúc dữ liệu ở tầng dưới thay đổi nhưng cấu trúc tầng trên hoặc chương trình ứng dụng không bị ảnh hưởng.

### 10.1. 논리적 독립성 (Logical Data Independence)
- **Bản chất:** Khi **개념 스키마 (Lược đồ logic toàn cục)** bị thay đổi (ví dụ: thêm bảng mới, bổ sung thêm cột vào bảng, điều chỉnh quan hệ), **외부 스키마 và chương trình ứng dụng vẫn không phải sửa đổi**.
- **Cơ chế:** Nhờ có **외부/개념 사상 (Logical Mapping)**, ta chỉ cần điều chỉnh lại định nghĩa ánh xạ (ví dụ: cập nhật lại câu lệnh View) để duy trì giao diện cũ cho người dùng mà không cần viết lại toàn bộ mã nguồn chương trình.
- **Ví dụ thực tế:**
  Bảng `CUSTOMER` được bổ sung thêm cột `EMAIL` và `PHONE_NUMBER`. Chương trình kế toán cũ chỉ truy vấn `CUSTOMER_ID` và `CUSTOMER_NAME` vẫn chạy bình thường mà không phát sinh bất kỳ lỗi nào.

### 10.2. 물리적 독립성 (Physical Data Independence)
- **Bản chất:** Khi **내부 스키마 (Cấu trúc lưu trữ vật lý)** bị thay đổi (ví dụ: tạo thêm Index mới, di chuyển sang ổ đĩa SSD mới, chia phân vùng Partitioning, tổ chức lại khối dữ liệu), **개념 스키마 và chương trình ứng dụng hoàn toàn không bị ảnh hưởng**.
- **Cơ chế:** Nhờ có **개념/내부 사상 (Physical Mapping)**, hệ quản trị CSDL tự động ánh xạ cấu trúc bảng logic sang vị trí vật lý mới mà câu lệnh SQL của ứng dụng không cần thay đổi một ký tự nào.
- **Ví dụ thực tế:**
  DBA tạo thêm chỉ mục `CREATE INDEX IDX_CUST_NAME ON CUSTOMER(CUSTOMER_NAME)` hoặc phân vùng bảng theo năm. Câu lệnh `SELECT * FROM CUSTOMER WHERE CUSTOMER_NAME = 'Lee'` trong mã nguồn ứng dụng vẫn giữ nguyên, tốc độ truy vấn tăng lên mà mã nguồn không cần sửa đổi.

---

### 10.3. Bảng đối chiếu tổng hợp Kiến trúc ANSI/SPARC và Tính độc lập dữ liệu

| Tầng lược đồ (Schema) | Góc nhìn kiến trúc | Số lượng lược đồ | Cơ chế ánh xạ (Mapping) | Tính độc lập dữ liệu bảo đảm |
| :--- | :--- | :---: | :--- | :--- |
| **외부 스키마 (External)** | Người dùng cá nhân / Ứng dụng (**사용자 관점**) | Nhiều (N) | **논리적 사상 (External/Conceptual)** | **논리적 독립성 (Logical Independence)**: Khái niệm đổi, ứng dụng không đổi. |
| **개념 스키마 (Conceptual)** | Toàn bộ tổ chức / Doanh nghiệp (**통합 관점**) | 1 | | |
| **내부 스키마 (Internal)** | Lưu trữ vật lý trên đĩa cứng (**물리적 저장 관점**) | 1 | **물리적 사상 (Conceptual/Internal)** | **물리적 독립성 (Physical Independence)**: Vật lý đổi, khái niệm và ứng dụng không đổi. |

---

## 11. Hậu quả khi không duy trì tính độc lập dữ liệu

**데이터 독립성이 유지되지 않으면 데이터의 중복성과 복잡성이 증가한다.**

Nếu không duy trì tính độc lập dữ liệu thì sự trùng lặp và phức tạp của dữ liệu sẽ tăng lên.

**또한 요구사항에 대응하기 어려워지고 데이터 유지보수 비용이 급격히 증가한다.**

Ngoài ra, việc đáp ứng yêu cầu mới trở nên chậm chạp và chi phí bảo trì dữ liệu tăng vọt.

Chuỗi ảnh hưởng tiêu cực khi thiếu tính độc lập:

```
Cấu trúc lưu trữ đĩa thay đổi
→ Câu lệnh SQL buộc phải thay đổi
→ Mã nguồn chương trình ứng dụng phải viết lại
→ Tốn kém chi phí kiểm thử hồi quy toàn diện
→ Nguy cơ phát sinh lỗi tiềm ẩn cao
```

---

## 12. Cạm bẫy thi cử trọng điểm (출제 함정 & 오답 노트)

Trong kỳ thi SQLD Môn 1, các câu hỏi về nền tảng mô hình hóa dữ liệu thường giăng bẫy thí sinh ở các khía cạnh sau:

### Cạm bẫy 1: Hoán đổi thuật ngữ 3 đặc trưng mô hình hóa (추상화, 단순화, 명확화)
- **Bẫy đề thi:** Đề bài đưa ra phát biểu như: *"Mô hình hóa dữ liệu là quá trình cụ thể hóa (구체화) và phức tạp hóa (복잡화) thế giới thực nhằm phản ánh toàn diện mọi chi tiết nghiệp vụ"* hoặc *"Đặc trưng của mô hình hóa là trừu tượng hóa, đơn giản hóa và tổng quát hóa (일반화)"*.
- **Cách phá bẫy:** 3 đặc trưng duy nhất được chuẩn hóa bởi K-Data là **추상화 (Abstraction)**, **단순화 (Simplification)**, **명확화 (Clarity)**. Mọi từ ngữ khác như `구체화` (Cụ thể hóa - SAI), `복잡화` (Phức tạp hóa - SAI), `일반화` (Tổng quát hóa - SAI) đều là phương án gây nhiễu!

### Cạm bẫy 2: Nhầm lẫn giữa "Mô hình khái niệm" và "Mô hình logic"
- **Bẫy đề thi:** Khẳng định rằng *"Mô hình hóa khái niệm là giai đoạn áp dụng chuẩn hóa (Normalization) để triệt tiêu trùng lặp"* hoặc *"Mô hình hóa logic có mức độ trừu tượng cao nhất"*.
- **Cách phá bẫy:**
  - Mức độ trừu tượng cao nhất: **개념적 데이터 모델링 (Mô hình khái niệm)**.
  - Giai đoạn thực hiện Chuẩn hóa (정규화), xác định chi tiết Khóa chính (PK), Khóa ngoại (FK), Thuộc tính (Attribute): **논리적 데이터 모델링 (Mô hình logic)**.
  - Giai đoạn tính toán hiệu năng bộ nhớ đệm, Tablespace, Index vật lý: **물리적 데이터 모델링 (Mô hình vật lý)**.

### Cạm bẫy 3: Đánh đồng giữa "관계 (Relationship)" và "페어링 (Pairing)"
- **Bẫy đề thi:** Cho rằng *"Một quan hệ (Relationship) chỉ tồn tại giữa hai bản ghi (Instance) cụ thể"*.
- **Cách phá bẫy:**
  - Mối liên hệ giữa 2 bản ghi/cá thể cụ thể gọi là **페어링 (Pairing)**.
  - **관계 (Relationship)** là khái niệm tập hợp, biểu diễn tập hợp của toàn bộ các 페어링 giữa hai Thực thể (Entity Type).

### Cạm bẫy 4: Đảo chéo 2 cơ chế ánh xạ ANSI/SPARC và Tính độc lập dữ liệu
- **Bẫy đề thi:** *"Ánh xạ 외부/개념 사상 đảm bảo tính độc lập dữ liệu vật lý (물리적 독립성)"* hoặc *"Khi thay đổi cấu trúc bảng trong 개념 스키마, người dùng bên ngoài buộc phải thay đổi theo"*.
- **Cách phá bẫy:**
  - **외부/개념 사상 (Logical Mapping):** Đảm bảo **논리적 데이터 독립성 (Độc lập logic)**. Thay đổi 개념 스키마 (thêm cột, thêm bảng) thì 외부 스키마 (View của người dùng) vẫn giữ nguyên không đổi.
  - **개념/내부 사상 (Physical Mapping):** Đảm bảo **물리적 데이터 독립성 (Độc lập vật lý)**. Thay đổi 내부 스키마 (chia lại Partition, thêm Index, đổi loại đĩa SSD) thì 개념 스키마 và ứng dụng hoàn toàn không bị ảnh hưởng.

---

## 13. Câu hỏi trắc nghiệm thi thử mô phỏng (실전 기출 변형 문제 & 정답 해설)

### Câu 1 (Đặc trưng & Vấn đề cần tránh khi mô hình hóa)
**Đề bài:** Trong các phát biểu dưới đây về đặc trưng và các vấn đề cần lưu ý khi thực hiện mô hình hóa dữ liệu (데이터 모델링), phát biểu nào sau đây là **SAI**?

A. Mô hình hóa dữ liệu hướng tới 3 đặc trưng cốt lõi: trừu tượng hóa (추상화), đơn giản hóa (단순화) và làm rõ (명확화).
B. Vấn đề không linh hoạt (비유연성) xảy ra khi định nghĩa dữ liệu bị gắn chặt với quy trình xử lý, khiến mô hình phải thay đổi liên tục khi có biến động nghiệp vụ nhỏ.
C. Để nâng cao độ chính xác, mô hình hóa dữ liệu cần cụ thể hóa (구체화) tối đa tất cả các chi tiết phát sinh ngoài thế giới thực vào cơ sở dữ liệu.
D. Vấn đề không nhất quán (비일관성) phát sinh khi mối quan hệ và các ràng buộc toàn vẹn giữa các dữ liệu không được định nghĩa một cách chặt chẽ.

**Đáp án đúng:** **C**

**Giải thích chi tiết:**
- **Phương án C sai** (và là đáp án cần chọn): Bản chất của mô hình hóa là trừu tượng hóa (추상화 - loại bỏ chi tiết vụn vặt ngoài lề, chỉ giữ lại bản chất nghiệp vụ cần quản lý), chứ không phải là "cụ thể hóa" (구체화) mọi chi tiết đời thực. Đưa quá nhiều chi tiết thừa vào sẽ làm mô hình cồng kềnh, vi phạm nguyên tắc đơn giản hóa và tốn kém chi phí lưu trữ.
- **Phương án A đúng:** 3 đặc trưng chuẩn K-Data là 추상화, 단순화, 명확화.
- **Phương án B đúng:** Đây là định nghĩa chuẩn xác về tính không linh hoạt (비유연성 - Inflexibility).
- **Phương án D đúng:** Đây là định nghĩa chuẩn xác về tính không nhất quán (비일관성 - Inconsistency).

---

### Câu 2 (Ba yếu tố cấu thành & Cặp khái niệm Tập hợp vs Đơn lẻ)
**Đề bài:** Bảng nào dưới đây phân loại **CHÍNH XÁC** mối tương quan giữa khái niệm Tập hợp (복수·집합 개념) và khái niệm Cá thể (개별·단수 개념) trong 3 yếu tố cấu thành của mô hình dữ liệu?

A. Đối tượng: 엔터티 (Entity) — 속성 (Attribute)
B. Mối liên hệ: 페어링 (Pairing) — 관계 (Relationship)
C. Mối liên hệ: 관계 (Relationship) — 페어링 (Pairing)
D. Đặc tính: 속성값 (Attribute Value) — 속성 (Attribute)

**Đáp án đúng:** **C**

**Giải thích chi tiết:**
- **Phương án C đúng:** Khái niệm tập hợp (복수 개념) của yếu tố mối liên hệ là `관계 (Relationship)`, và khái niệm cá thể đơn lẻ (단수 개념) tương ứng là `페어링 (Pairing)`. Quan hệ là tập hợp của các pairing giữa các instance.
- **Phương án A sai:** Cả hai đều không biểu diễn cặp tập hợp - cá thể của Đối tượng (Đối tượng phải là 엔터티 vs 인스턴스).
- **Phương án B sai:** Bị đảo ngược thứ tự (페어링 là cá thể, 관계 mới là tập hợp).
- **Phương án D sai:** Bị đảo ngược thứ tự (속성 là tập hợp, 속성값 mới là cá thể đơn lẻ).

---

### Câu 3 (Cấp độ mô hình hóa & Chuẩn hóa dữ liệu)
**Đề bài:** Xét các phát biểu sau về 3 cấp độ mô hình hóa dữ liệu (개념적, 논리적, 물리적 모델링), phát biểu nào sau đây là **ĐÚNG**?

A. Mô hình hóa khái niệm (개념적 모델링) có mức độ trừu tượng thấp nhất vì nó phải xác định cụ thể kiểu dữ liệu vật lý của từng cột.
B. Quá trình chuẩn hóa dữ liệu (정규화 - Normalization) là hoạt động trọng tâm được thực hiện chủ yếu trong giai đoạn mô hình hóa logic (논리적 모델링).
C. Thiết lập chỉ mục (Index), phân vùng bảng (Partitioning) và cấp phát Tablespace được hoàn thiện trong giai đoạn mô hình hóa logic.
D. Mô hình hóa vật lý (물리적 모델링) hoàn toàn độc lập với hệ quản trị cơ sở dữ liệu (DBMS) được lựa chọn triển khai.

**Đáp án đúng:** **B**

**Giải thích chi tiết:**
- **Phương án B đúng:** Chuẩn hóa (정규화) là hoạt động đại diện, mang tính cốt lõi của giai đoạn mô hình hóa logic (논리적 모델링) nhằm loại bỏ trùng lặp và đảm bảo tính nhất quán dữ liệu trước khi chuyển giao xuống tầng vật lý.
- **Phương án A sai:** Mô hình hóa khái niệm có mức độ trừu tượng **cao nhất** (추상화 수준이 가장 높음), không xét đến kiểu dữ liệu vật lý.
- **Phương án C sai:** Index, Partitioning và Tablespace là các yếu tố kỹ thuật thuộc giai đoạn mô hình hóa vật lý (물리적 모델링).
- **Phương án D sai:** Mô hình hóa vật lý phụ thuộc chặt chẽ vào đặc tính của DBMS cụ thể (Oracle, SQL Server, PostgreSQL, MySQL,...).

---

### Câu 4 (Kiến trúc 3 tầng ANSI/SPARC & Tính độc lập dữ liệu)
**Đề bài:** Trong kiến trúc 3 tầng lược đồ ANSI/SPARC, cơ chế nào bảo đảm **Tính độc lập dữ liệu logic (논리적 데이터 독립성)**?

A. Ánh xạ giữa Lược đồ khái niệm và Lược đồ nội bộ (개념/내부 사상)
B. Ánh xạ giữa Lược đồ ngoài và Lược đồ khái niệm (외부/개념 사상)
C. Khả năng tự động tối ưu hóa của trình biên dịch SQL (Cost-Based Optimizer)
D. Việc phân vùng bảng vật lý (Table Partitioning) trên các ổ đĩa độc lập

**Đáp án đúng:** **B**

**Giải thích chi tiết:**
- **Phương án B đúng:** Ánh xạ ngoài/khái niệm (`외부/개념 사상` - Logical Mapping) kết nối khung nhìn người dùng (`외부 스키마`) với cấu trúc toàn cục của tổ chức (`개념 스키마`). Khi cấu trúc logic toàn cục thay đổi (thêm cột mới, mở rộng quan hệ), ta chỉ cần cập nhật ánh xạ này mà không cần sửa đổi chương trình ứng dụng hay màn hình người dùng, bảo đảm tính độc lập logic.
- **Phương án A sai:** Ánh xạ khái niệm/nội bộ (`개념/내부 사상` - Physical Mapping) bảo đảm tính độc lập dữ liệu vật lý (물리적 데이터 독립성).
- **Phương án C và D sai:** Đây là các tính năng và kỹ thuật vận hành DBMS, không phải là cơ chế ánh xạ chuẩn kiến trúc ANSI/SPARC.

---

## 14. Tóm tắt toàn bộ bài học

1. **Bản chất mô hình hóa:** Là quá trình trừu tượng hóa (**추상화**), đơn giản hóa (**단순화**) và làm rõ (**명확화**) thế giới thực thành cấu trúc cơ sở dữ liệu. Cần tránh 3 lỗi hiểm nghèo: Trùng lặp (**중복**), Không linh hoạt (**비유연성**) và Không nhất quán (**비일관성**).
2. **3 Góc nhìn (3 관점):**
   - **데이터 관점 (What):** Quản lý dữ liệu gì? Mô hình hóa đối tượng và mối liên kết (ERD).
   - **프로세스 관점 (How):** Dữ liệu được luân chuyển, xử lý theo trình tự nào? (DFD, Process Flow).
   - **상호작용 관점 (Interaction):** Quy trình xử lý tác động thay đổi dữ liệu ra sao? (CRUD Matrix).
3. **3 Yếu tố cấu thành & Cặp phạm trù đối ngẫu:**
   - Things: Thực thể (**엔터티 타입 - Class**) vs Cá thể (**인스턴스 - Occurrence**).
   - Relationships: Quan hệ tổng thể (**관계 - Relationship**) vs Ghép cặp cá thể (**페어링 - Pairing**).
   - Attributes: Thuộc tính (**속성 - Attribute**) vs Giá trị thuộc tính (**속성값 - Value**).
4. **6 Yếu tố mô hình tốt:** Hoàn thiện (**완전성**), Bỏ trùng lặp (**중복 배제**), Quy tắc nghiệp vụ (**업무 규칙**), Tái sử dụng (**데이터 재사용**), Giao tiếp thống nhất (**의사소통**), Tích hợp toàn cục (**통합성**).
5. **3 Cấp độ trừu tượng:**
   - **개념적 모델링:** Trừu tượng hóa cao nhất, trích xuất Entity cốt lõi toàn doanh nghiệp.
   - **논리적 모델링:** Chuyển sang bảng, xác định PK/FK/Attribute và thực hiện chuẩn hóa (정규화).
   - **물리적 모델링:** Gắn với DBMS cụ thể, thiết kế Index, Partitioning và cấu trúc lưu trữ.
6. **Kiến trúc 3 tầng ANSI/SPARC & 2 Cấp độ độc lập dữ liệu:**
   - `외부 스키마 (User View)` $\leftrightarrow$ [논리적 사상] $\leftrightarrow$ `개념 스키마 (Global Logic)` $\leftrightarrow$ [물리적 사상] $\leftrightarrow$ `내부 스키마 (Physical Storage)`.
   - **논리적 독립성:** 개념 thay đổi $\rightarrow$ 외부/ứng dụng không đổi.
   - **물리적 독립성:** 내부 thay đổi $\rightarrow$ 개념/외부/ứng dụng không đổi.

---

## 15. Nối mạch sang Bài 02: ERD, Entity, Thuộc tính, Quan hệ và Định danh

> **Mạch nối (Bridge):**
> - **Từ đâu (Kiến thức nền):** Bài 01 đã xác lập khung nền tảng của mô hình hóa dữ liệu: 3 đặc trưng, 3 góc nhìn (What, How, CRUD), 3 cấp độ (khái niệm, logic, vật lý), 3 yếu tố cấu thành và kiến trúc 3 tầng lược đồ ANSI/SPARC bảo đảm tính độc lập dữ liệu.
> - **Đang giải quyết gì:** Làm thế nào để phân rã các yêu cầu nghiệp vụ thực tế thành 4 thành phần trụ cột cấu thành nên một sơ đồ thực thể liên kết (ERD) hoàn chỉnh và chuẩn hóa?
> - **Dùng đi đâu:** Bàn giao trực tiếp sang [Bài 02 — ERD, Entity, Attribute, Relationship và Identifier](./02-erd-entity-attribute-relationship-identifier.md) để phân loại chi tiết Thực thể (Entity theo hình thái và thời điểm phát sinh), Thuộc tính (Attribute cơ bản, thiết kế, phái sinh), Quan hệ (Identifying vs Non-identifying) và Định danh (Natural vs Surrogate).
