from pathlib import Path
import re

BASE = Path("10_backend/java")
P1 = BASE / "java_part1_beginner_rewritten_detailed.md"
P2 = BASE / "java_part2_intermediate_rewritten_detailed.md"
P3 = BASE / "java_part3_senior_rewritten_detailed.md"
P4 = BASE / "java_master_supplement_rewritten_detailed.md"
FILES = [P1, P2, P3, P4]


def add_after_intro(text: str, block: str) -> str:
    if block.splitlines()[0] in text:
        return text
    pos = text.find("\n---\n")
    if pos < 0:
        raise RuntimeError("intro separator not found")
    return text[:pos] + "\n\n" + block.strip() + "\n" + text[pos:]


def replace_numbered_section(text: str, heading_text: str, replacement: str) -> str:
    pat = re.compile(
        r"(?ms)^# \d+\. " + re.escape(heading_text) + r"\n.*?(?=^---\n\n# \d+\.|^# References|\Z)"
    )
    m = pat.search(text)
    if not m:
        raise RuntimeError(f"section not found: {heading_text}")
    return text[:m.start()] + replacement.strip() + "\n\n" + text[m.end():]


def insert_after_numbered_section(text: str, heading_text: str, block: str) -> str:
    if block.splitlines()[0] in text:
        return text
    pat = re.compile(
        r"(?ms)^# \d+\. " + re.escape(heading_text) + r"\n.*?(?=^---\n\n# \d+\.|^# References|\Z)"
    )
    m = pat.search(text)
    if not m:
        raise RuntimeError(f"section not found: {heading_text}")
    return text[:m.end()] + "\n\n---\n\n" + block.strip() + "\n\n" + text[m.end():]


def insert_before_numbered_heading(text: str, heading_text: str, block: str) -> str:
    if block.splitlines()[0] in text:
        return text
    pat = re.compile(r"(?m)^# \d+\. " + re.escape(heading_text) + r"$")
    m = pat.search(text)
    if not m:
        raise RuntimeError(f"heading not found: {heading_text}")
    return text[:m.start()] + block.strip() + "\n\n---\n\n" + text[m.start():]


NAV1 = """## Cách đọc bộ Java canonical

Đây là file đầu tiên trong bốn note canonical của Java Knowledge Library. Hãy đọc theo thứ tự **Beginner → Intermediate → Senior → Master Supplement** thay vì nhảy thẳng vào JVM hoặc concurrency. Beginner xây type system, object model, collections, exception và I/O; Intermediate mở generics, concurrency, JDBC, reflection và JVM; Senior chuyển sang production correctness, profiling và performance; Master chỉ bổ sung low-level/runtime/library-author topics chưa phù hợp với ba phần trước.

Sau khi hoàn thành file này, tiếp tục tại [Java Part 2 — Intermediate](./java_part2_intermediate_rewritten_detailed.md)."""

NAV2 = """## Vị trí của Part 2 trong learning flow

Part 2 nối trực tiếp từ [Java Part 1 — Beginner](./java_part1_beginner_rewritten_detailed.md). Ở đây bạn không học lại syntax; bạn bắt đầu giải thích được contract của collections/generics, lifecycle của thread/resource, memory visibility, JDBC transaction, reflection, class loading và JVM. Sau khi hoàn thành Part 2, tiếp tục [Java Part 3 — Senior](./java_part3_senior_rewritten_detailed.md)."""

NAV3 = """## Vị trí của Part 3 trong learning flow

Part 3 giả định bạn đã đọc [Java Part 2 — Intermediate](./java_part2_intermediate_rewritten_detailed.md). Mục tiêu là đưa kiến thức Java sang production: Java Memory Model sâu hơn, thread/executor saturation, JVM/JIT/GC, profiling, database/HTTP resource boundaries, API compatibility và incident debugging. Những internals quá thấp như AQS, VarHandle, agents, Class-File API và FFM được để cho [Java Master Supplement](./java_master_supplement_rewritten_detailed.md) để không làm hỏng learning flow."""

