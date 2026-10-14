# 45. V-모델 (V-Model) 기반 애플리케이션 테스트 단계

## 45. V-모델 (V-Model) 기반 애플리케이션 테스트 단계
개발 단계와 테스트 단계를 짝지어 놓은 모델.
1. **단위 테스트 (Unit Test)** - *구현(Code)* 단계와 짝. 모듈/컴포넌트 초점 (주로 구조 기반/화이트박스).
2. **통합 테스트 (Integration Test)** - *설계(Design)* 단계와 짝. 모듈들을 결합하여 테스트.
   * **하향식 (Top-down)**: 스텁(Stub) 사용. 깊이/넓이 우선. 테스트 초기부터 시스템 구조 파악 가능.
   * **상향식 (Bottom-up)**: 드라이버(Driver)와 클러스터(Cluster) 사용.

---

- **Bandwidth (대역폭/전송률 - Băng thông):** Tốc độ truyền dữ liệu tối đa trong 1 giây (đơn vị bit/s hoặc byte/s). Băng thông càng lớn máy càng nhanh.
- **접근 속도 (Tốc độ tiếp cận Nhanh -> Chậm):** CPU 레지스터 -> Cache -> RAM(Main Memory) -> ROM -> 자기 코어 -> 자기 디스크 (HDD) -> 자기 테이프 (Tape).

### ROM (Read Only Memory - Bộ nhớ chỉ đọc)
Phần “ROM (Read Only Memory - Bộ nhớ chỉ đọc)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 전원이 꺼져도 내용이 지워지지 않는 비휘발성 (Không bay hơi khi mất điện).
- 주로 기본 입·출력 시스템(BIOS), 자가 진단 프로그램(POST) 저장 (Thường chứa BIOS, POST).
- **ROM 종류 (Các loại ROM):**
  - Mask ROM: Nhà máy làm sẵn, không đổi được.
  - PROM: Ghi được **1번** (1 lần).
  - EPROM: 자외선 (Tia cực tím - UV) để xóa, ghi lại nhiều lần.
  - EEPROM (EAROM): 전기적인 방법 (Phương pháp điện - Electrical) để xóa và ghi. (Ví dụ: USB Flash Drive, SSD).

- **Vietnamese Explanation:** Cycle Time luôn dài hơn Access Time vì bộ nhớ cần thời gian phục hồi lại năng lượng sau khi đọc. ROM giữ lại dữ liệu khi mất điện, có nhiều loại từ cứng nhắc (Mask) đến linh hoạt (EEPROM - dùng điện để xóa).
- **Ví dụ (Example):** EEPROM chính là công nghệ đằng sau cái USB nhỏ xinh bạn hay dùng. EPROM thì giống cái bảng viết phấn, bôi đi bằng tia UV (giẻ lau) rồi viết lại. Mask ROM là bia đá khắc chữ sẵn.
- 💡 **Mẹo ghi nhớ (Mnemonics):** "E" đầu tiên = Erasable (Xóa được). Nhớ: EPROM = UV (Tia cực tím), EEPROM = Điện (Electonic). Cycle Time ≥ Access Time.
