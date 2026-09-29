# 8. 주요 해싱 함수 (Hashing Functions)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **8. 주요 해싱 함수 (Hashing Functions)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **8. 주요 해싱 함수 (Hashing Functions)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **32. 추가 해싱 함수 (Additional Hashing Functions)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

주요, 해싱, 함수

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **029 & 030: 검색 알고리즘 및 해싱 (Search Algorithms & Hashing)**에서 만든 기준을 이어받아 **8. 주요 해싱 함수 (Hashing Functions)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 8. 주요 해싱 함수 (Hashing Functions)

Từ **029 & 030: 검색 알고리즘 및 해싱 (Search Algorithms & Hashing)**, ta đã có điểm tựa để bước vào **8. 주요 해싱 함수 (Hashing Functions)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 15/95 trước khi đi vào chi tiết.

Để đọc **8. 주요 해싱 함수 (Hashing Functions)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **제산법 (Division)**, **제곱법 (Mid-Square)**, **폴딩법 (Folding)**, **숫자 분석법 (Digit Analysis)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

* **제산법 (Division)**: 키 값을 소수(Prime)로 나눈 나머지를 주소로 사용.
* **제곱법 (Mid-Square)**: 키 값을 제곱한 후 중간 부분의 값을 주소로 사용.
* **폴딩법 (Folding)**: 키 값을 여러 부분으로 나눈 후 더하거나 XOR한 값을 주소로 사용.
* **숫자 분석법 (Digit Analysis)**: 숫자의 분포를 분석해 고른 자리를 주소로 사용.
* **VI (Vietnamese) (Tiếng Việt):** Các hàm băm (Hashing) giúp ánh xạ khóa (key) thành địa chỉ. Division (chia lấy dư), Mid-Square (bình phương lấy giữa), Folding (gấp/cộng các phần), Digit Analysis (phân tích chữ số).
* **Example**: 제산법으로 키 10을 해시 테이블 크기 7(소수)로 나누면 나머지 3이 주소가 됩니다.
* 💡 **Mẹo ghi nhớ**: Division = Chia lấy dư, Square = Bình phương, Fold = Gấp lại.

Điểm chốt của **8. 주요 해싱 함수 (Hashing Functions)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **32. 추가 해싱 함수 (Additional Hashing Functions)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.