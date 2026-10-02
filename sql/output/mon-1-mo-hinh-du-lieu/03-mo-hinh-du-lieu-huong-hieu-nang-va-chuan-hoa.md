# Mô hình dữ liệu hướng hiệu năng và chuẩn hóa

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Mô hình dữ liệu hướng hiệu năng và chuẩn hóa**. Route đi từ functional dependencies → normal forms → redundancy/anomalies → denormalization → index/query workload, để chuẩn hóa được cân bằng với cách truy cập.

> **Mục tiêu:** Quy trình tối ưu mô hình, phụ thuộc hàm, 1NF–5NF, BCNF và phi chuẩn hóa.

## Từ khóa cần nhớ (Keyword)

Phần giải thích dùng tiếng Việt trước. Ở mọi lần xuất hiện, thuật ngữ SQLD dùng dạng `nghĩa Việt (English / 한국어)` để vừa giữ mạch đọc vừa đối chiếu được từ khóa trong đề.

> **Chuyển mạch:** **Từ khóa cần nhớ** xác định các đối tượng dữ liệu; **Mạch tư duy** đặt chúng vào quan hệ phụ thuộc và hiệu năng, rồi **Mạch nối của bài học** dẫn tới lựa chọn mô hình cụ thể.

## Mạch tư duy (Logic học)

Hãy xác định **đối tượng dữ liệu** trước, sau đó đọc **điều kiện**, **phạm vi dòng**, **thứ tự xử lý** và cuối cùng kiểm tra **kết quả mong đợi**. Với SQL, luôn phân biệt điều kiện lọc trước nhóm (`WHERE`) với điều kiện lọc sau nhóm (`HAVING`); đây là cầu nối để hiểu vì sao cùng một truy vấn có thể cho kết quả khác nhau.

> **Chuyển mạch:** Khi đã có quan hệ và mục tiêu hiệu năng, **Mạch nối của bài học** chuyển sang **데이터 모델과 SQL** để xem mô hình được biểu diễn và truy vấn thế nào.

## Mạch nối của bài học

Bài này không đứng riêng: hãy nối **Mô hình dữ liệu hướng hiệu năng và chuẩn hóa** với bài trước bằng đối tượng dữ liệu/điều kiện mà nó tái sử dụng, rồi dùng kết quả ở phần cuối để chọn bài kế tiếp trong cùng môn. Khi gặp một truy vấn mới, nói rõ nó đang mở rộng mô hình dữ liệu, thứ tự xử lý hay cách kiểm tra kết quả nào trước khi nhớ cú pháp.

> **Cách học:** Đọc phần khái niệm → tự chạy lại các ví dụ SQL → chốt lại mục **từ khóa (Keyword)**, bảng so sánh và phần ghi nhớ cuối bài.

---

Để học **Mô hình dữ liệu hướng hiệu năng và chuẩn hóa** như một mạch suy luận, trước hết hãy giữ câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Mục đích của bài là biến **Quy trình tối ưu mô hình, phụ thuộc hàm, 1NF–5NF, BCNF và phi chuẩn hóa** thành cách đọc có thể áp dụng.

---

Ta bắt đầu **데이터 모델과 SQL** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** **데이터 모델과 SQL** nối sơ đồ với câu lệnh; **Mô hình dữ liệu và SQL** dùng cùng ví dụ để chỉ ra khi thiết kế ảnh hưởng trực tiếp đến cách đọc và tính kết quả.

## 데이터 모델과 SQL

Khi gom phần **데이터 모델과 SQL** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **데이터 모델과 SQL**. Bây giờ chuyển sang **Mô hình dữ liệu và SQL**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Mô hình dữ liệu và SQL** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Trong **Mô hình dữ liệu hướng hiệu năng và chuẩn hóa**, **데이터 모델과 SQL** nêu điều cần giải thích; **Mô hình dữ liệu và SQL** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **3. 정규화** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình dữ liệu và SQL

Khi gom phần **Mô hình dữ liệu và SQL** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Mô hình dữ liệu và SQL**. Bây giờ chuyển sang **1. 성능 데이터 모델링의 개요**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **1. 성능 데이터 모델링의 개요** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 1. 성능 데이터 모델링의 개요

Khi gom phần **1. 성능 데이터 모델링의 개요** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **1. 성능 데이터 모델링의 개요**. Bây giờ chuyển sang **1. Khái quát về mô hình hóa dữ liệu hướng hiệu năng**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **1. Khái quát về mô hình hóa dữ liệu hướng hiệu năng** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 1. Khái quát về mô hình hóa dữ liệu hướng hiệu năng

**성능 데이터 모델링은 데이터베이스의 성능을 고려하여 데이터 모델을 설계하는 것이다.**

**Mô hình hóa dữ liệu hướng hiệu năng là thiết kế mô hình dữ liệu có xem xét đến hiệu năng của cơ sở dữ liệu.**

Ảnh mô tả việc thiết kế mô hình dữ liệu liên quan đến:

- 정규화 — Normalization — Chuẩn hóa.
- 반정규화 — Denormalization — Phi chuẩn hóa.
- 테이블 통합 및 분할 — Gộp và tách bảng.
- 조인 구조 — Cấu trúc JOIN.
- PK/FK 설정 — Thiết lập PK/FK.
- 인덱스 — Index — Chỉ mục.

