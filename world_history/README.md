# World lịch sử (history / 이력) — Master kiến thức (knowledge / 지식) Book

> **Mạch đọc:** Đây là README owner của **World History — Master Knowledge Book**. Route đọc đi từ origins/agriculture → states/empires/networks → modernity/war/decolonization → globalization → methods, sources and cases; mỗi cụm nối một cơ chế với thời gian, không gian và bằng chứng.

Thư viện này giải thích lịch sử thế giới như một **hệ thống nhân quả liên vùng**, không phải danh sách ngày tháng hay bộ sưu tập “nền văn minh lớn”. Mỗi giai đoạn được đọc qua các dòng liên kết:

```text
technology ↔ resources ↔ institutions ↔ trade
          ↔ warfare ↔ demography ↔ ideas
```

Một thay đổi chỉ trở thành bước ngoặt khi nó làm đổi **khả năng huy động tài nguyên**, **quy mô phối hợp**, **phân bố dân cư**, hoặc **ý niệm về chính danh**. Vì vậy chapter luôn hỏi: ai có năng lực tổ chức; năng lượng, lương thực và thông tin đi qua đâu; chiến tranh và dịch bệnh làm đứt hay tái cấu trúc mạng nào; nhóm nào được hưởng và nhóm nào phải trả chi phí.

## Bắt đầu từ đâu

Đọc theo [mục lục và dependency graph](00_index_and_dependency.md). Nếu muốn có lộ trình theo mục tiêu, dùng [Learning Route](LEARNING_ROUTE.md); nếu muốn biết phần nào đã mạnh/yếu, xem [Coverage Audit](COVERAGE_AUDIT.md). Chuỗi chính là:

```text
01 Human origins
→ 02 Agricultural Revolution
→ 03 Early states and civilizations
→ 04 Classical civilizations
→ 05 Religions and transregional networks
→ 06 Medieval political/economic systems
→ 07 Early modern world
→ 08 Global trade and colonial expansion
→ 09 Scientific + Industrial Revolutions
→ 10 Imperialism
→ 11 World War I
→ 12 Interwar period
→ 13 World War II
→ 14 Cold War
→ 15 Decolonization
→ 16 Globalization
→ 17 Post-Cold-War world
```

Các chương không tuyên bố rằng lịch sử đi theo một đường thẳng. Chúng dùng các **chuyển tiếp** để chỉ ra điều kiện đã thay đổi, những đường đi bị bỏ lỡ và các continuity còn sót lại. Sau tuyến chính, dùng [comparative case studies](20_comparative_case_studies.md), [transition matrix](21_transition_matrix.md), [source workbench](22_source_workbench.md) và [annotated bibliography](23_annotated_bibliography.md) để kiểm tra mô hình trong nhiều vùng và nhiều loại bằng chứng.

Vòng độ sâu (depth / 깊이) pass hiện tại giữ nguyên tuyến và chuẩn gốc (canonical / 정본) files, nhưng làm dày 14 nút (node / 노드) từ Agricultural Revolution đến post-1991. Khi đọc các nút (node / 노드) này, theo chuỗi: `initial conditions → actors → institutions/material constraints → mechanism → event sequence → competing interpretations → consequences → path dependence`. Đây là tài liệu học độc lập ở mức advanced foundation, không phải chuyên khảo thay thế nguồn (source / 소스) workbench.

> **Chuyển mạch:** **Bắt đầu từ đâu** chọn tuyến và dependency; **Phạm vi và ranh giới** xác định điều gì thuộc world history và điều gì phải trả về owner khác trước khi dùng **Quy tắc đọc một giai đoạn**.

## Phạm vi và ranh giới

- `world_history/` tập trung vào cơ chế xuyên vùng và so sánh; không thay thế lịch sử quốc gia chuyên sâu như [`korean_history/`](../korean_history/).
- Địa hình, khí hậu, tài nguyên, tuyến biển và không gian được nối sang [`world_geography/`](../world_geography/); geography là ràng buộc (constraint / 제약조건) và opportunity, không phải định mệnh.
- Trao đổi, tín dụng, năng lượng và phân phối giá trị có thể đọc cùng [`investing/`](../investing/) và các chapter economics liên quan.
- Nhà nước, luật, quyền công dân, thuộc địa và chủ quyền được đặt cạnh [`korea_law_civic_life/`](../korea_law_civic_life/) khi cần một trường hợp (case / 사례) hiện đại.
- Tôn giáo, gia đình, giới, lao động, ký ức và đời sống thường ngày được đọc như institutions và xã hội (social / 사회적) practices; không giản lược chúng thành “văn hoá” bất biến.

> **Chuyển mạch:** Sau khi biết phạm vi, **Quy tắc đọc một giai đoạn** đặt cùng một khung scale–stock/flow–shock lên từng chapter; **Chất lượng và bằng chứng** kiểm tra khung đó bằng nguồn và counterfactual.

## Quy tắc đọc một giai đoạn

1. Xác định **quy mô (scale / 규모)**: hộ gia đình, thành phố, đế chế, đại dương hay hệ thống toàn cầu.
2. Vẽ các **stock/luồng (flow / 흐름)**: dân số, đất, nước, lương thực, bạc/vàng, năng lượng, hàng hoá, dữ liệu và nhân lực.
3. Tách **shock** khỏi xu hướng dài hạn: chiến tranh có thể ngắn nhưng làm đổi thuế, biên giới và quyền sở hữu nhiều thế hệ.
4. Kiểm tra **winners, losers, coercion và agency**; tăng trưởng của một mạng thường dựa trên chi phí bị đẩy sang nhóm khác.
5. So sánh ít nhất hai vùng và ghi rõ nơi mô hình không áp dụng.

> **Chuyển mạch:** **Chất lượng và bằng chứng** là bước kiểm tra cuối: mỗi claim phải chỉ ra cơ chế, quy mô, độ bất định và nguồn đủ mạnh trước khi được mang sang chapter kế tiếp.

## Chất lượng và bằng chứng

Mỗi chapter phân biệt nguồn sơ cấp, diễn giải sử học, số liệu dân số/kinh tế và suy luận của người đọc. Niên đại là mốc định hướng; nhân quả (causal / 인과적) claim phải nêu cơ chế, quy mô (scale / 규모), độ bất định và counterfactual tối thiểu. Xem [phương pháp và connections](18_methods_connections.md), [glossary](19_glossary_and_reference_map.md) và [coverage audit](COVERAGE_AUDIT.md).

> **Bàn giao:** Sau **Chất lượng và bằng chứng**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
