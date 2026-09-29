# 113 ~ 115: 버전 관리 도구 방식 (Version Control Tool Types)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **113 ~ 115: 버전 관리 도구 방식 (Version Control Tool Types)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **113 ~ 115: 버전 관리 도구 방식 (Version Control Tool Types)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **120-1: 소프트웨어의 분류 (Software Classification)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

버전, 관리, 도구, 방식

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **104-1 ~ 108: 소프트웨어 매뉴얼 (Software Manuals)**에서 만든 기준을 이어받아 **113 ~ 115: 버전 관리 도구 방식 (Version Control Tool Types)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 113 ~ 115: 버전 관리 도구 방식 (Version Control Tool Types)

Ở bước 94/95, **113 ~ 115: 버전 관리 도구 방식 (Version Control Tool Types)** xuất hiện như phần tiếp nối của **104-1 ~ 108: 소프트웨어 매뉴얼 (Software Manuals)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **113 ~ 115: 버전 관리 도구 방식 (Version Control Tool Types)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng cho ta tiêu chí đối chiếu, còn công thức cho ta quan hệ giữa các đại lượng; hãy dùng cả hai để kiểm tra cùng một kết luận.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

| 방식 (Cách thức) | 특징 (Đặc điểm) | 대표 도구 (Công cụ) |
|---|---|---|
| **공유 폴더 (Shared Folder)** | Copy đè file vào 1 folder dùng chung trên mạng Lan. Dễ mất dữ liệu. | SCCS, RCS, PVCS |
| **클라이언트/서버 (Client/Server)** | Có 1 máy Server trung tâm giữ code. Máy cá nhân (Client) lấy về sửa rồi đẩy lên. Server chết là nghỉ làm. | **CVS, SVN** (Subversion), ClearCase |
| **분산 저장소 (Distributed Repo)** | Mỗi máy cá nhân đều là 1 cái Kho thu nhỏ (Local Repo). Copy (Clone) từ Server (Remote Repo) về. Server chết vẫn làm việc bình thường ở máy cá nhân, lúc nào Server sống lại đẩy lên sau (Push). Rất an toàn. | **Git**, Mercurial, Bitkeeper |

- **Vietnamese Explanation:** SVN là kiểu "Đi mượn sách thư viện", mất thư viện là khỏi đọc. Git là kiểu "Photo cuốn sách về nhà", thư viện cháy mình vẫn còn sách đọc, sửa sách thoải mái.
- 💡 **Mẹo ghi nhớ (Mnemonics):** 
  - 공유 폴더 (Share folder) = RCS, PVCS. 
  - 클라이언트/서버 = CVS, SVN (Server tập trung). 
  - 분산 (Phân tán) = Git.

Như vậy, **113 ~ 115: 버전 관리 도구 방식 (Version Control Tool Types)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **120-1: 소프트웨어의 분류 (Software Classification)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.