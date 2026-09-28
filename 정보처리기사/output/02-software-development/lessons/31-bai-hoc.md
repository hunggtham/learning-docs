# 099: 소프트웨어 패키징 (Software Packaging)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **099: 소프트웨어 패키징 (Software Packaging)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

소프트웨어, 패키징

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **핵심 035 & 036: 소프트웨어 패키징 및 DRM (Software Packaging & DRM)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **100 & 100-1: 패키징 시 고려사항 및 순서 (Packaging Considerations & Sequence)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **099: 소프트웨어 패키징 (Software Packaging)** và nối nó với **100 & 100-1: 패키징 시 고려사항 및 순서 (Packaging Considerations & Sequence)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 099: 소프트웨어 패키징 (Software Packaging)

- 실행 파일들을 묶어 배포용 설치 파일을 만드는 과정. (Gom tất cả file thực thi, file hình, file cấu hình thành 1 file cài đặt (Setup.exe) để tung ra thị trường).
- **Nguyên tắc:**
  - **사용자 중심 (Hướng tới người dùng):** Người dùng cài đặt dễ dàng, không cần biết mã (code / 코드).
  - Cần phải 모듈화 (Module hóa) để dễ bảo trì, và tích hợp 보안 (Bảo mật / DRM).
