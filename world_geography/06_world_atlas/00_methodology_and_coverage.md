# Phương pháp, tên gọi và phạm vi của World Atlas

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Phương pháp, tên gọi và phạm vi của World Atlas**. Route đi từ inventory/schema → naming and boundary rules → country/region entries → physical/human indicators → comparison limits, để atlas nhất quán mà không giả định đồng nhất.

## Inventory và học tập (learning / 학습) profile là hai bài toán khác nhau

Cụm “mọi quốc gia và vùng lãnh thổ” có nhiều lớp thống kê và pháp lý. Để inventory không tùy ý, dự án (project / 프로젝트) dùng **UN M49** làm baseline cho danh mục `countries or areas`, với ISO 3166 làm tham chiếu bổ trợ khi phù hợp.

Việc một entry nằm trong inventory không buộc phải có một chapter riêng. Inventory giải quyết **completeness của danh sách**; học tập (learning / 학습) profile giải quyết **giá trị giáo dục**.

> **Chuyển mạch:** Trong **Phương pháp, tên gọi và phạm vi của World Atlas**, **Cấu trúc tệp (file / 파일) không phải tuyên bố chủ quyền** tiếp nhận điểm tựa từ **Inventory và học tập (learning / 학습) profile là hai bài toán khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Không tạo stub để chạy coverage** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cấu trúc tệp (file / 파일) không phải tuyên bố chủ quyền

Nếu một không gian được phân tích riêng, điều đó chỉ có nghĩa nó hữu ích cho địa lý. Folder, tên tệp (file / 파일) và mã không được dùng như kết luận về chủ quyền, tính chính danh hoặc đường biên.

Với khu vực có cách phân loại khác nhau giữa hệ thống quốc tế, profile phải ghi provenance và tách: hệ phân loại thống kê, tình trạng/quan điểm theo nguồn và cấu trúc địa lý đang phân tích. Không suy ý định chính trị từ bản đồ.

> **Chuyển mạch:** Ở chặng này của **Phương pháp, tên gọi và phạm vi của World Atlas**, **Không tạo stub để chạy coverage** tiếp nhận điểm tựa từ **Cấu trúc tệp (file / 파일) không phải tuyên bố chủ quyền** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bốn trạng thái nội dung** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Không tạo stub để chạy coverage

Một template có vài câu không phải profile. Từ kiểm tra (audit / 감사) này, quy tắc là:

- không auto-generate country files từ inventory;
- không đánh dấu completed chỉ vì tệp (file / 파일) tồn tại;
- không dùng số line/heading như chỉ số (metric / 지표) chất lượng;
- không bản sao (copy / 복사) cùng một đoạn cho hàng chục country rồi đổi tên;
- nếu trường hợp (case / 사례) không có đủ giá trị độc lập, gộp vào regional/comparative chapter.

Các stub legacy từ batch trước chỉ là transitional tham chiếu (reference / 참조) và sẽ được promote/merge/remove khi Atlas được cleanup.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phương pháp, tên gọi và phạm vi của World Atlas**, **Bốn trạng thái nội dung** tiếp nhận điểm tựa từ **Không tạo stub để chạy coverage** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Profile phải có thesis, không chỉ template** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bốn trạng thái nội dung

**Inventory only:** chỉ có entry trong danh mục.

**tham chiếu (reference / 참조):** có ghi chú ngắn để định vị nhưng chưa đủ làm bài học.

**học tập (learning / 학습) profile:** có chuỗi nhân quả (causal chain / 인과 사슬) hoàn chỉnh, misconception, mô hình tư duy (mental model / 사고 모델) và cross-link.

**Deep comparative profile:** ngoài học tập (learning / 학습) profile còn so sánh cơ chế với nơi khác, giải thích mạng (network / 네트워크) phụ thuộc (dependency / 의존성) và nối nhiều lĩnh vực (domain / 도메인) cốt lõi (core / 핵심).

Chỉ hai trạng thái cuối được tính vào educational coverage.

> **Chuyển mạch:** Trong **Phương pháp, tên gọi và phạm vi của World Atlas**, **Profile phải có thesis, không chỉ template** tiếp nhận điểm tựa từ **Bốn trạng thái nội dung** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Nội dung bền vững và dữ liệu theo thời điểm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Profile phải có thesis, không chỉ template

Mỗi profile nên trả lời một câu thesis, ví dụ: “địa lý của nơi này được tổ chức bởi một megadelta + export corridor + monsoon regime” hoặc “mountain water tower + landlocked trade dependence”.

