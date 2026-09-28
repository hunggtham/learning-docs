# 스토리지 시스템 (Storage Systems)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **스토리지 시스템 (Storage Systems)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

스토리지, 시스템

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **소프트웨어 생명주기 모델 (SDLC Models)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **1. 메모리 버퍼 오버플로 (Memory Buffer Overflow / Tràn bộ đệm bộ nhớ)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **스토리지 시스템 (Storage Systems)** và nối nó với **1. 메모리 버퍼 오버플로 (Memory Buffer Overflow / Tràn bộ đệm bộ nhớ)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 스토리지 시스템 (Storage Systems)
대용량 데이터를 저장하기 위한 장치 구성 방식.
- **DAS (Direct Attached Storage)**: 서버와 스토리지를 전용 케이블로 **직접 연결**.
- **NAS (Network Attached Storage)**: 서버와 스토리지를 **네트워크(LAN)**로 연결.
- **SAN (Storage Area Network)**: 스토리지 전용 **광 채널 네트워크(FC-SAN)**를 별도로 구성하여 고속 전송.

💡 **Mẹo ghi nhớ (Mnemonics):**
- **DAS**: Direct (Cắm trực tiếp).
- **NAS**: mạng (network / 네트워크).
- **SAN**: Area mạng (network / 네트워크).
