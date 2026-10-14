# 입력 값의 형변환 (Type Casting)

## 입력 값의 형변환 (Type Casting)
Phần “입력 값의 형변환 (Type Casting)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `input()` 함수는 입력되는 값을 무조건 문자열(String)로 저장하므로, 숫자로 사용하기 위해서는 형(Type)을 변환해야 합니다.
- **변환할 데이터가 1개일 때**: `int()`, `float()` 사용
- **변환할 데이터가 2개 이상일 때**: `map()`과 `split()` 사용
  - 형식: `변수1, 변수2 = map(int, input().split())`

> **Vietnamese Explanation**:
> Vì `input()` trả về chuỗi, bạn phải ép kiểu sang số thực (`float`) hoặc số nguyên (`int`). Để nhập nhiều số cùng lúc trên một dòng, dùng `split()` để tách chuỗi và `map()` để ép kiểu hàng loạt cho tất cả các phần tử.

**예시 / Ví dụ:**
```python
a, b = map(int, input("Nhập 2 số: ").split())
# Nếu nhập "10 20", a=10, b=20
```

💡 **Mẹo ghi nhớ (Mnemonics):**
**M.I.S** - **M**ap **I**nt **S**plit để nhập nhiều số nguyên cùng lúc.
