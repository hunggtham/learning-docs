# 13. 소프트웨어 품질 및 아키텍처 패턴 (Chất lượng SW & Mẫu Kiến trúc)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **13. 소프트웨어 품질 및 아키텍처 패턴 (Chất lượng SW & Mẫu Kiến trúc)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **13. 소프트웨어 품질 및 아키텍처 패턴 (Chất lượng SW & Mẫu Kiến trúc)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **1. 소프트웨어 아키텍처 (Software Architecture)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

소프트웨어, 품질, 아키텍처, 패턴

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **5. 소프트웨어 아키텍처 및 설계 (Kiến trúc và Thiết kế Phần mềm)**에서 만든 기준을 이어받아 **13. 소프트웨어 품질 및 아키텍처 패턴 (Chất lượng SW & Mẫu Kiến trúc)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 13. 소프트웨어 품질 및 아키텍처 패턴 (Chất lượng SW & Mẫu Kiến trúc)

Sau khi đã đặt nền bằng **5. 소프트웨어 아키텍처 및 설계 (Kiến trúc và Thiết kế Phần mềm)**, ta chuyển sang **13. 소프트웨어 품질 및 아키텍처 패턴 (Chất lượng SW & Mẫu Kiến trúc)**. Đây là mắt xích 23/55 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **13. 소프트웨어 품질 및 아키텍처 패턴 (Chất lượng SW & Mẫu Kiến trúc)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **ISO/IEC 9126 하위 품질 특성 (Đặc tính con của ISO/IEC 9126)**. Hãy xác định **ISO/IEC 9126 하위 품질 특성 (Đặc tính con của ISO/IEC 9126)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### ISO/IEC 9126 하위 품질 특성 (Đặc tính con của ISO/IEC 9126)

Phần nguồn của **ISO/IEC 9126 하위 품질 특성 (Đặc tính con của ISO/IEC 9126)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- *Đây là phần rất hay thi, cần ghi nhớ chi tiết.*
- **기능성 (Functionality):** 적절성 (Suitability), 정밀성 (Accuracy), 상호 운용성 (Interoperability), 보안성 (Security), 준수성 (Compliance).
- **신뢰성 (Reliability):** 성숙성 (Maturity), 고장 허용성 (Fault Tolerance), 회복성 (Recoverability).
- **사용성 (Usability):** 이해성 (Understandability), 학습성 (Learnability), 운용성 (Operability), 친밀성 (Attractiveness).
- **효율성 (Efficiency):** 시간 효율성 (Time Behaviour), 자원 효율성 (Resource Behaviour).
- **유지 보수성 (Maintainability):** 분석성 (Analyzability), 변경성 (Changeability), 안정성 (Stability), 시험성 (Testability).
- **이식성 (Portability):** 적용성 (Adaptability), 설치성 (Installability), 대체성 (Replaceability), 공존성 (Co-existence).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **KTSHDD** (Kỳ - Tín - Sử - Hiệu - Duy - Di): **Không Tin Sẽ Hư Dần Dần** (Tên 6 đặc tính chính).
  - 유지 보수성: **분변안시** (Phân - Biến - An - Thử).

Các bullet của **ISO/IEC 9126 하위 품질 특성 (Đặc tính con của ISO/IEC 9126)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **ISO/IEC 9126 하위 품질 특성 (Đặc tính con của ISO/IEC 9126)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **관련 품질 표준 (Các tiêu chuẩn ISO khác)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **관련 품질 표준 (Các tiêu chuẩn ISO khác)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 관련 품질 표준 (Các tiêu chuẩn ISO khác)

Các ý ngay dưới **관련 품질 표준 (Các tiêu chuẩn ISO khác)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- **ISO/IEC 25010:** 2011년 9126을 개정한 최신 표준. (Bản cập nhật của 9126).
- **ISO/IEC 12119:** 테스트 절차를 포함한 품질 표준. (Bao gồm quy trình test).
- **ISO/IEC 14598:** 평가자별 제품 평가 활동 규정. (Quy định hoạt động đánh giá).

Các bullet của **관련 품질 표준 (Các tiêu chuẩn ISO khác)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **관련 품질 표준 (Các tiêu chuẩn ISO khác)**, đừng bắt đầu lại từ số không. **기타 아키텍처 패턴 (Các mẫu kiến trúc bổ sung)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **기타 아키텍처 패턴 (Các mẫu kiến trúc bổ sung)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 기타 아키텍처 패턴 (Các mẫu kiến trúc bổ sung)

Bây giờ ta đi vào nội dung của **기타 아키텍처 패턴 (Các mẫu kiến trúc bổ sung)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- **마스터-슬레이브 패턴 (Master-Slave):** 마스터가 작업을 분할하고 슬레이브가 처리 결과를 돌려주는 패턴 (장애 허용 시스템, 병렬 컴퓨팅). (Master chia việc, Slave làm rồi trả kết quả -> Hệ thống tính toán song song).
- **브로커 패턴 (Broker):** 사용자가 요청하면 브로커가 적합한 컴포넌트를 연결해 줌 (분산 환경). (Môi giới kết nối User với Component phù hợp -> Hệ thống phân tán).
- **피어-투-피어 패턴 (Peer-To-Peer / P2P):** 각 피어가 클라이언트도 되고 서버도 됨. (Mỗi node vừa là Client vừa là Server).
- **이벤트-버스 패턴 (Event-Bus):** 소스가 이벤트를 발행(Publish)하면 리스너가 구독(Subscribe)하여 처리. (Mô hình Pub/Sub).
- **블랙보드 패턴 (Blackboard):** 모든 컴포넌트가 공유 데이터 저장소(블랙보드)에 접근 (음성 인식, 신호 해석). (Bảng đen dùng chung, các AI agents tự do truy cập -> Nhận diện giọng nói, xử lý tín hiệu).

Các bullet của **기타 아키텍처 패턴 (Các mẫu kiến trúc bổ sung)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **기타 아키텍처 패턴 (Các mẫu kiến trúc bổ sung)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Ta có thể khép mục **13. 소프트웨어 품질 및 아키텍처 패턴 (Chất lượng SW & Mẫu Kiến trúc)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **1. 소프트웨어 아키텍처 (Software Architecture)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.