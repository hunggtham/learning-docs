# 핵심 046: 인터페이스 설계 확인 (EAI 구축 유형 - EAI Integration Types)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **핵심 046: 인터페이스 설계 확인 (EAI 구축 유형 - EAI Integration Types)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

핵심, 인터페이스, 설계, 확인

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 핵심 046: 인터페이스 설계 확인 (EAI 구축 유형 - EAI Integration Types)

- **EAI (Enterprise Application Integration):** Doanh nghiệp có nhiều phần mềm (Kế toán, Nhân sự, Kho...), EAI giúp chúng nói chuyện được với nhau.

| 유형 (Kiểu) | 기능 (Chức năng) |
|---|---|
| **Point-to-Point** | 1:1로 연결 (Nối trực tiếp 1-1). Không có Middleware ở giữa. Khó thay đổi. |
| **Hub & Spoke** | 단일 접점인 허브 시스템을 통해 데이터를 전송하는 중앙 집중형. (Nối kiểu nan hoa xe đạp. Tập trung vào cái Hub ở giữa. Hub sập là chết hết.) |
| **Message Bus** | 미들웨어(버스)를 두어 처리하는 방식. 확장성이 뛰어나며 대용량 처리가 가능. (Dùng một trục xe bus (Middleware) ở giữa. Rất dễ mở rộng và xử lý lượng lớn.) |
| **Hybrid** | 그룹 내에서는 Hub & Spoke, 그룹 간에는 Message Bus. (Lai tạp: Trong nhóm thì dùng Hub, giữa các nhóm thì dùng Bus.) |

- 💡 **Mẹo ghi nhớ (Mnemonics):** Hub & Spoke = Nan hoa (Có tâm Hub, sập tâm là chết). Message Bus = Xe buýt (Chở được nhiều, dễ mở rộng).

---
