# 11. 분산 데이터베이스와 4대 투명성 (Cơ Sở Dữ Liệu Phân Tán và 4 Tính Chất Trong Suốt)

## 1. 개요 및 학습 목표 (Tổng quan & Mục tiêu học tập)

- [한국어]: **분산 데이터베이스(Distributed Database)**는 논리적으로는 하나의 일관된 시스템이지만 물리적으로는 네트워크를 통해 여러 지역의 사이트(Site)에 분산되어 있는 데이터베이스 시스템이다. 사용자가 물리적 분산 구조를 의식하지 않고 편리하게 데이터에 접근할 수 있도록 보장하는 **4대 투명성(Transparency)**과 데이터 무결성을 보장하는 **2단계 커밋(2-Phase Commit, 2PC)** 규약이 시스템 구축의 핵심을 이룬다.
- [Tiếng Việt]: **Cơ sở dữ liệu phân tán (Distributed Database / 분산 데이터베이스)** là hệ thống mà về mặt logic thuộc về một hệ thống nhất quán duy nhất nhưng về mặt vật lý lại được lưu trữ phân tán trên nhiều trạm (Site) kết nối qua mạng viễn thông. Để người dùng có thể thao tác tiện lợi mà không cần bận tâm đến kiến trúc vật lý bên dưới, hệ thống bắt buộc phải thỏa mãn **Bộ tứ tính chất trong suốt (4 Transparencies / 4대 투명성)** và áp dụng giao thức **Cam kết 2 pha (2-Phase Commit / 2PC)** để bảo toàn tính toàn vẹn giao dịch toàn cục.

### 학습 목표 (Mục tiêu kiến thức)
1. **분산 데이터베이스의 개념과 3대 구성요소 (Bản chất CSDL phân tán):** Nắm vững triết lý "Logic đơn nhất, Vật lý phân tán" (`논리적 단일, 물리적 분산`), vai trò của Bộ xử lý phân tán (`분산 처리기`), CSDL phân tán (`분산 데이터베이스`), và Mạng truyền thông (`통신 네트워크`).
2. **분산 데이터베이스 4대 투명성 (4 tính chất trong suốt sống còn):** Định nghĩa và nhận diện chính xác qua đề thi: Trong suốt vị trí (`위치 투명성`), Trong suốt nhân bản (`중복/복제 투명성`), Trong suốt đồng thời (`병행 투명성`), và Trong suốt sự cố (`장애 투명성`).
3. **데이터 분할 3대 기법 (3 phương pháp phân mảnh dữ liệu):** Phân biệt Phân mảnh ngang (`수평 분할` - dùng phép Select $\sigma$), Phân mảnh dọc (`수직 분할` - dùng phép Project $\pi$ kèm PK), và Phân mảnh hỗn hợp (`혼합 분할`).
4. **글로벌 트랜잭션과 2단계 커밋 (Giao dịch toàn cục & Giao thức 2PC):** Phân tích cơ chế cam kết nguyên tử gồm Pha chuẩn bị (`준비 단계 / Prepare Phase`) và Pha cam kết (`커밋 단계 / Commit Phase`).
5. **엔터프라이즈 스토리지 아키텍처 (Kiến trúc lưu trữ doanh nghiệp):** So sánh toàn diện DAS (cáp riêng trực tiếp), NAS (chia sẻ tệp qua Ethernet), SAN (mạng cáp quang chuyên dụng Block-level), và CAP/BASE theorem.

---

## 2. 개념 연결 및 브리지 (Cầu nối kiến thức)

- **Từ đâu (Origin - Xuất phát điểm):**
  - [한국어]: 이전 [10-view-index-system-catalog-va-ma-tran-crud.md](10-view-index-system-catalog-va-ma-tran-crud.md)에서 우리는 단일 DBMS 상에서의 뷰, 인덱스 물리 구조, CRUD 매트릭스를 통한 부하 분석을 학습했습니다.
  - [Tiếng Việt]: Ở bài học trước, chúng ta đã nghiên cứu các cấu trúc tối ưu truy cập trên một máy chủ đơn lẻ bao gồm View, Index và phân tích tải giao dịch qua Ma trận CRUD.
- **Đang giải quyết gì (Current Problem - Vấn đề bài học giải quyết):**
  - [한국어]: 단일 서버의 물리적 한계(CPU, 디스크 용량, 네트워크 I/O 병목)를 극복하고 지리적으로 분산된 대규모 엔터프라이즈 환경을 지원하기 위해, 물리적 노드를 분산시키면서도 사용자에게 단일 뷰를 제공하는 **분산 데이터베이스의 투명성(Transparency)**과 **동기화 프로토콜**을 정립합니다.
  - [Tiếng Việt]: Nhằm vượt qua giới hạn phần cứng của một máy chủ độc lập và phục vụ các hệ thống phân tán địa lý lớn, bài học này giải quyết bài toán thiết kế **Cơ sở dữ liệu phân tán** với **4 tính chất trong suốt** và các giao thức đồng thuận giao dịch toàn cục.
