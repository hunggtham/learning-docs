# 284 & 294. 구역성 (Locality / Tính cục bộ)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **284 & 294. 구역성 (Locality / Tính cục bộ)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **284 & 294. 구역성 (Locality / Tính cục bộ)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **285 & 295. 워킹 셋 (Working Set / Tập làm việc)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

구역성

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **인터프리터 언어 (Interpreter Languages / Ngôn ngữ thông dịch)**에서 만든 기준을 이어받아 **284 & 294. 구역성 (Locality / Tính cục bộ)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **284 & 294. 구역성 (Locality / Tính cục bộ)** và nối nó với **285 & 295. 워킹 셋 (Working Set / Tập làm việc)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 284 & 294. 구역성 (Locality / Tính cục bộ)

Sau khi đã đặt nền bằng **인터프리터 언어 (Interpreter Languages / Ngôn ngữ thông dịch)**, ta chuyển sang **284 & 294. 구역성 (Locality / Tính cục bộ)**. Đây là mắt xích 74/78 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **284 & 294. 구역성 (Locality / Tính cục bộ)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **개념 (Khái niệm)**, **핵심 키워드 (Từ khóa)**, **시험 포인트 (Điểm thi)**, **한 문장 설명 (Tóm tắt)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **TẦNG A – NOTE NÉN (ÔN / ĐI THI)**. Hãy xác định **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### TẦNG A – NOTE NÉN (ÔN / ĐI THI)

Phần nguồn của **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **개념 (Khái niệm)**: 프로세스가 실행되는 동안 주기억장치(Main memory)의 특정 영역만을 집중적으로 참조하는 성질. (Tính chất mà quá trình chỉ tham chiếu tập trung vào một số trang nhất định của bộ nhớ chính khi thực thi.)
- **핵심 키워드 (Từ khóa)**: 시간 구역성 (Temporal locality), 공간 구역성 (Spatial locality), 집중 참조 (Concentrated reference).
- **시험 포인트 (Điểm thi)**: 시간 구역성(Loop, Stack)과 공간 구역성(Array)의 구체적인 사례를 구분하는 것. (Phân biệt ví dụ của cục bộ thời gian và cục bộ không gian.)
- **한 문장 설명 (Tóm tắt)**: 스래싱(Thrashing) 방지를 위한 핵심 이론. (Lý thuyết cốt lõi để ngăn chặn hiện tượng Thrashing.)

Các ý về **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **TẦNG B – NOTE 보충 (HIỂU SÂU)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **TẦNG B – NOTE 보충 (HIỂU SÂU)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### TẦNG B – NOTE 보충 (HIỂU SÂU)

Các ý ngay dưới **TẦNG B – NOTE 보충 (HIỂU SÂU)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- **시간 구역성 (Temporal locality)**: 한 번 참조된 페이지는 가까운 시간 내에 다시 참조될 가능성이 높음. (Trang vừa dùng sẽ có khả năng cao được dùng lại sớm. Ví dụ: Vòng lặp/Loop, Ngăn xếp/Stack, Biến đếm.)
- **공간 구역성 (Spatial locality)**: 특정 페이지가 참조되면 인근 위치의 페이지가 계속 참조될 가능성이 높음. (Trang vừa dùng thì các trang liền kề nó dễ được gọi theo. Ví dụ: Mảng/Array, duyệt tuần tự.)
- **예시 (Ví dụ)**: 배열 `A[0]`부터 `A[100]`까지 순서대로 읽는 것은 공간 구역성이고, `for`문 안에서 변수 `i`를 계속 증가시키며 쓰는 것은 시간 구역성. (Đọc mảng theo thứ tự là cục bộ không gian; dùng biến i nhiều lần trong vòng lặp là cục bộ thời gian.)
- 💡 **Mẹo ghi nhớ**: **T**emporal = **T**ime (Lặp lại nhiều lần/Loop), **S**patial = **S**pace (Gần nhau/Array).

Với **TẦNG B – NOTE 보충 (HIỂU SÂU)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **TẦNG B – NOTE 보충 (HIỂU SÂU)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **284 & 294. 구역성 (Locality / Tính cục bộ)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **285 & 295. 워킹 셋 (Working Set / Tập làm việc)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.