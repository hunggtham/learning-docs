# 4. 운영 환경 구축 고려사항 (Operation Environment Considerations)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **4. 운영 환경 구축 고려사항 (Operation Environment Considerations)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

운영, 환경, 구축, 고려사항

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **2. 스크럼 및 XP 추가 개념 (Advanced Scrum & XP)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **6. 구조적 분석 도구 (Structured Analysis Tools)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **4. 운영 환경 구축 고려사항 (Operation Environment Considerations)** và nối nó với **6. 구조적 분석 도구 (Structured Analysis Tools)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 4. 운영 환경 구축 고려사항 (Operation Environment Considerations)
- **운영체제 (OS)** & **DBMS**: 가용성 (Availability), 성능 (Performance), 기술 지원 (Tech Support), 구축 비용 (Cost).
  - OS có thêm: 주변 기기 (Thiết bị ngoại vi).
  - DBMS có thêm: 상호 호환성 (Khả năng tương thích - JDBC/ODBC).
- **WAS (Web Application Server)**: Xử lý nội dung động. Có thêm **가비지 컬렉션 (GC - Dọn rác)**.
- **오픈 소스 (Open Source)**: Cần chú ý 라이선스 (Bản quyền), 사용자 수 (Số lượng người dùng), 기술의 지속 가능성 (Khả năng duy trì công nghệ).
