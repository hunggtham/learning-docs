# 핵심 258, 259, 260: 배열 (Array)

## 핵심 258, 259, 260: 배열 (Array)
Phần “핵심 258, 259, 260: 배열 (Array)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개념**: 동일한 자료형의 여러 변수를 연속된 메모리 공간에 묶어서 하나의 이름으로 관리. (Mảng: Tập hợp các biến cùng kiểu).
- **특징**:
  - C언어에서 인덱스(첨자)는 **0부터 시작**. (Chỉ số bắt đầu từ 0).
  - 1차원 배열: `int a[5];` (Mảng 1 chiều).
  - 2차원 배열: `int a[3][4];` (행(Row)과 열(Column)로 구성 / Mảng 2 chiều: Dòng và Cột).
- **초기화**:
  - `int a[3] = {1, 2, 3};`
  - 지정한 요소 개수보다 초기값이 적으면 나머지는 **0으로 채워짐**. (Nếu khai báo thiếu giá trị, các phần tử còn lại tự động bằng 0).
