# 21. 데이터 전환 및 정제 (Chuyển đổi dữ liệu - ETL)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa của Chuyển đổi dữ liệu (`데이터 전환 / Data Migration`): Quá trình trích xuất dữ liệu từ hệ thống thông tin cũ (`추출`), biến đổi cho phù hợp với cấu trúc chuẩn mới (`변환`), và nạp vào hệ thống cơ sở dữ liệu mới (`적재`).
- Hiểu sâu bản chất kỹ thuật của 3 giai đoạn **ETL**: **Extraction (`추출`)**, **Transformation (`변환`)**, và **Loading (`적재`)**.
- Nắm vững quy trình quản lý vòng đời trạng thái của Dữ liệu lỗi (`오류 데이터 정제`): **Open (Phát hiện)** $\rightarrow$ **Assigned (Giao việc)** $\rightarrow$ **Fixed (Đã sửa)** $\rightarrow$ **Closed (Xác nhận đóng)**, cùng trạng thái **Deferred (Trì hoãn)**.

## 핵심 키워드 (Từ khóa)
- 데이터 전환 (Chuyển đổi dữ liệu / Data Migration)
- ETL (추출, 변환, 적재 / Extraction, Transformation, Load)
- 추출 (Extraction / Trích xuất)
- 변환 (Transformation / Biến đổi)
- 적재 (Loading / Nạp dữ liệu)
- 오류 데이터 정제 (Làm sạch dữ liệu lỗi / Data Cleansing)
- 오류 상태 주기 (Vòng đời lỗi: Open, Assigned, Fixed, Closed, Deferred)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([02-bai-hoc.md](02-bai-hoc.md), [15-bai-hoc.md](15-bai-hoc.md), [52-bai-hoc.md](52-bai-hoc.md)):** Để bảo đảm dữ liệu từ hệ thống cũ khi chuyển sang CSDL mới không vi phạm các ràng buộc toàn vẹn thực thể và miền giá trị, khâu Transformation trong ETL đóng vai trò gác cổng kiểm soát chất lượng.
- **Tiếp nối sang bài sau ([54-bai-hoc.md](54-bai-hoc.md)):** Sau khi chuyển đổi và nạp dữ liệu sạch vào CSDL mới, các khung làm việc ánh xạ đối tượng (như MyBatis, ORM) sẽ kết nối và xử lý dữ liệu thông qua ứng dụng.

## 읽는 방법 (Cách đọc)
- Học thuộc 3 chữ cái ETL ở TẦNG A: **E (추출 - Trích xuất) $\rightarrow$ T (변환 - Biến đổi) $\rightarrow$ L (적재 - Nạp)**.
- Ghi nhớ vòng đời 5 trạng thái quản lý lỗi dữ liệu:
  - **Open:** Vừa mới phát hiện lỗi.
  - **Assigned:** Đã giao cho người chịu trách nhiệm sửa.
  - **Fixed:** Lập trình viên đã sửa xong.
  - **Closed:** Đã kiểm thử lại xác nhận dữ liệu chuẩn xác 100%.
  - **Deferred:** Tạm hoãn xử lý sang giai đoạn sau.

---

## 21. 데이터 전환 및 정제 (Chuyển đổi dữ liệu - ETL)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Định nghĩa Chuyển đổi dữ liệu (데이터 전환의 개념):**
  - Là toàn bộ chuỗi tiến trình kỹ thuật nhằm **trích xuất (Extraction)** dữ liệu tích lũy từ hệ thống thông tin kế thừa cũ (Legacy System), **chuyển đổi (Transformation)** định dạng và chuẩn hóa để tương thích với cấu trúc của hệ thống thông tin mới, sau đó **nạp (Loading)** an toàn vào cơ sở dữ liệu đích.
  - Được tiến hành khi nâng cấp phiên bản phần mềm, sáp nhập cơ sở dữ liệu doanh nghiệp, hoặc xây dựng Kho dữ liệu (Data Warehouse).
