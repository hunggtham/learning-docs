# 028: 정렬 (Sorting / Thuật toán sắp xếp)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **028: 정렬 (Sorting / Thuật toán sắp xếp)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **028: 정렬 (Sorting / Thuật toán sắp xếp)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **7. 이분 검색 (Binary Search)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

정렬

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **31. 추가 정렬 알고리즘 (Additional Sorting Algorithms)**에서 만든 기준을 이어받아 **028: 정렬 (Sorting / Thuật toán sắp xếp)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 028: 정렬 (Sorting / Thuật toán sắp xếp)

Từ **31. 추가 정렬 알고리즘 (Additional Sorting Algorithms)**, ta đã có điểm tựa để bước vào **028: 정렬 (Sorting / Thuật toán sắp xếp)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 12/95 trước khi đi vào chi tiết.

Để đọc **028: 정렬 (Sorting / Thuật toán sắp xếp)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng là bằng chứng để so sánh các lựa chọn theo cùng tiêu chí, không phải danh sách cần học thuộc từng ô.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

| 알고리즘 (Thuật toán) | 설명 (Giải thích) | 평균 복잡도 (Average) | 최악 (Worst) |
|---|---|---|---|
| 삽입 정렬 (Insertion Sort) | Lấy phần tử thứ i chèn vào đúng vị trí trong mảng con từ 1 tới i-1 đã sắp xếp. | O(n²) | O(n²) |
| 거품 정렬 (Bubble Sort) | So sánh 2 phần tử kề nhau, sai thì đổi chỗ. Phần tử to nhất sẽ "nổi bọt" về cuối. Cần N-1 Pass (Vòng lặp). | O(n²) | O(n²) |
| 선택 정렬 (Selection Sort) | Tìm phần tử nhỏ nhất rồi đổi chỗ nó về vị trí đầu tiên chưa sắp xếp. | O(n²) | O(n²) |
| 퀵 정렬 (Quick Sort) | Chọn Pivot (Chốt), chia làm 2 nửa: Trái nhỏ hơn, Phải to hơn. Lặp lại (Divide & Conquer). | O(n log n) | **O(n²)** |
| 합병 정렬 (Merge Sort) | Chia đôi mảng cho đến khi còn 1 phần tử, sau đó gộp (Merge) lại theo thứ tự. | O(n log n) | O(n log n) |
| 힙 정렬 (Heap Sort) | Dùng cây Complete Binary Tree (Heap) để tìm min/max rồi đưa ra ngoài, cấu trúc lại Heap. | O(n log n) | O(n log n) |

- **Vietnamese Explanation:** Bubble, Selection, Insertion là 3 thuật toán cơ bản, chạy chậm O(n²). Quick, Merge, Heap là thuật toán xịn, chạy nhanh O(n log n). Nhưng Quick Sort xui xẻo (Worst case) vẫn có thể dính O(n²).
- 💡 **Mẹo ghi nhớ (Mnemonics):** Quick Sort (Nhanh) nhưng Worst là N². Bọt (Bubble), Chọn (Selection), Chèn (Insertion) đều là N².

---

Điểm chốt của **028: 정렬 (Sorting / Thuật toán sắp xếp)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **7. 이분 검색 (Binary Search)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.