Khi gom phần **1. Khái quát về mô hình hóa dữ liệu hướng hiệu năng** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **1. Khái quát về mô hình hóa dữ liệu hướng hiệu năng**. Bây giờ chuyển sang **Thời điểm thực hiện**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Thời điểm thực hiện** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Thời điểm thực hiện

**성능 데이터 모델링은 분석·설계 단계에서 수행하는 것이 가장 좋다.**

**Mô hình hóa dữ liệu hướng hiệu năng nên được thực hiện ở giai đoạn phân tích và thiết kế.**

Ảnh có biểu đồ:

```
분석/설계 → 구현 → 테스트 → 운영
Phân tích/thiết kế → Triển khai → Kiểm thử → Vận hành
```

**데이터 모델의 문제는 늦게 발견할수록 수정 비용이 증가한다.**

**Càng phát hiện vấn đề của mô hình dữ liệu muộn thì chi phí sửa càng tăng.**

Nếu sửa ở giai đoạn `분석/설계`, chỉ cần sửa mô hình và thiết kế liên quan. Nếu sửa ở giai đoạn `운영`, có thể phải sửa dữ liệu, SQL, chương trình, Index và quy trình vận hành.

---

Khi gom phần **Thời điểm thực hiện** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Thời điểm thực hiện**. Bây giờ chuyển sang **2. 성능 데이터 모델링 진행 순서**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **2. 성능 데이터 모델링 진행 순서** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 2. 성능 데이터 모델링 진행 순서

Khi gom phần **2. 성능 데이터 모델링 진행 순서** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **2. 성능 데이터 모델링 진행 순서**. Bây giờ chuyển sang **2. Thứ tự thực hiện mô hình hóa dữ liệu hướng hiệu năng**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **2. Thứ tự thực hiện mô hình hóa dữ liệu hướng hiệu năng** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 2. Thứ tự thực hiện mô hình hóa dữ liệu hướng hiệu năng

Khi gom phần **2. Thứ tự thực hiện mô hình hóa dữ liệu hướng hiệu năng** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **2. Thứ tự thực hiện mô hình hóa dữ liệu hướng hiệu năng**. Bây giờ chuyển sang **1) 정규화를 정확하게 수행한다**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **1) 정규화를 정확하게 수행한다** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 1) 정규화를 정확하게 수행한다

**정규화를 정확하게 수행하여 데이터 중복과 데이터 이상을 줄인다.**

**Thực hiện chuẩn hóa chính xác để giảm dữ liệu trùng lặp và các lỗi dữ liệu.**

Khi gom phần **1) 정규화를 정확하게 수행한다** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **1) 정규화를 정확하게 수행한다**. Bây giờ chuyển sang **2) DB 용량을 산정한다**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **2) DB 용량을 산정한다** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 2) DB 용량을 산정한다

**각 엔터티에 어느 정도의 데이터와 트랜잭션이 들어오는지 파악하기 위해 DB 용량을 산정한다.**

**Cần ước tính dung lượng DB để biết mỗi Entity sẽ chứa bao nhiêu dữ liệu và tiếp nhận bao nhiêu giao dịch.**

`용량 산정` có nghĩa là dự đoán:

- Số bản ghi hiện tại.
- Số bản ghi tăng mỗi ngày.
- Dữ liệu sẽ được lưu trong bao lâu.
- Tần suất truy vấn.
- Tần suất cập nhật và xóa.

Khi gom phần **2) DB 용량을 산정한다** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **2) DB 용량을 산정한다**. Bây giờ chuyển sang **3) 트랜잭션 유형을 파악한다**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **3) 트랜잭션 유형을 파악한다** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 3) 트랜잭션 유형을 파악한다

**DB에서 발생하는 트랜잭션 유형을 파악하기 위해 CRUD 매트릭스를 활용한다.**

**Sử dụng ma trận CRUD để xác định các loại giao dịch phát sinh trong DB.**

| Ký hiệu | English | Nghĩa |
| --- | --- | --- |
| C | Create | Tạo mới |
| R | Read | Đọc, truy vấn |
| U | Update | Cập nhật |
| D | Delete | Xóa |

Ví dụ, nghiệp vụ `수강신청` có thể:

- Đọc thông tin sinh viên.
- Tạo dữ liệu đăng ký môn học.

Khi gom phần **3) 트랜잭션 유형을 파악한다** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **3) 트랜잭션 유형을 파악한다**. Bây giờ chuyển sang **4) 반정규화를 수행한다**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **4) 반정규화를 수행한다** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 4) 반정규화를 수행한다

**용량과 트랜잭션 유형을 분석한 후 필요한 경우 반정규화를 수행한다.**

**Sau khi phân tích dung lượng và loại giao dịch, nếu cần thì thực hiện phi chuẩn hóa.**

Chuẩn hóa làm giảm trùng lặp nhưng có thể làm tăng số bảng và số lần JOIN. Nếu việc đó làm truy vấn chậm, có thể cân nhắc phi chuẩn hóa.

