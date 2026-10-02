# 118 ~ 120: 빌드 자동화 도구 (Build Automation Tools)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **118 120: 빌드 자동화 도구 (Build Automation Tools)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối build automation với pipeline, dependency, artifact và release, để build có thể tái lập.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **118 ~ 120: 빌드 자동화 도구 (Build Automation Tools)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **118 ~ 120: 빌드 자동화 도구 (Build Automation Tools)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **11. DRM (디지털 저작권 관리, Digital Rights Management)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **118 120: 빌드 자동화 도구 (Build Automation Tools)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

빌드, 자동화, 도구

> **Chuyển mạch:** Ở chặng này của **118 120: 빌드 자동화 도구 (Build Automation Tools)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **41. 빌드 자동화 도구 심화: Jenkins vs Gradle**에서 만든 기준을 이어받아 **118 ~ 120: 빌드 자동화 도구 (Build Automation Tools)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **118 120: 빌드 자동화 도구 (Build Automation Tools)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **118 120: 빌드 자동화 도구 (Build Automation Tools)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **118 120: 빌드 자동화 도구 (Build Automation Tools)**, **118 120: 빌드 자동화 도구 (Build Automation Tools)** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 118 ~ 120: 빌드 자동화 도구 (Build Automation Tools)

Ở bước 49/101, **118 ~ 120: 빌드 자동화 도구 (Build Automation Tools)** xuất hiện như phần tiếp nối của **41. 빌드 자동화 도구 심화: Jenkins vs Gradle**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **118 ~ 120: 빌드 자동화 도구 (Build Automation Tools)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “118 ~ 120: 빌드 자동화 도구 (Build Automation Tools)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 소스 코드를 실행 파일로 만드는 과정과 배포를 자동화. (Tự động hóa việc dịch code, test và đóng gói phát hành - CI/CD).
- **Jenkins:** Viết bằng Java, chạy trên web (Web GUI). Điểm mạnh là test phân tán trên nhiều máy.
- **Gradle:** Viết bằng Groovy (Ngôn ngữ kịch bản), dùng **DSL**. Điểm mạnh là có **빌드 캐시 (Build Cache)** giúp build lại cực nhanh, thường dùng làm chuẩn cho Android.

- 💡 **Mẹo ghi nhớ (Mnemonics):** Jenkins = Java, Web GUI, Phân tán. Gradle = Groovy, DSL, Cache, Android.

---

Như vậy, **118 ~ 120: 빌드 자동화 도구 (Build Automation Tools)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **11. DRM (디지털 저작권 관리, Digital Rights Management)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

> **Bàn giao:** Sau **118 120: 빌드 자동화 도구 (Build Automation Tools)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
