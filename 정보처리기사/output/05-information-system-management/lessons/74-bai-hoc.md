# 소프트웨어 생명주기 모델 (Các Mô hình Vòng đời Phát triển Phần mềm - SDLC)

## 학습 목표 (Mục tiêu)
- Nắm vững đặc trưng kiến trúc, ưu nhược điểm của 4 mô hình vòng đời phát triển phần mềm kinh điển: Thác nước (폭포수 모델 - Waterfall), Mẫu thử (프로토타입 모델 - Prototyping), Xoắn ốc (나선형 모델 - Spiral), và Mô hình chữ V (V 모델).
- Phân tích 4 hoạt động lặp tuần tự của mô hình xoắn ốc Spiral của Barry Boehm và vai trò của Phân tích rủi ro (위험 분석).
- Làm chủ mối quan hệ ánh xạ đối xứng giữa các pha thiết kế và các cấp độ kiểm thử trong mô hình V-Model (Unit Test, Integration Test, System Test, Acceptance Test).

## 핵심 키워드 (Từ khóa)
- **폭포수 모델 (Waterfall)**: Tuyến tính tuần tự, bắt buộc hoàn thành tài liệu từng pha, khó thay đổi yêu cầu.
- **프로토타입 모델 (Prototyping)**: Tạo bản mẫu thử nghiệm rút gọn để làm rõ các yêu cầu chưa rõ ràng từ khách hàng.
- **나선형 모델 (Spiral - Boehm)**: 4 bước (목표 설정 $\rightarrow$ 위험 분석 $\rightarrow$ 개발/검증 $\rightarrow$ 고객 평가/계획), dự án lớn, giảm thiểu rủi ro.
- **V 모델 (V-Model)**: Ánh xạ 1:1 giữa giai đoạn phát triển và giai đoạn kiểm thử, tăng cường thẩm định (Verification & Validation).

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [01-bai-hoc.md](01-bai-hoc.md) (Phương pháp luận phát triển phần mềm và SDLC).
- Liên kết với [67-bai-hoc.md](67-bai-hoc.md) (Tổng quan phương pháp luận Môn 5).
- Liên kết với [01-software-design/03-bai-hoc.md](../../01-software-design/lessons/03-bai-hoc.md) (SDLC models chi tiết).

## 읽는 방법 (Cách đọc)
- Nhận diện nhanh các từ khóa trong đề thi trắc nghiệm:
  - Cứ thấy từ khóa "위험 분석 (Phân tích rủi ro)" $\rightarrow$ Chọn ngay **나선형 모델 (Spiral Model)**.
  - "Xây dựng 시제품 (sản phẩm mẫu thử) cho khách hàng xem trước" $\rightarrow$ Chọn **프로토타입 모델 (Prototyping Model)**.
  - "Mô hình cổ điển nhất, làm theo từng bước tuần tự có tài liệu phê duyệt" $\rightarrow$ Chọn **폭포수 모델 (Waterfall Model)**.
  - "Ánh xạ tương ứng giữa từng bước thiết kế với bước kiểm thử" $\rightarrow$ Chọn **V 모델 (V-Model)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng so sánh 4 Mô hình SDLC kinh điển
| Mô hình (KR / EN) | Đặc trưng tiến trình | Ưu điểm cốt lõi | Nhược điểm lớn nhất | Trường hợp áp dụng phù hợp |
| :--- | :--- | :--- | :--- | :--- |
| **폭포수 모델 / (Waterfall Model)** | Tuyến tính tuần tự nghiêm ngặt (Pha sau chỉ bắt đầu khi pha trước đã hoàn tất có tài liệu phê duyệt) | Dễ quản lý tiến độ, sản phẩm tài liệu bàn giao rõ ràng ở từng bước | Rất khó điều chỉnh khi có sự thay đổi yêu cầu; phát hiện lỗi muộn ở khâu cuối | Dự án có yêu cầu rõ ràng, ổn định và ít thay đổi (ví dụ: phần mềm vũ trụ, y tế) |
| **프로토타입 모델 / (Prototyping Model)** | Nhanh chóng tạo ra bản mẫu thử thu nhỏ (Prototype) cho người dùng trải nghiệm | Làm rõ các yêu cầu mơ hồ, giảm thiểu bất đồng giao tiếp giữa khách hàng và lập trình viên | Bản mẫu dễ bị lầm tưởng là sản phẩm hoàn thiện; chi phí xây dựng bản mẫu bỏ đi | Dự án có giao diện người dùng phức tạp hoặc khách hàng chưa hình dung rõ yêu cầu |
| **나선형 모델 / (Spiral Model)** | Lặp đi lặp lại nhiều vòng xoắn ốc tăng dần, tích hợp bước **Phân tích rủi ro** chuyên sâu | Quản lý rủi ro xuất sắc, giảm thiểu tối đa nguy cơ thất bại trong các dự án quy mô lớn | Chi phí cao, phụ thuộc nhiều vào năng lực của chuyên gia đánh giá rủi ro | Các dự án phần mềm quy mô khổng lồ, công nghệ hoàn toàn mới và tính rủi ro cao |
| **V 모델 / (V-Model)** | Cấu trúc hình chữ V, ghép đôi từng bước phát triển bên trái với bước kiểm thử tương ứng bên phải | Tăng cường tính thẩm định chất lượng (Verification & Validation) ở mọi cấp độ | Vẫn giữ bản chất tuyến tính như Waterfall, khó thích ứng linh hoạt với thay đổi | Dự án đòi hỏi độ tin cậy và an toàn cực cao (Hàng không, Hệ thống phanh ô tô tự động) |

