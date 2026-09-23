# 3. 트리 (Tree)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **3. 트리 (Tree)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

트리

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 3. 트리 (Tree)
* 정점(Node)과 선분(Branch)을 이용하여 사이클을 이루지 않도록 구성한 그래프의 특수한 형태.
* **디그리 (Degree, 차수)**: 각 노드에서 뻗어 나온 가지의 수.
* **단말 노드 (Terminal Node) = 잎 노드 (Leaf Node)**: 자식이 하나도 없는 노드, 즉 디그리가 0인 노드.
* **VI (Vietnamese) (Tiếng Việt):**
  * Cây là đồ thị đặc biệt không có chu trình.
  * Bậc (Degree): Số nhánh của một nút con.
  * Nút lá (Leaf): Nút không có con (bậc = 0).
* **Example**: 폴더 구조에서 하위 폴더가 없는 폴더가 단말 노드입니다. (Trong cấu trúc thư mục, thư mục không chứa thư mục con là nút lá).
* 💡 **Mẹo ghi nhớ**: Degree là số con trực tiếp. Leaf là chiếc lá ở cuối cành không mọc thêm được nữa.