Khi gom phần **4) 반정규화를 수행한다** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **4) 반정규화를 수행한다**. Bây giờ chuyển sang **5) 이력 모델과 인덱스를 조정한다**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **5) 이력 모델과 인덱스를 조정한다** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 5) 이력 모델과 인덱스를 조정한다

**이력 모델, 인덱스, PK/FK 순서, 슈퍼타입·서브타입 구조를 성능 관점에서 조정한다.**

**Điều chỉnh mô hình lịch sử, Index, thứ tự PK/FK và cấu trúc Supertype/Subtype theo góc nhìn hiệu năng.**

- `이력 모델`: Mô hình lưu lại lịch sử thay đổi.
- `인덱스`: Cấu trúc giúp tìm kiếm nhanh.
- `슈퍼타입`: Entity cha chứa thuộc tính chung.
- `서브타입`: Entity con chứa thuộc tính riêng.

Khi gom phần **5) 이력 모델과 인덱스를 조정한다** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **5) 이력 모델과 인덱스를 조정한다**. Bây giờ chuyển sang **6) 성능을 검증한다**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **6) 성능을 검증한다** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 6) 성능을 검증한다

**마지막으로 성능 관점에서 데이터 모델을 검증한다.**

**Cuối cùng phải kiểm tra mô hình dữ liệu từ góc nhìn hiệu năng.**

Cần kiểm tra thời gian chạy SQL, số lần JOIN, dung lượng dữ liệu và hiệu quả của Index.

---

Khi gom phần **6) 성능을 검증한다** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **6) 성능을 검증한다**. Bây giờ chuyển sang **3. 정규화**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **3. 정규화** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Ở chặng này của **Mô hình dữ liệu hướng hiệu năng và chuẩn hóa**, **Mô hình dữ liệu và SQL** nêu điều cần giải thích; **3. 정규화** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **3. Chuẩn hóa** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. 정규화

Khi gom phần **3. 정규화** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **3. 정규화**. Bây giờ chuyển sang **3. Chuẩn hóa**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **3. Chuẩn hóa** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** **3. 정규화** giới thiệu mục tiêu giảm dư thừa; **3. Chuẩn hóa** diễn đạt mục tiêu đó bằng tiếng Việt trước khi đi vào **4. 함수적 종속성**, là cơ chế kiểm chứng.

## 3. Chuẩn hóa

Khi gom phần **3. Chuẩn hóa** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **3. Chuẩn hóa**. Bây giờ chuyển sang **3.1 정규화의 정의**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **3.1 정규화의 정의** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 3.1 정규화의 정의

**정규화는 최소한의 데이터 중복과 최대한의 데이터 유연성 및 일관성을 위해 데이터를 분리하는 과정이다.**

**Chuẩn hóa là quá trình tách dữ liệu để giảm trùng lặp, tăng tính linh hoạt và bảo đảm tính nhất quán.**

Ảnh cho thấy một bảng đang chứa đồng thời:

- Thông tin môn học.
- Thông tin đăng ký môn học.
- Thông tin sinh viên.

Ví dụ:

| 과목코드 | 과목명 | 학번 | 이름 | 연락처 |
| --- | --- | --- | --- | --- |
| C01 | DB개론 | 2401 | 강감찬 | 010-1234-5678 |
| C02 | DB실무 | 2401 | 강감찬 | 010-1234-5678 |
| A01 | 마이닝 | 2402 | 홍길동 | 010-6363-8282 |
| B01 | 통계 | 2401 | 강감찬 | 010-1234-5678 |
| C01 | DB개론 | 2403 | 이춘향 | 010-9876-5432 |

Tên và số điện thoại của sinh viên `2401` bị lặp lại ở nhiều dòng.

---

Khi gom phần **3.1 정규화의 정의** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **3.1 정규화의 정의**. Bây giờ chuyển sang **3.2 데이터 이상**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **3.2 데이터 이상** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 3.2 데이터 이상

Khi gom phần **3.2 데이터 이상** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **3.2 데이터 이상**. Bây giờ chuyển sang **삭제 이상**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **삭제 이상** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 삭제 이상

**삭제 이상은 원하는 정보만 삭제하려고 했는데 다른 정보까지 삭제되는 현상이다.**

**Lỗi xóa là hiện tượng muốn xóa một thông tin nhưng thông tin khác cũng bị xóa theo.**

Nếu sinh viên `2402` xóa đăng ký môn `A01`, và không còn sinh viên nào học `A01`, thông tin môn học `A01` cũng có thể bị mất.

Khi gom phần **삭제 이상** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **삭제 이상**. Bây giờ chuyển sang **삽입 이상**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **삽입 이상** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 삽입 이상

**삽입 이상은 관련된 다른 정보가 없어서 원하는 정보를 입력할 수 없는 현상이다.**

**Lỗi chèn là hiện tượng không thể thêm thông tin mong muốn vì thông tin liên quan khác chưa tồn tại.**

Nếu sinh viên mới `2404` chưa học môn nào, bảng cũ có thể không cho phép thêm riêng thông tin sinh viên vì khóa cần cả thông tin môn học và đăng ký học.

