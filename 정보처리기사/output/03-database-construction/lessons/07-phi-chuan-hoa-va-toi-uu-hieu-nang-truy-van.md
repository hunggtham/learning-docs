# 07. 반정규화와 쿼리 성능 최적화 (Phi Chuẩn Hóa và Tối Ưu Hóa Hiệu Năng Truy Vấn)

## 1. 개요 및 학습 목표 (Tổng quan & Mục tiêu học tập)

- [한국어]: **반정규화(Denormalization, 역정규화)**는 시스템의 성능 향상, 개발 및 운영의 편의성을 위해 정규화된 데이터 모델을 의도적으로 통합, 중복, 분할하는 데이터베이스 설계 기법이다. 성능 최적화 과정에서 **옵티마이저(Optimizer)**의 실행 계획(Execution Plan) 분석과 비용 기반 접근이 핵심을 이룬다.
- [Tiếng Việt]: **Phi chuẩn hóa (Denormalization / 역정규화)** là kỹ thuật thiết kế cơ sở dữ liệu cố tình tích hợp, nhân bản hoặc phân chia lại các mô hình dữ liệu đã được chuẩn hóa nhằm nâng cao hiệu năng hệ thống, tạo thuận tiện cho phát triển và vận hành. Trong quy trình tối ưu hóa hiệu năng, việc phân tích kế hoạch thực thi (Execution Plan) của **Bộ tối ưu hóa truy vấn (Optimizer)** và tiếp cận dựa trên chi phí đóng vai trò cốt lõi.

### 학습 목표 (Mục tiêu kiến thức)
1. **반정규화의 개념과 트레이드오프 (Khái niệm & Đánh đổi của phi chuẩn hóa):** Hiểu rõ lý do cố tình vi phạm quy tắc chuẩn hóa để giảm thiểu phép kết nối (`Join`) và I/O đĩa cứng, đồng thời quản lý rủi ro suy giảm tính nhất quán (`일관성 저하`) và dị thường dữ liệu.
2. **반정규화 4대 대상 및 기법 (4 đối tượng & kỹ thuật phi chuẩn hóa chính):** Phân tích sâu kỹ thuật gộp bảng (`테이블 통합`), chia bảng (`테이블 분할` - ngang/dọc), thêm bảng trùng lặp (`중복 테이블 추가`), và thêm thuộc tính trùng lặp (`중복 속성 추가`).
3. **쿼리 성능 최적화와 옵티마이저 (Tối ưu hóa truy vấn & Optimizer):** Phân biệt bản chất bộ tối ưu hóa theo quy tắc (RBO) và bộ tối ưu hóa theo chi phí (CBO), cách đọc kế hoạch thực thi (`실행 계획 / Execution Plan`).

---

## 2. 개념 연결 및 브리지 (Cầu nối kiến thức)

- **Từ đâu (Origin - Xuất phát điểm):**
  - [한국어]: 이전 [06-bat-thuong-du-lieu-phu-thuoc-ham-va-chuan-hoa-1nf-5nf.md](06-bat-thuong-du-lieu-phu-thuoc-ham-va-chuan-hoa-1nf-5nf.md)에서 우리는 데이터 중복과 이상 현상(삽입·삭제·갱신 이상)을 완전히 제거하기 위해 릴레이션을 1NF부터 5NF까지 엄격하게 분해(Decomposition)하는 정규화 과정을 학습했습니다.
  - [Tiếng Việt]: Ở bài học trước, chúng ta đã nắm vững quy trình chuẩn hóa từ 1NF đến 5NF nhằm phân rã triệt để quan hệ để loại trừ hoàn toàn dư thừa dữ liệu và 3 loại dị thường (thêm, xóa, cập nhật).
- **Đang giải quyết gì (Current Problem - Vấn đề bài học giải quyết):**
  - [한국어]: 과도한 정규화는 테이블을 지나치게 잘게 쪼개어 단순한 데이터 조회에도 수많은 조인(Join)과 다량의 디스크 I/O를 유발하여 시스템 응답 속도를 심각하게 저하시킵니다. 본 강의에서는 성능 향상을 위해 의도적으로 정규화 원칙을 위배하는 **반정규화(Denormalization)** 기법과 SQL 쿼리를 최적화하는 **옵티마이저(Optimizer)** 메커니즘을 규명합니다.
  - [Tiếng Việt]: Việc chuẩn hóa quá đà chia cắt dữ liệu thành quá nhiều bảng nhỏ, khiến các câu truy vấn thông thường phải thực hiện nhiều phép Join phức tạp và gây thắt cổ chai I/O đĩa, làm sụt giảm nghiêm trọng hiệu năng. Bài học này giải quyết bài toán tái cân bằng hiệu năng bằng kỹ thuật **Phi chuẩn hóa (Denormalization)** và tối ưu truy vấn thông qua **Bộ tối ưu hóa (Optimizer)**.
