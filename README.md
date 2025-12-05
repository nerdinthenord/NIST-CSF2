# NIST CSF two Governance Assessment Bot

V1

This project is a containerized web application that delivers an enterprise grade NIST Cybersecurity Framework two governance and program maturity assessment. It is designed for internal security teams, consultants and organizations that want a fast way to collect structured maturity data across all CSF functions using a simple one to five scale.

The entire project runs inside Docker with no system level Python or virtual environments required. All user input happens on the web UI and results are generated instantly with visual charts for reporting.

---

## Features

**Full CSF two covered**
All six functions are included: Govern, Identify, Protect, Detect, Respond, Recover.
Each NIST subcategory is represented as one maturity question.

**Simple one to five scoring scale**
One represents no controls and five represents mature and measurable controls.
The scale aligns to common enterprise maturity models.

**Web interface only**
The assessment is completed entirely in the browser.
No command line interaction required by end users.

**Instant scoring**
Overall maturity
Function level maturity
Subcategory detail
Generated immediately on submission.

**Visual dashboard**
A bar chart shows the maturity of each CSF function.

**Zero local setup**
The application is fully isolated in a Docker container.
SQLite runs inside a named Docker volume.
Rebuilding or upgrading is trivial and leaves data untouched unless you remove the volume.

---

## Project structure

```
app/
  nist/
    seed_data.py         Seeds NIST CSF two subcategories and template
  services/
    assessment_service.py   Scoring logic and answer handling
  templates/
    base.html
    index.html
    assessment_run.html
    results.html
  web/
    router_views.py      Web routes for assessment workflow
  static/
    main.css
  config.py
  db.py
  models.py
entrypoint.sh
requirements.txt
Dockerfile
docker-compose.yml
seed_db.py
```

---

## How it works

**Start a new assessment**
User enters organization name and optional assessor name.

**Answer the questions**
Each row corresponds to a unique CSF subcategory.
Users rate the maturity of the statement from one to five.

**Submit**
Backend collects answers and builds a full maturity profile.

**Results page**
Shows overall maturity
Shows function level scores
Shows subcategory detail
Shows visual bar chart with Chart.js

---

## Technology stack

**FastAPI** for the backend
**Jinja2** for server side HTML templates
**SQLite** stored in a Docker volume
**Chart.js** for the function level bar chart
**Uvicorn** as the ASGI web server
**Docker** for fully isolated execution

---

## Running the application

Inside your project folder:

```
docker compose build
docker compose up
```

Open the interface in your browser:

```
http://localhost:8000
```

---

## Resetting the database if you want fresh questions

The SQLite database lives in a volume named `csf2bot_csf2_data`.
Remove it to trigger a clean reseed:

```
docker compose down
docker volume rm csf2bot_csf2_data
docker compose up
```

---

## Extending the project

This is Version One. The architecture is intentionally modular for expansion. Suggested future enhancements include:

**PDF export** of the full report with charts and recommendations
**AI explaining mode** on each question
**Qualitative comment fields** per subcategory
**Multiple templates** such as governance only, program only or supply chain focussed
**Radar chart view** for executive reporting
**Authentication and multi user mode** for enterprise deployment
**Batch export** to Excel for cross team reviews

---

## Purpose and intent

The goal of this tool is to give organizations a fast, structured and repeatable way to self evaluate their cybersecurity maturity using NIST CSF two. It is targeted for use by internal audit teams, security architects, risk managers and operational leadership.

This is not a compliance certification mechanism. It is a structured assessment tool that produces consistent maturity scoring aligned to the NIST framework.

