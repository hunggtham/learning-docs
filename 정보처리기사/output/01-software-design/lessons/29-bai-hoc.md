# 7. 설계 도구 및 모듈화 심화 (Công cụ thiết kế & Mô-đun hóa chuyên sâu)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, đặc trưng và các quy tắc cấu trúc của Biểu đồ Nassi-Shneiderman (`N-S 차트 / NS Chart`).
- Khắc sâu 3 đặc điểm nhận diện sống còn của N-S Chart trong đề thi: Chỉ dùng 3 cấu trúc (Tuần tự, Lựa chọn, Lặp), **Tuyệt đối không dùng mũi tên (`화살표 없음`)**, và **Không sử dụng lệnh nhảy `GOTO`**.
- Hiểu rõ mục tiêu của nguyên lý Mô-đun hóa (`모듈화` - Modularity) trong việc kiểm soát độ phức tạp phần mềm và nâng cao tính độc lập của hệ thống.

## 핵심 키워드 (Từ khóa)
- N-S 차트 (Nassi-Shneiderman Chart / 상자 다이어그램)
- 화살표 없음 (Không sử dụng mũi tên / No Arrows)
- GOTO문 배제 (Loại trừ lệnh GOTO / No Goto Statements)
- 순차·선택·반복 (Tuần tự, Lựa chọn, Lặp lại / 3 cấu trúc cơ bản)
- 모듈화 (Mô-đun hóa / Modularity / 분할과 정복)
- 추상화 / 정보 은닉 (Trừu tượng hóa / Che giấu thông tin)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([1. 객체지향 설계 5대 원칙 (SOLID)](28-bai-hoc.md)):** Sau khi nắm 5 nguyên tắc thiết kế hướng đối tượng, bài này tìm hiểu các công cụ biểu diễn thuật toán có cấu trúc và nền tảng của kỹ thuật mô-đun hóa.
- **Tiếp nối sang bài sau ([3. 모듈](30-bai-hoc.md)):** Đi sâu vào việc đo lường độ độc lập của mô-đun thông qua Độ kết hợp (`결합도 - Coupling`) 6 cấp độ.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để ghi nhớ chắc chắn 3 điều cấm của N-S Chart: không mũi tên, không GOTO, chỉ gồm các hộp chữ nhật lồng nhau.
- Đọc TẦNG B để so sánh trực quan ưu nhược điểm giữa Flowchart truyền thống và N-S Chart trong việc ngăn ngừa mã nguồn "mì ăn liền" (Spaghetti Code).

---

## 7. 설계 도구 및 모듈화 심화 (Công cụ thiết kế & Mô-đun hóa chuyên sâu)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Biểu đồ Nassi-Shneiderman (N-S 차트 / 박스 다이어그램):**
  - **Khái niệm:** Là công cụ biểu diễn thuật toán và logic điều khiển chi tiết của phần mềm dưới dạng các hộp chữ nhật lồng nhau theo chuẩn lập trình có cấu trúc (Structured Programming).
  - **3 cấu trúc điều khiển cơ bản duy nhất:**
    1. `순차 구조 (Sequence Structure - Cấu trúc tuần tự)`: Các câu lệnh thực thi lần lượt từ trên xuống dưới theo thứ tự các ô hộp.
    2. `선택 / 조건 구조 (Selection Structure - Cấu trúc lựa chọn)`: Điều kiện If-Then-Else hoặc Switch-Case, chia hộp thành các tam giác hoặc ngăn rẽ nhánh.
    3. `반복 구조 (Iteration Structure - Cấu trúc lặp)`: Vòng lặp For/While, khối lệnh lặp được lồng gọn bên trong khung thân vòng lặp.
  - **3 đặc điểm thi trắc nghiệm kinh điển (Bắt buộc phải thuộc):**
    - **TUYỆT ĐỐI KHÔNG SỬ DỤNG MŨI TÊN (`화살표를 사용하지 않음`)**: Dòng điều khiển chỉ chảy tự nhiên từ đỉnh hộp xuống đáy hộp.
    - **LOẠI TRỪ HOÀN TOÀN LỆNH NHẢY GOTO (`GOTO문 사용을 배제함`)**: Cấu trúc khối hộp chặt chẽ ngăn cấm việc nhảy lung tung giữa các khối mã nguồn.
    - **CÁC KHỐI ĐƯỢC LỒNG NHAU RÕ RÀNG (`상자 안에 상자가 들어가는 계층적 표현`)**: Rất trực quan và dễ dàng ánh xạ trực tiếp 1-1 sang mã nguồn lập trình.