- **Dùng đi đâu (Forward Handoff - Chuyển tiếp tương lai):**
  - [한국어]: 본 장에서 다룬 물리적 노드 분산 및 스토리지 구조는 다음 [12-phan-vung-du-lieu-va-bao-mat-ma-hoa-csdl.md](12-phan-vung-du-lieu-va-bao-mat-ma-hoa-csdl.md)에서 대용량 단일 테이블을 분할하는 파티셔닝(Partitioning) 기법과 네트워크 전송 데이터의 암호화 및 보안 통제 체계로 확장됩니다.
  - [Tiếng Việt]: Kiến trúc phân tán và lưu trữ này sẽ kết nối trực tiếp với kỹ thuật phân vùng bảng (Partitioning) và cơ chế mã hóa, bảo mật đa tầng của CSDL ở bài học tiếp theo.

---

## 3. 핵심 이론 및 용어 대조 (Lý thuyết cốt lõi & Đối chiếu thuật ngữ)

### 3.1. 분산 데이터베이스의 개념과 3대 구성요소 (Bản chất CSDL Phân tán)

- [한국어]: **분산 데이터베이스(Distributed Database)**는 지리적으로 분산된 다수의 컴퓨터 시스템에 데이터베이스를 분산 저장하고, 이를 통신 네트워크로 연결하여 논리적으로는 하나의 데이터베이스처럼 운용하는 시스템이다.
  - **핵심 특징:** **논리적 단일성(Logical Unity)**과 **물리적 분산성(Physical Distribution)**의 결합.
- [Tiếng Việt]: **Cơ sở dữ liệu phân tán** là hệ thống lưu trữ CSDL phân tán trên nhiều máy tính đặt ở các vị trí địa lý khác nhau kết nối qua mạng viễn thông, nhưng được quản lý sao cho người dùng cảm thấy như một hệ thống logic duy nhất.

```
                  [ 통신 네트워크 (Mạng truyền thông) ]
                       │                   │
         ┌─────────────┴────────┐ ┌────────┴────────────┐
         ▼                      ▼ ▼                     ▼
  [ 사이트 1 (Hà Nội) ]                 [ 사이트 2 (TP. Hồ Chí Minh) ]
  • 분산 처리기 (Processor)             • 분산 처리기 (Processor)
  • 분산 데이터베이스 (DB)              • 분산 데이터베이스 (DB)
  • 지역 자치성 (Local Autonomy)         • 지역 자치성 (Local Autonomy)
```

- **3대 핵심 구성요소:**
  1. **분산 처리기 (Distributed Processor):** 각 지역 사이트에 위치하여 자체적인 CPU 연산 및 DBMS 관리 기능을 수행하는 독립적 컴퓨터 시스템.
  2. **분산 데이터베이스 (Distributed Database):** 각 지역 사이트의 물리적 스토리지에 분산되어 저장된 데이터 파일 집합.
  3. **통신 네트워크 (Communication Network):** 지리적으로 분리된 분산 처리기들을 유기적으로 결합하는 초고속 전송망.

---

### 3.2. 분산 데이터베이스의 4대 투명성 (Bộ tứ Tính Chất Trong Suốt)

- [한국어]: **투명성(Transparency)**이란 사용자가 시스템 내부의 복잡한 물리적 구현이나 분산 구조를 알 필요 없이, 마치 자신만의 단일 로컬 데이터베이스를 사용하는 것처럼 편리하게 작업할 수 있도록 보장하는 특성이다.

