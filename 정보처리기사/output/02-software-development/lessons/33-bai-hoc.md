# 10. 빌드 자동화 도구 (Build Automation Tools)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **10. 빌드 자동화 도구 (Build Automation Tools)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **10. 빌드 자동화 도구 (Build Automation Tools)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **36. IDE (통합 개발 환경) 및 빌드 도구 (IDE & Build Tools)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

빌드, 자동화, 도구

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **100 & 100-1: 패키징 시 고려사항 및 순서 (Packaging Considerations & Sequence)**에서 만든 기준을 이어받아 **10. 빌드 자동화 도구 (Build Automation Tools)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 10. 빌드 자동화 도구 (Build Automation Tools)

Từ **100 & 100-1: 패키징 시 고려사항 및 순서 (Packaging Considerations & Sequence)**, ta đã có điểm tựa để bước vào **10. 빌드 자동화 도구 (Build Automation Tools)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 33/95 trước khi đi vào chi tiết.

Để đọc **10. 빌드 자동화 도구 (Build Automation Tools)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **Ant**, **Maven**, **Jenkins**, **Gradle** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

* **Ant**: 아파치 소프트웨어 재단에서 개발.
* **Maven**: Ant의 대안.
* **Jenkins**: JAVA 기반의 오픈 소스 빌드 자동화 도구.
* **Gradle**: Groovy 기반의 오픈 소스 빌드 자동화 도구.
* **VI (Vietnamese) (Tiếng Việt):** Các công cụ tự động hóa quá trình build phần mềm (biên dịch, đóng gói).
* **Example**: 개발자가 코드를 수정하면 Jenkins가 자동으로 빌드와 테스트를 실행합니다.
* 💡 **Mẹo ghi nhớ**: AMJG (Ant, Maven, Jenkins, Gradle).

Điểm chốt của **10. 빌드 자동화 도구 (Build Automation Tools)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **36. IDE (통합 개발 환경) 및 빌드 도구 (IDE & Build Tools)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.