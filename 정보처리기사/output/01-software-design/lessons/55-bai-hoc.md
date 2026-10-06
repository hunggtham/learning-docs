# 12. 외부 정렬 및 정렬 알고리즘 (External Sort & Sorting Algorithms)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **12. 외부 정렬 및 정렬 알고리즘 (External Sort & Sorting Algorithms)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối external sort với disk I/O, run generation và merge, để sắp xếp lớn được thiết kế theo bộ nhớ.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **12. 외부 정렬 및 정렬 알고리즘 (External Sort & Sorting Algorithms)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **12. 외부 정렬 및 정렬 알고리즘 (External Sort & Sorting Algorithms)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **13. 검색 및 해싱 (Search & Hashing)** khi chuyển sang phần tiếp theo.

> **Nối mạch:** Trong **12. 외부 정렬 및 정렬 알고리즘 (External Sort & Sorting Algorithms)**, **핵심 키워드 (Từ khóa)** nối từ **학습 목표 (Mục tiêu)** sang **선행·연결 개념 (Kiến thức liên kết)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 핵심 키워드 (Từ khóa)

외부, 정렬, 알고리즘

> **Nối mạch:** Ở chặng này của **12. 외부 정렬 및 정렬 알고리즘 (External Sort & Sorting Algorithms)**, **핵심 키워드 (Từ khóa)** dẫn sang **선행·연결 개념 (Kiến thức liên kết)**, nơi tài liệu chuẩn và vị trí sở hữu được chỉ rõ để biết chỗ đào sâu tiếp; **읽는 방법 (Cách đọc)** mở rộng hệ quả liên quan.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **11. 수식의 표기법 (Expression Notation)**에서 만든 기준을 이어받아 **12. 외부 정렬 및 정렬 알고리즘 (External Sort & Sorting Algorithms)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Nối mạch:** Đặt trong câu hỏi lớn của **12. 외부 정렬 및 정렬 알고리즘 (External Sort & Sorting Algorithms)**, **읽는 방법 (Cách đọc)** nối từ **선행·연결 개념 (Kiến thức liên kết)** sang **12. 외부 정렬 및 정렬 알고리즘 (External Sort & Sorting Algorithms)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Nối mạch:** Trong **12. 외부 정렬 및 정렬 알고리즘 (External Sort & Sorting Algorithms)**, **12. 외부 정렬 및 정렬 알고리즘 (External Sort & Sorting Algorithms)** nối từ **읽는 방법 (Cách đọc)** sang phần giải thích tiếp theo, vì phần trước cung cấp điểm tựa cho chủ đề này.

## 12. 외부 정렬 및 정렬 알고리즘 (External Sort & Sorting Algorithms)

Ở bước 55/69, **12. 외부 정렬 및 정렬 알고리즘 (External Sort & Sorting Algorithms)** xuất hiện như phần tiếp nối của **11. 수식의 표기법 (Expression Notation)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **12. 외부 정렬 및 정렬 알고리즘 (External Sort & Sorting Algorithms)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **외부 정렬 (External Sort)**, **주요 정렬 알고리즘 (Main Sorting Algorithms)**, **삽입 정렬 (Insertion Sort)**, **버블 정렬 (Bubble Sort)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “12. 외부 정렬 및 정렬 알고리즘 (External Sort & Sorting Algorithms)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **외부 정렬 (External Sort)**: Dùng bộ nhớ phụ (보조기억장치) để sắp xếp dữ liệu lớn. Chủ yếu dùng Merge Sort (병합 정렬).
  - Phân loại: Balance Merge, Cascade Merge, Polyphase Merge, Oscillating Merge.
- **주요 정렬 알고리즘 (Main Sorting Algorithms)**:
  - **삽입 정렬 (Insertion Sort)**: Chèn phần tử vào đúng vị trí của mảng đã sắp xếp.
  - **버블 정렬 (Bubble Sort)**: Đổi chỗ 2 phần tử kề nhau nếu sai thứ tự (nổi bọt).
  - **선택 정렬 (Selection Sort)**: Tìm phần tử nhỏ nhất và đưa lên đầu.
  - **2-Way 합병 정렬 (2-Way Merge Sort)**: Chia đôi liên tục rồi gộp lại (Merge) theo thứ tự.
- **Ví dụ**: Sắp xếp 8, 5, 6, 2, 4 bằng Bubble Sort: (8,5) đổi -> 5,8,6,2,4 -> ...

Như vậy, **12. 외부 정렬 및 정렬 알고리즘 (External Sort & Sorting Algorithms)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **13. 검색 및 해싱 (Search & Hashing)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

> **Bàn giao:** Sau **12. 외부 정렬 및 정렬 알고리즘 (External Sort & Sorting Algorithms)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
