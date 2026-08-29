# 1. 소프트웨어 공학 및 개발 방법론 (Kỹ nghệ phần mềm và Phương pháp luận phát triển)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **1. 소프트웨어 공학 및 개발 방법론 (Kỹ nghệ phần mềm và Phương pháp luận phát triển)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

소프트웨어, 공학, 개발, 방법론

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 1. 소프트웨어 공학 및 개발 방법론 (Kỹ nghệ phần mềm và Phương pháp luận phát triển)

### 001. 소프트웨어 공학의 기본 원칙 (Nguyên tắc cơ bản của kỹ nghệ phần mềm)
- 현대적인 프로그래밍 기술을 계속적으로 적용해야 한다. (Phải liên tục áp dụng các kỹ thuật lập trình hiện đại.)
- 개발된 소프트웨어의 품질이 유지되도록 지속적으로 검증해야 한다. (Phải liên tục xác minh để duy trì chất lượng phần mềm đã phát triển.)
- 소프트웨어 개발 관련 사항 및 결과에 대한 명확한 기록을 유지해야 한다. (Phải lưu giữ hồ sơ rõ ràng về các vấn đề và kết quả liên quan đến phát triển phần mềm.)
- **Ví dụ (Example):** Áp dụng CI/CD (Continuous Integration/Continuous Deployment) để liên tục kiểm thử (검증) phần mềm mỗi khi có code mới.
- 💡 **Mẹo ghi nhớ (Mnemonic):** **HKK** (Hiện - Kiểm - Ký): **Hãy Kiểm Kê** (Kỹ thuật hiện đại - Kiểm chứng - Ghi chép).

### 002. 폭포수 모형 (Waterfall Model / Mô hình thác nước)
- 이전 단계로 돌아갈 수 없다는 전제하에 각 단계를 확실히 매듭짓고 다음 단계를 진행하는 개발 방법론이다. (Là phương pháp phát triển với tiền đề không thể quay lại giai đoạn trước, hoàn thành dứt điểm từng giai đoạn rồi mới tiến sang giai đoạn tiếp theo.)
- 보헴이 제시한 고전적 생명 주기 모형이다. (Là mô hình vòng đời cổ điển do Boehm đề xuất.)
- 요구사항을 반영하기 어렵다. (Khó phản ánh/thay đổi yêu cầu.)
- **Ví dụ (Example):** Xây dựng một ngôi nhà, bạn không thể xây mái nhà khi chưa làm xong móng. (Phải theo tuần tự).
- 💡 **Mẹo ghi nhớ (Mnemonic):** Nước chảy từ trên xuống, không chảy ngược lại (이전 단계로 돌아갈 수 없음).

### 003. 나선형 모형 (Spiral Model / Mô hình xoắn ốc)
- 나선을 따라 돌듯이 점진적으로 완벽한 최종 소프트웨어를 개발하는 것이다. (Phát triển phần mềm cuối cùng hoàn hảo một cách tuần tự giống như quay theo hình xoắn ốc.)
- '계획 수립 → 위험 분석 → 개발 및 검증 → 고객 평가' 과정이 반복적으로 수행된다. (Quá trình 'Lập kế hoạch → Phân tích rủi ro → Phát triển & Kiểm chứng → Khách hàng đánh giá' được lặp đi lặp lại.)
- **Ví dụ (Example):** Phát triển một game lớn, ban đầu làm bản demo (1 vòng xoắn), đánh giá rủi ro, rồi mới phát triển thêm tính năng (vòng xoắn tiếp theo).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **KNKK** (Kế - Nguy - Khai - Khách): **Kế Nguy Khách Khóc** (Lập KH - Rủi ro - Phát triển - Khách hàng).

### 004. 애자일 모형의 주요 방법론 (Các phương pháp luận chính của mô hình Agile)
- 스크럼 (Scrum
- XP (eXtreme Programming)
- 기능 중심 개발 (FDD; Feature Driven Development)
- 칸반 (Kanban)
- Lean
- **Ví dụ (Example):** Các công ty startup thường dùng Scrum để phát triển nhanh một ứng dụng, chia thành các Sprint ngắn 2 tuần.
- 💡 **Mẹo ghi nhớ (Mnemonic):** **SXFKL** (Scrum, XP, FDD, Kanban, Lean): **Sợ Xấu Phải Kiêng Luôn**.

### 005. 애자일 개발 4가지 핵심 가치 (4 Giá trị cốt lõi của phát triển Agile)
- 프로세스와 도구보다는 개인과 상호작용에 더 가치를 둔다. (Coi trọng cá nhân và sự tương tác hơn là quy trình và công cụ.)
- 방대한 문서보다는 실행되는 SW에 더 가치를 둔다. (Coi trọng phần mềm chạy được hơn là tài liệu đồ sộ.)
- 계약 협상보다는 고객과 협업에 더 가치를 둔다. (Coi trọng sự cộng tác với khách hàng hơn là đàm phán hợp đồng.)
- 계획을 따르기 보다는 변화에 반응하는 것에 더 가치를 둔다. (Coi trọng việc phản hồi với sự thay đổi hơn là bám sát kế hoạch.)
- **Ví dụ (Example):** Thay vì viết tài liệu 100 trang cho khách, nhóm Agile sẽ đưa cho khách một bản demo chạy được (실행되는 SW) để lấy ý kiến ngay.
- 💡 **Mẹo ghi nhớ (Mnemonic):** **CTKB** (Cá - Thực - Khách - Biến): **Cá Thực Khó Bắt** (Cá nhân - Thực thi - Khách hàng - Biến đổi).

### 006. XP의 핵심 가치 (Giá trị cốt lõi của XP - eXtreme Programming)
- 의사소통 (Communication - Giao tiếp)
- 단순성 (Simplicity - Sự đơn giản)
- 용기 (Courage - Dũng cảm)
- 존중 (Respect - Tôn trọng)
- 피드백 (Feedback - Phản hồi)
- **Ví dụ (Example):** Developer có 'dũng cảm' (용기) để xóa những đoạn code cũ không cần thiết và viết lại cho 'đơn giản' (단순성).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **YĐDTP** (Ý - Đơn - Dũng - Tôn - Phản): **Ý Định Dũng Tướng Phàm**.
