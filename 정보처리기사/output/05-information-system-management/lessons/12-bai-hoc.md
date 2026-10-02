# 1. 데이터 통신 개요 (Tổng quan Truyền thông Dữ liệu)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **1. 데이터 통신 개요 (Tổng quan Truyền thông Dữ liệu)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối data communication với signal, channel, encoding và protocol, để dữ liệu đi qua môi trường nào.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **1. 데이터 통신 개요 (Tổng quan Truyền thông Dữ liệu)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **1. 데이터 통신 개요 (Tổng quan Truyền thông Dữ liệu)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **2. 데이터 전송 방식 및 변조 (Phương thức truyền & Điều chế)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **1. 데이터 통신 개요 (Tổng quan Truyền thông Dữ liệu)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

데이터, 통신, 개요

> **Chuyển mạch:** Ở chặng này của **1. 데이터 통신 개요 (Tổng quan Truyền thông Dữ liệu)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **소프트웨어 프로세스 품질 및 성숙도 표준 (Quality & Maturity Standards)**에서 만든 기준을 이어받아 **1. 데이터 통신 개요 (Tổng quan Truyền thông Dữ liệu)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **1. 데이터 통신 개요 (Tổng quan Truyền thông Dữ liệu)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **1. 데이터 통신 개요 (Tổng quan Truyền thông Dữ liệu)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **1. 데이터 통신 개요 (Tổng quan Truyền thông Dữ liệu)**, **읽는 방법 (Cách đọc)** nêu điều cần giải thích; **1. 데이터 통신 개요 (Tổng quan Truyền thông Dữ liệu)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 1. 데이터 통신 개요 (Tổng quan Truyền thông Dữ liệu)

Từ **소프트웨어 프로세스 품질 및 성숙도 표준 (Quality & Maturity Standards)**, ta đã có điểm tựa để bước vào **1. 데이터 통신 개요 (Tổng quan Truyền thông Dữ liệu)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 12/86 trước khi đi vào chi tiết.

Để đọc **1. 데이터 통신 개요 (Tổng quan Truyền thông Dữ liệu)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **1.1 데이터 통신 및 주요 발전** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 1.1 데이터 통신 및 주요 발전

Các ý ngay dưới **1.1 데이터 통신 및 주요 발전** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “1.1 데이터 통신 및 주요 발전” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **데이터 통신:** 컴퓨터와 통신기기 사이에서 디지털(0과 1) 정보를 송수신. (데이터 통신 = 데이터 전송 기술 + 데이터 처리 기술).
- **정보 통신:** 전기 통신 + 컴퓨터 (정보 처리). 통신의 3요소: 정보원, 수신원, 전송 매체.
- **주요 시스템:**
  - `SAGE`: 최초의 데이터 통신 시스템.
  - `SABRE`: 최초 상업용.
  - `ARPANET`: 인터넷의 효시.
  - `ALOHA`: 최초 무선 패킷 교환.
- **Tiếng Việt:** Truyền thông dữ liệu truyền thông tin số (0, 1). 3 yếu tố: Nguồn, Đích, Môi trường truyền. ARPANET là tiền thân của Internet.

Với **1.1 데이터 통신 및 주요 발전**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **1.1 데이터 통신 및 주요 발전** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **1.2 통신 회선 및 매체 (Transmission Media)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **1.2 통신 회선 및 매체 (Transmission Media)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 1.2 통신 회선 및 매체 (Transmission Media)

Bây giờ ta đi vào nội dung của **1.2 통신 회선 및 매체 (Transmission Media)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “1.2 통신 회선 및 매체 (Transmission Media)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **꼬임선 (Twisted Pair):** 저렴하고 설치 간편, 간섭에 취약.
- **동축 케이블 (Coaxial Cable):** 대역폭이 넓고 누화 적음, 중계기 필요.
- **광섬유 케이블 (Optical Fiber):** 빛의 반사 원리. 가장 빠르고 대역폭 큼. 도청 어려워 보안성 우수. 무유도, 무누화.
- **마이크로파/위성 통신:** 장거리 대용량 통신. 다중 접속 방식: FDMA(주파수), TDMA(시간), CDMA(코드).
- **Tiếng Việt:**
  - Twisted Pair: Rẻ, dễ nhiễu.
  - Coaxial: Băng thông rộng, ít nhiễu.
  - Optical Fiber: Cáp quang (phản xạ ánh sáng), siêu tốc, siêu bảo mật.
  - Vệ tinh: Phân chia theo Tần số (FDMA), Thời gian (TDMA), Mã (CDMA).

Các bullet của **1.2 통신 회선 및 매체 (Transmission Media)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **1.2 통신 회선 및 매체 (Transmission Media)**, đừng bắt đầu lại từ số không. **1.3 통신 제어장치 (CCU) & 전처리기 (FEP)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **1.3 통신 제어장치 (CCU) & 전처리기 (FEP)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 1.3 통신 제어장치 (CCU) & 전처리기 (FEP)

Phần nguồn của **1.3 통신 제어장치 (CCU) & 전처리기 (FEP)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “1.3 통신 제어장치 (CCU) & 전처리기 (FEP)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **CCU:** 데이터 신호의 직·병렬 변환 등 전반적인 제어.
- **FEP (Front-End Processor):** 호스트와 단말기 사이에 위치해 통신 제어를 전담하여 메인 컴퓨터의 부하를 줄임.
- **Tiếng Việt:** CCU điều khiển truyền tải. FEP xử lý tiền kỳ để giảm tải cho máy chủ (Host).

Các bullet của **1.3 통신 제어장치 (CCU) & 전처리기 (FEP)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **1.3 통신 제어장치 (CCU) & 전처리기 (FEP)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Điểm chốt của **1. 데이터 통신 개요 (Tổng quan Truyền thông Dữ liệu)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **2. 데이터 전송 방식 및 변조 (Phương thức truyền & Điều chế)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

> **Bàn giao:** Sau **1. 데이터 통신 개요 (Tổng quan Truyền thông Dữ liệu)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
