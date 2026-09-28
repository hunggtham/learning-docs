# 025: 트리 (Tree / Cây)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **025: 트리 (Tree / Cây)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

트리

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **30. 트리 구조 추가 용어 (Tree Terminology Additional)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **026: 그래프 (Graph / Đồ thị)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **025: 트리 (Tree / Cây)** và nối nó với **026: 그래프 (Graph / Đồ thị)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 025: 트리 (Tree / Cây)

| 용어 (Thuật ngữ) | 설명 (Giải thích) | 예시 (Ví dụ) |
|---|---|---|
| 루트 노드 (Root Node) | Nút gốc, không có cha. Chỉ có 1 gốc. | A |
| 단말 노드 (Leaf/Terminal Node) | Nút lá, ở cuối cùng, không có con. | D, E, H, I, G |
| 레벨 (Level) | Độ sâu từ gốc tới nút. | E có mức (level / 수준) là 3. |
| 깊이 (Depth) | Độ sâu lớn nhất của cây (Max Level - 1 hoặc tùy cách tính). | độ sâu (depth / 깊이) = 3. |
| 차수 (Degree of Node) | Bậc của một nút: Số lượng con của nút đó. | B có 3 con => Degree = 3. |
| 트리의 차수 (Degree of Tree) | Bậc của cây: Bậc lớn nhất trong tất cả các nút. | Cả cây có nút max là 3 => Degree của cây = 3. |

### 트리 순회 (Tree Traversal - Duyệt cây)
- **전위 순회 (Preorder):** gốc (root / 루트) -> Left -> Right.
- **중위 순회 (Inorder):** Left -> gốc (root / 루트) -> Right.
- **후위 순회 (Postorder):** Left -> Right -> gốc (root / 루트).

- **Vietnamese Explanation:** Cách tính Bậc của cây rất hay thi: Tìm cái nút nào đẻ nhiều con nhất, số con đó chính là Bậc của toàn bộ cây. Khi duyệt cây, chữ "Pre/In/Post" (Trước/Giữa/Sau) dùng để chỉ vị trí của gốc (root / 루트). gốc (root / 루트) đứng trước là Pre, ở giữa là In, ở cuối là Post.
- 💡 **Mẹo ghi nhớ (Mnemonics):** 단말 (Đoạn mạt = Cuối) = Leaf (Lá). Degree = Bậc = Số con. Pre/In/Post = Vị trí của gốc (root / 루트).

---
