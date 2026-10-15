# 6. DDL, DML, DCL 상세 (Chi tiết DDL, DML, DCL)

## 학습 목표 (Mục tiêu)
- Nắm vững toàn bộ cú pháp chi tiết và các tùy chọn nâng cao của 3 nhóm ngôn ngữ SQL: **DDL (`데이터 정의어`)**, **DML (`데이터 조작어`)**, và **DCL/TCL (`데이터 제어어 / 트랜잭션 제어어`)**.
- Phân biệt chi tiết 3 hàm xếp hạng (Ranking Functions) kinh điển trong đề thi: **`RANK()`**, **`DENSE_RANK()`**, và **`ROW_NUMBER()`**.
- Phân biệt sự khác nhau giữa hai mệnh đề tổng hợp đa chiều: **`ROLLUP`** (tổng con phân cấp) và **`CUBE`** (tổng con đa chiều toàn diện).
- Nắm chắc sự khác biệt giữa `DROP TABLE`, `TRUNCATE TABLE`, và `DELETE FROM TABLE`.

## 핵심 키워드 (Từ khóa)
- DDL / DML / DCL / TCL 상세 문법 (Cú pháp chi tiết)
- TRUNCATE TABLE (Xóa trắng bảng không thể Rollback)
- 순위 함수 (Hàm xếp hạng / Ranking Functions)
- RANK() (Xếp hạng bỏ cách: 1, 1, 3)
- DENSE_RANK() (Xếp hạng liên tục: 1, 1, 2)
- ROW_NUMBER() (Đánh số thứ tự dòng: 1, 2, 3)
- ROLLUP (Hàm tổng con phân cấp) / CUBE (Hàm tổng con đa chiều)
- 집계 함수 (Hàm tập hợp: STDDEV, VARIANCE)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([26-bai-hoc.md](26-bai-hoc.md), [28-bai-hoc.md](28-bai-hoc.md), [29-bai-hoc.md](29-bai-hoc.md)):** Sau khi nắm khung sườn cơ bản của SQL ở bài 26-29, bài học này nâng cấp lên toàn bộ các tính năng phân tích nâng cao của SQL:2016 như Window Functions và Grouping Sets.
- **Tiếp nối sang bài sau ([51-bai-hoc.md](51-bai-hoc.md)):** Để kết hợp dữ liệu giữa nhiều bảng phức tạp, kỹ sư phối hợp các hàm nâng cao này cùng với các toán tử tập hợp (UNION, INTERSECT, MINUS) và các dạng JOIN.

## 읽는 방법 (Cách đọc)
- Học thuộc bảng phân biệt 3 hàm xếp hạng ở TẦNG A:
  - Cùng điểm nhận cùng hạng, **bỏ qua số hạng tiếp theo (1, 1, 3)** $\rightarrow$ **`RANK()`**.
  - Cùng điểm nhận cùng hạng, **không bỏ qua số hạng tiếp theo (1, 1, 2)** $\rightarrow$ **`DENSE_RANK()`**.
  - Không quan tâm điểm số, **đánh số thứ tự duy nhất tăng dần (1, 2, 3)** $\rightarrow$ **`ROW_NUMBER()`**.
- Nhớ câu phân biệt ROLLUP vs CUBE:
  - **ROLLUP:** Tính tổng con phân cấp một chiều (phải qua trái) + Tổng cộng.
  - **CUBE:** Tính tất cả các tổ hợp tổng con khả dĩ của các cột (đa chiều).

---

## 6. DDL, DML, DCL 상세 (Chi tiết DDL, DML, DCL)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Phân biệt các lệnh xóa dữ liệu và bảng:**
  | Câu lệnh | Nhóm ngôn ngữ | Bản chất thao tác | Khả năng khôi phục (Rollback) | Tốc độ xử lý |
  |---|:---:|---|:---:|:---:|
  | **`DROP TABLE`** | DDL | Xóa toàn bộ dữ liệu và **xóa luôn cả định nghĩa cấu trúc bảng** khỏi CSDL | **Không thể Rollback** (Auto-commit) | Cực nhanh |
  | **`TRUNCATE TABLE`** | DDL | Xóa toàn bộ dữ liệu, giải phóng vùng nhớ khối đĩa, **giữ lại cấu trúc bảng rỗng** | **Không thể Rollback** (Auto-commit) | Cực nhanh |
  | **`DELETE FROM`** | DML | Xóa từng dòng bản ghi dữ liệu (có thể kèm điều kiện `WHERE`), ghi log từng dòng | **Có thể Rollback** trước khi Commit | Chậm hơn |

