## SQL Style Guide là gì?

Một câu SQL có thể chạy đúng nhưng vẫn khó đọc, khó review và khó sửa. Trong pipeline dữ liệu, query thường trở thành một model được chạy lại nhiều lần, được nối với các model khác và được người khác tiếp quản sau vài tháng. Vì vậy style không chỉ là chuyện trình bày: nó là một phần của khả năng đọc, kiểm thử và bảo trì SQL.

SQL Style Guide của Simon Holywell là một bộ quy ước ngắn, có tính định hướng và tương thích với nhiều ý tưởng trong *SQL Programming Style* của Joe Celko. Tác giả nói rõ đây là một guide, không phải luật: có thể dùng nguyên bản, fork để sửa, hoặc lấy nó làm điểm xuất phát cho quy ước riêng. Bất biến quan trọng nhất là chọn một style rồi áp dụng nhất quán trong cùng repository.

## Cách đọc nguồn và phạm vi áp dụng

Bản gốc có [bản tiếng Anh](https://www.sqlstyle.guide/) và [bản dịch tiếng Việt](https://www.sqlstyle.guide/vn/). Tài liệu được phát hành theo giấy phép **Creative Commons Attribution-ShareAlike 4.0 International**; nếu sao chép hoặc sửa thành quy ước của project, cần giữ attribution và điều kiện chia sẻ tương tự. Nguồn cũng cung cấp Markdown để đặt vào repository, nhưng khi đưa vào project thật nên ghi rõ phần nào là quy ước upstream, phần nào là quyết định riêng của team.

Đọc guide theo ba lớp: (1) tên và schema để người đọc đoán đúng ý nghĩa dữ liệu, (2) hình thức query để mắt quét được cấu trúc, và (3) lựa chọn cú pháp để giảm phụ thuộc vendor. Ba lớp này hỗ trợ nhau nhưng không thay thế nhau: query được căn lề đẹp vẫn có thể sai grain, sai `JOIN` hoặc sai xử lý `NULL`.

## Đặt tên: ưu tiên ngữ nghĩa ổn định

Tên tốt giúp người đọc suy ra vai trò của đối tượng trước khi phải mở schema. Quy tắc chung là dùng tên mô tả, duy nhất, bắt đầu bằng chữ cái, chỉ dùng chữ cái/số/gạch dưới, không kết thúc bằng gạch dưới, không có nhiều gạch dưới liên tiếp và không trùng reserved keyword. Dùng `snake_case` thay cho `camelCase`, tránh tiền tố kiểu Hungarian như `tbl_` hoặc `sp_`, và chỉ viết tắt khi đó là viết tắt phổ biến trong domain.

Giới hạn 30 **bytes** là quy ước của guide; với bộ ký tự một byte thường tương đương 30 ký tự, nhưng không nên áp dụng máy móc cho mọi engine hiện đại. Giới hạn thực tế còn phụ thuộc database, migration tool và encoding của project. Nếu engine cho phép tên dài hơn, team có thể chọn quy tắc riêng nhưng phải ghi lại để linter và code review dùng cùng một chuẩn.

Đối với bảng, guide ưu tiên danh từ tập hợp tự nhiên như `staff`, sau đó mới đến dạng số nhiều như `employees`. Đối với cột, dùng danh từ số ít và tránh cột chỉ tên `id` nếu tên có ngữ nghĩa rõ hơn. Không đặt bảng trùng tên với một cột của chính nó. Bảng quan hệ nên có tên biểu đạt quan hệ nghiệp vụ thay vì ghép cơ học hai tên bảng, chẳng hạn `services` thay vì `cars_mechanics` khi đó thực sự là dịch vụ bảo dưỡng.

Alias nên liên quan đến đối tượng đang đại diện; có thể dùng chữ cái đầu của các từ và thêm số nếu bị trùng. Guide khuyến nghị viết rõ `AS`, nhất là với alias của biểu thức tính toán. Tuy nhiên, `AS` cho table alias khác nhau giữa dialect; ví dụ Oracle truyền thống không chấp nhận `AS` cho alias bảng. Trong project đa engine, hãy ghi ngoại lệ này trong quy ước dialect thay vì âm thầm trộn hai phong cách.

## Hậu tố thống nhất và giới hạn của chúng

Các hậu tố giúp đọc nhanh vai trò của cột:

| Hậu tố | Ý nghĩa quy ước | Ví dụ |
| --- | --- | --- |
| `_id` | định danh hoặc khóa tham chiếu | `customer_id` |
| `_status` | trạng thái hoặc cờ trạng thái | `publication_status` |
| `_total` | tổng của một tập giá trị | `order_total` |
| `_num` | một giá trị số nói chung | `staff_num` |
| `_name` | tên | `first_name` |
| `_seq` | dãy liên tục | `line_seq` |
| `_date` | ngày của một sự kiện | `release_date` |
| `_tally` | số lượng đếm được | `error_tally` |
| `_size` | kích thước hoặc dung lượng | `file_size` |
| `_addr` | địa chỉ vật lý hoặc logic | `ip_addr` |

Hậu tố là metadata ngữ nghĩa, không phải type annotation. `file_size` có thể là `INTEGER`, `BIGINT` hoặc `NUMERIC` tùy miền giá trị; `release_date` còn phải phân biệt `DATE` với `TIMESTAMP` và múi giờ. Vì vậy hãy dùng hậu tố cùng với DDL, data contract và kiểm tra kiểu, không dùng tên cột để đoán chắc kiểu vật lý.

## Từ khóa, khoảng trắng và “dòng sông” của query

Từ khóa SQL nên viết hoa (`SELECT`, `FROM`, `WHERE`, `JOIN`, `GROUP BY`) và tránh dạng viết tắt khi có từ đầy đủ tương đương. Mục tiêu của việc căn lề là tách phần cấu trúc khỏi chi tiết triển khai: các từ khóa chính tạo thành một “dòng sông” thẳng đứng, còn tên cột và điều kiện bắt đầu ở cùng vùng đọc.

```sql
SELECT  o.order_id,
        o.customer_id,
        SUM(oi.line_total) AS order_total
  FROM  orders AS o
        JOIN order_item AS oi
          ON oi.order_id = o.order_id
 WHERE  o.order_date >= DATE '2026-01-01'
    AND o.order_date <  DATE '2027-01-01'
 GROUP BY o.order_id,
          o.customer_id;
```

Trong style này, đặt khoảng trắng quanh toán tử, sau dấu phẩy và giữa các mệnh đề; xuống dòng trước `AND`/`OR`, sau mỗi mệnh đề lớn và sau dấu chấm phẩy khi có nhiều statement. `JOIN`/`ON` được thụt vào theo cùng logic; subquery được định dạng như một query độc lập. Dấu phẩy đứng sau phần tử trước nó giúp đoạn SQL vẫn tự nhiên khi đọc, còn việc dùng dấu phẩy đầu dòng là lựa chọn khác của team chứ không phải yêu cầu của guide.

Khoảng trắng không sửa được lỗi logic. Với `LEFT JOIN`, điều kiện lọc đặt trong `WHERE` có thể biến kết quả thành gần như `INNER JOIN`; với window function, `ORDER BY` và window frame vẫn quyết định kết quả dù query đã căn lề hoàn hảo. Vì vậy style phải đi cùng kiểm tra grain, cardinality và kế hoạch thực thi.

## Idiom truy vấn và tính portable

Guide khuyến nghị dùng `BETWEEN` khi thật sự diễn đạt một khoảng có hai đầu mút, `IN` cho một tập giá trị và `CASE` khi cần diễn giải giá trị ngay trong database. Ba lựa chọn này làm ý định rõ hơn, nhưng không được thay thế việc hiểu semantics:

```sql
SELECT  CASE o.order_status
          WHEN 'P' THEN 'pending'
          WHEN 'C' THEN 'completed'
          ELSE 'other'
        END AS order_status_group
  FROM  orders AS o
 WHERE  o.order_date >= DATE '2026-01-01'
    AND o.order_date <  DATE '2026-02-01'
    AND o.channel IN ('web', 'store');
```

Trong ví dụ ngày, dùng nửa khoảng `[start, end)` thường an toàn hơn `BETWEEN` khi cột là `TIMESTAMP`, vì `BETWEEN` bao gồm cả hai đầu mút. `IN` cũng có tương tác với `NULL`; khi cần kiểm tra thiếu dữ liệu phải dùng `IS NULL`/`IS NOT NULL` và kiểm thử riêng. `UNION` hoặc temporary table nên tránh khi chúng chỉ che giấu một schema kém phù hợp, nhưng vẫn đúng và cần thiết trong các bài toán hợp tập, staging, recursion hoặc tối ưu có chủ đích. “Avoid” trong guide nghĩa là xem xét lý do, không phải cấm tuyệt đối.

Ưu tiên hàm, kiểu dữ liệu và cú pháp chuẩn SQL khi khả thi để giảm chi phí chuyển engine. Khi buộc dùng `DATE_TRUNC`, `QUALIFY`, `CONNECT BY`, `TOP`, `PIVOT` hoặc kiểu dữ liệu riêng của vendor, hãy đặt phần đó ở ranh giới dialect, ghi rõ engine/version và có test tương ứng. Ngày giờ nên dùng biểu diễn ISO 8601 và phải thống nhất timezone, precision, cũng như quy tắc chuyển đổi trước khi ghi vào warehouse; chuỗi nhìn giống ISO không tự bảo đảm semantics đúng.

## CREATE TABLE, kiểu dữ liệu và constraints

DDL cũng cần đọc được như query. Nhóm các cột liên quan, đặt khóa chính và constraints ở vị trí ổn định, thụt định nghĩa cột bốn spaces theo guide, đặt default cùng kiểu với cột và dùng `CHECK` cho miền giá trị biết trước. Với số cần tính chính xác, ưu tiên `NUMERIC`/`DECIMAL` thay vì `REAL`/`FLOAT` trừ khi thực sự cần số thực gần đúng.

```sql
CREATE TABLE order_item (
    order_item_id  INTEGER      NOT NULL,
    order_id       INTEGER      NOT NULL,
    quantity       NUMERIC(12, 3) NOT NULL,
    line_total     NUMERIC(18, 2) NOT NULL,
    CONSTRAINT order_item_pk PRIMARY KEY (order_item_id),
    CONSTRAINT order_item_quantity_ck CHECK (quantity > 0)
);
```

Tên constraint, thứ tự cột và kiểu dữ liệu nên được quyết định cùng data model chứ không chỉ để đẹp mắt. Khóa phải cân bằng tính duy nhất, ổn định kiểu dữ liệu, khả năng kiểm tra và độ đơn giản; compound key vẫn hợp lý khi phản ánh đúng nghiệp vụ. Đây là điểm nối trực tiếp tới các bài về khóa, chuẩn hóa và constraints trong mục SQLD.

## Những thiết kế nên xem xét lại

Guide cảnh báo bốn mùi thiết kế thường làm query khó hiểu hoặc khó tối ưu: áp mô hình object của application thẳng vào schema quan hệ; tách giá trị và đơn vị thành hai cột khiến mọi consumer phải ghép lại; dùng Entity–Attribute–Value (EAV) cho dữ liệu lẽ ra có schema rõ; và chia một bảng thành nhiều bảng theo năm, địa điểm hoặc quy ước tùy tiện khiến mọi truy vấn phải `UNION` lại.

Đây là heuristic, không phải lệnh cấm. Partitioning, archival table, EAV có kiểm soát hoặc schema phục vụ ORM có thể có lý do vận hành rõ ràng. Khi chọn ngoại lệ, hãy ghi lại grain, workload, retention, cách truy vấn và chi phí migration; đừng dùng style guide để thay thế phân tích yêu cầu.

## Quy ước bổ sung cho SQL trong pipeline AI

Guide gốc tập trung vào readability và portability. Với pipeline có model SQL được AI sinh, review hoặc refactor, nên bổ sung một lớp quy ước về ngữ nghĩa:

- Mỗi model phải ghi rõ grain: một dòng đại diện cho gì, khóa logic là gì và đầu ra có thể nhân dòng ở `JOIN` nào.
- Tránh `SELECT *` trong model lâu dài; liệt kê cột để schema drift không âm thầm đổi contract.
- Alias đầu ra phải ổn định, mô tả vai trò và không đổi chỉ vì rút gọn query. Cột tính toán nên có tên như cột schema (`order_total`, `customer_tally`).
- Comment lý do nghiệp vụ, đơn vị đo, timezone, nguồn dữ liệu và ngoại lệ dialect; không comment lại cú pháp hiển nhiên.
- Tách CTE theo bước có ý nghĩa, nhưng không tạo CTE chỉ để đổi tên một biểu thức. Mỗi bước nên có một invariant để người và AI có thể kiểm tra.
- Làm rõ `NULL`, late-arriving data, duplicate key, timezone và thứ tự ổn định khi có `LIMIT`/pagination. Một query chạy được chưa chứng minh nó deterministic.
- Review SQL theo thứ tự: cú pháp → grain/cardinality → null và biên thời gian → tính đúng của aggregate/window → hiệu năng → portability.

Ví dụ, hai câu lệnh dưới đây có thể cho cùng số liệu ở dữ liệu hiện tại, nhưng câu thứ hai có contract rõ hơn:

```sql
-- Mơ hồ: phụ thuộc schema và có thể đổi khi bảng thêm cột
SELECT *
  FROM orders;

-- Rõ contract: một dòng là một order, cột đầu ra có tên ổn định
SELECT  o.order_id,
        o.customer_id,
        o.order_date,
        o.order_status
  FROM  orders AS o;
```

Style làm AI dễ đọc hơn vì cấu trúc và tên nhất quán, nhưng không biến AI thành bộ kiểm định. Vẫn cần test dữ liệu, snapshot kết quả quan trọng, kiểm tra schema và review của người hiểu domain.

## Checklist áp dụng trong repository

Trước khi merge một file SQL, hãy kiểm tra: tên có nhất quán và không trùng keyword không; từ khóa, alias, `JOIN` và điều kiện đã có format chung chưa; query có nêu rõ grain và cột đầu ra không; `NULL`, khoảng thời gian và duplicate có test không; cú pháp vendor-specific đã ghi dialect/version chưa; và linter/formatter có chạy cùng CI không. Nếu lệch guide vì lý do chính đáng, ghi lý do ngay cạnh quyết định hoặc trong tài liệu của project.

Phụ lục của guide liệt kê reserved words của ANSI SQL cùng các phiên bản cũ của MySQL, PostgreSQL, SQL Server, ODBC và Oracle. Đây là điểm khởi đầu tốt để tránh đặt tên trùng keyword, nhưng không phải danh sách hiện hành cho mọi engine. Khi tạo schema mới, hãy kiểm tra tài liệu reserved words của đúng engine/version và để migration test bắt lỗi sớm.

## Kết luận và đường học tiếp

SQL Style Guide cung cấp một default thực dụng: tên có ngữ nghĩa, query có “dòng sông” dễ quét, schema có constraints và cú pháp ưu tiên tính portable. Hai điểm nên áp dụng ngay cho pipeline là căn lề nhất quán và hậu tố có nghĩa; hai điểm phải luôn kiểm tra lại là semantics (`NULL`, biên thời gian, grain) và ngoại lệ dialect. Sau bài này, quay lại các bài `JOIN`, `Subquery`, `Group Functions`, `Window Functions` và `DDL/Constraints` để áp style vào query thật, rồi dùng checklist ở trên khi review model dài trong pull request.
