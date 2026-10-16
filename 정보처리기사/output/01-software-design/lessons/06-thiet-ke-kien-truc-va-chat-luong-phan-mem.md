# 소프트웨어 아키텍처 및 품질 표준 (Thiết kế Kiến trúc phần mềm và Tiêu chuẩn chất lượng ISO)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, vai trò và phân cấp 2 tầng thiết kế của Kiến trúc phần mềm: Thiết kế mức cao (`상위 설계 - High-level Design`) vs Thiết kế mức thấp (`하위 설계 - Low-level Design`).
- Phân tích sâu sắc Mô hình kiến trúc 4+1 View của Philippe Kruchten và vai trò trung tâm kiểm chứng của `유스케이스 뷰 (Use Case View)`.
- Làm chủ các Mẫu kiến trúc kinh điển (`Architectural Patterns`): Mẫu phân tầng (`Layered`), Đường ống - Bộ lọc (`Pipe-Filter`), `MVC`, Máy khách - Máy chủ (`Client-Server`), `Broker`, và Bảng đen (`Blackboard`).
- Thuộc nằm lòng 3 nguyên lý thiết kế nền tảng do David Parnas khởi xướng: Trừu tượng hóa (`추상화`), Che giấu thông tin (`정보 은닉`), và Mô-đun hóa (`모듈화`).
- Ghi nhớ trọn vẹn 6 đặc tính chất lượng phần mềm theo tiêu chuẩn quốc tế ISO/IEC 9126 (thần chú `기-신-사-효-유-이`) cùng bản cập nhật mở rộng ISO/IEC 25010 (SQuaRE).

## 핵심 키워드 (Từ khóa)
- 소프트웨어 아키텍처 (Kiến trúc phần mềm / Software Architecture)
- 상위 설계 vs 하위 설계 (High-level vs Low-level Design / 아키텍처 vs 모듈 상세)
- 4+1 뷰 모델 (4+1 View Model: 유스케이스, 논리, 프로세스, 구현, 배포 뷰)
- 아키텍처 패턴 (Layered, Client-Server, Pipe-Filter, MVC, Broker, Blackboard)
- 추상화 (Trừu tượng hóa / Abstraction: 과정, 데이터, 제어 추상화)
- 정보 은닉 (Che giấu thông tin / Information Hiding / David Parnas)
- ISO/IEC 9126 6대 품질 특성 (기능성, 신뢰성, 사용성, 효율성, 유지보수성, 이식성)
- ISO/IEC 25010 (SQuaRE: 8대 품질 특성 / 보안성, 호환성 추가)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin / Prerequisite):** Tiếp nối từ [05-thiet-ke-giao-dien-ui-ux.md](05-thiet-ke-giao-dien-ui-ux.md), sau khi giao diện bên ngoài và các luồng tương tác của người dùng đã được định hình, hệ thống cần một bộ khung xương chịu lực vững chắc bên dưới để phân chia trách nhiệm giữa các thành phần logic, bảo đảm hiệu năng và khả năng bảo trì lâu dài.
- **Đang giải quyết gì (Current Problem):** Bài học này thuộc trọng tâm của **Chương 3: 애플리케이션 설계 (Thiết kế ứng dụng)**, giải quyết bài toán lựa chọn phong cách kiến trúc tổng thể, thiết lập các nguyên lý thiết kế độc lập và áp dụng các tiêu chuẩn chất lượng quốc tế (ISO/IEC 9126) làm thước đo nghiệm thu phần mềm.
- **Dùng đi đâu (Forward Handoff):** Khi khung kiến trúc tổng thể đã hoàn tất, các thành phần phần mềm cần được thiết kế cụ thể theo mô hình đối tượng và tuân thủ các quy tắc viết code chuẩn mực. Kiến thức này chuyển giao trực tiếp sang [07-huong-doi-tuong-va-nguyen-ly-solid.md](07-huong-doi-tuong-va-nguyen-ly-solid.md) để khảo sát tư duy Hướng đối tượng và 5 nguyên tắc vàng SOLID.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để ghi nhớ: bảng đối chiếu Thượng tầng vs Hạ tầng thiết kế; 5 góc nhìn trong 4+1 View; các từ khóa nhận diện các Architectural Pattern; và câu thần chú thuộc 6 đặc tính ISO 9126: **Kì - Shin - Sa - Hyo - Yu - I** (`기 - 신 - 사 - 효 - 유 - 이`).
- Đọc TẦNG B để hiểu sâu cơ chế che giấu thông tin của David Parnas trong việc giảm thiểu hiệu ứng gợn sóng (Ripple Effect) khi sửa code, và cấu trúc luồng dữ liệu độc lập trong Pipe-Filter Pattern.

