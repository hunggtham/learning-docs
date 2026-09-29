# 7. 이분 검색 (Binary Search)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **7. 이분 검색 (Binary Search)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **7. 이분 검색 (Binary Search)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **029 & 030: 검색 알고리즘 및 해싱 (Search Algorithms & Hashing)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

이분, 검색

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **086-1: 기수 정렬 (Radix Sort / Bucket Sort)**에서 만든 기준을 이어받아 **7. 이분 검색 (Binary Search)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **7. 이분 검색 (Binary Search)** và nối nó với **029 & 030: 검색 알고리즘 및 해싱 (Search Algorithms & Hashing)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 7. 이분 검색 (Binary Search)

Ở bước 25/101, **7. 이분 검색 (Binary Search)** xuất hiện như phần tiếp nối của **086-1: 기수 정렬 (Radix Sort / Bucket Sort)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **7. 이분 검색 (Binary Search)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “7. 이분 검색 (Binary Search)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* 검색할 데이터가 정렬되어 있어야 함.
* 비교 횟수를 거듭할 때마다 검색 대상이 반(절반)으로 줄어듦.
* 탐색 효율이 좋고 시간이 적게 소요됨. 중간 레코드 번호(M) = (F+L)/2.
* **VI (Vietnamese) (Tiếng Việt):** Tìm kiếm nhị phân. Dữ liệu phải được sắp xếp trước. Mỗi lần chia đôi không gian tìm kiếm.
* **Example**: 사전에서 단어를 찾을 때 책을 반으로 계속 쪼개며 찾는 방식입니다.
* 💡 **Mẹo ghi nhớ**: Binary = chia đôi (phải sắp xếp trước!).

Như vậy, **7. 이분 검색 (Binary Search)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **029 & 030: 검색 알고리즘 및 해싱 (Search Algorithms & Hashing)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.