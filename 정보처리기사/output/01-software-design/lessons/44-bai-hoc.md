# 1. 회복 (Recovery)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và mục tiêu của cơ chế Phục hồi cơ sở dữ liệu (`회복 - Recovery`) khi xảy ra sự cố hỏng hóc phần cứng, phần mềm hoặc lỗi giao dịch.
- Phân biệt rõ bản chất của hai thao tác khôi phục cốt lõi: `REDO` (Làm lại các thay đổi sau khi giao dịch đã Commit) và `UNDO` (Hủy bỏ các thay đổi của giao dịch chưa Commit).
- Thuộc nằm lòng 4 kỹ thuật phục hồi kinh điển: Cập nhật trì hoãn (`연기 갱신`), Cập nhật tức thời (`즉각 갱신`), Điểm kiểm tra (`검사점 기법 - Checkpoint`), và Phân trang bóng (`그림자 페이징 - Shadow Paging`).

## 핵심 키워드 (Từ khóa)
- 회복 (Phục hồi CSDL / Recovery)
- REDO (Làm lại / Tái thực thi giao dịch đã Commit)
- UNDO (Hủy bỏ / Khôi phục trạng thái ban đầu của giao dịch chưa Commit)
- 연기 갱신 기법 (Deferred Update / Cập nhật trì hoãn / Chỉ REDO)
- 즉각 갱신 기법 (Immediate Update / Cập nhật tức thời / REDO + UNDO)
- 검사점 기법 (Checkpoint / Checkpoint Log)
- 그림자 페이징 (Shadow Paging / Shadow Page Table)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([6. SQL과 객체, 시스템 개념](43-bai-hoc.md)):** Sau khi nắm vững 4 tính chất ACID của giao dịch (đặc biệt là Tính nguyên tử và Tính bền vững), bài này đi sâu vào giải pháp kỹ thuật giúp CSDL duy trì tính toàn vẹn đó khi gặp sự cố.
- **Tiếp nối sang bài sau ([2. Commit & Rollback 연산](45-bai-hoc.md)):** Khảo sát chi tiết hai câu lệnh điều khiển giao dịch cơ sở: `COMMIT` và `ROLLBACK` cùng điểm lưu tạm `SAVEPOINT`.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để nhớ quy tắc vàng thi trắc nghiệm: Cập nhật trì hoãn (연기 갱신) CHỈ DÙNG REDO (không cần UNDO vì chưa ghi đĩa); Cập nhật tức thời (즉각 갱신) PHẢI DÙNG CẢ REDO VÀ UNDO.
- Đọc TẦNG B để hiểu cơ chế Checkpoint giúp DBMS không phải quét ngược toàn bộ tệp nhật ký Log từ thời điểm khởi tạo hệ thống.

---

## 1. 회복 (Recovery)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **개념 (Định nghĩa Phục hồi CSDL):**
  - Là quá trình khôi phục cơ sở dữ liệu về trạng thái nhất quán và chính xác gần nhất trước khi xảy ra sự cố hỏng hóc (mất điện, lỗi đĩa cứng, lỗi phần mềm).
- **2 thao tác phục hồi cốt lõi trong tệp nhật ký (로그 - Log):**
  - `REDO (Làm lại)`:
    - Áp dụng cho các giao dịch **đã ghi xong bản ghi `[COMMIT]` vào Log** trước thời điểm sự cố nhưng dữ liệu trên đĩa cứng chưa kịp cập nhật hoàn tất. DBMS sẽ đọc Log và ghi lại toàn bộ các thay đổi đó xuống đĩa.
  - `UNDO (Hủy bỏ / Quay lui)`:
    - Áp dụng cho các giao dịch **chưa có bản ghi `[COMMIT]` trong Log** tại thời điểm sự cố. DBMS sẽ đọc Log ngược từ dưới lên và hoàn trả lại các giá trị ban đầu trước khi giao dịch bắt đầu chạy.
