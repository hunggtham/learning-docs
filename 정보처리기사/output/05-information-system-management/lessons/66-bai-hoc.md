# OSI 7계층 참조 모델 (OSI 7 Layer Reference Model)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **OSI 7계층 참조 모델 (OSI 7 Layer Reference Model)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối OSI model với encapsulation, protocol và boundary, để lỗi mạng được khoanh theo lớp.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **OSI 7계층 참조 모델 (OSI 7 Layer Reference Model)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **OSI 7계층 참조 모델 (OSI 7 Layer Reference Model)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **5과목 정보시스템 구축 관리 (Information System Construction Management)** khi chuyển sang phần tiếp theo.

> **Nối mạch:** Trong **OSI 7계층 참조 모델 (OSI 7 Layer Reference Model)**, **핵심 키워드 (Từ khóa)** nối từ **학습 목표 (Mục tiêu)** sang **선행·연결 개념 (Kiến thức liên kết)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 핵심 키워드 (Từ khóa)

OSI, 계층, 참조, 모델

> **Nối mạch:** Ở chặng này của **OSI 7계층 참조 모델 (OSI 7 Layer Reference Model)**, **핵심 키워드 (Từ khóa)** dẫn sang **선행·연결 개념 (Kiến thức liên kết)**, nơi tài liệu chuẩn và vị trí sở hữu được chỉ rõ để biết chỗ đào sâu tiếp; **읽는 방법 (Cách đọc)** mở rộng hệ quả liên quan.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **IP 주소 및 서브네팅 (IP Address & Subnetting)**에서 만든 기준을 이어받아 **OSI 7계층 참조 모델 (OSI 7 Layer Reference Model)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Nối mạch:** Đặt trong câu hỏi lớn của **OSI 7계층 참조 모델 (OSI 7 Layer Reference Model)**, **읽는 방법 (Cách đọc)** nối từ **선행·연결 개념 (Kiến thức liên kết)** sang **OSI 7계층 참조 모델 (OSI 7 Layer Reference Model)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Nối mạch:** Trong **OSI 7계층 참조 모델 (OSI 7 Layer Reference Model)**, **읽는 방법 (Cách đọc)** dẫn sang **OSI 7계층 참조 모델 (OSI 7 Layer Reference Model)**, nơi tài liệu chuẩn và vị trí sở hữu được chỉ rõ để biết chỗ đào sâu tiếp.

## OSI 7계층 참조 모델 (OSI 7 Layer Reference Model)

Từ **IP 주소 및 서브네팅 (IP Address & Subnetting)**, ta đã có điểm tựa để bước vào **OSI 7계층 참조 모델 (OSI 7 Layer Reference Model)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 66/86 trước khi đi vào chi tiết.

Để đọc **OSI 7계층 참조 모델 (OSI 7 Layer Reference Model)** như một bài học cho người mới, hãy giữ câu hỏi: **ta dùng mô hình nào để biểu diễn đối tượng, quan hệ hoặc hành vi, và giới hạn của mỗi cách là gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **물리 계층 (Physical)**, **데이터 링크 계층 (Data Link)**, **네트워크 계층 (Network)**, **전송 계층 (Transport)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

국제표준화기구(ISO)에서 제안한 통신 규약으로, 하위 3계층과 상위 4계층으로 나뉩니다.
- **물리 계층 (Physical)**: 실제 접속, 기계적/전기적 특성 정의.
- **데이터 링크 계층 (Data Link)**: 인접 시스템 간 신뢰성 있는 전송, 흐름 제어, 오류 제어, 동기화.
- **네트워크 계층 (Network)**: 경로 설정(Routing), 트래픽 제어, 패킷 전송.
- **전송 계층 (Transport)**: 종단(End-to-End) 간 신뢰성 있는 데이터 전송, 연결 설정, 다중화.
- **세션 계층 (Session)**: 대화(회화) 제어, 동기 제어.
- **표현 계층 (Presentation)**: 데이터 형식 변환, 암호화, 압축.
- **응용 계층 (Application)**: 사용자에게 통신 서비스 제공.

> **Vietnamese Explanation**:
> Mô hình OSI chia quá trình truyền mạng thành 7 lớp. 3 lớp dưới (Physical, Data Link, Network) lo việc truyền dẫn tín hiệu, tìm đường (routing). 4 lớp trên (Transport, Session, Presentation, Application) lo việc kiểm tra lỗi, mã hóa dữ liệu và giao tiếp với người dùng.

Điểm chốt của **OSI 7계층 참조 모델 (OSI 7 Layer Reference Model)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **5과목 정보시스템 구축 관리 (Information System Construction Management)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

> **Bàn giao:** Sau **OSI 7계층 참조 모델 (OSI 7 Layer Reference Model)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
