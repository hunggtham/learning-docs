# 핵심 115 & 116: 연관 기억장치 및 메모리 인터리빙 (Associative Memory & Memory Interleaving)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và cơ chế hoạt động của bộ nhớ liên kết (연관 기억장치 - Associative Memory / CAM): tìm kiếm và truy xuất thông tin bằng **nội dung dữ liệu (기억된 내용)** thay vì dựa vào địa chỉ ô nhớ.
- Hiểu rõ ứng dụng của CAM trong bộ nhớ đệm Cache và bảng ánh xạ trang (Page Table / TLB) của bộ nhớ ảo.
- Nắm vững kỹ thuật xen kẽ bộ nhớ (메모리 인터리빙 - Memory Interleaving): phân phối luân phiên các địa chỉ trên nhiều mô-đun nhớ độc lập để CPU có thể truy cập song song cùng lúc, gia tăng đáng kể băng thông bộ nhớ.

## 핵심 키워드 (Từ khóa)
- 연관 기억장치 (Associative Memory / CAM - Content Addressable Memory)
- 내용에 의한 참조 (Content-based Reference / 주소 대신 내용 검색)
- 일치 회로 (Match Circuit / 병렬 비교 회로)
- 캐시 및 가상메모리 매핑 (Cache & TLB Mapping)
- 메모리 인터리빙 (Memory Interleaving / 모듈 분산 배치)
- 병행 접근 (Concurrent / Parallel Memory Access)
- 고속 DMA 전송 (High-speed Direct Memory Access)

## 선행·연결 개념 (Kiến thức liên kết)
- [85-bai-hoc.md](85-bai-hoc.md): Bộ nhớ phụ và thời gian truy cập đĩa từ (Disk Access Time).
- [87-bai-hoc.md](87-bai-hoc.md): Bộ nhớ đệm Cache Memory và các chính sách ghi.
- [88-bai-hoc.md](88-bai-hoc.md): Bộ nhớ ảo (Virtual Memory) và hiện tượng lỗi trang (Page Fault).

## 읽는 방법 (Cách đọc)
- Phân biệt hai công nghệ tăng tốc bộ nhớ:
  - **연관 기억장치 (CAM):** Bình thường muốn tìm dữ liệu phải biết địa chỉ ô nhớ (như tìm học sinh theo số báo danh). CAM cho phép tìm trực tiếp theo nội dung (như hô to "Ai tên Nam đứng lên!"). Tốc độ tìm kiếm tức thì cực nhanh nhưng phần cứng rất đắt tiền vì mỗi ô nhớ phải tích hợp thêm mạch so sánh logic song song.
  - **메모리 인터리빙 (Memory Interleaving):** Giống như một trạm thu phí mở 4 làn đường song song thay vì 1 làn duy nhất. Các địa chỉ liên tiếp $0, 1, 2, 3$ được chia đều cho Module $0, 1, 2, 3$. CPU có thể gửi yêu cầu nạp đồng thời 4 từ nhớ từ 4 module trong cùng một chu kỳ bus.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng so sánh chi tiết: 연관 기억장치 (CAM) vs 메모리 인터리빙 (Interleaving):**

| Tiêu chuẩn so sánh | 연관 기억장치 (Associative Memory / CAM) | 메모리 인터리빙 (Memory Interleaving) |
| :--- | :--- | :--- |
| **Nguyên lý cốt lõi** | **Truy xuất theo NỘI DUNG (내용)**; so sánh đồng thời từ khóa tìm kiếm với tất cả các từ nhớ trong bộ nhớ | **Phân tán địa chỉ luân phiên** trên nhiều khối bộ nhớ (Memory Modules) độc lập |
| **Mục tiêu kỹ thuật** | Tối đa hóa **tốc độ tìm kiếm (신속한 검색)** dữ liệu mà không cần biết trước địa chỉ ô nhớ | Tăng **băng thông truyền dữ liệu**, cho phép CPU truy cập song song (병행 접근) nhiều module cùng lúc |
| **Ứng dụng tiêu biểu** | Bảng ánh xạ bộ nhớ ảo (**TLB**), bộ nhớ đệm kết hợp (**Associative Cache**) | Bộ nhớ chính của hệ thống hiệu năng cao, đường truyền **DMA tốc độ cao** |
| **Hạn chế kỹ thuật** | Chi phí phần cứng đắt đỏ do đòi hỏi mạch so sánh phần cứng song song tại từng bit | Đòi hỏi bộ điều khiển bộ nhớ (Memory Controller) hỗ trợ kiến trúc đa kênh (Multi-channel) |

- **Cơ chế đánh địa chỉ trong Memory Interleaving:**
  - **Low-order Interleaving (인터리빙 하위):** Các bit thấp của địa chỉ dùng để chọn Module nhớ $\rightarrow$ Các địa chỉ liên tiếp nhau nằm trên các module khác nhau $\rightarrow$ Tối ưu hóa truy cập tuần tự liên tục (Burst mode).
  - **High-order Interleaving (인터리빙 상위):** Các bit cao của địa chỉ dùng để chọn Module $\rightarrow$ Mỗi module chứa một dải địa chỉ liên tục $\rightarrow$ Phù hợp hệ thống đa xử lý độc lập.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Cấu trúc bên trong của CAM:**
  - CAM bao gồm: Thanh ghi đối sánh (Argument Register) lưu giá trị cần tìm, Thanh ghi mặt nạ (Mask Register) để lọc các bit quan tâm, Mảng từ nhớ CAM, và Mạch chỉ báo khớp (Match Logic).
  - Kết quả trả về là địa chỉ hoặc dữ liệu tương ứng của dòng có nội dung trùng khớp 100% chỉ trong 1 chu kỳ xung nhịp.

### 복습 체크리스트
- [ ] Nhớ từ khóa sống còn của 연관 기억장치: "주소가 아닌 내용의 일부로 접근" (Truy cập bằng nội dung thay vì địa chỉ).
- [ ] Nhớ ứng dụng của CAM: Dùng trong Cache và bảng ánh xạ trang bộ nhớ ảo.
- [ ] Nhớ cơ chế của 메모리 인터리빙: Phân tán địa chỉ trên nhiều module để CPU truy cập song song (병행 접근).
- [ ] Nắm được vai trò của Interleaving trong việc hỗ trợ truyền DMA tốc độ cao.
