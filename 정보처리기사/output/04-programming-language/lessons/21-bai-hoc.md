# 배열과 포인터 심화 (Arrays & Pointers - Advanced)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **배열과 포인터 심화 (Arrays & Pointers - Advanced)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

배열과, 포인터, 심화

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 배열과 포인터 심화 (Arrays & Pointers - Advanced)
### 260. 배열의 초기화 (Array Initialization / Khởi tạo mảng)
- 배열 선언 시 초기값을 지정할 수 있다. (Có thể gán giá trị khởi tạo ngay khi khai báo mảng).
- 배열의 크기를 생략하려면 반드시 초기값을 지정해야 한다. (Nếu bỏ trống kích thước mảng trong ngoặc `[]`, bắt buộc phải có giá trị khởi tạo để máy tự đếm).
- 적은 수로 초기화하면 나머지 요소는 0이 입력된다. (Nếu khởi tạo ít phần tử hơn kích thước mảng, các phần tử còn lại tự động bằng 0).
  - *Example / Ví dụ*: `int a[5] = {3};` -> `[3, 0, 0, 0, 0]`.
  - 💡 *Mẹo ghi nhớ*: C/Java không tự làm sạch bộ nhớ trừ khi bạn khởi tạo ít nhất 1 phần tử.

### 261. 배열 형태의 문자열 변수 (String as Array / Chuỗi dưới dạng mảng - Bổ sung)
- 배열에 문자열을 저장할 때는 초기값으로 지정해야 하며, 이미 선언된 배열에는 대입 연산자로 문자열을 통째로 저장할 수 없다. (Chỉ được gán chuỗi trực tiếp lúc khởi tạo. Không được gán chuỗi vào mảng đã khai báo bằng dấu `=`).
- `%s`를 이용해 문자열을 출력할 때는 배열 이름이나 포인터 변수만 적어주면 된다. (Khi in chuỗi bằng `%s`, chỉ cần truyền tên mảng hoặc con trỏ, không cần dấu `&`).

### 262. 포인터와 포인터 변수 (Pointer & Pointer Variable / Con trỏ - Bổ sung)
- 포인터 변수는 동적으로 할당되는 메모리 영역인 **힙(Heap) 영역**에 접근하는 동적 변수이다. (Con trỏ là biến động truy cập vào vùng nhớ Heap được cấp phát động).
- `*` 연산자: 간접 연산자 (Lấy giá trị).
- `&` 연산자: 번지 연산자 (Lấy địa chỉ).
  - 💡 *Mẹo ghi nhớ*: Con trỏ giống như tấm bản đồ (chỉ chứa địa chỉ), dùng `*` để đi đến đích và lấy kho báu (giá trị).

### 263. 포인터와 배열 (Pointer & Array / Con trỏ và mảng - Bổ sung)
- `p + 1`은 메모리 주소가 1 증가하는 것이 아니라 해당 자료형의 크기(int는 4Byte)만큼 증가한다. (`p + 1` không cộng thêm 1 vào địa chỉ, mà cộng thêm kích thước của kiểu dữ liệu, ví dụ int thì cộng thêm 4 Bytes).
  - *Example / Ví dụ*: `p` là `1000` -> `p + 1` là `1004` (với int).
