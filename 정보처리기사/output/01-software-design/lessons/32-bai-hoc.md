# 7. 설계 도구 및 모듈화 심화 (Công cụ thiết kế & Mô-đun hóa chuyên sâu)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **7. 설계 도구 및 모듈화 심화 (Công cụ thiết kế & Mô-đun hóa chuyên sâu)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

설계, 도구, 모듈화, 심화

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 7. 설계 도구 및 모듈화 심화 (Công cụ thiết kế & Mô-đun hóa chuyên sâu)

### NS 차트 (Nassi-Shneiderman Chart)
- 논리의 기술에 중점을 둔 도형을 이용한 표현 방법이다. (Là phương pháp biểu diễn bằng hình khối, trọng tâm vào việc mô tả logic.)
- 연속, 선택 및 다중 선택, 반복 등의 제어 논리 구조를 표현한다. (Thể hiện cấu trúc logic điều khiển như tuần tự, lựa chọn (if-else), đa lựa chọn (switch), lặp lại (while/for).)
- GOTO나 화살표를 사용하지 않는다. (Không sử dụng lệnh GOTO hay mũi tên.)
- 시각적으로 명확히 식별하는 데 적합하다. (Thích hợp để nhận diện rõ ràng về mặt thị giác.)
- 이해하기 쉽고, 코드 변환이 용이하다. (Dễ hiểu và dễ chuyển đổi thành code.)
- **Ví dụ (Example):** Dùng các khối hình chữ nhật xếp chồng lên nhau để biểu diễn một hàm tính toán thay vì dùng sơ đồ khối (Flowchart) có mũi tên rườm rà.

### 재사용 (Reuse / Tái sử dụng)
- 이미 개발된 기능을 새로운 시스템이나 기능 개발에 사용할 수 있는 정도를 의미한다. (Mức độ có thể sử dụng lại các chức năng đã phát triển cho hệ thống hoặc chức năng mới.)
- 재사용 규모에 따른 분류: 함수와 객체, 컴포넌트, 애플리케이션. (Phân loại theo quy mô: Hàm/Đối tượng, Component, Ứng dụng).

### 효과적인 모듈 설계 방안 (Phương án thiết kế module hiệu quả)
- 결합도는 줄이고 응집도는 높인다. (Giảm độ kết dính (Coupling) và tăng độ gắn kết (Cohesion).)
- 복잡도와 중복성을 줄인다. (Giảm độ phức tạp và sự trùng lặp.)
- 일관성을 유지시킨다. (Duy trì tính nhất quán.)
- 모듈의 기능은 지나치게 제한적이어서는 안 된다. (Chức năng của module không nên quá hạn hẹp.)
- 유지보수가 용이해야 한다. (Phải dễ dàng bảo trì.)
- 💡 **Mẹo ghi nhớ (Mnemonic):** **CUTK** (Cao Ứng - Thấp Kết): **Cứ Ứng Thật Kỹ** -> 응집도 높게(Cohesion High), 결합도 낮게(Coupling Low).

### 주요 코드 (Các loại Code cơ bản)
- 순차 코드 (Sequence Code): 일정 기준에 따라서 차례로 일련번호를 부여하는 방법. (Gắn số thứ tự liên tiếp theo một tiêu chuẩn định sẵn - VD: 001, 002, 003).
- 표의 숫자 코드 (Significant Digit Code): 코드화 대상 항목의 중량, 면적, 용량 등의 물리적 수치를 적용시키는 방법. (Sử dụng trực tiếp các chỉ số vật lý như trọng lượng, kích thước vào mã - VD: Tivi 50 inch thì mã là TV-50).
