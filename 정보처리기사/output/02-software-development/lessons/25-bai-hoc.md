# 109 ~ 112: 형상 관리 (SCM - Software Configuration Management)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **109 ~ 112: 형상 관리 (SCM - Software Configuration Management)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

형상, 관리

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **핵심 032 & 033: 형상 관리 및 IDE (Configuration Management & IDE)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **116 & 117: 형상 관리 도구 (SVN vs Git)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **109 ~ 112: 형상 관리 (SCM - Software Configuration Management)** và nối nó với **116 & 117: 형상 관리 도구 (SVN vs Git)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 109 ~ 112: 형상 관리 (SCM - Software Configuration Management)

- **형상 관리 (SCM):** 소프트웨어 변경 사항을 체계적으로 관리. (Quản lý mọi thay đổi của phần mềm: Source code, tài liệu, thiết kế... trong suốt vòng đời).
- **목적:** 가시성 (Tính hiển thị - ai đang làm gì), 추적성 (Tính truy xuất - ai gây ra lỗi này), 무절제한 변경 방지 (Ngăn chặn việc sửa code vô tội vạ).

### 형상 관리 5대 기능 (5 Chức năng của SCM)
1. **형상 식별 (Identification):** Đặt tên, đánh số phiên bản, phân nhánh (Tree) để dễ quản lý.
2. **버전 제어 (Version Control):** Lưu lại các phiên bản (version / 버전) cũ/mới.
3. **형상 통제 (Configuration Control):** Yêu cầu đổi mã (code / 코드) phải được xem xét kỹ trước khi nhập vào bản chính (Baseline).
4. **형상 감사 (Audit):** Kiểm tra lại xem mã (code / 코드) đã chuẩn chưa.
5. **형상 기록 (Status Reporting):** Ghi chép lịch sử báo cáo.

### 버전 관리 용어 (Thuật ngữ Version Control)
- **저장소 (Repository):** Kho lưu trữ mã (code / 코드).
- **체크아웃 (Check-out):** Lấy mã (code / 코드) từ Kho về máy mình để sửa.
- **체크인 (Check-in) / 커밋 (Commit):** Lưu mã (code / 코드) mình vừa sửa vào máy mình (Local) hoặc đưa lên Kho.
- **동기화 (Update):** Lấy mã (code / 코드) mới nhất của người khác trên Kho về máy mình để đồng bộ.

---
