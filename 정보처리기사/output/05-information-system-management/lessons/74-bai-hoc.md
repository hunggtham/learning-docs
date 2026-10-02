# 소프트웨어 생명주기 모델 (SDLC Models)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **소프트웨어 생명주기 모델 (SDLC Models)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối SDLC models với phase, feedback, risk và delivery, để mô hình phù hợp mức bất định.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **소프트웨어 생명주기 모델 (SDLC Models)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **소프트웨어 생명주기 모델 (SDLC Models)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **스토리지 시스템 (Storage Systems)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **소프트웨어 생명주기 모델 (SDLC Models)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

소프트웨어, 생명주기, 모델

> **Chuyển mạch:** Ở chặng này của **소프트웨어 생명주기 모델 (SDLC Models)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **리눅스의 커널 로그 (Linux Kernel Logs)**에서 만든 기준을 이어받아 **소프트웨어 생명주기 모델 (SDLC Models)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **소프트웨어 생명주기 모델 (SDLC Models)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **소프트웨어 생명주기 모델 (SDLC Models)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **소프트웨어 생명주기 모델 (SDLC Models)**, **소프트웨어 생명주기 모델 (SDLC Models)** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 소프트웨어 생명주기 모델 (SDLC Models)

Sau khi đã đặt nền bằng **리눅스의 커널 로그 (Linux Kernel Logs)**, ta chuyển sang **소프트웨어 생명주기 모델 (SDLC Models)**. Đây là mắt xích 74/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **소프트웨어 생명주기 모델 (SDLC Models)** như một bài học cho người mới, hãy giữ câu hỏi: **ta dùng mô hình nào để biểu diễn đối tượng, quan hệ hoặc hành vi, và giới hạn của mỗi cách là gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **폭포수 모델 (Waterfall)**, **프로토타입 모델 (Prototyping)**, **나선형 모델 (Spiral)**, **V 모델 (V Model)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “소프트웨어 생명주기 모델 (SDLC Models)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **폭포수 모델 (Waterfall)**: 각 단계를 명확히 마무리한 후 다음 단계로 넘어가는 선형 순차적 모델 (요구사항 변경 어려움).
- **프로토타입 모델 (Prototyping)**: 시제품(Prototype)을 만들어 최종 결과물을 예측.
- **나선형 모델 (Spiral)**: 점진적으로 개발하며 **위험 분석(Risk Analysis)** 기능을 추가한 대형 프로젝트용 모델.
- **V 모델 (V Model)**: 폭포수 모델에 테스트 단계를 세부적으로 추가하여 검증을 강화한 모델.

> **Vietnamese Explanation**:
> - **Waterfall (Thác nước)**: Làm xong bước này mới qua bước khác.
> - **Prototyping (Mẫu thử)**: Làm một bản nháp cho khách hàng xem trước.
> - **Spiral (Xoắn ốc)**: Làm từng phần và liên tục đánh giá rủi ro (Risk analysis).
> - **V Model (Chữ V)**: Nhấn mạnh vào việc kiểm thử (Testing) ở mỗi giai đoạn tương ứng.

Ta có thể khép mục **소프트웨어 생명주기 모델 (SDLC Models)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **스토리지 시스템 (Storage Systems)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

> **Bàn giao:** Sau **소프트웨어 생명주기 모델 (SDLC Models)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
