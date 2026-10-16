# 08. 트랜잭션, ACID 특성과 동시성 제어 (Giao Dịch, Đặc Tính ACID và Điều Khiển Đồng Thời)

## 1. 개요 및 학습 목표 (Tổng quan & Mục tiêu học tập)

- [한국어]: **트랜잭션(Transaction)**은 데이터베이스의 상태를 변환시키는 하나의 논리적 기능을 수행하기 위한 작업의 단위 또는 한꺼번에 모두 수행되어야 할 일련의 연산들을 의미한다. 데이터 무결성을 보장하기 위해 **ACID 특성**을 엄격히 준수해야 하며, 다중 사용자 환경에서 발생하는 이상 현상을 방지하기 위해 **병행 제어(Concurrency Control)** 및 **회복(Recovery)** 기법이 적용된다.
- [Tiếng Việt]: **Giao dịch (Transaction / 트랜잭션)** là đơn vị thao tác logic cơ bản hoặc một tập hợp các phép toán bắt buộc phải thực thi trọn vẹn nhằm biến đổi trạng thái của cơ sở dữ liệu. Nhằm đảm bảo tính toàn vẹn dữ liệu, giao dịch phải tuân thủ nghiêm ngặt **bộ 4 đặc tính ACID**, đồng thời áp dụng các cơ chế **Điều khiển đồng thời (Concurrency Control / 병행 제어)** và **Phục hồi (Recovery / 회복)** để ngăn chặn các dị thường trong môi trường đa người dùng.

### 학습 목표 (Mục tiêu kiến thức)
1. **트랜잭션의 개념과 ACID 4대 특성 (Khái niệm & 4 đặc tính ACID):** Nắm vững bản chất đơn vị thao tác logic (`논리적 작업 단위`), cơ chế "All or Nothing" của tính nguyên tử (`원자성`), tính nhất quán (`일관성`), tính cô lập (`격리성/독립성`), và tính bền vững (`영속성`).
2. **트랜잭션 5대 상태 전이 (5 trạng thái vòng đời giao dịch):** Phân tích sơ đồ chuyển đổi trạng thái: Đang hoạt động (`활동 / Active`), Hoàn thành một phần (`부분 완료 / Partially Committed`), Hoàn tất (`완료 / Committed`), Thất bại (`실패 / Failed`), và Bị hủy bỏ (`철회 / Aborted`).
3. **병행 제어 미수행 시 4대 문제점 (4 sự cố khi thiếu kiểm soát đồng thời):** Nhận diện chính xác Mất cập nhật (`갱신 분실`), Mâu thuẫn dữ liệu (`모순성`), Hoàn tác dây chuyền (`연쇄 복귀`), và Đọc rác (`비완료 의존성 / Dirty Read`).
4. **병행 제어 주요 기법 (Các kỹ thuật kiểm soát đồng thời then chốt):** So sánh cơ chế Khóa (`로킹 / Locking - S-Lock vs X-Lock`), đánh đổi đơn vị khóa (`로킹 단위`), Giao thức khóa 2 pha (`2PL`), Gán mốc thời gian (`타임스탬프`), và Kiểm soát lạc quan (`낙관적 검증`).
5. **데이터베이스 회복 기법 (Kỹ thuật phục hồi CSDL):** Phân biệt cơ chế Redo/Undo trong Cập nhật trì hoãn (`연기 갱신`), Cập nhật tức thì (`즉각 갱신`), Điểm kiểm tra (`검사점 / Checkpoint`), và Phân trang bóng (`그림자 페이징`).

---

## 2. 개념 연결 및 브리지 (Cầu nối kiến thức)

- **Từ đâu (Origin - Xuất phát điểm):**
  - [한국어]: 이전 [07-phi-chuan-hoa-va-toi-uu-hieu-nang-truy-van.md](07-phi-chuan-hoa-va-toi-uu-hieu-nang-truy-van.md)에서 우리는 성능 향상을 위한 반정규화 기법과 옵티마이저의 실행 계획을 학습했습니다.
  - [Tiếng Việt]: Ở bài học trước, chúng ta đã nghiên cứu các kỹ thuật phi chuẩn hóa để tăng tốc truy vấn và cơ chế lập kế hoạch thực thi của Optimizer.
