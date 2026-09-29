# 40. 형상 관리 (SCM) 및 버전 관리 방식 (Version Control Methods)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **40. 형상 관리 (SCM) 및 버전 관리 방식 (Version Control Methods)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **40. 형상 관리 (SCM) 및 버전 관리 방식 (Version Control Methods)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **핵심 032 & 033: 형상 관리 및 IDE (Configuration Management & IDE)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

형상, 관리

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **13. 형상 관리 (SCM - Software Configuration Management)**에서 만든 기준을 이어받아 **40. 형상 관리 (SCM) 및 버전 관리 방식 (Version Control Methods)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 40. 형상 관리 (SCM) 및 버전 관리 방식 (Version Control Methods)

Sau khi đã đặt nền bằng **13. 형상 관리 (SCM - Software Configuration Management)**, ta chuyển sang **40. 형상 관리 (SCM) 및 버전 관리 방식 (Version Control Methods)**. Đây là mắt xích 23/95 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **40. 형상 관리 (SCM) 및 버전 관리 방식 (Version Control Methods)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **형상 관리 (SCM)**, **기능**, **버전 관리 방식 3가지**, **SVN (Subversion)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

* **형상 관리 (SCM)**: 소프트웨어 개발 과정에서 변경 사항을 관리하는 일련의 활동.
  * **기능**: 형상 식별, 버전 제어, 형상 통제(변경 관리), 형상 감사, 형상 기록.
* **버전 관리 방식 3가지**:
  1. **공유 폴더 방식 (Shared Folder)**: 로컬 공유 폴더에 저장. (SCCS, RCS 등).
  2. **클라이언트/서버 방식 (C/S)**: 중앙 서버에 저장하여 관리. (CVS, SVN 등). 
     * **SVN (Subversion)**: `trunk`에서 주로 개발, `branches`에서 추가 작업 후 병합(merge). 커밋 시 리비전(Revision) 1씩 증가.
  3. **분산 저장소 방식 (Distributed)**: 로컬 저장소와 원격 저장소에 함께 저장. (Git 등).
     * **Git**: 로컬에서 버전 관리가 가능해 빠르고 네트워크 문제 시에도 작업 가능. 스냅샷(Snapshot)으로 파일 변화를 저장.
* **주요 기능**: Repository, Import, Check-Out(가져오기), Check-In/Commit(반영), Update(동기화).
* **VI (Vietnamese) (Tiếng Việt):** Quản lý cấu hình (SCM) và các cách quản lý phiên bản.
  * Shared Folder: Lưu ở thư mục chung.
  * C/S: Lưu ở server trung tâm (SVN).
  * Distributed: Lưu phân tán cả local và server (Git). Git dùng Snapshot để lưu thay đổi.
* **Example**: 회사에서 SVN을 쓰면 중앙 서버가 죽었을 때 작업을 올릴 수 없지만, Git을 쓰면 내 PC(Local)에 저장해뒀다가 서버가 복구되면 올릴 수 있습니다.

Ta có thể khép mục **40. 형상 관리 (SCM) 및 버전 관리 방식 (Version Control Methods)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **핵심 032 & 033: 형상 관리 및 IDE (Configuration Management & IDE)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.