- **2. Bảng phân tích 3 hàm xếp hạng bắt buộc trong đề thi (순위 함수):**
  | Hàm xếp hạng | Quy tắc đánh số khi trùng điểm | Ví dụ kết quả với dãy điểm: [100, 90, 90, 80] |
  |---|---|:---:|
  | **`RANK()`** | Các dòng có cùng giá trị nhận cùng một thứ hạng; **thứ hạng tiếp theo bị nhảy cóc / bỏ qua** tương ứng với số lượng dòng bị trùng. | **1, 2, 2, 4** (Hạng 3 bị bỏ qua) |
  | **`DENSE_RANK()`** | Các dòng có cùng giá trị nhận cùng một thứ hạng; **thứ hạng tiếp theo KHÔNG bị bỏ qua**, đánh số liên tục kế tiếp. | **1, 2, 2, 3** (Không bỏ sót hạng nào) |
  | **`ROW_NUMBER()`** | Không quan tâm giá trị có bị trùng hay không; **mỗi dòng luôn nhận một số thứ tự duy nhất tăng dần**. | **1, 2, 3, 4** (Đánh số tuần tự) |

- **3. Các hàm tổng hợp nhóm nâng cao (GROUP BY 확장 함수):**
  - **`ROLLUP(A, B)`:** Tính toán các tổng phụ phân cấp từ phải sang trái:
    - Nhóm theo `(A, B)` $\rightarrow$ Tổng con theo `(A)` $\rightarrow$ Tổng chung toàn bộ hệ thống (`Grand Total`).
  - **`CUBE(A, B)`:** Tính toán tất cả các tổ hợp tổng có thể có ($2^N$ tổ hợp):
    - Nhóm theo `(A, B)`, nhóm theo `(A)`, nhóm theo `(B)`, và Tổng chung toàn bộ hệ thống.
  - **Các hàm thống kê tập hợp:** Ngoài `SUM`, `AVG`, `COUNT`, `MAX`, `MIN`, đề thi còn có:
    - **`STDDEV`:** Tính độ lệch chuẩn của tập dữ liệu.
    - **`VARIANCE`:** Tính phương sai của tập dữ liệu.
- **주의/함정 (Bẫy đề thi trắc nghiệm):**
  - Đề hỏi: *"Khi có hai người cùng đồng hạng nhì (hạng 2), người tiếp theo được xếp hạng 4 thì đó là hàm gì?"* $\rightarrow$ Đáp án: **`RANK()`**.
  - Đề hỏi: *"Lệnh nào xóa toàn bộ dữ liệu trong bảng nhanh chóng nhưng không thể hoàn tác bằng Rollback?"* $\rightarrow$ Đáp án: **`TRUNCATE TABLE`**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Minh họa cú pháp hàm Xếp hạng trong SQL thực tế:**
  ```sql
  SELECT HoTen, Diem,
         RANK() OVER (ORDER BY Diem DESC) AS Rank_Result,
         DENSE_RANK() OVER (ORDER BY Diem DESC) AS Dense_Result,
         ROW_NUMBER() OVER (ORDER BY Diem DESC) AS Row_Result
  FROM SINH_VIEN;
  ```
- **Kết quả minh họa trực quan:**
  | HoTen | Diem | Rank_Result | Dense_Result | Row_Result |
  |---|:---:|:---:|:---:|:---:|
  | Kim | 100 | **1** | **1** | **1** |
  | Lee | 90 | **2** | **2** | **2** |
  | Park | 90 | **2** | **2** | **3** |
  | Choi | 80 | **4** | **3** | **4** |

### 복습 체크리스트
- [ ] Phân biệt được sự khác nhau giữa DROP, TRUNCATE và DELETE (về cấu trúc và Rollback).
- [ ] Phân biệt chính xác kết quả của RANK() (1,2,2,4), DENSE_RANK() (1,2,2,3) và ROW_NUMBER() (1,2,3,4).
- [ ] Nêu được sự khác nhau giữa hàm phân cấp ROLLUP và hàm đa chiều CUBE.
- [ ] Nhớ tên hai hàm thống kê: STDDEV (độ lệch chuẩn) và VARIANCE (phương sai).
