# Economics Knowledge Library

Thư viện Economics độc lập bắt đầu từ phần kiến thức đã có trong `investing/04_economics/`, nhưng mở rộng boundary từ “kinh tế học phục vụ quyết định đầu tư” sang Economics như một ngành nền tảng. Mục tiêu là giải thích cách cá nhân, doanh nghiệp, thị trường, nhà nước và các nền kinh tế tương tác dưới điều kiện khan hiếm, thông tin không hoàn hảo và ràng buộc thể chế.

Xem [Coverage Audit](./COVERAGE_AUDIT.md) để biết module nào đã bắt đầu, phần nào còn là roadmap và quy tắc migrate nội dung từ Investing.

## Phạm vi và nguyên tắc tách

`investing/04_economics/` vẫn là nguồn chuyên sâu hiện tại cho macro, monetary system, capital flows, crisis transmission, public debt, demographics, productivity và policy regime trong bối cảnh đầu tư. Domain này sẽ được migrate hoặc cross-link dần; không copy hàng loạt nội dung chỉ để đổi vị trí.

Economics độc lập sẽ bổ sung các nhánh mà investing chỉ chạm tới ở mức cần thiết:

- consumer theory và producer theory;
- market structure và industrial organization;
- game theory và strategic interaction;
- labor economics;
- public economics;
- international trade;
- development economics;
- econometrics;
- economic history và lịch sử thể chế.

## Lộ trình hiện tại

```text
00 Foundations
   ↓
01 Microeconomics
   ↓
02 Market Structure & Game Theory
   ↓
03 Macroeconomics
   ↓
04 Applied Fields
   ├── Labor Economics
   ├── Public Economics
   ├── International Trade
   ├── Development Economics
   └── Industrial Organization
   ↓
05 Econometrics
   ↓
06 Economic History & Institutions
```

### 00 — Foundations — đã bắt đầu

Đã bắt đầu bằng [Economic reasoning](./00_foundations/00_economic_reasoning.md): khan hiếm, opportunity cost, marginal analysis, incentives, equilibrium, efficiency và phân biệt positive với normative analysis.

### 01 — Microeconomics — đã bắt đầu

Module đầu tiên là [Consumer & producer theory](./01_microeconomics/00_consumer_and_producer_theory.md): budget constraint, preferences, utility, demand, technology, cost, profit, supply, market failure và boundary giữa private với social outcome.

### Các bước tiếp theo

1. Hoàn thiện microeconomics bằng welfare, externalities, public goods và asymmetric information.
2. Tách market structure và game theory thành một mạch riêng, nối hành vi chiến lược với industrial organization.
3. Chuẩn hóa macro độc lập từ national accounts, business cycle, inflation, unemployment, growth, money, fiscal policy và open economy; sau đó cross-link các chapter đầu tư hiện có.
4. Bổ sung labor, public, international trade và development economics.
5. Thêm econometrics như lớp đo lường và kiểm định, không dùng regression như một hộp đen.
6. Kết nối economic history với thay đổi thể chế, công nghệ, thương mại, tài chính và năng lực nhà nước.

## Các domain liên quan

- [Investing](../investing/README.md): ứng dụng Economics vào tài sản, doanh nghiệp, định giá và danh mục.
- [Korea Business & Economy](../korea_business_economy_knowledge_library/README.md): case và thể chế kinh tế Hàn Quốc.
- [Mathematics](../mathematics/README.md): calculus, probability, statistics, optimization và dynamical systems.
- [Psychology](../psychology/README.md): behavioral economics, bounded rationality và decision-making.

## Quy ước nội dung

Mỗi chapter phải phân biệt rõ:

1. model và assumptions;
2. cơ chế nhân quả;
3. dự đoán hoặc comparative statics;
4. evidence và giới hạn đo lường;
5. trường hợp mô hình không còn phù hợp.

Không dùng một kết quả cân bằng đơn giản để thay thế cho lịch sử, quyền lực, thể chế hoặc phân phối. Khi chuyển sang chính sách, phải tách câu hỏi positive (“điều gì xảy ra?”) khỏi câu hỏi normative (“nên chọn gì?”).
