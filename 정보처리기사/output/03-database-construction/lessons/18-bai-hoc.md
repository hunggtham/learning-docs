# 179-182. 정규화와 이상 심화 (Normalization & Anomaly - Deep Dive)

> **Mạch đọc:** [README](../README.md) là owner của **179-182. 정규화와 이상 심화 (Normalization & Anomaly - Deep Dive)**; định vị bài ở nhánh schema design trước khi đọc. Từ **학습 목표 (Mục tiêu)** sang **핵심 키워드 (Từ khóa)**, nối dependency, insertion/update/delete anomaly với các dạng chuẩn, rồi dùng **선행·연결 개념 (Kiến thức liên kết)** để giải thích khi nào phải chấp nhận denormalization vì hiệu năng hoặc vận hành.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **179-182. 정규화와 이상 심화 (Normalization & Anomaly - Deep Dive)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **179-182. 정규화와 이상 심화 (Normalization & Anomaly - Deep Dive)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **184-185. 반정규화 (Denormalization)** khi chuyển sang phần tiếp theo.

> **Nối mạch:** Trong **179-182. 정규화와 이상 심화 (Normalization & Anomaly - Deep Dive)**, **핵심 키워드 (Từ khóa)** nối từ **학습 목표 (Mục tiêu)** sang **선행·연결 개념 (Kiến thức liên kết)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 핵심 키워드 (Từ khóa)

정규화와, 이상, 심화

> **Nối mạch:** Ở chặng này của **179-182. 정규화와 이상 심화 (Normalization & Anomaly - Deep Dive)**, **핵심 키워드 (Từ khóa)** dẫn sang **선행·연결 개념 (Kiến thức liên kết)**, nơi tài liệu chuẩn và vị trí sở hữu được chỉ rõ để biết chỗ đào sâu tiếp; **읽는 방법 (Cách đọc)** mở rộng hệ quả liên quan.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **123-125. 정규화 (Normalization)**에서 만든 기준을 이어받아 **179-182. 정규화와 이상 심화 (Normalization & Anomaly - Deep Dive)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Nối mạch:** Đặt trong câu hỏi lớn của **179-182. 정규화와 이상 심화 (Normalization & Anomaly - Deep Dive)**, **읽는 방법 (Cách đọc)** nối từ **선행·연결 개념 (Kiến thức liên kết)** sang **179-182. 정규화와 이상 심화 (Normalization & Anomaly - Deep Dive)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Nối mạch:** Trong **179-182. 정규화와 이상 심화 (Normalization & Anomaly - Deep Dive)**, **179-182. 정규화와 이상 심화 (Normalization & Anomaly - Deep Dive)** nối từ **읽는 방법 (Cách đọc)** sang phần giải thích tiếp theo, vì phần trước cung cấp điểm tựa cho chủ đề này.

## 179-182. 정규화와 이상 심화 (Normalization & Anomaly - Deep Dive)

Từ **123-125. 정규화 (Normalization)**, ta đã có điểm tựa để bước vào **179-182. 정규화와 이상 심화 (Normalization & Anomaly - Deep Dive)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 18/54 trước khi đi vào chi tiết.

Để đọc **179-182. 정규화와 이상 심화 (Normalization & Anomaly - Deep Dive)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “179-182. 정규화와 이상 심화 (Normalization & Anomaly - Deep Dive)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **정규화 목적 (180):** 데이터 중복 배제, 무결성 유지, 이상 발생 방지. 논리적 설계 단계 수행.
- **이상 (Anomaly - 181):**
  - 삽입 이상 (Insertion Anomaly): 원하지 않는 값까지 삽입해야 하는 현상.
  - 삭제 이상 (Deletion Anomaly): 의도치 않은 연쇄 삭제(Cascade).
  - 갱신 이상 (Update Anomaly): 일부만 갱신되어 정보 모순 발생.
- **정규화 단계 암기 요령 (182):** 두부이결다조 (도메인 원자값, 부분 함수 종속 제거, 이행적 함수 종속 제거, 결정자이면서 후보키 아닌 것 제거, 다치 종속 제거, 조인 종속).
- **VI (Vietnamese) (Tiếng Việt):** Chuẩn hóa và Dị thường dữ liệu (Sâu hơn).
  - Dị thường: Thêm (phải thêm dữ liệu không cần thiết), Xóa (bị mất dữ liệu liên quan), Sửa (cập nhật không đồng bộ gây mâu thuẫn).
  - Quy tắc ghi nhớ các chuẩn: Do-Bu-I-Gyeol-Da-Jo (Nguyên tử - Phần - Bắc cầu - Định thức - Đa trị - Kết nối).
- **Example:** 학번만 지우려다 이름과 학과 정보까지 다 지워지는 것이 '삭제 이상'. / Định xóa mã SV nhưng vô tình xóa luôn tên và khoa là 'Dị thường xóa'.

Điểm chốt của **179-182. 정규화와 이상 심화 (Normalization & Anomaly - Deep Dive)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **184-185. 반정규화 (Denormalization)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

> **Bàn giao:** Sau **179-182. 정규화와 이상 심화 (Normalization & Anomaly - Deep Dive)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
