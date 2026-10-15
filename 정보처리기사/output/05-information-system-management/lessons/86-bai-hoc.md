# 318. 소프트웨어 재사용 (Software Reuse / Tái sử dụng Phần mềm)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, mục tiêu chiến lược và các lợi ích kinh tế kỹ thuật của việc tái sử dụng phần mềm (Software Reuse).
- Phân biệt bản chất của hai phương pháp tiếp cận tái sử dụng: Tiếp cận dựa trên tổng hợp / khối linh kiện (합성 중심 - Composition-based) và Tiếp cận dựa trên sinh mã / mẫu đặc tả (생성 중심 - Generation-based).
- Hiểu rõ các điều kiện kỹ thuật để một thành phần phần mềm đạt khả năng tái sử dụng cao (Độ kết dính cao, Độ ghép nối thấp, Giao diện chuẩn hóa).
- Tổng kết toàn diện mối liên hệ giữa Tái sử dụng, Phương pháp luận CBD và Quản trị vòng đời hệ thống thông tin trong chương trình thi Kỹ sư xử lý thông tin.

## 핵심 키워드 (Từ khóa)
- **소프트웨어 재사용 (Software Reuse)**: Sử dụng lại tài sản phần mềm đã được kiểm chứng (mã nguồn, thiết kế, test case).
- **합성 중심 (Composition-Based)**: Lắp ghép các khối module phần mềm độc lập (블록 구성 방법).
- **생성 중심 (Generation-Based)**: Sinh mã tự động từ mô hình đặc tả trừu tượng (패턴 구성 방법).
- **재사용성 향상 요건**: 응집도 향상 (Tăng Cohesion), 결합도 감소 (Giảm Coupling), 표준화된 인터페이스.

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [67-bai-hoc.md](67-bai-hoc.md) (Phương pháp luận phát triển phần mềm và CBD).
- Liên kết với [68-bai-hoc.md](68-bai-hoc.md) (Các hoạt động tái sử dụng và tái kỹ nghệ phần mềm).
- Liên kết với [04-programming-language/55-bai-hoc.md](../../04-programming-language/lessons/55-bai-hoc.md) (Nguyên lý thiết kế module: Cohesion và Coupling).

## 읽는 방법 (Cách đọc)
- Đi thi chú ý nhận diện nhanh:
  - "Lắp ráp các linh kiện/khối phần mềm có sẵn như các chip điện tử" $\rightarrow$ **합성 중심 (Composition-Based)**.
  - "Tự động sinh mã nguồn chương trình từ các bản đặc tả trừu tượng cấp cao" $\rightarrow$ **생성 중심 (Generation-Based)**.
  - Điều kiện để module dễ tái sử dụng: **응집도는 높이고(High Cohesion), 결합도는 낮춘다(Loose Coupling)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Khái niệm và Lợi ích Chiến lược của Tái sử dụng Phần mềm
- **Định nghĩa**: Quá trình tận dụng lại các tri thức, kinh nghiệm, mô hình thiết kế, mã nguồn hoặc các thành phần phần mềm đã được kiểm chứng chất lượng từ các dự án trước đó để xây dựng hệ thống mới.
- **Phạm vi tái sử dụng**:
  - Không chỉ giới hạn ở việc "sao chép mã nguồn" (Code reuse), mà bao gồm cả: Tái sử dụng kiến trúc hệ thống (Software Architecture), Tái sử dụng đặc tả yêu cầu, Tái sử dụng các ca kiểm thử (Test Cases), và Tái sử dụng tài liệu hướng dẫn.
- **Bảng các lợi ích vượt trội**:
  | Lợi ích kinh tế & Kỹ thuật | Mô tả chi tiết |
  | :--- | :--- |
  | **Rút ngắn thời gian phát triển** | Giảm thiểu khối lượng công việc lập trình mới từ 30% đến 50%, giúp đưa sản phẩm ra thị trường nhanh hơn |
  | **Giảm thiểu chi phí dự án** | Tiết kiệm chi phí nhân công và chi phí kiểm toán chất lượng ban đầu |
  | **Nâng cao chất lượng & Độ tin cậy** | Các module tái sử dụng đã trải qua thời gian dài vận hành thực tế nên hầu như không còn lỗi tiềm ẩn |
  | **Tăng năng suất phần mềm** | Các kỹ sư tập trung vào việc giải quyết bài toán nghiệp vụ cốt lõi thay vì viết lại các thành phần phụ trợ |
  | **Chuẩn hóa quy trình** | Thúc đẩy việc tài liệu hóa và thiết kế giao diện (Interface) theo các tiêu chuẩn chung của doanh nghiệp |

