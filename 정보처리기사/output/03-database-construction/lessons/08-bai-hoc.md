# 12. 관계형 데이터 모델과 릴레이션 (Mô hình dữ liệu quan hệ & Relation)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **12. 관계형 데이터 모델과 릴레이션 (Mô hình dữ liệu quan hệ & Relation)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

관계형, 데이터, 모델과, 릴레이션

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 12. 관계형 데이터 모델과 릴레이션 (Mô hình dữ liệu quan hệ & Relation)

### 12.1 릴레이션의 구조 (Cấu trúc Relation / Bảng)
- **릴레이션 (Relation):** Bảng dữ liệu gồm hàng và cột.
- **튜플 (Tuple):** Hàng (Row / Record).
- **속성 (Attribute):** Cột (Column / Field).
- **차수 (Degree / 디그리):** Số lượng thuộc tính (Cột).
- **카디널리티 (Cardinality):** Số lượng 튜플 (Hàng).
- **도메인 (Domain):** Tập hợp các giá trị nguyên tử (Atomic) mà một thuộc tính có thể nhận.
- **인스턴스 (Instance):** Tập hợp các 튜플 tại một thời điểm (Dữ liệu thực tế).

> 💡 **Mẹo ghi nhớ:** **Car-Tu, De-At** (Cardinality = Tuple/Hàng, Degree = Attribute/Cột).

### 12.2 릴레이션의 특징 (Đặc điểm của Relation)
- **튜플의 유일성:** Không có 2 hàng nào giống hệt nhau.
- **튜플/속성의 무순서:** Thứ tự của các hàng và các cột **không quan trọng**.
- **원자값:** Mỗi ô (giao giữa hàng và cột) chỉ được chứa một giá trị duy nhất (không thể chia nhỏ).

---
