# 092-1: 쿼리 성능 최적화 (Query Performance Optimization)

## 092-1: 쿼리 성능 최적화 (Query Performance Optimization)
Phần “092-1: 쿼리 성능 최적화 (Query Performance Optimization)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 데이터 입·출력 애플리케이션의 성능 향상을 위해 **SQL 코드를 최적화**하는 작업. (Tối ưu hóa mã SQL để tăng tốc độ truy xuất).
- **최적화 절차 (Trình tự tối ưu hóa):**
  1. **대상 선정:** **APM (Application Performance Monitoring)** 등 성능 측정 도구를 사용하여 느린 쿼리를 찾아냄. (Dùng APM tìm câu SQL chạy chậm).
  2. **계획 검토:** **옵티마이저 (Optimizer)**가 수립한 **실행 계획 (Execution Plan)**을 분석. (Xem bản đồ đường đi do bộ Tối ưu hóa lập ra xem có bị đi lòng vòng không).
  3. **재구성 (튜닝):** SQL 코드를 수정하거나 **인덱스 (Index)**를 재구성. (Sửa lại code hoặc tạo Index để tăng tốc).

- 💡 **Mẹo ghi nhớ (Mnemonics):** APM (Tìm bệnh) -> Optimizer/Execution Plan (Khám bệnh / Xem phim X-quang) -> Tuning (Chữa bệnh / Tạo Index).

---
