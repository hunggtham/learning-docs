# 323. 수학적 산정 기법 (Mathematical Estimation Techniques / Kỹ thuật ước lượng toán học)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, nguồn gốc dữ liệu và cơ chế lượng hóa của các mô hình toán học ước tính chi phí phần mềm (**수학적 산정 기법 - Mathematical Cost Estimation Models**).
- Phân tích chi tiết ranh giới phân loại, đặc điểm nghiệp vụ và phạm vi ứng dụng của 3 chế độ phát triển trong mô hình **COCOMO** (Organic - 조직형, Semi-Detached - 반분리형, và Embedded - 내장형).
- Thấu hiểu cơ sở lý thuyết đường cong phân bố nỗ lực **Rayleigh-Norden** trong mô hình **Putnam** và quy trình đo lường điểm chức năng **Function Point (FP)** độc lập với ngôn ngữ lập trình.

## 핵심 키워드 (Từ khóa)
- 수학적 산정 기법 (Mathematical Estimation Models)
- COCOMO 모형 (Boehm - LOC 기반 상향식 산정)
- 조직형 (Organic Mode - 5만 라인 이하 `≤ 50 KDSI`)
- 반분리형 (Semi-Detached Mode - 30만 라인 이하 `> 50 ~ 300 KDSI`)
- 내장형 (Embedded Mode - 30만 라인 초과 `> 300 KDSI`)
- Putnam 모형 (Rayleigh-Norden 곡선, SLIM 소프트웨어)
- 기능 점수 (FP - Function Point, 언어 독립적 기능 크기 측정)

## 선행·연결 개념 (Kiến thức liên kết)
- [08-bai-hoc.md](08-bai-hoc.md): Đại cương các phương pháp ước tính chi phí (Top-Down vs Bottom-Up).
- [10-bai-hoc.md](10-bai-hoc.md): Các tiêu chuẩn chất lượng quy trình (ISO 12207, CMMI, SPICE).
- [06-bai-hoc.md](06-bai-hoc.md): Quản lý dự án và các công thức tính toán Man-Month.

## 읽는 방법 (Cách đọc)
- Điểm mấu chốt khi giải bài toán về 3 mô hình toán học:
  - **COCOMO:** Bắt buộc nhớ chuẩn xác con số giới hạn:
    - **조직형 (Organic):** Dưới hoặc bằng 50.000 dòng (`≤ 50 KDSI`) $\rightarrow$ Các phần mềm văn phòng, nghiệp vụ thương mại quy mô vừa và nhỏ.
    - **반분리형 (Semi-Detached):** Từ trên 50 đến 300.000 dòng (`> 50 ~ 300 KDSI`) $\rightarrow$ Phần mềm hệ thống như trình biên dịch (Compiler), hệ quản trị DBMS, tiện ích hệ điều hành.
    - **내장형 (Embedded):** Trên 300.000 dòng (`> 300 KDSI`) $\rightarrow$ Hệ thống nhúng thời gian thực siêu phức tạp (Hệ điều hành, phần mềm điều khiển tên lửa, vệ tinh, thiết bị y tế).
  - **Putnam:** Luôn đi liền với từ khóa **"Rayleigh-Norden 곡선"** và phần mềm **"SLIM"**.
  - **Function Point (FP):** Nhớ đặc điểm ưu việt nhất là **"언어 독립적" (Hoàn toàn độc lập với ngôn ngữ lập trình)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng phân loại chi tiết 3 chế độ phát triển của COCOMO (Boehm):**