Khi gom phần **삽입 이상** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **삽입 이상**. Bây giờ chuyển sang **갱신 이상**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **갱신 이상** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 갱신 이상

**갱신 이상은 하나의 정보를 변경하기 위해 여러 행을 수정해야 하는 현상이다.**

**Lỗi cập nhật là hiện tượng phải sửa nhiều dòng để thay đổi một thông tin.**

Nếu Kang Gam-chan đổi số điện thoại, phải sửa tất cả dòng có tên Kang Gam-chan. Nếu bỏ sót một dòng, dữ liệu sẽ không nhất quán.

---

Khi gom phần **갱신 이상** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **갱신 이상**. Bây giờ chuyển sang **4. 함수적 종속성**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **4. 함수적 종속성** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Từ mục tiêu chuẩn hóa, **4. 함수적 종속성** chỉ ra thuộc tính nào quyết định thuộc tính nào; **4. Phụ thuộc hàm** chốt cách đọc quan hệ đó bằng ví dụ.

## 4. 함수적 종속성

Khi gom phần **4. 함수적 종속성** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **4. 함수적 종속성**. Bây giờ chuyển sang **4. Phụ thuộc hàm**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **4. Phụ thuộc hàm** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Khi đã xác định phụ thuộc hàm, **5. 정규화 절차** dùng nó để tách quan hệ theo từng bước; trọng tâm chuyển từ nhận diện sang thao tác.

## 4. Phụ thuộc hàm

Khi gom phần **4. Phụ thuộc hàm** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **4. Phụ thuộc hàm**. Bây giờ chuyển sang **4.1 Khái niệm**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **4.1 Khái niệm** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 4.1 Khái niệm

**함수적 종속성은 한 속성의 값이 다른 속성의 값을 결정하는 관계이다.**

**Phụ thuộc hàm là quan hệ trong đó giá trị của một thuộc tính quyết định giá trị của thuộc tính khác.**

Ký hiệu:

```
X → Y
```

- `X`: 결정자 — Determinant — Thuộc tính quyết định.
- `Y`: 종속자 — Dependent Attribute — Thuộc tính phụ thuộc.

**X의 값 하나에 대응되는 Y의 값은 하나만 존재해야 한다.**

**Một giá trị X phải chỉ tương ứng với một giá trị Y duy nhất.**

Ví dụ:

```
학번 → 학생명
Mã sinh viên → Tên sinh viên
```

Một mã sinh viên chỉ xác định một tên sinh viên.

---

Khi gom phần **4.1 Khái niệm** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **4.1 Khái niệm**. Bây giờ chuyển sang **4.2 Ví dụ 학번 và 혈액형**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **4.2 Ví dụ 학번 và 혈액형** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 4.2 Ví dụ 학번 và 혈액형

**학번이 혈액형을 결정한다고 가정하면 학번 → 혈액형이다.**

**Nếu giả định mã sinh viên quyết định nhóm máu thì có 학번 → 혈액형.**

Ví dụ:

```
2401 → A형
```

**혈액형 → 학번은 성립하지 않는다.**

**혈액형 → 학번 không tồn tại.**

Một nhóm máu có thể thuộc về nhiều sinh viên nên không thể dùng nhóm máu để xác định duy nhất mã sinh viên.

---

Khi gom phần **4.2 Ví dụ 학번 và 혈액형** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **4.2 Ví dụ 학번 và 혈액형**. Bây giờ chuyển sang **5. 정규화 절차**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **5. 정규화 절차** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** **5. Quy trình chuẩn hóa** diễn giải chuỗi tách quan hệ bằng tiêu chí 1NF–5NF; phần kế tiếp áp dụng từng tiêu chí vào một dạng chuẩn cụ thể.

## 5. 정규화 절차

Khi gom phần **5. 정규화 절차** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **5. 정규화 절차**. Bây giờ chuyển sang **5. Quy trình chuẩn hóa**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **5. Quy trình chuẩn hóa** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Trong **Mô hình dữ liệu hướng hiệu năng và chuẩn hóa**, **5. 정규화 절차** xác định đầu vào; **5. Quy trình chuẩn hóa** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **6. 제1정규형 — 1NF** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Quy trình chuẩn hóa

Thứ tự trong ảnh:

```
비정규형 → 1NF → 2NF → 3NF → BCNF → 4NF → 5NF
```

Cách nhớ:

```
원 · 부 · 이 · 결 · 다 · 조
```

| Nhớ | Nội dung |
| --- | --- |
| 원 | 원자성 — Tính nguyên tử |
| 부 | 부분 함수 종속 제거 — Loại bỏ phụ thuộc bộ phận |
| 이 | 이행 함수 종속 제거 — Loại bỏ phụ thuộc bắc cầu |
| 결 | 결정자는 후보키 — Determinant phải là Candidate Key |
| 다 | 다치 종속 제거 — Loại bỏ phụ thuộc đa trị |
| 조 | 조인 종속 제거 — Loại bỏ phụ thuộc JOIN |

**이전 정규형을 만족해야 다음 정규형으로 진행할 수 있다.**

**Phải đạt dạng chuẩn trước thì mới có thể tiến hành dạng chuẩn tiếp theo.**

---

