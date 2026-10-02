# Python kỹ thuật (engineering / 엔지니어링) trường hợp (case / 사례) Studies

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Python kỹ thuật (engineering / 엔지니어링) trường hợp (case / 사례) Studies**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Trường hợp (case / 사례) 1 — “Tôi chỉ gán sang biến khác, tại sao dữ liệu cũ cũng đổi?”** gom dữ liệu hoặc nguồn để kiểm tra một nhận định cụ thể; sau đó sang **Trường hợp (case / 사례) 2 — Import làm dịch vụ (service / 서비스) khởi động chậm hoặc thất bại trước khi nhận yêu cầu (request / 요청)** để đem mô hình vào tình huống cụ thể. Mạch này nối case study engineering với triệu chứng, giả thuyết, trade-off và outcome, để bài học đi từ sự cố thật đến quyết định có thể lặp lại.

> Baseline: Python 3.14.7. Kiểm chứng: 2026-09-22.

Tài liệu này không tạo thêm một mức (level / 수준) học mới và cũng không lặp lại bốn chuẩn gốc (canonical / 정본) part. Mục tiêu là buộc các concept đã học phải hoạt động cùng nhau trong một tình huống gần môi trường vận hành (production / 운영 환경). Mỗi trường hợp (case / 사례) bắt đầu từ một hiện tượng quan sát được, xác định bất biến (invariant / 불변식) cần giữ, lần theo cơ chế (mechanism / 메커니즘) tạo ra hành vi (behavior / 동작), rồi mới chọn thiết kế hoặc công cụ. Cách đọc này quan trọng vì bug thực tế hiếm khi tự giới thiệu mình bằng tên chapter như “đây là lỗi iterator” hay “đây là lỗi vòng lặp sự kiện (event loop / 이벤트 루프)”.

Nếu một thuật ngữ cơ sở chưa chắc, quay lại [Part 1](python_01_beginner.md) và [Part 2](python_02_intermediate.md). Nếu vấn đề liên quan dự án (project / 프로젝트), tính đồng thời (concurrency / 동시성) hoặc vận hành, đọc song song [Part 3](python_03_senior.md). Khi cần đi xuống thời gian chạy (runtime / 런타임), GIL, GC hoặc thực thi (execution / 실행) internals, dùng [Part 4](python_04_master.md). Các khái niệm tiến trình (process / 프로세스), scheduling, mạng (network / 네트워크) và phân tán (distributed / 분산) coordination rộng hơn được nối sang [Computer Science Knowledge Library](../../computer_science/README.md).

---

## Trường hợp (case / 사례) 1 — “Tôi chỉ gán sang biến khác, tại sao dữ liệu cũ cũng đổi?”

Giả sử một dịch vụ (service / 서비스) nhận cấu hình mặc định rồi thêm option theo yêu cầu (request / 요청):

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

Nhìn bề mặt, `copy()` dường như đã tạo cấu hình mới. Nhưng đây là bản sao nông (shallow copy / 얕은 복사). `options` là `dict` mới, còn giá trị (value / 값) tại key `"headers"` vẫn là cùng một nested `dict` với `DEFAULT_OPTIONS`. Khi `update()` mutate nested đối tượng (object / 객체), default toàn cục cũng thay đổi.

Bất biến (invariant / 불변식) thực sự cần giữ là: một yêu cầu (request / 요청) không được làm biến đổi cấu hình mặc định dùng cho yêu cầu (request / 요청) khác. Vì vậy câu hỏi đúng không phải “nên dùng `copy()` hay `deepcopy()`?”, mà là “đối tượng (object / 객체) nào thuộc quyền sở hữu (ownership / 소유권) của ai và ranh giới (boundary / 경계) nào phải tạo snapshot?”. Một cách rõ hơn là tạo đối tượng (object / 객체) mới tại đúng nested ranh giới (boundary / 경계):

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

`deepcopy()` có thể chữa ví dụ nhỏ, nhưng không phải lời giải tổng quát. đối tượng (object / 객체) đồ thị (graph / 그래프) thực tế có thể chứa khóa (lock / 잠금), socket, tệp (file / 파일) handle, bộ nhớ đệm (cache / 캐시) hoặc đối tượng (object / 객체) có định danh (identity / 식별자) ngữ nghĩa (semantics / 의미론). Thiết kế bền hơn là làm quyền sở hữu (ownership / 소유권) tường minh (explicit / 명시적) và ưu tiên immutable giá trị (value / 값) tại ranh giới (boundary / 경계) nơi mutation không có ý nghĩa.

Bằng chứng (evidence / 증거) khi gỡ lỗi (debug / 디버그) trường hợp (case / 사례) này là kiểm tra định danh (identity / 식별자) của nested đối tượng (object / 객체), không chỉ in giá trị (value / 값):

```python
options = DEFAULT_OPTIONS.copy()
assert options is not DEFAULT_OPTIONS
assert options["headers"] is DEFAULT_OPTIONS["headers"]
```

Mô hình tư duy (mental model / 사고 모델) cần mang sang môi trường vận hành (production / 운영 환경) là `name → object → nested object graph`. Gán tên, bản sao (copy / 복사) bộ chứa (container / 컨테이너) và mutate trạng thái (state / 상태) là ba thao tác khác nhau.

