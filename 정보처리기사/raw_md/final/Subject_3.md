# 3과목 데이터베이스 구축

## 101. 개념적 설계 (Conceptual Design)
- 정보의 구조를 얻기 위하여 현실 세계에 대한 인식을 추상적 개념으로 표현하는 과정이다.
- 개념 스키마 모델링과 트랜잭션 모델링을 병행 수행한다.
- **Vietnamese:** Thiết kế khái niệm. Quá trình biểu diễn nhận thức về thế giới thực thành các khái niệm trừu tượng để có được cấu trúc thông tin. Thực hiện song song mô hình hóa lược đồ khái niệm và mô hình hóa giao dịch.
- **Example (Korean/Vietnamese):** 현실 세계의 '학생'과 '수업'을 E-R 다이어그램으로 그리는 것. / Vẽ sơ đồ E-R cho 'học sinh' và 'lớp học' trong thế giới thực.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Khái-Trừu (Khái niệm = Trừu tượng).

## 102. 논리적 설계 (Logical Design / Data Modeling)
- 자료를 특정 DBMS가 지원하는 논리적 자료 구조로 변환(mapping)시키는 과정이다.
- **Vietnamese:** Thiết kế logic (Mô hình hóa dữ liệu). Quá trình chuyển đổi (ánh xạ) dữ liệu thành cấu trúc dữ liệu logic được hỗ trợ bởi một DBMS cụ thể.
- **Example (Korean/Vietnamese):** E-R 다이어그램을 관계형 데이터베이스의 테이블 구조로 변환하는 것. / Chuyển đổi sơ đồ E-R thành cấu trúc bảng của cơ sở dữ liệu quan hệ.
- 💡 **Mẹo ghi nhớ:** Logic-Bảng (Thiết kế Logic = Chuyển đổi sang Bảng).

## 103. 물리적 설계 (Physical Design)
- 논리적 구조로 표현된 데이터를 물리적 구조의 데이터로 변환하는 과정이다.
- 데이터베이스 파일의 저장 구조 및 액세스 경로를 결정한다.
- **Vietnamese:** Thiết kế vật lý. Quá trình chuyển đổi dữ liệu cấu trúc logic thành cấu trúc vật lý (lưu trữ ổ đĩa, đường dẫn truy cập).
- **Example (Korean/Vietnamese):** 테이블에 인덱스를 생성하여 검색 속도를 높이는 것. / Tạo chỉ mục (index) trên bảng để tăng tốc độ tìm kiếm.
- 💡 **Mẹo ghi nhớ:** Vật-Lưu (Thiết kế Vật lý = Cấu trúc Lưu trữ).

## 104. 데이터 모델에 표시할 요소 (Elements of Data Model)
- **구조 (Structure):** 논리적으로 표현된 개체 타입들 간의 관계로 데이터 구조 및 정적 성질.
- **연산 (Operation):** 실제 데이터를 처리하는 작업 명세.
- **제약 조건 (Constraint):** 실제 데이터의 논리적인 제약 조건.
- **Vietnamese:** Các yếu tố trong mô hình dữ liệu.
  - Cấu trúc: Mối quan hệ giữa các kiểu thực thể (tĩnh).
  - Phép toán: Đặc tả công việc xử lý dữ liệu (động).
  - Ràng buộc: Điều kiện giới hạn logic của dữ liệu.
- **Example (Korean/Vietnamese):** 구조: 학생 테이블, 연산: 정보 검색, 제약조건: 나이는 0 이상. / Cấu trúc: Bảng sinh viên, Phép toán: Tìm kiếm, Ràng buộc: Tuổi >= 0.
- 💡 **Mẹo ghi nhớ:** Cấu-Toán-Buộc (Cấu trúc, Toán tử, Ràng buộc).

## 105. E-R 다이어그램 (E-R Diagram)
- 사각형 (Rectangle): 개체 (Entity)
- 마름모 (Diamond): 관계 (Relationship)
- 타원 (Oval): 속성 (Attribute)
- 이중 타원 (Double Oval): 다중값 속성 (Multivalued Attribute)
- 선 (Line): 연결 (Link)
- **Vietnamese:** Sơ đồ E-R. Hình chữ nhật (Thực thể), Hình thoi (Mối quan hệ), Hình bầu dục (Thuộc tính), Hình bầu dục kép (Thuộc tính đa trị).
- **Example:** 고객(사각형)이 상품(사각형)을 구매(마름모)한다. / Khách hàng (HCN) mua (Hình thoi) sản phẩm (HCN).

## 106-107. 튜플(Tuple)과 속성(Attribute)
- **튜플 (Tuple):** 릴레이션을 구성하는 행(Row). 튜플의 수 = 카디널리티 (Cardinality).
- **속성 (Attribute):** 데이터베이스를 구성하는 가장 작은 논리적 단위. 열(Column). 속성의 수 = 디그리 (Degree).
- **Vietnamese:** Tuple (Hàng) và Attribute (Cột).
  - Tuple: Hàng. Số hàng = Cardinality.
  - Attribute: Cột, đơn vị logic nhỏ nhất. Số cột = Degree.
- **Example:** 학생 테이블의 '홍길동' 데이터 한 줄이 튜플, '이름', '학번' 열이 속성. / Một dòng dữ liệu 'Hong Gil-dong' là Tuple, các cột 'Tên', 'Mã SV' là Attribute.
- 💡 **Mẹo ghi nhớ:** Tu-Car (Tuple = Cardinality), At-De (Attribute = Degree).

## 108. 도메인 (Domain)
- 하나의 애트리뷰트가 취할 수 있는 같은 타입의 원자(Atomic) 값들의 집합.
- **Vietnamese:** Miền giá trị. Tập hợp các giá trị nguyên tử (không thể chia nhỏ) cùng kiểu mà một thuộc tính có thể nhận.
- **Example:** '성별' 속성의 도메인은 {남, 여}. / Miền giá trị của thuộc tính 'Giới tính' là {Nam, Nữ}.

## 110-114. 키 (Keys)
- **후보키 (Candidate Key):** 튜플을 유일하게 식별하는 속성. 유일성과 최소성 만족.
- **기본키 (Primary Key):** 후보키 중 선정된 주키. 중복과 NULL 불가.
- **대체키 (Alternate Key):** 후보키 중 기본키를 제외한 나머지 (보조키).
- **슈퍼키 (Super Key):** 유일성은 만족하지만 최소성은 만족하지 못하는 속성 집합.
- **외래키 (Foreign Key):** 다른 릴레이션의 기본키를 참조하는 속성.
- **Vietnamese:** Các loại khóa (Keys).
  - Candidate Key (Khóa ứng viên): Định danh duy nhất, thỏa mãn tính duy nhất và tính tối thiểu.
  - Primary Key (Khóa chính): Chọn từ khóa ứng viên, không trùng lặp, không NULL.
  - Alternate Key (Khóa thay thế): Các khóa ứng viên còn lại.
  - Super Key (Siêu khóa): Thỏa mãn tính duy nhất nhưng không tối thiểu.
  - Foreign Key (Khóa ngoại): Thuộc tính tham chiếu đến khóa chính của bảng khác.

## 115. 무결성 (Integrity)
- **개체 무결성 (Entity Integrity):** 기본키는 NULL값이나 중복값을 가질 수 없다.
- **참조 무결성 (Referential Integrity):** 외래키 값은 NULL이거나 참조 릴레이션의 기본키 값과 동일해야 한다.
- **Vietnamese:** Tính toàn vẹn.
  - Toàn vẹn thực thể: Khóa chính không NULL và không trùng.
  - Toàn vẹn tham chiếu: Khóa ngoại phải là NULL hoặc khớp với khóa chính được tham chiếu.

## 116-121. 관계대수 (Relational Algebra)
- 절차적인 언어 (Procedural Language). 질의에 대한 해를 구하기 위한 연산 순서 명시.
- **Select (σ):** 조건에 맞는 튜플 부분집합 추출 (행 추출).
- **Project (π):** 속성 리스트에 제시된 속성값 추출 (열 추출).
- **Join (⋈):** 두 릴레이션을 하나로 합침.
- **Division (÷):** 속성값을 모두 가진 튜플 추출.
- **교차곱 (Cartesian Product):** 두 릴레이션 튜플들의 모든 순서쌍. 카디널리티의 곱.
- **Vietnamese:** Đại số quan hệ (Ngôn ngữ thủ tục).
  - Select (σ): Lọc hàng (hàng).
  - Project (π): Chọn cột (cột).
  - Join (⋈): Kết nối 2 bảng.
  - Division (÷): Chia quan hệ.

## 123-125. 정규화 (Normalization)
- 데이터 중복을 배제하여 이상(Anomaly: 삽입, 삭제, 갱신 이상) 발생을 방지하는 과정. 논리적 설계 단계에서 수행.
- **1NF:** 도메인이 원자값 (Domain is Atomic).
- **2NF:** 부분적 함수 종속 제거 (Remove Partial Dependency).
- **3NF:** 이행적 함수 종속 제거 (Remove Transitive Dependency).
- **BCNF:** 결정자이면서 후보키가 아닌 것 제거.
- **4NF:** 다치 종속 제거 (Remove Multivalued Dependency).
- **5NF:** 조인 종속성 이용.
- **Vietnamese:** Chuẩn hóa. Giảm thiểu dư thừa dữ liệu để ngăn ngừa dị thường (Anomaly).
- 💡 **Mẹo ghi nhớ:** Nguyên-Phần-Bắc-Quyết-Đa-Chung (Nguyên tử -> Từng phần -> Bắc cầu -> Quyết định -> Đa trị -> Chung).

