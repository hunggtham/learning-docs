# 9. 인덱스와 트랜잭션 (Index và Giao dịch)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **9. 인덱스와 트랜잭션 (Index và Giao dịch)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

인덱스와, 트랜잭션

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 9. 인덱스와 트랜잭션 (Index và Giao dịch)

### 인덱스 (Index - Chỉ mục)
Dùng để tăng tốc độ tìm kiếm.
- **트리 기반 (Tree-based):** Thường dùng B-Tree, tốt cho tìm theo khoảng.
- **해시 (Hash):** Dùng Key-Value, truy cập nhanh và chi phí đồng đều, không tốt cho tìm khoảng.
- **비트맵 (Bitmap):** Dùng bit 0 và 1, phù hợp cho cột có ít giá trị khác biệt (Gender: M/F).
- **클러스터드 인덱스 (Clustered Index):** Dữ liệu thực sự được sắp xếp vật lý theo thứ tự Index. Rất tốt để tìm khoảng (Range search).

### 트랜잭션 (Transaction - Giao dịch) - ACID
| 특징 (Đặc tính) | 설명 (Mô tả) | Ý nghĩa (VN) |
|---|---|---|
| **원자성 (Atomicity)** | All or Nothing (모두 반영되거나 전혀 반영되지 않음). | **Tính nguyên tử:** Chuyển tiền: hoặc cả 2 người cùng cập nhật, hoặc không ai thay đổi gì. Dùng Commit/Rollback. |
| **일관성 (Consistency)** | 일관적인 DB 상태 유지 (Trạng thái DB nhất quán). | **Tính nhất quán:** Dữ liệu sau giao dịch phải hợp lệ. |
| **고립성 (Isolation)** | 서로 간섭 불가 (Không can thiệp lẫn nhau). | **Tính cô lập:** Khi giao dịch A đang chạy, giao dịch B không thể nhảy vào làm sai lệch. |
| **영속성 (Durability)** | 영구적으로 결과 저장 (Lưu kết quả vĩnh viễn). | **Tính bền vững:** Sau khi COMMIT, dù sập nguồn dữ liệu vẫn tồn tại. |

> 💡 **Mẹo ghi nhớ:** **ACID** (Nguyên tử - Nhất quán - Cô lập - Bền vững).

---
