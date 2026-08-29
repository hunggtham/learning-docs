# 핵심 037 & 038: 매뉴얼 및 빌드/배포 도구 (Manuals & Build/Deploy Tools)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **핵심 037 & 038: 매뉴얼 및 빌드/배포 도구 (Manuals & Build/Deploy Tools)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

핵심, 매뉴얼, 빌드, 배포, 도구

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 핵심 037 & 038: 매뉴얼 및 빌드/배포 도구 (Manuals & Build/Deploy Tools)

### 제품 소프트웨어 매뉴얼 (Tài liệu hướng dẫn)
- **설치 매뉴얼 (Installation Manual):** Hướng dẫn cài đặt. (Lưu ý cách cài, cấu hình hệ thống, cách xóa cài đặt - Uninstall).
- **사용자 매뉴얼 (User Manual):** Hướng dẫn sử dụng. (Giao diện UI, cấu hình tối thiểu, cách dùng tính năng).
- Cả hai đều phải viết theo góc nhìn của **사용자 (Người dùng)**.

### 빌드 및 모니터링 도구 (Công cụ Build & Monitoring)
- **빌드 자동화 도구 (Build Automation):** Biến source code thành file chạy một cách tự động. Ví dụ: Ant, Maven, Gradle, **Jenkins**.
- **버전 관리 도구 (Version Control):** Git, SVN.
- **정적 분석 도구 (Static Analysis):** Phân tích code tìm lỗi mà **KHÔNG CHẠY** chương trình. Ví dụ: PMD, Cppcheck, SonarQube.
- **동적 분석 도구 (Dynamic Analysis):** Vừa **CHẠY** chương trình vừa tìm lỗi (tràn bộ nhớ, v.v.). Ví dụ: Avalanche, Valgrind.

- **Vietnamese Explanation:** "Tĩnh" (Static) nghĩa là code nằm im trên giấy, dùng tool soi từng dòng xem có viết sai cú pháp hay không. "Động" (Dynamic) là bấm nút chạy phần mềm rồi xem nó có bị sập hay tốn RAM không.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Tĩnh (Static) = PMD, SonarQube (Soi code). Động (Dynamic) = Valgrind (Chạy thử). Build = Jenkins (Ông quản gia tự động).

---
