# Version control, build, linking và package dependency

Source code không trực tiếp trở thành deployable system. Reproducible development cần history, dependency graph, compilation/transformation, linking, packaging và artifact identity. Git, build tools và package managers giải các parts khác nhau của pipeline.

## Version control as history graph

Git model stores content-addressed objects: blobs, trees, commits. Commit points to tree snapshot + parent(s) + metadata. Branch is movable reference to commit; merge commit can have multiple parents.

History therefore is DAG, not folders of diffs. Diff is computed between snapshots/trees. Understanding this explains why rebase creates new commits (new parents → new hashes) rather than “moves same commit”.

## Content addressing

Object identifier derives from content/metadata format hash. Same content can be deduplicated. Hash identity helps integrity but Git hash semantics/version depend implementation era; don't treat commit IDs as arbitrary crypto authentication without signed trust context.

## Build system

Build system models dependency graph from sources to outputs. It should rebuild artifact when inputs/commands/environment affecting result change.

Make uses timestamps/rules; modern systems may use explicit dependency graph, content hashes and remote cache. Incremental build reuses unchanged outputs.

Undeclared dependency creates non-reproducible “works on my machine” behavior because build result depends hidden state.

## Compilation and linking

Compiled languages may go source → object files → linker → executable/library. Linker resolves symbols and relocations. Static link embeds code; dynamic link resolves shared libraries at load/runtime.

Managed ecosystems package bytecode/classes and runtime resolves modules/dependencies differently, but same concept: names/references must resolve to compatible artifacts.

## Package manager

Package manager solves dependency resolution, version constraints, downloading, integrity and installation layout. Dependency graph can contain diamond conflicts: A needs C v1, B needs C v2. Ecosystems handle by single resolution, multiple versions, shading/isolation or failure.

Lockfile records exact resolved versions/checksums to improve reproducibility. Version range without lock means same manifest may install different dependency later.

## Semantic and binary compatibility

Upgrade can compile but fail runtime due semantic changes; native library may break ABI; Java library may preserve binary linkage but behavior changes. Compatibility has source, binary, behavioral and data-format dimensions.

## Reproducible builds

Same declared inputs should create bit-for-bit identical artifact. Hidden timestamps, filesystem ordering, locale, dependency fetching and compiler versions can break. Reproducibility improves supply-chain verification and debugging.

## CI/CD pipeline

CI automates build/test/static checks on controlled environment. CD packages and promotes artifacts. Best practice is build once, promote same immutable artifact through environments; rebuilding at production can change dependencies/toolchain.

## Supply-chain security

Dependencies/build scripts execute code with developer/CI privileges. Pin/verify artifacts, protect publishing credentials, review transitive dependencies, sign/provenance artifacts and minimize untrusted build steps.

## Mental Model

> Source repository is a **graph of versions**; build is a **graph transformation** from declared inputs to immutable artifacts; package manager is a **dependency solver + artifact fetcher**. Reproducibility requires no hidden inputs.

## Common Misconceptions

**“Git commit is a diff.”** Commit references a snapshot tree and parent; diff is derived.

**“package-lock only for dependency install speed.”** It primarily fixes exact dependency graph/integrity for repeatability.

**“CI passing means deploy artifact identical everywhere.”** Only if artifact is preserved/promoted and environment contracts controlled.

## Kết nối

[Graph theory](../01_algorithms_data_structures/06_graphs_and_graph_algorithms.md) explains dependency DAGs; [compiler/linker](../04_programming_languages/03_compilers_interpreters_vm_and_jit.md) supplies transformation; [security vulnerabilities](../07_security_reliability/03_software_vulnerabilities.md) covers supply-chain risk.
