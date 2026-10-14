# Python 데이터 입·출력 함수 (Python Input/Output Functions)

## Python 데이터 입·출력 함수 (Python Input/Output Functions)

### 1. input( ) 함수
Phần “1. input( ) 함수” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- Python의 표준 입력 함수로, 키보드로 입력받아 변수에 문자열(String) 형태로 저장합니다.
- **형식**: `변수 = input('출력문자')`

### 2. print( ) 함수
Phần “2. print( ) 함수” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **형식**: `print(출력값1, 출력값2, ..., sep='분리문자', end='종료문자')`
  - `sep`: 여러 값을 출력할 때 값 사이를 구분하는 문자 (기본값: 공백 한 칸)
  - `end`: 맨 마지막에 표시할 문자 (기본값: 줄 바꿈 `\n`)

> **Vietnamese Explanation**:
> Hàm `input()` dùng để nhận dữ liệu nhập từ bàn phím (mặc định luôn là chuỗi string). Hàm `print()` dùng để in ra màn hình, có thể tùy chỉnh dấu ngăn cách giữa các giá trị `sep` và ký tự kết thúc `end`.

**예시 / Ví dụ:**
```python
print(82, 24, sep='-', end=',')
# 출력/Output: 82-24,
```
