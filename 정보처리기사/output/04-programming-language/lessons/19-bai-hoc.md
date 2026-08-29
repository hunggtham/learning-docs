# 구조체, 배열 및 포인터 (Structs, Arrays, and Pointers)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **구조체, 배열 및 포인터 (Structs, Arrays, and Pointers)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

구조체, 배열, 포인터

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 구조체, 배열 및 포인터 (Structs, Arrays, and Pointers)
### C언어의 구조체 (Struct in C / Cấu trúc trong C)
- 자료의 종류가 다른 변수의 모임이다. (Tập hợp các biến có kiểu dữ liệu khác nhau).
- 예약어 `struct`를 이용해 정의한다. (Định nghĩa bằng từ khóa `struct`).
  - *Example / Ví dụ*: `struct Person { char name[20]; int age; };`
  - 💡 *Mẹo ghi nhớ*: Mảng (Array) lưu các giá trị cùng kiểu, Cấu trúc (Struct) lưu các giá trị khác kiểu.

### 177. 1차원 배열 (1D Array / Mảng 1 chiều)
- 변수들을 일직선상의 개념으로 조합한 배열이다. (Tập hợp các biến trên một đường thẳng).
  - *Example / Ví dụ*: `char a[3] = {'A', 'B', 'C'};`
  - 💡 *Mẹo ghi nhớ*: Chỉ số mảng luôn bắt đầu từ 0.

### 178. 2차원 배열 (2D Array / Mảng 2 chiều)
- 변수들을 평면, 즉 행과 열로 조합한 배열이다. (Tập hợp các biến theo dạng bảng gồm hàng và cột).
  - *Example / Ví dụ*: `int b[2][3] = {{11, 22, 33}, {44, 55, 66}};`
  - 💡 *Mẹo ghi nhớ*: `[hàng][cột]` (Row x Column).

### 179. 배열 형태의 문자열 변수 (String as Array / Chuỗi dưới dạng mảng)
- C언어에서는 큰따옴표("")로 묶인 글자는 문자열로 처리된다. (Trong C, chữ nằm trong ngoặc kép được xem là chuỗi).
- 배열에 문자열을 저장하면 널 문자('\0')가 문자열 끝에 자동으로 삽입된다. (Khi lưu chuỗi vào mảng, ký tự null `\0` tự động được thêm vào cuối).
  - *Example / Ví dụ*: `char a[5] = "love";` (Bao gồm l, o, v, e, \0).
  - 💡 *Mẹo ghi nhớ*: Độ dài mảng phải lớn hơn số ký tự của chuỗi ít nhất 1 (để chứa `\0`).

### 180. 포인터와 포인터 변수 (Pointers / Con trỏ)
- 포인터 변수를 선언할 때는 자료형 뒤에 `*`를 붙인다. (Khai báo biến con trỏ bằng dấu `*`).
- 변수의 주소를 알아낼 때는 `&`를 붙인다. (Lấy địa chỉ của biến bằng dấu `&`).
- 실행문에서 포인터 변수에 `*`를 붙이면 해당 변수가 가리키는 곳의 값을 의미한다. (Dùng `*` trước con trỏ để lấy giá trị tại địa chỉ đó).
  - *Example / Ví dụ*: `int a = 50; int *b = &a; printf("%d", *b);` (In ra 50).
  - 💡 *Mẹo ghi nhớ*: `&` là địa chỉ (Address), `*` là giá trị (Value).

### 181. 포인터와 배열 (Pointer and Array / Con trỏ và mảng)
- 배열을 포인터 변수에 저장한 후 포인터를 이용해 배열의 요소에 접근할 수 있다. (Có thể dùng con trỏ để truy cập các phần tử mảng).
- 배열의 대표명은 배열의 첫 번째 요소의 주소와 같다. (Tên mảng chính là địa chỉ của phần tử đầu tiên).
  - *Example / Ví dụ*: `int a[5]; int *b = a;` tương đương với `b = &a[0];`.
  - 💡 *Mẹo ghi nhớ*: `a[i]` hoàn toàn tương đương với `*(a + i)`.