NAV4 = """## Vị trí của Master Supplement trong learning flow

Master Supplement chỉ nên đọc sau [Java Part 3 — Senior](./java_part3_senior_rewritten_detailed.md). Đây không phải “Part 3 nhưng nhiều API hơn”; nó là phần bù cho low-level runtime, framework/library engineering và modern JDK internals. Nếu một chủ đề application-level đã được giải thích đủ ở ba phần trước, file này không lặp lại chỉ để tăng số lượng nội dung."""

p1 = add_after_intro(P1.read_text(encoding="utf-8"), NAV1)
p2 = add_after_intro(P2.read_text(encoding="utf-8"), NAV2)
p3 = add_after_intro(P3.read_text(encoding="utf-8"), NAV3)
p4 = add_after_intro(P4.read_text(encoding="utf-8"), NAV4)

VERSION_BEGINNER = """# 74. Java 8 → 11 → 17 → 21: version thay đổi cách lập trình như thế nào?

Nếu chỉ học version bằng danh sách “release X thêm feature Y”, bạn rất nhanh quên. Cách hữu ích hơn là nhìn bốn generation như bốn lần **thay đổi phong cách viết và vận hành Java**.

**Java 8** là mốc đưa functional style thực dụng vào Java application code. Lambda, method reference và Stream không chỉ rút ngắn cú pháp; chúng biến *behavior* thành thứ có thể truyền vào API. Trước Java 8, một `Comparator`, callback hoặc `Runnable` thường được viết bằng anonymous class dài:

```java
Collections.sort(users,
    new Comparator<User>() {
        @Override
        public int compare(User a, User b) {
            return a.name().compareTo(b.name());
        }
    });
```

Java 8 cho phép diễn đạt intent trực tiếp hơn:

```java
users.sort(
    Comparator.comparing(User::name));
```

Stream API tiếp tục ý tưởng này cho data transformation, còn `java.time` thay đổi cách xử lý thời gian từ `Date`/`Calendar` mutable và dễ sai sang những type có semantic rõ như `LocalDate`, `Instant`, `Duration`. Vì rất nhiều enterprise code từng baseline Java 8 trong thời gian dài, bạn phải đọc được cả anonymous classes, `Date`/`Calendar` lẫn code hiện đại tương đương.

**Java 11** nên được hiểu như mốc Java hiện đại đầu tiên sau quá trình modular hóa JDK. Ở application code có các API nhỏ nhưng hữu ích như `String.isBlank()`, `strip()`, `lines()`, `Files.readString()` và standard `HttpClient`. Quan trọng hơn với enterprise migration là một số Java EE/CORBA modules như JAXB/JAX-WS không còn được bundle trong JDK. Một project Java 8 từng compile chỉ vì JAXB “có sẵn trong JDK” có thể fail khi lên 11 cho tới khi build khai báo dependency rõ. Từ đây bạn phải phân biệt **Java SE platform** với framework/library dependencies của application.

**Java 17** làm domain modeling và platform encapsulation mạnh hơn. Records giúp data carrier/value-like objects giảm boilerplate; sealed classes giúp mô hình một tập subtype đóng; pattern matching cho `instanceof` giảm cast ceremony. Quan trọng hơn ở production migration, JDK internals bị strong encapsulation theo default mạnh hơn trước. Framework/library cũ dùng deep reflection vào private internals của `java.*` có thể gặp `InaccessibleObjectException`, vì vậy code bền vững hơn phải dựa supported API thay vì internal implementation.

Trước records, một data carrier có thể cần constructor, accessors và equality boilerplate. Với Java 17, intent có thể được biểu diễn rõ hơn:

```java
record UserSummary(
    long id,
    String name) {
}
```

Ý nghĩa không chỉ là “record ngắn hơn class”, mà là language có một cách biểu diễn rõ ràng type chủ yếu được định nghĩa bởi dữ liệu của nó.

**Java 21** thay đổi hai hướng lớn. Hướng thứ nhất là data-oriented programming: record patterns và pattern matching for `switch` làm closed/sealed model dễ destructure và xử lý exhaustive hơn. Hướng thứ hai là concurrency: Virtual Threads được final. Với nhiều I/O-bound server workloads, bạn có thể giữ imperative blocking style mà scale số concurrent tasks cao hơn thay vì buộc application chuyển sang callback/reactive style chỉ để tiết kiệm OS threads.

```java
try (var executor =
        Executors.newVirtualThreadPerTaskExecutor()) {
    Future<Response> future =
        executor.submit(this::callRemoteService);
    return future.get();
}
```

Virtual thread không làm database, CPU hay external API nhanh hơn. Nó thay **cost model của thread**, không thay capacity của downstream resource. Phần Intermediate và Senior sẽ mở kỹ điểm này.

Các release 9, 10, 14, 15 và 16 vẫn quan trọng vì collection factories, `var`, switch expressions, text blocks, records và pattern matching đã hình thành Java hiện đại. Tuy nhiên hãy học chúng theo **vấn đề chúng loại bỏ** thay vì nhớ chronology. LTS cũng không có nghĩa feature “tốt hơn”; nó chủ yếu phản ánh support cadence phù hợp long-lived production."""

