# 핵심 035 & 036: 소프트웨어 패키징 및 DRM (Software Packaging & DRM)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **핵심 035 & 036: 소프트웨어 패키징 및 DRM (Software Packaging & DRM)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

핵심, 소프트웨어, 패키징, DRM

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 핵심 035 & 036: 소프트웨어 패키징 및 DRM (Software Packaging & DRM)

### 패키징 고려사항 (Lưu ý khi đóng gói)
- **사용자를 중심**으로 진행. (Phải hướng tới người dùng, không phải lập trình viên).
- 보안, 이기종 연동, 복잡성 및 비효율성 문제 고려, 적합한 암호화 알고리즘 적용. (Bảo mật, liên kết đa nền tảng, dễ dùng, mã hóa).

### DRM (Digital Rights Management - Quản lý bản quyền kỹ thuật số)
- 허가된 권한 범위 내에서 콘텐츠의 이용이 가능하도록 통제하는 기술. (Kỹ thuật mã hóa, chống copy lậu, giới hạn số lần mở/in/sao chép nội dung kỹ thuật số).
- **Thành phần (Cấu trúc DRM):**
  - **Contents Provider (Người cung cấp):** Tác giả, người tạo nội dung.
  - **Contents Distributor (Người phân phối):** Nơi bán/phân phối (App Store, Melon...).
  - **Clearing House (Trung tâm thanh toán / Quản lý):** Quản lý Key (khóa), cấp phép License và tính tiền.
  - **Packager (Bộ đóng gói):** Đóng gói nội dung + Meta data + Mã hóa.
  - **DRM Controller (Bộ điều khiển):** Kiểm soát quyền sử dụng trên máy người dùng.

- **Vietnamese Explanation:** DRM là công nghệ chống vi phạm bản quyền (ví dụ: nhạc tải trên Spotify không thể copy ra máy MP3 thường nghe được). Clearing House là trọng tài ở giữa giữ chìa khóa và thu tiền.
- 💡 **Mẹo ghi nhớ (Mnemonics):** DRM = Chống copy lậu. **Clearing House** = Trạm kiểm soát và cấp phép (Rất hay thi). Firewall (Tường lửa) KHÔNG phải là công nghệ của DRM.

---
