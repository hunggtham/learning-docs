# 4. 이진 트리의 운행법 (Binary Tree Traversal)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **4. 이진 트리의 운행법 (Binary Tree Traversal)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

이진, 트리의, 운행법

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 4. 이진 트리의 운행법 (Binary Tree Traversal)
* **Preorder (전위)**: Root → Left → Right
* **Inorder (중위)**: Left → Root → Right
* **Postorder (후위)**: Left → Right → Root
* **VI (Vietnamese) (Tiếng Việt):**
  * Preorder: Gốc -> Trái -> Phải.
  * Inorder: Trái -> Gốc -> Phải.
  * Postorder: Trái -> Phải -> Gốc.
* **Example**: 수식 `A + B`를 전위 표기하면 `+ A B`, 중위 표기하면 `A + B`, 후위 표기하면 `A B +`가 됩니다.
* 💡 **Mẹo ghi nhớ**: Tiền/Trung/Hậu tố chỉ vị trí của Root (Gốc) so với Trái/Phải.