## 130-132. 트랜잭션 (Transaction)
- 데이터베이스 상태를 변환시키는 논리적 작업의 단위.
- **ACID 특성:**
  - **Atomicity (원자성):** 모두 반영되거나(Commit) 전혀 반영되지 않아야 함(Rollback).
  - **Consistency (일관성):** 성공 시 일관성 있는 상태 유지.
  - **Isolation (독립성/격리성):** 다른 트랜잭션의 연산이 끼어들 수 없음.
  - **Durability (영속성):** 성공한 결과는 시스템 고장에도 영구 반영.
- **Vietnamese:** Giao dịch (Transaction) & Tính chất ACID.
  - Atomicity (Tính nguyên tử): Tất cả hoặc không có gì.
  - Consistency (Tính nhất quán): Giữ trạng thái nhất quán.
  - Isolation (Tính độc lập): Không bị can thiệp bởi giao dịch khác.
  - Durability (Tính bền vững): Lưu trữ vĩnh viễn dù có lỗi hệ thống.

## 136-137. 분산 데이터베이스 (Distributed DB)
- 논리적으로는 하나이나 물리적으로 분산된 데이터베이스.
- **목표 (Goals):** 위치 투명성 (Location), 중복 투명성 (Replication), 병행 투명성 (Concurrency), 장애 투명성 (Failure).
- **Vietnamese:** Cơ sở dữ liệu phân tán. Tính trong suốt về: Vị trí, Nhân bản, Đồng thời, Lỗi.

## 143-145. SQL 분류 (SQL Categories)
- **DDL (데이터 정의어):** CREATE, ALTER, DROP (스키마, 테이블 등 정의/변경/삭제).
- **DML (데이터 조작어):** SELECT, INSERT, DELETE, UPDATE (데이터 조회 및 변경).
- **DCL (데이터 제어어):** COMMIT, ROLLBACK, GRANT, REVOKE (보안, 무결성, 권한 제어).
- **Vietnamese:** Phân loại SQL.
  - DDL (Định nghĩa dữ liệu): CREATE, ALTER, DROP.
  - DML (Thao tác dữ liệu): SELECT, INSERT, DELETE, UPDATE.
  - DCL (Điều khiển dữ liệu): COMMIT, ROLLBACK, GRANT, REVOKE.

## 150-155. 데이터 조작어 (DML) 확장 및 조건 연산자
- **DELETE (150):** 튜플을 삭제. `DELETE FROM 테이블명 [WHERE 조건];`
- **UPDATE (151):** 튜플 내용 변경. `UPDATE 테이블명 SET 속성명 = 데이터 [WHERE 조건];`
- **SELECT (152, 153):** 데이터 검색. `SELECT [DISTINCT] 속성명 FROM 테이블명 [WHERE] [GROUP BY] [HAVING] [ORDER BY ASC|DESC];`
- **LIKE (154):** 문자 패턴 일치 검색. 
  - `%`: 모든 문자
  - `_`: 문자 하나
  - `#`: 숫자 하나
- **BETWEEN (155):** 두 숫자 사이의 값 검색.
- **Vietnamese:** Mở rộng DML và toán tử điều kiện.
  - DELETE: Xóa dữ liệu (hàng).
  - UPDATE: Cập nhật dữ liệu.
  - SELECT: Truy vấn dữ liệu (DISTINCT: Loại bỏ trùng lặp).
  - LIKE: Tìm kiếm theo mẫu ký tự. `%` đại diện cho chuỗi, `_` đại diện 1 ký tự, `#` đại diện 1 số.
  - BETWEEN: Trong khoảng giá trị.
- **Example:** `SELECT * FROM 학생 WHERE 이름 LIKE '김%';` / Tìm tất cả sinh viên có tên bắt đầu bằng họ 'Kim' (김).

## 163-167. 데이터베이스 설계 순서 (Database Design Process)
- **요구 조건 분석 (Requirements Analysis):** 요구 조건 명세서 작성.
- **개념적 설계 (Conceptual Design - 164):** 개념 스키마, E-R 모델, DBMS 독립적.
- **논리적 설계 (Logical Design - 165):** 논리 스키마 설계, 매핑.
- **물리적 설계 (Physical Design - 166):** 물리적 구조 변환, 접근 경로, 저장 레코드 양식 결정.
- **구현 (Implementation):** DDL로 DB 생성.
- **Vietnamese:** Quy trình thiết kế CSDL.
  - Phân tích yêu cầu -> Thiết kế Khái niệm (E-R) -> Thiết kế Logic (Bảng/Lược đồ logic) -> Thiết kế Vật lý (Lưu trữ) -> Triển khai (Code DDL).
- 💡 **Mẹo ghi nhớ:** Yêu-Khái-Lo-Vật-Cài (Yêu cầu -> Khái niệm -> Logic -> Vật lý -> Cài đặt).

## 168-172. 관계형 데이터 모델 및 E-R 모델 심화 (Relational & E-R Model Deep Dive)
- **E-R 모델 (168-169):** 피터 첸 제안. 기본키 속성은 '밑줄 타원(Underlined Oval)', 복합 속성은 '복수 타원(Multiple Ovals)'. 1:1, 1:N, N:M 표현.
- **관계형 데이터 모델 (170):** 2차원 표(Table) 형태.
- **릴레이션 특징 (172):**
  - 똑같은 튜플 포함 불가 (튜플의 유일성).
  - 튜플 사이, 속성 사이 순서 없음.
  - 속성 이름은 유일, 속성 값은 중복 가능.
  - 원자값(Atomic)만 허용.
- **Vietnamese:** Mô hình E-R và Mô hình quan hệ.
  - E-R: Thuộc tính khóa chính có gạch chân, thuộc tính phức hợp có nhiều vòng bầu dục.
  - Đặc điểm quan hệ (Bảng): Hàng không trùng lặp (duy nhất), không quan trọng thứ tự hàng/cột, chỉ chứa giá trị nguyên tử.

## 173-177. 키와 무결성, 관계대수 요약 (Keys, Integrity, Relational Algebra)
*Note: Includes duplicated points consolidated.*
- **도메인 무결성 (Domain Integrity):** 속성 값이 정의된 도메인에 속해야 함.
- **사용자 정의 무결성 (User-Defined Integrity):** 사용자가 정의한 제약 조건 만족.
- **순수 관계 연산자 (Pure Relational Operators):**
  - Select (σ): 수평 연산 (Horizontal) - 튜플 구함.
  - Project (π): 수직 연산 (Vertical) - 속성 구함.
  - Join (⋈) / Division (÷).
- **일반 집합 연산자 (Set Operators):** UNION (합집합), INTERSECTION (교집합), DIFFERENCE (차집합), CARTESIAN PRODUCT (교차곱).
- **Vietnamese:** Các ràng buộc và Đại số quan hệ (nhắc lại).
  - Toàn vẹn miền (Domain): Giá trị phải nằm trong miền cho phép.
  - Select: Phép toán ngang (lọc hàng).
  - Project: Phép toán dọc (lọc cột).
  - Phép toán tập hợp: Hợp, Giao, Hiệu, Tích Đề-các.

## 178. 관계해석 (Relational Calculus)
- E.F. Codd가 제안, 비절차적(원하는 정보가 무엇인지만 정의) 특성.
- 튜플 관계해석과 도메인 관계해석으로 나뉨. 관계대수와 능력 동등.
- **Vietnamese:** Giải tích quan hệ (Relational Calculus).
  - Do E.F. Codd đề xuất. Tính phi thủ tục (chỉ cần biết 'là gì' thay vì 'làm thế nào').
  - Có sức mạnh tính toán tương đương đại số quan hệ.

## 179-182. 정규화와 이상 심화 (Normalization & Anomaly - Deep Dive)
- **정규화 목적 (180):** 데이터 중복 배제, 무결성 유지, 이상 발생 방지. 논리적 설계 단계 수행.
- **이상 (Anomaly - 181):**
  - 삽입 이상 (Insertion Anomaly): 원하지 않는 값까지 삽입해야 하는 현상.
  - 삭제 이상 (Deletion Anomaly): 의도치 않은 연쇄 삭제(Cascade).
  - 갱신 이상 (Update Anomaly): 일부만 갱신되어 정보 모순 발생.
- **정규화 단계 암기 요령 (182):** 두부이결다조 (도메인 원자값, 부분 함수 종속 제거, 이행적 함수 종속 제거, 결정자이면서 후보키 아닌 것 제거, 다치 종속 제거, 조인 종속).
- **Vietnamese:** Chuẩn hóa và Dị thường dữ liệu (Sâu hơn).
  - Dị thường: Thêm (phải thêm dữ liệu không cần thiết), Xóa (bị mất dữ liệu liên quan), Sửa (cập nhật không đồng bộ gây mâu thuẫn).
  - Quy tắc ghi nhớ các chuẩn: Do-Bu-I-Gyeol-Da-Jo (Nguyên tử - Phần - Bắc cầu - Định thức - Đa trị - Kết nối).
