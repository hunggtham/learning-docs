# 메모리 관리 (Memory Management)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **메모리 관리 (Memory Management)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối memory management với allocation, paging, replacement và process, để tài nguyên được điều phối.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **메모리 관리 (Memory Management)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **메모리 관리 (Memory Management)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **페이지 교체 알고리즘과 페이지 크기 (Page Replacement & Size)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **메모리 관리 (Memory Management)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

메모리, 관리

> **Chuyển mạch:** Ở chặng này của **메모리 관리 (Memory Management)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **UNIX 주요 구성요소 (UNIX Components)**에서 만든 기준을 이어받아 **메모리 관리 (Memory Management)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **메모리 관리 (Memory Management)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **메모리 관리 (Memory Management)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **메모리 관리 (Memory Management)**, **메모리 관리 (Memory Management)** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 메모리 관리 (Memory Management)

Sau khi đã đặt nền bằng **UNIX 주요 구성요소 (UNIX Components)**, ta chuyển sang **메모리 관리 (Memory Management)**. Đây là mắt xích 59/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **메모리 관리 (Memory Management)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **최초 적합 (First Fit)**, **최적 적합 (Best Fit)**, **최악 적합 (Worst Fit)**, **페이징(Paging) 기법** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **1. 배치 전략 (Placement Strategy)**. Hãy xác định **1. 배치 전략 (Placement Strategy)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 1. 배치 전략 (Placement Strategy)

Phần nguồn của **1. 배치 전략 (Placement Strategy)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

새로 반입되는 프로그램이나 데이터를 주기억장치의 어디에 위치시킬 것인지 결정합니다.
- **최초 적합 (First Fit)**: 빈 영역 중 첫 번째 분할 영역에 배치.
- **최적 적합 (Best Fit)**: 단편화(Fragmentation/Khoảng trống thừa)를 가장 작게 남기는 분할 영역에 배치.
- **최악 적합 (Worst Fit)**: 단편화를 가장 많이 남기는 분할 영역에 배치.

Các bullet của **1. 배치 전략 (Placement Strategy)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **1. 배치 전략 (Placement Strategy)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. 가상기억장치 구현 기법 (Virtual Memory Techniques)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **2. 가상기억장치 구현 기법 (Virtual Memory Techniques)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 2. 가상기억장치 구현 기법 (Virtual Memory Techniques)

Các ý ngay dưới **2. 가상기억장치 구현 기법 (Virtual Memory Techniques)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “2. 가상기억장치 구현 기법 (Virtual Memory Techniques)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **페이징(Paging) 기법**: 가상기억장치와 주기억장치를 **동일한 크기**로 나누어 적재. (프로그램 단위: 페이지, 주기억장치 단위: 페이지 프레임)
  - 외부 단편화는 발생하지 않으나, **내부 단편화**는 발생 가능.
- **세그먼테이션(Segmentation) 기법**: 프로그램을 배열이나 함수 등 **다양한 크기의 논리적인 단위(세그먼트)**로 나누어 적재.
  - 내부 단편화는 발생하지 않으나, **외부 단편화**는 발생 가능.

💡 **Mẹo ghi nhớ (Mnemonics):**
- **Paging**: Bằng nhau (Page). Lỗi nội bộ (내부 단편화).
- **Segmentation**: Khác nhau (Theo logic). Lỗi bên ngoài (외부 단편화).

Các bullet của **2. 가상기억장치 구현 기법 (Virtual Memory Techniques)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **2. 가상기억장치 구현 기법 (Virtual Memory Techniques)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **메모리 관리 (Memory Management)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **페이지 교체 알고리즘과 페이지 크기 (Page Replacement & Size)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

> **Bàn giao:** Sau **메모리 관리 (Memory Management)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