- **Dùng đi đâu (Forward Handoff - Chuyển tiếp tương lai):**
  - [한국어]: 본 장에서 최적화된 테이블 구조와 인덱스 설계는 다음 [08-giao-dich-trang-thai-acid-va-dieu-khien-dong-thoi.md](08-giao-dich-trang-thai-acid-va-dieu-khien-dong-thoi.md)에서 다중 사용자 환경의 트랜잭션 무결성과 동시성 제어(Concurrency Control)를 보장하는 기반 인프라로 연결됩니다.
  - [Tiếng Việt]: Cấu trúc bảng và đường dẫn tối ưu được thiết lập ở bài học này sẽ là nền móng vận hành để xử lý an toàn các giao dịch đa người dùng và kiểm soát đồng thời (Concurrency Control) ở bài học tiếp theo.

---

## 3. 핵심 이론 및 용어 대조 (Lý thuyết cốt lõi & Đối chiếu thuật ngữ)

### 3.1. 반정규화의 개념과 필요성 (Bản chất Phi chuẩn hóa)

- [한국어]: **반정규화(Denormalization)**는 시스템의 성능 향상 및 운영 편의성을 위해 정규화된 데이터 모델을 통합, 중복, 분할하는 과정이다. 무조건적인 정규화가 아닌, **데이터 무결성과 시스템 성능 간의 균형(Trade-off)**을 맞추는 엔지니어링 의사결정이다.
- [Tiếng Việt]: **Phi chuẩn hóa (Denormalization)** là quá trình tích hợp, tạo trùng lặp hoặc phân chia các mô hình dữ liệu đã được chuẩn hóa nhằm nâng cao hiệu năng hệ thống và độ tiện lợi trong vận hành. Đây là quyết định kỹ thuật nhằm cân bằng giữa **tính toàn vẹn dữ liệu** và **tốc độ đáp ứng hệ thống**.

```
[ Mô hình Chuẩn hóa cao ]  --- (Join nhiều, I/O chậm) --->  [ Áp dụng 반정규화 ]
(Ưu tiên: Toàn vẹn, không dị thường)                   (Ưu tiên: Tốc độ đọc, giảm Join)
```

- **반정규화 고려 대상 (Trường hợp cần xem xét phi chuẩn hóa):**
  - [한국어]: 자주 수행되는 쿼리에서 다수의 조인(Join) 연산으로 인해 성능 저하가 발생하는 경우.
  - [Tiếng Việt]: Khi các truy vấn thường xuyên xuất hiện nhiều phép kết nối bảng (Join) gây suy giảm hiệu năng nghiêm trọng.
  - [한국어]: 대량의 데이터에 대해 주기적으로 집계 연산(SUM, AVG, COUNT)을 수행해야 하는 경우.
  - [Tiếng Việt]: Khi phải liên tục thực hiện các phép tính toán tổng hợp (SUM, AVG, COUNT) trên tập dữ liệu khổng lồ.
  - [한국어]: 특정 범위의 데이터를 조회할 때 지나치게 많은 디스크 블록을 읽어야 하는 경우.
  - [Tiếng Việt]: Khi việc đọc một phạm vi dữ liệu cụ thể đòi hỏi phải quét qua quá nhiều khối đĩa vật lý.

---

### 3.2. 반정규화의 4대 기법 (4 Kỹ thuật Phi chuẩn hóa chính)

| 기법 (Phương pháp) | 세부 기법 (Kỹ thuật chi tiết) | 설명 및 목적 (Mục đích tối ưu) |
|---|---|---|
| **테이블 통합**<br>(Gộp bảng) | • 1:1 관계 테이블 통합<br>• 1:N 관계 테이블 통합<br>• 슈퍼/서브타입 테이블 통합 | • 조인(Join) 연산을 완전히 제거하여 단일 I/O로 데이터 인출.<br>• 단, 테이블 크기가 비대해져 Full Scan 비용이 증가할 위험 존재. |
| **테이블 분할**<br>(Chia bảng) | • **수평 분할 (Horizontal)**: 레코드(Row) 단위 분할<br>• **수직 분할 (Vertical)**: 속성(Column) 단위 분할 | • **수평 분할**: 특정 기간/지역별 분할로 I/O 범위 국소화.<br>• **수직 분할**: 자주 조회되는 속성과 대용량 TEXT/LOB 컬럼 분리. |
| **중복 테이블 추가**<br>(Thêm bảng trùng lặp) | • **집계 테이블 (Aggregation Table)**<br>• **진행 테이블 (Progress Table)**<br>• **특정 부분 테이블 (Subset Table)** | • 매번 집계 함수(SUM, COUNT)를 계산하지 않고 사전 계산값 유지.<br>• 서버 작업 부하를 경감시키고 대시보드 조회 속도 극대화. |
| **중복 속성 추가**<br>(Thêm cột trùng lặp) | • 타 테이블 속성 복사<br>• 파생 속성(Derived Column) 추가<br>• PK 속성의 외래키 통합 | • 단 1~2개 컬럼을 읽기 위해 조인하는 비효율 원천 차단.<br>• 갱신 이상(Update Anomaly) 발생 가능성이 가장 높은 지점. |

