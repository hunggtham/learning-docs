# 1. 사용자 인터페이스 (User Interface - UI)

## 학습 목표 (Mục tiêu)
- Nắm vững các loại hình giao diện người dùng hiện đại bao gồm giao diện tự nhiên (`NUI`) và giao diện hữu cơ (`OUI`).
- Thuộc nằm lòng các cử chỉ cảm ứng trên thiết bị di động (`모바일 제스처`): Tap, Double Tap, Drag, Pan, Press, Flick, Pinch.
- Phân biệt tuyệt đối giữa 4 công cụ thiết kế giao diện tiêu chuẩn: Khung xương (`와이어프레임`), Bản dựng tĩnh (`목업`), Bảng cốt truyện (`스토리보드`), và Bản mẫu động (`프로토타입`).

## 핵심 키워드 (Từ khóa)
- OUI (Organic User Interface / 유기적 인터페이스)
- 모바일 제스처 (Cử chỉ cảm ứng di động: Tap, Drag, Pan, Flick, Pinch)
- 와이어프레임 (Khung xương layout / Wireframe / 뼈대)
- 목업 (Bản dựng đồ họa tĩnh / Mockup / 정적 모형)
- 스토리보드 (Bảng cốt truyện luồng điều hướng / Storyboard / 이동 흐름)
- 프로토타입 (Bản mẫu thử nghiệm tương tác / Prototype / 동적 모형)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([4. 사용자 인터페이스](19-bai-hoc.md)):** Sau khi nắm vững 4 nguyên tắc vàng của UI (Trực quan, Hữu hiệu, Dễ học, Linh hoạt), bài này trang bị bộ công cụ kỹ thuật và thao tác cử chỉ để hiện thực hóa giao diện đó.
- **Tiếp nối sang bài sau ([12. UI 및 아키텍처 설계 심화](21-bai-hoc.md)):** Nâng cao quy trình thiết kế UI lấy người dùng làm trung tâm (User-centric, Usability) và chuẩn bị chuyển tiếp sang Thiết kế kiến trúc phần mềm.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để ghi nhớ chắc chắn sự khác biệt giữa 4 công cụ thiết kế UI (Wireframe là khung xương; Mockup là hình ảnh đẹp tĩnh; Storyboard có luồng di chuyển; Prototype là mô hình động bấm thử được).
- Đọc TẦNG B để hiểu rõ tại sao việc sử dụng Prototype giúp tiết kiệm chi phí sửa chữa giao diện trước khi lập trình viên bắt tay viết code thật.

---

## 1. 사용자 인터페이스 (User Interface - UI)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Các loại hình UI hiện đại:**
  - `CLI (Command Line Interface)`: Dòng lệnh văn bản.
  - `GUI (Graphical User Interface)`: Đồ họa hình ảnh, chuột, menu.
  - `NUI (Natural User Interface)`: Cử chỉ tự nhiên, giọng nói (chạm, vẫy tay, ra lệnh âm thanh).
  - `OUI (Organic User Interface)`: Giao diện hữu cơ, tương tác trên các vật thể vật lý thực tế, màn hình uốn cong, dẻo, có thể gập hoặc co giãn theo hình dạng vật thể.
- **2. Bảng thao tác cử chỉ di động chuẩn (모바일 제스처):**
  - `Tap (탭)`: Chạm nhẹ một ngón tay vào màn hình rồi nhấc lên ngay (tương đương click chuột).
  - `Double Tap (더블 탭)`: Chạm hai lần liên tiếp thật nhanh vào một vị trí (thường dùng để phóng to hình ảnh).
  - `Drag (드래그)`: Chạm ngón tay vào đối tượng, giữ nguyên và kéo di chuyển sang vị trí khác rồi mới nhấc ngón tay.
  - `Pan (팬)`: Đặt ngón tay lên màn hình và di chuyển liên tục theo mọi hướng mà không rời tay (di chuyển bản đồ, cuộn nội dung tự do).
  - `Press (프레스 / Long Press)`: Chạm ngón tay và ấn giữ nguyên tại một vị trí trong khoảng thời gian nhất định (thường để mở menu ngữ cảnh).
  - `Flick (플릭)`: Đặt ngón tay lướt thật nhanh trên màn hình theo một hướng rồi buông tay (cuộn trang nhanh, chuyển ảnh album).
  - `Pinch (핀치)`: Đặt hai ngón tay lên màn hình và chụm lại gần nhau (Pinch Close - Thu nhỏ) hoặc tách xa nhau ra (Pinch Open - Phóng to).
