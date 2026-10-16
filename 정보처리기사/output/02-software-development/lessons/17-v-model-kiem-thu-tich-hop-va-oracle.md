# Môn 2 · Bài 17 — Cấp độ kiểm thử V-Model, kiểm thử tích hợp và Test Oracle

> **Mạch đọc:** [README](../README.md) là bản đồ chủ đề của **Môn 2 — 소프트웨어 개발 (Software Development)**. Sau khi đã nắm vững các kỹ thuật kiểm thử hộp trắng ([Bài 15](15-kiem-thu-hop-trang-va-coverage.md)) và kiểm thử hộp đen ([Bài 16](16-kiem-thu-hop-den-va-test-case.md)), bài học này khép lại toàn diện **Chương 4: Quản lý kiểm thử phần mềm** bằng việc liên kết các kỹ thuật đó vào vòng đời phát triển thông qua **Mô hình chữ V (V-모델)**, các chiến lược kiểm thử tích hợp hạ thấu (Stub) / thượng thăng (Driver) và cơ chế phán đoán tính đúng đắn của kết quả kiểm thử bằng **Test Oracle**.

> **Phạm vi nguồn:** Hợp nhất và chuẩn hóa nội dung từ các bài học cũ `53-bai-hoc.md`, `54-bai-hoc.md`, `55-bai-hoc.md`, `60-bai-hoc.md` và `66-bai-hoc.md` (tương ứng với các mục 16, 17, 20, 45, 132 ~ 136 trong tài liệu chuẩn gốc). Toàn bộ thuật ngữ và các cặp đối ứng kiểm thử được đối chiếu chính xác theo chuẩn khảo thí HRDK và ISTQB.

> **Mạch kiến thức:** Bài học giải quyết ba bài toán cốt lõi trong tổ chức kiểm thử: (1) Các giai đoạn phát triển phần mềm (nhánh trái V-Model) ánh xạ đối xứng với những cấp độ kiểm thử nào (nhánh phải)? (2) Khi ghép các module lại với nhau, tại sao phương pháp Big Bang lại nguy hiểm, và làm sao phân biệt bản chất giữa Test Stub (Top-down) và Test Driver (Bottom-up)? (3) Máy tính dựa vào cơ chế nào để tự động thẩm định kết quả kiểm thử là ĐÚNG hay SAI qua 4 loại Test Oracle?

---

## 1. V-모델 기반 테스트 레벨 — Các cấp độ kiểm thử theo mô hình chữ V

**V-모델은 소프트웨어 개발 단계와 테스트 단계를 상호 대응시켜 개발 단계의 산출물을 각 테스트 단계에서 검증 및 확인하는 모델이다.**

Mô hình chữ V (V-Model) là mô hình kinh điển trong kỹ nghệ phần mềm thể hiện mối quan hệ đối xứng trực tiếp 1-1 giữa các pha phát triển phần mềm (nhánh trái đi xuống — quá trình phân rã và chi tiết hóa hệ thống) và các cấp độ kiểm thử tương ứng (nhánh phải đi lên — quá trình lắp ráp và tích hợp dần từ dưới lên).

### Kiến trúc đối xứng của Mô hình V-Model

```
[ 요구사항 분석 ]  <====== (Nghiệm thu thực tế) ======>  [ 인수 테스트 ]
       \                                                      /
   [ 시스템 설계 ]  <==== (Kiểm tra phi chức năng) ====>  [ 시스템 테스트 ]
          \                                                /
      [ 상세 설계 ]  <=== (Kiểm tra Interface) ===>  [ 통합 테스트 ]
             \                                          /
         [ 구현/코딩 ]  <-- (Kiểm tra logic/code) --> [ 단위 테스트 ]
```

### Bảng ánh xạ 4 cặp giai đoạn phát triển - kiểm thử chuẩn đề thi

