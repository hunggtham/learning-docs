# Python 클래스 (Class) - 기초 (Cơ bản)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Python 클래스 (Class) - 기초 (Cơ bản)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối Python class với object, attribute, method và inheritance, để mã hóa trách nhiệm trong runtime.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **Python 클래스 (Class) - 기초 (Cơ bản)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **Python 클래스 (Class) - 기초 (Cơ bản)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **Python 클래스와 함수 (Class and Functions)** khi chuyển sang phần tiếp theo.

> **Nối mạch:** Trong **Python 클래스 (Class) - 기초 (Cơ bản)**, **핵심 키워드 (Từ khóa)** nối từ **학습 목표 (Mục tiêu)** sang **선행·연결 개념 (Kiến thức liên kết)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 핵심 키워드 (Từ khóa)

Python, 클래스

> **Nối mạch:** Ở chặng này của **Python 클래스 (Class) - 기초 (Cơ bản)**, **핵심 키워드 (Từ khóa)** dẫn sang **선행·연결 개념 (Kiến thức liên kết)**, nơi tài liệu chuẩn và vị trí sở hữu được chỉ rõ để biết chỗ đào sâu tiếp; **읽는 방법 (Cách đọc)** mở rộng hệ quả liên quan.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **Python 제어문 (Control Statements): if문, for문**에서 만든 기준을 이어받아 **Python 클래스 (Class) - 기초 (Cơ bản)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Python 클래스 (Class) - 기초 (Cơ bản)**, **읽는 방법 (Cách đọc)** nối từ **선행·연결 개념 (Kiến thức liên kết)** sang **Python 클래스 (Class) - 기초 (Cơ bản)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Nối mạch:** Trong **Python 클래스 (Class) - 기초 (Cơ bản)**, **Python 클래스 (Class) - 기초 (Cơ bản)** nối từ **읽는 방법 (Cách đọc)** sang phần giải thích tiếp theo, vì phần trước cung cấp điểm tựa cho chủ đề này.

## Python 클래스 (Class) - 기초 (Cơ bản)

Từ **Python 제어문 (Control Statements): if문, for문**, ta đã có điểm tựa để bước vào **Python 클래스 (Class) - 기초 (Cơ bản)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 51/86 trước khi đi vào chi tiết.

Để đọc **Python 클래스 (Class) - 기초 (Cơ bản)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “Python 클래스 (Class) - 기초 (Cơ bản)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **정의 형식**:
  ```python
  class 클래스명:
      def 메소드명(self, 인수):
          실행할 문장
          return 값
  ```
- `def`는 메소드(Method/Phương thức)를 정의하는 예약어입니다.
- `self`는 메소드에서 자기 클래스에 속한 변수에 접근할 때 사용하는 명칭으로 첫 번째 인수로 반드시 작성합니다.

> **Vietnamese Explanation**:
> Class là khuôn mẫu để tạo ra các đối tượng (Objects). Hàm định nghĩa bên trong class được gọi là method (phương thức) và luôn phải có tham số `self` đại diện cho chính đối tượng đó.

Điểm chốt của **Python 클래스 (Class) - 기초 (Cơ bản)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **Python 클래스와 함수 (Class and Functions)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

> **Bàn giao:** Sau **Python 클래스 (Class) - 기초 (Cơ bản)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