---

## 소프트웨어 아키텍처 및 품질 표준

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Định nghĩa và Phân cấp Thiết kế Kiến trúc

##### A. Định nghĩa Kiến trúc phần mềm (Software Architecture)
- **핵심 원리 (Nguyên tắc cốt lõi):**
  - [Hàn/Anh]: `소프트웨어 아키텍처는 소프트웨어의 골격이 되는 기본 구조이자, 소프트웨어를 구성하는 컴포넌트들과 그들이 지닌 특성, 그리고 컴포넌트 간의 상호작용 및 관계를 총체적으로 정의한 것이다.`
  - [Tiếng Việt]: Kiến trúc phần mềm là bộ khung xương cấu trúc cơ bản của hệ thống, định nghĩa tổng thể các thành phần phần mềm (Components), các đặc tính kỹ thuật bên trong chúng, cũng như các mối quan hệ tương tác và quy tắc ràng buộc giữa các thành phần nhằm đảm bảo hệ thống vận hành ổn định và dễ tiến hóa.

##### B. Phân cấp 2 tầng thiết kế: 상위 설계 vs 하위 설계

| Tiêu chí | 상위 설계 (High-level Design — Thiết kế mức cao) | 하위 설계 (Low-level Design — Thiết kế mức thấp) |
|:---|:---|:---|
| **Tên gọi tương đương** | **아키텍처 설계 (Thiết kế kiến trúc)**, 예비 설계 (Thiết kế sơ bộ) | **모듈 상세 설계 (Thiết kế chi tiết module)** |
| **Phạm vi đối tượng** | Toàn bộ khung hệ thống ở mức vĩ mô | Chi tiết từng module cụ thể ở mức vi mô |
| **Nội dung thiết kế** | • Cấu trúc kiến trúc tổng thể; Phân chia subsystem và cơ sở dữ liệu; Cấu trúc giao diện liên kết hệ thống | • Logic và thuật toán nội bộ từng module; Cấu trúc dữ liệu nội bộ; Định dạng tham số hàm và mã lệnh cụ thể |
| **Bẫy nhận diện** | Gắn với từ khóa: **Kiến trúc (아키텍처), Cấu trúc tổng thể (전체 구조)** | Gắn với từ khóa: **Thuật toán (알고리즘), Logic nội bộ (내부 로직)** |

---

#### 2. Mô hình kiến trúc 4+1 View (Kruchten's 4+1 View Model)
Để mô tả kiến trúc từ góc nhìn của nhiều bên liên quan khác nhau, Philippe Kruchten đề xuất mô hình gồm 4 góc nhìn chuyên biệt xoay quanh 1 góc nhìn kiểm chứng trung tâm:

```
                  ┌───────────────────────────────┐
                  │    논리 뷰 (Logical View)      │
                  │  (Lập trình viên / Chức năng) │
                  └───────────────┬───────────────┘
                                  │
┌──────────────────────────────┐  │  ┌──────────────────────────────┐
│   프로세스 뷰 (Process View)  │  │  │    구현 뷰 (Implementation)  │
│(Tích hợp / Đa luồng, Hiệu năng)├─┼──┤ (Quản lý cấu hình / Source) │
└──────────────────────────────┘  │  └──────────────────────────────┘
                                  ▼
                 ┌─────────────────────────────────┐
                 │ ★ 유스케이스 뷰 (Use Case View) │
                 │    (Người dùng cuối / Trung tâm) │
                 └────────────────┬────────────────┘
                                  │
                  ┌───────────────▼───────────────┐
                  │    배포 뷰 (Deployment View)   │
                  │   (Kỹ sư vận hành / Phần cứng)│
                  └───────────────────────────────┘
```