Khi gom phần **5. Quy trình chuẩn hóa** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **5. Quy trình chuẩn hóa**. Bây giờ chuyển sang **6. 제1정규형 — 1NF**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **6. 제1정규형 — 1NF** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Ở chặng này của **Mô hình dữ liệu hướng hiệu năng và chuẩn hóa**, **5. Quy trình chuẩn hóa** xác định đầu vào; **6. 제1정규형 — 1NF** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **6. Dạng chuẩn 1 — 1NF** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. 제1정규형 — 1NF

Khi gom phần **6. 제1정규형 — 1NF** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **6. 제1정규형 — 1NF**. Bây giờ chuyển sang **6. Dạng chuẩn 1 — 1NF**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **6. Dạng chuẩn 1 — 1NF** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** **6. 제1정규형 — 1NF** yêu cầu giá trị nguyên tử; **6. Dạng chuẩn 1 — 1NF** chốt điều kiện đó trước khi **7. 제2정규형 — 2NF** xử lý phụ thuộc từng phần.

## 6. Dạng chuẩn 1 — 1NF

**제1정규형은 모든 속성이 원자값을 가져야 한다.**

**1NF yêu cầu mọi thuộc tính phải chứa giá trị nguyên tử.**

Một ô không được chứa nhiều giá trị.

Sai:

| 학번 | 전화번호 |
| --- | --- |
| 2401 | 010-1111-1111, 010-2222-2222 |

Đúng hơn là tách thành nhiều dòng hoặc một bảng riêng.

**1NF는 반복되는 그룹과 여러 값을 한 칸에 저장하는 문제를 제거한다.**

**1NF loại bỏ nhóm lặp và việc lưu nhiều giá trị trong một ô.**

---

Khi gom phần **6. Dạng chuẩn 1 — 1NF** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **6. Dạng chuẩn 1 — 1NF**. Bây giờ chuyển sang **7. 제2정규형 — 2NF**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **7. 제2정규형 — 2NF** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Sau khi dữ liệu đã nguyên tử ở 1NF, **7. 제2정규형 — 2NF** kiểm tra khóa ghép và phụ thuộc từng phần; **7. Dạng chuẩn 2 — 2NF** diễn giải hệ quả khi tách bảng.

## 7. 제2정규형 — 2NF

Khi gom phần **7. 제2정규형 — 2NF** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **7. 제2정규형 — 2NF**. Bây giờ chuyển sang **7. Dạng chuẩn 2 — 2NF**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **7. Dạng chuẩn 2 — 2NF** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Khi phụ thuộc từng phần đã được loại bỏ, **8. 제3정규형 — 3NF** chuyển sang kiểm tra phụ thuộc bắc cầu; chuỗi chuẩn hóa vì vậy đi từ khóa ghép sang thuộc tính không khóa.

## 7. Dạng chuẩn 2 — 2NF

**제2정규형은 1NF를 만족하고 부분 함수 종속을 제거한 상태이다.**

**2NF là trạng thái đạt 1NF và loại bỏ phụ thuộc hàm bộ phận.**

Bảng trong ảnh:

```
학번(PK), 과목코드(PK), 평점, 과목명, 학생명, 소속학과코드, 학과명
```

Khóa chính ghép:

```
(학번, 과목코드)
```

Các phụ thuộc:

```
(학번, 과목코드) → 평점
학번 → 학생명
과목코드 → 과목명
```

`평점` phụ thuộc vào toàn bộ khóa ghép.

`학생명` chỉ phụ thuộc vào `학번`.

`과목명` chỉ phụ thuộc vào `과목코드`.

**복합 PK의 일부만으로 일반 속성이 결정되면 부분 함수 종속이다.**

**Nếu một thuộc tính thường chỉ bị quyết định bởi một phần của khóa ghép thì đó là phụ thuộc hàm bộ phận.**

Tách thành:

```
과목(과목코드 PK, 과목명)
수강(학번 PK, 과목코드 PK, 평점)
학생(학번 PK, 학생명, 소속학과코드, 학과명)
```

---

Khi gom phần **7. Dạng chuẩn 2 — 2NF** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **7. Dạng chuẩn 2 — 2NF**. Bây giờ chuyển sang **8. 제3정규형 — 3NF**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **8. 제3정규형 — 3NF** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** **8. 제3정규형 — 3NF** đặt điều kiện không có phụ thuộc bắc cầu; **8. Dạng chuẩn 3 — 3NF** minh họa cách tách thuộc tính trung gian mà vẫn giữ liên kết.

## 8. 제3정규형 — 3NF

Khi gom phần **8. 제3정규형 — 3NF** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **8. 제3정규형 — 3NF**. Bây giờ chuyển sang **8. Dạng chuẩn 3 — 3NF**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **8. Dạng chuẩn 3 — 3NF** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Sau 3NF, **9. 정규화의 성능** đặt câu hỏi ngược về chi phí JOIN, I/O và truy vấn; chuẩn hóa đúng không đồng nghĩa luôn nhanh hơn.

## 8. Dạng chuẩn 3 — 3NF

**제3정규형은 2NF를 만족하고 이행 함수 종속을 제거한 상태이다.**

**3NF là trạng thái đạt 2NF và loại bỏ phụ thuộc hàm bắc cầu.**

