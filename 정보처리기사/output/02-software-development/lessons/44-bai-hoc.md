# 099: 소프트웨어 패키징 (Software Packaging)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **099: 소프트웨어 패키징 (Software Packaging)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **099: 소프트웨어 패키징 (Software Packaging)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **100 & 100-1: 패키징 시 고려사항 및 순서 (Packaging Considerations & Sequence)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

소프트웨어, 패키징

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **39. DRM 패키징 과정 상세 (DRM Packaging Process)**에서 만든 기준을 이어받아 **099: 소프트웨어 패키징 (Software Packaging)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **099: 소프트웨어 패키징 (Software Packaging)** và nối nó với **100 & 100-1: 패키징 시 고려사항 및 순서 (Packaging Considerations & Sequence)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 099: 소프트웨어 패키징 (Software Packaging)

Sau khi đã đặt nền bằng **39. DRM 패키징 과정 상세 (DRM Packaging Process)**, ta chuyển sang **099: 소프트웨어 패키징 (Software Packaging)**. Đây là mắt xích 44/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **099: 소프트웨어 패키징 (Software Packaging)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “099: 소프트웨어 패키징 (Software Packaging)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 실행 파일들을 묶어 배포용 설치 파일을 만드는 과정. (Gom tất cả file thực thi, file hình, file cấu hình thành 1 file cài đặt (Setup.exe) để tung ra thị trường).
- **Nguyên tắc:**
  - **사용자 중심 (Hướng tới người dùng):** Người dùng cài đặt dễ dàng, không cần biết code.
  - Cần phải 모듈화 (Module hóa) để dễ bảo trì, và tích hợp 보안 (Bảo mật / DRM).

Ta có thể khép mục **099: 소프트웨어 패키징 (Software Packaging)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **100 & 100-1: 패키징 시 고려사항 및 순서 (Packaging Considerations & Sequence)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.