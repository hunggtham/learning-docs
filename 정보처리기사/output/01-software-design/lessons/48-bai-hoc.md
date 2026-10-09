# 5. 보안 및 암호화 (Security & Encryption)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **5. 보안 및 암호화 (Security & Encryption)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối security với encryption, identity và threat boundary, để bảo vệ dữ liệu gắn với quyền và đường tấn công.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **5. 보안 및 암호화 (Security & Encryption)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **5. 보안 및 암호화 (Security & Encryption)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **6. 분산 데이터베이스 (Distributed Database)** khi chuyển sang phần tiếp theo.

Mục tiêu xác định security bảo vệ dữ liệu và identity trước threat boundary ra sao; từ khóa khoanh vùng encryption, quyền và đường tấn công.

## 핵심 키워드 (Từ khóa)

보안, 암호화

Kiến thức liên kết đặt security và encryption trên nền architecture; cách đọc tiếp theo giúp tách confidentiality, integrity, identity và threat.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **4. 병행 제어 (Concurrency Control)**에서 만든 기준을 이어받아 **5. 보안 및 암호화 (Security & Encryption)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

Cách đọc đã đặt khung đối tượng–điều kiện–hệ quả; phần security dùng khung đó để nối control với rủi ro và evidence.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

Phần này khép lại bằng threat boundary và control; khi sang distributed database, hãy giữ lại identity và integrity cần bảo vệ.

## 5. 보안 및 암호화 (Security & Encryption)

Từ **4. 병행 제어 (Concurrency Control)**, ta đã có điểm tựa để bước vào **5. 보안 및 암호화 (Security & Encryption)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 48/69 trước khi đi vào chi tiết.

Để đọc **5. 보안 및 암호화 (Security & Encryption)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **개인키 암호 방식 (Private Key / Secret Key)**, **공개키 암호 방식 (Public Key)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “5. 보안 및 암호화 (Security & Encryption)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개인키 암호 방식 (Private Key / Secret Key)**: Mã hóa đối xứng (대칭). Dùng cùng 1 khóa (DES). Nhanh, nhưng khó quản lý nhiều khóa.
- **공개키 암호 방식 (Public Key)**: Mã hóa bất đối xứng (비대칭). Khóa 공개키 (công khai) để mã hóa, khóa 비밀키 (bí mật) để giải mã (RSA). Quản lý khóa dễ, nhưng chậm.
- 💡 **Mẹo ghi nhớ**: 개인키 = 빠름, 키많음 (Private = Fast, Many keys). 공개키 = 느림, 키적음 (Public = Slow, Few keys).

Điểm chốt của **5. 보안 및 암호화 (Security & Encryption)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **6. 분산 데이터베이스 (Distributed Database)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

> **Bàn giao:** Sau **5. 보안 및 암호화 (Security & Encryption)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