| Giai đoạn phát triển (Nhánh trái) | Cấp độ kiểm thử đối ứng (Nhánh phải) | Mục tiêu kiểm tra trọng tâm và kỹ thuật sử dụng |
| :--- | :--- | :--- |
| **요구사항 분석 (Requirements Analysis)** | **인수 테스트 (Acceptance Test)** | Kiểm tra xem hệ thống có thỏa mãn đúng hợp đồng và nhu cầu thực tế của người dùng cuối hay không. Gồm **알파 테스트 (Alpha Test)** và **베타 테스트 (Beta Test)** |
| **시스템 설계 (System Design)** | **시스템 테스트 (System Test)** | Kiểm tra toàn bộ hệ thống tích hợp hoàn chỉnh trên môi trường thực tế. Bao gồm cả **Chức năng (Functional)** và **Phi chức năng (Non-functional)**: Hiệu năng, Bảo mật, Chịu tải quá mức (Stress), Phục hồi sự cố |
| **상세 설계 (Detailed Design)** | **통합 테스트 (Integration Test)** | Kiểm tra sự tương tác, truyền nhận tham số và **lỗi giao diện liên kết (Interface Error)** giữa các module khi ghép nối lại. Sử dụng chiến lược **Top-down** (Stub) hoặc **Bottom-up** (Driver) |
| **구현 / 코딩 (Implementation / Coding)** | **단위 테스트 (Unit Test)** | Kiểm tra từng module, hàm, lớp riêng lẻ xem thuật toán có đúng không, có rò rỉ bộ nhớ hay lỗi vòng lặp không. Sử dụng chủ yếu **화이트박스 테스트 (White-Box)** |

### Phân biệt hai hình thức Kiểm thử chấp nhận: Alpha Test vs Beta Test
- **알파 테스트 (Alpha Test):**
  - Thực hiện trong môi trường phòng thí nghiệm có kiểm soát (Lab) của nhà phát triển.
  - Người dùng thử nghiệm thao tác **dưới sự quan sát và ghi nhận trực tiếp của lập trình viên (개발자 앞에서)**.
- **베타 테스트 (Beta Test / Field Test):**
  - Phát hành cho số lượng lớn người dùng đại chúng trải nghiệm tự do trên môi trường thực tế (Real-world).
  - **Hoàn toàn không có lập trình viên giám sát**, người dùng tự trải nghiệm và gửi phản hồi lỗi về cho nhóm phát triển.

---

## 2. 통합 테스트 기법 — Các kỹ thuật kiểm thử tích hợp

Sau khi từng module đã vượt qua kiểm thử đơn vị, chúng được ghép nối lại trong **통합 테스트 (Integration Testing)**. Lỗi giao tiếp giữa các module là nguyên nhân phổ biến nhất gây sập hệ thống. Có hai trường phái tích hợp chính:

### 2.1. 빅뱅 통합 테스트 (Big-Bang Integration Testing — Tích hợp phi gia tăng)
- **Cơ chế:** Lắp ghép toàn bộ tất cả các module lại với nhau **cùng một lúc thành một khối duy nhất** rồi mới bấm nút chạy kiểm thử toàn diện.
- **Ưu điểm:** Phù hợp với các phần mềm quy mô rất nhỏ, tốn ít thời gian chuẩn bị công cụ giàn giáo.
- **Nhược điểm cốt lõi (Bẫy đề thi):** Khi xảy ra sự cố, **cực kỳ khó định vị nguyên nhân và vị trí gây lỗi (원인 식별 곤란)** do lỗi phát sinh từ sự xung đột chéo của nhiều module cùng lúc.

### 2.2. 점진적 통합 테스트 (Incremental Integration Testing — Tích hợp gia tăng)
Tích hợp từng bước lần lượt từng module vào hệ thống. Lỗi phát sinh ở đâu sẽ được khoanh vùng ngay lập tức tại vị trí module vừa thêm vào. Gồm hai hướng tiếp cận kinh điển:

#### 1. 하향식 통합 테스트 (Top-down Integration Testing — Tích hợp từ trên xuống)
- **Trình tự:** Bắt đầu từ **Mô-đun điều khiển chính ở đỉnh cao nhất (Main Control Module)**, sau đó tích hợp dần dần các module cấp dưới theo cấu trúc cây phân cấp điều khiển.
- **Chiến lược duyệt:** Duyệt theo chiều sâu (**깊이 우선 — Depth-First**) hoặc duyệt theo chiều rộng (**너비 우선 — Breadth-First**).
- **Công cụ bổ trợ:** **테스트 스텁 (Test Stub)**:
  - Khi module cấp trên đã viết xong nhưng module con cấp dưới chưa hoàn thiện, ta tạo ra các **Test Stub** (module con giả lập) để nhận tham số gọi và trả về giá trị mẫu giả định (Dummy Data) giúp module cấp trên có thể chạy thử nghiệm được.
