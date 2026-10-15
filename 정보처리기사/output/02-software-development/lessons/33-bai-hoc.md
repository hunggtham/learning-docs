# 093 & 093-1 & 093-2: 단위 모듈 및 명세서 (Unit Module & Specifications)

## 학습 목표 (Mục tiêu)
- Định nghĩa Bản đặc tả chức năng đơn vị (단위 기능 명세서 - Unit Function Specification) và vai trò làm cầu nối giữa bản vẽ thiết kế kiến trúc và giai đoạn lập trình mã nguồn.
- Nằm lòng 3 nguyên tắc nền tảng khi biên soạn bản đặc tả chức năng: Trừu tượng hóa (추상화 - Abstraction), Cấu trúc hóa (구조화 - Structuring) và Che giấu thông tin (정보 은닉 - Information Hiding).
- Phân biệt hai thành phần kỹ thuật cốt lõi trong triển khai mô-đun: Triển khai luồng vào/ra (입·출력 구현 - I/O Implementation) và Triển khai thuật toán xử lý nội tại (알고리즘 구현 - Algorithm Implementation).

## 핵심 키워드 (Từ khóa)
- 단위 모듈 (Unit Module)
- 단위 기능 명세서 (Unit Function Specification)
- 추상화 (Abstraction / 간결화)
- 구조화 (Structuring / 계층적 분해)
- 정보 은닉 (Information Hiding / 내부 캡슐화)
- 입·출력 기능 구현 (I/O Implementation)
- 알고리즘 구현 (Algorithm Implementation)

## 선행·연결 개념 (Kiến thức liên kết)
- [31-bai-hoc.md](31-bai-hoc.md): Khái niệm 단위 모듈 (Unit Module) và các kênh IPC.
- [32-bai-hoc.md](32-bai-hoc.md): Trình tự 4 bước triển khai mô-đun phần mềm.
- [35-bai-hoc.md](35-bai-hoc.md): Kiểm thử đơn vị (Unit Test) dựa trên bản đặc tả chức năng.

## 읽는 방법 (Cách đọc)
- Học thuộc 3 trụ cột của bản đặc tả chức năng: **Trừu tượng hóa - Cấu trúc hóa - Che giấu thông tin** (추상화, 구조화, 정보 은닉).
- Nhớ thứ tự logic khi code mô-đun: Phải xác định rõ ràng Đầu vào (Input) và Đầu ra (Output) trước, sau đó mới tiến hành viết thuật toán xử lý logic bên trong (Process).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Định nghĩa Bản đặc tả chức năng đơn vị (단위 기능 명세서):**
  - Là tài liệu kỹ thuật mô tả chi tiết yêu cầu xử lý logic, dữ liệu đầu vào, dữ liệu đầu ra và các ràng buộc nghiệp vụ của một mô-đun đơn vị cụ thể, làm căn cứ trực tiếp để lập trình viên viết code và kiểm thử viên thiết kế Test Case.
- **3 nguyên tắc viết bản đặc tả chức năng chuẩn mực:**

| Nguyên tắc (Hàn / Anh) | Định nghĩa kỹ thuật | Mục đích thiết kế (Từ khóa đề thi) |
| :--- | :--- | :--- |
| **Trừu tượng hóa / 추상화 (Abstraction)** | Lược bỏ các chi tiết kỹ thuật phức tạp không cần thiết ở mức cao, chỉ giữ lại các đặc tính cốt lõi của chức năng | Làm cho hệ thống trở nên **đơn giản, dễ hiểu và dễ tiếp cận (간결성, 단순화)** |
| **Cấu trúc hóa / 구조화 (Structuring)** | Phân chia hệ thống lớn thành các phân hệ nhỏ hơn theo cấu trúc thứ bậc hình cây (Hierarchical Top-Down) | Giúp việc quản lý, phân công và kiểm soát luồng điều khiển trở nên **rõ ràng, có thứ bậc (계층적 구성)** |
| **Che giấu thông tin / 정보 은닉 (Information Hiding)** | Đóng gói biến dữ liệu và chi tiết giải thuật bên trong nội bộ mô-đun, chỉ công khai các giao diện giao tiếp cần thiết | **Ngăn chặn các mô-đun khác can thiệp sửa đổi trái phép**, giảm thiểu tối đa độ phụ thuộc (Loose Coupling) |

- **Hai thành phần triển khai mô-đun thực tế:**
  1. **입·출력 기능 구현 (Triển khai luồng Vào / Ra):**
     - Xác định kiểu dữ liệu, định dạng, độ dài và các kiểm tra hợp lệ (Validation) của tham số đầu vào.
     - Định nghĩa cấu trúc kết quả trả về (Return Value) hoặc thông báo mã lỗi (Exception Code).
     - Thiết lập kết nối giao diện đồ họa (GUI), dòng lệnh (CLI) hoặc giao tiếp qua API.
  2. **알고리즘 구현 (Triển khai thuật toán xử lý):**
     - Hiện thực hóa các bước tính toán, xử lý nghiệp vụ, vòng lặp và câu lệnh rẽ nhánh để biến đổi dữ liệu đầu vào thành kết quả đầu ra theo đúng yêu cầu thiết kế.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Mối liên hệ giữa Information Hiding và tính độc lập mô-đun:**
  - David Parnas (1972) là người đầu tiên đề xuất nguyên lý **Information Hiding**: Mỗi mô-đun cần phải "giấu kín một bí mật thiết kế" bên trong nó (ví dụ: cấu trúc bảng DB hoặc thuật toán mã hóa cụ thể).
  - Khi yêu cầu nghiệp vụ thay đổi (ví dụ đổi thuật toán mã hóa từ MD5 sang SHA-256), lập trình viên chỉ cần sửa bên trong mô-đun đó mà không làm ảnh hưởng đến bất kỳ dòng code nào của các mô-đun khác trong toàn bộ hệ thống.

### 복습 체크리스트
- [ ] Định nghĩa vai trò của bản đặc tả chức năng đơn vị làm căn cứ lập trình và kiểm thử.
- [ ] Nhớ 3 nguyên tắc biên soạn: 추상화 (Abstraction), 구조화 (Structuring), 정보 은닉 (Information Hiding).
- [ ] Giải thích được tại sao Information Hiding giúp giảm độ kết hợp giữa các mô-đun.
- [ ] Phân biệt rõ nhiệm vụ của Triển khai I/O (Giao tiếp) và Triển khai Thuật toán (Xử lý).
