# student-starter-template

A ready-to-code environment for learning Python/FastAPI, Vue, and PostgreSQL.

## Quickstart

Requires [Docker](https://docs.docker.com/get-docker/) and [VS Code](https://code.visualstudio.com/) with the **Dev Containers** extension.

1. Clone this repo and open the folder in VS Code.
2. When prompted, click **Reopen in Container** (or run `Dev Containers: Reopen in Container` from the command palette).
3. Wait for the container to build. On first run this takes a few minutes.

## What you get

- **Python 3.12** — for FastAPI backends
- **Node.js 22 + npm** — for Vue frontends
- **PostgreSQL 15** — running in its own container

## Connecting to the database

Inside the container:

```
psql $DATABASE_URL
```

Connection details:

| Field    | Value        |
|----------|--------------|
| Host     | `db`         |
| Port     | `5432`       |
| User     | `student`    |
| Password | `student`    |
| Database | `student_db` |

From your host machine (e.g. a GUI tool), use `localhost:5432`.

## Ports

- `8000` — FastAPI
- `5173` — Vite dev server (Vue)
- `5432` — PostgreSQL
