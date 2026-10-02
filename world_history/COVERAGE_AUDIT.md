# Coverage kiểm tra (audit / 감사) — World lịch sử (history / 이력)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Coverage audit — World History**. Route đi từ chapter inventory → dependency/owner checks → evidence and link coverage → quality matrix → remediation priorities, để audit dẫn tới hành động cụ thể.

## Kết luận hiện tại

`world_history/` đã có **breadth tốt**: đủ 17 giai đoạn theo chuỗi người dùng yêu cầu, có phương pháp, glossary và cross-link với Geography/Korean lịch sử (history / 이력)/Culture. độ sâu (depth / 깊이) pass này đã làm dày 14 chuẩn gốc (canonical / 정본) chapters trọng tâm (Agricultural Revolution → post-1991) bằng initial conditions, actors, institutions, material các ràng buộc (constraints / 제약조건들), cơ chế (mechanism / 메커니즘), sự kiện (event / 이벤트) chuỗi (sequence / 시퀀스), competing interpretations, consequences và đường dẫn (path / 경로) dependence. Mục tiêu là chapter đọc độc lập ở mức **advanced foundation**; đây vẫn không phải chuyên khảo theo từng vùng, nguồn hay tranh luận sử học.

Đây là baseline đủ chắc để chuyển từ “lấp khoảng trống” sang **độ sâu (depth / 깊이) có chọn lọc**. Vòng đánh giá này đã bổ sung trường hợp (case / 사례) studies liên vùng, chuyển tiếp (transition / 전이) ma trận (matrix / 행렬) và nguồn (source / 소스) workbench; ưu tiên kế tiếp là gắn các trường hợp (case / 사례) đó vào bibliography cụ thể và các chapter chuyên đề, không sinh thêm hàng loạt tệp (file / 파일) timeline.

> **Chuyển mạch:** Trong **Coverage kiểm tra (audit / 감사) — World lịch sử (history / 이력)**, **Ma trận chất lượng** gom các mảnh từ **Kết luận hiện tại** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Ranh giới cần giữ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ma trận chất lượng

| Tiêu chí | Trạng thái | Ghi chú |
| --- | --- | --- |
| Period coverage | Mạnh | 17 giai đoạn từ origins đến post-Cold War |
| nhân quả (causal / 인과적) spine | Mạnh | Mỗi chapter có technology/resources/institutions/trade/warfare/demography/ideas và độ sâu (depth / 깊이) chuỗi (sequence / 시퀀스) |
| Regional balance | Khá–mạnh | Đã thêm trường hợp (case / 사례) West Africa, South/Southeast Asia, East Asia, Mesoamerica/Andes và các basin/biển; cần độ sâu (depth / 깊이) chapter riêng nếu chọn ưu tiên |
| Material các hệ thống (systems / 시스템들) | Mạnh | Food, land, năng lượng (energy / 에너지), metals, shipping, finance và ecological externality đã có nhân quả (causal / 인과적) treatment |
| Institutions | Mạnh | trạng thái (state / 상태), empire, law, religion, company, party, alliance đã được đặt vào chuỗi |
| xã hội (social / 사회적) phân phối (distribution / 분포) | Khá–mạnh | Có coercion, slavery, gender, lớp (class / 클래스), di chuyển (migration / 마이그레이션) và winner–loser; cần trường hợp (case / 사례) study tiếng nói bị trị |
| Demography/disease | Khá–mạnh | Có disease, di chuyển (migration / 마이그레이션), displacement và bất định (uncertainty / 불확실성); cần thời gian (time / 시간) series chọn lọc |
| Warfare/logistics | Mạnh | Từ raid đến total war/proxy war, có supply, debt, food, năng lượng (energy / 에너지) và alliance logistics |
| Ideas/legitimacy | Mạnh | Không tách ideas khỏi institutions và material cơ sở (base / 기반) |
| bằng chứng (evidence / 증거)/nguồn (source / 소스) practice | Mạnh | Mỗi chapter ghi loại bằng chứng (evidence / 증거), archive độ lệch (bias / 편향) và limitation; `22_source_workbench` chuẩn hoá cách kiểm tra và `23_annotated_bibliography` cung cấp reading map có giới hạn rõ |
| Cross-links | Mạnh | chỉ mục (index / 인덱스), methods và link sang Geography/Korea đã có |
| Study usability | Mạnh | README, phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프), học tập (learning / 학습) tuyến (route / 경로), kiểm tra (audit / 감사), glossary, trường hợp (case / 사례) studies và chuyển tiếp (transition / 전이) ma trận (matrix / 행렬) đã có |

