# Python Engineering Case Studies

> Baseline: Python 3.14.7. Kiểm chứng: 2026-09-22.

Tài liệu này không tạo thêm một level học mới và cũng không lặp lại bốn canonical part. Mục tiêu là buộc các concept đã học phải hoạt động cùng nhau trong một tình huống gần production. Mỗi case bắt đầu từ một hiện tượng quan sát được, xác định invariant cần giữ, lần theo mechanism tạo ra behavior, rồi mới chọn thiết kế hoặc công cụ. Cách đọc này quan trọng vì bug thực tế hiếm khi tự giới thiệu mình bằng tên chapter như “đây là lỗi iterator” hay “đây là lỗi event loop”.

Nếu một thuật ngữ cơ sở chưa chắc, quay lại [Part 1](python_01_beginner.md) và [Part 2](python_02_intermediate.md). Nếu vấn đề liên quan project, concurrency hoặc vận hành, đọc song song [Part 3](python_03_senior.md). Khi cần đi xuống runtime, GIL, GC hoặc execution internals, dùng [Part 4](python_04_master.md). Các khái niệm process, scheduling, network và distributed coordination rộng hơn được nối sang [Computer Science Knowledge Library](../../computer_science/README.md).

---

## Case 1 — “Tôi chỉ gán sang biến khác, tại sao dữ liệu cũ cũng đổi?”

Giả sử một service nhận cấu hình mặc định rồi thêm option theo request:

```python
DEFAULT_OPTIONS = {
    "headers": {"accept": "application/json"},
    "retries": 2,
}


def build_options(user_options: dict) -> dict:
    options = DEFAULT_OPTIONS.copy()
    options["headers"].update(user_options.get("headers", {}))
    return options
```

Nhìn bề mặt, `copy()` dường như đã tạo cấu hình mới. Nhưng đây là bản sao nông (shallow copy / 얕은 복사). `options` là `dict` mới, còn value tại key `"headers"` vẫn là cùng một nested `dict` với `DEFAULT_OPTIONS`. Khi `update()` mutate nested object, default toàn cục cũng thay đổi.

Invariant thực sự cần giữ là: một request không được làm biến đổi cấu hình mặc định dùng cho request khác. Vì vậy câu hỏi đúng không phải “nên dùng `copy()` hay `deepcopy()`?”, mà là “object nào thuộc ownership của ai và boundary nào phải tạo snapshot?”. Một cách rõ hơn là tạo object mới tại đúng nested boundary:

```python
def build_options(user_options: dict) -> dict:
    headers = {
        **DEFAULT_OPTIONS["headers"],
        **user_options.get("headers", {}),
    }
    return {
        "headers": headers,
        "retries": user_options.get("retries", DEFAULT_OPTIONS["retries"]),
    }
```

`deepcopy()` có thể chữa ví dụ nhỏ, nhưng không phải lời giải tổng quát. Object graph thực tế có thể chứa lock, socket, file handle, cache hoặc object có identity semantics. Thiết kế bền hơn là làm ownership explicit và ưu tiên immutable value tại boundary nơi mutation không có ý nghĩa.

Evidence khi debug case này là kiểm tra identity của nested object, không chỉ in value:

```python
options = DEFAULT_OPTIONS.copy()
assert options is not DEFAULT_OPTIONS
assert options["headers"] is DEFAULT_OPTIONS["headers"]
```

Mental model cần mang sang production là `name → object → nested object graph`. Gán tên, copy container và mutate state là ba thao tác khác nhau.

---

## Case 2 — Import làm service khởi động chậm hoặc thất bại trước khi nhận request

Một module thường được viết kiểu:

```python
# config.py
CONFIG = load_remote_config()
MODEL = build_large_model(CONFIG)
```

Sau đó nhiều module chỉ cần `from config import MODEL`. Vấn đề là import lần đầu thực thi top-level code. Network chậm, credential chưa có, remote service down hoặc model build nặng đều biến import thành startup side effect. Test chỉ import một helper cũng có thể vô tình gọi network.

Invariant cần giữ là: import phải đủ deterministic để module có thể được load cho test, tooling và application startup mà không phụ thuộc side effect không cần thiết. Điều này không đồng nghĩa “top-level code luôn xấu”; constant đơn giản và definition là bình thường. Boundary nguy hiểm là I/O, process creation, database connection hoặc initialization có failure mode lớn.