- **Ưu điểm lớn nhất:** Luồng điều khiển kiến trúc chính được kiểm tra rất sớm; **sớm có bản mẫu demo (Prototype)** cho khách hàng xem.

#### 2. 상향식 통합 테스트 (Bottom-up Integration Testing — Tích hợp từ dưới lên)
- **Trình tự:** Bắt đầu từ các **mô-đun lá ở tầng đáy cùng (Bottom Layer)** — nơi thực hiện các thuật toán tính toán và truy xuất dữ liệu cốt lõi, gom thành các nhóm cụm (**클러스터 — Test Cluster**), sau đó tích hợp dần lên các module điều khiển cấp cao hơn.
- **Công cụ bổ trợ:** **테스트 드라이버 (Test Driver)**:
  - Do module cấp trên chưa được gọi tới hoặc chưa hoàn thiện, ta phải viết một chương trình điều khiển giả lập (**Test Driver**) để truyền dữ liệu đầu vào và gọi module cấp dưới thực thi, sau đó in kết quả ra màn hình.
- **Ưu điểm lớn nhất:** Kiểm tra kỹ lưỡng các thuật toán xử lý dữ liệu nặng ở tầng đáy; **dễ thiết kế Test Case** vì các module thực thi đã hoàn chỉnh.

### Bảng so sánh đối đầu Top-down vs Bottom-up Integration

| Tiêu chí | 하향식 통합 테스트 (Top-down) | 상향식 통합 테스트 (Bottom-up) |
| :--- | :--- | :--- |
| **Hướng tích hợp** | Từ mô-đun chính ở đỉnh đi dần xuống dưới | Từ các mô-đun lá ở đáy đi dần lên trên |
| **Công cụ hỗ trợ bắt buộc** | **테스트 스텁 (Test Stub)** — Giả lập mô-đun con bị gọi | **테스트 드라이버 (Test Driver)** — Giả lập chương trình gọi xuống |
| **Ưu điểm lớn nhất** | Sớm có bản mẫu demo (**Prototype**) cho khách hàng | Kiểm tra kỹ thuật toán xử lý dữ liệu ở đáy; dễ viết ca test |
| **Nhược điểm lớn nhất** | Các hàm xử lý dữ liệu chi tiết ở đáy bị test muộn | Mô-đun điều khiển ở đỉnh bị test muộn; không sớm có demo |

- **샌드위치 테스트 (Sandwich Testing / 혼합식 통합):** Kết hợp cả hai: Tầng trên tích hợp Top-down (dùng Stub), tầng dưới tích hợp Bottom-up (dùng Driver), hai hướng gặp nhau tại tầng giữa (Middle Layer).

---

## 3. 테스트 오라클 및 테스트 하네스 — Test Oracle & Test Harness

### 3.1. Bản chất của Test Oracle (테스트 오라클)

**테스트 오라클은 테스트 수행 결과가 참인지 거짓인지를 판단하기 위해 사전에 정의된 참값을 대입하여 비교하는 활동 혹은 그 참값을 의미한다.**

Khi một ca kiểm thử tự động chạy xong, nó sẽ trả về kết quả thực tế (Actual Result). Nhưng làm sao hệ thống biết kết quả đó là ĐÚNG hay SAI? Ta phải có một "nguồn chân lý định trước" để đối chiếu. Nguồn chân lý đó được gọi là **테스트 오라클 (Test Oracle)**.

### Bốn loại Test Oracle chuẩn đề thi

| Loại Test Oracle | Tên tiếng Hàn & Anh | Cơ chế hoạt động chi tiết | Trường hợp áp dụng thực tế |
| :--- | :--- | :--- | :--- |
| **Oracle Chân lý** | **참 오라클 (True Oracle)** | Kiểm tra **tất cả mọi ca kiểm thử (전수 검사)** bằng cách so sánh với kết quả kỳ vọng đúng tuyệt đối 100% | Áp dụng cho các hệ thống an toàn tính mạng cao: Hàng không, thiết bị y tế, ngân hàng cốt lõi |
| **Oracle Lấy mẫu** | **샘플링 오라클 (Sampling Oracle)** | **Chỉ chọn ra một số ca kiểm thử mẫu đại diện** để đối chiếu với kết quả đúng chính xác, các ca còn lại chỉ kiểm tra sơ bộ | Áp dụng khi không gian dữ liệu đầu vào quá lớn, không thể kiểm tra hết 100% |
| **Oracle Ước lượng** | **추정 / 휴리스틱 오라클 (Heuristic Oracle)** | Khi không thể tính toán kết quả chính xác tuyệt đối, sử dụng **kinh nghiệm chuyên gia, phán đoán xác suất và giải thuật xấp xỉ** | Áp dụng cho hệ thống Trí tuệ nhân tạo (AI), xử lý hình ảnh phức tạp, mô phỏng thời tiết |
| **Oracle Nhất quán** | **일관성 검사 오라클 (Consistent Oracle)** | **So sánh kết quả thực thi trước và sau khi sửa đổi mã nguồn** để xem hành vi của hệ thống có bị biến đổi ngoài ý muốn không | Áp dụng chủ yếu trong **Kiểm thử hồi quy (회귀 테스트 / Regression Testing)** |