---

> **Chuyển mạch:** Trong **Python kỹ thuật (engineering / 엔지니어링) trường hợp (case / 사례) Studies**, **Trường hợp (case / 사례) 1 — “Tôi chỉ gán sang biến khác, tại sao dữ liệu cũ cũng đổi?”** cho ta quy tắc; **Trường hợp (case / 사례) 2 — Import làm dịch vụ (service / 서비스) khởi động chậm hoặc thất bại trước khi nhận yêu cầu (request / 요청)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Trường hợp (case / 사례) 3 — “Máy tôi chạy được” nhưng CI hoặc môi trường vận hành (production / 운영 환경) cài phụ thuộc (dependency / 의존성) khác** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trường hợp (case / 사례) 2 — Import làm dịch vụ (service / 서비스) khởi động chậm hoặc thất bại trước khi nhận yêu cầu (request / 요청)

Một mô-đun (module / 모듈) thường được viết kiểu:

```python
# config.py
CONFIG = load_remote_config()
MODEL = build_large_model(CONFIG)
```

Sau đó nhiều mô-đun (module / 모듈) chỉ cần `from config import MODEL`. Vấn đề là import lần đầu thực thi top-level mã (code / 코드). mạng (network / 네트워크) chậm, credential chưa có, remote dịch vụ (service / 서비스) down hoặc mô hình (model / 모델) bản dựng (build / 빌드) nặng đều biến import thành startup side tác động (effect / 효과). kiểm thử (test / 테스트) chỉ import một helper cũng có thể vô tình gọi mạng (network / 네트워크).

Bất biến (invariant / 불변식) cần giữ là: import phải đủ deterministic để mô-đun (module / 모듈) có thể được tải (load / 로드) cho kiểm thử (test / 테스트), tooling và ứng dụng (application / 애플리케이션) startup mà không phụ thuộc side tác động (effect / 효과) không cần thiết. Điều này không đồng nghĩa “top-level mã (code / 코드) luôn xấu”; constant đơn giản và definition là bình thường. ranh giới (boundary / 경계) nguy hiểm là I/O, tiến trình (process / 프로세스) creation, cơ sở dữ liệu (database / 데이터베이스) liên kết (connection / 연결) hoặc initialization có dạng thất bại (failure mode / 실패 모드) lớn.

Thiết kế rõ hơn là đưa side tác động (effect / 효과) vào composition gốc (root / 루트):

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

Circular import là phiên bản kiến trúc của cùng vấn đề. Nếu `domain.py` import `service.py` để lấy helper, còn `service.py` import `domain.py` để lấy mô hình (model / 모델), thời gian chạy (runtime / 런타임) có thể quan sát mô-đun (module / 모듈) đang partially initialized. Di chuyển import vào hàm (function / 함수) đôi khi tránh lỗi tức thời nhưng không sửa phụ thuộc (dependency / 의존성) direction. Cách chữa bền hơn thường là tách lớp trừu tượng (abstraction / 추상화) chung xuống tầng (layer / 계층) thấp hơn hoặc đưa orchestration lên tầng (layer / 계층) cao hơn.

Khi startup chậm, đo import đồ thị (graph / 그래프) thay vì đoán. Khi import thất bại (fail / 실패), nhìn mô-đun (module / 모듈) nào đang partially initialized và phụ thuộc (dependency / 의존성) nào chạy ngược chiều kiến trúc.

---

> **Chuyển mạch:** Ở chặng này của **Python kỹ thuật (engineering / 엔지니어링) trường hợp (case / 사례) Studies**, **Trường hợp (case / 사례) 2 — Import làm dịch vụ (service / 서비스) khởi động chậm hoặc thất bại trước khi nhận yêu cầu (request / 요청)** cho ta quy tắc; **Trường hợp (case / 사례) 3 — “Máy tôi chạy được” nhưng CI hoặc môi trường vận hành (production / 운영 환경) cài phụ thuộc (dependency / 의존성) khác** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Trường hợp (case / 사례) 4 — Async endpoint nhưng dịch vụ (service / 서비스) vẫn “đơ”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trường hợp (case / 사례) 3 — “Máy tôi chạy được” nhưng CI hoặc môi trường vận hành (production / 운영 환경) cài phụ thuộc (dependency / 의존성) khác

Một dự án (project / 프로젝트) Python không chỉ là mã nguồn (source code / 소스 코드). hành vi (behavior / 동작) còn phụ thuộc trình thông dịch (interpreter / 인터프리터), phân phối (distribution / 분포) packages, bản địa (native / 네이티브) libraries, nền tảng (platform / 플랫폼) tag và cách môi trường (environment / 환경) được resolve. `pyproject.toml` giải quyết siêu dữ liệu (metadata / 메타데이터)/bản dựng (build / 빌드)/công cụ (tool / 도구) cấu hình (configuration / 구성), nhưng không tự động đảm bảo mọi triển khai (deployment / 배포) resolve đúng cùng phụ thuộc (dependency / 의존성) set.

