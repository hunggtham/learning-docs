# 1. 소프트웨어 아키텍처 (Software Architecture)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **1. 소프트웨어 아키텍처 (Software Architecture)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

소프트웨어, 아키텍처

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **13. 소프트웨어 품질 및 아키텍처 패턴 (Chất lượng SW & Mẫu Kiến trúc)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **6. 객체지향 (Hướng Đối Tượng - OOP)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **1. 소프트웨어 아키텍처 (Software Architecture)** và nối nó với **6. 객체지향 (Hướng Đối Tượng - OOP)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 1. 소프트웨어 아키텍처 (Software Architecture)
- **상위 설계 (High-level)**: 아키텍처 (Architecture), 자료구조 (Data Structure), 인터페이스 (Interface).
- **하위 설계 (Low-level)**: 모듈 (Module), 프로시저 (Procedure).
- **아키텍처 패턴 (Architecture Patterns)**:
  - **레이어 패턴 (Layers)**: Chia thành các tầng (OSI 7 layer).
  - **클라이언트-서버 패턴 (Client-Server)**: Máy khách - Máy chủ.
  - **파이프-필터 패턴 (Pipe-Filter)**: Dữ liệu qua các bộ lọc liên tiếp (Ví dụ: Unix shell).
  - **MVC 패턴**: mô hình (model / 모델) (Dữ liệu), View (Giao diện), Controller (Điều khiển).
  - **브로커 패턴 (Broker)**: Có môi giới ở giữa.
  - **마스터-슬레이브 (Master-Slave)**: Một chủ, nhiều tớ (Hệ thống thời gian thực).
