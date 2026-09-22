# Python Part 3 — Senior: Packaging, testing, concurrency và production engineering

> Baseline: Python 3.14.7. Kiểm chứng: 2026-09-22.

Part này giả định bạn đã hiểu object/reference, data model, iterable/generator, exception và standard-library boundaries. Mục tiêu chuyển từ “viết Python chạy được” sang “xây Python project có thể tái lập, kiểm chứng, chạy đồng thời và vận hành an toàn”.

## 1. Project environment: interpreter và dependency là một phần của chương trình

`môi trường ảo (virtual environment / 가상 환경)`

Python project không chỉ gồm `.py`. Behavior còn phụ thuộc interpreter version, installed distributions, OS/native libraries, environment variables và external services. Nếu hai máy cài dependency khác nhau, cùng source có thể cho behavior khác.

`venv` tạo môi trường có interpreter context và site-packages tách khỏi global environment:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
```

Activation chủ yếu sửa shell `PATH`; nó không tạo container hay security sandbox. Trong automation/CI, có thể gọi trực tiếp `.venv/bin/python` thay vì phụ thuộc activation.

Senior note: đừng `pip install` bừa vào system Python trên server. Cần boundary rõ giữa OS-owned Python và application-owned environment.

## 2. Packaging và distribution model

`gói phân phối (distribution package / 배포 패키지)`

`gói import (import package / 임포트 패키지)`

Tên package import và tên distribution trên PyPI không bắt buộc giống nhau. `pip install some-name` cài distribution metadata/files; `import some_name` thao tác với import system. Đây là nguồn nhầm lẫn phổ biến.

Modern packaging lấy `pyproject.toml` làm configuration hub. Ba vùng quan trọng là `[build-system]`, `[project]` và `[tool.*]`.

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

`[build-system]` nói cần gì để build. `[project]` mô tả project metadata/dependencies. `[tool.*]` dành config của tool. Đừng trộn khái niệm build backend, package installer và dependency resolver thành một từ “pip”.

### Dependency groups

Packaging ecosystem hiện có standardized dependency groups trong `pyproject.toml` cho nhóm development/internal như test/docs mà không cần trở thành project metadata/runtime dependency. Tool support cần được kiểm tra theo tool/version thực tế.

```toml
[dependency-groups]
test = ["pytest>=8", "coverage"]
```

### `requirements.txt` có còn dùng được không?

Có. Nó là format/tooling convention rất phổ biến cho environment installation/pinning. `pyproject.toml` giải quyết project metadata/build và ngày càng nhiều dependency workflows; không nên tuyên bố `requirements.txt` “đã chết”. Chọn model dựa vào application/library, deployment và toolchain.

### Pinning strategy

Library thường không nên pin mọi runtime dependency tới exact patch vì sẽ làm dependency resolution của consumer quá cứng. Application/deployment thường cần lock/reproducibility mạnh hơn. Tách “declared compatibility range” khỏi “resolved deploy environment”.

### Source distribution, wheel và build boundary

Một source distribution (`sdist`) mang source + metadata cần thiết để build; wheel là artifact đã build theo wheel format. Pure-Python wheel thường portable rộng hơn, còn wheel chứa native extension bị ràng buộc bởi Python/ABI/platform tags. Vì vậy “cài cùng version package” vẫn chưa đủ để kết luận hai máy chạy cùng binary path.

Khi installer không tìm được wheel phù hợp, nó có thể phải build từ source tùy project/toolchain. Lúc đó compiler, header, system library và build backend trở thành dependency của installation. Đây là lý do lỗi “máy developer cài được nhưng production không cài được” đôi khi không nằm ở source application mà ở artifact compatibility.

Build backend cũng là code được thực thi trong build environment. `[build-system].requires` vì vậy nằm ở trust/supply-chain boundary, không phải metadata thụ động. CI có yêu cầu security cao nên kiểm soát source, version, cache và build isolation tương ứng.

### Editable install không phải deployment artifact

Editable install hữu ích cho development vì import có thể trỏ trực tiếp tới working tree. Nhưng behavior editable phụ thuộc build backend và development layout; nó không chứng minh wheel/sdist publish ra sẽ đúng. Library/package nên có ít nhất một đường test artifact thật: build wheel/sdist rồi cài vào environment sạch để phát hiện thiếu file, sai package data, entry point hoặc metadata.

## 3. Import architecture và dependency direction

Circular import thường là architecture smell. Layer thấp không nên import ngược layer orchestration chỉ để lấy utility. Một cấu trúc đơn giản:

```text
app/
  domain/
  services/
  adapters/
  cli.py