### 3.2. Giàn giáo kiểm thử (Test Harness - 테스트 하네스)
Test Harness là tập hợp tất cả các phần mềm, công cụ, cấu hình và dữ liệu giả lập được dựng lên để hỗ trợ việc thực thi kiểm thử tự động:
- **테스트 드라이버 (Test Driver):** Chương trình cấp trên giả lập gọi module cần test (dùng trong Bottom-up).
- **테스트 스텁 (Test Stub):** Module cấp dưới giả lập nhận lệnh và trả về dữ liệu mẫu (dùng trong Top-down).
- **테스트 슈트 (Test Suite):** Tập hợp nhiều Test Case được gom nhóm lại để thực thi cùng một lúc trong một lần chạy.
- **테스트 스크립트 (Test Script):** File kịch bản chứa các dòng lệnh tự động hóa thực thi các Test Case.
- **목 오브젝트 (Mock Object):** Đối tượng giả lập hành vi của các thành phần phụ thuộc bên ngoài (như giả lập Database kết nối mạng, giả lập Payment Gateway bên thứ ba).

---

## 4. Nối mạch kiến thức sang Chương 5: Đảm bảo chất lượng mã nguồn & Tái cấu trúc

Sau khi hoàn thành toàn diện 4 bài học của Chương 4 (`Bài 14, 15, 16, 17`) về kiểm thử phần mềm, bước tiếp theo trong quy trình kỹ nghệ là đảm bảo chất lượng mã nguồn nội bộ, tái cấu trúc để loại bỏ nợ kỹ thuật và ứng dụng các công cụ phân tích tự động. Tiếp tục với **[18-clean-code-refactoring-va-kiem-tra-tinh.md](18-clean-code-refactoring-va-kiem-tra-tinh.md)** để nắm vững 5 nguyên tắc Clean Code, kỹ thuật Refactoring, nhận diện Alien Code và các công cụ phân tích tĩnh PMD, SonarQube.

---

## 5. 복습 체크리스트 (Checklist ôn tập)

- [ ] Vẽ lại chuẩn xác mô hình V-Model và 4 cặp giai đoạn phát triển - kiểm thử đối ứng.
- [ ] Nhớ đúng cặp: Yêu cầu $\leftrightarrow$ 인수 테스트; Thiết kế hệ thống $\leftrightarrow$ 시스템 테스트.
- [ ] Nhớ đúng cặp: Thiết kế chi tiết $\leftrightarrow$ 통합 테스트; Lập trình $\leftrightarrow$ 단위 테스트.
- [ ] Phân biệt 알파 테스트 (trong phòng Lab có mặt lập trình viên) và 베타 테스트 (ngoài thực địa không có lập trình viên).
- [ ] Phân biệt 빅뱅 통합 (ghép 1 lần, khó tìm nguyên nhân lỗi) và 점진적 통합 (ghép từng bước).
- [ ] Nhớ thần chú: 하향식 (Top-down) dùng 테스트 스텁 (Test Stub); 상향식 (Bottom-up) dùng 테스트 드라이버 (Test Driver).
- [ ] Định nghĩa Test Oracle là cơ chế thẩm định kết quả kiểm thử là Đúng hay Sai.
- [ ] Kể tên và phân biệt 4 loại Test Oracle: 참 (True), 샘플링 (Sampling), 추정/휴리스틱 (Heuristic), 일관성 (Consistent).
- [ ] Nhớ 일관성 검사 오라클 chuyên dùng cho kiểm thử hồi quy Regression Testing.
