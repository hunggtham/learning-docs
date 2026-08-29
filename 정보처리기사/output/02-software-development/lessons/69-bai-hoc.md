# 핵심 047: 인터페이스 보안, 기능 구현 및 검증 (Interface Security, Implementation, Verification)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **핵심 047: 인터페이스 보안, 기능 구현 및 검증 (Interface Security, Implementation, Verification)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

핵심, 인터페이스, 보안, 기능, 구현, 검증

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 핵심 047: 인터페이스 보안, 기능 구현 및 검증 (Interface Security, Implementation, Verification)

### 네트워크 보안 기술 (Kỹ thuật bảo mật mạng)
- **IPSec (IP Security):** 네트워크 계층 (Network Layer). Chống giả mạo, ẩn giấu gói tin IP.
- **SSL (Secure Socket Layer):** TCP/IP ~ 애플리케이션 계층 사이. Chứng thực, mã hóa (thường dùng cho HTTPS).
- **S-HTTP:** 애플리케이션 계층 (Application Layer). Mã hóa mọi tin nhắn giữa Client và Server.

### 인터페이스 데이터 포맷 (Định dạng dữ liệu giao tiếp)
- **AJAX:** Bất đồng bộ (Asynchronous), dùng JS và XML để cập nhật một phần trang web mà không cần tải lại toàn bộ trang.
- **JSON:** Cặp "Key-Value", định dạng nhẹ, dễ đọc (Thay thế cho XML rất nhiều).
- **XML:** Thẻ Markup đa mục đích (như HTML nhưng tự tạo thẻ được).
- **YAML:** "YAML Ain't Markup Language". Định dạng dữ liệu tuần tự hóa, rất dễ đọc cho con người (hay dùng làm file config).

### 인터페이스 구현 검증 도구 (Công cụ kiểm chứng Test Interface)
- **xUnit:** Test từng "Đơn vị" (Unit) - jUnit, cppUnit.
- **STAF:** Test trong "Môi trường phân tán" (Distributed environment).
- **FitNesse:** Framework test nền web (Điền bảng là tự chạy test).
- **NTAF:** Kết hợp FitNesse + STAF (Do Naver làm).

- **Vietnamese Explanation:** Khi gửi dữ liệu giữa các máy, JSON đang là vua vì nhẹ và dễ nhìn. YAML thì thường dùng để cấu hình server. Khi test xem các máy tính nói chuyện với nhau ổn không, người ta dùng xUnit (Test từng hàm) hoặc STAF (Test qua nhiều máy).
- 💡 **Mẹo ghi nhớ (Mnemonics):** IPSec = Tầng Mạng (IP). SSL = Tầng giữa (Socket). JSON = Key-Value. STAF = Phân tán (Phân tán (Distributed)).

---

# [복습 / 심화 노트 - Revision & Deep Dive Notes]

---
