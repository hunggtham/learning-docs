# Python Part 3 — cấp cao (senior / 시니어): Packaging, testing, tính đồng thời (concurrency / 동시성) và môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)

> **Mạch đọc:** Đặt **Python Part 3 — cấp cao (senior / 시니어): Packaging, testing, tính đồng thời (concurrency / 동시성) và môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. dự án (project / 프로젝트) môi trường (environment / 환경): trình thông dịch (interpreter / 인터프리터) và phụ thuộc (dependency / 의존성) là một phần của chương trình** sang **2. Packaging và phân phối (distribution / 분포) mô hình (model / 모델)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


> Baseline: Python 3.14.7. Kiểm chứng: 2026-09-22.

Part này giả định bạn đã hiểu đối tượng (object / 객체)/tham chiếu (reference / 참조), mô hình dữ liệu (data model / 데이터 모델), iterable/generator, exception và standard-library boundaries. Mục tiêu chuyển từ “viết Python chạy được” sang “xây Python dự án (project / 프로젝트) có thể tái lập, kiểm chứng, chạy đồng thời và vận hành an toàn”.

## 1. dự án (project / 프로젝트) môi trường (environment / 환경): trình thông dịch (interpreter / 인터프리터) và phụ thuộc (dependency / 의존성) là một phần của chương trình

`môi trường ảo (virtual environment / 가상 환경)`

Python dự án (project / 프로젝트) không chỉ gồm `.py`. hành vi (behavior / 동작) còn phụ thuộc trình thông dịch (interpreter / 인터프리터) phiên bản (version / 버전), installed distributions, OS/bản địa (native / 네이티브) libraries, môi trường (environment / 환경) variables và bên ngoài (external / 외부) services. Nếu hai máy cài phụ thuộc (dependency / 의존성) khác nhau, cùng nguồn (source / 소스) có thể cho hành vi (behavior / 동작) khác.

`venv` tạo môi trường có trình thông dịch (interpreter / 인터프리터) ngữ cảnh (context / 맥락) và site-packages tách khỏi toàn cục (global / 전역) môi trường (environment / 환경):

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
```

Activation chủ yếu sửa shell `PATH`; nó không tạo bộ chứa (container / 컨테이너) hay bảo mật (security / 보안) sandbox. Trong automation/CI, có thể gọi trực tiếp `.venv/bin/python` thay vì phụ thuộc activation.

Cấp cao (senior / 시니어) ghi chú (note / 노트): đừng `pip install` bừa vào hệ thống (system / 시스템) Python trên máy chủ (server / 서버). Cần ranh giới (boundary / 경계) rõ giữa OS-owned Python và application-owned môi trường (environment / 환경).

## 2. Packaging và phân phối (distribution / 분포) mô hình (model / 모델)

`gói phân phối (distribution package / 배포 패키지)`

`gói import (import package / 임포트 패키지)`

Tên gói (package / 패키지) import và tên phân phối (distribution / 분포) trên PyPI không bắt buộc giống nhau. `pip install some-name` cài phân phối (distribution / 분포) siêu dữ liệu (metadata / 메타데이터)/files; `import some_name` thao tác với import hệ thống (system / 시스템). Đây là nguồn nhầm lẫn phổ biến.

Hiện đại (modern / 현대적) packaging lấy `pyproject.toml` làm cấu hình (configuration / 구성) hub. Ba vùng quan trọng là `[build-system]`, `[project]` và `[tool.*]`.

```toml
[build-system]
requires = ["hatchling>=1.26"]
build-backend = "hatchling.build"

[project]
name = "report-worker"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = [
  "httpx>=0.28,<1",
]

[project.optional-dependencies]
dev = ["pytest>=8"]
```

`[build-system]` nói cần gì để bản dựng (build / 빌드). `[project]` mô tả dự án (project / 프로젝트) siêu dữ liệu (metadata / 메타데이터)/dependencies. `[tool.*]` dành cấu hình (config / 설정) của công cụ (tool / 도구). Đừng trộn khái niệm bản dựng (build / 빌드) backend, gói (package / 패키지) installer và phụ thuộc (dependency / 의존성) resolver thành một từ “pip”.

### Phụ thuộc (dependency / 의존성) groups

Packaging ecosystem hiện có standardized phụ thuộc (dependency / 의존성) groups trong `pyproject.toml` cho nhóm development/nội bộ (internal / 내부) như kiểm thử (test / 테스트)/docs mà không cần trở thành dự án (project / 프로젝트) siêu dữ liệu (metadata / 메타데이터)/thời gian chạy (runtime / 런타임) phụ thuộc (dependency / 의존성). công cụ (tool / 도구) hỗ trợ (support / 지원) cần được kiểm tra theo công cụ (tool / 도구)/phiên bản (version / 버전) thực tế.

```toml
[dependency-groups]
test = ["pytest>=8", "coverage"]
```

### `requirements.txt` có còn dùng được không?

Có. Nó là format/tooling convention rất phổ biến cho môi trường (environment / 환경) installation/pinning. `pyproject.toml` giải quyết dự án (project / 프로젝트) siêu dữ liệu (metadata / 메타데이터)/bản dựng (build / 빌드) và ngày càng nhiều phụ thuộc (dependency / 의존성) workflows; không nên tuyên bố `requirements.txt` “đã chết”. Chọn mô hình (model / 모델) dựa vào ứng dụng (application / 애플리케이션)/thư viện (library / 라이브러리), triển khai (deployment / 배포) và toolchain.

### Pinning chiến lược (strategy / 전략)

Thư viện (library / 라이브러리) thường không nên pin mọi thời gian chạy (runtime / 런타임) phụ thuộc (dependency / 의존성) tới chính xác (exact / 정확한) patch vì sẽ làm phụ thuộc (dependency / 의존성) resolution của bên tiêu thụ (consumer / 소비자) quá cứng. ứng dụng (application / 애플리케이션)/triển khai (deployment / 배포) thường cần khóa (lock / 잠금)/reproducibility mạnh hơn. Tách “declared tính tương thích (compatibility / 호환성) phạm vi (range / 범위)” khỏi “resolved deploy môi trường (environment / 환경)”.

### Nguồn (source / 소스) phân phối (distribution / 분포), wheel và bản dựng (build / 빌드) ranh giới (boundary / 경계)

Một nguồn (source / 소스) phân phối (distribution / 분포) (`sdist`) mang nguồn (source / 소스) + siêu dữ liệu (metadata / 메타데이터) cần thiết để bản dựng (build / 빌드); wheel là sản phẩm tạo ra (artifact / 산출물) đã bản dựng (build / 빌드) theo wheel format. Pure-Python wheel thường portable rộng hơn, còn wheel chứa bản địa (native / 네이티브) extension bị ràng buộc bởi Python/ABI/nền tảng (platform / 플랫폼) tags. Vì vậy “cài cùng phiên bản (version / 버전) gói (package / 패키지)” vẫn chưa đủ để kết luận hai máy chạy cùng nhị phân (binary / 이진) đường dẫn (path / 경로).

Khi installer không tìm được wheel phù hợp, nó có thể phải bản dựng (build / 빌드) từ nguồn (source / 소스) tùy dự án (project / 프로젝트)/toolchain. Lúc đó trình biên dịch (compiler / 컴파일러), header, hệ thống (system / 시스템) thư viện (library / 라이브러리) và bản dựng (build / 빌드) backend trở thành phụ thuộc (dependency / 의존성) của installation. Đây là lý do lỗi “máy nhà phát triển (developer / 개발자) cài được nhưng môi trường vận hành (production / 운영 환경) không cài được” đôi khi không nằm ở nguồn (source / 소스) ứng dụng (application / 애플리케이션) mà ở sản phẩm tạo ra (artifact / 산출물) tính tương thích (compatibility / 호환성).

Bản dựng (build / 빌드) backend cũng là mã (code / 코드) được thực thi trong bản dựng (build / 빌드) môi trường (environment / 환경). `[build-system].requires` vì vậy nằm ở trust/supply-chain ranh giới (boundary / 경계), không phải siêu dữ liệu (metadata / 메타데이터) thụ động. CI có yêu cầu bảo mật (security / 보안) cao nên kiểm soát nguồn (source / 소스), phiên bản (version / 버전), bộ nhớ đệm (cache / 캐시) và bản dựng (build / 빌드) isolation tương ứng.

### Editable install không phải triển khai (deployment / 배포) sản phẩm tạo ra (artifact / 산출물)

Editable install hữu ích cho development vì import có thể trỏ trực tiếp tới working cây (tree / 트리). Nhưng hành vi (behavior / 동작) editable phụ thuộc bản dựng (build / 빌드) backend và development bố cục (layout / 레이아웃); nó không chứng minh wheel/sdist publish ra sẽ đúng. thư viện (library / 라이브러리)/gói (package / 패키지) nên có ít nhất một đường kiểm thử (test / 테스트) sản phẩm tạo ra (artifact / 산출물) thật: bản dựng (build / 빌드) wheel/sdist rồi cài vào môi trường (environment / 환경) sạch để phát hiện thiếu tệp (file / 파일), sai gói (package / 패키지) dữ liệu (data / 데이터), entry điểm (point / 지점) hoặc siêu dữ liệu (metadata / 메타데이터).

## 3. Import kiến trúc (architecture / 아키텍처) và phụ thuộc (dependency / 의존성) direction

Circular import thường là kiến trúc (architecture / 아키텍처) smell. tầng (layer / 계층) thấp không nên import ngược tầng (layer / 계층) orchestration chỉ để lấy utility. Một cấu trúc đơn giản:

```text
app/
  domain/
  services/
  adapters/
  cli.py
