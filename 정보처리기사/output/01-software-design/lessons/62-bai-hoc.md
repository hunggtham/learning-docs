# 6. 구조적 분석 도구 (Structured Analysis Tools)

## 학습 목표 (Mục tiêu)
- Nắm vững bộ 4 công cụ phân tích có cấu trúc truyền thống (`구조적 분석 기법 4대 도구`): Sơ đồ luồng dữ liệu (`DFD`), Từ điển dữ liệu (`DD`), Đặc tả tiến trình con (`소단위 명세서 - Mini-spec`), và Sơ đồ phân cấp `HIPO`.
- Thuộc nằm lòng vai trò của `소단위 명세서 (Mini-spec)` trong việc mô tả các tiến trình cơ sở (Primitive Process) ở tầng cuối cùng của DFD bằng Ngôn ngữ có cấu trúc hoặc Bảng quyết định.
- Khắc sâu 4 ký hiệu hình học của DFD và 6 toán tử của Từ điển dữ liệu DD để giải quyết trọn vẹn câu hỏi trắc nghiệm liên quan.

## 핵심 키워드 (Từ khóa)
- 구조적 분석 도구 (Công cụ phân tích có cấu trúc / Structured Analysis Tools)
- 자료 흐름도 (Data Flow Diagram - DFD)
- 자료 사전 (Data Dictionary - DD)
- 소단위 명세서 (Mini-spec / Process Specification / 원시 프로세스 / Primitive Process)
- 구조적 언어 / 의사결정표 (Structured English / Decision Table)
- HIPO (Hierarchy plus Input-Process-Output)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([4. 운영 환경 구축 고려사항](61-bai-hoc.md)):** Sau khi xem xét hạ tầng máy chủ và lưu trữ, bài này hệ thống hóa các công cụ mô hình hóa phân tích có cấu trúc.
- **Tiếp nối sang bài sau ([10. 소프트웨어 설계 원리](63-bai-hoc.md)):** Chuyển từ công cụ phân tích sang các nguyên lý thiết kế phần mềm cốt lõi (Trừu tượng hóa, Mô-đun hóa, Che giấu thông tin, Tinh chỉnh từng bước).

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để nhớ định nghĩa của Mini-spec: dùng để mô tả các tiến trình lá không thể phân rã thêm (원시 프로세스) của DFD bằng Structured English hoặc Decision Table.
- Đọc TẦNG B để theo dõi cấu trúc lồng ghép hoàn chỉnh giữa DFD $\rightarrow$ Mini-spec $\rightarrow$ DD $\rightarrow$ HIPO.

---

## 6. 구조적 분석 도구 (Structured Analysis Tools)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bộ 4 công cụ phân tích có cấu trúc kinh điển:**
  1. **자료 흐름도 (DFD - Data Flow Diagram):**
     - Mô hình hóa con đường dịch chuyển và biến đổi của luồng dữ liệu trong hệ thống.
     - **4 thành phần hình học:**
       - `프로세스 (Process - Tiến trình)`: Hình tròn (Yourdon/DeMarco) hoặc Chữ nhật bo góc (Gane/Sarson).
       - `자료 흐름 (Data Flow - Luồng dữ liệu)`: Mũi tên chỉ hướng dịch chuyển.
       - `자료 저장소 (Data Store - Kho dữ liệu)`: Hai đường thẳng song song.
       - `단말 (Terminator - Tác nhân ngoài)`: Hình chữ nhật.
     - *Nguyên tắc:* Tuyệt đối không biểu diễn luồng điều khiển thời gian (không có điều kiện rẽ nhánh hay vòng lặp).
  2. **자료 사전 (DD - Data Dictionary - Từ điển dữ liệu):**
     - Giải thích và định nghĩa chi tiết cấu trúc dữ liệu của các luồng và kho dữ liệu trong DFD (`메타데이터`).
     - **6 ký hiệu toán tử:**
       - `=`: `정의 (is composed of)`
       - `+`: `연결 (and)`
       - `( )`: `생략 (optional)`
       - `[ | ]`: `선택 (or)`
       - `{ }`: `반복 (iteration)`
       - `* *`: `설명 / 주석 (comment)`
  3. **소단위 명세서 (Mini-spec / Process Specification - Đặc tả tiến trình con):**
     - **Khái niệm:** Dùng để mô tả chi tiết logic xử lý cụ thể của các **Tiến trình cơ sở (`원시 프로세스 - Primitive Process`)** nằm ở tầng lá thấp nhất của DFD mà không thể tiếp tục chia nhỏ phân rã thêm được nữa.
     - **Công cụ biểu diễn:** Thường sử dụng **Ngôn ngữ có cấu trúc (`구조적 언어 - Structured English`)**, **Bảng quyết định (`의사결정표 - Decision Table`)**, hoặc Cây quyết định (`의사결정나무 - Decision Tree`).
  4. **HIPO (Hierarchy plus Input-Process-Output):**
     - Công cụ tài liệu hóa và mô hình hóa phân cấp chức năng theo hướng từ trên xuống (`하향식`).
     - **3 loại biểu đồ:** `가시적 도표 (Visual TOC)`, `총체적 도표 (Overview Diagram)`, và `세부적 도표 (Detail Diagram)`.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Công cụ nào dùng để mô tả logic của các tiến trình cơ sở (Primitive Process) trong DFD?"* -> **소단위 명세서 (Mini-spec / Process Specification)**.
  - **Bẫy 2:** *"Bảng quyết định (Decision Table) và Ngôn ngữ có cấu trúc (Structured English) được dùng chủ yếu trong công cụ nào?"* -> **소단위 명세서 (Mini-spec)**.
  - **Bẫy 3:** *"DFD có biểu diễn vòng lặp và logic điều khiển rẽ nhánh không?"* -> **Hoàn toàn KHÔNG**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Phân tích cấu trúc có bộ 4: DFD luồng dữ liệu, DD giải nghĩa cấu trúc, Mini-spec tả logic tiến trình lá bằng Bảng quyết định, HIPO phân cấp Top-down".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Ví dụ về Mini-spec sử dụng Structured English:**
  - Với một tiến trình nguyên thủy `Tính_Giảm_Giá` trên DFD:
    ```text
    IF Khách_Hàng_VIP = True THEN
        IF Tổng_Tiền >= 1.000.000 THEN
            Tỷ_Lệ_Giảm = 0.15
        ELSE
            Tỷ_Lệ_Giảm = 0.10
        ENDIF
    ELSE
        Tỷ_Lệ_Giảm = 0.05
    ENDIF
    Tiền_Giảm = Tổng_Tiền * Tỷ_Lệ_Giảm
    ```
  - Cách viết này giúp lập trình viên cài đặt thuật toán chính xác 100% theo đúng logic nghiệp vụ phân tích mà không bị hiểu sai lệch.

### 복습 체크리스트
- [ ] Kể tên đầy đủ 4 công cụ phân tích có cấu trúc: DFD, DD, Mini-spec, HIPO.
- [ ] Định nghĩa đúng vai trò của 소단위 명세서 (Mini-spec) với tiến trình nguyên thủy (Primitive Process).
- [ ] Nhớ 3 công cụ viết Mini-spec: Structured English, Decision Table, Decision Tree.
- [ ] Vẽ đúng 4 hình học của DFD và 6 ký hiệu của Từ điển dữ liệu DD.
