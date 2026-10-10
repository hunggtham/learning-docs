# 087. 환경변수와 쉘 스크립트 명령어 (Environment Variables & Shell Scripts)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **087. 환경변수와 쉘 스크립트 명령어 (Environment Variables & Shell Scripts)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối environment variables với shell scripts, process context và path, để lệnh chạy đúng môi trường.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **087. 환경변수와 쉘 스크립트 명령어 (Environment Variables & Shell Scripts)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **087. 환경변수와 쉘 스크립트 명령어 (Environment Variables & Shell Scripts)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **237. 변수명 작성 규칙 (Variable Naming Rules)** khi chuyển sang phần tiếp theo.

> **Mối nối:** Mục tiêu đã đặt câu hỏi về môi trường chạy lệnh; các **핵심 키워드 (Từ khóa)** tiếp theo thu hẹp câu hỏi đó vào biến môi trường, script và lệnh. Khi đọc, hãy giữ cả hai vế: biến được truyền vào tiến trình nào và lệnh sử dụng giá trị đó ra sao.

## 핵심 키워드 (Từ khóa)

환경변수와, 스크립트, 명령어

> **Mối nối:** Ba từ khóa vừa nêu chỉ tên đối tượng; phần **선행·연결 개념 (Kiến thức liên kết)** đặt chúng vào quan hệ với kiểu dữ liệu và ngữ cảnh tiến trình. Sau đó, **읽는 방법 (Cách đọc)** sẽ biến quan hệ ấy thành các bước kiểm tra: giá trị ở đâu, phạm vi đến đâu và lệnh nào đọc được nó.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **235. JAVA의 데이터 타입 크기 (Data Type Sizes in JAVA)**에서 만든 기준을 이어받아 **087. 환경변수와 쉘 스크립트 명령어 (Environment Variables & Shell Scripts)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Mối nối:** Kiến thức liên kết giải thích vì sao một lệnh chỉ có tác dụng trong shell hiện tại hoặc được truyền tiếp cho tiến trình con. Hãy dùng ba bước đọc vừa nêu để kiểm tra cơ chế đó trong **087. 환경변수와 쉘 스크립트 명령어 (Environment Variables & Shell Scripts)**, đặc biệt khi so sánh `set` với `export`.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Mối nối:** Khung đọc vừa thiết lập sẽ được kiểm chứng bằng các lệnh và ví dụ ở phần chính. Hãy theo dõi một giá trị từ lúc được đặt trong shell đến lúc lệnh hoặc tiến trình đọc nó; chuỗi đó là cầu nối để chuyển sang quy tắc đặt tên ở bài kế tiếp.

## 087. 환경변수와 쉘 스크립트 명령어 (Environment Variables & Shell Scripts)

Từ **235. JAVA의 데이터 타입 크기 (Data Type Sizes in JAVA)**, ta đã có điểm tựa để bước vào **087. 환경변수와 쉘 스크립트 명령어 (Environment Variables & Shell Scripts)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 6/91 trước khi đi vào chi tiết.

Để đọc **087. 환경변수와 쉘 스크립트 명령어 (Environment Variables & Shell Scripts)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **환경변수 명령어**, **운영체제별 주요 명령어 (Windows / Unix(Linux))** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “087. 환경변수와 쉘 스크립트 명령어 (Environment Variables & Shell Scripts)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **환경변수 명령어**:
  - `printenv`: 단일 변수 반환.
  - `env`: 환경 변수 출력/설정.
  - `set` / `setenv`: 변수 추가/업데이트.
  - `export`: 변수를 전역(Global) 변수로 변경 (export 안하면 현재 쉘에만 국한됨).
- **운영체제별 주요 명령어 (Windows / Unix(Linux))**:
  - 목록 보기: `dir` / `ls`
  - 복사: `copy` / `cp`
  - 삭제: `del` / `rm`
  - 이름 변경/이동: `ren`, `move` / `mv`
  - 폴더 생성: `md` / `mkdir`
  - 기타 Unix 명령어:
    - `chmod`: 권한 변경. / `chown`: 소유자 변경.
    - `cat`: 파일 내용 출력.
    - `grep`: 문자열(패턴) 검색 (Windows의 `find`).
    - `ps`: 프로세스 상태. / `kill`: 프로세스 종료.
    - `tar`: 파일 묶기/풀기. / `crontab`: 스케줄링.

**Giải thích (Vietnamese):**
- Lệnh `export` rất hay dùng trong Linux để set biến môi trường (Ví dụ: `export PATH=...`) để các chương trình khác cũng đọc được biến đó.
- Các lệnh Linux kinh điển: `ls` (list - liệt kê), `cp` (copy), `rm` (remove), `mv` (move), `mkdir` (make directory), `grep` (tìm text).

---

Điểm chốt của **087. 환경변수와 쉘 스크립트 명령어 (Environment Variables & Shell Scripts)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **237. 변수명 작성 규칙 (Variable Naming Rules)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

> **Bàn giao:** Sau **087. 환경변수와 쉘 스크립트 명령어 (Environment Variables & Shell Scripts)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
