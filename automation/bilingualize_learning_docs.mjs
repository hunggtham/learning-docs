#!/usr/bin/env node

/**
 * Vietnamese-first retrofit for authored learning Markdown.
 *
 * The pass deliberately keeps code, inline code, links, raw/imported captures
 * and generated site files out of scope. It translates a bounded set of common
 * conceptual terms; every prose occurrence keeps Vietnamese first and the
 * English/Korean lookup keywords immediately beside it.
 */

import { readFile, readdir, writeFile } from 'node:fs/promises';
import path from 'node:path';

const ROOT = process.cwd();
const forceStructural = process.argv.includes('--force-structural');
const EXCLUDED_SEGMENTS = new Set([
  '.git', 'node_modules', 'raw', 'raw_md', 'input', 'notion',
  'generated_markdown', 'generated_markdown_translated', 'workflow-output',
  'site'
]);
const EXCLUDED_TOP = new Set(['learning-library']);
const STRUCTURAL_FILES = new Set(['CATALOG.md']);

// Long phrases must come before their component words. Keep this list bounded:
// the goal is readable prose, not a bilingual gloss after every noun.
const TERMS = [
  ['frontend development knowledge library', 'thư viện kiến thức phát triển giao diện web', 'frontend development knowledge library', '프런트엔드 개발 지식 라이브러리'],
  ['backend development knowledge library', 'thư viện kiến thức phát triển phía máy chủ', 'backend development knowledge library', '백엔드 개발 지식 라이브러리'],
  ['computer science knowledge library', 'thư viện kiến thức khoa học máy tính', 'computer science knowledge library', '컴퓨터 과학 지식 라이브러리'],
  ['data engineering knowledge library', 'thư viện kiến thức kỹ thuật dữ liệu', 'data engineering knowledge library', '데이터 엔지니어링 지식 라이브러리'],
  ['Python knowledge library', 'thư viện kiến thức Python', 'Python knowledge library', '파이썬 지식 라이브러리'],
  ['world history knowledge library', 'thư viện kiến thức lịch sử thế giới', 'world history knowledge library', '세계사 지식 라이브러리'],
  ['JVM class loader', 'bộ nạp lớp JVM', 'JVM class loader', 'JVM 클래스 로더'],
  ['bytecode instruction', 'lệnh bytecode', 'bytecode instruction', '바이트코드 명령어'],
  ['machine multiply instruction', 'lệnh nhân của máy', 'machine multiply instruction', '기계 곱셈 명령어'],
  ['library algorithms', 'thuật toán thư viện', 'library algorithms', '라이브러리 알고리즘'],
  ['source type', 'kiểu ở mã nguồn', 'source type', '소스 타입'],
  ['final instructions', 'các lệnh cuối', 'final instructions', '최종 명령어'],
  ['CPU-bound loop', 'vòng lặp giới hạn bởi CPU', 'CPU-bound loop', 'CPU 바운드 루프'],
  ['kernel boundary', 'ranh giới nhân hệ điều hành', 'kernel boundary', '커널 경계'],
  ['language arithmetic layer', 'tầng số học của ngôn ngữ', 'language arithmetic layer', '언어 산술 계층'],
  ['DB constraint error', 'lỗi ràng buộc cơ sở dữ liệu', 'DB constraint error', 'DB 제약조건 오류'],
  ['end-to-end diagram', 'sơ đồ đầu-cuối', 'end-to-end diagram', '엔드투엔드 다이어그램'],
  ['high-level developer', 'nhà phát triển cấp cao', 'high-level developer', '고수준 개발자'],
  ['cache miss', 'trượt bộ nhớ đệm', 'cache miss', '캐시 미스'],
  ['knowledge library', 'thư viện kiến thức', 'knowledge library', '지식 라이브러리'],
  ['frontend development', 'phát triển giao diện web', 'frontend development', '프런트엔드 개발'],
  ['backend development', 'phát triển phía máy chủ', 'backend development', '백엔드 개발'],
  ['native mobile development', 'phát triển di động bản địa', 'native mobile development', '네이티브 모바일 개발'],
  ['computer science', 'khoa học máy tính', 'computer science', '컴퓨터 과학'],
  ['software engineering', 'kỹ nghệ phần mềm', 'software engineering', '소프트웨어 공학'],
  ['platform engineering', 'kỹ thuật nền tảng', 'platform engineering', '플랫폼 엔지니어링'],
  ['data engineering', 'kỹ thuật dữ liệu', 'data engineering', '데이터 엔지니어링'],
  ['web platform', 'nền tảng Web', 'web platform', '웹 플랫폼'],
  ['Kubernetes workloads', 'các tải công việc Kubernetes', 'Kubernetes workloads', '쿠버네티스 워크로드'],
  ['workload abstraction', 'lớp trừu tượng tải công việc', 'workload abstraction', '워크로드 추상화'],
  ['scheduling unit', 'đơn vị lập lịch', 'scheduling unit', '스케줄링 단위'],
  ['service discovery', 'khám phá dịch vụ', 'service discovery', '서비스 디스커버리'],
  ['service abstraction', 'lớp trừu tượng dịch vụ', 'service abstraction', '서비스 추상화'],
  ['data plane', 'mặt phẳng dữ liệu', 'data plane', '데이터 플레인'],
  ['control loop', 'vòng điều khiển', 'control loop', '제어 루프'],
  ['target port', 'cổng đích', 'target port', '대상 포트'],
  ['network policy', 'chính sách mạng', 'network policy', '네트워크 정책'],
  ['load balancer', 'bộ cân bằng tải', 'load balancer', '로드 밸런서'],
  ['resource request', 'yêu cầu tài nguyên', 'resource request', '리소스 요청'],
  ['memory limit', 'giới hạn bộ nhớ', 'memory limit', '메모리 제한'],
  ['CPU limit', 'giới hạn CPU', 'CPU limit', 'CPU 제한'],
  ['resource tuning', 'điều chỉnh tài nguyên', 'resource tuning', '리소스 튜닝'],
  ['failure behavior', 'hành vi khi thất bại', 'failure behavior', '실패 동작'],
  ['critical service', 'dịch vụ trọng yếu', 'critical service', '핵심 서비스'],
  ['page table', 'bảng trang', 'page table', '페이지 테이블'],
  ['hot path', 'đường xử lý nóng', 'hot path', '핫 패스'],
  ['final result', 'kết quả cuối', 'final result', '최종 결과'],
  ['current ISA', 'ISA hiện tại', 'current ISA', '현재 ISA'],
  ['business logic', 'lô-gic nghiệp vụ', 'business logic', '비즈니스 로직'],
  ['causal chain', 'chuỗi nhân quả', 'causal chain', '인과 사슬'],
  ['feedback loop', 'vòng phản hồi', 'feedback loop', '피드백 루프'],
  ['linear model', 'mô hình tuyến tính', 'linear model', '선형 모델'],
  ['linear system', 'hệ tuyến tính', 'linear system', '선형 시스템'],
  ['container image', 'ảnh bộ chứa', 'container image', '컨테이너 이미지'],
  ['team capability', 'năng lực nhóm', 'team capability', '팀 역량'],
  ['shared state', 'trạng thái dùng chung', 'shared state', '공유 상태'],
  ['stack trace', 'dấu vết ngăn xếp', 'stack trace', '스택 트레이스'],
  ['dynamic model', 'mô hình động', 'dynamic model', '동적 모델'],
  ['dynamic system', 'hệ động', 'dynamic system', '동적 시스템'],
  ['hash table', 'bảng băm', 'hash table', '해시 테이블'],
  ['state transition', 'chuyển tiếp trạng thái', 'state transition', '상태 전이'],
  ['product owner', 'chủ sản phẩm', 'product owner', '제품 책임자'],
  ['current state', 'trạng thái hiện tại', 'current state', '현재 상태'],
  ['public API', 'API công khai', 'public API', '공개 API'],
  ['complexity analysis', 'phân tích độ phức tạp', 'complexity analysis', '복잡도 분석'],
  ['transport layer', 'tầng vận chuyển', 'transport layer', '전송 계층'],
  ['timeout budget', 'ngân sách thời gian chờ', 'timeout budget', '타임아웃 예산'],
  ['distributed system', 'hệ thống phân tán', 'distributed system', '분산 시스템'],
  ['semantic model', 'mô hình ngữ nghĩa', 'semantic model', '의미 모델'],
  ['integration test', 'kiểm thử tích hợp', 'integration test', '통합 테스트'],
  ['external system', 'hệ thống bên ngoài', 'external system', '외부 시스템'],
  ['audit log', 'nhật ký kiểm tra', 'audit log', '감사 로그'],
  ['binary search', 'tìm kiếm nhị phân', 'binary search', '이진 탐색'],
  ['code review', 'rà soát mã', 'code review', '코드 리뷰'],
  ['matrix multiplication', 'phép nhân ma trận', 'matrix multiplication', '행렬 곱셈'],
  ['capability model', 'mô hình năng lực', 'capability model', '역량 모델'],
  ['call stack', 'ngăn xếp lời gọi', 'call stack', '호출 스택'],
  ['heap memory', 'bộ nhớ vùng động', 'heap memory', '힙 메모리'],
  ['measurement error', 'sai số đo lường', 'measurement error', '측정 오차'],
  ['ordering constraint', 'ràng buộc thứ tự', 'ordering constraint', '순서 제약'],
  ['support level', 'mức hỗ trợ', 'support level', '지원 수준'],
  ['copy-on-write', 'sao chép khi ghi', 'copy-on-write', '쓰기 시 복사'],
  ['rollback strategy', 'chiến lược quay lui', 'rollback strategy', '롤백 전략'],
  ['inference engine', 'bộ máy suy luận', 'inference engine', '추론 엔진'],
  ['device driver', 'trình điều khiển thiết bị', 'device driver', '장치 드라이버'],
  ['population model', 'mô hình quần thể', 'population model', '개체군 모델'],
  ['geometry model', 'mô hình hình học', 'geometry model', '기하 모델'],
  ['lifetime scope', 'phạm vi tồn tại', 'lifetime scope', '수명 범위'],
  ['config file', 'tệp cấu hình', 'config file', '구성 파일'],
  ['window function', 'hàm cửa sổ', 'window function', '윈도우 함수'],
  ['agent system', 'hệ tác nhân', 'agent system', '에이전트 시스템'],
  ['join condition', 'điều kiện nối', 'join condition', '조인 조건'],
  ['sample size', 'cỡ mẫu', 'sample size', '표본 크기'],
  ['result set', 'tập kết quả', 'result set', '결과 집합'],
  ['physical model', 'mô hình vật lý', 'physical model', '물리 모델'],
  ['port mapping', 'ánh xạ cổng', 'port mapping', '포트 매핑'],
  ['entity relationship', 'quan hệ thực thể', 'entity relationship', '개체 관계'],
  ['lock contention', 'tranh chấp khóa', 'lock contention', '잠금 경합'],
  ['package manager', 'trình quản lý gói', 'package manager', '패키지 관리자'],
  ['image processing', 'xử lý ảnh', 'image processing', '이미지 처리'],
  ['infrastructure as code', 'hạ tầng dưới dạng mã', 'infrastructure as code', '코드형 인프라'],
  ['stress test', 'kiểm thử sức chịu tải', 'stress test', '스트레스 테스트'],
  ['trace context', 'ngữ cảnh dấu vết', 'trace context', '추적 컨텍스트'],
  ['requirement analysis', 'phân tích yêu cầu', 'requirement analysis', '요구사항 분석'],
  ['conflict resolution', 'giải quyết xung đột', 'conflict resolution', '충돌 해결'],
  ['internal state', 'trạng thái nội bộ', 'internal state', '내부 상태'],
  ['critical path', 'đường găng', 'critical path', '임계 경로'],
  ['governance policy', 'chính sách quản trị', 'governance policy', '거버넌스 정책'],
  ['loss function', 'hàm mất mát', 'loss function', '손실 함수'],
  ['test case', 'trường hợp kiểm thử', 'test case', '테스트 케이스'],
  ['test suite', 'bộ kiểm thử', 'test suite', '테스트 스위트'],
  ['code path', 'đường đi mã', 'code path', '코드 경로'],
  ['build system', 'hệ thống dựng', 'build system', '빌드 시스템'],
  ['database query', 'truy vấn cơ sở dữ liệu', 'database query', '데이터베이스 쿼리'],
  ['query plan', 'kế hoạch truy vấn', 'query plan', '쿼리 계획'],
  ['feature flag', 'cờ tính năng', 'feature flag', '기능 플래그'],
  ['release process', 'quy trình phát hành', 'release process', '릴리스 프로세스'],
  ['recovery strategy', 'chiến lược khôi phục', 'recovery strategy', '복구 전략'],
  ['market value', 'giá trị thị trường', 'market value', '시장 가치'],
  ['training data', 'dữ liệu huấn luyện', 'training data', '학습 데이터'],
  ['load test', 'kiểm thử tải', 'load test', '부하 테스트'],
  ['project structure', 'cấu trúc dự án', 'project structure', '프로젝트 구조'],
  ['problem space', 'không gian bài toán', 'problem space', '문제 공간'],
  ['decision tree', 'cây quyết định', 'decision tree', '의사결정 트리'],
  ['canonical file', 'tệp chuẩn gốc', 'canonical file', '정본 파일'],
  ['knowledge connection', 'liên kết kiến thức', 'knowledge connection', '지식 연결'],
  ['class file', 'tệp lớp', 'class file', '클래스 파일'],
  ['JIT compiler', 'trình biên dịch JIT', 'JIT compiler', 'JIT 컴파일러'],
  ['native machine code', 'mã máy bản địa', 'native machine code', '네이티브 기계어'],
  ['execution unit', 'đơn vị thực thi', 'execution unit', '실행 유닛'],
  ['data request', 'yêu cầu dữ liệu', 'data request', '데이터 요청'],
  ['user process', 'tiến trình người dùng', 'user process', '사용자 프로세스'],
  ['user mode', 'chế độ người dùng', 'user mode', '사용자 모드'],
  ['system call', 'lời gọi hệ thống', 'system call', '시스템 호출'],
  ['file access', 'truy cập tệp', 'file access', '파일 접근'],
  ['network access', 'truy cập mạng', 'network access', '네트워크 접근'],
  ['language layer', 'tầng ngôn ngữ', 'language layer', '언어 계층'],
  ['source line', 'dòng mã nguồn', 'source line', '소스 코드 줄'],
  ['error propagation', 'lan truyền lỗi', 'error propagation', '오류 전파'],
  ['failure domain', 'miền lỗi', 'failure domain', '장애 도메인'],
  ['state identity', 'định danh trạng thái', 'state identity', '상태 식별성'],
  ['memory and cache', 'bộ nhớ và bộ nhớ đệm', 'memory and cache', '메모리와 캐시'],
  ['browser support', 'mức hỗ trợ trình duyệt', 'browser support', '브라우저 지원'],
  ['language idiom', 'lối viết quen dùng của ngôn ngữ', 'language idiom', '언어 관용구'],
  ['coding pattern', 'mẫu lập trình', 'coding pattern', '코딩 패턴'],
  ['programming pattern', 'mẫu lập trình', 'programming pattern', '프로그래밍 패턴'],
  ['design pattern', 'mẫu thiết kế', 'design pattern', '디자인 패턴'],
  ['box model', 'mô hình hộp', 'box model', '박스 모델'],
  ['normal flow', 'luồng bố cục thông thường', 'normal flow', '일반 흐름'],
  ['formatting context', 'ngữ cảnh định dạng', 'formatting context', '서식 컨텍스트'],
  ['containing block', 'khối chứa tham chiếu', 'containing block', '컨테이닝 블록'],
  ['intrinsic sizing', 'định cỡ nội tại', 'intrinsic sizing', '내재 크기 결정'],
  ['stacking context', 'ngữ cảnh xếp chồng', 'stacking context', '쌓임 맥락'],
  ['application model', 'mô hình ứng dụng', 'application model', '애플리케이션 모델'],
  ['runtime semantics', 'ngữ nghĩa thời gian chạy', 'runtime semantics', '런타임 의미론'],
  ['browser boundary', 'ranh giới trình duyệt', 'browser boundary', '브라우저 경계'],
  ['security boundary', 'ranh giới bảo mật', 'security boundary', '보안 경계'],
  ['performance evidence', 'bằng chứng hiệu năng', 'performance evidence', '성능 증거'],
  ['state ownership', 'quyền sở hữu trạng thái', 'state ownership', '상태 소유권'],
  ['framework track', 'nhánh học khung phần mềm', 'framework track', '프레임워크 트랙'],
  ['production evidence', 'bằng chứng vận hành', 'production evidence', '운영 증거'],
  ['browser storage', 'lưu trữ trình duyệt', 'browser storage', '브라우저 저장소'],
  ['source map', 'bản đồ mã nguồn', 'source map', '소스 맵'],
  ['application contract', 'đặc tả ứng dụng', 'application contract', '애플리케이션 계약'],
  ['API contract', 'đặc tả API', 'API contract', 'API 계약'],
  ['browser platform', 'nền tảng trình duyệt', 'browser platform', '브라우저 플랫폼'],
  ['framework semantics', 'ngữ nghĩa khung phần mềm', 'framework semantics', '프레임워크 의미론'],
  ['resource hints', 'gợi ý tài nguyên', 'resource hints', '리소스 힌트'],
  ['formatting model', 'mô hình định dạng', 'formatting model', '포매팅 모델'],
  ['production architecture', 'kiến trúc vận hành', 'production architecture', '운영 아키텍처'],
  ['legacy layer', 'tầng cũ', 'legacy layer', '레거시 계층'],
  ['learning spine', 'trục học', 'learning spine', '학습 축'],
  ['framework magic', 'phép màu của khung phần mềm', 'framework magic', '프레임워크 마법'],
  ['canonical owner', 'đơn vị sở hữu chuẩn gốc', 'canonical owner', '정본 소유자'],
  ['learning flow', 'mạch học', 'learning flow', '학습 흐름'],
  ['event loop', 'vòng lặp sự kiện', 'event loop', '이벤트 루프'],
  ['source of truth', 'nguồn chuẩn', 'source of truth', '정본'],
  ['object representation', 'biểu diễn đối tượng', 'object representation', '객체 표현'],
  ['semantic meaning', 'ý nghĩa', 'semantic meaning', '의미적 뜻'],
  ['machine code', 'mã máy', 'machine code', '기계어'],
  ['request path', 'đường đi của yêu cầu', 'request path', '요청 경로'],
  ['accessibility tree', 'cây khả năng tiếp cận', 'accessibility tree', '접근성 트리'],
  ['data structure', 'cấu trúc dữ liệu', 'data structure', '자료구조'],
  ['execution model', 'mô hình thực thi', 'execution model', '실행 모델'],
  ['module boundary', 'ranh giới mô-đun', 'module boundary', '모듈 경계'],
  ['mental models', 'mô hình tư duy', 'mental models', '사고 모델들'],
  ['source-level', 'tầng mã nguồn', 'source-level', '소스 수준'],
  ['object model', 'mô hình đối tượng', 'object model', '객체 모델'],
  ['type system', 'hệ kiểu', 'type system', '타입 시스템'],
  ['standard library', 'thư viện chuẩn', 'standard library', '표준 라이브러리'],
  ['class loading', 'nạp lớp', 'class loading', '클래스 로딩'],
  ['native instructions', 'lệnh máy bản địa', 'native instructions', '네이티브 명령어'],
  ['machine instruction', 'lệnh máy', 'machine instruction', '기계 명령어'],
  ['causal reasoning', 'lập luận nhân quả', 'causal reasoning', '인과적 추론'],
  ['namespace', 'không gian tên', 'namespace', '네임스페이스'],
  ['framework', 'khung phần mềm', 'framework', '프레임워크'],
  ['pipeline', 'chuỗi xử lý', 'pipeline', '파이프라인'],
  ['browser', 'trình duyệt', 'browser', '브라우저'],
  ['developer', 'nhà phát triển', 'developer', '개발자'],
  ['abstraction', 'lớp trừu tượng', 'abstraction', '추상화'],
  ['mechanism', 'cơ chế', 'mechanism', '메커니즘'],
  ['protocol', 'giao thức', 'protocol', '프로토콜'],
  ['compiler', 'trình biên dịch', 'compiler', '컴파일러'],
  ['interpreter', 'trình thông dịch', 'interpreter', '인터프리터'],
  ['syntax', 'cú pháp', 'syntax', '문법'],
  ['keyword', 'từ khóa', 'keyword', '키워드'],
  ['layer', 'tầng', 'layer', '계층'],
  ['primitive', 'thành phần nguyên thủy', 'primitive', '기본 요소'],
  ['canonical', 'chuẩn gốc', 'canonical', '정본'],
  ['entrypoint', 'điểm vào', 'entrypoint', '진입점'],
  ['track', 'nhánh học', 'track', '트랙'],
  ['standard', 'tiêu chuẩn', 'standard', '표준'],
  ['interaction', 'tương tác', 'interaction', '상호작용'],
  ['accessibility', 'khả năng tiếp cận', 'accessibility', '접근성'],
  ['invalidation', 'vô hiệu hóa', 'invalidation', '무효화'],
  ['pixel', 'điểm ảnh', 'pixel', '픽셀'],
  ['render', 'kết xuất', 'render', '렌더링'],
  ['component', 'thành phần', 'component', '컴포넌트'],
  ['stylesheet', 'biểu định kiểu', 'stylesheet', '스타일시트'],
  ['navigation', 'điều hướng', 'navigation', '내비게이션'],
  ['execution', 'thực thi', 'execution', '실행'],
  ['module', 'mô-đun', 'module', '모듈'],
  ['catalog', 'danh mục', 'catalog', '카탈로그'],
  ['debug', 'gỡ lỗi', 'debug', '디버그'],
  ['concurrency', 'tính đồng thời', 'concurrency', '동시성'],
  ['test', 'kiểm thử', 'test', '테스트'],
  ['cost', 'chi phí', 'cost', '비용'],
  ['code', 'mã', 'code', '코드'],
  ['path', 'đường dẫn', 'path', '경로'],
  ['local', 'cục bộ', 'local', '로컬'],
  ['input', 'đầu vào', 'input', '입력'],
  ['change', 'thay đổi', 'change', '변경'],
  ['build', 'bản dựng', 'build', '빌드'],
  ['project', 'dự án', 'project', '프로젝트'],
  ['server', 'máy chủ', 'server', '서버'],
  ['type', 'kiểu', 'type', '타입'],
  ['representation', 'biểu diễn', 'representation', '표현'],
  ['design', 'thiết kế', 'design', '설계'],
  ['learning', 'học tập', 'learning', '학습'],
  ['note', 'ghi chú', 'note', '노트'],
  ['class', 'lớp', 'class', '클래스'],
  ['node', 'nút', 'node', '노드'],
  ['search', 'tìm kiếm', 'search', '검색'],
  ['database', 'cơ sở dữ liệu', 'database', '데이터베이스'],
  ['problem', 'bài toán', 'problem', '문제'],
  ['work', 'công việc', 'work', '작업'],
  ['tree', 'cây', 'tree', '트리'],
  ['task', 'tác vụ', 'task', '작업'],
  ['library', 'thư viện', 'library', '라이브러리'],
  ['query', 'truy vấn', 'query', '쿼리'],
  ['feature', 'tính năng', 'feature', '기능'],
  ['language', 'ngôn ngữ', 'language', '언어'],
  ['migration', 'di chuyển', 'migration', '마이그레이션'],
  ['retry', 'thử lại', 'retry', '재시도'],
  ['lifecycle', 'vòng đời', 'lifecycle', '생명주기'],
  ['transaction', 'giao dịch', 'transaction', '트랜잭션'],
  ['index', 'chỉ mục', 'index', '인덱스'],
  ['rule', 'quy tắc', 'rule', '규칙'],
  ['uncertainty', 'bất định', 'uncertainty', '불확실성'],
  ['artifact', 'sản phẩm tạo ra', 'artifact', '산출물'],
  ['release', 'bản phát hành', 'release', '릴리스'],
  ['signal', 'tín hiệu', 'signal', '신호'],
  ['scale', 'quy mô', 'scale', '규모'],
  ['size', 'kích thước', 'size', '크기'],
  ['operation', 'thao tác', 'operation', '연산'],
  ['space', 'không gian', 'space', '공간'],
  ['metric', 'chỉ số', 'metric', '지표'],
  ['update', 'cập nhật', 'update', '업데이트'],
  ['target', 'mục tiêu', 'target', '대상'],
  ['ownership', 'quyền sở hữu', 'ownership', '소유권'],
  ['metadata', 'siêu dữ liệu', 'metadata', '메타데이터'],
  ['load', 'tải', 'load', '로드'],
  ['action', 'hành động', 'action', '동작'],
  ['scope', 'phạm vi', 'scope', '범위'],
  ['token', 'đơn vị từ', 'token', '토큰'],
  ['platform', 'nền tảng', 'platform', '플랫폼'],
  ['workload', 'tải công việc', 'workload', '워크로드'],
  ['energy', 'năng lượng', 'energy', '에너지'],
  ['access', 'truy cập', 'access', '접근'],
  ['recovery', 'khôi phục', 'recovery', '복구'],
  ['environment', 'môi trường', 'environment', '환경'],
  ['strategy', 'chiến lược', 'strategy', '전략'],
  ['client', 'máy khách', 'client', '클라이언트'],
  ['market', 'thị trường', 'market', '시장'],
  ['quality', 'chất lượng', 'quality', '품질'],
  ['reference', 'tham chiếu', 'reference', '참조'],
  ['base', 'cơ sở', 'base', '기반'],
  ['optimization', 'tối ưu hóa', 'optimization', '최적화'],
  ['native', 'bản địa', 'native', '네이티브'],
  ['consumer', 'bên tiêu thụ', 'consumer', '소비자'],
  ['outcome', 'kết quả', 'outcome', '결과'],
  ['sequence', 'chuỗi', 'sequence', '시퀀스'],
  ['training', 'huấn luyện', 'training', '학습'],
  ['probability', 'xác suất', 'probability', '확률'],
  ['theory', 'lý thuyết', 'theory', '이론'],
  ['analysis', 'phân tích', 'analysis', '분석'],
  ['time', 'thời gian', 'time', '시간'],
  ['logic', 'lô-gic', 'logic', '논리'],
  ['graph', 'đồ thị', 'graph', '그래프'],
  ['order', 'thứ tự', 'order', '순서'],
  ['distribution', 'phân phối', 'distribution', '분포'],
  ['global', 'toàn cục', 'global', '전역'],
  ['systems', 'các hệ thống', 'systems', '시스템들'],
  ['business', 'nghiệp vụ', 'business', '비즈니스'],
  ['senior', 'cấp cao', 'senior', '시니어'],
  ['core', 'cốt lõi', 'core', '핵심'],
  ['knowledge', 'kiến thức', 'knowledge', '지식'],
  ['compatibility', 'tính tương thích', 'compatibility', '호환성'],
  ['gradient', 'độ dốc', 'gradient', '기울기'],
  ['loss', 'mất mát', 'loss', '손실'],
  ['engineering', 'kỹ thuật', 'engineering', '엔지니어링'],
  ['text', 'văn bản', 'text', '텍스트'],
  ['causal', 'nhân quả', 'causal', '인과적'],
  ['common', 'dùng chung', 'common', '공통'],
  ['external', 'bên ngoài', 'external', '외부'],
  ['feedback', 'phản hồi', 'feedback', '피드백'],
  ['linear', 'tuyến tính', 'linear', '선형'],
  ['container', 'bộ chứa', 'container', '컨테이너'],
  ['level', 'mức', 'level', '수준'],
  ['team', 'nhóm', 'team', '팀'],
  ['vector', 'véc-tơ', 'vector', '벡터'],
  ['modern', 'hiện đại', 'modern', '현대적'],
  ['history', 'lịch sử', 'history', '이력'],
  ['point', 'điểm', 'point', '지점'],
  ['audit', 'kiểm tra', 'audit', '감사'],
  ['binary', 'nhị phân', 'binary', '이진'],
  ['commit', 'lần ghi nhận', 'commit', '커밋'],
  ['review', 'rà soát', 'review', '검토'],
  ['matrix', 'ma trận', 'matrix', '행렬'],
  ['capability', 'năng lực', 'capability', '역량'],
  ['heap', 'vùng nhớ động', 'heap', '힙'],
  ['chain', 'chuỗi', 'chain', '사슬'],
  ['shared', 'dùng chung', 'shared', '공유'],
  ['stack', 'ngăn xếp', 'stack', '스택'],
  ['models', 'các mô hình', 'models', '모델들'],
  ['dynamic', 'động', 'dynamic', '동적'],
  ['hash', 'băm', 'hash', '해시'],
  ['transition', 'chuyển tiếp', 'transition', '전이'],
  ['route', 'tuyến', 'route', '경로'],
  ['product', 'sản phẩm', 'product', '제품'],
  ['current', 'hiện tại', 'current', '현재'],
  ['public', 'công khai', 'public', '공개'],
  ['complexity', 'độ phức tạp', 'complexity', '복잡도'],
  ['depth', 'độ sâu', 'depth', '깊이'],
  ['unit', 'đơn vị', 'unit', '단위'],
  ['transport', 'vận chuyển', 'transport', '전송'],
  ['timeout', 'hết thời gian chờ', 'timeout', '타임아웃'],
  ['layout', 'bố cục', 'layout', '레이아웃'],
  ['assumptions', 'các giả định', 'assumptions', '가정들'],
  ['tool', 'công cụ', 'tool', '도구'],
  ['loop', 'vòng lặp', 'loop', '루프'],
  ['algorithm', 'thuật toán', 'algorithm', '알고리즘'],
  ['measurement', 'đo lường', 'measurement', '측정'],
  ['ordering', 'thứ tự', 'ordering', '순서'],
  ['support', 'hỗ trợ', 'support', '지원'],
  ['copy', 'bản sao', 'copy', '복사'],
  ['integration', 'tích hợp', 'integration', '통합'],
  ['budget', 'ngân sách', 'budget', '예산'],
  ['bias', 'độ lệch', 'bias', '편향'],
  ['explicit', 'tường minh', 'explicit', '명시적'],
  ['distributed', 'phân tán', 'distributed', '분산'],
  ['method', 'phương thức', 'method', '메서드'],
  ['semantic', 'ngữ nghĩa', 'semantic', '의미적'],
  ['bridge', 'cầu nối', 'bridge', '브리지'],
  ['objective', 'mục tiêu', 'objective', '목표'],
  ['incident', 'sự cố', 'incident', '인시던트'],
  ['rollback', 'quay lui', 'rollback', '롤백'],
  ['fail', 'thất bại', 'fail', '실패'],
  ['inference', 'suy luận', 'inference', '추론'],
  ['device', 'thiết bị', 'device', '장치'],
  ['safety', 'an toàn', 'safety', '안전'],
  ['geometry', 'hình học', 'geometry', '기하학'],
  ['social', 'xã hội', 'social', '사회적'],
  ['lifetime', 'thời gian tồn tại', 'lifetime', '수명'],
  ['condition', 'điều kiện', 'condition', '조건'],
  ['config', 'cấu hình', 'config', '설정'],
  ['window', 'cửa sổ', 'window', '윈도우'],
  ['mode', 'chế độ', 'mode', '모드'],
  ['agent', 'tác nhân', 'agent', '에이전트'],
  ['table', 'bảng', 'table', '테이블'],
  ['sample', 'mẫu', 'sample', '표본'],
  ['result', 'kết quả', 'result', '결과'],
  ['physical', 'vật lý', 'physical', '물리적'],
  ['join', 'phép nối', 'join', '조인'],
  ['constraints', 'các ràng buộc', 'constraints', '제약조건들'],
  ['correctness', 'tính đúng đắn', 'correctness', '정확성'],
  ['root', 'gốc', 'root', '루트'],
  ['range', 'phạm vi', 'range', '범위'],
  ['port', 'cổng', 'port', '포트'],
  ['entity', 'thực thể', 'entity', '엔터티'],
  ['block', 'khối', 'block', '블록'],
  ['relation', 'quan hệ', 'relation', '관계'],
  ['call', 'lời gọi', 'call', '호출'],
  ['lock', 'khóa', 'lock', '잠금'],
  ['package', 'gói', 'package', '패키지'],
  ['image', 'ảnh', 'image', '이미지'],
  ['infrastructure', 'hạ tầng', 'infrastructure', '인프라'],
  ['throughput', 'thông lượng', 'throughput', '처리량'],
  ['trace', 'dấu vết', 'trace', '추적'],
  ['list', 'danh sách', 'list', '목록'],
  ['requirement', 'yêu cầu', 'requirement', '요구사항'],
  ['exact', 'chính xác', 'exact', '정확한'],
  ['conflict', 'xung đột', 'conflict', '충돌'],
  ['mapping', 'ánh xạ', 'mapping', '매핑'],
  ['internal', 'nội bộ', 'internal', '내부'],
  ['write', 'ghi', 'write', '쓰기'],
  ['critical', 'trọng yếu', 'critical', '중요'],
  ['governance', 'quản trị', 'governance', '거버넌스'],
  ['first principles', 'nguyên lý nền tảng', 'first principles', '제일 원리'],
  ['mental model', 'mô hình tư duy', 'mental model', '사고 모델'],
  ['learning path', 'lộ trình học', 'learning path', '학습 경로'],
  ['request lifecycle', 'vòng đời yêu cầu', 'request lifecycle', '요청 생명주기'],
  ['runtime behavior', 'hành vi thời gian chạy', 'runtime behavior', '런타임 동작'],
  ['failure mode', 'dạng thất bại', 'failure mode', '실패 모드'],
  ['edge case', 'trường hợp biên', 'edge case', '경계 사례'],
  ['root cause', 'nguyên nhân gốc', 'root cause', '근본 원인'],
  ['trade-off', 'sự đánh đổi', 'trade-off', '트레이드오프'],
  ['state machine', 'máy trạng thái', 'state machine', '상태 머신'],
  ['source code', 'mã nguồn', 'source code', '소스 코드'],
  ['data model', 'mô hình dữ liệu', 'data model', '데이터 모델'],
  ['data flow', 'luồng dữ liệu', 'data flow', '데이터 흐름'],
  ['access control', 'kiểm soát truy cập', 'access control', '접근 제어'],
  ['quality gate', 'cổng chất lượng', 'quality gate', '품질 게이트'],
  ['build artifact', 'hiện vật bản dựng', 'build artifact', '빌드 산출물'],
  ['deployment', 'triển khai', 'deployment', '배포'],
  ['implementation', 'hiện thực', 'implementation', '구현'],
  ['configuration', 'cấu hình', 'configuration', '구성'],
  ['architecture', 'kiến trúc', 'architecture', '아키텍처'],
  ['interface', 'giao diện', 'interface', '인터페이스'],
  ['constraint', 'ràng buộc', 'constraint', '제약조건'],
  ['assumption', 'giả định', 'assumption', '가정'],
  ['invariant', 'bất biến', 'invariant', '불변식'],
  ['boundary', 'ranh giới', 'boundary', '경계'],
  ['dependency', 'phụ thuộc', 'dependency', '의존성'],
  ['model', 'mô hình', 'model', '모델'],
  ['state', 'trạng thái', 'state', '상태'],
  ['data', 'dữ liệu', 'data', '데이터'],
  ['system', 'hệ thống', 'system', '시스템'],
  ['memory', 'bộ nhớ', 'memory', '메모리'],
  ['network', 'mạng', 'network', '네트워크'],
  ['storage', 'lưu trữ', 'storage', '저장소'],
  ['cache', 'bộ nhớ đệm', 'cache', '캐시'],
  ['queue', 'hàng đợi', 'queue', '큐'],
  ['thread', 'luồng thực thi', 'thread', '스레드'],
  ['process', 'tiến trình', 'process', '프로세스'],
  ['schema', 'lược đồ', 'schema', '스키마'],
  ['record', 'bản ghi', 'record', '레코드'],
  ['field', 'trường dữ liệu', 'field', '필드'],
  ['property', 'thuộc tính', 'property', '속성'],
  ['object', 'đối tượng', 'object', '객체'],
  ['function', 'hàm', 'function', '함수'],
  ['event', 'sự kiện', 'event', '이벤트'],
  ['request', 'yêu cầu', 'request', '요청'],
  ['response', 'phản hồi', 'response', '응답'],
  ['error', 'lỗi', 'error', '오류'],
  ['failure', 'thất bại', 'failure', '실패'],
  ['behavior', 'hành vi', 'behavior', '동작'],
  ['evidence', 'bằng chứng', 'evidence', '증거'],
  ['context', 'ngữ cảnh', 'context', '맥락'],
  ['policy', 'chính sách', 'policy', '정책'],
  ['production', 'môi trường vận hành', 'production', '운영 환경'],
  ['source', 'nguồn', 'source', '소스'],
  ['semantics', 'ngữ nghĩa', 'semantics', '의미론'],
  ['contract', 'đặc tả hợp đồng', 'contract', '계약'],
  ['runtime', 'thời gian chạy', 'runtime', '런타임'],
  ['resource', 'tài nguyên', 'resource', '자원'],
  ['version', 'phiên bản', 'version', '버전'],
  ['connection', 'liên kết', 'connection', '연결'],
  ['owner', 'đơn vị sở hữu', 'owner', '오너'],
  ['structure', 'cấu trúc', 'structure', '구조'],
  ['case', 'trường hợp', 'case', '사례'],
  ['control', 'điều khiển', 'control', '제어'],
  ['file', 'tệp', 'file', '파일'],
  ['pattern', 'mẫu', 'pattern', '패턴'],
  ['effect', 'tác động', 'effect', '효과'],
  ['identity', 'định danh', 'identity', '식별자'],
  ['security', 'bảo mật', 'security', '보안'],
  ['information', 'thông tin', 'information', '정보'],
  ['flow', 'luồng', 'flow', '흐름'],
  ['latency', 'độ trễ', 'latency', '지연 시간'],
  ['reasoning', 'lập luận', 'reasoning', '추론'],
  ['capacity', 'sức chứa', 'capacity', '용량'],
  ['decision', 'quyết định', 'decision', '결정'],
  ['service', 'dịch vụ', 'service', '서비스'],
  ['output', 'đầu ra', 'output', '출력'],
  ['user', 'người dùng', 'user', '사용자'],
  ['domain', 'lĩnh vực', 'domain', '도메인'],
  ['application', 'ứng dụng', 'application', '애플리케이션'],
  ['performance', 'hiệu năng', 'performance', '성능'],
  ['reliability', 'độ tin cậy', 'reliability', '신뢰성'],
  ['observability', 'khả năng quan sát', 'observability', '관측 가능성'],
  ['validation', 'kiểm tra hợp lệ', 'validation', '검증'],
  ['verification', 'xác minh', 'verification', '확인'],
  ['risk', 'rủi ro', 'risk', '위험'],
  ['value', 'giá trị', 'value', '값'],
  ['rate', 'tỷ lệ', 'rate', '비율']
].map(([term, vi, en, ko]) => ({ term, vi, en, ko }));