1. **유스케이스 뷰 (Use Case View — Góc nhìn trường hợp sử dụng / Scenarios):**
   - **Vị trí cốt lõi:** Đóng vai trò là **Góc nhìn trung tâm (+1)** liên kết và kiểm chứng tính đúng đắn của 4 view còn lại.
   - Thể hiện các hành vi và chức năng của hệ thống dưới góc nhìn của người dùng cuối (`최종 사용자`).
2. **논리 뷰 (Logical View — Góc nhìn logic):**
   - Phục vụ người thiết kế và lập trình viên; mô tả các chức năng nghiệp vụ mà hệ thống cung cấp dưới dạng các lớp (Class), đối tượng và mối quan hệ giữa chúng (thường dùng Class Diagram).
3. **프로세스 뷰 (Process View — Góc nhìn tiến trình):**
   - Phục vụ chuyên gia tích hợp hệ thống; mô tả các khía cạnh phi chức năng như tính đồng thời (`동시성 - Concurrency`), đa luồng (`스레드 - Thread`), hiệu năng và khả năng mở rộng.
4. **구현 뷰 (Implementation View — Góc nhìn hiện thực / Component View):**
   - Phục vụ kỹ sư phát triển và quản lý cấu hình; mô tả cấu trúc vật lý tĩnh của mã nguồn, các module phần mềm, component, file thực thi và thư viện liên kết.
5. **배포 뷰 (Deployment View — Góc nhìn triển khai):**
   - Phục vụ kỹ sư vận hành và hạ tầng; mô tả cách thức phân bổ các component phần mềm lên các nút phần cứng vật lý (`물리적 노드`), máy chủ và cấu hình mạng.

---

#### 3. Các Mẫu kiến trúc phần mềm kinh điển (Architectural Patterns)

| Architectural Pattern | Bản chất kỹ thuật & Cơ chế hoạt động | Tình huống ứng dụng thực tế |
|:---|:---|:---|
| **Layered Pattern (Mẫu phân tầng)** | Chia hệ thống thành các tầng phân cấp độc lập nằm chồng lên nhau (thường là 3-4 tầng: Presentation $\rightarrow$ Business $\rightarrow$ Data). **Mỗi tầng chỉ tương tác với tầng liền kề dưới nó**. Tăng tính độc lập và khả năng bảo trì. | Ứng dụng Web doanh nghiệp, hệ điều hành (OS). |
| **Pipe-Filter Pattern (Đường ống - Bộ lọc)** | Dữ liệu di chuyển liên tục qua một chuỗi các **bộ lọc (Filter)** độc lập thông qua các **kênh truyền (Pipe)**. Mỗi Filter nhận dữ liệu, biến đổi và đẩy ra Pipe mà không cần biết Filter trước và sau là ai. | Dòng lệnh Unix (`ps \| grep \| awk`), xử lý hình ảnh, xử lý luồng dữ liệu (ETL / Streaming). |
| **MVC Pattern (Model-View-Controller)** | Tách biệt hoàn toàn thành 3 thành phần: • **Model**: Quản lý dữ liệu và logic nghiệp vụ; • **View**: Hiển thị dữ liệu lên màn hình; • **Controller**: Tiếp nhận thao tác người dùng, điều phối Model và View. | Ứng dụng Web hiện đại (Spring MVC, Django, Angular). |
| **Client-Server Pattern (Máy khách - Máy chủ)** | Một Server trung tâm cung cấp tài nguyên/dịch vụ; nhiều Client gửi yêu cầu và nhận kết quả từ Server. | Trình duyệt Web và Máy chủ Web, Email. |
| **Master-Slave Pattern (Chủ - Tớ)** | Một nút Master phân chia bài toán thành nhiều phần việc nhỏ và giao cho các nút Slave thực thi song song, sau đó Master tổng hợp kết quả cuối cùng. | Tính toán song song, hệ thống CSDL Master-Slave (Replication). |
| **Broker Pattern (Môi giới)** | Thành phần **Broker** đứng ở giữa làm cầu nối điều phối liên lạc giữa Client và Server khi Client không biết vị trí vật lý cụ thể của Server. | Hệ thống phân tán, kiến trúc hướng dịch vụ (CORBA, Message Broker). |
| **Blackboard Pattern (Bảng đen)** | Các mô-đun chuyên gia độc lập (Knowledge Sources) cùng đọc và ghi các giải pháp trung gian lên một vùng nhớ chia sẻ chung gọi là **Bảng đen (Blackboard)** để cùng giải quyết một bài toán phức tạp chưa có thuật toán tất định. | Nhận dạng tiếng nói, AI tri thức chuyên gia, thị giác máy tính. |

