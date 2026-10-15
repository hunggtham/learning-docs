# 1. 인증 기술 (Authentication Types / Các Công nghệ Xác thực)

## 학습 목표 (Mục tiêu)
- Phân biệt toàn diện 4 nhóm nhân tố xác thực người dùng: Tri thức (지식 기반), Sở hữu (소유 기반), Sinh trắc (생체 기반), và Hành vi/Vị trí (행위/위치 기반).
- Nắm vững nguyên tắc triển khai của Xác thực đa nhân tố (MFA - Multi-Factor Authentication).
- Làm chủ hai chỉ số sai số then chốt trong công nghệ nhận diện sinh trắc học: Tỷ lệ chấp nhận sai (FAR) và Tỷ lệ từ chối sai (FRR) cùng điểm giao thoa cân bằng (CER/EER).

## 핵심 키워드 (Từ khóa)
- **인증 4대 요소 (4 Factors)**: Something You Know (지식 - Mật khẩu, PIN), Something You Have (소유 - OTP, Smart Card), Something You Are (생체 - Vân tay, Mống mắt), Something You Do (행위 - Chữ ký, Nhịp gõ phím).
- **MFA (다중 요소 인증)**: Bắt buộc kết hợp từ 2 nhóm nhân tố khác nhau trở lên.
- **FAR (False Acceptance Rate)**: Tỷ lệ nhận diện nhầm kẻ mạo danh là người hợp lệ (đo lường độ an toàn).
- **FRR (False Rejection Rate)**: Tỷ lệ từ chối nhầm người dùng hợp lệ (đo lường độ tiện dụng).
- **CER / EER (Crossover Error Rate)**: Điểm mà tại đó $FAR = FRR$, chỉ số đánh giá chất lượng thuật toán sinh trắc học.

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [83-bai-hoc.md](83-bai-hoc.md) (Khung kiến trúc xác thực AAA và Kerberos).
- Liên kết với [85-bai-hoc.md](85-bai-hoc.md) (Chính sách kiểm soát truy cập sau khi đã xác thực).
- Liên kết với [30-bai-hoc.md](30-bai-hoc.md) (Hệ thống xác thực và phạm vi an toàn thông tin).

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh dạng câu hỏi trong đề thi:
  - "Xác thực dựa trên những gì người dùng biết trong đầu" $\rightarrow$ **지식 기반 (Knowledge)**.
  - "Xác thực dựa trên đồ vật người dùng cầm theo" $\rightarrow$ **소유 기반 (Possession)**.
  - "Xác thực dựa trên nhịp gõ phím hoặc dáng đi" $\rightarrow$ **행위 기반 (Behavior)**.
  - "Trường hợp nào được coi là MFA?" $\rightarrow$ Mật khẩu (Tri thức) + Mã OTP trên điện thoại (Sở hữu). Nếu dùng "Mật khẩu đăng nhập + Mã PIN 6 số" thì KHÔNG PHẢI MFA (vì cùng là nhóm Tri thức).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng 4 Nhóm Nhân tố Xác thực (Authentication Factors)
| Nhóm nhân tố | Bản chất kỹ thuật | Phương thức triển khai tiêu biểu | Ưu điểm & Rủi ro |
| :--- | :--- | :--- | :--- |
| **지식 기반 / (Something You Know)** | Dựa trên những thông tin bí mật được lưu trong trí nhớ người dùng | Mật khẩu (Password), mã PIN cá nhân, câu hỏi bảo mật | Dễ triển khai, chi phí thấp; Dễ bị quên, bị lộ lọt, bị tấn công dò quét (Brute-force/Dictionary) |
| **소유 기반 / (Something You Have)** | Dựa trên vật thể vật lý hoặc thiết bị mà người dùng đang nắm giữ | Thẻ thông minh (Smart Card), Khóa phần cứng FIDO2 (YubiKey), Thiết bị OTP Token, Mã OTP qua SMS | An toàn trước các cuộc tấn công từ xa thuần túy; Rủi ro bị thất lạc, mất cắp vật lý thiết bị |
| **생체 기반 / (Something You Are)** | Dựa trên đặc điểm hình thái học sinh học duy nhất của cơ thể con người | Dấu vân tay, quét mống mắt (Iris), nhận diện khuôn mặt 3D, quét tĩnh mạch mu bàn tay/ngón tay | Không thể bị quên hoặc làm mất; Chi phí phần cứng đầu đọc cao, có thể bị làm giả (Deepfake, mô hình silicone) |
| **행위/위치 기반 / (Something You Do / Where)** | Dựa trên thói quen hành vi độc động học hoặc vị trí địa lý của thiết bị | Động học gõ phím (Keystroke Dynamics), đặc trưng chữ ký tay, dáng đi (Gait), tọa độ GPS, địa chỉ IP mạng nội bộ | Hoạt động ngầm liên tục (Continuous Authentication); Độ chính xác phụ thuộc thiết bị và môi trường |