```

Lĩnh vực (domain / 도메인) giữ lô-gic (logic / 논리) và lớp trừu tượng (abstraction / 추상화); adapter biết filesystem/HTTP/cơ sở dữ liệu (database / 데이터베이스); entry điểm (point / 지점) wire dependencies. Đây không phải khung phần mềm (framework / 프레임워크) bắt buộc, mà là phụ thuộc (dependency / 의존성) direction giúp kiểm thử (test / 테스트)/import đơn giản.

Avoid `sys.path.append(...)` trong ứng dụng (application / 애플리케이션) như fix packaging. Nó thay import tìm kiếm (search / 검색) đường dẫn (path / 경로) thời gian chạy (runtime / 런타임) và che cấu trúc gói (package / 패키지) sai. Hãy cài dự án (project / 프로젝트) editable khi phát triển hoặc cấu hình gói (package / 패키지) đúng.

## 4. Testing: kiểm chứng đặc tả hợp đồng (contract / 계약), không kiểm chứng hiện thực (implementation / 구현) trivia

`kiểm thử đơn vị (unit test / 단위 테스트)`

`kiểm thử tích hợp (integration test / 통합 테스트)`

Kiểm thử (test / 테스트) tốt bảo vệ observable hành vi (behavior / 동작)/bất biến (invariant / 불변식). kiểm thử (test / 테스트) quá dính nội bộ (internal / 내부) lời gọi (call / 호출) count/private phương thức (method / 메서드) khiến refactor hợp lệ vẫn phá suite.

```python
def normalize_email(raw: str) -> str:
    return raw.strip().lower()


def test_normalize_email():
    assert normalize_email(" A@EXAMPLE.COM ") == "a@example.com"
```

### `pytest`

`pytest` là third-party công cụ (tool / 도구), không thuộc thư viện chuẩn (standard library / 표준 라이브러리) nhưng là de facto phổ biến. Fixture quản lý kiểm thử (test / 테스트) phụ thuộc (dependency / 의존성)/vòng đời (lifecycle / 생명주기):

```python
import pytest

@pytest.fixture
def sample_users():
    return ["a", "b"]


def test_count(sample_users):
    assert len(sample_users) == 2
```

Fixture không nên trở thành hidden dịch vụ (service / 서비스) locator khổng lồ. phạm vi (scope / 범위) rộng (`session`, `module`) có thể tạo trạng thái dùng chung (shared state / 공유 상태) và thứ tự (order / 순서) phụ thuộc (dependency / 의존성) nếu lạm dụng.

Repository hiện có [automation/test_pipeline.py](../../automation/test_pipeline.py) dùng standard-library `unittest`. Đây là ví dụ tốt để phân biệt concept testing với một kiểm thử (test / 테스트) runner cụ thể: hiểu kiểm thử (test / 테스트) isolation/assertion trước, rồi chọn `unittest` hay `pytest` theo dự án (project / 프로젝트).

### Mocking

Mock ranh giới (boundary / 경계) gây side tác động (effect / 효과)/nondeterminism như HTTP, clock, random nguồn (source / 소스) hoặc bên ngoài (external / 외부) dịch vụ (service / 서비스), chứ không mock mọi hàm (function / 함수) nội bộ. Nếu phải mock 10 collaborator để kiểm thử (test / 테스트) một đối tượng (object / 객체), kiến trúc (architecture / 아키텍처) có thể quá coupling.

Patch tại nơi name được lookup, không nhất thiết nơi hàm (function / 함수) ban đầu được định nghĩa. Điều này bắt nguồn từ name binding/import mô hình (model / 모델) Part 1.

### Thuộc tính (property / 속성)/bất biến (invariant / 불변식) thinking

Ví dụ parser có bất biến (invariant / 불변식) “serialize rồi parse phải bảo toàn giá trị (value / 값) hợp lệ”. Property-based testing có thể tìm edge cases tốt hơn vài example kiểm thử (test / 테스트), nhưng công cụ (tool / 도구) cụ thể như Hypothesis nằm ngoài cốt lõi (core / 핵심) Python.

Một thuộc tính (property / 속성) không nhất thiết là equality tuyệt đối. Parser/normalizer có thể có thuộc tính (property / 속성) “normalize(normalize(x)) == normalize(x)” (idempotence), sorter có thuộc tính (property / 속성) đầu ra (output / 출력) đã ordered và giữ multiset của đầu vào (input / 입력), serializer có thuộc tính (property / 속성) round-trip bảo toàn ngữ nghĩa (semantic / 의미적) giá trị (value / 값). Việc phát biểu bất biến (invariant / 불변식) trước giúp kiểm thử (test / 테스트) không bị khóa vào hiện thực (implementation / 구현) hiện tại.

### Deterministic kiểm thử (test / 테스트): kiểm soát nguồn không xác định thay vì thử lại (retry / 재시도) kiểm thử (test / 테스트)

Flaky kiểm thử (test / 테스트) thường xuất hiện vì kiểm thử (test / 테스트) để clock thật, random toàn cục (global / 전역), UUID, filesystem temp trạng thái (state / 상태), môi trường (environment / 환경) variable, mạng (network / 네트워크) hoặc tác vụ (task / 작업) scheduling quyết định kết quả. thử lại (retry / 재시도) kiểm thử (test / 테스트) chỉ giảm xác suất nhìn thấy bug; nó không biến hệ thống (system / 시스템) thành deterministic.

Một thiết kế (design / 설계) dễ kiểm thử (test / 테스트) đưa nondeterminism qua ranh giới (boundary / 경계) tường minh (explicit / 명시적). Với thời gian (time / 시간), truyền clock/callable; với random, truyền `random.Random` hoặc generator thuộc quyền sở hữu (ownership / 소유권) của thành phần (component / 컴포넌트); với bên ngoài (external / 외부) I/O, dùng adapter/fake phù hợp đặc tả hợp đồng (contract / 계약).

```python
from collections.abc import Callable
from datetime import datetime


def build_record(now: Callable[[], datetime]) -> dict[str, str]:
    return {"created_at": now().isoformat()}
