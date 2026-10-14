# 199. 검사 전략 (Testing Strategies / Chiến lược kiểm thử)

## 199. 검사 전략 (Testing Strategies / Chiến lược kiểm thử)
Phần “199. 검사 전략 (Testing Strategies / Chiến lược kiểm thử)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **단위 검사 (Unit Testing)**: 코딩 후 최소 단위인 '모듈' 초점 검사 (화이트 박스 기법).
- **하향식 통합 검사 (Top-Down Integration)**: 상위 모듈 -> 하위 모듈 방향. 임시 시험용 모듈인 **스터브(Stub)** 필요.
- **상향식 통합 검사 (Bottom-Up Integration)**: 하위 모듈 -> 상위 모듈 방향. 제어 모듈과 종속 모듈 그룹인 **클러스터(Cluster)**와 드라이버(Driver) 필요. (Stub 불필요).
- **검증(확인) 검사 (Validation Testing)**: 요구사항 충족 여부 확인 (블랙 박스 기법).
  - **알파 검사 (Alpha Test)**: **개발자 환경(장소)**에서 사용자가 테스트 (통제된 환경).
  - **베타 검사 (Beta Test)**: **실제 사용자 환경**에서 여러 사용자가 테스트 (개발자 통제 없음).
- **시스템 검사 (System Test)**: 전체 시스템(하드웨어 포함)에서 완벽히 수행되는지 검사. (복구/보안/강도/성능 검사).

**Giải thích (Vietnamese):**
- Kiểm thử tích hợp từ trên xuống (Top-down) cần làm các module giả (Stub) để thay thế cho module con chưa code xong. Từ dưới lên (Bottom-up) cần nhóm (Cluster/Driver) để gọi module con.
- Alpha Test: Bạn mời khách hàng đến công ty bạn ngồi test app trước mặt bạn.
- Beta Test: Bạn tung app lên store cho người dùng tải về dùng thử và báo lỗi (bạn không ngồi cạnh họ).

**💡 Mẹo ghi nhớ (Mnemonics):**
**하스 상드** (Hạ - Stub, Thượng - Driver): **하**향식 = **스**터브(Stub). **상**향식 = 드라이버(Driver)/클러스터(Cluster).

---