```

Domain giữ logic và abstraction; adapter biết filesystem/HTTP/database; entry point wire dependencies. Đây không phải framework bắt buộc, mà là dependency direction giúp test/import đơn giản.

Avoid `sys.path.append(...)` trong application như fix packaging. Nó thay import search path runtime và che cấu trúc package sai. Hãy cài project editable khi phát triển hoặc cấu hình package đúng.

## 4. Testing: kiểm chứng contract, không kiểm chứng implementation trivia

`kiểm thử đơn vị (unit test / 단위 테스트)`

`kiểm thử tích hợp (integration test / 통합 테스트)`

Test tốt bảo vệ observable behavior/invariant. Test quá dính internal call count/private method khiến refactor hợp lệ vẫn phá suite.

```python
def normalize_email(raw: str) -> str:
    return raw.strip().lower()


def test_normalize_email():
    assert normalize_email(" A@EXAMPLE.COM ") == "a@example.com"
```

### `pytest`

`pytest` là third-party tool, không thuộc standard library nhưng là de facto phổ biến. Fixture quản lý test dependency/lifecycle:

```python
import pytest

@pytest.fixture
def sample_users():
    return ["a", "b"]


def test_count(sample_users):
    assert len(sample_users) == 2
```

Fixture không nên trở thành hidden service locator khổng lồ. Scope rộng (`session`, `module`) có thể tạo shared state và order dependency nếu lạm dụng.

Repository hiện có [automation/test_pipeline.py](../../automation/test_pipeline.py) dùng standard-library `unittest`. Đây là ví dụ tốt để phân biệt concept testing với một test runner cụ thể: hiểu test isolation/assertion trước, rồi chọn `unittest` hay `pytest` theo project.

### Mocking

Mock boundary gây side effect/nondeterminism như HTTP, clock, random source hoặc external service, chứ không mock mọi function nội bộ. Nếu phải mock 10 collaborator để test một object, architecture có thể quá coupling.

Patch tại nơi name được lookup, không nhất thiết nơi function ban đầu được định nghĩa. Điều này bắt nguồn từ name binding/import model Part 1.

### Property/invariant thinking

Ví dụ parser có invariant “serialize rồi parse phải bảo toàn value hợp lệ”. Property-based testing có thể tìm edge cases tốt hơn vài example test, nhưng tool cụ thể như Hypothesis nằm ngoài core Python.

Một property không nhất thiết là equality tuyệt đối. Parser/normalizer có thể có property “normalize(normalize(x)) == normalize(x)” (idempotence), sorter có property output đã ordered và giữ multiset của input, serializer có property round-trip bảo toàn semantic value. Việc phát biểu invariant trước giúp test không bị khóa vào implementation hiện tại.

### Deterministic test: kiểm soát nguồn không xác định thay vì retry test

Flaky test thường xuất hiện vì test để clock thật, random global, UUID, filesystem temp state, environment variable, network hoặc task scheduling quyết định kết quả. Retry test chỉ giảm xác suất nhìn thấy bug; nó không biến system thành deterministic.

Một design dễ test đưa nondeterminism qua boundary explicit. Với time, truyền clock/callable; với random, truyền `random.Random` hoặc generator thuộc ownership của component; với external I/O, dùng adapter/fake phù hợp contract.

```python
from collections.abc import Callable
from datetime import datetime


def build_record(now: Callable[[], datetime]) -> dict[str, str]:
    return {"created_at": now().isoformat()}
