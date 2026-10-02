# 081-2: 셸 정렬 (Shell Sort)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **081-2: 셸 정렬 (Shell Sort)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối Shell sort với gap sequence, insertion và locality, để cải thiện sắp xếp qua thứ tự khoảng cách.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **081-2: 셸 정렬 (Shell Sort)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **081-2: 셸 정렬 (Shell Sort)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **082: 선택 정렬 (Selection Sort)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **081-2: 셸 정렬 (Shell Sort)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

정렬

> **Chuyển mạch:** Ở chặng này của **081-2: 셸 정렬 (Shell Sort)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **081: 삽입 정렬 (Insertion Sort - Sắp xếp chèn)**에서 만든 기준을 이어받아 **081-2: 셸 정렬 (Shell Sort)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **081-2: 셸 정렬 (Shell Sort)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **081-2: 셸 정렬 (Shell Sort)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **081-2: 셸 정렬 (Shell Sort)**, **081-2: 셸 정렬 (Shell Sort)** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 081-2: 셸 정렬 (Shell Sort)

Từ **081: 삽입 정렬 (Insertion Sort - Sắp xếp chèn)**, ta đã có điểm tựa để bước vào **081-2: 셸 정렬 (Shell Sort)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 18/101 trước khi đi vào chi tiết.

Để đọc **081-2: 셸 정렬 (Shell Sort)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “081-2: 셸 정렬 (Shell Sort)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **삽입 정렬(Insertion Sort)을 보완/확장**한 알고리즘. (Phiên bản nâng cấp của Insertion Sort).
- 입력 파일을 매개변수 **h(간격)** 만큼 떨어진 레코드들끼리 묶어 서브파일을 구성하고, 각 서브파일을 삽입 정렬. (Chia mảng thành các nhóm con cách nhau một khoảng $h$, sắp xếp chèn từng nhóm. Sau đó giảm $h$ dần dần về 1).
- **시간 복잡도:** 평균 O(n^1.5), 최악 O(n²). 부분적으로 정렬되어 있는 경우에 매우 유리. (Nhanh hơn O(n²) thông thường. Rất hiệu quả nếu mảng đã "hơi hơi" có thứ tự).

- **Vietnamese Explanation:** Insertion Sort thường yếu khi số nhỏ nằm tuốt ở cuối mảng (phải nhích từng bước lên đầu). Shell Sort dùng khoảng cách $h$ (ví dụ nhảy 5 bước 1 lần) để đưa số nhỏ về đầu nhanh hơn.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Shell = Vỏ ốc (Xoáy từ rộng vào hẹp). Từ khóa: **h (Khoảng cách nhảy)**, **O(n^1.5)**.

---

Điểm chốt của **081-2: 셸 정렬 (Shell Sort)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **082: 선택 정렬 (Selection Sort)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

> **Bàn giao:** Sau **081-2: 셸 정렬 (Shell Sort)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
