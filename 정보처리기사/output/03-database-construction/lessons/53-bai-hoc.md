# 15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **21. 데이터 전환 및 정제 (Chuyển đổi dữ liệu - ETL)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

관계, 데이터, 언어

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **7. 집합연산자 및 조인 (Toán tử tập hợp và JOIN)**에서 만든 기준을 이어받아 **15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)

Sau khi đã đặt nền bằng **7. 집합연산자 및 조인 (Toán tử tập hợp và JOIN)**, ta chuyển sang **15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)**. Đây là mắt xích 53/55 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng cho ta tiêu chí đối chiếu, còn công thức cho ta quan hệ giữa các đại lượng; hãy dùng cả hai để kiểm tra cùng một kết luận.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **일반 집합 연산자 (Toán tử tập hợp cơ bản)**. Hãy xác định **일반 집합 연산자 (Toán tử tập hợp cơ bản)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 일반 집합 연산자 (Toán tử tập hợp cơ bản)

Phần nguồn của **일반 집합 연산자 (Toán tử tập hợp cơ bản)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **합집합 (UNION, ∪):** Hợp (lấy tất cả, bỏ trùng lặp).
- **교집합 (INTERSECTION, ∩):** Giao (lấy phần chung).
- **차집합 (DIFFERENCE, —):** Hiệu (R - S: có trong R nhưng không có trong S).
- **교차곱 (CARTESIAN PRODUCT, Х):** Tích Đề-các (kết hợp tất cả các dòng của 2 bảng).

Các bullet của **일반 집합 연산자 (Toán tử tập hợp cơ bản)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **일반 집합 연산자 (Toán tử tập hợp cơ bản)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **순수 관계 연산자 (Toán tử quan hệ thuần túy)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **순수 관계 연산자 (Toán tử quan hệ thuần túy)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 순수 관계 연산자 (Toán tử quan hệ thuần túy)

Các ý ngay dưới **순수 관계 연산자 (Toán tử quan hệ thuần túy)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

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

Ta có thể khép mục **15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **21. 데이터 전환 및 정제 (Chuyển đổi dữ liệu - ETL)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.