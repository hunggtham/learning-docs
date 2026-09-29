# 194. 파티션 (Partition)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **194. 파티션 (Partition)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **194. 파티션 (Partition)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **199-200. 접근통제 모델 심화 (Access Control Models Deep Dive)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

파티션

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **190. CRUD 분석**에서 만든 기준을 이어받아 **194. 파티션 (Partition)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 194. 파티션 (Partition)

Từ **190. CRUD 분석**, ta đã có điểm tựa để bước vào **194. 파티션 (Partition)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 48/55 trước khi đi vào chi tiết.

Để đọc **194. 파티션 (Partition)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- 대용량 테이블/인덱스를 작은 논리적 단위로 분할.
- 종류: 범위(Range - 예: 월별), 해시(Hash), 조합(Composite), 목록(List), 라운드 로빈(Round Robin).
- **VI (Vietnamese) (Tiếng Việt):** Phân vùng dữ liệu (Partition). Chia bảng lớn thành phần nhỏ: theo Khoảng (Range), Băm (Hash), Danh sách (List)...

Điểm chốt của **194. 파티션 (Partition)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **199-200. 접근통제 모델 심화 (Access Control Models Deep Dive)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.