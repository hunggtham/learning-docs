# 200. 유지보수 (Maintenance / Bảo trì phần mềm)

## 학습 목표 (Mục tiêu)
- Nắm vững vai trò, tỷ trọng chi phí và tầm quan trọng của giai đoạn bảo trì phần mềm (소프트웨어 유지보수 - Software Maintenance) trong toàn bộ vòng đời SDLC.
- Phân biệt chính xác bản chất nghiệp vụ của 4 loại hình bảo trì phần mềm kinh điển: Sửa lỗi (수정 보수 / Corrective), Thích ứng môi trường (적응 보수 / Adaptive), Hoàn thiện nâng cấp (완전화 보수 / Perfective), và Phòng ngừa rủi ro (예방 보수 / Preventive).
- Ghi nhớ loại hình bảo trì nào chiếm tỷ trọng thời gian và ngân sách tài chính lớn nhất trong thực tế.

## 핵심 키워드 (Từ khóa)
- 소프트웨어 유지보수 (Software Maintenance)
- 수정 보수 (Corrective Maintenance - 하자 보수)
- 적응 보수 (Adaptive Maintenance - 환경 변화)
- 완전화 보수 (Perfective Maintenance - 기능 추가/성능 개선)
- 예방 보수 (Preventive Maintenance - 사전 예방/재공학)
- 가장 큰 비용 (Perfective Maintenance Dominance)
- 암기 공식 (수적완예)

## 선행·연결 개념 (Kiến thức liên kết)
- [61-bai-hoc.md](61-bai-hoc.md): Chiến lược kiểm thử phần mềm (Đơn vị, Tích hợp, Hệ thống).
- [63-bai-hoc.md](63-bai-hoc.md): Mã nguồn ngoài hành tinh (Alien Code) và hiểm họa khi thiếu tài liệu hóa.
- [67-bai-hoc.md](67-bai-hoc.md): Kỹ thuật tái công nghệ phần mềm (Software Reengineering).

## 읽는 방법 (Cách đọc)
- Khẩu quyết 4 loại hình bảo trì theo tiếng Hàn:
  $$\mathbf{수 \rightarrow 적 \rightarrow 완 \rightarrow 예}$$
  - **수**정 (Corrective): Thấy lỗi $\rightarrow$ Sửa (하자 보수).
  - **적**응 (Adaptive): Môi trường đổi (OS, HW) $\rightarrow$ Thích nghi (환경 적응).
  - **완**전 (Perfective): Người dùng muốn thêm tính năng, tăng tốc $\rightarrow$ Hoàn thiện (**Chiếm chi phí lớn nhất, khoảng 50% tổng chi phí bảo trì**).
  - **예**방 (Preventive): Sợ tương lai lỗi $\rightarrow$ Phòng ngừa trước (Refactoring).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Tỷ trọng ngân sách của giai đoạn bảo trì:**
  - Bảo trì là giai đoạn **kéo dài nhất và tiêu tốn nhiều nhân lực, chi phí nhất** trong toàn bộ vòng đời phát triển phần mềm (chiếm tới 60% ~ 70% tổng chi phí vòng đời).
  - Khác với suy nghĩ thông thường rằng "xây mới tốn tiền nhất", chi phí vận hành và nâng cấp phần mềm theo năm tháng mới là gánh nặng tài chính chính.

- **2. Bảng phân loại 4 hình thức bảo trì chuẩn mực:**

| Loại hình bảo trì | Tên tiếng Hàn & Anh | Mục đích kỹ thuật | Tỷ lệ chi phí |
| :--- | :--- | :--- | :---: |
| **Bảo trì sửa lỗi** | **수정 보수** (Corrective) | Khắc phục các lỗi sai sót (Bug), khiếm khuyết tiềm ẩn phát sinh trong quá trình vận hành mà giai đoạn kiểm thử trước đó chưa phát hiện được. | ~ 20% |
| **Bảo trì thích ứng** | **적응 보수** (Adaptive) | Điều chỉnh phần mềm để tương thích khi có sự thay đổi về môi trường vận hành (nâng cấp hệ điều hành mới, thay đổi phần cứng máy chủ, cập nhật phiên bản DBMS). | ~ 25% |
| **Bảo trì hoàn thiện** | **완전화 보수** (Perfective) | Bổ sung các chức năng nghiệp vụ mới theo yêu cầu cải tiến của người dùng, tái cấu trúc nâng cao hiệu năng và độ thân thiện của giao diện. | **~ 50% (Lớn nhất)** |
| **Bảo trì phòng ngừa** | **예방 보수** (Preventive) | Chủ động tái cấu trúc mã nguồn (Refactoring) và chuẩn hóa tài liệu trước khi lỗi xảy ra, nhằm kéo dài tuổi thọ phần mềm và giảm độ phức tạp sau này. | ~ 5% |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Hiện tượng suy thoái phần mềm (Software Deterioration / Aging):**
  - Mặc dù phần mềm không bị mài mòn vật lý như máy móc cơ khí, nhưng qua nhiều đợt bảo trì sửa lỗi chắp vá (Patching) vội vã mà không tuân thủ thiết kế ban đầu, mã nguồn sẽ dần bị rác hóa, xuất hiện mã ngoài hành tinh (Alien Code), làm tăng độ phức tạp và chi phí bảo trì cấp số nhân.

### 복습 체크리스트
- [ ] Thuộc lòng 4 loại hình bảo trì theo khẩu quyết: **수적완예** (수정, 적응, 완전, 예방).
- [ ] Ghi nhớ chắc chắn: **완전화 보수 (Perfective Maintenance)** là loại hình chiếm tỷ trọng chi phí cao nhất (khoảng 50%).
- [ ] Phân biệt được Adaptive (thích ứng thay đổi phần cứng/OS) và Corrective (sửa bug chức năng).
- [ ] Hiểu rõ Preventive Maintenance là hành động chủ động phòng ngừa lỗi tương lai qua tái cấu trúc mã.