Các section sau phải chứng minh thesis. Nếu heading đầy đủ nhưng nội dung chỉ lặp fact, profile vẫn chưa đạt.

> **Chuyển mạch:** Ở chặng này của **Phương pháp, tên gọi và phạm vi của World Atlas**, **Profile phải có thesis, không chỉ template** nêu điều cần giải thích; **Nội dung bền vững và dữ liệu theo thời điểm** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Political geography và ranh giới (boundary / 경계) provenance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nội dung bền vững và dữ liệu theo thời điểm

Ưu tiên vị trí, relief, basin, climate regime, population mẫu (pattern / 패턴), urban hierarchy, môi trường vận hành (production / 운영 환경) belt, cổng (port / 포트)/corridor và hazard cơ chế (mechanism / 메커니즘).

Population/GDP/trade share, hiện tại (current / 현재) government, ranking và sự kiện (event / 이벤트) thay đổi nhanh chỉ thêm khi phục vụ một luận điểm, phải ghi năm và nguồn (source / 소스). Không biến profile thành snapshot dễ lỗi thời.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phương pháp, tên gọi và phạm vi của World Atlas**, **Nội dung bền vững và dữ liệu theo thời điểm** đã nêu tiêu chí phân biệt, còn **Political geography và ranh giới (boundary / 경계) provenance** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Tên tệp (file / 파일) và mã** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Political geography và ranh giới (boundary / 경계) provenance

M49 là hệ thống thống kê; việc dùng M49 không đồng nghĩa Atlas tự đưa ra phán quyết pháp lý. Khi cần mô tả ranh giới (boundary / 경계) hoặc maritime claim, phải dùng nguồn có thẩm quyền phù hợp, ghi thời điểm và thể hiện bất định/tranh chấp bằng wording trung tính.

Bản đồ ranh giới (boundary / 경계) cũng là dữ liệu (data / 데이터) sản phẩm (product / 제품): cần biết nguồn (source / 소스), phiên bản (version / 버전) và quy tắc (rule / 규칙) biểu diễn.

> **Chuyển mạch:** Trong **Phương pháp, tên gọi và phạm vi của World Atlas**, **Political geography và ranh giới (boundary / 경계) provenance** đã nêu tiêu chí phân biệt, còn **Tên tệp (file / 파일) và mã** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Profile priority** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tên tệp (file / 파일) và mã

Nếu có ISO alpha-3, tệp (file / 파일) có thể dùng dạng `KOR_republic_of_korea.md`, `VNM_viet_nam.md`. Mã giúp link ổn định hơn tên hiển thị, nhưng mã không phải bản chất địa lý của territory.

> **Chuyển mạch:** Ở chặng này của **Phương pháp, tên gọi và phạm vi của World Atlas**, **Profile priority** tiếp nhận điểm tựa từ **Tên tệp (file / 파일) và mã** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Definition of Done** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Profile priority

Thứ tự ưu tiên không dựa trên diện tích hoặc “quan trọng hơn” theo giá trị chính trị. Nó dựa trên **học tập (learning / 학습) leverage**: nơi nào giúp hiểu nhiều concept, có liên hệ Korea–Vietnam hoặc có vai trò rõ trong economy/lịch sử (history / 이력)/mạng (network / 네트워크) geography thì được làm sâu trước.

Nhóm đầu gồm East Asia, Southeast Asia, major toàn cục (global / 전역) economies, chokepoint/corridor cases, megadeltas, landlocked states, city-states, archipelagos và resource-system cases.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phương pháp, tên gọi và phạm vi của World Atlas**, **Definition of Done** tiếp nhận điểm tựa từ **Profile priority** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Definition of Done

Một profile chỉ được gắn `Learning profile` khi người đọc có thể trả lời:

- vật lý (physical / 물리적) cấu trúc (structure / 구조) tạo ràng buộc (constraint / 제약조건)/opportunity gì;
- climate/water được tạo bởi cơ chế nào;
- population/urban mẫu (pattern / 패턴) vì sao nằm ở đó;
- môi trường vận hành (production / 운영 환경) và mạng (network / 네트워크) có hình dạng nào;
- bên ngoài (external / 외부) phụ thuộc (dependency / 의존성) và chokepoint nào quan trọng;
- hazard biến thành rủi ro (risk / 위험) qua exposure/vulnerability ra sao;
- claim nào chỉ là mô hình (model / 모델) hoặc có limitation;
- profile nối với prerequisite cốt lõi (core / 핵심) files nào.

Nếu chưa trả lời được, nó vẫn là tham chiếu (reference / 참조), không phải completed content.

> **Bàn giao:** Sau **Definition of Done**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
