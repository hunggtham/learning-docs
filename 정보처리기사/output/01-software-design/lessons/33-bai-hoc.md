# 2. 모듈 (Module) & 독립성 (Independence)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **2. 모듈 (Module) & 독립성 (Independence)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

모듈

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 2. 모듈 (Module) & 독립성 (Independence)
**개념 (Khái niệm):** 시스템의 기능을 분리한 단위. 단독 컴파일과 재사용 가능 (Module là các đơn vị chức năng được phân tách của hệ thống, có thể biên dịch độc lập và tái sử dụng).

*   **기능적 독립성 (Functional Independence - Tính độc lập chức năng):**
    *   **Korean:** 각 모듈이 하나의 기능만을 수행하고 상호작용을 최소화하는 것. 결합도(Coupling)는 약하게(Weak), 응집도(Cohesion)는 강하게(Strong) 해야 함.
    *   **VI (Vietnamese) (Tiếng Việt):** Mỗi module chỉ thực hiện một chức năng và hạn chế tương tác với bên ngoài. Cần Độ phụ thuộc (Coupling) thấp và Độ gắn kết (Cohesion) cao. Kích thước module nên nhỏ gọn.
    *   **Example:**
        *   *KR:* 독립된 로그인 모듈은 다른 모듈 변경 시 영향을 받지 않음.
        *   *VN:* Module đăng nhập đứng độc lập, khi sửa giỏ hàng thì module đăng nhập không bị ảnh hưởng.

---
