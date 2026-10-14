# 핵심 119 & 120: 병렬 컴퓨터 분류 및 병렬처리기법 (Flynn's Taxonomy & Parallel Processing)

## 핵심 119 & 120: 병렬 컴퓨터 분류 및 병렬처리기법 (Flynn's Taxonomy & Parallel Processing)

### 플린(Flynn)의 분류 (Phân loại Flynn)
Phần “플린(Flynn)의 분류 (Phân loại Flynn)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **SISD (Single Instruction, Single Data):** 1 Lệnh xử lý 1 Dữ liệu. (Máy tính truyền thống Von Neumann).
- **SIMD (Single Instruction, Multi Data):** 1 Lệnh xử lý Nhiều Dữ liệu. (Array Processor, xử lý đồng bộ).
- **MISD (Multi Instruction, Single Data):** Nhiều Lệnh, 1 Dữ liệu. (Không dùng trong thực tế).
- **MIMD (Multi Instruction, Multi Data):** Nhiều Lệnh xử lý Nhiều Dữ liệu. (Máy đa nhân hiện đại - Đa xử lý bất đồng bộ). Tightly Coupled (Multiprocessor), Loosely Coupled (Distributed).

### 병렬처리기법 (Kỹ thuật xử lý song song)
Phần “병렬처리기법 (Kỹ thuật xử lý song song)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **파이프라인 프로세서 (Pipeline):** Chia lệnh thành các Sub-task (như dây chuyền nhà máy). Các bước: Fetch, Decode, Operand, Execute.
- **벡터 프로세서 (Vector Processor):** Xử lý mảng dữ liệu cực nhanh (Systolic algorithm).
- **배열 프로세서 (Array Processor):** Có nhiều bộ ALU (Processing Elements), điều khiển tập trung, tính toán song song theo không gian (SIMD).
- **데이터 흐름 컴퓨터 (Data Flow Computer):** Ngược với Von Neumann (Control-flow). Lệnh không chạy theo thứ tự PC, mà cứ hễ **đủ Dữ liệu là chạy** (Không cần Program Counter).

- **Vietnamese Explanation:** SISD là làm việc một mình. SIMD là 1 ông chủ ra lệnh cho 10 người cùng làm. MIMD là 10 người tự làm 10 việc khác nhau. Data Flow là cách làm việc "không cần quản lý", ai có đủ nguyên liệu thì tự động nấu, không cần chờ sếp hô hào.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Flynn: S = Single (Đơn), M = Multi (Đa), I = Instruction (Lệnh), D = Data (Dữ liệu). Data Flow = Data dẫn dắt, Không cần PC.

---

# [과목 2] 소프트웨어 개발 (Subject 2: Software Development)
