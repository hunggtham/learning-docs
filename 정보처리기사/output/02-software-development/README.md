# Môn 2 — 소프트웨어 개발 (Software Development / Phát triển phần mềm)

Chào mừng bạn đến với tài liệu học tập toàn diện Môn 2 thuộc kỳ thi Kỹ sư xử lý thông tin Hàn Quốc (정보처리기사 필기). 

Toàn bộ nội dung học phần đã được tinh chỉnh, hợp nhất từ các tài liệu rời rạc thành **19 bài học chuyên đề chuẩn mực**, tuân thủ nghiêm ngặt tiêu chuẩn song ngữ Hàn - Việt (한국어 thuật ngữ chuẩn thi kèm giải thích kỹ thuật tiếng Việt), cấu trúc 3 tầng sư phạm không boilerplate và bảng biểu tối ưu cho thiết bị di động.

---

## Danh mục 19 bài học chuyên đề (19 Thematic Master Lessons)

### Chương 1: Cấu trúc dữ liệu, Thuật toán & Tối ưu I/O (자료구조 및 알고리즘)
1. [01. Cấu trúc dữ liệu tuyến tính (선형 자료구조 - Danh sách liên tục, Danh sách liên kết, Stack, Queue, Deque)](lessons/01-cau-truc-du-lieu-tuyen-tinh.md)
2. [02. Ký pháp biểu thức và Ngăn xếp (수식 표기법과 스택 - Infix, Prefix, Postfix & Stack Evaluation)](lessons/02-ky-phap-bieu-thuc-va-stack.md)
3. [03. Cây và Duyệt cây nhị phân (트리 및 이진 트리 운행법 - Cây nhị phân, Preorder, Inorder, Postorder)](lessons/03-cay-va-duyet-cay-nhi-phan.md)
4. [04. Đồ thị và Biểu diễn đồ thị (그래프 및 인접 행렬 - Ma trận kề, Danh sách kề, DFS, BFS, MST)](lessons/04-do-thi-va-bieu-dien-do-thi.md)
5. [05. Thuật toán sắp xếp và Độ phức tạp (정렬 알고리즘 및 시간 복잡도 - Chèn, Chọn, Nổi bọt, Shell, Quick, Heap, Merge, Radix)](lessons/05-thuat-toan-sap-xep-va-do-phuc-tap.md)
6. [06. Thuật toán tìm kiếm và Bảng băm (검색 알고리즘 및 해싱 - Tìm kiếm tuần tự, Tìm kiếm nhị phân, Bảng băm, Hàm băm & Xử lý xung đột)](lessons/06-thuat-toan-tim-kiem-va-bang-bam.md)
7. [07. Cơ sở dữ liệu và Tối ưu hóa truy vấn I/O (데이터베이스 및 쿼리 성능 최적화 - Kiến trúc 3 tầng Schema, Procedural SQL, APM, RBO/CBO)](lessons/07-co-so-du-lieu-va-toi-uu-truy-van.md)

### Chương 2: Thiết kế & Hiện thực Module, Tích hợp hệ thống (모듈 구현 및 시스템 인터페이스)
8. [08. Hiện thực module và Truyền thông liên tiến trình IPC (단위 모듈 구현 및 IPC - Coupling, Cohesion, IPC, Tái sử dụng)](lessons/08-hien-thuc-module-va-ipc.md)
9. [09. Tích hợp hệ thống ứng dụng doanh nghiệp (EAI / ESB 및 연계 통신 - 4 mô hình EAI, ESB, JSON, XML, AJAX, RESTful API)](lessons/09-tich-hop-he-thong-eai-esb.md)
10. [10. Bảo mật giao diện và công cụ kiểm chứng (인터페이스 보안 및 검증 도구 - IPSec AH/ESP/IKE, SSL/TLS, Tripwire, xUnit, STAF, FitNesse, NTAF)](lessons/10-bao-mat-giao-dien-va-kiem-chung.md)

