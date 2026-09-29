# 스크립트 및 운영체제 (Script Languages & Operating Systems)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **스크립트 및 운영체제 (Script Languages & Operating Systems)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **스크립트 및 운영체제 (Script Languages & Operating Systems)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **운영체제 - 메모리 및 프로세스 관리 (OS - Memory & Process Management)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

스크립트, 운영체제

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **279 - 280. 라이브러리 (Library)**에서 만든 기준을 이어받아 **스크립트 및 운영체제 (Script Languages & Operating Systems)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **스크립트 및 운영체제 (Script Languages & Operating Systems)** và nối nó với **운영체제 - 메모리 및 프로세스 관리 (OS - Memory & Process Management)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 스크립트 및 운영체제 (Script Languages & Operating Systems)

Sau khi đã đặt nền bằng **279 - 280. 라이브러리 (Library)**, ta chuyển sang **스크립트 및 운영체제 (Script Languages & Operating Systems)**. Đây là mắt xích 32/91 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **스크립트 및 운영체제 (Script Languages & Operating Systems)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **자바스크립트 (JavaScript)**, **PHP**, **파이썬 (Python)**, **쉘 스크립트 (Shell Script)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **193. 스크립트 언어의 종류 (Types of Scripting Languages / Các loại ngôn ngữ kịch bản)**. Hãy xác định **193. 스크립트 언어의 종류 (Types of Scripting Languages / Các loại ngôn ngữ kịch bản)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 193. 스크립트 언어의 종류 (Types of Scripting Languages / Các loại ngôn ngữ kịch bản)

Phần nguồn của **193. 스크립트 언어의 종류 (Types of Scripting Languages / Các loại ngôn ngữ kịch bản)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “193. 스크립트 언어의 종류 (Types of Scripting Languages / Các loại ngôn ngữ kịch bản)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **자바스크립트 (JavaScript)**: 클라이언트용 웹 동작 제어 (Phía client, điều khiển hành vi web).
- **PHP**: 서버용 스크립트 언어 (Phía server, dùng trên Linux, Unix, Windows).
- **파이썬 (Python)**: 대화형 인터프리터 언어 (Ngôn ngữ thông dịch tương tác).
- **쉘 스크립트 (Shell Script)**: 명령어들의 조합 (Tập hợp các lệnh shell).
- **Basic**: 절차지향 대화형 인터프리터 (Thông dịch tương tác, hướng thủ tục).
  - 💡 *Mẹo ghi nhớ*: JS = Client Web, PHP = Server, Python = Thông dịch, Shell = Lệnh HĐH.

Với **193. 스크립트 언어의 종류 (Types of Scripting Languages / Các loại ngôn ngữ kịch bản)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **193. 스크립트 언어의 종류 (Types of Scripting Languages / Các loại ngôn ngữ kịch bản)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **194. 쉘 스크립트 제어문 (Shell Script Control Statements)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **194. 쉘 스크립트 제어문 (Shell Script Control Statements)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 194. 쉘 스크립트 제어문 (Shell Script Control Statements)

Các ý ngay dưới **194. 쉘 스크립트 제어문 (Shell Script Control Statements)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “194. 쉘 스크립트 제어문 (Shell Script Control Statements)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **선택형 (Điều kiện)**: `if`, `case`
- **반복형 (Vòng lặp)**: `for`, `while`, `until`

Các bullet của **194. 쉘 스크립트 제어문 (Shell Script Control Statements)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **194. 쉘 스크립트 제어문 (Shell Script Control Statements)**, đừng bắt đầu lại từ số không. **195. 라이브러리 (Libraries / Thư viện)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **195. 라이브러리 (Libraries / Thư viện)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 195. 라이브러리 (Libraries / Thư viện)

Bây giờ ta đi vào nội dung của **195. 라이브러리 (Libraries / Thư viện)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “195. 라이브러리 (Libraries / Thư viện)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **표준 (Standard)**: 기본적으로 포함된 모듈 (Tích hợp sẵn trong ngôn ngữ).
- **외부 (External)**: 다운받아 설치한 후 사용 (Phải tải và cài đặt từ bên ngoài).
  - 💡 *Mẹo ghi nhớ*: Built-in = Không cần cài, External = Cần pip/npm/v.v.

Với **195. 라이브러리 (Libraries / Thư viện)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

**195. 라이브러리 (Libraries / Thư viện)** vừa cho ta cách đặt câu hỏi. Bây giờ **196. C언어의 stdlib.h (Standard Library in C)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Với **196. C언어의 stdlib.h (Standard Library in C)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 196. C언어의 stdlib.h (Standard Library in C)

Phần nguồn của **196. C언어의 stdlib.h (Standard Library in C)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “196. C언어의 stdlib.h (Standard Library in C)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 자료형 변환, 난수 발생, 메모리 할당 기능을 제공한다. (Cung cấp chức năng ép kiểu, tạo số ngẫu nhiên, cấp phát bộ nhớ).
- 주요 함수 (Các hàm chính): `atoi`, `atof`, `srand`, `rand`, `malloc`, `free`.

Các bullet của **196. C언어의 stdlib.h (Standard Library in C)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **196. C언어의 stdlib.h (Standard Library in C)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **197. UNIX의 특징 (Features of UNIX / Đặc điểm của UNIX)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **197. UNIX의 특징 (Features of UNIX / Đặc điểm của UNIX)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 197. UNIX의 특징 (Features of UNIX / Đặc điểm của UNIX)

Các ý ngay dưới **197. UNIX의 특징 (Features of UNIX / Đặc điểm của UNIX)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “197. UNIX의 특징 (Features of UNIX / Đặc điểm của UNIX)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

---

Phần **197. UNIX의 특징 (Features of UNIX / Đặc điểm của UNIX)** không có nhiều dữ liệu rời để tách nhỏ, vì vậy hãy giữ câu hỏi mục đích và tự chốt bằng một câu giải thích trước khi đi tiếp.

Sau khi đọc **197. UNIX의 특징 (Features of UNIX / Đặc điểm của UNIX)**, đừng bắt đầu lại từ số không. **206. UNIX의 주요 명령어 (UNIX Commands / Lệnh UNIX)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **206. UNIX의 주요 명령어 (UNIX Commands / Lệnh UNIX)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 206. UNIX의 주요 명령어 (UNIX Commands / Lệnh UNIX)

Bây giờ ta đi vào nội dung của **206. UNIX의 주요 명령어 (UNIX Commands / Lệnh UNIX)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “206. UNIX의 주요 명령어 (UNIX Commands / Lệnh UNIX)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `fork`: 새로운 프로세스 생성 (Tạo tiến trình mới).
- `uname`: 시스템 정보 표시 (Hiển thị thông tin hệ thống).
- `wait`: 자식 프로세스 종료 대기 (Chờ tiến trình con kết thúc).
- `chmod`: 파일 보호 모드 설정 (Đổi quyền truy cập file).
- `ls`: 파일 목록 확인 (Liệt kê file).
- `cat`: 파일 내용 표시 (Xem nội dung file).
- `chown`: 소유자 변경 (Đổi chủ sở hữu file).
  - 💡 *Mẹo ghi nhớ*: fork (nhân bản, nĩa), chmod (change mode), chown (change owner).

Các bullet của **206. UNIX의 주요 명령어 (UNIX Commands / Lệnh UNIX)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **206. UNIX의 주요 명령어 (UNIX Commands / Lệnh UNIX)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Ta có thể khép mục **스크립트 및 운영체제 (Script Languages & Operating Systems)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **운영체제 - 메모리 및 프로세스 관리 (OS - Memory & Process Management)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.