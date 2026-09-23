# 298. PCB (Process Control Block)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **298. PCB (Process Control Block)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

PCB

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 298. PCB (Process Control Block)
### TẦNG A – NOTE NÉN (ÔN / ĐI THI)
- **개념 (Khái niệm)**: 운영체제가 각 프로세스를 관리하기 위해 정보를 저장하는 데이터 구조. (Cấu trúc dữ liệu HĐH dùng để lưu thông tin quản lý từng tiến trình.)
- **핵심 키워드 (Từ khóa)**: 프로세스 상태 (Trạng thái tiến trình), 식별자 (PID), 우선순위 (Priority).
- **시험 포인트 (Điểm thi)**: 프로세스 생성 시 고유하게 생성되며, 종료 시 제거됨. (Được tạo ra duy nhất khi tiến trình bắt đầu và bị xóa khi kết thúc.)

### TẦNG B – NOTE 보충 (HIỂU SÂU)
- 현재 상태(준비/실행/대기), CPU 레지스터 정보, 자원 정보 포함. (Chứa trạng thái hiện tại, thanh ghi CPU, tài nguyên được cấp.)
- 문맥 교환(Context Switching) 시, 현재까지 진행 상황을 PCB에 저장. (Khi chuyển đổi ngữ cảnh, lưu tiến độ vào PCB để sau này chạy tiếp.)
- **예시 (Ví dụ)**: 병원에서 환자(프로세스)마다 차트(PCB)를 만들어 병력과 현재 상태를 기록하는 것과 같음. 퇴원하면 차트를 닫음. (Giống như Bệnh án (PCB) của từng bệnh nhân (Process), ghi lại tình trạng, xuất viện thì đóng hồ sơ.)
- 💡 **Mẹo ghi nhớ**: PCB giống như "Thẻ căn cước + Hồ sơ bệnh án" của một tiến trình.
