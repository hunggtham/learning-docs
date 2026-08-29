# 31. 추가 정렬 알고리즘 (Additional Sorting Algorithms)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **31. 추가 정렬 알고리즘 (Additional Sorting Algorithms)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

추가, 정렬, 알고리즘

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 31. 추가 정렬 알고리즘 (Additional Sorting Algorithms)
* **퀵 정렬 (Quick Sort)**: 키를 기준으로 작은 값은 왼쪽, 큰 값은 오른쪽 서브파일로 분해시키는 방식. 분할(Divide)과 정복(Conquer)을 통해 자료를 정렬. 
  * 평균 시간 복잡도: O(n log n), 최악: O(n^2).
* **2-Way 합병 정렬 (Merge Sort)**: 정렬되어 있는 두 개의 파일을 한 개의 파일로 합병하는 방식. 평균/최악 모두 O(n log n).
* **힙 정렬 (Heap Sort)**: 전이진 트리(Complete Binary Tree)를 이용한 정렬 방식. 평균/최악 모두 O(n log n).
* **VI (Vietnamese) (Tiếng Việt):** Các thuật toán sắp xếp bổ sung:
  * Quick Sort: Chia để trị (Divide & Conquer), dùng chốt (pivot).
  * Merge Sort: Trộn 2 mảng đã sắp xếp.
  * Heap Sort: Dùng cây nhị phân hoàn chỉnh.
* **Example**: 퀵 정렬은 반장(기준)을 뽑아서 키 작은 사람은 왼쪽, 큰 사람은 오른쪽으로 세우는 방식입니다.
* 💡 **Mẹo ghi nhớ**: Quick = Nhanh nhưng rủi ro (worst case O(n^2)). Merge/Heap = Luôn ổn định O(n log n).
