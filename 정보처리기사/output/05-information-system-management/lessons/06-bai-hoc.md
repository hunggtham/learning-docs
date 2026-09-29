# 3. 다중화 및 전송 제어 (Đa hợp & Điều khiển truyền)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **3. 다중화 및 전송 제어 (Đa hợp & Điều khiển truyền)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **3. 다중화 및 전송 제어 (Đa hợp & Điều khiển truyền)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **4. 오류 제어 및 교환 방식 (Kiểm soát lỗi & Chuyển mạch)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

다중화, 전송, 제어

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **2. 데이터 전송 방식 및 변조 (Phương thức truyền & Điều chế)**에서 만든 기준을 이어받아 **3. 다중화 및 전송 제어 (Đa hợp & Điều khiển truyền)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 3. 다중화 및 전송 제어 (Đa hợp & Điều khiển truyền)

Từ **2. 데이터 전송 방식 및 변조 (Phương thức truyền & Điều chế)**, ta đã có điểm tựa để bước vào **3. 다중화 및 전송 제어 (Đa hợp & Điều khiển truyền)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 6/18 trước khi đi vào chi tiết.

Để đọc **3. 다중화 및 전송 제어 (Đa hợp & Điều khiển truyền)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **3.1 다중화기 (Multiplexer)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 3.1 다중화기 (Multiplexer)

Các ý ngay dưới **3.1 다중화기 (Multiplexer)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- 여러 단말기가 하나의 통신 회선을 공유.
- **FDM (주파수 분할 다중화):** 주파수를 분할. 보호 대역(Guard Band) 필요(대역폭 낭비). 아날로그, 비동기식.
- **TDM (시분할 다중화):** 시간을 분할(Time Slot). 동기식/디지털.
  - **STDM (동기식):** 데이터 유무 상관없이 고정 시간 폭 할당 (효율 낮음).
  - **ATDM (비동기식/통계적):** 데이터가 있는 단말에만 시간 할당 (효율 높음).
- **역 다중화기 (Inverse MUX):** 하나의 고속 채널을 2개의 저속 채널로 분할.
- **집중화기 (Concentrator):** 회선이 부족할 때 동적으로 할당(버퍼 필요). (입력 > 출력 회선).
- **Tiếng Việt:** 
  - FDM: Chia tần số (cần khoảng vệ bảo vệ Guard Band). 
  - TDM: Chia thời gian. (STDM: Cố định, ATDM: Động/Thống kê). 
  - Concentrator: Gom kênh, cần bộ đệm, số đầu vào > đầu ra.

Các bullet của **3.1 다중화기 (Multiplexer)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **3.1 다중화기 (Multiplexer)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **3.2 통신 속도 (Speed Metrics)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **3.2 통신 속도 (Speed Metrics)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 3.2 통신 속도 (Speed Metrics)

Bây giờ ta đi vào nội dung của **3.2 통신 속도 (Speed Metrics)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- **변조 속도 (Baud):** 1초 동안 신호 변화 횟수. (Baud = Bps / 상태 변화 수).
- **신호 속도 (Bps):** 1초 동안 전송 비트 수.
- **상태 변화 수:** Mono(1), Di(2), Tri(3), Quad(4) bit.
- **Tiếng Việt:** Baud: Số lần đổi trạng thái/s. Bps: Số bit/s.

Với **3.2 통신 속도 (Speed Metrics)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Sau khi đọc **3.2 통신 속도 (Speed Metrics)**, đừng bắt đầu lại từ số không. **3.3 전송 제어 (Transmission Control)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **3.3 전송 제어 (Transmission Control)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 3.3 전송 제어 (Transmission Control)

Phần nguồn của **3.3 전송 제어 (Transmission Control)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **5단계 절차:** 회선 접속 → 링크 설정 → 메시지 전송 → 링크 해제 → 회선 절단.
- **전송 제어 문자:**
  - `SYN`: 동기화
  - `SOH`/`STX`/`ETX`/`ETB`/`EOT`: 헤더, 텍스트(본문), 블록, 전송 종료
  - `ENQ`: 링크 설정 요구
  - `DLE`: 데이터 링크 이스케이프 (투과성 확보)
  - `ACK`/`NAK`: 긍정/부정 응답
- **Tiếng Việt:** Các ký tự điều khiển: SYN (Đồng bộ), STX (Bắt đầu văn bản), ETX (Kết thúc văn bản), ACK (Xác nhận), NAK (Từ chối).

Các bullet của **3.3 전송 제어 (Transmission Control)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**3.3 전송 제어 (Transmission Control)** vừa cho ta cách đặt câu hỏi. Bây giờ **3.4 HDLC 프로토콜 (High-level Data Link Control)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Đoạn **3.4 HDLC 프로토콜 (High-level Data Link Control)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 3.4 HDLC 프로토콜 (High-level Data Link Control)

Các ý ngay dưới **3.4 HDLC 프로토콜 (High-level Data Link Control)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- **비트(Bit) 위주**의 프로토콜. 전이중/반이중 지원, 동기식 전송.
- **비트 투과성 (Bit Stuffing):** 연속된 '1'이 5개면 강제로 '0' 추가 (플래그 `01111110`과 구분).
- **프레임 종류:**
  - **I (정보):** 데이터 전달 (0으로 시작).
  - **S (감독):** 오류/흐름 제어 (10).
  - **U (비번호):** 링크 모드 설정 (11).
- **전송 모드:** NRM (정규), ARM (비동기), ABM (비동기 균형 - 전이중 P2P).
- **Tiếng Việt:** HDLC là giao thức truyền theo bit. Dùng "Bit Stuffing" để chèn bit '0' sau 5 bit '1' liên tiếp. 3 loại Frame: I (Thông tin), S (Giám sát), U (Không số).

Các bullet của **3.4 HDLC 프로토콜 (High-level Data Link Control)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Với **3.4 HDLC 프로토콜 (High-level Data Link Control)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Điểm chốt của **3. 다중화 및 전송 제어 (Đa hợp & Điều khiển truyền)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **4. 오류 제어 및 교환 방식 (Kiểm soát lỗi & Chuyển mạch)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.