## 포인터와 배열 (Pointer and Array)
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


## Python의 기본 문법 (Python Basic Syntax)
- **특징**:
  - 변수의 자료형(Data Type/Kiểu dữ liệu)에 대한 선언이 없습니다.
  - 문장의 끝을 의미하는 세미콜론(`;`)을 사용할 필요가 없습니다.
  - 변수에 연속하여 값을 저장하는 것이 가능합니다. (예: `x, y, z = 10, 20, 30`)
  - `if`나 `for`와 같이 코드 블록(Code Block/Khối lệnh)을 포함하는 명령문을 작성할 때, 콜론(`:`)과 여백(Indentation/Thụt lề)으로 구분합니다.
  - 여백은 일반적으로 4칸 또는 한 개의 탭(Tab)만큼 띄워야 하며, 같은 수준의 코드들은 반드시 동일한 여백을 가져야 합니다.

> **Vietnamese Explanation**: 
> Khác với C hay Java, Python không cần khai báo kiểu dữ liệu cho biến, không cần dấu chấm phẩy `;` ở cuối dòng. Python dùng khoảng trắng (thụt lề) để phân chia các khối lệnh thay vì dùng dấu ngoặc nhọn `{}`.

**예시 / Ví dụ:**
```python
x, y = 10, 20
if x < y:
    print("x is smaller") # Thụt lề 4 khoảng trắng
```

💡 **Mẹo ghi nhớ (Mnemonics):** 
**P.I.T** - **P**ython **I**ndents **T**hings (Python thụt lề mọi thứ).


## Python 데이터 입·출력 함수 (Python Input/Output Functions)

### 1. input( ) 함수
- Python의 표준 입력 함수로, 키보드로 입력받아 변수에 문자열(String) 형태로 저장합니다.
- **형식**: `변수 = input('출력문자')`

### 2. print( ) 함수
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


## 입력 값의 형변환 (Type Casting)
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


## Python 자료구조 (Data Structures): 리스트(List)와 딕셔너리(Dictionary)

### 1. 리스트 (List / Danh sách)
- C/Java의 배열(Array)과 달리 크기를 지정하지 않으며, 정수/실수/문자열 등 다양한 자료형을 섞어서 저장할 수 있습니다.
- 위치(Index)는 0부터 시작합니다.
- **형식**: `리스트명 = [값1, 값2, ...]` 또는 `list([값1, 값2, ...])`

### 2. 딕셔너리 (Dictionary / Từ điển)
- 연관된 값을 묶어서 저장하는 용도로, 인덱스 대신 사용자가 원하는 값을 키(Key)로 지정해 사용합니다. 키-값 쌍(Key-Value pairs) 형태로 저장합니다.
- **형식**: `딕셔너리명 = {키1:값1, 키2:값2, ...}` 또는 `dict(...)`

> **Vietnamese Explanation**: 
> List giống như Array nhưng linh hoạt hơn nhiều (có thể chứa nhiều kiểu dữ liệu cùng lúc, tự động thay đổi kích thước). Dictionary lưu dữ liệu theo dạng Cặp Chìa khóa - Giá trị (Key-Value), cho phép tra cứu nhanh theo Key.

**예시 / Ví dụ:**
```python
# List
my_list = [10, "mike", 23.45]
# Dictionary
my_dict = {"이름": "홍길동", "나이": 25}
my_dict["주소"] = "서울" # Thêm phần tử
```

💡 **Mẹo ghi nhớ (Mnemonics):** 
- **List**: Ngoặc vuông `[]` (Ví dụ: cái hộp hình vuông chứa đủ đồ).
- **Dict**: Ngoặc nhọn `{}` (Có dạng `Key: Value`).


## 슬라이스 (Slice)
- **개념**: 문자열이나 리스트와 같은 순차형 객체에서 일부를 잘라(Slicing) 반환하는 기능입니다.
- **형식**: `객체명[초기위치:최종위치:증가값]`
  - `초기위치`에서 `최종위치 - 1` 까지의 요소들을 가져옵니다.
  - 인수를 생략하면 전체를 의미하거나, 기본값(처음, 끝, 1씩 증가)이 적용됩니다.

> **Vietnamese Explanation**: 
> Slice (cắt lát) giúp lấy ra một phần của List hoặc String một cách dễ dàng. Nhớ là vị trí kết thúc không bao giờ được bao gồm (chỉ lấy đến `cuối - 1`).

**예시 / Ví dụ:**
```python
a = ['a', 'b', 'c', 'd', 'e']
print(a[1:3])    # ['b', 'c']
print(a[0:5:2])  # ['a', 'c', 'e'] (Lấy cách nhau 2 bước)
print(a[::-1])   # Lật ngược list (âm là đi lùi)
```


## Python 제어문 (Control Statements): if문, for문

### 1. if문 (if Statement / Câu lệnh điều kiện)
- **형식**:
  ```python
  if 조건:
      실행할 문장
  ```
- 조건 뒤에 콜론(`:`)을 붙이고, 실행할 문장은 반드시 여백(Indentation)을 주어야 합니다.

### 2. for문 (for Statement / Vòng lặp for)
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


## Python 클래스 (Class) - 기초 (Cơ bản)
- **정의 형식**:
  ```python
  class 클래스명:
      def 메소드명(self, 인수):
          실행할 문장
          return 값
  ```
- `def`는 메소드(Method/Phương thức)를 정의하는 예약어입니다.
- `self`는 메소드에서 자기 클래스에 속한 변수에 접근할 때 사용하는 명칭으로 첫 번째 인수로 반드시 작성합니다.

> **Vietnamese Explanation**: 
> Class là khuôn mẫu để tạo ra các đối tượng (Objects). Hàm định nghĩa bên trong class được gọi là method (phương thức) và luôn phải có tham số `self` đại diện cho chính đối tượng đó.

## Python 클래스와 함수 (Class and Functions)

### 1. 객체 생성 및 메소드 (Objects and Methods)
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


## Python 제어문: while문 (While Loop)
- **형식**:
  ```python
  while 조건:
      실행할 문장
  ```
- 조건이 참(True)인 동안 실행할 문장을 반복 수행합니다.

**예시 / Ví dụ:**
```python
i = 0
while i < 5:
    i += 1
```


## 프로그래밍 언어의 분류 (Classification of Programming Languages)

### 1. 절차적 프로그래밍 언어 (Procedural)
- **C**: UNIX의 일부를 구현한 언어. 시스템 프로그래밍에 적합하며 포인터(Pointer) 제공.
- **ALGOL**: 과학 기술 계산용. PASCAL과 C의 모체.
- **COBOL**: 사무 처리용. 영어 문장 형식 (4개의 DIVISION).
- **FORTRAN**: 수학과 공학 등 과학 기술 계산용.

### 2. 객체지향 프로그래밍 언어 (Object-Oriented)
- **JAVA**: 분산 네트워크 환경 적합, 멀티스레드(Multi-thread) 지원, 이식성 강함.
- **C++**: C언어에 객체지향 개념을 추가.
- **Smalltalk**: 1세대 순수 객체지향 언어로, 최초로 GUI를 제공.

