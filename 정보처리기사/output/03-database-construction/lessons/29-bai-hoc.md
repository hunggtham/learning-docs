# A+ Deep Dive: SQL 결과를 행 단위로 추적하기

## 학습 목표 (Mục tiêu)
- Nắm vững thứ tự thực thi logic 6 bước của câu lệnh truy vấn SQL: **FROM $\rightarrow$ WHERE $\rightarrow$ GROUP BY $\rightarrow$ HAVING $\rightarrow$ SELECT $\rightarrow$ ORDER BY**.
- Theo dõi và truy vết chính xác kết quả đầu ra theo từng dòng dữ liệu (Row-level tracing) qua từng giai đoạn xử lý mệnh đề.
- Phân biệt bản chất giữa bộ lọc dòng cá thể (`WHERE`) và bộ lọc nhóm sau tập hợp (`HAVING`).
- Nhận diện các bẫy đề thi kinh điển: sử dụng hàm tập hợp trong WHERE hoặc sử dụng bí danh (Alias) trước khi mệnh đề SELECT được thực thi.

## 핵심 키워드 (Từ khóa)
- SQL 실행 순서 (Thứ tự thực thi SQL / Execution Order)
- FROM / WHERE / GROUP BY / HAVING / SELECT / ORDER BY
- 집계 함수 (Hàm tập hợp / Aggregate Functions: SUM, AVG, COUNT, MAX, MIN)
- 행 필터 (Bộ lọc dòng đơn lẻ - WHERE)
- 그룹 필터 (Bộ lọc nhóm - HAVING)
- 별칭 (Bí danh cột / Alias)
- 행 단위 추적 (Truy vết từng dòng dữ liệu / Row-Level Trace)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([16-bai-hoc.md](16-bai-hoc.md), [28-bai-hoc.md](28-bai-hoc.md)):** Thứ tự thực thi SQL phản ánh trực tiếp thứ tự các phép toán trong đại số quan hệ: Từ bảng nguồn (FROM), lọc hàng (Select $\sigma$ tương ứng WHERE), gom nhóm, lọc nhóm, chọn cột (Project $\pi$ tương ứng SELECT) và sắp xếp.
- **Tiếp nối sang bài sau ([30-bai-hoc.md](30-bai-hoc.md)):** Hiểu rõ thứ tự thực thi sẽ giúp áp dụng chính xác các toán tử điều kiện mở rộng như LIKE, BETWEEN, IN, và EXISTS mà không mắc lỗi cú pháp.

## 읽는 방법 (Cách đọc)
- Học thuộc như in trong đầu chuỗi 6 bước thực thi:
  $$\mathbf{FROM \rightarrow WHERE \rightarrow GROUP\ BY \rightarrow HAVING \rightarrow SELECT \rightarrow ORDER\ BY}$$
- Quy tắc vàng sống còn:
  - **WHERE lọc trước khi nhóm**; **HAVING lọc sau khi nhóm**.
  - **Tuyệt đối không dùng hàm tập hợp (như SUM, AVG, COUNT) trong WHERE**.
  - **Không dùng Alias đặt ở SELECT bên trong WHERE** (vì WHERE thực thi trước SELECT).

---

## A+ Deep Dive: SQL 결과를 행 단위로 추적하기

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Thứ tự thực thi logic 6 giai đoạn của câu lệnh SELECT (SQL 실행 순서 6단계):**
  | Thứ tự | Mệnh đề | Chức năng kỹ thuật trong bộ máy xử lý (Engine) |
  |:---:|---|---|
  | **1** | **FROM** | Xác định các bảng dữ liệu nguồn và thực hiện các phép kết nối (JOIN) nếu có. |
  | **2** | **WHERE** | Áp dụng điều kiện lọc trên **từng dòng đơn lẻ (hàng cá thể)** của bảng trước khi gom nhóm. |
  | **3** | **GROUP BY** | Nhóm các dòng có cùng giá trị trên các cột chỉ định thành các nhóm dữ liệu đại diện. |
  | **4** | **HAVING** | Áp dụng điều kiện lọc trên **các nhóm sau khi đã gom**, sử dụng kết quả của hàm tập hợp (Aggregate). |
  | **5** | **SELECT** | Trích xuất các cột cần hiển thị, áp dụng các phép tính toán, gán bí danh (Alias), và khử trùng lặp (DISTINCT). |
  | **6** | **ORDER BY** | Sắp xếp toàn bộ tập kết quả cuối cùng theo thứ tự tăng dần (ASC) hoặc giảm dần (DESC). |

