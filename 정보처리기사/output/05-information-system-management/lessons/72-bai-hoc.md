# 침입 탐지 시스템 (IDS; Intrusion Detection System)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **침입 탐지 시스템 (IDS; Intrusion Detection System)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **침입 탐지 시스템 (IDS; Intrusion Detection System)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **리눅스의 커널 로그 (Linux Kernel Logs)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

침입, 탐지, 시스템

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **교착상태 (Dead Lock)**에서 만든 기준을 이어받아 **침입 탐지 시스템 (IDS; Intrusion Detection System)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **침입 탐지 시스템 (IDS; Intrusion Detection System)** và nối nó với **리눅스의 커널 로그 (Linux Kernel Logs)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 침입 탐지 시스템 (IDS; Intrusion Detection System)

Từ **교착상태 (Dead Lock)**, ta đã có điểm tựa để bước vào **침입 탐지 시스템 (IDS; Intrusion Detection System)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 72/86 trước khi đi vào chi tiết.

Để đọc **침입 탐지 시스템 (IDS; Intrusion Detection System)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **오용 탐지 (Misuse Detection)**, **이상 탐지 (Anomaly Detection)**, **종류**, **HIDS (Host-Based)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

컴퓨터 시스템의 비정상적인 사용, 오용, 남용 등을 실시간으로 탐지하는 시스템.
- **오용 탐지 (Misuse Detection)**: 미리 입력해 둔 공격 패턴 감지 (시그니처 기반).
- **이상 탐지 (Anomaly Detection)**: 평균적인 상태를 기준으로 비정상 행위 감지 (행위 기반).
- **종류**:
  - **HIDS (Host-Based)**: 내부 시스템 감시 (OSSEC 등).
  - **NIDS (Network-Based)**: 외부로부터의 네트워크 트래픽 감시 (Snort 등).

Điểm chốt của **침입 탐지 시스템 (IDS; Intrusion Detection System)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **리눅스의 커널 로그 (Linux Kernel Logs)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.