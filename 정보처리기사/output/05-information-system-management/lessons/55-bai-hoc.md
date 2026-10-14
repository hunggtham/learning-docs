# 라이브러리 및 예외 처리 (Libraries and Exception Handling)

## 라이브러리 및 예외 처리 (Libraries and Exception Handling)

### 1. 라이브러리 (Library)
Phần “1. 라이브러리 (Library)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 자주 사용하는 함수나 데이터들을 미리 만들어 모아 놓은 집합체 (표준 라이브러리, 외부 라이브러리).
- **C언어 대표 표준 라이브러리**:
  - `stdio.h`: 입출력 (`printf`, `scanf`)
  - `math.h`: 수학 함수 (`sqrt`, `pow`)
  - `string.h`: 문자열 처리 (`strlen`, `strcpy`)
  - `stdlib.h`: 자료형 변환, 메모리 할당, 난수 (`atoi`, `malloc`, `rand`)
  - `time.h`: 시간 처리 (`time`)

### 2. 예외 처리 (Exception Handling)
Phần “2. 예외 처리 (Exception Handling)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 프로그램의 정상적인 실행을 방해하는 조건이나 상태를 예외(Exception)라고 합니다.
- 예외 발생 시 비정상 종료를 막고 대비해 놓은 처리 루틴을 수행하는 것을 의미합니다.

> **Vietnamese Explanation**:
> Thư viện (Library) là nơi chứa các hàm viết sẵn để bạn gọi ra dùng (ví dụ nhập xuất, toán học). Xử lý ngoại lệ (Exception Handling) là việc bắt các lỗi có thể xảy ra trong lúc chạy (như chia cho 0, mất kết nối) để chương trình không bị sập ngang.
