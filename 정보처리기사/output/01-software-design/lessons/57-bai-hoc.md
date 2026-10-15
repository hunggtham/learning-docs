# 14. 파일 편성 방식 (File Organization)

## 학습 목표 (Mục tiêu)
- Nắm vững 3 phương thức tổ chức tập tin dữ liệu vật lý trên bộ nhớ ngoài: Tập tin tuần tự (`순차 파일 - Sequential`), Tập tin chỉ mục tuần tự (`색인 순차 파일 - ISAM`), và Tập tin trực tiếp (`직접 파일 - Direct`).
- Thuộc nằm lòng cấu trúc 3 vùng nhớ đặc thù của tệp chỉ mục tuần tự ISAM: Vùng cơ sở (`기본 구역`), Vùng chỉ mục (`색인 구역`), và Vùng tràn (`오버플로 구역`).
- Phân biệt phạm vi áp dụng của thiết bị lưu trữ truy xuất tuần tự (`SASD` - Băng từ) và thiết bị truy xuất trực tiếp (`DASD` - Đĩa cứng).

## 핵심 키워드 (Từ khóa)
- 파일 편성 (Tổ chức tập tin / File Organization)
- 순차 파일 (Sequential File / 일괄 처리 / 자기 테이프 SASD)
- 색인 순차 파일 (Indexed Sequential File / ISAM / DASD)
- 기본 구역 (Prime Area / 실제 레코드 저장)
- 색인 구역 (Index Area: 트랙, 실린더, 마스터 색인)
- 오버플로 구역 (Overflow Area: 실린더, 독립 오버플로 구역)
- 직접 파일 (Direct File / Random File / 해시 함수 / DASD)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([13. 검색 및 해싱 (Search & Hashing)](56-bai-hoc.md)):** Sau khi xem xét các giải thuật tìm kiếm và bảng băm Hashing, bài này ứng dụng chúng vào các mô hình tổ chức lưu trữ file thực tế trên đĩa từ.
- **Tiếp nối sang cụm sau ([6. 애자일 방법론](58-bai-hoc.md)):** Chuyển từ hạ tầng dữ liệu và tập tin sang các bài học chuyên sâu về quy trình phát triển linh hoạt Agile, Scrum, XP và các chỉ số đo lường module.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để nhớ 3 vùng nhớ của ISAM (Prime, Index, Overflow) và phân biệt thiết bị: Tuần tự chạy được cả trên băng từ (SASD); ISAM và Direct bắt buộc phải chạy trên đĩa từ (DASD).
- Đọc TẦNG B để hiểu cơ chế phân cấp 3 tầng chỉ mục của ISAM (Track $\rightarrow$ Cylinder $\rightarrow$ Master Index).

---