- **2. Nguyên lý Mô-đun hóa (모듈화 - Modularity):**
  - **Bản chất:** Áp dụng chiến lược "Chia để trị" (Divide and Conquer), phân tách một hệ thống phần mềm lớn, phức tạp thành các đơn vị mô-đun nhỏ hơn, có chức năng hoàn chỉnh và có thể biên dịch, kiểm thử độc lập.
  - **Lợi ích kỹ thuật:**
    - Giảm thiểu độ phức tạp (`복잡도 감소`), nâng cao tính dễ đọc và dễ hiểu của mã nguồn.
    - Tăng khả năng tái sử dụng (`재사용성 향상`) các hàm và thư viện dùng chung.
    - Cho phép phân công nhiều lập trình viên làm việc song song mà không bị giẫm chân lên nhau.
    - Giúp việc khoanh vùng lỗi, bảo trì và nâng cấp sửa đổi trở nên dễ dàng.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Biểu đồ N-S sử dụng mũi tên để biểu diễn luồng điều khiển rẽ nhánh phức tạp?"* -> **Sai hoàn toàn**. Biểu đồ N-S **tuyệt đối không dùng mũi tên (화살표 없음)**.
  - **Bẫy 2:** *"Có thể dùng lệnh GOTO trong biểu đồ N-S để nhảy ra khỏi vòng lặp lồng nhau?"* -> **Sai**. N-S Chart được tạo ra chính là để **loại bỏ hoàn toàn GOTO**.
  - **Bẫy 3:** *"Mô-đun hóa càng nhiều thì chi phí tích hợp (통합 비용) càng giảm?"* -> **Sai**. Mô-đun chia quá nhỏ thì chi phí phát triển mô-đun đơn lẻ giảm nhưng **chi phí tích hợp và giao tiếp giữa các mô-đun sẽ tăng vọt**. Do đó cần tìm điểm cân bằng tối ưu.
- **한 문장 설명 (Câu chốt ghi nhớ):** "N-S Chart là hộp chữ nhật không mũi tên, cấm tiệt GOTO; Mô-đun hóa chia để trị tăng tái sử dụng và giảm phức tạp".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **So sánh Flowchart truyền thống vs N-S Chart:**
  - **Lưu đồ truyền thống (Flowchart):** Dùng các hình thoi, hình chữ nhật và các mũi tên chỉ hướng nối lung tung. Điểm yếu lớn nhất là cho phép vẽ mũi tên nhảy ngược xuôi tùy tiện, tạo ra cấu trúc mã Spaghetti rất khó bảo trì và dễ sinh lỗi bộ nhớ.
  - **N-S Chart:** Buộc kỹ sư phải tư duy theo đúng 3 cấu trúc chuẩn hóa (Tuần tự, Lựa chọn, Lặp). Không thể vẽ một đường mũi tên nhảy xiên từ giữa vòng lặp này sang giữa hàm khác. Nhờ đó mã nguồn sinh ra luôn đạt chuẩn Clean Code.

### 복습 체크리스트
- [ ] Nhớ 3 đặc điểm kỹ thuật sống còn của N-S Chart: không mũi tên, không GOTO, chỉ gồm 3 cấu trúc (tuần tự, lựa chọn, lặp).
- [ ] Nhận diện được hình vẽ dạng hộp lồng nhau đặc thù của N-S Chart.
- [ ] Nêu được định nghĩa và 4 lợi ích của nguyên lý mô-đun hóa (Modularity).
- [ ] Hiểu được mối quan hệ đánh đổi giữa chi phí phát triển mô-đun và chi phí tích hợp.
