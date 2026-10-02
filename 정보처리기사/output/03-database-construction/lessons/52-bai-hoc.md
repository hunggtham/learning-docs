# 15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối relational data language với selection, projection, join và algebraic composition, để truy vấn được đọc như phép biến đổi quan hệ.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **21. 데이터 전환 및 정제 (Chuyển đổi dữ liệu - ETL)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

관계, 데이터, 언어

> **Chuyển mạch:** Ở chặng này của **15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **7. 집합연산자 및 조인 (Toán tử tập hợp và JOIN)**에서 만든 기준을 이어받아 **15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)**, **읽는 방법 (Cách đọc)** nêu điều cần giải thích; **15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)

Ở bước 52/54, **15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)** xuất hiện như phần tiếp nối của **7. 집합연산자 및 조인 (Toán tử tập hợp và JOIN)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng cho ta tiêu chí đối chiếu, còn công thức cho ta quan hệ giữa các đại lượng; hãy dùng cả hai để kiểm tra cùng một kết luận.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **일반 집합 연산자 (Toán tử tập hợp cơ bản)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **일반 집합 연산자 (Toán tử tập hợp cơ bản)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 일반 집합 연산자 (Toán tử tập hợp cơ bản)

Bây giờ ta đi vào nội dung của **일반 집합 연산자 (Toán tử tập hợp cơ bản)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “일반 집합 연산자 (Toán tử tập hợp cơ bản)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **합집합 (UNION, ∪):** Hợp (lấy tất cả, bỏ trùng lặp).
- **교집합 (INTERSECTION, ∩):** Giao (lấy phần chung).
- **차집합 (DIFFERENCE, —):** Hiệu (R - S: có trong R nhưng không có trong S).
- **교차곱 (CARTESIAN PRODUCT, Х):** Tích Đề-các (kết hợp tất cả các dòng của 2 bảng).

Các bullet của **일반 집합 연산자 (Toán tử tập hợp cơ bản)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **일반 집합 연산자 (Toán tử tập hợp cơ bản)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **순수 관계 연산자 (Toán tử quan hệ thuần túy)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **순수 관계 연산자 (Toán tử quan hệ thuần túy)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 순수 관계 연산자 (Toán tử quan hệ thuần túy)

Phần nguồn của **순수 관계 연산자 (Toán tử quan hệ thuần túy)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “순수 관계 연산자 (Toán tử quan hệ thuần túy)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

| 연산자 (Toán tử) | 기호 (Ký hiệu) | 설명 (Mô tả) |
|---|---|---|
| **Select (선택)** | **σ (Sigma)** | Lấy các **Hàng (Tuple)** thỏa mãn điều kiện (Phép toán nằm ngang - 수평). |
| **Project (추출)** | **π (Pi)** | Lấy các **Cột (Attribute)** được chỉ định, loại bỏ trùng lặp (Phép toán dọc - 수직). |
| **Join (조인)** | **⋈ (Bowtie)** | Kết hợp 2 bảng dựa trên thuộc tính chung. |
| **Division (나누기)** | **÷ (Divide)** | Trả về các 튜플 của bảng R mà khớp với tất cả giá trị thuộc tính của bảng S. |

> 💡 **Mẹo ghi nhớ:** **Se-Hàng, Pro-Cột** (Select = Hàng/Tuple, Project = Cột/Attribute).

---

Khi đọc **순수 관계 연산자 (Toán tử quan hệ thuần túy)**, hãy tách hai lớp: bảng giúp đối chiếu các loại hoặc tiêu chí, còn công thức cần được đọc theo biến, đơn vị và quan hệ giữa các đại lượng. Cách tách này giúp ta hiểu cơ chế trước khi ghi nhớ ký hiệu.

Điểm chốt của **순수 관계 연산자 (Toán tử quan hệ thuần túy)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Như vậy, **15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **21. 데이터 전환 및 정제 (Chuyển đổi dữ liệu - ETL)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

> **Bàn giao:** Sau **15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