Ảnh biểu diễn:

```
학번 → 소속학과코드
소속학과코드 → 학과명
따라서 학번 → 학과명
```

`학번` không trực tiếp quyết định `학과명`; nó quyết định `소속학과코드`, rồi `소속학과코드` quyết định `학과명`.

**일반 속성이 다른 일반 속성을 결정하면 이행 함수 종속이다.**

**Nếu một thuộc tính thường quyết định một thuộc tính thường khác thì đó là phụ thuộc hàm bắc cầu.**

Tách thành:

```
학생(학번 PK, 학생명, 소속학과코드 FK)
학과(소속학과코드 PK, 학과명)
```

---

Khi gom phần **8. Dạng chuẩn 3 — 3NF** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **8. Dạng chuẩn 3 — 3NF**. Bây giờ chuyển sang **9. 정규화의 성능**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **9. 정규화의 성능** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** **9. Hiệu năng của chuẩn hóa** chuyển các trade-off của 3NF thành tiêu chí đo; từ đó có thể cân nhắc bước chuẩn hóa cao hơn thay vì áp dụng máy móc.

## 9. 정규화의 성능

Khi gom phần **9. 정규화의 성능** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **9. 정규화의 성능**. Bây giờ chuyển sang **9. Hiệu năng của chuẩn hóa**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **9. Hiệu năng của chuẩn hóa** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Khi hiệu năng và dư thừa đã được cân bằng, **10. BCNF** kiểm tra chặt hơn vai trò của mọi determinant; đây là bước mở rộng điều kiện 3NF.

## 9. Hiệu năng của chuẩn hóa

**정규화는 데이터 중복을 줄이고 저장 용량을 줄일 수 있다.**

**Chuẩn hóa có thể giảm dữ liệu trùng lặp và dung lượng lưu trữ.**

**정규화는 데이터 입력·수정·삭제 시 변경 범위를 줄여 성능을 향상시킬 수 있다.**

**Chuẩn hóa có thể cải thiện hiệu năng bằng cách giảm phạm vi thay đổi khi thêm, sửa và xóa dữ liệu.**

Tuy nhiên:

**조회에서는 여러 테이블을 JOIN해야 하므로 성능이 저하될 수 있다.**

**Khi truy vấn, hiệu năng có thể giảm vì phải JOIN nhiều bảng.**

Ảnh đưa ra ví dụ:

- Trước chuẩn hóa: một bảng, khoảng 1천만 건.
- Sau chuẩn hóa: bảng học sinh khoảng 4천 건, bảng đăng ký khoảng 1천만 건.

Khi đổi năm học của một sinh viên:

- Trước chuẩn hóa: phải sửa nhiều dòng đăng ký.
- Sau chuẩn hóa: chỉ sửa một dòng trong bảng sinh viên.

Khi truy vấn `학번, 학생명, 과목명, 평점`:

- Trước chuẩn hóa: truy vấn trong một bảng.
- Sau chuẩn hóa: cần JOIN, có thể giảm hiệu năng một phần.

---

Khi gom phần **9. Hiệu năng của chuẩn hóa** lại, ta không cần nhớ các dòng như những mảnh rời: ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **9. Hiệu năng của chuẩn hóa**. Bây giờ chuyển sang **10. BCNF**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **10. BCNF** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** **10. BCNF** nêu điều kiện trên determinant; **10. Dạng chuẩn BCNF** dùng ví dụ để chỉ ra quan hệ có thể đạt 3NF nhưng vẫn còn dư thừa.

## 10. BCNF

Khi gom phần **10. BCNF** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **10. BCNF**. Bây giờ chuyển sang **10. Dạng chuẩn BCNF**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **10. Dạng chuẩn BCNF** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Sau BCNF, **11. 제4정규형 — 4NF** mở rộng phân tích sang phụ thuộc đa trị; câu hỏi không còn chỉ là một determinant quyết định một thuộc tính.

## 10. Dạng chuẩn BCNF

**BCNF는 3NF의 강화 버전이며 모든 결정자가 후보키여야 한다.**

**BCNF là phiên bản mạnh hơn của 3NF và yêu cầu mọi Determinant phải là Candidate Key.**

Cách nhớ:

```
BCNF = 결정자는 반드시 후보키
BCNF = Determinant bắt buộc phải là Candidate Key
```

Ảnh có bảng:

```
학생번호(PK), 과목명(PK), 지도교수
```

Giả định:

```
(학생번호, 과목명) → 지도교수
지도교수 → 과목명
```

`지도교수` quyết định `과목명`, nhưng `지도교수` không phải Candidate Key trong bảng ban đầu.

**후보키가 아닌 속성이 다른 속성을 결정하면 BCNF를 만족하지 못할 수 있다.**

**Nếu một thuộc tính không phải Candidate Key quyết định thuộc tính khác thì bảng có thể không đạt BCNF.**

Tách thành:

```
학생-지도교수(학생번호, 지도교수)
지도교수-과목(지도교수, 과목명)
```

---

