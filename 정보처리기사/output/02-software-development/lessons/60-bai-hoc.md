# 45. V-모델 (V-Model) 기반 애플리케이션 테스트 단계

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **45. V-모델 (V-Model) 기반 애플리케이션 테스트 단계**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối V-Model với requirement, design, implementation và test level, để mỗi đầu ra có một tầng kiểm chứng đối xứng.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **45. V-모델 (V-Model) 기반 애플리케이션 테스트 단계**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **45. V-모델 (V-Model) 기반 애플리케이션 테스트 단계** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **097-2: 테스트 프로세스 (Test Process - Quy trình kiểm thử)** khi chuyển sang phần tiếp theo.

Mục tiêu nối nhánh phát triển với nhánh kiểm thử trong V-model; từ khóa khoanh vùng requirement, design, integration và acceptance.

## 핵심 키워드 (Từ khóa)

모델

Kiến thức liên kết đặt V-model trên nền coverage criteria và test phases; cách đọc tiếp theo giúp theo dõi artifact nào sinh ra test nào.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **44. 화이트박스 테스트 검증 기준 (White Box Test Coverage Criteria)**에서 만든 기준을 이어받아 **45. V-모델 (V-Model) 기반 애플리케이션 테스트 단계**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

Cách đọc đã đặt khung đối tượng–điều kiện–hệ quả; phần V-model dùng khung đó để nối đầu ra phát triển với mục tiêu xác minh.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

Phần này khép lại bằng traceability giữa yêu cầu và test; khi sang test process, hãy chuyển mapping đó thành chu trình thực thi và báo cáo.

## 45. V-모델 (V-Model) 기반 애플리케이션 테스트 단계

Từ **44. 화이트박스 테스트 검증 기준 (White Box Test Coverage Criteria)**, ta đã có điểm tựa để bước vào **45. V-모델 (V-Model) 기반 애플리케이션 테스트 단계**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 60/101 trước khi đi vào chi tiết.

Để đọc **45. V-모델 (V-Model) 기반 애플리케이션 테스트 단계** như một bài học cho người mới, hãy giữ câu hỏi: **ta dùng mô hình nào để biểu diễn đối tượng, quan hệ hoặc hành vi, và giới hạn của mỗi cách là gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **하향식 (Top-down)**, **상향식 (Bottom-up)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

개발 단계와 테스트 단계를 짝지어 놓은 모델.
1. **단위 테스트 (Unit Test)** - *구현(Code)* 단계와 짝. 모듈/컴포넌트 초점 (주로 구조 기반/화이트박스).
2. **통합 테스트 (Integration Test)** - *설계(Design)* 단계와 짝. 모듈들을 결합하여 테스트.
   * **하향식 (Top-down)**: 스텁(Stub) 사용. 깊이/넓이 우선. 테스트 초기부터 시스템 구조 파악 가능.
   * **상향식 (Bottom-up)**: 드라이버(Driver)와 클러스터(Cluster) 사용.

---

- **Bandwidth (대역폭/전송률 - Băng thông):** Tốc độ truyền dữ liệu tối đa trong 1 giây (đơn vị bit/s hoặc byte/s). Băng thông càng lớn máy càng nhanh.
- **접근 속도 (Tốc độ tiếp cận Nhanh -> Chậm):** CPU 레지스터 -> Cache -> RAM(Main Memory) -> ROM -> 자기 코어 -> 자기 디스크 (HDD) -> 자기 테이프 (Tape).

Để không đọc **ROM (Read Only Memory - Bộ nhớ chỉ đọc)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### ROM (Read Only Memory - Bộ nhớ chỉ đọc)

Các ý ngay dưới **ROM (Read Only Memory - Bộ nhớ chỉ đọc)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “ROM (Read Only Memory - Bộ nhớ chỉ đọc)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 전원이 꺼져도 내용이 지워지지 않는 비휘발성 (Không bay hơi khi mất điện).
- 주로 기본 입·출력 시스템(BIOS), 자가 진단 프로그램(POST) 저장 (Thường chứa BIOS, POST).
- **ROM 종류 (Các loại ROM):**
  - Mask ROM: Nhà máy làm sẵn, không đổi được.
  - PROM: Ghi được **1번** (1 lần).
  - EPROM: 자외선 (Tia cực tím - UV) để xóa, ghi lại nhiều lần.
  - EEPROM (EAROM): 전기적인 방법 (Phương pháp điện - Electrical) để xóa và ghi. (Ví dụ: USB Flash Drive, SSD).

- **Vietnamese Explanation:** Cycle Time luôn dài hơn Access Time vì bộ nhớ cần thời gian phục hồi lại năng lượng sau khi đọc. ROM giữ lại dữ liệu khi mất điện, có nhiều loại từ cứng nhắc (Mask) đến linh hoạt (EEPROM - dùng điện để xóa).
- **Ví dụ (Example):** EEPROM chính là công nghệ đằng sau cái USB nhỏ xinh bạn hay dùng. EPROM thì giống cái bảng viết phấn, bôi đi bằng tia UV (giẻ lau) rồi viết lại. Mask ROM là bia đá khắc chữ sẵn.
- 💡 **Mẹo ghi nhớ (Mnemonics):** "E" đầu tiên = Erasable (Xóa được). Nhớ: EPROM = UV (Tia cực tím), EEPROM = Điện (Electonic). Cycle Time ≥ Access Time.

Với **ROM (Read Only Memory - Bộ nhớ chỉ đọc)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Với **ROM (Read Only Memory - Bộ nhớ chỉ đọc)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Điểm chốt của **45. V-모델 (V-Model) 기반 애플리케이션 테스트 단계** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **097-2: 테스트 프로세스 (Test Process - Quy trình kiểm thử)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

> **Bàn giao:** Sau **45. V-모델 (V-Model) 기반 애플리케이션 테스트 단계**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
