# 10. 코드 (Code) 개요 & 종류

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **10. 코드 (Code) 개요 & 종류**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối code với source, build artifact, runtime và maintenance, để loại mã được đọc theo vòng đời.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **10. 코드 (Code) 개요 & 종류**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **10. 코드 (Code) 개요 & 종류** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **phần tổng hợp của môn** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **10. 코드 (Code) 개요 & 종류**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

코드

> **Chuyển mạch:** Ở chặng này của **10. 코드 (Code) 개요 & 종류**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **8. 재사용 (Reuse)**에서 만든 기준을 이어받아 **10. 코드 (Code) 개요 & 종류**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **10. 코드 (Code) 개요 & 종류**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. 코드 (Code) 개요 & 종류** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **10. 코드 (Code) 개요 & 종류**, **10. 코드 (Code) 개요 & 종류** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 10. 코드 (Code) 개요 & 종류

Từ **8. 재사용 (Reuse)**, ta đã có điểm tựa để bước vào **10. 코드 (Code) 개요 & 종류**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 69/69 trước khi đi vào chi tiết.

Để đọc **10. 코드 (Code) 개요 & 종류** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

**개념 (Khái niệm):** 데이터를 식별, 분류, 배열하기 위해 사용하는 기호 (Ký hiệu dùng để nhận dạng, phân loại và sắp xếp dữ liệu).

*   **기능 (Chức năng):** 식별(Nhận dạng), 분류(Phân loại), 배열(Sắp xếp), 표준화(Chuẩn hóa), 간소화(Đơn giản hóa).
*   **종류 (Các loại Code):**
    1.  **순차 코드 (Sequential):** 발생 순서대로 일련번호 부여 (Đánh số thứ tự 1, 2, 3...).
    2.  **블록 코드 (Block):** 공통성 있는 항목을 블록으로 묶음 (Phân khối theo nhóm chung).
    3.  **10진 코드 (Decimal):** 0~9까지 10진 분할 반복, 도서분류 (Phân loại thập phân như sách thư viện).
    4.  **그룹 분류 코드 (Group Classification):** 대/중/소분류 (Phân nhóm lớn/vừa/nhỏ như 1-01-001).
    5.  **연상 코드 (Mnemonic):** 명칭이나 약호와 관계있는 기호 (Mã gợi nhớ, ví dụ: TV-40 cho Tivi 40 inch).
    6.  **표의 숫자 코드 (Significant Digit):** 물리적 수치를 직접 적용 (Dùng kích thước vật lý làm mã).
    7.  **합성 코드 (Combined):** 2개 이상 조합 (Kết hợp nhiều mã).

*   **코드 부여 체계 (Code Assignment System):**
    *   **Korean:** 이름만으로 개체의 용도와 적용 범위를 알 수 있게 상세 명시 (자릿수, 구분자).
    *   **VI (Vietnamese) (Tiếng Việt):** Hệ thống đánh mã sao cho nhìn vào tên mã là biết ngay công dụng và phạm vi (cần nêu rõ số chữ số, dấu phân cách).
    *   **Example:** 연도(00) + 학과(00) + 개인번호(000) -> 2401001.

---

Khép lại **10. 코드 (Code) 개요 & 종류**, điều cần giữ lại là mối quan hệ giữa mục đích, cơ chế và điểm giới hạn của các khái niệm trong nguồn. Khi ôn lại, hãy tự giải thích chúng bằng một câu hoàn chỉnh rồi đối chiếu với các điểm dễ nhầm trước khi chuyển sang bài tổng hợp của môn.

> **Bàn giao:** Sau **10. 코드 (Code) 개요 & 종류**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
