# 핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

핵심, 재사용, 기법

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **핵심 039: 소프트웨어 품질 관련 국제 표준 (Software Quality Standards)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)** và nối nó với **핵심 039: 소프트웨어 품질 관련 국제 표준 (Software Quality Standards)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)

- **재사용 (Reuse):** 이미 개발되어 인정받았던 소프트웨어의 전체 또는 일부분을 다시 사용하는 기법. (Sử dụng lại code/phần mềm cũ đã được kiểm chứng để tiết kiệm thời gian, chi phí và giảm lỗi.)
- **Phân loại theo kỹ thuật:**
  - **분석 (Analysis):** Hiểu mã (code / 코드) cũ để chọn cái cần tái sử dụng.
  - **재구조 (Restructuring):** Đổi cấu trúc, không đổi chức năng.
  - **역공학 (Reverse Engineering):** Dịch ngược từ mã (code / 코드) ra bản thiết kế.
  - **이식 (Migration):** Chuyển sang môi trường / phần cứng mới.
  - **재개발 (Re-Development):** Đập đi xây lại có tham khảo cái cũ.
- **Phân loại theo phạm vi:**
  - Hàm & Đối tượng (Function/Class), thành phần (component / 컴포넌트), ứng dụng (application / 애플리케이션).

- 💡 **Mẹo ghi nhớ (Mnemonics):** Reverse kỹ thuật (engineering / 엔지니어링) (Dịch ngược) = Từ mã (code / 코드) -> Bản thiết kế. di chuyển (migration / 마이그레이션) = Chuyển nhà (môi trường).

---
