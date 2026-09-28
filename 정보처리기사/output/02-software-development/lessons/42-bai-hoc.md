# 17. 테스트 오라클 및 테스트 도구 (Test Oracle & Tools)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **17. 테스트 오라클 및 테스트 도구 (Test Oracle & Tools)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

테스트, 오라클, 도구

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **16. 소프트웨어 테스트 단계 (Software Testing Phases)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **20. 하향식 통합 테스트와 테스트 스텁 (Top-down Integration Test & Test Stub)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **17. 테스트 오라클 및 테스트 도구 (Test Oracle & Tools)** và nối nó với **20. 하향식 통합 테스트와 테스트 스텁 (Top-down Integration Test & Test Stub)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 17. 테스트 오라클 및 테스트 도구 (Test Oracle & Tools)
* **테스트 오라클 (Test Oracle)**: 테스트 결과가 참인지 판단하기 위해 사전에 정의된 참 값을 대입하여 비교. (참, 샘플링, 추정, 일관성 검사 오라클).
* **테스트 드라이버 (Test Driver)**: (상향식 테스트에서) 하위 모듈을 호출하고 매개 변수를 전달하여 결과를 도출하는 도구. (가짜 메인 프로그램).
* **VI (Vietnamese) (Tiếng Việt):**
  * kiểm thử (test / 테스트) Oracle: Cơ chế/Nguồn chân lý để xác định kết quả đúng hay sai.
  * kiểm thử (test / 테스트) Driver: Chương trình giả lập gọi mô-đun (module / 모듈) con (dùng trong Bottom-up).
* **Example**: 테스트 오라클은 정답지 역할을 합니다.
* 💡 **Mẹo ghi nhớ**: Oracle = Nhà tiên tri/Chân lý. Driver = Người lái xe (Gọi cấp dưới).
