# 285 & 295. 워킹 셋 (Working Set / Tập làm việc)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **285 & 295. 워킹 셋 (Working Set / Tập làm việc)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

워킹

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 285 & 295. 워킹 셋 (Working Set / Tập làm việc)
### TẦNG A – NOTE NÉN (ÔN / ĐI THI)
- **개념 (Khái niệm)**: 프로세스가 원활한 수행을 위해 일정 시간 동안 집중적으로 참조하는 페이지들의 집합. (Tập hợp các trang mà tiến trình tham chiếu tập trung trong một khoảng thời gian để chạy mượt mà.)
- **핵심 키워드 (Từ khóa)**: 데닝 (Denning), Locality 활용 (Ứng dụng Locality), 페이지 부재 감소 (Giảm Page Fault), 동적 변경 (Thay đổi động).
- **시험 포인트 (Điểm thi)**: 자주 참조되는 워킹 셋을 주기억장치에 상주시킴으로써 시스템을 안정화(스래싱 방지)한다는 점. (Giữ Working Set trong bộ nhớ chính giúp hệ thống ổn định và tránh Thrashing.)

### TẦNG B – NOTE 보충 (HIỂU SÂU)
- 데닝(Denning)이 제안한 모델로, 프로그램의 국부성(Locality)을 이용. (Mô hình do Denning đề xuất dựa trên tính cục bộ.)
- 시간에 따라 참조하는 페이지가 달라지므로 지속적으로 (동적으로) 변경됨. (Thay đổi động theo thời gian.)
- **예시 (Ví dụ)**: 당신이 시험 공부를 할 때 지금 당장 책상 위에 꺼내놓은 책과 필기구들이 '워킹 셋'입니다. 과목이 바뀌면 책상 위 물건(워킹 셋)도 바뀝니다. (Những cuốn sách và bút bạn đang để trên bàn học ngay lúc này chính là 'Working Set'. Khi chuyển môn, đồ trên bàn cũng thay đổi.)
- 💡 **Mẹo ghi nhớ**: Working Set = Những món đồ đang "Working" (Đang dùng) phải để sẵn trên bàn (Memory).