Hãy tách ba câu hỏi. dự án (project / 프로젝트) tuyên bố tương thích với phụ thuộc (dependency / 의존성) nào? hệ thống dựng (build system / 빌드 시스템) dùng backend nào để tạo sản phẩm tạo ra (artifact / 산출물)? triển khai (deployment / 배포) cụ thể đã resolve chính xác phiên bản (version / 버전) nào?

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

`[project].dependencies` là đặc tả hợp đồng (contract / 계약) thời gian chạy (runtime / 런타임) của phân phối (distribution / 분포). `dependency-groups` phù hợp cho nhóm development/nội bộ (internal / 내부) và không trở thành phụ thuộc (dependency / 의존성) siêu dữ liệu (metadata / 메타데이터) của gói (package / 패키지) bản dựng (build / 빌드). chính xác (exact / 정확한) resolved môi trường (environment / 환경) cho môi trường vận hành (production / 운영 환경) lại là một concern khác, thường cần khóa (lock / 잠금) hoặc sản phẩm tạo ra (artifact / 산출물) reproducible theo toolchain của dự án (project / 프로젝트).

Wheel làm bài toán thú vị hơn. Pure-Python wheel có portability cao hơn. Wheel chứa bản địa (native / 네이티브) extension phụ thuộc Python/ABI/nền tảng (platform / 플랫폼) tính tương thích (compatibility / 호환성) tags. Vì vậy “gói (package / 패키지) tồn tại trên PyPI” không bảo đảm có nhị phân (binary / 이진) sản phẩm tạo ra (artifact / 산출물) phù hợp với trình thông dịch (interpreter / 인터프리터) và kiến trúc (architecture / 아키텍처) đang deploy. Nếu installer phải bản dựng (build / 빌드) từ nguồn (source / 소스), máy chủ (server / 서버) lại cần trình biên dịch (compiler / 컴파일러)/header/bản địa (native / 네이티브) phụ thuộc (dependency / 의존성) phù hợp.

Khi sự cố (incident / 인시던트) xảy ra chỉ trên một môi trường (environment / 환경), bằng chứng (evidence / 증거) cần thu không chỉ là `pip freeze`. Ghi cả `python -VV`, nền tảng (platform / 플랫폼)/kiến trúc (architecture / 아키텍처), khóa (lock / 잠금) trạng thái (state / 상태), sản phẩm tạo ra (artifact / 산출물) băm (hash / 해시), wheel tag hoặc bản địa (native / 네이티브) phụ thuộc (dependency / 의존성) liên quan. Reproducibility là thuộc tính của toàn chuỗi bản dựng (build / 빌드) → resolve → install → run.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Python kỹ thuật (engineering / 엔지니어링) trường hợp (case / 사례) Studies**, **Trường hợp (case / 사례) 3 — “Máy tôi chạy được” nhưng CI hoặc môi trường vận hành (production / 운영 환경) cài phụ thuộc (dependency / 의존성) khác** cho ta quy tắc; **Trường hợp (case / 사례) 4 — Async endpoint nhưng dịch vụ (service / 서비스) vẫn “đơ”** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Trường hợp (case / 사례) 5 — thông lượng (throughput / 처리량) tăng rồi bộ nhớ (memory / 메모리) tăng không giới hạn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trường hợp (case / 사례) 4 — Async endpoint nhưng dịch vụ (service / 서비스) vẫn “đơ”

Một endpoint FastAPI `async def` có thể phải gọi một chuỗi xử lý đồng bộ qua `asyncio.to_thread`. Đây là case study tốt vì nó thể hiện ranh giới phổ biến: ứng dụng async không tự biến mã sync thành non-blocking.

Nếu coroutine gọi trực tiếp một hàm (function / 함수) sync chạy lâu:

```python
@app.post("/run")
async def run():
    return Pipeline().run()
```

thì event-loop luồng thực thi (thread / 스레드) bị giữ cho đến khi lời gọi (call / 호출) trả về. Trong thời gian đó, coroutine khác trên cùng vòng lặp (loop / 루프) không được schedule bình thường. `async def` không biến mã (code / 코드) con thành non-blocking.

`asyncio.to_thread()` offload synchronous hàm (function / 함수) sang worker luồng thực thi (thread / 스레드), giúp vòng lặp sự kiện (event loop / 이벤트 루프) tiếp tục phục vụ I/O khác:

```python
result = await asyncio.to_thread(Pipeline().run)
```

Nhưng đây chưa phải lời giải cho mọi thứ. Nếu chuỗi xử lý (pipeline / 파이프라인) là CPU-bound pure Python trên bản dựng (build / 빌드) có GIL, luồng thực thi (thread / 스레드) không tự tạo multi-core speedup. Nếu chuỗi xử lý (pipeline / 파이프라인) giữ tài nguyên (resource / 자원) không thread-safe, offload lại mở thêm tính đồng thời (concurrency / 동시성) concern. Nếu yêu cầu (request / 요청) bị cancel, cancellation của coroutine cũng không đồng nghĩa Python có thể cưỡng chế dừng synchronous hàm (function / 함수) đang chạy trong luồng thực thi (thread / 스레드).

`asyncio.Lock` trong một endpoint chỉ bảo vệ bất biến “một tiến trình không chạy hai chuỗi xử lý qua endpoint cùng lúc”. Nó không bảo vệ bất biến “toàn triển khai chỉ có một chuỗi xử lý”, vì nhiều worker hoặc replica có khóa riêng. Khi quy mô tăng, bất biến toàn hệ thống cần coordination bên ngoài, idempotency hoặc job system thích hợp.

