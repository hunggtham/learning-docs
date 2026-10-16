# V-모델 테스트 레벨과 테스트 오라클 (Cấp độ kiểm thử V-Model và Test Oracle)

## 학습 목표
- Nắm vững kiến trúc đối xứng của Mô hình chữ V (`V-모델 / V-Model`) và 4 cặp giai đoạn phát triển - kiểm thử đối ứng: Phân tích yêu cầu $\leftrightarrow$ Kiểm thử chấp nhận (`인수 테스트`), Thiết kế hệ thống $\leftrightarrow$ Kiểm thử hệ thống (`시스템 테스트`), Thiết kế chi tiết $\leftrightarrow$ Kiểm thử tích hợp (`통합 테스트`), Lập trình/Cài đặt $\leftrightarrow$ Kiểm thử đơn vị (`단위 테스트`).
- Phân biệt hai hình thức kiểm thử chấp nhận: Alpha Test (`알파 테스트` - trong phòng Lab, có lập trình viên giám sát) và Beta Test (`베타 테스트` - ngoài thực địa, người dùng tự do gửi phản hồi).
- Nắm vững hai chiến lược kiểm thử tích hợp gia tăng (`점진적 통합`): Tích hợp từ trên xuống (`하향식 / Top-down` dùng `테스트 스텁 / Test Stub`) và Tích hợp từ dưới lên (`상향식 / Bottom-up` dùng `테스트 드라이버 / Test Driver`).
- Nắm vững định nghĩa Test Oracle (`테스트 오라클`) và phân biệt 4 loại Test Oracle chuẩn thi: Oracle Chân lý (`참`), Oracle Lấy mẫu (`샘플링`), Oracle Ước lượng (`추정/휴리스틱`), Oracle Nhất quán (`일관성 검사` trong Regression Testing).
- Nắm vững các thành phần của Giàn giáo kiểm thử (`테스트 하네스 / Test Harness`): Driver, Stub, Suite, Script, Mock Object.

## 핵심 키워드
- V-모델 (Mô hình chữ V / V-Model / 개발 단계와 테스트 단계 상호 대응)
- 인수·시스템·통합·단위 테스트 (4 cấp độ kiểm thử / Acceptance, System, Integration, Unit)
- 알파 테스트 & 베타 테스트 (Alpha Test - 개발자 관찰 vs Beta Test - 실환경 자유 배포)
- 하향식 & 상향식 통합 (Top-down - 스텁 Stub vs Bottom-up - 드라이버 Driver)
- 빅뱅 통합 (Big-Bang Integration / phi gia tăng / khó khoanh vùng lỗi)
- 테스트 오라클 (Test Oracle / 참값 비교 / 참, 샘플링, 추정, 일관성 오라클)
- 테스트 하네스 (Test Harness / Driver, Stub, Suite, Script, Mock Object)

## 선행·연결 개념
- **Từ đâu (Origin / Prerequisite):** Ở bài học trước [16-kiem-thu-hop-den-va-test-case.md](16-kiem-thu-hop-den-va-test-case.md), chúng ta đã khảo sát các kỹ thuật thiết kế ca kiểm thử hộp đen dựa trên đặc tả.
- **Đang giải quyết gì (Current Problem):** Bài học này tổ chức phân bổ các kỹ thuật kiểm thử vào từng giai đoạn phát triển theo mô hình chữ V, giải quyết bài toán tích hợp module bằng Stub/Driver, và thiết lập cơ chế so sánh kết quả tự động bằng Test Oracle.
- **Dùng đi đâu (Forward Handoff):** Sau khi hoàn tất quy trình kiểm thử, bàn giao sang [18-clean-code-refactoring-va-kiem-tra-tinh.md](18-clean-code-refactoring-va-kiem-tra-tinh.md) để đánh giá chất lượng mã nguồn nội bộ qua 5 nguyên tắc Clean Code, kỹ thuật Refactoring và công cụ phân tích tĩnh PMD/SonarQube.

## 읽는 방법
- Đọc TẦNG A để thuộc lòng sơ đồ V-Model và 4 cặp đối ứng, bảng so sánh Top-down vs Bottom-up (thần chú: Hạ thấu dùng Stub, Thượng thăng dùng Driver), và bảng 4 loại Test Oracle.
- Đọc TẦNG B để hiểu sâu cấu tạo Test Harness, cơ chế Mock Object, và kỹ thuật Sandwich Testing.

---