- **2. Bảng so sánh kinh điển: WHERE vs HAVING:**
  | Tiêu chí | Mệnh đề WHERE | Mệnh đề HAVING |
  |---|---|---|
  | **Thời điểm thực thi** | Thực thi **trước** khi dữ liệu được gom nhóm (trước GROUP BY) | Thực thi **sau** khi dữ liệu đã được gom nhóm (sau GROUP BY) |
  | **Đối tượng áp dụng** | Áp dụng trên **từng dòng dữ liệu độc lập** của bảng | Áp dụng trên **từng nhóm dữ liệu tổng hợp** |
  | **Sử dụng hàm tập hợp** | **CẤM TUYỆT ĐỐI** (Không được dùng `SUM(cột) > 100`, `COUNT(*) >= 5`) | **HOÀN TOÀN HỢP LỆ** (Dùng để lọc nhóm: `HAVING AVG(Diem) >= 8.0`) |
  | **Sử dụng bí danh (Alias)** | Không dùng được bí danh của cột khai báo trong SELECT | Trong một số hệ DBMS có thể dùng, nhưng chuẩn ANSI vẫn ưu tiên biểu thức gốc |

- **주의/함정 (Các bẫy đề thi trắc nghiệm thường gặp):**
  - Đề đưa câu lệnh: `SELECT PhongBan, SUM(Luong) FROM NHAN_VIEN WHERE SUM(Luong) >= 5000 GROUP BY PhongBan;` $\rightarrow$ **Câu lệnh LỖI CÚ PHÁP**, vì `SUM(Luong)` là hàm tập hợp, không được nằm ở mệnh đề `WHERE` mà phải chuyển sang `HAVING`.
  - Đề hỏi: *"Mệnh đề nào được thực thi cuối cùng trong câu truy vấn SELECT?"* $\rightarrow$ Đáp án: **ORDER BY**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Truy vết kết quả theo từng dòng (Row-Level Trace) qua bài toán cụ thể:**
  - **Bảng nguồn `DON_HANG` (4 dòng):**
    | MaDH | PhongBan | DoanhSo |
    |:---:|:---:|:---:|
    | 1 | A | 120 |
    | 2 | A | 80 |
    | 3 | B | 90 |
    | 4 | B | 40 |
  - **Câu lệnh truy vấn:**
    ```sql
    SELECT PhongBan, SUM(DoanhSo) AS TongDoanhSo
    FROM DON_HANG
    WHERE DoanhSo >= 80
    GROUP BY PhongBan
    HAVING SUM(DoanhSo) >= 150
    ORDER BY TongDoanhSo DESC;
    ```
  - **Quá trình thực thi từng bước của DBMS:**
    - **Bước 1 (FROM DON_HANG):** Nạp toàn bộ 4 dòng của bảng.
    - **Bước 2 (WHERE DoanhSo >= 80):** Loại bỏ dòng 4 (`B, 40`). Còn lại 3 dòng: `(A, 120)`, `(A, 80)`, và `(B, 90)`.
    - **Bước 3 (GROUP BY PhongBan):** Gom thành 2 nhóm:
      - Nhóm `A`: gồm `(A, 120)` và `(A, 80)` $\rightarrow$ `SUM(DoanhSo) = 200`.
      - Nhóm `B`: gồm `(B, 90)` $\rightarrow$ `SUM(DoanhSo) = 90`.
    - **Bước 4 (HAVING SUM(DoanhSo) >= 150):** Nhóm `A` có tổng 200 $\ge$ 150 (Thỏa mãn). Nhóm `B` có tổng 90 < 150 (Bị loại bỏ).
    - **Bước 5 (SELECT):** Trích xuất cột `PhongBan` và `TongDoanhSo` $\rightarrow$ Kết quả tạm thời: `A | 200`.
    - **Bước 6 (ORDER BY TongDoanhSo DESC):** Sắp xếp kết quả $\rightarrow$ Kết quả cuối cùng trả về duy nhất **1 dòng: `A | 200`**.

### 복습 체크리스트
- [ ] Nhớ chính xác thứ tự: FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY.
- [ ] Nắm vững lý do tại sao hàm tập hợp không được đặt trong mệnh đề WHERE.
- [ ] Tự truy vết được bài toán lọc dòng kết hợp WHERE và HAVING.
- [ ] Hiểu được vì sao bí danh của SELECT không thể sử dụng ở mệnh đề WHERE.