## 14. 파일 편성 방식 (File Organization)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **3 phương thức tổ chức tập tin kinh điển:**
  1. **순차 파일 (Sequential File / 순차 편성 - Tập tin tuần tự):**
     - **Cơ chế:** Các bản ghi được ghi liên tục nối tiếp nhau vào bộ nhớ theo thứ tự khóa hoặc thứ tự thời gian xuất hiện.
     - *Thiết bị áp dụng:* Có thể lưu trên mọi loại phương tiện lưu trữ, bao gồm cả thiết bị truy xuất tuần tự như **Băng từ (`자기 테이프 - SASD`)** lẫn Đĩa từ (`DASD`).
     - *Ưu điểm:* Không lãng phí dung lượng đĩa, tận dụng tối đa không gian nhớ; **rất hiệu quả khi thực hiện các tác vụ xử lý hàng loạt (`일괄 처리 - Batch Processing`)**.
     - *Nhược điểm:* Việc chèn hoặc xóa một bản ghi ở giữa file cực kỳ phức tạp và tốn kém; truy xuất ngẫu nhiên rất chậm vì phải duyệt tuần tự từ đầu $O(N)$.
  2. **색인 순차 파일 (Indexed Sequential File / ISAM - Tập tin chỉ mục tuần tự):**
     - **Cơ chế:** Dữ liệu bản ghi được sắp xếp tuần tự theo khóa, đồng thời hệ thống xây dựng thêm các **Bảng chỉ mục (`색인 - Index`)** tương ứng.
     - *Đặc điểm:* Hỗ trợ **cả hai phương thức truy xuất: vừa có thể đọc tuần tự (Sequential), vừa có thể truy xuất ngẫu nhiên (Random Access)** thông qua chỉ mục.
     - *Thiết bị áp dụng:* Bắt buộc phải lưu trên thiết bị truy xuất trực tiếp như **Đĩa từ (`자기 디스크 - DASD`)**, không thể lưu trên băng từ.
     - **Cấu trúc 3 vùng nhớ của ISAM (Điểm thi trọng tâm):**
       1. `기본 구역 (Prime Area - Vùng cơ sở)`: Nơi lưu trữ các bản ghi dữ liệu thực tế tại thời điểm khởi tạo tệp.
       2. `색인 구역 (Index Area - Vùng chỉ mục)`: Lưu trữ các bảng chỉ mục phân tầng để tăng tốc độ định vị bản ghi. Gồm 3 cấp:
          - **트랙 색인 (Track Index)**: Chỉ mục trên từng rãnh đĩa (Track).
          - **실린더 색인 (Cylinder Index)**: Chỉ mục trên từng khối trụ đĩa (Cylinder).
          - **마스터 색인 (Master Index)**: Chỉ mục cấp cao nhất quản lý các Cylinder Index.
       3. `오버플로 구역 (Overflow Area - Vùng tràn)`: Chứa các bản ghi mới được chèn vào sau này khi Prime Area đã bị đầy kín:
          - *실린더 오버플로 구역 (Cylinder Overflow Area):* Vùng tràn nằm trên cùng một cylinder.
          - *독립 오버플로 구역 (Independent Overflow Area):* Vùng tràn độc lập nằm ở khu vực đĩa riêng biệt.
  3. **직접 파일 (Direct File / Random File - Tập tin trực tiếp):**
     - **Cơ chế:** Sử dụng **Hàm băm (`해시 함수 - Hashing`)** chuyển đổi trực tiếp giá trị khóa bản ghi thành địa chỉ khối vật lý trên đĩa cứng mà không cần tra cứu qua bảng chỉ mục.
     - *Ưu điểm:* Tốc độ truy xuất ngẫu nhiên **nhanh nhất trong các loại tệp ($O(1)$)**.
     - *Nhược điểm:* Phải lưu trên DASD; có thể xảy ra hiện tượng xung đột/tràn (Collision/Overflow); tốn kém dung lượng đĩa vì bảng băm có mật độ trống cao.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Tập tin tuần tự (순차 파일) có thể lưu trên băng từ (자기 테이프 - SASD) không?"* -> **Có thể (가능함)**. Nhưng ISAM và Direct File thì tuyệt đối KHÔNG thể lưu trên băng từ.
  - **Bẫy 2 (Cấu trúc ISAM):** 3 vùng nhớ của ISAM là gì? -> **기본 구역 (Prime Area), 색인 구역 (Index Area), và 오버플로 구역 (Overflow Area)**.
  - **Bẫy 3:** *"Tập tin chỉ mục tuần tự (ISAM) chỉ cho phép truy xuất tuần tự?"* -> **Sai**. ISAM hỗ trợ **CẢ truy xuất tuần tự LẪN truy xuất ngẫu nhiên**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Tuần tự lưu cả băng từ chạy hàng loạt; ISAM vừa tuần tự vừa ngẫu nhiên có 3 vùng Cơ sở, Chỉ mục, Tràn; Trực tiếp dùng hàm băm truy xuất tức thì".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Quy trình tra cứu bản ghi trong ISAM:**
  $$\text{Master Index (Tìm Cylinder)} \longrightarrow \text{Cylinder Index (Tìm Track)} \longrightarrow \text{Track Index (Tìm Block)} \longrightarrow \text{Prime Area (Đọc dữ liệu)}$$
  - Nhờ cấu trúc chỉ mục phân tầng này, thời gian tìm kiếm một bản ghi trong hàng triệu bản ghi giảm từ hàng nghìn phép đọc đĩa xuống chỉ còn 3 đến 4 lần đọc đĩa (I/O operations).

### 복습 체크리스트
- [ ] Phân biệt được đặc trưng của 3 loại tập tin: 순차, 색인 순차, 직접 파일.
- [ ] Nhớ tập tin tuần tự chạy được trên SASD (băng từ) và tối ưu cho xử lý hàng loạt.
- [ ] Thuộc tên 3 vùng nhớ của ISAM: 기본 구역, 색인 구역, 오버플로 구역.
- [ ] Nhớ tệp trực tiếp (Direct File) sử dụng hàm băm Hashing để truy xuất ngẫu nhiên.
