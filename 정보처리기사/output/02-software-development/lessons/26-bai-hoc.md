# 116 & 117: 형상 관리 도구 (SVN vs Git)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **116 & 117: 형상 관리 도구 (SVN vs Git)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

형상, 관리, 도구

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **109 ~ 112: 형상 관리 (SCM - Software Configuration Management)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **12. 소프트웨어 패키징 및 설치 매뉴얼 (Software Packaging & Manual)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **116 & 117: 형상 관리 도구 (SVN vs Git)** và nối nó với **12. 소프트웨어 패키징 및 설치 매뉴얼 (Software Packaging & Manual)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 116 & 117: 형상 관리 도구 (SVN vs Git)

### Subversion (SVN)
- 클라이언트/서버 구조 (Cấu trúc Client/Server tập trung).
- **Trunk:** Thư mục chính (Main).
- **Branches:** Th nhánh để làm tính năng riêng.
- **Revision:** Mỗi lần lần ghi nhận (commit / 커밋) thành công, số Revision tăng lên 1.

### Git (깃)
- 분산 저장소 방식 (Lưu trữ phân tán). Phát minh bởi Linus Torvalds.
- **Snapshot (스냅샷):** Lưu lại toàn bộ trạng thái tệp (file / 파일) tại một thời điểm rất nhanh chóng.
- **로컬 저장소 (Local Repo) vs 원격 저장소 (Remote Repo):** Internet đứt vẫn làm việc bình thường ở cục bộ (local / 로컬).

- 💡 **Mẹo ghi nhớ (Mnemonics):** SVN = Trunk (Thân cây), Revision tăng dần. Git = Snapshot, phân tán (distributed / 분산).

---
