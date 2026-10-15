# 4. 디자인 패턴 (Design Patterns - GoF)

## 학습 목표 (Mục tiêu)
- Nắm vững chi tiết cơ chế hoạt động, ngữ cảnh áp dụng thực tế của 5 Mẫu khởi tạo (`생성 패턴`) và 7 Mẫu cấu trúc (`구조 패턴`).
- Phân biệt rõ sự khác nhau giữa `Factory Method` (1 sản phẩm) và `Abstract Factory` (họ nhiều sản phẩm liên quan).
- Phân biệt cơ chế bao bọc đối tượng giữa `Adapter` (đổi giao diện), `Decorator` (thêm chức năng), `Proxy` (kiểm soát truy cập) và `Facade` (đơn giản hóa hệ thống con).

## 핵심 키워드 (Từ khóa)
- Singleton (싱글톤 / 유일한 인스턴스)
- Factory Method vs Abstract Factory (팩토리 메소드 vs 추상 팩토리)
- Builder / Prototype (빌더 / 프로토타입 / Clone)
- Adapter (어댑터 / 호환성 변환)
- Decorator (데코레이터 / 동적 기능 확장)
- Facade (퍼사드 / 하위 시스템 단순화)
- Proxy (프록시 / 대리자 / 접근 제어)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([8. 디자인 패턴](35-bai-hoc.md)):** Sau khi có bức tranh tổng thể phân loại 23 mẫu GoF, bài này đi sâu vào chi tiết kỹ thuật của nhóm Khởi tạo và nhóm Cấu trúc.
- **Tiếp nối sang bài sau ([11. 디자인 패턴](37-bai-hoc.md)):** Khảo sát sâu nhóm Mẫu hành vi (Behavioral Patterns) như Observer, Strategy, State, Template Method.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc định nghĩa bản chất của từng mẫu qua các từ khóa nhận diện đề thi (ví dụ: "nhân bản clone" -> Prototype; "đơn giản hóa hệ thống con" -> Facade).
- Đọc TẦNG B để phân tích ma trận so sánh các mẫu bao bọc Wrapper (Adapter, Decorator, Proxy, Facade) - đây là nơi đề thi hay giăng bẫy nhất.

---

## 4. 디자인 패턴 (Design Patterns - GoF)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Chi tiết 5 Mẫu khởi tạo (생성 패턴 - Creational Patterns):**
  - `Singleton (싱글톤)`:
    - Đảm bảo một lớp **chỉ có duy nhất một thể hiện (`유일한 인스턴스`)** trong toàn bộ vòng đời ứng dụng.
    - Dùng cho: Quản lý kết nối cơ sở dữ liệu (Connection Pool), Bộ ghi nhật ký (Logger), Trình quản lý cấu hình hệ thống.
  - `Factory Method (팩토리 메소드)`:
    - Lớp cha định nghĩa giao diện khởi tạo đối tượng nhưng **để cho các lớp con quyết định lớp cụ thể nào sẽ được tạo (`생성을 서브클래스에 위임`)**.
  - `Abstract Factory (추상 팩토리)`:
    - Cung cấp giao diện để tạo ra **các họ đối tượng liên quan hoặc phụ thuộc lẫn nhau (`연관된 서브 클래스들의 모음 / 객체 군`)** mà không cần chỉ định rõ các lớp cụ thể.
  - `Builder (빌더)`:
    - Phân tách quá trình khởi tạo một đối tượng phức tạp thành từng bước riêng biệt, cho phép cùng một quy trình xây dựng có thể tạo ra các biến thể biểu diễn khác nhau.
  - `Prototype (프로토타입)`:
    - Tạo đối tượng mới bằng cách **sao chép nhân bản từ một đối tượng mẫu có sẵn (`기존 객체를 복제 / Clone`)**, giúp tiết kiệm chi phí tạo đối tượng tốn kém tài nguyên.