| Chế độ COCOMO | Giới hạn quy mô mã nguồn | Đặc điểm đội ngũ & Môi trường phát triển | Lĩnh vực ứng dụng điển hình |
| :--- | :--- | :--- | :--- |
| **조직형 (Organic)** | **`≤ 50 KDSI`** (Dưới 50.000 dòng code) | Quy mô nhỏ, yêu cầu nghiệp vụ rõ ràng; đội ngũ lập trình viên đã có nhiều kinh nghiệm tương tự; môi trường phát triển ổn định. | Phần mềm kế toán doanh nghiệp nhỏ, quản lý bán lẻ, ứng dụng văn phòng nội bộ. |
| **반분리형 (Semi-Detached)** | **`> 50 ~ 300 KDSI`** (Từ 50.000 đến 300.000 dòng) | Quy mô trung bình, độ phức tạp trung bình; đội ngũ kết hợp giữa kỹ sư giàu kinh nghiệm và kỹ sư mới; có một phần yêu cầu kỹ thuật mới. | Trình biên dịch (Compiler), Trình điều khiển thiết bị (Device Driver), Hệ quản trị cơ sở dữ liệu (DBMS). |
| **내장형 (Embedded)** | **`> 300 KDSI`** (Trên 300.000 dòng code) | Dự án đại quy mô, yêu cầu độ tin cậy và an toàn tối cao; ràng buộc phần cứng và thời gian thực khắt khe; môi trường chưa từng có tiền lệ. | Hệ điều hành lớn, Phần mềm điều khiển vũ khí quân sự, Hàng không vũ trụ, Hệ thống điều khiển nhà máy hạt nhân. |

- **2. Mô hình vòng đời Putnam (Putnam Model):**
  - Dựa trên công trình nghiên cứu phân bố nhân lực của Peter Norden tại IBM, Larry Putnam đã mô hình hóa nỗ lực theo thời gian bằng **Đường cong Rayleigh-Norden**.
  - Đặc điểm: Lượng nhân lực ban đầu tham gia ít (giai đoạn khảo sát/thiết kế), tăng vọt lên mức đỉnh điểm ở giai đoạn mã hóa/kiểm thử, sau đó giảm dần khi chuyển sang bảo trì.
  - Công cụ phần mềm tự động hóa đại diện: **SLIM (Software Life-cycle Management)**.

- **3. Mô hình Điểm chức năng (Function Point - Albrecht):**
  - Đo lường kích thước phần mềm từ góc nhìn của **người sử dụng (User Perspective)** thông qua số lượng các chức năng logic mà hệ thống mang lại.
  - **Ưu điểm vượt trội so với LOC:**
    - Có thể ước tính sớm ngay từ giai đoạn hoàn thành tài liệu phân tích yêu cầu (khi chưa viết bất kỳ dòng code nào).
    - Không bị phụ thuộc vào sự dài dòng của ngôn ngữ (viết bằng Java hay Assembly thì một chức năng đăng nhập vẫn có cùng điểm FP).

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Công thức tính nỗ lực cơ bản của COCOMO:**
  - $\text{Nỗ lực (Man-Month)} = a \times (\text{KDSI})^b$
  - Trong đó $a$ và $b$ là các hằng số thực nghiệm được Boehm xác định cho từng chế độ:
    - Organic: $\text{MM} = 2.4 \times (\text{KDSI})^{1.05}$
    - Semi-Detached: $\text{MM} = 3.0 \times (\text{KDSI})^{1.12}$
    - Embedded: $\text{MM} = 3.6 \times (\text{KDSI})^{1.20}$
  - Hệ số mũ $b > 1$ phản ánh quy luật chi phí tăng phi tuyến tính theo quy mô dự án.

### 복습 체크리스트
- [ ] Ghi nhớ chính xác 3 ngưỡng quy mô COCOMO: Organic (`≤ 50 KDSI`), Semi-Detached (`> 50 ~ 300 KDSI`), Embedded (`> 300 KDSI`).
- [ ] Nhớ hệ điều hành và hệ thống tên lửa vũ trụ thuộc chế độ **Embedded**.
- [ ] Ghi nhớ mô hình Putnam gắn liền với đường cong Rayleigh-Norden và công cụ SLIM.
- [ ] Nắm được ưu điểm lớn nhất của Function Point: Ước lượng sớm và độc lập với ngôn ngữ lập trình.
