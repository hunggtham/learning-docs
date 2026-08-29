# 가상기억장치 및 페이지 교체 (Virtual Memory & Page Replacement)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **가상기억장치 및 페이지 교체 (Virtual Memory & Page Replacement)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

가상기억장치, 페이지, 교체

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 가상기억장치 및 페이지 교체 (Virtual Memory & Page Replacement)
### 290. 페이징 기법 (Paging / Phân trang)
- 프로그램을 **동일한 크기**로 나눔 (Chia chương trình thành các phần có kích thước BẰNG NHAU).
- 프로그램 단위 = 페이지 (Page), 기억장치 단위 = 페이지 프레임 (Page Frame).
- **내부 단편화 (Internal Fragmentation)** 발생 가능. (Có thể xảy ra phân mảnh trong).

### 291. 세그먼테이션 기법 (Segmentation / Phân đoạn)
- 프로그램을 배열이나 함수 같은 **다양한 크기의 논리적인 단위**로 나눔. (Chia theo khối logic kích thước KHÁC NHAU).
- **외부 단편화 (External Fragmentation)** 발생 가능. (Có thể xảy ra phân mảnh ngoài).
  - 💡 *Mẹo ghi nhớ*: Page = Kích thước cố định (Sinh ra rác bên trong). Segment = Kích thước logic (Sinh ra rác bên ngoài).

### 292. 페이지 교체 알고리즘 (Page Replacement Algorithms / Thuật toán thay thế trang)
- **OPT (Optimal)**: 앞으로 가장 오랫동안 사용하지 않을 페이지 교체. (Thay thế trang sẽ lâu được dùng nhất trong tương lai - Tốt nhất nhưng khó thực hiện).
- **FIFO (First In First Out)**: 가장 먼저 들어온 페이지 교체. (Vào trước ra trước).
- **LRU (Least Recently Used)**: 최근에 가장 오랫동안 사용하지 않은 페이지 교체. (Thay thế trang lâu nhất chưa được truy cập).
- **LFU (Least Frequently Used)**: 사용 빈도가 가장 적은 페이지 교체. (Thay thế trang có số lần truy cập ít nhất).
- **NUR (Not Used Recently)**: 참조 비트와 변형 비트 사용. (Tương tự LRU nhưng dùng 2 bit để theo dõi).

### 293. 페이지 크기 (Page Size / Kích thước trang)
- **작을 경우 (Kích thước nhỏ)**: 단편화 감소, 매핑 늦어짐, 디스크 접근 많아짐. (Phân mảnh ít, nhưng bảng ánh xạ lớn, truy cập ổ đĩa nhiều hơn).
- **클 경우 (Kích thước lớn)**: 단편화 증가, 매핑 빨라짐, 불필요한 내용까지 적재될 수 있음. (Phân mảnh nhiều, ánh xạ nhanh, có thể load cả những phần thừa).

### 294. Locality (국부성 / Tính địa phương)
- 프로세스가 실행되는 동안 주기억장치의 일부 페이지만 집중적으로 참조하는 성질. (Tiến trình có xu hướng chỉ tập trung truy cập một số trang cụ thể).
- **시간 구역성 (Temporal Locality)**: Loop, 스택, 변수 (Vòng lặp, stack, biến - Truy cập cùng 1 chỗ nhiều lần).
- **공간 구역성 (Spatial Locality)**: 배열 순회, 순차적 코드 (Mảng, mã tuần tự - Truy cập các ô nhớ cạnh nhau).

### 295. 워킹 셋 (Working Set / Tập làm việc)
- 프로세스가 자주 참조하는 페이지들의 집합. (Tập hợp các trang được truy cập thường xuyên nhất).
- 주기억장치에 상주시킴으로써 페이지 부재(Page Fault)를 줄인다. (Giữ trong RAM để giảm thiểu lỗi trang).

### 296. 스래싱 (Thrashing / Hiện tượng tráo đổi quá mức)
- 페이지 교체 시간이 처리 시간보다 많아지는 현상. (Mất thời gian hoán đổi trang nhiều hơn thời gian xử lý thực tế).
- 방지: 다중 프로그래밍 정도 조절, 워킹 셋 유지. (Kiểm soát đa nhiệm, dùng Working Set).