#### 수평 분할 vs 수직 분할 심층 비교 (Phân vùng ngang vs Phân vùng dọc)

- **수평 분할 (Horizontal Partitioning / 레코드 분할):**
  - [한국어]: 레코드(Row)가 너무 많아 특정 연도, 지점, 상태값(예: 최근 3개월 데이터 vs 과거 보관 데이터)을 기준으로 행을 나누는 방식.
  - [Tiếng Việt]: Chia bảng theo hàng (Row) dựa trên các tiêu chí như khoảng thời gian, chi nhánh, trạng thái dữ liệu (ví dụ: dữ liệu 3 tháng gần nhất tách riêng khỏi kho lưu trữ lịch sử).
- **수직 분할 (Vertical Partitioning / 컬럼 분할):**
  - [한국어]: 컬럼(Column) 수가 너무 많거나, 자주 사용되는 컬럼과 거의 쓰이지 않는 LOB/TEXT 컬럼(예: 프로필 이미지, 장문 소개글)을 분리하여 디스크 블록 당 저장 레코드 수를 늘리는 방식.
  - [Tiếng Việt]: Chia bảng theo cột (Column) khi bảng có quá nhiều thuộc tính hoặc chứa các trường dữ liệu dung lượng lớn (LOB/TEXT), giúp tăng mật độ bản ghi trên mỗi khối đĩa, tối ưu bộ đệm (Buffer Cache).

---

### 3.3. 반정규화의 위험성과 트레이드오프 (Rủi ro & Đánh đổi)

- [한국어]: **과도한 반정규화(Excessive Denormalization)**는 성능을 향상시키기는커녕 다음과 같은 심각한 부작용을 초래한다:
  1. **데이터 이상 현상 재발:** 중복 데이터로 인해 삽입, 삭제, 갱신 이상이 다시 발생할 수 있음.
  2. **데이터 일관성 저하(Inconsistency):** 한 쪽 테이블만 수정되고 중복 속성이 갱신되지 않으면 데이터 간 불일치 초래.
  3. **저장 공간 낭비 및 CUD 성능 저하:** 데이터 INSERT/UPDATE/DELETE 시 여러 테이블과 중복 컬럼을 동시에 갱신해야 하므로 쓰기 성능이 급격히 저하됨.
- [Tiếng Việt]: **Phi chuẩn hóa quá đà** không những không cải thiện được hiệu năng mà còn gây ra các hệ lụy kỹ thuật nghiêm trọng:
  1. **Tái phát dị thường dữ liệu:** Dư thừa dữ liệu làm tái xuất hiện các dị thường thêm, xóa, sửa.
  2. **Suy giảm tính nhất quán:** Khi dữ liệu ở bảng chính thay đổi mà trường trùng lặp chưa kịp cập nhật, hệ thống rơi vào trạng thái xung đột dữ liệu.
  3. **Tốn bộ nhớ & Chậm thao tác ghi (CUD):** Mọi thao tác INSERT/UPDATE/DELETE phải đồng bộ trên nhiều bảng và cột trùng lặp, khiến tốc độ ghi giảm mạnh.

---

### 3.4. 쿼리 성능 최적화와 옵티마이저 (Tối ưu hóa Truy vấn & Optimizer)

- [한국어]: **옵티마이저(Optimizer)**는 사용자가 작성한 SQL 문을 가장 빠르고 효율적으로 처리하기 위해 DBMS 내부에서 최소 비용의 실행 경로(Execution Plan)를 결정하는 핵심 엔진이다.
- [Tiếng Việt]: **Bộ tối ưu hóa (Optimizer)** là động cơ cốt lõi trong DBMS chịu trách nhiệm phân tích câu lệnh SQL của người dùng và thiết lập lộ trình thực thi (Execution Plan) có chi phí tài nguyên thấp nhất và tốc độ xử lý nhanh nhất.