---

#### 4. 3 Nguyên lý thiết kế phần mềm kinh điển (David Parnas)
1. **추상화 (Abstraction — Trừu tượng hóa):**
   - Quá trình lược bỏ các chi tiết kỹ thuật phức tạp không cần thiết, chỉ giữ lại những đặc tính bản chất cốt lõi nhất của đối tượng để giảm tải độ phức tạp nhận thức.
   - **3 Loại trừu tượng hóa thường gặp:**
     - `과정 추상화 (Process Abstraction)`: Đóng gói toàn bộ chuỗi hành động phức tạp bên trong một tên hàm/thủ tục (ví dụ: hàm `calculateTax()`).
     - `데이터 추상화 (Data Abstraction)`: Định nghĩa cấu trúc dữ liệu đi kèm các thao tác hợp lệ mà không để lộ cách lưu trữ bộ nhớ bên trong (Kiểu dữ liệu trừu tượng ADT / Class).
     - `제어 추상화 (Control Abstraction)`: Trừu tượng hóa luồng thực thi lệnh (các cấu trúc rẽ nhánh IF-ELSE, vòng lặp FOR/WHILE thay vì nhảy địa chỉ GOTO).
2. **정보 은닉 (Information Hiding — Che giấu thông tin):**
   - Do David Parnas đề xuất; quy định rằng **mỗi module phải che giấu tuyệt đối các chi tiết cài đặt nội bộ (thuộc tính dữ liệu, thuật toán) khỏi tầm nhìn của các module khác**.
   - Các module bên ngoài chỉ được phép tương tác thông qua giao diện công khai (`공개 인터페이스 - Public Interface`).
   - *Lợi ích:* Khi một module thay đổi thuật toán nội bộ để tối ưu hiệu năng, **các module khác hoàn toàn không bị ảnh hưởng**, triệt tiêu hiệu ứng gợn sóng (Ripple Effect).
3. **모듈화 (Modularization — Mô-đun hóa):**
   - Chia một hệ thống phần mềm lớn thành các khối module nhỏ hơn có chức năng chuyên biệt, độc lập để dễ dàng phân chia công việc phát triển, kiểm thử và tái sử dụng.

---

#### 5. Tiêu chuẩn Chất lượng phần mềm ISO/IEC 9126 và ISO/IEC 25010

##### A. 6 Đặc tính chất lượng cốt lõi của ISO/IEC 9126
- **Mẹo ghi nhớ thần chú:** **기 - 신 - 사 - 효 - 유 - 이** (*Kì - Shin - Sa - Hyo - Yu - I*).
1. `기능성 (Functionality — Tính chức năng)`: Phần mềm có cung cấp đầy đủ và đúng các chức năng thỏa mãn nhu cầu người dùng hay không.
   - *Đặc tính con:* 적절성 (Tính phù hợp), 정밀성 (Tính chính xác), 상호운용성 (Khả năng tương tác), **보안성 (Tính bảo mật)**, 준수성 (Tính tuân thủ).
