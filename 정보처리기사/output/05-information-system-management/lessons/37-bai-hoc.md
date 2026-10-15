# 2. 소프트웨어 공학 기법 (Kỹ thuật Công nghệ Phần mềm)

## 학습 목표 (Mục tiêu)
- Nắm vững lợi ích và phân loại hai phương pháp tái sử dụng phần mềm (합성 중심 vs 생성 중심).
- Hiểu rõ bản chất của tái kỹ nghệ phần mềm (Software Reengineering) và 4 hoạt động chính theo trình tự chuẩn (분석, 재구성, 역공학, 이식).
- Phân loại toàn diện các công cụ hỗ trợ công nghệ phần mềm bằng máy tính (CASE: Upper CASE, Lower CASE, Integrated CASE) và vai trò của kho lưu trữ tập trung (Central Repository).

## 핵심 키워드 (Từ khóa)
- **소프트웨어 재사용 (Software Reuse)**: 합성 중심 (Composition-based - lắp ghép module), 생성 중심 (Generation-based - sinh mã từ đặc tả).
- **소프트웨어 재공학 (Reengineering)**: 4 bước cốt lõi (분석 $\rightarrow$ 재구성 $\rightarrow$ 역공학 $\rightarrow$ 이식), cải thiện khả năng bảo trì.
- **역공학 (Reverse Engineering)**: Phân tích mã nguồn hiện tại để tìm lại tài liệu thiết kế và kiến trúc ban đầu.
- **CASE 도구**: 상위 CASE (Yêu cầu, Thiết kế), 하위 CASE (Sinh code, Kiểm thử), 통합 CASE, Repository (kho lưu trữ thông tin chung).

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [04-bai-hoc.md](04-bai-hoc.md) (소프트웨어 재사용 및 비용 산정 - Tổng quan chi phí và tái sử dụng).
- Liên kết với [01-software-design/02-bai-hoc.md](../../01-software-design/lessons/02-bai-hoc.md) (Mô hình quy trình phát triển phần mềm).
- Liên kết với [04-programming-language/67-bai-hoc.md](../../04-programming-language/lessons/67-bai-hoc.md) (Khái niệm CASE và bảo trì phần mềm).

## 읽는 방법 (Cách đọc)
- Đi thi chú ý nhận diện nhanh:
  - Lắp ráp như chip linh kiện điện tử $\rightarrow$ **합성 중심 (Composition-based)**.
  - Sinh code từ đặc tả trừu tượng $\rightarrow$ **생성 중심 (Generation-based)**.
  - 4 giai đoạn Reengineering theo thứ tự: **분석 (Analysis) $\rightarrow$ 재구성 (Restructuring) $\rightarrow$ 역공학 (Reverse Engineering) $\rightarrow$ 이식 (Migration)** (Nhớ cụm từ viết tắt: **분-재-역-이**).
  - Upper CASE hỗ trợ vẽ DFD, ERD, phân tích yêu cầu; Lower CASE hỗ trợ sinh mã nguồn và kiểm thử.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Tái sử dụng phần mềm (Software Reuse)
- **Định nghĩa**: Việc tận dụng lại các tài sản tri thức đã được kiểm chứng (mã nguồn, đặc tả thiết kế, tài liệu yêu cầu, kịch bản kiểm thử) từ các dự án trước để phát triển hệ thống mới.
- **Lợi ích**: Giảm thiểu chi phí và thời gian phát triển, tăng năng suất lập trình, nâng cao độ tin cậy và chất lượng phần mềm, chuẩn hóa tài liệu kỹ thuật.
- **Hai phương pháp tiếp cận cốt lõi**:
  - **합성 중심 (Composition-based / Block-based)**: Xây dựng các khối linh kiện phần mềm (Software Components) độc lập, sau đó lắp ghép chúng lại với nhau giống như việc gắn các chip điện tử lên bo mạch chủ.
  - **생성 중심 (Generation-based / Pattern-based)**: Mô tả chức năng phần mềm dưới dạng các bản đặc tả kỹ thuật trừu tượng cấp cao (High-level Abstract Specification), sau đó công cụ tự động hóa sẽ biên dịch và sinh ra mã nguồn chương trình hoàn chỉnh.

