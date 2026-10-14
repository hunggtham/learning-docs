# 페이지 교체 알고리즘과 페이지 크기 (Page Replacement & Size)

## 페이지 교체 알고리즘과 페이지 크기 (Page Replacement & Size)

### 1. 페이지 교체 알고리즘 (Page Replacement Algorithms)
페이지 부재(Page Fault) 발생 시, 어떤 페이지 프레임을 교체할 것인지 결정합니다.
- **OPT (Optimal)**: 앞으로 가장 오랫동안 사용하지 않을 페이지 교체 (가장 효율적이나 미래 예측이 필요해 비현실적).
- **FIFO (First In First Out)**: 가장 먼저 들어와서 가장 오래 있었던 페이지 교체.
- **LRU (Least Recently Used)**: 최근에 가장 오랫동안 사용하지 않은 페이지 교체 (계수기나 스택 사용).
- **LFU (Least Frequently Used)**: 사용 빈도(횟수)가 가장 적은 페이지 교체.
- **NUR (Not Used Recently)**: LRU의 오버헤드를 줄이기 위해 참조 비트와 변형 비트를 사용하여 최근 사용 안 된 페이지 교체.
- **SCR (Second Chance Replacement)**: FIFO의 단점을 보완하여 자주 사용되는 페이지는 한 번 더 기회를 줌.

### 2. 페이지 크기 (Page Size)
Phần “2. 페이지 크기 (Page Size)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **크기가 작을 경우**: 페이지 단편화 감소, 워킹 셋 효율 증가, Locality 일치로 기억장치 효율 상승. 단, 페이지 맵 테이블 크기가 커지고 매핑 속도가 느려지며 디스크 입출력 횟수가 증가.
- **크기가 클 경우**: 페이지 맵 테이블 크기 감소, 매핑 속도 상승, 디스크 입출력 횟수 감소. 단, 불필요한 내용까지 적재될 수 있고 페이지 단편화가 증가.
