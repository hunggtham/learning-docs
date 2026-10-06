# 핵심 119 & 120: 병렬 컴퓨터 분류 및 병렬처리기법 (Flynn's Taxonomy & Parallel Processing)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **핵심 119 & 120: 병렬 컴퓨터 분류 및 병렬처리기법 (Flynn's Taxonomy & Parallel Processing)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối Flynn taxonomy với instruction/data stream và parallel processing, để phân loại gắn với mô hình thực thi.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **핵심 119 & 120: 병렬 컴퓨터 분류 및 병렬처리기법 (Flynn's Taxonomy & Parallel Processing)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **핵심 119 & 120: 병렬 컴퓨터 분류 및 병렬처리기법 (Flynn's Taxonomy & Parallel Processing)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **023 & 024: 자료구조 (Data Structures / Cấu trúc dữ liệu)** khi chuyển sang phần tiếp theo.

> **Nối mạch:** Trong **핵심 119 & 120: 병렬 컴퓨터 분류 및 병렬처리기법 (Flynn's Taxonomy & Parallel Processing)**, **핵심 키워드 (Từ khóa)** nối từ **학습 목표 (Mục tiêu)** sang **선행·연결 개념 (Kiến thức liên kết)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 핵심 키워드 (Từ khóa)

핵심, 병렬, 컴퓨터, 분류, 병렬처리기법

> **Nối mạch:** Ở chặng này của **핵심 119 & 120: 병렬 컴퓨터 분류 및 병렬처리기법 (Flynn's Taxonomy & Parallel Processing)**, **핵심 키워드 (Từ khóa)** dẫn sang **선행·연결 개념 (Kiến thức liên kết)**, nơi tài liệu chuẩn và vị trí sở hữu được chỉ rõ để biết chỗ đào sâu tiếp; **읽는 방법 (Cách đọc)** mở rộng hệ quả liên quan.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **핵심 118: 가상 기억장치 (Virtual Memory)**에서 만든 기준을 이어받아 **핵심 119 & 120: 병렬 컴퓨터 분류 및 병렬처리기법 (Flynn's Taxonomy & Parallel Processing)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Nối mạch:** Đặt trong câu hỏi lớn của **핵심 119 & 120: 병렬 컴퓨터 분류 및 병렬처리기법 (Flynn's Taxonomy & Parallel Processing)**, **읽는 방법 (Cách đọc)** nối từ **선행·연결 개념 (Kiến thức liên kết)** sang **핵심 119 & 120: 병렬 컴퓨터 분류 및 병렬처리기법 (Flynn's Taxonomy & Parallel Processing)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Nối mạch:** Trong **핵심 119 & 120: 병렬 컴퓨터 분류 및 병렬처리기법 (Flynn's Taxonomy & Parallel Processing)**, **읽는 방법 (Cách đọc)** đặt đầu vào cho **핵심 119 & 120: 병렬 컴퓨터 분류 및 병렬처리기법 (Flynn's Taxonomy & Parallel Processing)**, rồi nối sang phần giải thích tiếp theo.

## 핵심 119 & 120: 병렬 컴퓨터 분류 및 병렬처리기법 (Flynn's Taxonomy & Parallel Processing)

Sau khi đã đặt nền bằng **핵심 118: 가상 기억장치 (Virtual Memory)**, ta chuyển sang **핵심 119 & 120: 병렬 컴퓨터 분류 및 병렬처리기법 (Flynn's Taxonomy & Parallel Processing)**. Đây là mắt xích 89/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **핵심 119 & 120: 병렬 컴퓨터 분류 및 병렬처리기법 (Flynn's Taxonomy & Parallel Processing)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **플린(Flynn)의 분류 (Phân loại Flynn)**. Hãy xác định **플린(Flynn)의 분류 (Phân loại Flynn)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 플린(Flynn)의 분류 (Phân loại Flynn)

Phần nguồn của **플린(Flynn)의 분류 (Phân loại Flynn)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “플린(Flynn)의 분류 (Phân loại Flynn)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **SISD (Single Instruction, Single Data):** 1 Lệnh xử lý 1 Dữ liệu. (Máy tính truyền thống Von Neumann).
- **SIMD (Single Instruction, Multi Data):** 1 Lệnh xử lý Nhiều Dữ liệu. (Array Processor, xử lý đồng bộ).
- **MISD (Multi Instruction, Single Data):** Nhiều Lệnh, 1 Dữ liệu. (Không dùng trong thực tế).
- **MIMD (Multi Instruction, Multi Data):** Nhiều Lệnh xử lý Nhiều Dữ liệu. (Máy đa nhân hiện đại - Đa xử lý bất đồng bộ). Tightly Coupled (Multiprocessor), Loosely Coupled (Distributed).

Các bullet của **플린(Flynn)의 분류 (Phân loại Flynn)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **플린(Flynn)의 분류 (Phân loại Flynn)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **병렬처리기법 (Kỹ thuật xử lý song song)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **병렬처리기법 (Kỹ thuật xử lý song song)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 병렬처리기법 (Kỹ thuật xử lý song song)

Các ý ngay dưới **병렬처리기법 (Kỹ thuật xử lý song song)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “병렬처리기법 (Kỹ thuật xử lý song song)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **파이프라인 프로세서 (Pipeline):** Chia lệnh thành các Sub-task (như dây chuyền nhà máy). Các bước: Fetch, Decode, Operand, Execute.
- **벡터 프로세서 (Vector Processor):** Xử lý mảng dữ liệu cực nhanh (Systolic algorithm).
- **배열 프로세서 (Array Processor):** Có nhiều bộ ALU (Processing Elements), điều khiển tập trung, tính toán song song theo không gian (SIMD).
- **데이터 흐름 컴퓨터 (Data Flow Computer):** Ngược với Von Neumann (Control-flow). Lệnh không chạy theo thứ tự PC, mà cứ hễ **đủ Dữ liệu là chạy** (Không cần Program Counter).

- **Vietnamese Explanation:** SISD là làm việc một mình. SIMD là 1 ông chủ ra lệnh cho 10 người cùng làm. MIMD là 10 người tự làm 10 việc khác nhau. Data Flow là cách làm việc "không cần quản lý", ai có đủ nguyên liệu thì tự động nấu, không cần chờ sếp hô hào.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Flynn: S = Single (Đơn), M = Multi (Đa), I = Instruction (Lệnh), D = Data (Dữ liệu). Data Flow = Data dẫn dắt, Không cần PC.

---

# [과목 2] 소프트웨어 개발 (Subject 2: Software Development)

Với **병렬처리기법 (Kỹ thuật xử lý song song)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **병렬처리기법 (Kỹ thuật xử lý song song)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **핵심 119 & 120: 병렬 컴퓨터 분류 및 병렬처리기법 (Flynn's Taxonomy & Parallel Processing)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **023 & 024: 자료구조 (Data Structures / Cấu trúc dữ liệu)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

> **Bàn giao:** Sau **핵심 119 & 120: 병렬 컴퓨터 분류 및 병렬처리기법 (Flynn's Taxonomy & Parallel Processing)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