- **3. Phân biệt 4 công cụ thiết kế UI (UI 설계 도구 4총사):**
  1. **와이어프레임 (Wireframe):**
     - Bản phác thảo khung xương tĩnh ban đầu (`개략적인 레이아웃이나 뼈대`), dùng đường nét đơn giản, hình hộp để bố trí vị trí các thành phần cơ bản (Header, Menu, Body) mà chưa hề có màu sắc hay hình ảnh hoàn chỉnh.
  2. **목업 (Mockup):**
     - Mô hình dạng **TĨNH (`정적인 형태의 모형`)** được thiết kế đồ họa chi tiết giống hệt màn hình thật về màu sắc, font chữ, icon. Dùng để khách hàng duyệt mặt thị giác nhưng **hoàn toàn không có tương tác bấm chạy logic**.
  3. **스토리보드 (Storyboard):**
     - Tài liệu thiết kế hoàn chỉnh nhất gồm: **Wireframe + Nội dung giải thích chi tiết + Luồng di chuyển giữa các trang (`페이지 이동 흐름`)**. Là kim chỉ nam tham khảo cuối cùng cho cả đội ngũ thiết kế và lập trình viên.
  4. **프로토타입 (Prototype):**
     - Mô hình dạng **ĐỘNG (`동적인 형태의 모형`)** có khả năng tương tác bấm thử thực tế, mô phỏng sinh động hành vi của ứng dụng để kiểm thử nghiệm thu trải nghiệm người dùng trước khi code chính thức.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Công cụ thiết kế UI nào là mô hình tĩnh, có đồ họa chi tiết nhưng không bấm tương tác được?"* -> **목업 (Mockup)**, không phải Prototype.
  - **Bẫy 2:** *"Tài liệu nào mô tả chi tiết bố cục kèm theo luồng điều hướng trang (페이지 이동 흐름) làm căn cứ cho lập trình viên?"* -> **스토리보드 (Storyboard)**.
  - **Bẫy 3:** *"Cử chỉ dùng 2 ngón tay chụm lại hoặc mở rộng để zoom màn hình gọi là gì?"* -> **Pinch (핀치)**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Wireframe khung xương, Mockup tĩnh đẹp, Storyboard luồng trang, Prototype động bấm thử; Pinch hai ngón phóng to thu nhỏ".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Quy trình phối hợp 4 công cụ trong một dự án UX/UI chuẩn:**
  $$\text{Wireframe (Vẽ khung giấy/Balsamiq)} \rightarrow \text{Mockup (Vẽ Figma đẹp)} \rightarrow \text{Storyboard (Ghi chú luồng click)} \rightarrow \text{Prototype (Tạo link tương tác test)}$$
- **So sánh Drag và Flick:**
  - `Drag` có chủ đích di chuyển một vật thể từ tọa độ A đến tọa độ B, ngón tay kiểm soát vật thể đến khi dừng lại.
  - `Flick` tận dụng lực quán tính (Inertia), ngón tay vuốt dứt khoát một đường rồi rời màn hình ngay, nội dung tiếp tục trôi theo quán tính rồi mới dừng lại.

### 복습 체크리스트
- [ ] Phân biệt được đặc trưng của 4 loại UI: CLI, GUI, NUI, OUI.
- [ ] Nhớ tên và hành vi của 7 cử chỉ cảm ứng di động: Tap, Double Tap, Drag, Pan, Press, Flick, Pinch.
- [ ] Phân biệt tuyệt đối giữa Wireframe (khung xương), Mockup (tĩnh đẹp), Storyboard (luồng trang), và Prototype (động tương tác).
- [ ] Nhận diện được công cụ phù hợp trong từng câu hỏi tình huống đề thi.
