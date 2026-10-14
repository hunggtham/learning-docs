# 197. 분산 데이터베이스의 장단점 (Distributed DB Pros/Cons)

## 197. 분산 데이터베이스의 장단점 (Distributed DB Pros/Cons)
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