Thiết kế rõ hơn là đưa side effect vào composition root:

```python
# config.py
from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
    endpoint: str
    token: str


def load_settings() -> Settings:
    ...
```

```python
# app.py

def main() -> None:
    settings = load_settings()
    model = build_model(settings)
    run_server(model)
```

Circular import là phiên bản kiến trúc của cùng vấn đề. Nếu `domain.py` import `service.py` để lấy helper, còn `service.py` import `domain.py` để lấy model, runtime có thể quan sát module đang partially initialized. Di chuyển import vào function đôi khi tránh lỗi tức thời nhưng không sửa dependency direction. Cách chữa bền hơn thường là tách abstraction chung xuống layer thấp hơn hoặc đưa orchestration lên layer cao hơn.

Khi startup chậm, đo import graph thay vì đoán. Khi import fail, nhìn module nào đang partially initialized và dependency nào chạy ngược chiều kiến trúc.

---

## Case 3 — “Máy tôi chạy được” nhưng CI hoặc production cài dependency khác

Một project Python không chỉ là source code. Behavior còn phụ thuộc interpreter, distribution packages, native libraries, platform tag và cách environment được resolve. `pyproject.toml` giải quyết metadata/build/tool configuration, nhưng không tự động đảm bảo mọi deployment resolve đúng cùng dependency set.

Hãy tách ba câu hỏi. Project tuyên bố tương thích với dependency nào? Build system dùng backend nào để tạo artifact? Deployment cụ thể đã resolve chính xác version nào?

Ví dụ:

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

[dependency-groups]
test = ["pytest>=8", "coverage"]
```

`[project].dependencies` là contract runtime của distribution. `dependency-groups` phù hợp cho nhóm development/internal và không trở thành dependency metadata của package build. Exact resolved environment cho production lại là một concern khác, thường cần lock hoặc artifact reproducible theo toolchain của project.

Wheel làm bài toán thú vị hơn. Pure-Python wheel có portability cao hơn. Wheel chứa native extension phụ thuộc Python/ABI/platform compatibility tags. Vì vậy “package tồn tại trên PyPI” không bảo đảm có binary artifact phù hợp với interpreter và architecture đang deploy. Nếu installer phải build từ source, server lại cần compiler/header/native dependency phù hợp.

Khi incident xảy ra chỉ trên một environment, evidence cần thu không chỉ là `pip freeze`. Ghi cả `python -VV`, platform/architecture, lock state, artifact hash, wheel tag hoặc native dependency liên quan. Reproducibility là thuộc tính của toàn chuỗi build → resolve → install → run.

---

## Case 4 — Async endpoint nhưng service vẫn “đơ”

Repository hiện có [automation/app.py](../../automation/app.py) dùng FastAPI endpoint `async def`, `asyncio.Lock` và `asyncio.to_thread(Pipeline().run)`. Đây là case study tốt vì nó thể hiện một boundary rất phổ biến: application async phải gọi pipeline sync.

Nếu coroutine gọi trực tiếp một function sync chạy lâu:

```python
@app.post("/run")
async def run():
    return Pipeline().run()
```

thì event-loop thread bị giữ cho đến khi call trả về. Trong thời gian đó, coroutine khác trên cùng loop không được schedule bình thường. `async def` không biến code con thành non-blocking.

`asyncio.to_thread()` offload synchronous function sang worker thread, giúp event loop tiếp tục phục vụ I/O khác:

```python
result = await asyncio.to_thread(Pipeline().run)
```

Nhưng đây chưa phải lời giải cho mọi thứ. Nếu pipeline là CPU-bound pure Python trên build có GIL, thread không tự tạo multi-core speedup. Nếu pipeline giữ resource không thread-safe, offload lại mở thêm concurrency concern. Nếu request bị cancel, cancellation của coroutine cũng không đồng nghĩa Python có thể cưỡng chế dừng synchronous function đang chạy trong thread.

`asyncio.Lock` trong `automation/app.py` bảo vệ invariant “một process không chạy hai pipeline qua endpoint cùng lúc”. Nó không bảo vệ invariant “toàn deployment chỉ có một pipeline”, vì nhiều worker process hoặc replica có lock riêng. Khi scale, invariant toàn hệ thống cần external coordination, idempotency hoặc job system thích hợp.

Đây là ví dụ điển hình cho cách reasoning theo scope: task scope → event loop → thread → process → replica → distributed system. Một primitive đúng ở tầng thấp không tự mở rộng semantics lên tầng cao hơn.

---

## Case 5 — Throughput tăng rồi memory tăng không giới hạn

Một async producer đọc message nhanh hơn consumer ghi database:

```python
queue = asyncio.Queue()

