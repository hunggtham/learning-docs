# 프로젝트 일정 관리 (Project Schedule Management)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **프로젝트 일정 관리 (Project Schedule Management)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối project schedule với task, dependency, critical path và resource, để tiến độ gắn với ràng buộc.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **프로젝트 일정 관리 (Project Schedule Management)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **프로젝트 일정 관리 (Project Schedule Management)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **소프트웨어 비용 산정 기법 (Software Cost Estimation)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **프로젝트 일정 관리 (Project Schedule Management)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

프로젝트, 일정, 관리

> **Chuyển mạch:** Ở chặng này của **프로젝트 일정 관리 (Project Schedule Management)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **3. 프로젝트 관리 및 비용 산정 (Quản lý dự án & Ước tính chi phí)**에서 만든 기준을 이어받아 **프로젝트 일정 관리 (Project Schedule Management)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **프로젝트 일정 관리 (Project Schedule Management)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **프로젝트 일정 관리 (Project Schedule Management)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **프로젝트 일정 관리 (Project Schedule Management)**, **프로젝트 일정 관리 (Project Schedule Management)** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 프로젝트 일정 관리 (Project Schedule Management)

Ở bước 7/86, **프로젝트 일정 관리 (Project Schedule Management)** xuất hiện như phần tiếp nối của **3. 프로젝트 관리 및 비용 산정 (Quản lý dự án & Ước tính chi phí)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **프로젝트 일정 관리 (Project Schedule Management)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **1. PERT (Program Evaluation and Review Technique)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **1. PERT (Program Evaluation and Review Technique)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 1. PERT (Program Evaluation and Review Technique)

Bây giờ ta đi vào nội dung của **1. PERT (Program Evaluation and Review Technique)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

과거 경험이 없어 예측이 어려운 프로젝트에 사용. 각 작업별로 낙관치, 기대치, 비관치를 나누어 종료 시기를 계산합니다.
- `예측치 = (비관치 + 4*기대치 + 낙관치) / 6`

Với **1. PERT (Program Evaluation and Review Technique)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **1. PERT (Program Evaluation and Review Technique)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. CPM (Critical Path Method, 임계 경로 기법)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **2. CPM (Critical Path Method, 임계 경로 기법)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 2. CPM (Critical Path Method, 임계 경로 기법)

Phần nguồn của **2. CPM (Critical Path Method, 임계 경로 기법)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

작업 사이의 의존 관계를 노드와 간선으로 구성. 네트워크에서 최장 경로가 **임계 경로(Critical Path)**가 됩니다.

Phần **2. CPM (Critical Path Method, 임계 경로 기법)** không có nhiều dữ liệu rời để tách nhỏ, vì vậy hãy giữ câu hỏi mục đích và tự chốt bằng một câu giải thích trước khi đi tiếp.

Sau khi đọc **2. CPM (Critical Path Method, 임계 경로 기법)**, đừng bắt đầu lại từ số không. **3. 간트 차트 (Gantt Chart, 시간선 차트)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **3. 간트 차트 (Gantt Chart, 시간선 차트)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 3. 간트 차트 (Gantt Chart, 시간선 차트)

Các ý ngay dưới **3. 간트 차트 (Gantt Chart, 시간선 차트)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

각 작업의 시작과 종료를 막대 도표로 표시하는 일정표. 적응성이 약하지만 이정표와 작업 기간을 한눈에 파악하기 쉽습니다.

Phần **3. 간트 차트 (Gantt Chart, 시간선 차트)** không có nhiều dữ liệu rời để tách nhỏ, vì vậy hãy giữ câu hỏi mục đích và tự chốt bằng một câu giải thích trước khi đi tiếp.

Như vậy, **3. 간트 차트 (Gantt Chart, 시간선 차트)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Như vậy, **프로젝트 일정 관리 (Project Schedule Management)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **소프트웨어 비용 산정 기법 (Software Cost Estimation)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

> **Bàn giao:** Sau **프로젝트 일정 관리 (Project Schedule Management)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
