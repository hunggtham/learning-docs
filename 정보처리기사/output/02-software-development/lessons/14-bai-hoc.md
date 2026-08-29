# 029 & 030: 검색 알고리즘 및 해싱 (Search Algorithms & Hashing)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **029 & 030: 검색 알고리즘 및 해싱 (Search Algorithms & Hashing)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

검색, 알고리즘, 해싱

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 029 & 030: 검색 알고리즘 및 해싱 (Search Algorithms & Hashing)

### 검색 (Search - Tìm kiếm)
- **순차 검색 (Sequential/Linear Search):** Tìm tuần tự từ đầu đến cuối. Dùng cho mảng *chưa sắp xếp*. O(n).
- **이진 검색 (Binary Search):** Tìm nhị phân. Chia đôi mảng liên tục. **Bắt buộc mảng phải ĐÃ SẮP XẾP.** O(log n). Rất nhanh.

### 해싱 (Hashing - Băm dữ liệu)
- Dùng hàm băm (Hash Function) tính ra trực tiếp địa chỉ bộ nhớ để lưu hoặc tìm kiếm dữ liệu. Nhanh nhất (O(1)).

- **Vietnamese Explanation:** Tìm tuần tự là lật từng trang sách. Tìm nhị phân là mở giữa cuốn từ điển, xem vần nào rồi gập nửa bỏ đi, tìm tiếp ở nửa kia. Băm (Hashing) là nhìn Mục lục rồi lật thẳng trang đó.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Binary Search = Phải Sắp Xếp (Sắp xếp), Chia đôi (절반). Hashing = O(1) Siêu Tốc.

### 해시 충돌 해결 방법 (Hash Collision Resolution / Các phương pháp giải quyết đụng độ Hash)

| 방법 (Phương pháp) | 설명 (Giải thích) |
|---|---|
| **체이닝 (Chaining - Móc xích)** | 버킷 내에 연결리스트(Linked List)를 할당하여 데이터들을 연결하는 방식. (Dùng danh sách liên kết để nối các phần tử bị đụng độ lại với nhau trong cùng 1 bucket.) |
| **개방 주소법 (Open Addressing - Địa chỉ mở)** | 충돌이 일어났을 때 다른 버킷에 데이터를 삽입해 해결하는 방식. (Khi đụng độ, tìm một ô trống khác để nhét vào. Địa chỉ dữ liệu bị thay đổi so với ban đầu.) |
| 선형 탐색 (Linear Probing) | 해시충돌 시 다음 버킷, 혹은 몇 개를 건너뛰어 삽입. (Thử tuyến tính: Tìm ô trống kế tiếp.) |
| 제곱 탐색 (Quadratic Probing) | 해시충돌 시 제곱만큼 건너뛴 버킷에 삽입 (1, 4, 9, 16...). (Thử bậc hai: Nhảy xa dần theo bình phương để tránh tụ tập.) |
| 이중 해시 (Double Hashing) | 해시충돌 시 다른 해싱함수를 한 번 더 적용. (Băm kép: Dùng thêm một hàm băm phụ để tìm khoảng nhảy.) |

- **Vietnamese Explanation:** Khi hai dữ liệu băm ra cùng một địa chỉ (Collision), ta phải giải quyết. Chaining là cho chúng ở chung một nhà nhưng nối đuôi nhau (như xâu chuỗi). Open Addressing là "nhà này có người rồi, mời anh đi tìm nhà khác". 
- 💡 **Mẹo ghi nhớ (Mnemonics):** Chaining = Dây xích (Linked List). Open Addressing = Mở cửa đi tìm nhà khác (Linear, Quadratic, Double).

---

# Chapter 2. 통합 구현 (Integration Implementation)