## V-모델 테스트 레벨과 테스트 오라클

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Mô hình chữ V (V-모델) và 4 cặp đối ứng giai đoạn
- **Định nghĩa:**
  - [한국어]: **V-모델은 소프트웨어 개발 단계와 테스트 단계를 상호 대응시켜 개발 단계의 산출물을 각 테스트 단계에서 검증 및 확인하는 모델이다.**
  - [Tiếng Việt]: Mô hình chữ V là mô hình kỹ nghệ phần mềm thể hiện mối quan hệ đối xứng trực tiếp 1-1 giữa các pha phát triển phần mềm (nhánh trái đi xuống) và các cấp độ kiểm thử tương ứng (nhánh phải đi lên).

```
[ 요구사항 분석 ]  <====== (Nghiệm thu thực tế) ======>  [ 인수 테스트 ]
       \                                                      /
   [ 시스템 설계 ]  <==== (Kiểm tra phi chức năng) ====>  [ 시스템 테스트 ]
          \                                                /
      [ 상세 설계 ]  <=== (Kiểm tra Interface) ===>  [ 통합 테스트 ]
             \                                          /
         [ 구현/코딩 ]  <-- (Kiểm tra logic/code) --> [ 단위 테스트 ]
```

#### Bảng ánh xạ 4 cặp giai đoạn phát triển - kiểm thử chuẩn đề thi
| Giai đoạn phát triển (Nhánh trái) | Cấp độ kiểm thử đối ứng (Nhánh phải) | Mục tiêu kiểm tra trọng tâm và kỹ thuật sử dụng |
| :--- | :--- | :--- |
| **요구사항 분석 (Requirements Analysis)** | **인수 테스트 (Acceptance Test)** | Kiểm tra xem hệ thống có thỏa mãn hợp đồng và nhu cầu người dùng. Gồm **알파 테스트 (Alpha Test)** và **베타 테스트 (Beta Test)** |
| **시스템 설계 (System Design)** | **시스템 테스트 (System Test)** | Kiểm tra toàn bộ hệ thống hoàn chỉnh trên môi trường thực tế gồm chức năng và phi chức năng (Hiệu năng, Bảo mật, Chịu tải Stress) |
| **상세 설계 (Detailed Design)** | **통합 테스트 (Integration Test)** | Kiểm tra sự tương tác, truyền nhận tham số và **lỗi giao diện liên kết (Interface Error)** giữa các module khi ghép nối |
| **구현 / 코딩 (Implementation / Coding)** | **단위 테스트 (Unit Test)** | Kiểm tra từng module, hàm, lớp riêng lẻ xem thuật toán có đúng không. Sử dụng chủ yếu **화이트박스 테스트 (White-Box)** |

#### 2. Phân biệt Alpha Test vs Beta Test
| Tiêu chí | 알파 테스트 (Alpha Test) | 베타 테스트 (Beta Test / Field Test) |
| :--- | :--- | :--- |
| **Môi trường** | Phòng thí nghiệm có kiểm soát (Lab) của nhà phát triển | Môi trường thực tế phân tán của người dùng đại chúng |
| **Giám sát** | **Có lập trình viên quan sát trực tiếp (개발자 앞에서)** | **Hoàn toàn không có lập trình viên giám sát** |
| **Phản hồi** | Lập trình viên ghi nhận lỗi tức thì tại chỗ | Người dùng tự trải nghiệm và gửi báo cáo lỗi về |

#### 3. Bảng so sánh đối đầu Top-down vs Bottom-up Integration

```text
  [1. TÍCH HỢP TỪ TRÊN XUỐNG (TOP-DOWN)]             [2. TÍCH HỢP TỪ DƯỚI LÊN (BOTTOM-UP)]
              ┌───────────────┐                                 ┌───────────────┐
              │  MODULE ĐỈNH  │ (Mã nguồn thật)                 │  TEST DRIVER  │ (Giả lập điều khiển)
              └───────┬───────┘                                 └───────┬───────┘
                      │ Gọi xuống                                       │ Gọi kích hoạt
          ┌───────────┴───────────┐                                     ▼
          ▼                       ▼                             ┌───────────────┐
   ┌──────────────┐        ┌──────────────┐                     │ CLUSTER/NHÓM  │ (Các module con
   │ TEST STUB 1  │        │ TEST STUB 2  │                     │  [Module A]   │  thực tế đã code)
   └──────────────┘        └──────────────┘                     │  [Module B]   │
   (Giả lập module con cấp dưới nhận tham số)                   └───────────────┘
```

