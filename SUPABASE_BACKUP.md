# Supabase data backup

The repository now contains a private GitHub Actions backup workflow at `.github/workflows/backup-supabase.yml`.

It exports the public application tables below through Supabase REST, paginates safely, compresses the JSON, encrypts it with AES-256-CBC, and stores only the encrypted file as a private Actions artifact for 90 days:

- `learning_progress`
- `tasks`
- `goals`
- `public_shares`
- `english_task_progress`

The workflow does not export `auth.users` or passwords. Supabase-managed backups remain responsible for platform schemas and authentication data.

## Required GitHub Actions secrets

The existing frontend secrets are not sufficient for a full backup. Add these repository secrets:

- `SUPABASE_SECRET_KEY`: Supabase secret/publishable-management key with server-side data access. Never use `VITE_SUPABASE_ANON_KEY` here.
- `SUPABASE_BACKUP_PASSPHRASE`: a long random passphrase used to encrypt the artifact.

`VITE_SUPABASE_URL` is reused for the project URL. The backup workflow never prints secret values and never stores the plaintext JSON in the repository.

## Run and restore

After both secrets exist, run **Actions → Backup Supabase data → Run workflow** once to verify it. The workflow also runs weekly on Sunday at 18:17 UTC (Monday 03:17 Korea time).

Download the encrypted artifact from the completed workflow and decrypt it locally:

```bash
openssl enc -d -aes-256-cbc -pbkdf2 \
  -in supabase-backup.json.gz.enc \
  -out supabase-backup.json.gz
gunzip supabase-backup.json.gz
```

The resulting JSON is an application-data export. A restore should be performed deliberately with a migration-aware script; do not blindly replay it against production.
