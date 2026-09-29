# 2. 접근 제어 정책 (Access Control Policies)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **2. 접근 제어 정책 (Access Control Policies)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **2. 접근 제어 정책 (Access Control Policies)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **318. 소프트웨어 재사용 (Software Reuse / Tái sử dụng phần mềm)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

접근, 제어, 정책

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **1. 인증 기술 (Authentication Types)**에서 만든 기준을 이어받아 **2. 접근 제어 정책 (Access Control Policies)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **2. 접근 제어 정책 (Access Control Policies)** và nối nó với **318. 소프트웨어 재사용 (Software Reuse / Tái sử dụng phần mềm)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 2. 접근 제어 정책 (Access Control Policies)

Từ **1. 인증 기술 (Authentication Types)**, ta đã có điểm tựa để bước vào **2. 접근 제어 정책 (Access Control Policies)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 60/61 trước khi đi vào chi tiết.

Để đọc **2. 접근 제어 정책 (Access Control Policies)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **DAC (임의적 접근 통제 / Discretionary)**, **MAC (강제적 접근 통제 / Mandatory)**, **RBAC (역할 기반 접근 통제 / Role-Based)**, **방화벽 (Firewall)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **DAC (임의적 접근 통제 / Discretionary)**: 신분(Identity) 기반. 데이터 소유자가 권한 부여.
- **MAC (강제적 접근 통제 / Mandatory)**: 보안등급(Label) 기반. 시스템 관리자가 강제로 권한 부여.
- **RBAC (역할 기반 접근 통제 / Role-Based)**: 역할(Role) 기반. 변경이 용이.
- 💡 **Mẹo ghi nhớ**: DAC = Danh tính, MAC = Mức độ bảo mật, RBAC = Role (Vai trò).

---

# 110 네트워크 보안 솔루션 (Network Security Solutions)

Phần **110 네트워크 보안 솔루션 (Network Security Solutions)** cần được đọc như một bước trong bài giảng: trước hết xác định mục đích, sau đó nối các ý bên dưới với điều kiện và hệ quả trước khi ghi nhớ từng dòng.
- **방화벽 (Firewall)**: 트래픽 접근 허용/차단 (Tường lửa cơ bản).
- **WAF (웹 방화벽)**: SQL 인젝션, XSS 등 웹 특화 공격 방어 (Tường lửa chuyên cho Web).
- **IDS (침입 탐지 시스템)**: 침입을 실시간으로 "탐지(Detect)" (Hệ thống phát hiện xâm nhập).
- **IPS (침입 방지 시스템)**: 유해 트래픽을 실시간으로 "차단(Prevent)" (Hệ thống ngăn chặn xâm nhập).
- **VPN (가상사설망)**: 공중망을 전용망처럼 안전하게 사용 (Mạng riêng ảo).

---

Điểm chốt của **2. 접근 제어 정책 (Access Control Policies)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **318. 소프트웨어 재사용 (Software Reuse / Tái sử dụng phần mềm)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.