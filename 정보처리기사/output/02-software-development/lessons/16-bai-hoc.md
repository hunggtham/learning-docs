# 028: 정렬 (Sorting / Thuật toán sắp xếp)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **028: 정렬 (Sorting / Thuật toán sắp xếp)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối sorting với comparison, stability, memory và complexity, để chọn thuật toán theo dữ liệu và ràng buộc.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **028: 정렬 (Sorting / Thuật toán sắp xếp)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **028: 정렬 (Sorting / Thuật toán sắp xếp)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **081: 삽입 정렬 (Insertion Sort - Sắp xếp chèn)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **028: 정렬 (Sorting / Thuật toán sắp xếp)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

정렬

> **Chuyển mạch:** Ở chặng này của **028: 정렬 (Sorting / Thuật toán sắp xếp)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **31. 추가 정렬 알고리즘 (Additional Sorting Algorithms)**에서 만든 기준을 이어받아 **028: 정렬 (Sorting / Thuật toán sắp xếp)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **028: 정렬 (Sorting / Thuật toán sắp xếp)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **028: 정렬 (Sorting / Thuật toán sắp xếp)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **028: 정렬 (Sorting / Thuật toán sắp xếp)**, **028: 정렬 (Sorting / Thuật toán sắp xếp)** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 028: 정렬 (Sorting / Thuật toán sắp xếp)

Ở bước 16/101, **028: 정렬 (Sorting / Thuật toán sắp xếp)** xuất hiện như phần tiếp nối của **31. 추가 정렬 알고리즘 (Additional Sorting Algorithms)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **028: 정렬 (Sorting / Thuật toán sắp xếp)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng là bằng chứng để so sánh các lựa chọn theo cùng tiêu chí, không phải danh sách cần học thuộc từng ô.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “028: 정렬 (Sorting / Thuật toán sắp xếp)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

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

Như vậy, **028: 정렬 (Sorting / Thuật toán sắp xếp)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **081: 삽입 정렬 (Insertion Sort - Sắp xếp chèn)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

> **Bàn giao:** Sau **028: 정렬 (Sorting / Thuật toán sắp xếp)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
