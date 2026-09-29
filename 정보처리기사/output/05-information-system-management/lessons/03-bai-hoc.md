# 프레임워크 특징 및 SW 신기술 (Framework & SW Tech)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **프레임워크 특징 및 SW 신기술 (Framework & SW Tech)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **프레임워크 특징 및 SW 신기술 (Framework & SW Tech)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **5과목 추가: 소프트웨어 재사용, 산정 기법, 프레임워크** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

프레임워크, 특징, 신기술

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **소프트웨어 개발 방법론 테일러링 및 프레임워크 (Tailoring & Framework)**에서 만든 기준을 이어받아 **프레임워크 특징 및 SW 신기술 (Framework & SW Tech)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **프레임워크 특징 및 SW 신기술 (Framework & SW Tech)** và nối nó với **5과목 추가: 소프트웨어 재사용, 산정 기법, 프레임워크**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 프레임워크 특징 및 SW 신기술 (Framework & SW Tech)

Từ **소프트웨어 개발 방법론 테일러링 및 프레임워크 (Tailoring & Framework)**, ta đã có điểm tựa để bước vào **프레임워크 특징 및 SW 신기술 (Framework & SW Tech)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 3/86 trước khi đi vào chi tiết.

Để đọc **프레임워크 특징 및 SW 신기술 (Framework & SW Tech)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **모듈화 (Modularity)**, **재사용성 (Reusability)**, **확장성 (Extensibility)**, **제어의 역흐름 (Inversion of Control)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **1. 프레임워크의 특성 (Characteristics of Framework)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 1. 프레임워크의 특성 (Characteristics of Framework)

Các ý ngay dưới **1. 프레임워크의 특성 (Characteristics of Framework)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “1. 프레임워크의 특성 (Characteristics of Framework)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **모듈화 (Modularity)**: 캡슐화로 모듈화를 강화하여 변경 영향을 최소화.
- **재사용성 (Reusability)**: 재사용 가능한 모듈 제공으로 생산성 향상.
- **확장성 (Extensibility)**: 다형성을 통한 인터페이스 확장.
- **제어의 역흐름 (Inversion of Control)**: 개발자가 아닌 프레임워크가 객체들을 제어하고 통제.

Các bullet của **1. 프레임워크의 특성 (Characteristics of Framework)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **1. 프레임워크의 특성 (Characteristics of Framework)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. SDE (Software-Defined Everything)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **2. SDE (Software-Defined Everything)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 2. SDE (Software-Defined Everything)

Bây giờ ta đi vào nội dung của **2. SDE (Software-Defined Everything)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

하드웨어 자원을 가상화하여 소프트웨어만으로 제어 및 관리하는 기술.
- **SDN**: 소프트웨어 정의 네트워킹 (네트워크 가상화)
- **SDDC**: 소프트웨어 정의 데이터 센터 (데이터 센터 전체 가상화)
- **SDS**: 소프트웨어 정의 스토리지 (스토리지 가상화)

Các bullet của **2. SDE (Software-Defined Everything)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **2. SDE (Software-Defined Everything)**, đừng bắt đầu lại từ số không. **3. 주요 SW 및 관련 용어** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **3. 주요 SW 및 관련 용어**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 3. 주요 SW 및 관련 용어

Phần nguồn của **3. 주요 SW 및 관련 용어** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “3. 주요 SW 및 관련 용어” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **SOA (Service Oriented Architecture)**: 서비스나 컴포넌트 중심으로 구축하는 아키텍처.
- **디지털 트윈 (Digital Twin)**: 물리적 자산을 소프트웨어로 가상화(복제)하여 효율성을 높이는 기술.
- **텐서플로 (TensorFlow)**: 구글이 만든 딥러닝/데이터 흐름용 오픈소스 라이브러리.
- **도커 (Docker)**: 컨테이너(Container) 기술을 자동화하는 오픈소스 프로젝트.

Các bullet của **3. 주요 SW 및 관련 용어** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **3. 주요 SW 및 관련 용어** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Điểm chốt của **프레임워크 특징 및 SW 신기술 (Framework & SW Tech)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **5과목 추가: 소프트웨어 재사용, 산정 기법, 프레임워크**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.