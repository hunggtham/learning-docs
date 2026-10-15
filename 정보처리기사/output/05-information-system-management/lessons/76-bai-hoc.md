# 1. 메모리 버퍼 오버플로 (Memory Buffer Overflow / Tràn bộ đệm bộ nhớ)

## 학습 목표 (Mục tiêu)
- Nắm vững cơ chế phát sinh lỗ hổng tràn bộ đệm bộ nhớ (Memory Buffer Overflow) trên cấu trúc vùng nhớ ngăn xếp (Stack) và đống (Heap).
- Phân tích hậu quả bảo mật khi kẻ tấn công ghi đè lên địa chỉ quay về của hàm (Return Address / EIP) để chiếm quyền điều khiển luồng thực thi chương trình.
- Làm chủ các kỹ thuật lập trình an toàn và cơ chế bảo vệ ở cấp độ trình biên dịch / phần cứng: Hàm an toàn có giới hạn kích thước, Stack Guard (Canary), ASLR, và DEP/NX.

## 핵심 키워드 (Từ khóa)
- **버퍼 오버플로 (Buffer Overflow)**: Ghi dữ liệu vượt quá kích thước vùng đệm được cấp phát, ghi đè lên các vùng nhớ liền kề.
- **반환 주소 (Return Address / EIP)**: Mục tiêu ghi đè của kẻ tấn công nhằm chuyển hướng thực thi tới mã độc (Shellcode).
- **스택 가드 (Stack Guard / Canary)**: Giá trị kiểm tra ngẫu nhiên đặt trước Return Address để phát hiện hành vi ghi tràn.
- **ASLR (Address Space Layout Randomization)**: Ngẫu nhiên hóa không gian địa chỉ bộ nhớ mỗi lần chương trình chạy.
- **DEP/NX (Data Execution Prevention)**: Cấm thực thi mã trên vùng dữ liệu Stack và Heap.

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [32-bai-hoc.md](32-bai-hoc.md) (Lỗ hổng bảo mật và chức năng an toàn).
- Liên kết với [80-bai-hoc.md](80-bai-hoc.md) (Sử dụng API không an toàn dẫn tới tràn bộ đệm).
- Liên kết với [04-programming-language/70-bai-hoc.md](../../04-programming-language/lessons/70-bai-hoc.md) (Lỗ hổng bảo mật phần mềm).

## 읽는 방법 (Cách đọc)
- Đi thi chú ý nhận diện nhanh:
  - "Lỗ hổng xảy ra khi ghi dữ liệu vượt quá kích thước vùng nhớ được cấp phát" $\rightarrow$ **메모리 버퍼 오버플로 (Buffer Overflow)**.
  - "Kỹ thuật chèn giá trị kiểm tra (Canary) trước địa chỉ quay về của hàm" $\rightarrow$ **스택 가드 (Stack Guard)**.
  - "Kỹ thuật ngẫu nhiên hóa vị trí nạp Stack, Heap, Thư viện trong bộ nhớ" $\rightarrow$ **ASLR**.
  - "Ngăn chặn việc thực thi mã độc trên vùng nhớ dữ liệu" $\rightarrow$ **DEP / NX bit**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Cơ chế phát sinh Lỗ hổng Tràn bộ đệm
- **Nguyên nhân**: Trong các ngôn ngữ lập trình bậc thấp như C/C++, việc quản lý bộ nhớ được giao hoàn toàn cho lập trình viên mà không có cơ chế tự động kiểm tra biên mảng (Bounds Checking).
- Khi sử dụng các hàm sao chép không giới hạn kích thước đầu vào (như `gets`, `strcpy`), nếu người dùng nhập chuỗi dữ liệu dài hơn độ dài vùng nhớ đệm (Buffer) đã khai báo, phần dữ liệu thừa sẽ tràn qua ranh giới bộ đệm và ghi đè tuần tự lên:
  1. Con trỏ khung ngăn xếp cũ (Saved EBP / Frame Pointer).
  2. Địa chỉ quay về của hàm (**Return Address / EIP**).
- **Hậu quả**: Kẻ tấn công tính toán chính xác số byte cần tràn để ghi đè địa chỉ Return Address thành địa chỉ của đoạn mã độc (Shellcode) đã được nhúng sẵn trên Stack. Khi hàm kết thúc (lệnh `ret`), CPU sẽ nhảy thẳng vào thực thi Shellcode với đặc quyền của chương trình.

#### 2. Bảng các Biện pháp Phòng chống Toàn diện
| Cấp độ bảo vệ | Biện pháp kỹ thuật | Nguyên lý phòng thủ cốt lõi |
| :--- | :--- | :--- |
| **Mã nguồn (Lập trình an toàn)** | Sử dụng các hàm an toàn có kiểm soát độ dài | Thay thế `strcpy()` bằng `strncpy()`, `gets()` bằng `fgets()`, `sprintf()` bằng `snprintf()`; luôn kiểm tra chặt chẽ độ dài chuỗi trước khi xử lý |
| **Trình biên dịch (Compiler)** | **Stack Guard (Stack Canary)** | Chèn một giá trị số ngẫu nhiên bí mật (Canary) nằm ngay trước Return Address. Trước khi hàm thoát, kiểm tra giá trị Canary: nếu bị thay đổi thì hủy tiến trình ngay |
| **Hệ điều hành & CPU** | **ASLR (Address Space Layout Randomization)** | Mỗi lần chương trình khởi chạy, hệ điều hành sẽ nạp các phân vùng Stack, Heap và các thư viện liên kết động (`.dll`, `.so`) vào các địa chỉ RAM ngẫu nhiên khác nhau, khiến hacker không đoán được địa chỉ để nhảy |
| **Phần cứng vi xử lý (CPU)** | **DEP / NX (Data Execution Prevention / No-Execute)** | Đánh dấu thuộc tính cấm thực thi trên các trang bộ nhớ của Stack và Heap; CPU sẽ từ chối chạy bất kỳ lệnh nào nằm trên vùng nhớ dữ liệu |

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Sơ đồ ngăn xếp (Stack Frame) trước và sau khi bị tấn công tràn bộ đệm
```
[Trạng thái bình thường]
Đỉnh Stack ──► [Vùng đệm cục bộ (Buffer: 16 bytes)]
               [Giá trị kiểm tra Stack Canary]
               [Saved EBP (Frame Pointer cũ)]
Đáy Stack  ──► [RETURN ADDRESS (Địa chỉ quay về hàm main)]

[Trạng thái bị tấn công ghi tràn 32 bytes]
Đỉnh Stack ──► ['A' 'A' 'A' ... (Dữ liệu rác lấp đầy Buffer)]
               ['A' 'A' ... (Đè hỏng giá trị Canary!)]
               ['A' 'A' ... (Đè hỏng Saved EBP)]
Đáy Stack  ──► [ĐỊA CHỈ SHELLCODE CỦA HACKER] ◄─── (Ghi đè Return Address!)
```

---

### 복습 체크리스트
- [ ] Mục tiêu ghi đè quan trọng nhất của kẻ tấn công trong kỹ thuật khai thác tràn bộ đệm ngăn xếp là gì?
- [ ] Cơ chế Stack Guard (Canary) phát hiện hành vi tấn công tràn bộ đệm bằng cách nào?
- [ ] Công nghệ ASLR trong hệ điều hành bảo vệ bộ nhớ dựa trên nguyên lý kỹ thuật gì?
- [ ] Tính năng phần cứng DEP/NX ngăn chặn shellcode của hacker thực thi trên những vùng nhớ nào?
