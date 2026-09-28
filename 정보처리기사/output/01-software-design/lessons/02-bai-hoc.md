# 1. 소프트웨어 생명 주기 (SDLC - Software Development Life Cycle)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **1. 소프트웨어 생명 주기 (SDLC - Software Development Life Cycle)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

소프트웨어, 생명, 주기

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **소프트웨어 생명 주기 및 개발 방법론 (SDLC & Methodologies)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **1. 소프트웨어 공학 및 개발 방법론 (Kỹ nghệ phần mềm và Phương pháp luận phát triển)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **1. 소프트웨어 생명 주기 (SDLC - Software Development Life Cycle)** và nối nó với **1. 소프트웨어 공학 및 개발 방법론 (Kỹ nghệ phần mềm và Phương pháp luận phát triển)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 1. 소프트웨어 생명 주기 (SDLC - Software Development Life Cycle)
- **개념**: Toàn bộ quá trình phát triển (Yêu cầu -> Thiết kế -> Code -> Test -> Bảo trì). Là tiêu chuẩn để quản lý dự án, chi phí, nhân lực.
- **폭포수 모형 (Waterfall Model)**:
  - Tuần tự (선형 순차적). Xong bước này mới qua bước khác. Không quay lại được.
  - Phù hợp dự án có yêu cầu rõ ràng, hệ thống nhà nước/ngân hàng. Tài liệu là trọng tâm.
- **나선형 모형 (Spiral Model)**:
  - Do Boehm đề xuất. Trọng tâm: Phân tích rủi ro (위험 분석).
  - Chu trình: Kế hoạch (계획) -> Phân tích rủi ro (위험) -> Phát triển (개발) -> Đánh giá (평가).
  - Phù hợp dự án lớn, rủi ro cao.
- **프로토타입 모형 (Prototype Model)**:
  - Làm bản nháp (시제품) trước khi phát triển thật. Phù hợp khi yêu cầu chưa rõ ràng.
- **V-모형 (V-Model)**:
  - Mỗi bước phát triển tương ứng với một bước kiểm thử (test / 테스트) (Ánh xạ Dev-Test). Yêu cầu chất lượng cực cao (Y tế, Hàng không).
