# 5. 관계 데이터 연산 및 정규화 (Phép toán quan hệ & Chuẩn hóa)

## 5. 관계 데이터 연산 및 정규화 (Phép toán quan hệ & Chuẩn hóa)

### 관계대수와 관계해석 (Đại số quan hệ & Giải tích quan hệ)
Phần “관계대수와 관계해석 (Đại số quan hệ & Giải tích quan hệ)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **관계대수 (Relational Algebra):** 절차적 언어 (Procedural). 원하는 정보와 그 정보를 **어떻게** 유도하는지 기술. (Ngôn ngữ thủ tục: Chỉ ra 'Cái gì' và 'Làm thế nào').
- **관계해석 (Relational Calculus):** 비절차적 언어 (Non-procedural). 원하는 정보가 **무엇**인지 만을 정의. (Ngôn ngữ phi thủ tục: Chỉ ra 'Cái gì').

### 순수 관계 연산자 4가지 (4 Phép toán quan hệ thuần túy)
Phần “순수 관계 연산자 4가지 (4 Phép toán quan hệ thuần túy)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **Select (σ / 시그마):** 조건을 만족하는 행(튜플)을 구하는 수평 연산. (Chọn ra các hàng thỏa mãn điều kiện).
- **Project (π / 파이):** 제시된 열(속성)만을 추출하는 수직 연산. (Chọn ra các cột cần thiết).
- **Join (▷◁):** 공통 속성을 중심으로 2개의 릴레이션을 하나로 합침. (Kết nối 2 bảng).
- **Division (÷):** R의 속성이 S의 속성값을 모두 가진 튜플에서 S가 가진 속성을 제외하고 구하는 연산. (Phép chia: Lấy ra các giá trị của bảng R có mặt đầy đủ trong bảng S).

### 이상(Anomaly) 현상 (Hiện tượng Dị thường dữ liệu)
Phần “이상(Anomaly) 현상 (Hiện tượng Dị thường dữ liệu)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 정규화를 거치지 않아 데이터가 중복될 때 발생하는 예기치 못한 현상. (Lỗi xảy ra do dữ liệu trùng lặp khi chưa chuẩn hóa).
- **삽입 이상 (Insertion):** 원하지 않는 값까지 억지로 삽입해야 하는 현상. (Khi thêm dữ liệu phải thêm cả dữ liệu không mong muốn do bắt buộc).
- **삭제 이상 (Deletion):** 한 튜플을 삭제할 때 의도와 상관없는 값까지 연쇄 삭제되는 현상. (Xóa 1 thông tin kéo theo mất luôn thông tin khác).
- **갱신 이상 (Update):** 일부 정보만 갱신되어 정보의 모순이 생기는 현상. (Cập nhật thiếu sót gây ra mâu thuẫn dữ liệu).

### 정규화(Normalization) 과정과 암기법 (Quy trình chuẩn hóa)
Phần “정규화(Normalization) 과정과 암기법 (Quy trình chuẩn hóa)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 잘못 설계된 스키마를 쪼개어 바람직하게 만드는 논리적 설계 단계. (Chia nhỏ bảng để tối ưu dữ liệu).
- **1NF:** 도메인이 원자값 (Mỗi ô chỉ có 1 giá trị duy nhất).
- **2NF:** 부분적 함수 종속 제거 (Loại bỏ phụ thuộc hàm từng phần).
- **3NF:** 이행적 함수 종속 제거 (Loại bỏ phụ thuộc hàm bắc cầu A->B->C).
- **BCNF:** 결정자이면서 후보키가 아닌 것 제거 (Mọi yếu tố quyết định đều phải là khóa ứng viên).
- **4NF:** 다치 종속 제거 (Loại bỏ phụ thuộc đa trị).
- **5NF:** 조인 종속성 이용 (Dùng phụ thuộc Join).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **DBIGDJ** (Do-Bu-I-Gyul-Da-Jo): **Đi Bộ Ít Giúp Đỡ Jo** -> Do (Domain), Bu (부분), I (이행), Gyul (결정자), Da (다치), Jo (조인).
