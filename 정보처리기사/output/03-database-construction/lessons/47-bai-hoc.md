# 148-154. 파일 시스템과 디렉터리, 보안 (File System & Security)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **148-154. 파일 시스템과 디렉터리, 보안 (File System & Security)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **148-154. 파일 시스템과 디렉터리, 보안 (File System & Security)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **1. UNIX 파일 시스템의 구조 (Cấu trúc hệ thống tệp UNIX)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

파일, 시스템과, 디렉터리, 보안

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **194. 파티션 (Partition)**에서 만든 기준을 이어받아 **148-154. 파일 시스템과 디렉터리, 보안 (File System & Security)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **148-154. 파일 시스템과 디렉터리, 보안 (File System & Security)** và nối nó với **1. UNIX 파일 시스템의 구조 (Cấu trúc hệ thống tệp UNIX)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 148-154. 파일 시스템과 디렉터리, 보안 (File System & Security)

Sau khi đã đặt nền bằng **194. 파티션 (Partition)**, ta chuyển sang **148-154. 파일 시스템과 디렉터리, 보안 (File System & Security)**. Đây là mắt xích 47/54 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **148-154. 파일 시스템과 디렉터리, 보안 (File System & Security)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “148-154. 파일 시스템과 디렉터리, 보안 (File System & Security)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **순차 파일 (Sequential File):** 연속 기록 (자기 테이프). 접근 느림.
- **색인 순차 파일 (Indexed Sequential File):** 순차 + 색인(포인터). (기본, 색인, 오버플로 영역).
- **직접 파일 (Direct File):** 해싱 함수로 물리적 주소 직접 계산. 접근 빠름.
- **디렉터리 구조:** 1단계, 2단계, 트리, 비순환 그래프(공유 허용), 일반적인 그래프(순환 허용).
- **보안 기법:** 접근 제어 행렬, 전역 테이블, 접근 제어 리스트, 권한 리스트.
- **VI (Vietnamese) (Tiếng Việt):** Hệ thống file & Bảo mật.
  - Cấu trúc file: Tuần tự, Tuần tự có chỉ mục, Trực tiếp (hashing).
  - Cấu trúc thư mục: Cây, Đồ thị không chu trình (cho phép chia sẻ).

# 3과목 데이터베이스 구축 (Phần 3: Xây dựng Cơ sở dữ liệu) - Phần 1

> [!NOTE]
> Mặc dù đây là nội dung môn 3 (CSDL), có một số kiến thức hệ điều hành UNIX còn sót lại từ phần trước.

Ta có thể khép mục **148-154. 파일 시스템과 디렉터리, 보안 (File System & Security)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **1. UNIX 파일 시스템의 구조 (Cấu trúc hệ thống tệp UNIX)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.