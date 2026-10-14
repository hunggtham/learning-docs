# Python 제어문 (Control Statements): if문, for문

## Python 제어문 (Control Statements): if문, for문

### 1. if문 (if Statement / Câu lệnh điều kiện)
Phần “1. if문 (if Statement / Câu lệnh điều kiện)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **형식**:
  ```python
  if 조건:
      실행할 문장
  ```
- 조건 뒤에 콜론(`:`)을 붙이고, 실행할 문장은 반드시 여백(Indentation)을 주어야 합니다.

### 2. for문 (for Statement / Vòng lặp for)
Phần “2. for문 (for Statement / Vòng lặp for)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **형식 1 (range 이용)**:
  ```python
  for 변수 in range(초기값, 최종값, 증가값):
      실행할 문장
  ```
  - `최종값` - 1 까지 반복합니다.
- **형식 2 (리스트 이용)**:
  ```python
  for 변수 in 리스트:
      실행할 문장
  ```

> **Vietnamese Explanation**:
> `if` dùng để rẽ nhánh điều kiện. `for` dùng để lặp. Hàm `range(start, end, step)` sinh ra một dãy số từ `start` tới `end-1` với khoảng cách là `step`.

**예시 / Ví dụ:**
```python
# Tính tổng các số từ 1 đến 4
sum = 0
for i in range(1, 5):
    sum += i
print(sum) # Output: 10 (1+2+3+4)
```
