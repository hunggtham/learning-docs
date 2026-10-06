# 191-192. 인덱스 (Index)

> **Mạch đọc:** [README](../README.md) là owner của **191-192. 인덱스 (Index)**; dùng bản đồ đó để định vị bài trong nhánh truy vấn và hiệu năng. Từ **학습 목표 (Mục tiêu)** sang **핵심 키워드 (Từ khóa)**, rồi nối cấu trúc index, selectivity và chi phí truy vấn với **선행·연결 개념 (Kiến thức liên kết)** và phần distributed database; mục sau chỉ có ý nghĩa khi trade-off đọc/ghi đã rõ.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **191-192. 인덱스 (Index)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **191-192. 인덱스 (Index)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **136-137. 분산 데이터베이스 (Distributed DB)** khi chuyển sang phần tiếp theo.

> **Nối mạch:** Trong **191-192. 인덱스 (Index)**, **핵심 키워드 (Từ khóa)** nối từ **학습 목표 (Mục tiêu)** sang **선행·연결 개념 (Kiến thức liên kết)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 핵심 키워드 (Từ khóa)

인덱스

> **Nối mạch:** Ở chặng này của **191-192. 인덱스 (Index)**, **핵심 키워드 (Từ khóa)** dẫn sang **선행·연결 개념 (Kiến thức liên kết)**, nơi tài liệu chuẩn và vị trí sở hữu được chỉ rõ để biết chỗ đào sâu tiếp; **읽는 방법 (Cách đọc)** mở rộng hệ quả liên quan.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **8. 서브쿼리와 뷰 (Truy vấn con và View)**에서 만든 기준을 이어받아 **191-192. 인덱스 (Index)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Nối mạch:** Đặt trong câu hỏi lớn của **191-192. 인덱스 (Index)**, **읽는 방법 (Cách đọc)** nối từ **선행·연결 개념 (Kiến thức liên kết)** sang **191-192. 인덱스 (Index)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Nối mạch:** Trong **191-192. 인덱스 (Index)**, **191-192. 인덱스 (Index)** nối từ **읽는 방법 (Cách đọc)** sang phần giải thích tiếp theo, vì phần trước cung cấp điểm tựa cho chủ đề này.

## 191-192. 인덱스 (Index)

Từ **8. 서브쿼리와 뷰 (Truy vấn con và View)**, ta đã có điểm tựa để bước vào **191-192. 인덱스 (Index)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 33/54 trước khi đi vào chi tiết.

Để đọc **191-192. 인덱스 (Index)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “191-192. 인덱스 (Index)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 데이터 접근을 빠르게 하기 위한 <키 값, 포인터> 구조. DDL로 제어. 트리 기반(B+ 트리), 비트맵, 함수 기반, 도메인 인덱스 등.
- **VI (Vietnamese) (Tiếng Việt):** Chỉ mục (Index). Cấu trúc <Khóa, Con trỏ> giúp truy cập nhanh. Sử dụng B+ Tree, Bitmap...

Điểm chốt của **191-192. 인덱스 (Index)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **136-137. 분산 데이터베이스 (Distributed DB)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

> **Bàn giao:** Sau **191-192. 인덱스 (Index)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