| 투명성 (Tính trong suốt) | 영문 / 한글 명칭 | 기술적 핵심 정의 (Định nghĩa kỹ thuật) | 기출 지문 핵심 키워드 (Dấu hiệu nhận diện đề thi) |
|---|---|---|---|
| **Trong suốt vị trí** | **Location Transparency**<br>`위치 투명성` | 데이터가 물리적으로 어느 서버(사이트, 도시, IP 주소)에 저장되어 있는지 알 필요 없이, **데이터의 논리적 명칭만으로 접근 가능**함. | • *"데이터의 실제 물리적 저장 위치를 알 필요 없음"*<br>• *"논리적 이름만으로 질의 수행"* |
| **Trong suốt nhân bản** | **Replication Transparency**<br>`중복 / 복제 투명성` | 시스템 성능 및 가용성을 위해 동일한 데이터가 여러 사이트에 중복 저장되어 있더라도, 사용자는 **오직 하나의 단일 데이터만 존재하는 것처럼 인식**함. | • *"동일 데이터가 여러 곳에 중복되어 있어도 하나의 데이터로 인식"*<br>• *"시스템이 중복 데이터의 일관성을 자동 갱신"* |
| **Trong suốt đồng thời** | **Concurrency Transparency**<br>`병행 투명성` | 여러 사이트에서 다수의 트랜잭션이 동시에 실행되더라도, 상호 간섭 없이 **각각 독립적으로 올바르게 수행되어 직렬성이 보장**됨. | • *"다수의 트랜잭션이 동시 실행되어도 결과에 왜곡이 없음"*<br>• *"트랜잭션 간 간섭 배제"* |
| **Trong suốt sự cố** | **Failure Transparency**<br>`장애 투명성` | 특정 사이트의 하드웨어 고장, 네트워크 단절, DBMS 오류가 발생하더라도, **전체 글로벌 트랜잭션의 원자성과 무결성이 보존**됨. | • *"특정 사이트나 네트워크 장애에도 트랜잭션 정확 처리"*<br>• *"장애 발생 시 자동 복구 및 원자성 유지"* |

---

### 3.3. 데이터 분할 3대 기법 (Data Fragmentation)

- [한국어]: 테이블 전체를 단일 사이트에 두지 않고 논리적 조건에 따라 쪼개어 분산 배치하는 기법이다.

| 분할 방식 (Kỹ thuật) | 한글 명칭 | 분할 기준 및 관계대수 (Đại số quan hệ) | 특징 및 적용 사례 |
|---|---|---|---|
| **수평 분할** | `수평 분할`<br>(Horizontal) | **행(Row, 튜플) 단위 분할**<br>• **관계대수 셀렉트($\sigma$) 연산** 적용 | • 지사별(서울지사, 부산지사) 데이터 분리.<br>• 각 사이트는 동일한 속성 스키마를 공유함. |
| **수직 분할** | `수직 분할`<br>(Vertical) | **열(Column, 속성) 단위 분할**<br>• **관계대수 프로젝트($\pi$) 연산** 적용 | • 기본 정보와 대용량/민감 정보 분리.<br>• 원래 테이블로 무손실 복원하기 위해 **모든 분할 조각에 기본키(PK)가 포함**되어야 함. |
| **혼합 분할** | `혼합 분할`<br>(Hybrid) | 수평 분할과 수직 분할의 조합 | • 대규모 글로벌 시스템에서 행과 열을 동시에 격자형으로 분할. |

---

### 3.4. 2단계 커밋 프로토콜 (2-Phase Commit Protocol, 2PC)

- [한국어]: 분산 트랜잭션에 참여하는 모든 노드(Participant)들이 하나의 트랜잭션에 대해 원자적(All or Nothing)으로 커밋되거나 롤백되도록 조율하는 합의 프로토콜이다.
  - **조정자(Coordinator):** 분산 트랜잭션을 총괄 지휘하는 마스터 노드.
  - **참여자(Participant):** 실제 데이터 갱신을 수행하는 각 지역 사이트 노드.

```
[ 조정자 (Coordinator) ]                       [ 참여자 (Participants) ]
          │                                              │
          │ ── 1. 준비 요청 (Prepare / Can you commit?) ──> │ (1단계: 준비 단계)
          │ <── 2. 준비 완료 응답 (Vote Yes / Ready) ─────── │
          │                                              │
          │ ── 3. 최종 확정 (Global Commit / Abort) ──────> │ (2단계: 커밋 단계)
          │ <── 4. 완료 확인 (Acknowledge) ──────────────── │
```

1. **1단계 - 준비 단계 (Prepare Phase):** 조정자가 모든 참여자에게 트랜잭션 커밋 준비를 요청(`Prepare`). 참여자들은 로컬 로그에 기록 후 준비 완료(`Ready`) 또는 실패(`Abort`) 신호를 회신.
2. **2단계 - 커밋 단계 (Commit Phase):**
   - 모든 참여자가 `Ready`를 보낸 경우 $\rightarrow$ 조정자가 **글로벌 커밋(Global Commit)** 명령 전송.
   - 단 하나라도 `Abort`를 보내거나 응답 타임아웃 발생 시 $\rightarrow$ 조정자가 **글로벌 롤백(Global Abort)** 명령 전송.

---

### 3.5. 엔터프라이즈 스토리지 아키텍처 (DAS vs NAS vs SAN)

