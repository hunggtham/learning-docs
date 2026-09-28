# 10. 트랜잭션 관리 기법 및 제어 (Quản lý và điều khiển giao dịch)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **10. 트랜잭션 관리 기법 및 제어 (Quản lý và điều khiển giao dịch)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

트랜잭션, 관리, 기법, 제어

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **9. 인덱스와 트랜잭션 (Index và Giao dịch)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **143-145. SQL 분류 (SQL Categories)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **10. 트랜잭션 관리 기법 및 제어 (Quản lý và điều khiển giao dịch)** và nối nó với **143-145. SQL 분류 (SQL Categories)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 10. 트랜잭션 관리 기법 및 제어 (Quản lý và điều khiển giao dịch)

### 병행제어 기법 (Concurrency Control - Kiểm soát đồng thời)
- **로킹 (Locking):** Khóa tài nguyên để đảm bảo giao dịch chạy tuần tự (직렬화).
  - *Đơn vị khóa (Locking Unit):* Càng lớn (DB, Bảng) -> Ít khóa (lock / 잠금), Overhead nhỏ, Tính đồng thời giảm. Càng nhỏ (Bản ghi, Trường) -> Nhiều khóa (lock / 잠금), Overhead lớn, Tính đồng thời cao.
- **타임스탬프 (Time Stamping):** Gắn mốc thời gian để ưu tiên.
- **다중버전 동시제어 (MVCC):** Giữ nhiều phiên bản dữ liệu.
- **낙관적 병행제어 (Optimistic):** Cứ cho chạy đi, kết thúc mới kiểm tra lỗi (thích hợp môi trường ít xung đột).

### 트랜잭션 상태 (Trạng thái giao dịch)
- **활동 (Active):** Đang chạy.
- **부분 완료 (Partially Committed):** Đã chạy lệnh xong, chuẩn bị lần ghi nhận (commit / 커밋) nhưng chưa ghi lên đĩa.
- **완료 (Committed):** Thành công và lưu vĩnh viễn.
- **실패 (Failed):** Có lỗi xảy ra.
- **철회 (Aborted):** Bị hủy bỏ (Rollback).

### 데이터 사전 (Data Dictionary / System Catalog / Metadata)
- Lưu thông tin về các đối tượng (bảng, view, index...).
- DBMS tự động cập nhật, người dùng **chỉ được Read Only (조회만 가능)**.

---
