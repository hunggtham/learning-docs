# 핵심 111 & 112: 반도체 기억소자 및 자기 코어 (Semiconductor Memory & Magnetic Core)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **핵심 111 & 112: 반도체 기억소자 및 자기 코어 (Semiconductor Memory & Magnetic Core)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **핵심 111 & 112: 반도체 기억소자 및 자기 코어 (Semiconductor Memory & Magnetic Core)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **핵심 113 & 114: 보조기억장치 및 디스크 접근 시간 (Auxiliary Memory & Disk Access Time)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

핵심, 반도체, 기억소자, 자기, 코어

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **핵심 110: RAM (Random Access Memory)**에서 만든 기준을 이어받아 **핵심 111 & 112: 반도체 기억소자 및 자기 코어 (Semiconductor Memory & Magnetic Core)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **핵심 111 & 112: 반도체 기억소자 및 자기 코어 (Semiconductor Memory & Magnetic Core)** và nối nó với **핵심 113 & 114: 보조기억장치 및 디스크 접근 시간 (Auxiliary Memory & Disk Access Time)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 핵심 111 & 112: 반도체 기억소자 및 자기 코어 (Semiconductor Memory & Magnetic Core)

Từ **핵심 110: RAM (Random Access Memory)**, ta đã có điểm tựa để bước vào **핵심 111 & 112: 반도체 기억소자 및 자기 코어 (Semiconductor Memory & Magnetic Core)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 84/101 trước khi đi vào chi tiết.

Để đọc **핵심 111 & 112: 반도체 기억소자 및 자기 코어 (Semiconductor Memory & Magnetic Core)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **RAM/ROM의 용량 계산 (Tính dung lượng RAM/ROM)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### RAM/ROM의 용량 계산 (Tính dung lượng RAM/ROM)

Các ý ngay dưới **RAM/ROM의 용량 계산 (Tính dung lượng RAM/ROM)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “RAM/ROM의 용량 계산 (Tính dung lượng RAM/ROM)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 주소선 (Address Bus) số lượng quyết định số Word: Nếu có n đường thì có 2^n Word. (Liên quan đến MAR và PC).
- 데이터 버스 (Data Bus) số lượng quyết định kích thước mỗi Word. (Liên quan đến MBR và IR).
- `Dung lượng = Số Word × Kích thước Word`. Ví dụ: 7 Address lines, 8 Data lines => 2^7 × 8 Bit = 128 × 8 Bit.

Với **RAM/ROM의 용량 계산 (Tính dung lượng RAM/ROM)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **RAM/ROM의 용량 계산 (Tính dung lượng RAM/ROM)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **자기 코어 (Magnetic Core - Lõi từ)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **자기 코어 (Magnetic Core - Lõi từ)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 자기 코어 (Magnetic Core - Lõi từ)

Bây giờ ta đi vào nội dung của **자기 코어 (Magnetic Core - Lõi từ)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “자기 코어 (Magnetic Core - Lõi từ)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 부피에 비해 용량이 작고 가격이 비싸 현재는 거의 사용하지 않는다. (Dung lượng nhỏ, giá đắt, ít dùng hiện nay.)
- 데이터를 읽으면 읽은 내용이 지워지는 파괴 메모리(DRO Memory)이므로, 재저장(Restoration Time) 시간이 필요하다. (Đọc xong là mất dữ liệu (Phá hủy), nên cần thời gian ghi lại.)
- Cấu tạo: 구동선(X, Y) 2개 (2 dây chọn địa chỉ), 센스 선 1개 (1 dây cảm biến trạng thái), 금지선 1개 (1 dây cấm).

- **Vietnamese Explanation:** Kích thước bộ nhớ phụ thuộc vào Address Bus (chiều dài) và Data Bus (chiều rộng). Lõi từ là công nghệ cổ, đọc xong bị mất dữ liệu nên phải tốn thời gian khôi phục, hiện không còn dùng.
- 💡 **Mẹo ghi nhớ (Mnemonics):** 자기 코어 (Magnetic Core) = Đọc là Mất (DRO), Cần ghi lại. 4 dây = 2 X/Y + 1 Sense + 1 Inhibit.

---

Với **자기 코어 (Magnetic Core - Lõi từ)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **자기 코어 (Magnetic Core - Lõi từ)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **핵심 111 & 112: 반도체 기억소자 및 자기 코어 (Semiconductor Memory & Magnetic Core)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **핵심 113 & 114: 보조기억장치 및 디스크 접근 시간 (Auxiliary Memory & Disk Access Time)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.