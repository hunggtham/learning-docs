# 1. 메모리 버퍼 오버플로 (Memory Buffer Overflow / Tràn bộ đệm bộ nhớ)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **1. 메모리 버퍼 오버플로 (Memory Buffer Overflow / Tràn bộ đệm bộ nhớ)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **1. 메모리 버퍼 오버플로 (Memory Buffer Overflow / Tràn bộ đệm bộ nhớ)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **2. 운영체제 명령어 삽입 (OS Command Injection / Tiêm lệnh hệ điều hành)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

메모리, 버퍼, 오버플로

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **스토리지 시스템 (Storage Systems)**에서 만든 기준을 이어받아 **1. 메모리 버퍼 오버플로 (Memory Buffer Overflow / Tràn bộ đệm bộ nhớ)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **1. 메모리 버퍼 오버플로 (Memory Buffer Overflow / Tràn bộ đệm bộ nhớ)** và nối nó với **2. 운영체제 명령어 삽입 (OS Command Injection / Tiêm lệnh hệ điều hành)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 1. 메모리 버퍼 오버플로 (Memory Buffer Overflow / Tràn bộ đệm bộ nhớ)

Ở bước 76/86, **1. 메모리 버퍼 오버플로 (Memory Buffer Overflow / Tràn bộ đệm bộ nhớ)** xuất hiện như phần tiếp nối của **스토리지 시스템 (Storage Systems)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **1. 메모리 버퍼 오버플로 (Memory Buffer Overflow / Tràn bộ đệm bộ nhớ)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **개념**, **Tiếng Việt**, **예시 (Example)**, **대책** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “1. 메모리 버퍼 오버플로 (Memory Buffer Overflow / Tràn bộ đệm bộ nhớ)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개념**: 연속된 메모리 공간을 사용하는 프로그램에서 할당된 메모리의 범위를 넘어선 위치에서 자료를 읽거나 쓰려고 할 때 발생하는 취약점.
- **Tiếng Việt**: Lỗ hổng xảy ra khi chương trình ghi hoặc đọc dữ liệu vượt quá giới hạn vùng nhớ đã được cấp phát.
- **예시 (Example)**:
  - (KR) 10바이트 공간에 20바이트의 데이터를 입력하면 다른 메모리 영역을 침범함.
  - (VN) Nhập 20 byte dữ liệu vào mảng chỉ có kích thước 10 byte, làm ghi đè lên các vùng nhớ khác.
- **대책**: 버퍼의 크기를 적절히 설정.
- 💡 **Mẹo ghi nhớ**: Buffer Overflow = Bơm nước quá đầy làm tràn ly.

Như vậy, **1. 메모리 버퍼 오버플로 (Memory Buffer Overflow / Tràn bộ đệm bộ nhớ)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **2. 운영체제 명령어 삽입 (OS Command Injection / Tiêm lệnh hệ điều hành)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.