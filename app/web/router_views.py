from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from ..db import get_db
from ..models import AssessmentTemplate, AssessmentRun, AssessmentQuestion
from ..services.assessment_service import (
    start_assessment_run,
    save_answers,
    calculate_scores,
)

router = APIRouter()


@router.get("/")
def index(request: Request, db: Session = Depends(get_db)):
    template = (
        db.query(AssessmentTemplate)
        .filter_by(name="Enterprise CSF 2 Governance Assessment")
        .first()
    )
    return request.app.state.templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "template": template,
        },
    )


@router.post("/start")
def start(
    request: Request,
    organization_name: str = Form(...),
    created_by: str = Form("anonymous"),
    db: Session = Depends(get_db),
):
    template = (
        db.query(AssessmentTemplate)
        .filter_by(name="Enterprise CSF 2 Governance Assessment")
        .first()
    )
    run = start_assessment_run(db, template.id, organization_name, created_by)
    return RedirectResponse(
        url=f"/run/{run.id}",
        status_code=303,
    )


@router.get("/run/{run_id}")
def run_view(run_id: int, request: Request, db: Session = Depends(get_db)):
    run = db.query(AssessmentRun).filter_by(id=run_id).first()
    if not run:
        return RedirectResponse("/", status_code=302)

    questions = (
        db.query(AssessmentQuestion)
        .filter_by(template_id=run.template_id)
        .order_by(AssessmentQuestion.id)
        .all()
    )

    return request.app.state.templates.TemplateResponse(
        "assessment_run.html",
        {
            "request": request,
            "run": run,
            "questions": questions,
        },
    )


@router.post("/run/{run_id}")
async def submit_run(
    run_id: int,
    request: Request,
    db: Session = Depends(get_db),
):
    form = await request.form()
    answers_payload = []
    for key, value in form.items():
        if not key.startswith("q_"):
            continue
        q_id = int(key.split("_", 1)[1])
        if not value:
            continue
        numeric = float(value)
        answers_payload.append(
            {"question_id": q_id, "numeric_value": numeric}
        )

    if answers_payload:
        save_answers(db, run_id, answers_payload)

    return RedirectResponse(
        url=f"/run/{run_id}/results",
        status_code=303,
    )


@router.get("/run/{run_id}/results")
def results(run_id: int, request: Request, db: Session = Depends(get_db)):
    scores = calculate_scores(db, run_id)
    return request.app.state.templates.TemplateResponse(
        "results.html",
        {
            "request": request,
            "scores": scores,
        },
    )