async def producer():
    while True:
        item = await receive()
        await queue.put(item)
```

Code functional có thể đúng trong test nhỏ nhưng queue không giới hạn biến chênh lệch throughput thành memory growth. Vấn đề không nằm ở garbage collector: item vẫn reachable vì queue đang giữ reference.

Invariant vận hành là hệ thống phải có giới hạn work-in-flight tương ứng với capacity downstream. Bounded queue tạo backpressure (áp lực ngược / backpressure / 백프레셔):

```python
queue = asyncio.Queue(maxsize=100)
```

Khi queue đầy, `await queue.put(item)` suspend producer. Việc này chuyển overload từ “ăn RAM đến chết” thành một state có thể quan sát và điều khiển. Nhưng size 100 không phải con số ma thuật; nó liên hệ với latency, throughput, memory per item và burst tolerance.

Production evidence cần nhìn cùng lúc queue depth, enqueue/dequeue rate, processing latency, error/retry rate và memory. Nếu retry tự tạo thêm item, retry policy có thể trở thành load amplifier. Nếu consumer gọi external service không có deadline, vài request treo có thể chiếm hết worker và làm queue đầy dù CPU còn rảnh.

Backpressure vì vậy không phải API của `asyncio`; nó là invariant của pipeline dữ liệu.

---

## Case 6 — Chọn thread, process, async hay free-threaded build

Một lỗi thiết kế phổ biến là chọn concurrency model dựa trên slogan: “Python có GIL nên dùng process”, hoặc “async nhanh hơn thread”. Cách đúng là bắt đầu từ dominant work.

Nếu phần lớn thời gian chờ socket hoặc blocking I/O sync, thread pool có thể overlap thời gian chờ với ít thay đổi code. Nếu dependency graph đã async-native và cần rất nhiều concurrent connections, `asyncio` có thể giảm cost per task và cho lifecycle rõ qua `TaskGroup`. Nếu workload CPU-bound pure Python trên CPython có GIL, process pool thường là baseline để sử dụng nhiều core, nhưng phải trả startup/IPC/serialization cost. Nếu heavy computation nằm trong native library có release GIL, thread lại có thể scale CPU tốt.

Python 3.14 thêm một nhánh lựa chọn quan trọng: free-threaded CPython được hỗ trợ chính thức nhưng vẫn optional. Nó cho phép nhiều thread chạy Python code song song, nhưng không biến shared mutable state thành an toàn. Dependency native phải tương thích, và performance profile single-thread/multi-thread cần đo trên build thật.

Decision thực tế nên dựa trên measurement:

```text
workload dominant ở đâu?
    ↓
I/O wait / Python CPU / native CPU / IPC?
    ↓
state có share không?
    ↓
latency, throughput, isolation và deployment constraint là gì?
    ↓
chọn model nhỏ nhất đáp ứng invariant
```

Nếu phải truyền hàng GB giữa processes mỗi job, process pool có thể chậm hơn single process. Nếu free-threaded giúp CPU nhưng extension quan trọng bật lại GIL hoặc chưa compatible, benefit biến mất. Nếu async code gọi sync library nặng, event loop vẫn bị block nếu không có adapter boundary.

---

## Case 7 — Migration sang free-threaded Python không phải chỉ đổi interpreter

Giả sử service hiện chạy ổn với CPython có GIL và muốn thử free-threaded 3.14. Sai lầm nguy hiểm là suy luận rằng code đã chạy nhiều thread lâu nay nên mặc nhiên thread-safe.

GIL trước đây serialize nhiều execution ở interpreter level, nhưng business invariant có thể vẫn racy. Một cache kiểu check-then-set là ví dụ:

```python
if key not in cache:
    cache[key] = compute(key)