Đây là ví dụ điển hình cho cách lập luận (reasoning / 추론) theo phạm vi (scope / 범위): tác vụ (task / 작업) phạm vi (scope / 범위) → vòng lặp sự kiện (event loop / 이벤트 루프) → luồng thực thi (thread / 스레드) → tiến trình (process / 프로세스) → replica → hệ thống phân tán (distributed system / 분산 시스템). Một thành phần nguyên thủy (primitive / 기본 요소) đúng ở tầng thấp không tự mở rộng ngữ nghĩa (semantics / 의미론) lên tầng cao hơn.

---

> **Chuyển mạch:** Trong **Python kỹ thuật (engineering / 엔지니어링) trường hợp (case / 사례) Studies**, **Trường hợp (case / 사례) 4 — Async endpoint nhưng dịch vụ (service / 서비스) vẫn “đơ”** cho ta quy tắc; **Trường hợp (case / 사례) 5 — thông lượng (throughput / 처리량) tăng rồi bộ nhớ (memory / 메모리) tăng không giới hạn** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Trường hợp (case / 사례) 6 — Chọn luồng thực thi (thread / 스레드), tiến trình (process / 프로세스), async hay free-threaded bản dựng (build / 빌드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trường hợp (case / 사례) 5 — thông lượng (throughput / 처리량) tăng rồi bộ nhớ (memory / 메모리) tăng không giới hạn

Một async producer đọc message nhanh hơn bên tiêu thụ (consumer / 소비자) ghi cơ sở dữ liệu (database / 데이터베이스):

```python
queue = asyncio.Queue()

async def producer():
    while True:
        item = await receive()
        await queue.put(item)
```

Mã (code / 코드) functional có thể đúng trong kiểm thử (test / 테스트) nhỏ nhưng hàng đợi (queue / 큐) không giới hạn biến chênh lệch thông lượng (throughput / 처리량) thành bộ nhớ (memory / 메모리) growth. Vấn đề không nằm ở garbage collector: item vẫn reachable vì hàng đợi (queue / 큐) đang giữ tham chiếu (reference / 참조).

Bất biến (invariant / 불변식) vận hành là hệ thống phải có giới hạn work-in-flight tương ứng với sức chứa (capacity / 용량) downstream. Bounded hàng đợi (queue / 큐) tạo backpressure (áp lực ngược / backpressure / 백프레셔):

```python
queue = asyncio.Queue(maxsize=100)
```

Khi hàng đợi (queue / 큐) đầy, `await queue.put(item)` suspend producer. Việc này chuyển overload từ “ăn RAM đến chết” thành một trạng thái (state / 상태) có thể quan sát và điều khiển. Nhưng kích thước (size / 크기) 100 không phải con số ma thuật; nó liên hệ với độ trễ (latency / 지연 시간), thông lượng (throughput / 처리량), bộ nhớ (memory / 메모리) per item và burst tolerance.

Bằng chứng vận hành (production evidence / 운영 증거) cần nhìn cùng lúc hàng đợi (queue / 큐) độ sâu (depth / 깊이), enqueue/dequeue tỷ lệ (rate / 비율), processing độ trễ (latency / 지연 시간), lỗi (error / 오류)/thử lại (retry / 재시도) tỷ lệ (rate / 비율) và bộ nhớ (memory / 메모리). Nếu thử lại (retry / 재시도) tự tạo thêm item, thử lại (retry / 재시도) chính sách (policy / 정책) có thể trở thành tải (load / 로드) amplifier. Nếu bên tiêu thụ (consumer / 소비자) gọi bên ngoài (external / 외부) dịch vụ (service / 서비스) không có deadline, vài yêu cầu (request / 요청) treo có thể chiếm hết worker và làm hàng đợi (queue / 큐) đầy dù CPU còn rảnh.

Backpressure vì vậy không phải API của `asyncio`; nó là bất biến (invariant / 불변식) của chuỗi xử lý (pipeline / 파이프라인) dữ liệu.

---

> **Chuyển mạch:** Ở chặng này của **Python kỹ thuật (engineering / 엔지니어링) trường hợp (case / 사례) Studies**, **Trường hợp (case / 사례) 5 — thông lượng (throughput / 처리량) tăng rồi bộ nhớ (memory / 메모리) tăng không giới hạn** cho ta quy tắc; **Trường hợp (case / 사례) 6 — Chọn luồng thực thi (thread / 스레드), tiến trình (process / 프로세스), async hay free-threaded bản dựng (build / 빌드)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Trường hợp (case / 사례) 7 — di chuyển (migration / 마이그레이션) sang free-threaded Python không phải chỉ đổi trình thông dịch (interpreter / 인터프리터)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trường hợp (case / 사례) 6 — Chọn luồng thực thi (thread / 스레드), tiến trình (process / 프로세스), async hay free-threaded bản dựng (build / 빌드)

Một lỗi thiết kế phổ biến là chọn tính đồng thời (concurrency / 동시성) mô hình (model / 모델) dựa trên slogan: “Python có GIL nên dùng tiến trình (process / 프로세스)”, hoặc “async nhanh hơn luồng thực thi (thread / 스레드)”. Cách đúng là bắt đầu từ dominant công việc (work / 작업).

Nếu phần lớn thời gian chờ socket hoặc blocking I/O sync, luồng thực thi (thread / 스레드) pool có thể overlap thời gian chờ với ít thay đổi mã (code / 코드). Nếu phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) đã async-native và cần rất nhiều concurrent connections, `asyncio` có thể giảm chi phí (cost / 비용) per tác vụ (task / 작업) và cho vòng đời (lifecycle / 생명주기) rõ qua `TaskGroup`. Nếu tải công việc (workload / 워크로드) CPU-bound pure Python trên CPython có GIL, tiến trình (process / 프로세스) pool thường là baseline để sử dụng nhiều cốt lõi (core / 핵심), nhưng phải trả startup/IPC/serialization chi phí (cost / 비용). Nếu heavy computation nằm trong bản địa (native / 네이티브) thư viện (library / 라이브러리) có bản phát hành (release / 릴리스) GIL, luồng thực thi (thread / 스레드) lại có thể quy mô (scale / 규모) CPU tốt.

