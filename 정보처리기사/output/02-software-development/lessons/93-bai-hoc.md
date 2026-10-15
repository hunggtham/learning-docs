# 088-2: 데이터베이스 (Database) & 089: DBMS

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và 4 đặc trưng cốt lõi của cơ sở dữ liệu (데이터베이스의 4대 특징 - ISOS): Dữ liệu tích hợp (통합된 데이터), Dữ liệu lưu trữ (저장된 데이터), Dữ liệu vận hành (운영 데이터), và Dữ liệu dùng chung (공용 데이터).
- Hiểu rõ 4 đặc tính vận hành thực tế của cơ sở dữ liệu: Tính tiếp cận theo thời gian thực (실시간 접근성), Tính liên tục biến đổi (계속적인 변화), Tính chia sẻ đồng thời (동시 공용), và Tính tham chiếu theo nội dung (내용에 의한 참조).
- Ôn tập củng cố 3 chức năng chính của DBMS: Chức năng định nghĩa (정의), Chức năng thao tác (조작), và Chức năng điều khiển (제어).

## 핵심 키워드 (Từ khóa)
- 데이터베이스 (Database)
- 통합된 데이터 (Integrated Data / 중복 배제)
- 저장된 데이터 (Stored Data / 컴퓨터 매체 저장)
- 운영 데이터 (Operational Data / 고유 업무 필수 자료)
- 공용 데이터 (Shared Data / 공동 소유)
- 실시간 접근성 (Real-time Accessibility)
- 계속적인 변화 (Continuous Evolution)
- 동시 공용 (Concurrent Sharing)
- 내용에 의한 참조 (Content Reference)

## 선행·연결 개념 (Kiến thức liên kết)
- [92-bai-hoc.md](92-bai-hoc.md): Kỹ thuật tái sử dụng phần mềm.
- [94-bai-hoc.md](94-bai-hoc.md): Tính độc lập của dữ liệu trong cơ sở dữ liệu.
- [81-bai-hoc.md](81-bai-hoc.md): Hệ thống quản lý cơ sở dữ liệu (DBMS).

## 읽는 방법 (Cách đọc)
- Ghi nhớ thần chú viết tắt **ISOS** cho 4 đặc trưng của cơ sở dữ liệu:
  - **I (Integrated - 통합):** Dữ liệu được gom lại và **loại bỏ tối đa sự trùng lặp (중복의 최소화)**.
  - **S (Stored - 저장):** Dữ liệu được lưu trữ vĩnh viễn trên **các thiết bị nhớ máy tính** (ổ đĩa từ, SSD).
  - **O (Operational - 운영):** Dữ liệu thiết yếu **phục vụ trực tiếp cho hoạt động nghiệp vụ của tổ chức**, không phải dữ liệu rác hay dữ liệu thừa.
  - **S (Shared - 공용):** Dữ liệu được **chia sẻ dùng chung đồng thời** cho nhiều người dùng và nhiều ứng dụng khác nhau.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng 4 đặc trưng định nghĩa cơ sở dữ liệu (ISOS):**

| Thuật ngữ | Tiếng Hàn | Bản chất chuẩn đề thi |
| :--- | :--- | :--- |
| **Integrated Data** | **통합된 데이터** | Dữ liệu được chuẩn hóa, **loại trừ trùng lặp có nguyên tắc (중복 배제)** để duy trì tính nhất quán |
| **Stored Data** | **저장된 데이터** | Dữ liệu được lưu trữ trên **phương tiện lưu trữ điện tử (컴퓨터 저장 매체)** để truy xuất lâu dài |
| **Operational Data** | **운영 데이터** | Dữ liệu **cốt lõi phục vụ vận hành nghiệp vụ của tổ chức (업무 수행에 반드시 필요한 자료)** |
| **Shared Data** | **공용 데이터** | Dữ liệu được **nhiều ứng dụng và người dùng cùng sở hữu và khai thác đồng thời (공동 소유)** |

- **Bảng 4 đặc tính vận hành của hệ thống cơ sở dữ liệu:**

| Đặc tính vận hành | Tên tiếng Hàn & Anh | Diễn giải kỹ thuật thực tế |
| :--- | :--- | :--- |
| **Truy cập thời gian thực** | **실시간 접근성 (Real-time Accessibility)** | Đáp ứng truy vấn của người dùng ngay lập tức trong vài phần giây |
| **Liên tục biến đổi** | **계속적인 변화 (Continuous Evolution)** | Luôn phản ánh đúng trạng thái thực tế thông qua các thao tác Insert, Update, Delete liên tục |
| **Chia sẻ đồng thời** | **동시 공용 (Concurrent Sharing)** | Nhiều người dùng có thể cùng truy cập một bảng dữ liệu tại cùng một thời điểm mà không bị khóa nghẽn |
| **Tham chiếu theo nội dung** | **내용에 의한 참조 (Content Reference)** | Dữ liệu được tìm kiếm dựa trên **giá trị nội dung (값/내용)** của các trường thay vì dựa vào địa chỉ vật lý ô nhớ |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tham chiếu theo nội dung trong SQL:**
  - Khi viết `SELECT * FROM student WHERE gpa > 3.5;`, câu lệnh không cần biết bản ghi nằm ở cung đĩa nào, mà DBMS tự quét và lọc theo giá trị nội dung `gpa > 3.5`.
  - Đây chính là sự khác biệt căn bản giữa cơ sở dữ liệu quan hệ với cấu trúc bộ nhớ truyền thống truy cập theo con trỏ địa chỉ.

### 복습 체크리스트
- [ ] Đọc vanh vách 4 chữ ISOS: 통합 (Integrated), 저장 (Stored), 운영 (Operational), 공용 (Shared).
- [ ] Nhớ chữ O là Operational (vận hành thiết yếu), không phải Optional.
- [ ] Kể tên 4 đặc tính vận hành: 실시간 접근성, 계속적인 변화, 동시 공용, 내용에 의한 참조.
- [ ] Phân biệt rõ tham chiếu theo nội dung (giá trị dữ liệu) với tham chiếu theo địa chỉ ô nhớ.
