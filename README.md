```markdown
# NIST CSF two Governance Assessment Bot  
Version One

This project began as a vibe coded idea and turned into a fully containerized assessment engine built around the NIST Cybersecurity Framework two. It runs entirely inside Docker, has no external dependencies, and provides a clean one to five maturity scoring model through a browser interface.

It was created with a mix of structure and improvisation, focusing on fast iteration, clarity, and simplicity rather than heavy GRC architecture. Despite being vibe coded, the system is stable, modular and easy to expand.

## What this project does

Runs a full CSF two maturity assessment.  
Each NIST subcategory is presented as a clear statement.  
Users select a maturity score from one to five.

Generates structured scoring:  
Overall maturity  
Function level averages  
Subcategory level detail

Produces visual output with a bar chart summarizing each CSF function.

Zero local Python required.  
Everything runs inside Docker with SQLite stored in a Docker volume.

## Features

Covers all six CSF two functions:  
Govern  
Identify  
Protect  
Detect  
Respond  
Recover  

Maturity scale:  
1 = no controls  
2 = some controls  
3 = medium controls  
4 = developed controls  
5 = mature, measured controls  

Browser only workflow.

Clean modular architecture:  
Service layer  
NIST seed logic  
Templates  
Routes separated from logic  

## Quick start

```

docker compose build
docker compose up

```

Open in a browser:

```

[http://localhost:8000](http://localhost:8000)

```

## Project structure

```

app/
nist/
services/
templates/
static/
web/
config.py
db.py
models.py
entrypoint.sh
seed_db.py
Dockerfile
docker-compose.yml
requirements.txt

```

## Resetting the database

```

docker compose down
docker volume rm csf2bot_csf2_data
docker compose up

```

## Future enhancements

PDF export  
AI explanations  
Radar chart  
Editable templates  
Comment fields  
Authentication  
Excel export  

## Licensing

This project is released under the Unlicense.  
Free to use, modify and distribute without restriction.

## Notes

This was vibe coded for speed, clarity and simplicity.  
The structure remains clean and ready for practical use.
```
