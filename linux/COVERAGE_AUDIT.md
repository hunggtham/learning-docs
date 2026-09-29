# Linux — Coverage Audit

**Audit date:** 2026-09-29  
**Canonical root:** `linux/`  
**Entrypoint:** [`README.md`](./README.md)

## 1. Canonical ownership

`linux/` owns the host/runtime operating-system layer used by development and production systems: kernel/userspace boundaries, filesystems, processes, identity/permissions, shell, systemd, logging, time, CPU/memory/storage, networking, package/deployment mechanics, security controls, tracing, containers and production troubleshooting.

It should explain mechanisms and observable system state rather than become a command cheat sheet.

Adjacent owners:

- OS theory, algorithms and distributed systems → [`../computer_science/`](../computer_science/README.md);
- backend application contracts → [`../10_backend/`](../10_backend/README.md);
- container orchestration, delivery, SRE and platform engineering → [`../devops_platform_engineering/`](../devops_platform_engineering/README.md).

## 2. Coverage currently strong

The current README exposes a dependency graph rather than a flat list. Strong areas include:

- kernel/userspace/system-call boundary;
- `/proc`, `/sys`, device/kernel interfaces;
- filesystem/inode/VFS/page-cache/writeback/crash-consistency concepts;
- processes, threads, signals and IPC;
- shell pipelines and reliable Bash scripting;
- credentials, ACL, capabilities, MAC and seccomp;
- boot/initramfs/systemd/service dependencies;
- journald/rsyslog/log pipelines and time synchronization;
- storage, virtual memory, reclaim, OOM, scheduling and I/O performance;
- routing/NAT/conntrack/DNS/TCP/TLS/reverse proxy;
- tracing with `strace`, `perf` and eBPF;
- namespaces/cgroups/capabilities/seccomp and containers;
- deployment, backup/restore, incident reasoning and SRE connections.

This is substantially deeper than an administration-command library and already supports production reasoning.

## 3. Invariants for future chapters

Every substantial Linux topic should make the following chain explicit where applicable:

```text
resource/object
→ kernel state
→ user-space interface
→ accounting/limits
→ observable evidence
→ failure mode
→ recovery/change action
```

A command is evidence or an actuator, not the concept itself.

For example:

```text
memory pressure
≠ free output

memory pressure
→ working sets + page cache + reclaim + cgroup limits + PSI
→ observable counters/events
→ latency/OOM consequences
```

## 4. Boundaries to preserve

### Linux networking vs network theory

Linux may own sockets, routing tables, namespaces, conntrack, packet path observability and host-level TCP behavior. Protocol design and distributed-system theory remain in Computer Science.

### Linux containers vs orchestration

Linux owns namespace/cgroup/capability/seccomp mechanics. Kubernetes scheduling, controllers, GitOps and cluster operations remain DevOps/Platform Engineering.

### Linux troubleshooting vs application debugging

Linux owns host/process/resource evidence. Application transaction semantics and business invariants remain Backend or the relevant application domain.

### Security controls vs security architecture

Linux may explain kernel/user-space enforcement mechanisms and local privilege boundaries. Threat modeling, identity architecture and cross-system control/evidence chains remain Computer Science Security.

## 5. Gaps / next depth

### P1 — Unified resource-pressure route

Create a connection route that follows one overloaded service through:

```text
traffic increase
→ socket/backlog
→ process/thread/event-loop pressure
→ CPU scheduling
→ memory/page cache/reclaim
→ storage/network I/O
→ cgroup limits
→ latency/errors
→ evidence and recovery
```

This would connect existing deep dives without duplicating them.

### P1 — Filesystem/database durability boundary

Strengthen the cross-domain explanation of:

- application write;
- userspace buffering;
- page cache;
- filesystem journal;
- block layer/device cache;
- `fsync`/barriers;
- what a database commit can and cannot assume.

Linux should explain the OS/storage side and link to database owners for WAL/transaction semantics.

### P1 — cgroup v2 operational accounting

Consolidate CPU, memory, I/O and PID limits around cgroup v2 as a single resource-governance model, including how host-level and container-level observations can disagree.

### P2 — Network namespace packet-path evidence

Add a reusable packet-path troubleshooting model:

```text
process/socket
→ namespace/interface
→ route
→ firewall/NAT/conntrack
→ physical/virtual interface
→ remote path
```

The goal is evidence localization, not command memorization.

### P2 — eBPF safety and interpretation boundary

Explain when eBPF adds useful evidence, when lower-cost tools are sufficient, and how instrumentation overhead/sampling/aggregation can mislead diagnosis.

### P2 — Package/runtime provenance

Strengthen the chain from package/repository/signature to installed files, dynamic libraries, service executable and running process. This should connect supply-chain reasoning to actual host evidence.

### P2 — Recovery-state verification

After restart, rollback, restore or failover, teach verification of:

- process/service state;
- mounted storage;
- clocks/time sync;
- network bindings/routes;
- resource limits;
- logs/journal continuity;
- application-facing health.

Recovery is not complete merely because the service process is running.

## 6. Version/time sensitivity

Linux mechanisms are relatively durable, but commands, defaults, kernel features, systemd behavior and distribution packaging can change.

When a chapter makes a version-sensitive claim, record enough context to distinguish:

- kernel behavior;
- systemd behavior;
- distribution-specific packaging/defaults;
- container-runtime behavior;
- tool-version behavior.

Avoid presenting one distro's default as a universal Linux invariant.

## 7. Review protocol

For major Linux additions:

```text
concept owner
→ kernel/userspace boundary
→ resource/accounting model
→ observable evidence
→ failure mode
→ change/recovery semantics
→ version/distro sensitivity
→ links to Backend/DevOps/Computer Science
```

Reject additions that are only lists of commands without explaining system state and interpretation.

## 8. Current assessment

**Conceptual breadth: very strong.**  
**Kernel/resource depth: strong.**  
**Production troubleshooting coverage: strong.**  
**Cross-resource overload reasoning: partial.**  
**cgroup v2 as unified accounting model: can be stronger.**  
**Durability boundary with databases: can be stronger.**  
**Version/distro sensitivity governance: should be made explicit in future updates.**

The highest-value next work is integration across existing deep dives, not adding more isolated command chapters.