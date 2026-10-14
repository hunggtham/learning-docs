# 핵심 117: 캐시 메모리 (Cache Memory)

## 핵심 117: 캐시 메모리 (Cache Memory)
Phần “핵심 117: 캐시 메모리 (Cache Memory)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- CPU의 속도와 메모리의 속도 차이를 줄이기 위해 사용하는 고속 Buffer Memory. (Bộ đệm tốc độ cao giảm chênh lệch tốc độ giữa CPU và RAM.)
- 캐시 메모리는 메모리 계층 구조에서 가장 빠른 소자 (Nhanh nhất trong hệ thống phân cấp bên ngoài register, dùng SRAM.)
- `적중률 (Hit Ratio) = 적중 횟수(Hits) / 총 접근 횟수 (Total Accesses)`

### 매핑 프로세스 (Mapping Process)
Phần “매핑 프로세스 (Mapping Process)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 주기억장치로부터 캐시 메모리로 데이터를 전송하는 방법 (Cách ánh xạ RAM vào Cache.)
- 종류: 직접(Direct) 매핑, 어소시에이티브(Associative) 매핑, 세트-어소시에이티브(Set-Associative) 매핑.

### 쓰기 정책 (Write Policy)
Phần “쓰기 정책 (Write Policy)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 캐시에 저장되어 있는 데이터에 수정이 발생했을 때 주기억장치에 갱신하는 시기와 방법. (Khi Cache bị thay đổi, khi nào thì ghi lại vào RAM?)
- **Write-Through:** 쓰기 동작이 이루어질 때마다 캐시와 주기억장치를 동시에 갱신. (Ghi đồng thời cả 2, an toàn nhưng chậm.)
- **Write-Back:** 캐시로부터 제거될 때 주기억장치에 복사. (Chỉ ghi vào RAM khi bị đuổi khỏi Cache, nhanh nhưng rủi ro nếu mất điện.)

- **Vietnamese Explanation:** Cache giống như cái ví tiền lẻ (SRAM) bạn để túi quần. RAM là két sắt (DRAM) ở nhà. Lấy tiền lẻ nhanh hơn về nhà mở két.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Write-Through (Xuyên qua) = Ghi luôn vào RAM (Chậm, Chắc). Write-Back (Ghi lại sau) = Khi nào dọn Cache mới ghi (Nhanh, Nguy hiểm).

---