2. `신뢰성 (Reliability — Độ tin cậy)`: Khả năng duy trì mức hiệu năng ổn định trong điều kiện hoạt động xác định qua thời gian.
   - *Đặc tính con:* 성숙성 (Độ chín muồi), 결함 허용성 (Khả năng chịu lỗi / Fault Tolerance), 회복성 (Khả năng phục hồi).
3. `사용성 (Usability — Tính khả dụng)`: Mức độ dễ hiểu, dễ học và tiện lợi khi người dùng thao tác.
   - *Đặc tính con:* 이해성 (Dễ hiểu), 학습성 (Dễ học), 운용성 (Dễ vận hành), 친근성/매력성 (Tính hấp dẫn).
4. `효율성 (Efficiency — Tính hiệu quả)`: Tương quan giữa mức hiệu năng của phần mềm và lượng tài nguyên phần cứng (CPU, RAM, thời gian) tiêu hao.
   - *Đặc tính con:* 시간 반응성 (Thời gian đáp ứng), 자원 활용성 (Mức sử dụng tài nguyên).
5. `유지보수성 (Maintainability — Khả năng bảo trì)`: Mức độ dễ dàng khi cần sửa lỗi, cải tiến hoặc thích nghi với môi trường mới.
   - *Đặc tính con:* 분석성 (Dễ phân tích), 변경성 (Dễ sửa đổi), 안정성 (Tính ổn định), 시험성 (Dễ kiểm thử / Testability).
6. `이식성 (Portability — Khả năng di chuyển)`: Khả năng chuyển phần mềm sang vận hành trên các môi trường phần cứng hoặc hệ điều hành khác nhau.
   - *Đặc tính con:* 적용성 (Khả năng thích ứng), 설치성 (Dễ cài đặt), 대체성 (Khả năng thay thế), 공존성 (Khả năng cùng tồn tại).

##### B. Tiêu chuẩn nâng cấp ISO/IEC 25010 (SQuaRE Series)
- Là bản tiêu chuẩn hiện đại thay thế cho ISO/IEC 9126, mở rộng từ 6 đặc tính thành **8 đặc tính chất lượng phần mềm**, trong đó tách và nâng cấp 2 đặc tính cực kỳ quan trọng trong thời đại số thành nhóm độc lập:
  1. **보안성 (Security — Tính an toàn bảo mật):** Được nâng lên thành 1 đặc tính lớn (gồm Tính bảo mật Confidentiality, Tính toàn vẹn Integrity, Tính chống chối bỏ Non-repudiation, Tính xác thực Authenticity).
  2. **호환성 (Compatibility — Tính tương thích):** Được bổ sung thành 1 đặc tính lớn (gồm Khả năng cùng tồn tại Co-existence, Khả năng tương tác liên thông Interoperability).

---

#### 6. Bẫy đề thi trắc nghiệm thường gặp (주의/함정)
- **Bẫy 1 (High-level vs Low-level Design):**
  - Thiết kế kiến trúc tổng thể, cơ sở dữ liệu, phân chia subsystem $\rightarrow$ **상위 설계 (Thiết kế mức cao)**.
  - Thiết kế thuật toán chi tiết, cấu trúc dữ liệu bên trong module $\rightarrow$ **하위 설계 (Thiết kế mức thấp)**.
- **Bẫy 2 (4+1 View Model):** Góc nhìn nào đóng vai trò **trung tâm liên kết và thẩm định 4 góc nhìn còn lại?** $\rightarrow$ Đáp án chắc chắn là **유스케이스 뷰 (Use Case View)**.
- **Bẫy 3 (Pipe-Filter Pattern):** Dữ liệu di chuyển tuần tự qua các bộ lọc độc lập, nhận dạng lệnh pipe Unix $\rightarrow$ **파이프-필터 패턴 (Pipe-Filter Pattern)**.
- **Bẫy 4 (ISO/IEC 9126):** Đề hỏi *"Bảo mật (보안성) nằm trong đặc tính lớn nào của ISO/IEC 9126?"* $\rightarrow$ Nằm trong **기능성 (Functionality - Tính chức năng)** (Lưu ý: Sang ISO 25010 mới tách riêng thành đặc tính lớn).

