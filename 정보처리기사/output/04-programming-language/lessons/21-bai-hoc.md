# 배열과 포인터 심화 (Arrays & Pointers - Advanced)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **배열과 포인터 심화 (Arrays & Pointers - Advanced)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **배열과 포인터 심화 (Arrays & Pointers - Advanced)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **075 - 077. 배열, 조건문, 반복문 (Arrays, Conditionals & Loops)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

배열과, 포인터, 심화

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **배열 심화 (Arrays - Advanced)**에서 만든 기준을 이어받아 **배열과 포인터 심화 (Arrays & Pointers - Advanced)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **배열과 포인터 심화 (Arrays & Pointers - Advanced)** và nối nó với **075 - 077. 배열, 조건문, 반복문 (Arrays, Conditionals & Loops)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 배열과 포인터 심화 (Arrays & Pointers - Advanced)

Từ **배열 심화 (Arrays - Advanced)**, ta đã có điểm tựa để bước vào **배열과 포인터 심화 (Arrays & Pointers - Advanced)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 21/91 trước khi đi vào chi tiết.

Để đọc **배열과 포인터 심화 (Arrays & Pointers - Advanced)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **260. 배열의 초기화 (Array Initialization / Khởi tạo mảng)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 260. 배열의 초기화 (Array Initialization / Khởi tạo mảng)

Các ý ngay dưới **260. 배열의 초기화 (Array Initialization / Khởi tạo mảng)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “260. 배열의 초기화 (Array Initialization / Khởi tạo mảng)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 배열 선언 시 초기값을 지정할 수 있다. (Có thể gán giá trị khởi tạo ngay khi khai báo mảng).
- 배열의 크기를 생략하려면 반드시 초기값을 지정해야 한다. (Nếu bỏ trống kích thước mảng trong ngoặc `[]`, bắt buộc phải có giá trị khởi tạo để máy tự đếm).
- 적은 수로 초기화하면 나머지 요소는 0이 입력된다. (Nếu khởi tạo ít phần tử hơn kích thước mảng, các phần tử còn lại tự động bằng 0).
  - *Example / Ví dụ*: `int a[5] = {3};` -> `[3, 0, 0, 0, 0]`.
  - 💡 *Mẹo ghi nhớ*: C/Java không tự làm sạch bộ nhớ trừ khi bạn khởi tạo ít nhất 1 phần tử.

Với **260. 배열의 초기화 (Array Initialization / Khởi tạo mảng)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **260. 배열의 초기화 (Array Initialization / Khởi tạo mảng)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **261. 배열 형태의 문자열 변수 (String as Array / Chuỗi dưới dạng mảng - Bổ sung)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **261. 배열 형태의 문자열 변수 (String as Array / Chuỗi dưới dạng mảng - Bổ sung)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 261. 배열 형태의 문자열 변수 (String as Array / Chuỗi dưới dạng mảng - Bổ sung)

Bây giờ ta đi vào nội dung của **261. 배열 형태의 문자열 변수 (String as Array / Chuỗi dưới dạng mảng - Bổ sung)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “261. 배열 형태의 문자열 변수 (String as Array / Chuỗi dưới dạng mảng - Bổ sung)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 배열에 문자열을 저장할 때는 초기값으로 지정해야 하며, 이미 선언된 배열에는 대입 연산자로 문자열을 통째로 저장할 수 없다. (Chỉ được gán chuỗi trực tiếp lúc khởi tạo. Không được gán chuỗi vào mảng đã khai báo bằng dấu `=`).
- `%s`를 이용해 문자열을 출력할 때는 배열 이름이나 포인터 변수만 적어주면 된다. (Khi in chuỗi bằng `%s`, chỉ cần truyền tên mảng hoặc con trỏ, không cần dấu `&`).

Các bullet của **261. 배열 형태의 문자열 변수 (String as Array / Chuỗi dưới dạng mảng - Bổ sung)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **261. 배열 형태의 문자열 변수 (String as Array / Chuỗi dưới dạng mảng - Bổ sung)**, đừng bắt đầu lại từ số không. **262. 포인터와 포인터 변수 (Pointer & Pointer Variable / Con trỏ - Bổ sung)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **262. 포인터와 포인터 변수 (Pointer & Pointer Variable / Con trỏ - Bổ sung)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 262. 포인터와 포인터 변수 (Pointer & Pointer Variable / Con trỏ - Bổ sung)

Phần nguồn của **262. 포인터와 포인터 변수 (Pointer & Pointer Variable / Con trỏ - Bổ sung)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “262. 포인터와 포인터 변수 (Pointer & Pointer Variable / Con trỏ - Bổ sung)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 포인터 변수는 동적으로 할당되는 메모리 영역인 **힙(Heap) 영역**에 접근하는 동적 변수이다. (Con trỏ là biến động truy cập vào vùng nhớ Heap được cấp phát động).
- `*` 연산자: 간접 연산자 (Lấy giá trị).
- `&` 연산자: 번지 연산자 (Lấy địa chỉ).
  - 💡 *Mẹo ghi nhớ*: Con trỏ giống như tấm bản đồ (chỉ chứa địa chỉ), dùng `*` để đi đến đích và lấy kho báu (giá trị).

Các bullet của **262. 포인터와 포인터 변수 (Pointer & Pointer Variable / Con trỏ - Bổ sung)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**262. 포인터와 포인터 변수 (Pointer & Pointer Variable / Con trỏ - Bổ sung)** vừa cho ta cách đặt câu hỏi. Bây giờ **263. 포인터와 배열 (Pointer & Array / Con trỏ và mảng - Bổ sung)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Đoạn **263. 포인터와 배열 (Pointer & Array / Con trỏ và mảng - Bổ sung)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 263. 포인터와 배열 (Pointer & Array / Con trỏ và mảng - Bổ sung)

Các ý ngay dưới **263. 포인터와 배열 (Pointer & Array / Con trỏ và mảng - Bổ sung)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “263. 포인터와 배열 (Pointer & Array / Con trỏ và mảng - Bổ sung)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `p + 1`은 메모리 주소가 1 증가하는 것이 아니라 해당 자료형의 크기(int는 4Byte)만큼 증가한다. (`p + 1` không cộng thêm 1 vào địa chỉ, mà cộng thêm kích thước của kiểu dữ liệu, ví dụ int thì cộng thêm 4 Bytes).
  - *Example / Ví dụ*: `p` là `1000` -> `p + 1` là `1004` (với int).

Các ý về **263. 포인터와 배열 (Pointer & Array / Con trỏ và mảng - Bổ sung)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Với **263. 포인터와 배열 (Pointer & Array / Con trỏ và mảng - Bổ sung)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Điểm chốt của **배열과 포인터 심화 (Arrays & Pointers - Advanced)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **075 - 077. 배열, 조건문, 반복문 (Arrays, Conditionals & Loops)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.