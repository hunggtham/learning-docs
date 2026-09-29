# 15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **21. 데이터 전환 및 정제 (Chuyển đổi dữ liệu - ETL)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

관계, 데이터, 언어

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **7. 집합연산자 및 조인 (Toán tử tập hợp và JOIN)**에서 만든 기준을 이어받아 **15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)** và nối nó với **21. 데이터 전환 및 정제 (Chuyển đổi dữ liệu - ETL)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)

Từ **7. 집합연산자 및 조인 (Toán tử tập hợp và JOIN)**, ta đã có điểm tựa để bước vào **15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 54/56 trước khi đi vào chi tiết.

Để đọc **15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng cho ta tiêu chí đối chiếu, còn công thức cho ta quan hệ giữa các đại lượng; hãy dùng cả hai để kiểm tra cùng một kết luận.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **일반 집합 연산자 (Toán tử tập hợp cơ bản)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 일반 집합 연산자 (Toán tử tập hợp cơ bản)

Các ý ngay dưới **일반 집합 연산자 (Toán tử tập hợp cơ bản)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- **합집합 (UNION, ∪):** Hợp (lấy tất cả, bỏ trùng lặp).
- **교집합 (INTERSECTION, ∩):** Giao (lấy phần chung).
- **차집합 (DIFFERENCE, —):** Hiệu (R - S: có trong R nhưng không có trong S).
- **교차곱 (CARTESIAN PRODUCT, Х):** Tích Đề-các (kết hợp tất cả các dòng của 2 bảng).

Các bullet của **일반 집합 연산자 (Toán tử tập hợp cơ bản)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **일반 집합 연산자 (Toán tử tập hợp cơ bản)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **순수 관계 연산자 (Toán tử quan hệ thuần túy)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **순수 관계 연산자 (Toán tử quan hệ thuần túy)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 순수 관계 연산자 (Toán tử quan hệ thuần túy)

Bây giờ ta đi vào nội dung của **순수 관계 연산자 (Toán tử quan hệ thuần túy)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

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

Điểm chốt của **15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **21. 데이터 전환 및 정제 (Chuyển đổi dữ liệu - ETL)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.