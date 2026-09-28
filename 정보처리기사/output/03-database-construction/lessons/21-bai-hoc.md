# 20. 쿼리 성능 최적화와 반정규화 (Tối ưu hóa Truy vấn và Phi chuẩn hóa)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **20. 쿼리 성능 최적화와 반정규화 (Tối ưu hóa Truy vấn và Phi chuẩn hóa)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

쿼리, 성능, 최적화와, 반정규화

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **16. 정규화(Normalization)와 이상 현상(Anomaly)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **130-132. 트랜잭션 (Transaction)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **20. 쿼리 성능 최적화와 반정규화 (Tối ưu hóa Truy vấn và Phi chuẩn hóa)** và nối nó với **130-132. 트랜잭션 (Transaction)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 20. 쿼리 성능 최적화와 반정규화 (Tối ưu hóa Truy vấn và Phi chuẩn hóa)

### 쿼리 성능 최적화 (Query Optimization)
Tối ưu hóa tốc độ chạy SQL thông qua **Optimizer (옵티마이저 - Bộ tối ưu)**.
- **RBO (Rule-Based Optimizer):** Tối ưu theo **규칙 (Quy tắc)** định sẵn. Phụ thuộc vào kinh nghiệm người lập trình.
- **CBO (Cost-Based Optimizer):** Tối ưu theo **비용 (Chi phí)** ước tính dựa trên thống kê dữ liệu. Rất thông minh và phổ biến hiện nay.
- **APM (Application Performance Management):** Công cụ giám sát hiệu suất ứng dụng.

### 반정규화 (Denormalization - Phi chuẩn hóa)
- **개념:** Cố tình phá vỡ chuẩn hóa (Gộp bảng, thêm dữ liệu trùng lặp).
- **목적:** Để **tăng hiệu suất truy vấn (조회 속도 향상)** khi thao tác phép nối (join / 조인) quá nhiều.
- **단점:** Đánh đổi bằng sự **suy giảm tính nhất quán** (데이터 정합성 저하) và khó khăn khi cập nhật dữ liệu.

---
