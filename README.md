# NIST CSF two Governance Assessment Bot

Version One

This project began as a vibe coded idea and evolved into a fully containerized assessment engine built around the NIST Cybersecurity Framework two. It runs entirely inside Docker, has no external dependencies, and provides a clean one to five maturity scoring model through a browser interface.

It blends structure with improvisation, prioritizing speed and simplicity while still maintaining a clear, modular architecture.

## What this project does

Runs a complete CSF two maturity assessment.
Each NIST subcategory is presented as a clear, plain language statement.
Users select a maturity score from one to five.

Produces structured scoring:

* Overall maturity
* Function level averages
* Subcategory level detail

Displays a bar chart summarizing each CSF function.

Everything runs inside Docker with SQLite stored in a Docker volume.
No local Python or virtual environments required.

## Features

Covers all six CSF two functions:

* Govern
* Identify
* Protect
* Detect
* Respond
* Recover

Maturity scale:

* 1 = no controls
* 2 = some controls
* 3 = medium controls
* 4 = developed controls
* 5 = mature, measured controls

Browser only workflow.
Clean modular layout with clear separation of routes, logic, templates and seed data.

## Quick start

Run in the project folder:

```
docker compose build
docker compose up
```

Open in a browser:

```
http://localhost:8000
```

## Project structure

Directory layout:

app
 nist
 services
 templates
 static
 web
 config.py
 db.py
 models.py

entrypoint.sh
seed_db.py
Dockerfile
docker-compose.yml
requirements.txt

## Resetting the database

To recreate a clean database with fresh seed data:

```
docker compose down
docker volume rm csf2bot_csf2_data
docker compose up
```

## Future enhancements

* PDF export
* AI explanations for each subcategory
* Radar chart for executive reporting
* Editable template definitions
* Comment fields
* Authentication
* Excel export

## Licensing

This project is released under the Unlicense.
It is free to use, modify and distribute without restriction.

## Notes

This tool was vibe coded for speed and clarity.
Despite the improvisational start, the structure is clean, maintainable and immediately usable for internal or consulting assessments.
