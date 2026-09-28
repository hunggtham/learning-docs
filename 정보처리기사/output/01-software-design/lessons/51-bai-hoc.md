# 10. 소프트웨어 설계 원리 (Software Design Principles)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **10. 소프트웨어 설계 원리 (Software Design Principles)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

소프트웨어, 설계, 원리

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **6. 구조적 분석 도구 (Structured Analysis Tools)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **3. 결합도 (Coupling - Độ phụ thuộc)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **10. 소프트웨어 설계 원리 (Software Design Principles)** và nối nó với **3. 결합도 (Coupling - Độ phụ thuộc)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 10. 소프트웨어 설계 원리 (Software Design Principles)
- **모듈화 (Modularity)**:
  - mô-đun (module / 모듈) quá nhỏ -> Chi phí tích hợp (Integration Cost) tăng.
  - mô-đun (module / 모듈) quá lớn -> Chi phí phát triển từng mô-đun (module / 모듈) (Development Cost) tăng.
- **추상화 (Abstraction)**: 3 loại (과정 - Quá trình, 데이터 - Dữ liệu, 제어 - Điều khiển).
- **단계적 분해 (Stepwise Refinement)**: Đi từ trên xuống (Top-down).
- **정보 은닉 (Information Hiding)**: Giấu thông tin để giảm phụ thuộc.
- **시스템 타입 (System Types)**:
  - **대화형 (Interactive)**: Tương tác (VD: Web bán hàng).
  - **이벤트 중심 (Event-driven)**: Dựa trên sự kiện (VD: Chuông báo cháy).
  - **변환형 (Transformational)**: Biến đổi dữ liệu (VD: Trình biên dịch - Compiler).
  - **객체 영속형 (Object Persistence)**: Lưu trữ lâu dài (VD: Database Server).
