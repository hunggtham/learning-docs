# 소프트웨어 비용 산정 기법 (Software Cost Estimation)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **소프트웨어 비용 산정 기법 (Software Cost Estimation)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **소프트웨어 비용 산정 기법 (Software Cost Estimation)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **323. 수학적 산정 기법 (Mathematical Estimation Techniques / Kỹ thuật ước lượng toán học)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

소프트웨어, 비용, 산정, 기법

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **프로젝트 일정 관리 (Project Schedule Management)**에서 만든 기준을 이어받아 **소프트웨어 비용 산정 기법 (Software Cost Estimation)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **소프트웨어 비용 산정 기법 (Software Cost Estimation)** và nối nó với **323. 수학적 산정 기법 (Mathematical Estimation Techniques / Kỹ thuật ước lượng toán học)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 소프트웨어 비용 산정 기법 (Software Cost Estimation)

Sau khi đã đặt nền bằng **프로젝트 일정 관리 (Project Schedule Management)**, ta chuyển sang **소프트웨어 비용 산정 기법 (Software Cost Estimation)**. Đây là mắt xích 8/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **소프트웨어 비용 산정 기법 (Software Cost Estimation)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **공식**, **COCOMO 모형 (Boehm 제안)**, **Putnam 모형 (생명 주기 예측 모형)**, **FP (Function Point, 기능 점수) 모형** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **1. LOC (Line Of Code) 기법**. Hãy xác định **1. LOC (Line Of Code) 기법** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 1. LOC (Line Of Code) 기법

Phần nguồn của **1. LOC (Line Of Code) 기법** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “1. LOC (Line Of Code) 기법” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 원시 코드(Source Code) 라인 수의 낙관치, 비관치, 기대치를 측정해 예측치를 구하여 비용을 산정.
- **공식**:
  - 노력(인월, Man-Month) = `LOC / 1인당 월평균 생산 코드 라인 수` = `개발 기간 × 투입 인원`
  - 개발 비용 = `노력(인월) × 단위 비용(월평균 인건비)`

Với **1. LOC (Line Of Code) 기법**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **1. LOC (Line Of Code) 기법** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. 수학적 산정 기법** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **2. 수학적 산정 기법** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 2. 수학적 산정 기법

Các ý ngay dưới **2. 수학적 산정 기법** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

과거의 프로젝트 데이터를 기반으로 한 상향식 비용 산정 모델입니다.
- **COCOMO 모형 (Boehm 제안)**: LOC 기반 산정. 고전 COCOMO의 경계는 다음처럼 겹치지 않게 해석한다.
  1. **조직형 (Organic)**: `≤ 50 KDSI` (중소 규모 업무용).
  2. **반분리형 (Semi-Detached)**: `> 50 ~ 300 KDSI` (컴파일러, 유틸리티).
  3. **내장형 (Embedded)**: `> 300 KDSI` (초대형 운영체제, 미사일 제어).
- **Putnam 모형 (생명 주기 예측 모형)**: 시간에 따른 **Rayleigh-Norden 곡선**의 노력 분포도를 기초로 산정.
- **FP (Function Point, 기능 점수) 모형**: 알브레히트(Albrecht) 제안. 기능 요인(입력, 출력, 사용자 질의, 데이터 파일, 외부 인터페이스)별로 가중치를 부여해 산정.

> **Vietnamese Explanation**:
> - **LOC**: Tính chi phí dựa trên số dòng code.
> - **COCOMO**: Phân loại theo độ lớn dự án (Organic: nhỏ, Semi: vừa, Embedded: lớn).
> - **Putnam**: Dựa trên đường cong phân bố nỗ lực theo thời gian Rayleigh-Norden.
> - **FP (Function Point)**: Dựa trên số lượng chức năng phần mềm mang lại cho người dùng.

💡 **Mẹo ghi nhớ (Mnemonics):**
- FP의 5가지 요인: **I.O.Q.F.I** (Input, Output, inQuiry, File, Interface).

Các bullet của **2. 수학적 산정 기법** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **2. 수학적 산정 기법** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **소프트웨어 비용 산정 기법 (Software Cost Estimation)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **323. 수학적 산정 기법 (Mathematical Estimation Techniques / Kỹ thuật ước lượng toán học)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.