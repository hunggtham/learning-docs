# 084. 페이지 교체 알고리즘 (Page Replacement Algorithms / Thuật toán thay thế trang nhớ)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **084. 페이지 교체 알고리즘 (Page Replacement Algorithms / Thuật toán thay thế trang nhớ)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

페이지, 교체, 알고리즘

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **079. 프로그래밍 언어의 종류 (Types of Programming Languages)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **교착상태 필요충분조건 1 - 상호배제 (Deadlock Conditions - Mutual Exclusion)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **084. 페이지 교체 알고리즘 (Page Replacement Algorithms / Thuật toán thay thế trang nhớ)** và nối nó với **교착상태 필요충분조건 1 - 상호배제 (Deadlock Conditions - Mutual Exclusion)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 084. 페이지 교체 알고리즘 (Page Replacement Algorithms / Thuật toán thay thế trang nhớ)
- 메모리가 꽉 찼을 때 어떤 페이지를 내보낼지 결정.
- **FIFO (First In First Out)**: 가장 먼저 들어온 페이지를 교체.
- **OPT (Optimal)**: 앞으로 가장 오랫동안 사용되지 않을 페이지를 교체 (이론상 최적).
- **LRU (Least Recently Used)**: (과거 기준) 가장 오랫동안 사용되지 않은 페이지를 교체.
- **LFU (Least Frequently Used)**: 사용(참조) 횟수가 가장 적은 페이지 교체.
- **NUR (Not Used Recently)**: 참조 비트(R)와 변형/수정 비트(M)를 조합해 페이지를 네 등급으로 나누고 낮은 등급부터 교체한다.
- **지역성 (Locality)**: 프로세스가 특정 메모리 영역을 집중적으로 참조하는 현상.
  - 공간 지역성: 근처 메모리 참조 (배열).
  - 시간 지역성: 방금 참조한 곳 다시 참조 (루프, 변수).
- **스레싱 (Thrashing)**: 실제 CPU 연산보다 페이지 교체에 더 많은 시간이 소요되어 시스템 성능이 뚝 떨어지는 현상.

**Giải thích (Vietnamese):**
Khi RAM đầy, máy phải đẩy tạm dữ liệu ra ổ cứng.
- LRU: Đuổi cái nào lâu nhất không ai thèm đụng tới (Thường xuyên dùng nhất).
- LFU: Đuổi cái nào ít được gọi tên nhất.
- Locality: Chương trình có xu hướng dùng lại những dữ liệu gần nhau (Ví dụ chạy vòng lặp `for`).
- Thrashing: Tình trạng máy tính bị đơ, giật lag vì RAM quá đầy, máy mải mê swap dữ liệu ra vào ổ cứng mà không chịu tính toán xử lý.

---
