# Software law, licenses và intellectual thuộc tính (property / 속성)

> **Mạch đọc:** Đọc **Software law, licenses và intellectual thuộc tính (property / 속성)** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Copyright và software** sang **Open-source license**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Nhà phát triển (developer / 개발자) thường bản sao (copy / 복사) gói (package / 패키지), mã (code / 코드) snippet, mô hình (model / 모델)/dữ liệu (data / 데이터) hoặc deploy dịch vụ (service / 서비스) mà không nhận ra đang đi qua legal contracts/licensing boundaries. Chapter này không thay tư vấn pháp lý; mục tiêu là mô hình tư duy (mental model / 사고 모델) để biết lúc nào technical choice có legal ràng buộc (constraint / 제약조건) cần kiểm tra.

## Copyright và software

Mã nguồn (source code / 소스 코드) thường được copyright bảo vệ như creative công việc (work / 작업) theo jurisdiction. Copyright controls reproduction/derivative phân phối (distribution / 분포) rights; nó không giống patent hay trademark.

Publicly visible nguồn (source / 소스) không mặc định cho quyền bản sao (copy / 복사)/use tùy ý nếu không có license grant phù hợp.


> **Chuyển mạch:** Từ **Copyright và software**, ta sang **Open-source license** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Open-source license

Permissive licenses như MIT/BSD/Apache-2.0 thường cho use/modify/distribute rộng với attribution/notice conditions; Apache còn có patent provisions.

Copyleft licenses như GPL yêu cầu nguồn (source / 소스)/derivative phân phối (distribution / 분포) conditions mạnh hơn trong triggering contexts. LGPL/AGPL có phạm vi (scope / 범위)/conditions khác.

Không nên suy từ “open nguồn (source / 소스)” thành “không có obligations”.


> **Chuyển mạch:** Từ **Open-source license**, ta sang **phụ thuộc (dependency / 의존성) license tính tương thích (compatibility / 호환성)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Phụ thuộc (dependency / 의존성) license tính tương thích (compatibility / 호환성)

Dự án (project / 프로젝트) có nhiều dependencies với licenses khác. phân phối (distribution / 분포) mô hình (model / 모델), linking và modifications có thể ảnh hưởng obligations.

License scanning giúp inventory nhưng edge cases cần legal rà soát (review / 검토), đặc biệt commercial phân phối (distribution / 분포)/embedded products.


> **Chuyển mạch:** Từ **phụ thuộc (dependency / 의존성) license tính tương thích (compatibility / 호환성)**, ta sang **SaaS và mạng (network / 네트워크) copyleft** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## SaaS và mạng (network / 네트워크) copyleft

Một số copyleft obligations trigger khi distribute binaries/nguồn (source / 소스); AGPL có network-interaction provisions nhằm cover máy chủ (server / 서버) software use trường hợp (case / 사례) khác.

Kiến trúc (architecture / 아키텍처) triển khai (deployment / 배포) mô hình (model / 모델) vì vậy có thể thay legal phân tích (analysis / 분석) dù mã (code / 코드) same.


> **Chuyển mạch:** Từ **SaaS và mạng (network / 네트워크) copyleft**, ta sang **Patents** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Patents

Patent bảo vệ inventions/claims trong period/jurisdiction nếu valid. Software patent eligibility khác nhau theo country và lĩnh vực (domain / 도메인).

Open-source license có thể grant patent rights hoặc retaliation clauses; đây là reason đọc license beyond copyright sentence.


> **Chuyển mạch:** Từ **Patents**, ta sang **Trademark** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Trademark

Trademark bảo vệ source-identifying names/logos. Fork open-source mã (code / 코드) có thể hợp license mã (code / 코드) nhưng không có quyền dùng dự án (project / 프로젝트) trademark theo cách gây confusion.


> **Chuyển mạch:** Từ **Trademark**, ta sang **dữ liệu (data / 데이터)/mô hình (model / 모델) licenses** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Dữ liệu (data / 데이터)/mô hình (model / 모델) licenses

Datasets, fonts, images, pretrained các mô hình (models / 모델들) và APIs có licenses/terms riêng. “Download được” không nghĩa redistribution/commercial use allowed.

AI-generated/AI-training legal questions đang thay đổi nhanh theo jurisdiction, nên hiện tại (current / 현재) chính sách (policy / 정책)/law cần verify riêng khi hành động (action / 동작) thực tế phụ thuộc nó.


> **Chuyển mạch:** Từ **dữ liệu (data / 데이터)/mô hình (model / 모델) licenses**, ta sang **Terms of dịch vụ (service / 서비스) và APIs** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Terms of dịch vụ (service / 서비스) và APIs

API usage chịu đặc tả hợp đồng (contract / 계약)/tỷ lệ (rate / 비율)/dữ liệu (data / 데이터) restrictions. Reverse kỹ thuật (engineering / 엔지니어링)/scraping có legal + technical dimensions khác nhau theo site, jurisdiction và authentication/truy cập (access / 접근) controls.

Nhà phát triển (developer / 개발자) nên escalate khi nghiệp vụ (business / 비즈니스) mô hình (model / 모델) phụ thuộc interpretation mơ hồ thay vì giả định.


> **Chuyển mạch:** Từ **Terms of dịch vụ (service / 서비스) và APIs**, ta sang **Compliance as kỹ thuật (engineering / 엔지니어링) ràng buộc (constraint / 제약조건)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Compliance as kỹ thuật (engineering / 엔지니어링) ràng buộc (constraint / 제약조건)

Legal retention, export điều khiển (control / 제어), privacy or khả năng tiếp cận (accessibility / 접근성) requirements có thể ảnh hưởng kiến trúc (architecture / 아키텍처). Compliance tốt biến rules thành requirements/tests/kiểm tra (audit / 감사) bằng chứng (evidence / 증거) thay vì checklist cuối bản phát hành (release / 릴리스).


> **Chuyển mạch:** Từ **Compliance as kỹ thuật (engineering / 엔지니어링) ràng buộc (constraint / 제약조건)**, ta sang **dùng chung (common / 공통) Misconceptions** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

**“Có trên GitHub là dùng tự do.”** Không license hoặc license restrictive vẫn có copyright implications.

**“MIT nghĩa không cần làm gì.”** Thường vẫn có copyright/license notice obligations.

**“Legal là việc sau khi mã (code / 코드) xong.”** License/dữ liệu (data / 데이터)/location requirements có thể buộc đổi kiến trúc (architecture / 아키텍처)/sản phẩm (product / 제품) mô hình (model / 모델).


> **Chuyển mạch:** Từ **dùng chung (common / 공통) Misconceptions**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> mã (code / 코드)/dữ liệu (data / 데이터)/sản phẩm tạo ra (artifact / 산출물) luôn đi kèm rights và obligations. Technical phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) cũng là legal phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) ở một mức nào đó.


> **Chuyển mạch:** Từ **mô hình tư duy (mental model / 사고 모델)**, ta sang **Kết nối** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Kết nối

Đọc [package/supply chain](../07_security_reliability/08_supply_chain_and_secure_software_lifecycle.md), [version control/packages](../08_software_systems/01_version_control_build_link_and_packages.md) và [professional responsibility](./00_computing_ethics_privacy_and_professional_responsibility.md).

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 computing ethics privacy and professional responsibility](./00_computing_ethics_privacy_and_professional_responsibility.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