- **한 문장 설명 (Câu chốt ghi nhớ):** "Thượng tầng lo kiến trúc, Hạ tầng lo thuật toán; 4+1 View lấy Use Case làm tim; Parnas che giấu triệt tiêu gợn sóng; ISO 9126 thuộc lòng Kì - Shin - Sa - Hyo - Yu - I".

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Nguyên lý Che giấu thông tin (Information Hiding) và Hiệu ứng gợn sóng (Ripple Effect)
- Trong kỹ nghệ phần mềm cổ điển, khi các module truy cập trực tiếp vào biến toàn cục hoặc cấu trúc dữ liệu nội bộ của nhau, một thay đổi nhỏ ở module A sẽ làm phát sinh hàng loạt lỗi dây chuyền ở module B, C, D... Hiện tượng này gọi là **Hiệu ứng gợn sóng (`파급 효과 - Ripple Effect`)**.
- David Parnas đã chứng minh rằng: Bằng cách áp dụng **정보 은닉 (Information Hiding)**, chúng ta đóng gói các quyết định thiết kế dễ bị thay đổi (như thuật toán sắp xếp, định dạng lưu trữ file) vào bên trong module và chỉ công khai giao diện phương thức (Interface). Nhờ đó:
  - Lập trình viên có thể tùy ý tối ưu hóa lại code bên trong module mà không làm ảnh hưởng đến bất kỳ dòng code nào của các module gọi nó bên ngoài.
  - Chi phí kiểm thử hồi quy (Regression Testing) giảm thiểu tối đa.

#### 2. So sánh chuyên sâu: Pipe-Filter Pattern vs Layered Pattern
- **Layered Pattern:** Phân chia theo cấp độ trừu tượng nghiệp vụ. Tầng trên phục vụ nghiệp vụ mức cao, tầng dưới phục vụ hạ tầng mức thấp. Có sự ràng buộc về mặt phụ thuộc phân cấp (Top-down dependency).
- **Pipe-Filter Pattern:** Phân chia theo dòng chảy của luồng dữ liệu (Data Stream). Không có khái niệm tầng trên tầng dưới; mỗi Filter là một tiến trình độc lập hoàn toàn có thể chạy song song đa luồng. Bộ lọc Filter chỉ cần đọc dữ liệu từ đầu vào của Pipe, xử lý và đẩy ra Pipe tiếp theo, rất phù hợp cho xử lý video, âm thanh, hay tính toán khoa học dữ liệu lớn.

#### 3. Sơ đồ phân loại 6 đặc tính chất lượng phần mềm ISO/IEC 9126

##### A. Sơ đồ cây ASCII phân cấp 6 đặc tính lớn và 21 đặc tính con
```
                      ┌─────────────────────────────────────────────────────────┐
                      │      ISO/IEC 9126 소프트웨어 품질 특성 (6대 품질 특성)   │
                      │           (Mẹo thần chú: 기 - 신 - 사 - 효 - 유 - 이)    │
                      └────────────────────────────┬────────────────────────────┘
                                                   │
    ┌──────────────┬──────────────┬────────────────┼──────────────┬──────────────┐
    ▼              ▼              ▼                ▼              ▼              ▼
┌────────┐     ┌────────┐     ┌────────┐       ┌────────┐     ┌────────┐     ┌────────┐
│ 기능성 │     │ 신뢰성 │     │ 사용성 │       │ 효율성 │     │유지보수│     │ 이식성 │
│(Funct.)│     │(Rel.)  │     │(Usab.) │       │(Eff.)  │     │(Maint.)│     │(Port.) │
└───┬────┘     └───┬────┘     └───┬────┘       └───┬────┘     └───┬────┘     └───┬────┘
    │              │              │                │              │              │
    ├─ 적절성      ├─ 성숙성      ├─ 이해성        ├─ 시간반응성  ├─ 분석성      ├─ 적용성
    ├─ 정밀성      ├─ 결함허용성  ├─ 학습성        └─ 자원활용성  ├─ 변경성      ├─ 설치성
    ├─ 상호운용성  └─ 회복성      ├─ 운용성                       ├─ 안정성      ├─ 공존성
    ├─ 보안성 ★                  └─ 친근성                       └─ 시험성      └─ 대체성
    └─ 준수성                                                                    └─ 준수성
```

