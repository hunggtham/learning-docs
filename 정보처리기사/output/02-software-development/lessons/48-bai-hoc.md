# 45. V-모델 (V-Model) 기반 애플리케이션 테스트 단계

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **45. V-모델 (V-Model) 기반 애플리케이션 테스트 단계**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **45. V-모델 (V-Model) 기반 애플리케이션 테스트 단계** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **46. 애플리케이션 테스트 프로세스 (Test Process)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

모델

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **44. 화이트박스 테스트 검증 기준 (White Box Test Coverage Criteria)**에서 만든 기준을 이어받아 **45. V-모델 (V-Model) 기반 애플리케이션 테스트 단계**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **45. V-모델 (V-Model) 기반 애플리케이션 테스트 단계** và nối nó với **46. 애플리케이션 테스트 프로세스 (Test Process)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 45. V-모델 (V-Model) 기반 애플리케이션 테스트 단계

Từ **44. 화이트박스 테스트 검증 기준 (White Box Test Coverage Criteria)**, ta đã có điểm tựa để bước vào **45. V-모델 (V-Model) 기반 애플리케이션 테스트 단계**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 48/95 trước khi đi vào chi tiết.

Để đọc **45. V-모델 (V-Model) 기반 애플리케이션 테스트 단계** như một bài học cho người mới, hãy giữ câu hỏi: **ta dùng mô hình nào để biểu diễn đối tượng, quan hệ hoặc hành vi, và giới hạn của mỗi cách là gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **하향식 (Top-down)**, **상향식 (Bottom-up)**, **Example** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

개발 단계와 테스트 단계를 짝지어 놓은 모델.
1. **단위 테스트 (Unit Test)** - *구현(Code)* 단계와 짝. 모듈/컴포넌트 초점 (주로 구조 기반/화이트박스).
2. **통합 테스트 (Integration Test)** - *설계(Design)* 단계와 짝. 모듈들을 결합하여 테스트.
   * **하향식 (Top-down)**: 스텁(Stub) 사용. 깊이/넓이 우선. 테스트 초기부터 시스템 구조 파악 가능.
   * **상향식 (Bottom-up)**: 드라이버(Driver)와 클러스터(Cluster) 사용.
3. **시스템 테스트 (System Test)** - *분석(Specification)* 단계와 짝. 실제 환경과 유사하게 구성, 기능적/비기능적 요구사항 점검.
4. **인수 테스트 (Acceptance Test)** - *요구사항(Requirements)* 단계와 짝. 사용자가 직접 테스트. (알파/베타 테스트).
* **VI (Vietnamese) (Tiếng Việt):** Mô hình chữ V (V-Model). Code <-> Unit, Design <-> Integration, Analysis <-> System, Requirements <-> Acceptance.
* **Example**: 코드 짠 사람이 직접 해보는 건 단위 테스트, 고객이 요구사항대로 됐는지 최종 확인하는 건 인수 테스트입니다.

Điểm chốt của **45. V-모델 (V-Model) 기반 애플리케이션 테스트 단계** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **46. 애플리케이션 테스트 프로세스 (Test Process)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.