### 3. 스크립트 언어 (Scripting)
- **클라이언트 측 (Client-side)**:
  - **JavaScript**: 웹 페이지 동작 제어.
  - **VBScript**: Microsoft 애플리케이션 제어 (Active X).
- **서버 측 (Server-side)**:
  - **ASP**: Microsoft 제작, Windows 전용.
  - **JSP**: Java 기반, 다양한 운영체제 지원.
  - **PHP**: C/Java와 유사한 문법, Linux/Unix/Windows 등 다양하게 지원.
- **기타**: Python(대화형 인터프리터, 플랫폼 독립적), Shell Script(유닉스/리눅스 명령어 조합).

### 4. 선언형 프로그래밍 언어 (Declarative)
- **HTML**: 하이퍼텍스트 웹 표준 문서 생성.
- **LISP**: 인공지능 분야. 연결 리스트(Linked List) 및 재귀(Recursion) 호출 사용.
- **PROLOG**: 논리학 기초, 인공지능 논리 추론.
- **XML**: HTML 단점 보완, 태그(Tag) 사용자 정의 가능.
- **Haskell**: 함수형 언어로 부작용(Side Effect)이 없음.

💡 **Mẹo ghi nhớ (Mnemonics):** 
- **C.A.C.F** = Các ngôn ngữ thủ tục (C, Algol, Cobol, Fortran).
- **J.A.P** = Các ngôn ngữ kịch bản Server-side (JSP, ASP, PHP).


## 라이브러리 및 예외 처리 (Libraries and Exception Handling)

### 1. 라이브러리 (Library)
- 자주 사용하는 함수나 데이터들을 미리 만들어 모아 놓은 집합체 (표준 라이브러리, 외부 라이브러리).
- **C언어 대표 표준 라이브러리**:
  - `stdio.h`: 입출력 (`printf`, `scanf`)
  - `math.h`: 수학 함수 (`sqrt`, `pow`)
  - `string.h`: 문자열 처리 (`strlen`, `strcpy`)
  - `stdlib.h`: 자료형 변환, 메모리 할당, 난수 (`atoi`, `malloc`, `rand`)
  - `time.h`: 시간 처리 (`time`)

### 2. 예외 처리 (Exception Handling)
- 프로그램의 정상적인 실행을 방해하는 조건이나 상태를 예외(Exception)라고 합니다.
- 예외 발생 시 비정상 종료를 막고 대비해 놓은 처리 루틴을 수행하는 것을 의미합니다.

> **Vietnamese Explanation**: 
> Thư viện (Library) là nơi chứa các hàm viết sẵn để bạn gọi ra dùng (ví dụ nhập xuất, toán học). Xử lý ngoại lệ (Exception Handling) là việc bắt các lỗi có thể xảy ra trong lúc chạy (như chia cho 0, mất kết nối) để chương trình không bị sập ngang.


## 운영체제 (OS: Operating System) 기초

### 1. 정의 및 목적
- 하드웨어를 제어하고 사용자가 편리하게 컴퓨터를 사용할 수 있도록 돕는 시스템 소프트웨어.
- **성능 평가 4가지 기준**:
  1. **처리 능력 (Throughput)**: 일정 시간 내에 시스템이 처리하는 일의 양. (높을수록 좋음)
  2. **반환 시간 (Turn Around Time)**: 작업 의뢰부터 완료될 때까지 걸린 시간. (짧을수록 좋음)
  3. **사용 가능도 (Availability)**: 시스템을 필요할 때 즉시 사용할 수 있는 정도. (높을수록 좋음)
  4. **신뢰도 (Reliability)**: 시스템이 문제를 정확하게 해결하는 정도. (높을수록 좋음)

### 2. 운영체제의 구성
- **제어 프로그램 (Control Program)**:
  - 감시 프로그램 (Supervisor): 자원 할당 및 작동 감시 (가장 핵심).
  - 작업 관리 (Job Management): 작업 순서 및 방법 관리.
  - 데이터 관리 (Data Management): 데이터/파일 처리 관리.
- **처리 프로그램 (Processing Program)**:
  - 언어 번역 프로그램 (컴파일러, 어셈블러 등).
  - 서비스 프로그램 (유틸리티 등).

💡 **Mẹo ghi nhớ (Mnemonics):** 
- **Hiệu suất OS**: T.T.A.R (Throughput - Turnaround - Availability - Reliability).
- **Chương trình điều khiển**: Giám sát (Supervisor) - Công việc (Job) - Dữ liệu (Data).


## Windows와 UNIX 운영체제 (Windows & UNIX)

### 1. Windows 주요 특징
- **GUI (Graphic User Interface)**: 마우스 기반 그래픽 환경.
- **선점형 멀티태스킹 (Preemptive Multi-Tasking)**: 응용 프로그램 문제 시 OS가 강제 종료시켜 자원 반환.
- **PnP (Plug and Play)**: 하드웨어 설치 시 OS가 자동 감지 및 환경 구성.
- **OLE (Object Linking and Embedding)**: 문자/그림 개체를 다른 문서에 연결하거나 삽입.
- **긴 파일명**: 최대 255자 지정 가능 (VFAT 이용).

### 2. UNIX 주요 특징
- 대화식 시분할 시스템 (Time Sharing System) 및 개방형 시스템 (Open System).
- 주로 **C언어**로 작성되어 이식성이 높고 파일 시스템은 트리(Tree) 구조를 가짐.
- **다중 사용자 (Multi-User)** 및 **다중 작업 (Multi-Tasking)** 지원.

### 3. 파일 디스크립터 (File Descriptor)
- 파일 제어 블록(FCB; File Control Block)이라고도 하며, 시스템(OS)이 필요로 하는 파일에 대한 정보를 가진 제어 블록.
- 파일마다 독립적으로 존재하며 보통 보조기억장치에 있다가 파일이 열릴(Open) 때 주기억장치로 옮겨집니다.

### 4. UNIX 시스템 구조: 커널 (Kernel)
- UNIX의 가장 **핵심적인 부분**. 프로그램과 하드웨어 간의 인터페이스 역할을 담당하며 프로세스, 메모리, 입출력 관리 등을 수행합니다.

> **Vietnamese Explanation**: 
> Windows nổi bật với giao diện chuột GUI, Plug and Play (cắm là chạy). UNIX là hệ điều hành mã nguồn mở, đa nhiệm, đa người dùng, chủ yếu viết bằng C. Trong UNIX, Kernel (nhân) là phần cốt lõi quản lý phần cứng và giao tiếp với phần mềm. File Descriptor lưu giữ thông tin quan trọng về các file đang được hệ thống quản lý.

## UNIX 주요 구성요소 (UNIX Components)

### 1. 쉘 (Shell)
- 사용자의 명령어를 인식하여 프로그램을 호출하고 명령을 수행하는 **명령어 해석기**입니다.
- 주기억장치에 상주하지 않고 명령어가 포함된 파일 형태로 존재합니다.
- 파이프라인 기능을 지원하며 입·출력 재지정(Redirection)이 가능합니다.
- 예: Bourne Shell, C Shell, Korn Shell 등

