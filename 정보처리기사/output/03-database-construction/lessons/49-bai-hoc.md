# 199-200. 접근통제 모델 심화 (Access Control Models Deep Dive)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **199-200. 접근통제 모델 심화 (Access Control Models Deep Dive)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **199-200. 접근통제 모델 심화 (Access Control Models Deep Dive)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **220-230. 하위 질의, 트리거, DBMS 접속 및 데이터 전환** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

접근통제, 모델, 심화

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **194. 파티션 (Partition)**에서 만든 기준을 이어받아 **199-200. 접근통제 모델 심화 (Access Control Models Deep Dive)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 199-200. 접근통제 모델 심화 (Access Control Models Deep Dive)

Ở bước 49/55, **199-200. 접근통제 모델 심화 (Access Control Models Deep Dive)** xuất hiện như phần tiếp nối của **194. 파티션 (Partition)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **199-200. 접근통제 모델 심화 (Access Control Models Deep Dive)** như một bài học cho người mới, hãy giữ câu hỏi: **ta dùng mô hình nào để biểu diễn đối tượng, quan hệ hoặc hành vi, và giới hạn của mỗi cách là gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **DAC (임의 접근통제):** 데이터 소유자가 사용자 신원에 따라 권한 부여 (GRANT/REVOKE).
- **MAC (강제 접근통제):** 시스템이 주체와 객체의 보안 등급을 비교해 권한 부여.
  - **벨 라파듈라 (Bell-LaPadula):** 기밀성(Confidentiality) 중심.
  - **비바 (Biba):** 무결성(Integrity) 중심. (비인가자 데이터 변형 방지).
  - **클락-윌슨 (Clark-Wilson):** 상업용 무결성 모델. 프로그램에 의한 접근.
  - **만리장성 (Chinese Wall):** 이해 충돌 관계 객체 간 정보 접근 통제.
- **RBAC (역할기반 접근통제):** 중앙관리자가 사용자의 역할(Role)에 따라 권한 부여.
- **VI (Vietnamese) (Tiếng Việt):** Mô hình kiểm soát truy cập.
  - DAC: Dựa trên danh tính (Người dùng cấp quyền).
  - MAC: Dựa trên cấp độ bảo mật (Hệ thống cấp quyền). Các mô hình: Bell-LaPadula (Bảo mật), Biba (Toàn vẹn)...
  - RBAC: Dựa trên vai trò (Role).

Như vậy, **199-200. 접근통제 모델 심화 (Access Control Models Deep Dive)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **220-230. 하위 질의, 트리거, DBMS 접속 및 데이터 전환**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.