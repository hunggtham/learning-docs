# 084. 페이지 교체 알고리즘 (Page Replacement Algorithms / Thuật toán thay thế trang nhớ)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **084. 페이지 교체 알고리즘 (Page Replacement Algorithms / Thuật toán thay thế trang nhớ)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **084. 페이지 교체 알고리즘 (Page Replacement Algorithms / Thuật toán thay thế trang nhớ)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **교착상태 필요충분조건 1 - 상호배제 (Deadlock Conditions - Mutual Exclusion)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

페이지, 교체, 알고리즘

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **079. 프로그래밍 언어의 종류 (Types of Programming Languages)**에서 만든 기준을 이어받아 **084. 페이지 교체 알고리즘 (Page Replacement Algorithms / Thuật toán thay thế trang nhớ)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **084. 페이지 교체 알고리즘 (Page Replacement Algorithms / Thuật toán thay thế trang nhớ)** và nối nó với **교착상태 필요충분조건 1 - 상호배제 (Deadlock Conditions - Mutual Exclusion)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 084. 페이지 교체 알고리즘 (Page Replacement Algorithms / Thuật toán thay thế trang nhớ)

Từ **079. 프로그래밍 언어의 종류 (Types of Programming Languages)**, ta đã có điểm tựa để bước vào **084. 페이지 교체 알고리즘 (Page Replacement Algorithms / Thuật toán thay thế trang nhớ)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 60/78 trước khi đi vào chi tiết.

Để đọc **084. 페이지 교체 알고리즘 (Page Replacement Algorithms / Thuật toán thay thế trang nhớ)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **FIFO (First In First Out)**, **OPT (Optimal)**, **LRU (Least Recently Used)**, **LFU (Least Frequently Used)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- 메모리가 꽉 찼을 때 어떤 페이지를 내보낼지 결정.
- **FIFO (First In First Out)**: 가장 먼저 들어온 페이지를 교체.
- **OPT (Optimal)**: 앞으로 가장 오랫동안 사용되지 않을 페이지를 교체 (이론상 최적).
- **LRU (Least Recently Used)**: (과거 기준) 가장 오랫동안 사용되지 않은 페이지를 교체.
- **LFU (Least Frequently Used)**: 사용(참조) 횟수가 가장 적은 페이지 교체.
- **NUR (Not Used Recently)**: 참조 비트(R)와 변형/수정 비트(M)를 조합해 페이지를 네 등급으로 나누고 낮은 등급부터 교체한다.
- **지역성 (Locality)**: 프로세스가 특정 메모리 영역을 집중적으로 참조하는 현상.
  - 공간 지역성: 근처 메모리 참조 (배열).
  - 시간 지역성: 방금 참조한 곳 다시 참조 (루프, 변수).
- **스레싱 (Thrashing)**: 실제 CPU 연산보다 페이지 교체에 더 많은 시간이 소요되어 시스템 성능이 뚝 떨어지는 현상.

**Giải thích (Vietnamese):**
Khi RAM đầy, máy phải đẩy tạm dữ liệu ra ổ cứng.
- LRU: Đuổi cái nào lâu nhất không ai thèm đụng tới (Thường xuyên dùng nhất).
- LFU: Đuổi cái nào ít được gọi tên nhất.
- Locality: Chương trình có xu hướng dùng lại những dữ liệu gần nhau (Ví dụ chạy vòng lặp `for`).
- Thrashing: Tình trạng máy tính bị đơ, giật lag vì RAM quá đầy, máy mải mê swap dữ liệu ra vào ổ cứng mà không chịu tính toán xử lý.

---

Điểm chốt của **084. 페이지 교체 알고리즘 (Page Replacement Algorithms / Thuật toán thay thế trang nhớ)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **교착상태 필요충분조건 1 - 상호배제 (Deadlock Conditions - Mutual Exclusion)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.