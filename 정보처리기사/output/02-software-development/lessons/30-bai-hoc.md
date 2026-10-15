# 088: 해싱 (Hashing) & 088-1: 데이터저장소 (Data Storage)

## 학습 목표 (Mục tiêu)
- Nắm vững hệ thống thuật ngữ cấu trúc của Bảng băm: Khóa (Key), Hàm băm (Hash Function), Địa chỉ gốc (Home Address), Thùng chứa (Bucket), Khe cắm (Slot), Từ đồng nghĩa (Synonym), Đụng độ (Collision) và Tràn thùng (Overflow).
- Phân biệt rạch ròi giữa Kho lưu trữ dữ liệu logic (논리 데이터저장소) và Kho lưu trữ dữ liệu vật lý (물리 데이터저장소).
- Tổng hợp toàn diện các chỉ số dung lượng bảng băm và nguyên lý ánh xạ dữ liệu từ mô hình quan niệm xuống thiết bị lưu trữ phần cứng.

## 핵심 키워드 (Từ khóa)
- 해싱 (Hashing)
- 버킷 (Bucket) & 슬롯 (Slot)
- 충돌 (Collision) & 동의어 (Synonym) & 오버플로 (Overflow)
- 제산법 (Division Method: $K \pmod M$)
- 논리 데이터저장소 (Logical Data Storage)
- 물리 데이터저장소 (Physical Data Storage)

## 선행·연결 개념 (Kiến thức liên kết)
- [26-bai-hoc.md](26-bai-hoc.md): Giải thuật tìm kiếm và các phương pháp giải quyết đụng độ bảng băm.
- [28-bai-hoc.md](28-bai-hoc.md): Các hàm băm kinh điển (Division, Mid-square, Folding).
- [31-bai-hoc.md](31-bai-hoc.md): 단위 모듈과 IPC (Inter-Process Communication).

## 읽는 방법 (Cách đọc)
- Phân biệt bộ ba thuật ngữ Hashing cực kỳ hay bị nhầm lẫn trong đề thi:
  - **Synonym (동의어):** Hai khóa khác nhau cho ra cùng một địa chỉ băm ($h(K_1) = h(K_2)$).
  - **Collision (충돌):** Hiện tượng hai khóa Synonym muốn chui vào cùng một Bucket.
  - **Overflow (오버플로):** Khi một Bucket đã đầy sạch Slot mà vẫn có khóa mới đòi chui vào.
- Phân biệt Logic vs Physical: Logic là cấu trúc quan hệ trên giấy tờ/schema; Physical là ổ cứng, sector, block, tablespace thực tế.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Hệ thống thuật ngữ giải phẫu Bảng băm (Hash Table Terminology):**

```
+--------------------------------------------------------+
| HASH TABLE                                             |
|                                                        |
| Bucket 0: [ Slot 1: Data A ] [ Slot 2: Empty  ]        |
| Bucket 1: [ Slot 1: Data B ] [ Slot 2: Data C ] (FULL) | <-- Overflow nếu thêm vào đây!
| Bucket 2: [ Slot 1: Empty  ] [ Slot 2: Empty  ]        |
+--------------------------------------------------------+
```

| Thuật ngữ | Tên tiếng Hàn & Anh | Định nghĩa chuẩn mực đề thi |
| :--- | :--- | :--- |
| **Hàm băm** | **해시 함수 (Hash Function)** | Hàm toán học biến đổi khóa tìm kiếm $K$ thành địa chỉ vật lý $h(K)$ |
| **Địa chỉ gốc** | **홈 주소 (Home Address)** | Giá trị địa chỉ trả về trực tiếp từ hàm băm $h(K)$ |
| **Thùng chứa** | **버킷 (Bucket)** | Một khối lưu trữ tương ứng với một địa chỉ băm, bên trong chia thành nhiều Slot |
| **Khe cắm** | **슬롯 (Slot)** | Một vị trí ô nhớ lưu trữ đúng 1 bản ghi dữ liệu bên trong Bucket |
| **Từ đồng nghĩa** | **동의어 (Synonym)** | **Tập hợp các khóa khác nhau nhưng có cùng địa chỉ băm**: $h(K_1) = h(K_2)$ |
| **Đụng độ** | **충돌 (Collision)** | **Hiện tượng 2 khóa khác nhau được ánh xạ vào cùng một Bucket** |
| **Tràn thùng** | **오버플로 (Overflow)** | Hiện tượng xảy ra khi một Bucket **không còn Slot trống nào** để chứa thêm bản ghi |

- **So sánh Kho lưu trữ dữ liệu Logic vs Vật lý:**

| Tiêu chí so sánh | 논리 데이터저장소 (Kho lưu trữ Logic) | 물리 데이터저장소 (Kho lưu trữ Vật lý) |
| :--- | :--- | :--- |
| **Bản chất** | Thiết kế cấu trúc dữ liệu, quan hệ giữa các thực thể và ràng buộc toàn vẹn | Thiết bị phần cứng và cấu trúc phân bổ khối nhớ thực tế |
| **Đối tượng quản lý** | Bảng (Table), Khóa chính (PK), Khóa ngoại (FK), Lược đồ (Schema), Khung nhìn (View) | Đĩa cứng HDD, Ổ SSD, SAN/NAS, Tablespace, Block, Extent, Phân vùng (Partition) |
| **Đặc trưng** | Độc lập với phần cứng máy tính (Tính độc lập dữ liệu) | Phụ thuộc vào hệ điều hành, hệ thống tệp tin (File System) và thông số phần cứng |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Mối liên hệ giữa Collision và Overflow:**
  - Nếu mỗi Bucket chỉ có **đúng 1 Slot** (1 Bucket = 1 Slot): Khi xảy ra Collision thì **đồng thời lập tức xảy ra Overflow**.
  - Nếu mỗi Bucket có **nhiều Slot** (ví dụ 4 Slot): Khi xảy ra Collision, bản ghi mới vẫn có thể được lưu an toàn vào Slot trống tiếp theo của cùng Bucket đó. Chỉ khi cả 4 Slot đều đã kín thì mới phát sinh hiện tượng Overflow.

### 복습 체크리스트
- [ ] Định nghĩa chính xác và phân biệt Synonym, Collision và Overflow.
- [ ] Nhớ mối quan hệ giữa Bucket (chứa nhiều Slot) và Slot (chứa 1 bản ghi).
- [ ] Khẳng định nếu Bucket có 1 Slot thì Collision luôn kéo theo Overflow.
- [ ] Phân biệt rõ 논리 데이터저장소 (Schema, Bảng, Quan hệ) và 물리 데이터저장소 (Ổ đĩa, Tablespace, Block).