p1 = replace_numbered_section(p1, "Java Version Roadmap cần nhận biết", VERSION_BEGINNER)

THREAD_FOUNDATION = """## `Thread`: object Java và execution context khác nhau thế nào?

Trước khi học `synchronized`, executor hay virtual thread, cần hiểu `Thread` ở mức trực tiếp. Một `Thread` object biểu diễn một luồng thực thi có lifecycle. Tạo object chưa làm code chạy song song:

```java
Thread thread =
    new Thread(() -> doWork());
```

Chỉ khi gọi `thread.start()` JVM mới tạo/schedule execution mới và thread đó sau đó thực thi `run()`. Nếu gọi trực tiếp `thread.run()`, đó chỉ là một method call bình thường trên **thread hiện tại**; không có concurrency mới.

Bạn có thể chờ thread khác hoàn thành bằng `join()`. `join()` không chỉ “đợi cho xong”; việc thread kết thúc rồi thread khác join thành công còn tạo happens-before relationship, nên các effects trước khi thread kết thúc được thread join quan sát theo Java Memory Model.

`Thread.sleep(...)` chỉ tạm dừng thread hiện tại; nó không nhả monitor lock đang giữ và không phải primitive để chờ một condition. Nếu test hoặc production code dùng `sleep(100)` để “đợi task chắc chạy xong”, design đang phụ thuộc timing. Hãy dùng `join`, latch, `Future` hoặc condition phù hợp.

Platform thread có các trạng thái như `NEW`, `RUNNABLE`, `BLOCKED`, `WAITING`, `TIMED_WAITING`, `TERMINATED`. Trong production thread dump, state chỉ là đầu mối: một worker WAITING trên queue có thể hoàn toàn bình thường, còn hàng trăm threads BLOCKED trên cùng monitor mới là tín hiệu contention cần điều tra.

Daemon thread không giữ JVM sống khi tất cả non-daemon threads đã kết thúc. Background work quan trọng không nên dựa vào giả định “daemon thread sẽ còn kịp flush”. Durability phải đến từ explicit persistence và lifecycle.

Trong application production, bạn hiếm khi tự tạo một platform `Thread` cho từng task; `ExecutorService` quản lý lifecycle và capacity tốt hơn. Java 21 Virtual Threads lại làm thread-per-task style khả thi với cost model khác. Nhưng hiểu `Thread` vẫn bắt buộc để đọc stack trace, thread dump, interruption và framework execution."""

p2 = insert_after_numbered_section(p2, "Concurrency bắt đầu từ shared mutable state", THREAD_FOUNDATION)