#### 2. Tái kỹ nghệ phần mềm (Software Reengineering)
- **Mục tiêu**: Cải tạo, nâng cấp cấu trúc và chất lượng của hệ thống phần mềm cũ (Legacy System) để cải thiện tính dễ bảo trì (Maintainability) mà không làm thay đổi các chức năng nghiệp vụ vốn có.
- **4 hoạt động chính theo quy trình chuẩn**:
  1. **분석 (Analysis)**: Rà soát, kiểm toán mã nguồn và tài liệu hiện tại nhằm đánh giá tình trạng hệ thống và xác định các thành phần cần tái công nghệ.
  2. **재구성 (Restructuring)**: Tái cơ cấu lại cấu trúc điều khiển và luồng dữ liệu của mã nguồn để nâng cao tính module, loại bỏ các đoạn mã rác (Dead code, Spagetti code) mà vẫn giữ nguyên hành vi bên ngoài.
  3. **역공학 (Reverse Engineering)**: Phân tích ngược mã nguồn hoặc tệp thực thi để phục hồi lại các tài liệu thiết kế bị thất lạc (sơ đồ lớp, luồng dữ liệu, cấu trúc thực thể ERD).
  4. **이식 (Migration)**: Chuyển đổi và tương thích hóa phần mềm sang hoạt động trên nền tảng phần cứng, hệ điều hành hoặc cơ sở dữ liệu hiện đại mới.

#### 3. Công cụ CASE (Computer-Aided Software Engineering)
- **Khái niệm**: Bộ công cụ phần mềm chuyên dụng tự động hóa các thao tác thủ công trong toàn bộ hoặc một giai đoạn cụ thể của chu trình sống phát triển phần mềm (SDLC).
- **Phân loại công cụ CASE**:
  - **상위 CASE (Upper CASE)**: Hỗ trợ các giai đoạn đầu của dự án gồm lập kế hoạch, phân tích yêu cầu nghiệp vụ và thiết kế kiến trúc hệ thống. Hỗ trợ vẽ lược đồ DFD, ERD, sơ đồ cấu trúc.
  - **하위 CASE (Lower CASE)**: Hỗ trợ các giai đoạn sau gồm tự động sinh mã nguồn (Code Generation), biên dịch, phát hiện lỗi cú pháp và chạy các kịch bản kiểm thử (Testing).
  - **통합 CASE (Integrated CASE / I-CASE)**: Kết nối toàn diện cả 상위 CASE và 하위 CASE thành một môi trường thống nhất thông qua một **Kho lưu trữ tập trung (Central Repository)**.
- **Kho lưu trữ trung tâm (Repository)**: Trái tim của hệ thống CASE, nơi lưu trữ đồng bộ tất cả các định nghĩa dữ liệu, lược đồ thiết kế, mã nguồn, lịch sử sửa đổi và tài liệu dự án để các nhà phát triển chia sẻ xuyên suốt.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Sơ đồ chu trình Reengineering và Reverse Engineering
```
        [Hệ thống phần mềm cũ (Legacy)]
                      │
                      ▼ 1. 분석 (Analysis - Đánh giá hiện trạng)
              [Lựa chọn module lỗi thời]
                      │
                      ▼ 2. 역공학 (Reverse Engineering - Trích xuất tài liệu thiết kế)
              [Tài liệu đặc tả & Lược đồ kiến trúc]
                      │
                      ▼ 3. 재구성 (Restructuring - Tối ưu mã nguồn & cấu trúc)
              [Mã nguồn chuẩn hóa, sạch sẽ]
                      │
                      ▼ 4. 이식 (Migration - Nâng cấp lên nền tảng mới)
        [Hệ thống phần mềm hiện đại mới]
```

#### 2. Bảng phân định công cụ Upper CASE vs Lower CASE
| Tiêu chí so sánh | Upper CASE (상위 CASE) | Lower CASE (하위 CASE) |
| :--- | :--- | :--- |
| **Pha SDLC phục vụ** | Lập kế hoạch, Phân tích yêu cầu, Thiết kế | Cài đặt mã nguồn, Kiểm thử, Bảo trì |
| **Đối tượng người dùng** | Quản lý dự án (PM), Kiến trúc sư hệ thống (SA), BA | Lập trình viên (Developer), Chuyên viên kiểm thử (Tester) |
| **Công cụ và Sản phẩm** | Trình vẽ sơ đồ DFD, ERD, công cụ từ điển dữ liệu (DD) | Trình sinh code tự động, Trình gỡ lỗi (Debugger), Test runner |

---

### 복습 체크리스트
- [ ] Phân biệt sự khác nhau giữa phương pháp tái sử dụng 합성 중심 và 생성 중심?
- [ ] Bốn giai đoạn tái kỹ nghệ phần mềm (분석, 재구성, 역공학, 이식) diễn ra theo trình tự nào?
- [ ] Hoạt động 역공학 (Reverse Engineering) giải quyết vấn đề gì trong các dự án phần mềm cũ?
- [ ] Vai trò cốt lõi của Repository trong hệ thống tích hợp I-CASE là gì?
