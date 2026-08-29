# Python 기본 문법 (Python Basic Syntax)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **Python 기본 문법 (Python Basic Syntax)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

Python, 기본, 문법

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## Python 기본 문법 (Python Basic Syntax)
### 264. Python의 기본 문법 (Python Basic Syntax / Cú pháp cơ bản của Python)
- **자료형 선언 없음**: 변수 선언 시 타입을 명시하지 않는다. (Không cần khai báo kiểu dữ liệu).
- **세미콜론 생략**: 문장 끝에 `;`이 필요 없다. (Không cần dấu chấm phẩy ở cuối câu).
- **연속 할당**: `x, y, z = 10, 20, 30` (Có thể gán liên tiếp nhiều biến).
- **코드 블록**: 콜론(`:`)과 여백(Indentation)으로 구분한다. (Dùng dấu hai chấm và thụt lề để xác định khối lệnh, thay vì dùng `{ }`).
  - 💡 *Mẹo ghi nhớ*: Python yêu cầu thụt lề (thường là 4 spaces) vô cùng khắt khe. Sai thụt lề = Lỗi (IndentationError).

### 265 ~ 269. Python 입출력, 리스트, 딕셔너리, 슬라이스 (Python I/O, List, Dict, Slice - Ôn tập)
*(Các khái niệm này đã được đề cập kỹ ở phần trước, dưới đây là tóm tắt nhanh các điểm chú ý)*:
- **`input()`**: Luôn trả về chuỗi. Dùng `int(input())` để ép kiểu. Đa trị: `map(int, input().split())`.
- **`print()`**: Có thể dùng `sep` (ký tự phân tách) và `end` (ký tự kết thúc).
- **리스트 (List)**: Khai báo bằng `[]` hoặc `list()`. Hỗ trợ chứa nhiều kiểu dữ liệu hỗn hợp.
- **딕셔너리 (Dictionary)**: Khai báo bằng `{}` hoặc `dict()`. Cấu trúc Key:Value.
- **슬라이스 (Slice)**: Cắt `[start:stop:step]`. Nếu bỏ trống `start` thì lấy từ đầu, bỏ trống `stop` thì lấy đến cuối.
