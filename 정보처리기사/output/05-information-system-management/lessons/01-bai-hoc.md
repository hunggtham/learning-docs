# 1. 소프트웨어 개발 방법론 및 프레임워크 (Phương pháp luận & Framework phát triển PM)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **1. 소프트웨어 개발 방법론 및 프레임워크 (Phương pháp luận & Framework phát triển PM)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

소프트웨어, 개발, 방법론, 프레임워크

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 1. 소프트웨어 개발 방법론 및 프레임워크 (Phương pháp luận & Framework phát triển PM)

### 1.1 구조적 방법론 (Structured Methodology)
- 정형화된 분석 절차에 따라 사용자 요구사항을 파악하여 문서화하는 **처리(Process) 중심**의 방법론이다.
- 복잡한 문제를 다루기 위해 **분할과 정복 (Divide and Conquer)** 원리를 적용한다.
- **Tiếng Việt:** Là phương pháp luận trung tâm vào xử lý (Process), lập tài liệu yêu cầu người dùng theo quy trình phân tích chuẩn. Áp dụng nguyên lý chia để trị (Divide and Conquer) cho các vấn đề phức tạp.
- **Example:**
  - *KR:* 큰 시스템을 여러 개의 작은 모듈로 나누어 개발.
  - *VN:* Chia một hệ thống lớn thành nhiều module nhỏ để phát triển.

### 1.2 정보공학 방법론 (Information Engineering Methodology)
- 정보 시스템의 개발을 위해 정형화된 기법들을 상호 연관성 있게 통합 및 적용하는 **자료(Data) 중심**의 방법론이다.
- 데이터베이스 설계를 위한 데이터 모델링으로 **개체 관계도 (ERD; Entity Relationship Diagram)**를 사용한다.
- **Tiếng Việt:** Phương pháp luận trung tâm vào dữ liệu (Data), tích hợp các kỹ thuật chuẩn hóa để phát triển hệ thống. Sử dụng sơ đồ thực thể liên kết (ERD) cho mô hình hóa dữ liệu.
- **Example:**
  - *KR:* 고객과 주문의 관계를 ERD로 모델링하여 시스템 구축.
  - *VN:* Mô hình hóa mối quan hệ giữa Khách hàng và Đơn hàng bằng ERD để xây dựng hệ thống.

### 1.3 컴포넌트 기반(CBD) 방법론 (Component-Based Development)
- 기존의 시스템이나 소프트웨어를 구성하는 **컴포넌트를 조합**하여 하나의 새로운 애플리케이션을 만드는 방법론이다.
- 분석 단계에서 사용자 요구사항 정의서가 산출된다.
- **Tiếng Việt:** Phương pháp luận tạo ứng dụng mới bằng cách kết hợp các thành phần (component) có sẵn. Tài liệu định nghĩa yêu cầu được tạo ra ở bước phân tích.
- **Example:**
  - *KR:* 결제 컴포넌트와 장바구니 컴포넌트를 조립하여 쇼핑몰 구축.
  - *VN:* Lắp ráp component thanh toán và component giỏ hàng để tạo trang thương mại điện tử.
- 💡 **Mẹo ghi nhớ:** CBD = "Lego" (lắp ráp các mảnh ghép có sẵn).

### 1.4 소프트웨어 개발 프레임워크 (Software Development Framework)
- 공통적으로 사용되는 구성 요소와 아키텍처를 일반화하여 제공해주는 반제품 형태의 소프트웨어 시스템.
- 사업자 종속성이 해소되며, 객체들의 제어를 프레임워크에 넘김으로써 생산성을 향상시킨다.
- **Tiếng Việt:** Hệ thống phần mềm dạng bán thành phẩm cung cấp các thành phần và kiến trúc chung. Giải quyết sự phụ thuộc vào nhà cung cấp và tăng năng suất.
- **Example:**
  - *KR:* Spring 프레임워크를 사용하여 Java 웹 애플리케이션을 빠르게 개발.
  - *VN:* Sử dụng Spring framework để phát triển nhanh ứng dụng web Java.
