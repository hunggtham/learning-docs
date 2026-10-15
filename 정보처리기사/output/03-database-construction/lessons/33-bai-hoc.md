# 191-192. 인덱스 (Index)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và bản chất vật lý của Chỉ mục (`인덱스 / Index`): Cấu trúc dữ liệu dạng cặp `<Giá trị khóa, Con trỏ>` (`<키 값, 포인터>`) giúp hệ quản trị CSDL truy xuất nhanh chóng đến các khối dữ liệu trên đĩa.
- Phân tích chi tiết 5 loại cấu trúc chỉ mục theo giáo trình thi Kỹ sư xử lý thông tin Hàn Quốc: **Chỉ mục cây B+Tree (`트리 기반 인덱스`)**, **Chỉ mục Bitmap (`비트맵 인덱스`)**, **Chỉ mục dựa trên hàm (`함수 기반 인덱스`)**, **Chỉ mục kết nối Bitmap (`비트맵 조인 인덱스`)**, và **Chỉ mục mở rộng miền (`도메인 인덱스`)**.
- Nhớ rõ nguyên tắc vàng khi thiết kế chỉ mục: Bảng có nhiều thao tác INSERT/DELETE liên tục thì phải hạn chế số lượng chỉ mục để tránh quá tải hệ thống.

## 핵심 키워드 (Từ khóa)
- 인덱스 (Chỉ mục / Index)
- 키 값과 포인터 (<Giá trị khóa, Con trỏ>)
- B+ 트리 인덱스 (Chỉ mục B+ Tree)
- 비트맵 인덱스 (Chỉ mục Bitmap: 0 và 1)
- 함수 기반 인덱스 (Chỉ mục dựa trên hàm / Function-Based Index)
- 비트맵 조인 인덱스 (Chỉ mục kết nối Bitmap / Bitmap Join Index)
- 도메인 인덱스 (Chỉ mục miền mở rộng / Extensible Index)
- 클러스터드 인덱스 (Chỉ mục gom cụm / Clustered Index)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([03-bai-hoc.md](03-bai-hoc.md), [21-bai-hoc.md](21-bai-hoc.md), [24-bai-hoc.md](24-bai-hoc.md)):** Chỉ mục là công cụ vật lý cốt lõi giúp Bộ tối ưu hóa truy vấn (CBO/RBO) tránh việc phải quét toàn bộ bảng (`Table Full Scan`), từ đó tăng tốc vượt bậc các câu lệnh SELECT.
- **Tiếp nối sang các bài sau ([34-bai-hoc.md](34-bai-hoc.md), [35-bai-hoc.md](35-bai-hoc.md)):** Trong các hệ thống CSDL phân tán (`분산 데이터베이스`), chỉ mục được lưu trữ phân tán trên từng nút mạng để tăng tốc độ truy vấn cục bộ.

## 읽는 방법 (Cách đọc)
- Học thuộc bảng 5 loại Index ở TẦNG A:
  - B+Tree: Phổ biến nhất, tìm kiếm khoảng xuất sắc.
  - Bitmap: Dùng bit 0/1 cho cột ít giá trị phân biệt (Low Cardinality).
  - Function-Based: Dùng hàm/biểu thức, tốn chi phí tính toán khi Insert/Update.
  - Domain Index: Lập trình viên tự định nghĩa mở rộng.
- Nhớ câu hỏi trắc nghiệm kinh điển: **Khi nào nên giảm số lượng Index? $\rightarrow$ Khi bảng có thao tác INSERT, DELETE diễn ra thường xuyên**.

---

## 191-192. 인덱스 (Index)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Khái niệm và Đặc trưng của Chỉ mục (인덱스의 개요):**
  - Là cấu trúc dữ liệu lưu trữ các cặp **`<Giá trị khóa, Con trỏ>` (`<키 값, 포인터>`)** nhằm cung cấp đường dẫn truy cập trực tiếp và nhanh nhất đến các bản ghi trên ổ đĩa.
  - Được tạo lập, thay đổi và xóa bỏ bằng các câu lệnh ngôn ngữ định nghĩa dữ liệu **DDL** (`CREATE INDEX`, `DROP INDEX`).
  - **Quy tắc thiết kế hiệu năng:** Việc tạo quá nhiều chỉ mục sẽ làm chậm nghiêm trọng các thao tác **`INSERT`, `UPDATE`, `DELETE`**, vì mỗi khi sửa đổi dữ liệu DBMS bắt buộc phải tính toán và cập nhật lại toàn bộ cây chỉ mục tương ứng.
