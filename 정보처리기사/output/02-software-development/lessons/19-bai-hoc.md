# 핵심 031: 모듈 구현 (Module Implementation)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **핵심 031: 모듈 구현 (Module Implementation)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

핵심, 모듈, 구현

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **34. 단위 모듈과 IPC (Unit Module & Inter-Process Communication)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **094 & 094-1: IPC 및 모듈별 알고리즘 구현 (IPC & Algorithm by Module Type)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **핵심 031: 모듈 구현 (Module Implementation)** và nối nó với **094 & 094-1: IPC 및 모듈별 알고리즘 구현 (IPC & Algorithm by Module Type)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 핵심 031: 모듈 구현 (Module Implementation)

- **구현 (Implementation):** 설계 명세서가 컴퓨터가 알 수 있는 모습으로 변환되는 과정. 프로그래밍 또는 코딩. (Quá trình chuyển thiết kế thành code.)
- **작업 절차 (Trình tự):** 코딩 계획 (Lập kế hoạch) → 코딩 (Code) → 컴파일 (Compile) → 테스트 (Test).
- **모듈 (Module):** 독립적인 기능을 갖는 단위. 모듈이 모이면 프로그램이 됨. (Một đơn vị độc lập thực hiện một chức năng cụ thể.)
- **컴포넌트 (Component):** 독립적으로 존재할 수 있는 부분, 재사용되는 단위, 인터페이스를 통해서만 접근. (Thành phần có thể tái sử dụng, giao tiếp qua Interface.)

- **Vietnamese Explanation:** mô-đun (module / 모듈) là một khối mã (code / 코드) (như một hàm hoặc một class). thành phần (component / 컴포넌트) là một khối lớn hơn, đóng gói sẵn và có thể lắp ráp vào nhiều phần mềm khác nhau (như một nút bấm UI, một bộ lịch).
- 💡 **Mẹo ghi nhớ (Mnemonics):** Trình tự: Kế hoạch -> mã (code / 코드) -> Dịch (Compile) -> Thử (Test). mô-đun (module / 모듈) = Ghép lại thành chương trình. thành phần (component / 컴포넌트) = Tái sử dụng qua giao diện (interface / 인터페이스).

---
