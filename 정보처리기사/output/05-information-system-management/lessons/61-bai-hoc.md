# 프로세스 동작 특성 (Process Behavior: Locality, Working Set, Thrashing)

## 프로세스 동작 특성 (Process Behavior: Locality, Working Set, Thrashing)

### 1. Locality (국부성, 구역성)
프로세스 실행 중 일부 페이지만 집중적으로 참조하는 성질.
- **시간 구역성 (Temporal Locality)**: 하나의 페이지를 짧은 시간 동안 집중 참조 (반복문, 스택 등).
- **공간 구역성 (Spatial Locality)**: 특정 위치 주변의 페이지를 집중 참조 (배열, 순차적 코드 등).

### 2. 워킹 셋 (Working Set)
프로세스가 일정 시간 동안 자주 참조하는 페이지들의 집합. (시간에 따라 변함). 주기억장치에 상주시키면 페이지 부재 현상이 줄어듭니다.

### 3. 스래싱 (Thrashing)
프로세스 처리 시간보다 페이지 교체에 소요되는 시간이 더 많아져 시스템 성능이 급격히 저하되는 현상.
- **방지 방법**: 다중 프로그래밍 정도 조절, 페이지 부재 빈도 조절, 워킹 셋 유지 등.

> **Vietnamese Explanation**:
> **Locality** là tính cục bộ (hay dùng lại chỗ vừa dùng). **Working Set** là tập hợp các trang bộ nhớ đang được dùng nhiều nhất, cần giữ lại ở RAM. **Thrashing** là hiện tượng "giậm chân tại chỗ", máy bận rộn tráo đổi dữ liệu với ổ cứng nhiều hơn là thực sự chạy chương trình, làm máy bị đơ.
