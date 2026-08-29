# 19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

암호화, 기법과, 접근, 통제

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)

### 개인키 암호 방식 (Private Key / Symmetric Key - Mã hóa Khóa đối xứng)
- **개념 (Khái niệm):** Dùng **CÙNG MỘT KHÓA** để mã hóa và giải mã (단일키 - Khóa đơn).
- **장점 (Ưu điểm):** Tốc độ xử lý cực kỳ nhanh.
- **단점 (Nhược điểm):** Khó phân phối và quản lý khóa khi có quá nhiều người dùng.
- **종류 (Thuật toán tiêu biểu):** DES, AES, SEED, ARIA. (Chia làm 2 dạng: Block - theo khối, Stream - theo luồng bit).

> 💡 **Mẹo ghi nhớ:** **Đối-Cá-Nhanh-Khó** (Khóa Đối xứng = Khóa Cá nhân = Nhanh = Khó quản lý khóa).

### 접근통제 기술 (Access Control - Kỹ thuật kiểm soát truy cập)
| 종류 (Loại) | 기준 (Tiêu chí) | 특징 (Đặc điểm VN) |
|---|---|---|
| **DAC (임의 접근통제)** | 소유자 (Chủ sở hữu) | Chủ dữ liệu tự do cấp/thu quyền (GRANT/REVOKE). |
| **MAC (강제 접근통제)** | 보안 등급 (Mức độ bảo mật) | Hệ thống ép buộc dựa trên cấp độ bảo mật (VD: Top Secret). |
| **RBAC (역할기반 접근통제)** | 역할 (Vai trò) | Quyền gắn với chức vụ (VD: Manager, Staff). Đổi chức vụ = tự đổi quyền. |

### MAC 보안 모델 (Các mô hình bảo mật của MAC)
- **벨-라파듈라 (Bell-LaPadula):** Tập trung vào **기밀성 (Tính Bảo mật / Kín đáo)** (Quân đội). Không đọc lên trên, Không ghi xuống dưới.
- **비바 (Biba):** Tập trung vào **무결성 (Tính Toàn vẹn)**. Ngăn chặn việc sửa đổi trái phép.
- **클락-윌슨 (Clark-Wilson):** Dành cho thương mại, chỉ cho phép sửa qua phần mềm được ủy quyền.
- **만리장성 (Chinese Wall):** Tránh xung đột lợi ích (người xem hồ sơ công ty A thì không được xem của đối thủ B).

---