### 2. 유틸리티 프로그램 (Utility Program)
- 일반 사용자가 작성한 응용 프로그램을 처리하는 데 사용됩니다. (에디터, 컴파일러, 디버거 등)

> **Vietnamese Explanation**: 
> Shell trong UNIX đóng vai trò như người phiên dịch, nhận lệnh từ người dùng và giao cho hệ thống xử lý. Chương trình tiện ích (Utility) là các công cụ hỗ trợ người dùng như trình soạn thảo, trình biên dịch.


## 메모리 관리 (Memory Management)

### 1. 배치 전략 (Placement Strategy)
새로 반입되는 프로그램이나 데이터를 주기억장치의 어디에 위치시킬 것인지 결정합니다.
- **최초 적합 (First Fit)**: 빈 영역 중 첫 번째 분할 영역에 배치.
- **최적 적합 (Best Fit)**: 단편화(Fragmentation/Khoảng trống thừa)를 가장 작게 남기는 분할 영역에 배치.
- **최악 적합 (Worst Fit)**: 단편화를 가장 많이 남기는 분할 영역에 배치.

### 2. 가상기억장치 구현 기법 (Virtual Memory Techniques)
- **페이징(Paging) 기법**: 가상기억장치와 주기억장치를 **동일한 크기**로 나누어 적재. (프로그램 단위: 페이지, 주기억장치 단위: 페이지 프레임)
  - 외부 단편화는 발생하지 않으나, **내부 단편화**는 발생 가능.
- **세그먼테이션(Segmentation) 기법**: 프로그램을 배열이나 함수 등 **다양한 크기의 논리적인 단위(세그먼트)**로 나누어 적재.
  - 내부 단편화는 발생하지 않으나, **외부 단편화**는 발생 가능.

💡 **Mẹo ghi nhớ (Mnemonics):** 
- **Paging**: Bằng nhau (Page). Lỗi nội bộ (내부 단편화).
- **Segmentation**: Khác nhau (Theo logic). Lỗi bên ngoài (외부 단편화).


## 페이지 교체 알고리즘과 페이지 크기 (Page Replacement & Size)

### 1. 페이지 교체 알고리즘 (Page Replacement Algorithms)
페이지 부재(Page Fault) 발생 시, 어떤 페이지 프레임을 교체할 것인지 결정합니다.
- **OPT (Optimal)**: 앞으로 가장 오랫동안 사용하지 않을 페이지 교체 (가장 효율적이나 미래 예측이 필요해 비현실적).
- **FIFO (First In First Out)**: 가장 먼저 들어와서 가장 오래 있었던 페이지 교체.
- **LRU (Least Recently Used)**: 최근에 가장 오랫동안 사용하지 않은 페이지 교체 (계수기나 스택 사용).
- **LFU (Least Frequently Used)**: 사용 빈도(횟수)가 가장 적은 페이지 교체.
- **NUR (Not Used Recently)**: LRU의 오버헤드를 줄이기 위해 참조 비트와 변형 비트를 사용하여 최근 사용 안 된 페이지 교체.
- **SCR (Second Chance Replacement)**: FIFO의 단점을 보완하여 자주 사용되는 페이지는 한 번 더 기회를 줌.

### 2. 페이지 크기 (Page Size)
- **크기가 작을 경우**: 페이지 단편화 감소, 워킹 셋 효율 증가, Locality 일치로 기억장치 효율 상승. 단, 페이지 맵 테이블 크기가 커지고 매핑 속도가 느려지며 디스크 입출력 횟수가 증가.
- **크기가 클 경우**: 페이지 맵 테이블 크기 감소, 매핑 속도 상승, 디스크 입출력 횟수 감소. 단, 불필요한 내용까지 적재될 수 있고 페이지 단편화가 증가.


## 프로세스 동작 특성 (Process Behavior: Locality, Working Set, Thrashing)

### 1. Locality (국부성, 구역성)
프로세스 실행 중 일부 페이지만 집중적으로 참조하는 성질.
- **시간 구역성 (Temporal Locality)**: 하나의 페이지를 짧은 시간 동안 집중 참조 (반복문, 스택 등).
- **공간 구역성 (Spatial Locality)**: 특정 위치 주변의 페이지를 집중 참조 (배열, 순차적 코드 등).

### 2. 워킹 셋 (Working Set)
프로세스가 일정 시간 동안 자주 참조하는 페이지들의 집합. (시간에 따라 변함). 주기억장치에 상주시키면 페이지 부재 현상이 줄어듭니다.

### 3. 스래싱 (Thrashing)
프로세스 처리 시간보다 페이지 교체에 소요되는 시간이 더 많아져 시스템 성능이 급격히 저하되는 현상.
- **방지 방법**: 다중 프로그래밍 정도 조절, 페이지 부재 빈도 조절, 워킹 셋 유지 등.

> **Vietnamese Explanation**: 
> **Locality** là tính cục bộ (hay dùng lại chỗ vừa dùng). **Working Set** là tập hợp các trang bộ nhớ đang được dùng nhiều nhất, cần giữ lại ở RAM. **Thrashing** là hiện tượng "giậm chân tại chỗ", máy bận rộn tráo đổi dữ liệu với ổ cứng nhiều hơn là thực sự chạy chương trình, làm máy bị đơ.


## 프로세스와 스레드 (Process and Thread)

### 1. 프로세스 (Process)
- CPU에 의해 처리되는 실행 중인 프로그램 (작업/Job, 태스크/Task).
- **PCB(Process Control Block)**: 운영체제가 프로세스에 대한 중요한 정보를 저장하는 곳. (현재 상태, 포인터, 고유 식별자, 스케줄링 우선순위 등). 프로세스 생성 시 만들어지고 완료 시 제거됨.

### 2. 프로세스 상태 전이 (Process State Transition)
- **제출(Submit) -> 접수(Hold) -> 준비(Ready) -> 실행(Run) -> 대기(Wait/Block) -> 종료(Exit)**
- **주요 용어**:
  - **Dispatch (디스패치)**: 준비 상태 -> 실행 상태로 전이 (CPU 할당).
  - **Wake Up (웨이크 업)**: 입·출력 완료 후 대기 상태 -> 준비 상태로 전이.
  - **Spooling (스풀링)**: 디스크를 버퍼처럼 활용해 느린 입출력 장치와 CPU 간 속도 차이를 보완.

### 3. 스레드 (Thread)
- 프로세스 내에서의 작업 단위 (경량 프로세스/Light Weight Process).
- 동일 프로세스 환경에서 서로 독립적인 다중 수행이 가능하여 응답 시간을 단축하고 기억장소 낭비를 줄입니다.

> **Vietnamese Explanation**: 
> **Process** là một chương trình đang chạy. **Thread** là các luồng xử lý nhỏ nằm bên trong Process. Dùng nhiều thread giúp chương trình chạy nhanh hơn và chia sẻ bộ nhớ tốt hơn (ví dụ nhiều tab trên trình duyệt). **Dispatch** là hành động cấp CPU cho một tiến trình đang xếp hàng chờ.


