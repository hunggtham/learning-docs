# 086-1: 기수 정렬 (Radix Sort / Bucket Sort)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **086-1: 기수 정렬 (Radix Sort / Bucket Sort)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **086-1: 기수 정렬 (Radix Sort / Bucket Sort)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **7. 이분 검색 (Binary Search)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

기수, 정렬

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **086: 2-Way 합병 정렬 (Merge Sort)**에서 만든 기준을 이어받아 **086-1: 기수 정렬 (Radix Sort / Bucket Sort)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **086-1: 기수 정렬 (Radix Sort / Bucket Sort)** và nối nó với **7. 이분 검색 (Binary Search)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 086-1: 기수 정렬 (Radix Sort / Bucket Sort)

Từ **086: 2-Way 합병 정렬 (Merge Sort)**, ta đã có điểm tựa để bước vào **086-1: 기수 정렬 (Radix Sort / Bucket Sort)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 24/101 trước khi đi vào chi tiết.

Để đọc **086-1: 기수 정렬 (Radix Sort / Bucket Sort)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “086-1: 기수 정렬 (Radix Sort / Bucket Sort)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 데이터를 비교하지 않음! **큐(Queue)**를 이용하여 데이터의 **자릿수(Digit)**별로 나누어 담았다가 꺼냄. (Không dùng dấu < hay > để so sánh. Nhìn vào chữ số hàng Đơn vị, phân vào 10 cái Queue (0-9). Xong ráp lại, làm tiếp hàng Chục, Trăm...).
- **시간 복잡도:** **O(d*n)** (Trong đó d là số chữ số dài nhất). Cực kỳ nhanh, vượt qua giới hạn n log n của các thuật toán so sánh thông thường.

- 💡 **Mẹo ghi nhớ (Mnemonics):** Radix (Cơ số) = Chữ số (Hàng đơn vị, chục...) (Chữ số), Queue/Bucket. Siêu tốc O(dn).

---

Điểm chốt của **086-1: 기수 정렬 (Radix Sort / Bucket Sort)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **7. 이분 검색 (Binary Search)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.