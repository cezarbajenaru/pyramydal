# spreadsheetSJS
Create a platform for my fathers 100k excel line loading problem

```
   Browser (User)
   ───────────────────────────────
   | Django login page           |
   | Django-protected /spread/   |
   | SpreadJS (JS) inside page   |
   ───────────────────────────────
             |
             v
      Django (Backend)
   ────────────────────────────────
   | Authentication system         |
   | File manager backend          |
   | Versioning                   |
   | Permissions                   |
   | Serve Excel/JSON to SJS       |
   ────────────────────────────────
             |
             v
        Storage
   ───────────────────────────────
   | S3 Buckets / PostgreSQL      |
   | Folder structure             |
   | Version history              |
   ───────────────────────────────

```
