# 284 & 294. 구역성 (Locality / Tính cục bộ)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **284 & 294. 구역성 (Locality / Tính cục bộ)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối locality với temporal/spatial access và cache, để hiệu năng phụ thuộc dữ liệu gần nhau thế nào.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **284 & 294. 구역성 (Locality / Tính cục bộ)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **284 & 294. 구역성 (Locality / Tính cục bộ)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **285 & 295. 워킹 셋 (Working Set / Tập làm việc)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **284 & 294. 구역성 (Locality / Tính cục bộ)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

구역성

> **Chuyển mạch:** Ở chặng này của **284 & 294. 구역성 (Locality / Tính cục bộ)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **인터프리터 언어 (Interpreter Languages / Ngôn ngữ thông dịch)**에서 만든 기준을 이어받아 **284 & 294. 구역성 (Locality / Tính cục bộ)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **284 & 294. 구역성 (Locality / Tính cục bộ)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **284 & 294. 구역성 (Locality / Tính cục bộ)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **284 & 294. 구역성 (Locality / Tính cục bộ)**, **284 & 294. 구역성 (Locality / Tính cục bộ)** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 284 & 294. 구역성 (Locality / Tính cục bộ)

Từ **인터프리터 언어 (Interpreter Languages / Ngôn ngữ thông dịch)**, ta đã có điểm tựa để bước vào **284 & 294. 구역성 (Locality / Tính cục bộ)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 87/91 trước khi đi vào chi tiết.

Để đọc **284 & 294. 구역성 (Locality / Tính cục bộ)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **개념 (Khái niệm)**, **핵심 키워드 (Từ khóa)**, **시험 포인트 (Điểm thi)**, **한 문장 설명 (Tóm tắt)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### TẦNG A – NOTE NÉN (ÔN / ĐI THI)

Các ý ngay dưới **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “TẦNG A – NOTE NÉN (ÔN / ĐI THI)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개념 (Khái niệm)**: 프로세스가 실행되는 동안 주기억장치(Main memory)의 특정 영역만을 집중적으로 참조하는 성질. (Tính chất mà quá trình chỉ tham chiếu tập trung vào một số trang nhất định của bộ nhớ chính khi thực thi.)
- **핵심 키워드 (Từ khóa)**: 시간 구역성 (Temporal locality), 공간 구역성 (Spatial locality), 집중 참조 (Concentrated reference).
- **시험 포인트 (Điểm thi)**: 시간 구역성(Loop, Stack)과 공간 구역성(Array)의 구체적인 사례를 구분하는 것. (Phân biệt ví dụ của cục bộ thời gian và cục bộ không gian.)
- **한 문장 설명 (Tóm tắt)**: 스래싱(Thrashing) 방지를 위한 핵심 이론. (Lý thuyết cốt lõi để ngăn chặn hiện tượng Thrashing.)

Các ý về **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **TẦNG A – NOTE NÉN (ÔN / ĐI THI)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **TẦNG B – NOTE 보충 (HIỂU SÂU)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **TẦNG B – NOTE 보충 (HIỂU SÂU)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### TẦNG B – NOTE 보충 (HIỂU SÂU)

Bây giờ ta đi vào nội dung của **TẦNG B – NOTE 보충 (HIỂU SÂU)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “TẦNG B – NOTE 보충 (HIỂU SÂU)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **시간 구역성 (Temporal locality)**: 한 번 참조된 페이지는 가까운 시간 내에 다시 참조될 가능성이 높음. (Trang vừa dùng sẽ có khả năng cao được dùng lại sớm. Ví dụ: Vòng lặp/Loop, Ngăn xếp/Stack, Biến đếm.)
- **공간 구역성 (Spatial locality)**: 특정 페이지가 참조되면 인근 위치의 페이지가 계속 참조될 가능성이 높음. (Trang vừa dùng thì các trang liền kề nó dễ được gọi theo. Ví dụ: Mảng/Array, duyệt tuần tự.)
- **예시 (Ví dụ)**: 배열 `A[0]`부터 `A[100]`까지 순서대로 읽는 것은 공간 구역성이고, `for`문 안에서 변수 `i`를 계속 증가시키며 쓰는 것은 시간 구역성. (Đọc mảng theo thứ tự là cục bộ không gian; dùng biến i nhiều lần trong vòng lặp là cục bộ thời gian.)
- 💡 **Mẹo ghi nhớ**: **T**emporal = **T**ime (Lặp lại nhiều lần/Loop), **S**patial = **S**pace (Gần nhau/Array).

Với **TẦNG B – NOTE 보충 (HIỂU SÂU)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **TẦNG B – NOTE 보충 (HIỂU SÂU)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **284 & 294. 구역성 (Locality / Tính cục bộ)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **285 & 295. 워킹 셋 (Working Set / Tập làm việc)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

> **Bàn giao:** Sau **284 & 294. 구역성 (Locality / Tính cục bộ)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
