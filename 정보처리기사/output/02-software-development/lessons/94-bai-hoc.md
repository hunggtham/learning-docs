# 113 ~ 115: 버전 관리 도구 방식 (Version Control Tool Types)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **113 ~ 115: 버전 관리 도구 방식 (Version Control Tool Types)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

버전, 관리, 도구, 방식

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 113 ~ 115: 버전 관리 도구 방식 (Version Control Tool Types)

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