| Tiêu chí | 하향식 통합 테스트 (Top-down) | 상향식 통합 테스트 (Bottom-up) |
|:---|:---|:---|
| **Hướng tích hợp** | Từ mô-đun chính ở đỉnh đi dần xuống dưới | Từ các mô-đun lá ở đáy đi dần lên trên |
| **Công cụ hỗ trợ** | **테스트 스텁 (Test Stub)** - Giả lập mô-đun con bị gọi | **테스트 드라이버 (Test Driver)** - Giả lập chương trình gọi xuống |
| **Đơn vị tích hợp** | Từng module theo nhánh (Depth-first / Breadth-first) | Gom các module con thành cụm (**클러스터 / Cluster**) |
| **Ưu điểm lớn nhất** | Sớm có bản mẫu demo (**Prototype**) cho khách hàng xem | Kiểm tra kỹ thuật toán xử lý dữ liệu ở đáy; dễ viết ca test |
| **Nhược điểm** | Các hàm xử lý dữ liệu chi tiết ở đáy bị test muộn | Mô-đun điều khiển ở đỉnh bị test muộn; không sớm có demo |

- **Chi tiết hai chiến lược duyệt nhánh trong Top-down:**
  - `깊이 우선 (Depth-First)`: Tích hợp dọc theo một nhánh điều khiển chính đi thẳng từ đỉnh xuống đáy trước khi chuyển sang nhánh rẽ khác.
  - `너비 우선 (Breadth-First)`: Tích hợp và kiểm tra tất cả các module ngang hàng trong cùng một cấp trước khi đi xuống cấp sâu hơn.
- **Quy trình tích hợp trong Bottom-up:**
  1. Gom các module cấp thấp thực hiện các chức năng liên quan thành các cụm (`클러스터 / Cluster` hoặc `Build`).
  2. Viết chương trình điều khiển giả lập (`테스트 드라이버 - Test Driver`) để truyền tham số và gọi cluster thực thi.
  3. Thực hiện kiểm thử trên cluster.
  4. Gỡ bỏ Test Driver và thay thế bằng các module cấp trên thực tế khi chúng được hoàn thiện.
- **빅뱅 통합 테스트 (Big-Bang Integration):** Lắp ghép toàn bộ tất cả các module cùng một lúc rồi mới chạy test. Nhược điểm chí tử: **Cực kỳ khó xác định nguyên nhân và vị trí lỗi (원인 식별 곤란)**, chỉ phù hợp dự án quy mô rất nhỏ.
- **혼합식 통합 (Sandwich / Hybrid Testing):** Tầng trên tích hợp Top-down (dùng Stub), tầng dưới tích hợp Bottom-up (dùng Driver), hai hướng gặp nhau tại tầng điều phối trung gian.

#### 4. Bốn loại Test Oracle (테스트 오라클)
- **Định nghĩa:**
  - [한국어]: **테스트 오라클은 테스트 수행 결과가 참인지 거짓인지를 판단하기 위해 사전에 정의된 참값을 대입하여 비교하는 활동 혹은 그 참값을 의미한다.**
  - [Tiếng Việt]: Test Oracle là hoạt động hoặc giá trị chân lý định trước được đưa vào so sánh nhằm phán đoán kết quả thực thi kiểm thử là Đúng hay Sai.

| Loại Test Oracle | Tên tiếng Hàn & Anh | Cơ chế hoạt động chi tiết | Trường hợp áp dụng thực tế |
|:---|:---|:---|:---|
| **Oracle Chân lý** | **참 오라클 (True Oracle)** | Kiểm tra **tất cả mọi ca kiểm thử (전수 검사)** bằng cách so sánh với kết quả kỳ vọng đúng tuyệt đối 100% | Hệ thống an toàn sinh mạng: Hàng không, vũ trụ, thiết bị y tế, ngân hàng |
| **Oracle Lấy mẫu** | **샘플링 오라클 (Sampling Oracle)** | **Chỉ chọn một số ca kiểm thử mẫu đại diện** để đối chiếu kết quả chính xác, các ca khác kiểm tra sơ bộ | Không gian dữ liệu đầu vào quá lớn, không thể tính toán trước kết quả của 100% trường hợp |
| **Oracle Ước lượng** | **추정 / 휴리스틱 오라클 (Heuristic Oracle)** | Sử dụng **kinh nghiệm chuyên gia, lý thuyết xác suất và giải thuật xấp xỉ** khi không thể tính chính xác | Hệ thống Trí tuệ nhân tạo (AI/ML), xử lý hình ảnh, thị giác máy tính, mô hình hóa dự báo thời tiết |
| **Oracle Nhất quán** | **일관성 검사 오라클 (Consistent Oracle)** | **So sánh kết quả thực thi trước và sau khi sửa đổi mã nguồn** xem có phát sinh biến đổi ngoài ý muốn | Áp dụng chủ yếu trong **Kiểm thử hồi quy (회귀 테스트 / Regression Testing)** |