- **4 kỹ thuật phục hồi cơ sở dữ liệu kinh điển:**
  1. **연기 갱신 기법 (Deferred Update - Kỹ thuật cập nhật trì hoãn):**
     - Mọi thay đổi của giao dịch chỉ được ghi tạm thời vào tệp nhật ký (Log); việc ghi dữ liệu thực sự xuống cơ sở dữ liệu trên đĩa cứng **bị trì hoãn cho đến khi giao dịch hoàn tất và Commit thành công**.
     - **Điểm thi then chốt:** Khi xảy ra sự cố, **CHỈ CẦN THỰC HIỆN THAO TÁC REDO (`REDO만 수행`), TUYỆT ĐỐI KHÔNG CẦN UNDO** vì dữ liệu chưa hề được ghi vào CSDL trên đĩa.
  2. **즉각 갱신 기법 (Immediate Update - Kỹ thuật cập nhật tức thời):**
     - Mọi thay đổi của giao dịch được ghi đồng thời vào tệp nhật ký Log và ghi ngay lập tức xuống cơ sở dữ liệu trên đĩa cứng trong quá trình giao dịch đang thực thi.
     - **Điểm thi then chốt:** Khi xảy ra sự cố, **PHẢI THỰC HIỆN CẢ HAI THAO TÁC: REDO VÀ UNDO (`REDO와 UNDO를 모두 수행`)**. Giao dịch đã commit thì REDO, giao dịch dở dang chưa commit thì UNDO.
  3. **검사점 기법 (Checkpoint - Kỹ thuật điểm kiểm tra):**
     - Định kỳ, DBMS ghi một bản ghi Checkpoint vào Log và đồng bộ toàn bộ bộ đệm (Buffer) xuống đĩa cứng.
     - **Lợi ích:** Khi phục hồi, hệ thống chỉ cần quét Log từ thời điểm Checkpoint gần nhất trở lại đây, **rút ngắn đáng kể thời gian phục hồi** so với việc phải quét từ đầu file Log.
  4. **그림자 페이징 기법 (Shadow Paging - Kỹ thuật phân trang bóng):**
     - Duy trì 2 bảng trang: Bảng trang hiện hành (Current Page Table) và Bảng trang bóng (Shadow Page Table). Khi giao dịch thất bại, chỉ cần trỏ con trỏ lại Bảng trang bóng ban đầu để phục hồi tức thì mà không cần dùng Log.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Kỹ thuật Cập nhật trì hoãn (연기 갱신) cần thực hiện cả thao tác REDO và UNDO?"* -> **Sai hoàn toàn**. **Chỉ cần REDO (REDO만 필요)**, không cần UNDO.
  - **Bẫy 2:** *"Kỹ thuật nào giúp giảm bớt lượng tệp Log phải quét khi phục hồi sau sự cố?"* -> **검사점 기법 (Checkpoint)**.
  - **Bẫy 3:** *"Kỹ thuật nào duy trì hai bảng trang và không cần dùng đến tệp Log để khôi phục?"* -> **그림자 페이징 (Shadow Paging)**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Commit rồi thì REDO, dở dang thì UNDO; Trì hoãn chỉ REDO, Tức thời cả hai, Checkpoint rút ngắn thời gian, Phân trang bóng dùng 2 bảng".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tình huống xác định REDO hay UNDO từ tệp nhật ký (Log Trace):**
  - Cho tệp Log ghi lại trình tự các sự kiện trước khi mất điện:
    - $T_1$: Bắt đầu $\rightarrow$ Ghi dữ liệu $\rightarrow$ `COMMIT`
    - $T_2$: Bắt đầu $\rightarrow$ Ghi dữ liệu $\rightarrow$ (Sự cố mất điện xảy ra!)
  - **Phân tích:**
    - Giao dịch $T_1$ đã có chữ `COMMIT` trong Log $\rightarrow$ Hệ thống thực hiện **REDO cho $T_1$**.
    - Giao dịch $T_2$ chưa có chữ `COMMIT` trong Log $\rightarrow$ Hệ thống thực hiện **UNDO cho $T_2$**.

### 복습 체크리스트
- [ ] Phân biệt được mục đích của REDO (làm lại sau commit) và UNDO (hủy bỏ trước commit).
- [ ] Nhớ chắc chắn: 연기 갱신 chỉ dùng REDO; 즉각 갱신 dùng cả REDO và UNDO.
- [ ] Nêu được lợi ích của 검사점 기법 (Checkpoint) trong việc giảm thời gian phục hồi.
- [ ] Định nghĩa được cơ chế của 그림자 페이징 (Shadow Paging) với 2 bảng trang.
