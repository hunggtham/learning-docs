# 095 & 096: 단위 모듈 테스트 및 테스트 케이스 (Unit Test & Test Case)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **095 & 096: 단위 모듈 테스트 및 테스트 케이스 (Unit Test & Test Case)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối unit test với test case, oracle, isolation và coverage, để kiểm thử module có mục tiêu và bằng chứng.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **095 & 096: 단위 모듈 테스트 및 테스트 케이스 (Unit Test & Test Case)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **095 & 096: 단위 모듈 테스트 및 테스트 케이스 (Unit Test & Test Case)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **13. 형상 관리 (SCM - Software Configuration Management)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **095 & 096: 단위 모듈 테스트 및 테스트 케이스 (Unit Test & Test Case)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

단위, 모듈, 테스트, 케이스

> **Chuyển mạch:** Ở chặng này của **095 & 096: 단위 모듈 테스트 및 테스트 케이스 (Unit Test & Test Case)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **094 & 094-1: IPC 및 모듈별 알고리즘 구현 (IPC & Algorithm by Module Type)**에서 만든 기준을 이어받아 **095 & 096: 단위 모듈 테스트 및 테스트 케이스 (Unit Test & Test Case)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **095 & 096: 단위 모듈 테스트 및 테스트 케이스 (Unit Test & Test Case)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **095 & 096: 단위 모듈 테스트 및 테스트 케이스 (Unit Test & Test Case)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **095 & 096: 단위 모듈 테스트 및 테스트 케이스 (Unit Test & Test Case)**, **읽는 방법 (Cách đọc)** cho ta quy tắc; **095 & 096: 단위 모듈 테스트 및 테스트 케이스 (Unit Test & Test Case)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 095 & 096: 단위 모듈 테스트 및 테스트 케이스 (Unit Test & Test Case)

Sau khi đã đặt nền bằng **094 & 094-1: IPC 및 모듈별 알고리즘 구현 (IPC & Algorithm by Module Type)**, ta chuyển sang **095 & 096: 단위 모듈 테스트 및 테스트 케이스 (Unit Test & Test Case)**. Đây là mắt xích 35/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **095 & 096: 단위 모듈 테스트 및 테스트 케이스 (Unit Test & Test Case)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **단위 모듈 테스트 (Unit Module Test)**. Hãy xác định **단위 모듈 테스트 (Unit Module Test)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 단위 모듈 테스트 (Unit Module Test)

Phần nguồn của **단위 모듈 테스트 (Unit Module Test)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “단위 모듈 테스트 (Unit Module Test)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 코딩 직후 최소 단위인 모듈이나 컴포넌트에 초점을 맞춤. (Test ngay sau khi code xong 1 hàm/module).
- Chủ yếu dùng **화이트박스 (White-box test)** để tìm lỗi thuật toán, vòng lặp vô hạn, lỗi công thức toán học.

Với **단위 모듈 테스트 (Unit Module Test)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **단위 모듈 테스트 (Unit Module Test)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **테스트 케이스 (Test Case)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **테스트 케이스 (Test Case)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 테스트 케이스 (Test Case)

Các ý ngay dưới **테스트 케이스 (Test Case)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “테스트 케이스 (Test Case)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 입력 값, 실행 조건, 기대 결과의 명세서. (Tài liệu ghi rõ: Nhập gì, Điều kiện gì, Kết quả mong đợi là gì).
- 테스트 케이스를 미리 작성(사전에 정의)해야 인력과 시간 낭비를 방지. (Phải viết Test Case **trước** khi code hoặc test, để tránh test lung tung tốn thời gian).

- 💡 **Mẹo ghi nhớ (Mnemonics):** Test Case = Input + Condition + Expected Output. Bắt buộc viết trước khi test.

---

Với **테스트 케이스 (Test Case)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **테스트 케이스 (Test Case)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **095 & 096: 단위 모듈 테스트 및 테스트 케이스 (Unit Test & Test Case)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **13. 형상 관리 (SCM - Software Configuration Management)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

> **Bàn giao:** Sau **095 & 096: 단위 모듈 테스트 및 테스트 케이스 (Unit Test & Test Case)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
