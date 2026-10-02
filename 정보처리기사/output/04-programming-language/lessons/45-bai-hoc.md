# 088. 인터넷 구성과 네트워크 - TCP vs UDP & 흐름/오류 제어

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **088. 인터넷 구성과 네트워크 - TCP vs UDP & 흐름/오류 제어**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối TCP/UDP với flow control, error control và latency, để chọn transport theo yêu cầu tin cậy và thời gian.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **088. 인터넷 구성과 네트워크 - TCP vs UDP & 흐름/오류 제어**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **088. 인터넷 구성과 네트워크 - TCP vs UDP & 흐름/오류 제어** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **309 - 314. OSI 7계층과 네트워크 프로토콜 (OSI 7 Layers & Protocols)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **088. 인터넷 구성과 네트워크 - TCP vs UDP & 흐름/오류 제어**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

인터넷, 구성과, 네트워크, TCP, UDP, 흐름, 오류, 제어

> **Chuyển mạch:** Ở chặng này của **088. 인터넷 구성과 네트워크 - TCP vs UDP & 흐름/오류 제어**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **088. 인터넷 구성과 네트워크 - OSI 7계층 (OSI 7 Layer)**에서 만든 기준을 이어받아 **088. 인터넷 구성과 네트워크 - TCP vs UDP & 흐름/오류 제어**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **088. 인터넷 구성과 네트워크 - TCP vs UDP & 흐름/오류 제어**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **088. 인터넷 구성과 네트워크 - TCP vs UDP & 흐름/오류 제어** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **088. 인터넷 구성과 네트워크 - TCP vs UDP & 흐름/오류 제어**, **088. 인터넷 구성과 네트워크 - TCP vs UDP & 흐름/오류 제어** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 088. 인터넷 구성과 네트워크 - TCP vs UDP & 흐름/오류 제어

Từ **088. 인터넷 구성과 네트워크 - OSI 7계층 (OSI 7 Layer)**, ta đã có điểm tựa để bước vào **088. 인터넷 구성과 네트워크 - TCP vs UDP & 흐름/오류 제어**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 45/91 trước khi đi vào chi tiết.

Để đọc **088. 인터넷 구성과 네트워크 - TCP vs UDP & 흐름/오류 제어** như một bài học cho người mới, hãy giữ câu hỏi: **các thành phần trao đổi dữ liệu theo lớp, quy tắc và điều kiện nào?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **TCP (Transmission Control Protocol)**, **UDP (User Datagram Protocol)**, **TCP 흐름 제어 (Flow Control)**, **TCP 오류 제어 (Error Control)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “088. 인터넷 구성과 네트워크 - TCP vs UDP & 흐름/오류 제어” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **TCP (Transmission Control Protocol)**: 연결 지향, 신뢰성 높음, 흐름 및 오류 제어 지원. 속도는 느림.
- **UDP (User Datagram Protocol)**: 비연결 지향, 신뢰성 낮음(오류 복구 안함). 실시간 전송(스트리밍)에 유리하여 속도가 빠름.
- **TCP 흐름 제어 (Flow Control)**: 수신측이 처리할 수 있는 만큼만 보냄 (Window 크기 사용).
  - Stop and Wait: 1개 보내고 응답 기다림.
  - Sliding Window: 윈도우 크기만큼 한 번에 여러 개 보냄 (효율적).
- **TCP 오류 제어 (Error Control)**:
  - Go Back n: 오류 발생한 패킷부터 **그 이후의 모든 패킷** 재전송.
  - Selective Repeat: 오류가 발생한 **해당 패킷만** 골라서 재전송.

**Giải thích (Vietnamese):**
- TCP giống như gửi thư bảo đảm, phải có người ký nhận mới yên tâm. Chậm nhưng chắc.
- UDP giống như phát loa phóng thanh, cứ phát ra, ai nghe được thì nghe. Phù hợp gọi Video call (Rớt 1 hình cũng không sao, quan trọng là độ trễ thấp).
- Trượt cửa sổ (Sliding Window): Kỹ thuật gửi liên tục nhiều gói tin mà không cần đợi từng gói báo nhận.
- Go Back N: Bị lỗi gói số 3, hệ thống sẽ gửi lại từ gói 3, 4, 5... Selective Repeat: Lỗi gói 3 thì chỉ gửi lại đúng gói 3.

---

Điểm chốt của **088. 인터넷 구성과 네트워크 - TCP vs UDP & 흐름/오류 제어** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **309 - 314. OSI 7계층과 네트워크 프로토콜 (OSI 7 Layers & Protocols)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

> **Bàn giao:** Sau **088. 인터넷 구성과 네트워크 - TCP vs UDP & 흐름/오류 제어**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
