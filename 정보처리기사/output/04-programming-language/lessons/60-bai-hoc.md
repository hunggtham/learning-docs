# 198. 블랙 박스 테스트 (Black Box Test / Kiểm thử Hộp đen)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **198. 블랙 박스 테스트 (Black Box Test / Kiểm thử Hộp đen)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **198. 블랙 박스 테스트 (Black Box Test / Kiểm thử Hộp đen)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **199. 검사 전략 (Testing Strategies / Chiến lược kiểm thử)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

블랙, 박스, 테스트

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **196. 화이트 박스 테스트 (White Box Test / Kiểm thử Hộp trắng)**에서 만든 기준을 이어받아 **198. 블랙 박스 테스트 (Black Box Test / Kiểm thử Hộp đen)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **198. 블랙 박스 테스트 (Black Box Test / Kiểm thử Hộp đen)** và nối nó với **199. 검사 전략 (Testing Strategies / Chiến lược kiểm thử)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 198. 블랙 박스 테스트 (Black Box Test / Kiểm thử Hộp đen)

Từ **196. 화이트 박스 테스트 (White Box Test / Kiểm thử Hộp trắng)**, ta đã có điểm tựa để bước vào **198. 블랙 박스 테스트 (Black Box Test / Kiểm thử Hộp đen)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 60/91 trước khi đi vào chi tiết.

Để đọc **198. 블랙 박스 테스트 (Black Box Test / Kiểm thử Hộp đen)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **동치 분할 검사 (Equivalence Partitioning)**, **경계값 분석 (Boundary Value Analysis)**, **원인-효과 그래프 (Cause-Effect Graphing)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “198. 블랙 박스 테스트 (Black Box Test / Kiểm thử Hộp đen)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **기능 검사**라고도 함. 내부 코드를 보지 않고, 소프트웨어의 인터페이스(입·출력)에서 기능이 완전히 작동하는지 입증.
- 테스트 과정 **후반부**에 적용됨.
- 종류:
  - **동치 분할 검사 (Equivalence Partitioning)**: 타당한 입력과 타당하지 않은 입력 자료의 갯수를 균등하게 나눠 테스트. (Ví dụ: Yêu cầu nhập từ 1-100. Test case: 50 (hợp lệ), 150 (không hợp lệ)).
  - **경계값 분석 (Boundary Value Analysis)**: 경계값에서 오류가 발생할 확률이 높음을 이용. (Ví dụ: Test case: 0, 1, 100, 101).
  - **원인-효과 그래프 (Cause-Effect Graphing)**: 입력(원인)과 출력(효과)의 관계 분석.

Điểm chốt của **198. 블랙 박스 테스트 (Black Box Test / Kiểm thử Hộp đen)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **199. 검사 전략 (Testing Strategies / Chiến lược kiểm thử)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.