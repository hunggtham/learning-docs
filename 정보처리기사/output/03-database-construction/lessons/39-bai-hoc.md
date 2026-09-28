# 201-203. 스토리지 시스템 (Storage Systems)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **201-203. 스토리지 시스템 (Storage Systems)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

스토리지, 시스템

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **198. 암호화 심화 (Encryption Deep Dive)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **201-203. 스토리지 시스템 (Storage Systems)** và nối nó với **198. 암호화 심화 (Encryption Deep Dive)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 201-203. 스토리지 시스템 (Storage Systems)
- **DAS (Direct Attached Storage):** 서버와 저장장치를 전용 케이블로 직접 연결. (외장하드 방식). 확장성 떨어짐.
- **NAS (Network Attached Storage):** 네트워크를 통해 연결. 파일 공유 가능, 확장성 우수.
- **SAN (Storage Area Network):** 서버와 저장장치를 연결하는 전용 네트워크 구성. (광 채널 스위치). DAS의 속도 + NAS의 공유 장점.
- **VI (Vietnamese) (Tiếng Việt):** Hệ thống lưu trữ.
  - DAS: Kết nối trực tiếp (cáp).
  - NAS: Kết nối qua mạng LAN (chia sẻ file).
  - SAN: Mạng lưu trữ chuyên dụng (tốc độ cao + chia sẻ).