### Chương 3: Đóng gói phần mềm, Quản lý cấu hình & Tự động hóa Build (소프트웨어 패키징 및 형상 관리)
11. [11. Đóng gói phần mềm, DRM và tài liệu phát hành (소프트웨어 패키징 및 저작권 관리 - Quy trình đóng gói 7 bước, Kiến trúc DRM 6 thành phần, Release Note, Manuals)](lessons/11-dong-goi-phan-mem-va-drm.md)
12. [12. Quản lý cấu hình phần mềm (SCM) và Công cụ kiểm soát phiên bản (형상 관리 및 버전 제어 - Baseline, CCB, 4 bước SCM, SVN vs Git)](lessons/12-quan-ly-cau-hinh-scm-va-git.md)
13. [13. Môi trường phát triển tích hợp (IDE) và Tự động hóa Build (통합 개발 환경 및 빌드 자동화 - 4 chức năng IDE, Ant, Maven, Gradle, CI/CD Jenkins)](lessons/13-ide-va-tu-dong-hoa-build.md)

### Chương 4: Quản lý kiểm thử phần mềm (애플리케이션 테스트 관리)
14. [14. Nguyên lý và Phân loại kiểm thử phần mềm (애플리케이션 테스트 원리 및 분류 - 7 nguyên lý kiểm thử, Verification vs Validation, Quy trình 5 bước)](lessons/14-nguyen-ly-va-phan-loai-kiem-thu.md)
15. [15. Kiểm thử hộp trắng và Độ bao phủ mã (화이트박스 테스트 및 테스트 커버리지 - Basis Path Testing, McCabe V(G), Statement/Branch/Condition/MC-DC Coverage)](lessons/15-kiem-thu-hop-trang-va-coverage.md)
16. [16. Kiểm thử hộp đen và Thiết kế Test Case (블랙박스 테스트 및 테스트 케이스 설계 - Phân vùng tương đương, Phân tích giá trị biên, ISO/IEC/IEEE 29119-3)](lessons/16-kiem-thu-hop-den-va-test-case.md)
17. [17. V-Model, Kiểm thử tích hợp và Test Oracle (V-모델, 통합 테스트 및 테스트 오라클 - 4 tầng V-Model, Stub/Driver, 4 loại Test Oracle)](lessons/17-v-model-kiem-thu-tich-hop-va-oracle.md)

### Chương 5: Đảm bảo chất lượng mã nguồn & Tái cấu trúc (코드 품질 및 리팩토링)
18. [18. Mã nguồn sạch, Tái cấu trúc và Phân tích tĩnh (클린 코드, 리팩토링 및 정적 분석 - 5 nguyên tắc Clean Code, Alien Code, Spaghetti Code, Refactoring, PMD, SonarQube)](lessons/18-clean-code-refactoring-va-kiem-tra-tinh.md)

### Phụ lục liên môn: Phân cấp bộ nhớ & Kiến trúc phần cứng liên kết (기억장치 및 컴퓨터 구조)
19. [19. Phân cấp bộ nhớ và Kiến trúc phần cứng liên kết (기억장치 계층 구조 및 컴퓨터 구조 - DRAM vs SRAM, Đĩa từ SLT, CAM, Cache Locality, Bộ nhớ ảo, Flynn)](lessons/19-phan-cap-bo-nho-va-phan-cung-lien-ket.md)

---

## Hướng dẫn phương pháp học tập hiệu quả

1. **Ghi nhớ từ khóa Hàn - Việt song song:** Đề thi trắc nghiệm và tự luận (실기) đều dùng trực tiếp thuật ngữ tiếng Hàn. Luôn chú ý các từ khóa in đậm trong mỗi bài học.
2. **Nắm vững công thức và cơ chế:** 
   - Công thức McCabe $V(G) = E - N + 2 = P + 1$.
   - Công thức thời gian truy cập đĩa $Seek + Latency + Transmission$.
   - Tỷ lệ trúng Cache $H$ và thời gian truy cập hiệu dụng $T_{\text{avg}}$.
   - Số cạnh tối đa của đồ thị có hướng $n(n-1)$ và vô hướng $n(n-1)/2$.
3. **Liên kết ranh giới môn học:** 
   - Bài 07 liên kết trực tiếp với **Môn 3 (데이터베이스 구축 - Cơ sở dữ liệu)**.
   - Bài 19 liên kết trực tiếp với **Môn 4 (프로그래밍 언어 활용 - Hệ điều hành)** và **Môn 5 (정보시스템 구축관리 - Kiến trúc hạ tầng)**.