- **Đang giải quyết gì (Current Problem - Vấn đề bài học giải quyết):**
  - [한국어]: 실무 운영 환경에서는 수많은 사용자가 동시에 데이터를 조회하고 수정합니다. 이때 데이터가 엉키거나 시스템 장애 시 데이터가 유실되지 않도록 보장하는 **트랜잭션의 원자적 관리(ACID)**와 **병행 제어(Concurrency Control)** 메커니즘을 규명합니다.
  - [Tiếng Việt]: Trong môi trường sản xuất thực tế, hàng ngàn người dùng cùng truy cập và sửa đổi dữ liệu đồng thời. Bài học này giải quyết bài toán chống xung đột, chống mất mát dữ liệu khi có sự cố thông qua cơ chế quản trị giao dịch nguyên tử **ACID** và các giao thức **Điều khiển đồng thời (Concurrency Control)**.
- **Dùng đi đâu (Forward Handoff - Chuyển tiếp tương lai):**
  - [한국어]: 트랜잭션의 무결성 개념은 다음 [09-ngon-ngu-sql-ddl-dml-dcl-va-procedural-sql.md](09-ngon-ngu-sql-ddl-dml-dcl-va-procedural-sql.md)에서 DDL, DML과 함께 트랜잭션을 직접 제어하는 TCL(COMMIT, ROLLBACK) 및 저장 프로시저(Stored Procedure)의 구문 문법으로 구체화됩니다.
  - [Tiếng Việt]: Nguyên lý giao dịch này sẽ được hiện thực hóa trực tiếp bằng các câu lệnh SQL điều khiển giao dịch TCL (COMMIT, ROLLBACK) và thủ tục lưu trữ (Stored Procedure) ở bài học tiếp theo.

---

## 3. 핵심 이론 및 용어 대조 (Lý thuyết cốt lõi & Đối chiếu thuật ngữ)

### 3.1. 트랜잭션의 정의와 ACID 4대 특성 (Khái niệm & Bộ 4 đặc tính ACID)

- [한국어]: **트랜잭션(Transaction)**은 데이터베이스에서 하나의 논리적 기능을 수행하기 위한 작업의 단위(`논리적 작업 단위 / Logical Unit of Work`)이다.
- [Tiếng Việt]: **Giao dịch (Transaction)** là đơn vị thao tác logic cơ bản thực hiện một chức năng nghiệp vụ hoàn chỉnh làm biến đổi trạng thái của cơ sở dữ liệu.

| 특성 (Đặc tính) | 영문 / 한글 명칭 | 기술적 핵심 정의 (Định nghĩa kỹ thuật) | 보장 메커니즘 (Cơ chế bảo đảm) |
|---|---|---|---|
| **Tính nguyên tử** | **Atomicity**<br>`원자성` | **"All or Nothing"** (모두 반영되거나 전혀 반영되지 않음). 트랜잭션 내의 모든 연산이 완벽히 실행(Commit)되거나, 오류 시 완전히 취소(Rollback)되어야 함. | 회복 관리자 (Recovery Manager), 로그(Log/Journal), Undo 연산 |
| **Tính nhất quán** | **Consistency**<br>`일관성` | 트랜잭션이 성공적으로 완료되면 언제나 모순 없이 일관성 있는 데이터베이스 상태를 보존해야 함 (도메인 제약조건, 외래키 무결성 유지). | 무결성 제약조건 엔진 (Integrity Engine), 트리거 |
| **Tính cô lập** | **Isolation**<br>`격리성 / 독립성` | 둘 이상의 트랜잭션이 병행 실행될 때, 어느 하나의 트랜잭션도 다른 트랜잭션의 중간 연산 결과에 끼어들거나 간섭할 수 없음. | 병행 제어 기법 (로킹, 타임스탬프, 격리성 수준 설정) |
| **Tính bền vững** | **Durability**<br>`영속성` | 성공적으로 완료(Commit)된 트랜잭션의 결과는 시스템 장애(정전, OS 다운)가 발생하더라도 영구적으로 반영되어 보존되어야 함. | 비휘발성 저장소, Redo 로그 기록, Checkpoint |

---

### 3.2. 트랜잭션의 5대 상태 전이 (Sơ đồ 5 trạng thái vòng đời)

```
       [ 활동 (Active) ] ───────────┐
              │                     │
              ▼                     ▼
     [ 부분 완료 (Partially     [ 실패 (Failed) ]
        Committed) ]                │
              │                     ▼
              ├──────────────> [ 철회 (Aborted) ]
              ▼
       [ 완료 (Committed) ]
```

