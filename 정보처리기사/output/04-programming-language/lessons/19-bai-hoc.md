# 배열 심화 (Arrays - Advanced)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **배열 심화 (Arrays - Advanced)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

배열, 심화

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 배열 심화 (Arrays - Advanced)
### 258. 배열과 1차원 배열 (Array & 1D Array / Mảng 1 chiều - Bổ sung)
- 배열은 행 우선으로 데이터가 할당된다. (Mảng được cấp phát theo thứ tự ưu tiên hàng).
- 첨자 없이 배열 이름을 사용하면 첫 번째 요소의 주소를 지정하는 것과 같다. (Tên mảng không có chỉ số chính là địa chỉ phần tử đầu tiên).
  - *Example / Ví dụ*: Khởi tạo mảng bằng `for` loop: `for(i=0; i<5; i++) a[i] = i+10;`
  - 💡 *Mẹo ghi nhớ*: Mảng trong C/Java đếm từ 0.

### 259. 2차원 배열 (2D Array / Mảng 2 chiều - Bổ sung)
- 변수들을 평면, 즉 행과 열로 조합한 배열. (Mảng kết hợp hàng và cột).
- 형식: `자료형 변수명[행개수][열개수]`
  - *Example / Ví dụ*: `int b[3][3];` (Mảng 3 hàng, 3 cột. Chỉ số hàng 0-2, cột 0-2).
  - Sử dụng vòng lặp lồng nhau (Nested loops) để gán giá trị: `for(i=0; i<3; i++) { for(j=0; j<4; j++) { a[i][j] = ++k; } }`
  - 💡 *Mẹo ghi nhớ*: Array 2D giống như ma trận Toán học. `i` là hàng (bên ngoài), `j` là cột (bên trong).