## 주요 스케줄링 알고리즘 (Major Scheduling Algorithms)

### 1. FCFS (First Come First Service) / FIFO
준비 큐에 도착한 순서대로 CPU를 할당하는 기법 (선입선출). 구현은 가장 간단하나, 긴 작업이 먼저 오면 뒤의 짧은 작업이 오래 기다리게 됨.

### 2. SJF (Shortest Job First)
실행 시간이 가장 짧은 프로세스에게 먼저 CPU를 할당하는 기법. 가장 적은 평균 대기 시간을 제공하지만, 실행 시간이 긴 프로세스는 무한정 기다릴 수 있음.

### 3. HRN (Highest Response-ratio Next)
SJF의 단점(긴 작업 불리)을 보완하여 대기 시간과 실행 시간을 함께 고려함.
- **우선순위 계산식**: `(대기 시간 + 서비스 시간) / 서비스 시간`
- 결과값이 높은 것부터 우선순위를 부여함.

## UNIX/LINUX 환경 변수 및 기본 명령어 (UNIX Variables & Commands)

### 1. 주요 환경 변수 (Environment Variables)
환경 변수를 사용할 때는 변수명 앞에 `$`를 붙입니다.
- `$HOME`: 사용자의 홈 디렉터리
- `$PWD`: 현재 작업하는 디렉터리
- `$PATH`: 실행 파일을 찾는 경로
- `$USER`: 사용자의 이름

### 2. 기본 명령어 (Basic Commands)
- `cat`: 파일 내용 화면 표시
- `chmod`: 파일 보호 모드 설정 (사용 허가 지정)
- `chown`: 파일 소유자 변경
- `cp`: 파일 복사 / `rm`: 파일 삭제
- `find`: 파일 검색
- `fork`: 새로운 프로세스 생성 (프로세스 복제)
- `fsck`: 파일 시스템 검사 및 보수
- `ls`: 현재 디렉터리 내 파일 목록 확인

> **Vietnamese Explanation**: 
> Biến môi trường trong UNIX/LINUX giúp hệ thống biết các cài đặt mặc định (như đường dẫn `$PATH`, thư mục chủ `$HOME`). Các lệnh cơ bản như `chmod` dùng để phân quyền file, `fork` để nhân bản tiến trình.


## IP 주소 및 서브네팅 (IP Address & Subnetting)

### 1. IPv4 주소 (Internet Protocol version 4)
- 8비트씩 4부분, 총 **32비트**로 구성됩니다.
- 네트워크 크기에 따라 A~E 클래스로 나뉩니다.
  - **A Class**: 국가/대형 망 (0~127)
  - **B Class**: 중대형 망 (128~191)
  - **C Class**: 소규모 망 (192~223)
  - **D Class**: 멀티캐스트용 (224~239)
  - **E Class**: 실험적 주소

### 2. 서브네팅 (Subnetting)
할당된 네트워크 주소를 다시 여러 개의 작은 네트워크로 나누어 사용하는 기법입니다. (서브넷 마스크 활용).

### 3. IPv6 주소 (Internet Protocol version 6)
- IPv4의 주소 부족 문제를 해결하기 위해 개발되었습니다.
- 16비트씩 8부분, 총 **128비트**로 구성되며 콜론(`:`)으로 구분합니다.
- 인증성, 기밀성, 무결성을 지원하여 보안이 뛰어나고, 주소 확장성과 호환성이 좋습니다.
- **주소 체계**:
  - **유니캐스트 (Unicast)**: 1 대 1 통신
  - **멀티캐스트 (Multicast)**: 1 대 다 통신
  - **애니캐스트 (Anycast)**: 1 대 1 통신 (가장 가까운 수신자에게 전송)

💡 **Mẹo ghi nhớ (Mnemonics):** 
- **IPv4**: 32-bit (4 x 8).
- **IPv6**: 128-bit (8 x 16), **U.M.A** (Unicast, Multicast, Anycast).


## OSI 7계층 참조 모델 (OSI 7 Layer Reference Model)
국제표준화기구(ISO)에서 제안한 통신 규약으로, 하위 3계층과 상위 4계층으로 나뉩니다.
- **물리 계층 (Physical)**: 실제 접속, 기계적/전기적 특성 정의.
- **데이터 링크 계층 (Data Link)**: 인접 시스템 간 신뢰성 있는 전송, 흐름 제어, 오류 제어, 동기화.
- **네트워크 계층 (Network)**: 경로 설정(Routing), 트래픽 제어, 패킷 전송.
- **전송 계층 (Transport)**: 종단(End-to-End) 간 신뢰성 있는 데이터 전송, 연결 설정, 다중화.
- **세션 계층 (Session)**: 대화(회화) 제어, 동기 제어.
- **표현 계층 (Presentation)**: 데이터 형식 변환, 암호화, 압축.
- **응용 계층 (Application)**: 사용자에게 통신 서비스 제공.

> **Vietnamese Explanation**: 
> Mô hình OSI chia quá trình truyền mạng thành 7 lớp. 3 lớp dưới (Physical, Data Link, Network) lo việc truyền dẫn tín hiệu, tìm đường (routing). 4 lớp trên (Transport, Session, Presentation, Application) lo việc kiểm tra lỗi, mã hóa dữ liệu và giao tiếp với người dùng.


## 네트워크 관련 장비 (Network Equipment)
- **NIC (Network Interface Card)**: 컴퓨터와 네트워크 연결 (랜카드).
- **허브 (Hub)**: 여러 컴퓨터 연결 및 회선 통합 관리 (리피터 역할 포함).
- **리피터 (Repeater)**: 약해진 신호를 증폭/재생하여 다시 전송.
- **브리지 (Bridge)**: LAN과 LAN을 연결 (MAC 주소 기반).
- **스위치 (Switch)**: 브리지와 유사하나 하드웨어 기반으로 속도가 더 빠름.
- **라우터 (Router)**: 최적 경로(Routing) 선택, 서로 다른 네트워크 연결 (네트워크 계층).
- **게이트웨이 (Gateway)**: 프로토콜이 전혀 다른 네트워크들을 연결하는 출입구 역할 (전 계층).

💡 **Mẹo ghi nhớ (Mnemonics):** 
- **Repeater**: Tầng 1 (Khuếch đại tín hiệu).
- **Bridge/Switch**: Tầng 2 (Nối LAN).
- **Router**: Tầng 3 (Tìm đường IP).
- **Gateway**: Tầng 4-7 (Cổng nối các mạng khác biệt).


## 계층별 주요 프로토콜 (Major Protocols by Layer)

### 1. 응용 계층 (Application)
- **FTP**: 파일 전송 / **SMTP**: 이메일 송신 / **HTTP**: 웹 문서 송수신
- **TELNET**: 원격 접속 가상 터미널 / **DNS**: 도메인 네임을 IP 주소로 변환

### 2. 전송 계층 (Transport)
- **TCP**: 연결 지향, 양방향, 신뢰성 보장, 스트림 위주 전달, 흐름 및 순서 제어 기능 제공.
- **UDP**: 비연결형, 빠른 전송 속도 (실시간 전송 유리, 오버헤드 적음).