> **Chuyển mạch:** **Ma trận chất lượng** cho biết tiêu chí nào đang thiếu; **Ranh giới cần giữ** khóa phạm vi audit, rồi **Ưu tiên nâng cấp** chọn lỗ hổng có tác động lớn nhất thay vì sửa dàn trải.

## Ranh giới cần giữ

```text
world_history/      = causal comparison xuyên vùng và thời gian
korean_history/     = lịch sử bán đảo Triều Tiên chuyên sâu
world_geography/    = spatial/physical/resource constraints và networks
korean_culture/     = institutions, practices và everyday meanings
investing/economics = market, finance, risk và allocation tools
```

Khi một chapter mới cần mô tả địa hình, không duplicate toàn bộ Geography; khi cần niên đại Hàn Quốc, link sang Korean lịch sử (history / 이력); khi cần mô hình kinh tế, giữ phần lịch sử ở đây và trỏ sang Economics.

> **Chuyển mạch:** Khi ranh giới đã rõ, **Ưu tiên nâng cấp** biến issue thành thứ tự hành động; **Definition of done** nêu bằng chứng tối thiểu để xác nhận một depth pass thật sự hoàn tất.

## Ưu tiên nâng cấp

### P0 — giữ nhất quán

- Mỗi chapter mới phải có ít nhất một chuỗi nhân quả (causal chain / 인과 사슬), một ranh giới (boundary / 경계)/limitation và một chuyển tiếp (transition / 전이).
- Dùng cùng vocabulary cho `stock`, `flow`, `capacity`, `extraction`, `legitimacy`, `chokepoint`, `agency`.
- Ghi rõ khi periodization là quy ước phân tích chứ không phải ranh giới tự nhiên.

### P1 — tăng chiều sâu có chọn lọc (đã thực hiện vòng này)

- Đã deepen trực tiếp 14 chuẩn gốc (canonical / 정본) files, không tạo thêm breadth/chapter timeline.
- Đã làm rõ coal–steam–factory–empire, colonial extraction, debt/borders/mass politics và logistics trong các chapter tương ứng.
- Bước tiếp theo là gắn từng trường hợp (case / 사례) trong `20_comparative_case_studies.md` với nguồn (source / 소스) cụ thể, dataset và tranh luận học thuật; đây là refinement, không phải mở folder mới.

### P2 — mở rộng sau khi P1 ổn định

- Thêm các mô-đun (module / 모듈) theo vùng: West Africa, South Asia, Southeast Asia, Mesoamerica/Andes, East Asia.
- Tạo timeline tra cứu nhanh chỉ sau khi nhân quả (causal / 인과적) chapters đủ sâu.
- Bổ sung bibliography có chú thích ngắn: nguồn sơ cấp, textbook, monograph và dataset.

> **Chuyển mạch:** **Definition of done** khép vòng audit bằng claim, nguồn, reasoning và link có thể kiểm tra; thiếu một trong các bằng chứng đó thì issue vẫn mở.

## Definition of done cho một độ sâu (depth / 깊이) pass

Một chapter chỉ được xem là đã nâng cấp khi có:

1. ít nhất hai quy mô (scale / 규모) được phân biệt;
2. một bảng hoặc sơ đồ stock/luồng (flow / 흐름);
3. một ví dụ về phân phối (distribution / 분포)/winner–loser;
4. một counterfactual có giới hạn;
5. tối thiểu hai loại bằng chứng (evidence / 증거) và ghi rõ bất định (uncertainty / 불확실성);
6. link trước–sau và link sang lĩnh vực (domain / 도메인) liên quan;
7. một đoạn “khi mô hình không áp dụng”.

Độ sâu (depth / 깊이) pass bổ sung thêm một chất lượng (quality / 품질) chuỗi (sequence / 시퀀스) bắt buộc cho các chapter chuẩn gốc (canonical / 정본):

```text
initial conditions → actors → institutions/material constraints
→ mechanism → event sequence → competing interpretations
→ consequences → long-run path dependence
```

> **Bàn giao:** Sau **Definition of done cho một độ sâu (depth / 깊이) pass**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