Khi gom phần **10. Dạng chuẩn BCNF** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **10. Dạng chuẩn BCNF**. Bây giờ chuyển sang **11. 제4정규형 — 4NF**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **11. 제4정규형 — 4NF** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** **11. 제4정규형 — 4NF** tách các nhóm giá trị độc lập; **11. Dạng chuẩn 4 — 4NF** cho thấy vì sao gộp chúng trong một bảng tạo tích Descartes ngoài ý muốn.

## 11. 제4정규형 — 4NF

Khi gom phần **11. 제4정규형 — 4NF** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **11. 제4정규형 — 4NF**. Bây giờ chuyển sang **11. Dạng chuẩn 4 — 4NF**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **11. Dạng chuẩn 4 — 4NF** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Khi phụ thuộc đa trị đã được tách, **12. 제5정규형 — 5NF** kiểm tra phụ thuộc kết nối và khả năng phân rã không mất thông tin.

## 11. Dạng chuẩn 4 — 4NF

**제4정규형은 BCNF를 만족하면서 다치 종속을 제거한 상태이다.**

**4NF là trạng thái đạt BCNF và loại bỏ phụ thuộc đa trị.**

Ảnh có bảng:

```
학생번호(PK), 과목명(PK), 취미
```

Một sinh viên có:

- Nhiều môn học.
- Nhiều sở thích.
- Môn học và sở thích độc lập với nhau.

Ví dụ:

| 학생번호 | 과목명 | 취미 |
| --- | --- | --- |
| 2401 | DB개론 | 그림 |
| 2401 | DB개론 | 게임 |
| 2401 | DB실무 | 그림 |
| 2401 | DB실무 | 게임 |

**학생번호에 대해 과목명과 취미가 서로 독립적으로 여러 개 존재하면 다치 종속이다.**

**Nếu với một mã sinh viên có nhiều môn học và nhiều sở thích độc lập với nhau thì đó là phụ thuộc đa trị.**

Ký hiệu:

```
학생번호 →→ 과목명
학생번호 →→ 취미
```

Tách thành:

```
학생-과목(학생번호, 과목명)
학생-취미(학생번호, 취미)
```

---

Khi gom phần **11. Dạng chuẩn 4 — 4NF** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **11. Dạng chuẩn 4 — 4NF**. Bây giờ chuyển sang **12. 제5정규형 — 5NF**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **12. 제5정규형 — 5NF** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** **12. Dạng chuẩn 5 — 5NF** dùng join dependency để kiểm tra phân rã cuối; chỉ nên áp dụng khi lợi ích toàn vẹn lớn hơn độ phức tạp truy vấn.

## 12. 제5정규형 — 5NF

Khi gom phần **12. 제5정규형 — 5NF** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **12. 제5정규형 — 5NF**. Bây giờ chuyển sang **12. Dạng chuẩn 5 — 5NF**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **12. Dạng chuẩn 5 — 5NF** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Sau 5NF, **13. 반정규화** đặt câu hỏi thực dụng: khi nào nên giữ dư thừa có kiểm soát để giảm JOIN và đáp ứng workload.

## 12. Dạng chuẩn 5 — 5NF

**제5정규형은 4NF를 만족하고 조인 종속을 제거한 상태이다.**

**5NF là trạng thái đạt 4NF và loại bỏ phụ thuộc JOIN.**

**5NF는 Project Join Normal Form 또는 PJ/NF라고 한다.**

**5NF còn được gọi là Project Join Normal Form hoặc PJ/NF.**

Ảnh mô tả:

```
A를 B와 C로 분해
B와 C를 JOIN
다시 A가 됨
```

Nghĩa là:

```
A tách thành B và C
B JOIN với C
Khôi phục lại A
```

**분해한 테이블을 다시 JOIN했을 때 원래 관계가 정확하게 복원되어야 한다.**

**Khi JOIN lại các bảng đã tách, quan hệ ban đầu phải được khôi phục chính xác.**

5NF hiếm khi được áp dụng trong thiết kế DB thông thường.

---

Khi gom phần **12. Dạng chuẩn 5 — 5NF** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **12. Dạng chuẩn 5 — 5NF**. Bây giờ chuyển sang **13. 반정규화**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **13. 반정규화** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** **13. 반정규화** mô tả quyết định đánh đổi; **13. Phi chuẩn hóa** chốt cách ghi rõ lý do, invariant và cơ chế đồng bộ khi cố ý lặp dữ liệu.

## 13. 반정규화

Khi gom phần **13. 반정규화** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **13. 반정규화**. Bây giờ chuyển sang **13. Phi chuẩn hóa**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **13. Phi chuẩn hóa** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Khi đã nêu rõ điều kiện và rủi ro của phi chuẩn hóa, **KẾT LUẬN GHI NHỚ CUỐI BÀI** gom chuỗi quyết định từ phụ thuộc hàm đến trade-off hiệu năng.

## 13. Phi chuẩn hóa

**반정규화는 성능 향상을 위해 데이터 중복을 허용하고 JOIN을 줄이는 방법이다.**

**Phi chuẩn hóa là phương pháp cho phép trùng lặp dữ liệu và giảm JOIN để cải thiện hiệu năng.**

**반정규화는 비정규화와 같지 않고 정규화된 모델을 성능 목적에 맞게 조정하는 것이다.**