- **1. 활동 (Active):**
  - [한국어]: 트랜잭션이 시작되어 명령어를 순차적으로 실행 중인 초기 상태.
  - [Tiếng Việt]: Trạng thái ban đầu khi giao dịch khởi động và đang trong quá trình thực thi các câu lệnh đọc/ghi.
- **2. 부분 완료 (Partially Committed):**
  - [한국어]: 트랜잭션의 마지막 연산(SQL 문)까지 모두 실행을 마쳤으나, 최종 커밋(COMMIT) 연산이 디스크에 아직 완전히 기록되지 않은 상태.
  - [Tiếng Việt]: Trạng thái ngay sau khi câu lệnh cuối cùng đã chạy xong trong bộ đệm RAM nhưng thao tác COMMIT vật lý xuống đĩa cứng chưa hoàn tất.
- **3. 완료 (Committed):**
  - [한국어]: 트랜잭션이 성공적으로 종료되어 변경 내용이 데이터베이스에 안전하게 영구 반영된 상태.
  - [Tiếng Việt]: Trạng thái giao dịch hoàn tất thành công 100%, dữ liệu được ghi an toàn vĩnh viễn lên đĩa.
- **4. 실패 (Failed):**
  - [한국어]: 트랜잭션 실행 도중 오류(하드웨어 장애, 논리적 오류, 데드락 등)가 발생하여 정상 진행이 중단된 상태.
  - [Tiếng Việt]: Trạng thái phát sinh lỗi trong quá trình thực thi khiến giao dịch bị đình chỉ bất thường.
- **5. 철회 (Aborted):**
  - [한국어]: 트랜잭션이 비정상 종료되어 Rollback 연산을 통해 트랜잭션 시작 이전의 원래 상태로 복원된 상태.
  - [Tiếng Việt]: Trạng thái sau khi DBMS thực thi xong thao tác ROLLBACK để hoàn tác mọi biến đổi, đưa CSDL về nguyên trạng ban đầu.

---

### 3.3. 병행 제어 미수행 시 발생하는 4대 문제점 (4 Sự cố khi thiếu kiểm soát đồng thời)

- [한국어]: **병행 제어(Concurrency Control)**는 다중 사용자 환경에서 여러 트랜잭션이 동시에 실행될 때, 데이터베이스의 일관성을 해치지 않도록 트랜잭션의 상호작용을 제어하는 것이다. 이를 수행하지 않으면 다음과 같은 4대 부작용이 발생한다.
- [Tiếng Việt]: **Điều khiển đồng thời (Concurrency Control)** là cơ chế kiểm soát sự tương tác giữa các giao dịch khi chạy song song nhằm bảo toàn tính nhất quán của CSDL. Nếu không kiểm soát đồng thời, hệ thống sẽ gặp 4 thảm họa dữ liệu sau:

| 문제점 (Tên sự cố) | 영문 / 한글 명칭 | 기술적 발생 원인 (Bản chất kỹ thuật) |
|---|---|---|
| **Mất cập nhật** | **Lost Update**<br>`갱신 분실` | 둘 이상의 트랜잭션이 동일한 데이터를 동시에 갱신할 때, 나중에 완료된 트랜잭션이 먼저 갱신한 결과를 덮어써서 이전 갱신이 무효화되는 현상. |
| **Tính mâu thuẫn** | **Inconsistency**<br>`모순성 / 불일치` | 하나의 트랜잭션이 여러 데이터를 수정하는 도중에 다른 트랜잭션이 끼어들어 일부는 수정 전, 일부는 수정 후의 데이터를 읽어 데이터 간 정합성이 깨지는 현상. |
| **Hoàn tác dây chuyền** | **Cascading Rollback**<br>`연쇄 복귀` | 트랜잭션 $T_1$이 수정한 데이터를 트랜잭션 $T_2$가 읽어서 작업을 진행했는데, $T_1$이 실패하여 롤백될 때 $T_2$도 함께 강제 롤백되어야 하는 연쇄 파급 현상. |
| **Đọc rác / Chưa hoàn tất** | **Dirty Read**<br>`비완료 의존성` | 트랜잭션 $T_1$이 작업 중인 미완료 데이터(Commit되지 않은 임시 값)를 다른 트랜잭션 $T_2$가 읽어서 사용하는 현상 ($T_1$이 취소되면 잘못된 값을 참조한 꼴). |

---

### 3.4. 병행 제어 주요 기법 (Các kỹ thuật kiểm soát đồng thời)

