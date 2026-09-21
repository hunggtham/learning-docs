# Software law, licenses và intellectual property

Developer thường copy package, code snippet, model/data hoặc deploy service mà không nhận ra đang đi qua legal contracts/licensing boundaries. Chapter này không thay tư vấn pháp lý; mục tiêu là mental model để biết lúc nào technical choice có legal constraint cần kiểm tra.

## Copyright và software

Source code thường được copyright bảo vệ như creative work theo jurisdiction. Copyright controls reproduction/derivative distribution rights; nó không giống patent hay trademark.

Publicly visible source không mặc định cho quyền copy/use tùy ý nếu không có license grant phù hợp.

## Open-source license

Permissive licenses như MIT/BSD/Apache-2.0 thường cho use/modify/distribute rộng với attribution/notice conditions; Apache còn có patent provisions.

Copyleft licenses như GPL yêu cầu source/derivative distribution conditions mạnh hơn trong triggering contexts. LGPL/AGPL có scope/conditions khác.

Không nên suy từ “open source” thành “không có obligations”.

## Dependency license compatibility

Project có nhiều dependencies với licenses khác. Distribution model, linking và modifications có thể ảnh hưởng obligations.

License scanning giúp inventory nhưng edge cases cần legal review, đặc biệt commercial distribution/embedded products.

## SaaS và network copyleft

Một số copyleft obligations trigger khi distribute binaries/source; AGPL có network-interaction provisions nhằm cover server software use case khác.

Architecture deployment model vì vậy có thể thay legal analysis dù code same.

## Patents

Patent bảo vệ inventions/claims trong period/jurisdiction nếu valid. Software patent eligibility khác nhau theo country và domain.

Open-source license có thể grant patent rights hoặc retaliation clauses; đây là reason đọc license beyond copyright sentence.

## Trademark

Trademark bảo vệ source-identifying names/logos. Fork open-source code có thể hợp license code nhưng không có quyền dùng project trademark theo cách gây confusion.

## Data/model licenses

Datasets, fonts, images, pretrained models và APIs có licenses/terms riêng. “Download được” không nghĩa redistribution/commercial use allowed.

AI-generated/AI-training legal questions đang thay đổi nhanh theo jurisdiction, nên current policy/law cần verify riêng khi action thực tế phụ thuộc nó.

## Terms of Service và APIs

API usage chịu contract/rate/data restrictions. Reverse engineering/scraping có legal + technical dimensions khác nhau theo site, jurisdiction và authentication/access controls.

Developer nên escalate khi business model phụ thuộc interpretation mơ hồ thay vì giả định.

## Compliance as engineering constraint

Legal retention, export control, privacy or accessibility requirements có thể ảnh hưởng architecture. Compliance tốt biến rules thành requirements/tests/audit evidence thay vì checklist cuối release.

## Common Misconceptions

**“Có trên GitHub là dùng tự do.”** Không license hoặc license restrictive vẫn có copyright implications.

**“MIT nghĩa không cần làm gì.”** Thường vẫn có copyright/license notice obligations.

**“Legal là việc sau khi code xong.”** License/data/location requirements có thể buộc đổi architecture/product model.

## Mental Model

> Code/data/artifact luôn đi kèm rights và obligations. Technical dependency graph cũng là legal dependency graph ở một mức nào đó.

## Kết nối

Đọc [package/supply chain](../07_security_reliability/08_supply_chain_and_secure_software_lifecycle.md), [version control/packages](../08_software_systems/01_version_control_build_link_and_packages.md) và [professional responsibility](./00_computing_ethics_privacy_and_professional_responsibility.md).