LEGACY = """# 106. Legacy Java bạn sẽ gặp trong enterprise và cách hiện đại hóa mà không phá hệ thống

Legacy Java không đồng nghĩa “code xấu”. Nhiều hệ thống quan trọng được viết đúng với constraints của Java 6/7/8 và framework thời đó. Kỹ năng cần có là **đọc mental model cũ, nhận ra replacement hiện đại, rồi migrate có kiểm soát** thay vì rewrite theo style mới chỉ vì nhìn đẹp hơn.

Trong code Java 8 hoặc cũ hơn, bạn sẽ gặp anonymous classes ở những nơi code mới dùng lambda. Đổi sang lambda có thể giảm noise, nhưng đừng biến callback nhiều state/logic thành lambda 30 dòng chỉ để “modernize”. Named class đôi khi vẫn dễ đọc hơn.

Bạn cũng sẽ gặp `Date`, `Calendar` và `SimpleDateFormat`. `SimpleDateFormat` mutable và không thread-safe; static shared formatter trong server có thể race. Code mới nên dùng `java.time` và immutable `DateTimeFormatter`. Khi migrate, phải xác định semantic trước: `Date` cũ đang đại diện exact instant, local business date hay chỉ timestamp DB? Chuyển bừa sang `LocalDateTime` có thể làm mất timezone meaning.

Legacy collections có `Vector`, `Hashtable` và `Stack`. Chúng không “không dùng được”, nhưng synchronization semantics và API design thường không phải lựa chọn tốt cho code mới. `ArrayList`, `HashMap`/`ConcurrentHashMap`, `ArrayDeque` thường rõ hơn tùy requirement. Không thay `Hashtable` bằng `HashMap` chỉ vì mới hơn nếu old code thật sự dựa concurrent access; trước tiên phải xác định compound atomicity và ownership.

I/O legacy thường dùng `File`, `FileInputStream`, `FileReader` với platform default charset. Modern code nên ưu tiên `Path`/`Files` và charset explicit. Concurrency legacy có thể tạo raw `Thread`, dùng `wait/notify`, `Timer/TimerTask` hoặc synchronized collections; modern executors, `BlockingQueue`, scheduled executors và atomics thường dễ reason hơn, nhưng migration phải preserve protocol chứ không chỉ replace API names.

JDK 8 → 11 migration có một nhóm lỗi không nằm trong source style: JAXB/JAX-WS và Java EE/CORBA modules từng đi kèm JDK đã bị loại khỏi JDK 11. Code cũ có thể compile/run trên JDK 8 rồi báo missing class trên 11 cho tới khi dependencies được khai báo rõ trong build.

JDK 17 tạo compatibility boundary khác: strong encapsulation của JDK internals mạnh hơn. Library cũ dùng reflection vào private fields của `java.*` có thể fail. `--add-opens` có thể là temporary migration bridge, nhưng long-term fix là update library hoặc chuyển sang supported API.

Khi lên Java 21, Virtual Threads không có nghĩa phải rewrite executor architecture ngay. Trước hết đo workload: bottleneck là blocking platform threads hay DB pool/CPU? Virtual thread giảm cost chờ của Java threads, nhưng pool 30 database connections vẫn chỉ có 30 connections.

Cách migrate an toàn là tách **platform upgrade** khỏi **source modernization** khi có thể: chạy tests trên JDK mới, sửa dependencies/removed APIs, xử lý illegal reflection, đo GC/memory/latency baseline, rồi refactor từng vùng với tests. Hai mục tiêu có risk profile khác nhau."""

p2 = replace_numbered_section(p2, "Legacy APIs cần nhận biết", LEGACY)

