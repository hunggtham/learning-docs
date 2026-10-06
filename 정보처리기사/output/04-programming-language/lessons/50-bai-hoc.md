# 252. 다중 if문 (Multiple if Statement)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **252. 다중 if문 (Multiple if Statement)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Hãy so sánh các điều kiện độc lập, thứ tự đánh giá và nhánh lồng nhau để biết nhiều if thay đổi luồng chương trình thế nào.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **252. 다중 if문 (Multiple if Statement)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **252. 다중 if문 (Multiple if Statement)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **305 - 308. IP 주소 체계 (IPv4 vs IPv6)** khi chuyển sang phần tiếp theo.

> **Nối mạch:** Trong **252. 다중 if문 (Multiple if Statement)**, **핵심 키워드 (Từ khóa)** nối từ **학습 목표 (Mục tiêu)** sang **선행·연결 개념 (Kiến thức liên kết)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 핵심 키워드 (Từ khóa)

다중

> **Nối mạch:** Ở chặng này của **252. 다중 if문 (Multiple if Statement)**, **핵심 키워드 (Từ khóa)** dẫn sang **선행·연결 개념 (Kiến thức liên kết)**, nơi tài liệu chuẩn và vị trí sở hữu được chỉ rõ để biết chỗ đào sâu tiếp; **읽는 방법 (Cách đọc)** mở rộng hệ quả liên quan.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **089. IP와 서브네팅, IPv4 vs IPv6 (IP & Subnetting)**에서 만든 기준을 이어받아 **252. 다중 if문 (Multiple if Statement)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Nối mạch:** Đặt trong câu hỏi lớn của **252. 다중 if문 (Multiple if Statement)**, **읽는 방법 (Cách đọc)** nối từ **선행·연결 개념 (Kiến thức liên kết)** sang **252. 다중 if문 (Multiple if Statement)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Nối mạch:** Trong **252. 다중 if문 (Multiple if Statement)**, **252. 다중 if문 (Multiple if Statement)** nối từ **읽는 방법 (Cách đọc)** sang phần giải thích tiếp theo, vì phần trước cung cấp điểm tựa cho chủ đề này.

## 252. 다중 if문 (Multiple if Statement)

Sau khi đã đặt nền bằng **089. IP와 서브네팅, IPv4 vs IPv6 (IP & Subnetting)**, ta chuyển sang **252. 다중 if문 (Multiple if Statement)**. Đây là mắt xích 50/91 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **252. 다중 if문 (Multiple if Statement)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “252. 다중 if문 (Multiple if Statement)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 처리할 조건이 여러 개일 때 `else if`를 사용해 순차적으로 판단.
- 위에서 조건이 참이면 해당 블록을 실행하고 빠져나옴 (아래 조건은 검사하지 않음).
- 모든 조건이 거짓일 때 마지막 `else`가 실행됨.

---

Ta có thể khép mục **252. 다중 if문 (Multiple if Statement)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **305 - 308. IP 주소 체계 (IPv4 vs IPv6)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

> **Bàn giao:** Sau **252. 다중 if문 (Multiple if Statement)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
