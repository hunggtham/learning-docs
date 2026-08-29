# 16. 정규화(Normalization)와 이상 현상(Anomaly)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **16. 정규화(Normalization)와 이상 현상(Anomaly)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

정규화

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 16. 정규화(Normalization)와 이상 현상(Anomaly)

**정규화 (Chuẩn hóa):** Quá trình chia nhỏ các bảng để giảm thiểu dư thừa dữ liệu và tránh các hiện tượng bất thường (이상 현상).

### 이상 현상 (Anomaly - Bất thường)
- **삽입 이상 (Insertion Anomaly):** Lỗi khi thêm dữ liệu (phải thêm các dữ liệu không mong muốn).
- **갱신 이상 (Update Anomaly):** Lỗi khi cập nhật (cập nhật thiếu sót dẫn đến dữ liệu không nhất quán).
- **삭제 이상 (Deletion Anomaly):** Lỗi 연쇄 삭제 (Xóa dây chuyền) (xóa một dữ liệu kéo theo mất luôn dữ liệu quan trọng khác).

### 정규화 단계 (Các chuẩn - Bắt buộc học thuộc)
| 정규형 (Chuẩn) | 조건 (Điều kiện để đạt được) | Mẹo ghi nhớ (VN) |
|---|---|---|
| **1NF** | **도**메인이 **원자값** (Mọi giá trị phải là Nguyên tử) | **도** (Do - Domain nguyên tử) |
| **2NF** | **부**분 함수 종속 제거 (Loại bỏ phụ thuộc hàm từng phần) | **부** (Bu - Bỏ phụ thuộc phần) |
| **3NF** | **이**행 함수 종속 제거 (Loại bỏ phụ thuộc hàm bắc cầu: A→B, B→C => A→C) | **이** (I - Loại bắc cầu / I-haeng) |
| **BCNF** | 모든 **결**정자가 후보키 (Tất cả yếu tố quyết định phải là Khóa ứng viên) | **결** (Gyeol - BCNF) |
| **4NF** | **다**치 종속 제거 (Loại bỏ phụ thuộc đa trị) | **다** (Da - Đa trị) |
| **5NF** | **조**인 종속 제거 (Loại bỏ phụ thuộc Join) | **조** (Jo - Join) |

> 💡 **Mẹo ghi nhớ:** **Đồ-Bếp-I-Kết-Đa-Giò** (Đô-main, Bếp-Phần, I-Bắc cầu, Kết-Quyết định, Đa trị, Giò-Chung).

---
