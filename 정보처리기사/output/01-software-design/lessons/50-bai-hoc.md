# 3. 결합도 (Coupling - Độ phụ thuộc)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **3. 결합도 (Coupling - Độ phụ thuộc)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **3. 결합도 (Coupling - Độ phụ thuộc)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **4. 응집도 (Cohesion - Độ gắn kết)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

결합도

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **10. 소프트웨어 설계 원리 (Software Design Principles)**에서 만든 기준을 이어받아 **3. 결합도 (Coupling - Độ phụ thuộc)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 3. 결합도 (Coupling - Độ phụ thuộc)

Sau khi đã đặt nền bằng **10. 소프트웨어 설계 원리 (Software Design Principles)**, ta chuyển sang **3. 결합도 (Coupling - Độ phụ thuộc)**. Đây là mắt xích 50/55 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **3. 결합도 (Coupling - Độ phụ thuộc)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

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

Ta có thể khép mục **3. 결합도 (Coupling - Độ phụ thuộc)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **4. 응집도 (Cohesion - Độ gắn kết)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.