```
[ SQL 문 작성 ] ---> [ 구문 분석 (Parser) ] ---> [ 옵티마이저 (Optimizer) ] ---> [ 실행 계획 (Execution Plan) ] ---> [ 실행 엔진 ]
                                                     │
                                   ┌─────────────────┴─────────────────┐
                                   ▼                                   ▼
                           규칙 기반 (RBO)                     비용 기반 (CBO)
```

| 구분 (Tiêu chí) | RBO (규칙 기반 옵티마이저 / Rule-Based) | CBO (비용 기반 옵티마이저 / Cost-Based) |
|---|---|---|
| **최적화 기준** | 정해진 **규칙의 우선순위(1~15순위)**에 따라 경로 결정 | **예상되는 자원 소모 비용(Cost)**을 계산하여 최소 비용 선택 |
| **핵심 의존성** | **개발자의 SQL 작성 방식** 및 인덱스 구조에 절대적 의존 | **통계 정보(Statistics Info)**의 정확도와 DBMS 계산 모델에 의존 |
| **비용 계산 여부** | 연산 비용(I/O, CPU)을 전혀 고려하지 않음 | 디스크 I/O 횟수, CPU 사용량, 메모리 점유율을 종합 예측 |
| **예측 가능성** | 실행 계획이 고정되어 있어 예측이 매우 쉬움 | 데이터 규모와 분포도(Histogram)에 따라 동적으로 변동 |

- **APM (Application Performance Management):**
  - [한국어]: 애플리케이션의 성능 병목 현상을 실시간 모니터링하여 병목 쿼리(Slow Query), 커넥션 누수(Connection Leak), 트랜잭션 지연을 감지하는 도구이다.
  - [Tiếng Việt]: Công cụ quản lý hiệu năng ứng dụng, theo dõi theo thời gian thực để phát hiện các câu truy vấn thắt cổ chai (Slow Query), rò rỉ kết nối (Connection Leak) và tắc nghẽn giao dịch.

---

## 4. 실전 시험 대비 / 함정 분석 (Bẫy đề thi & Trắc nghiệm)

### 함정 포인트 (Trap Points)
1. **Bẫy định nghĩa RBO vs CBO:**
   - Đề hỏi: *"Bộ tối ưu hóa nào sử dụng thông tin thống kê (통계 정보) và phân bố dữ liệu để lập kế hoạch?"* $\rightarrow$ Bắt buộc chọn **CBO (비용 기반 옵티마이저)**. Nếu chọn RBO là sai.
   - Đề hỏi: *"Bộ tối ưu nào đưa ra kế hoạch thực thi phụ thuộc hoàn toàn vào thứ tự viết câu lệnh và sự hiểu biết quy tắc của lập trình viên?"* $\rightarrow$ Bắt buộc chọn **RBO (규칙 기반 옵티마이저)**.
2. **Bẫy mục đích 반정규화:**
   - Khẳng định: *"Phi chuẩn hóa luôn luôn làm tăng hiệu năng toàn diện của hệ thống trong mọi trường hợp"* $\rightarrow$ **SAI**. Phi chuẩn hóa chỉ tăng tốc độ ĐỌC (SELECT), nhưng làm GIẢM hiệu năng GHI (INSERT, UPDATE, DELETE) và tăng nguy cơ bất nhất quán dữ liệu.
3. **Phân biệt 수평 분할 vs 수직 분할:**
   - Chia theo dòng (Row / Record) $\rightarrow$ **수평 분할 (Horizontal Partitioning)**.
   - Chia theo cột (Column / Attribute) $\rightarrow$ **수직 분할 (Vertical Partitioning)**.

---

## 5. 복습 체크리스트 (Bảng kiểm tra ôn tập)

- [ ] Định nghĩa được 반정규화 và giải thích tại sao nó là một sự đánh đổi giữa hiệu năng và tính toàn vẹn.
- [ ] Phân biệt rõ ràng 4 nhóm kỹ thuật: 테이블 통합, 테이블 분할, 중복 테이블 추가, 중복 속성 추가.
- [ ] Giải thích được sự khác biệt cốt lõi giữa 수평 분할 (Row) và 수직 분할 (Column).
- [ ] Trình bày được bản chất của 2 cơ chế 옵티마이저: RBO (Rule-Based) và CBO (Cost-Based).
- [ ] Nhận biết vai trò của công cụ APM trong việc phát hiện 병목 쿼리 (Slow Query).
