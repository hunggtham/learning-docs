# ⦁ 보안 취약점 및 보안 기능 (Lỗ hổng bảo mật & Chức năng bảo mật)

## 1. 메모리 버퍼 오버플로 (Memory Buffer Overflow / Tràn bộ đệm bộ nhớ)
- **개념**: 연속된 메모리 공간을 사용하는 프로그램에서 할당된 메모리의 범위를 넘어선 위치에서 자료를 읽거나 쓰려고 할 때 발생하는 취약점.
- **Tiếng Việt**: Lỗ hổng xảy ra khi chương trình ghi hoặc đọc dữ liệu vượt quá giới hạn vùng nhớ đã được cấp phát.
- **예시 (Example)**: 
  - (KR) 10바이트 공간에 20바이트의 데이터를 입력하면 다른 메모리 영역을 침범함.
  - (VN) Nhập 20 byte dữ liệu vào mảng chỉ có kích thước 10 byte, làm ghi đè lên các vùng nhớ khác.
- **대책**: 버퍼의 크기를 적절히 설정.
- 💡 **Mẹo ghi nhớ**: Buffer Overflow = Bơm nước quá đầy làm tràn ly.

## 2. 운영체제 명령어 삽입 (OS Command Injection / Tiêm lệnh hệ điều hành)
- **개념**: 외부 입력값을 통해 시스템 명령어의 실행을 유도함으로써 권한을 탈취하거나 장애를 유발하는 취약점.
- **Tiếng Việt**: Chèn các lệnh hệ điều hành thông qua đầu vào của người dùng để thực thi trái phép trên server.
- **예시 (Example)**: 
  - (KR) 웹 입력창에 `; rm -rf /` 와 같은 명령어를 삽입하여 서버 파일을 삭제.
  - (VN) Chèn lệnh `; rm -rf /` vào ô input trên web để xoá file trên máy chủ.
- **대책**: 외부 입력값을 검증 없이 내부 명령어로 사용하지 않음.

## 3. 사이트 간 요청 위조 (CSRF; Cross-Site Request Forgery / Giả mạo yêu cầu liên trang)
- **개념**: 사용자가 자신의 의지와 무관하게 공격자가 의도한 행위를 특정 웹사이트에 요청하게 하는 취약점.
- **Tiếng Việt**: Lợi dụng phiên đăng nhập (session) hợp lệ của người dùng để thực hiện các yêu cầu không mong muốn.
- **예시 (Example)**: 
  - (KR) 로그인된 상태에서 공격자가 보낸 링크를 클릭하면 내 계정에서 몰래 송금이 됨.
  - (VN) Khi đang đăng nhập ngân hàng, lỡ click vào link của hacker thì bị tự động chuyển tiền.
- **대책**: GET 방식 대신 POST 방식 사용, CSRF 토큰 사용.
- 💡 **Mẹo ghi nhớ**: C-S-R-F = Cứ Sợ Rằng Fake (Sợ người dùng thật nhưng gửi request fake).

## 4. 보안 기능 및 에러 처리 (Chức năng bảo mật & Xử lý lỗi)
- **적절한 인증 없이 중요기능 허용 (Missing Authentication)**: 중대한 기능에 재인증이 없음. (Không yêu cầu xác thực lại khi làm việc quan trọng).
- **중요정보 평문 저장 및 전송 (Plaintext Storage/Transmission)**: 패스워드를 암호화 없이 저장/전송. (Lưu hoặc truyền mật khẩu không mã hóa).
- **하드코드된 비밀번호 (Hardcoded Password)**: 소스코드에 비밀번호를 직접 작성. (Ghi cứng mật khẩu trong source code).
- **오류 메시지 통한 정보 노출 (Information Exposure Through Error Message)**: 시스템 내부 구조나 파일 경로가 오류 메시지에 포함되어 노출됨. (Thông báo lỗi làm lộ đường dẫn nội mục hệ thống).
- **예시 (Example)**: 
  - (KR) DB 연결 실패 시 "root 계정 연결 실패" 같은 메시지를 띄우지 않고 "일시적인 오류입니다"로 대체.
  - (VN) Thay vì hiện lỗi "Không kết nối được tài khoản root", chỉ hiển thị "Lỗi hệ thống tạm thời".

---

# ⦁ 코드 오류 및 API 오용 (Lỗi mã nguồn & Dùng sai API)

