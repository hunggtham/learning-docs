# 14. 파레토 법칙 (Pareto Principle)

## 학습 목표 (Mục tiêu)
- Nắm vững định luật Pareto (파레토 법칙 - Nguyên lý 80/20) trong kiểm thử phần mềm và quản lý chất lượng dự án.
- Hiểu rõ hiện tượng tập trung lỗi (결함 집중 - Defect Clustering): khoảng 80% tổng số khiếm khuyết trong phần mềm thường xuất hiện tập trung trong 20% các mô-đun phức tạp hoặc quan trọng nhất.
- Biết cách vận dụng định luật Pareto để tối ưu hóa nguồn lực kiểm thử, tập trung kiểm thử chuyên sâu vào các thành phần trọng yếu có nguy cơ lỗi cao.

## 핵심 키워드 (Từ khóa)
- 파레토 법칙 (Pareto Principle / 80:20 Rule)
- 결함 집중 (Defect Clustering)
- 위험 기반 테스팅 (Risk-based Testing)
- 테스팅 원리 (Principles of Testing)
- 살충제 패러독스 (Pesticide Paradox)

## 선행·연결 개념 (Kiến thức liên kết)
- [71-bai-hoc.md](71-bai-hoc.md): Kiến trúc ba tầng lược đồ trong cơ sở dữ liệu.
- [73-bai-hoc.md](73-bai-hoc.md): Độ phức tạp thời gian trong trường hợp xấu nhất.
- [56-bai-hoc.md](56-bai-hoc.md): Các nguyên lý cốt lõi của kiểm thử phần mềm (Testing Principles).

## 읽는 방법 (Cách đọc)
- Liên hệ giữa định luật Pareto và chiến lược kiểm thử thực tế:
  - Nếu một dự án có 100 mô-đun, không nên dàn trải nguồn lực kiểm thử đều nhau 1% cho mỗi mô-đun.
  - Cần xác định 20 mô-đun cốt lõi (xử lý nghiệp vụ phức tạp, tương tác dữ liệu liên tục, hoặc do các lập trình viên mới viết) vì 80% lỗi sẽ tập trung ở đây.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Nội dung định luật Pareto trong kiểm thử phần mềm:**

| Khái niệm | Tỷ lệ vàng | Ý nghĩa cốt lõi trong phần mềm | Ứng dụng thực tế |
| :--- | :--- | :--- | :--- |
| **파레토 법칙 (Pareto Principle)** | **80 : 20** | **Khoảng 80% lỗi (Defects/Faults)** được phát hiện chỉ tập trung trong **khoảng 20% số mô-đun** của toàn bộ hệ thống | Phân bổ ngân sách, thời gian và nhân lực kiểm thử ưu tiên cho nhóm 20% mô-đun rủi ro cao nhất |
| **결함 집중 (Defect Clustering)** | Hiện tượng bó cụm lỗi | Các lỗi không phân bố đồng đều ngẫu nhiên mà thường kết cụm tại các thành phần logic phức tạp | Khi phát hiện 1 lỗi trong mô-đun, cần tiếp tục kiểm tra kỹ mô-đun đó vì khả năng còn nhiều lỗi khác ẩn giấu |

- **Bảng so sánh các nguyên lý kiểm thử liên quan:**

| Nguyên lý kiểm thử | Bản chất vấn đề | Giải pháp khắc phục |
| :--- | :--- | :--- |
| **파레토 법칙 (Pareto / Defect Clustering)** | Lỗi tập trung ở 20% mô-đun phức tạp | Áp dụng kiểm thử dựa trên rủi ro (Risk-based Testing) để dồn lực vào 20% trọng điểm |
| **살충제 패러독스 (Pesticide Paradox)** | Chạy mãi một bộ test case cũ thì sâu bọ kháng thuốc, không tìm thêm được lỗi mới | Định kỳ rà soát, cập nhật và viết thêm các test case mới |
| **오류-부재의 궤변 (Absence-of-Errors Fallacy)** | Sửa hết 100% lỗi kỹ thuật nhưng phần mềm không đáp ứng đúng nhu cầu người dùng thì vẫn là thất bại | Luôn bám sát yêu cầu nghiệp vụ thực tế của người dùng cuối |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Phương pháp xác định 20% mô-đun rủi ro cao:**
  - Sử dụng độ đo độ phức tạp vòng Cyclomatic Complexity của McCabe: Những hàm có độ phức tạp Cyclomatic $V(G) > 10$ có nguy cơ lỗi cao gấp nhiều lần.
  - Đánh giá lịch sử thay đổi mã nguồn (Code Churn): Các tệp thường xuyên bị sửa đổi (commit liên tục) thường chứa nhiều lỗi hồi quy.

### 복습 체크리스트
- [ ] Nhớ con số tỷ lệ vàng của Pareto: 80% lỗi nằm trong 20% mô-đun.
- [ ] Nhớ thuật ngữ 결함 집중 (Defect Clustering) đồng nghĩa với hiện tượng mô tả trong định luật Pareto.
- [ ] Phân biệt được Pareto với Pesticide Paradox và Absence-of-Errors Fallacy.
