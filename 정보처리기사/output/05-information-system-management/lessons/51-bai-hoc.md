# 1. 메모리 버퍼 오버플로 (Memory Buffer Overflow / Tràn bộ đệm bộ nhớ)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **1. 메모리 버퍼 오버플로 (Memory Buffer Overflow / Tràn bộ đệm bộ nhớ)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

메모리, 버퍼, 오버플로

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 1. 메모리 버퍼 오버플로 (Memory Buffer Overflow / Tràn bộ đệm bộ nhớ)
- **개념**: 연속된 메모리 공간을 사용하는 프로그램에서 할당된 메모리의 범위를 넘어선 위치에서 자료를 읽거나 쓰려고 할 때 발생하는 취약점.
- **Tiếng Việt**: Lỗ hổng xảy ra khi chương trình ghi hoặc đọc dữ liệu vượt quá giới hạn vùng nhớ đã được cấp phát.
- **예시 (Example)**:
  - (KR) 10바이트 공간에 20바이트의 데이터를 입력하면 다른 메모리 영역을 침범함.
  - (VN) Nhập 20 byte dữ liệu vào mảng chỉ có kích thước 10 byte, làm ghi đè lên các vùng nhớ khác.
- **대책**: 버퍼의 크기를 적절히 설정.
- 💡 **Mẹo ghi nhớ**: Buffer Overflow = Bơm nước quá đầy làm tràn ly.
