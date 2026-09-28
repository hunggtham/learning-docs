# 소프트웨어 공학 (Software Engineering)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **소프트웨어 공학 (Software Engineering)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

소프트웨어, 공학

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **가상기억장치 및 페이지 교체 (Virtual Memory & Page Replacement)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **071. 보안 취약성 식별 (Security Vulnerability Identification / Lỗ hổng bảo mật)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **소프트웨어 공학 (Software Engineering)** và nối nó với **071. 보안 취약성 식별 (Security Vulnerability Identification / Lỗ hổng bảo mật)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 소프트웨어 공학 (Software Engineering)

---

- **모듈화 (Modularity)**: 캡슐화로 영향 최소화, 유지보수 용이.
- **재사용성 (Reusability)**: 반복 모듈 제공으로 생산성/품질 향상.
- **확장성 (Extensibility)**: 다형성 통한 인터페이스 확장.
- **제어 반전 (Inversion of Control, IoC)**: 프레임워크가 흐름을 제어하고 사용자(외부) 코드를 호출.

**Giải thích (Vietnamese):**
khung phần mềm (framework / 프레임워크) (như Spring, Django) là một bộ khung có sẵn. Tính năng đặc biệt nhất của khung phần mềm (framework / 프레임워크) là IoC (Đảo ngược quyền điều khiển): Thay vì bạn tự gọi thư viện (library / 라이브러리), thì khung phần mềm (framework / 프레임워크) sẽ là người gọi mã (code / 코드) của bạn!

---