- **2. Ba giai đoạn trong quy trình ETL (ETL 3단계):**
  | Giai đoạn ETL | Thuật ngữ Hàn - Anh | Nội dung kỹ thuật thực hiện |
  |:---:|---|---|
  | **E** | `추출` (Extraction) | Đọc và trích xuất dữ liệu từ nhiều nguồn phân tán khác nhau (RDBMS cũ, tệp phẳng CSV, tệp Excel, bản ghi log, XML). |
  | **T** | `변환` (Transformation) | Làm sạch dữ liệu rác, chuẩn hóa định dạng (ví dụ: đổi ngày `DD/MM/YYYY` sang `YYYY-MM-DD`), loại bỏ trùng lặp, mã hóa bảo mật, và đối chiếu các quy tắc toàn vẹn miền. |
  | **L** | `적재` (Loading) | Ghi dữ liệu đã làm sạch vào các bảng vật lý của cơ sở dữ liệu đích hoặc Data Mart / Data Warehouse. |

- **3. Vòng đời 5 trạng thái quản lý Dữ liệu lỗi (오류 데이터 정제 상태 주기):**
  | Trạng thái | Thuật ngữ tiếng Hàn & Anh | Khái niệm & Hành động kỹ thuật |
  |---|---|---|
  | **Open** | `오류 발생 / 오픈` | Dữ liệu lỗi vừa được công cụ kiểm toán hoặc kỹ sư phát hiện trong quá trình ETL; lỗi được ghi nhận vào nhật ký nhưng chưa được phân tích nguyên nhân. |
  | **Assigned** | `담당자 할당` | Lỗi dữ liệu được bàn giao chính thức cho kỹ sư dữ liệu hoặc lập trình viên phụ trách mô-đun đó để nghiên cứu phương án khắc phục. |
  | **Fixed** | `조치 완료 / 수정` | Lập trình viên đã hoàn thành việc chỉnh sửa mã nguồn làm sạch hoặc điều chỉnh ánh xạ chuyển đổi dữ liệu. |
  | **Closed** | `검증 완료 / 종료` | Đội ngũ kiểm thử đã chạy lại tiến trình chuyển đổi trên dữ liệu thực tế, kiểm tra tính toàn vẹn và xác nhận dữ liệu đã nạp thành công, chính thức đóng lỗi. |
  | **Deferred** | `조치 연기 / 보류` | Quyết định tạm hoãn việc sửa chữa dữ liệu sang các đợt phát hành sau do mức độ ưu tiên thấp hoặc chi phí sửa đổi quá lớn. |

- **주의/함정 (Bẫy đề thi trắc nghiệm):**
  - Đề hỏi: *"Trình tự 3 bước của quy trình di chuyển dữ liệu là gì?"* $\rightarrow$ Đáp án: **추출(Extraction) $\rightarrow$ 변환(Transformation) $\rightarrow$ 적재(Loading)**.
  - Đề hỏi: *"Trạng thái sau khi dữ liệu lỗi đã được sửa xong và kiểm thử thành công được gọi là gì?"* $\rightarrow$ Đáp án: **Closed (종료 / 검증 완료)**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Minh họa quy trình Data Cleansing (Làm sạch dữ liệu):**
  - Hệ thống cũ có các lỗi dữ liệu phổ biến:
    - Cột `SoDienThoai` bị dính chữ cái hoặc khoảng trắng: `'090-123-4567'`, `'090 123 4567'`, `'090abc1234'`.
    - Cột `GioiTinh` lưu lung tung: `'Nam'`, `'M'`, `'1'`, `'Male'`.
  - Trong bước **Transformation**:
    - Công cụ ETL áp dụng biểu thức chính quy (Regex) để lọc sạch ký tự rác, chuẩn hóa số điện thoại về chuỗi 10 chữ số thuần túy `0901234567`.
    - Chuẩn hóa cột giới tính về miền giá trị hợp lệ duy nhất là `'M'` hoặc `'F'`.

### 복습 체크리스트
- [ ] Định nghĩa được 데이터 전환 và 3 bước ETL (추출, 변환, 적재).
- [ ] Phân tích được các công việc chính trong bước Transformation (변환).
- [ ] Nhớ thứ tự vòng đời quản lý lỗi: Open -> Assigned -> Fixed -> Closed (và trạng thái Deferred).
- [ ] Nêu ví dụ về việc làm sạch dữ liệu trong thực tế.
