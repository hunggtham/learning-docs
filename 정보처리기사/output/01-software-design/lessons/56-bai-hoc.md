# 8. 재사용 (Reuse)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **8. 재사용 (Reuse)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

재사용

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **6. N-S 차트 (Nassi-Schneiderman Chart)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **10. 코드 (Code) 개요 & 종류**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **8. 재사용 (Reuse)** và nối nó với **10. 코드 (Code) 개요 & 종류**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 8. 재사용 (Reuse)
**개념 (Khái niệm):** 기존 기능을 최적화하여 다시 쓰는 것 (Tái sử dụng chức năng để tiết kiệm thời gian và chi phí).

*   **Korean:** 결합도는 낮고 응집도는 높아야 함.
*   **VI (Vietnamese) (Tiếng Việt):** Yêu cầu: Độ phụ thuộc (Coupling) THẤP và Độ gắn kết (Cohesion) CAO.
*   **분류 (Phân loại):**
    *   **함수와 객체 (Function & Object):** 소스 코드 단위 (Mức mã nguồn / Class).
    *   **컴포넌트 (Component):** 인터페이스 통신 (Mức Interface, không sửa code gốc).
    *   **애플리케이션 (Application):** 시스템 전체 (Mức ứng dụng hoàn chỉnh).

---
