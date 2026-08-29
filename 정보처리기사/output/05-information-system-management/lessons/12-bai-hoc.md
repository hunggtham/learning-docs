# 7. 데이터베이스 핵심 기술 (Công nghệ lõi Cơ sở dữ liệu)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **7. 데이터베이스 핵심 기술 (Công nghệ lõi Cơ sở dữ liệu)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

데이터베이스, 핵심, 기술

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 7. 데이터베이스 핵심 기술 (Công nghệ lõi Cơ sở dữ liệu)

### 7.1 회복 및 동시성 제어 (Recovery & Concurrency)
- **회복 (Recovery):** 장애 발생 시 손상 이전의 정상 상태로 복구.
- **즉각 갱신 기법 (Immediate Update):** 트랜잭션 부분 완료 전이라도 즉시 DB에 반영. 갱신 내용은 **Log에 보관**하여 회복에 대비.
- **로킹 단위 (Locking Granularity):** 병행제어에서 한꺼번에 로킹하는 객체 크기.
  - **단위가 크면:** 로크 수가 작아 관리하기 쉽지만 병행성 저하.
  - **단위가 작으면:** 로크 수가 많아 관리 복잡/오버헤드 증가, 하지만 병행성 상승.
- **타임 스탬프 순서 (Time Stamp Ordering):** 직렬성 순서를 결정하기 위해 트랜잭션 처리 순서를 미리 선택.
- **Tiếng Việt:** 
  - Immediate Update: Cập nhật ngay lập tức (dùng Log để phục hồi).
  - Locking Granularity: Kích thước khóa. Khóa lớn -> dễ quản lý, đồng thời thấp. Khóa nhỏ -> khó quản lý, đồng thời cao.

### 7.2 교착상태 (Deadlock)
- **발생 4가지 조건:** 상호 배제(Mutual Exclusion), 점유와 대기(Hold and Wait), 비선점(Non-preemption), 환형 대기(Circular Wait).
- **회피 기법 (Avoidance):** 교착상태 가능성을 피해 나가는 방법. 주로 **은행원 알고리즘 (Banker's Algorithm, E. J. Dijkstra)** 사용.
- **Tiếng Việt:** 4 điều kiện Deadlock: Loại trừ lẫn nhau, Giữ & Chờ, Không trưng dụng, Chờ vòng tròn. Tránh Deadlock dùng Thuật toán Nhà băng.
- 💡 **Mẹo ghi nhớ:** Điều kiện Deadlock: Độc Giữ Không Vòng (Độc quyền, Giữ và chờ, Không ưu tiên, Vòng tròn).
