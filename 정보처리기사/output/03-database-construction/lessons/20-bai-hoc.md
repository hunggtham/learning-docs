# 16. 정규화(Normalization)와 이상 현상(Anomaly)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **16. 정규화(Normalization)와 이상 현상(Anomaly)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **16. 정규화(Normalization)와 이상 현상(Anomaly)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **20. 쿼리 성능 최적화와 반정규화 (Tối ưu hóa Truy vấn và Phi chuẩn hóa)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

정규화

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **184-185. 반정규화 (Denormalization)**에서 만든 기준을 이어받아 **16. 정규화(Normalization)와 이상 현상(Anomaly)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 16. 정규화(Normalization)와 이상 현상(Anomaly)

Sau khi đã đặt nền bằng **184-185. 반정규화 (Denormalization)**, ta chuyển sang **16. 정규화(Normalization)와 이상 현상(Anomaly)**. Đây là mắt xích 20/55 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **16. 정규화(Normalization)와 이상 현상(Anomaly)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng là bằng chứng để so sánh các lựa chọn theo cùng tiêu chí, không phải danh sách cần học thuộc từng ô.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

**정규화 (Chuẩn hóa):** Quá trình chia nhỏ các bảng để giảm thiểu dư thừa dữ liệu và tránh các hiện tượng bất thường (이상 현상).

Ta bắt đầu phần nội dung bằng **이상 현상 (Anomaly - Bất thường)**. Hãy xác định **이상 현상 (Anomaly - Bất thường)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 이상 현상 (Anomaly - Bất thường)

Phần nguồn của **이상 현상 (Anomaly - Bất thường)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **삽입 이상 (Insertion Anomaly):** Lỗi khi thêm dữ liệu (phải thêm các dữ liệu không mong muốn).
- **갱신 이상 (Update Anomaly):** Lỗi khi cập nhật (cập nhật thiếu sót dẫn đến dữ liệu không nhất quán).
- **삭제 이상 (Deletion Anomaly):** Lỗi 연쇄 삭제 (Xóa dây chuyền) (xóa một dữ liệu kéo theo mất luôn dữ liệu quan trọng khác).

Các bullet của **이상 현상 (Anomaly - Bất thường)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **이상 현상 (Anomaly - Bất thường)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **정규화 단계 (Các chuẩn - Bắt buộc học thuộc)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **정규화 단계 (Các chuẩn - Bắt buộc học thuộc)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 정규화 단계 (Các chuẩn - Bắt buộc học thuộc)

Các ý ngay dưới **정규화 단계 (Các chuẩn - Bắt buộc học thuộc)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

| 정규형 (Chuẩn) | 조건 (Điều kiện để đạt được) | Mẹo ghi nhớ (VN) |
|---|---|---|
| **1NF** | **도**메인이 **원자값** (Mọi giá trị phải là Nguyên tử) | **도** (Do - Domain nguyên tử) |
| **2NF** | **부**분 함수 종속 제거 (Loại bỏ phụ thuộc hàm từng phần) | **부** (Bu - Bỏ phụ thuộc phần) |
| **3NF** | **이**행 함수 종속 제거 (Loại bỏ phụ thuộc hàm bắc cầu: A→B, B→C => A→C) | **이** (I - Loại bắc cầu / I-haeng) |
| **BCNF** | 모든 **결**정자가 후보키 (Tất cả yếu tố quyết định phải là Khóa ứng viên) | **결** (Gyeol - BCNF) |
| **4NF** | **다**치 종속 제거 (Loại bỏ phụ thuộc đa trị) | **다** (Da - Đa trị) |
| **5NF** | **조**인 종속 제거 (Loại bỏ phụ thuộc Join) | **조** (Jo - Join) |

> 💡 **Mẹo ghi nhớ:** **Đồ-Bếp-I-Kết-Đa-Giò** (Đô-main, Bếp-Phần, I-Bắc cầu, Kết-Quyết định, Đa trị, Giò-Chung).

---

Bảng trong **정규화 단계 (Các chuẩn - Bắt buộc học thuộc)** không phải danh sách rời. Hãy đọc theo từng cột để nhận ra tiêu chí so sánh, rồi tự diễn đạt bằng một câu: đối tượng nào khác nhau ở điểm nào và trong điều kiện nào sự khác biệt đó có ý nghĩa.

Điểm chốt của **정규화 단계 (Các chuẩn - Bắt buộc học thuộc)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **16. 정규화(Normalization)와 이상 현상(Anomaly)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **20. 쿼리 성능 최적화와 반정규화 (Tối ưu hóa Truy vấn và Phi chuẩn hóa)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.