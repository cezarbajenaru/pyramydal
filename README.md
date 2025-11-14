# spreadsheetSJS
Create a platform for my fathers 100k excel line loading problem
The project is a Cloud-Native tool created around Python tooling.
The platform will bring
   instant spreadsheet rendering
   multi file management
   versioning
   S3 backup storage
   printable final output
   AWS infra
   API driven backend (Django + D



Django will be used as a framwork for this project
   Solves the login issue - complete admin dashboard - User management - Permissions - Authentication -> Login/Logout pages
   Crud Pages(create,read,update,delete)
   Tables/ views for any model
   Forms for editing data
   Search, filters
   ORM built in
   Easy to connect to SpreadJS frontend
   Easy REST API with Django Rest framework

Terraform for infrastructure(Tofu)

   ALB = load balancing
   S3 = stores Excel + JSON + SpreadJS assets - FRONTEND

   ECS Fargate = production Django BACKEND
   RDS PostgreSQL = metadata, file info
   S3 BUCKET = Excel + json file storage
   
   IAM roles = secure access
   
   
```

Browser (User)
────────────────────────────────────
│ Django login page                │
│ Django-protected /spread/ route  │
│ SpreadJS frontend UI             │
────────────────────────────────────
              │
              ▼
Django Backend
────────────────────────────────────
│ Authentication                   │
│ File manager API                 │
│ Versioning                       │
│ Permissions / Roles              │
│ Excel/JSON transformations       │
│ REST API via DRF                 │
────────────────────────────────────
              │
              ▼
Cloud Storage / Database
────────────────────────────────────
│ S3 Buckets (excel + json)        │
│ PostgreSQL (metadata)            │
│ Folder structure                 │
│ Version history                  │
────────────────────────────────────


```

Wannabe Github repo structure
```
factoryspread/ → project config

spreadsheet/ → main logic

models.py → file metadata & versions

api_views.py → REST API

spreadsheet.html → page containing SpreadJS

static/js/ → SpreadJS init + API calls

factory-spreadsheet-platform/
│
├── backend/
│   ├── factoryspread/          # Django project
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   │
│   ├── spreadsheet/            # Main app
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── admin.py
│   │   ├── serializers.py
│   │   ├── api_views.py        # DRF endpoints
│   │   ├── templates/
│   │   │   └── spreadsheet.html
│   │   └── static/
│   │       └── js/
│   │           ├── spread-init.js
│   │           └── api-client.js
│   │
│   ├── requirements.txt
│   ├── Dockerfile
│   └── manage.py
│
├── frontend/
│   └── spreadjs/               # SpreadJS library + custom JS
│       ├── gc.spread.sheets.all.min.js
│       └── styles/
│
├── infrastructure/
│   ├── docker-compose.yaml
│   ├── aws/
│   │   ├── terraform/
│   │   └── cloudformation/
│   └── nginx/
│       └── nginx.conf
│
├── docs/
│   ├── architecture-diagram.png
│   ├── mvp-plan.md
│   └── roadmap.md
│
├── .github/
│   └── workflows/
│       └── deploy.yml          # CI/CD pipeline
│
├── LICENSE
└── README.md


```
The task order:

Sprint 1:
Backend:
Initialize Django project
Add /spread/ page
Add login system
Add file metadata model
Add admin panel entries
Add endpoint: /api/file/<id>/load/
Add endpoint: /api/file/<id>/save/

Frontend:
Embed SpreadJS in template
Load sample JSON
Basic toolbar (save, open, print)

Sprint 2:
Add Excel import → JSON converter
Add JSON → Excel export
Connect to database
Implement S3 storage (optional in MVP)
Add file list sidebar
Add “Save As New Version”
Add printing integration
Add search/filtering

Sprint 3:
Add pagination for large files
Add color-coded rows
Add metadata sidebar fields
Add basic user roles
Add documentation
Deploy to EC2 or Elastic Beanstalk

Sprint 4:
Directory manager
Folder structure
Multiple spreadsheets open at once
Drag-and-drop file organization
Permissions per file
File locking
Version comparison
Audit logs
Notifications
Bulk import of files
Multi-department setup

Sprint 5:
Possibility to print the resulted page
Export as PDF or Excel
