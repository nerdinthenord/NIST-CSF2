from typing import List, Dict, Any
from sqlalchemy.orm import Session

from ..models import AssessmentRun, AssessmentAnswer


SCALE_LABELS = {
    1: "No controls in place",
    2: "Some controls defined",
    3: "Medium controls, partially implemented",
    4: "Developed controls, consistently applied",
    5: "Mature controls, measured and improved",
}


def start_assessment_run(
    db: Session,
    template_id: int,
    organization_name: str,
    created_by: str,
) -> AssessmentRun:
    run = AssessmentRun(
        template_id=template_id,
        organization_name=organization_name,
        created_by=created_by,
    )
    db.add(run)
    db.commit()
    db.refresh(run)
    return run


def save_answers(
    db: Session,
    run_id: int,
    answers: List[Dict[str, Any]],
) -> None:
    for ans in answers:
        db.add(
            AssessmentAnswer(
                run_id=run_id,
                question_id=ans["question_id"],
                numeric_value=ans.get("numeric_value"),
                text_value=ans.get("text_value"),
            )
        )
    db.commit()


def calculate_scores(db: Session, run_id: int) -> dict:
    run = db.query(AssessmentRun).filter_by(id=run_id).first()
    if not run:
        raise ValueError("Assessment run not found")

    scores_by_subcat = {}
    scores_by_function = {}

    for ans in run.answers:
        if ans.numeric_value is None:
            continue
        q = ans.question
        req = q.requirement

        sub_key = req.subcategory_code
        fun_key = req.function_group

        scores_by_subcat.setdefault(sub_key, {
            "function_group": req.function_group,
            "category_id": req.category_id,
            "title": req.title,
            "values": [],
        })
        scores_by_subcat[sub_key]["values"].append(ans.numeric_value)

        scores_by_function.setdefault(fun_key, []).append(ans.numeric_value)

    subcategories = []
    for code, data in scores_by_subcat.items():
        values = data["values"]
        avg = sum(values) / len(values) if values else 0.0
        subcategories.append(
            {
                "subcategory_code": code,
                "function_group": data["function_group"],
                "category_id": data["category_id"],
                "title": data["title"],
                "average_score": avg,
            }
        )

    functions = []
    for fun, values in scores_by_function.items():
        avg = sum(values) / len(values) if values else 0.0
        functions.append(
            {
                "function_group": fun,
            "average_score": avg,
            }
        )

    overall = 0.0
    all_vals = [item["average_score"] for item in subcategories if item["average_score"] > 0]
    if all_vals:
        overall = sum(all_vals) / len(all_vals)

    return {
        "run_id": run.id,
        "organization_name": run.organization_name,
        "created_at": run.created_at.isoformat(),
        "overall_maturity": overall,
        "subcategories": subcategories,
        "functions": functions,
        "scale_labels": SCALE_LABELS,
    }
