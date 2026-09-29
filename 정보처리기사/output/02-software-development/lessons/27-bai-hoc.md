# 12. 소프트웨어 패키징 및 설치 매뉴얼 (Software Packaging & Manual)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **12. 소프트웨어 패키징 및 설치 매뉴얼 (Software Packaging & Manual)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **12. 소프트웨어 패키징 및 설치 매뉴얼 (Software Packaging & Manual)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **37. 소프트웨어 패키징 고려사항 추가 (Packaging Considerations)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

소프트웨어, 패키징, 설치, 매뉴얼

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **116 & 117: 형상 관리 도구 (SVN vs Git)**에서 만든 기준을 이어받아 **12. 소프트웨어 패키징 및 설치 매뉴얼 (Software Packaging & Manual)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **12. 소프트웨어 패키징 및 설치 매뉴얼 (Software Packaging & Manual)** và nối nó với **37. 소프트웨어 패키징 고려사항 추가 (Packaging Considerations)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 12. 소프트웨어 패키징 및 설치 매뉴얼 (Software Packaging & Manual)

Từ **116 & 117: 형상 관리 도구 (SVN vs Git)**, ta đã có điểm tựa để bước vào **12. 소프트웨어 패키징 및 설치 매뉴얼 (Software Packaging & Manual)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 27/95 trước khi đi vào chi tiết.

Để đọc **12. 소프트웨어 패키징 및 설치 매뉴얼 (Software Packaging & Manual)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **패키징 (Packaging)**, **설치 매뉴얼 (Installation Manual)**, **Example** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

* **패키징 (Packaging)**: 모듈별 실행 파일들을 묶어 배포용 설치 파일을 만드는 것. 사용자 중심으로 진행하며 보안(암호화, DRM 연동) 고려.
* **설치 매뉴얼 (Installation Manual)**: 사용자를 기준으로 작성. 기본 사항, 소프트웨어 개요, 설치 파일, 프로그램 삭제 등 포함.
* **VI (Vietnamese) (Tiếng Việt):**
  * Packaging: Đóng gói các file thực thi thành file cài đặt (hướng đến người dùng cuối).
  * Manual: Tài liệu hướng dẫn cài đặt viết cho người dùng, bao gồm cách cài và gỡ.
* **Example**: `.exe` 설치 파일을 만들고, "다음, 다음, 완료"를 설명하는 설명서를 작성하는 과정입니다.

Điểm chốt của **12. 소프트웨어 패키징 및 설치 매뉴얼 (Software Packaging & Manual)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **37. 소프트웨어 패키징 고려사항 추가 (Packaging Considerations)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.