##### B. Giải phẫu chi tiết 6 nhóm đặc tính theo chuẩn đề thi
1. **기능성 (Functionality — Tính chức năng):** Phần mềm có đáp ứng đầy đủ và chuẩn xác các nhu cầu nghiệp vụ được người dùng ủy thác hay không:
   - `적절성 (Suitability)`: Cung cấp đúng và đủ bộ chức năng phù hợp cho các tác vụ nghiệp vụ mục tiêu.
   - `정밀성 / 정확성 (Accuracy)`: Đưa ra kết quả tính toán, xử lý dữ liệu với độ chính xác tuyệt đối như cam kết.
   - `상호운용성 (Interoperability)`: Khả năng tương tác, bắt tay trao đổi dữ liệu mượt mà với các hệ thống phần mềm khác.
   - `보안성 (Security - ★ Bẫy đề thi)`: Khả năng ngăn chặn sự truy cập, can thiệp hoặc sửa đổi dữ liệu trái phép từ bên ngoài (Lưu ý: Đề thi thường bẫy Security thuộc nhóm nào trong ISO 9126 $\rightarrow$ Thuộc về **기능성**).
   - `준수성 (Compliance)`: Tuân thủ các quy định pháp lý, điều lệ chuyên ngành và tiêu chuẩn kỹ thuật hiện hành.
2. **신뢰성 (Reliability — Độ tin cậy):** Khả năng duy trì mức hiệu năng ổn định trong những điều kiện vận hành xác định qua thời gian:
   - `성숙성 (Maturity)`: Khả năng phần mềm tránh được các trạng thái đổ vỡ, ngừng hoạt động do lỗi tiềm ẩn trong mã nguồn.
   - `결함 허용성 (Fault Tolerance)`: Khả năng tiếp tục duy trì hoạt động ở mức chấp nhận được ngay cả khi phát sinh lỗi phần mềm hoặc sự cố phần cứng.
   - `회복성 (Recoverability)`: Khả năng khôi phục nhanh chóng trạng thái làm việc và phục hồi dữ liệu bị ảnh hưởng trực tiếp sau khi xảy ra sự cố sập hệ thống.
3. **사용성 (Usability — Tính khả dụng):** Mức độ tiện lợi, dễ dàng mà người dùng cảm nhận được khi tiếp cận và thao tác:
   - `이해성 (Understandability)`: Người dùng dễ dàng nhận biết phần mềm có phù hợp với nhu cầu của mình không và hiểu được phương thức vận hành.
   - `학습성 (Learnability)`: Người dùng có thể học và thành thạo các thao tác sử dụng trong khoảng thời gian ngắn nhất.
   - `운용성 (Operability)`: Người dùng có thể dễ dàng kiểm soát, điều khiển và vận hành các tính năng mà không bị nhầm lẫn.
   - `친근성 / 매력성 (Attractiveness)`: Giao diện được thiết kế thẩm mỹ, thân thiện và tạo cảm giác tích cực cho người sử dụng.
4. **효율성 (Efficiency — Tính hiệu quả):** Mối tương quan giữa mức độ hoàn thành nhiệm vụ và lượng tài nguyên bị tiêu hao:
   - `시간 반응성 (Time Behaviour)`: Thời gian phản hồi (`Response Time`), thời gian xử lý và lưu lượng giao dịch (`Throughput`) khi thực thi tác vụ.
   - `자원 활용성 (Resource Utilization)`: Lượng tài nguyên phần cứng (CPU, dung lượng bộ nhớ RAM, lưu lượng băng thông mạng, dung lượng đĩa) bị tiêu tốn.
