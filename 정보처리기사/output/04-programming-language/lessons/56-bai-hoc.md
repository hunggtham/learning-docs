# 192. 응집도 (Cohesion / Mức độ gắn kết)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **192. 응집도 (Cohesion / Mức độ gắn kết)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **192. 응집도 (Cohesion / Mức độ gắn kết)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **193 - 194. 효과적인 모듈화 설계 방안 & N-S 차트 (Effective Modular Design & Nassi-Schneiderman Chart)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

응집도

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **191. 결합도 (Coupling / Mức độ phụ thuộc)**에서 만든 기준을 이어받아 **192. 응집도 (Cohesion / Mức độ gắn kết)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **192. 응집도 (Cohesion / Mức độ gắn kết)** và nối nó với **193 - 194. 효과적인 모듈화 설계 방안 & N-S 차트 (Effective Modular Design & Nassi-Schneiderman Chart)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 192. 응집도 (Cohesion / Mức độ gắn kết)

Sau khi đã đặt nền bằng **191. 결합도 (Coupling / Mức độ phụ thuộc)**, ta chuyển sang **192. 응집도 (Cohesion / Mức độ gắn kết)**. Đây là mắt xích 56/91 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **192. 응집도 (Cohesion / Mức độ gắn kết)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “192. 응집도 (Cohesion / Mức độ gắn kết)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 모듈 안의 요소들이 서로 관련되어 있는 정도. 강할수록 독립성이 높고 품질이 좋음.
- **응집도가 약한 것부터 강한 순서 (Xấu -> Tốt)**:
  1. **우연적 (Coincidental)**: 아무 관련 없는 요소들이 우연히 모임 (가장 나쁨).
  2. **논리적 (Logical)**: 논리적으로 유사한 성격의 작업들을 모음.
  3. **시간적 (Temporal)**: 특정 시간에 같이 처리되는 기능들을 모음 (예: 초기화).
  4. **절차적 (Procedural)**: 기능들이 순차적으로 수행됨.
  5. **교환/통신적 (Communication)**: 동일한 입력/출력 데이터를 사용.
  6. **순차적 (Sequential)**: 앞 활동의 출력 데이터를 다음 활동의 입력 데이터로 사용.
  7. **기능적 (Functional)**: 내부 모든 요소가 단일 목적(기능)만을 위해 존재 (가장 좋음).

**Giải thích (Vietnamese):**
Cohesion đo lường sự tập trung của một module. Nếu một hàm vừa làm toán cộng, vừa in hóa đơn, vừa gửi email -> Quá nhiều việc không liên quan (Xấu). Hàm chỉ làm đúng một việc là "Tính tổng" -> Tuyệt vời (Functional).

**💡 Mẹo ghi nhớ (Mnemonics):**
**우논시절 교순기** (U - Luận - Thời - Tiết - Giao - Tuần - Kỹ): 우연 (Coincidental) -> 논리 (Logical) -> 시간 (Temporal) -> 절차 (Procedural) -> 교환 (Communication) -> 순차 (Sequential) -> 기능 (Functional). Từ Xấu đến Tốt.

---

Ta có thể khép mục **192. 응집도 (Cohesion / Mức độ gắn kết)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **193 - 194. 효과적인 모듈화 설계 방안 & N-S 차트 (Effective Modular Design & Nassi-Schneiderman Chart)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.