# Life Knowledge Library — Kiến thức đời sống

Thư viện này giải thích những đối tượng rất thường gặp trong đời sống nhưng dễ bị hiểu theo tên gọi, thương hiệu hoặc marketing hơn là theo bản chất. Mục tiêu là để người đọc hiểu **nó giải quyết vấn đề gì, được tạo ra hoặc vận hành như thế nào, vì sao có các loại khác nhau, thông số hay nhãn nào thực sự có ý nghĩa, cách sử dụng/bảo dưỡng thay đổi kết quả ra sao, và kiến thức đó được dùng thế nào khi so sánh sản phẩm**.

Nội dung kế thừa [`prompt/COMMON_PROMPT.md`](../prompt/COMMON_PROMPT.md): ưu tiên mô hình tư duy, cơ chế, nguyên lý nền tảng và mạch giải thích liên tục; thuật ngữ chuyên môn được giải thích bằng tiếng Việt kèm từ khóa tiếng Anh/Hàn khi phù hợp.

## Life sở hữu phạm vi nào?

`life/` không phải folder “mọi thứ ngoài đời”. Nó là **everyday object & consumer literacy**: những đồ vật, sản phẩm, vật liệu và hệ thống nhỏ mà một người trực tiếp sử dụng, bảo quản, bảo dưỡng, so sánh hoặc mua.

Mental model chung:

```text
problem / use case
→ material / ingredient
→ construction / production
→ mechanism
→ classification axes
→ specs / labels
→ trade-offs
→ use / maintenance
→ failure / degradation
→ comparison / ownership
```

Boundary quan trọng:

- hệ thống hạ tầng end-to-end như điện, road, banking, logistics → `how-things-work/` khi domain đó canonical;
- affordability, debt, budget, financial resilience → [`personal-finance/`](../personal-finance/README.md);
- reasoning framework cho claim/decision → [`thinking/`](../thinking/README.md);
- scientific theory sâu → Physics, Chemistry, Biology, Electrical Engineering và các canonical owner tương ứng;
- luật/quy trình hành chính → domain legal/civic phù hợp.

## Bản đồ học

### Consumer Literacy

Bắt đầu từ [`consumer_literacy/README.md`](consumer_literacy/README.md) nếu mục tiêu là học cách đọc specification, label, review, warranty, durability, repairability và total cost mà không bị feature count hay marketing dẫn dắt.

### Đồ uống và văn hóa thưởng thức

Bắt đầu từ [`food_drink/README.md`](food_drink/README.md). Nhánh đầu tiên đi sâu vào whisky và bia: nguyên liệu → quá trình tạo thành → hệ phân loại → hương vị → cách đọc nhãn → cách thưởng thức và so sánh. Sau khi hai nhánh seed đủ sâu mới mở rộng sang wine, coffee, tea hoặc fermentation.

### Phương tiện và xe hơi

Bắt đầu từ [`vehicles/README.md`](vehicles/README.md), sau đó vào [`vehicles/cars/README.md`](vehicles/cars/README.md). Nhánh xe hơi không học bằng cách thuộc tên mẫu xe. Nó bắt đầu từ nhu cầu di chuyển và cấu trúc của một chiếc xe, sau đó nối động cơ, truyền động, chassis, thân xe, thông số, trải nghiệm lái, bảo dưỡng và kinh tế sở hữu thành một hệ thống.

## Nguyên tắc của domain

Life Knowledge không phải catalog sản phẩm và cũng không phải bộ mẹo mua hàng. Một khái niệm chỉ thực sự được hiểu khi người đọc có thể giải thích được **vì sao** hai sản phẩm thuộc hai loại khác nhau, sự khác biệt đó đến từ đâu, nó tạo ra hệ quả gì và khi nào sự khác biệt ấy thực sự quan trọng.

Vì vậy các chapter ưu tiên đường đi:

```text
nguồn gốc / vấn đề
→ cấu tạo hoặc nguyên liệu
→ cơ chế
→ phân loại
→ thuộc tính cảm nhận được
→ cách đọc thông tin
→ sử dụng / bảo dưỡng / failure
→ ứng dụng thực tế
```

Thương hiệu và model cụ thể chỉ xuất hiện khi chúng giúp làm rõ một mechanism, classification hoặc trade-off; không dùng brand list để thay cho kiến thức.

## Coordination

- [`CONCEPTUAL_DEPENDENCIES.md`](CONCEPTUAL_DEPENDENCIES.md) — các concept dùng lại giữa nhiều product domains.
- [`COVERAGE_AUDIT.md`](COVERAGE_AUDIT.md) — phần nào đã đủ sâu, seed-only, planned hoặc thuộc domain khác.

Mục tiêu dài hạn không phải bao phủ mọi sản phẩm. Mục tiêu là tạo một tập mental models đủ mạnh để người đọc gặp một đồ vật chưa từng học vẫn biết **nên hỏi những câu gì để hiểu nó**.