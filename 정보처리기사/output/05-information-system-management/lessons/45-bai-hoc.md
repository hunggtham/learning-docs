# Python의 기본 문법 (Python Basic Syntax)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Python의 기본 문법 (Python Basic Syntax)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối Python syntax với variable, control flow, collection và function, để cú pháp gắn với runtime.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **Python의 기본 문법 (Python Basic Syntax)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **Python의 기본 문법 (Python Basic Syntax)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **Python 데이터 입·출력 함수 (Python Input/Output Functions)** khi chuyển sang phần tiếp theo.

> **Nối mạch:** Trong **Python의 기본 문법 (Python Basic Syntax)**, **핵심 키워드 (Từ khóa)** nối từ **학습 목표 (Mục tiêu)** sang **선행·연결 개념 (Kiến thức liên kết)**, vì mục tiêu đặt câu hỏi trung tâm còn từ khóa thu hẹp phạm vi cần kiểm tra.

## 핵심 키워드 (Từ khóa)

기본, 문법

> **Nối mạch:** Ở chặng này của **Python의 기본 문법 (Python Basic Syntax)**, **선행·연결 개념 (Kiến thức liên kết)** nối từ **핵심 키워드 (Từ khóa)** sang **읽는 방법 (Cách đọc)**, đồng thời chỉ rõ tài liệu chuẩn và vị trí sở hữu để biết chỗ đào sâu tiếp.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **포인터와 배열 (Pointer and Array)**에서 만든 기준을 이어받아 **Python의 기본 문법 (Python Basic Syntax)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Python의 기본 문법 (Python Basic Syntax)**, **읽는 방법 (Cách đọc)** nối từ **선행·연결 개념 (Kiến thức liên kết)** sang phần giải thích chính, vì tiêu chí đọc cần biến điểm tựa trước đó thành cách kiểm tra điều kiện và hệ quả.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Nối mạch:** Trong **Python의 기본 문법 (Python Basic Syntax)**, phần giải thích chính nối từ **읽는 방법 (Cách đọc)** sang các quy tắc và ví dụ, vì tiêu chí đọc vừa đặt ra sẽ giúp kiểm tra cú pháp theo điều kiện và hệ quả.

## Python의 기본 문법 (Python Basic Syntax)

Từ **포인터와 배열 (Pointer and Array)**, ta đã có điểm tựa để bước vào **Python의 기본 문법 (Python Basic Syntax)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 45/86 trước khi đi vào chi tiết.

Để đọc **Python의 기본 문법 (Python Basic Syntax)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “Python의 기본 문법 (Python Basic Syntax)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **특징**:
  - 변수의 자료형(Data Type/Kiểu dữ liệu)에 대한 선언이 없습니다.
  - 문장의 끝을 의미하는 세미콜론(`;`)을 사용할 필요가 없습니다.
  - 변수에 연속하여 값을 저장하는 것이 가능합니다. (예: `x, y, z = 10, 20, 30`)
  - `if`나 `for`와 같이 코드 블록(Code Block/Khối lệnh)을 포함하는 명령문을 작성할 때, 콜론(`:`)과 여백(Indentation/Thụt lề)으로 구분합니다.
  - 여백은 일반적으로 4칸 또는 한 개의 탭(Tab)만큼 띄워야 하며, 같은 수준의 코드들은 반드시 동일한 여백을 가져야 합니다.

> **Vietnamese Explanation**:
> Khác với C hay Java, Python không cần khai báo kiểu dữ liệu cho biến, không cần dấu chấm phẩy `;` ở cuối dòng. Python dùng khoảng trắng (thụt lề) để phân chia các khối lệnh thay vì dùng dấu ngoặc nhọn `{}`.

**예시 / Ví dụ:**
```python
x, y = 10, 20
if x < y:
    print("x is smaller") # Thụt lề 4 khoảng trắng
```

💡 **Mẹo ghi nhớ (Mnemonics):**
**P.I.T** - **P**ython **I**ndents **T**hings (Python thụt lề mọi thứ).

Điểm chốt của **Python의 기본 문법 (Python Basic Syntax)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **Python 데이터 입·출력 함수 (Python Input/Output Functions)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

> **Bàn giao:** Sau **Python의 기본 문법 (Python Basic Syntax)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
