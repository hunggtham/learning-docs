# 12. 관계형 데이터 모델과 릴레이션 (Mô hình dữ liệu quan hệ & Relation)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **12. 관계형 데이터 모델과 릴레이션 (Mô hình dữ liệu quan hệ & Relation)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **12. 관계형 데이터 모델과 릴레이션 (Mô hình dữ liệu quan hệ & Relation)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **13. 데이터 모델과 E-R 다이어그램 (Mô hình dữ liệu & Biểu đồ E-R)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

관계형, 데이터, 모델과, 릴레이션

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **168-172. 관계형 데이터 모델 및 E-R 모델 심화 (Relational & E-R Model Deep Dive)**에서 만든 기준을 이어받아 **12. 관계형 데이터 모델과 릴레이션 (Mô hình dữ liệu quan hệ & Relation)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **12. 관계형 데이터 모델과 릴레이션 (Mô hình dữ liệu quan hệ & Relation)** và nối nó với **13. 데이터 모델과 E-R 다이어그램 (Mô hình dữ liệu & Biểu đồ E-R)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 12. 관계형 데이터 모델과 릴레이션 (Mô hình dữ liệu quan hệ & Relation)

Sau khi đã đặt nền bằng **168-172. 관계형 데이터 모델 및 E-R 모델 심화 (Relational & E-R Model Deep Dive)**, ta chuyển sang **12. 관계형 데이터 모델과 릴레이션 (Mô hình dữ liệu quan hệ & Relation)**. Đây là mắt xích 8/56 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **12. 관계형 데이터 모델과 릴레이션 (Mô hình dữ liệu quan hệ & Relation)** như một bài học cho người mới, hãy giữ câu hỏi: **ta dùng mô hình nào để biểu diễn đối tượng, quan hệ hoặc hành vi, và giới hạn của mỗi cách là gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **12.1 릴레이션의 구조 (Cấu trúc Relation / Bảng)**. Hãy xác định **12.1 릴레이션의 구조 (Cấu trúc Relation / Bảng)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 12.1 릴레이션의 구조 (Cấu trúc Relation / Bảng)

Phần nguồn của **12.1 릴레이션의 구조 (Cấu trúc Relation / Bảng)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **릴레이션 (Relation):** Bảng dữ liệu gồm hàng và cột.
- **튜플 (Tuple):** Hàng (Row / Record).
- **속성 (Attribute):** Cột (Column / Field).
- **차수 (Degree / 디그리):** Số lượng thuộc tính (Cột).
- **카디널리티 (Cardinality):** Số lượng 튜플 (Hàng).
- **도메인 (Domain):** Tập hợp các giá trị nguyên tử (Atomic) mà một thuộc tính có thể nhận.
- **인스턴스 (Instance):** Tập hợp các 튜플 tại một thời điểm (Dữ liệu thực tế).

> 💡 **Mẹo ghi nhớ:** **Car-Tu, De-At** (Cardinality = Tuple/Hàng, Degree = Attribute/Cột).

Với **12.1 릴레이션의 구조 (Cấu trúc Relation / Bảng)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **12.1 릴레이션의 구조 (Cấu trúc Relation / Bảng)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **12.2 릴레이션의 특징 (Đặc điểm của Relation)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **12.2 릴레이션의 특징 (Đặc điểm của Relation)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 12.2 릴레이션의 특징 (Đặc điểm của Relation)

Các ý ngay dưới **12.2 릴레이션의 특징 (Đặc điểm của Relation)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- **튜플의 유일성:** Không có 2 hàng nào giống hệt nhau.
- **튜플/속성의 무순서:** Thứ tự của các hàng và các cột **không quan trọng**.
- **원자값:** Mỗi ô (giao giữa hàng và cột) chỉ được chứa một giá trị duy nhất (không thể chia nhỏ).

---

Các bullet của **12.2 릴레이션의 특징 (Đặc điểm của Relation)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **12.2 릴레이션의 특징 (Đặc điểm của Relation)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **12. 관계형 데이터 모델과 릴레이션 (Mô hình dữ liệu quan hệ & Relation)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **13. 데이터 모델과 E-R 다이어그램 (Mô hình dữ liệu & Biểu đồ E-R)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.