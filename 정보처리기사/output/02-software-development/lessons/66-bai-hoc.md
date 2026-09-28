# 55. APM (애플리케이션 성능 관리/모니터링)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **55. APM (애플리케이션 성능 관리/모니터링)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

APM

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **50. 애플리케이션 성능 측정 지표 (Performance Metrics)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **24. 인터페이스 보안 - 네트워크 영역 (Interface Security - Network Area)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **55. APM (애플리케이션 성능 관리/모니터링)** và nối nó với **24. 인터페이스 보안 - 네트워크 영역 (Interface Security - Network Area)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 55. APM (애플리케이션 성능 관리/모니터링)
* 애플리케이션의 성능 관리를 위해 자원 현황, 트랜잭션 등을 모니터링.
* **리소스 방식**: Nagios, Zabbix, Cacti.
* **엔드투엔드(End-to-End) 방식**: VisualVM, 제니퍼(Jennifer), 스카우터(Scouter).
* **VI (Vietnamese) (Tiếng Việt):** Công cụ giám sát hiệu năng (APM). Có 2 loại: Theo dõi tài nguyên (Nagios) và Từ đầu đến cuối (VisualVM, Scouter).

---
*(이하 전자계산기 구조 파트 - Computer Architecture)*

---

자료구조: 컴퓨터상 자료를 효율적으로 저장하기 위해 만들어진 논리적인 구조 (Cấu trúc logic để lưu trữ dữ liệu hiệu quả).

### 선형 구조 (Linear - Nối tiếp nhau)
- **리스트 (List):** 순서에 의해 나열된 구조. (Cấu trúc tuyến tính).
  - **선형 리스트 (Linear List / Array):** Kích thước cố định (고정), lưu liên tục (연속). Tìm kiếm cực nhanh (검색 빠름), nhưng chèn/xóa cực chậm (삽입, 삭제 느림).
  - **연결 리스트 (Linked List):** Kích thước linh hoạt (가변), liên kết bằng Pointer. Chèn/xóa cực nhanh, nhưng tìm kiếm chậm (phải dò từng cái) và tốn không gian lưu Pointer.
- **스택 (Stack):** LIFO (Last-In-First-Out). Vào/Ra ở một đầu. Dùng cho: Gọi hàm (Subroutine), Lưu địa chỉ trở về, Đệ quy (Recursion), Tính biểu thức toán học, DFS (Duyệt sâu).
- **큐 (Queue):** FIFO (First-In-First-Out). Vào một đầu, ra một đầu. Dùng cho: Lập lịch hệ điều hành (Job Scheduling), Hàng đợi in.
- **데크 (Deque):** Kết hợp ngăn xếp (stack / 스택) và hàng đợi (queue / 큐), có thể Vào/Ra ở CẢ HAI đầu.

### 비선형 구조 (Non-linear - Không nối tiếp)
- **트리 (Tree):** Cây. Có nút (node / 노드) (Đỉnh) và Branch (Nhánh). **Không có chu trình (Cycle).**
- **그래프 (Graph):** Đồ thị. Có Đỉnh (Vertex) và Cạnh (Edge). Có thể có hướng hoặc vô hướng. (Cây là một dạng Đồ thị không có chu trình).

- **Vietnamese Explanation:** Cấu trúc dữ liệu là cách sắp xếp thông tin.
  - tuyến tính (linear / 선형) danh sách (list / 목록) như dãy ghế đá (tìm số ghế thì nhanh, nhưng muốn chen vào giữa phải bắt mọi người xích ra).
  - Linked danh sách (list / 목록) như trò chơi nắm tay nhau (muốn chen vào giữa chỉ cần thả tay và nắm người mới, rất dễ, nhưng tìm người thứ 10 thì phải đếm từ đầu).
  - ngăn xếp (stack / 스택) như hộp bóng bàn (LIFO - vứt vào sau thì lấy ra trước). hàng đợi (queue / 큐) như xếp hàng mua vé (FIFO - ai đến trước mua trước).
- 💡 **Mẹo ghi nhớ (Mnemonics):** ngăn xếp (stack / 스택) = LIFO (Gọi Hàm, Đệ quy). hàng đợi (queue / 큐) = FIFO (Lập lịch). Liên kết (Linked) = Nhanh chèn/xóa, Chậm tìm kiếm.

---
