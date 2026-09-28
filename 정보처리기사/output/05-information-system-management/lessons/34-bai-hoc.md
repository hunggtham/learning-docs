# 4. 보안 기능 및 에러 처리 (Chức năng bảo mật & Xử lý lỗi)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **4. 보안 기능 및 에러 처리 (Chức năng bảo mật & Xử lý lỗi)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

보안, 기능, 에러, 처리

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **⦁ 보안 취약점 및 보안 기능 (Lỗ hổng bảo mật & Chức năng bảo mật)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **9. 암호화 기술 (Công nghệ Mã hóa)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **4. 보안 기능 및 에러 처리 (Chức năng bảo mật & Xử lý lỗi)** và nối nó với **9. 암호화 기술 (Công nghệ Mã hóa)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 4. 보안 기능 및 에러 처리 (Chức năng bảo mật & Xử lý lỗi)
- **적절한 인증 없이 중요기능 허용 (Missing Authentication)**: 중대한 기능에 재인증이 없음. (Không yêu cầu xác thực lại khi làm việc quan trọng).
- **중요정보 평문 저장 및 전송 (Plaintext Storage/Transmission)**: 패스워드를 암호화 없이 저장/전송. (Lưu hoặc truyền mật khẩu không mã hóa).
- **하드코드된 비밀번호 (Hardcoded Password)**: 소스코드에 비밀번호를 직접 작성. (Ghi cứng mật khẩu trong source code).
- **오류 메시지 통한 정보 노출 (Information Exposure Through Error Message)**: 시스템 내부 구조나 파일 경로가 오류 메시지에 포함되어 노출됨. (Thông báo lỗi làm lộ đường dẫn nội mục hệ thống).
- **예시 (Example)**:
  - (KR) DB 연결 실패 시 "gốc (root / 루트) 계정 연결 실패" 같은 메시지를 띄우지 않고 "일시적인 오류입니다"로 대체.
  - (VN) Thay vì hiện lỗi "Không kết nối được tài khoản gốc (root / 루트)", chỉ hiển thị "Lỗi hệ thống tạm thời".

---
