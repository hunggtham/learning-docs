# 298. PCB (Process Control Block)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **298. PCB (Process Control Block)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **298. PCB (Process Control Block)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **phần tổng hợp của môn** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

PCB

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **292. 페이지 교체 알고리즘 (Thuật toán thay thế trang / Page Replacement)**에서 만든 기준을 이어받아 **298. PCB (Process Control Block)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **298. PCB (Process Control Block)** và nối nó với **phần tổng hợp của môn**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 298. PCB (Process Control Block)

Từ **292. 페이지 교체 알고리즘 (Thuật toán thay thế trang / Page Replacement)**, ta đã có điểm tựa để bước vào **298. PCB (Process Control Block)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 78/78 trước khi đi vào chi tiết.

Để đọc **298. PCB (Process Control Block)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **개념 (Khái niệm)**, **핵심 키워드 (Từ khóa)**, **시험 포인트 (Điểm thi)**, **예시 (Ví dụ)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### TẦNG A – NOTE NÉN (ÔN / ĐI THI)

Các ý ngay dưới **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- **개념 (Khái niệm)**: 운영체제가 각 프로세스를 관리하기 위해 정보를 저장하는 데이터 구조. (Cấu trúc dữ liệu HĐH dùng để lưu thông tin quản lý từng tiến trình.)
- **핵심 키워드 (Từ khóa)**: 프로세스 상태 (Trạng thái tiến trình), 식별자 (PID), 우선순위 (Priority).
- **시험 포인트 (Điểm thi)**: 프로세스 생성 시 고유하게 생성되며, 종료 시 제거됨. (Được tạo ra duy nhất khi tiến trình bắt đầu và bị xóa khi kết thúc.)

Các bullet của **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **TẦNG B – NOTE 보충 (HIỂU SÂU)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **TẦNG B – NOTE 보충 (HIỂU SÂU)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### TẦNG B – NOTE 보충 (HIỂU SÂU)

Bây giờ ta đi vào nội dung của **TẦNG B – NOTE 보충 (HIỂU SÂU)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 현재 상태(준비/실행/대기), CPU 레지스터 정보, 자원 정보 포함. (Chứa trạng thái hiện tại, thanh ghi CPU, tài nguyên được cấp.)
- 문맥 교환(Context Switching) 시, 현재까지 진행 상황을 PCB에 저장. (Khi chuyển đổi ngữ cảnh, lưu tiến độ vào PCB để sau này chạy tiếp.)
- **예시 (Ví dụ)**: 병원에서 환자(프로세스)마다 차트(PCB)를 만들어 병력과 현재 상태를 기록하는 것과 같음. 퇴원하면 차트를 닫음. (Giống như Bệnh án (PCB) của từng bệnh nhân (Process), ghi lại tình trạng, xuất viện thì đóng hồ sơ.)
- 💡 **Mẹo ghi nhớ**: PCB giống như "Thẻ căn cước + Hồ sơ bệnh án" của một tiến trình.

Các ý về **TẦNG B – NOTE 보충 (HIỂU SÂU)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Điểm chốt của **TẦNG B – NOTE 보충 (HIỂU SÂU)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Khép lại **298. PCB (Process Control Block)**, điều cần giữ lại là mối quan hệ giữa mục đích, cơ chế và điểm giới hạn của các khái niệm trong nguồn. Khi ôn lại, hãy tự giải thích chúng bằng một câu hoàn chỉnh rồi đối chiếu với các điểm dễ nhầm trước khi chuyển sang bài tổng hợp của môn.