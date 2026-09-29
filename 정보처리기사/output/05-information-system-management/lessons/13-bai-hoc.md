# 2. 데이터 전송 방식 및 변조 (Phương thức truyền & Điều chế)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **2. 데이터 전송 방식 및 변조 (Phương thức truyền & Điều chế)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **2. 데이터 전송 방식 및 변조 (Phương thức truyền & Điều chế)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **3. 다중화 및 전송 제어 (Đa hợp & Điều khiển truyền)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

데이터, 전송, 방식, 변조

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **1. 데이터 통신 개요 (Tổng quan Truyền thông Dữ liệu)**에서 만든 기준을 이어받아 **2. 데이터 전송 방식 및 변조 (Phương thức truyền & Điều chế)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **2. 데이터 전송 방식 및 변조 (Phương thức truyền & Điều chế)** và nối nó với **3. 다중화 및 전송 제어 (Đa hợp & Điều khiển truyền)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 2. 데이터 전송 방식 및 변조 (Phương thức truyền & Điều chế)

Ở bước 13/86, **2. 데이터 전송 방식 및 변조 (Phương thức truyền & Điều chế)** xuất hiện như phần tiếp nối của **1. 데이터 통신 개요 (Tổng quan Truyền thông Dữ liệu)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **2. 데이터 전송 방식 및 변조 (Phương thức truyền & Điều chế)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **2.1 통신 방식 및 전송 동기 (Transmission Modes & Sync)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **2.1 통신 방식 및 전송 동기 (Transmission Modes & Sync)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 2.1 통신 방식 및 전송 동기 (Transmission Modes & Sync)

Bây giờ ta đi vào nội dung của **2.1 통신 방식 및 전송 동기 (Transmission Modes & Sync)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “2.1 통신 방식 및 전송 동기 (Transmission Modes & Sync)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **방향에 따른 분류:** 단방향 (Simplex), 반이중 (Half-Duplex, 무전기), 전이중 (Full-Duplex, 전화).
- **비동기식 (Asynchronous):** 문자마다 Start Bit / Stop Bit를 붙여 전송. 저속 단거리, 오버헤드 큼.
- **동기식 (Synchronous):** 프레임(블록) 단위로 일시에 전송. 속도 빠르고 효율 좋음. 비트/블록 동기 방식.
- **Tiếng Việt:**
  - Đơn công (Simplex), Bán song công (Half-Duplex), Song công toàn phần (Full-Duplex).
  - Bất đồng bộ: Dùng Start/Stop bit (overhead cao). Đồng bộ: Truyền theo block (nhanh, hiệu quả).

Các bullet của **2.1 통신 방식 및 전송 동기 (Transmission Modes & Sync)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **2.1 통신 방식 및 전송 동기 (Transmission Modes & Sync)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2.2 신호 변환 장치 (MODEM & DSU)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **2.2 신호 변환 장치 (MODEM & DSU)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 2.2 신호 변환 장치 (MODEM & DSU)

Phần nguồn của **2.2 신호 변환 장치 (MODEM & DSU)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “2.2 신호 변환 장치 (MODEM & DSU)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **모뎀 (MODEM):** 디지털 ↔ 아날로그 변환.
- **DSU (Digital Service Unit):** 디지털 ↔ 디지털 (단극성 ↔ 양극성 변환). 디지털 전용선에 사용.
- **Tiếng Việt:** MODEM (Chuyển đổi Số <-> Tương tự). DSU (Chuyển đổi Số <-> Số).
- 💡 **Mẹo ghi nhớ:** MO-Dem = MOdulation - DEModulation. D-SU = Digital - Digital.

Với **2.2 신호 변환 장치 (MODEM & DSU)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Sau khi đọc **2.2 신호 변환 장치 (MODEM & DSU)**, đừng bắt đầu lại từ số không. **2.3 디지털 변조 (Digital Modulation - Keying)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **2.3 디지털 변조 (Digital Modulation - Keying)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 2.3 디지털 변조 (Digital Modulation - Keying)

Các ý ngay dưới **2.3 디지털 변조 (Digital Modulation - Keying)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “2.3 디지털 변조 (Digital Modulation - Keying)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **ASK (진폭 편이):** 진폭 변화.
- **FSK (주파수 편이):** 주파수 변화 (1,200bps 이하).
- **PSK (위상 편이):** 위상 변화 (중/고속 모뎀).
- **QAM (직교 진폭 변조):** 진폭과 위상 동시 변화 (고속, 9,600bps 표준).
- **Tiếng Việt:** Điều chế tín hiệu số sang tương tự: ASK (Biên độ), FSK (Tần số), PSK (Pha), QAM (Biên độ + Pha kết hợp cho tốc độ cao).

Các bullet của **2.3 디지털 변조 (Digital Modulation - Keying)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**2.3 디지털 변조 (Digital Modulation - Keying)** vừa cho ta cách đặt câu hỏi. Bây giờ **2.4 PCM (Pulse Code Modulation)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Ở đoạn **2.4 PCM (Pulse Code Modulation)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 2.4 PCM (Pulse Code Modulation)

Bây giờ ta đi vào nội dung của **2.4 PCM (Pulse Code Modulation)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “2.4 PCM (Pulse Code Modulation)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 아날로그 데이터를 디지털 신호로 변환. CODEC 이용.
- **과정:** 표본화(Sampling) → 양자화(Quantizing) → 부호화(Encoding) → 복호화(Decoding) → 여파화(Filtering).
- **표본화 (Sampling):** 횟수 = 2 × 최고 주파수.
- **Tiếng Việt:** Biến đổi Tương tự -> Số (dùng CODEC). Quá trình: Lấy mẫu -> Lượng tử hóa -> Mã hóa.
- 💡 **Mẹo ghi nhớ:** Mẫu Lượng Mã Giải Lọc (Lấy mẫu -> Lượng tử hóa -> Mã hóa -> Giải mã -> Lọc).

Với **2.4 PCM (Pulse Code Modulation)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Với **2.4 PCM (Pulse Code Modulation)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Như vậy, **2. 데이터 전송 방식 및 변조 (Phương thức truyền & Điều chế)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **3. 다중화 및 전송 제어 (Đa hợp & Điều khiển truyền)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.