### 3. 인터넷 계층 (Internet / Network)
- **IP**: 데이터 주소 지정 및 경로 설정.
- **ICMP**: 제어 메시지 및 오류 처리 관리.
- **ARP**: IP 주소 -> MAC 주소 (물리적 주소)로 변환.
- **RARP**: MAC 주소 -> IP 주소로 변환.

### 4. 네트워크 액세스 계층 (Data Link & Physical)
- **Ethernet (IEEE 802.3)**, **HDLC**, **X.25**, **RS-232C** 등.


## 5과목 정보시스템 구축 관리 (Information System Construction Management)

### 소프트웨어 개발 방법론 (Software Development Methodologies)
- **구조적 방법론 (Structured)**: 처리(Process) 중심. 분할과 정복(Divide and Conquer) 원리 적용.
- **정보공학 방법론 (Information Engineering)**: 자료(Data) 중심. 대규모 정보 시스템 구축에 적합.
- **컴포넌트 기반 방법론 (CBD)**: 기존 컴포넌트를 조합하여 새로운 애플리케이션 생성. 재사용성(Reusability)과 확장성이 높고 유지보수 비용 최소화.

### 소프트웨어 재사용과 재공학 (Software Reuse & Reengineering)
- **소프트웨어 재사용 (Reuse)**: 이미 검증된 소프트웨어를 새로운 개발에 사용하여 개발 시간 및 비용 단축, 품질 향상.
- **소프트웨어 재공학 (Reengineering)**: 기존 시스템을 유지보수 관점에서 개조 및 개선하여 새로운 기능을 추가하고 성능을 높이는 기술 (예방 유지보수 측면).

> **Vietnamese Explanation**: 
> - **Methodologies**: Structured (Tập trung vào quá trình), Information Engineering (Tập trung vào dữ liệu), CBD (Lắp ráp từ các linh kiện có sẵn).
> - **Reuse**: Dùng lại code/module cũ cho dự án mới để tiết kiệm chi phí. 
> - **Reengineering**: Tái cấu trúc, cải tiến hệ thống cũ để dễ bảo trì và đáp ứng nhu cầu mới.

## 소프트웨어 재사용 및 재공학 활동 (Software Reuse & Reengineering Activities)

### 1. 재사용 방법 (Reuse Methods)
- **합성 중심 (Composition-Based)**: 소프트웨어 부품(블록)을 만들어 끼워 맞추어 완성시키는 방법. (블록 구성 방법)
- **생성 중심 (Generation-Based)**: 추상화 형태의 명세를 구체화하여 프로그램을 만드는 방법. (패턴 구성 방법)

### 2. 재공학 주요 활동 (Reengineering Activities)
기존 시스템을 개선하고 유지보수성을 높이는 활동입니다.
- **분석 (Analysis)**: 기존 명세서를 확인해 동작을 이해하고 대상을 선정.
- **재구성 (Restructuring)**: 외적인 동작은 유지하면서 코드 구조를 향상.
- **역공학 (Reverse Engineering)**: 기존 코드를 분석해 설계 정보나 구성 요소를 다시 추출(도출)해 내는 활동.
- **이식 (Migration)**: 다른 운영체제나 하드웨어 환경에서 사용할 수 있도록 변환.


## CASE (Computer Aided Software Engineering)
- 소프트웨어 개발 생명 주기(요구 분석, 설계, 구현, 검사 등) 전체 또는 일부를 **컴퓨터와 전용 도구를 사용해 자동화**하는 기법.
- 개발의 표준화를 지향하며 생산성 및 품질을 향상시킵니다.


## 소프트웨어 비용 산정 기법 (Software Cost Estimation)

### 1. LOC (Line Of Code) 기법
- 원시 코드(Source Code) 라인 수의 낙관치, 비관치, 기대치를 측정해 예측치를 구하여 비용을 산정.
- **공식**:
  - 노력(인월, Man-Month) = `LOC / 1인당 월평균 생산 코드 라인 수` = `개발 기간 × 투입 인원`
  - 개발 비용 = `노력(인월) × 단위 비용(월평균 인건비)`

### 2. 수학적 산정 기법
과거의 프로젝트 데이터를 기반으로 한 상향식 비용 산정 모델입니다.
- **COCOMO 모형 (Boehm 제안)**: LOC 기반 산정. 소프트웨어 규모에 따라 3가지로 분류.
  1. **조직형 (Organic)**: 5만 라인 이하 (중소 규모 업무용).
  2. **반분리형 (Semi-Detached)**: 30만 라인 이하 (컴파일러, 유틸리티).
  3. **내장형 (Embedded)**: 30만 라인 이상 (초대형 운영체제, 미사일 제어).
- **Putnam 모형 (생명 주기 예측 모형)**: 시간에 따른 **Rayleigh-Norden 곡선**의 노력 분포도를 기초로 산정.
- **FP (Function Point, 기능 점수) 모형**: 알브레히트(Albrecht) 제안. 기능 요인(입력, 출력, 사용자 질의, 데이터 파일, 외부 인터페이스)별로 가중치를 부여해 산정.

> **Vietnamese Explanation**: 
> - **LOC**: Tính chi phí dựa trên số dòng code.
> - **COCOMO**: Phân loại theo độ lớn dự án (Organic: nhỏ, Semi: vừa, Embedded: lớn).
> - **Putnam**: Dựa trên đường cong phân bố nỗ lực theo thời gian Rayleigh-Norden.
> - **FP (Function Point)**: Dựa trên số lượng chức năng phần mềm mang lại cho người dùng.

💡 **Mẹo ghi nhớ (Mnemonics):** 
- FP의 5가지 요인: **I.O.Q.F.I** (Input, Output, inQuiry, File, Interface).


## 프로젝트 일정 관리 (Project Schedule Management)

### 1. PERT (Program Evaluation and Review Technique)
과거 경험이 없어 예측이 어려운 프로젝트에 사용. 각 작업별로 낙관치, 기대치, 비관치를 나누어 종료 시기를 계산합니다.
- `예측치 = (비관치 + 4*기대치 + 낙관치) / 6`

### 2. CPM (Critical Path Method, 임계 경로 기법)
작업 사이의 의존 관계를 노드와 간선으로 구성. 네트워크에서 최장 경로가 **임계 경로(Critical Path)**가 됩니다.

### 3. 간트 차트 (Gantt Chart, 시간선 차트)
각 작업의 시작과 종료를 막대 도표로 표시하는 일정표. 적응성이 약하지만 이정표와 작업 기간을 한눈에 파악하기 쉽습니다.


## 소프트웨어 프로세스 품질 및 성숙도 표준 (Quality & Maturity Standards)

### 1. ISO/IEC 12207
표준 소프트웨어 생명 주기 프로세스. 3가지(기본, 지원, 조직 프로세스)로 분류.

### 2. CMMI (Capability Maturity Model Integration)
조직의 성숙도를 평가하는 모델 (5단계).
- **초기(Initial) -> 관리(Managed) -> 정의(Defined) -> 정량적 관리(Quantitatively Managed) -> 최적화(Optimizing)**

