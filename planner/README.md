# Study Planner archive

`planner/` is a supporting archive, not an active application checkout. The
current repository keeps historical study-plan exports and demo artifacts under
[`stuty-planner-data/`](./stuty-planner-data/); the folder name is preserved for
backward compatibility.

The active Study Planner application and Supabase project live outside this
repository. `learning-library/` may still reference that external project for
optional progress sync, but this archive is not a runtime dependency for local
reading or publication.

Do not add new application code here. When an archived plan is reused, record
the source file and migration/date in the consuming project before importing it.