- **2. Bảng phân loại 5 cấu trúc Chỉ mục trong đề thi:**
  | Tên loại Index | Thuật ngữ Hàn - Anh | Cấu trúc & Đặc trưng kỹ thuật | Trường hợp áp dụng tối ưu |
  |---|---|---|---|
  | **Chỉ mục cây B+** | `트리 기반 인덱스` (B+ Tree Index) | Các khối chỉ mục tổ chức theo cấu trúc cây cân bằng (Root $\rightarrow$ Branch $\rightarrow$ Leaf). Các nút lá được liên kết kép hai chiều. | Phổ biến nhất trong các RDBMS thương mại (Oracle, MySQL, PostgreSQL). Rất tối ưu cho tìm kiếm chính xác và tìm kiếm theo khoảng (`BETWEEN`, `<`, `>`). |
  | **Chỉ mục Bitmap** | `비트맵 인덱스` (Bitmap Index) | Chuyển đổi dữ liệu của cột thành các bit nhị phân `0` hoặc `1` để làm khóa chỉ mục. Kích thước cực nhỏ gọn. | Tối ưu cho các cột có **độ phân biệt thấp (Low Cardinality)** như Giới tính (`Nam/Nữ`), Tình trạng hôn nhân. Rất phổ biến trong Kho dữ liệu (Data Warehouse). |
  | **Chỉ mục dựa trên hàm** | `함수 기반 인덱스` (Function-Based Index) | Không dùng giá trị gốc của cột mà dùng giá trị tính toán sau khi áp dụng hàm (`Function`) hoặc biểu thức (`Expression`). | Dùng khi câu lệnh truy vấn thường xuyên chứa hàm ở mệnh đề WHERE (ví dụ: `WHERE UPPER(Email) = ...`). Tốn thêm tải CPU khi nhập dữ liệu. |
  | **Chỉ mục kết nối Bitmap** | `비트맵 조인 인덱스` (Bitmap Join Index) | Chỉ mục gồm nhiều đối tượng đã được kết nối (JOIN) trước với nhau, tối ưu riêng cho các phép Join phức tạp. | Dùng trong mô hình Star Schema của Data Warehouse để tăng tốc truy vấn Join giữa bảng Fact và Dimension. |
  | **Chỉ mục miền mở rộng** | `도메인 인덱스` (Domain / Extensible Index) | Chỉ mục chuyên biệt do chính lập trình viên hoặc nhà phát triển tự thiết kế và cài đặt theo nghiệp vụ đặc thù. | Xử lý dữ liệu không gian địa lý (GIS), dữ liệu đa phương tiện hoặc dữ liệu văn bản phi cấu trúc. |

- **3. Phân biệt Clustered Index vs Non-Clustered Index:**
  - **클러스터드 인덱스 (Clustered Index):** Dữ liệu thực tế trên đĩa được sắp xếp vật lý theo thứ tự chỉ mục; **mỗi bảng chỉ có DUY NHẤT 1** Clustered Index.
  - **넌클러스터드 인덱스 (Non-Clustered Index):** Dữ liệu thực tế không đổi vị trí, nút lá chứa con trỏ trỏ đến dòng dữ liệu; **mỗi bảng có thể tạo NHIỀU** Non-Clustered Index.
- **주의/함정 (Bẫy đề thi trắc nghiệm):**
  - Đề hỏi: *"Chỉ mục nào chuyển dữ liệu thành bit 0 hoặc 1?"* $\rightarrow$ Đáp án: **비트맵 인덱스 (Bitmap Index)**.
  - Đề hỏi: *"Khi nào cần tối thiểu hóa số lượng chỉ mục trên một bảng?"* $\rightarrow$ Đáp án: **Khi các thao tác INSERT, DELETE xảy ra thường xuyên (레코드의 삽입과 삭제가 수시로 일어나는 경우)**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Minh họa cơ chế hoạt động của Bitmap Index:**
  - Bảng `KHACH_HANG` có cột `GioiTinh` gồm các giá trị `M` (Nam) và `F` (Nữ) cho 5 dòng:
    - Dòng 1: `M`
    - Dòng 2: `F`
    - Dòng 3: `M`
    - Dòng 4: `M`
    - Dòng 5: `F`
  - Bitmap tương ứng:
    - Vector `M`: `1 0 1 1 0`
    - Vector `F`: `0 1 0 0 1`
  - Khi người dùng truy vấn `WHERE GioiTinh = 'M'`: DBMS chỉ cần thực hiện phép toán bit logic `AND/OR` trên CPU ở tốc độ nano giây, không cần đọc từng dòng dữ liệu từ đĩa.

### 복습 체크리스트
- [ ] Định nghĩa được 인덱스 là cấu trúc cặp `<키 값, 포인터>`.
- [ ] Kể tên và giải thích 5 loại cấu trúc chỉ mục: B+ 트리, 비트맵, 함수 기반, 비트맵 조인, 도메인 인덱스.
- [ ] Phân biệt được Clustered Index (1 cái) và Non-Clustered Index (nhiều cái).
- [ ] Nhớ rõ nguyên tắc: bảng có nhiều INSERT/DELETE thì nên giữ số lượng Index ở mức tối thiểu.
