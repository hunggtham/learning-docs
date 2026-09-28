# 28. 선형 리스트 심화: 연속 리스트 vs 연결 리스트 (Contiguous vs Linked List)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **28. 선형 리스트 심화: 연속 리스트 vs 연결 리스트 (Contiguous vs Linked List)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

선형, 리스트, 심화, 연속, 연결

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **27. JSON 및 AJAX (JSON & AJAX)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **33. DBMS (데이터베이스 관리 시스템)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **28. 선형 리스트 심화: 연속 리스트 vs 연결 리스트 (Contiguous vs Linked List)** và nối nó với **33. DBMS (데이터베이스 관리 시스템)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 28. 선형 리스트 심화: 연속 리스트 vs 연결 리스트 (Contiguous vs Linked List)
* 앞서 배운 선형 리스트는 두 가지로 나뉩니다.
* **연속 리스트 (Contiguous List - 예: 배열)**:
  * 연속되는 기억장소에 저장. 기억장소 이용 효율 밀도가 1(가장 좋음).
  * 중간에 데이터를 삽입/삭제 시 자료의 이동이 필요(오버헤드 발생).
* **연결 리스트 (Linked List)**:
  * 임의의 기억공간에 저장하며, 포인터(링크)를 이용해 서로 연결.
  * 노드의 삽입/삭제가 용이. 순차 리스트에 비해 기억 공간 이용 효율은 낮고, 포인터를 찾는 시간 때문에 접근 속도가 느림.
  * 중간 노드가 끊어지면 다음 노드를 찾기 힘듦.
* **오버플로/언더플로 (Overflow/Underflow)**: 스택/리스트가 꽉 찬 상태에서 삽입하면 Overflow, 빈 상태에서 삭제하면 Underflow 발생.
* **VI (Vietnamese) (Tiếng Việt):**
  * Contiguous danh sách (list / 목록) (Mảng): Dữ liệu lưu liên tiếp. Chèn/Xóa chậm do phải dịch chuyển dữ liệu. Mật độ = 1.
  * Linked danh sách (list / 목록): Dữ liệu lưu rải rác, nối bằng pointer. Chèn/Xóa nhanh, nhưng truy cập chậm.
* 💡 **Mẹo ghi nhớ**: Array = Nhà chung cư sát vách. Linked danh sách (list / 목록) = Các nhà rải rác nhưng có bản đồ chỉ đường đến nhà tiếp theo.
