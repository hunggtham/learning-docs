# 소프트웨어 유지보수, 재공학 및 CASE 도구 (Bảo trì, Tái kỹ nghệ & Công cụ CASE)

## 학습 목표 (Mục tiêu)
- Nắm vững 4 loại hình bảo trì phần mềm (소프트웨어 유지보수): Sửa lỗi (수정 보수), Thích ứng (적응 보수), Hoàn thiện (완전화 보수 - chiếm chi phí lớn nhất ~50%), và Phòng ngừa (예방 보수).
- Thấu hiểu khái niệm Mã nguồn ngoài hành tinh (외계인 코드 - Alien Code) và 4 hoạt động của Tái kỹ nghệ phần mềm (소프트웨어 재공학: Phân tích, Tái cấu trúc, Dịch ngược Reverse Engineering, Di chuyển Migration).
- Phân biệt các phân loại của Công cụ kỹ nghệ phần mềm hỗ trợ máy tính (CASE): Thượng vị CASE (상위 CASE - Phân tích & Thiết kế) và Hạ vị CASE (하위 CASE - Viết mã & Kiểm thử), cùng vai trò của Kho lưu trữ CASE (Repository).

## 핵심 키워드 (Từ khóa)
- 소프트웨어 유지보수 (Software Maintenance) — 수정(20%), 적응(25%), 완전화(50% 최대), 예방(5%).
- 완전화 보수 (Perfective Maintenance) — Thêm tính năng mới và cải tiến hiệu năng theo yêu cầu người dùng.
- 외계인 코드 (Alien Code) — Mã nguồn cũ thiếu tài liệu hóa (문서화 부재) cực kỳ khó bảo trì.
- 소프트웨어 재공학 (Software Reengineering) — Cải tiến nâng cao khả năng bảo trì giữ nguyên hành vi chức năng.
- 역공학 (Reverse Engineering) — Phân tích mã nguồn hiện có để khôi phục lại tài liệu thiết kế.
- CASE 도구 (CASE Tools) — 상위 CASE (요구분석/설계), 하위 CASE (구현/테스트), 통합 CASE (Repository).

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Kế thừa từ `20-kiem-thu-phan-mem-va-vong-doi-loi.md`, sau khi hoàn thành kiểm thử nghiệm thu và bàn giao cho khách hàng, phần mềm chính thức bước vào giai đoạn vận hành và bảo trì.
- **Đang giải quyết gì (Current Problem):** Giải quyết câu hỏi quản trị kỹ thuật: Làm sao duy trì một hệ thống phần mềm kế thừa qua hàng chục năm không bị đào thải, xử lý thế nào khi lập trình viên ban đầu rời đi để lại mã nguồn không tài liệu và dùng công cụ nào để tự động hóa vòng đời phát triển.
- **Dùng đi đâu (Forward Handoff):** Các kỹ thuật tái cấu trúc và tự động hóa này sẽ hoàn thiện bức tranh công nghệ phần mềm và chuẩn bị nền móng cho việc triển khai ứng dụng máy chủ và bảo mật ở bài `22-trien-khai-server-batch-bao-mat-va-ket-noi-csdl.md`.

## 읽는 방법 (Cách đọc)
- **4 loại bảo trì:**
  - Sửa lỗi phát sinh $\rightarrow$ **Bảo trì sửa lỗi (수정 보수)**.
  - Đổi hệ điều hành/luật pháp bên ngoài $\rightarrow$ **Bảo trì thích ứng (적응 보수)**.
  - Khách hàng đòi thêm tính năng mới $\rightarrow$ **Bảo trì hoàn thiện (완전화 보수 - CHIẾM 50% CHI PHÍ)**.
  - Tái cấu trúc mã nguồn phòng ngừa lỗi $\rightarrow$ **Bảo trì phòng ngừa (예방 보수)**.
- **CASE:**
  - **Thượng vị (상위 CASE):** Phân tích yêu cầu, Thiết kế (vẽ DFD, ERD).
  - **Hạ vị (하위 CASE):** Viết mã (Coding), Kiểm thử (Test).
  - **Kho thông tin (Repository):** Trái tim lưu trữ dữ liệu chung của CASE.

---

## 소프트웨어 유지보수, 재공학 및 CASE 도구

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