Python 3.14 thêm một nhánh lựa chọn quan trọng: free-threaded CPython được hỗ trợ chính thức nhưng vẫn optional. Nó cho phép nhiều luồng thực thi (thread / 스레드) chạy Python mã (code / 코드) song song, nhưng không biến dùng chung (shared / 공유) mutable trạng thái (state / 상태) thành an toàn. phụ thuộc (dependency / 의존성) bản địa (native / 네이티브) phải tương thích, và hiệu năng (performance / 성능) profile single-thread/multi-thread cần đo trên bản dựng (build / 빌드) thật.

Quyết định (decision / 결정) thực tế nên dựa trên đo lường (measurement / 측정):

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

Nếu phải truyền hàng GB giữa processes mỗi job, tiến trình (process / 프로세스) pool có thể chậm hơn single tiến trình (process / 프로세스). Nếu free-threaded giúp CPU nhưng extension quan trọng bật lại GIL hoặc chưa compatible, benefit biến mất. Nếu async mã (code / 코드) gọi sync thư viện (library / 라이브러리) nặng, vòng lặp sự kiện (event loop / 이벤트 루프) vẫn bị khối (block / 블록) nếu không có adapter ranh giới (boundary / 경계).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Python kỹ thuật (engineering / 엔지니어링) trường hợp (case / 사례) Studies**, sau khi thấy quy trình trong **Trường hợp (case / 사례) 6 — Chọn luồng thực thi (thread / 스레드), tiến trình (process / 프로세스), async hay free-threaded bản dựng (build / 빌드)**, **Trường hợp (case / 사례) 7 — di chuyển (migration / 마이그레이션) sang free-threaded Python không phải chỉ đổi trình thông dịch (interpreter / 인터프리터)** đặt nó vào một trường hợp đủ cụ thể để nhận ra điều kiện thành công và chỗ dễ sai. Từ đây, **Trường hợp (case / 사례) 8 — kiểm thử (test / 테스트) pass nhưng hệ thống vẫn sai vì kiểm thử (test / 테스트) không kiểm bất biến (invariant / 불변식)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trường hợp (case / 사례) 7 — di chuyển (migration / 마이그레이션) sang free-threaded Python không phải chỉ đổi trình thông dịch (interpreter / 인터프리터)

Giả sử dịch vụ (service / 서비스) hiện chạy ổn với CPython có GIL và muốn thử free-threaded 3.14. Sai lầm nguy hiểm là suy luận rằng mã (code / 코드) đã chạy nhiều luồng thực thi (thread / 스레드) lâu nay nên mặc nhiên thread-safe.

GIL trước đây serialize nhiều thực thi (execution / 실행) ở trình thông dịch (interpreter / 인터프리터) mức (level / 수준), nhưng nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식) có thể vẫn racy. Một bộ nhớ đệm (cache / 캐시) kiểu check-then-set là ví dụ:

```python
if key not in cache:
    cache[key] = compute(key)
return cache[key]
```

Hai luồng thực thi (thread / 스레드) có thể cùng thấy key chưa tồn tại rồi cùng compute. Ngay cả khi final dict không corrupt, side tác động (effect / 효과) của `compute()` có thể chạy hai lần. tính đúng đắn (correctness / 정확성) phải dựa trên bất biến (invariant / 불변식) và synchronization thích hợp, không dựa trên observation rằng một built-in thao tác (operation / 연산) “có vẻ atomic”.

Di chuyển (migration / 마이그레이션) kiểm tra (audit / 감사) cần nhìn dùng chung (shared / 공유) mutable objects, singleton/toàn cục (global / 전역) registries, lazy initialization, caches, random/process-wide trạng thái (state / 상태), môi trường (environment / 환경) mutation, tín hiệu (signal / 신호) handling, C extensions và kiểm thử (test / 테스트) các giả định (assumptions / 가정들). Sau đó chạy stress/race-oriented kiểm thử (test / 테스트) trên chính free-threaded bản dựng (build / 빌드). Một kiểm thử (test / 테스트) pass một lần gần như không chứng minh absence of race vì scheduling không gian (space / 공간) rất lớn.

