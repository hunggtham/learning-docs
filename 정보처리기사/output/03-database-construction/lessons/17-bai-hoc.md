# 123-125. 정규화 (Normalization)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **123-125. 정규화 (Normalization)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

정규화

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **116-121. 관계대수 (Relational Algebra)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **179-182. 정규화와 이상 심화 (Normalization & Anomaly - Deep Dive)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **123-125. 정규화 (Normalization)** và nối nó với **179-182. 정규화와 이상 심화 (Normalization & Anomaly - Deep Dive)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 123-125. 정규화 (Normalization)
- 데이터 중복을 배제하여 이상(Anomaly: 삽입, 삭제, 갱신 이상) 발생을 방지하는 과정. 논리적 설계 단계에서 수행.
- **1NF:** 도메인이 원자값 (Domain is Atomic).
- **2NF:** 부분적 함수 종속 제거 (Remove Partial Dependency).
- **3NF:** 이행적 함수 종속 제거 (Remove Transitive Dependency).
- **BCNF:** 결정자이면서 후보키가 아닌 것 제거.
- **4NF:** 다치 종속 제거 (Remove Multivalued Dependency).
- **5NF:** 조인 종속성 이용.
- **VI (Vietnamese) (Tiếng Việt):** Chuẩn hóa. Giảm thiểu dư thừa dữ liệu để ngăn ngừa dị thường (Anomaly).
- 💡 **Mẹo ghi nhớ:** Nguyên-Phần-Bắc-Quyết-Đa-Chung (Nguyên tử -> Từng phần -> Bắc cầu -> Quyết định -> Đa trị -> Chung).