- **핵심 원리 (Nguyên tắc cốt lõi):**
  - [한국어]: `소프트웨어 유지보수 중 사용자의 기능 개선 요구를 반영하는 완전화(Perfective) 보수가 약 50%로 가장 큰 비용을 차지한다. 외계인 코드는 문서화가 부재한 레거시 코드이다. 역공학은 소스코드로부터 설계를 추출하는 기법이며, 상위 CASE는 요구분석/설계, 하위 CASE는 코드생성/테스트를 지원한다.`
  - [Tiếng Việt]: Trong bảo trì phần mềm, bảo trì hoàn thiện (Perfective) đáp ứng yêu cầu cải tiến tính năng của người dùng chiếm chi phí lớn nhất khoảng 50%. Alien code là mã nguồn kế thừa thiếu tài liệu hóa. Dịch ngược (Reverse Engineering) trích xuất tài liệu thiết kế từ code; Thượng vị CASE hỗ trợ phân tích/thiết kế, Hạ vị CASE hỗ trợ viết mã/kiểm thử.

- **1. Bảng 4 loại hình bảo trì phần mềm (소프트웨어 유지보수 4대 유형):**

| Loại hình bảo trì | Thuật ngữ Hàn / Anh | Tỷ trọng chi phí | Hoàn cảnh và mục đích kích hoạt |
| :--- | :--- | :---: | :--- |
| **1. Bảo trì hoàn thiện**<br>(기능 개선) | **완전화 보수**<br>(Perfective Maintenance) | **$\approx$ 50%<br>(LỚN NHẤT)** | **Bổ sung tính năng mới theo yêu cầu người dùng**, nâng cấp giao diện, tối ưu hóa hiệu năng hệ thống. |
| **2. Bảo trì thích ứng**<br>(환경 적응) | **적응 보수**<br>(Adaptive Maintenance) | $\approx$ 25% | Điều chỉnh phần mềm để **thích nghi với sự thay đổi của môi trường bên ngoài** (nâng cấp HĐH, luật thuế mới). |
| **3. Bảo trì sửa lỗi**<br>(오류 수정) | **수정 보수**<br>(Corrective Maintenance) | $\approx$ 20% | Phát hiện và khắc phục các **lỗi tiềm ẩn phát sinh trong quá trình vận hành thực tế**. |
| **4. Bảo trì phòng ngừa**<br>(예방 개선) | **예방 보수**<br>(Preventive Maintenance) | $\approx$ 5% | **Tái cấu trúc mã nguồn (Refactoring)** để tăng khả năng bảo trì, ngăn ngừa lỗi phát sinh trong tương lai. |

- **2. Bảng 4 hoạt động cốt lõi của Tái kỹ nghệ phần mềm (소프트웨어 재공학):**

| Hoạt động kỹ thuật | Thuật ngữ Hàn / Anh | Bản chất thao tác thực hiện |
| :--- | :--- | :--- |
| **1. Phân tích** | **분석** (Analysis) | Đánh giá hiện trạng mã nguồn cũ, xác định các thành phần cần cải tiến hoặc thay thế. |
| **2. Tái cấu trúc** | **재구성 / 개조** (Restructuring) | **Tối ưu hóa cấu trúc mã nguồn bên trong** mà hoàn toàn giữ nguyên hành vi chức năng bên ngoài. |
| **3. Dịch ngược** | **역공학** (Reverse Engineering) | **Đi ngược từ mã nguồn để khôi phục lại tài liệu thiết kế**, sơ đồ cấu trúc và lược đồ CSDL. |
| **4. Di chuyển** | **이설 / 마이그레이션** (Migration)| Chuyển đổi toàn bộ hệ thống sang vận hành trên môi trường phần cứng hoặc nền tảng công nghệ mới. |

- **3. Bảng phân loại công cụ hỗ trợ phát triển phần mềm CASE (CASE 도구 분류):**

