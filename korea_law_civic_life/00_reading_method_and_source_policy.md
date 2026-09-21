# 00. Phương pháp đọc pháp luật và chính sách nguồn

## 1. Mục tiêu của file này

Khi sống ở Hàn Quốc, phần khó thường không phải là “không có thông tin”, mà là **không biết thông tin nào có giá trị pháp lý, thông tin nào đã cũ, và cơ quan nào thực sự có thẩm quyền**. Vì vậy, kỹ năng quan trọng nhất là xây một chuỗi kiểm tra nguồn thay vì ghi nhớ thật nhiều con số.

Một quy trình an toàn nên đi theo thứ tự:

```text
vấn đề thực tế
→ lĩnh vực pháp luật
→ cơ quan phụ trách
→ luật/quy định hiện hành
→ hướng dẫn thủ tục hiện hành
→ biểu mẫu/hồ sơ
→ thời hạn và cách nộp
→ kết quả / cơ chế phản đối nếu không đồng ý
```

## 2. Phân biệt bốn lớp thông tin

### 2.1. Luật đang có hiệu lực

Đây là lớp quan trọng nhất khi cần xác định quyền và nghĩa vụ. Nguồn chuẩn là **Trung tâm thông tin pháp luật quốc gia (국가법령정보센터)** tại `law.go.kr`.

Khi mở một luật, hãy kiểm tra ba thứ trước khi đọc nội dung: tên luật, ngày có hiệu lực `시행일`, và trạng thái sửa đổi. Một điều khoản đúng trong bản cũ có thể không còn đúng trong bản hiện hành.

### 2.2. Hướng dẫn chính thức của cơ quan thực thi

Ví dụ, cùng là luật lao động nhưng hướng dẫn thực tế có thể cần xem tại Bộ Việc làm và Lao động (고용노동부), Work24 hoặc cơ quan lao động địa phương. Luật cho biết nguyên tắc; cơ quan thực thi thường cho biết mẫu đơn, cách khai và kênh xử lý.

### 2.3. Tài liệu giải thích chính thức

Các nguồn như `찾기쉬운 생활법령정보`, `정부24`, `국민신문고`, FAQ của bộ/ngành rất hữu ích để hiểu luật bằng ngôn ngữ đời sống. Chúng thường dễ đọc hơn văn bản luật nhưng vẫn cần quay lại luật gốc nếu có tranh chấp hoặc điểm quan trọng.

### 2.4. Nguồn không chính thức

Blog, diễn đàn, YouTube, cộng đồng người nước ngoài có giá trị để biết “người khác từng gặp gì”, nhưng không nên là điểm dừng cuối cùng. Hãy dùng chúng để lấy **từ khóa**, sau đó kiểm tra lại trên nguồn chính thức.

## 3. Nhận biết thông tin nhạy theo thời gian

Các nội dung sau phải coi là **dynamic data**, không nên học thuộc như chân lý cố định:

- mức đóng bảo hiểm;
- mức lương tối thiểu;
- giới hạn, ngưỡng tiền hoặc mức phạt;
- điều kiện visa và thường trú;
- danh sách quốc gia thuộc cơ chế tương hỗ;
- mẫu đơn;
- thời hạn khai báo;
- cơ quan hoặc tên hệ thống điện tử;
- quy trình nộp online/offline;
- tiêu chí hỗ trợ phúc lợi.

Trong library này, những phần như vậy được trình bày theo **cơ chế** và kèm nơi kiểm tra hiện hành thay vì cố nhồi thật nhiều số liệu.

## 4. Cách đọc một điều luật

Một điều luật thường có cấu trúc:

```text
Điều (조)
→ Khoản (항)
→ Điểm/số (호)
→ Mục nhỏ (목)
```

Ví dụ `제17조 제1항 제2호` nghĩa là Điều 17, Khoản 1, Số 2. Khi một FAQ dẫn điều khoản, nên mở đúng điều này trên `law.go.kr` thay vì chỉ đọc bản tóm tắt.

Các cụm cần nhận biết:

- `하여야 한다`: phải làm;
- `할 수 있다`: có thể;
- `하여서는 아니 된다`: không được làm;
- `다만`: tuy nhiên / ngoại lệ;
- `대통령령으로 정한다`: chi tiết được giao cho nghị định tổng thống;
- `부령으로 정한다`: chi tiết được giao cho quy định cấp bộ;
- `별표`: phụ lục;
- `시행령`: nghị định thi hành;
- `시행규칙`: quy tắc thi hành.

## 5. Một luật thường không đứng một mình

Ví dụ một vấn đề thuê nhà có thể cần đọc cả:

```text
주택임대차보호법
→ 주택임대차보호법 시행령
→ 관련 대법원규칙
→ 주민센터/등기소/정부24 hướng dẫn
→ 등기부등본 thực tế của căn nhà
```

Tương tự, vấn đề lao động có thể cần `근로기준법`, nghị định/quy tắc thi hành, hướng dẫn của `고용노동부`, hợp đồng lao động và chứng cứ thực tế như bảng lương, log chấm công.

## 6. Tách “quy định chung” khỏi “trường hợp của tôi”

Một nguyên tắc rất quan trọng: **quy định chung không tự động trả lời trường hợp cá nhân**.

Ví dụ một người hỏi “tôi có được overtime không?” nhưng để trả lời chính xác có thể phải biết loại hợp đồng, vị trí, số giờ, quy mô nơi làm việc, cách tính lương, có thuộc ngoại lệ hay không, thời điểm phát sinh sự việc và nội dung thỏa thuận. Vì vậy library này giải thích cách hệ thống vận hành, không kết luận thay cho tư vấn pháp lý cá nhân.

## 7. Quy tắc ghi chép khi tự nghiên cứu

Mỗi lần tra một vấn đề, nên ghi theo mẫu:

```markdown
## Vấn đề
...

## Cơ quan phụ trách
...

## Luật gốc
- tên luật:
- điều khoản:
- 시행일:

## Hướng dẫn chính thức
...

## Điều kiện / ngoại lệ
...

## Việc cần xác minh thêm
...

## Ngày kiểm tra
YYYY-MM-DD
```

Cách ghi này giúp bạn nhận ra một note cũ cần kiểm tra lại khi luật thay đổi.

## 8. Nguồn lõi của library

Các cổng được dùng lặp lại trong toàn bộ tài liệu gồm:

- `law.go.kr` — 국가법령정보센터;
- `moleg.go.kr` — 법제처;
- `gov.kr` — 정부24;
- `epeople.go.kr` — 국민신문고;
- `scourt.go.kr` — 대한민국 법원;
- `moel.go.kr`, `work24.go.kr` — lao động và việc làm;
- `nts.go.kr`, `hometax.go.kr` — thuế;
- `nps.or.kr`, `nhis.or.kr`, `comwel.or.kr` — bảo hiểm xã hội;
- `immigration.go.kr`, `hikorea.go.kr` — xuất nhập cảnh và cư trú;
- `consumer.go.kr`, `kca.go.kr` — quyền người tiêu dùng;
- `iros.go.kr` — đăng ký bất động sản;
- `acrc.go.kr` — 국민권익위원회.

Danh sách đầy đủ và mục đích sử dụng nằm trong [`SOURCES.md`](SOURCES.md).