# 279 - 280. 라이브러리 (Library)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và vai trò của thư viện phần mềm (라이브러리 - Library): tập hợp các hàm, lớp và tài nguyên được biên dịch sẵn nhằm hỗ trợ tái sử dụng mã nguồn và rút ngắn thời gian phát triển phần mềm.
- Phân biệt sâu sắc hai cơ chế liên kết thư viện: Liên kết tĩnh (정적 링킹 - Static Linking) và Liên kết động (동적 링킹 - Dynamic Linking).
- Nhớ tên các tệp tiêu đề thư viện chuẩn của ngôn ngữ C (`<stdio.h>`, `<stdlib.h>`, `<string.h>`, `<math.h>`) và phần mở rộng tệp thư viện trên hệ điều hành Windows (`.lib`, `.dll`) và Linux (`.a`, `.so`).

## 핵심 키워드 (Từ khóa)
- 라이브러리 (Library / 표준 라이브러리 vs 사용자 정의 라이브러리)
- 정적 링킹 (Static Linking / `.lib`, `.a` / 실행 파일 포함)
- 동적 링킹 (Dynamic Linking / `.dll`, `.so` / 실행 시 적재)
- 헤더 파일 (Header Files / `.h` / 선언부)
- 모듈 재사용 (Module Reuse)
- 공유 라이브러리 (Shared Library)

## 선행·연결 개념 (Kiến thức liên kết)
- [30-bai-hoc.md](30-bai-hoc.md): Thư viện chuẩn C và xử lý ngoại lệ.
- [32-bai-hoc.md](32-bai-hoc.md): Ngôn ngữ kịch bản và đặc trưng hệ điều hành UNIX.
- [정보처리기사/output/02-software-development/lessons/92-bai-hoc.md](../../02-software-development/lessons/92-bai-hoc.md): Các kỹ thuật tái sử dụng phần mềm.

## 읽는 방법 (Cách đọc)
- Phân biệt hai cơ chế liên kết thư viện:
  - **정적 라이브러리 (Static Linking - `.lib`, `.a`):** Toàn bộ mã máy của thư viện được sao chép và nhúng trực tiếp vào tệp thực thi (`.exe`) ngay trong giai đoạn build. Tệp thực thi có dung lượng lớn nhưng chạy độc lập hoàn toàn, không phụ thuộc vào hệ thống bên ngoài.
  - **동적 라이브러리 (Dynamic Linking - `.dll`, `.so`):** Mã thư viện không nhúng vào tệp thực thi mà được nạp lên RAM dùng chung khi chương trình bắt đầu chạy. Nhiều chương trình có thể cùng chia sẻ một tệp thư viện, giúp tiết kiệm dung lượng đĩa và bộ nhớ RAM.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng so sánh: 정적 링킹 (Static) vs 동적 링킹 (Dynamic):**

| Tiêu chuẩn so sánh | 정적 링킹 (Static Linking) | 동적 링킹 (Dynamic Linking / DLL) |
| :--- | :--- | :--- |
| **Thời điểm liên kết** | Giai đoạn biên dịch và đóng gói (**빌드 / 컴파일 시점**) | Giai đoạn nạp vào bộ nhớ và thực thi (**런타임 / 실행 시점**) |
| **Phần mở rộng Windows** | **`.lib`** (Static Library) | **`.dll`** (Dynamic Link Library) |
| **Phần mở rộng Linux** | **`.a`** (Archive) | **`.so`** (Shared Object) |
| **Dung lượng tệp `.exe`** | **Lớn**, do chứa toàn bộ mã của thư viện bên trong | **Nhỏ**, chỉ chứa bảng tham chiếu địa chỉ hàm |
| **Mức chiếm dụng RAM** | Mỗi tiến trình sở hữu bản sao riêng, gây lãng phí bộ nhớ | **Nhiều tiến trình chia sẻ chung** một bản nạp trên RAM |
| **Bảo trì và cập nhật** | Khi thư viện cập nhật, **bắt buộc phải biên dịch lại toàn bộ phần mềm** | Chỉ cần thay thế tệp `.dll` mới mà không cần biên dịch lại tệp `.exe` |

- **Bốn tệp tiêu đề thư viện chuẩn cơ bản trong C:**
  - `<stdio.h>`: Chứa các hàm nhập xuất cơ bản (`printf`, `scanf`, `getchar`).
  - `<stdlib.h>`: Chứa các hàm cấp phát bộ nhớ động (`malloc`, `free`) và chuyển đổi kiểu (`atoi`).
  - `<string.h>`: Chứa các hàm xử lý chuỗi ký tự (`strlen`, `strcpy`, `strcat`, `strcmp`).
  - `<math.h>`: Chứa các hàm toán học nâng cao (`sqrt`, `pow`, `abs`).

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Sự cố "DLL Hell" trong hệ điều hành Windows:**
  - Trong kiến trúc Dynamic Linking, nếu một phần mềm cài đặt đè một phiên bản DLL mới không tương thích lên thư mục hệ thống `System32`, các phần mềm cũ phụ thuộc vào phiên bản DLL trước đó có thể bị sập đồng loạt.
  - Để giải quyết vấn đề này, các hệ điều hành hiện đại áp dụng cơ chế Side-by-Side (SxS) Assembly và đóng gói Container (Docker).

### 복습 체크리스트
- [ ] Phân biệt được phần mở rộng: Static (.lib, .a) vs Dynamic (.dll, .so).
- [ ] Nhớ Static linking nhúng code vào file exe khi build, Dynamic linking nạp vào RAM khi chạy.
- [ ] Nhớ ưu điểm của DLL: Tiết kiệm RAM do chia sẻ chung và dễ nâng cấp không cần compile lại app.
- [ ] Nhớ 4 header file cơ bản của C: stdio.h, stdlib.h, string.h, math.h.