- **Example:** 학번만 지우려다 이름과 학과 정보까지 다 지워지는 것이 '삭제 이상'. / Định xóa mã SV nhưng vô tình xóa luôn tên và khoa là 'Dị thường xóa'.

## 183. 함수적 종속과 이행적 종속 (Functional & Transitive Dependency)
- **함수적 종속 (Functional Dependency):** X -> Y (X가 결정되면 Y가 결정됨).
- **이행적 종속 (Transitive Dependency):** A -> B, B -> C 일 때 A -> C 인 관계.
- **Vietnamese:** Phụ thuộc hàm và Phụ thuộc bắc cầu.

## 184-185. 반정규화 (Denormalization)
- 시스템 성능 향상을 위해 정규화 원칙을 의도적으로 위배 (통합, 중복, 분리).
- **방법:** 테이블 통합, 테이블 분할 (수평/수직 분할), 중복 테이블/속성 추가.
- **Vietnamese:** Phi chuẩn hóa.
  - Cố tình phá vỡ quy tắc chuẩn hóa để tăng hiệu suất truy vấn.
  - Phương pháp: Gộp bảng, Chia bảng (ngang/dọc), Thêm cột/bảng dư thừa.
- **Example:** 조인(Join)을 피하기 위해 부서 테이블의 '부서명'을 사원 테이블에 중복 저장. / Thêm cột 'Tên phòng' vào bảng 'Nhân viên' để tránh phải Join.

## 186. 시스템 카탈로그 (System Catalog)
- DBMS의 객체(테이블, 뷰 등) 정보를 포함하는 시스템 데이터베이스. (데이터 사전, 메타 데이터)
- 사용자가 조회는 가능하나 직접 갱신(INSERT/UPDATE/DELETE)은 불가 (시스템 자동 갱신).
- **Vietnamese:** Danh mục hệ thống (System Catalog / Data Dictionary).
  - Chứa thông tin (metadata) về các đối tượng trong DB.
  - Người dùng có thể xem (SELECT) nhưng KHÔNG thể sửa đổi trực tiếp.

## 187-189. 트랜잭션의 상태와 특성 (Transaction State & ACID)
- **상태 (188):** 활동(Active) -> [부분 완료(Partially Committed) -> 완료(Committed)] 또는 [실패(Failed) -> 철회(Aborted/Rollback)].
- **특성 (189):** 원자성(Atomicity - 전부 또는 전무), 일관성(Consistency), 독립성(Isolation - 병행 중 간섭 불가), 영속성(Durability).
- **Vietnamese:** Trạng thái và tính chất giao dịch.
  - Trạng thái: Đang chạy -> Hoàn thành một phần -> Commit HOẶC Lỗi -> Rollback.

## 190. CRUD 분석
- Create, Read, Update, Delete 연산의 매트릭스 분석으로 데이터 양 유추.
- **Vietnamese:** Phân tích ma trận CRUD (Tạo, Đọc, Sửa, Xóa).

## 191-192. 인덱스 (Index)
- 데이터 접근을 빠르게 하기 위한 <키 값, 포인터> 구조. DDL로 제어. 트리 기반(B+ 트리), 비트맵, 함수 기반, 도메인 인덱스 등.
- **Vietnamese:** Chỉ mục (Index). Cấu trúc <Khóa, Con trỏ> giúp truy cập nhanh. Sử dụng B+ Tree, Bitmap...

## 193. 뷰 (View)
- 기본 테이블로부터 유도된 가상 테이블 (물리적 구현 X). 
- 장점: 논리적 데이터 독립성, 보안 강화. 단점: 인덱스 불가, 뷰 정의 변경 불가, 갱신 제약.
- **Vietnamese:** Khung nhìn (View). Bảng ảo. Ưu điểm: Độc lập dữ liệu, bảo mật. Nhược điểm: Không có index độc lập, khó cập nhật.

## 194. 파티션 (Partition)
- 대용량 테이블/인덱스를 작은 논리적 단위로 분할.
- 종류: 범위(Range - 예: 월별), 해시(Hash), 조합(Composite), 목록(List), 라운드 로빈(Round Robin).
- **Vietnamese:** Phân vùng dữ liệu (Partition). Chia bảng lớn thành phần nhỏ: theo Khoảng (Range), Băm (Hash), Danh sách (List)...

## 195-196. 분산 데이터베이스 목표 (Distributed DB Goals)
- 위치 투명성(Location), 중복 투명성(Replication), 병행 투명성(Concurrency), 장애 투명성(Failure).
- **Vietnamese:** Mục tiêu CSDL phân tán (Tính trong suốt về: vị trí, nhân bản, đồng thời, sự cố).

## 197. 분산 데이터베이스의 장단점 (Distributed DB Pros/Cons)
- **장점:** 지역 자치성, 자료 공유성 향상, 시스템 성능 및 신뢰성/가용성 향상.
- **단점:** 설계 및 소프트웨어 개발 어려움, 처리 비용 및 잠재적 오류 증가.
- **Vietnamese:** Ưu nhược điểm của CSDL phân tán.
  - Ưu điểm: Độc lập cục bộ, tăng chia sẻ, tin cậy cao, dễ mở rộng.
  - Nhược điểm: Phức tạp, khó thiết kế, tăng chi phí và lỗi tiềm ẩn.

## 198. 암호화 심화 (Encryption Deep Dive)
- **개인키(비밀키) 암호 방식 (Private/Symmetric Key):** 암호화와 복호화 키가 동일. 단일키, 대칭 암호. (예: DES)
- **공개키 암호 방식 (Public/Asymmetric Key):** 암호화 키는 공개(Public), 복호화 키는 비밀(Secret). 비대칭 암호. (예: RSA)
- **Vietnamese:** Mã hóa dữ liệu.
  - Khóa cá nhân (Đối xứng): Khóa mã hóa và giải mã giống nhau (DES).
  - Khóa công khai (Bất đối xứng): Khóa mã hóa công khai, khóa giải mã bí mật (RSA).

## 199-200. 접근통제 모델 심화 (Access Control Models Deep Dive)
- **DAC (임의 접근통제):** 데이터 소유자가 사용자 신원에 따라 권한 부여 (GRANT/REVOKE).
- **MAC (강제 접근통제):** 시스템이 주체와 객체의 보안 등급을 비교해 권한 부여.
  - **벨 라파듈라 (Bell-LaPadula):** 기밀성(Confidentiality) 중심.
  - **비바 (Biba):** 무결성(Integrity) 중심. (비인가자 데이터 변형 방지).
  - **클락-윌슨 (Clark-Wilson):** 상업용 무결성 모델. 프로그램에 의한 접근.
  - **만리장성 (Chinese Wall):** 이해 충돌 관계 객체 간 정보 접근 통제.
- **RBAC (역할기반 접근통제):** 중앙관리자가 사용자의 역할(Role)에 따라 권한 부여.
- **Vietnamese:** Mô hình kiểm soát truy cập.
  - DAC: Dựa trên danh tính (Người dùng cấp quyền).
  - MAC: Dựa trên cấp độ bảo mật (Hệ thống cấp quyền). Các mô hình: Bell-LaPadula (Bảo mật), Biba (Toàn vẹn)...
  - RBAC: Dựa trên vai trò (Role).

## 201-203. 스토리지 시스템 (Storage Systems)
- **DAS (Direct Attached Storage):** 서버와 저장장치를 전용 케이블로 직접 연결. (외장하드 방식). 확장성 떨어짐.
- **NAS (Network Attached Storage):** 네트워크를 통해 연결. 파일 공유 가능, 확장성 우수.
- **SAN (Storage Area Network):** 서버와 저장장치를 연결하는 전용 네트워크 구성. (광 채널 스위치). DAS의 속도 + NAS의 공유 장점.
- **Vietnamese:** Hệ thống lưu trữ.
  - DAS: Kết nối trực tiếp (cáp).
  - NAS: Kết nối qua mạng LAN (chia sẻ file).
  - SAN: Mạng lưu trữ chuyên dụng (tốc độ cao + chia sẻ).

## 204-219. SQL 명령어 심화 (SQL Commands Detail)
- **DDL (204, 207-209):** , , .
  -  옵션:  (참조하는 모든 개체 연쇄 제거),  (참조 중이면 제거 취소).
- **DML (205, 214-218):** , , , .
  - : 중복 튜플 제거.
  - : 정렬 (오름차순/내림차순).
- **DCL (206, 210-213):** , , , .
  - : 권한 부여. (옵션: 남에게 권한 부여 가능).
  - : 권한 회수.
  - : 변경 내용을 DB에 영구 반영.
  - : 변경 취소, 이전 상태로 복구.
- **Vietnamese:** Chi tiết các lệnh SQL.
  - : Xóa dây chuyền các phần phụ thuộc. : Không cho xóa nếu đang bị phụ thuộc.
  - : Cấp quyền và cho phép người đó cấp quyền tiếp cho người khác.
  - : Xác nhận lưu thay đổi. : Hoàn tác.

