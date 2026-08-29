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
