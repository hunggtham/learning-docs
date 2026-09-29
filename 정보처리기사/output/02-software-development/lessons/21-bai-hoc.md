# 095 & 096: 단위 모듈 테스트 및 테스트 케이스 (Unit Test & Test Case)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **095 & 096: 단위 모듈 테스트 및 테스트 케이스 (Unit Test & Test Case)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **095 & 096: 단위 모듈 테스트 및 테스트 케이스 (Unit Test & Test Case)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **13. 형상 관리 (SCM - Software Configuration Management)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

단위, 모듈, 테스트, 케이스

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **094 & 094-1: IPC 및 모듈별 알고리즘 구현 (IPC & Algorithm by Module Type)**에서 만든 기준을 이어받아 **095 & 096: 단위 모듈 테스트 및 테스트 케이스 (Unit Test & Test Case)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 095 & 096: 단위 모듈 테스트 및 테스트 케이스 (Unit Test & Test Case)

Từ **094 & 094-1: IPC 및 모듈별 알고리즘 구현 (IPC & Algorithm by Module Type)**, ta đã có điểm tựa để bước vào **095 & 096: 단위 모듈 테스트 및 테스트 케이스 (Unit Test & Test Case)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 21/95 trước khi đi vào chi tiết.

Để đọc **095 & 096: 단위 모듈 테스트 및 테스트 케이스 (Unit Test & Test Case)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **단위 모듈 테스트 (Unit Module Test)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 단위 모듈 테스트 (Unit Module Test)

Các ý ngay dưới **단위 모듈 테스트 (Unit Module Test)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- 코딩 직후 최소 단위인 모듈이나 컴포넌트에 초점을 맞춤. (Test ngay sau khi code xong 1 hàm/module).
- Chủ yếu dùng **화이트박스 (White-box test)** để tìm lỗi thuật toán, vòng lặp vô hạn, lỗi công thức toán học.

Với **단위 모듈 테스트 (Unit Module Test)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **단위 모듈 테스트 (Unit Module Test)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **테스트 케이스 (Test Case)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **테스트 케이스 (Test Case)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 테스트 케이스 (Test Case)

Bây giờ ta đi vào nội dung của **테스트 케이스 (Test Case)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 입력 값, 실행 조건, 기대 결과의 명세서. (Tài liệu ghi rõ: Nhập gì, Điều kiện gì, Kết quả mong đợi là gì).
- 테스트 케이스를 미리 작성(사전에 정의)해야 인력과 시간 낭비를 방지. (Phải viết Test Case **trước** khi code hoặc test, để tránh test lung tung tốn thời gian).

- 💡 **Mẹo ghi nhớ (Mnemonics):** Test Case = Input + Condition + Expected Output. Bắt buộc viết trước khi test.

---

Với **테스트 케이스 (Test Case)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **테스트 케이스 (Test Case)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **095 & 096: 단위 모듈 테스트 및 테스트 케이스 (Unit Test & Test Case)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **13. 형상 관리 (SCM - Software Configuration Management)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.