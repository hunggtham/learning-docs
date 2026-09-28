# Quy ước ngôn ngữ cho Thư viện kiến thức khoa học máy tính (computer science knowledge library / 컴퓨터 과학 지식 라이브러리)

> **Mạch đọc:** Đặt **Quy ước ngôn ngữ cho Thư viện kiến thức khoa học máy tính (computer science knowledge library / 컴퓨터 과학 지식 라이브러리)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Quy tắc chính** sang **Những thứ không dịch máy móc**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Thư viện này viết **chủ yếu bằng tiếng Việt**. Thuật ngữ tiếng Anh được giữ lại để người đọc nhận diện đúng từ khóa khi đọc giáo trình, tài liệu kỹ thuật, API hoặc trao đổi trong công việc, nhưng không được dùng tiếng Anh thay cho phần giải thích tiếng Việt khi đã có cách diễn đạt tự nhiên và chính xác.

## Quy tắc chính

Khi một thuật ngữ quan trọng xuất hiện lần đầu trong một ngữ cảnh, ưu tiên dạng:

```text
thuật ngữ tiếng Việt (English term)
```

Ví dụ: `câu hỏi (question)`, `bộ nhớ đệm (cache)`, `khối lượng công việc (workload)`, `nút thắt cổ chai (bottleneck)`, `tính nhất quán (consistency)`.

Sau khi đã giới thiệu thuật ngữ, phần giải thích tiếp theo ưu tiên tiếng Việt. Chỉ lặp lại từ tiếng Anh khi cần phân biệt chính xác nhiều khái niệm gần nhau hoặc khi từ đó là tên chuẩn mà người đọc cần nhận diện.

Nếu một câu đang pha quá nhiều tiếng Anh, phải viết lại toàn bộ ý bằng một câu tiếng Việt tự nhiên rồi chỉ giữ các **từ khóa kỹ thuật quan trọng** trong ngoặc. Không viết kiểu nửa câu tiếng Việt, nửa câu tiếng Anh nếu không có lý do kỹ thuật.


> **Chuyển mạch:** Từ **Quy tắc chính**, ta sang **Những thứ không dịch máy móc** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Những thứ không dịch máy móc

Không dịch tên API, giao thức, chuẩn, lệnh, identifier, đường dẫn tệp (file / 파일), tên sản phẩm, tên thuật toán riêng hoặc nội dung trong mã (code / 코드) khối (block / 블록). Ví dụ `HTTP`, `TLS`, `OAuth 2.0`, `OpenID Connect`, `io_uring`, `epoll`, `B+Tree`, `Raft`, `Java`, `C`, `JavaScript` được giữ nguyên.

Các từ viết tắt nên được giải thích bằng nghĩa tiếng Việt khi xuất hiện lần đầu nếu điều đó giúp hiểu bản chất. Ví dụ: `bộ đệm dịch địa chỉ (Translation Lookaside Buffer — TLB)`.


> **Chuyển mạch:** Từ **Những thứ không dịch máy móc**, ta sang **Thuật ngữ Hàn Quốc** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Thuật ngữ Hàn Quốc

Thuật ngữ tiếng Hàn chỉ thêm khi có giá trị thực tế trong giáo trình, kỳ thi, tài liệu công ty hoặc giao tiếp kỹ thuật. Cách viết ưu tiên:

```text
thuật ngữ tiếng Việt (English term / 한국어 용어)
```

Không thêm tiếng Hàn vào mọi câu chỉ để đủ ba ngôn ngữ.


> **Chuyển mạch:** Từ **Thuật ngữ Hàn Quốc**, ta sang **Mục tiêu** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mục tiêu

Người đọc phải có thể đọc liền mạch bằng tiếng Việt và hiểu bản chất mà không cần tự dịch trong đầu. Đồng thời, khi gặp tài liệu tiếng Anh hoặc tiếng Hàn, họ vẫn nhận ra các thuật ngữ chuẩn đã được ghi chú trong ngoặc.

> **Bàn giao:** Sau **Mục tiêu**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [99 glossary](./99_glossary.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