```

Test có thể truyền fixed `now` mà không patch sâu vào standard library. Cùng nguyên tắc áp dụng cho UUID, retry sleep, current user hoặc feature flag.

Không nên hiểu dependency injection là phải dùng framework DI. Chỉ cần code sở hữu source of nondeterminism ở boundary rõ. Khi test buộc thay global environment (`os.environ`, current working directory, locale, timezone), fixture/context manager phải restore state kể cả khi assertion fail; nếu không một test có thể làm test sau sai theo order.

Seed random cũng cần đúng scope. Seed một global generator có thể làm test khác phụ thuộc order; tốt hơn là mỗi test/component sở hữu generator riêng khi random là phần của behavior. Mục tiêu không phải “mọi test không dùng thời gian/random”, mà là cùng input + controlled dependencies phải cho behavior dự đoán được.

## 5. Debugging: quan sát state và execution path

`trình gỡ lỗi (debugger / 디버거)`

Debugging hiệu quả bắt đầu bằng reproducibility: input nào, version nào, branch/commit nào, environment nào, failure boundary nào.

Built-in `breakpoint()` thường vào `pdb` theo default hook:

```python
value = compute()
breakpoint()
consume(value)
```

Debug production không đồng nghĩa attach debugger vào live process. Logging, metrics, traces, core dumps/native tooling và reproducible staging thường an toàn hơn.

Exception traceback là call-path evidence. Đọc từ exception type/message rồi đi lên frames để tìm nơi invariant đầu tiên bị phá, thay vì chỉ patch frame cuối.

## 6. Profiling trước optimization

`lập hồ sơ hiệu năng (profiling / 프로파일링)`

Performance work cần measurement. CPU profiler cho biết thời gian ở đâu; memory profiler/tracemalloc giúp biết allocation ở đâu; benchmark cần warm-up/noise/context phù hợp.

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

Đừng tối ưu một comprehension 2 ms khi network call mất 800 ms. Senior reasoning ưu tiên dominant cost.

### Algorithm trước micro-optimization

Đổi lookup O(n) lặp lại thành index/dict có thể lớn hơn nhiều so với đổi syntax Python. Sau đó mới xem allocation, serialization, batching, native/vectorized operations hoặc concurrency.

## 7. Memory: reference lifetime, GC, cache và object graph

CPython chủ yếu dùng reference counting kết hợp cyclic garbage collector. Khi reference count về zero, object thường được deallocate sớm; cycle cần cyclic GC nếu các object phù hợp. Đây là implementation detail quan trọng nhưng không phải contract chung của mọi Python implementation.

Không dựa vào “CPython sẽ destroy ngay” để quản lý file/socket. Dùng context manager explicit.

Memory leak trong Python thường là reference vẫn còn reachable: cache không giới hạn, global collection, callback registry, task còn sống, closure giữ object graph, hoặc native extension. GC không thể giải phóng object nếu chương trình vẫn tham chiếu nó.

`tracemalloc` có thể snapshot allocation Python:

```python
import tracemalloc
tracemalloc.start()
# workload
snapshot = tracemalloc.take_snapshot()
for stat in snapshot.statistics("lineno")[:10]:
    print(stat)
```

### Cache là retained state có freshness contract

Cache đổi computation/I/O cost lấy memory + stale-data risk + invalidation complexity. Câu hỏi đầu tiên không phải “dùng decorator nào?”, mà là key đại diện identity gì, result hợp lệ bao lâu, ai invalidate, cache sống ở scope nào và memory bound ở đâu.

`functools.cache`/`lru_cache` hữu ích cho pure-ish function với hashable arguments:

```python
from functools import lru_cache

@lru_cache(maxsize=1024)
def parse_schema(version: str):
    ...
