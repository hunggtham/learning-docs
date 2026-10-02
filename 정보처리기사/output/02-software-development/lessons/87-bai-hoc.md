# 핵심 117: 캐시 메모리 (Cache Memory)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **핵심 117: 캐시 메모리 (Cache Memory)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối cache memory với locality, hierarchy và latency, để CPU performance được đọc qua dữ liệu gần.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **핵심 117: 캐시 메모리 (Cache Memory)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **핵심 117: 캐시 메모리 (Cache Memory)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **핵심 118: 가상 기억장치 (Virtual Memory)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **핵심 117: 캐시 메모리 (Cache Memory)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

핵심, 캐시, 메모리

> **Chuyển mạch:** Ở chặng này của **핵심 117: 캐시 메모리 (Cache Memory)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **핵심 115 & 116: 연관 기억장치 및 메모리 인터리빙 (Associative Memory & Memory Interleaving)**에서 만든 기준을 이어받아 **핵심 117: 캐시 메모리 (Cache Memory)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **핵심 117: 캐시 메모리 (Cache Memory)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **핵심 117: 캐시 메모리 (Cache Memory)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **핵심 117: 캐시 메모리 (Cache Memory)**, **핵심 117: 캐시 메모리 (Cache Memory)** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 핵심 117: 캐시 메모리 (Cache Memory)

Từ **핵심 115 & 116: 연관 기억장치 및 메모리 인터리빙 (Associative Memory & Memory Interleaving)**, ta đã có điểm tựa để bước vào **핵심 117: 캐시 메모리 (Cache Memory)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 87/101 trước khi đi vào chi tiết.

Để đọc **핵심 117: 캐시 메모리 (Cache Memory)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “핵심 117: 캐시 메모리 (Cache Memory)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- CPU의 속도와 메모리의 속도 차이를 줄이기 위해 사용하는 고속 Buffer Memory. (Bộ đệm tốc độ cao giảm chênh lệch tốc độ giữa CPU và RAM.)
- 캐시 메모리는 메모리 계층 구조에서 가장 빠른 소자 (Nhanh nhất trong hệ thống phân cấp bên ngoài register, dùng SRAM.)
- `적중률 (Hit Ratio) = 적중 횟수(Hits) / 총 접근 횟수 (Total Accesses)`

Để không đọc **매핑 프로세스 (Mapping Process)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 매핑 프로세스 (Mapping Process)

Các ý ngay dưới **매핑 프로세스 (Mapping Process)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “매핑 프로세스 (Mapping Process)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 주기억장치로부터 캐시 메모리로 데이터를 전송하는 방법 (Cách ánh xạ RAM vào Cache.)
- 종류: 직접(Direct) 매핑, 어소시에이티브(Associative) 매핑, 세트-어소시에이티브(Set-Associative) 매핑.

Các bullet của **매핑 프로세스 (Mapping Process)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **매핑 프로세스 (Mapping Process)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **쓰기 정책 (Write Policy)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **쓰기 정책 (Write Policy)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 쓰기 정책 (Write Policy)

Bây giờ ta đi vào nội dung của **쓰기 정책 (Write Policy)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “쓰기 정책 (Write Policy)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 캐시에 저장되어 있는 데이터에 수정이 발생했을 때 주기억장치에 갱신하는 시기와 방법. (Khi Cache bị thay đổi, khi nào thì ghi lại vào RAM?)
- **Write-Through:** 쓰기 동작이 이루어질 때마다 캐시와 주기억장치를 동시에 갱신. (Ghi đồng thời cả 2, an toàn nhưng chậm.)
- **Write-Back:** 캐시로부터 제거될 때 주기억장치에 복사. (Chỉ ghi vào RAM khi bị đuổi khỏi Cache, nhanh nhưng rủi ro nếu mất điện.)

- **Vietnamese Explanation:** Cache giống như cái ví tiền lẻ (SRAM) bạn để túi quần. RAM là két sắt (DRAM) ở nhà. Lấy tiền lẻ nhanh hơn về nhà mở két.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Write-Through (Xuyên qua) = Ghi luôn vào RAM (Chậm, Chắc). Write-Back (Ghi lại sau) = Khi nào dọn Cache mới ghi (Nhanh, Nguy hiểm).

---

Với **쓰기 정책 (Write Policy)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **쓰기 정책 (Write Policy)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **핵심 117: 캐시 메모리 (Cache Memory)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **핵심 118: 가상 기억장치 (Virtual Memory)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

> **Bàn giao:** Sau **핵심 117: 캐시 메모리 (Cache Memory)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
