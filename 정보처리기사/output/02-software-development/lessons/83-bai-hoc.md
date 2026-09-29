# 핵심 110: RAM (Random Access Memory)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **핵심 110: RAM (Random Access Memory)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **핵심 110: RAM (Random Access Memory)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **핵심 111 & 112: 반도체 기억소자 및 자기 코어 (Semiconductor Memory & Magnetic Core)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

핵심, RAM

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **38. 릴리즈 노트 (Release Note)**에서 만든 기준을 이어받아 **핵심 110: RAM (Random Access Memory)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **핵심 110: RAM (Random Access Memory)** và nối nó với **핵심 111 & 112: 반도체 기억소자 및 자기 코어 (Semiconductor Memory & Magnetic Core)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 핵심 110: RAM (Random Access Memory)

Sau khi đã đặt nền bằng **38. 릴리즈 노트 (Release Note)**, ta chuyển sang **핵심 110: RAM (Random Access Memory)**. Đây là mắt xích 83/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **핵심 110: RAM (Random Access Memory)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng cho ta tiêu chí đối chiếu, còn công thức cho ta quan hệ giữa các đại lượng; hãy dùng cả hai để kiểm tra cùng một kết luận.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “핵심 110: RAM (Random Access Memory)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 자유롭게 읽고 쓸 수 있는 기억장치로, RWM(Read Write Memory)이라고도 한다. (Bộ nhớ có thể đọc và ghi tự do.)
- RAM에는 현재 사용중인 프로그램이나 데이터가 저장되어 있다. (Lưu trữ chương trình và dữ liệu đang được sử dụng hiện tại.)
- 전원이 꺼지면 기억된 내용이 모두 사라지는 휘발성 메모리이다. (Bộ nhớ dễ bay hơi, mất dữ liệu khi tắt nguồn.)
- 일반적으로 ‘주기억장치’ 또는 ‘메모리’라고 하면 램을 의미한다. (Thường được gọi là bộ nhớ chính hoặc đơn giản là 'bộ nhớ'.)

| 구분 (Phân loại) | DRAM (Dynamic RAM - RAM động) | SRAM (Static RAM - RAM tĩnh) |
|---|---|---|
| 구성소자 (Thành phần) | 콘덴서 (Tụ điện) | 플립플롭 (Flip-Flop) |
| 특징 (Đặc điểm) | 전하가 방전되므로 주기적인 재충전(Refresh)이 필요함 (Cần làm mới định kỳ do tụ điện bị phóng điện) | 전원이 공급되는 동안에는 기억 내용이 유지 (Giữ nội dung miễn là có nguồn) |
| 전력소모 (Tiêu thụ điện) | 적음 (Ít) | 많음 (Nhiều) |
| 접근속도 (Tốc độ) | 느림 (Chậm) | 빠름 (Nhanh) |
| 집적도 (Mật độ) | 높음 (Cao - dung lượng lớn) | 낮음 (Thấp - dung lượng nhỏ) |
| 가격 (Giá) | 저가 (Rẻ) | 고가 (Đắt) |
| 용도 (Sử dụng cho) | 일반적인 주기억장치 (Bộ nhớ chính thông thường) | 캐시 메모리 (Bộ nhớ đệm / Cache) |

- **Vietnamese Explanation:** RAM là bộ nhớ làm việc của máy tính. DRAM rẻ, dung lượng cao nhưng chậm và hay quên (phải refresh liên tục), thường dùng làm thanh RAM máy tính. SRAM đắt, dung lượng nhỏ nhưng cực nhanh, không cần refresh, dùng làm Cache trong CPU.
- **Ví dụ (Example):** SRAM giống như bộ nhớ ngắn hạn của bạn khi tính nhẩm (nhanh nhưng nhớ được ít số). DRAM giống như cuốn sổ nháp (nhớ được nhiều nhưng phải tra cứu chậm hơn, và chốc chốc phải tô lại chữ mờ - refresh).
- 💡 **Mẹo ghi nhớ (Mnemonics):** **S**RAM = **S**iêu tốc (Flip-Flop, Cache). **D**RAM = **D**ump (Đổ liên tục - Refresh, Tụ điện, RAM thường).

---

Ta có thể khép mục **핵심 110: RAM (Random Access Memory)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **핵심 111 & 112: 반도체 기억소자 및 자기 코어 (Semiconductor Memory & Magnetic Core)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.