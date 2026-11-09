# StudyFlow: Technical Review and Development Plan

**Project:** StudyFlow Flask + React API  
**Repository:** https://github.com/Mairaelefante/studyflow-flask-react-api  
**Report date:** 2026-11-09  
**Status:** Existing personal full-stack prototype. All roadmap features below are **proposed future work**, not completed changes.

## 1. Purpose

StudyFlow is a local task-management prototype intended for managing personal study tasks and technical practice. It combines a Python Flask REST API with a React frontend using Vite. This review is based on inspection of repository files, **not on running the application or an automated security scan**.

## 2. Existing code and behavior

- `studyflow-flask-react-api/backend/app.py` exposes GET and POST `/api/tasks`, plus PATCH and DELETE `/api/tasks/<id>`.
- The backend initializes two sample tasks, holds data in an in-memory list, and generates sequential task IDs.
- POST rejects empty task titles; PATCH updates title and/or completion status; DELETE removes an existing task.
- `studyflow-flask-react-api/frontend/src/App.jsx` displays tasks, adds new tasks, toggles completion, and deletes tasks through fetch requests.
- `studyflow-flask-react-api/frontend/src/styles.css` provides minimal layout and styling.
- `studyflow-flask-react-api/frontend/package.json` defines Vite dev/build/preview commands and React dependencies.

There is no evidence in the reviewed files of a persistent database, user accounts, automated tests, deployments, or analytics features. Do not present them as existing functionality.

## 3. Technical observations

### Persistence
Task state is process-local and resets on backend restart. Replace it with a small SQLite database with explicit schema and migrations.

### Validation and error handling
POST checks non-empty titles, but PATCH permits empty titles; both endpoints assume certain payload shapes. Introduce consistent request validation and error messages. The frontend currently handles POST errors only in a limited way; expand network, server, and loading-state handling.

### Frontend configuration
The API address is hard-coded to `http://localhost:5000/api/tasks`. Introduce environment-based configuration, with a documented local default and a safe deployment strategy.

### Testing and reproducibility
Add Flask API tests and React component-level tests, with repeatable setup commands. Document expected behaviors, including invalid payloads, missing IDs, empty task lists, and backend outages.

### Security and privacy
Flask starts with `debug=True` in the local entry point. Keep the development-only behavior distinct from deployment settings. Limit CORS appropriately if deployment is added. Do not store real sensitive or regulated data in test fixtures.

## 4. Proposed roadmap: at least 20 hours of future work

Estimates are provisional and should only be represented as planned work if the owner genuinely intends to implement them.

| Workstream | Planned deliverable | Estimated hours |
| --- | --- | ---: |
| Persistence | SQLite data model, repository layer, migrations and restart-persistence checks | 6 |
| API quality | Request validation, consistent error responses, status codes, edge cases | 4 |
| Study planning | Priority and due-date fields, sorting and filtering | 5 |
| Frontend robustness | Loading/error/empty states, API configuration, responsive UI and basic accessibility | 4 |
| Automated tests | Backend endpoint tests, frontend interaction tests, run instructions | 5 |
| Documentation and CI | Setup guide, sample fixtures, lint/test automation and contributor notes | 3 |
| **Total** | | **27 hours** |

These 27 hours are **estimates of proposed future development**, not logged effort, paid time, or evidence of project usage.

## 5. Acceptance criteria

1. Tasks remain available after a backend restart when persistence work is complete.
2. Empty or malformed POST/PATCH payloads produce consistent, documented 4xx responses.
3. Users can set task priority and deadline, and filter or order the displayed tasks.
4. The interface reports API failures without silently dropping actions.
5. Tests can run from a clean checkout with documented commands.
6. CI executes the specified checks and reports meaningful failures.
7. No real personal records, API keys, or credentials are added to the repository.

## 6. Submission readiness

- Public GitHub repository: verified during review.
- Historical commits: preserve as-is; do not squash or replace original history.
- MIT license: added at repository root.
- README: expanded with truthful current scope and run instructions.
- Development plan: the proposed 27-hour roadmap is documented here.
- Ownership: repository is in an individual account, but legal ownership/third-party claims must be confirmed by the owner before signing contributor terms.
- Secret scanning: a complete source/history scan has **not** yet been carried out.
- Execution verification: no backend or frontend installation/run was performed in this review.

The application should remain a personal software project, not work commissioned by an employer, client, or university. Further coding work should be done in ordinary, verifiable commits.
