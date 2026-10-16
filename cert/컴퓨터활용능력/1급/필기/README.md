# 컴퓨터활용능력 1급 필기 — Tổng quan & Lộ trình lý thuyết

Kỳ thi 컴퓨터활용능력 1급 (Tin học văn phòng cấp độ 1) do Phòng Thương mại và Công nghiệp Hàn Quốc (KORCHAM - 대한상공회의소) chủ trì là chứng chỉ tin học ứng dụng cấp quốc gia có độ khó và giá trị tuyển dụng cao nhất tại Hàn Quốc. Phần thi lý thuyết (필기) đóng vai trò là rào cản phân loại đầu tiên, đòi hỏi thí sinh không chỉ nắm vững thao tác phần mềm mà còn phải hiểu sâu sắc nguyên lý kiến trúc máy tính, thuật toán mảng, và cơ sở dữ liệu quan hệ.

---

## 1. Cấu trúc bài thi và tiêu chuẩn điểm đỗ

Bài thi lý thuyết 1급 được tổ chức theo hình thức trắc nghiệm trên máy tính (CBT - Computer Based Testing).

| Hạng mục | Quy cách chuẩn |
|---|---|
| **Số môn thi** | 3 môn (과목 1: 컴퓨터 일반, 과목 2: 스프레드시트 일반, 과목 3: 데이터베이스 일반) |
| **Số lượng câu hỏi** | 60 câu trắc nghiệm (mỗi môn 20 câu, 4 lựa chọn) |
| **Thời gian làm bài** | 60 phút (đồng hồ đếm ngược liên tục cho cả 3 môn, thí sinh tự do chuyển đổi giữa các câu hỏi) |
| **Thang điểm** | 100 điểm / môn (mỗi câu đúng tương ứng 5 điểm) |
| **Tiêu chuẩn điểm đỗ** | • Từng môn đạt từ **40 điểm** trở lên (tránh điểm liệt — 과락); • Điểm trung bình cả 3 môn đạt từ **60 điểm** trở lên (tổng điểm $\ge 180$) |
| **Điều kiện số câu đúng** | • Mỗi môn đúng tối thiểu **8 / 20 câu**; • Toàn bài đúng tối thiểu **36 / 60 câu** |

### Cơ chế điểm liệt (과락)

Thí sinh cần đặc biệt lưu ý cơ chế điểm liệt (과락 기준). Dù tổng điểm 2 môn còn lại đạt điểm tuyệt đối ($100 + 100 = 200$), nhưng nếu môn thứ ba chỉ đạt 35 điểm (đúng 7 câu), kết quả chung cuộc vẫn là **불합격 (Trượt)**.

- **Kịch bản trượt vì điểm liệt:** Môn 1: 85 điểm (17 câu), Môn 2: 70 điểm (14 câu), Môn 3: 35 điểm (7 câu) $\to$ Điểm trung bình là 63.3 điểm (vượt 60), nhưng trượt do Môn 3 dưới 40 điểm.
- **Kịch bản đỗ an toàn:** Môn 1: 75 điểm (15 câu), Môn 2: 60 điểm (12 câu), Môn 3: 65 điểm (13 câu) $\to$ Điểm trung bình 66.7 điểm, không môn nào dưới 40 $\to$ **합격 (Đỗ)**.

---

## 2. So sánh phạm vi kiến thức: 1급 và 2급

Sự khác biệt giữa cấp độ 1 (1급) và cấp độ 2 (2급) thể hiện ở cả số lượng môn thi và chiều sâu tư duy:

| Tiêu chí | 컴퓨터활용능력 2급 | 컴퓨터활용능력 1급 |
|---|---|---|
| **Số môn thi** | 2 môn (40 câu / 40 phút) | 3 môn (60 câu / 60 phút) |
| **Môn 1 (컴퓨터 일반)** | Khái niệm phần cứng cơ bản, thao tác Windows 10 thường nhật, Internet căn bản. | Kiến trúc vi xử lý chuyên sâu (Pipeline, Cache L1/L2/L3, RISC/CISC), quản lý bộ nhớ ảo (Paging, Segmentation, Thrashing), System Bus, cấu hình mảng đĩa RAID, Windows Registry 5 nhánh chính, Event Viewer, mô hình mạng OSI 7 tầng & TCP/IP, địa chỉ IPv4/IPv6, an toàn thông tin & mật mã học (PKI, AES, RSA, IPS/IDS), Cloud & Big Data. |
| **Môn 2 (스프레드시트 일반)** | Hàm cơ bản, định dạng ô, sắp xếp, lọc dữ liệu, Pivot Table căn bản, biểu đồ đơn giản. | Định dạng số tùy chỉnh nâng cao (`양수;음수;0;텍스트`, ký hiệu `#`, `0`, `?`, `@`, `*`), bản chất toán học của công thức mảng (`배열 수식`), hàm tìm kiếm ma trận (`INDEX`, `MATCH`, `OFFSET`), hàm tài chính dòng tiền (`PMT`, `PV`, `FV`, `RATE`, `NPER`), công cụ tối ưu hóa Solver (`해 찾기`), Calculated Field vs Calculated Item trong Pivot Table, lập trình VBA và mô hình đối tượng Excel. |
| **Môn 3 (데이터베이스 일반)** | **Không thi môn này.** | Toàn bộ nền tảng Cơ sở dữ liệu quan hệ (RDBMS) với Microsoft Access: Lý thuyết quan hệ (Tuple, Attribute, Degree, Cardinality), ràng buộc toàn vẹn thực thể và tham chiếu, chuẩn hóa CSDL (1NF $\to$ BCNF), thuộc tính trường Access (Input Mask 3 phần, Validation Rule), ngôn ngữ SQL (DDL & DML), cấu trúc Form & Report, hàm miền tổng hợp (`DLookup`, `DSum`), và Access VBA / đối tượng `DoCmd`. |