#### 1. 로킹 기법 (Locking Mechanism)
- [한국어]: 트랜잭션이 사용할 데이터 항목에 대해 독점권을 확보하는 기법.
  - **공유 락(Shared Lock, S-Lock):** 읽기(Read) 전용 락. 여러 트랜잭션이 동시에 S-Lock을 걸고 읽을 수 있으나, 쓰기는 불가능함.
  - **배타 락(Exclusive Lock, X-Lock):** 읽기/쓰기(Read/Write) 전용 락. 하나의 트랜잭션만 점유 가능하며, 다른 트랜잭션의 접근(읽기·쓰기 모두)을 전면 차단함.

#### 2. 로킹 단위와 트레이드오프 (Đơn vị khóa & Quy luật đánh đổi)
- [한국어]: **로킹 단위(Locking Granularity)**는 한 번에 잠그는 데이터의 크기(데이터베이스 전체, 테이블, 레코드, 속성)를 말한다.

| 로킹 단위 (Đơn vị khóa) | 락의 개수 (Số lượng Lock) | 관리 오버헤드 (Chi phí quản lý) | 병행성 수준 (Tính đồng thời) |
|---|:---:|:---:|:---:|
| **크다 (Đại thể: DB, Table)** | 적다 (Ít) | 가볍다 / 단순함 | **낮다 (Giảm mạnh)** |
| **작다 (Vi thể: Row, Column)** | 많다 (Nhiều) | 무겁다 / 복잡함 | **높다 (Tăng cao)** |

#### 3. 2단계 로킹 규약 (2-Phase Locking Protocol, 2PL)
- [한국어]: 직렬 가능성(Serializability)을 보장하기 위한 대표적 규약.
  - **확장 단계(Growing Phase):** 트랜잭션은 락을 획득(Lock)하기만 하고 해제(Unlock)할 수는 없는 단계.
  - **축소 단계(Shrinking Phase):** 트랜잭션은 락을 해제(Unlock)하기만 하고 새로운 락을 획득할 수는 없는 단계.
  - **핵심 특징:** **직렬성(Serializability)은 보장**되지만, 상호 대기로 인한 **교착 상태(Deadlock)는 방지하지 못함**.

#### 4. 기타 병행 제어 기법 (Timestamp, Validation, MVCC)
- **타임스탬프 순서 (Timestamp Ordering):**
  - [한국어]: 트랜잭션에 시스템 타임스탬프(시작 시간)를 부여하여, 락(Lock) 없이 시간 순서대로 접근을 허용하는 비잠금(Non-locking) 방식. **교착 상태(Deadlock)가 발생하지 않음**.
  - [Tiếng Việt]: Gán nhãn thời gian cho giao dịch và sắp xếp thứ tự xử lý; hoàn toàn không dùng Lock nên **loại trừ nguy cơ bế tắc (Deadlock)**.
- **낙관적 검증 기법 (Optimistic Concurrency Control):**
  - [한국어]: 트랜잭션 수행 중에는 충돌이 없을 것으로 가정하고 자유롭게 처리하다가, 커밋 시점의 유효성 검사 단계(Validation Phase)에서 충돌을 감지하여 롤백하는 기법.
  - [Tiếng Việt]: Kỹ thuật kiểm soát lạc quan; đọc ghi trên bộ đệm cục bộ và chỉ kiểm tra xung đột tại pha thẩm định (Validation phase) trước khi ghi.
- **MVCC (Multi-Version Concurrency Control):**
  - [한국어]: 데이터 갱신 시 기존 데이터를 덮어쓰지 않고 타임스탬프가 매겨진 새 버전을 생성하여, 읽기(Read) 작업과 쓰기(Write) 작업이 서로를 블로킹하지 않도록 지원.
  - [Tiếng Việt]: Điều khiển đồng thời đa phiên bản; tạo bản sao phiên bản cũ giúp thao tác đọc không bao giờ bị khóa bởi thao tác ghi (được PostgreSQL, Oracle sử dụng phổ biến).

---

### 3.5. 데이터베이스 회복 기법 (Kỹ thuật phục hồi CSDL)

- [한국어]: 장애 발생 시 데이터베이스를 트랜잭션 수행 전의 일관된 상태로 되돌리는 기법이다.
  - **REDO (재실행):** 장애 발생 시점 이전에 Commit된 트랜잭션의 변경 내용을 로그를 기반으로 다시 수행하여 영속성을 보장함.
  - **UNDO (취소/원상복구):** 장애 발생 시점에 아직 Commit되지 못한 미완료 트랜잭션의 변경 내용을 취소하여 원자성을 보장함.