## 220-230. 하위 질의, 트리거, DBMS 접속 및 데이터 전환
- **하위 질의 (Subquery):** 조건절에 주어진 질의를 먼저 수행하여 결과를 피연산자로 사용.
- **트리거 (Trigger):** 데이터의 삽입/갱신/삭제 등 이벤트 발생 시 관련 작업이 자동 수행되는 절차형 SQL. DCL 사용 불가.
- **DBMS 접속 기술:** JDBC(Java 표준 API), ODBC(개방형 표준 API), MyBatis(SQL Mapping 프레임워크), ORM(객체와 DB 매핑).
- **데이터 전환 (Data Migration/ETL):** 기존 시스템에서 데이터를 추출(Extraction), 변환(Transformation), 적재(Loading)하는 과정.
- **Vietnamese:** Truy vấn con, Trigger, Kết nối DBMS & Chuyển đổi dữ liệu.
  - Subquery: Truy vấn lồng nhau.
  - Trigger: Tự động kích hoạt khi có sự kiện (INSERT/UPDATE/DELETE). Không dùng DCL trong Trigger.
  - Kết nối: JDBC (cho Java), ODBC (chuẩn mở), ORM (Ánh xạ đối tượng - quan hệ).
  - ETL: Trích xuất (E), Chuyển đổi (T), Tải (L) dữ liệu sang hệ thống mới.

---

# 3과목 운영체제 (Operating System - 추가 포함된 내용)

## 121-124. 운영체제 개요 및 시스템 소프트웨어
- **시스템 소프트웨어:** 제어 프로그램(감시, 작업 제어, 자료 관리)과 처리 프로그램(언어 번역, 서비스, 문제 프로그램)으로 구성.
- **운영체제 목적:** 처리 능력(Throughput) 향상, 신뢰도(Reliability) 향상, 사용 가능도(Availability) 향상, 반환 시간(Turn Around Time) 단축.
- **발달 과정:** 일괄 처리 -> 다중 프로그래밍/시분할/실시간 -> 다중 모드 -> 분산 처리.
- **컴파일러 vs 인터프리터:** 컴파일러는 전체 번역(목적 프로그램 생성, 실행 빠름). 인터프리터는 한 줄씩 번역/실행(목적 프로그램 없음, 번역 빠르나 실행 느림).
- **Vietnamese:** Tổng quan Hệ điều hành (OS) & Phần mềm hệ thống.
  - Mục tiêu OS: Tăng thông lượng, độ tin cậy, tính khả dụng; giảm thời gian phản hồi.
  - Trình biên dịch (Compiler) dịch toàn bộ, Trình thông dịch (Interpreter) dịch từng dòng.

## 125-129. 프로세스, 스레드, PCB (Process, Thread, PCB)
- **프로세스 (Process):** 실행 중인 프로그램, PCB를 가진 프로그램, 디스패치 가능한 단위.
- **PCB (Process Control Block):** OS가 프로세스 정보를 저장하는 곳 (상태, 포인터, 고유 식별자, 우선순위, 레지스터 등).
- **상태 전이:** 준비(Ready) -> 실행(Run) -> 대기(Wait/Block) -> 준비.
  - Dispatch: 준비 -> 실행. Wake-Up: 대기 -> 준비.
- **스레드 (Thread):** 프로세스 내의 독립적인 스케줄링 최소 단위. 경량 프로세스. 병행성 증대.
- **Vietnamese:** Tiến trình (Process) & Luồng (Thread).
  - Process: Chương trình đang chạy. PCB lưu trữ thông tin của tiến trình.
  - Thread: Đơn vị lập lịch nhỏ nhất trong tiến trình, giúp tăng cường độ đồng thời.
  - Vòng đời: Ready -> Run -> Wait -> Ready.

## 130-134. 스케줄링 기법 (Scheduling)
- **비선점형 (Non-preemptive):** 뺏을 수 없음. FCFS(FIFO), SJF(Shortest Job First), HRN(우선순위=대기시간+서비스시간/서비스시간). 에이징(Aging) 기법으로 기아 상태 해결.
- **선점형 (Preemptive):** 뺏을 수 있음. SRT, RR(Round Robin - 시간 할당량), 다단계 큐.
- **Vietnamese:** Lập lịch CPU (Scheduling).
  - Không độc chiếm (Non-preemptive): Không bị ngắt giữa chừng (FCFS, SJF, HRN).
  - Độc chiếm (Preemptive): Có thể bị ngắt (SRT, RR).

## 135-138. 교착 상태와 동기화 (Deadlock & Synchronization)
- **임계 구역 (Critical Section):** 하나의 프로세스만 사용 가능한 공유 자원 영역.
- **상호 배제 (Mutual Exclusion):** 동시 사용 막는 기법. 데커 알고리즘, 피터슨 알고리즘.
- **세마포어 (Semaphore):** P연산(Wait)과 V연산(Signal)으로 동기화 유지.
- **교착 상태 (Deadlock) 4조건:** 상호 배제, 점유와 대기, 비선점, 환형 대기.
- **해결 기법:** 예방(조건 부정), 회피(은행원 알고리즘), 발견, 회복.
- **Vietnamese:** Tắc nghẽn (Deadlock) & Đồng bộ hóa.
  - Vùng tới hạn: Chỉ 1 tiến trình được dùng tại 1 thời điểm.
  - Mutual Exclusion: Ngăn chặn truy cập đồng thời.
  - Semaphore: Dùng P (chờ) và V (tín hiệu).
  - Deadlock: Xảy ra khi đủ 4 điều kiện. Khắc phục bằng Ngăn ngừa, Tránh (Thuật toán Banker), Phát hiện, Phục hồi.

## 139-147. 기억장치 관리 및 페이지 교체 (Memory Management)
- **반입 전략:** 요구 반입, 예상 반입.
- **배치 전략:** 최초 적합(First Fit), 최적 적합(Best Fit), 최악 적합(Worst Fit).
- **단편화 (Fragmentation):** 내부 단편화(남는 공간), 외부 단편화(들어갈 수 없는 작은 공간). 통합/압축으로 해결.
- **가상 기억장치 (Virtual Memory):** 페이징(동일 크기 분할, 내부 단편화 발생), 세그먼테이션(논리적 크기 분할, 외부 단편화 발생).
- **페이지 교체 알고리즘:** FIFO(먼저 들어온 것 교체), LRU(최근에 가장 오랫동안 사용 안 한 것 교체), LFU(사용 빈도 가장 적은 것 교체).
- **국부성 (Locality):** 시간 구역성(반복문, 스택), 공간 구역성(배열 순회).
- **스래싱 (Thrashing):** 페이지 부재가 너무 잦아 시스템 성능 저하. 워킹 셋(Working Set)으로 방지.
- **Vietnamese:** Quản lý bộ nhớ.
  - Phân mảnh: Nội vi (còn dư), Ngoại vi (không đủ chỗ).
  - Bộ nhớ ảo: Phân trang (Paging - kích thước bằng nhau) và Phân đoạn (Segmentation - theo logic).
  - Thuật toán thay trang: FIFO, LRU, LFU. Thrashing xảy ra khi lỗi trang quá nhiều.

## 148-154. 파일 시스템과 디렉터리, 보안 (File System & Security)
- **순차 파일 (Sequential File):** 연속 기록 (자기 테이프). 접근 느림.
- **색인 순차 파일 (Indexed Sequential File):** 순차 + 색인(포인터). (기본, 색인, 오버플로 영역).
- **직접 파일 (Direct File):** 해싱 함수로 물리적 주소 직접 계산. 접근 빠름.
- **디렉터리 구조:** 1단계, 2단계, 트리, 비순환 그래프(공유 허용), 일반적인 그래프(순환 허용).
- **보안 기법:** 접근 제어 행렬, 전역 테이블, 접근 제어 리스트, 권한 리스트.
- **Vietnamese:** Hệ thống file & Bảo mật.
  - Cấu trúc file: Tuần tự, Tuần tự có chỉ mục, Trực tiếp (hashing).
  - Cấu trúc thư mục: Cây, Đồ thị không chu trình (cho phép chia sẻ).


# 3과목 데이터베이스 구축 (Phần 3: Xây dựng Cơ sở dữ liệu) - Phần 1

> [!NOTE]
> Mặc dù đây là nội dung môn 3 (CSDL), có một số kiến thức hệ điều hành UNIX còn sót lại từ phần trước.

## 1. UNIX 파일 시스템의 구조 (Cấu trúc hệ thống tệp UNIX)

- **부트 블록 (Boot Block - Khối khởi động):**
  - 부팅 시 필요한 코드를 저장하고 있는 블록.
  - _Giải thích VN:_ Khối lưu trữ mã cần thiết khi khởi động máy.
  - _Ví dụ:_ MBR (Master Boot Record) trong Windows, nhưng ở UNIX nó nằm ở Boot Block, chứa bootloader để nạp hệ điều hành.

- **슈퍼 블록 (Super Block - Siêu khối):**
  - 전체 파일 시스템에 대한 정보를 저장. 사용 가능한 I-node, 사용 가능한 디스크 블록의 개수 등을 포함.
  - _Giải thích VN:_ Chứa thông tin về toàn bộ hệ thống tệp: số lượng I-node trống, các khối đĩa trống. Mỗi hệ thống tệp có Super Block riêng.
  - _Ví dụ:_ Giống như mục lục tổng quát của một thư viện cho biết thư viện có bao nhiêu kệ sách và bao nhiêu sách chưa được mượn.

