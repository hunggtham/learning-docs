# 13. 검색 및 해싱 (Search & Hashing)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **13. 검색 및 해싱 (Search & Hashing)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **13. 검색 및 해싱 (Search & Hashing)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **14. 파일 편성 방식 (File Organization)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

검색, 해싱

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **12. 외부 정렬 및 정렬 알고리즘 (External Sort & Sorting Algorithms)**에서 만든 기준을 이어받아 **13. 검색 및 해싱 (Search & Hashing)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **13. 검색 및 해싱 (Search & Hashing)** và nối nó với **14. 파일 편성 방식 (File Organization)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 13. 검색 및 해싱 (Search & Hashing)

Sau khi đã đặt nền bằng **12. 외부 정렬 및 정렬 알고리즘 (External Sort & Sorting Algorithms)**, ta chuyển sang **13. 검색 및 해싱 (Search & Hashing)**. Đây là mắt xích 56/69 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **13. 검색 및 해싱 (Search & Hashing)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **이분 검색 / 이진 검색 (Binary Search)**, **해싱 (Hashing)**, **Thuật ngữ**, **버킷 (Bucket)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “13. 검색 및 해싱 (Search & Hashing)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **이분 검색 / 이진 검색 (Binary Search)**:
  - Dữ liệu phải được sắp xếp (순서화).
  - Tìm kiếm bằng cách chia đôi: `M = (F + L) / 2` (F: Đầu, L: Cuối).
  - Cực kỳ nhanh do mỗi lần giảm một nửa phạm vi tìm kiếm.
- **해싱 (Hashing)**:
  - Tính toán địa chỉ (Home Address) qua hàm băm (Hash Function).
  - Cực nhanh, tốt cho thêm/xóa thường xuyên, nhưng tốn không gian.
  - **Thuật ngữ**:
    - **버킷 (Bucket)**: Khu vực lưu trữ, gồm nhiều Slot.
    - **슬롯 (Slot)**: Chỗ lưu 1 bản ghi (Record).
    - **Collision (충돌)**: 2 khóa ra cùng địa chỉ.
    - **Synonym**: Các khóa cùng địa chỉ.
    - **Overflow (오버플로)**: Hết chỗ lưu khi xảy ra Collision.
- 💡 **Mẹo ghi nhớ**: 해싱 용어: B/S/C/S/O (Bucket, Slot, Collision, Synonym, Overflow) -> **Bỏ Sót Con Sẽ Ôm**

Ta có thể khép mục **13. 검색 및 해싱 (Search & Hashing)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **14. 파일 편성 방식 (File Organization)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.