#### 2. Bốn giai đoạn lặp của Mô hình Xoắn ốc (Spiral Model)
Do Barry Boehm đề xuất, mỗi chu kỳ xoắn ốc gồm 4 hoạt động liên tiếp:
1. **목표 설정 (Xác định mục tiêu)**: Xác định mục tiêu cụ thể của chu kỳ, các phương án kỹ thuật thay thế và ràng buộc ngân sách, thời gian.
2. **위험 분석 (Phân tích rủi ro)**: Nhận diện, đánh giá và đề xuất các giải pháp kỹ thuật để triệt tiêu các rủi ro tiềm ẩn (đây là đặc trưng phân biệt quan trọng nhất).
3. **개발 및 검증 (Phát triển và kiểm chứng)**: Tiến hành lập trình và kiểm thử sản phẩm cho chu kỳ hiện tại tương ứng.
4. **고객 평가 및 다음 단계 계획 (Đánh giá và lập kế hoạch)**: Khách hàng đánh giá kết quả của chu kỳ và cùng thống nhất kế hoạch cho vòng xoắn ốc tiếp theo.

#### 3. Bảng ánh xạ kiểm thử trong Mô hình V-Model
| Giai đoạn Phát triển (Bên trái chữ V) | Cấp độ Kiểm thử đối xứng (Bên phải chữ V) | Mục tiêu kiểm thử |
| :--- | :--- | :--- |
| **Yêu cầu người dùng (User Requirements)** | **Kiểm thử nghiệm thu (Acceptance Test)** | Người dùng kiểm tra phần mềm có đáp ứng đúng mục đích kinh doanh không |
| **Phân tích yêu cầu hệ thống (System Req)** | **Kiểm thử hệ thống (System Test)** | Kiểm tra toàn bộ hệ thống về hiệu năng, bảo mật, tải trọng trên môi trường thực |
| **Thiết kế kiến trúc tổng thể (Architecture)** | **Kiểm thử tích hợp (Integration Test)** | Kiểm tra các giao diện liên kết và luồng dữ liệu trao đổi giữa các module |
| **Thiết kế chi tiết module (Detailed Design)** | **Kiểm thử đơn vị (Unit Test)** | Lập trình viên kiểm tra tính đúng đắn của từng hàm, phương thức, lớp độc lập |

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Sơ đồ mô hình chữ V (V-Model Architecture)
```
[Yêu cầu người dùng] ──────────────────────────────────────────► [Kiểm thử nghiệm thu]
        │                                                               ▲
        ▼                                                               │
[Yêu cầu hệ thống] ────────────────────────────────────────► [Kiểm thử hệ thống]
        │                                                           ▲
        ▼                                                           │
[Thiết kế kiến trúc] ──────────────────────────────────► [Kiểm thử tích hợp]
        │                                                      ▲
        ▼                                                      │
[Thiết kế chi tiết] ──────────────────────────────► [Kiểm thử đơn vị]
        │                                                  ▲
        └─────────────────► [LẬP TRÌNH (CODING)] ──────────┘
```

---

### 복습 체크리스트
- [ ] Đặc trưng kỹ thuật khác biệt quan trọng nhất của mô hình 나선형 모델 (Spiral Model) là gì?
- [ ] Bốn hoạt động tuần tự lặp lại trong mỗi vòng xoắn ốc của mô hình Spiral là gì?
- [ ] Trong mô hình V-Model, giai đoạn Thiết kế kiến trúc (Architecture Design) được kiểm chứng thông qua cấp độ kiểm thử nào?
- [ ] Tại sao mô hình Waterfall lại ít được áp dụng trong các dự án phát triển phần mềm thương mại hiện đại?
