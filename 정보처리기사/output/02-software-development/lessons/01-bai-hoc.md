# 1. 자료 구조의 분류 (Classification of Data Structures)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **1. 자료 구조의 분류 (Classification of Data Structures)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

자료, 구조의, 분류

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 이 과목의 핵심 질문을 세우는 출발점이다. 읽은 뒤에는 **073 & 074: 자료 구조의 정의 및 선형 리스트 (Data Structures & Linear List)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **1. 자료 구조의 분류 (Classification of Data Structures)** và nối nó với **073 & 074: 자료 구조의 정의 및 선형 리스트 (Data Structures & Linear List)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 1. 자료 구조의 분류 (Classification of Data Structures)
* **선형 구조 (Linear Structure)**: 배열(Array), 선형 리스트(Linear List), 스택(Stack), 큐(Queue), 데크(Deque)
* **비선형 구조 (Non-linear Structure)**: 트리(Tree), 그래프(Graph)
* **방향/무방향 그래프의 최대 간선 수 (Maximum edges in graphs)**:
  * 무방향 그래프 (Undirected Graph): n(n-1)/2
  * 방향 그래프 (Directed Graph): n(n-1)
* **VI (Vietnamese) (Tiếng Việt):**
  * Cấu trúc tuyến tính: Mảng, danh sách tuyến tính, ngăn xếp, hàng đợi, hàng đợi hai đầu.
  * Cấu trúc phi tuyến: Cây, Đồ thị.
  * Số cạnh tối đa: Đồ thị vô hướng là n(n-1)/2, có hướng là n(n-1).
* **Example**: 노드가 4개인 무방향 그래프의 최대 간선 수는 4(4-1)/2 = 6개입니다. (Với đồ thị vô hướng có 4 đỉnh, số cạnh tối đa là 6).
* 💡 **Mẹo ghi nhớ**: tuyến tính (linear / 선형) là một đường thẳng (Mảng, Stack, Queue). Phi tuyến là rẽ nhánh (Cây, Đồ thị).