#### 2. So sánh Hai Phương pháp Tái sử dụng Phần mềm Cốt lõi
| Tiêu chí so sánh | 합성 중심 (Composition-Based) | 생성 중심 (Generation-Based) |
| :--- | :--- | :--- |
| **Tên gọi tương đương** | **블록 구성 방법 (Phương pháp ghép khối)** | **패턴 구성 방법 (Phương pháp mẫu đặc tả)** |
| **Bản chất kỹ thuật** | Tạo ra các khối linh kiện phần mềm (Software Components) độc lập, sau đó ghép nối chúng lại với nhau | Mô tả chức năng và hành vi của ứng dụng dưới dạng các bản vẽ đặc tả trừu tượng cấp cao |
| **Phương thức sinh mã** | Không tự sinh mã mới; chỉ liên kết và cấu hình các khối module đã có sẵn | Các công cụ tự động hóa biên dịch bản đặc tả và sinh ra toàn bộ mã nguồn chương trình hoàn chỉnh |
| **Mô hình tương tự trong đời thực** | Lắp ráp các khối đồ chơi Lego hoặc gắn chip điện tử lên bo mạch chủ | Bản thiết kế kiến trúc ngôi nhà đưa vào máy in 3D để in tự động |

#### 3. Các Điều kiện Kỹ thuật để Nâng cao Khả năng Tái sử dụng
- **Tối ưu hóa thiết kế Module**:
  - **응집도 (Cohesion - Độ kết dính)**: Phải ở mức **cao nhất (High)** - mỗi module chỉ tập trung giải quyết trọn vẹn một chức năng duy nhất.
  - **결합도 (Coupling - Độ ghép nối)**: Phải ở mức **thấp nhất (Loose)** - các module giao tiếp với nhau độc lập, không phụ thuộc vào trạng thái nội bộ của nhau.
- **Chuẩn hóa Giao diện (Interface Standardization)**:
  - Tách rời giao diện định nghĩa (Interface) khỏi việc cài đặt chi tiết bên trong (Implementation). Khách hàng chỉ tương tác qua hợp đồng giao diện chuẩn.
- **Tài liệu hóa hoàn chỉnh**:
  - Mỗi thành phần tái sử dụng bắt buộc phải có tài liệu mô tả rõ ràng về: Điều kiện đầu vào (Pre-conditions), Điều kiện đầu ra (Post-conditions), Các ngoại lệ có thể phát sinh, và Ví dụ sử dụng.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Sơ đồ chu trình phát triển phần mềm dựa trên tái sử dụng (CBD)
```
          [Kho lưu trữ Linh kiện Phần mềm dùng chung (Component Repository)]
                                  │
         ┌────────────────────────┴────────────────────────┐
         │ (Tìm kiếm & Đánh giá)                           │ (Lưu linh kiện mới)
         ▼                                                 ▼
[Phân tích Yêu cầu] ──► [Lựa chọn Linh kiện] ──► [Ghép nối & Cấu hình] ──► [Sản phẩm Hoàn thiện]
```

---

### 복습 체크리스트
- [ ] Việc tái sử dụng phần mềm (Software Reuse) mang lại những lợi ích cốt lõi nào cho dự án CNTT?
- [ ] Phân biệt sự khác biệt bản chất giữa phương pháp 합성 중심 và 생성 중심?
- [ ] Để một module có khả năng tái sử dụng cao trong hệ thống, độ kết dính (Cohesion) và độ ghép nối (Coupling) của nó cần đạt trạng thái như thế nào?
- [ ] Tại sao việc chuẩn hóa giao diện Interface lại là điều kiện tiên quyết cho việc tái sử dụng linh kiện phần mềm?