**Phi chuẩn hóa không giống với không chuẩn hóa; đó là việc điều chỉnh mô hình đã chuẩn hóa vì mục tiêu hiệu năng.**

Khi gom phần **13. Phi chuẩn hóa** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **13. Phi chuẩn hóa**. Bây giờ chuyển sang **Khi thực hiện**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Khi thực hiện** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### Khi thực hiện

**정규화로 엔터티와 관계가 많아져 JOIN 성능 저하가 예상될 때 반정규화를 수행할 수 있다.**

**Có thể phi chuẩn hóa khi việc chuẩn hóa làm tăng Entity và quan hệ, dẫn đến dự đoán hiệu năng JOIN giảm.**

**대량의 범위를 자주 처리하거나 특정 범위의 데이터만 자주 처리할 때 반정규화를 고려할 수 있다.**

**Có thể cân nhắc phi chuẩn hóa khi thường xuyên xử lý lượng dữ liệu lớn hoặc một phạm vi dữ liệu cụ thể.**

**요약이나 집계 정보가 자주 필요할 때 반정규화를 고려할 수 있다.**

**Có thể cân nhắc phi chuẩn hóa khi thường xuyên cần dữ liệu tổng hợp hoặc thống kê.**

Khi gom phần **Khi thực hiện** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Khi thực hiện**. Bây giờ chuyển sang **Nhược điểm**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Nhược điểm** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### Nhược điểm

**반정규화는 조회 속도를 높일 수 있지만 입력·수정·삭제 성능을 저하시킬 수 있다.**

**Phi chuẩn hóa có thể tăng tốc truy vấn nhưng có thể làm giảm hiệu năng thêm, sửa và xóa dữ liệu.**

**반정규화는 조회 성능 향상을 항상 보장하지 않는다.**

**Phi chuẩn hóa không phải lúc nào cũng bảo đảm cải thiện hiệu năng truy vấn.**

---

Khi gom phần **Nhược điểm** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Nhược điểm**. Bây giờ chuyển sang **KẾT LUẬN GHI NHỚ CUỐI BÀI**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **KẾT LUẬN GHI NHỚ CUỐI BÀI** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Kết luận cuối trả lại tiêu chí ban đầu: chọn mức chuẩn hóa dựa trên phụ thuộc, toàn vẹn và workload cụ thể, rồi mang tiêu chí đó sang bài thiết kế kế tiếp.

## KẾT LUẬN GHI NHỚ CUỐI BÀI

Khi gom phần **KẾT LUẬN GHI NHỚ CUỐI BÀI** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **KẾT LUẬN GHI NHỚ CUỐI BÀI**. Bây giờ chuyển sang **Chuỗi ghi nhớ**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Chuỗi ghi nhớ** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### Chuỗi ghi nhớ

Phần này nối mạch SQL với “Chuỗi ghi nhớ”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```
원 → 부 → 이 → 결 → 다 → 조
```

**원자값 → 부분 함수 종속 제거 → 이행 함수 종속 제거 → 결정자는 후보키 → 다치 종속 제거 → 조인 종속 제거**

**Giá trị nguyên tử → loại bỏ phụ thuộc bộ phận → loại bỏ phụ thuộc bắc cầu → Determinant là Candidate Key → loại bỏ phụ thuộc đa trị → loại bỏ phụ thuộc JOIN.**

Khi gom phần **Chuỗi ghi nhớ** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Chuỗi ghi nhớ**. Bây giờ chuyển sang **Các dạng chuẩn**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Các dạng chuẩn** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### Các dạng chuẩn

Phần này nối mạch SQL với “Các dạng chuẩn”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```
1NF = 원자값
2NF = 부분 함수 종속 제거
3NF = 이행 함수 종속 제거
BCNF = 결정자는 후보키
4NF = 다치 종속 제거
5NF = 조인 종속 제거
```

Khi gom phần **Các dạng chuẩn** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Các dạng chuẩn**. Bây giờ chuyển sang **Câu tổng kết tiếng Hàn**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Câu tổng kết tiếng Hàn** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### Câu tổng kết tiếng Hàn

**정규화는 데이터 중복과 입력·수정·삭제 이상을 줄이기 위해 함수적 종속성을 기준으로 테이블을 분리하는 과정이며, 반정규화는 정규화 이후 JOIN 증가로 성능 문제가 발생할 때 제한적으로 수행한다.**

**Chuẩn hóa là quá trình tách bảng dựa trên phụ thuộc hàm để giảm trùng lặp và các lỗi chèn, cập nhật, xóa; phi chuẩn hóa chỉ được thực hiện có giới hạn khi JOIN tăng sau chuẩn hóa gây ra vấn đề hiệu năng.**

Khi gom phần **Câu tổng kết tiếng Hàn** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Như vậy, **Câu tổng kết tiếng Hàn** đã được đặt trong quan hệ giữa đầu vào, quy tắc xử lý và kết quả. Khi ôn lại, hãy tự diễn đạt ranh giới của nó rồi dùng ranh giới đó làm điểm nối sang bài tiếp theo.

> **Bàn giao:** Sau **KẾT LUẬN GHI NHỚ CUỐI BÀI**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