```

Kiểm thử (test / 테스트) có thể truyền fixed `now` mà không patch sâu vào thư viện chuẩn (standard library / 표준 라이브러리). Cùng nguyên tắc áp dụng cho UUID, thử lại (retry / 재시도) sleep, hiện tại (current / 현재) người dùng (user / 사용자) hoặc cờ tính năng (feature flag / 기능 플래그).

Không nên hiểu phụ thuộc (dependency / 의존성) injection là phải dùng khung phần mềm (framework / 프레임워크) DI. Chỉ cần mã (code / 코드) sở hữu nguồn (source / 소스) of nondeterminism ở ranh giới (boundary / 경계) rõ. Khi kiểm thử (test / 테스트) buộc thay toàn cục (global / 전역) môi trường (environment / 환경) (`os.environ`, current working directory, locale, timezone), fixture/ngữ cảnh (context / 맥락) manager phải restore trạng thái (state / 상태) kể cả khi assertion thất bại (fail / 실패); nếu không một kiểm thử (test / 테스트) có thể làm kiểm thử (test / 테스트) sau sai theo thứ tự (order / 순서).

Seed random cũng cần đúng phạm vi (scope / 범위). Seed một toàn cục (global / 전역) generator có thể làm kiểm thử (test / 테스트) khác phụ thuộc thứ tự (order / 순서); tốt hơn là mỗi kiểm thử (test / 테스트)/thành phần (component / 컴포넌트) sở hữu generator riêng khi random là phần của hành vi (behavior / 동작). Mục tiêu không phải “mọi kiểm thử (test / 테스트) không dùng thời gian/random”, mà là cùng đầu vào (input / 입력) + controlled dependencies phải cho hành vi (behavior / 동작) dự đoán được.

## 5. Debugging: quan sát trạng thái (state / 상태) và thực thi (execution / 실행) đường dẫn (path / 경로)

`trình gỡ lỗi (debugger / 디버거)`

Debugging hiệu quả bắt đầu bằng reproducibility: đầu vào (input / 입력) nào, phiên bản (version / 버전) nào, branch/lần ghi nhận (commit / 커밋) nào, môi trường (environment / 환경) nào, thất bại (failure / 실패) ranh giới (boundary / 경계) nào.

Built-in `breakpoint()` thường vào `pdb` theo default hook:

```python
value = compute()
breakpoint()
consume(value)
```

Gỡ lỗi (debug / 디버그) môi trường vận hành (production / 운영 환경) không đồng nghĩa attach debugger vào live tiến trình (process / 프로세스). Logging, metrics, traces, cốt lõi (core / 핵심) dumps/bản địa (native / 네이티브) tooling và reproducible staging thường an toàn hơn.

Exception traceback là call-path bằng chứng (evidence / 증거). Đọc từ exception kiểu (type / 타입)/message rồi đi lên frames để tìm nơi bất biến (invariant / 불변식) đầu tiên bị phá, thay vì chỉ patch frame cuối.

## 6. Profiling trước tối ưu hóa (optimization / 최적화)

`lập hồ sơ hiệu năng (profiling / 프로파일링)`

Hiệu năng (performance / 성능) công việc (work / 작업) cần đo lường (measurement / 측정). CPU profiler cho biết thời gian ở đâu; bộ nhớ (memory / 메모리) profiler/tracemalloc giúp biết allocation ở đâu; benchmark cần warm-up/noise/ngữ cảnh (context / 맥락) phù hợp.

```bash
python -m cProfile -o app.prof app.py
```

`time.perf_counter()` dùng cho elapsed timing ngắn:

```python
from time import perf_counter
start = perf_counter()
run_job()
elapsed = perf_counter() - start
```

Đừng tối ưu một comprehension 2 ms khi mạng (network / 네트워크) lời gọi (call / 호출) mất 800 ms. cấp cao (senior / 시니어) lập luận (reasoning / 추론) ưu tiên dominant chi phí (cost / 비용).

### Thuật toán (algorithm / 알고리즘) trước micro-optimization

Đổi lookup O(n) lặp lại thành chỉ mục (index / 인덱스)/dict có thể lớn hơn nhiều so với đổi cú pháp (syntax / 문법) Python. Sau đó mới xem allocation, serialization, batching, bản địa (native / 네이티브)/vectorized operations hoặc tính đồng thời (concurrency / 동시성).

## 7. bộ nhớ (memory / 메모리): tham chiếu (reference / 참조) thời gian tồn tại (lifetime / 수명), GC, bộ nhớ đệm (cache / 캐시) và đối tượng (object / 객체) đồ thị (graph / 그래프)

CPython chủ yếu dùng tham chiếu (reference / 참조) counting kết hợp cyclic garbage collector. Khi tham chiếu (reference / 참조) count về zero, đối tượng (object / 객체) thường được deallocate sớm; cycle cần cyclic GC nếu các đối tượng (object / 객체) phù hợp. Đây là hiện thực (implementation / 구현) detail quan trọng nhưng không phải đặc tả hợp đồng (contract / 계약) chung của mọi Python hiện thực (implementation / 구현).

Không dựa vào “CPython sẽ destroy ngay” để quản lý tệp (file / 파일)/socket. Dùng ngữ cảnh (context / 맥락) manager tường minh (explicit / 명시적).

Bộ nhớ (memory / 메모리) leak trong Python thường là tham chiếu (reference / 참조) vẫn còn reachable: bộ nhớ đệm (cache / 캐시) không giới hạn, toàn cục (global / 전역) collection, callback registry, tác vụ (task / 작업) còn sống, closure giữ đối tượng (object / 객체) đồ thị (graph / 그래프), hoặc bản địa (native / 네이티브) extension. GC không thể giải phóng đối tượng (object / 객체) nếu chương trình vẫn tham chiếu nó.

`tracemalloc` có thể snapshot allocation Python:

```python
import tracemalloc
tracemalloc.start()
# workload
snapshot = tracemalloc.take_snapshot()
for stat in snapshot.statistics("lineno")[:10]:
    print(stat)
```

### Bộ nhớ đệm (cache / 캐시) là retained trạng thái (state / 상태) có freshness đặc tả hợp đồng (contract / 계약)

Bộ nhớ đệm (cache / 캐시) đổi computation/I/O chi phí (cost / 비용) lấy bộ nhớ (memory / 메모리) + stale-data rủi ro (risk / 위험) + vô hiệu hóa (invalidation / 무효화) độ phức tạp (complexity / 복잡도). Câu hỏi đầu tiên không phải “dùng decorator nào?”, mà là key đại diện định danh (identity / 식별자) gì, kết quả (result / 결과) hợp lệ bao lâu, ai invalidate, bộ nhớ đệm (cache / 캐시) sống ở phạm vi (scope / 범위) nào và bộ nhớ (memory / 메모리) bound ở đâu.

`functools.cache`/`lru_cache` hữu ích cho pure-ish hàm (function / 함수) với hashable arguments:

```python
from functools import lru_cache

@lru_cache(maxsize=1024)
def parse_schema(version: str):
    ...
