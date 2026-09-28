# 21. 데이터 전환 및 정제 (Chuyển đổi dữ liệu - ETL)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **21. 데이터 전환 및 정제 (Chuyển đổi dữ liệu - ETL)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

데이터, 전환, 정제

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **22. 기타 주요 개념 (Các khái niệm quan trọng khác)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **21. 데이터 전환 및 정제 (Chuyển đổi dữ liệu - ETL)** và nối nó với **22. 기타 주요 개념 (Các khái niệm quan trọng khác)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 21. 데이터 전환 및 정제 (Chuyển đổi dữ liệu - ETL)

### 데이터 전환 (Data Migration - Di chuyển dữ liệu)
Là quá trình chuyển dữ liệu từ hệ thống cũ sang hệ thống mới.
- **ETL 3 bước:**
  1. **E**xtraction (추출): Trích xuất từ nguồn.
  2. **T**ransformation (변환): Biến đổi cho phù hợp chuẩn mới.
  3. **L**oad (적재): Nạp vào hệ thống đích.

### 오류 데이터 정제 (Error Data Cleansing)
Quản lý trạng thái lỗi trong quá trình chuyển đổi:
- **Open (Mở):** Phát hiện lỗi, chưa phân tích.
- **Assigned (Đã giao):** Giao cho lập trình viên sửa.
- **Fixed (Đã sửa):** Đã sửa xong.
- **Closed (Đóng):** Đã kiểm thử (test / 테스트) lại và xác nhận bình thường.
- **Deferred (Trì hoãn):** Quyết định chưa sửa lúc này (hoặc không phải lỗi).

---
