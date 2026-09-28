# 50. 애플리케이션 성능 측정 지표 (Performance Metrics)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **50. 애플리케이션 성능 측정 지표 (Performance Metrics)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

애플리케이션, 성능, 측정, 지표

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **A+ Deep Dive: 알고리즘 dấu vết (trace / 추적)와 테스트 판정**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **55. APM (애플리케이션 성능 관리/모니터링)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **50. 애플리케이션 성능 측정 지표 (Performance Metrics)** và nối nó với **55. APM (애플리케이션 성능 관리/모니터링)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 50. 애플리케이션 성능 측정 지표 (Performance Metrics)
* **처리량 (Throughput)**: 일정 시간 내 처리하는 일의 양.
* **응답 시간 (Response Time)**: 요청을 전달한 후 '응답이 도착할 때'까지 걸린 시간.
* **경과 시간 (Turn Around Time)**: 작업을 의뢰한 후 '처리가 완료될 때'까지 걸린 시간.
* **자원 사용률 (Resource Usage)**: CPU, 메모리, 네트워크 등의 자원 사용량.
* **VI (Vietnamese) (Tiếng Việt):** Các chỉ số hiệu năng: thông lượng (throughput / 처리량), Thời gian phản hồi (response / 응답), Thời gian hoàn thành (Turn Around), Mức sử dụng tài nguyên (Resource Usage).
* **Example**: 식당에서 주문하고 물이 나오는 시간(응답 시간), 음식을 다 먹고 나오는 시간(경과 시간).
* 💡 **Mẹo ghi nhớ**: phản hồi (response / 응답) = Phản hồi đầu tiên. Turn Around = Hoàn thành toàn bộ.
