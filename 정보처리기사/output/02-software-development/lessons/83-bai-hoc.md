# 52. 소스 코드 최적화와 순환 복잡도 (Source Code Optimization & Cyclomatic Complexity)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **52. 소스 코드 최적화와 순환 복잡도 (Source Code Optimization & Cyclomatic Complexity)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

소스, 코드, 최적화와, 순환, 복잡도

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 52. 소스 코드 최적화와 순환 복잡도 (Source Code Optimization & Cyclomatic Complexity)
* **소스 코드 최적화**: 배제해야 할 '나쁜 코드(Bad Code - 스파게티 코드, 외계인 코드)'와 작성해야 할 '클린 코드(Clean Code - 가독성, 단순성, 의존성 배제, 중복성 최소화, 추상화)'가 있음.
* **순환 복잡도 (McCabe's Cyclomatic Complexity)**: 프로그램 논리의 복잡도를 측정.
  * 계산 방법: `V(G) = 화살표 수(E) - 노드 수(N) + 2` 또는 제어 흐름도의 닫힌 영역 수 + 1.
* **소스 코드 품질 분석 도구 심화**:
  * **정적 분석 도구**: pmd, cppcheck, SonarQube, checkstyle, ccm.
  * **동적 분석 도구**: Avalanche, Valgrind (메모리 누수, 스레드 결함 발견).
* **VI (Vietnamese) (Tiếng Việt):** Tối ưu mã nguồn & Độ phức tạp Cyclomatic (McCabe). 
  * Clean code > Bad code (Spaghetti/Alien).
  * V(G) = Cạnh(E) - Đỉnh(N) + 2. Số V(G) chính là số lượng test case cơ bản cần thiết.
  * Công cụ tĩnh (không chạy code): SonarQube. Động (chạy code tìm rò rỉ bộ nhớ): Valgrind.