- **I-node 블록 (I-node Block - Khối I-node):**
  - 각 파일이나 디렉터리에 대한 모든 정보를 저장. (소유자 UID/GID, 파일 크기, 타입, 생성/변경 시기, 권한, 데이터 블록 시작 주소 등).
  - _Giải thích VN:_ Lưu trữ siêu dữ liệu (metadata) của tệp (chủ sở hữu, kích thước, quyền, địa chỉ bắt đầu của dữ liệu, thời gian tạo/sửa).
  - _Ví dụ:_ I-node giống như thẻ căn cước (ID card) của tệp, mọi thông tin quản lý đều nằm ở đây trừ tên tệp và nội dung thực sự.

- **데이터 블록 (Data Block - Khối dữ liệu):**
  - 실제 파일에 대한 데이터가 저장된 블록.
  - _Giải thích VN:_ Nơi lưu trữ nội dung thực tế của tệp hoặc danh sách các thư mục con.
  - _Ví dụ:_ Các trang sách chứa nội dung chữ bên trong thư viện.

> 💡 **Mẹo ghi nhớ (Mnemonics):** 
> Thứ tự các khối: **B**oot -> **S**uper -> **I**-node -> **D**ata (**BSID** - Bác Sĩ I-node Dễ thương).

---

## 2. UNIX의 주요 명령어 (Các lệnh UNIX chính)

| 명령어 (Command) | 의미 (Ý nghĩa) | Giải thích & Ví dụ (VN) |
|---|---|---|
| `fork` | 새로운 프로세스 생성 (Tạo tiến trình con/nhân bản tiến trình). | Giống như phân thân. Ví dụ: Tiến trình cha gọi `fork` tạo ra một tiến trình con y hệt để làm việc song song. |
| `exec` | 새로운 프로세스 수행 (Thực thi tiến trình mới). | Thay thế tiến trình hiện tại bằng tiến trình mới. Ví dụ: Dùng `exec` để mở chương trình máy tính (calculator). |
| `&` | 백그라운드 처리 (Chạy nền). | Đặt ở cuối lệnh. Ví dụ: `find / -name test.txt &` (Tìm kiếm ngầm, cho phép gõ tiếp lệnh khác). |
| `wait` | 하위 프로세스 종료 대기 (Đợi tiến trình con kết thúc). | Ví dụ: Tiến trình cha đứng đợi (wait) tiến trình con hoàn thành công việc mới tiếp tục. |
| `exit` | 프로세스 수행 종료 (Kết thúc tiến trình). | Ví dụ: Gõ `exit` để đóng terminal. |
| `cat` | 파일 내용 표시 (Hiển thị nội dung tệp, giống `TYPE` trong DOS). | Ví dụ: `cat file.txt` (In nội dung file.txt ra màn hình). |
| `chmod` | 파일 권한 지정 (Thay đổi quyền truy cập tệp). | Ví dụ: `chmod 777 file.sh` (Cấp toàn quyền đọc, ghi, chạy). |
| `chown` | 소유자 변경 (Thay đổi chủ sở hữu). | Ví dụ: `chown root file.txt` (Đổi chủ tệp thành root). |
| `mount` | 파일 시스템 마운팅 (Gắn hệ thống tệp). | Ví dụ: Cắm USB vào và dùng `mount` để hệ thống nhận diện nội dung USB. |
| `mkfs` | 파일 시스템 생성 (Tạo hệ thống tệp). | Format ổ đĩa. Ví dụ: `mkfs.ext4 /dev/sda1`. |
| `chdir` / `cd` | 디렉터리 위치 변경 (Thay đổi thư mục). | Ví dụ: `cd /home`. |
| `fsck` | 파일 시스템 검사 및 보수 (Kiểm tra và sửa lỗi hệ thống tệp). | Giống chkdsk trong Windows. Ví dụ: `fsck /dev/sda1`. |
| `rmdir` | 디렉터리 삭제 (Xóa thư mục rỗng). | Ví dụ: `rmdir empty_folder`. |
| `ls` | 파일 목록 확인 (Xem danh sách tệp). | Ví dụ: `ls -l` (Xem danh sách chi tiết). |
| `getpid` / `getppid` | 자신의 / 부모 프로세스 ID 획득 (Lấy PID / Parent PID). | ID tiến trình để quản lý (vd: dùng kill để tắt). |
| `cp` / `mv` / `rm`| 복사 (Copy) / 이동 및 이름 변경 (Move/Rename) / 삭제 (Remove). | `cp a.txt b.txt`, `mv old.txt new.txt`, `rm a.txt`. |
| `finger` | 사용자 정보 표시 (Hiển thị thông tin người dùng). | Xem ai đang đăng nhập vào hệ thống. |

---

# CHAPTER 01 SQL 응용 (Ứng dụng SQL)

## 3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)

| 종류 (Loại) | 설명 (Mô tả) | Ví dụ & Giải thích (VN) |
|---|---|---|
| **트리거 (Trigger)** | 테이블 이벤트(Insert, Update, Delete)에 반응해 **자동**으로 실행되는 작업. (Thực thi tự động khi có sự kiện). | _Ví dụ:_ Khi xóa 1 nhân viên khỏi bảng NhânViên, một trigger tự động lưu thông tin nhân viên đó vào bảng NhanVien_NghiViec (Audit log). |
| **프로시저 (Procedure)** | 어떤 행동을 수행하기 위한 일련의 작업 순서. (Một chuỗi các thao tác lưu sẵn để thực thi chung). | _Ví dụ:_ Một procedure `Tinh_Luong_Thang` chạy cuối tháng để tính lương cho toàn bộ công ty. |
| **사용자 정의 함수 (User-Defined Function)** | 단일 값으로 반환할 수 있도록 수행. (Hàm do người dùng định nghĩa, trả về một giá trị duy nhất). | _Ví dụ:_ Hàm `GET_AGE(ngay_sinh)` tự động tính và trả về tuổi. |

---

## 4. SQL 문법의 종류 (Các loại cú pháp SQL)

| 종류 (Loại) | 명령어 (Lệnh) | 설명 & 역할 (Mô tả & Vai trò) | Giải thích (VN) |
|---|---|---|---|
| **DDL** (Data Definition Language) | CREATE, ALTER, DROP, TRUNCATE | 데이터베이스를 **정의**하는 언어, 구조 결정. (Ngôn ngữ định nghĩa dữ liệu - Cấu trúc). | Dùng để Tạo (CREATE), Sửa (ALTER), Xóa hoàn toàn (DROP), hoặc Xóa trắng (TRUNCATE) bảng. Giống như việc xây/đập một ngôi nhà. |
| **DML** (Data Manipulation Language) | SELECT, INSERT, UPDATE, DELETE | 저장된 자료를 조회, 삽입, 수정, 삭제. (Ngôn ngữ thao tác dữ liệu - Nội dung). | Dùng để Thêm, Sửa, Xóa, Lấy dữ liệu bên trong bảng. Giống như việc sắp xếp đồ đạc trong nhà. |
| **DCL** (Data Control Language) | GRANT, REVOKE, COMMIT, ROLLBACK | 데이터 보안, 무결성, 권한, 병행 수행제어. (Ngôn ngữ điều khiển dữ liệu - Quyền & Giao dịch). | Dùng để Cấp quyền (GRANT), Thu hồi quyền (REVOKE), hoặc kiểm soát giao dịch (COMMIT/ROLLBACK). |

> 💡 **Mẹo ghi nhớ:**
> DDL: **CADT** (Create, Alter, Drop, Truncate - "Cắt" cấu trúc).
> DML: **SUDI** (Select, Update, Delete, Insert - "Sửa đi" dữ liệu).
> DCL: **GRCR** (Grant, Revoke, Commit, Rollback - "Gác cổng" bảo vệ).

---

## 5. 스키마 (Schema - Lược đồ)

- **외부 스키마 (External Schema - Lược đồ ngoại):** 사용자나 개발자의 관점 (Góc nhìn người dùng). Nhiều lược đồ ngoại tồn tại cùng lúc (Mỗi người nhìn hệ thống một kiểu).
- **개념 스키마 (Conceptual Schema - Lược đồ khái niệm):** 조직 전체의 논리적 구조, 단 하나만 존재 (Cấu trúc logic của toàn bộ tổ chức, chỉ có 1). Quản lý quan hệ, quyền, bảo mật.
- **내부 스키마 (Internal Schema - Lược đồ nội):** 물리적 저장장치의 관점 (Góc nhìn lưu trữ vật lý). Tổ chức các bản ghi, chỉ mục trên ổ đĩa.

> 💡 **Mẹo ghi nhớ:** **Ngoại - Khái - Nội** (Người dùng (Ngoại) -> Thiết kế CSDL (Khái) -> Ổ cứng (Nội)).

---

## 6. DDL, DML, DCL 상세 (Chi tiết DDL, DML, DCL)

### 6.1 DDL 문법 (Cú pháp DDL)
- `CREATE TABLE`: Tạo bảng. Các ràng buộc: `PRIMARY KEY` (Khóa chính), `FOREIGN KEY` (Khóa ngoại), `UNIQUE` (Duy nhất), `CONSTRAINT` (Điều kiện), `CHECK` (Kiểm tra), `DEFAULT` (Mặc định), `NOT NULL` (Không được rỗng).
- `ALTER TABLE`:
  - `ADD` (Thêm cột): `ALTER TABLE table_name ADD col_name datatype;`
  - `MODIFY` (Sửa kiểu/ràng buộc cột): `ALTER TABLE table_name MODIFY col_name datatype;`
  - `DROP` (Xóa cột): `ALTER TABLE table_name DROP col_name;`
  - `RENAME COLUMN`: Đổi tên cột.