const LEGACY_MARKERS = new Map([
  ['các mô hình tư duy (mental models / 사고 모델들)', 'mô hình tư duy (mental models / 사고 모델들)'],
  ['ý nghĩa ngữ nghĩa (semantic meaning / 의미적 의미)', 'ý nghĩa (semantic meaning / 의미적 뜻)'],
  ['logic nghiệp vụ (business logic / 비즈니스 로직)', 'lô-gic nghiệp vụ (business logic / 비즈니스 로직)'],
  ['lô-gic (logic / 논리) nghiệp vụ (business logic / 비즈니스 로직)', 'lô-gic nghiệp vụ (business logic / 비즈니스 로직)'],
  ['bộ nhớ heap (heap memory / 힙 메모리)', 'bộ nhớ vùng động (heap memory / 힙 메모리)'],
  ['vùng nhớ heap (heap / 힙)', 'vùng nhớ động (heap / 힙)']
]);

function termPattern(term) {
  return term
    .split(/\s+/)
    .map(part => part.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'))
    .join('\\s+');
}

function isExcluded(relative) {
  const parts = relative.replaceAll('\\', '/').split('/');
  return (!forceStructural && STRUCTURAL_FILES.has(relative)) || EXCLUDED_TOP.has(parts[0]) || parts.some(part => EXCLUDED_SEGMENTS.has(part.toLowerCase()));
}

async function walk(directory, result = []) {
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    const absolute = path.join(directory, entry.name);
    const relative = path.relative(ROOT, absolute).replaceAll('\\', '/');
    if (entry.isDirectory() && (EXCLUDED_SEGMENTS.has(entry.name.toLowerCase()) || EXCLUDED_TOP.has(relative.split('/')[0]))) continue;
    if (entry.isDirectory()) await walk(absolute, result);
    else if (entry.isFile() && entry.name.endsWith('.md') && !isExcluded(relative)) result.push(relative);
  }
  return result;
}