### 3. SPICE (ISO/IEC 15504)
프로세스 수행 능력 단계를 평가 (6단계).
- **불완전(Incomplete) -> 수행(Performed) -> 관리(Managed) -> 확립(Established) -> 예측(Predictable) -> 최적화(Optimizing)**

> **Vietnamese Explanation**: 
> Các tiêu chuẩn như CMMI và SPICE dùng để đánh giá xem một công ty phần mềm làm việc chuyên nghiệp đến đâu. CMMI có 5 cấp độ (từ lộn xộn đến tối ưu hóa liên tục), còn SPICE có 6 cấp độ.


## 소프트웨어 개발 방법론 테일러링 및 프레임워크 (Tailoring & Framework)

### 1. 테일러링 (Tailoring)
프로젝트 특성에 맞게 개발 방법론의 절차나 기법을 수정 및 보완하는 작업.
- **내부적 기준**: 목표 환경, 요구사항, 프로젝트 규모, 보유 기술.
- **외부적 기준**: 법적 제약사항, 표준 품질 기준.

### 2. 소프트웨어 개발 프레임워크 (Framework)
공통 사용되는 구성 요소와 아키텍처를 일반화하여 제공하는 반제품 형태의 시스템. (예외 처리, 트랜잭션, DB 연동 등 기본 기능 제공).
- **종류**: 스프링(Spring - Java용), 닷넷(.NET - Windows용), 전자정부 프레임워크(공공부문 지원).

## 프레임워크 특징 및 SW 신기술 (Framework & SW Tech)

### 1. 프레임워크의 특성 (Characteristics of Framework)
- **모듈화 (Modularity)**: 캡슐화로 모듈화를 강화하여 변경 영향을 최소화.
- **재사용성 (Reusability)**: 재사용 가능한 모듈 제공으로 생산성 향상.
- **확장성 (Extensibility)**: 다형성을 통한 인터페이스 확장.
- **제어의 역흐름 (Inversion of Control)**: 개발자가 아닌 프레임워크가 객체들을 제어하고 통제.

### 2. SDE (Software-Defined Everything)
하드웨어 자원을 가상화하여 소프트웨어만으로 제어 및 관리하는 기술.
- **SDN**: 소프트웨어 정의 네트워킹 (네트워크 가상화)
- **SDDC**: 소프트웨어 정의 데이터 센터 (데이터 센터 전체 가상화)
- **SDS**: 소프트웨어 정의 스토리지 (스토리지 가상화)

### 3. 주요 SW 및 관련 용어
- **SOA (Service Oriented Architecture)**: 서비스나 컴포넌트 중심으로 구축하는 아키텍처.
- **디지털 트윈 (Digital Twin)**: 물리적 자산을 소프트웨어로 가상화(복제)하여 효율성을 높이는 기술.
- **텐서플로 (TensorFlow)**: 구글이 만든 딥러닝/데이터 흐름용 오픈소스 라이브러리.
- **도커 (Docker)**: 컨테이너(Container) 기술을 자동화하는 오픈소스 프로젝트.


## 네트워크 구조 및 기술 (Network Structures & Technologies)

### 1. 네트워크 설치 구조 (Network Topologies)
- **성형 (Star, 중앙 집중형)**: 중앙 컴퓨터를 중심으로 단말기가 연결 (Point-to-Point).
- **링형 (Ring, 루프형)**: 이웃하는 장치끼리 연결. 단방향 시 하나만 고장나도 전체 마비.
- **버스형 (Bus)**: 한 개의 통신 회선에 여러 장치 연결 (단말기 추가/제거 용이).
- **계층형 (Tree, 분산형)**: 중앙에서 중간 단말장치로 다시 분기되는 형태.
- **망형 (Mesh)**: 모든 지점을 연결. 통신량이 많을 때 유리하며 회선이 가장 많이 필요함 (`n(n-1)/2` 개).

### 2. 근거리 통신망 (LAN) 표준 및 기술
- **IEEE 802 규격**: 802.3(CSMA/CD), 802.4(토큰 버스), 802.5(토큰 링), 802.11(무선 LAN).
- **VLAN**: 물리적 배치와 상관없이 논리적으로 분리하는 기술.
- **CSMA/CA**: 무선 LAN(802.11)에서 매체가 비어있음을 확인 후 충돌 회피(Avoidance)를 위해 기다렸다가 전송하는 방식.

### 3. 경로 제어 (Routing) 및 흐름 제어 (Flow Control)
- **IGP (내부 게이트웨이 프로토콜)**: AS 내에서 사용. **RIP**(거리 벡터, 최대 15홉 제한)와 **OSPF**(링크 상태, 대규모 망)가 있음.
- **EGP / BGP**: AS(자율 시스템) 간의 라우팅 프로토콜.
- **흐름 제어**: **정지-대기(Stop-and-Wait)** (수신 확인 후 다음 패킷 전송) / **슬라이딩 윈도우(Sliding Window)** (수신 확인 없이 윈도우 크기만큼 연속 전송).

💡 **Mẹo ghi nhớ (Mnemonics):** 
- **RIP**: 15 Hops max (Dùng cho mạng nhỏ).
- **OSPF**: Link State (Dùng cho mạng lớn).
- **CSMA/CD**: Mạng LAN có dây (Collision Detection).
- **CSMA/CA**: Mạng không dây (Collision Avoidance).


## 정보 보안 및 하드웨어 신기술 (Security & HW Tech)

### 1. 보안 용어 및 Secure OS
- **BaaS (Blockchain as a Service)**: 클라우드 기반 블록체인 개발 환경 제공.
- **OWASP**: 웹 취약점을 연구하는 비영리 단체 (10대 취약점 발표).
- **허니팟 (Honeypot)**: 침입자를 속여 정보를 수집하기 위해 설치해 둔 시스템 (미끼).
- **Secure OS**: 기존 OS에 보안 기능 커널을 이식한 운영체제. 암호적, 논리적, 시간적, 물리적 분리 방법을 통해 보호하며 식별, 인증, 접근통제(MAC, DAC) 기능을 제공합니다.

### 2. 하드웨어 신기술
- **HA (High Availability, 고가용성)**: 장애 발생 시 즉시 다른 시스템으로 대체 가능한 이중화 환경.
- **RAID**: 여러 개의 하드디스크에 데이터를 분산 저장하여 속도와 안정성을 향상시키는 기술.
- **트러스트존 (TrustZone)**: 프로세서 내에 일반 구역과 보안 구역을 분할하는 ARM의 하드웨어 보안 기술.


## 데이터베이스 신기술 (DB New Technologies)

### 1. 빅데이터 및 분석 기술
- **하둡 (Hadoop)**: 대용량 데이터를 병렬로 처리하기 위한 자바 소프트웨어 프레임워크 (오픈소스).
- **맵리듀스 (MapReduce)**: 하둡 기반 분산 처리 프로그래밍 모델 (Map으로 분류, Reduce로 추출).
- **데이터 마이닝 (Data Mining)**: 대량의 데이터에서 패턴을 규명하여 유용한 정보를 추출하는 기법.
- **OLAP**: 다차원 데이터로부터 통계적 요약 정보를 분석하여 의사결정에 활용. (연산: Roll-up, Drill-down, Pivoting 등).


