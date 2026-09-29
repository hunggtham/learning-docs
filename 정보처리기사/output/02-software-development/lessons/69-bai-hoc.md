# 핵심 046: 인터페이스 설계 확인 (EAI 구축 유형 - EAI Integration Types)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **핵심 046: 인터페이스 설계 확인 (EAI 구축 유형 - EAI Integration Types)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **핵심 046: 인터페이스 설계 확인 (EAI 구축 유형 - EAI Integration Types)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **핵심 047: 인터페이스 보안, 기능 구현 및 검증 (Interface Security, Implementation, Verification)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

핵심, 인터페이스, 설계, 확인

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **26. 인터페이스 구현 검증 도구 (Interface Verification Tools)**에서 만든 기준을 이어받아 **핵심 046: 인터페이스 설계 확인 (EAI 구축 유형 - EAI Integration Types)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **핵심 046: 인터페이스 설계 확인 (EAI 구축 유형 - EAI Integration Types)** và nối nó với **핵심 047: 인터페이스 보안, 기능 구현 및 검증 (Interface Security, Implementation, Verification)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 핵심 046: 인터페이스 설계 확인 (EAI 구축 유형 - EAI Integration Types)

Từ **26. 인터페이스 구현 검증 도구 (Interface Verification Tools)**, ta đã có điểm tựa để bước vào **핵심 046: 인터페이스 설계 확인 (EAI 구축 유형 - EAI Integration Types)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 69/95 trước khi đi vào chi tiết.

Để đọc **핵심 046: 인터페이스 설계 확인 (EAI 구축 유형 - EAI Integration Types)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng cho ta tiêu chí đối chiếu, còn công thức cho ta quan hệ giữa các đại lượng; hãy dùng cả hai để kiểm tra cùng một kết luận.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **EAI (Enterprise Application Integration):** Doanh nghiệp có nhiều phần mềm (Kế toán, Nhân sự, Kho...), EAI giúp chúng nói chuyện được với nhau.

| 유형 (Kiểu) | 기능 (Chức năng) |
|---|---|
| **Point-to-Point** | 1:1로 연결 (Nối trực tiếp 1-1). Không có Middleware ở giữa. Khó thay đổi. |
| **Hub & Spoke** | 단일 접점인 허브 시스템을 통해 데이터를 전송하는 중앙 집중형. (Nối kiểu nan hoa xe đạp. Tập trung vào cái Hub ở giữa. Hub sập là chết hết.) |
| **Message Bus** | 미들웨어(버스)를 두어 처리하는 방식. 확장성이 뛰어나며 대용량 처리가 가능. (Dùng một trục xe bus (Middleware) ở giữa. Rất dễ mở rộng và xử lý lượng lớn.) |
| **Hybrid** | 그룹 내에서는 Hub & Spoke, 그룹 간에는 Message Bus. (Lai tạp: Trong nhóm thì dùng Hub, giữa các nhóm thì dùng Bus.) |

- 💡 **Mẹo ghi nhớ (Mnemonics):** Hub & Spoke = Nan hoa (Có tâm Hub, sập tâm là chết). Message Bus = Xe buýt (Chở được nhiều, dễ mở rộng).

---

Điểm chốt của **핵심 046: 인터페이스 설계 확인 (EAI 구축 유형 - EAI Integration Types)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **핵심 047: 인터페이스 보안, 기능 구현 및 검증 (Interface Security, Implementation, Verification)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.