5. **유지보수성 (Maintainability — Khả năng bảo trì):** Mức độ dễ dàng khi kỹ sư phần mềm cần can thiệp để sửa lỗi, nâng cấp hoặc tối ưu hóa:
   - `분석성 (Analyzability)`: Khả năng nhanh chóng chẩn đoán các khuyết tật, nguyên nhân hỏng hóc hoặc xác định chính xác các đoạn code cần sửa đổi.
   - `변경성 (Changeability)`: Khả năng thực hiện các sửa đổi mã nguồn một cách dễ dàng mà không làm phát sinh xung đột nội bộ.
   - `안정성 (Stability)`: Nguy cơ phát sinh các hiệu ứng phụ bất ngờ (`Side Effects`) sau khi thay đổi mã nguồn được giữ ở mức thấp nhất.
   - `시험성 (Testability)`: Khả năng dễ dàng thiết lập và thực thi các kịch bản kiểm thử để xác thực tính đúng đắn của phần mềm sau khi sửa đổi.
6. **이식성 (Portability — Khả năng chuyển giao):** Khả năng chuyển phần mềm sang vận hành trên các môi trường nền tảng khác:
   - `적용성 / 적응성 (Adaptability)`: Khả năng thích nghi mượt mà với các môi trường phần cứng hoặc hệ điều hành khác nhau mà không cần sửa code.
   - `설치성 (Installability)`: Khả năng cài đặt thành công và thuận tiện vào môi trường đích định trước.
   - `공존성 (Co-existence)`: Khả năng cùng tồn tại và chia sẻ tài nguyên chung một cách hòa bình với các phần mềm độc lập khác trên cùng một máy chủ.
   - `대체성 (Replaceability)`: Khả năng thay thế một phần mềm tương tự khác trong cùng môi trường vận hành mà không làm gián đoạn nghiệp vụ.

---

#### 4. Bảng so sánh tiến hóa kiến trúc chất lượng: ISO/IEC 9126 vs ISO/IEC 25010

| Tiêu chuẩn quốc tế | Năm ban hành | Số lượng đặc tính lớn | Xử lý đặc tính Bảo mật (보안성) | Xử lý đặc tính Tương thích (호환성) |
|:---|:---:|:---:|:---|:---|
| **ISO/IEC 9126** | 1991 (Sửa đổi 2001) | **6 đại đặc tính** (기-신-사-효-유-이) | Nằm ẩn bên trong nhóm **기능성 (Tính chức năng)** | Nằm phân tán ở `상호운용성` (기능성) và `공존성` (이식성) |
| **ISO/IEC 25010** | 2011 (Chuẩn SQuaRE) | **8 đại đặc tính** (기-신-사-효-유-이 + 보안, 호환) | Tách riêng thành **Đại đặc tính độc lập (Security)** với 5 khía cạnh con | Tách riêng thành **Đại đặc tính độc lập (Compatibility)** gồm Co-existence và Interoperability |

---

### 복습 체크리스트
- [ ] Phân biệt được sự khác nhau giữa 상위 설계 (kiến trúc tổng thể) và 하위 설계 (chi tiết module/thuật toán).
- [ ] Kể tên đủ 5 view trong mô hình 4+1 View và nhớ Use Case View là trung tâm kiểm chứng.
- [ ] Nhận diện được đặc trưng của các Architectural Pattern: Layered (phân tầng), Pipe-Filter (bộ lọc luồng dữ liệu), MVC (tách dữ liệu-giao diện-điều phối), Broker (môi giới trung gian), Blackboard (bảng đen tri thức).
- [ ] Định nghĩa được 3 loại trừu tượng hóa: quá trình (과정), dữ liệu (데이터), điều khiển (제어).
- [ ] Giải thích được nguyên lý che giấu thông tin của David Parnas giúp ngăn chặn hiệu ứng gợn sóng như thế nào.
- [ ] Đọc vanh vách thần chú 6 đặc tính chất lượng của ISO/IEC 9126: 기능성, 신뢰성, 사용성, 효율성, 유지보수성, 이식성.
- [ ] Nhớ 2 đặc tính mới được nâng cấp thành nhóm độc lập trong ISO/IEC 25010 là 보안성 (Bảo mật) và 호환성 (Tương thích).