## DB 회복 및 병행 제어 (DB Recovery & Concurrency Control)

### 1. 회복 기법 (Recovery)
장애 발생 시 데이터베이스를 정상 상태로 복구합니다.
- **연기 갱신 (Deferred Update)**: 트랜잭션이 완료될 때까지 DB 갱신을 연기하고 로그(Log)에 보관. 실패 시 무시하면 됨. (Redo만 가능).
- **즉각 갱신 (Immediate Update)**: 즉시 DB에 갱신하고 로그에 보관. 실패 시 취소(Undo)와 재실행(Redo) 모두 사용.
- **그림자 페이지 (Shadow Paging)**: 복사본(그림자) 페이지를 보관해두고, 실패 시 대체하는 방식 (로그 불필요).
- **검사점 (Check Point)**: 특정 단계에 검사점을 찍어 장애 시 그 시점부터 회복(시간 절약).

### 2. 병행 제어 기법 (Concurrency Control)
다중 트랜잭션 실행 시 DB의 일관성이 파괴되지 않도록 제어합니다.
- **로킹 (Locking)**: 데이터 엑세스 전에 Lock(잠금)을 요청하는 기법. (로킹 단위: DB, 파일, 레코드 등 한꺼번에 잠그는 크기).
- **타임 스탬프 순서 (Time Stamp Ordering)**: 트랜잭션 실행 전 시간표(Time Stamp)를 부여해 그 순서대로 처리 (교착상태 미발생).
- **다중 버전 기법**: 갱신될 때마다 새로운 버전(Version)을 부여해 관리.

> **Vietnamese Explanation**: 
> **Recovery (Phục hồi DB)** có Deferred (chờ xong mới cập nhật - chỉ Redo), Immediate (cập nhật ngay - cần cả Undo và Redo).
> **Concurrency Control (Kiểm soát đồng thời)** dùng Locking (khóa dữ liệu khi đang dùng) hoặc Time Stamp (cấp tem thời gian để xếp hàng trước sau) tránh việc 2 giao dịch cùng sửa 1 dữ liệu gây lỗi.

## 교착상태 (Dead Lock)
둘 이상의 프로세스가 자원을 점유한 상태에서 서로 다른 프로세스의 자원을 무한정 기다리는 현상.

### 1. 교착상태 발생의 4가지 필요충분조건
모두 충족해야 교착상태가 발생합니다.
- **상호 배제 (Mutual Exclusion)**: 한 번에 한 프로세스만 자원 사용.
- **점유와 대기 (Hold and Wait)**: 자원을 점유한 채로 다른 자원을 대기.
- **비선점 (Non-preemption)**: 할당된 자원을 강제로 빼앗을 수 없음.
- **환형 대기 (Circular Wait)**: 대기하는 프로세스들이 원형(Cycle)을 이룸.

