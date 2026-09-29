# Supabase dữ liệu (data / 데이터) backup

The repository now contains a private GitHub Actions backup workflow at `.github/workflows/backup-supabase.yml`.

It exports the công khai (public / 공개) ứng dụng (application / 애플리케이션) tables below through Supabase REST, paginates safely, compresses the JSON, encrypts it with AES-256-CBC, and stores only the encrypted tệp (file / 파일) as a private Actions sản phẩm tạo ra (artifact / 산출물) for 90 days:

- `learning_progress`
- `tasks`
- `goals`
- `public_shares`
- `english_task_progress`

The workflow does not export `auth.users` or passwords. Supabase-managed backups remain responsible for nền tảng (platform / 플랫폼) schemas and authentication dữ liệu (data / 데이터).

## Required GitHub Actions secrets

The existing frontend secrets are not sufficient for a full backup. Add these repository secrets:

- `SUPABASE_SECRET_KEY`: Supabase secret/publishable-management key with server-side dữ liệu (data / 데이터) truy cập (access / 접근). Never use `VITE_SUPABASE_ANON_KEY` here.
- `SUPABASE_BACKUP_PASSPHRASE`: a long random passphrase used to encrypt the sản phẩm tạo ra (artifact / 산출물).

`VITE_SUPABASE_URL` is reused for the dự án (project / 프로젝트) URL. The backup workflow never prints secret values and never stores the plaintext JSON in the repository.

## Run and restore

After both secrets exist, run **Actions → Backup Supabase dữ liệu (data / 데이터) → Run workflow** once to verify it. The workflow also runs weekly on Sunday at 18:17 UTC (Monday 03:17 Korea time).

Download the encrypted sản phẩm tạo ra (artifact / 산출물) from the completed workflow and decrypt it locally:

```bash
openssl enc -d -aes-256-cbc -pbkdf2 \
  -in supabase-backup.json.gz.enc \
  -out supabase-backup.json.gz
gunzip supabase-backup.json.gz
```

The resulting JSON is an application-data export. A restore should be performed deliberately with a migration-aware script; do not blindly replay it against môi trường vận hành (production / 운영 환경).