| 구분 (Kiến trúc) | DAS (Direct Attached Storage) | NAS (Network Attached Storage) | SAN (Storage Area Network) |
|---|---|---|---|
| **연결 방식** | 전용 케이블(SATA, SAS)로 서버에 직접 결합 | 일반 LAN(이더넷) 네트워크에 연결 | 광 채널(FC Switch) 전용 고속 네트워크 |
| **데이터 접근 수준** | 블록 레벨 (Block-level) | **파일 레벨 (File-level)** (NFS, CIFS) | **블록 레벨 (Block-level)** (SCSI over FC) |
| **핵심 장점** | 속도 빠름, 설치 간단, 비용 저렴 | 다수 서버 간 파일 공유 용이 | 초고속 전송, 대용량 트랜잭션, 고가용성 |
| **주요 단점** | **다른 서버와 직접 공유 불가**, 확장성 제한 | 네트워크 트래픽 증가 시 병목 발생 | **구축 및 유지보수 비용 극히 고가**, 관리 복잡 |
| **DB 적용도** | 소규모 독립형 DB | 단순 백업 및 비정형 파일 공유 | **대규모 엔터프라이즈 핵심 RDBMS** |

- **CAP 정리 (CAP Theorem - Eric Brewer):**
  - 분산 시스템은 **일관성(Consistency)**, **가용성(Availability)**, **분할 허용성(Partition Tolerance)**의 3대 특성 중 **동시에 최대 2가지만 보장**할 수 있다.
  - 네트워크 단절이 발생할 수 있는 실제 분산 환경에서는 P(분할 허용성)를 기본 전제하므로, 현실적인 선택은 **CP 시스템(일관성 우선 - HBase, MongoDB)** 또는 **AP 시스템(가용성 우선 - Cassandra, DynamoDB)**이 된다.

---

## 4. 실전 시험 대비 / 함정 분석 (Bẫy đề thi & Trắc nghiệm)

### 함정 포인트 (Trap Points)
1. **Bẫy 4대 투명성 매칭 (4 Transparencies Mapping):**
   - Đề bài: *"Người dùng chỉ cần gõ tên logic của bảng mà không cần quan tâm bảng đó đặt tại máy chủ nào"* $\rightarrow$ Bắt buộc chọn **위치 투명성 (Location Transparency)**. Nếu chọn 분할 투명성 là sai.
   - Đề bài: *"Dữ liệu được nhân bản ở nhiều nơi nhưng người dùng chỉ cảm nhận có 1 bản duy nhất"* $\rightarrow$ Bắt buộc chọn **중복/복제 투명성 (Replication Transparency)**.
2. **Bẫy đại số quan hệ trong phân mảnh (Fragmentation Operators):**
   - 수평 분할 (Horizontal): Chia theo dòng $\rightarrow$ Phép toán **Select ($\sigma$)**.
   - 수직 분할 (Vertical): Chia theo cột $\rightarrow$ Phép toán **Project ($\pi$)**. Luôn phải mang theo Khóa chính (PK) để Join hoàn lại dữ liệu gốc.
3. **Bẫy NAS vs SAN:**
   - Đề hỏi: *"Kiến trúc lưu trữ nào sử dụng mạng cáp quang chuyên dụng (FC) và truy xuất ở cấp độ khối (Block-level)?"* $\rightarrow$ Đáp án: **SAN (Storage Area Network)**. Nếu chọn NAS là sai (NAS dùng mạng Ethernet và truy xuất cấp độ tệp File-level).
4. **Bẫy 2PC (2단계 커밋):**
   - Khẳng định: *"Trong 2PC, chỉ cần quá bán (đa số) các nút đồng ý thì 조정자 sẽ phát lệnh Global Commit"* $\rightarrow$ **SAI**. 2PC yêu cầu **100% tất cả các nút phải đồng ý (`All-Ready`)**, chỉ cần 1 nút thất bại là lập tức Rollback toàn bộ.

---

## 5. 복습 체크리스트 (Bảng kiểm tra ôn tập)

- [ ] Định nghĩa được 분산 데이터베이스 (논리적 단일, 물리적 분산).
- [ ] Phân biệt và giải thích đúng 4 tính chất trong suốt: 위치, 중복/복제, 병행, 장애 투명성.
- [ ] Phân biệt được 수평 분할 (Select $\sigma$) và 수직 분할 (Project $\pi$).
- [ ] Trình bày được 2 bước của 2PC: chuẩn bị (Prepare) và 커밋 (Commit), vai trò của 조정자 và 참여자.
- [ ] So sánh 3 kiến trúc lưu trữ DAS, NAS, SAN theo phương thức kết nối và cấp độ truy cập (File vs Block).
- [ ] Trình bày định lý CAP và sự đánh đổi giữa 일관성(C) và 가용성(A).
