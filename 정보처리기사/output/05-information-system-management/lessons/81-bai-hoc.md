# 106 암호 알고리즘 (Cryptography Algorithms / Thuật toán mã hoá)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **106 암호 알고리즘 (Cryptography Algorithms / Thuật toán mã hoá)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **106 암호 알고리즘 (Cryptography Algorithms / Thuật toán mã hoá)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **2. 대칭 키 vs 비대칭 키 (Symmetric vs Asymmetric)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

암호, 알고리즘

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **3. 취약한 API 사용 (Vulnerable API / API dễ bị tổn thương)**에서 만든 기준을 이어받아 **106 암호 알고리즘 (Cryptography Algorithms / Thuật toán mã hoá)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **106 암호 알고리즘 (Cryptography Algorithms / Thuật toán mã hoá)** và nối nó với **2. 대칭 키 vs 비대칭 키 (Symmetric vs Asymmetric)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 106 암호 알고리즘 (Cryptography Algorithms / Thuật toán mã hoá)

Từ **3. 취약한 API 사용 (Vulnerable API / API dễ bị tổn thương)**, ta đã có điểm tựa để bước vào **106 암호 알고리즘 (Cryptography Algorithms / Thuật toán mã hoá)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 81/86 trước khi đi vào chi tiết.

Để đọc **106 암호 알고리즘 (Cryptography Algorithms / Thuật toán mã hoá)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các đoạn prose và thuật ngữ bên dưới cần được đọc như các bước trả lời cho câu hỏi đó.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Điểm chốt của **106 암호 알고리즘 (Cryptography Algorithms / Thuật toán mã hoá)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **2. 대칭 키 vs 비대칭 키 (Symmetric vs Asymmetric)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.