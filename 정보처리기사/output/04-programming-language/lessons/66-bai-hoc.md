# 208. 소프트웨어의 재사용 (Software Reuse / Tái sử dụng phần mềm)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **208. 소프트웨어의 재사용 (Software Reuse / Tái sử dụng phần mềm)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối software reuse với component, interface và maintenance, để tái sử dụng không tạo coupling ẩn.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **208. 소프트웨어의 재사용 (Software Reuse / Tái sử dụng phần mềm)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **208. 소프트웨어의 재사용 (Software Reuse / Tái sử dụng phần mềm)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **209. 소프트웨어 재공학 (Software Reengineering / Tái cấu trúc phần mềm)** khi chuyển sang phần tiếp theo.

> **Nối mạch:** Trong **208. 소프트웨어의 재사용 (Software Reuse / Tái sử dụng phần mềm)**, **핵심 키워드 (Từ khóa)** nối từ **학습 목표 (Mục tiêu)** sang **선행·연결 개념 (Kiến thức liên kết)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 핵심 키워드 (Từ khóa)

소프트웨어의, 재사용

> **Nối mạch:** Ở chặng này của **208. 소프트웨어의 재사용 (Software Reuse / Tái sử dụng phần mềm)**, **핵심 키워드 (Từ khóa)** dẫn sang **선행·연결 개념 (Kiến thức liên kết)**, nơi tài liệu chuẩn và vị trí sở hữu được chỉ rõ để biết chỗ đào sâu tiếp; **읽는 방법 (Cách đọc)** mở rộng hệ quả liên quan.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **206 - 207. 객체지향 설계 및 프로그래밍 (OO Design & Programming)**에서 만든 기준을 이어받아 **208. 소프트웨어의 재사용 (Software Reuse / Tái sử dụng phần mềm)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Nối mạch:** Đặt trong câu hỏi lớn của **208. 소프트웨어의 재사용 (Software Reuse / Tái sử dụng phần mềm)**, **읽는 방법 (Cách đọc)** nối từ **선행·연결 개념 (Kiến thức liên kết)** sang **208. 소프트웨어의 재사용 (Software Reuse / Tái sử dụng phần mềm)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Nối mạch:** Trong **208. 소프트웨어의 재사용 (Software Reuse / Tái sử dụng phần mềm)**, **208. 소프트웨어의 재사용 (Software Reuse / Tái sử dụng phần mềm)** nối từ **읽는 방법 (Cách đọc)** sang phần giải thích tiếp theo, vì phần trước cung cấp điểm tựa cho chủ đề này.

## 208. 소프트웨어의 재사용 (Software Reuse / Tái sử dụng phần mềm)

Từ **206 - 207. 객체지향 설계 및 프로그래밍 (OO Design & Programming)**, ta đã có điểm tựa để bước vào **208. 소프트웨어의 재사용 (Software Reuse / Tái sử dụng phần mềm)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 66/91 trước khi đi vào chi tiết.

Để đọc **208. 소프트웨어의 재사용 (Software Reuse / Tái sử dụng phần mềm)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “208. 소프트웨어의 재사용 (Software Reuse / Tái sử dụng phần mềm)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 이미 개발된 소프트웨어 전체/일부를 다른 개발에 사용하는 것. 개발 시간/비용 단축, 품질 향상.
- **컴포넌트 (Component)**: 객체들의 모임으로 대규모 재사용 단위.
- 모듈 크기가 작고 일반적일수록 재사용률이 높음.
- 문제점: 표준화 부족, 공통 요소 발견의 어려움, 새 코드에 통합하기 어려움.

**Giải thích (Vietnamese):**
Đừng "phát minh lại cái bánh xe". Lấy những module, function đã chạy tốt ở dự án trước để ghép vào dự án này (ví dụ: dùng lại module đăng nhập bằng Google).

---

Điểm chốt của **208. 소프트웨어의 재사용 (Software Reuse / Tái sử dụng phần mềm)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **209. 소프트웨어 재공학 (Software Reengineering / Tái cấu trúc phần mềm)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

> **Bàn giao:** Sau **208. 소프트웨어의 재사용 (Software Reuse / Tái sử dụng phần mềm)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