```

Bộ nhớ đệm (cache / 캐시) hiện thực (implementation / 구현) giữ nội bộ (internal / 내부) cấu trúc (structure / 구조) coherent khi nhiều luồng thực thi (thread / 스레드) truy cập, nhưng điều đó **không đồng nghĩa single-flight**. Nếu hai luồng thực thi (thread / 스레드) cùng miss trước khi kết quả (result / 결과) đầu tiên được bộ nhớ đệm (cache / 캐시), wrapped hàm (function / 함수) có thể chạy hơn một lần. Nếu hàm (function / 함수) có side tác động (effect / 효과) hoặc “chỉ được chạy một lần”, `lru_cache` không phải synchronization thành phần nguyên thủy (primitive / 기본 요소).

Bộ nhớ đệm (cache / 캐시) key cũng giữ references tới arguments/kết quả (result / 결과) cho tới eviction/clear. phương thức (method / 메서드) bộ nhớ đệm (cache / 캐시) có thể giữ `self` thông qua key, khiến instance sống lâu hơn dự kiến. Unbounded `@cache` với key cardinality tăng theo yêu cầu (request / 요청)/người dùng (user / 사용자) có thể trở thành bộ nhớ (memory / 메모리) leak về mặt vận hành dù GC hoạt động hoàn toàn đúng.

Tiến trình (process / 프로세스) mô hình (model / 모델) lại tạo ranh giới (boundary / 경계) khác: bộ nhớ đệm (cache / 캐시) in-memory của mỗi worker không tự chia sẻ với worker/replica khác. vô hiệu hóa (invalidation / 무효화) cục bộ (local / 로컬) không đảm bảo freshness toàn triển khai (deployment / 배포). Vì vậy bộ nhớ đệm (cache / 캐시) tính đúng đắn (correctness / 정확성) phải được lập luận (reasoning / 추론) cùng tiến trình (process / 프로세스)/replica topology, không chỉ cùng hàm (function / 함수) body.

## 8. tính đồng thời (concurrency / 동시성), parallelism và asynchrony là ba khái niệm khác nhau

`đồng thời (concurrency / 동시성)`

`song song (parallelism / 병렬성)`

`bất đồng bộ (asynchrony / 비동기)`

Tính đồng thời (concurrency / 동시성) là nhiều tác vụ (task / 작업) có progress chồng lấn. Parallelism là thực sự chạy computation cùng lúc trên nhiều thực thi (execution / 실행) tài nguyên (resource / 자원). Async là programming mô hình (model / 모델) nơi tác vụ (task / 작업) có thể suspend tại awaitable/sự kiện (event / 이벤트) ranh giới (boundary / 경계) thay vì khối (block / 블록) thực thi (execution / 실행) ngữ cảnh (context / 맥락).

Vì vậy `async def` không đồng nghĩa multi-core và cũng không làm Vòng lặp giới hạn bởi CPU (CPU-bound loop / CPU 바운드 루프) nhanh hơn.

## 9. Threading và dùng chung (shared / 공유) bộ nhớ (memory / 메모리)

Luồng thực thi (thread / 스레드) trong cùng tiến trình (process / 프로세스) chia sẻ bộ nhớ (memory / 메모리). Đây vừa là lợi thế vừa là nguồn race điều kiện (condition / 조건).

```python
from threading import Thread, Lock

counter = 0
lock = Lock()

def increment_many():
    global counter
    for _ in range(100_000):
        with lock:
            counter += 1
```

Không suy luận “có GIL nên mã (code / 코드) thread-safe”. Một logical thao tác (operation / 연산) có thể gồm nhiều bytecode/steps; thư viện (library / 라이브러리) có thể bản phát hành (release / 릴리스) GIL; free-threaded bản dựng (build / 빌드) thay giả định (assumption / 가정); dùng chung (shared / 공유) mutable bất biến (invariant / 불변식) vẫn cần synchronization hoặc kiến trúc (architecture / 아키텍처) tránh trạng thái dùng chung (shared state / 공유 상태).

### GIL trong Python 3.14

`khóa thông dịch toàn cục (Global Interpreter Lock, GIL / 전역 인터프리터 잠금)`

Với CPython bản dựng (build / 빌드) mặc định có GIL, một luồng thực thi (thread / 스레드) phải giữ GIL để thao tác Python objects/execute Python bytecode. Blocking I/O và một số bản địa (native / 네이티브) operations có thể bản phát hành (release / 릴리스) GIL, nên threading vẫn rất hữu ích cho I/O-bound workloads.

Python 3.13 đưa free-threaded bản dựng (build / 빌드) vào experimental; Python 3.14 nâng nó thành officially supported nhưng vẫn optional. Free-threaded bản dựng (build / 빌드) có thể disable GIL và cho threads thực thi Python mã (code / 코드) song song, nhưng extension tính tương thích (compatibility / 호환성), synchronization và hiệu năng (performance / 성능) profile phải được đánh giá. Không viết documentation kiểu “Python không thể chạy threads song song” nữa, cũng không viết kiểu “Python 3.14 đã bỏ GIL”. Cả hai đều sai khi thiếu bản dựng (build / 빌드)/thời gian chạy (runtime / 런타임) ngữ cảnh (context / 맥락).

### Luồng thực thi (thread / 스레드) pool

`concurrent.futures.ThreadPoolExecutor` phù hợp khi muốn bounded worker pool cho blocking I/O hoặc hàm (function / 함수) sync. Bounded tính đồng thời (concurrency / 동시성) quan trọng: 10,000 tasks không có nghĩa 10,000 threads.

### Khóa (lock / 잠금) bảo vệ bất biến (invariant / 불변식), không bảo vệ “một dòng mã (code / 코드)”

Khóa (lock / 잠금) có ý nghĩa khi gắn với một bất biến (invariant / 불변식) của trạng thái dùng chung (shared state / 공유 상태). Ví dụ nếu `available_balance` và `reserved_balance` phải thay đổi atomically theo một transfer, chỉ khóa (lock / 잠금) một phép cộng nhưng để phép trừ ở ngoài vẫn có thể phá bất biến (invariant / 불변식). phạm vi (scope / 범위) khóa (lock / 잠금) phải bao quanh chuyển tiếp trạng thái (state transition / 상태 전이) cần nhìn như một thao tác (operation / 연산) không thể xen kẽ.

Nhiều khóa (lock / 잠금) tạo deadlock rủi ro (risk / 위험). Nếu luồng thực thi (thread / 스레드) A giữ khóa (lock / 잠금) X rồi chờ Y, còn luồng thực thi (thread / 스레드) B giữ Y rồi chờ X, cả hai có thể chờ vô hạn. Hai chiến lược nền là giảm dùng chung (shared / 공유) mutable trạng thái (state / 상태) và giữ khóa (lock / 잠금) thứ tự (ordering / 순서) nhất quán. hết thời gian chờ (timeout / 타임아웃) trên khóa (lock / 잠금) có thể giúp hệ thống thoát một số tình huống nhưng không sửa thiết kế cycle quyền sở hữu (ownership / 소유권).

`RLock` cho phép cùng luồng thực thi (thread / 스레드) acquire lại khóa (lock / 잠금); `Semaphore` giới hạn số worker đồng thời; `Event` truyền tín hiệu (signal / 신호) trạng thái; `Condition` phối hợp chờ một predicate trên trạng thái dùng chung (shared state / 공유 상태). Chọn thành phần nguyên thủy (primitive / 기본 요소) từ bất biến (invariant / 불변식), không từ tên nghe phù hợp.

## 10. Multiprocessing: tiến trình (process / 프로세스) isolation đổi lấy communication chi phí (cost / 비용)

Tiến trình (process / 프로세스) có address không gian (space / 공간) riêng, giúp CPU-bound Python tải công việc (workload / 워크로드) dùng nhiều cốt lõi (core / 핵심) trên GIL-enabled CPython. Đổi lại startup, serialization/IPC, bộ nhớ (memory / 메모리) và operational độ phức tạp (complexity / 복잡도) lớn hơn.

```python
from concurrent.futures import ProcessPoolExecutor

def cpu_work(n: int) -> int:
    return sum(i * i for i in range(n))

if __name__ == "__main__":
    with ProcessPoolExecutor() as pool:
        results = list(pool.map(cpu_work, [1_000_000] * 4))
