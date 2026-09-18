# Boolean algebra và logic số

Boolean algebra (불 대수) làm việc với hai values thường viết `0/1` hoặc `false/true`. Nó là nền toán học của conditions trong software và digital circuits.

## Operations

NOT:

```text
¬P
```

AND:

```text
P ∧ Q
```

OR:

```text
P ∨ Q
```

XOR true khi exactly one input true:

```text
P ⊕ Q
```

## Truth tables

Truth table liệt kê output cho mọi input combinations. Với `n` Boolean inputs có `2^n` rows vì mỗi input có two states.

Truth tables là brute-force proof method cho finite propositional equivalence.

## De Morgan laws

```math
\neg(P\land Q)=(\neg P)\lor(\neg Q)
```

```math
\neg(P\lor Q)=(\neg P)\land(\neg Q)
```

Trong code, chúng giúp rewrite conditions. Nhưng language short-circuit và side effects có thể làm operational behavior khác dù truth value logic tương đương.

## Boolean identities

Idempotent:

```text
P ∨ P = P
P ∧ P = P
```

Absorption:

```text
P ∨ (P ∧ Q) = P
```

Distributive laws tồn tại theo cả directions trong Boolean algebra.

## Gates

AND, OR, NOT gates implement Boolean operations bằng electronics. NAND hoặc NOR alone là functionally complete: có thể build mọi Boolean function chỉ từ một loại gate đó.

Software conditions cuối cùng được compiled qua layers tới machine operations trên bits/branches, nên Boolean algebra nối high-level logic với hardware.

## Bitwise operations

Bitwise AND/OR/XOR áp operation từng bit trên integers. Ví dụ permissions có thể encode bit masks.

```text
READ  = 001
WRITE = 010
EXEC  = 100
```

Combine READ+WRITE bằng OR: `011`. Check WRITE bằng AND mask.

Bitwise operator khác logical operator ở type và semantics; trong many languages `&` và `&&` không interchangeable.

## Two's complement connection

Signed integers thường dùng two's complement để arithmetic addition hardware dùng same adder cho positive/negative. Bitwise interpretation cần biết fixed width; `~x` phụ thuộc representation width.

## Karnaugh/minimization idea

Boolean expression có thể simplify để giảm gates/conditions. Hardware logic minimization dùng algebra, Karnaugh maps hoặc algorithmic synthesis. Trong software, simplify condition improves readability nhưng phải preserve null/side-effect semantics.

## Mental Model

> Boolean algebra là arithmetic của decisions. Truth tables mô tả mọi finite cases; gates biến algebra thành circuits; bit masks biến multiple Boolean flags thành compact integer representation.

## Common Misconceptions

XOR không giống OR. Logical operators và bitwise operators không luôn giống nhau. Hai Boolean expressions truth-equivalent có thể khác runtime side effects nếu evaluation strategy khác.

## Worked Example: simplify access rule

Giả sử access được phép nếu user là admin, hoặc vừa active vừa owner:

```text
A OR (B AND C)
```

Nếu code deny condition bằng phủ định:

```text
NOT [A OR (B AND C)]
```

De Morgan:

```text
(NOT A) AND [NOT(B AND C)]
```

rồi

```text
(NOT A) AND [(NOT B) OR (NOT C)]
```

Transformation giúp review logic điều kiện rõ hơn, nhưng production code còn phải xét nullable values, role hierarchy và side effects của permission checks.

## XOR và parity

XOR có property associative và `x XOR x=0`. Vì vậy XOR checksum có thể detect một số patterns và tìm element xuất hiện odd number lần, nhưng checksum đơn giản không phải một fingerprint duy nhất: nhiều different inputs có thể collide. Algebraic property vừa tạo utility vừa tạo limitation.