PROFILING = """## Profiling production: chọn bằng chứng theo loại bottleneck

Profiling không phải mở một profiler rồi nhìn flame graph cho mọi vấn đề. Trước hết hãy phân loại symptom. Nếu CPU cao, CPU sampling/JFR là điểm bắt đầu tốt. Nếu CPU thấp nhưng latency cao, hãy nhìn thread states, socket/DB waits, connection-pool acquisition, lock contention và distributed trace. Nếu GC CPU/pause cao, cần allocation profile, live-set/heap occupancy và GC events. Nếu RSS tăng nhưng heap ổn, heap profiler một mình không đủ; phải xét direct buffers, thread stacks, metaspace và native memory.

Một workflow production có thể bắt đầu bằng metrics để xác nhận khi nào và phạm vi sự cố, sau đó JFR để xem JVM-level events, thread dump để xem execution đang chờ ở đâu, heap dump nếu cần retained-object analysis, và database/network tooling cho downstream. Không có tool duy nhất nhìn thấy toàn hệ thống.

CPU sampling trả lời “stack nào đang tiêu CPU theo thời gian”. Allocation profiling trả lời “code nào đang tạo nhiều object/bytes”. Lock profiling trả lời “thread nào đang chờ monitor/lock”. Khi nhìn flame graph, width biểu thị sample frequency/cost tương đối chứ không phải call count chính xác; hãy đọc từ stack root tới hot leaf và kiểm tra source/workload trước khi tối ưu.

Quan trọng nhất là luôn có **before/after measurement**. Nếu đổi data structure nhưng p99, CPU và allocation không cải thiện, đó không phải optimization có giá trị. Performance engineering là vòng lặp hypothesis → measurement → change → verification."""

p3 = insert_after_numbered_section(p3, "JFR", PROFILING)

VERSION_SENIOR = """## Java 8 → 11 → 17 → 21 dưới góc nhìn production engineer

Ở level Senior, version evolution không còn là câu chuyện syntax đẹp hơn. Mỗi mốc thay đổi assumptions của build, runtime hoặc concurrency model.

Java 8 đưa lambdas/streams/`java.time` vào mainstream, nhưng cũng là generation nơi rất nhiều enterprise frameworks dựa classpath, deep reflection và JDK-bundled Java EE APIs. “Java 8 application” thường mang assumptions mà source code không thể hiện rõ.

Java 11 buộc build trở nên explicit hơn. JAXB/JAX-WS và Java EE/CORBA modules không còn bundled trong JDK, standard HTTP Client xuất hiện và một số deployment assumptions cũ biến mất. Khi migration, dependency graph và packaging quan trọng ngang source compatibility. `ClassNotFoundException` sau upgrade có thể là platform component đã bị removed chứ không phải bug mới trong business code.

Java 17 làm encapsulation boundary cứng hơn. Strong encapsulation làm nhiều illegal reflective accesses trở thành lỗi thay vì warning. Đồng thời records, sealed classes và pattern matching giúp application model closed/value-centric concepts bằng type system thay vì conventions.

Java 21 thay đổi concurrency economics với Virtual Threads. High-concurrency blocking servers có thể giữ imperative style với rất nhiều lightweight threads, nhưng Senior vẫn phải đặt bulkhead tại database, HTTP client, rate limit và CPU. Thread không còn là scarce resource theo cùng cách; **downstream capacity vẫn scarce**. Pattern matching for `switch` và record patterns cũng làm sealed hierarchies hữu ích hơn vì compiler có thể check exhaustiveness.

Khi nâng version production, tách platform upgrade, dependency upgrade và source modernization khi có thể. Chạy tests trên target JDK, dùng `jdeps`/`jdeprscan`, kiểm tra removed/deprecated APIs, đo startup/heap/GC/JFR baseline, rồi mới quyết định dùng feature mới. Version upgrade thành công không chỉ là “compile được”; nó phải giữ correctness và SLO."""

p3 = insert_after_numbered_section(p3, "JDK Upgrade is Engineering Project", VERSION_SENIOR)

