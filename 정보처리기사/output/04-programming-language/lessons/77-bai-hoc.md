# 292. 페이지 교체 알고리즘 (Thuật toán thay thế trang / Page Replacement)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **292. 페이지 교체 알고리즘 (Thuật toán thay thế trang / Page Replacement)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

페이지, 교체, 알고리즘

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **287. UNIX 시스템의 구성 (Cấu trúc hệ thống UNIX)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **298. PCB (Process Control Block)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **292. 페이지 교체 알고리즘 (Thuật toán thay thế trang / Page Replacement)** và nối nó với **298. PCB (Process Control Block)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 292. 페이지 교체 알고리즘 (Thuật toán thay thế trang / Page Replacement)
### TẦNG A – ghi chú (note / 노트) NÉN (ÔN / ĐI THI)
- **개념 (Khái niệm)**: 주기억장치 빈 공간이 없을 때 어떤 페이지를 내보낼지 결정하는 기법. (Kỹ thuật chọn trang để loại bỏ khi bộ nhớ chính đã đầy để nhường chỗ cho trang mới.)
- **핵심 키워드 (Từ khóa)**: OPT, FIFO, LRU, LFU, NUR.
- **시험 포인트 (Điểm thi)**: 각 알고리즘별 교체 대상 선정 기준 묻는 문제. (Tiêu chí chọn trang của từng thuật toán.)

### TẦNG B – ghi chú (note / 노트) 보충 (HIỂU SÂU)
- **OPT (Optimal)**: 앞으로 가장 오랫동안 안 쓸 페이지 교체 (이론적 최고). (Thay trang sẽ lâu nhất không được dùng trong tương lai - Tốt nhất nhưng chỉ trên lý thuyết.)
- **FIFO (First-In First-Out)**: 들어온 지 가장 오래된 페이지 교체. (Thay trang vào bộ nhớ sớm nhất.)
- **LRU (Least Recently Used)**: 최근에 가장 오랫동안 안 쓴 페이지 교체. (Thay trang lâu nhất chưa được sử dụng tính từ hiện tại.)
- **LFU (Least Frequently Used)**: 참조 횟수가 가장 적은 페이지 교체. (Thay trang có số lần sử dụng ít nhất.)
- **NUR (Not Used Recently)**: 참조 비트(R)와 변형/수정 비트(M)를 조합해 낮은 등급의 페이지부터 교체한다. (Dùng hai bit R/M để phân loại và thay trang.)
- **예시 (Ví dụ)**: 스마트폰에서 앱을 여러 개 켜다가 램이 부족해지면, 제일 먼저 켰던 앱(FIFO)을 끄거나 최근에 가장 안 본 앱(LRU)을 종료시킴. (Khi điện thoại đầy RAM, nó sẽ tắt app mở đầu tiên (FIFO) hoặc app lâu rồi chưa đụng tới (LRU).)
- 💡 **Mẹo ghi nhớ**: **R**ecently = Lâu không đụng (Thời gian), **F**requently = Ít dùng (Số lần).
