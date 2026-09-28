# 2. 자원 처리 오류 (Resource Handling Errors)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **2. 자원 처리 오류 (Resource Handling Errors)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

자원, 처리, 오류

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **⦁ 코드 오류 및 API 오용 (Lỗi mã nguồn & Dùng sai API)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **5. 네트워크 및 인프라 기술 (Công nghệ Mạng & Hạ tầng)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **2. 자원 처리 오류 (Resource Handling Errors)** và nối nó với **5. 네트워크 및 인프라 기술 (Công nghệ Mạng & Hạ tầng)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 2. 자원 처리 오류 (Resource Handling Errors)
- **부적절한 자원 해제 (Improper Resource Release)**: 힙 메모리나 소켓을 사용 후 반환(close)하지 않아 자원 고갈 발생. (Không giải phóng bộ nhớ, kết nối sau khi dùng xong).
- **해제된 자원 사용 (Use After Free)**: 반환된 메모리를 다시 참조하여 오작동 유발. (Dùng lại vùng nhớ đã được giải phóng).
- **초기화되지 않은 변수 사용 (Uninitialized Variable)**: 변수 선언 후 값을 넣지 않고 사용하여 이전 쓰레기 값이 노출됨. (Dùng biến chưa khởi tạo giá trị).
