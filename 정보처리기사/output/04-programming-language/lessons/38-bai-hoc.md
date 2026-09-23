# 289 - 296. 메모리 관리 및 가상 기억장치 (Memory Management)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **289 - 296. 메모리 관리 및 가상 기억장치 (Memory Management)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

메모리, 관리, 가상, 기억장치

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 289 - 296. 메모리 관리 및 가상 기억장치 (Memory Management)
- **배치 전략 (Placement)**: 최초 적합(First Fit, 빠름), 최적 적합(Best Fit, 단편화 최소), 최악 적합(Worst Fit, 큰 공간 남김).
- **페이징(Paging)**: 메모리를 **동일한 고정 크기**로 나눔. **내부 단편화** 발생 (빈 공간이 남아버림).
- **세그먼테이션(Segmentation)**: 논리적 의미(함수 등)에 따라 **가변 크기**로 나눔. **외부 단편화** 발생 (공간이 작아서 못 들어감).
- **페이지 크기**: 페이지가 작으면 내부 단편화는 줄지만, 맵 테이블이 커져 매핑 속도가 느려짐.
- **스래싱 (Thrashing)**: 빈번한 페이지 교체로 인해 시스템 처리량보다 교체 시간이 더 많아져 CPU 이용률이 급감하는 마비 상태.

**Giải thích (Vietnamese):**
- Paging (Phân trang): Cắt bánh thành các miếng bằng nhau. Điểm yếu: Ăn không hết 1 miếng sẽ dư thừa (Nội phân mảnh).
- Segmentation (Phân đoạn): Cắt bánh theo sức ăn của mỗi người (to nhỏ khác nhau). Điểm yếu: Chừa lại các khoảng trống lắt nhắt không ai nhét vừa (Ngoại phân mảnh).
- Thrashing: Máy quá tải, giật lag do mải lấy dữ liệu từ ổ cứng đắp vào RAM.

---
