# 4. 응집도 (Cohesion - Độ gắn kết)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **4. 응집도 (Cohesion - Độ gắn kết)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **4. 응집도 (Cohesion - Độ gắn kết)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **5. Fan-In / Fan-Out (팬인 / 팬아웃)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

응집도

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **3. 결합도 (Coupling - Độ phụ thuộc)**에서 만든 기준을 이어받아 **4. 응집도 (Cohesion - Độ gắn kết)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 4. 응집도 (Cohesion - Độ gắn kết)

Từ **3. 결합도 (Coupling - Độ phụ thuộc)**, ta đã có điểm tựa để bước vào **4. 응집도 (Cohesion - Độ gắn kết)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 51/55 trước khi đi vào chi tiết.

Để đọc **4. 응집도 (Cohesion - Độ gắn kết)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

**개념 (Khái niệm):** 모듈 내부 요소들이 서로 밀접하게 관련되어 있는 정도 (Mức độ liên quan chặt chẽ của các thành phần BÊN TRONG 1 module). **강할수록 좋음 (Càng cao càng tốt).**

순서 (Từ Tốt nhất đến Xấu nhất): **기능(Functional) -> 순차(Sequential) -> 교환(Communication) -> 절차(Procedural) -> 시간(Temporal) -> 논리(Logical) -> 우연(Coincidental)**
💡 **Mẹo ghi nhớ:** K-S-K-C-S-N-U (Kì-Sun-Kiều-Chul-Shi-Non-U) -> **Không Tin Kiều Chỉ Sợ Người Ù**

1.  **기능적 응집도 (Functional):**
    *   **Korean:** 단일 문제와 연관되어 수행. (Tốt nhất)
    *   **VI (Vietnamese) (Tiếng Việt):** Mọi thành phần trong module cùng giải quyết MỘT bài toán duy nhất.
2.  **순차적 응집도 (Sequential):**
    *   **Korean:** 출력 데이터가 다음 활동의 입력 데이터로 사용됨.
    *   **VI (Vietnamese) (Tiếng Việt):** Đầu ra của bước này là đầu vào của bước kia (trong cùng module).
3.  **교환(통신)적 응집도 (Communication):**
    *   **Korean:** 동일한 입출력을 사용하여 서로 다른 기능 수행.
    *   **VI (Vietnamese) (Tiếng Việt):** Các chức năng khác nhau dùng chung một tập dữ liệu đầu vào / đầu ra.
4.  **절차적 응집도 (Procedural):**
    *   **Korean:** 기능들을 순차적으로 수행.
    *   **VI (Vietnamese) (Tiếng Việt):** Các phần tử được thực hiện theo trình tự thời gian / kịch bản nhất định.
5.  **시간적 응집도 (Temporal):**
    *   **Korean:** 특정 시간에 처리되는 기능들을 모음.
    *   **VI (Vietnamese) (Tiếng Việt):** Gom các tác vụ xảy ra cùng một thời điểm (VD: khối khởi tạo hệ thống Init).
6.  **논리적 응집도 (Logical):**
    *   **Korean:** 유사한 성격/형태로 분류되는 요소들을 모음.
    *   **VI (Vietnamese) (Tiếng Việt):** Gom các hàm có tính chất logic giống nhau (VD: Hàm in các loại báo cáo, mặc dù báo cáo khác nhau).
7.  **우연적 응집도 (Coincidental) - XẤU NHẤT:**
    *   **Korean:** 아무 관련 없이 구성됨.
    *   **VI (Vietnamese) (Tiếng Việt):** Các phần tử gom lại ngẫu nhiên, không liên quan gì nhau.

---

Điểm chốt của **4. 응집도 (Cohesion - Độ gắn kết)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **5. Fan-In / Fan-Out (팬인 / 팬아웃)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.