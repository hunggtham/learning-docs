# 197. 분산 데이터베이스의 장단점 (Distributed DB Pros/Cons)

## 학습 목표 (Mục tiêu)
- Phân tích toàn diện 8 ưu điểm kỹ thuật của Cơ sở dữ liệu phân tán (`분산 데이터베이스의 장점`): Tính tự trị cục bộ cao (`지역 자치성`), Nâng cao khả năng chia sẻ dữ liệu, Hiệu năng hệ thống vượt trội, Độ tin cậy và tính sẵn sàng cao, Dễ dàng mở rộng dung lượng từng bước.
- Nhận diện 5 nhược điểm và thách thức lớn trong vận hành: Phần mềm DBMS phức tạp, Khó khăn trong thiết kế lược đồ phân tán, Chi phí phát triển và truyền thông mạng gia tăng, Nguy cơ phát sinh lỗi tiềm ẩn.
- Hiểu rõ cơ chế giao thức Cam kết 2 pha (2PC - `2단계 커밋 규약 / Two-Phase Commit Protocol`) dùng để bảo đảm tính nguyên tử của giao dịch trên nhiều trạm phân tán.

## 핵심 키워드 (Từ khóa)
- 분산 데이터베이스 장단점 (Ưu nhược điểm CSDL phân tán / Distributed DB Pros and Cons)
- 지역 자치성 (Tính tự trị cục bộ / Local Autonomy)
- 신뢰성 및 가용성 (Độ tin cậy và Tính sẵn sàng / Reliability and Availability)
- 점진적 시스템 확장 (Mở rộng hệ thống từng bước / Incremental Expansion)
- 2단계 커밋 규약 (Giao thức Cam kết 2 pha / 2PC - Two-Phase Commit)
- 통신 비용 (Chi phí truyền thông mạng / Network Communication Cost)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([34-bai-hoc.md](34-bai-hoc.md), [35-bai-hoc.md](35-bai-hoc.md)):** Để thỏa mãn 4 đặc tính trong suốt (Vị trí, Nhân bản, Đồng thời, Sự cố), kiến trúc phân tán mang lại sự linh hoạt vượt bậc nhưng cũng đòi hỏi sự đánh đổi lớn về mặt chi phí và kiểm soát lỗi.
- **Tiếp nối sang bài sau ([37-bai-hoc.md](37-bai-hoc.md)):** Khía cạnh vật lý của hệ thống CSDL phân tán gắn liền mật thiết với các kiến trúc lưu trữ phần cứng hiện đại như DAS, NAS, SAN và SDS.

## 읽는 방법 (Cách đọc)
- Học thuộc 2 từ khóa đắt giá nhất của Ưu điểm: **지역 자치성 (Tự trị cục bộ)** và **점진적 확장 용이 (Mở rộng linh hoạt từng bước)**.
- Ghi nhớ nhược điểm lớn nhất: **소프트웨어 개발 및 처리 비용 증가 (Chi phí phát triển và chi phí xử lý tăng cao)**.
- Nắm vững vai trò của giao thức **2PC (Two-Phase Commit)**: Giải pháp sống còn để đảm bảo tính nguyên tử (Atomicity) khi một giao dịch ghi dữ liệu lên nhiều máy chủ phân tán.

---

## 197. 분산 데이터베이스의 장단점 (Distributed DB Pros/Cons)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng phân tích chi tiết Ưu điểm của CSDL phân tán (장점 8가지):**
  | Ưu điểm nổi bật | Thuật ngữ tiếng Hàn | Ý nghĩa kỹ thuật trong thực tế |
  |---|---|---|
  | **Tính tự trị cục bộ cao** | `지역 자치성이 높음` | Mỗi chi nhánh / trạm mạng có quyền tự chủ quản lý và tối ưu hóa dữ liệu phục vụ riêng cho nghiệp vụ của mình. |
  | **Tăng khả năng chia sẻ** | `자료의 공유성이 향상됨` | Dữ liệu ở trạm này có thể được chia sẻ an toàn cho các trạm khác trên toàn hệ thống thông qua mạng. |
  | **Kiểm soát phân tán** | `분산 제어가 가능함` | Tránh việc dồn toàn bộ quyền kiểm soát vào một điểm nghẽn duy nhất; tải quản lý được phân bổ đều. |
  | **Tăng hiệu năng hệ thống** | `시스템 성능이 향상됨` | Các truy vấn cục bộ được xử lý ngay tại trạm gần nhất, giảm độ trễ mạng và giảm tải cho máy chủ trung tâm. |
  | **Kháng lỗi máy chủ trung tâm** | `중앙 컴퓨터 장애 영향 차단` | Sự cố hỏng hóc tại một máy tính trung tâm không làm tê liệt toàn bộ hoạt động của các chi nhánh còn lại. |
  | **Độ tin cậy và tính sẵn sàng cao** | `신뢰성 및 가용성이 높음` | Dữ liệu được nhân bản lưu ở nhiều nơi, nếu một trạm bị mất điện thì hệ thống tự động chuyển sang đọc ở trạm khác. |
  | **Mở rộng dung lượng dễ dàng** | `점진적 시스템 용량 확장 용이` | Khi doanh nghiệp mở thêm chi nhánh mới, chỉ cần bổ sung thêm trạm mạng mới mà không cần đập đi xây lại hệ thống cũ. |
  | **Tính linh hoạt và hữu dụng** | `효용성과 융통성이 높음` | Thích ứng nhanh chóng với các thay đổi trong cấu trúc tổ chức doanh nghiệp phân tán. |

