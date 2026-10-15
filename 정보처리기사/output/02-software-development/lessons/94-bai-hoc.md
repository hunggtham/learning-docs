# 090-1: 데이터의 독립성 (Data Independence)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và ý nghĩa sống còn của tính độc lập dữ liệu (데이터의 독립성 - Data Independence) trong các hệ thống cơ sở dữ liệu hiện đại.
- Phân biệt sâu sắc hai cấp độ độc lập dữ liệu: Tính độc lập logic (논리적 독립성 - Logical Data Independence) và Tính độc lập vật lý (물리적 독립성 - Physical Data Independence).
- Hiểu rõ cơ chế hai lớp ánh xạ (사상 - Mapping) của kiến trúc 3 tầng lược đồ ANSI/SPARC giúp hiện thực hóa tính độc lập dữ liệu như thế nào.

## 핵심 키워드 (Từ khóa)
- 데이터 독립성 (Data Independence)
- 논리적 독립성 (Logical Data Independence / 외부-개념 사상)
- 물리적 독립성 (Physical Data Independence / 개념-내부 사상)
- 사상 (Mapping / 사상 함수)
- 데이터 종속성 해소 (Elimination of Data Dependency)
- 응용 프로그램 수정 최소화 (Application Modification Minimization)

## 선행·연결 개념 (Kiến thức liên kết)
- [93-bai-hoc.md](93-bai-hoc.md): Đặc trưng cơ sở dữ liệu và hệ thống DBMS.
- [95-bai-hoc.md](95-bai-hoc.md): Lược đồ cơ sở dữ liệu (Schema 3 tầng).
- [71-bai-hoc.md](71-bai-hoc.md): Chi tiết kiến trúc 3 tầng lược đồ ANSI/SPARC.

## 읽는 방법 (Cách đọc)
- Phân biệt hai loại độc lập qua tác động:
  - **논리적 독립성 (Độc lập Logic):** Khi DBA sửa đổi cấu trúc bảng ở tầng giữa (thêm cột mới, đổi tên bảng, tách bảng), các chương trình ứng dụng cũ của người dùng (Application) **không bị lỗi và không cần viết lại mã nguồn**. Tầng ánh xạ Ngoại - Quan niệm (External-Conceptual Mapping) sẽ chịu trách nhiệm chuyển đổi.
  - **물리적 독립성 (Độc lập Vật lý):** Khi kỹ sư thay đổi thiết bị lưu trữ (nâng cấp từ HDD sang SSD, thay đổi dung lượng khối block đĩa, đổi thuật toán chỉ mục B-Tree), cấu trúc logic của cơ sở dữ liệu và mã ứng dụng **hoàn toàn không bị ảnh hưởng**. Tầng ánh xạ Quan niệm - Trong (Conceptual-Internal Mapping) sẽ tự động điều phối.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng so sánh hai cấp độ độc lập dữ liệu:**

| Cấp độ độc lập | Tầng ánh xạ đảm nhiệm | Khi nào xảy ra thay đổi? | Kết quả bảo đảm |
| :--- | :--- | :--- | :--- |
| **논리적 독립성 (Độc lập logic)** | **외부 - 개념 사상 (External-Conceptual Mapping)** | Khi cấu trúc dữ liệu quan niệm thay đổi (thêm bảng mới, bổ sung trường dữ liệu mới) | **Ứng dụng của người dùng (외부 스키마 / 응용 프로그램) không cần thay đổi**, vẫn chạy bình thường |
| **물리적 독립성 (Độc lập vật lý)** | **개념 - 내부 사상 (Conceptual-Internal Mapping)** | Khi thiết bị phần cứng lưu trữ hoặc cấu trúc tệp đĩa thay đổi (đổi index, đổi block size, đổi ổ cứng) | **Cấu trúc logic của cơ sở dữ liệu (개념 스키마) và ứng dụng hoàn toàn không bị ảnh hưởng** |

- **So sánh với hệ thống tệp truyền thống (File Processing System):**
  - Hệ thống tệp có tính phụ thuộc cao (Data Dependency): Cấu trúc dữ liệu bị gắn chặt vào mã nguồn của chương trình. Chỉ cần định dạng một trường dữ liệu trong file bị đổi từ 8 ký tự thành 10 ký tự là toàn bộ chương trình đọc file đó bị sập và phải biên dịch lại từ đầu.
  - DBMS loại bỏ sự phụ thuộc này nhờ tính độc lập dữ liệu hai tầng.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Cơ chế hoạt động của Ánh xạ (Mapping / 사상):**
  - Khi một cột mới được thêm vào bảng nhân viên (`ALTER TABLE employee ADD COLUMN address VARCHAR(100);`), các ứng dụng chỉ truy vấn cột `id` và `name` thông qua View cũ vẫn nhận được kết quả nguyên vẹn nhờ ánh xạ logic.
  - Nhờ có tính độc lập vật lý, DBA có thể thoải mái tạo thêm hoặc xóa bỏ các chỉ mục (Index) để tối ưu hiệu năng mà không sợ làm hỏng logic của các câu lệnh SQL nghiệp vụ.

### 복습 체크리스트
- [ ] Nhớ tính độc lập logic liên kết với ánh xạ 외부-개념 사상.
- [ ] Nhớ tính độc lập vật lý liên kết với ánh xạ 개념-내부 사상.
- [ ] Giải thích được tại sao thêm cột mới vào DB lại không làm sập các chương trình ứng dụng cũ.
- [ ] Phân biệt được sự phụ thuộc dữ liệu của hệ thống tệp với sự độc lập dữ liệu của DBMS.