return cache[key]
```

Hai thread có thể cùng thấy key chưa tồn tại rồi cùng compute. Ngay cả khi final dict không corrupt, side effect của `compute()` có thể chạy hai lần. Correctness phải dựa trên invariant và synchronization thích hợp, không dựa trên observation rằng một built-in operation “có vẻ atomic”.

Migration audit cần nhìn shared mutable objects, singleton/global registries, lazy initialization, caches, random/process-wide state, environment mutation, signal handling, C extensions và test assumptions. Sau đó chạy stress/race-oriented test trên chính free-threaded build. Một test pass một lần gần như không chứng minh absence of race vì scheduling space rất lớn.

Điểm quan trọng của Python 3.14 là free-threading đã trở thành supported option, nhưng library documentation vẫn phải nói rõ build/runtime context. Code portable không nên dựa vào việc GIL luôn tồn tại, cũng không nên giả định GIL luôn bị tắt.

---

## Case 8 — Test pass nhưng hệ thống vẫn sai vì test không kiểm invariant

Giả sử function retry payment API. Unit test chỉ mock client và assert `client.post` được gọi ba lần khi timeout. Test đó kiểm implementation detail, nhưng chưa kiểm invariant quan trọng hơn: operation có bị duplicate side effect không?

Test design nên xuất phát từ contract. Nếu operation phải idempotent, test cần model cùng idempotency key qua retry và verify server/fake adapter không tạo hai payment. Nếu parser có property serialize → parse bảo toàn semantic value, example-based test vài input đẹp là chưa đủ; property-based hoặc fuzz testing có thể khám phá empty input, Unicode, nesting, size extreme và malformed boundary tốt hơn.

Nondeterminism cũng cần ownership. Clock, random, network và process environment nên đi qua boundary có thể thay thế trong test. Thay vì patch mọi private function, inject clock hoặc adapter nơi side effect xuất hiện:

```python
from collections.abc import Callable
from datetime import datetime


def make_record(now: Callable[[], datetime]) -> dict:
    return {"created_at": now().isoformat()}