- `DROP TABLE` [CASCADE | RESTRICT]: Xóa bảng. CASCADE (xóa luôn đối tượng phụ thuộc), RESTRICT (không xóa nếu đang bị tham chiếu).
- `TRUNCATE TABLE`: Xóa nhanh toàn bộ dữ liệu, giữ lại cấu trúc, **không thể ROLLBACK**.

### 6.2 DCL 문법 (Cú pháp DCL)
- `GRANT 권한 ON 테이블 TO 사용자 [WITH GRANT OPTION];` (Cấp quyền. WITH GRANT OPTION: cho phép người đó cấp quyền tiếp cho người khác).
- `REVOKE 권한 ON 테이블 FROM 사용자 [CASCADE CONSTRAINTS];` (Thu hồi quyền. CASCADE: thu hồi luôn quyền mà người này đã cấp cho người khác).
- `COMMIT`: Lưu vĩnh viễn giao dịch (Transaction) thành công.
- `ROLLBACK`: Hủy bỏ giao dịch bị lỗi, quay về trạng thái cũ.
- `SAVEPOINT`: Đặt điểm lưu để Rollback về điểm đó thay vì toàn bộ.

### 6.3 DML 문법 (Cú pháp DML)
- `SELECT [DISTINCT] 속성명 FROM 테이블 WHERE 조건 GROUP BY 속성명 HAVING 조건 ORDER BY 속성명 [ASC|DESC];`
  - `DISTINCT`: Loại bỏ dòng trùng lặp.
  - `GROUP BY`: Nhóm dữ liệu (ROLLUP, CUBE để tính tổng phụ).
  - `HAVING`: Điều kiện cho nhóm (GROUP BY).
- **집계 함수 (Hàm tập hợp):** `COUNT`, `SUM`, `AVG`, `MAX`, `MIN`, `STDDEV` (độ lệch chuẩn), `VARIANCE` (phương sai).
- **순위 함수 (Hàm xếp hạng):** `RANK` (bỏ qua số hạng: 1, 1, 3), `DENSE_RANK` (không bỏ qua: 1, 1, 2), `ROW_NUMBER` (đánh số thứ tự: 1, 2, 3).
- **WHERE 연산자 (Toán tử điều kiện):** `LIKE '%'` (Nhiều ký tự), `LIKE '_'` (1 ký tự), `BETWEEN A AND B`, `IN()`, `IS NULL`.
- `UPDATE 테이블 SET 속성 = 데이터 WHERE 조건;` (Sửa dữ liệu).
- `DELETE FROM 테이블 WHERE 조건;` (Xóa dữ liệu, có thể ROLLBACK).
- `INSERT INTO 테이블 (속성) VALUES (데이터);` (Thêm dữ liệu).

---

## 7. 집합연산자 및 조인 (Toán tử tập hợp và JOIN)

### 집합 연산자 (Toán tử tập hợp)
- `UNION`: Hợp (Loại bỏ trùng lặp).
- `UNION ALL`: Hợp tất cả (Giữ nguyên trùng lặp).
- `INTERSECT`: Giao (Chỉ lấy phần chung).
- `MINUS` / `EXCEPT`: Hiệu (Lấy bảng 1 trừ đi các dòng có trong bảng 2).

### 조인 (JOIN)
- **INNER JOIN**: Lấy các dòng có dữ liệu khớp nhau (Giao). `SELECT * FROM A INNER JOIN B ON A.id = B.id;`
- **OUTER JOIN (LEFT, RIGHT, FULL)**: Lấy cả dữ liệu không khớp. Bên thiếu dữ liệu sẽ điền NULL.
  - Cú pháp Oracle (+): `WHERE A.id = B.id(+)` (Đây là LEFT OUTER JOIN vì dấu (+) nằm ở bảng B, tức là bảng B thiếu cũng không sao).
- **SELF JOIN**: Bảng tự JOIN với chính nó. (Dùng `AS` để tạo bí danh).
- **CROSS JOIN**: Tích Đề-các (Cartesian product), bắt cặp tất cả các dòng của 2 bảng.

---

## 8. 서브쿼리와 뷰 (Truy vấn con và View)

### 서브쿼리 (Subquery)
- **단일 행 서브쿼리 (Single-row Subquery):** Trả về 1 dòng. Dùng toán tử `=`, `>`, `<`.
- **다중 행 서브쿼리 (Multi-row Subquery):** Trả về nhiều dòng. Dùng `IN`, `ANY`, `ALL`.
- **인라인 뷰 (Inline View):** Subquery nằm trong mệnh đề `FROM`, tạo thành bảng ảo tạm thời.

### 뷰 (VIEW - Bảng ảo)
- `CREATE VIEW 뷰명 AS (SELECT문);`
- `DROP VIEW 뷰명;`
- **장점 (Ưu điểm):** Bảo mật (chỉ cho xem cột cần thiết), Đơn giản hóa truy vấn phức tạp, Đảm bảo tính toàn vẹn dữ liệu.
- **단점 (Nhược điểm):** Không thể sửa đổi cấu trúc dễ dàng, cơ bản là Read Only, **Không thể gắn Index (인덱스 불가능)**.

---

## 9. 인덱스와 트랜잭션 (Index và Giao dịch)

### 인덱스 (Index - Chỉ mục)
Dùng để tăng tốc độ tìm kiếm.
- **트리 기반 (Tree-based):** Thường dùng B-Tree, tốt cho tìm theo khoảng.
- **해시 (Hash):** Dùng Key-Value, truy cập nhanh và chi phí đồng đều, không tốt cho tìm khoảng.
- **비트맵 (Bitmap):** Dùng bit 0 và 1, phù hợp cho cột có ít giá trị khác biệt (Gender: M/F).
- **클러스터드 인덱스 (Clustered Index):** Dữ liệu thực sự được sắp xếp vật lý theo thứ tự Index. Rất tốt để tìm khoảng (Range search).

### 트랜잭션 (Transaction - Giao dịch) - ACID
| 특징 (Đặc tính) | 설명 (Mô tả) | Ý nghĩa (VN) |
|---|---|---|
| **원자성 (Atomicity)** | All or Nothing (모두 반영되거나 전혀 반영되지 않음). | **Tính nguyên tử:** Chuyển tiền: hoặc cả 2 người cùng cập nhật, hoặc không ai thay đổi gì. Dùng Commit/Rollback. |
| **일관성 (Consistency)** | 일관적인 DB 상태 유지 (Trạng thái DB nhất quán). | **Tính nhất quán:** Dữ liệu sau giao dịch phải hợp lệ. |
| **고립성 (Isolation)** | 서로 간섭 불가 (Không can thiệp lẫn nhau). | **Tính cô lập:** Khi giao dịch A đang chạy, giao dịch B không thể nhảy vào làm sai lệch. |
| **영속성 (Durability)** | 영구적으로 결과 저장 (Lưu kết quả vĩnh viễn). | **Tính bền vững:** Sau khi COMMIT, dù sập nguồn dữ liệu vẫn tồn tại. |

> 💡 **Mẹo ghi nhớ:** **ACID** (Nguyên tử - Nhất quán - Cô lập - Bền vững).

---

## 10. 트랜잭션 관리 기법 및 제어 (Quản lý và điều khiển giao dịch)

### 병행제어 기법 (Concurrency Control - Kiểm soát đồng thời)
- **로킹 (Locking):** Khóa tài nguyên để đảm bảo giao dịch chạy tuần tự (직렬화).
  - *Đơn vị khóa (Locking Unit):* Càng lớn (DB, Bảng) -> Ít Lock, Overhead nhỏ, Tính đồng thời giảm. Càng nhỏ (Bản ghi, Trường) -> Nhiều Lock, Overhead lớn, Tính đồng thời cao.
- **타임스탬프 (Time Stamping):** Gắn mốc thời gian để ưu tiên.
- **다중버전 동시제어 (MVCC):** Giữ nhiều phiên bản dữ liệu.
- **낙관적 병행제어 (Optimistic):** Cứ cho chạy đi, kết thúc mới kiểm tra lỗi (thích hợp môi trường ít xung đột).

### 트랜잭션 상태 (Trạng thái giao dịch)
- **활동 (Active):** Đang chạy.
- **부분 완료 (Partially Committed):** Đã chạy lệnh xong, chuẩn bị COMMIT nhưng chưa ghi lên đĩa.
- **완료 (Committed):** Thành công và lưu vĩnh viễn.
- **실패 (Failed):** Có lỗi xảy ra.
- **철회 (Aborted):** Bị hủy bỏ (Rollback).

### 데이터 사전 (Data Dictionary / System Catalog / Metadata)
- Lưu thông tin về các đối tượng (bảng, view, index...).
- DBMS tự động cập nhật, người dùng **chỉ được Read Only (조회만 가능)**.

---

## 11. 데이터베이스 설계 (Thiết kế cơ sở dữ liệu)

