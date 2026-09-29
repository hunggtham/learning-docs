# 199-200. 접근통제 모델 심화 (Access Control Models Deep Dive)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **199-200. 접근통제 모델 심화 (Access Control Models Deep Dive)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **199-200. 접근통제 모델 심화 (Access Control Models Deep Dive)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **220-230. 하위 질의, 트리거, DBMS 접속 및 데이터 전환** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

접근통제, 모델, 심화

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **194. 파티션 (Partition)**에서 만든 기준을 이어받아 **199-200. 접근통제 모델 심화 (Access Control Models Deep Dive)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **199-200. 접근통제 모델 심화 (Access Control Models Deep Dive)** và nối nó với **220-230. 하위 질의, 트리거, DBMS 접속 및 데이터 전환**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 199-200. 접근통제 모델 심화 (Access Control Models Deep Dive)

Sau khi đã đặt nền bằng **194. 파티션 (Partition)**, ta chuyển sang **199-200. 접근통제 모델 심화 (Access Control Models Deep Dive)**. Đây là mắt xích 50/56 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

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

Ta có thể khép mục **199-200. 접근통제 모델 심화 (Access Control Models Deep Dive)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **220-230. 하위 질의, 트리거, DBMS 접속 및 데이터 전환**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.