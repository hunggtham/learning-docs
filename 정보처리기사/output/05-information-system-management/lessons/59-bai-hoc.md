# 메모리 관리 (Memory Management)

## 메모리 관리 (Memory Management)

### 1. 배치 전략 (Placement Strategy)
새로 반입되는 프로그램이나 데이터를 주기억장치의 어디에 위치시킬 것인지 결정합니다.
- **최초 적합 (First Fit)**: 빈 영역 중 첫 번째 분할 영역에 배치.
- **최적 적합 (Best Fit)**: 단편화(Fragmentation/Khoảng trống thừa)를 가장 작게 남기는 분할 영역에 배치.
- **최악 적합 (Worst Fit)**: 단편화를 가장 많이 남기는 분할 영역에 배치.

### 2. 가상기억장치 구현 기법 (Virtual Memory Techniques)
Phần “2. 가상기억장치 구현 기법 (Virtual Memory Techniques)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **페이징(Paging) 기법**: 가상기억장치와 주기억장치를 **동일한 크기**로 나누어 적재. (프로그램 단위: 페이지, 주기억장치 단위: 페이지 프레임)
  - 외부 단편화는 발생하지 않으나, **내부 단편화**는 발생 가능.
- **세그먼테이션(Segmentation) 기법**: 프로그램을 배열이나 함수 등 **다양한 크기의 논리적인 단위(세그먼트)**로 나누어 적재.
  - 내부 단편화는 발생하지 않으나, **외부 단편화**는 발생 가능.

💡 **Mẹo ghi nhớ (Mnemonics):**
- **Paging**: Bằng nhau (Page). Lỗi nội bộ (내부 단편화).
- **Segmentation**: Khác nhau (Theo logic). Lỗi bên ngoài (외부 단편화).
