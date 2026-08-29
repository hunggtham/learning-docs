# 100 & 100-1: 패키징 시 고려사항 및 순서 (Packaging Considerations & Sequence)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **100 & 100-1: 패키징 시 고려사항 및 순서 (Packaging Considerations & Sequence)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

패키징, 고려사항, 순서

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 100 & 100-1: 패키징 시 고려사항 및 순서 (Packaging Considerations & Sequence)

### 패키징 시 고려사항
- 최소 환경 정의 (OS/CPU/RAM). (Phải ghi rõ cấu hình tối thiểu để chạy app).
- UI와 매뉴얼 일치. (Hình ảnh UI trong thực tế và trong tài liệu phải giống nhau).
- 보안 및 암호화, DRM 연동 고려. (Bảo mật, mã hóa, tích hợp chống copy).

### 소프트웨어 패키징 순서 (Trình tự đóng gói)
1. **기능 식별 (Xác định chức năng)**
2. **모듈화 (Module hóa)**
3. **빌드 진행 (Build - Dịch ra file chạy)**
4. **사용자 환경 분석 (Phân tích môi trường người dùng - OS/CPU)**
5. **패키징 및 적용 시험 (Đóng gói & Test thử)**
6. **패키징 변경 개선 (Sửa lỗi nếu có)**
7. **배포 (Deployment - Phát hành)**

- 💡 **Mẹo ghi nhớ (Mnemonics):** Nhận-Mô-Build-Môi-Gói-Cải-Phân (Nhận diện - Module - Build - Môi trường - Đóng gói - Cải tiến - Phân phối).

---
