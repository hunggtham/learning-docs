# 3. 결합도 (Coupling - Độ phụ thuộc)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **3. 결합도 (Coupling - Độ phụ thuộc)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

결합도

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 3. 결합도 (Coupling - Độ phụ thuộc)
**개념 (Khái niệm):** 모듈 간의 의존성 정도 (Mức độ phụ thuộc giữa các module với nhau). **낮을수록 좋음 (Càng thấp càng tốt).**

순서 (Từ Tốt nhất đến Xấu nhất): **자료(Data) -> 스탬프(Stamp) -> 제어(Control) -> 외부(External) -> 공통(Common) -> 내용(Content)**
💡 **Mẹo ghi nhớ:** T-S-C-N-C-N (Data-Stamp-Control-External-Common-Content) -> **Tính Sao Cho Nhẹ Cả Người**

1.  **자료 결합도 (Data Coupling) - TỐT NHẤT:**
    *   **Korean:** 파라미터(자료 요소)만 전달.
    *   **VI (Vietnamese) (Tiếng Việt):** Chỉ truyền tham số dữ liệu cần thiết.
    *   **Example:** `sum(a, b)` truyền đúng 2 số a, b.
2.  **스탬프 결합도 (Stamp Coupling):**
    *   **Korean:** 배열/레코드 등 자료구조가 전달됨.
    *   **VI (Vietnamese) (Tiếng Việt):** Truyền toàn bộ cấu trúc dữ liệu (mảng, đối tượng) nhưng chỉ dùng 1 phần.
    *   **Example:** Truyền đối tượng `User` nhưng chỉ dùng `User.name`.
3.  **제어 결합도 (Control Coupling):**
    *   **Korean:** 제어 신호(Flag)를 전달하여 모듈 흐름 제어.
    *   **VI (Vietnamese) (Tiếng Việt):** Truyền cờ điều khiển (flag, boolean) can thiệp vào logic của module khác.
    *   **Example:** Truyền `isExpress=true` để quyết định cách xử lý.
4.  **외부 결합도 (External Coupling):**
    *   **Korean:** 외부 변수/데이터 참조.
    *   **VI (Vietnamese) (Tiếng Việt):** Cùng phụ thuộc vào dữ liệu / file / thiết bị bên ngoài.
    *   **Example:** Hai module dùng chung một file `config.txt`.
5.  **공통 결합도 (Common Coupling):**
    *   **Korean:** 공통 데이터 영역(전역 변수) 공유.
    *   **VI (Vietnamese) (Tiếng Việt):** Nhiều module dùng chung biến toàn cục (global variables).
    *   **Example:** Sử dụng `public static int totalCount` chung.
6.  **내용 결합도 (Content Coupling) - XẤU NHẤT:**
    *   **Korean:** 내부 기능/자료 직접 참조. 스파게티 코드.
    *   **VI (Vietnamese) (Tiếng Việt):** Truy cập, sửa đổi trực tiếp dữ liệu/logic nội bộ của module khác.
    *   **Example:** `moduleB.internalValue = 10` từ module A.

---
