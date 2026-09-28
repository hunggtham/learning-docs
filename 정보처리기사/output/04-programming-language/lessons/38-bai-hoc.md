# 083. 메모리 관리 기법 - 배치 전략 (Memory Placement Strategies)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **083. 메모리 관리 기법 - 배치 전략 (Memory Placement Strategies)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

메모리, 관리, 기법, 배치, 전략

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **283 - 288. 운영체제 구성 및 UNIX 시스템 (OS & UNIX)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **289 - 296. 메모리 관리 및 가상 기억장치 (Memory Management)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **083. 메모리 관리 기법 - 배치 전략 (Memory Placement Strategies)** và nối nó với **289 - 296. 메모리 관리 및 가상 기억장치 (Memory Management)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 083. 메모리 관리 기법 - 배치 전략 (Memory Placement Strategies)
- **최초 적합 (First fit)**: 가장 처음 만나는 빈 공간에 할당 (빠름).
- **최적 적합 (Best fit)**: 자원 낭비(단편화)가 가장 적은 핏(딱 맞는) 공간에 할당.
- **최악 적합 (Worst fit)**: 단편화가 가장 큰(넓은) 공간에 할당 (남은 공간을 다시 쓰기 위해).

**Giải thích (Vietnamese):**
Khi một phần mềm cần RAM, OS sẽ nhét nó vào đâu?
- First fit: Thấy chỗ nào trống nhét vào luôn (Nhanh).
- Best fit: Tìm chỗ nào vừa khít nhất để nhét (Tiết kiệm chỗ).
- Worst fit: Cố tình nhét vào chỗ rộng nhất (Để chừa lại không gian rộng cho các app sau).

---
