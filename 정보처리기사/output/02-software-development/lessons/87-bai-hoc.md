# 027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

알고리즘, 설계, 기법과, 시간, 복잡도

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)

### 알고리즘 설계 기법 (Kỹ thuật thiết kế thuật toán)
- **분할과 정복 (Divide & Conquer):** Chia để trị. Chia nhỏ vấn đề đến khi không chia được nữa rồi gộp lại. (VD: Merge Sort, Quick Sort).
- **동적계획법 (Dynamic Programming - Quy hoạch động):** Chia bài toán, nhưng CÓ lưu lại kết quả (bộ nhớ) để tận dụng cho lần sau. (VD: Fibonacci).
- **탐욕법 (Greedy):** Tham lam. Chọn cái tốt nhất ở *ngay thời điểm hiện tại*, không cần biết tương lai.
- **백트래킹 (Backtracking):** Quay lui. Đi thử, nếu thấy bế tắc (không triển vọng - promising) thì quay lại nút cha.

### 시간 복잡도 (Time Complexity - Độ phức tạp thời gian)
- Đếm số lần thực thi các phép toán (không phải tính thời gian bằng giây).
- Biểu diễn: Big-O (최악 - Tệ nhất), Theta (평균 - Trung bình), Omega (최상 - Tốt nhất).
- **Thứ tự (Nhanh -> Chậm):** O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ)
- O(1) nghĩa là: Dữ liệu lớn đến đâu thời gian vẫn không đổi.

- **Vietnamese Explanation:** Greedy giống như đi nhặt tiền: cứ thấy tờ to nhất trước mặt là nhặt, bất chấp sau đó dẫn vào ngõ cụt. Dynamic Programming giống như làm toán: kết quả bài 1 lưu ra nháp để dùng cho bài 2.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Divide = Cắt nhỏ. Dynamic = Nhớ bài cũ. Greedy = Tham bát bỏ mâm. Backtrack = Đi lùi. O(1) là nhanh nhất.

---