| Phân loại công cụ | Giai đoạn SDLC hỗ trợ | Chức năng và công cụ đại diện |
| :--- | :--- | :--- |
| **상위 CASE (Thượng vị)** | **Giai đoạn đầu:** Phân tích yêu cầu và Thiết kế hệ thống. | Hỗ trợ vẽ sơ đồ luồng dữ liệu (DFD), sơ đồ thực thể liên kết (ERD), mô hình hóa UML. |
| **하위 CASE (Hạ vị)** | **Giai đoạn sau:** Cài đặt mã nguồn và Kiểm thử hệ thống. | Hỗ trợ **sinh mã nguồn tự động (Code Generator)**, phát hiện lỗi cú pháp, kiểm thử tự động. |
| **통합 CASE (Tích hợp)** | **Toàn bộ vòng đời phát triển:** Từ yêu cầu đến bảo trì. | Đồng bộ hóa toàn bộ tài liệu và mã nguồn thông qua **Kho lưu trữ thông tin chung (CASE Repository)**. |

- **주의/함정 (Bẫy đề thi):**
  - **Loại bảo trì tốn chi phí nhất:** Đề thi hỏi *"Loại bảo trì nào chiếm tỷ trọng ngân sách lớn nhất?"* $\rightarrow$ Đáp án đúng bắt buộc là **완전화 보수 (Bảo trì hoàn thiện / Perfective Maintenance, ~50%)**, chọn sửa lỗi (수정) là sai bẫy.
  - **Định nghĩa Alien Code (외계인 코드):** Đặc trưng nhận diện bất di bất dịch của Alien Code là **문서화 부재 (Hoàn toàn thiếu tài liệu hóa)**.
  - **Khái niệm Dịch ngược (역공학):** Là đi ngược từ Mã nguồn (Code) $\rightarrow$ Thiết kế (Design), chứ không phải dịch từ thiết kế sang mã.

- **한 문장 설명 (Câu chốt tự nhớ):**
  - *"Hoàn thiện tính năng chiếm 50% chi phí; Alien code thiếu tài liệu hóa; Thượng vị CASE phân tích thiết kế, Hạ vị CASE viết mã sinh test."*

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Sơ đồ chu trình Tái kỹ nghệ phần mềm (Software Reengineering Lifecycle):
$$\begin{array}{ccc}
\text{Mã nguồn cũ (Legacy Code)} & \xrightarrow{\quad \mathbf{Dịch\ ngược\ (Reverse\ Engineering)} \quad} & \text{Tài liệu thiết kế khôi phục} \\
\downarrow & & \downarrow \text{Cải tiến thiết kế} \\
\mathbf{\text{Tái cấu trúc (Restructuring)}} & \xrightarrow{\quad \mathbf{Kỹ\ nghệ\ xuôi\ (Forward\ Engineering)} \quad} & \text{Hệ thống mới tối ưu}
\end{array}$$

#### 2. Kiến trúc trung tâm của hệ thống công cụ CASE:
- Mọi công cụ trong bộ CASE (Công cụ vẽ DFD, Công cụ sinh Code, Công cụ kiểm thử) đều không giao tiếp trực tiếp với nhau mà trao đổi thông qua **CASE Repository (Kho lưu trữ thông tin chung)**:
$$\text{Công cụ vẽ thiết kế} \longleftrightarrow \mathbf{CASE\ Repository\ (Kho\ thông\ tin\ trung\ tâm)} \longleftrightarrow \text{Trình sinh mã Code Generator}$$
- Nhờ Repository, khi một thuộc tính trên mô hình thiết kế thay đổi, mã nguồn tương ứng sẽ được tự động cập nhật đồng bộ.

---

### 복습 체크리스트
- [ ] Ghi nhớ 4 loại bảo trì: Sửa lỗi (20%), Thích ứng (25%), Hoàn thiện (50% lớn nhất), Phòng ngừa (5%).
- [ ] Nhớ bảo trì hoàn thiện (완전화 보수) là đáp ứng yêu cầu thêm tính năng của người dùng.
- [ ] Nắm vững đặc trưng Alien Code: Mã nguồn cũ hoàn toàn thiếu tài liệu hóa (문서화 부재).
- [ ] Thuộc lòng 4 hoạt động tái kỹ nghệ: Phân tích $\rightarrow$ Tái cấu trúc $\rightarrow$ Dịch ngược $\rightarrow$ Di chuyển.
- [ ] Hiểu rõ Dịch ngược (역공학): Trích xuất tài liệu thiết kế từ mã nguồn có sẵn.
- [ ] Phân biệt được: Thượng vị CASE (phân tích/thiết kế) vs Hạ vị CASE (sinh mã/kiểm thử).
