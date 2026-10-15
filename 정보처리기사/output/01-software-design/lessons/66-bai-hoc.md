# 5. Fan-In / Fan-Out (팬인 / 팬아웃)

## 학습 목표 (Mục tiêu)
- Định nghĩa chính xác hai chỉ số cấu trúc kiến trúc mô-đun: Fan-In (Số luồng gọi vào) và Fan-Out (Số luồng gọi ra).
- Hiểu rõ nguyên tắc thiết kế tối ưu hệ thống phần mềm: Fan-In nên cao (tăng khả năng tái sử dụng) và Fan-Out nên thấp (giảm độ phức tạp phụ thuộc).
- Thành thạo kỹ năng đọc biểu đồ cấu trúc (Structure Chart) để tính toán chính xác Fan-In, Fan-Out, Depth (Độ sâu) và Width (Độ rộng) trong các bài thi trắc nghiệm.

## 핵심 키워드 (Từ khóa)
- 팬인 (Fan-In)
- 팬아웃 (Fan-Out)
- 구조 차트 (Structure Chart)
- 재사용성 (Reusability)
- 단일 장애점 (Single Point of Failure - SPOF)
- 시스템 복잡도 (System Complexity)
- 깊이 (Depth) & 너비 (Width)

## 선행·연결 개념 (Kiến thức liên kết)
- [65-bai-hoc.md](65-bai-hoc.md): 응집도 (Cohesion) - Nội lực tập trung của từng mô-đun.
- [67-bai-hoc.md](67-bai-hoc.md): N-S 차트 (Nassi-Schneiderman Chart) - Biểu diễn logic hộp không mũi tên.
- [32-bai-hoc.md](32-bai-hoc.md): Nguyên tắc thiết kế cấu trúc mô-đun hiệu quả (Effective Modular Design).

## 읽는 방법 (Cách đọc)
- Phân biệt bằng chiều mũi tên trên sơ đồ cây phân cấp (Structure Chart):
  - Mũi tên đâm **VÀO** mô-đun $\rightarrow$ **Fan-In** (Bao nhiêu đứa phụ thuộc vào tôi).
  - Mũi tên đâm **RA** khỏi mô-đun $\rightarrow$ **Fan-Out** (Tôi chỉ huy bao nhiêu đứa bên dưới).
- Ghi nhớ câu thần chú thiết kế: "Fan-In cao chứng tỏ hữu dụng, Fan-Out thấp chứng tỏ tinh gọn".

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Định nghĩa chi tiết hai chỉ số:**

| Tiêu chí so sánh | Fan-In (팬인 - Luồng vào) | Fan-Out (팬아웃 - Luồng ra) |
| :--- | :--- | :--- |
| **Bản chất** | Số lượng mô-đun cấp trên gọi đến mô-đun hiện tại (나를 호출하는 상위 모듈의 수) | Số lượng mô-đun cấp dưới mà mô-đun hiện tại trực tiếp gọi (내가 호출하는 하위 모듈의 수) |
| **Chiều trên sơ đồ** | Số mũi tên trỏ **VÀO** nút mô-đun đó | Số mũi tên trỏ **RA** từ nút mô-đun đó xuống dưới |
| **Kỳ vọng thiết kế** | **Nên CAO (높게 설계)** | **Nên THẤP (낮게 설계)** |
| **Ý nghĩa tích cực** | Thể hiện tính tái sử dụng cao (재사용성 우수), mô-đun là tiện ích chung được dùng ở nhiều nơi | Cấu trúc hệ thống đơn giản, ít phụ thuộc chéo, dễ bảo trì và kiểm thử |
| **Rủi ro khi quá cao** | Nếu mô-đun này bị lỗi hoặc crash, toàn bộ các mô-đun gọi nó đều bị ảnh hưởng (Single Point of Failure - 단일 장애점) | Mô-đun bị ôm đồm quá nhiều trách nhiệm, logic điều khiển phức tạp, khó kiểm soát luồng dữ liệu |

- **Quy tắc tính toán trên Structure Chart (Cấu trúc phân cấp mô-đun):**
  - **Mô-đun gốc (Root Module):** Luôn có $\text{Fan-In} = 0$ (vì không có ai đứng trên để gọi nó).
  - **Mô-đun lá (Leaf Module):** Luôn có $\text{Fan-Out} = 0$ (vì không gọi thêm mô-đun con nào bên dưới).
  - **Độ sâu (Depth - 깊이):** Số tầng cấp bậc từ đỉnh xuống đáy của cây cấu trúc.
  - **Độ rộng (Width - 너비):** Số lượng mô-đun tối đa nằm trên cùng một tầng cấp bậc.

```
       [A]           <-- Fan-In(A) = 0, Fan-Out(A) = 2 (Gọi B, C)
      /   \
    [B]   [C]        <-- Fan-In(B) = 1, Fan-Out(B) = 2 (Gọi D, E)
   /   \ /           <-- Fan-In(C) = 1, Fan-Out(C) = 1 (Gọi D)
 [D]   [E]           <-- Fan-In(D) = 2 (B và C cùng gọi D), Fan-Out(D) = 0
```
- Ở ví dụ trên:
  - Nút `D` có Fan-In = 2 (Được cả `B` và `C` gọi) $\rightarrow$ Thể hiện tính tái sử dụng.
  - Nút `D` có Fan-Out = 0 $\rightarrow$ Là mô-đun lá (Leaf).

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Chiến lược tối ưu kiến trúc mô-đun thực tế:**
  - Nếu một mô-đun có **Fan-Out quá cao** (ví dụ gọi cùng lúc 10-15 hàm con):
    - Cần áp dụng kỹ thuật tái cấu trúc (Refactoring): Tách nhỏ mô-đun hoặc tạo thêm một tầng trung gian (Intermediate Layer) để phân cấp quản lý.
  - Nếu một mô-đun có **Fan-In rất cao** (ví dụ thư viện Logging, DB Connection, Utility Format):
    - Cần viết Unit Test bao phủ 100% mã nguồn (Code Coverage cao).
    - Cần quản lý đồng bộ và kiểm soát tương tranh chặt chẽ (Thread-safety) để tránh hiện tượng thắt cổ chai hiệu năng hoặc sự cố dây chuyền.

### 복습 체크리스트
- [ ] Phân biệt rõ Fan-In (Mô-đun khác gọi vào tôi) và Fan-Out (Tôi gọi mô-đun khác).
- [ ] Nhớ mục tiêu thiết kế tối ưu: Fan-In cao (tái sử dụng tốt), Fan-Out thấp (giảm phức tạp).
- [ ] Tính chính xác Fan-In và Fan-Out của một nút bất kỳ khi nhìn vào Structure Chart.
- [ ] Nhận diện nguy cơ Single Point of Failure khi Fan-In của một mô-đun quá cao.
