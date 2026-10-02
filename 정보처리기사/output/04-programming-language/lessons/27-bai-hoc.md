# 236. Python의 시퀀스 자료형 (Sequence Data Types in Python)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **236. Python의 시퀀스 자료형 (Sequence Data Types in Python)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối Python sequence types với indexing, slicing, mutability và iteration, để cấu trúc gắn với thao tác.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **236. Python의 시퀀스 자료형 (Sequence Data Types in Python)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **236. Python의 시퀀스 자료형 (Sequence Data Types in Python)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **264 - 274. 파이썬 문법 (Python Syntax & Basics)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **236. Python의 시퀀스 자료형 (Sequence Data Types in Python)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

시퀀스, 자료형

> **Chuyển mạch:** Ở chặng này của **236. Python의 시퀀스 자료형 (Sequence Data Types in Python)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **Python 기본 문법 (Python Basic Syntax)**에서 만든 기준을 이어받아 **236. Python의 시퀀스 자료형 (Sequence Data Types in Python)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **236. Python의 시퀀스 자료형 (Sequence Data Types in Python)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **236. Python의 시퀀스 자료형 (Sequence Data Types in Python)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **236. Python의 시퀀스 자료형 (Sequence Data Types in Python)**, **236. Python의 시퀀스 자료형 (Sequence Data Types in Python)** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 236. Python의 시퀀스 자료형 (Sequence Data Types in Python)

Từ **Python 기본 문법 (Python Basic Syntax)**, ta đã có điểm tựa để bước vào **236. Python의 시퀀스 자료형 (Sequence Data Types in Python)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 27/91 trước khi đi vào chi tiết.

Để đọc **236. Python의 시퀀스 자료형 (Sequence Data Types in Python)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **리스트(List)**, **튜플(Tuple)**, **range** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “236. Python의 시퀀스 자료형 (Sequence Data Types in Python)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 여러 값이 연속적으로 이어진 데이터 구조.
- **리스트(List)**: `[]` 사용. 데이터의 추가/삭제/변경이 자유로움 (Mutable).
- **튜플(Tuple)**: `()` 사용. 한 번 생성하면 데이터의 변경(수정/삭제)이 **불가능함** (Immutable). 읽기 전용에 적합.
- **range**: 반복문에서 연속된 숫자를 생성할 때 사용.

**Giải thích (Vietnamese):**
List và Tuple đều dùng để lưu danh sách. Nhưng List có thể sửa được, còn Tuple thì "Bất di bất dịch" (không thể thêm/xoá/sửa sau khi tạo).

---

Điểm chốt của **236. Python의 시퀀스 자료형 (Sequence Data Types in Python)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **264 - 274. 파이썬 문법 (Python Syntax & Basics)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

> **Bàn giao:** Sau **236. Python의 시퀀스 자료형 (Sequence Data Types in Python)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