| 단계 (Giai đoạn) | 설명 (Mô tả & Hoạt động) | Giải thích (VN) |
|---|---|---|
| **1. 요구조건 분석** | 목적 파악, 요구조건 식별 | Phân tích yêu cầu: Tìm hiểu người dùng cần gì. |
| **2. 개념적 설계** | 개념 스키마, E-R 다이어그램, 트랜잭션 모델링 | Thiết kế Khái niệm: Độc lập với DBMS. Vẽ biểu đồ ER (Thực thể - Mối quan hệ). |
| **3. 논리적 설계** | 논리적 자료구조, **정규화(Normalization)**, 트랜잭션 인터페이스 설계 | Thiết kế Logic: Chuyển đổi ER sang bảng (Table). **Thực hiện chuẩn hóa (Normalization)**. |
| **4. 물리적 설계** | 물리적 구조, 저장 레코드 양식, **접근 경로(Access Path)** | Thiết kế Vật lý: Định dạng file trên đĩa cứng, chọn kiểu dữ liệu thực tế, thiết lập cấu trúc lưu trữ và Index (Đường truy cập). |

> 💡 **Mẹo ghi nhớ:** **Yêu - Khái - Lo - Vật** (Yêu cầu -> Khái niệm -> Logic -> Vật lý). Dễ thi: Chuẩn hóa ở bước Logic, Access Path/Lưu trữ ở bước Vật lý.

test
---

## 12. 관계형 데이터 모델과 릴레이션 (Mô hình dữ liệu quan hệ & Relation)

### 12.1 릴레이션의 구조 (Cấu trúc Relation / Bảng)
- **릴레이션 (Relation):** Bảng dữ liệu gồm hàng và cột.
- **튜플 (Tuple):** Hàng (Row / Record).
- **속성 (Attribute):** Cột (Column / Field).
- **차수 (Degree / 디그리):** Số lượng thuộc tính (Cột).
- **카디널리티 (Cardinality):** Số lượng 튜플 (Hàng).
- **도메인 (Domain):** Tập hợp các giá trị nguyên tử (Atomic) mà một thuộc tính có thể nhận.
- **인스턴스 (Instance):** Tập hợp các 튜플 tại một thời điểm (Dữ liệu thực tế).

> 💡 **Mẹo ghi nhớ:** **Car-Tu, De-At** (Cardinality = Tuple/Hàng, Degree = Attribute/Cột).

### 12.2 릴레이션의 특징 (Đặc điểm của Relation)
- **튜플의 유일성:** Không có 2 hàng nào giống hệt nhau.
- **튜플/속성의 무순서:** Thứ tự của các hàng và các cột **không quan trọng**.
- **원자값:** Mỗi ô (giao giữa hàng và cột) chỉ được chứa một giá trị duy nhất (không thể chia nhỏ).

---

## 13. 데이터 모델과 E-R 다이어그램 (Mô hình dữ liệu & Biểu đồ E-R)

### 데이터 모델 구성 요소 (Thành phần mô hình dữ liệu)
- **개체 (Entity):** Đối tượng thực tế (ví dụ: Sinh viên, Môn học).
- **속성 (Attribute):** Đặc điểm của đối tượng (ví dụ: Mã SV, Tên).
- **관계 (Relationship):** Sự liên kết giữa các đối tượng (ví dụ: Đăng ký).
- *Lưu ý: 3 yếu tố cơ bản của mô hình là Cấu trúc (Structure), Phép toán (Operation), và Ràng buộc (Constraint).*

### E-R 다이어그램 기호 (Ký hiệu biểu đồ E-R - Peter Chen)
| 기호 (Ký hiệu) | 의미 (Ý nghĩa) | Giải thích (VN) |
|---|---|---|
| **사각형 (Hình chữ nhật)** | 개체 (Entity) | Đối tượng thực thể. |
| **마름모 (Hình thoi)** | 관계 (Relationship) | Mối quan hệ giữa các thực thể (1:1, 1:N, N:M). |
| **타원 (Hình bầu dục)** | 속성 (Attribute) | Thuộc tính. |
| **밑줄 타원 (Bầu dục gạch dưới)** | 기본키 (Primary Key) | Thuộc tính Khóa chính. |
| **이중 타원 (Bầu dục kép)** | 다중 값 속성 (Multi-valued) | Thuộc tính đa trị (có thể chứa nhiều giá trị, vd: Số điện thoại). |
| **선 (Đường thẳng)** | 링크 (Link) | Đường nối kết. |

---

## 14. 키(Key)의 종류와 데이터베이스 무결성 (Các loại Khóa & Tính Toàn vẹn)

### 키(Key) 종류 (Các loại Khóa)
| 종류 (Loại) | 설명 (Mô tả) | Tính chất (VN) |
|---|---|---|
| **슈퍼키 (Super Key)** | 튜플을 구별할 수 있는 속성 집합. | **Tính duy nhất (유일성).** |
| **후보키 (Candidate Key)** | 기본키가 될 수 있는 키 (유일성 + 최소성). | **Duy nhất + Tối thiểu (최소성).** (Không dư thừa thuộc tính). |
| **기본키 (Primary Key)** | 후보키 중 선택된 주키. NULL 불가. | Khóa chính. **Không được trùng, Không được NULL.** |
| **대체키 (Alternate Key)** | 기본키로 선택되지 못한 나머지 후보키. | Khóa thay thế (Khóa phụ). |
| **외래키 (Foreign Key)** | 다른 릴레이션의 기본키를 참조하는 속성. | Khóa ngoại. Dùng để liên kết 2 bảng. |

### 무결성 (Integrity - Tính toàn vẹn / chính xác)
- **개체 무결성 (Entity):** Khóa chính (Primary Key) không được trùng lặp và **không được NULL**.
- **참조 무결성 (Referential):** Khóa ngoại (Foreign Key) phải khớp với Khóa chính của bảng tham chiếu, hoặc có thể là NULL.
- **도메인 무결성 (Domain):** Giá trị phải nằm trong phạm vi định nghĩa (ví dụ: Giới tính chỉ là Nam/Nữ).
- **사용자 정의 무결성 (User-defined):** Phải thỏa mãn các điều kiện do người dùng tự định nghĩa.

---

## 15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)

### 일반 집합 연산자 (Toán tử tập hợp cơ bản)
- **합집합 (UNION, ∪):** Hợp (lấy tất cả, bỏ trùng lặp).
- **교집합 (INTERSECTION, ∩):** Giao (lấy phần chung).
- **차집합 (DIFFERENCE, —):** Hiệu (R - S: có trong R nhưng không có trong S).
- **교차곱 (CARTESIAN PRODUCT, Х):** Tích Đề-các (kết hợp tất cả các dòng của 2 bảng).

### 순수 관계 연산자 (Toán tử quan hệ thuần túy)
| 연산자 (Toán tử) | 기호 (Ký hiệu) | 설명 (Mô tả) |
|---|---|---|
| **Select (선택)** | **σ (Sigma)** | Lấy các **Hàng (Tuple)** thỏa mãn điều kiện (Phép toán nằm ngang - 수평). |
| **Project (추출)** | **π (Pi)** | Lấy các **Cột (Attribute)** được chỉ định, loại bỏ trùng lặp (Phép toán dọc - 수직). |
| **Join (조인)** | **⋈ (Bowtie)** | Kết hợp 2 bảng dựa trên thuộc tính chung. |
| **Division (나누기)** | **÷ (Divide)** | Trả về các 튜플 của bảng R mà khớp với tất cả giá trị thuộc tính của bảng S. |

> 💡 **Mẹo ghi nhớ:** **Se-Hàng, Pro-Cột** (Select = Hàng/Tuple, Project = Cột/Attribute).

---

## 16. 정규화(Normalization)와 이상 현상(Anomaly)

**정규화 (Chuẩn hóa):** Quá trình chia nhỏ các bảng để giảm thiểu dư thừa dữ liệu và tránh các hiện tượng bất thường (이상 현상).

### 이상 현상 (Anomaly - Bất thường)
- **삽입 이상 (Insertion Anomaly):** Lỗi khi thêm dữ liệu (phải thêm các dữ liệu không mong muốn).
- **갱신 이상 (Update Anomaly):** Lỗi khi cập nhật (cập nhật thiếu sót dẫn đến dữ liệu không nhất quán).
- **삭제 이상 (Deletion Anomaly):** Lỗi 연쇄 삭제 (Xóa dây chuyền) (xóa một dữ liệu kéo theo mất luôn dữ liệu quan trọng khác).

### 정규화 단계 (Các chuẩn - Bắt buộc học thuộc)
| 정규형 (Chuẩn) | 조건 (Điều kiện để đạt được) | Mẹo ghi nhớ (VN) |
|---|---|---|
| **1NF** | **도**메인이 **원자값** (Mọi giá trị phải là Nguyên tử) | **도** (Do - Domain nguyên tử) |
| **2NF** | **부**분 함수 종속 제거 (Loại bỏ phụ thuộc hàm từng phần) | **부** (Bu - Bỏ phụ thuộc phần) |
| **3NF** | **이**행 함수 종속 제거 (Loại bỏ phụ thuộc hàm bắc cầu: A→B, B→C => A→C) | **이** (I - Loại bắc cầu / I-haeng) |
| **BCNF** | 모든 **결**정자가 후보키 (Tất cả yếu tố quyết định phải là Khóa ứng viên) | **결** (Gyeol - BCNF) |
| **4NF** | **다**치 종속 제거 (Loại bỏ phụ thuộc đa trị) | **다** (Da - Đa trị) |
| **5NF** | **조**인 종속 제거 (Loại bỏ phụ thuộc Join) | **조** (Jo - Join) |