---

## 3. Hệ thống tài liệu trong thư mục

Bộ tài liệu được biên soạn đồng bộ, phân chia theo từng môn thi và khép lại bằng chiến lược tối ưu điểm số:

1. **[01 — 컴퓨터 일반 (Tin học đại cương & Kiến trúc hệ thống)](./01-컴퓨터-일반.md)**
   Hệ thống hóa toàn bộ phần cứng, kiến trúc CPU, phân cấp bộ nhớ, cơ chế hệ điều hành Windows, mạng truyền thông và an toàn thông tin.

2. **[02 — 스프레드시트 일반 (Bảng tính đại cương & Excel nâng cao)](./02-스프레드시트-일반.md)**
   Phân tích cơ chế công thức mảng, cú pháp định dạng số chuyên sâu, nhóm hàm tài chính và tra cứu ma trận, công cụ phân tích What-If và nền tảng lập trình VBA.

3. **[03 — 데이터베이스 일반 (Cơ sở dữ liệu đại cương & Microsoft Access)](./03-데이터베이스-일반.md)**
   Bao quát toàn diện mô hình RDBMS, quy trình chuẩn hóa dữ liệu, thiết kế bảng và biểu thức ràng buộc trong Access, cú pháp SQL chuẩn, và kiến trúc Form/Report.

4. **[90 — 필기 문제풀이 전략 (Chiến lược giải đề & phân loại bẫy KCCI)](./90-필기-문제풀이-전략.md)**
   Cung cấp sơ đồ phân bổ thời gian thực chiến 60 phút, nguyên tắc né bẫy đề thi kinh điển của KCCI, và phương pháp loại trừ phương án trắc nghiệm theo tư duy logic.

---

## 4. Ma trận trọng tâm ôn tập

```
                    ┌──────────────────────────────────────────────┐
                    │      컴퓨터활용능력 1급 필기 (60 câu)        │
                    └──────────────────────┬───────────────────────┘
                                           │
         ┌─────────────────────────────────┼─────────────────────────────────┐
         │ (20 câu)                        │ (20 câu)                        │ (20 câu)
         ▼                                 ▼                                 ▼
┌──────────────────┐             ┌──────────────────┐              ┌──────────────────┐
│ 01. 컴퓨터 일반  │             │02.스프레드시트일반│              │03.데이터베이스일반│
├──────────────────┤             ├──────────────────┤              ├──────────────────┤
│• CPU & Pipeline  │             │• Cú pháp 서식    │              │• RDBMS & Chuẩn hóa│
│• Cache & Bộ nhớ ảo│            │• Mã lỗi Excel    │              │• Input Mask 3 phần│
│• System Bus & RAID│            │• Công thức mảng  │              │• Cú pháp SQL chuẩn│
│• Registry & Logs │             │• PMT/PV/INDEX    │              │• Form & Report   │
│• OSI 7 tầng & IP │             │• Calculated Field│              │• Hàm miền DLookup│
│• PKI & Mật mã học│             │• Macro & VBA Code│              │• DoCmd & Sự kiện │
└──────────────────┘             └──────────────────┘              └──────────────────┘
```

- **Môn 1 (컴퓨터 일반):** Đòi hỏi độ bao quát rộng. Chiến lược học là lập bảng đối chiếu các cặp khái niệm (RISC vs CISC, Paging vs Segmentation, Symmetric vs Asymmetric Key, IPv4 vs IPv6).
- **Môn 2 (스프레드시트 일반):** Đòi hỏi sự chính xác tuyệt đối về cú pháp và logic toán học. Tránh học vẹt công thức; cần hiểu cơ chế ma trận và dấu âm/dương trong dòng tiền tài chính.
- **Môn 3 (데이터베이스 일반):** Đòi hỏi tư duy quan hệ và kiến trúc cơ sở dữ liệu. Điểm mấu chốt là phân biệt các tầng chuẩn hóa và cú pháp bộ lọc trong Access.