MASTER_COMPAT = """## Tại sao Master vẫn phải hiểu Java 8 → 11 → 17 → 21 thay vì chỉ nhìn Java 25/26

Master Supplement dùng Java 25/26 để giải thích platform mới, nhưng framework/library engineer thường phải support code được viết từ nhiều generation. Vì vậy bốn mốc 8, 11, 17 và 21 phải được xem như **compatibility boundaries**.

Java 8 là boundary nơi functional interfaces/default methods trở thành mainstream. Default methods đặc biệt quan trọng với library evolution: interface có thể thêm behavior mà không ngay lập tức phá mọi implementation cũ. Lambdas dựa target typing và `invokedynamic`, nên bytecode/runtime model khác anonymous class dù source intent có thể tương tự.

Java 11 là boundary của post-modular JDK distribution. Library từng dựa JAXB/JAX-WS “có trong JDK” phải khai dependency riêng; jlink/module ecosystem và standard HTTP client thay deployment assumptions. Nếu library claim support 8 và 11+, CI phải thật sự test multiple runtimes thay vì compile một lần rồi suy đoán.

Java 17 là boundary của strong encapsulation. Frameworks làm DI/ORM/serialization bằng reflection phải tách giữa reflection vào application classes — legitimate use case — và illegal access vào JDK internals. `--add-opens` là deployment escape hatch, không phải public API guarantee. Records/sealed types cũng tạo source models mới mà code generators/serializers cần hiểu.

Java 21 là boundary của concurrency model. Frameworks/executors/pools viết với assumption “mỗi request = expensive OS-backed platform thread” cần được xem lại khi virtual threads được dùng. Instrumentation, `ThreadLocal`, blocking detection, pool sizing và observability phải phân biệt platform với virtual threads.

Khi thiết kế library multi-release, hãy xác định **minimum supported Java**, **build JDK**, **test matrix**, **optional fast paths** và **public API type surface**. Đừng expose Java 21-only type trong public API của library claim Java 17 compatibility rồi cố giải bằng reflection. Nếu muốn implementation tối ưu theo runtime mới, Multi-Release JAR hoặc runtime feature detection có thể phù hợp nhưng làm test/packaging phức tạp hơn."""

p4 = insert_before_numbered_heading(p4, "Preview, Incubator, Experimental: đừng trộn", MASTER_COMPAT)

P1.write_text(p1, encoding="utf-8")
P2.write_text(p2, encoding="utf-8")
P3.write_text(p3, encoding="utf-8")
P4.write_text(p4, encoding="utf-8")

# Consolidate: canonical Beginner replaces the older parallel note.
old = BASE / "java_beginner_explained_with_senior_notes.md"
if old.exists():
    old.unlink()

# Coverage audit: intentionally checks the four canonical notes as one learning library.
combined = "\n".join(p.read_text(encoding="utf-8").lower() for p in FILES)
checks = {
    "syntax/control flow": ["switch", "loop"],
    "primitive/reference": ["primitive", "reference"],
    "oop": ["encapsulation", "inheritance", "polymorphism", "interface"],
    "generics/collections": ["generics", "collections"],
    "exceptions/io": ["exception", "nio"],
    "time/stream/lambda/optional": ["java.time", "stream", "lambda", "optional"],
    "reflection/annotation": ["reflection", "annotation"],
    "threads/concurrency": ["thread", "synchronized", "reentrantlock", "executorservice", "completablefuture"],
    "jvm/runtime": ["stack", "heap", "garbage collection", "class loading", "bytecode", "jit"],
    "production": ["profiling", "jfr", "performance"],
    "versions": ["java 8", "java 11", "java 17", "java 21"],
    "legacy": ["legacy java"],
}
missing = [name for name, terms in checks.items() if not all(term in combined for term in terms)]
if missing:
    raise SystemExit(f"Coverage audit failed: {missing}")

for p in FILES:
    data = p.read_text(encoding="utf-8")
    print(f"{p}: {len(data.splitlines())} lines, {len(data.split())} words")
print("Canonical Java audit passed; legacy duplicate removed.")
