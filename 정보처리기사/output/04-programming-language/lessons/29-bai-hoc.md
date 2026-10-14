# A+ Deep Dive: Java 비교 연산과 Python 제어 흐름

## A+ Deep Dive: Java 비교 연산과 Python 제어 흐름

### 1. Java의 `==`는 문맥을 먼저 본다
Phần “1. Java의 `==`는 문맥을 먼저 본다” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

```java
int a = 1;
double b = 1.0;
System.out.println(a == b);        // true: 수치 승격 후 비교
String x = new String("A");
String y = new String("A");
System.out.println(x == y);        // false: 서로 다른 객체 참조
System.out.println(x.equals(y));   // true: 내용 비교
```

- 숫자형 피연산자는 binary numeric promotion 후 비교한다.
- 참조형 `==`는 같은 객체를 가리키는지 비교하고, 문자열 내용 비교에는 `equals`를 사용한다.
- `a == b == c`는 “세 값이 모두 같은가”가 아니라 왼쪽부터 계산되므로 별도 비교식이 필요하다.

### 2. Python `for`와 `while`의 trace 포인트
Phần “2. Python `for`와 `while`의 trace 포인트” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

```python
items = [1, 2, 3]
total = 0
for value in items:
    if value == 2:
        continue
    total += value
print(total)  # 4
```

`continue`는 현재 반복의 나머지를 건너뛰고 다음 반복으로 이동한다. `break`는 반복문 전체를 종료한다. 문제를 풀 때 초기값, 조건 검사 시점, 증감/자료 갱신 위치를 표로 추적한다.

> **시험 함정:** Java 문자열의 `==`와 `equals`, Python의 `continue`와 `break`를 섞지 않는다.

### 자주 혼동하는 판별 포인트
Phần “자주 혼동하는 판별 포인트” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- C 반복문은 초기값·조건·증감식과 실제 접근 인덱스를 따로 표로 적는다. `i += 2`이면 짝수 인덱스만 방문할 수 있다.
- Java의 후위 감소 `y--`는 비교에 현재 값을 사용한 뒤 값을 줄인다. 반복 종료 시점의 변수값을 마지막 조건 평가까지 반영한다.
- Python `split(delimiter)`는 지정한 구분자로 문자열을 나누고, `map(int, ...)`는 각 조각을 정수로 바꾼다.
- IPv6는 128비트 주소와 anycast를 사용한다. IPv6 패킷/헤더 크기를 무제한으로 해석하거나 IPv4의 32비트와 혼동하지 않는다.
