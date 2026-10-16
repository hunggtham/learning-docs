# Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)

## Bài học tổng hợp
- [Tài liệu học đầy đủ (Tổng quan)](01-tai-lieu-hoc-day-du.md)

---

## Danh mục 18 Chuyên đề Chuẩn mực theo Syllabus HRDK/Q-Net

Hệ thống bài học Môn 5 được rà soát, tái cấu trúc và hợp nhất toàn diện từ 86 bài học cũ thành **18 chuyên đề chuẩn mực**, đảm bảo chuẩn song ngữ Hàn - Việt kỹ thuật sâu sắc, mô hình 3 vế liên kết kiến thức, cấu trúc 2 tầng (Tầng A: Nén thi - Tầng B: Hiểu sâu hệ thống) và checklist ôn tập thực tế:

1. [Chuyên đề 01: Phương pháp luận & Khung phát triển Phần mềm (소프트웨어 개발 방법론 및 프레임워크)](lessons/01-phuong-phap-luan-va-framework.md)
   *Vòng đời phát triển SDLC, mô hình Agile/Scrum/XP, Tailoring phương pháp luận và Spring/eGovFrame.*
2. [Chuyên đề 02: Tái sử dụng & Công cụ Kỹ nghệ Phần mềm CASE (소프트웨어 재사용, 재공학 및 CASE 도구)](lessons/02-tai-su-dung-va-cong-cu-case.md)
   *Tái sử dụng (Reuse), tái kỹ nghệ (Re-engineering), kỹ nghệ ngược (Reverse Engineering) và công cụ CASE.*
3. [Chuyên đề 03: Quản lý Dự án, Chi phí & Tiến độ (프로젝트 관리, 비용 산정 및 일정 관리)](lessons/03-quan-ly-du-an-chi-phi-va-tien-do.md)
   *Mô hình toán học COCOMO, Putnam, Function Point (FP), sơ đồ mạng CPM/PERT và kỹ thuật đường găng Critical Path.*
4. [Chuyên đề 04: Tiêu chuẩn Chất lượng Phần mềm & Mô hình CMMI (품질 표준 및 프로세스 성숙도 CMMI/SPICE)](lessons/04-tieu-chuan-chat-luong-va-cmmi.md)
   *ISO/IEC 9126, 25010 (SQuaRE), 12119, 14598, mô hình trưởng thành CMMI 5 cấp độ và tiêu chuẩn SPICE (ISO 15504).*
5. [Chuyên đề 05: Khung Bảo mật Phần mềm & Hành lang Pháp lý (소프트웨어 보안 프레임워크 및 관련 법규)](lessons/05-khung-bao-mat-phan-mem-va-phap-luat.md)
   *Nguyên tắc CIA Triad, Secure SDLC (Seven Touchpoints, MS SDL), Luật bảo vệ thông tin cá nhân và quy định an toàn.*
6. [Chuyên đề 06: Lỗ hổng Phần mềm & Lập trình An toàn Secure Coding (SW 보안 취약점 및 시큐어 코딩)](lessons/06-lo-hong-phan-mem-va-secure-coding.md)
   *Buffer Overflow, OS Command Injection, SQL Injection, XSS vs CSRF, Null Pointer Dereference, Race Condition và 7 nhóm CWE.*
7. [Chuyên đề 07: Mật mã học & Thuật toán Mã hóa (암호학 및 암호 알고리즘 체계)](lessons/07-thuat-toan-ma-hoa-va-mat-ma-hoc.md)
   *Mã hóa đối xứng (DES, AES, SEED, ARIA), mã hóa bất đối xứng (RSA, ECC), hàm băm một chiều (SHA, MD5) và chế độ khối.*
8. [Chuyên đề 08: Xác thực & Kiểm soát Truy cập (인증 기술 및 접근 통제 체계)](lessons/08-xac-thuc-va-kiem-soat-truy-cap.md)
   *Mô hình xác thực (SSO, MFA, sinh trắc học, Kerberos, RADIUS), ma trận kiểm soát truy cập (DAC, MAC, RBAC) và mô hình Bell-LaPadula/Biba.*
9. [Chuyên đề 09: Tấn công Mạng & Mối đe dọa An ninh (네트워크 공격 유형 및 보안 위협)](lessons/09-tan-cong-mang-va-nguy-co-an-ninh.md)
   *Từ chối dịch vụ (DoS/DDoS, SYN Flooding, Smurf), tấn công giả mạo (ARP/IP/DNS Spoofing), Sniffing, APT, Ransomware và Zero-day.*