```

Cache implementation giữ internal structure coherent khi nhiều thread truy cập, nhưng điều đó **không đồng nghĩa single-flight**. Nếu hai thread cùng miss trước khi result đầu tiên được cache, wrapped function có thể chạy hơn một lần. Nếu function có side effect hoặc “chỉ được chạy một lần”, `lru_cache` không phải synchronization primitive.

Cache key cũng giữ references tới arguments/result cho tới eviction/clear. Method cache có thể giữ `self` thông qua key, khiến instance sống lâu hơn dự kiến. Unbounded `@cache` với key cardinality tăng theo request/user có thể trở thành memory leak về mặt vận hành dù GC hoạt động hoàn toàn đúng.

Process model lại tạo boundary khác: cache in-memory của mỗi worker không tự chia sẻ với worker/replica khác. Invalidation local không đảm bảo freshness toàn deployment. Vì vậy cache correctness phải được reasoning cùng process/replica topology, không chỉ cùng function body.

## 8. Concurrency, parallelism và asynchrony là ba khái niệm khác nhau

`đồng thời (concurrency / 동시성)`

`song song (parallelism / 병렬성)`

`bất đồng bộ (asynchrony / 비동기)`

Concurrency là nhiều task có progress chồng lấn. Parallelism là thực sự chạy computation cùng lúc trên nhiều execution resource. Async là programming model nơi task có thể suspend tại awaitable/event boundary thay vì block execution context.

Vì vậy `async def` không đồng nghĩa multi-core và cũng không làm CPU-bound loop nhanh hơn.

## 9. Threading và shared memory

Thread trong cùng process chia sẻ memory. Đây vừa là lợi thế vừa là nguồn race condition.

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

Không suy luận “có GIL nên code thread-safe”. Một logical operation có thể gồm nhiều bytecode/steps; library có thể release GIL; free-threaded build thay assumption; shared mutable invariant vẫn cần synchronization hoặc architecture tránh shared state.

### GIL trong Python 3.14

`khóa thông dịch toàn cục (Global Interpreter Lock, GIL / 전역 인터프리터 잠금)`

Với CPython build mặc định có GIL, một thread phải giữ GIL để thao tác Python objects/execute Python bytecode. Blocking I/O và một số native operations có thể release GIL, nên threading vẫn rất hữu ích cho I/O-bound workloads.

Python 3.13 đưa free-threaded build vào experimental; Python 3.14 nâng nó thành officially supported nhưng vẫn optional. Free-threaded build có thể disable GIL và cho threads thực thi Python code song song, nhưng extension compatibility, synchronization và performance profile phải được đánh giá. Không viết documentation kiểu “Python không thể chạy threads song song” nữa, cũng không viết kiểu “Python 3.14 đã bỏ GIL”. Cả hai đều sai khi thiếu build/runtime context.

### Thread pool

`concurrent.futures.ThreadPoolExecutor` phù hợp khi muốn bounded worker pool cho blocking I/O hoặc function sync. Bounded concurrency quan trọng: 10,000 tasks không có nghĩa 10,000 threads.

### Lock bảo vệ invariant, không bảo vệ “một dòng code”

Lock có ý nghĩa khi gắn với một invariant của shared state. Ví dụ nếu `available_balance` và `reserved_balance` phải thay đổi atomically theo một transfer, chỉ lock một phép cộng nhưng để phép trừ ở ngoài vẫn có thể phá invariant. Scope lock phải bao quanh state transition cần nhìn như một operation không thể xen kẽ.

Nhiều lock tạo deadlock risk. Nếu thread A giữ lock X rồi chờ Y, còn thread B giữ Y rồi chờ X, cả hai có thể chờ vô hạn. Hai chiến lược nền là giảm shared mutable state và giữ lock ordering nhất quán. Timeout trên lock có thể giúp hệ thống thoát một số tình huống nhưng không sửa thiết kế cycle ownership.

`RLock` cho phép cùng thread acquire lại lock; `Semaphore` giới hạn số worker đồng thời; `Event` truyền signal trạng thái; `Condition` phối hợp chờ một predicate trên shared state. Chọn primitive từ invariant, không từ tên nghe phù hợp.

## 10. Multiprocessing: process isolation đổi lấy communication cost

Process có address space riêng, giúp CPU-bound Python workload dùng nhiều core trên GIL-enabled CPython. Đổi lại startup, serialization/IPC, memory và operational complexity lớn hơn.

```python
from concurrent.futures import ProcessPoolExecutor

def cpu_work(n: int) -> int:
    return sum(i * i for i in range(n))

if __name__ == "__main__":
    with ProcessPoolExecutor() as pool:
        results = list(pool.map(cpu_work, [1_000_000] * 4))
