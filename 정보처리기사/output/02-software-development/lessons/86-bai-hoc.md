# 핵심 115 & 116: 연관 기억장치 및 메모리 인터리빙 (Associative Memory & Memory Interleaving)

## 핵심 115 & 116: 연관 기억장치 및 메모리 인터리빙 (Associative Memory & Memory Interleaving)

### 연관 기억장치 (Associative Memory / CAM)
Phần “연관 기억장치 (Associative Memory / CAM)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 주소에 의해 접근하지 않고, 기억된 내용의 일부를 이용하여 접근할 수 있는 기억장치. (Không tìm bằng Địa chỉ, mà tìm bằng Nội dung - Content Addressable Memory.)
- 정보 검색이 신속하다. (Tìm kiếm thông tin cực nhanh.)
- 캐시 메모리나 가상 메모리 매핑 테이블에 사용된다. (Dùng trong Cache hoặc Bảng ánh xạ bộ nhớ ảo.)
- 하드웨어 비용이 증가한다. (Tốn kém phần cứng vì cần mạch so sánh song song.)

### 메모리 인터리빙 (Memory Interleaving)
Phần “메모리 인터리빙 (Memory Interleaving)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- CPU가 각 모듈로 전송할 주소를 교대로 분산 배치한 후 차례대로 전송하여 여러 모듈을 병행 접근하는 기법. (Kỹ thuật phân tán địa chỉ bộ nhớ thành nhiều module độc lập để CPU truy cập song song cùng lúc.)
- 캐시 기억장치, 고속 DMA 전송 등에서 많이 사용된다. (Dùng trong Cache và DMA tốc độ cao.)

- **Vietnamese Explanation:** Associative Memory giống như việc bạn gọi "Ai tên Nam đứng lên!" thay vì hỏi "Học sinh số báo danh 10 tên gì?". Nhanh nhưng tốn kém (ai cũng phải tự vểnh tai nghe). Interleaving giống như có 4 làn thu phí thay vì 1 làn, xe cộ (dữ liệu) sẽ phân tán đi qua 4 làn cùng lúc, giảm tắc nghẽn.
- 💡 **Mẹo ghi nhớ (Mnemonics):** CAM (Content) = Tìm bằng Nội dung. Interleaving (Xen kẽ) = Đa Module, Truy cập song song.

---
