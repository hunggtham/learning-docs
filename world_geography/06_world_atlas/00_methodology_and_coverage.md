# Phương pháp, tên gọi và phạm vi của World Atlas

> **Mạch đọc:** Đặt **Phương pháp, tên gọi và phạm vi của World Atlas** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Inventory và học tập (learning / 학습) profile là hai bài toán khác nhau** sang **Cấu trúc tệp (file / 파일) không phải tuyên bố chủ quyền**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


## Inventory và học tập (learning / 학습) profile là hai bài toán khác nhau

Cụm “mọi quốc gia và vùng lãnh thổ” có nhiều lớp thống kê và pháp lý. Để inventory không tùy ý, dự án (project / 프로젝트) dùng **UN M49** làm baseline cho danh mục `countries or areas`, với ISO 3166 làm tham chiếu bổ trợ khi phù hợp.

Việc một entry nằm trong inventory không buộc phải có một chapter riêng. Inventory giải quyết **completeness của danh sách**; học tập (learning / 학습) profile giải quyết **giá trị giáo dục**.


> **Chuyển mạch:** Từ **Inventory và học tập (learning / 학습) profile là hai bài toán khác nhau**, ta sang **Cấu trúc tệp (file / 파일) không phải tuyên bố chủ quyền** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cấu trúc tệp (file / 파일) không phải tuyên bố chủ quyền

Nếu một không gian được phân tích riêng, điều đó chỉ có nghĩa nó hữu ích cho địa lý. Folder, tên tệp (file / 파일) và mã không được dùng như kết luận về chủ quyền, tính chính danh hoặc đường biên.

Với khu vực có cách phân loại khác nhau giữa hệ thống quốc tế, profile phải ghi provenance và tách: hệ phân loại thống kê, tình trạng/quan điểm theo nguồn và cấu trúc địa lý đang phân tích. Không suy ý định chính trị từ bản đồ.


> **Chuyển mạch:** Từ **Cấu trúc tệp (file / 파일) không phải tuyên bố chủ quyền**, ta sang **Không tạo stub để chạy coverage** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Không tạo stub để chạy coverage

Một template có vài câu không phải profile. Từ kiểm tra (audit / 감사) này, quy tắc là:

- không auto-generate country files từ inventory;
- không đánh dấu completed chỉ vì tệp (file / 파일) tồn tại;
- không dùng số line/heading như chỉ số (metric / 지표) chất lượng;
- không bản sao (copy / 복사) cùng một đoạn cho hàng chục country rồi đổi tên;
- nếu trường hợp (case / 사례) không có đủ giá trị độc lập, gộp vào regional/comparative chapter.

Các stub legacy từ batch trước chỉ là transitional tham chiếu (reference / 참조) và sẽ được promote/merge/remove khi Atlas được cleanup.


> **Chuyển mạch:** Từ **Không tạo stub để chạy coverage**, ta sang **Bốn trạng thái nội dung** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Bốn trạng thái nội dung

**Inventory only:** chỉ có entry trong danh mục.

**tham chiếu (reference / 참조):** có ghi chú ngắn để định vị nhưng chưa đủ làm bài học.

**học tập (learning / 학습) profile:** có chuỗi nhân quả (causal chain / 인과 사슬) hoàn chỉnh, misconception, mô hình tư duy (mental model / 사고 모델) và cross-link.

**Deep comparative profile:** ngoài học tập (learning / 학습) profile còn so sánh cơ chế với nơi khác, giải thích mạng (network / 네트워크) phụ thuộc (dependency / 의존성) và nối nhiều lĩnh vực (domain / 도메인) cốt lõi (core / 핵심).

Chỉ hai trạng thái cuối được tính vào educational coverage.


> **Chuyển mạch:** Từ **Bốn trạng thái nội dung**, ta sang **Profile phải có thesis, không chỉ template** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Profile phải có thesis, không chỉ template

Mỗi profile nên trả lời một câu thesis, ví dụ: “địa lý của nơi này được tổ chức bởi một megadelta + export corridor + monsoon regime” hoặc “mountain water tower + landlocked trade dependence”.

Các section sau phải chứng minh thesis. Nếu heading đầy đủ nhưng nội dung chỉ lặp fact, profile vẫn chưa đạt.


> **Chuyển mạch:** Từ **Profile phải có thesis, không chỉ template**, ta sang **Nội dung bền vững và dữ liệu theo thời điểm** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Nội dung bền vững và dữ liệu theo thời điểm

Ưu tiên vị trí, relief, basin, climate regime, population mẫu (pattern / 패턴), urban hierarchy, môi trường vận hành (production / 운영 환경) belt, cổng (port / 포트)/corridor và hazard cơ chế (mechanism / 메커니즘).

Population/GDP/trade share, hiện tại (current / 현재) government, ranking và sự kiện (event / 이벤트) thay đổi nhanh chỉ thêm khi phục vụ một luận điểm, phải ghi năm và nguồn (source / 소스). Không biến profile thành snapshot dễ lỗi thời.


> **Chuyển mạch:** Từ **Nội dung bền vững và dữ liệu theo thời điểm**, ta sang **Political geography và ranh giới (boundary / 경계) provenance** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Political geography và ranh giới (boundary / 경계) provenance

M49 là hệ thống thống kê; việc dùng M49 không đồng nghĩa Atlas tự đưa ra phán quyết pháp lý. Khi cần mô tả ranh giới (boundary / 경계) hoặc maritime claim, phải dùng nguồn có thẩm quyền phù hợp, ghi thời điểm và thể hiện bất định/tranh chấp bằng wording trung tính.

Bản đồ ranh giới (boundary / 경계) cũng là dữ liệu (data / 데이터) sản phẩm (product / 제품): cần biết nguồn (source / 소스), phiên bản (version / 버전) và quy tắc (rule / 규칙) biểu diễn.


> **Chuyển mạch:** Từ **Political geography và ranh giới (boundary / 경계) provenance**, ta sang **Tên tệp (file / 파일) và mã** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Tên tệp (file / 파일) và mã

Nếu có ISO alpha-3, tệp (file / 파일) có thể dùng dạng `KOR_republic_of_korea.md`, `VNM_viet_nam.md`. Mã giúp link ổn định hơn tên hiển thị, nhưng mã không phải bản chất địa lý của territory.


> **Chuyển mạch:** Từ **Tên tệp (file / 파일) và mã**, ta sang **Profile priority** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Profile priority

Thứ tự ưu tiên không dựa trên diện tích hoặc “quan trọng hơn” theo giá trị chính trị. Nó dựa trên **học tập (learning / 학습) leverage**: nơi nào giúp hiểu nhiều concept, có liên hệ Korea–Vietnam hoặc có vai trò rõ trong economy/lịch sử (history / 이력)/mạng (network / 네트워크) geography thì được làm sâu trước.

Nhóm đầu gồm East Asia, Southeast Asia, major toàn cục (global / 전역) economies, chokepoint/corridor cases, megadeltas, landlocked states, city-states, archipelagos và resource-system cases.


> **Chuyển mạch:** Từ **Profile priority**, ta sang **Definition of Done** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

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

> **Bàn giao:** Sau **Definition of Done**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 global inventory](./01_global_inventory.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
