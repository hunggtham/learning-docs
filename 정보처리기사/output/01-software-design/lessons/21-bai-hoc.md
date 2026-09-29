# 12. UI 및 아키텍처 설계 심화 (Thiết kế UI & Kiến trúc chuyên sâu)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **12. UI 및 아키텍처 설계 심화 (Thiết kế UI & Kiến trúc chuyên sâu)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **12. UI 및 아키텍처 설계 심화 (Thiết kế UI & Kiến trúc chuyên sâu)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **5. 요구공학 (Requirements Engineering)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

아키텍처, 설계, 심화

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **1. 사용자 인터페이스 (User Interface - UI)**에서 만든 기준을 이어받아 **12. UI 및 아키텍처 설계 심화 (Thiết kế UI & Kiến trúc chuyên sâu)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **12. UI 및 아키텍처 설계 심화 (Thiết kế UI & Kiến trúc chuyên sâu)** và nối nó với **5. 요구공학 (Requirements Engineering)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 12. UI 및 아키텍처 설계 심화 (Thiết kế UI & Kiến trúc chuyên sâu)

Từ **1. 사용자 인터페이스 (User Interface - UI)**, ta đã có điểm tựa để bước vào **12. UI 및 아키텍처 설계 심화 (Thiết kế UI & Kiến trúc chuyên sâu)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 21/69 trước khi đi vào chi tiết.

Để đọc **12. UI 및 아키텍처 설계 심화 (Thiết kế UI & Kiến trúc chuyên sâu)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **사용자 인터페이스(UI) 추가 유형 (Các loại UI bổ sung)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 사용자 인터페이스(UI) 추가 유형 (Các loại UI bổ sung)

Các ý ngay dưới **사용자 인터페이스(UI) 추가 유형 (Các loại UI bổ sung)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “사용자 인터페이스(UI) 추가 유형 (Các loại UI bổ sung)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **VUI (Voice User Interface):** 사람의 음성으로 기기를 조작하는 인터페이스. (Giao diện điều khiển bằng giọng nói - VD: Bixby, Alexa).
- **OUI (Organic User Interface):** 모든 사물과 사용자 간의 상호작용을 위한 인터페이스 (사물 인터넷, VR, AR, MR 등). (Giao diện hữu cơ, tương tác vật lý/thực tế ảo).

Các bullet của **사용자 인터페이스(UI) 추가 유형 (Các loại UI bổ sung)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **사용자 인터페이스(UI) 추가 유형 (Các loại UI bổ sung)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **사용자 인터페이스 설계 지침 (Hướng dẫn thiết kế UI)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **사용자 인터페이스 설계 지침 (Hướng dẫn thiết kế UI)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 사용자 인터페이스 설계 지침 (Hướng dẫn thiết kế UI)

Bây giờ ta đi vào nội dung của **사용자 인터페이스 설계 지침 (Hướng dẫn thiết kế UI)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “사용자 인터페이스 설계 지침 (Hướng dẫn thiết kế UI)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **사용자 중심 (User-centric):** 실사용자에 대한 이해가 바탕이 되어야 함. (Dựa trên sự hiểu biết về người dùng thực tế).
- **사용성 (Usability):** 설계 시 가장 우선적으로 고려해야 함. (Ưu tiên hàng đầu khi thiết kế - dễ hiểu, dễ dùng).
- **심미성 (Aesthetics):** 디자인적으로 완성도 높게 그래픽 요소 배치. (Bố trí đồ họa thẩm mỹ cao).
- **오류 발생 해결 (Error Recovery):** 오류 발생 시 쉽게 인지하고 해결할 수 있도록 설계. (Giúp user dễ nhận biết và khắc phục lỗi).

Các bullet của **사용자 인터페이스 설계 지침 (Hướng dẫn thiết kế UI)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **사용자 인터페이스 설계 지침 (Hướng dẫn thiết kế UI)**, đừng bắt đầu lại từ số không. **UI 설계 도구 심화 (Công cụ thiết kế UI chi tiết)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **UI 설계 도구 심화 (Công cụ thiết kế UI chi tiết)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### UI 설계 도구 심화 (Công cụ thiết kế UI chi tiết)

Phần nguồn của **UI 설계 도구 심화 (Công cụ thiết kế UI chi tiết)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “UI 설계 도구 심화 (Công cụ thiết kế UI chi tiết)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **와이어프레임 (Wireframe):** 개략적인 레이아웃이나 뼈대 설계 (손그림, 스케치). (Khung xương, layout sơ lược).
- **목업 (Mockup):** 실제 화면과 유사하게 만든 정적인 형태의 모형. (Mô hình tĩnh giống thật nhưng không chạy được logic).
- **스토리보드 (Storyboard):** 와이어프레임 + 콘텐츠 설명 + 페이지 이동 흐름. 디자이너/개발자의 최종 참고 문서. (Tài liệu chi tiết nhất gồm wireframe + mô tả nội dung + luồng di chuyển).
- **프로토타입 (Prototype):** 인터랙션을 적용하여 실제 구현된 것처럼 테스트 가능한 동적인 모형. (Mô hình động có tương tác, test thử được).
- **유스케이스 (Use Case):** 사용자 측면의 요구사항 기술. (Mô tả yêu cầu chức năng từ góc nhìn người dùng).

---

- **물리적 설계 (Thiết kế vật리):** 디스크에 저장될 물리적 구조(저장 레코드, 인덱스, 접근 경로) 설계. 성능 고려. (Thiết kế lưu trữ ổ đĩa, index, tối ưu hiệu năng).
- **구현 (Triển khai):** DDL로 DB 생성. (Code SQL tạo DB).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **YKLVC** (Yêu - Khái - Logic - Vật - Cụ): **Yêu Không Lo Về Cửa**.

Các bullet của **UI 설계 도구 심화 (Công cụ thiết kế UI chi tiết)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **UI 설계 도구 심화 (Công cụ thiết kế UI chi tiết)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Điểm chốt của **12. UI 및 아키텍처 설계 심화 (Thiết kế UI & Kiến trúc chuyên sâu)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **5. 요구공학 (Requirements Engineering)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.