10. [Chuyên đề 10: Thiết bị, Giải pháp Bảo mật Mạng & Giám sát Log (네트워크 보안 장비, 침입 탐지 및 로그 분석)](lessons/10-giai-phap-va-thiet-bi-bao-mat-mang.md)
    *Firewall các thế hệ, IDS (Misuse/Anomaly) vs IPS, WAF, VPN (IPsec/SSL), SIEM, ESM và phân tích log hệ điều hành Linux/Windows.*
11. [Chuyên đề 11: Truyền thông Dữ liệu, Điều chế & Đa hợp (데이터 통신, 변조 기술 및 다중화)](lessons/11-truyen-thong-du-lieu-va-dieu-che.md)
    *Băng thông, điều chế số (ASK, FSK, PSK, QAM), kỹ thuật ghép kênh (FDM, TDM, WDM), kiểm soát luồng và sửa lỗi (Parity, CRC, ARQ).*
12. [Chuyên đề 12: Mạng Máy tính, Mô hình OSI & Giao thức TCP/IP (네트워크 아키텍처, OSI 7계층 및 TCP/IP)](lessons/12-mang-may-tinh-va-giao-thuc-tcp-ip.md)
    *Mô hình OSI 7 tầng vs TCP/IP 4 tầng, định dạng IPv4 vs IPv6, Subnetting (CIDR/VLSM), bắt tay 3 bước TCP vs UDP và định tuyến.*
13. [Chuyên đề 13: Hệ điều hành, Quản lý Tiến trình & Điều phối (운영체제, 프로세스 관리 및 CPU 스케줄링)](lessons/13-he-dieu-hanh-tien-trinh-va-dieu-phoi.md)
    *Cấu trúc nhân Linux/UNIX, vòng đời Process vs Thread, thuật toán điều phối CPU (FCFS, SJF, RR, HRN), giải quyết Deadlock (Coffman).*
14. [Chuyên đề 14: Quản lý Bộ nhớ, Bộ nhớ Ảo & Hệ thống Lưu trữ (메모리 관리, 가상 메모리 및 스토리지)](lessons/14-quan-ly-bo-nho-va-luu-tru-storage.md)
    *Phân mảnh nội/ngoại, Paging vs Segmentation, thuật toán thay thế trang (FIFO, LRU, LFU), Thrashing, Working Set và RAID (0-6).*
15. [Chuyên đề 15: Quản trị Cơ sở Dữ liệu, Phục hồi, Điều khiển Đồng thời & Dữ liệu Lớn (DB 회복, 병행 제어 및 빅데이터)](lessons/15-quan-tri-co-so-du-lieu-va-big-data.md)
    *Tính chất ACID, điều khiển đồng thời (Locking 2PL, Timestamp), kỹ thuật phục hồi (Log-based Undo/Redo, Checkpoint) và hệ sinh thái Hadoop NoSQL.*
16. [Chuyên đề 16: Điện toán Đám mây & Xu hướng Công nghệ Mới (클라우드 컴퓨팅 및 최신 IT 기술)](lessons/16-dien-toan-dam-may-va-cong-nghe-moi.md)
    *Mô hình đám mây IaaS/PaaS/SaaS, Microservices Architecture (MSA), Docker, Kubernetes, IoT, Blockchain và Trí tuệ nhân tạo (AI).*
17. [Chuyên đề 17: Lập trình C, Con trỏ và Cấu trúc Bộ nhớ (C 언어, 포인터 및 메모리 구조)](lessons/17-lap-trinh-c-va-cau-truc-bo-nho.md)
    *Phân loại ngôn ngữ lập trình, lệnh rẽ nhánh break/continue, mảng 1D/2D, chuỗi ký tự kết thúc bằng '\0', toán tử con trỏ (&, \*) và mối liên hệ bảo mật vùng nhớ.*
18. [Chuyên đề 18: Lập trình Python, Cấu trúc Dữ liệu và Tự động hóa (Python 프로그래밍, 자료구조 및 시스템 자동화)](lessons/18-lap-trinh-python-va-tu-dong-hoa.md)
    *Cú pháp kịch bản, I/O, ép kiểu, 4 tập hợp (List, Tuple, Set, Dict), cắt lát Slicing, lập trình hướng đối tượng OOP, try-except và tự động hóa hệ thống.*