| 회복 기법 (Kỹ thuật) | 로그 기록 방식 (Cơ chế Log) | 회복 연산 (Thao tác Recovery) |
|---|---|---|
| **연기 갱신 기법**<br>(Deferred Update) | 트랜잭션이 성공적으로 완료(Commit)될 때까지 데이터베이스 본체에 쓰기를 지연하고 로그에만 기록함. | **REDO만 수행**<br>(Undo 불필요) |
| **즉각 갱신 기법**<br>(Immediate Update) | 트랜잭션 수행 도중이라도 연산 결과를 즉시 데이터베이스에 반영하고 변경 내용을 로그에 기록함. | **REDO와 UNDO 모두 수행** |
| **검사점 기법**<br>(Checkpoint) | 주기적으로 검사점(Checkpoint)을 두어 메모리의 로그 및 버퍼 블록을 디스크로 강제 플러시(Flush). | 장애 시 **가장 최근 Checkpoint** 이후의 트랜잭션만 REDO/UNDO 수행 (회복 시간 단축) |
| **그림자 페이징**<br>(Shadow Paging) | 로그를 사용하지 않고, 현재 페이지 테이블과 장애 복구용 그림자 페이지 테이블 2벌을 유지하여 회복함. | 하드웨어 입출력 오버헤드 존재, 로그 오버헤드는 없음 |

---

## 4. 실전 시험 대비 / 함정 분석 (Bẫy đề thi & Trắc nghiệm)

### 함정 포인트 (Trap Points)
1. **Bẫy trạng thái 부분 완료 (Partially Committed):**
   - Đề bài: *"Trạng thái sau khi toàn bộ các câu lệnh SQL trong giao dịch đã chạy xong nhưng chưa ghi hoàn tất xuống đĩa cứng được gọi là gì?"* $\rightarrow$ Đáp án: **부분 완료 (Partially Committed)**. Rất nhiều thí sinh chọn nhầm là `완료 (Committed)`.
2. **Bẫy 2PL (2단계 로킹 규약):**
   - Khẳng định: *"Giao thức khóa 2 pha (2PL) vừa đảm bảo tính tuần tự (직렬성) vừa ngăn ngừa hoàn toàn Deadlock"* $\rightarrow$ **SAI**. 2PL chỉ đảm bảo 직렬성, nhưng **VẪN CÓ THỂ XẢY RA DEADLOCK (교착상태)**.
3. **Bẫy đơn vị khóa (로킹 단위):**
   - Câu hỏi: *"Khi đơn vị khóa trở nên lớn hơn (ví dụ khóa toàn bộ bảng), chi phí quản lý khóa và mức độ đồng thời thay đổi ra sao?"* $\rightarrow$ **Chi phí quản lý GIẢM, nhưng mức độ đồng thời GIẢM theo**.
4. **Bẫy 연기 갱신 (Deferred Update):**
   - Khẳng định: *"Trong kỹ thuật phục hồi 연기 갱신 기법, khi gặp sự cố hệ thống phải thực hiện cả REDO và UNDO"* $\rightarrow$ **SAI**. Vì 연기 갱신 chỉ ghi vào DB sau khi Commit nên **CHỈ CẦN REDO, KHÔNG BAO GIỜ CẦN UNDO**.

---

## 5. 복습 체크리스트 (Bảng kiểm tra ôn tập)

- [ ] Thuộc lòng 4 đặc tính ACID (원자성, 일관성, 격리성, 영속성) và định nghĩa kỹ thuật của từng đặc tính.
- [ ] Vẽ lại sơ đồ 5 trạng thái giao dịch và phân biệt rõ 부분 완료 với 완료.
- [ ] Phân tích 4 sự cố khi thiếu kiểm soát đồng thời: 갱신 분실, 모순성, 연쇄 복귀, 비완료 의존성.
- [ ] So sánh Shared Lock (S-Lock) và Exclusive Lock (X-Lock).
- [ ] Nắm vững quy luật đánh đổi của 로킹 단위 (Lớn vs Nhỏ).
- [ ] Trình bày 2 pha của 2PL (확장 단계, 축소 단계) và lưu ý về Deadlock.
- [ ] Phân biệt cơ chế REDO và UNDO trong 회복 기법 (연기 갱신 vs 즉각 갱신 vs 검사점).
