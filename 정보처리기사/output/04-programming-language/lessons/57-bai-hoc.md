# 193 - 194. 효과적인 모듈화 설계 방안 & N-S 차트 (Effective Modular Design & Nassi-Schneiderman Chart)

## 학습 목표 (Mục tiêu)
- Nắm vững các chỉ dẫn kỹ thuật để thiết kế module hóa hiệu quả (효과적인 모듈화 설계 방안) trong các hệ thống phần mềm lớn.
- Hiểu cấu trúc chỉ số Fan-In (số module gọi đến) và Fan-Out (số module bị gọi), hướng tới cấu trúc tối ưu: **Fan-In cao (tái sử dụng cao), Fan-Out vừa phải (kiểm soát tốt)**.
- Phân biệt đặc trưng kiến trúc và ưu nhược điểm của biểu đồ N-S (Nassi-Schneiderman Chart) – biểu đồ cấu trúc hộp không mũi tên.

## 핵심 키워드 (Từ khóa)
- 효과적인 모듈화 (Effective Modularity)
- 결합도 최소화 & 응집도 최대화 (Low Coupling, High Cohesion)
- 팬인 (Fan-In / Số lượt gọi đến) & 팬아웃 (Fan-Out / Số lượt gọi đi)
- N-S 차트 (Nassi-Schneiderman / Box Diagram)
- GOTO문 부재 (No GOTO / No Arrow Flow)
- 3대 제어 구조 (순차, 선택, 반복 / Sequence, Selection, Iteration)
- 단일 진입·단일 진출 (Single Entry, Single Exit)

## 선행·연결 개념 (Kiến thức liên kết)
- [55-bai-hoc.md](55-bai-hoc.md): Thứ tự các cấp độ kết hợp (Coupling: 자스제 외공내).
- [56-bai-hoc.md](56-bai-hoc.md): Thứ tự các cấp độ gắn kết (Cohesion: 우논시절 교순기).
- [58-bai-hoc.md](58-bai-hoc.md): Lập trình có cấu trúc và tính toán độ phức tạp McCabe Cyclomatic.

## 읽는 방법 (Cách đọc)
- Trong bài thi kỹ sư CNTT:
  - Khi hỏi về **N-S Chart**, dấu hiệu nhận diện bất di bất dịch là: **"GOTO나 화살표(Arrow)를 사용하지 않는다"** (Không dùng lệnh GOTO, không dùng mũi tên luồng), thể hiện bằng các khối hộp lồng nhau (Box diagram).
  - Về Fan-in / Fan-out: Thiết kế tốt là thiết kế có **Fan-In cao** (module được tái sử dụng ở nhiều nơi) và **Fan-Out thấp/vừa phải** (module không ôm đồm điều khiển quá nhiều module con, thường không quá 3-4).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Các nguyên tắc vàng để thiết kế module hóa hiệu quả:**
  1. **Đảm bảo tính độc lập:** Luôn hướng tới kết hợp lỏng lẻo (Low Coupling) và gắn kết chặt chẽ (High Cohesion).
  2. **Quy mô module:** Tránh module quá to (khó hiểu, khó kiểm thử) hoặc quá nhỏ (bùng nổ chi phí gọi hàm).
  3. **Cấu trúc luồng chuẩn:** Một lối vào duy nhất và một lối ra duy nhất (Single Entry, Single Exit).
  4. **Quan hệ phạm vi:** Phạm vi ảnh hưởng (Scope of Effect) phải được giới hạn bên trong phạm vi kiểm soát (Scope of Control).
  5. **Tối ưu hóa Fan-In và Fan-Out:**
     - **Fan-In (팬인):** Số lượng module cấp trên gọi đến module hiện tại $\rightarrow$ **Càng cao càng tốt** (thể hiện tính tái sử dụng cao).
     - **Fan-Out (팬아웃):** Số lượng module cấp dưới mà module hiện tại gọi đi $\rightarrow$ **Nên giữ ở mức vừa phải** (thường từ 3 đến 4). Fan-Out quá lớn biểu hiện module cha đang quá phức tạp và ôm đồm.

- **2. Đặc trưng toàn diện của biểu đồ N-S (Nassi-Schneiderman Chart):**

| Tiêu chí | Đặc điểm kỹ thuật của biểu đồ N-S |
| :--- | :--- |
| **Hình thức biểu diễn** | Dạng biểu đồ hộp (Box Diagram) gồm các khối chữ nhật lồng ghép nhau. |
| **Quy tắc luồng** | **Tuyệt đối không dùng mũi tên (Arrow) và không dùng lệnh nhảy `GOTO`.** |
| **Luồng thực thi** | Luôn di chuyển tuần tự từ trên xuống dưới một cách tự nhiên. |
| **3 cấu trúc cơ bản** | Thể hiện trực quan 3 cấu trúc của lập trình có cấu trúc: **순차 (Sequence), 선택 (Selection / If-Else), 반복 (Iteration / While-For)**. |
| **Ưu điểm** | Cấu trúc phân cấp logic cực kỳ rõ ràng, dễ đọc hiểu toàn cảnh luồng thuật toán. |
| **Nhược điểm** | Rất khó vẽ thủ công và cực kỳ tốn công sức chỉnh sửa khi phát sinh thay đổi logic ở các khối bên trong. |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tính toán Fan-In và Fan-Out từ sơ đồ cây gọi (Call Tree):**
  - Giả sử hệ thống có các lệnh gọi: Module A gọi B, C, D. Module E gọi B.
  - Phân tích module B: Có 2 module gọi đến nó (A và E) $\rightarrow$ $\text{Fan-In của B} = 2$. B không gọi ai $\rightarrow$ $\text{Fan-Out của B} = 0$.
  - Phân tích module A: Không có ai gọi A $\rightarrow$ $\text{Fan-In của A} = 0$. A gọi 3 module (B, C, D) $\rightarrow$ $\text{Fan-Out của A} = 3$.

### 복습 체크리스트
- [ ] Ghi nhớ tiêu chí thiết kế tốt: Fan-In nên cao (tái sử dụng tốt), Fan-Out nên thấp/vừa phải.
- [ ] Nhớ đặc trưng nhận diện duy nhất của N-S Chart: **Không dùng mũi tên, không dùng GOTO**, vẽ dạng khối hộp.
- [ ] Kể tên 3 cấu trúc điều khiển cơ bản biểu diễn trên N-S Chart: 순차 (Tuần tự), 선택 (Rẽ nhánh), 반복 (Lặp).
- [ ] Biết cách tính Fan-In (mũi tên hướng vào) và Fan-Out (mũi tên trỏ ra) trên sơ đồ phân cấp module.