Điểm quan trọng của Python 3.14 là free-threading đã trở thành supported option, nhưng thư viện (library / 라이브러리) documentation vẫn phải nói rõ bản dựng (build / 빌드)/thời gian chạy (runtime / 런타임) ngữ cảnh (context / 맥락). mã (code / 코드) portable không nên dựa vào việc GIL luôn tồn tại, cũng không nên giả định GIL luôn bị tắt.

---

> **Chuyển mạch:** Trong **Python kỹ thuật (engineering / 엔지니어링) trường hợp (case / 사례) Studies**, **Trường hợp (case / 사례) 7 — di chuyển (migration / 마이그레이션) sang free-threaded Python không phải chỉ đổi trình thông dịch (interpreter / 인터프리터)** cho ta quy tắc; **Trường hợp (case / 사례) 8 — kiểm thử (test / 테스트) pass nhưng hệ thống vẫn sai vì kiểm thử (test / 테스트) không kiểm bất biến (invariant / 불변식)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Trường hợp (case / 사례) 9 — động (dynamic / 동적) tính năng (feature / 기능) biến thành ranh giới bảo mật (security boundary / 보안 경계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trường hợp (case / 사례) 8 — kiểm thử (test / 테스트) pass nhưng hệ thống vẫn sai vì kiểm thử (test / 테스트) không kiểm bất biến (invariant / 불변식)

Giả sử hàm (function / 함수) thử lại (retry / 재시도) payment API. đơn vị (unit / 단위) kiểm thử (test / 테스트) chỉ mock máy khách (client / 클라이언트) và assert `client.post` được gọi ba lần khi hết thời gian chờ (timeout / 타임아웃). kiểm thử (test / 테스트) đó kiểm hiện thực (implementation / 구현) detail, nhưng chưa kiểm bất biến (invariant / 불변식) quan trọng hơn: thao tác (operation / 연산) có bị duplicate side tác động (effect / 효과) không?

Kiểm thử (test / 테스트) thiết kế (design / 설계) nên xuất phát từ đặc tả hợp đồng (contract / 계약). Nếu thao tác (operation / 연산) phải idempotent, kiểm thử (test / 테스트) cần mô hình (model / 모델) cùng idempotency key qua thử lại (retry / 재시도) và verify máy chủ (server / 서버)/fake adapter không tạo hai payment. Nếu parser có thuộc tính (property / 속성) serialize → parse bảo toàn ngữ nghĩa (semantic / 의미적) giá trị (value / 값), example-based kiểm thử (test / 테스트) vài đầu vào (input / 입력) đẹp là chưa đủ; property-based hoặc fuzz testing có thể khám phá empty đầu vào (input / 입력), Unicode, nesting, kích thước (size / 크기) extreme và malformed ranh giới (boundary / 경계) tốt hơn.

Nondeterminism cũng cần quyền sở hữu (ownership / 소유권). Clock, random, mạng (network / 네트워크) và tiến trình (process / 프로세스) môi trường (environment / 환경) nên đi qua ranh giới (boundary / 경계) có thể thay thế trong kiểm thử (test / 테스트). Thay vì patch mọi private hàm (function / 함수), inject clock hoặc adapter nơi side tác động (effect / 효과) xuất hiện:

```python
from collections.abc import Callable
from datetime import datetime

def make_record(now: Callable[[], datetime]) -> dict:
    return {"created_at": now().isoformat()}
```

Kiểm thử (test / 테스트) tốt làm rõ bất biến (invariant / 불변식) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론). Mock chỉ là một kỹ thuật để cô lập ranh giới (boundary / 경계); số lượng mock không phải thước đo chất lượng kiểm thử (test / 테스트).

---

> **Chuyển mạch:** Ở chặng này của **Python kỹ thuật (engineering / 엔지니어링) trường hợp (case / 사례) Studies**, **Trường hợp (case / 사례) 8 — kiểm thử (test / 테스트) pass nhưng hệ thống vẫn sai vì kiểm thử (test / 테스트) không kiểm bất biến (invariant / 불변식)** cho ta quy tắc; **Trường hợp (case / 사례) 9 — động (dynamic / 동적) tính năng (feature / 기능) biến thành ranh giới bảo mật (security boundary / 보안 경계)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Trường hợp (case / 사례) 10 — sự cố (incident / 인시던트) môi trường vận hành (production / 운영 환경): CPU bình thường nhưng yêu cầu (request / 요청) độ trễ (latency / 지연 시간) tăng mạnh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trường hợp (case / 사례) 9 — động (dynamic / 동적) tính năng (feature / 기능) biến thành ranh giới bảo mật (security boundary / 보안 경계)

Python cho phép `eval`, `exec`, động (dynamic / 동적) import, pickle, template engine, regex và subprocess. Điểm chung không phải chúng “nguy hiểm”, mà là chúng diễn giải đầu vào (input / 입력) theo một grammar hoặc mô hình thực thi (execution model / 실행 모델) mạnh hơn string thông thường.

Ví dụ, chạy command bằng shell:

```python
subprocess.run(f"git show {user_input}", shell=True)
```

