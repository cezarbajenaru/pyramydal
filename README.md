# pyramydal project
Create a platform for my fathers 100k excel line loading problem
The project is a Cloud-Native tool created around Python tooling.
The platform will bring
   instant spreadsheet rendering
   multi file management
   versioning
   S3 backup storage
   printable final output
   AWS infra
   API driven backend (Django + D)



Project Brief — Django + HTMX Data Platform
Goal

Build a cloud-native data platform to replace large Excel workflows (100k+ rows) with a database-first, server-rendered system focused on correctness, scalability, versioning, and printability.

Technology Choices
Application

Django as primary framework

Authentication (login/logout)

User management and permissions

Admin dashboard

ORM and migrations

CRUD views and forms

Server-side pagination, search, filters

HTMX for frontend interactivity

Partial page updates

Inline edits

Modals and actions without SPA complexity

Django REST Framework (selective use)

Import/export endpoints

Async or bulk operations

Infrastructure (Terraform / OpenTofu)

ALB – HTTP entrypoint

ECS Fargate – Django backend runtime

RDS PostgreSQL – authoritative data store

S3

Excel imports/exports

JSON snapshots

Backups

IAM roles – least-privilege access for services

High-Level Architecture
Browser (User)
```
────────────────────────────────────
│ Django login                     │
│ Server-rendered tables           │
│ HTMX interactions               │
│ Print views                      │
────────────────────────────────────
              │
              ▼
Django Backend
────────────────────────────────────
│ Authentication & permissions     │
│ Dataset and row management       │
│ Versioning                       │
│ Import / export (Excel, CSV)     │
│ Audit & metadata APIs            │
────────────────────────────────────
              │
              ▼
Data & Storage
────────────────────────────────────
│ PostgreSQL (source of truth)     │
│ S3 (imports, exports, snapshots)│
│ Version history                  │
────────────────────────────────────
```
```
Repository Structure
factory-spreadsheet-platform/
│
├── backend/
│   ├── factoryspread/            # Django project
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   ├── spreadsheet/              # Core app
│   │   ├── models.py             # Dataset, rows, versions
│   │   ├── views.py              # HTML + HTMX views
│   │   ├── urls.py
│   │   ├── admin.py
│   │   ├── serializers.py        # DRF (imports/exports)
│   │   ├── api.py
│   │   ├── templates/
│   │   │   └── spreadsheet/
│   │   └── static/
│   │       └── spreadsheet/
│   │           └── htmx.js
│   │
│   ├── Dockerfile
│   ├── requirements.txt
│   └── manage.py
│
├── infra/
│   ├── tofu/
│   │   ├── modules/
│   │   └── envs/
│   └── docker-compose.yml        # local dev
│
├── .github/workflows/
│   └── deploy.yml
│
├── docs/
│   ├── architecture.md
│   ├── mvp-plan.md
│   └── roadmap.md
│
├── LICENSE
└── README.md
```
Delivery Plan
Sprint 1 — Core Platform

Initialize Django project

Authentication and protected routes

Dataset and row models

Admin CRUD

Server-rendered table view

HTMX pagination and edits

Initial print view

Sprint 2 — Data I/O

Excel import → database

Database → CSV / Excel export

Version snapshots

Search and filtering

Optional S3 integration

Sprint 3 — Scale & Deploy

Large-dataset pagination strategy

Indexing and performance tuning

Role-based access

Documentation

Deploy to ECS Fargate

Sprint 4 — Enterprise Features

Folder structure

File locking

Version comparison

Audit logs

Bulk operations

Multi-department isolation

Sprint 5 — Output & Reporting

Print-optimized views

PDF export

Styled Excel exports

Positioning

This project demonstrates:

Backend-owned data systems

Cloud-native architecture

Infrastructure as code

Operational safety and scalability

It is a platform engineering project, not a frontend showcase.