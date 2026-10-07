# AI WORKFLOW INDEX

Đây là bản đồ điều phối cho việc tạo, review và tích hợp learning docs khi có nhiều chat, worktree hoặc agent surface.

## Contract

- [00_ORCHESTRATOR_PROMPT.md](prompt/00_ORCHESTRATOR_PROMPT.md): chọn mode và evidence gate.
- [COMMON_PROMPT.md](prompt/COMMON_PROMPT.md): contract chất lượng learning docs hiện có.
- [DOCS_AUDIT_PROMPT.md](prompt/DOCS_AUDIT_PROMPT.md): audit bản nháp theo source, reasoning và prose.
- [DOCS_REVIEW_PROMPT.md](prompt/DOCS_REVIEW_PROMPT.md): review sau learner/user feedback cụ thể.
- [SOURCE_INGESTION_CONTRACT.md](prompt/SOURCE_INGESTION_CONTRACT.md): raw, provenance và derived Markdown.
- [ACCEPTANCE_CONTRACT.md](prompt/ACCEPTANCE_CONTRACT.md): content, evidence, Git và publication status.
- [CROSS_TOOL_AGENT_CONTRACT.md](prompt/CROSS_TOOL_AGENT_CONTRACT.md): quyền và handoff giữa Codex, Daintree, Antigravity và ChatGPT Web.

## Skills

- [learning-doc-intake](skills/learning-doc-intake/SKILL.md)
- [semantic-source-map](skills/semantic-source-map/SKILL.md)
- [docs-self-review](skills/docs-self-review/SKILL.md)
- [learner-feedback-triage](skills/learner-feedback-triage/SKILL.md)
- [source-generated-integrity](skills/source-generated-integrity/SKILL.md)
- [scope-claim](skills/scope-claim/SKILL.md)
- [agent-surface-dispatch](skills/agent-surface-dispatch/SKILL.md)
- [cross-tool-handoff](skills/cross-tool-handoff/SKILL.md)
- [acceptance-gate](skills/acceptance-gate/SKILL.md)

## Workflows

- [source-to-learning-docs](workflows/source-to-learning-docs.md)
- [parallel-agent-run](workflows/parallel-agent-run.md)
- [feedback-to-delta](workflows/feedback-to-delta.md)
- [source-generated-update](workflows/source-generated-update.md)
- [daintree-fleet-run](workflows/daintree-fleet-run.md)
- [acceptance-and-integration](workflows/acceptance-and-integration.md)

## Templates

See templates/ for task, source, handoff, semantic-map, source-ledger, reader-packet, feedback, outline, pilot, dependency, scope-claim, dispatch and acceptance artifacts.
