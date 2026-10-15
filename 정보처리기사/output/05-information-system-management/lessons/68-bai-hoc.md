# 소프트웨어 재사용 및 재공학 활동 (Hoạt động Tái sử dụng & Tái kỹ nghệ Phần mềm)

## 학습 목표 (Mục tiêu)
- Phân biệt chi tiết hai kỹ thuật tái sử dụng phần mềm: Tiếp cận dựa trên tổng hợp (합성 중심 - Composition-based) và Tiếp cận dựa trên sinh mã (생성 중심 - Generation-based).
- Nắm vững 4 hoạt động chính theo quy trình chuẩn của Tái kỹ nghệ phần mềm: Phân tích (분석), Tái cấu trúc (재구성), Kỹ nghệ ngược (역공학), và Di chuyển nền tảng (이식).
- Hiểu rõ vai trò của Kỹ nghệ ngược (Reverse Engineering) trong việc phục hồi tài liệu thiết kế bị thất lạc của các hệ thống cũ.

## 핵심 키워드 (Từ khóa)
- **합성 중심 (Composition-Based)**: Lắp ráp các khối phần mềm (Software blocks) như linh kiện điện tử.
- **생성 중심 (Generation-Based)**: Tự động sinh mã nguồn từ bản đặc tả trừu tượng (Pattern/Specification).
- **재공학 4대 활동 (4 Activities)**: 분석 (Analysis) $\rightarrow$ 재구성 (Restructuring) $\rightarrow$ 역공학 (Reverse Engineering) $\rightarrow$ 이식 (Migration).
- **역공학 (Reverse Engineering)**: Đi ngược từ mã nguồn hoặc tệp thực thi để truy xuất lại sơ đồ thiết kế kiến trúc.

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [67-bai-hoc.md](67-bai-hoc.md) (Tổng quan phương pháp luận và tái sử dụng phần mềm).
- Liên kết với [37-bai-hoc.md](37-bai-hoc.md) (Chi tiết kỹ thuật tái kỹ nghệ phần mềm).
- Liên kết với [69-bai-hoc.md](69-bai-hoc.md) (Công cụ CASE tự động hóa quy trình).

## 읽는 방법 (Cách đọc)
- Đi thi nhớ chuẩn hai cặp định nghĩa:
  - Lắp ráp khối/linh kiện $\rightarrow$ **합성 중심 (Composition-based)**.
  - Sinh code từ bản vẽ trừu tượng $\rightarrow$ **생성 중심 (Generation-based)**.
  - Thứ tự 4 bước Reengineering: **분-재-역-이** (Phân tích $\rightarrow$ Tái cấu trúc $\rightarrow$ Ngược $\rightarrow$ Di chuyển).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Hai phương pháp Tái sử dụng phần mềm (Software Reuse)
| Phương pháp (KR / EN) | Cơ chế thực hiện | Cách thức triển khai | Ví dụ điển hình |
| :--- | :--- | :--- | :--- |
| **합성 중심 / (Composition-Based)** | **Lắp ráp linh kiện (블록 구성)** | Tạo ra các khối phần mềm hoặc thành phần (Components) độc lập, sau đó ghép nối chúng lại để tạo thành ứng dụng hoàn chỉnh | Ghép module đăng nhập OAuth, module thanh toán Stripe vào website mới |
| **생성 중심 / (Generation-Based)** | **Sinh mã từ đặc tả (패턴 구성)** | Mô tả chức năng và cấu trúc hệ thống dưới dạng đặc tả trừu tượng, sau đó công cụ tự động biên dịch và sinh ra mã nguồn | Công cụ thiết kế giao diện tự động sinh mã HTML/CSS, ORM sinh câu lệnh SQL từ cấu trúc Entity |

#### 2. Bốn hoạt động chính của Tái kỹ nghệ phần mềm (Software Reengineering)
- **Mục tiêu**: Cải thiện tính bảo trì, khả năng mở rộng và độ tin cậy của phần mềm cũ mà không thay đổi các chức năng cốt lõi ban đầu.
- **Quy trình 4 hoạt động liên tiếp**:
  1. **분석 (Analysis - Phân tích)**: Rà soát toàn bộ mã nguồn và tài liệu hiện tại, phân tích mức độ phức tạp và chọn lọc các module cần được tái công nghệ.
  2. **재구성 (Restructuring - Tái cấu trúc)**: Tổ chức lại cấu trúc mã nguồn (Refactoring), chuẩn hóa tên biến, tối ưu hóa các khối lệnh lồng nhau, loại bỏ mã thừa (Dead Code) để nâng cao chất lượng nội tại.
  3. **역공학 (Reverse Engineering - Kỹ nghệ ngược)**: Phân tích mã nguồn hoặc tệp nhị phân có sẵn để phục hồi lại các bản thiết kế kiến trúc bị thất lạc (sơ đồ tuần tự, sơ đồ lớp UML, sơ đồ luồng dữ liệu DFD, mô hình dữ liệu ERD).
  4. **이식 (Migration - Di chuyển)**: Chuyển đổi toàn bộ hệ thống phần mềm đã được tái cấu trúc sang môi trường phần cứng mới, hệ điều hành mới hoặc hệ quản trị cơ sở dữ liệu hiện đại mới.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Sơ đồ mối quan hệ giữa Forward Engineering và Reverse Engineering
```
                [Yêu cầu nghiệp vụ (Requirements)]
                        │            ▲
      Forward           ▼            │  Reverse
    Engineering   [Thiết kế (Design)]│ Engineering
 (Kỹ nghệ thuận)        │            │ (Kỹ nghệ ngược)
                        ▼            │
                 [Mã nguồn (Source Code)]
                        │            ▲
                        ▼            │
                [Tệp thực thi (Binary / Executable)]
```

#### 2. Lợi ích định lượng của Tái kỹ nghệ so với Viết mới từ đầu
- Phát triển mới từ đầu (Scratch Development): Chi phí rất cao, rủi ro không hiểu hết nghiệp vụ ngầm (Implicit Business Rules) đã tích lũy nhiều năm trong hệ thống cũ.
- Tái kỹ nghệ (Reengineering): Giữ lại được 100% các logic nghiệp vụ đã chạy ổn định, giảm thiểu rủi ro thất bại dự án và tiết kiệm tới 60% tổng chi phí triển khai.

---

### 복습 체크리스트
- [ ] Phương pháp tái sử dụng 합성 중심 khác gì so với phương pháp 생성 중심?
- [ ] Bốn giai đoạn của quá trình Tái kỹ nghệ phần mềm diễn ra theo trình tự nào?
- [ ] Hoạt động Kỹ nghệ ngược (Reverse Engineering) hướng tới việc khôi phục tài sản nào của dự án?
- [ ] Hoạt động 이식 (Migration) trong tái kỹ nghệ giải quyết bài toán gì của hệ thống phần mềm?