```

Test tốt làm rõ invariant và failure semantics. Mock chỉ là một kỹ thuật để cô lập boundary; số lượng mock không phải thước đo chất lượng test.

---

## Case 9 — Dynamic feature biến thành security boundary

Python cho phép `eval`, `exec`, dynamic import, pickle, template engine, regex và subprocess. Điểm chung không phải chúng “nguy hiểm”, mà là chúng diễn giải input theo một grammar hoặc execution model mạnh hơn string thông thường.

Ví dụ, chạy command bằng shell:

```python
subprocess.run(f"git show {user_input}", shell=True)
```

biến `user_input` thành một phần shell grammar. Escape sai một ký tự có thể đổi nghĩa command. Nếu không cần shell feature, argument vector giữ data và syntax tách nhau:

```python
subprocess.run(["git", "show", user_input], check=True)
```

Tương tự, structured JSON nên parse bằng JSON parser chứ không regex; SQL nên parameterize bằng database API; HTML cần context-aware escaping; untrusted object data không được `pickle.loads()` chỉ vì file extension quen thuộc.

Không tồn tại một hàm `sanitize()` chung cho mọi boundary. Security reasoning phải hỏi: input đang đi vào grammar nào, parser/executor nào, quyền của process là gì, resource exhaustion có thể xảy ra không, và output/error có làm lộ secret không?

Repository [automation/pipeline.py](../../automation/pipeline.py) dùng argument list với `subprocess.run`, đây là pattern đáng giữ khi command không cần shell expansion.

---

## Case 10 — Incident production: CPU bình thường nhưng request latency tăng mạnh

Khi latency tăng, chỉ log exception thường không đủ vì request có thể chậm nhưng không fail. Observability cần phân biệt log, metric và trace.

Giả sử service gọi ba external dependencies. Metric cho biết p95 latency tăng từ 200 ms lên 3 s. Trace cho biết 2.7 s nằm ở một HTTP call. Log của call đó cho biết retry hai lần sau read timeout. Đây là causal chain mà một công cụ đơn lẻ khó cung cấp.

Instrument nên đặt tại boundary có semantic value: request/job start-end, external call latency, queue depth, retry count, concurrency saturation, error class và resource usage. Không cần log từng iteration trong loop nóng; lượng log lớn có thể tự trở thành I/O bottleneck.

Trong async service, correlation context không nên dựa mù quáng vào global mutable variable. `contextvars` cho phép context-local state truyền qua task boundaries phù hợp hơn trong nhiều async flow.

Khi điều tra memory growth, kết hợp RSS/process metric với `tracemalloc` hoặc object-level evidence. Khi điều tra CPU, profile call stacks/hotspots. Khi điều tra event-loop stall, tìm blocking synchronous work và task latency. Evidence phải khớp lớp mechanism đang nghi ngờ.

---

## Capstone — Review worker `automation/` như một hệ thống, không chỉ như code Python

Hãy đọc [automation/app.py](../../automation/app.py), [automation/pipeline.py](../../automation/pipeline.py) và [automation/test_pipeline.py](../../automation/test_pipeline.py) như một hệ thống có nhiều boundary.

`app.py` sở hữu HTTP/application concurrency boundary. `asyncio.Lock` hiện diễn tả single-process mutual exclusion. `asyncio.to_thread()` là adapter giữa event loop và synchronous pipeline. `pipeline.py` sở hữu filesystem, subprocess, HTTP và orchestration side effects. `test_pipeline.py` kiểm một phần behavior bằng `unittest`.

Một review theo first principles nên truy theo chuỗi sau:

```text
request
↓
application concurrency ownership
↓
sync/async boundary
↓
pipeline state và side effects
↓
external process / filesystem / HTTP
↓
timeout / retry / cancellation / idempotency
↓
logs / metrics / failure evidence
↓
deployment process / replica model
```

Nếu deployment chỉ có một process, local lock có thể đáp ứng invariant hiện tại. Nếu tăng nhiều worker hoặc replica, cùng invariant cần thiết kế lại. Nếu `Pipeline().run` có side effect không idempotent, retry ở HTTP layer phải hiểu semantics đó. Nếu request bị disconnect, thread chạy pipeline có thể vẫn tiếp tục; cancellation ownership cần quyết định rõ thay vì giả định framework sẽ “dừng hết”. Nếu output/log chứa token hoặc external response nguyên bản, security boundary phải được review.

Capstone này cho thấy senior Python không phải thuộc thêm syntax. Nó là khả năng nối object semantics, runtime, I/O, concurrency, packaging, security và operations thành một causal model đủ để dự đoán failure trước khi production buộc ta học bằng incident.

---

## Những câu hỏi nên tự trả lời sau tài liệu này

Bạn nên giải thích được vì sao shallow copy có thể làm default state đổi; vì sao import có thể gây I/O trước startup; vì sao `pyproject.toml` không đồng nghĩa deploy reproducible; vì sao `async def` vẫn có thể block; vì sao local `asyncio.Lock` không phải distributed lock; vì sao queue unbounded là memory-retention mechanism; vì sao GIL không phải thread-safety contract; vì sao free-threaded migration cần race audit; vì sao retry liên hệ trực tiếp với idempotency; và vì sao log, metric, trace trả lời các câu hỏi khác nhau.

Nếu một câu chỉ trả lời được bằng tên API mà chưa mô tả invariant và mechanism, nên quay lại canonical part tương ứng.

## Nguồn chính

- Python 3.14 Language Reference: https://docs.python.org/3.14/reference/
- Python 3.14 Standard Library: https://docs.python.org/3.14/library/
- `asyncio`: https://docs.python.org/3.14/library/asyncio.html
- `multiprocessing`: https://docs.python.org/3.14/library/multiprocessing.html
- Thread state và GIL: https://docs.python.org/3.14/c-api/threads.html
- Thread-safety guarantees: https://docs.python.org/3.14/builtins/threadsafety.html
- Python 3.14 What's New: https://docs.python.org/3.14/whatsnew/3.14.html
- Python Packaging User Guide: https://packaging.python.org/
- Dependency Groups specification: https://packaging.python.org/en/latest/specifications/dependency-groups/
- PyPA specifications: https://packaging.python.org/en/latest/specifications/