> 💡 **Mẹo ghi nhớ:** **Đồ-Bếp-I-Kết-Đa-Giò** (Đô-main, Bếp-Phần, I-Bắc cầu, Kết-Quyết định, Đa trị, Giò-Chung).

---

## 17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)

### 스토리지 (Storage - Thiết bị lưu trữ)
- **DAS (Direct Attached Storage):** Kết nối trực tiếp bằng cáp. Nhanh, an toàn nhưng khó mở rộng.
- **NAS (Network Attached Storage):** Kết nối qua mạng (Network-based, File-level). Mềm dẻo nhưng có thể nghẽn mạng.
- **SAN (Storage Area Network):** Dùng cáp quang (Fiber Channel), tốc độ cực cao, đắt tiền.
- **SDS (Software-defined Storage):** Quản lý toàn bộ tài nguyên lưu trữ bằng phần mềm (Ảo hóa lưu trữ).

### 분산 데이터베이스 (Distributed Database - CSDL Phân tán)
Dữ liệu phân bố ở nhiều nơi (máy chủ khác nhau) nhưng người dùng cảm giác như đang dùng 1 CSDL duy nhất.
- **장점 (Ưu điểm):** Đáng tin cậy, dễ mở rộng, tính tự trị khu vực cao.
- **단점 (Nhược điểm):** Thiết kế khó, chi phí cao, bảo mật phức tạp.

**4대 투명성 (4 Đặc tính Trong suốt - Transparency):**
1. **위치 투명성 (Location):** Người dùng không cần biết dữ liệu nằm ở máy chủ nào.
2. **중복(복제) 투명성 (Replication):** Không cần biết dữ liệu được nhân bản ra sao.
3. **병행 투명성 (Concurrency):** Nhiều người truy cập cùng lúc vẫn không bị lỗi kết quả.
4. **장애 투명성 (Failure):** Một Node chết, toàn hệ thống vẫn hoạt động bình thường.

---

## 18. 파티셔닝과 암호화 (Phân vùng và Mã hóa)

### 파티셔닝 (Partitioning)
Chia các bảng lớn thành các phần nhỏ (Partition) để dễ quản lý và tăng hiệu suất.
- **범위 분할 (Range):** Phân chia theo khoảng (VD: Tháng 1, Tháng 2).
- **해시 분할 (Hash):** Dùng hàm băm để chia đều. Dữ liệu phân bố đều nhưng khó tìm theo khoảng.
- **목록 분할 (List):** Phân chia theo danh sách giá trị (VD: Nước: VN, KR, US).
- **조합 분할 (Composite):** Kết hợp các phương pháp trên.
- **라운드 로빈 (Round Robin):** Chia xoay vòng đều nhau tuần tự (Không cần khóa).

### 데이터베이스 암호화 (Mã hóa CSDL)
- **암호화 (Encryption):** Biến 평문 (Plaintext - Văn bản gốc) thành 암호문 (Ciphertext - Bản mã).
- **복호화 (Decryption):** Giải mã từ Ciphertext về Plaintext.
- **키 (Key):** Chìa khóa dùng để mã hóa và giải mã.
---

## 19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)

### 개인키 암호 방식 (Private Key / Symmetric Key - Mã hóa Khóa đối xứng)
- **개념 (Khái niệm):** Dùng **CÙNG MỘT KHÓA** để mã hóa và giải mã (단일키 - Khóa đơn).
- **장점 (Ưu điểm):** Tốc độ xử lý cực kỳ nhanh.
- **단점 (Nhược điểm):** Khó phân phối và quản lý khóa khi có quá nhiều người dùng.
- **종류 (Thuật toán tiêu biểu):** DES, AES, SEED, ARIA. (Chia làm 2 dạng: Block - theo khối, Stream - theo luồng bit).

> 💡 **Mẹo ghi nhớ:** **Đối-Cá-Nhanh-Khó** (Khóa Đối xứng = Khóa Cá nhân = Nhanh = Khó quản lý khóa).

### 접근통제 기술 (Access Control - Kỹ thuật kiểm soát truy cập)
| 종류 (Loại) | 기준 (Tiêu chí) | 특징 (Đặc điểm VN) |
|---|---|---|
| **DAC (임의 접근통제)** | 소유자 (Chủ sở hữu) | Chủ dữ liệu tự do cấp/thu quyền (GRANT/REVOKE). |
| **MAC (강제 접근통제)** | 보안 등급 (Mức độ bảo mật) | Hệ thống ép buộc dựa trên cấp độ bảo mật (VD: Top Secret). |
| **RBAC (역할기반 접근통제)** | 역할 (Vai trò) | Quyền gắn với chức vụ (VD: Manager, Staff). Đổi chức vụ = tự đổi quyền. |

### MAC 보안 모델 (Các mô hình bảo mật của MAC)
- **벨-라파듈라 (Bell-LaPadula):** Tập trung vào **기밀성 (Tính Bảo mật / Kín đáo)** (Quân đội). Không đọc lên trên, Không ghi xuống dưới.
- **비바 (Biba):** Tập trung vào **무결성 (Tính Toàn vẹn)**. Ngăn chặn việc sửa đổi trái phép.
- **클락-윌슨 (Clark-Wilson):** Dành cho thương mại, chỉ cho phép sửa qua phần mềm được ủy quyền.
- **만리장성 (Chinese Wall):** Tránh xung đột lợi ích (người xem hồ sơ công ty A thì không được xem của đối thủ B).

---

## 20. 쿼리 성능 최적화와 반정규화 (Tối ưu hóa Truy vấn và Phi chuẩn hóa)

### 쿼리 성능 최적화 (Query Optimization)
Tối ưu hóa tốc độ chạy SQL thông qua **Optimizer (옵티마이저 - Bộ tối ưu)**.
- **RBO (Rule-Based Optimizer):** Tối ưu theo **규칙 (Quy tắc)** định sẵn. Phụ thuộc vào kinh nghiệm người lập trình.
- **CBO (Cost-Based Optimizer):** Tối ưu theo **비용 (Chi phí)** ước tính dựa trên thống kê dữ liệu. Rất thông minh và phổ biến hiện nay.
- **APM (Application Performance Management):** Công cụ giám sát hiệu suất ứng dụng.

### 반정규화 (Denormalization - Phi chuẩn hóa)
- **개념:** Cố tình phá vỡ chuẩn hóa (Gộp bảng, thêm dữ liệu trùng lặp).
- **목적:** Để **tăng hiệu suất truy vấn (조회 속도 향상)** khi thao tác JOIN quá nhiều.
- **단점:** Đánh đổi bằng sự **suy giảm tính nhất quán** (데이터 정합성 저하) và khó khăn khi cập nhật dữ liệu.

---

## 21. 데이터 전환 및 정제 (Chuyển đổi dữ liệu - ETL)

### 데이터 전환 (Data Migration - Di chuyển dữ liệu)
Là quá trình chuyển dữ liệu từ hệ thống cũ sang hệ thống mới.
- **ETL 3 bước:** 
  1. **E**xtraction (추출): Trích xuất từ nguồn.
  2. **T**ransformation (변환): Biến đổi cho phù hợp chuẩn mới.
  3. **L**oad (적재): Nạp vào hệ thống đích.

### 오류 데이터 정제 (Error Data Cleansing)
Quản lý trạng thái lỗi trong quá trình chuyển đổi:
- **Open (Mở):** Phát hiện lỗi, chưa phân tích.
- **Assigned (Đã giao):** Giao cho lập trình viên sửa.
- **Fixed (Đã sửa):** Đã sửa xong.
- **Closed (Đóng):** Đã test lại và xác nhận bình thường.
- **Deferred (Trì hoãn):** Quyết định chưa sửa lúc này (hoặc không phải lỗi).

---

## 22. 기타 주요 개념 (Các khái niệm quan trọng khác)

### CRUD 분석 (Phân tích CRUD)
- Tạo ma trận (Matrix) giữa **Process (Tiến trình)** và **Table (Bảng)**.
- Đánh dấu **C**reate, **R**ead, **U**pdate, **D**elete để xem bảng nào bị thao tác nhiều/ít, phát hiện bảng bị bỏ sót (ít nhất mỗi bảng phải có 1 thao tác).

### MyBatis (프레임워크)
- Khung làm việc (Framework) giúp đơn giản hóa JDBC trong Java.
- **Đặc điểm:** Tách mã SQL ra khỏi mã Java (lưu trong file XML hoặc Annotation), thân thiện với lập trình viên SQL.

### 시스템 카탈로그 (System Catalog)
- **Định nghĩa:** CSDL đặc biệt chứa "dữ liệu về dữ liệu" (Metadata / Data Dictionary).
- **Đặc điểm:** Chỉ có hệ thống (DBMS) mới được quyền cập nhật (Tự động cập nhật). Người dùng chỉ có quyền **SELECT (Đọc)**.

### 연산자 우선순위 (Thứ tự ưu tiên toán tử trong SQL)
- 산술 연산자 (Toán học: `* / + -`) **>** 관계 연산자 (So sánh: `< > = !=`) **>** 논리 연산자 (Logic: `NOT > AND > OR`).

> 💡 **Mẹo ghi nhớ:** **Toán - Quan - Lo** (Toán học - Quan hệ - Logic). Nhân chia trước, cộng trừ sau, rồi đến so sánh, cuối cùng là AND/OR.

EOF