biến `user_input` thành một phần shell grammar. Escape sai một ký tự có thể đổi nghĩa command. Nếu không cần shell tính năng (feature / 기능), argument véc-tơ (vector / 벡터) giữ dữ liệu (data / 데이터) và cú pháp (syntax / 문법) tách nhau:

```python
subprocess.run(["git", "show", user_input], check=True)
```

Tương tự, structured JSON nên parse bằng JSON parser chứ không regex; SQL nên parameterize bằng cơ sở dữ liệu (database / 데이터베이스) API; HTML cần context-aware escaping; untrusted đối tượng (object / 객체) dữ liệu (data / 데이터) không được `pickle.loads()` chỉ vì tệp (file / 파일) extension quen thuộc.

Không tồn tại một hàm `sanitize()` chung cho mọi ranh giới (boundary / 경계). bảo mật (security / 보안) lập luận (reasoning / 추론) phải hỏi: đầu vào (input / 입력) đang đi vào grammar nào, parser/executor nào, quyền của tiến trình (process / 프로세스) là gì, tài nguyên (resource / 자원) exhaustion có thể xảy ra không, và đầu ra (output / 출력)/lỗi (error / 오류) có làm lộ secret không?

Một tích hợp subprocess được viết thủ công dùng argument dạng danh sách với `subprocess.run`; đây là mẫu đáng giữ khi command không cần shell expansion.

---

> **Chuyển mạch:** Hai case trước lần lượt chỉ ra ranh giới bảo mật và ranh giới độ trễ. Capstone gộp chúng thành một câu hỏi hệ thống: khi endpoint, subprocess, trạng thái và test cùng thay đổi, bằng chứng nào cho thấy thiết kế vẫn an toàn?

## Trường hợp (case / 사례) 10 — sự cố (incident / 인시던트) môi trường vận hành (production / 운영 환경): CPU bình thường nhưng yêu cầu (request / 요청) độ trễ (latency / 지연 시간) tăng mạnh

Khi độ trễ (latency / 지연 시간) tăng, chỉ log exception thường không đủ vì yêu cầu (request / 요청) có thể chậm nhưng không thất bại (fail / 실패). khả năng quan sát (observability / 관측 가능성) cần phân biệt log, chỉ số (metric / 지표) và dấu vết (trace / 추적).

Giả sử dịch vụ (service / 서비스) gọi ba bên ngoài (external / 외부) dependencies. chỉ số (metric / 지표) cho biết p95 độ trễ (latency / 지연 시간) tăng từ 200 ms lên 3 s. dấu vết (trace / 추적) cho biết 2.7 s nằm ở một HTTP lời gọi (call / 호출). Log của lời gọi (call / 호출) đó cho biết thử lại (retry / 재시도) hai lần sau read hết thời gian chờ (timeout / 타임아웃). Đây là chuỗi nhân quả (causal chain / 인과 사슬) mà một công cụ đơn lẻ khó cung cấp.

Instrument nên đặt tại ranh giới (boundary / 경계) có ngữ nghĩa (semantic / 의미적) giá trị (value / 값): yêu cầu (request / 요청)/job start-end, bên ngoài (external / 외부) lời gọi (call / 호출) độ trễ (latency / 지연 시간), hàng đợi (queue / 큐) độ sâu (depth / 깊이), thử lại (retry / 재시도) count, tính đồng thời (concurrency / 동시성) saturation, lỗi (error / 오류) lớp (class / 클래스) và tài nguyên (resource / 자원) usage. Không cần log từng iteration trong vòng lặp (loop / 루프) nóng; lượng log lớn có thể tự trở thành I/O bottleneck.

Trong async dịch vụ (service / 서비스), correlation ngữ cảnh (context / 맥락) không nên dựa mù quáng vào toàn cục (global / 전역) mutable variable. `contextvars` cho phép context-local trạng thái (state / 상태) truyền qua tác vụ (task / 작업) boundaries phù hợp hơn trong nhiều async luồng (flow / 흐름).

Khi điều tra bộ nhớ (memory / 메모리) growth, kết hợp RSS/tiến trình (process / 프로세스) chỉ số (metric / 지표) với `tracemalloc` hoặc object-level bằng chứng (evidence / 증거). Khi điều tra CPU, profile lời gọi (call / 호출) stacks/hotspots. Khi điều tra event-loop stall, tìm blocking synchronous công việc (work / 작업) và tác vụ (task / 작업) độ trễ (latency / 지연 시간). bằng chứng (evidence / 증거) phải khớp lớp cơ chế (mechanism / 메커니즘) đang nghi ngờ.

---

> **Chuyển mạch:** Sau khi nối symptom với invariant và evidence ở mục 10, capstone yêu cầu đọc toàn hệ thống thay vì một hàm riêng lẻ. Những câu hỏi cuối tài liệu dùng kết quả đó để khép lại mạch và chỉ ra phần cần kiểm chứng thêm.

## Capstone — rà soát một dịch vụ Python như một hệ thống, không chỉ như mã Python

Hãy đọc một endpoint async, một tác vụ sync có subprocess và bộ kiểm thử tương ứng như một hệ thống có nhiều ranh giới.

