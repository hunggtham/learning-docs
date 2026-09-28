# 120-2 ~ 126: 애플리케이션 테스트 이론 (Application Test Theory)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **120-2 ~ 126: 애플리케이션 테스트 이론 (Application Test Theory)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

애플리케이션, 테스트, 이론

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **105: 시각에 따른 테스트 (Verification vs Validation)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **127 ~ 129: 화이트박스 테스트 (White Box Test)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **120-2 ~ 126: 애플리케이션 테스트 이론 (Application Test Theory)** và nối nó với **127 ~ 129: 화이트박스 테스트 (White Box Test)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 120-2 ~ 126: 애플리케이션 테스트 이론 (Application Test Theory)

### 테스트의 기본 원리 (Nguyên lý cơ bản)
- **완벽한 테스트 불가능:** Không thể khẳng định 100% hết bug.
- **파레토 법칙 (Pareto):** 80% bug nằm ở 20% mã (code / 코드) cốt lõi. (Đám mây lỗi).
- **살충제 패러독스 (Pesticide Paradox):** kiểm thử (test / 테스트) hoài 1 kịch bản sẽ bị "nhờn", phải liên tục thay đổi bộ kiểm thử (test / 테스트).
- **정황 의존 (Context):** Tùy thuộc ngữ cảnh (Web, Game) mà kiểm thử (test / 테스트) khác nhau.

### 테스트 분류 (Phân loại Test)
1. **실행 여부 (Theo việc có chạy code không):**
   - **정적 테스트 (Static):** Không chạy mã (code / 코드). Đọc, rà soát (review / 검토) tài liệu (Walkthrough, Inspection).
   - **동적 테스트 (Dynamic):** Chạy mã (code / 코드). (White box, Black box).
2. **테스트 기반 (Theo căn cứ Test):**
   - **명세 기반 (Specification):** Dựa vào tài liệu yêu cầu.
   - **구조 기반 (Structure):** Dựa vào luồng lô-gic (logic / 논리) của mã (code / 코드).
   - **경험 기반 (Experience):** Dựa vào kinh nghiệm tester (Đoán lỗi).
3. **목적 (Theo mục đích):**
   - **강도 (Stress):** Ép tải (Dồn dập bắt nó sập).
   - **회귀 (Regression):** Sửa mã (code / 코드) xong kiểm thử (test / 테스트) lại xem có hỏng chỗ cũ không.
   - **회복 (Recovery):** Giả vờ ngắt điện xem app phục hồi dữ liệu (data / 데이터) được không.
   - **병행 (Parallel):** Chạy app cũ và app mới cùng lúc để so kết quả.

- 💡 **Mẹo ghi nhớ (Mnemonics):** Inspection (Khám nghiệm) = Tĩnh (Static). Regression (Hồi quy) = Sửa xong kiểm thử (test / 테스트) lại.

---
