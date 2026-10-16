# 교착상태 및 임계구역 동기화 (Khóa chết & Đồng bộ hóa tiến trình)

## 학습 목표 (Mục tiêu)
- Nắm vững khái niệm Bế tắc (교착상태 - Deadlock) và thuộc lòng 4 điều kiện cần và đủ để phát sinh bế tắc theo khẩu quyết **상점비환** (Tương hỗ loại trừ, Chiếm giữ và chờ, Không thể trưng dụng, Chờ đợi vòng tròn).
- Phân biệt 4 chiến lược giải quyết bế tắc: Phòng ngừa (예방 - Prevention), Né tránh (회피 - Avoidance với Thuật toán Banker), Phát hiện (탐지 - Detection với Đồ thị RAG), và Phục hồi (회복 - Recovery).
- Thấu hiểu 3 yêu cầu bắt buộc của bài toán Miền găng (임계 구역 - Critical Section: Tương hỗ loại trừ, Tiến triển, Chờ đợi hữu hạn) và cơ chế vận hành của các giải thuật đồng bộ: Dekker, Peterson, Lamport Bakery và Semaphore ($P/V$ Operations).

## 핵심 키워드 (Từ khóa)
- 교착상태 4대 발생조건 (Deadlock 4 Conditions) — 상호 배제, 점유와 대기, 비선점, 환형 대기 (상점비환).
- 은행원 알고리즘 (Banker's Algorithm) — Thuật toán né tránh bế tắc dựa trên trạng thái an toàn (Safe State) của Dijkstra.
- 임계 구역 3대 조건 (Critical Section 3 Requirements) — 상호 배제 (Mutual Exclusion), 진행 (Progress), 유한 대기 (Bounded Waiting).
- 데커 & 피터슨 알고리즘 (Dekker & Peterson) — Giải thuật đồng bộ miền găng bằng phần mềm cho 2 tiến trình.
- 램포트 베이커리 (Lamport's Bakery Algorithm) — Giải thuật phát số thứ tự vào miền găng cho $N$ tiến trình.
- 세마포어 P/V 연산 (Semaphore P/V) — $P(S)$ giảm và chờ (Wait) vs $V(S)$ tăng và báo hiệu (Signal).

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Kế thừa từ `12-tien-trinh-luong-va-dieu-phoi-cpu.md`, khi các tiến trình và luồng cùng chạy tương tranh (Concurrency) và cạnh tranh tài nguyên hữu hạn của hệ thống.
- **Đang giải quyết gì (Current Problem):** Giải quyết câu hỏi: Tại sao hệ thống máy chủ bị treo cứng (Freeze/Hang) dù CPU không quá tải, và bằng cơ chế nào Hệ điều hành đảm bảo hai tiến trình không cùng ghi đè lên một vùng dữ liệu chung tại cùng một thời điểm.
- **Dùng đi đâu (Forward Handoff):** Tài nguyên cạnh tranh lớn nhất của các tiến trình trong hệ thống chính là không gian bộ nhớ RAM; các chiến lược cấp phát và bảo vệ bộ nhớ sẽ được trình bày ở bài `14-quan-ly-bo-nho-thuc-va-chien-luoc-cap-phat.md`.

## 읽는 방법 (Cách đọc)
- **Khẩu quyết 4 điều kiện Deadlock:** Bắt buộc phải thuộc lòng: **상·점·비·환** (상호 배제 $\rightarrow$ 점유와 대기 $\rightarrow$ 비선점 $\rightarrow$ 환형 대기). Cả 4 điều kiện này phải **đồng thời xảy ra** thì bế tắc mới xuất hiện; chỉ cần phá vỡ được 1 điều kiện là phòng ngừa được bế tắc.
- **Banker's Algorithm:** Cứ thấy chữ "Thuật toán Ngân hàng (은행원 알고리즘)" $\rightarrow$ Chọn ngay chiến lược **Né tránh (회피 - Avoidance)** và điều kiện **Trạng thái an toàn (안전 상태 - Safe State)**.
- **Semaphore:** $P(S)$ là trừ ($S = S - 1$) và đợi; $V(S)$ là cộng ($S = S + 1$) và nhả khóa.

---

## 교착상태 및 임계구역 동기화

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

- **핵심 원리 (Nguyên tắc cốt lõi):**
  - [한국어]: `교착상태 발생의 4대 필요충분조건은 상호 배제, 점유와 대기, 비선점, 환형 대기(상점비환)이다. 다익스트라의 은행원 알고리즘은 안전 상태를 유지하여 교착상태를 회피(Avoidance)한다. 세마포어에서 P연산은 자원을 획득(감소/대기)하고, V연산은 자원을 반납(증가/신호)한다.`
  - [Tiếng Việt]: 4 điều kiện cần và đủ phát sinh bế tắc là Tương hỗ loại trừ, Chiếm giữ và chờ, Không thể trưng dụng, Chờ đợi vòng tròn (상점비환). Thuật toán Banker của Dijkstra duy trì trạng thái an toàn để né tránh bế tắc (Avoidance). Trong Semaphore, thao tác P xin cấp phát tài nguyên (giảm/đợi) và thao tác V trả lại tài nguyên (tăng/báo hiệu).

- **1. Bảng 4 điều kiện cần và đủ phát sinh bế tắc (교착상태 4대 발생조건 - 상점비환):**

| Điều kiện bế tắc | Thuật ngữ Hàn / Anh | Bản chất cơ chế kỹ thuật |
| :--- | :--- | :--- |
| **1. Tương hỗ loại trừ** | **상호 배제** (Mutual Exclusion) | Tại một thời điểm, tài nguyên chỉ được sở hữu bởi **duy nhất 1 tiến trình**; tiến trình khác muốn dùng phải đợi. |
| **2. Chiếm giữ và chờ** | **점유와 대기** (Hold and Wait) | Tiến trình đang nắm giữ ít nhất 1 tài nguyên nhưng lại yêu cầu cấp phát thêm tài nguyên khác đang bị chiếm giữ. |
| **3. Không thể trưng dụng**| **비선점** (Non-preemption) | Tài nguyên đã cấp **không thể bị cưỡng chế thu hồi**; chỉ được giải phóng khi tiến trình sở hữu tự nguyện nhả ra. |
| **4. Chờ đợi vòng tròn** | **환형 대기** (Circular Wait) | Tồn tại một chuỗi các tiến trình chờ đợi lẫn nhau khép kín ($P_0 \rightarrow P_1 \rightarrow P_2 \rightarrow P_0$). |

- **2. Bảng 4 chiến lược giải quyết bế tắc (교착상태 해결 4대 방안):**

| Chiến lược | Thuật ngữ Hàn / Anh | Nguyên lý hành động | Cơ chế / Thuật toán tiêu biểu |
| :--- | :--- | :--- | :--- |
| **Phòng ngừa** | **예방** (Prevention) | Phá vỡ trước ít nhất 1 trong 4 điều kiện bế tắc (상점비환). | Đánh số thứ tự tài nguyên để phá Circular Wait; yêu cầu xin toàn bộ tài nguyên cùng lúc. |
| **Né tránh** | **회피** (Avoidance) | Đánh giá động trước khi cấp phát; chỉ cấp nếu duy trì **Safe State**. | **Thuật toán Ngân hàng kiểm toán (은행원 알고리즘 - Banker's Algorithm)** của Dijkstra. |
| **Phát hiện** | **탐지** (Detection) | Cho phép bế tắc xảy ra, định kỳ rà soát để phát hiện chu trình. | Sử dụng **Đồ thị cấp phát tài nguyên (자원 할당 그래프 - RAG)**. |
| **Phục hồi** | **회복** (Recovery) | Triệt tiêu bế tắc sau khi phát hiện để đưa hệ thống về bình thường. | Thu hồi tài nguyên cưỡng chế hoặc **Hủy bỏ tiến trình (Process Kill)** theo độ ưu tiên. |

- **3. Bảng 3 yêu cầu bắt buộc của giải pháp Miền găng (임계 구역 3대 조건):**

| Yêu cầu | Thuật ngữ Hàn / Anh | Nội dung quy định bắt buộc |
| :--- | :--- | :--- |
| **1. Tương hỗ loại trừ** | **상호 배제** (Mutual Exclusion) | **Không bao giờ có từ 2 tiến trình cùng nằm trong miền găng** tại một thời điểm. |
| **2. Tiến triển** | **진행** (Progress) | Khi không có tiến trình nào trong miền găng, việc chọn ai được vào kế tiếp **không được bị trì hoãn vô hạn**. |
| **3. Chờ đợi hữu hạn** | **유한 대기** (Bounded Waiting) | Mỗi tiến trình chỉ phải chờ đợi một số lần hữu hạn trước khi được vào miền găng; **chống đói CPU (Starvation)**. |

- **4. Bảng phân loại các giải thuật đồng bộ hóa tương hỗ loại trừ:**

| Tên giải thuật | Số lượng tiến trình | Cơ chế kỹ thuật chủ đạo chuẩn đề thi |
| :--- | :---: | :--- |
| **데커 (Dekker)** | 2 tiến trình | Giải thuật phần mềm đầu tiên; kết hợp biến cờ trạng thái (`flag`) và biến lượt ưu tiên (`turn`). |
| **피터슨 (Peterson)** | 2 tiến trình | Cải tiến gọn hơn Dekker; khi muốn vào, bật cờ và chủ động **gán lượt cho tiến trình kia (`turn = other`)**. |
| **램포트 베이커리 (Lamport)**| **$N$ tiến trình** | **Mô hình tiệm bánh mì:** Mỗi tiến trình rút một vé số thứ tự; số nhỏ nhất được vào miền găng trước. |
| **세마포어 (Semaphore)** | Đa tiến trình | Dùng biến nguyên $S$ với 2 hàm nguyên tử: **$P(S)$ giảm và đợi**, **$V(S)$ tăng và báo hiệu thức dậy**. |

- **주의/함정 (Bẫy đề thi):**
  - **Nhầm Banker sang Phòng ngừa:** Đề thi hỏi *"Thuật toán Banker thuộc chiến lược nào?"* $\rightarrow$ Đáp án đúng là **Né tránh (회피 - Avoidance)**, chọn Phòng ngừa (예방) là sai bẫy.
  - **Chi phí của chiến lược Phòng ngừa:** Phòng ngừa bế tắc làm lãng phí tài nguyên và làm giảm nghiêm trọng hiệu suất toàn hệ thống.
  - **Thao tác Semaphore:** $P$ là trừ ($S = S - 1$) và chờ nếu $S \le 0$; $V$ là cộng ($S = S + 1$) và giải phóng tiến trình khác.

- **한 문장 설명 (Câu chốt tự nhớ):**
  - *"상점비환 4 điều kiện khóa chết; Banker né tránh giữ Safe State; Semaphore nhớ kỹ P giảm đợi, V tăng nhả."*

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Sơ đồ ASCII 4 điều kiện bế tắc của Coffman (상점비환):

Năm 1971, Edward G. Coffman Jr. chứng minh rằng bế tắc hệ thống chỉ xảy ra khi và chỉ khi cả 4 điều kiện sau đồng thời xuất hiện:

```text
+--------------------------------------------------------------------------+
|              4 ĐIỀU KIỆN COFFMAN DẪN ĐẾN KHÓA CHẾT (DEADLOCK)            |
+--------------------------------------------------------------------------+
| 1. 상호 배제 (Mutual Exclusion)                                          |
|    Tài nguyên R1 không thể chia sẻ: Tại một thời điểm chỉ 1 tiến trình   |
|    được phép sử dụng.                                                    |
|    [Tiến trình P1] <====== [Tài nguyên R1] ======X [Tiến trình P2]       |
+--------------------------------------------------------------------------+
| 2. 점유와 대기 (Hold and Wait)                                           |
|    P1 đang nắm giữ ít nhất 1 tài nguyên R1, đồng thời yêu cầu cấp phát   |
|    thêm tài nguyên R2 mới mà tài nguyên này đang bị P2 chiếm giữ.        |
|    [Tiến trình P1] ===== Đang giữ =====> [Tài nguyên R1]                 |
|           |                                                              |
|           +======== Đang chờ đợi =====> [Tài nguyên R2]                  |
+--------------------------------------------------------------------------+
| 3. 비선점 (Non-preemption)                                               |
|    Hệ điều hành không thể cưỡng chế tước đoạt tài nguyên R2 từ P2.       |
|    Chỉ khi P2 tự nguyện giải phóng thì R2 mới được cấp cho tiến trình    |
|    khác.                                                                 |
+--------------------------------------------------------------------------+
| 4. 환형 대기 (Circular Wait)                                             |
|    Tồn tại chuỗi chờ đợi khép kín hình vòng tròn:                        |
|           ( P1 ) ---- Yêu cầu cấp phát ----> [ R2 ]                      |
|             ^                                   |                        |
|             |                                   v                        |
|           [ R1 ] <--- Yêu cầu cấp phát ----- ( P2 )                      |
|    Trong đó: P1 đang giữ R1, P2 đang giữ R2.                             |
+--------------------------------------------------------------------------+
```

*Nguyên lý cốt lõi:* Cả 4 điều kiện này là **điều kiện cần**. Do đó, chỉ cần **triệt tiêu bất kỳ 1 trong 4 điều kiện** là ngăn chặn (Prevention) được Deadlock hoàn toàn.

#### 2. Sơ đồ Đồ thị Cấp phát Tài nguyên (Resource Allocation Graph - RAG):

Đồ thị RAG là công cụ đồ thị toán học dùng trong chiến lược **Phát hiện bế tắc (탐지 - Detection)**:
- **Nút tiến trình:** Biểu diễn bằng hình tròn `( Pi )`.
- **Nút tài nguyên:** Biểu diễn bằng hình chữ nhật `[ Rj ]`, bên trong chứa các chấm `*` đại diện cho số lượng bản sao (Instances).
- **Cạnh yêu cầu (Request Edge):** `( Pi ) ---> [ Rj ]` (Tiến trình đang chờ cấp phát tài nguyên $R_j$).
- **Cạnh cấp phát (Assignment Edge):** `[ Rj ] ---> ( Pi )` (Tài nguyên $R_j$ đã được gán cho tiến trình $P_i$).

```text
[TRƯỜNG HỢP 1: Tài nguyên đơn bản sao (Single-instance) -> CÓ CHU TRÌNH LÀ DEADLOCK CHẮC CHẮN]

       ( P1 ) ---------------- Yêu cầu -------------> [ R1 (*) ]
         ^                                                |
         |                                           Đã cấp phát
    Đã cấp phát                                           |
         |                                                v
      [ R2 (*) ] <------------ Yêu cầu -------------- ( P2 )

   * Giải thích: Chu trình (P1 -> R1 -> P2 -> R2 -> P1) khép kín.
     Vì R1 và R2 chỉ có 1 instance duy nhất, P1 và P2 khóa cứng vĩnh viễn -> DEADLOCK!
```

```text
[TRƯỜNG HỢP 2: Tài nguyên đa bản sao (Multi-instance) -> CÓ CHU TRÌNH NHƯNG KHÔNG DEADLOCK]

       ( P1 ) ---------------- Yêu cầu -------------> [ R1 (* *) ] <--- Đã cấp --- ( P3 )
         ^                                                |
         |                                           Đã cấp phát
    Đã cấp phát                                           |
         |                                                v
      [ R2 (* *) ] <---------- Yêu cầu -------------- ( P2 )
         ^
         |
    Đã cấp phát
         |
       ( P4 )

   * Giải thích:
     - Xuất hiện chu trình khép kín giữa P1, R1, P2, R2.
     - TUY NHIÊN, R1 và R2 có 2 bản sao. Instance thứ hai của R1 đang cấp cho P3, và của R2 cấp cho P4.
     - P3 và P4 không bị nghẽn (không chờ ai). Khi P3 hoàn tất trả lại R1, R1 được trao cho P1.
     - Chu trình bị phá vỡ -> HỆ THỐNG AN TOÀN, KHÔNG BỊ DEADLOCK!
```

*Quy tắc vàng HRDK:*
- Nếu tài nguyên chỉ có **1 instance**: Tồn tại chu trình $\Leftrightarrow$ Bế tắc (Deadlock).
- Nếu tài nguyên có **nhiều instance**: Tồn tại chu trình là điều kiện cần nhưng **chưa đủ** để kết luận bế tắc.

#### 3. Minh họa nguyên lý giải thuật Peterson cho 2 tiến trình ($P_0$ và $P_1$):
```c
// Các biến chia sẻ chung
boolean flag[2] = {false, false}; // Cờ thể hiện nguyện vọng muốn vào miền găng
int turn = 0;                     // Lượt ưu tiên

// Đoạn mã cho tiến trình Pi (với Pj là tiến trình đối phương)
void process_i(int i, int j) {
    while (true) {
        flag[i] = true; // Báo hiệu: "Tôi muốn vào miền găng"
        turn = j;       // Nhường lượt: "Nhường bạn j chạy trước nếu bạn cũng muốn"

        // Đợi chừng nào bạn j cũng muốn vào VÀ đang là lượt của bạn j
        while (flag[j] && turn == j) {
            // Chờ đợi bận (Busy waiting)
        }

        // --- BẮT ĐẦU MIỀN GĂNG (CRITICAL SECTION) ---
        // Thao tác an toàn trên tài nguyên dùng chung
        // --- KẾT THÚC MIỀN GĂNG ---

        flag[i] = false; // Ra khỏi miền găng, hạ cờ báo hiệu đã xong

        // Phần còn lại (Remainder Section)
    }
}
```

#### 4. Cấu trúc nguyên tử của hai hàm Semaphore ($P$ và $V$):
```c
struct Semaphore {
    int count;
    Queue queue; // Hàng đợi các tiến trình đang chờ
};

// Thao tác P(S) - Wait
void P(Semaphore S) {
    S.count--;
    if (S.count < 0) {
        // Tài nguyên đã hết -> Đưa tiến trình vào hàng đợi và chuyển sang trạng thái Wait (Block)
        block();
    }
}

// Thao tác V(S) - Signal
void V(Semaphore S) {
    S.count++;
    if (S.count <= 0) {
        // Vẫn còn tiến trình đang đợi trong hàng đợi -> Đánh thức 1 tiến trình (Wakeup)
        wakeup();
    }
}
```

#### 5. Bảng phân tích trạng thái an toàn trong Thuật toán Banker:
Giả sử hệ thống có 3 loại tài nguyên và 3 tiến trình $P_1, P_2, P_3$:
- **Tài nguyên có sẵn (Available):** Số lượng tài nguyên chưa cấp phát mà OS đang nắm giữ.
- **Yêu cầu tối đa (Max):** Nhu cầu cực đại mà mỗi tiến trình có thể đòi hỏi.
- **Đang giữ (Allocation):** Số lượng tài nguyên đã cấp cho mỗi tiến trình.
- **Nhu cầu còn lại (Need):** $\text{Need} = \text{Max} - \text{Allocation}$.

*Quy tắc Safe Sequence (Chuỗi an toàn):*
- Hệ điều hành tìm xem có tiến trình nào mà $\text{Need} \le \text{Available}$ không.
- Nếu có, giả định cấp phát cho nó chạy xong và thu hồi toàn bộ tài nguyên ($\text{Available} = \text{Available} + \text{Allocation}$).
- Tiếp tục tìm cho các tiến trình còn lại; nếu tìm được chuỗi thứ tự thỏa mãn cho mọi tiến trình $\rightarrow$ Hệ thống ở **Trạng thái an toàn (Safe State)** và đồng ý cấp phát!

---

### 복습 체크리스트
- [ ] Thuộc lòng 4 điều kiện cần của bế tắc: **상점비환** (상호 배제, 점유와 대기, 비선점, 환형 대기).
- [ ] Ghi nhớ 4 chiến lược giải quyết: Phòng ngừa (예방), Né tránh (회피), Phát hiện (탐지), Phục hồi (회복).
- [ ] Nắm chắc: Thuật toán Banker của Dijkstra thuộc chiến lược Né tránh (회피) dựa trên Safe State.
- [ ] Kể tên 3 yêu cầu của Miền găng: Tương hỗ loại trừ (Mutual Exclusion), Tiến triển (Progress), Chờ đợi hữu hạn (Bounded Waiting).
- [ ] Nhớ Dekker & Peterson áp dụng cho 2 tiến trình, Lamport Bakery áp dụng cho $N$ tiến trình.
- [ ] Thuộc bản chất Semaphore: $P(S)$ là trừ và đợi, $V(S)$ là cộng và đánh thức.