### 2. 교착상태 해결 방법
- **예방 (Prevention)**: 4가지 조건 중 하나를 제거 (자원 낭비가 가장 심함).
- **회피 (Avoidance)**: 발생 가능성을 인정하고 적절히 피해감 (**은행원 알고리즘 / Banker's Algorithm**).
- **발견 (Detection)**: 발생 여부를 점검 (자원 할당 그래프 등).
- **회복 (Recovery)**: 교착상태에 있는 프로세스를 종료하거나 자원을 선점하여 회복.

> **Vietnamese Explanation**: 
> **Deadlock (Bế tắc)** giống như kẹt xe ở ngã tư, ai cũng chờ người kia nhường đường nên không ai đi được. Để giải quyết, phương pháp **Avoidance (Né tránh)** dùng thuật toán Banker (người giữ tiền) để đảm bảo luôn có đủ tài nguyên cấp phát một cách an toàn.


## 소프트웨어 보안 (Software Security)

### 1. 보안 3대 요소 (CIA Triad)
- **기밀성 (Confidentiality)**: 인가된 사용자만 접근 가능 (암호화).
- **무결성 (Integrity)**: 인가된 사용자만 수정 가능 (변조 방지).
- **가용성 (Availability)**: 인가된 사용자는 언제든 사용 가능.
- 기타: 인증(Authentication), 부인 방지(Non-Repudiation).

### 2. Secure SDLC
보안상 안전한 SW 개발을 위해 SDLC(생명주기)에 보안 활동을 추가한 것.
- **방법론**: CLASP(초기 단계 중심), SDL(MS사 개발), Seven Touchpoints(각 단계별 모범사례 적용).

### 3. 주요 보안 약점 및 방어
- **SQL 삽입 (SQL Injection)**: 입력 폼에 SQL 명령어를 넣어 DB를 조작. (방어: 입력값 필터링 및 매개변수화).
- **XSS (크로스사이트 스크립팅)**: 웹페이지에 악성 스크립트를 삽입해 사용자 정보 탈취. (방어: `<, >, &` 등 특수문자 치환).
- **메모리 버퍼 오버플로**: 할당된 메모리 범위를 넘어서 기록하여 오동작 유발.
  - **스택 가드 (Stack Guard)**: 복귀 주소와 변수 사이에 특정 값을 넣어 오버플로를 탐지하는 기술.
- **접근 지정자 (Access Modifier)**: `Public`(모두 접근), `Protected`(패키지+상속), `Default`(같은 패키지), `Private`(클래스 내부만).

💡 **Mẹo ghi nhớ (Mnemonics):** 
- 보안 3요소: **C.I.A** (Confidentiality - Integrity - Availability).
- 접근 한정자: **P.P.D.P** (Public - Protected - Default - Private).


## 암호화 기법 (Encryption Techniques)

### 1. 개인키 (대칭키) 암호화 (Private Key / Symmetric Key)
- 암호화와 복호화에 **동일한 키(비밀키)**를 사용합니다.
- 장점: 속도가 빠름 / 단점: 키 분배가 어렵고 키 개수가 많아짐.
- 필요한 키의 개수: `n(n-1) / 2`
- **종류**: DES, 3DES, AES, SEED(국내), ARIA(국내).

### 2. 공개키 (비대칭키) 암호화 (Public Key / Asymmetric Key)
- 암호화할 때는 공개키(Public Key), 복호화할 때는 비밀키(Private Key)를 사용합니다.
- 장점: 키 분배 용이, 키 개수 적음 / 단점: 암복호화 속도가 느림.
- 필요한 키의 개수: `2n`
- **종류**: RSA.

### 3. 해시(Hash)와 솔트(Salt)
- **해시 (Hash)**: 임의의 길이 데이터를 고정된 길이의 값으로 변환(단방향). 무결성 검증 및 패스워드 암호화에 사용 (예: SHA-256, MD5).
- **솔트 (Salt)**: 암호화 전 원문에 덧붙이는 무작위 값. 동일한 패스워드라도 솔트가 다르면 해시값이 달라져 레인보우 테이블 공격을 방어합니다.

> **Vietnamese Explanation**: 
> **Mã hóa đối xứng (Private Key)**: Dùng chung 1 chìa khóa để khóa và mở (nhanh nhưng khó chia sẻ chìa khóa an toàn).
> **Mã hóa bất đối xứng (Public Key)**: Dùng khóa công khai để khóa, khóa bí mật để mở (chậm hơn nhưng an toàn). 
> **Hash (Băm)** là mã hóa 1 chiều (không dịch ngược được). **Salt (Muối)** là thêm chuỗi ngẫu nhiên vào mật khẩu trước khi băm để tăng độ khó.


## 네트워크 및 정보 침해 공격 (Network & Info Security Attacks)

### 1. 네트워크 공격
- **DDoS (분산 서비스 거부 공격)**: 여러 대의 PC(Agent/Zombie)를 이용해 특정 서버에 대량의 트래픽을 보내 마비시킴. (툴: Trin00, TFN, TFN2K, Stacheldraht).
- **스머핑 (SMURFING)**: IP/ICMP 특성을 악용해 한 사이트에 엄청난 데이터를 집중시키는 공격.
- **세션 하이재킹 (Session Hijacking)**: 클라이언트 세션을 가로채어 정상적인 사용자인 척하는 공격.
- **스위치 재밍 (Switch Jamming)**: 위조된 MAC 주소를 대량으로 보내 스위치를 더미 허브처럼 작동하게 만듦.

### 2. 블루투스 공격
- **블루버그 (BlueBug)**: 원격 조종 및 통화 감청.
- **블루스나프 (BlueSnarf)**: 장비 파일에 접근해 정보 탈취.
- **블루재킹 (BlueJacking)**: 스팸 메시지를 익명으로 퍼뜨림.

### 3. 시스템 및 소프트웨어 공격
- **제로 데이 공격 (Zero Day Attack)**: 보안 취약점이 공표되기 전, 혹은 패치가 나오기 전에 신속하게 이루어지는 공격.
- **랜섬웨어 (Ransomware)**: 파일을 암호화하고 돈(Ransom)을 요구하는 악성 프로그램.
- **백도어 (Back Door)**: 관리자 편의를 위해 만들어 놓은 비밀 통로를 악용.

💡 **Mẹo ghi nhớ (Mnemonics):** 
- **BlueSnarf**: Sniff (Đánh hơi/Trộm thông tin).
- **BlueBug**: Bug (Cài bọ/Nghe lén).
- **BlueJacking**: Hijack (Chặn tin/Gửi tin nhắn rác).


## 인증 및 보안 체계 (Authentication & Security System)

### 1. 인증 수단 4가지
- **지식 기반 (Something You Know)**: 패스워드, PIN (머릿속 기억).
- **소유 기반 (Something You Have)**: 신분증, 스마트카드, OTP.
- **생체 기반 (Something You Are)**: 지문, 홍채, 정맥 인식.
- **위치 기반 (Somewhere You Are)**: 접속 IP 위치, GPS.

### 2. 보안 체계 3영역
- **관리적 보안**: 정보보호 정책, 조직, 교육 등 사람 중심.
- **물리적 보안**: 출입 통제, 전산실 관리 등 물리적 보호.
- **기술적 보안**: 사용자 인증, 암호화, 접근 제어 등 IT 기술 보호.

## 침입 탐지 시스템 (IDS; Intrusion Detection System)
컴퓨터 시스템의 비정상적인 사용, 오용, 남용 등을 실시간으로 탐지하는 시스템.
- **오용 탐지 (Misuse Detection)**: 미리 입력해 둔 공격 패턴 감지 (시그니처 기반).
- **이상 탐지 (Anomaly Detection)**: 평균적인 상태를 기준으로 비정상 행위 감지 (행위 기반).
- **종류**:
  - **HIDS (Host-Based)**: 내부 시스템 감시 (OSSEC 등).
  - **NIDS (Network-Based)**: 외부로부터의 네트워크 트래픽 감시 (Snort 등).

## 리눅스의 커널 로그 (Linux Kernel Logs)
- `/var/log/wtmp`: 성공한 로그인/로그아웃 및 시스템 시작/종료 시간 기록.
- `/var/run/utmp`: 현재 로그인한 사용자의 상태 기록.
- `/var/log/btmp`: 실패한 로그인 기록.
- `/var/log/lastlog`: 마지막으로 성공한 로그인 기록.


## 네트워크 보안 기술 (Network Security Tech)
- **VPN (가상 사설 통신망)**: 공중 네트워크를 전용 회선처럼 사용할 수 있게 해주는 암호화 보안 솔루션.
- **SSH (시큐어 셸)**: 원격 로그인, 파일 복사 등을 안전하게 수행하는 프로토콜 (포트 22번 사용, 데이터 암호화 지원).


## 소프트웨어 생명주기 모델 (SDLC Models)
- **폭포수 모델 (Waterfall)**: 각 단계를 명확히 마무리한 후 다음 단계로 넘어가는 선형 순차적 모델 (요구사항 변경 어려움).
- **프로토타입 모델 (Prototyping)**: 시제품(Prototype)을 만들어 최종 결과물을 예측.
- **나선형 모델 (Spiral)**: 점진적으로 개발하며 **위험 분석(Risk Analysis)** 기능을 추가한 대형 프로젝트용 모델.
- **V 모델 (V Model)**: 폭포수 모델에 테스트 단계를 세부적으로 추가하여 검증을 강화한 모델.

> **Vietnamese Explanation**: 
> - **Waterfall (Thác nước)**: Làm xong bước này mới qua bước khác. 
> - **Prototyping (Mẫu thử)**: Làm một bản nháp cho khách hàng xem trước.
> - **Spiral (Xoắn ốc)**: Làm từng phần và liên tục đánh giá rủi ro (Risk analysis).
> - **V Model (Chữ V)**: Nhấn mạnh vào việc kiểm thử (Testing) ở mỗi giai đoạn tương ứng.


## 스토리지 시스템 (Storage Systems)
대용량 데이터를 저장하기 위한 장치 구성 방식.
- **DAS (Direct Attached Storage)**: 서버와 스토리지를 전용 케이블로 **직접 연결**.
- **NAS (Network Attached Storage)**: 서버와 스토리지를 **네트워크(LAN)**로 연결.
- **SAN (Storage Area Network)**: 스토리지 전용 **광 채널 네트워크(FC-SAN)**를 별도로 구성하여 고속 전송.

💡 **Mẹo ghi nhớ (Mnemonics):** 
- **DAS**: Direct (Cắm trực tiếp).
- **NAS**: Network (Qua mạng LAN).
- **SAN**: Area Network (Mạng quang riêng tốc độ cao).


## 소프트웨어 개발 보안 관련 법규
- **개인정보 보호법**: 개인정보 처리 및 보호에 관한 전반적 사항.
- **정보통신망법**: 정보통신망을 통한 개인정보 수집/이용 보호.
- **신용정보법**: 개인의 신용정보 취급 보호.
- **위치정보법**: 개인 위치정보 수집 및 제공 보호.

