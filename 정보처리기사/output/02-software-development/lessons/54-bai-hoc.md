# 핵심 041: 테스트 케이스 / 시나리오 / 오라클 (Test Case/Scenario/Oracle)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **핵심 041: 테스트 케이스 / 시나리오 / 오라클 (Test Case/Scenario/Oracle)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

핵심, 테스트, 케이스, 시나리오, 오라클

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **핵심 040: 애플리케이션 테스트 원리 및 종류 (Test Principles & Types)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **핵심 042: 블랙박스 테스트 / 화이트박스 테스트 (Black-Box vs White-Box)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **핵심 041: 테스트 케이스 / 시나리오 / 오라클 (Test Case/Scenario/Oracle)** và nối nó với **핵심 042: 블랙박스 테스트 / 화이트박스 테스트 (Black-Box vs White-Box)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 핵심 041: 테스트 케이스 / 시나리오 / 오라클 (Test Case/Scenario/Oracle)

- **테스트 케이스 (Test Case):** Một bộ gồm: Dữ liệu đầu vào, Điều kiện chạy, Kết quả mong đợi.
- **테스트 시나리오 (Test Scenario):** Kịch bản gồm nhiều trường hợp kiểm thử (test case / 테스트 케이스) nối tiếp nhau.
- **테스트 오라클 (Test Oracle):** Tiêu chuẩn/Cơ chế để tự động đánh giá kết quả kiểm thử (test / 테스트) là Đúng hay Sai (True/False).
  - **참 (True):** Kiểm tra 100% mọi trường hợp (Dùng cho máy bay, y tế).
  - **샘플링 (Sampling):** Lấy mẫu ngẫu nhiên vài trường hợp kiểm thử (test case / 테스트 케이스).
  - **추정 (Heuristic):** Lấy mẫu vài cái chắc chắn, còn lại thì dùng lô-gic (logic / 논리) ước lượng (Heuristic).
  - **일관성 검사 (Consistent):** Kiểm tra xem mã (code / 코드) cũ và mới có cho kết quả giống nhau không khi bị thay đổi (Hồi quy).

- 💡 **Mẹo ghi nhớ (Mnemonics):** Oracle (Nhà tiên tri) = Cái để phán xét đúng/sai. True = 100%. Heuristic = Đoán.

---