```

Guard `__main__` đặc biệt quan trọng với multiprocessing start methods/nền tảng (platform / 플랫폼) nơi child import main mô-đun (module / 모듈). dữ liệu (data / 데이터) chuyển giữa processes thường phải serialize, nên đừng gửi đối tượng (object / 객체) đồ thị (graph / 그래프) khổng lồ nếu chi phí (cost / 비용) IPC vượt lợi ích parallelism.

Python 3.14 có thay đổi start-method/nền tảng (platform / 플랫폼) details theo OS; môi trường vận hành (production / 운영 환경) mã (code / 코드) không nên dựa vào giả định (assumption / 가정) “fork luôn là default ở mọi Unix”. Trên POSIX hỗ trợ phù hợp, `forkserver` là default từ 3.14; mã (code / 코드) cần ngữ nghĩa (semantics / 의미론) của `fork` phải chọn tường minh (explicit / 명시적) ngữ cảnh (context / 맥락). macOS và Windows có hành vi (behavior / 동작) platform-specific khác. Start phương thức (method / 메서드) là triển khai (deployment / 배포)/thời gian chạy (runtime / 런타임) choice, không phải chi tiết vô hại.

## 11. `asyncio`: cooperative tính đồng thời (concurrency / 동시성) qua vòng lặp sự kiện (event loop / 이벤트 루프)

`vòng lặp sự kiện (event loop / 이벤트 루프)`

`coroutine (coroutine / 코루틴)`

Vòng lặp sự kiện (event loop / 이벤트 루프) schedule tasks/callbacks và phối hợp non-blocking I/O. Coroutine chạy cho đến khi gặp điểm suspend (`await`) mà awaited thao tác (operation / 연산) chưa hoàn tất, rồi vòng lặp (loop / 루프) có thể chạy tác vụ (task / 작업) khác.

```python
import asyncio

async def fetch_one(client, url):
    return await client.get(url)

async def main():
    async with ... as client:
        a, b = await asyncio.gather(
            fetch_one(client, "https://a.example"),
            fetch_one(client, "https://b.example"),
        )

asyncio.run(main())
```

### Blocking lời gọi (call / 호출) bên trong async

Nếu gọi `time.sleep(10)` hoặc sync HTTP/filesystem thao tác (operation / 연산) nặng trực tiếp trong coroutine, event-loop luồng thực thi (thread / 스레드) bị khối (block / 블록) và các tác vụ (task / 작업) khác không được schedule. Có thể offload blocking hàm (function / 함수) qua `asyncio.to_thread()` khi phù hợp:

```python
result = await asyncio.to_thread(blocking_function, arg)
```

Repository đã dùng mẫu (pattern / 패턴) này trong [automation/app.py](../../automation/app.py): FastAPI endpoint giữ `asyncio.Lock`, rồi `await asyncio.to_thread(Pipeline().run)` để synchronous chuỗi xử lý (pipeline / 파이프라인) không khối (block / 블록) vòng lặp sự kiện (event loop / 이벤트 루프) trực tiếp. Đây là cầu nối (bridge / 브리지) tốt giữa cốt lõi (core / 핵심) cơ chế (mechanism / 메커니즘) và khung phần mềm (framework / 프레임워크) mã (code / 코드); ngữ nghĩa (semantics / 의미론) HTTP/FastAPI nằm ngoài cốt lõi (core / 핵심) thư viện (library / 라이브러리).

Có một giới hạn quan trọng: cancellation của coroutine đang chờ `to_thread()` không phải là cơ chế cưỡng chế dừng OS luồng thực thi (thread / 스레드). Nếu hàm (function / 함수) sync đã bắt đầu chạy, nó có thể tiếp tục side tác động (effect / 효과) sau khi yêu cầu (request / 요청)/tác vụ (task / 작업) async phía ngoài đã hết thời gian chờ (timeout / 타임아웃) hoặc bị cancel. Vì vậy long-running sync công việc (work / 작업) cần cancellation/cooperation riêng nếu nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식) yêu cầu dừng thật: ví dụ cancellation đơn vị từ (token / 토큰)/sự kiện (event / 이벤트) mà hàm (function / 함수) tự kiểm tra, subprocess có vòng đời (lifecycle / 생명주기) riêng, hoặc chuyển công việc (work / 작업) sang job/tiến trình (process / 프로세스) ranh giới (boundary / 경계) có thể terminate theo chính sách (policy / 정책).

### Async không bằng parallelism

Hai coroutine cùng vòng lặp sự kiện (event loop / 이벤트 루프) không chạy Python CPU vòng lặp (loop / 루프) đồng thời chỉ vì dùng `gather`. Nếu coroutine không `await` trong thời gian dài, nó chiếm vòng lặp sự kiện (event loop / 이벤트 루프). CPU-heavy công việc (work / 작업) cần tiến trình (process / 프로세스) pool/bản địa (native / 네이티브) mã (code / 코드)/free-threaded chiến lược (strategy / 전략) hoặc kiến trúc (architecture / 아키텍처) khác.

### `gather()` và `TaskGroup` có thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론) khác nhau

`asyncio.gather()` rất tiện khi muốn thu kết quả theo thứ tự đầu vào (input / 입력). Nhưng với mặc định `return_exceptions=False`, exception đầu tiên được propagate cho caller trong khi các awaitable khác không tự động bị cancel chỉ vì sibling thất bại (fail / 실패). Điều này có thể đúng cho independent công việc (work / 작업), nhưng sai nếu các tác vụ (task / 작업) tạo thành một thao tác (operation / 연산) chung phải “thất bại (fail / 실패) together”.

`TaskGroup` biểu diễn quyền sở hữu (ownership / 소유권) có cấu trúc hơn. Khi một child thất bại (fail / 실패) bằng exception thông thường, group cancel các sibling còn lại và gom thất bại (failure / 실패) khi rời ngữ cảnh (context / 맥락). Vì vậy lựa chọn không phải “API nào mới hơn”, mà là thất bại (failure / 실패) bất biến (invariant / 불변식): các tác vụ độc lập hay là children của cùng một thao tác (operation / 연산)?

### Cancellation là điều khiển (control / 제어) luồng (flow / 흐름)

Tác vụ (task / 작업) cancellation không phải “kill luồng thực thi (thread / 스레드)”. `CancelledError` được inject tại suspension điểm (point / 지점) và cleanup cần `try/finally`/ngữ cảnh (context / 맥락) manager. `CancelledError` kế thừa trực tiếp `BaseException`, nên `except Exception` thông thường không bắt nó. Nếu bắt cancellation để cleanup, đa số mã (code / 코드) nên raise lại; nuốt cancellation có thể phá ngữ nghĩa (semantics / 의미론) của `TaskGroup` và `asyncio.timeout()`.

### Timeouts và structured tính đồng thời (concurrency / 동시성)

Hiện đại (modern / 현대적) asyncio có `asyncio.timeout()` và `TaskGroup` cho vòng đời (lifecycle / 생명주기) có cấu trúc. `TaskGroup` giúp parent phạm vi (scope / 범위) sở hữu child tasks và propagate thất bại (failure / 실패)/cancellation dễ reason hơn so với fire-and-forget tác vụ (task / 작업) không được giữ tham chiếu (reference / 참조).

```python
async with asyncio.TaskGroup() as tg:
    tg.create_task(worker(1))
    tg.create_task(worker(2))
```

Fire-and-forget cần tường minh (explicit / 명시적) quyền sở hữu (ownership / 소유권), logging và shutdown chính sách (policy / 정책); nếu không tác vụ (task / 작업) có thể thất bại (fail / 실패) không ai observe.

### Vòng lặp sự kiện (event loop / 이벤트 루프) APIs hiện đại (modern / 현대적) vs legacy

Ứng dụng (application / 애플리케이션) mã (code / 코드) ưu tiên `asyncio.run()` hoặc `asyncio.Runner`. chính sách (policy / 정책) APIs như `get_event_loop_policy()`/`set_event_loop_policy()` deprecated ở Python 3.14 và dự kiến removed ở 3.16. `get_event_loop()` trong 3.14 cũng không còn ngầm tạo vòng lặp (loop / 루프) nếu không có hiện tại (current / 현재) vòng lặp sự kiện (event loop / 이벤트 루프); trong coroutine/callback, `get_running_loop()` rõ hơn cho low-level mã (code / 코드).

### Context-local trạng thái (state / 상태): `contextvars` không phải toàn cục (global / 전역) mutable trạng thái (state / 상태)

Yêu cầu (request / 요청) ID, dấu vết (trace / 추적) ID hoặc giao dịch (transaction / 트랜잭션) ngữ cảnh (context / 맥락) thường cần “có sẵn” ở nhiều hàm (function / 함수) nhưng không được rò sang yêu cầu (request / 요청)/tác vụ (task / 작업) khác. toàn cục (global / 전역) variable sai vì mọi concurrent công việc (work / 작업) nhìn cùng binding; `threading.local()` lại gắn trạng thái (state / 상태) với OS luồng thực thi (thread / 스레드) và không mô hình đúng khi nhiều asyncio tác vụ (task / 작업) xen kẽ trên cùng luồng thực thi (thread / 스레드).

`contextvars.ContextVar` gắn giá trị (value / 값) với thực thi (execution / 실행) ngữ cảnh (context / 맥락) hiện tại. `asyncio` hỗ trợ ngữ cảnh (context / 맥락) variables bản địa (native / 네이티브), nên child tác vụ (task / 작업) thường nhận ngữ cảnh (context / 맥락) phù hợp mà không cần truyền một toàn cục (global / 전역) mutable dict quanh ứng dụng (application / 애플리케이션).

```python
from contextvars import ContextVar

