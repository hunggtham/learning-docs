# 핵심 047: 인터페이스 보안, 기능 구현 및 검증 (Interface Security, Implementation, Verification)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **핵심 047: 인터페이스 보안, 기능 구현 및 검증 (Interface Security, Implementation, Verification)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

핵심, 인터페이스, 보안, 기능, 구현, 검증

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **핵심 046: 인터페이스 설계 확인 (EAI 구축 유형 - EAI Integration Types)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **9. 스키마 3계층 (Three-Schema Architecture)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **핵심 047: 인터페이스 보안, 기능 구현 및 검증 (Interface Security, Implementation, Verification)** và nối nó với **9. 스키마 3계층 (Three-Schema Architecture)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 핵심 047: 인터페이스 보안, 기능 구현 및 검증 (Interface Security, Implementation, Verification)

### 네트워크 보안 기술 (Kỹ thuật bảo mật mạng)
- **IPSec (IP Security):** 네트워크 계층 (Network Layer). Chống giả mạo, ẩn giấu gói tin IP.
- **SSL (Secure Socket Layer):** TCP/IP ~ 애플리케이션 계층 사이. Chứng thực, mã hóa (thường dùng cho HTTPS).
- **S-HTTP:** 애플리케이션 계층 (Application Layer). Mã hóa mọi tin nhắn giữa máy khách (client / 클라이언트) và máy chủ (server / 서버).

### 인터페이스 데이터 포맷 (Định dạng dữ liệu giao tiếp)
- **AJAX:** Bất đồng bộ (Asynchronous), dùng JS và XML để cập nhật một phần trang web mà không cần tải lại toàn bộ trang.
- **JSON:** Cặp "Key-Value", định dạng nhẹ, dễ đọc (Thay thế cho XML rất nhiều).
- **XML:** Thẻ Markup đa mục đích (như HTML nhưng tự tạo thẻ được).
- **YAML:** "YAML Ain't Markup ngôn ngữ (language / 언어)". Định dạng dữ liệu tuần tự hóa, rất dễ đọc cho con người (hay dùng làm file config).

### 인터페이스 구현 검증 도구 (Công cụ kiểm chứng Test Interface)
- **xUnit:** kiểm thử (test / 테스트) từng "Đơn vị" (Unit) - jUnit, cppUnit.
- **STAF:** kiểm thử (test / 테스트) trong "Môi trường phân tán" (Distributed environment).
- **FitNesse:** khung phần mềm (framework / 프레임워크) kiểm thử (test / 테스트) nền web (Điền bảng là tự chạy test).
- **NTAF:** Kết hợp FitNesse + STAF (Do Naver làm).

- **Vietnamese Explanation:** Khi gửi dữ liệu giữa các máy, JSON đang là vua vì nhẹ và dễ nhìn. YAML thì thường dùng để cấu hình máy chủ (server / 서버). Khi kiểm thử (test / 테스트) xem các máy tính nói chuyện với nhau ổn không, người ta dùng xUnit (Test từng hàm) hoặc STAF (Test qua nhiều máy).
- 💡 **Mẹo ghi nhớ (Mnemonics):** IPSec = Tầng Mạng (IP). SSL = Tầng giữa (Socket). JSON = Key-Value. STAF = phân tán (distributed / 분산).

---