```

Guard `__main__` đặc biệt quan trọng với multiprocessing start methods/platform nơi child import main module. Data chuyển giữa processes thường phải serialize, nên đừng gửi object graph khổng lồ nếu cost IPC vượt lợi ích parallelism.

Python 3.14 có thay đổi start-method/platform details theo OS; production code không nên dựa vào assumption “fork luôn là default ở mọi Unix”. Trên POSIX hỗ trợ phù hợp, `forkserver` là default từ 3.14; code cần semantics của `fork` phải chọn explicit context. macOS và Windows có behavior platform-specific khác. Start method là deployment/runtime choice, không phải chi tiết vô hại.

## 11. `asyncio`: cooperative concurrency qua event loop

`vòng lặp sự kiện (event loop / 이벤트 루프)`

`coroutine (coroutine / 코루틴)`

Event loop schedule tasks/callbacks và phối hợp non-blocking I/O. Coroutine chạy cho đến khi gặp điểm suspend (`await`) mà awaited operation chưa hoàn tất, rồi loop có thể chạy task khác.

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

### Blocking call bên trong async

Nếu gọi `time.sleep(10)` hoặc sync HTTP/filesystem operation nặng trực tiếp trong coroutine, event-loop thread bị block và các task khác không được schedule. Có thể offload blocking function qua `asyncio.to_thread()` khi phù hợp:

```python
result = await asyncio.to_thread(blocking_function, arg)
```

Repository đã dùng pattern này trong [automation/app.py](../../automation/app.py): FastAPI endpoint giữ `asyncio.Lock`, rồi `await asyncio.to_thread(Pipeline().run)` để synchronous pipeline không block event loop trực tiếp. Đây là bridge tốt giữa core mechanism và framework code; semantics HTTP/FastAPI nằm ngoài core library.

Có một giới hạn quan trọng: cancellation của coroutine đang chờ `to_thread()` không phải là cơ chế cưỡng chế dừng OS thread. Nếu function sync đã bắt đầu chạy, nó có thể tiếp tục side effect sau khi request/task async phía ngoài đã timeout hoặc bị cancel. Vì vậy long-running sync work cần cancellation/cooperation riêng nếu business invariant yêu cầu dừng thật: ví dụ cancellation token/event mà function tự kiểm tra, subprocess có lifecycle riêng, hoặc chuyển work sang job/process boundary có thể terminate theo policy.

### Async không bằng parallelism

Hai coroutine cùng event loop không chạy Python CPU loop đồng thời chỉ vì dùng `gather`. Nếu coroutine không `await` trong thời gian dài, nó chiếm event loop. CPU-heavy work cần process pool/native code/free-threaded strategy hoặc architecture khác.

### `gather()` và `TaskGroup` có failure semantics khác nhau

`asyncio.gather()` rất tiện khi muốn thu kết quả theo thứ tự input. Nhưng với mặc định `return_exceptions=False`, exception đầu tiên được propagate cho caller trong khi các awaitable khác không tự động bị cancel chỉ vì sibling fail. Điều này có thể đúng cho independent work, nhưng sai nếu các task tạo thành một operation chung phải “fail together”.

`TaskGroup` biểu diễn ownership có cấu trúc hơn. Khi một child fail bằng exception thông thường, group cancel các sibling còn lại và gom failure khi rời context. Vì vậy lựa chọn không phải “API nào mới hơn”, mà là failure invariant: các tác vụ độc lập hay là children của cùng một operation?

### Cancellation là control flow

Task cancellation không phải “kill thread”. `CancelledError` được inject tại suspension point và cleanup cần `try/finally`/context manager. `CancelledError` kế thừa trực tiếp `BaseException`, nên `except Exception` thông thường không bắt nó. Nếu bắt cancellation để cleanup, đa số code nên raise lại; nuốt cancellation có thể phá semantics của `TaskGroup` và `asyncio.timeout()`.

### Timeouts và structured concurrency

Modern asyncio có `asyncio.timeout()` và `TaskGroup` cho lifecycle có cấu trúc. `TaskGroup` giúp parent scope sở hữu child tasks và propagate failure/cancellation dễ reason hơn so với fire-and-forget task không được giữ reference.

```python
async with asyncio.TaskGroup() as tg:
    tg.create_task(worker(1))
    tg.create_task(worker(2))
