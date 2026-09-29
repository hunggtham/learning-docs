# 7. 공통 모듈 (Common Module)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **7. 공통 모듈 (Common Module)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **7. 공통 모듈 (Common Module)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **9. 효과적인 모듈 설계 방안 (Effective Module Design)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

공통, 모듈

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **2. 모듈 (Module) & 독립성 (Independence)**에서 만든 기준을 이어받아 **7. 공통 모듈 (Common Module)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 7. 공통 모듈 (Common Module)

Từ **2. 모듈 (Module) & 독립성 (Independence)**, ta đã có điểm tựa để bước vào **7. 공통 모듈 (Common Module)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 33/55 trước khi đi vào chi tiết.

Để đọc **7. 공통 모듈 (Common Module)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

**개념 (Khái niệm):** 여러 프로그램에서 공통적으로 사용할 수 있는 모듈 (Module dùng chung cho nhiều chương trình, ví dụ: Đăng nhập, tính toán).

*   **명세 기법 5가지 (5 nguyên tắc viết đặc tả module):**
    1.  **정확성 (Correctness):** 정확히 작성 (Chính xác).
    2.  **명확성 (Clarity):** 중의적이지 않게 (Rõ ràng, không mơ hồ).
    3.  **완전성 (Completeness):** 모든 것을 빠짐없이 (Đầy đủ).
    4.  **일관성 (Consistency):** 상호 충돌 없게 (Nhất quán).
    5.  **추적성 (Traceability):** 출처, 관계 추적 가능 (Có thể truy xuất nguồn gốc).
💡 **Mẹo ghi nhớ:** C-M-H-N-T (Chính-Rõ-Đủ-Nhất-Truy) -> **Chỉ Mong Học Nhất Trường**

---

Điểm chốt của **7. 공통 모듈 (Common Module)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **9. 효과적인 모듈 설계 방안 (Effective Module Design)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.