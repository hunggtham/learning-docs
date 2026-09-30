# 197. 분산 데이터베이스의 장단점 (Distributed DB Pros/Cons)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **197. 분산 데이터베이스의 장단점 (Distributed DB Pros/Cons)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **197. 분산 데이터베이스의 장단점 (Distributed DB Pros/Cons)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

분산, 데이터베이스의, 장단점

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **195-196. 분산 데이터베이스 목표 (Distributed DB Goals)**에서 만든 기준을 이어받아 **197. 분산 데이터베이스의 장단점 (Distributed DB Pros/Cons)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **197. 분산 데이터베이스의 장단점 (Distributed DB Pros/Cons)** và nối nó với **17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 197. 분산 데이터베이스의 장단점 (Distributed DB Pros/Cons)

Từ **195-196. 분산 데이터베이스 목표 (Distributed DB Goals)**, ta đã có điểm tựa để bước vào **197. 분산 데이터베이스의 장단점 (Distributed DB Pros/Cons)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 36/54 trước khi đi vào chi tiết.

Để đọc **197. 분산 데이터베이스의 장단점 (Distributed DB Pros/Cons)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “197. 분산 데이터베이스의 장단점 (Distributed DB Pros/Cons)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **장점:** 지역 자치성, 자료 공유성 향상, 시스템 성능 및 신뢰성/가용성 향상.
- **단점:** 설계 및 소프트웨어 개발 어려움, 처리 비용 및 잠재적 오류 증가.
- **VI (Vietnamese) (Tiếng Việt):** Ưu nhược điểm của CSDL phân tán.
  - Ưu điểm: Độc lập cục bộ, tăng chia sẻ, tin cậy cao, dễ mở rộng.

---

- **반입 전략:** 요구 반입, 예상 반입.
- **배치 전략:** 최초 적합(First Fit), 최적 적합(Best Fit), 최악 적합(Worst Fit).
- **단편화 (Fragmentation):** 내부 단편화(남는 공간), 외부 단편화(들어갈 수 없는 작은 공간). 통합/압축으로 해결.
- **가상 기억장치 (Virtual Memory):** 페이징(동일 크기 분할, 내부 단편화 발생), 세그먼테이션(논리적 크기 분할, 외부 단편화 발생).
- **페이지 교체 알고리즘:** FIFO(먼저 들어온 것 교체), LRU(최근에 가장 오랫동안 사용 안 한 것 교체), LFU(사용 빈도 가장 적은 것 교체).
- **국부성 (Locality):** 시간 구역성(반복문, 스택), 공간 구역성(배열 순회).
- **스래싱 (Thrashing):** 페이지 부재가 너무 잦아 시스템 성능 저하. 워킹 셋(Working Set)으로 방지.
- **VI (Vietnamese) (Tiếng Việt):** Quản lý bộ nhớ.
  - Phân mảnh: Nội vi (còn dư), Ngoại vi (không đủ chỗ).
  - Bộ nhớ ảo: Phân trang (Paging - kích thước bằng nhau) và Phân đoạn (Segmentation - theo logic).
  - Thuật toán thay trang: FIFO, LRU, LFU. Thrashing xảy ra khi lỗi trang quá nhiều.

Điểm chốt của **197. 분산 데이터베이스의 장단점 (Distributed DB Pros/Cons)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.