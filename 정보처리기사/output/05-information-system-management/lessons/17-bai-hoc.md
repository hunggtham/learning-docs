# 2. 자원 처리 오류 (Resource Handling Errors)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **2. 자원 처리 오류 (Resource Handling Errors)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **2. 자원 처리 오류 (Resource Handling Errors)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **5. 네트워크 및 인프라 기술 (Công nghệ Mạng & Hạ tầng)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

자원, 처리, 오류

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **⦁ 코드 오류 및 API 오용 (Lỗi mã nguồn & Dùng sai API)**에서 만든 기준을 이어받아 **2. 자원 처리 오류 (Resource Handling Errors)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **2. 자원 처리 오류 (Resource Handling Errors)** và nối nó với **5. 네트워크 및 인프라 기술 (Công nghệ Mạng & Hạ tầng)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 2. 자원 처리 오류 (Resource Handling Errors)

Sau khi đã đặt nền bằng **⦁ 코드 오류 및 API 오용 (Lỗi mã nguồn & Dùng sai API)**, ta chuyển sang **2. 자원 처리 오류 (Resource Handling Errors)**. Đây là mắt xích 17/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **2. 자원 처리 오류 (Resource Handling Errors)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **부적절한 자원 해제 (Improper Resource Release)**, **해제된 자원 사용 (Use After Free)**, **초기화되지 않은 변수 사용 (Uninitialized Variable)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “2. 자원 처리 오류 (Resource Handling Errors)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **부적절한 자원 해제 (Improper Resource Release)**: 힙 메모리나 소켓을 사용 후 반환(close)하지 않아 자원 고갈 발생. (Không giải phóng bộ nhớ, kết nối sau khi dùng xong).
- **해제된 자원 사용 (Use After Free)**: 반환된 메모리를 다시 참조하여 오작동 유발. (Dùng lại vùng nhớ đã được giải phóng).
- **초기화되지 않은 변수 사용 (Uninitialized Variable)**: 변수 선언 후 값을 넣지 않고 사용하여 이전 쓰레기 값이 노출됨. (Dùng biến chưa khởi tạo giá trị).

Ta có thể khép mục **2. 자원 처리 오류 (Resource Handling Errors)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **5. 네트워크 및 인프라 기술 (Công nghệ Mạng & Hạ tầng)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.