Endpoint sở hữu ranh giới HTTP và concurrency. `asyncio.Lock` diễn tả mutual exclusion trong một process; `asyncio.to_thread()` là adapter giữa event loop và chuỗi xử lý sync. Lớp xử lý phía sau sở hữu filesystem, subprocess, HTTP và side effect; bộ kiểm thử `unittest` chỉ xác nhận những hành vi đã được chọn.

Một rà soát (review / 검토) theo nguyên lý nền tảng (first principles / 제일 원리) nên truy theo chuỗi sau:

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

Nếu triển khai (deployment / 배포) chỉ có một tiến trình (process / 프로세스), cục bộ (local / 로컬) khóa (lock / 잠금) có thể đáp ứng bất biến (invariant / 불변식) hiện tại. Nếu tăng nhiều worker hoặc replica, cùng bất biến (invariant / 불변식) cần thiết kế lại. Nếu `Pipeline().run` có side tác động (effect / 효과) không idempotent, thử lại (retry / 재시도) ở HTTP tầng (layer / 계층) phải hiểu ngữ nghĩa (semantics / 의미론) đó. Nếu yêu cầu (request / 요청) bị disconnect, luồng thực thi (thread / 스레드) chạy chuỗi xử lý (pipeline / 파이프라인) có thể vẫn tiếp tục; cancellation quyền sở hữu (ownership / 소유권) cần quyết định rõ thay vì giả định khung phần mềm (framework / 프레임워크) sẽ “dừng hết”. Nếu đầu ra (output / 출력)/log chứa đơn vị từ (token / 토큰) hoặc bên ngoài (external / 외부) phản hồi (response / 응답) nguyên bản, ranh giới bảo mật (security boundary / 보안 경계) phải được rà soát (review / 검토).

Capstone này cho thấy cấp cao (senior / 시니어) Python không phải thuộc thêm cú pháp (syntax / 문법). Nó là khả năng nối đối tượng (object / 객체) ngữ nghĩa (semantics / 의미론), thời gian chạy (runtime / 런타임), I/O, tính đồng thời (concurrency / 동시성), packaging, bảo mật (security / 보안) và operations thành một nhân quả (causal / 인과적) mô hình (model / 모델) đủ để dự đoán thất bại (failure / 실패) trước khi môi trường vận hành (production / 운영 환경) buộc ta học bằng sự cố (incident / 인시던트).

---

> **Chuyển mạch:** **Những câu hỏi nên tự trả lời sau tài liệu này** gom lại các invariant, trade-off và bằng chứng đã gặp trong capstone. Đọc liền hai mục để chuyển từ phân tích một hệ thống sang kế hoạch kiểm chứng bằng nguồn chính và thử nghiệm cụ thể.

## Những câu hỏi nên tự trả lời sau tài liệu này

Bạn nên giải thích được vì sao shallow bản sao (copy / 복사) có thể làm default trạng thái (state / 상태) đổi; vì sao import có thể gây I/O trước startup; vì sao `pyproject.toml` không đồng nghĩa deploy reproducible; vì sao `async def` vẫn có thể khối (block / 블록); vì sao cục bộ (local / 로컬) `asyncio.Lock` không phải phân tán (distributed / 분산) khóa (lock / 잠금); vì sao hàng đợi (queue / 큐) unbounded là memory-retention cơ chế (mechanism / 메커니즘); vì sao GIL không phải thread-safety đặc tả hợp đồng (contract / 계약); vì sao free-threaded di chuyển (migration / 마이그레이션) cần race kiểm tra (audit / 감사); vì sao thử lại (retry / 재시도) liên hệ trực tiếp với idempotency; và vì sao log, chỉ số (metric / 지표), dấu vết (trace / 추적) trả lời các câu hỏi khác nhau.

Nếu một câu chỉ trả lời được bằng tên API mà chưa mô tả bất biến (invariant / 불변식) và cơ chế (mechanism / 메커니즘), nên quay lại chuẩn gốc (canonical / 정본) part tương ứng.

> **Chuyển mạch:** Các câu hỏi cuối file gom những failure mode từ từng case thành một checklist tự kiểm tra. **Nguồn chính** cho phép đối chiếu lại behavior Python thay vì dựa vào trí nhớ sau khi đọc.

## Nguồn chính

- Python 3.14 ngôn ngữ (language / 언어) tham chiếu (reference / 참조): https://docs.python.org/3.14/reference/
- Python 3.14 thư viện chuẩn (standard library / 표준 라이브러리): https://docs.python.org/3.14/library/
- `asyncio`: https://docs.python.org/3.14/library/asyncio.html
- `multiprocessing`: https://docs.python.org/3.14/library/multiprocessing.html
- luồng thực thi (thread / 스레드) trạng thái (state / 상태) và GIL: https://docs.python.org/3.14/c-api/threads.html
- Thread-safety guarantees: https://docs.python.org/3.14/builtins/threadsafety.html
- Python 3.14 What's New: https://docs.python.org/3.14/whatsnew/3.14.html
- Python Packaging người dùng (user / 사용자) Guide: https://packaging.python.org/
- phụ thuộc (dependency / 의존성) Groups specification: https://packaging.python.org/en/latest/specifications/dependency-groups/
- PyPA specifications: https://packaging.python.org/en/latest/specifications/

> **Bàn giao:** Sau **Nguồn chính**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
