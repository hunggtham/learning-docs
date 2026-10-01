# Quy ước ngôn ngữ cho Thư viện kiến thức khoa học máy tính (computer science knowledge library / 컴퓨터 과학 지식 라이브러리)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Quy ước ngôn ngữ cho Thư viện kiến thức khoa học máy tính (computer science knowledge library / 컴퓨터 과학 지식 라이브러리)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Quy tắc chính** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Những thứ không dịch máy móc** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Thư viện này viết **chủ yếu bằng tiếng Việt**. Thuật ngữ tiếng Anh được giữ lại để người đọc nhận diện đúng từ khóa khi đọc giáo trình, tài liệu kỹ thuật, API hoặc trao đổi trong công việc, nhưng không được dùng tiếng Anh thay cho phần giải thích tiếng Việt khi đã có cách diễn đạt tự nhiên và chính xác.

## Quy tắc chính

Khi một thuật ngữ quan trọng xuất hiện lần đầu trong một ngữ cảnh, ưu tiên dạng:

```text
thuật ngữ tiếng Việt (English term)
```

Ví dụ: `câu hỏi (question)`, `bộ nhớ đệm (cache)`, `khối lượng công việc (workload)`, `nút thắt cổ chai (bottleneck)`, `tính nhất quán (consistency)`.

Sau khi đã giới thiệu thuật ngữ, phần giải thích tiếp theo ưu tiên tiếng Việt. Chỉ lặp lại từ tiếng Anh khi cần phân biệt chính xác nhiều khái niệm gần nhau hoặc khi từ đó là tên chuẩn mà người đọc cần nhận diện.

Nếu một câu đang pha quá nhiều tiếng Anh, phải viết lại toàn bộ ý bằng một câu tiếng Việt tự nhiên rồi chỉ giữ các **từ khóa kỹ thuật quan trọng** trong ngoặc. Không viết kiểu nửa câu tiếng Việt, nửa câu tiếng Anh nếu không có lý do kỹ thuật.

> **Chuyển mạch:** Trong **Quy ước ngôn ngữ cho Thư viện kiến thức khoa học máy tính (computer science knowledge library / 컴퓨터 과학 지식 라이브러리)**, **Những thứ không dịch máy móc** tiếp nhận điểm tựa từ **Quy tắc chính** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thuật ngữ Hàn Quốc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những thứ không dịch máy móc

Không dịch tên API, giao thức, chuẩn, lệnh, identifier, đường dẫn tệp (file / 파일), tên sản phẩm, tên thuật toán riêng hoặc nội dung trong mã (code / 코드) khối (block / 블록). Ví dụ `HTTP`, `TLS`, `OAuth 2.0`, `OpenID Connect`, `io_uring`, `epoll`, `B+Tree`, `Raft`, `Java`, `C`, `JavaScript` được giữ nguyên.

Các từ viết tắt nên được giải thích bằng nghĩa tiếng Việt khi xuất hiện lần đầu nếu điều đó giúp hiểu bản chất. Ví dụ: `bộ đệm dịch địa chỉ (Translation Lookaside Buffer — TLB)`.

> **Chuyển mạch:** Ở chặng này của **Quy ước ngôn ngữ cho Thư viện kiến thức khoa học máy tính (computer science knowledge library / 컴퓨터 과학 지식 라이브러리)**, **Thuật ngữ Hàn Quốc** tiếp nhận điểm tựa từ **Những thứ không dịch máy móc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mục tiêu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thuật ngữ Hàn Quốc

Thuật ngữ tiếng Hàn chỉ thêm khi có giá trị thực tế trong giáo trình, kỳ thi, tài liệu công ty hoặc giao tiếp kỹ thuật. Cách viết ưu tiên:

```text
thuật ngữ tiếng Việt (English term / 한국어 용어)
```

Không thêm tiếng Hàn vào mọi câu chỉ để đủ ba ngôn ngữ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quy ước ngôn ngữ cho Thư viện kiến thức khoa học máy tính (computer science knowledge library / 컴퓨터 과학 지식 라이브러리)**, **Mục tiêu** tiếp nhận điểm tựa từ **Thuật ngữ Hàn Quốc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mục tiêu

Người đọc phải có thể đọc liền mạch bằng tiếng Việt và hiểu bản chất mà không cần tự dịch trong đầu. Đồng thời, khi gặp tài liệu tiếng Anh hoặc tiếng Hàn, họ vẫn nhận ra các thuật ngữ chuẩn đã được ghi chú trong ngoặc.

> **Bàn giao:** Sau **Mục tiêu**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
