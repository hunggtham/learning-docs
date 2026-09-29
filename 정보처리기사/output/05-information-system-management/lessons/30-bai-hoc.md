# 인증 및 보안 체계 (Authentication & Security System)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **인증 및 보안 체계 (Authentication & Security System)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **인증 및 보안 체계 (Authentication & Security System)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **소프트웨어 개발 보안 관련 법규** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

인증, 보안, 체계

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **소프트웨어 보안 (Software Security)**에서 만든 기준을 이어받아 **인증 및 보안 체계 (Authentication & Security System)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **인증 및 보안 체계 (Authentication & Security System)** và nối nó với **소프트웨어 개발 보안 관련 법규**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 인증 및 보안 체계 (Authentication & Security System)

Từ **소프트웨어 보안 (Software Security)**, ta đã có điểm tựa để bước vào **인증 및 보안 체계 (Authentication & Security System)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 30/86 trước khi đi vào chi tiết.

Để đọc **인증 및 보안 체계 (Authentication & Security System)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **지식 기반 (Something You Know)**, **소유 기반 (Something You Have)**, **생체 기반 (Something You Are)**, **위치 기반 (Somewhere You Are)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **1. 인증 수단 4가지** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 1. 인증 수단 4가지

Các ý ngay dưới **1. 인증 수단 4가지** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “1. 인증 수단 4가지” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **지식 기반 (Something You Know)**: 패스워드, PIN (머릿속 기억).
- **소유 기반 (Something You Have)**: 신분증, 스마트카드, OTP.
- **생체 기반 (Something You Are)**: 지문, 홍채, 정맥 인식.
- **위치 기반 (Somewhere You Are)**: 접속 IP 위치, GPS.

Các bullet của **1. 인증 수단 4가지** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **1. 인증 수단 4가지** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. 보안 체계 3영역** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **2. 보안 체계 3영역**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 2. 보안 체계 3영역

Bây giờ ta đi vào nội dung của **2. 보안 체계 3영역**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “2. 보안 체계 3영역” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **관리적 보안**: 정보보호 정책, 조직, 교육 등 사람 중심.
- **물리적 보안**: 출입 통제, 전산실 관리 등 물리적 보호.
- **기술적 보안**: 사용자 인증, 암호화, 접근 제어 등 IT 기술 보호.

Các bullet của **2. 보안 체계 3영역** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **2. 보안 체계 3영역** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **인증 및 보안 체계 (Authentication & Security System)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **소프트웨어 개발 보안 관련 법규**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.