function maskProtected(text) {
  const protectedValues = [];
  const protect = value => {
    const index = protectedValues.push(value) - 1;
    return `\u0000${index}\u0000`;
  };
  let masked = text.replace(/```[\s\S]*?```|`[^`]*`|!?(?:\[[^\]]*\]\([^)]*\))/g, protect);
  masked = masked.replace(/Source canonical|Quality gates/g, protect);
  return { masked, protectedValues };
}

function restoreProtected(text, protectedValues) {
  return text.replace(/\u0000(\d+)\u0000/g, (_, index) => protectedValues[Number(index)]);
}

function hasExistingGloss(text, index, term) {
  const after = text.slice(index + term.length).match(/^\s*(\([^)]{0,180}\))/);
  if (!after) return false;
  const inside = after[1];
  // Existing glosses may use Vietnamese + Korean without repeating English.
  return inside.includes('/') || /[가-힣]/.test(inside);
}

function isInsideParenthetical(text, index) {
  const start = text.lastIndexOf('(', index);
  const end = text.indexOf(')', index);
  const previousEnd = text.lastIndexOf(')', index);
  return start >= 0 && start > previousEnd && end >= index && end - start <= 180;
}

function documentCandidates(markdown) {
  const { masked } = maskProtected(markdown);
  return new Set(TERMS.filter(entry => {
    const escaped = termPattern(entry.term);
    return new RegExp(`(?<![A-Za-z0-9_-])${escaped}(?![A-Za-z0-9_-])`, 'i').test(masked);
  }).map(entry => entry.term));
}

function transformLine(line, allowedTerms) {
  const { masked, protectedValues } = maskProtected(line);
  const entries = TERMS
    .filter(entry => allowedTerms.has(entry.term))
    .sort((a, b) => b.term.length - a.term.length);
  if (!entries.length) return line;
  let normalized = masked;
  for (const [legacy, current] of LEGACY_MARKERS) normalized = normalized.replaceAll(legacy, current);
  for (const entry of entries) {
    const escaped = termPattern(entry.term);
    const escapedVi = termPattern(entry.vi);
    const vietnameseFirst = new RegExp(`${escapedVi}\\s*\\(\\s*${escaped}\\s*\\)`, 'gi');
    normalized = normalized.replace(vietnameseFirst, `${entry.vi} (${entry.en} / ${entry.ko})`);
    const englishFirst = new RegExp(`(?<![A-Za-z0-9_-])${escaped}(?![A-Za-z0-9_-])\\s*(\\([^)]{0,180}(?:${escapedVi}|/|[가-힣])[^)]*\\))`, 'gi');
    normalized = normalized.replace(englishFirst, `${entry.vi} (${entry.en} / ${entry.ko})`);
  }
  const lookup = new Map(entries.map(entry => [entry.term.toLowerCase(), entry]));
  const alternatives = entries.map(entry => termPattern(entry.term));
  const regex = new RegExp(`(?<![A-Za-z0-9_-])(?:${alternatives.join('|')})(?![A-Za-z0-9_-])`, 'gi');
  const text = normalized.replace(regex, (matched, offset) => {
    const entry = lookup.get(matched.toLowerCase().replace(/\s+/g, ' '));
    if (!entry || isInsideParenthetical(normalized, offset) || hasExistingGloss(normalized, offset, entry.term)) return matched;
    let vietnamese = entry.vi;
    // Avoid awkward duplication in phrases such as "môi trường production".
    if (entry.term === 'production' && /môi trường\s*$/i.test(normalized.slice(0, offset))) {
      vietnamese = 'vận hành';
    }
    const before = normalized.slice(0, offset);
    const linePrefix = before.slice(before.lastIndexOf('\n') + 1);
    const beginsHeading = /^\s*#{1,6}\s+(?:[*_]{0,2})?$/.test(linePrefix);
    const beginsParagraph = /(?:^|\n\s*\n)\s*$/.test(before);
    if (matched.charAt(0) === matched.charAt(0).toUpperCase() && matched.charAt(0) !== matched.charAt(0).toLowerCase() || beginsHeading || beginsParagraph) {
      vietnamese = vietnamese.charAt(0).toUpperCase() + vietnamese.slice(1);
    }
    return `${vietnamese} (${entry.en} / ${entry.ko})`;
  });
  return restoreProtected(text, protectedValues);
}

function reverseLine(line) {
  const { masked, protectedValues } = maskProtected(line);
  let text = masked;
  const entries = [...TERMS].sort((a, b) => b.vi.length - a.vi.length);
  for (const entry of entries) {
    const marker = `${entry.vi} (${entry.en} / ${entry.ko})`;
    const capitalized = marker.charAt(0).toUpperCase() + marker.slice(1);
    const capitalizedEnglish = entry.en.charAt(0).toUpperCase() + entry.en.slice(1);
    text = text.replaceAll(marker, entry.en).replaceAll(capitalized, capitalizedEnglish);
  }
  return restoreProtected(text, protectedValues);
}

const writeMode = process.argv.includes('--write');
const includeOutput = process.argv.includes('--include-output');
const reverseMode = process.argv.includes('--reverse');
const only = process.argv.find(argument => argument.startsWith('--only='))?.slice('--only='.length);
const preview = process.argv.includes('--preview');
const files = await walk(ROOT);
let changed = 0;
let replacements = 0;
for (const relative of files.sort()) {
  if (!includeOutput && relative.split('/').includes('output')) continue;
  if (only && !relative.includes(only)) continue;
  const original = await readFile(path.join(ROOT, relative), 'utf8');
  const allowedTerms = documentCandidates(original);
  const transformed = reverseMode ? reverseLine(original) : transformLine(original, allowedTerms);
  if (transformed === original) continue;
  changed += 1;
  replacements += [...transformed.matchAll(/\([^)]*\/[^)]*[가-힣][^)]*\)/g)].length;
  if (writeMode) await writeFile(path.join(ROOT, relative), transformed, 'utf8');
  else if (preview) console.log(`\n--- ${relative} ---\n${transformed.slice(0, 3000)}`);
  else console.log(relative);
}
console.log(`${writeMode ? 'Updated' : 'Would update'} ${changed} file(s), with ${replacements} bilingual gloss markers.`);