- **2. Bảng phân tích chi tiết Nhược điểm của CSDL phân tán (단점 5가지):**
  | Nhược điểm | Thuật ngữ tiếng Hàn | Thách thức kỹ thuật phải đối mặt |
  |---|---|---|
  | **Phần mềm DBMS phức tạp** | `DBMS 기능이 복잡함` | Hệ quản trị CSDL phải gánh thêm các mô-đun phân tán: quản lý danh mục phân tán, tối ưu hóa truy vấn phân tán. |
  | **Thiết kế CSDL khó khăn** | `데이터베이스 설계가 어려움` | Phải giải quyết các bài toán phân mảnh (ngang/dọc), bài toán cấp phát vị trí lưu trữ và chiến lược đồng bộ bản sao. |
  | **Tăng chi phí phát triển phần mềm** | `소프트웨어 개발 비용 증가` | Đòi hỏi đội ngũ kỹ sư có trình độ cao về mạng máy tính, thuật toán đồng thuận và kiến trúc chịu lỗi. |
  | **Tăng chi phí xử lý và truyền thông** | `처리 비용 및 통신 비용 증가` | Chi phí lưu lượng đường truyền mạng giữa các chi nhánh tăng vọt để đồng bộ các giao dịch cập nhật. |
  | **Gia tăng nguy cơ lỗi tiềm ẩn** | `잠재적 오류가 증가함` | Nguy cơ phân mảnh mạng (Network Partition), lỗi đứt cáp viễn thông, và bài toán xung đột phiên bản dữ liệu. |

- **3. Giao thức Cam kết 2 pha (2PC - Two-Phase Commit Protocol):**
  - **Pha 1 (Chuẩn bị - Prepare Phase):** Trạm điều phối (Coordinator) gửi yêu cầu `PREPARE` đến tất cả các trạm tham gia (Participants). Các trạm ghi nhật ký và gửi phản hồi `READY` (sẵn sàng) hoặc `ABORT` (thất bại).
  - **Pha 2 (Cam kết - Commit Phase):**
    - Nếu **TẤT CẢ** các trạm đều gửi `READY` $\rightarrow$ Trạm điều phối phát lệnh `GLOBAL COMMIT`.
    - Chỉ cần **MỘT TRẠM** gửi `ABORT` hoặc hết thời gian chờ $\rightarrow$ Trạm điều phối phát lệnh `GLOBAL ROLLBACK`.
- **주의/함정 (Bẫy đề thi trắc nghiệm):**
  - Đề hỏi: *"Ưu điểm nổi bật nhất giúp chi nhánh tự quản lý CSDL của riêng mình là gì?"* $\rightarrow$ Đáp án: **지역 자치성 (Local Autonomy / Tính tự trị cục bộ)**.
  - Đề hỏi: *"CSDL phân tán có làm giảm chi phí phát triển phần mềm không?"* $\rightarrow$ **KHÔNG, chi phí phát triển và chi phí truyền thông TĂNG LÊN (소프트웨어 개발 비용 증가)**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Định lý CAP trong CSDL phân tán:**
  - Một hệ thống phân tán chỉ có thể đồng thời thỏa mãn tối đa 2 trong 3 yếu tố:
    - **C (Consistency - Tính nhất quán):** Mọi nút mạng đều nhìn thấy cùng một dữ liệu tại cùng một thời điểm.
    - **A (Availability - Tính sẵn sàng):** Mọi yêu cầu gửi đến đều nhận được phản hồi thành công.
    - **P (Partition Tolerance - Tính chịu đựng phân mảnh mạng):** Hệ thống vẫn vận hành bình thường dù đường mạng bị đứt gãy giữa các cụm.

### 복습 체크리스트
- [ ] Kể tên 4 ưu điểm lớn nhất: 지역 자치성, 신뢰성/가용성, 중앙 장애 영향 차단, 점진적 확장.
- [ ] Kể tên các nhược điểm: DBMS phức tạp, thiết kế khó, chi phí phát triển và truyền thông tăng.
- [ ] Trình bày cơ chế 2 pha của giao thức 2PC (Prepare phase và Commit phase).
- [ ] Hiểu được mối liên hệ giữa CSDL phân tán và định lý CAP.
