# A+ Deep Dive: 개발 모형 선택과 요구사항 검증

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **A+ Deep Dive: 개발 모형 선택과 요구사항 검증**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **A+ Deep Dive: 개발 모형 선택과 요구사항 검증** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **1. 현행 시스템 분석 (Current System Analysis)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

Deep, Dive, 개발, 모형, 선택과, 요구사항, 검증

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **12. 요구사항 (Requirements)**에서 만든 기준을 이어받아 **A+ Deep Dive: 개발 모형 선택과 요구사항 검증**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **A+ Deep Dive: 개발 모형 선택과 요구사항 검증** và nối nó với **1. 현행 시스템 분석 (Current System Analysis)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## A+ Deep Dive: 개발 모형 선택과 요구사항 검증

Sau khi đã đặt nền bằng **12. 요구사항 (Requirements)**, ta chuyển sang **A+ Deep Dive: 개발 모형 선택과 요구사항 검증**. Đây là mắt xích 11/57 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **A+ Deep Dive: 개발 모형 선택과 요구사항 검증** như một bài học cho người mới, hãy giữ câu hỏi: **một nhu cầu nghiệp vụ được chuyển thành yêu cầu có thể kiểm tra và bàn giao như thế nào?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng là bằng chứng để so sánh các lựa chọn theo cùng tiêu chí, không phải danh sách cần học thuộc từng ô.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **1. 모형 선택 비교표**. Hãy xác định **1. 모형 선택 비교표** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 1. 모형 선택 비교표

Phần nguồn của **1. 모형 선택 비교표** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

| 모형 | 가장 강한 신호 | 변경 대응 | 시험 함정 |
|---|---|---|---|
| 폭포수 (Waterfall) | 요구사항이 안정적이고 단계 산출물이 명확함 | 낮음 | 순차적이라는 뜻이 곧 테스트가 없다는 뜻은 아님 |
| 프로토타입 (Prototype) | 사용자가 원하는 결과를 말로 확정하기 어려움 | 요구사항 확인에 유리 | 시제품을 그대로 운영 제품으로 착각하지 않음 |
| 나선형 (Spiral) | 대규모·고위험·불확실성이 큼 | 반복마다 위험 분석 | 보헴(Boehm)과 연결되는 모형은 나선형 |
| 애자일 (Agile) | 짧은 주기와 지속적인 고객 피드백 | 높음 | Agile은 단일 방법론이 아니라 가치와 원칙의 묶음 |

Bảng trong **1. 모형 선택 비교표** không phải danh sách rời. Hãy đọc theo từng cột để nhận ra tiêu chí so sánh, rồi tự diễn đạt bằng một câu: đối tượng nào khác nhau ở điểm nào và trong điều kiện nào sự khác biệt đó có ý nghĩa.

Ta vừa chốt **1. 모형 선택 비교표** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. 요구사항 검증 미니 트레이스** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **2. 요구사항 검증 미니 트레이스** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 2. 요구사항 검증 미니 트레이스

Các ý ngay dưới **2. 요구사항 검증 미니 트레이스** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

1. **완전성(Completeness)**: 모든 기능·제약이 빠짐없이 적혔는가?
2. **일관성(Consistency)**: 서로 모순되는 요구가 없는가?
3. **추적성(Traceability)**: 요구사항 ID가 설계·테스트 항목과 연결되는가?
4. **검증 가능성(Verifiability)**: `빠른 응답` 대신 `95% 요청을 2초 이내 처리`처럼 시험 가능한가?

> **시험 함정:** 검증(Verification)은 명세에 맞게 만들었는지, 확인(Validation)은 사용자의 실제 목적에 맞는지를 묻는다.

Phần **2. 요구사항 검증 미니 트레이스** không có nhiều dữ liệu rời để tách nhỏ, vì vậy hãy giữ câu hỏi mục đích và tự chốt bằng một câu giải thích trước khi đi tiếp.

Sau khi đọc **2. 요구사항 검증 미니 트레이스**, đừng bắt đầu lại từ số không. **자주 혼동하는 판별 포인트** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **자주 혼동하는 판별 포인트**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 자주 혼동하는 판별 포인트

Bây giờ ta đi vào nội dung của **자주 혼동하는 판별 포인트**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- **형상 관리 항목**은 소스 코드만이 아니라 요구사항·설계서·설치/운영 문서처럼 변경 이력을 추적해야 하는 산출물까지 포함한다. 개인 일정이나 예산 자체는 형상 항목이 아니다.
- **EAI Hybrid**는 Hub-and-Spoke와 Message Bus를 조합한다. 모든 애플리케이션을 직접 연결하는 Point-to-Point와 다르다.
- **N-S 차트**는 순차·선택·반복이라는 구조적 제어 흐름을 표현한다. 클래스 메모리 배치나 패킷 헤더를 표현하는 도구가 아니다.
- 내부 자료를 직접 참조하는 모듈은 **내용 결합도**가 강하다. 독립성을 높이려면 결합도는 낮추고 응집도는 높인다.

Các bullet của **자주 혼동하는 판별 포인트** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **자주 혼동하는 판별 포인트** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Ta có thể khép mục **A+ Deep Dive: 개발 모형 선택과 요구사항 검증** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **1. 현행 시스템 분석 (Current System Analysis)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.