## 1. 널 포인터 역참조 (Null Pointer Dereference / Tham chiếu ngược con trỏ Null)
- **개념**: 널 포인터(값이 없는 메모리 주소)가 가리키는 메모리에 값을 저장하거나 읽을 때 발생하는 오류.
- **Tiếng Việt**: Lỗi xảy ra khi cố gắng đọc/ghi dữ liệu thông qua con trỏ đang có giá trị Null.
- **예시 (Example)**: 
  - (KR) 객체가 생성되지 않았는데 그 객체의 메서드를 호출하여 시스템이 다운됨.
  - (VN) Gọi hàm của một đối tượng chưa được khởi tạo (bằng Null), làm app bị crash.

## 2. 자원 처리 오류 (Resource Handling Errors)
- **부적절한 자원 해제 (Improper Resource Release)**: 힙 메모리나 소켓을 사용 후 반환(close)하지 않아 자원 고갈 발생. (Không giải phóng bộ nhớ, kết nối sau khi dùng xong).
- **해제된 자원 사용 (Use After Free)**: 반환된 메모리를 다시 참조하여 오작동 유발. (Dùng lại vùng nhớ đã được giải phóng).
- **초기화되지 않은 변수 사용 (Uninitialized Variable)**: 변수 선언 후 값을 넣지 않고 사용하여 이전 쓰레기 값이 노출됨. (Dùng biến chưa khởi tạo giá trị).

## 3. 취약한 API 사용 (Vulnerable API / API dễ bị tổn thương)
- **개념**: 보안 문제로 금지된 함수 (예: C언어의 `strcpy`, `strcat`) 사용.
- **Tiếng Việt**: Sử dụng các hàm không an toàn, dễ gây lỗi tràn bộ đệm (như `strcpy`).
- **예시 (Example)**: 
  - (KR) 길이 제한이 없는 `strcpy()` 대신 길이를 지정하는 `strncpy()` 사용.
  - (VN) Dùng `strncpy()` (có giới hạn độ dài) thay cho `strcpy()` (copy không giới hạn).

---

# 106 암호 알고리즘 (Cryptography Algorithms / Thuật toán mã hoá)

## 1. 암호화 기본 개념 (Concepts)
- **평문 (Plain)**: Bản rõ (chưa mã hoá)
- **암호문 (Cipher)**: Bản mã (đã mã hoá)
- **치환 암호 (Substitution Cipher)**: 문자를 다른 문자로 대체 (Mã hoá thay thế, vd: A -> C).
- **전치 암호 (Transposition Cipher)**: 문자의 위치를 바꿈 (Mã hoá hoán vị, vd: ABC -> BCA).

## 2. 대칭 키 vs 비대칭 키 (Symmetric vs Asymmetric)
- **대칭 키 (Symmetric Key)**: 암호화 키 = 복호화 키 (비밀 키).
  - 속도가 빠름, 키 관리가 어려움 (Nhanh nhưng khó quản lý phân phối key).
  - 종류 (Các loại): DES, AES, SEED, ARIA, IDEA (Block); RC4, LFSR (Stream).
- **비대칭 키 (Asymmetric Key)**: 암호화 키(공개 키) ≠ 복호화 키(개인 키).
  - 속도가 느림, 키 분배 및 관리가 쉬움 (Chậm nhưng dễ phân phối key, an toàn).
  - 종류 (Các loại): RSA, ECC, Diffie-Hellman.
- 💡 **Mẹo ghi nhớ**: 
  - 대칭 (Đại xưng) = 비밀 (Bí mật chung) -> AES, DES.
  - 비대칭 (Bất đại xưng) = 공개 (Công khai 1 nửa) -> RSA.

---

# 107 서비스 공격 기법 (Service Attack Techniques / Kỹ thuật tấn công dịch vụ)

- **Backdoor (백도어)**: 시스템 인증 절차를 우회하여 몰래 접속하는 경로 (Cửa sau, lách xác thực).
- **Key Logger (키로거)**: 키보드 입력 움직임을 탐지하여 비밀번호 등을 탈취 (Ghi lại thao tác bàn phím).
- **Rootkit (루트킷)**: 시스템 침입 사실을 숨기고 관리자 권한을 유지하는 도구 모음 (Bộ công cụ che giấu xâm nhập và giữ quyền admin).
- **Phishing, Smishing, Qshing (피싱, 스미싱, 큐싱)**: 이메일(Phishing), 문자(Smishing), QR코드(Qshing)로 개인정보 탈취 (Lừa đảo lấy thông tin qua mail, SMS, mã QR).
- **Zombie PC & Botnet (좀비 PC & 봇넷)**: 악성 봇에 감염되어 해커(C&C서버)의 명령에 따라 DDoS 공격 등을 수행하는 PC 무리 (Máy tính bị nhiễm bot, bị điều khiển hàng loạt).
- **Ransomware (랜섬웨어)**: 파일을 암호화하고 돈을 요구하는 악성 프로그램 (Mã độc tống tiền).
- **Zero Day Attack (제로데이 공격)**: 취약점이 공표되기도 전에 이루어지는 공격 (Tấn công ngay khi lỗ hổng vừa được phát hiện, chưa có bản vá).
- **Sniffing (스니핑)**: 네트워크 패킷을 몰래 엿보며 정보 수집 (Nghe lén gói tin trên mạng).
- **Spoofing (스푸핑 - IP, ARP)**: 위조된 IP나 MAC 주소로 속여 인증을 통과하거나 패킷을 가로챔 (Giả mạo địa chỉ IP hoặc MAC).
- **Session Hijacking (세션 하이재킹)**: 이미 로그인된 세션 정보를 가로채어 권한 획득 (Cướp phiên đăng nhập).
- 💡 **Mẹo ghi nhớ**: Spoof = 속이다 (Fake/Giả mạo), Sniff = 킁킁거리다 (Nghe lén/Trộm xem).

