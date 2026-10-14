# 포인터와 배열 (Pointer and Array)

## 포인터와 배열 (Pointer and Array)
Phần “포인터와 배열 (Pointer and Array)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개념**: C언어에서 배열을 포인터(Pointer/Con trỏ) 변수에 저장한 후 포인터를 이용해 배열의 요소에 접근할 수 있습니다.
- **특징**:
  - 배열 위치를 나타내는 첨자를 생략하고 배열의 대표명만 지정하면 배열의 첫 번째 요소의 주소를 지정하는 것과 같습니다. (예: `b = a;` 는 `b = &a[0];` 와 동일)
  - 배열 요소에 대한 주소를 지정할 때는 일반 변수와 동일하게 `&` 연산자를 사용합니다.
  - 배열의 요소가 포인터인 포인터형 배열을 선언할 수 있습니다.
  - 포인터 값에 정수를 더하면, 포인터가 가리키는 자료형의 크기(예: 정수형은 4바이트)만큼 물리적 주소가 증가합니다. (예: `p+1`은 4바이트 뒤의 주소)

> **Vietnamese Explanation**:
> Trong C, tên của mảng (array) chính là con trỏ (pointer) trỏ đến phần tử đầu tiên của mảng đó. Bạn có thể gán mảng cho một biến con trỏ, từ đó dùng con trỏ để truy cập các phần tử thay vì dùng chỉ số (index). Khi cộng 1 vào con trỏ, địa chỉ bộ nhớ sẽ tăng thêm số byte tương ứng với kiểu dữ liệu của nó (ví dụ int tăng 4 byte).

**예시 / Ví dụ:**
```c
int a[5] = {10, 11, 12, 13, 14};
int *p = a; // p trỏ tới a[0]
printf("%d", *(p+1)); // 출력/Output: 11
```

💡 **Mẹo ghi nhớ (Mnemonics):**
**Tên mảng = Địa chỉ đầu**. Mảng không cần `&` khi trỏ vào, nhưng phần tử thì cần (ví dụ `&a[0]`).