#### 2. Nguyên tắc Xác thực Đa nhân tố (MFA - Multi-Factor Authentication)
- **Định nghĩa**: Hệ thống bảo mật yêu cầu người dùng phải cung cấp thành công bằng chứng từ **ít nhất hai nhóm nhân tố độc lập khác nhau** trước khi được cấp quyền truy cập.
- **Quy tắc phân loại đúng/sai**:
  - Hợp lệ (MFA): Mật khẩu (지식) $+$ Khóa thẻ OTP (소유).
  - Hợp lệ (MFA): Vân tay (생체) $+$ Mã SMS gửi về điện thoại (소유).
  - Không hợp lệ: Mật khẩu chính $+$ Mật khẩu cấp 2 (Cùng thuộc nhóm 지식 $\rightarrow$ Vẫn chỉ là xác thực 1 nhân tố - Single Factor).

#### 3. Hai Chỉ số Sai số trong Nhận diện Sinh trắc học (Biometrics)
- **FAR (False Acceptance Rate - Tỷ lệ chấp nhận sai)**:
  - Tỷ lệ hệ thống nhận diện nhầm kẻ mạo danh (Impostor) là người dùng hợp lệ và cho phép truy cập.
  - Phản ánh **mức độ an toàn (Security level)** của hệ thống: FAR càng nhỏ thì độ an toàn càng cao.
- **FRR (False Rejection Rate - Tỷ lệ từ chối sai)**:
  - Tỷ lệ hệ thống từ chối nhầm người dùng chính chủ, hợp lệ do góc quét lệch hoặc ngón tay bị xước.
  - Phản ánh **mức độ tiện dụng (Convenience level)** của hệ thống: FRR càng nhỏ thì người dùng càng thoải mái.
- **CER / EER (Crossover / Equal Error Rate)**:
  - Điểm mà tại đó giá trị sai số $FAR = FRR$.
  - Giá trị EER là tiêu chí định lượng chuẩn nhất để so sánh độ chính xác của hai thuật toán sinh trắc học khác nhau (thuật toán nào có **EER càng thấp thì chất lượng nhận diện càng vượt trội**).

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Đồ thị đường cong giao thoa sai số CER / EER
```
Tỷ lệ lỗi (%)
      ▲
 100% │ \                                       /  ◄─── Đường cong FRR (Từ chối sai)
      │  \                                     /
      │   \                                   /
      │    \               [EER / CER]       /
      │     \                   ▲           /
      │      \                 / \         /
      │       \               /   \       /
      │        \             /     \     /
      │         \           /       \   /
      │          \         /         \ /
      │           \       /           X
      │            \     /           / \
      │             \   /           /   \   ◄─── Đường cong FAR (Chấp nhận sai)
      └──────────────┴─┴───────────┴─────┴────────► Ngưỡng nhạy (Threshold)
               (Rất lỏng lẻo)            (Rất khắt khe)
```

---

### 복습 체크리스트
- [ ] Bốn nhân tố xác thực người dùng bao gồm những nhóm nào?
- [ ] Tại sao việc kết hợp mật khẩu và câu hỏi bảo mật không được coi là xác thực đa nhân tố (MFA)?
- [ ] Chỉ số FAR trong nhận diện sinh trắc học đo lường loại rủi ro an ninh nào?
- [ ] Chỉ số EER (Equal Error Rate) được dùng để so sánh điều gì giữa các hệ thống sinh trắc học?
