# Python 클래스와 함수 (Class and Functions)

## Python 클래스와 함수 (Class and Functions)

### 1. 객체 생성 및 메소드 (Objects and Methods)
Phần “1. 객체 생성 및 메소드 (Objects and Methods)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **클래스 기반 객체 생성**: `변수명 = 클래스명()`
  - 예: `a = Cls()` (Cls 클래스의 객체 a를 생성)
  - 객체의 속성(변수)이나 메소드(함수)에 접근할 때는 마침표(`.`)를 사용합니다. (예: `a.x`, `a.chg()`)
- **함수 (클래스 없는 메소드)**: C언어의 함수처럼 클래스 없이 독립적으로 `def`를 이용해 메소드를 선언하고 사용할 수 있습니다.

> **Vietnamese Explanation**:
> Bạn có thể tạo đối tượng (object) từ một class bằng cú pháp `tên_biến = TênClass()`. Để truy cập biến hay hàm bên trong, ta dùng dấu chấm `.`. Ngoài ra, Python cũng cho phép định nghĩa các hàm độc lập không cần nằm trong class bằng từ khóa `def`.

**예시 / Ví dụ:**
```python
# Hàm độc lập (Function)
def calc(x, y):
    return x * y

a = calc(3, 4) # a = 12
```
