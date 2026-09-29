# 41. 빌드 자동화 도구 심화: Jenkins vs Gradle

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **41. 빌드 자동화 도구 심화: Jenkins vs Gradle**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **41. 빌드 자동화 도구 심화: Jenkins vs Gradle** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **핵심 037 & 038: 매뉴얼 및 빌드/배포 도구 (Manuals & Build/Deploy Tools)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

빌드, 자동화, 도구, 심화, Jenkins, Gradle

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **36. IDE (통합 개발 환경) 및 빌드 도구 (IDE & Build Tools)**에서 만든 기준을 이어받아 **41. 빌드 자동화 도구 심화: Jenkins vs Gradle**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **41. 빌드 자동화 도구 심화: Jenkins vs Gradle** và nối nó với **핵심 037 & 038: 매뉴얼 및 빌드/배포 도구 (Manuals & Build/Deploy Tools)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 41. 빌드 자동화 도구 심화: Jenkins vs Gradle

Sau khi đã đặt nền bằng **36. IDE (통합 개발 환경) 및 빌드 도구 (IDE & Build Tools)**, ta chuyển sang **41. 빌드 자동화 도구 심화: Jenkins vs Gradle**. Đây là mắt xích 35/95 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **41. 빌드 자동화 도구 심화: Jenkins vs Gradle** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **Jenkins**, **Gradle** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

* **Jenkins**: JAVA 기반 오픈 소스. 친숙한 Web GUI 제공. 분산 빌드/테스트 가능.
* **Gradle**: Groovy 기반 오픈 소스. 안드로이드 앱 개발 환경에서 주로 사용. DSL을 스크립트 언어로 사용하며 태스크(Task) 단위로 실행. 빌드 캐시(Build Cache)로 속도 향상.
* **VI (Vietnamese) (Tiếng Việt):** Jenkins (dựa trên Java, có Web GUI dễ dùng) và Gradle (dựa trên Groovy, dùng nhiều trong Android, tăng tốc bằng Build Cache).
* 💡 **Mẹo ghi nhớ**: Jenkins = Java, Gradle = Groovy (Android).

Ta có thể khép mục **41. 빌드 자동화 도구 심화: Jenkins vs Gradle** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **핵심 037 & 038: 매뉴얼 및 빌드/배포 도구 (Manuals & Build/Deploy Tools)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.