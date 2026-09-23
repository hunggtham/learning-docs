# A+ Deep Dive: Java 비교 연산과 Python 제어 흐름

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **A+ Deep Dive: Java 비교 연산과 Python 제어 흐름**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

Deep, Dive, Java, 비교, 연산과, Python, 제어, 흐름

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## A+ Deep Dive: Java 비교 연산과 Python 제어 흐름

### 1. Java의 `==`는 문맥을 먼저 본다

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