---

# 108 서버 인증 & 109 접근 제어 (Server Authentication & Access Control)

## 1. 인증 기술 (Authentication Types)
- **지식 기반 (Knowledge)**: 알고 있는 것 (Mật khẩu, mã PIN).
- **소유 기반 (Possession)**: 가지고 있는 것 (Token, Smart Card, OTP).
- **생체 기반 (Biometric)**: 고유한 신체 특징 (Vân tay, mống mắt).
- **행위 기반 (Behavior)**: 행동 특징 (Chữ ký, dáng đi).

## 2. 접근 제어 정책 (Access Control Policies)
- **DAC (임의적 접근 통제 / Discretionary)**: 신분(Identity) 기반. 데이터 소유자가 권한 부여.
- **MAC (강제적 접근 통제 / Mandatory)**: 보안등급(Label) 기반. 시스템 관리자가 강제로 권한 부여.
- **RBAC (역할 기반 접근 통제 / Role-Based)**: 역할(Role) 기반. 변경이 용이.
- 💡 **Mẹo ghi nhớ**: DAC = Danh tính, MAC = Mức độ bảo mật, RBAC = Role (Vai trò).

---

# 110 네트워크 보안 솔루션 (Network Security Solutions)
- **방화벽 (Firewall)**: 트래픽 접근 허용/차단 (Tường lửa cơ bản).
- **WAF (웹 방화벽)**: SQL 인젝션, XSS 등 웹 특화 공격 방어 (Tường lửa chuyên cho Web).
- **IDS (침입 탐지 시스템)**: 침입을 실시간으로 "탐지(Detect)" (Hệ thống phát hiện xâm nhập).
- **IPS (침입 방지 시스템)**: 유해 트래픽을 실시간으로 "차단(Prevent)" (Hệ thống ngăn chặn xâm nhập).
- **VPN (가상사설망)**: 공중망을 전용망처럼 안전하게 사용 (Mạng riêng ảo).

---

# 5과목 추가: 소프트웨어 재사용, 산정 기법, 프레임워크

## 318. 소프트웨어 재사용 (Software Reuse / Tái sử dụng phần mềm)
- **개념**: 검증된 소프트웨어의 일부를 다시 사용 (Sử dụng lại các phần mềm đã được kiểm chứng để giảm chi phí, tăng chất lượng).
- **방법**: 
  - **합성 중심 (Composition-Based)**: 블록 조립 (Lắp ráp các block như Lego).
  - **생성 중심 (Generation-Based)**: 추상적 명세로 코드 자동 생성 (Tự động sinh code từ bản đặc tả).

## 323. 수학적 산정 기법 (Mathematical Estimation Techniques / Kỹ thuật ước lượng toán học)
- **개념**: 통계 공식을 활용한 비용 예측 기법 (Dự toán chi phí dựa trên công thức toán học).
- **종류**:
  - **COCOMO**: LOC(라인 수) 기반 (Dựa vào số dòng code).
  - **Putnam**: 시간에 따른 인력 분포 곡선(Rayleigh-Norden) 활용 (Dựa vào đường cong phân bổ nhân lực).
  - **FP (Function Point)**: 입력, 출력, 인터페이스 등 기능적 요인 기반 (Dựa vào điểm chức năng).

## 336. 소프트웨어 개발 프레임워크 (Software Development Framework)
- **개념**: 개발에 공통 사용되는 구조를 제공하여 생산성을 높이는 기반.
- **특성**: 모듈화, 재사용성, 확장성, **제어의 역흐름(IoC)**.
- **Tiếng Việt**: Nền tảng cấu trúc sẵn giúp tăng năng suất (như Spring, .NET). Đặc tính: Module hóa, Tái sử dụng, Mở rộng, Đảo ngược luồng điều khiển (IoC).
