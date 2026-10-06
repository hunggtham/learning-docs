# 9. 인덱스와 트랜잭션 (Index và Giao dịch)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **9. 인덱스와 트랜잭션 (Index và Giao dịch)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối index với transaction, access path và locking, để tốc độ đọc không tách khỏi nhất quán.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **9. 인덱스와 트랜잭션 (Index và Giao dịch)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **9. 인덱스와 트랜잭션 (Index và Giao dịch)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **10. 트랜잭션 관리 기법 및 제어 (Quản lý và điều khiển giao dịch)** khi chuyển sang phần tiếp theo.

> **Nối mạch:** Trong **9. 인덱스와 트랜잭션 (Index và Giao dịch)**, **핵심 키워드 (Từ khóa)** nối từ **학습 목표 (Mục tiêu)** sang **선행·연결 개념 (Kiến thức liên kết)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 핵심 키워드 (Từ khóa)

인덱스와, 트랜잭션

> **Nối mạch:** Ở chặng này của **9. 인덱스와 트랜잭션 (Index và Giao dịch)**, **핵심 키워드 (Từ khóa)** dẫn sang **선행·연결 개념 (Kiến thức liên kết)**, nơi tài liệu chuẩn và vị trí sở hữu được chỉ rõ để biết chỗ đào sâu tiếp; **읽는 방법 (Cách đọc)** mở rộng hệ quả liên quan.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **187-189. 트랜잭션의 상태와 특성 (Transaction State & ACID)**에서 만든 기준을 이어받아 **9. 인덱스와 트랜잭션 (Index và Giao dịch)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Nối mạch:** Đặt trong câu hỏi lớn của **9. 인덱스와 트랜잭션 (Index và Giao dịch)**, **읽는 방법 (Cách đọc)** nối từ **선행·연결 개념 (Kiến thức liên kết)** sang **9. 인덱스와 트랜잭션 (Index và Giao dịch)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Nối mạch:** Trong **9. 인덱스와 트랜잭션 (Index và Giao dịch)**, **9. 인덱스와 트랜잭션 (Index và Giao dịch)** nối từ **읽는 방법 (Cách đọc)** sang phần giải thích tiếp theo, vì phần trước cung cấp điểm tựa cho chủ đề này.

## 9. 인덱스와 트랜잭션 (Index và Giao dịch)

Từ **187-189. 트랜잭션의 상태와 특성 (Transaction State & ACID)**, ta đã có điểm tựa để bước vào **9. 인덱스와 트랜잭션 (Index và Giao dịch)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 24/54 trước khi đi vào chi tiết.

Để đọc **9. 인덱스와 트랜잭션 (Index và Giao dịch)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng là bằng chứng để so sánh các lựa chọn theo cùng tiêu chí, không phải danh sách cần học thuộc từng ô.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **인덱스 (Index - Chỉ mục)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 인덱스 (Index - Chỉ mục)

Các ý ngay dưới **인덱스 (Index - Chỉ mục)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Dùng để tăng tốc độ tìm kiếm.
- **트리 기반 (Tree-based):** Thường dùng B-Tree, tốt cho tìm theo khoảng.
- **해시 (Hash):** Dùng Key-Value, truy cập nhanh và chi phí đồng đều, không tốt cho tìm khoảng.
- **비트맵 (Bitmap):** Dùng bit 0 và 1, phù hợp cho cột có ít giá trị khác biệt (Gender: M/F).
- **클러스터드 인덱스 (Clustered Index):** Dữ liệu thực sự được sắp xếp vật lý theo thứ tự Index. Rất tốt để tìm khoảng (Range search).

Các bullet của **인덱스 (Index - Chỉ mục)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **인덱스 (Index - Chỉ mục)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **트랜잭션 (Transaction - Giao dịch) - ACID** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **트랜잭션 (Transaction - Giao dịch) - ACID**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 트랜잭션 (Transaction - Giao dịch) - ACID

Bây giờ ta đi vào nội dung của **트랜잭션 (Transaction - Giao dịch) - ACID**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “트랜잭션 (Transaction - Giao dịch) - ACID” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

| 특징 (Đặc tính) | 설명 (Mô tả) | Ý nghĩa (VN) |
|---|---|---|
| **원자성 (Atomicity)** | All or Nothing (모두 반영되거나 전혀 반영되지 않음). | **Tính nguyên tử:** Chuyển tiền: hoặc cả 2 người cùng cập nhật, hoặc không ai thay đổi gì. Dùng Commit/Rollback. |
| **일관성 (Consistency)** | 일관적인 DB 상태 유지 (Trạng thái DB nhất quán). | **Tính nhất quán:** Dữ liệu sau giao dịch phải hợp lệ. |
| **고립성 (Isolation)** | 서로 간섭 불가 (Không can thiệp lẫn nhau). | **Tính cô lập:** Khi giao dịch A đang chạy, giao dịch B không thể nhảy vào làm sai lệch. |
| **영속성 (Durability)** | 영구적으로 결과 저장 (Lưu kết quả vĩnh viễn). | **Tính bền vững:** Sau khi COMMIT, dù sập nguồn dữ liệu vẫn tồn tại. |

> 💡 **Mẹo ghi nhớ:** **ACID** (Nguyên tử - Nhất quán - Cô lập - Bền vững).

---

Bảng trong **트랜잭션 (Transaction - Giao dịch) - ACID** không phải danh sách rời. Hãy đọc theo từng cột để nhận ra tiêu chí so sánh, rồi tự diễn đạt bằng một câu: đối tượng nào khác nhau ở điểm nào và trong điều kiện nào sự khác biệt đó có ý nghĩa.

Điểm chốt của **트랜잭션 (Transaction - Giao dịch) - ACID** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **9. 인덱스와 트랜잭션 (Index và Giao dịch)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **10. 트랜잭션 관리 기법 및 제어 (Quản lý và điều khiển giao dịch)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

> **Bàn giao:** Sau **9. 인덱스와 트랜잭션 (Index và Giao dịch)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
