# 9. 암호화 기술 (Công nghệ Mã hóa)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **9. 암호화 기술 (Công nghệ Mã hóa)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

암호화, 기술

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 9. 암호화 기술 (Công nghệ Mã hóa)

### 9.1 개인키 vs 공개키 암호화 (대칭키 vs 비대칭키)
- **개인키(대칭키) 암호화 (Private/Symmetric Key):**
  - **동일한 키**로 암호화/복호화. 속도가 빠름. 암호화 키 개수: n(n-1)/2.
  - 종류: 
    - **블록 암호화:** DES, SEED, AES, ARIA, IDEA
    - **스트림 암호화:** LFSR, RC4
- **공개키(비대칭키) 암호화 (Public/Asymmetric Key):**
  - 암호화(공개키), 복호화(비밀키/개인키). 키 개수: **2n**.
  - 대표 알고리즘: **RSA** (소인수분해 기반).
- **Tiếng Việt:** 
  - Khóa cá nhân (Đối xứng): Cùng 1 khóa, nhanh. (DES, AES, ARIA).
  - Khóa công khai (Bất đối xứng): 2 khóa (Public để mã hóa, Private để giải mã), an toàn nhưng chậm. (RSA).

### 9.2 해시 및 기타 암호화 요소
- **해시 (Hash):** 임의의 길이를 고정된 길이로 변환. 복호화가 불가한 **일방향 함수**. (종류: SHA, MD4, MD5 등).
- **솔트 (Salt):** 암호화 전 원문에 무작위 값을 덧붙이는 과정. (패스워드 보안 강화용).
- **Tiếng Việt:** Hash là hàm một chiều không thể giải mã (SHA, MD5). Salt là thêm chuỗi ngẫu nhiên trước khi mã hóa để chống tấn công từ điển.