request_id: ContextVar[str | None] = ContextVar("request_id", default=None)

async def handle(req):
    token = request_id.set(req.id)
    try:
        await service()
    finally:
        request_id.reset(token)
```

Reset bằng đơn vị từ (token / 토큰) làm quyền sở hữu (ownership / 소유권)/thời gian tồn tại (lifetime / 수명) tường minh (explicit / 명시적); không để ngữ cảnh (context / 맥락) cũ bleed sang công việc (work / 작업) sau. ngữ cảnh (context / 맥락) variable nên được khai báo ở mô-đun (module / 모듈) mức (level / 수준) thay vì tạo động trong closure nếu không có lý do đặc biệt, vì `Context` giữ strong tham chiếu (reference / 참조) tới `ContextVar`.

Một detail môi trường vận hành (production / 운영 환경) quan trọng: `asyncio.to_thread()` propagate hiện tại (current / 현재) `contextvars.Context` sang worker luồng thực thi (thread / 스레드). Điều này giúp logging/tracing ngữ cảnh (context / 맥락) tiếp tục nhìn thấy yêu cầu (request / 요청) ID trong sync adapter được offload. Nhưng propagation này không biến mutable đối tượng (object / 객체) nằm trong ngữ cảnh (context / 맥락) thành immutable/thread-safe; nếu ngữ cảnh (context / 맥락) giá trị (value / 값) là một dict mutable được share, vẫn phải lập luận (reasoning / 추론) về aliasing/tính đồng thời (concurrency / 동시성).

Qua tiến trình (process / 프로세스) hoặc subinterpreter ranh giới (boundary / 경계), đừng giả định ngữ cảnh (context / 맥락) tự đi theo. Correlation/tenant/auth ngữ cảnh (context / 맥락) cần trở thành tường minh (explicit / 명시적) message/tác vụ (task / 작업) siêu dữ liệu (metadata / 메타데이터). Đây là cùng nguyên tắc với dấu vết (trace / 추적) propagation trong hệ thống phân tán (distributed system / 분산 시스템): execution-local convenience không thay đặc tả hợp đồng (contract / 계약) qua isolation ranh giới (boundary / 경계).

## 12. Networking cơ bản

Mạng (network / 네트워크) I/O có partial reads/writes, hết thời gian chờ (timeout / 타임아웃), DNS, liên kết (connection / 연결) thất bại (failure / 실패), remote close và backpressure. High-level HTTP máy khách (client / 클라이언트) che nhiều chi tiết nhưng không xóa thất bại (failure / 실패) modes.

Built-in `socket` ở mức thấp. `asyncio` streams cung cấp lớp trừu tượng (abstraction / 추상화) async cao hơn. Với ứng dụng (application / 애플리케이션) nghiệp vụ (business / 비즈니스), thường dùng maintained giao thức (protocol / 프로토콜) thư viện (library / 라이브러리) thay vì tự implement HTTP/TLS.

Hết thời gian chờ (timeout / 타임아웃) không phải một số duy nhất nếu hệ thống cần độ tin cậy (reliability / 신뢰성): connect hết thời gian chờ (timeout / 타임아웃), read hết thời gian chờ (timeout / 타임아웃), total deadline và thử lại (retry / 재시도) ngân sách (budget / 예산) có ngữ nghĩa (semantics / 의미론) khác nhau.

### Thử lại (retry / 재시도)

Thử lại (retry / 재시도) chỉ an toàn khi thao tác (operation / 연산) có ngữ nghĩa (semantics / 의미론) phù hợp/idempotency hoặc có deduplication key. thử lại (retry / 재시도) POST payment một cách mù quáng có thể tạo duplicate side tác động (effect / 효과). Exponential backoff + jitter giảm synchronized thử lại (retry / 재시도) storm, nhưng vẫn cần overall deadline.

Thử lại (retry / 재시도) ngân sách (budget / 예산) phải thuộc cùng độ trễ (latency / 지연 시간)/deadline mô hình (model / 모델). Ba attempt mỗi attempt hết thời gian chờ (timeout / 타임아웃) 10 giây có thể tạo yêu cầu (request / 요청) 30+ giây nếu caller chỉ cho 5 giây. môi trường vận hành (production / 운영 환경) mã (code / 코드) nên propagate remaining deadline hoặc có chính sách (policy / 정책) tổng thay vì để từng tầng (layer / 계층) tự thử lại (retry / 재시도) độc lập.

## 13. bảo mật (security / 보안) trong Python ứng dụng (application / 애플리케이션)

Bảo mật (security / 보안) không phải mô-đun (module / 모듈) riêng; nó cắt ngang đầu vào (input / 입력), serialization, subprocess, phụ thuộc (dependency / 의존성), logging và triển khai (deployment / 배포).

### Untrusted đầu vào (input / 입력)

Validate cấu trúc (structure / 구조)/phạm vi (range / 범위) tại ranh giới (boundary / 경계). Không dùng `eval()` với đầu vào (input / 입력) không tin cậy. `ast.literal_eval()` chỉ parse subset literal nhưng vẫn không phải universal parser cho arbitrary large/malicious tài nguyên (resource / 자원) consumption.

### `pickle`

Không unpickle dữ liệu không tin cậy. Format này có thể kích hoạt đối tượng (object / 객체) reconstruction hành vi (behavior / 동작) nguy hiểm.

### Shell injection

Ưu tiên `subprocess.run([program, arg1, ...], shell=False)`. Nếu `shell=True` là bắt buộc, người dùng (user / 사용자) đầu vào (input / 입력) cần chiến lược (strategy / 전략) escaping/allowlist đúng shell/nền tảng (platform / 플랫폼); tốt nhất tránh ranh giới (boundary / 경계) này.

### Đường dẫn (path / 경로) traversal

Khi người dùng (user / 사용자) điều khiển (control / 제어) filename/đường dẫn (path / 경로), việc ghép vào gốc (root / 루트) cần canonicalization và authorization ranh giới (boundary / 경계). `Path.resolve()` hỗ trợ resolution nhưng bảo mật (security / 보안) quy tắc (rule / 규칙) vẫn phải kiểm tra resulting đường dẫn (path / 경로) thuộc allowed gốc (root / 루트) và symlink ngữ nghĩa (semantics / 의미론) phù hợp.

### Secrets

Secrets không hard-code/lần ghi nhận (commit / 커밋). Lấy từ secret manager/môi trường (environment / 환경)/tệp (file / 파일) permission ranh giới (boundary / 경계) tùy triển khai (deployment / 배포). Đừng log secret khi exception hoặc dump cấu hình (config / 설정).

### Phụ thuộc (dependency / 의존성) supply chuỗi (chain / 사슬)

Pin/khóa (lock / 잠금) deploy môi trường (environment / 환경), rà soát (review / 검토) gói (package / 패키지) provenance, cập nhật (update / 업데이트) bảo mật (security / 보안) fixes và hạn chế gói (package / 패키지) không cần thiết. gói (package / 패키지) name typo có thể trở thành typosquatting rủi ro (risk / 위험). bản dựng (build / 빌드) dependencies cũng thuộc supply chuỗi (chain / 사슬) vì bản dựng (build / 빌드) backend được thực thi trong quá trình tạo sản phẩm tạo ra (artifact / 산출물).

## 14. hiệu năng (performance / 성능) mô hình (model / 모델) thực tế

Python hiệu năng (performance / 성능) thường bị chi phối bởi một trong các lớp: thuật toán (algorithm / 알고리즘)/cấu trúc dữ liệu (data structure / 자료구조), Python trình thông dịch (interpreter / 인터프리터) overhead, allocation/đối tượng (object / 객체) count, I/O độ trễ (latency / 지연 시간), serialization, cơ sở dữ liệu (database / 데이터베이스)/mạng (network / 네트워크) round trip, bản địa (native / 네이티브) thư viện (library / 라이브러리) hoặc tính đồng thời (concurrency / 동시성) kiến trúc (architecture / 아키텍처).

Một số strategies:

- Batch bên ngoài (external / 외부) operations để giảm round trips khi ngữ nghĩa (semantics / 의미론) cho phép.
- Dùng built-in/bản địa (native / 네이티브) hiện thực (implementation / 구현) cho vòng lặp (loop / 루프) nặng khi có API phù hợp.
- Tránh tạo intermediate collections nếu streaming đủ.
- bộ nhớ đệm (cache / 캐시) chỉ khi có vô hiệu hóa (invalidation / 무효화)/bộ nhớ (memory / 메모리) bound rõ.
- Profile trước và sau thay đổi.

Không dùng `asyncio` như hiệu năng (performance / 성능) magic. Async tăng thông lượng (throughput / 처리량)/tính đồng thời (concurrency / 동시성) cho tải công việc (workload / 워크로드) chờ I/O tốt; nó có overhead và độ phức tạp (complexity / 복잡도) riêng.

Hiệu năng (performance / 성능) tối ưu hóa (optimization / 최적화) bằng bộ nhớ đệm (cache / 캐시) phải đo cả hit tỷ lệ (rate / 비율), retained bộ nhớ (memory / 메모리) và freshness chi phí (cost / 비용). Một bộ nhớ đệm (cache / 캐시) có hit tỷ lệ (rate / 비율) 99% nhưng giữ dữ liệu stale sai nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식) không phải tối ưu hóa (optimization / 최적화) thành công.

## 15. môi trường vận hành (production / 운영 환경) triển khai (deployment / 배포) mô hình (model / 모델)

Môi trường vận hành (production / 운영 환경) Python cần xác định rõ entry điểm (point / 지점), tiến trình (process / 프로세스) mô hình (model / 모델), cấu hình (config / 설정), graceful shutdown, health/readiness, logs/metrics, tài nguyên (resource / 자원) limits và triển khai (deployment / 배포) sản phẩm tạo ra (artifact / 산출물).

Một dịch vụ (service / 서비스) containerized không vì dùng Docker mà tự động production-ready. bộ chứa (container / 컨테이너) tiến trình (process / 프로세스) vẫn có thể leak bộ nhớ (memory / 메모리), ignore SIGTERM, không có hết thời gian chờ (timeout / 타임아웃) hoặc ghi trạng thái (state / 상태) vào ephemeral filesystem.

### Tiến trình (process / 프로세스) mô hình (model / 모델)

Nhiều web servers chạy nhiều worker processes. Nếu mỗi tiến trình (process / 프로세스) có toàn cục (global / 전역) bộ nhớ đệm (cache / 캐시)/khóa (lock / 잠금), trạng thái (state / 상태) đó không chia sẻ giữa processes. `asyncio.Lock` chỉ synchronize tasks trong vòng lặp sự kiện (event loop / 이벤트 루프)/tiến trình (process / 프로세스) tương ứng; nó không phải phân tán (distributed / 분산) khóa (lock / 잠금).

Điều này trực tiếp liên quan [automation/app.py](../../automation/app.py): module-level `asyncio.Lock()` ngăn concurrent run trong một app tiến trình (process / 프로세스). Nếu deploy nhiều worker/tiến trình (process / 프로세스)/replica, cần bên ngoài (external / 외부) coordination nếu bất biến (invariant / 불변식) là “toàn hệ thống chỉ một chuỗi xử lý (pipeline / 파이프라인) chạy”. Đây là senior-level distinction giữa in-process tính đồng thời (concurrency / 동시성) điều khiển (control / 제어) và phân tán (distributed / 분산) coordination.

Bộ nhớ đệm (cache / 캐시) cũng theo phạm vi (scope / 범위) tương tự: `lru_cache` hoặc dict toàn cục (global / 전역) trong một worker không phải bộ nhớ đệm (cache / 캐시) toàn triển khai (deployment / 배포). Nếu nghiệp vụ (business / 비즈니스) tính đúng đắn (correctness / 정확성) phụ thuộc invalidate đồng thời ở mọi replica, in-process bộ nhớ đệm (cache / 캐시) chỉ là một tối ưu hóa (optimization / 최적화) tầng (layer / 계층) và phải có freshness chiến lược (strategy / 전략) rõ.

### Graceful shutdown

Shutdown cần ngừng nhận công việc (work / 작업) mới, cho công việc (work / 작업) đang chạy kết thúc hoặc cancel theo deadline, flush cần thiết và bản phát hành (release / 릴리스) tài nguyên (resource / 자원). `finally`, ngữ cảnh (context / 맥락) manager và tác vụ (task / 작업) quyền sở hữu (ownership / 소유권) từ các phần trước chính là nền tảng.

Nếu ứng dụng (application / 애플리케이션) đã offload công việc (work / 작업) sang luồng thực thi (thread / 스레드) mà hàm (function / 함수) không hỗ trợ cooperative cancellation, shutdown deadline có thể hết trong khi luồng thực thi (thread / 스레드) vẫn chạy. Đây là lý do vòng đời (lifecycle / 생명주기) của background công việc (work / 작업) phải được thiết kế từ lúc chọn mô hình thực thi (execution model / 실행 모델), không vá ở tín hiệu (signal / 신호) handler cuối cùng.

### Cấu hình (configuration / 구성)

Môi trường (environment / 환경) variable là một vận chuyển (transport / 전송) phổ biến, không phải lược đồ (schema / 스키마). Parse/validate cấu hình (config / 설정) lúc startup và thất bại (fail / 실패) fast với message rõ. Boolean string như `"false"` là truthy nếu dùng trực tiếp; cần tường minh (explicit / 명시적) parsing.

## 16. trường hợp (case / 사례) study: rà soát (review / 검토) `automation/pipeline.py` bằng cấp cao (senior / 시니어) lens

[automation/pipeline.py](../../automation/pipeline.py) có các lựa chọn đáng học:

Nó dùng argument danh sách (list / 목록) với `subprocess.run`, giữ đơn vị từ (token / 토큰) khỏi command arguments và `.git/config`, đặt hết thời gian chờ (timeout / 타임아웃) cho clone, check return mã (code / 코드), dùng `Path`, guard chi phí (cost / 비용)/API calls và raise khi bên ngoài (external / 외부) phản hồi (response / 응답) không đạt bất biến (invariant / 불변식). Đây là examples nơi Python cốt lõi (core / 핵심) cơ chế (mechanism / 메커니즘) phục vụ môi trường vận hành (production / 운영 환경) an toàn (safety / 안전).

Nhưng cấp cao (senior / 시니어) rà soát (review / 검토) cũng hỏi thêm: HTTP thử lại (retry / 재시도)/deadline chính sách (policy / 정책) thế nào; `timeout=1800` có phù hợp per-request/overall ngân sách (budget / 예산) không; đầu ra (output / 출력) có kích thước (size / 크기) limit không; tiến trình (process / 프로세스) cancellation có propagate vào sync chuỗi xử lý (pipeline / 파이프라인) đang chạy trong luồng thực thi (thread / 스레드) không; một khóa (lock / 잠금) cục bộ (local / 로컬) có đủ khi quy mô (scale / 규모) workers không; cấu hình (config / 설정) parsing có lược đồ (schema / 스키마)/kiểm thử (test / 테스트) không; đơn vị từ (token / 토큰) có thể lộ qua lỗi (error / 오류)/log không; clock/random/môi trường (environment / 환경) có được isolate để kiểm thử (test / 테스트) deterministic không; nếu thêm bộ nhớ đệm (cache / 캐시) thì bộ nhớ đệm (cache / 캐시) key/vô hiệu hóa (invalidation / 무효화)/tiến trình (process / 프로세스) phạm vi (scope / 범위) sẽ là gì. Những câu hỏi này không phải chê mã (code / 코드), mà là cách lập luận (reasoning / 추론) khi ranh giới (boundary / 경계) môi trường vận hành (production / 운영 환경) mở rộng.

## 17. Khi chọn tính đồng thời (concurrency / 동시성) mô hình (model / 모델)

Một quyết định (decision / 결정) ma trận (matrix / 행렬) tối giản:

| tải công việc (workload / 워크로드) | Mô hình bắt đầu xem xét | Lý do chính |
|---|---|---|
| Nhiều blocking I/O sync thư viện (library / 라이브러리) | threads / `to_thread` | overlap thời gian chờ, tích hợp sync mã (code / 코드) |
| Nhiều async sockets/HTTP | `asyncio` | high tính đồng thời (concurrency / 동시성) với tác vụ (task / 작업) nhẹ |
| CPU-bound pure Python trên GIL-enabled bản dựng (build / 빌드) | multiprocessing/tiến trình (process / 프로세스) pool | multi-core qua tiến trình (process / 프로세스) isolation |
| CPU-bound bản địa (native / 네이티브) mã (code / 코드) bản phát hành (release / 릴리스) GIL | threads có thể phù hợp | bản địa (native / 네이티브) công việc (work / 작업) chạy ngoài GIL |
| CPython free-threaded 3.14+ | threads có thể parallel | cần verify bản dựng (build / 빌드), extension an toàn (safety / 안전), synchronization |
| Isolation trong cùng tiến trình (process / 프로세스), tác vụ (task / 작업) phù hợp subinterpreter | `InterpreterPoolExecutor` / multiple interpreters | multi-core + trình thông dịch (interpreter / 인터프리터) isolation, đổi lại tường minh (explicit / 명시적) dữ liệu (data / 데이터) transfer/tính tương thích (compatibility / 호환성) |
| Isolation/độ tin cậy (reliability / 신뢰성) mạnh | processes/services | thất bại (failure / 실패)/trạng thái (state / 상태) ranh giới (boundary / 경계) rõ hơn |

Đây không phải ranking tuyệt đối. dữ liệu (data / 데이터) kích thước (size / 크기), IPC, độ trễ (latency / 지연 시간), thư viện (library / 라이브러리) tính tương thích (compatibility / 호환성) và operational mô hình (model / 모델) có thể đổi quyết định. Multiple interpreters được đào sâu ở Part 4; chúng không phải “tiến trình (process / 프로세스) nhẹ” hay “luồng thực thi (thread / 스레드) có GIL khác” theo nghĩa có thể thay thế mù quáng.

Ngữ cảnh (context / 맥락) propagation cũng phải nằm trong quyết định (decision / 결정). luồng thực thi (thread / 스레드)/tác vụ (task / 작업)/tiến trình (process / 프로세스)/trình thông dịch (interpreter / 인터프리터) có isolation ngữ nghĩa (semantics / 의미론) khác nhau; yêu cầu (request / 요청) siêu dữ liệu (metadata / 메타데이터) tiện lợi trong `ContextVar` không nên được xem như phân tán (distributed / 분산) message ngữ cảnh (context / 맥락).

## 18. Checklist môi trường vận hành (production / 운영 환경) trước Part 4

Bạn nên có thể giải thích: vì sao venv không phải bộ chứa (container / 컨테이너); `pyproject.toml` giải quyết gì; vì sao thư viện (library / 라이브러리)/ứng dụng (application / 애플리케이션) có pinning chiến lược (strategy / 전략) khác; wheel khác nguồn (source / 소스) bản dựng (build / 빌드) ở ranh giới (boundary / 경계) nào; patch mock ở đâu; làm sao biến clock/random/môi trường (environment / 환경) thành deterministic phụ thuộc (dependency / 의존성); vì sao GC không chữa bộ nhớ đệm (cache / 캐시) leak; vì sao `lru_cache` thread-safe không đồng nghĩa single-flight; bộ nhớ đệm (cache / 캐시) phạm vi (scope / 범위) thay đổi ra sao khi có nhiều worker; tính đồng thời (concurrency / 동시성) khác parallelism thế nào; GIL hiện hành phụ thuộc bản dựng (build / 빌드) ra sao; vì sao `async def` vẫn có thể khối (block / 블록); vì sao cancel tác vụ (task / 작업) chờ `to_thread()` không đồng nghĩa dừng luồng thực thi (thread / 스레드); `gather()` và `TaskGroup` khác thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론) thế nào; `ContextVar` khác toàn cục (global / 전역)/thread-local ở đâu; tiến trình (process / 프로세스) pool tốn serialization gì; `asyncio.Lock` có phạm vi (scope / 범위) nào; và tại sao triển khai (deployment / 배포) tính đúng đắn (correctness / 정확성) không kết thúc ở `docker build`.

Part 4 sẽ đi sâu hơn vào thời gian chạy (runtime / 런타임) internals, bytecode/specialization, descriptors, attribute lookup, đối tượng (object / 객체)/lớp (class / 클래스) creation, GC/hiệu năng (performance / 성능) trade-offs, free-threading, multiple interpreters và cách đọc mã (code / 코드) legacy bằng mô hình tư duy (mental model / 사고 모델) hiện đại.

## Nguồn chính

- `venv`: https://docs.python.org/3.14/thư viện (library / 라이브러리)/venv.html
- Packaging người dùng (user / 사용자) Guide: https://packaging.python.org/
- `pyproject.toml`: https://packaging.python.org/en/latest/guides/writing-pyproject-toml/
- phụ thuộc (dependency / 의존성) Groups: https://packaging.python.org/en/latest/specifications/dependency-groups/
- Wheel specification: https://packaging.python.org/en/latest/specifications/binary-distribution-format/
- `unittest`: https://docs.python.org/3.14/thư viện (library / 라이브러리)/unittest.html
- `pdb`: https://docs.python.org/3.14/thư viện (library / 라이브러리)/pdb.html
- `cProfile`: https://docs.python.org/3.14/thư viện (library / 라이브러리)/profile.html
- `tracemalloc`: https://docs.python.org/3.14/thư viện (library / 라이브러리)/tracemalloc.html
- `functools`: https://docs.python.org/3.14/thư viện (library / 라이브러리)/functools.html
- `contextvars`: https://docs.python.org/3.14/thư viện (library / 라이브러리)/contextvars.html
- `threading`: https://docs.python.org/3.14/thư viện (library / 라이브러리)/threading.html
- `multiprocessing`: https://docs.python.org/3.14/thư viện (library / 라이브러리)/multiprocessing.html
- `concurrent.futures`: https://docs.python.org/3.14/thư viện (library / 라이브러리)/concurrent.futures.html
- `asyncio`: https://docs.python.org/3.14/thư viện (library / 라이브러리)/asyncio.html
- Coroutines and tasks: https://docs.python.org/3.14/thư viện (library / 라이브러리)/asyncio-task.html
- vòng lặp sự kiện (event loop / 이벤트 루프): https://docs.python.org/3.14/thư viện (library / 라이브러리)/asyncio-eventloop.html
- luồng thực thi (thread / 스레드) trạng thái (state / 상태)/GIL: https://docs.python.org/3.14/c-api/threads.html
- Python 3.14 What's New: https://docs.python.org/3.14/whatsnew/3.14.html

> **Bàn giao:** Sau **Nguồn chính**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [COVERAGE AUDIT](./COVERAGE_AUDIT.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