- **2. Chi tiết 7 Mẫu cấu trúc (구조 패턴 - Structural Patterns):**
  - `Adapter (어댑터)`:
    - Đóng vai trò bộ chuyển đổi, giúp các lớp có **giao diện không tương thích có thể làm việc trơn tru với nhau (`호환되지 않는 인터페이스를 변환`)** (giống cục sạc chuyển từ giắc 3 chân sang 2 chân).
  - `Bridge (브리지)`:
    - Tách rời phần trừu tượng (Abstraction) khỏi phần cài đặt cụ thể (Implementation) bằng một cây cầu nối tham chiếu, giúp cả hai nhánh phát triển độc lập.
  - `Composite (컴포지트)`:
    - Tổ chức các đối tượng theo cấu trúc cây (Tree) biểu diễn phân cấp toàn thể - bộ phận, giúp client đối xử với **đối tượng đơn lẻ và tập hợp các đối tượng phức hợp theo cách hoàn toàn đồng nhất** (ví dụ: Cấu trúc Thư mục và Tập tin).
  - `Decorator (데코레이터)`:
    - **Bổ sung thêm chức năng/trách nhiệm mới cho một đối tượng một cách linh hoạt trong thời gian chạy (Runtime) mà không cần can thiệp sửa đổi lớp gốc hay dùng kế thừa** (ví dụ: Cà phê nguyên chất $\rightarrow$ thêm Sữa $\rightarrow$ thêm Trân châu).
  - `Facade (퍼사드)`:
    - Cung cấp một **giao diện cấp cao đơn giản duy nhất (`단순화된 통합 인터페이스`)** đại diện cho cả một hệ sinh thái các lớp con phức tạp bên trong, giúp client dễ dàng sử dụng mà không cần biết chi tiết rườm rà.
  - `Flyweight (플라이웨이트)`:
    - Tối ưu hóa bộ nhớ RAM bằng cách **chia sẻ dùng chung các đối tượng nhỏ có trạng thái nội tại giống nhau (`공유를 통해 메모리 절약`)** (ví dụ: hiển thị hàng triệu ký tự font chữ trong văn bản).
  - `Proxy (프록시)`:
    - Tạo ra một đối tượng **đại diện thay thế (`대리자`)** để kiểm soát việc truy cập, trì hoãn khởi tạo đối tượng nặng (Lazy Loading) hoặc gọi dịch vụ từ xa qua mạng (Remote Proxy).
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Tạo đối tượng bằng cách sao chép (Clone) từ mẫu có sẵn là mẫu nào?"* -> **Prototype (프로토타입)**.
  - **Bẫy 2:** *"Bổ sung tính năng động trong runtime mà không dùng kế thừa là mẫu nào?"* -> **Decorator (데코레이터)**.
  - **Bẫy 3:** *"Cung cấp một giao diện đơn giản đại diện cho cả hệ thống con phức tạp là mẫu nào?"* -> **Facade (퍼사드)**.
  - **Bẫy 4:** *"Tạo ra một 'họ' các đối tượng liên quan (Family of related objects) là mẫu nào?"* -> **Abstract Factory (추상 팩토리)**, KHÔNG PHẢI Factory Method.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Singleton tạo 1, Factory tạo họ, Prototype clone; Adapter đổi cổng, Decorator trang trí thêm tính năng, Facade mặt tiền đơn giản, Proxy làm đại diện".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Ma trận phân biệt 4 mẫu bao bọc (Wrapper Patterns):**
  - **Adapter:** Giữ nguyên chức năng, **thay đổi giao diện** để tương thích.
  - **Decorator:** Giữ nguyên giao diện, **thêm chức năng mới** tại runtime.
  - **Proxy:** Giữ nguyên giao diện, **kiểm soát quyền truy cập** hoặc tải lười (Lazy load).
  - **Facade:** Thay đổi giao diện thành **giao diện mới đơn giản hơn**, che giấu nhiều lớp bên trong.

### 복습 체크리스트
- [ ] Phân biệt được Factory Method (giao việc tạo cho class con) và Abstract Factory (tạo họ đối tượng liên quan).
- [ ] Nhớ Singleton đảm bảo duy nhất 1 instance và dùng cho Connection Pool.
- [ ] Phân biệt được sự khác nhau cốt lõi giữa Adapter (đổi cổng) và Decorator (thêm tính năng).
- [ ] Định nghĩa được vai trò của Facade (giao diện đơn giản che giấu hệ thống con).
