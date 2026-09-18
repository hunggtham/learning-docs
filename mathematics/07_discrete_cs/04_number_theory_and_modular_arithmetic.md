# Lý thuyết số và số học modulo

Lý thuyết số (Number theory / 정수론) nghiên cứu integers và divisibility. Dù từng được xem là pure mathematics, nó có nhiều ứng dụng trong hashing, checksums, cyclic computations và các hệ thống số rời rạc.

## Divisibility

`a` divides `b`, viết

```math
a\mid b
```

nếu tồn tại integer `k` sao cho `b=ak`.

Nếu không tồn tại, `a∤b`.

## GCD và Euclidean algorithm

Greatest common divisor `gcd(a,b)` là largest positive integer divides both.

Euclidean algorithm dựa trên fact:

```math
gcd(a,b)=gcd(b,a\bmod b)
```

vì common divisors của `a,b` cũng divide remainder `a-qb`, và ngược lại.

Example:

```text
252 = 105×2 + 42
105 = 42×2 + 21
42  = 21×2 + 0
```

nên `gcd(252,105)=21`.

## Prime factorization

Mỗi integer >1 có factorization unique thành primes up to order:

```math
n=p_1^{a_1}\cdots p_k^{a_k}
```

Đây là Fundamental Theorem of Arithmetic.

GCD lấy minimum exponents chung; LCM lấy maximum exponents.

## Congruence modulo n

Ta viết

```math
a\equiv b\pmod n
```

nếu `n|(a-b)`, tức a và b có same remainder modulo n.

Ví dụ

```math
17\equiv5\pmod{12}
```

vì difference 12 divisible by 12.

Modular arithmetic là arithmetic trên equivalence classes, không chỉ operator `%`.

## Clock arithmetic

Hours modulo 12: `10+5=15≡3 mod 12`. Cyclic buffers, weekdays, hash buckets và sequence-number wraparound đều dùng same structure.

## Modular addition/multiplication

Nếu

```math
a\equiv b\pmod n,
\quad c\equiv d\pmod n
```

thì

```math
a+c\equiv b+d\pmod n
```

và

```math
ac\equiv bd\pmod n
```

Điều này cho phép reduce intermediate numbers.

## Modular inverse

`a^{-1} mod n` là number `x` sao cho

```math
ax\equiv1\pmod n
```

Inverse tồn tại iff

```math
\gcd(a,n)=1
```

Đây là condition coprime.

Extended Euclidean algorithm tìm integers `x,y` sao cho

```math
ax+ny=\gcd(a,n)
```

Nếu gcd=1, reduce modulo n cho modular inverse.

## Fermat/Euler idea

Nếu prime `p` và `a` không divisible by `p`:

```math
a^{p-1}\equiv1\pmod p
```

Fermat's little theorem. Euler generalizes với totient `φ(n)` cho coprime `a,n`:

```math
a^{\phi(n)}\equiv1\pmod n
```

Các results giúp modular exponentiation và nhiều constructions trong discrete computing.

## RSA connection

Một số hệ thống tính toán dùng modulus là product của large primes và modular exponentiation. Điều quan trọng về mặt toán học là factoring số composite lớn có thể khó về computational cost dù vẫn có thuật toán về nguyên tắc.

Ứng dụng thực tế của number theory còn phụ thuộc vào protocol, randomness, implementation và nhiều lớp engineering khác; mathematics alone không đủ để đảm bảo một hệ thống đúng trong thực tế.

## Hashing

Hash table thường map large hash value vào bucket range bằng modulo-like operation. Good hash aims spread keys; modulo không tự tạo uniformity nếu upstream hash poor hoặc patterns interact với table size.

## Mental Model

> Modular arithmetic coi integers chỉ khác nhau theo remainder class. Nó biến infinite number line thành finite cycle nhưng vẫn giữ addition/multiplication structure, nên rất phù hợp với periodic systems và discrete computing.

## Common Misconceptions

Modulo equivalence không phải ordinary equality. `%` behavior với negative numbers khác nhau giữa languages, nên programming semantics cần check. Các ứng dụng thực tế của number theory còn phụ thuộc vào assumptions và implementation, không chỉ vào việc “dùng số nguyên tố”.
