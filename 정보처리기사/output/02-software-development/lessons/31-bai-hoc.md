# 099: 소프트웨어 패키징 (Software Packaging)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **099: 소프트웨어 패키징 (Software Packaging)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **099: 소프트웨어 패키징 (Software Packaging)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **100 & 100-1: 패키징 시 고려사항 및 순서 (Packaging Considerations & Sequence)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

소프트웨어, 패키징

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **핵심 035 & 036: 소프트웨어 패키징 및 DRM (Software Packaging & DRM)**에서 만든 기준을 이어받아 **099: 소프트웨어 패키징 (Software Packaging)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 099: 소프트웨어 패키징 (Software Packaging)

Ở bước 31/95, **099: 소프트웨어 패키징 (Software Packaging)** xuất hiện như phần tiếp nối của **핵심 035 & 036: 소프트웨어 패키징 및 DRM (Software Packaging & DRM)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **099: 소프트웨어 패키징 (Software Packaging)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- 실행 파일들을 묶어 배포용 설치 파일을 만드는 과정. (Gom tất cả file thực thi, file hình, file cấu hình thành 1 file cài đặt (Setup.exe) để tung ra thị trường).
- **Nguyên tắc:** 
  - **사용자 중심 (Hướng tới người dùng):** Người dùng cài đặt dễ dàng, không cần biết code.
  - Cần phải 모듈화 (Module hóa) để dễ bảo trì, và tích hợp 보안 (Bảo mật / DRM).

Như vậy, **099: 소프트웨어 패키징 (Software Packaging)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **100 & 100-1: 패키징 시 고려사항 및 순서 (Packaging Considerations & Sequence)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.