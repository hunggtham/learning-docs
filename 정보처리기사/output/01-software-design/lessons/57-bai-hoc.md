# 14. 파일 편성 방식 (File Organization)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **14. 파일 편성 방식 (File Organization)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối file organization với record, block, index và access path, để dữ liệu vật lý gắn với cách truy cập.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **14. 파일 편성 방식 (File Organization)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **14. 파일 편성 방식 (File Organization)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **6. 애자일 방법론 (Agile Methodology)** khi chuyển sang phần tiếp theo.

> **Nối mạch:** Trong **14. 파일 편성 방식 (File Organization)**, **핵심 키워드 (Từ khóa)** nối từ **학습 목표 (Mục tiêu)** sang **선행·연결 개념 (Kiến thức liên kết)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 핵심 키워드 (Từ khóa)

파일, 편성, 방식

> **Nối mạch:** Ở chặng này của **14. 파일 편성 방식 (File Organization)**, **핵심 키워드 (Từ khóa)** dẫn sang **선행·연결 개념 (Kiến thức liên kết)**, nơi tài liệu chuẩn và vị trí sở hữu được chỉ rõ để biết chỗ đào sâu tiếp; **읽는 방법 (Cách đọc)** mở rộng hệ quả liên quan.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **13. 검색 및 해싱 (Search & Hashing)**에서 만든 기준을 이어받아 **14. 파일 편성 방식 (File Organization)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Nối mạch:** Đặt trong câu hỏi lớn của **14. 파일 편성 방식 (File Organization)**, **읽는 방법 (Cách đọc)** nối từ **선행·연결 개념 (Kiến thức liên kết)** sang **14. 파일 편성 방식 (File Organization)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Nối mạch:** Trong **14. 파일 편성 방식 (File Organization)**, **14. 파일 편성 방식 (File Organization)** nối từ **읽는 방법 (Cách đọc)** sang phần giải thích tiếp theo, vì phần trước cung cấp điểm tựa cho chủ đề này.

## 14. 파일 편성 방식 (File Organization)

Từ **13. 검색 및 해싱 (Search & Hashing)**, ta đã có điểm tựa để bước vào **14. 파일 편성 방식 (File Organization)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 57/69 trước khi đi vào chi tiết.

Để đọc **14. 파일 편성 방식 (File Organization)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **순차 파일 (Sequential File)**, **색인 순차 파일 (Indexed Sequential File / ISAM)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “14. 파일 편성 방식 (File Organization)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **순차 파일 (Sequential File)**: Lưu nối tiếp. Phù hợp băng từ (Magnetic Tape). Nhanh khi xử lý tuần tự, chậm khi thêm/xóa/tìm kiếm.
- **색인 순차 파일 (Indexed Sequential File / ISAM)**:
  - Vừa tuần tự vừa ngẫu nhiên (Sequential + Random).
  - Gồm 3 vùng: **기본 구역 (Prime Area)**, **색인 구역 (Index Area)**, **오버플로 구역 (Overflow Area)**.
  - Dễ dàng chèn/xóa, nhưng tốn dung lượng cho Index/Overflow và chậm hơn File ngẫu nhiên thuần.
- 💡 **Mẹo ghi nhớ**: ISAM 3 구역 (P/I/O - Prime, Index, Overflow) -> **Phải In Ô**

---
# 1과목 Chapter 1. 요구사항 확인 (Requirements)

Điểm chốt của **14. 파일 편성 방식 (File Organization)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **6. 애자일 방법론 (Agile Methodology)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

> **Bàn giao:** Sau **14. 파일 편성 방식 (File Organization)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
