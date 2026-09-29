# 2. 스택 (Stack) 및 응용 (Applications)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **2. 스택 (Stack) 및 응용 (Applications)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **2. 스택 (Stack) 및 응용 (Applications)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **29. 큐 (Queue)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

스택

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **073 & 074: 자료 구조의 정의 및 선형 리스트 (Data Structures & Linear List)**에서 만든 기준을 이어받아 **2. 스택 (Stack) 및 응용 (Applications)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **2. 스택 (Stack) 및 응용 (Applications)** và nối nó với **29. 큐 (Queue)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 2. 스택 (Stack) 및 응용 (Applications)

Từ **073 & 074: 자료 구조의 정의 및 선형 리스트 (Data Structures & Linear List)**, ta đã có điểm tựa để bước vào **2. 스택 (Stack) 및 응용 (Applications)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 3/95 trước khi đi vào chi tiết.

Để đọc **2. 스택 (Stack) 및 응용 (Applications)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **응용 분야 (Applications)**, **삽입/삭제 (Push/Pop)**, **Example** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

* 리스트의 한쪽 끝으로만 자료의 삽입, 삭제 작업이 이루어지는 자료 구조.
* 가장 나중에 삽입된 자료가 가장 먼저 삭제되는 후입선출(**LIFO**, Last-In First-Out) 방식.
* **응용 분야 (Applications)**: 인터럽트 처리 (Interrupt handling), 수식 계산 및 표기법 (Expression evaluation), 서브루틴 호출 및 복귀 주소 저장 (Subroutine calls).
* **삽입/삭제 (Push/Pop)**: `PUSH`는 자료 입력, `POP`은 자료 출력.
* **VI (Vietnamese) (Tiếng Việt):**
  * Stack là cấu trúc dữ liệu LIFO, thêm/xóa dữ liệu ở một đầu.
  * Ứng dụng: Xử lý ngắt, tính toán biểu thức, lưu địa chỉ khi gọi hàm.
* **Example**: 브라우저의 '뒤로 가기' 버튼은 스택 구조를 사용합니다. (Nút "Back" trên trình duyệt sử dụng cấu trúc stack).
* 💡 **Mẹo ghi nhớ**: LIFO - Vào sau ra trước, giống như xếp đĩa, lấy đĩa trên cùng ra trước.

Điểm chốt của **2. 스택 (Stack) 및 응용 (Applications)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **29. 큐 (Queue)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.