```

Fire-and-forget cần explicit ownership, logging và shutdown policy; nếu không task có thể fail không ai observe.

### Event loop APIs modern vs legacy

Application code ưu tiên `asyncio.run()` hoặc `asyncio.Runner`. Policy APIs như `get_event_loop_policy()`/`set_event_loop_policy()` deprecated ở Python 3.14 và dự kiến removed ở 3.16. `get_event_loop()` trong 3.14 cũng không còn ngầm tạo loop nếu không có current event loop; trong coroutine/callback, `get_running_loop()` rõ hơn cho low-level code.

### Context-local state: `contextvars` không phải global mutable state

Request ID, trace ID hoặc transaction context thường cần “có sẵn” ở nhiều function nhưng không được rò sang request/task khác. Global variable sai vì mọi concurrent work nhìn cùng binding; `threading.local()` lại gắn state với OS thread và không mô hình đúng khi nhiều asyncio task xen kẽ trên cùng thread.

`contextvars.ContextVar` gắn value với execution context hiện tại. `asyncio` hỗ trợ context variables native, nên child task thường nhận context phù hợp mà không cần truyền một global mutable dict quanh application.

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

Reset bằng token làm ownership/lifetime explicit; không để context cũ bleed sang work sau. Context variable nên được khai báo ở module level thay vì tạo động trong closure nếu không có lý do đặc biệt, vì `Context` giữ strong reference tới `ContextVar`.

Một detail production quan trọng: `asyncio.to_thread()` propagate current `contextvars.Context` sang worker thread. Điều này giúp logging/tracing context tiếp tục nhìn thấy request ID trong sync adapter được offload. Nhưng propagation này không biến mutable object nằm trong context thành immutable/thread-safe; nếu context value là một dict mutable được share, vẫn phải reasoning về aliasing/concurrency.

Qua process hoặc subinterpreter boundary, đừng giả định context tự đi theo. Correlation/tenant/auth context cần trở thành explicit message/task metadata. Đây là cùng nguyên tắc với trace propagation trong distributed system: execution-local convenience không thay contract qua isolation boundary.

## 12. Networking cơ bản

Network I/O có partial reads/writes, timeout, DNS, connection failure, remote close và backpressure. High-level HTTP client che nhiều chi tiết nhưng không xóa failure modes.

Built-in `socket` ở mức thấp. `asyncio` streams cung cấp abstraction async cao hơn. Với application business, thường dùng maintained protocol library thay vì tự implement HTTP/TLS.

Timeout không phải một số duy nhất nếu hệ thống cần reliability: connect timeout, read timeout, total deadline và retry budget có semantics khác nhau.

### Retry

Retry chỉ an toàn khi operation có semantics phù hợp/idempotency hoặc có deduplication key. Retry POST payment một cách mù quáng có thể tạo duplicate side effect. Exponential backoff + jitter giảm synchronized retry storm, nhưng vẫn cần overall deadline.

Retry budget phải thuộc cùng latency/deadline model. Ba attempt mỗi attempt timeout 10 giây có thể tạo request 30+ giây nếu caller chỉ cho 5 giây. Production code nên propagate remaining deadline hoặc có policy tổng thay vì để từng layer tự retry độc lập.

## 13. Security trong Python application

Security không phải module riêng; nó cắt ngang input, serialization, subprocess, dependency, logging và deployment.

### Untrusted input

Validate structure/range tại boundary. Không dùng `eval()` với input không tin cậy. `ast.literal_eval()` chỉ parse subset literal nhưng vẫn không phải universal parser cho arbitrary large/malicious resource consumption.

### `pickle`

Không unpickle dữ liệu không tin cậy. Format này có thể kích hoạt object reconstruction behavior nguy hiểm.

### Shell injection

Ưu tiên `subprocess.run([program, arg1, ...], shell=False)`. Nếu `shell=True` là bắt buộc, user input cần strategy escaping/allowlist đúng shell/platform; tốt nhất tránh boundary này.

### Path traversal

Khi user control filename/path, việc ghép vào root cần canonicalization và authorization boundary. `Path.resolve()` hỗ trợ resolution nhưng security rule vẫn phải kiểm tra resulting path thuộc allowed root và symlink semantics phù hợp.

### Secrets

Secrets không hard-code/commit. Lấy từ secret manager/environment/file permission boundary tùy deployment. Đừng log secret khi exception hoặc dump config.

### Dependency supply chain

Pin/lock deploy environment, review package provenance, update security fixes và hạn chế package không cần thiết. Package name typo có thể trở thành typosquatting risk. Build dependencies cũng thuộc supply chain vì build backend được thực thi trong quá trình tạo artifact.

## 14. Performance model thực tế

Python performance thường bị chi phối bởi một trong các lớp: algorithm/data structure, Python interpreter overhead, allocation/object count, I/O latency, serialization, database/network round trip, native library hoặc concurrency architecture.

Một số strategies:

- Batch external operations để giảm round trips khi semantics cho phép.
- Dùng built-in/native implementation cho loop nặng khi có API phù hợp.
- Tránh tạo intermediate collections nếu streaming đủ.
- Cache chỉ khi có invalidation/memory bound rõ.
- Profile trước và sau thay đổi.

Không dùng `asyncio` như performance magic. Async tăng throughput/concurrency cho workload chờ I/O tốt; nó có overhead và complexity riêng.

Performance optimization bằng cache phải đo cả hit rate, retained memory và freshness cost. Một cache có hit rate 99% nhưng giữ dữ liệu stale sai business invariant không phải optimization thành công.

## 15. Production deployment model

Production Python cần xác định rõ entry point, process model, config, graceful shutdown, health/readiness, logs/metrics, resource limits và deployment artifact.

Một service containerized không vì dùng Docker mà tự động production-ready. Container process vẫn có thể leak memory, ignore SIGTERM, không có timeout hoặc ghi state vào ephemeral filesystem.

### Process model

Nhiều web servers chạy nhiều worker processes. Nếu mỗi process có global cache/lock, state đó không chia sẻ giữa processes. `asyncio.Lock` chỉ synchronize tasks trong event loop/process tương ứng; nó không phải distributed lock.

Điều này trực tiếp liên quan [automation/app.py](../../automation/app.py): module-level `asyncio.Lock()` ngăn concurrent run trong một app process. Nếu deploy nhiều worker/process/replica, cần external coordination nếu invariant là “toàn hệ thống chỉ một pipeline chạy”. Đây là senior-level distinction giữa in-process concurrency control và distributed coordination.

Cache cũng theo scope tương tự: `lru_cache` hoặc dict global trong một worker không phải cache toàn deployment. Nếu business correctness phụ thuộc invalidate đồng thời ở mọi replica, in-process cache chỉ là một optimization layer và phải có freshness strategy rõ.

### Graceful shutdown

Shutdown cần ngừng nhận work mới, cho work đang chạy kết thúc hoặc cancel theo deadline, flush cần thiết và release resource. `finally`, context manager và task ownership từ các phần trước chính là nền tảng.

Nếu application đã offload work sang thread mà function không hỗ trợ cooperative cancellation, shutdown deadline có thể hết trong khi thread vẫn chạy. Đây là lý do lifecycle của background work phải được thiết kế từ lúc chọn execution model, không vá ở signal handler cuối cùng.

### Configuration

Environment variable là một transport phổ biến, không phải schema. Parse/validate config lúc startup và fail fast với message rõ. Boolean string như `"false"` là truthy nếu dùng trực tiếp; cần explicit parsing.

## 16. Case study: review `automation/pipeline.py` bằng senior lens

[automation/pipeline.py](../../automation/pipeline.py) có các lựa chọn đáng học:

Nó dùng argument list với `subprocess.run`, giữ token khỏi command arguments và `.git/config`, đặt timeout cho clone, check return code, dùng `Path`, guard cost/API calls và raise khi external response không đạt invariant. Đây là examples nơi Python core mechanism phục vụ production safety.

Nhưng senior review cũng hỏi thêm: HTTP retry/deadline policy thế nào; `timeout=1800` có phù hợp per-request/overall budget không; output có size limit không; process cancellation có propagate vào sync pipeline đang chạy trong thread không; một lock local có đủ khi scale workers không; config parsing có schema/test không; token có thể lộ qua error/log không; clock/random/environment có được isolate để test deterministic không; nếu thêm cache thì cache key/invalidation/process scope sẽ là gì. Những câu hỏi này không phải chê code, mà là cách reasoning khi boundary production mở rộng.

## 17. Khi chọn concurrency model

Một decision matrix tối giản:

| Workload | Mô hình bắt đầu xem xét | Lý do chính |
|---|---|---|
| Nhiều blocking I/O sync library | threads / `to_thread` | overlap thời gian chờ, tích hợp sync code |
| Nhiều async sockets/HTTP | `asyncio` | high concurrency với task nhẹ |
| CPU-bound pure Python trên GIL-enabled build | multiprocessing/process pool | multi-core qua process isolation |
| CPU-bound native code release GIL | threads có thể phù hợp | native work chạy ngoài GIL |
| CPython free-threaded 3.14+ | threads có thể parallel | cần verify build, extension safety, synchronization |
| Isolation trong cùng process, task phù hợp subinterpreter | `InterpreterPoolExecutor` / multiple interpreters | multi-core + interpreter isolation, đổi lại explicit data transfer/compatibility |
| Isolation/reliability mạnh | processes/services | failure/state boundary rõ hơn |

Đây không phải ranking tuyệt đối. Data size, IPC, latency, library compatibility và operational model có thể đổi quyết định. Multiple interpreters được đào sâu ở Part 4; chúng không phải “process nhẹ” hay “thread có GIL khác” theo nghĩa có thể thay thế mù quáng.

Context propagation cũng phải nằm trong decision. Thread/task/process/interpreter có isolation semantics khác nhau; request metadata tiện lợi trong `ContextVar` không nên được xem như distributed message context.

## 18. Checklist production trước Part 4

Bạn nên có thể giải thích: vì sao venv không phải container; `pyproject.toml` giải quyết gì; vì sao library/application có pinning strategy khác; wheel khác source build ở boundary nào; patch mock ở đâu; làm sao biến clock/random/environment thành deterministic dependency; vì sao GC không chữa cache leak; vì sao `lru_cache` thread-safe không đồng nghĩa single-flight; cache scope thay đổi ra sao khi có nhiều worker; concurrency khác parallelism thế nào; GIL hiện hành phụ thuộc build ra sao; vì sao `async def` vẫn có thể block; vì sao cancel task chờ `to_thread()` không đồng nghĩa dừng thread; `gather()` và `TaskGroup` khác failure semantics thế nào; `ContextVar` khác global/thread-local ở đâu; process pool tốn serialization gì; `asyncio.Lock` có scope nào; và tại sao deployment correctness không kết thúc ở `docker build`.

Part 4 sẽ đi sâu hơn vào runtime internals, bytecode/specialization, descriptors, attribute lookup, object/class creation, GC/performance trade-offs, free-threading, multiple interpreters và cách đọc code legacy bằng mental model hiện đại.

## Nguồn chính

- `venv`: https://docs.python.org/3.14/library/venv.html
- Packaging User Guide: https://packaging.python.org/
- `pyproject.toml`: https://packaging.python.org/en/latest/guides/writing-pyproject-toml/
- Dependency Groups: https://packaging.python.org/en/latest/specifications/dependency-groups/
- Wheel specification: https://packaging.python.org/en/latest/specifications/binary-distribution-format/
- `unittest`: https://docs.python.org/3.14/library/unittest.html
- `pdb`: https://docs.python.org/3.14/library/pdb.html
- `cProfile`: https://docs.python.org/3.14/library/profile.html
- `tracemalloc`: https://docs.python.org/3.14/library/tracemalloc.html
- `functools`: https://docs.python.org/3.14/library/functools.html
- `contextvars`: https://docs.python.org/3.14/library/contextvars.html
- `threading`: https://docs.python.org/3.14/library/threading.html
- `multiprocessing`: https://docs.python.org/3.14/library/multiprocessing.html
- `concurrent.futures`: https://docs.python.org/3.14/library/concurrent.futures.html
- `asyncio`: https://docs.python.org/3.14/library/asyncio.html
- Coroutines and tasks: https://docs.python.org/3.14/library/asyncio-task.html
- Event loop: https://docs.python.org/3.14/library/asyncio-eventloop.html
- Thread state/GIL: https://docs.python.org/3.14/c-api/threads.html
- Python 3.14 What's New: https://docs.python.org/3.14/whatsnew/3.14.html