#### 5. Bẫy đề thi trắc nghiệm kinh điển (기출 함정 포인트)
- **Bẫy 1: Ghép cặp V-Model:**
  - Yêu cầu $\leftrightarrow$ Nghiệm thu (`인수 테스트`).
  - Thiết kế kiến trúc/hệ thống $\leftrightarrow$ Hệ thống (`시스템 테스트`).
  - Thiết kế chi tiết $\leftrightarrow$ Tích hợp (`통합 테스트`).
  - Cài đặt/Mã nguồn $\leftrightarrow$ Đơn vị (`단위 테스트`).
- **Bẫy 2: Thần chú Stub vs Driver:**
  - **Hạ thấu (Top-down)** đi xuống cần module con giả lập bên dưới $\rightarrow$ **테스트 스텁 (Test Stub)**.
  - **Thượng thăng (Bottom-up)** đi lên cần chương trình điều khiển giả lập bên trên $\rightarrow$ **테스트 드라이버 (Test Driver)**.
- **Bẫy 3: Oracle Nhất quán (Consistent Oracle):** Khi đề hỏi "Loại Oracle nào so sánh kết quả trước và sau khi thay đổi phần mềm, chuyên dùng trong kiểm thử hồi quy?" $\rightarrow$ Chọn ngay **일관성 검사 오라클 (Consistent Oracle)**.
- **Bẫy 4: Kiểm thử Big-Bang:** Lắp ghép 1 lần toàn bộ module rồi test $\rightarrow$ Nhược điểm lớn nhất là **khó khoanh vùng xác định nguyên nhân lỗi (오류 위치 식별 곤란)**.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Giàn giáo kiểm thử (테스트 하네스 - Test Harness)
Test Harness là khung môi trường phần mềm hỗ trợ thực thi kiểm thử tự động gồm:
- **테스트 드라이버 (Test Driver):** Module điều khiển cấp trên giả lập gọi module cần test (dùng trong Bottom-up).
- **테스트 스텁 (Test Stub):** Module cấp dưới giả lập nhận lệnh và trả về dữ liệu mẫu (dùng trong Top-down).
- **테스트 슈트 (Test Suite):** Tập hợp nhiều Test Case được gom nhóm lại để thực thi trong một chu kỳ kiểm thử.
- **테스트 스크립트 (Test Script):** File kịch bản chứa các dòng lệnh tự động hóa thực thi các Test Case.
- **목 오브젝트 (Mock Object):** Đối tượng giả lập hành vi của các thành phần phụ thuộc bên ngoài (DB, API thứ ba) với các phản hồi được lập trình sẵn.

---

### 복습 체크리스트
- [ ] Vẽ lại chuẩn xác mô hình V-Model và 4 cặp giai đoạn phát triển - kiểm thử đối ứng.
- [ ] Nhớ đúng cặp: Yêu cầu $\leftrightarrow$ 인수 테스트; Thiết kế hệ thống $\leftrightarrow$ 시스템 테스트.
- [ ] Nhớ đúng cặp: Thiết kế chi tiết $\leftrightarrow$ 통합 테스트; Lập trình $\leftrightarrow$ 단위 테스트.
- [ ] Phân biệt 알파 테스트 (trong phòng Lab có mặt lập trình viên) và 베타 테스트 (ngoài thực địa không có lập trình viên).
- [ ] Phân biệt 빅뱅 통합 (ghép 1 lần, khó tìm nguyên nhân lỗi) và 점진적 통합 (ghép từng bước).
- [ ] Nhớ thần chú: 하향식 (Top-down) dùng 테스트 스텁 (Test Stub); 상향식 (Bottom-up) dùng 테스트 드라이버 (Test Driver).
- [ ] Định nghĩa Test Oracle là cơ chế thẩm định kết quả kiểm thử là Đúng hay Sai.
- [ ] Kể tên và phân biệt 4 loại Test Oracle: 참 (True), 샘플링 (Sampling), 추정/휴리스틱 (Heuristic), 일관성 (Consistent).
- [ ] Nhớ 일관성 검사 오라클 chuyên dùng cho kiểm thử hồi quy Regression Testing.
