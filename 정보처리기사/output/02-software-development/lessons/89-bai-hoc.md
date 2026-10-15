# 핵심 119 & 120: 병렬 컴퓨터 분류 및 병렬처리기법 (Flynn's Taxonomy & Parallel Processing)

## 학습 목표 (Mục tiêu)
- Nắm vững phân loại kiến trúc máy tính song song theo thang phân loại Flynn (플린의 분류법 - Flynn's Taxonomy) dựa trên số lượng luồng lệnh (Instruction Stream) và luồng dữ liệu (Data Stream): SISD, SIMD, MISD, và MIMD.
- Hiểu rõ sự khác biệt giữa hai kiến trúc đa xử lý MIMD: Ghép nối chặt (Tightly Coupled / Multiprocessor dùng chung bộ nhớ) và Ghép nối lỏng (Loosely Coupled / Distributed System qua mạng).
- Nắm vững 4 kỹ thuật xử lý song song kinh điển: Xử lý đường ống (파이프라인 - Pipelining), Bộ xử lý véc-tơ (Vector Processor), Bộ xử lý mảng (배열 프로세서 - Array Processor), và Máy tính luồng dữ liệu (데이터 흐름 컴퓨터 - Data Flow Computer).

## 핵심 키워드 (Từ khóa)
- 플린의 분류 (Flynn's Taxonomy)
- SISD (Single Instruction, Single Data / 폰 노이만 구조)
- SIMD (Single Instruction, Multi Data / 배열 프로세서, GPU)
- MISD (Multi Instruction, Single Data / 이론상 존재, 비실용적)
- MIMD (Multi Instruction, Multi Data / 멀티코어, 분산 시스템)
- 파이프라인 (Pipelining / IF, ID, OF, EX 단계 중첩)
- 데이터 흐름 컴퓨터 (Data Flow Computer / 비 폰 노이만, PC 없음)

## 선행·연결 개념 (Kiến thức liên kết)
- [88-bai-hoc.md](88-bai-hoc.md): Bộ nhớ ảo (Virtual Memory) và hiện tượng lỗi trang.
- [90-bai-hoc.md](90-bai-hoc.md): Tổng quan cấu trúc dữ liệu tuyến tính và phi tuyến tính.
- [정보처리기사/output/04-programming-language/lessons/04-bai-hoc.md](../../04-programming-language/lessons/04-bai-hoc.md): Quản lý luồng (Threads) và tiến trình (Processes) của hệ điều hành.

## 읽는 방법 (Cách đọc)
- Học theo bảng 4 góc vuông của Flynn:
  - **SISD:** 1 Lệnh $\times$ 1 Dữ liệu $\rightarrow$ Máy tính truyền thống đơn nhân Von Neumann.
  - **SIMD:** 1 Lệnh $\times$ Nhiều Dữ liệu $\rightarrow$ Áp dụng cùng 1 phép cộng cho cả mảng 1000 phần tử (Bộ xử lý đồ họa GPU, Array Processor).
  - **MISD:** Nhiều Lệnh $\times$ 1 Dữ liệu $\rightarrow$ Rất hiếm và phi thực tế (chỉ dùng trong hệ thống siêu dự phòng chuyên biệt).
  - **MIMD:** Nhiều Lệnh $\times$ Nhiều Dữ liệu $\rightarrow$ Máy tính đa nhân hiện đại, các cụm máy chủ điện toán đám mây.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng 4 loại kiến trúc máy tính theo phân loại của Flynn:**

| Ký hiệu | Luồng Lệnh (Instruction) | Luồng Dữ liệu (Data) | Đặc điểm kiến trúc | Ví dụ tiêu biểu |
| :--- | :--- | :--- | :--- | :--- |
| **SISD** | **Single (Đơn)** | **Single (Đơn)** | Kiến trúc Von Neumann thuần túy; thực thi tuần tự từng lệnh một | PC đơn nhân truyền thống |
| **SIMD** | **Single (Đơn)** | **Multiple (Đa)** | Một bộ điều khiển đơn phát 1 lệnh duy nhất cho nhiều phần tử xử lý (PE) chạy đồng bộ | **배열 프로세서 (Array Processor)**, Card đồ họa **GPU** |
| **MISD** | **Multiple (Đa)** | **Single (Đơn)** | Nhiều lệnh khác nhau cùng tác động lên duy nhất 1 luồng dữ liệu; ít ứng dụng thực tế | Hệ thống phân tích an toàn dự phòng hàng không |
| **MIMD** | **Multiple (Đa)** | **Multiple (Đa)** | Nhiều bộ vi xử lý thực thi độc lập các tập lệnh khác nhau trên các luồng dữ liệu riêng biệt | Máy tính đa nhân (Multi-core), Hệ phân tán (Cluster) |

- **Bảng so sánh 4 kỹ thuật xử lý song song:**

| Kỹ thuật | Cơ chế hoạt động cốt lõi | Đặc điểm nổi bật chuẩn thi |
| :--- | :--- | :--- |
| **파이프라인 (Pipelining)** | Chia chu trình lệnh thành nhiều giai đoạn nhỏ (**Fetch $\rightarrow$ Decode $\rightarrow$ Operand $\rightarrow$ Execute**); cho phép các lệnh kế tiếp nhau chạy gối đầu như dây chuyền sản xuất | Tăng thông lượng lệnh (Throughput) mà không cần tăng thêm số lượng ALU |
| **배열 프로세서 (Array Processor)** | Một khối điều khiển trung tâm phân phối lệnh cho hàng loạt bộ ALU (Processing Elements) làm việc song song theo không gian | Kiến trúc tiêu biểu của hệ thống **SIMD** |
| **벡터 프로세서 (Vector Processor)** | Tối ưu hóa cho các phép tính ma trận và mảng dữ liệu khoa học bằng các đường ống xử lý véc-tơ chuyên dụng | Thường ứng dụng trong các siêu máy tính dự báo thời tiết |
| **데이터 흐름 컴퓨터 (Data Flow)** | Ngược hoàn toàn với kiến trúc Von Neumann (điều khiển theo luồng lệnh): **Lệnh tự động được kích hoạt ngay khi có đủ dữ liệu đầu vào** | **Không dùng thanh ghi đếm chương trình (Program Counter - PC)** |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Hai hình thức ghép nối trong hệ thống MIMD:**
  - **Tightly Coupled (Ghép nối chặt - Multiprocessor):** Các CPU chia sẻ chung một không gian bộ nhớ chính (Shared Memory) và dùng chung một hệ điều hành duy nhất; liên lạc qua bus tốc độ cao.
  - **Loosely Coupled (Ghép nối lỏng - Multicomputer / Distributed):** Mỗi máy có CPU và bộ nhớ riêng biệt hoàn toàn (Independent Memory); liên lạc với nhau thông qua mạng truyền thông (Message Passing).

### 복습 체크리스트
- [ ] Phân loại chính xác 4 mô hình của Flynn: SISD, SIMD, MISD, MIMD.
- [ ] Nhớ Array Processor và GPU thuộc mô hình SIMD.
- [ ] Nhớ 4 bước của Pipelining: Instruction Fetch, Decode, Operand Fetch, Execute.
- [ ] Nhớ đặc trưng của Data Flow Computer: Không dùng Program Counter (PC), cứ đủ dữ liệu là chạy.
