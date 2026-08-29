# Nền tảng mô hình hóa dữ liệu

> **Mục tiêu:** Khái niệm, mục tiêu, đặc điểm, góc nhìn, ba cấp độ và tính độc lập dữ liệu.

## Từ khóa cần nhớ (Keyword)

Các thuật ngữ SQLD được giữ nguyên tiếng Hàn/English trong phần nguồn. Khi ghi chú, dùng mẫu `용어 (English) (Tiếng Việt)` để nối tên gọi trong đề với ý nghĩa thực tế.

## Mạch tư duy (Logic học)

Hãy xác định **đối tượng dữ liệu** trước, sau đó đọc **điều kiện**, **phạm vi dòng**, **thứ tự xử lý** và cuối cùng kiểm tra **kết quả mong đợi**. Với SQL, luôn phân biệt điều kiện lọc trước nhóm (`WHERE`) với điều kiện lọc sau nhóm (`HAVING`).

> **Cách học:** Đọc phần khái niệm → tự chạy lại các ví dụ SQL → chốt lại các mục `Keyword`, bảng so sánh và phần ghi nhớ cuối bài.

---

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

## 9. Tính độc lập của dữ liệu

**데이터 독립성이란 데이터 구조가 변경되어도 응용 프로그램이 반드시 변경될 필요가 없는 성질이다.**

Tính độc lập dữ liệu là đặc tính trong đó chương trình ứng dụng không nhất thiết phải thay đổi khi cấu trúc dữ liệu thay đổi.

#### Keyword: 데이터 독립성

**데이터 독립성은 데이터베이스의 한 계층이 변경되어도 다른 계층에 미치는 영향을 최소화하는 개념이다.**

Tính độc lập dữ liệu là khái niệm giảm thiểu ảnh hưởng giữa các tầng khi một tầng của database thay đổi.

---

### 9.1. 물리적 독립성 - Độc lập dữ liệu vật lý

**물리적 독립성은 저장 구조나 접근 방법이 변경되어도 논리적 스키마와 응용 프로그램이 영향을 받지 않는 것이다.**

Độc lập dữ liệu vật lý là khi cấu trúc lưu trữ hoặc phương thức truy cập thay đổi nhưng schema logic và chương trình ứng dụng không bị ảnh hưởng.

Ví dụ:

- Thêm Index.
- Thay đổi Index.
- Di chuyển Tablespace.
- Partition bảng.
- Thay đổi vị trí lưu trữ.

Ứng dụng vẫn dùng:

```sql
SELECT *
FROM CUSTOMER;
```

#### Keyword: 물리적 독립성

```
Thay đổi cách lưu trên đĩa
→ Không cần thay đổi ứng dụng
```

---

### 9.2. 논리적 독립성 - Độc lập dữ liệu logic

**논리적 독립성은 논리적 스키마가 변경되어도 외부 스키마와 응용 프로그램에 미치는 영향을 최소화하는 것이다.**

Độc lập dữ liệu logic là giảm thiểu ảnh hưởng đến schema bên ngoài và chương trình ứng dụng khi schema logic thay đổi.

Ví dụ thêm một cột:

```
CUSTOMER
- CUSTOMER_ID
- CUSTOMER_NAME
- EMAIL
```

Câu SQL cũ vẫn có thể chạy:

```sql
SELECT CUSTOMER_ID, CUSTOMER_NAME
FROM CUSTOMER;
```

Nhưng nếu đổi tên cột:

```
CUSTOMER_NAME → NAME
```

thì ứng dụng có thể lỗi nếu đang dùng `CUSTOMER_NAME`.

Có thể dùng View để duy trì giao diện cũ:

```sql
CREATE VIEW CUSTOMER_VIEW AS
SELECT CUSTOMER_ID,
       NAME AS CUSTOMER_NAME
FROM CUSTOMER;
```

#### Keyword: 논리적 독립성

```
Thay đổi cấu trúc logic
→ Hạn chế ảnh hưởng đến ứng dụng
```

---

## 10. Nếu không duy trì tính độc lập dữ liệu

**데이터 독립성이 유지되지 않으면 데이터의 중복성과 복잡성이 증가한다.**

Nếu không duy trì tính độc lập dữ liệu thì sự trùng lặp và phức tạp của dữ liệu sẽ tăng lên.

**또한 요구사항에 대응하기 어려워지고 데이터 유지보수 비용이 증가한다.**

Ngoài ra, việc đáp ứng yêu cầu trở nên khó khăn và chi phí bảo trì dữ liệu tăng lên.

#### Keyword: 유지보수 비용

**유지보수 비용은 데이터 구조나 프로그램을 변경하고 테스트하며 관리하는 데 필요한 비용이다.**

Chi phí bảo trì là chi phí cần thiết để thay đổi, kiểm thử và quản lý cấu trúc dữ liệu hoặc chương trình.

Chuỗi ảnh hưởng:

```
Cấu trúc dữ liệu thay đổi
→ SQL thay đổi
→ Code thay đổi
→ Kiểm thử lại
→ Triển khai lại
→ Có thể phát sinh lỗi
```

---

## 11. Tóm tắt toàn bộ hai trang

**데이터 모델링은 현실 세계의 업무를 데이터베이스 구조로 변환하는 과정이다.**

Mô hình hóa dữ liệu là quá trình chuyển nghiệp vụ trong thế giới thực thành cấu trúc database.

**이를 위해 현실 세계를 추상화하고 단순화하며 명확하게 표현한다.**

Để làm điều đó, ta trừu tượng hóa, đơn giản hóa và làm rõ thế giới thực.

**데이터 모델링은 데이터, 프로세스, 상호작용의 세 가지 관점에서 분석할 수 있다.**

Mô hình hóa dữ liệu có thể được phân tích theo ba góc nhìn: dữ liệu, quy trình và tương tác.

**데이터 모델링은 개념적, 논리적, 물리적 모델링의 3단계로 진행된다.**

Mô hình hóa dữ liệu được tiến hành qua ba giai đoạn: khái niệm, logic và vật lý.

**좋은 데이터 모델은 중복, 비유연성, 비일관성을 줄이고 데이터 품질과 데이터 독립성을 유지한다.**

Một mô hình dữ liệu tốt làm giảm trùng lặp, không linh hoạt và không nhất quán, đồng thời duy trì chất lượng và tính độc lập dữ liệu.

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
