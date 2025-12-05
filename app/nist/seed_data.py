from sqlalchemy.orm import Session

from ..models import NistRequirement, AssessmentTemplate, AssessmentQuestion


def seed_csf_requirements(db: Session, framework: str = "NIST_CSF_2_0") -> None:
    requirements = [
        # Govern function
        # Organizational context
        ("GV", "GV_OC", "GV_OC_01", "Business context documented",
         "Business mission, objectives, stakeholders and critical services are documented and maintained."),
        ("GV", "GV_OC", "GV_OC_02", "Asset and dependency understanding",
         "Critical assets and internal and external dependencies are identified and understood."),
        ("GV", "GV_OC", "GV_OC_03", "Threat environment understood",
         "Current and emerging cyber threats relevant to the organization are monitored and understood."),
        # Risk management strategy
        ("GV", "GV_RM", "GV_RM_01", "Risk appetite defined",
         "Cybersecurity risk appetite is defined and approved by senior leadership."),
        ("GV", "GV_RM", "GV_RM_02", "Risk tolerances set",
         "Risk tolerances for key business services are defined and used."),
        ("GV", "GV_RM", "GV_RM_03", "Risk approach consistent",
         "A consistent approach to risk identification, analysis and treatment is used across the enterprise."),
        # Roles responsibilities and oversight
        ("GV", "GV_RR", "GV_RR_01", "Roles and responsibilities defined",
         "Cybersecurity roles responsibilities and decision rights are defined and assigned."),
        ("GV", "GV_RR", "GV_RR_02", "Executive oversight",
         "Senior leadership or a board committee provides oversight of cybersecurity risk."),
        ("GV", "GV_RR", "GV_RR_03", "Accountability across functions",
         "Business and technology leaders are accountable for cybersecurity outcomes."),
        # Policy and procedures
        ("GV", "GV_PO", "GV_PO_01", "Policies defined and approved",
         "Cybersecurity policies are defined aligned to standards and formally approved."),
        ("GV", "GV_PO", "GV_PO_02", "Procedures documented",
         "Procedures to implement policy requirements are documented and used."),
        ("GV", "GV_PO", "GV_PO_03", "Policy review cycle",
         "Cybersecurity policies are reviewed and updated on a defined cycle."),
        # Supply chain risk management
        ("GV", "GV_SC", "GV_SC_01", "Supplier risk program",
         "A structured supplier or third party cyber risk management program exists."),
        ("GV", "GV_SC", "GV_SC_02", "Critical suppliers identified",
         "Critical suppliers and service providers are identified and prioritized for oversight."),
        ("GV", "GV_SC", "GV_SC_03", "Cyber in contracts",
         "Cybersecurity and data protection requirements are included in contracts."),
        # Oversight and performance
        ("GV", "GV_OV", "GV_OV_01", "Metrics and reporting",
         "Cybersecurity performance measures and risk metrics are defined and reported."),
        ("GV", "GV_OV", "GV_OV_02", "Independent assurance",
         "Independent assurance over cybersecurity controls and risks is obtained."),
        ("GV", "GV_OV", "GV_OV_03", "Continuous improvement",
         "Findings from incidents and reviews are used to improve the program."),

        # Identify function
        ("ID", "ID_AM", "ID_AM_01", "Asset inventory",
         "Hardware and software assets are inventoried and owned."),
        ("ID", "ID_AM", "ID_AM_02", "Data inventory",
         "Data types and locations are identified and classified."),
        ("ID", "ID_BE", "ID_BE_01", "Business environment",
         "Critical business processes and their dependencies are documented."),
        ("ID", "ID_RA", "ID_RA_01", "Risk assessments performed",
         "Cybersecurity risk assessments are performed for key systems and services."),
        ("ID", "ID_RA", "ID_RA_02", "Threat and vulnerability information used",
         "Threat and vulnerability information is used in risk assessments."),
        ("ID", "ID_RM", "ID_RM_01", "Risk responses tracked",
         "Risk treatment plans are defined and tracked to completion."),
        ("ID", "ID_SC", "ID_SC_01", "Supply chain risks identified",
         "Risks from suppliers and partners are identified and documented."),

        # Protect function
        ("PR", "PR_AC", "PR_AC_01", "Access based on least privilege",
         "Access to systems and data is granted based on least privilege and role."),
        ("PR", "PR_AC", "PR_AC_02", "Privileged access managed",
         "Privileged accounts are managed, monitored and periodically reviewed."),
        ("PR", "PR_DS", "PR_DS_01", "Data protection",
         "Sensitive data is protected in storage and in transit."),
        ("PR", "PR_DS", "PR_DS_02", "Data retention and disposal",
         "Retention and disposal of data follows defined rules."),
        ("PR", "PR_PT", "PR_PT_01", "Platform hardening",
         "Systems follow secure baseline configurations and hardening guidance."),
        ("PR", "PR_PT", "PR_PT_02", "Configuration management",
         "Changes to configurations follow a managed process."),
        ("PR", "PR_AW", "PR_AW_01", "Awareness training",
         "Users receive cybersecurity awareness and role specific training."),
        ("PR", "PR_SD", "PR_SD_01", "Secure development",
         "Secure development practices are used in the system development life cycle."),

        # Detect function
        ("DE", "DE_CM", "DE_CM_01", "Security monitoring",
         "Security relevant events are collected and monitored."),
        ("DE", "DE_CM", "DE_CM_02", "Use cases and rules",
         "Detection use cases and rules are defined and maintained."),
        ("DE", "DE_AN", "DE_AN_01", "Analysis of alerts",
         "Alerts are analyzed to determine impact and required actions."),
        ("DE", "DE_IM", "DE_IM_01", "Detection improvement",
         "Detection capabilities are regularly tuned and improved."),

        # Respond function
        ("RS", "RS_PL", "RS_PL_01", "Response plan",
         "An incident response plan is defined and approved."),
        ("RS", "RS_PL", "RS_PL_02", "Exercises",
         "Response plans are tested through exercises or simulations."),
        ("RS", "RS_CO", "RS_CO_01", "Communication",
         "Communication roles and channels for incidents are defined."),
        ("RS", "RS_AN", "RS_AN_01", "Incident analysis",
         "Incidents are analyzed to understand root cause and impact."),
        ("RS", "RS_MI", "RS_MI_01", "Mitigation",
         "Actions are taken to contain and mitigate incidents."),

        # Recover function
        ("RC", "RC_PL", "RC_PL_01", "Recovery plan",
         "Recovery plans exist for key systems and services."),
        ("RC", "RC_PL", "RC_PL_02", "Recovery objectives defined",
         "Recovery time and recovery point objectives are defined."),
        ("RC", "RC_IM", "RC_IM_01", "Recovery tests",
         "Backups and recovery capabilities are regularly tested."),
        ("RC", "RC_IM", "RC_IM_02", "Improvements after events",
         "Recovery processes are improved based on lessons learned."),
    ]

    for fun, cat, sub, title, text in requirements:
        existing = (
            db.query(NistRequirement)
            .filter_by(framework=framework, function_group=fun,
                       category_id=cat, subcategory_code=sub)
            .first()
        )
        if not existing:
            db.add(
                NistRequirement(
                    framework=framework,
                    function_group=fun,
                    category_id=cat,
                    subcategory_code=sub,
                    title=title,
                    text=text,
                )
            )
    db.commit()


def seed_csf_template_and_questions(db: Session, framework: str = "NIST_CSF_2_0") -> None:
    from ..models import AssessmentTemplate, AssessmentQuestion, NistRequirement

    seed_csf_requirements(db, framework=framework)

    template = (
        db.query(AssessmentTemplate)
        .filter_by(name="Enterprise CSF 2 Governance Assessment", framework=framework)
        .first()
    )
    if not template:
        template = AssessmentTemplate(
            name="Enterprise CSF 2 Governance Assessment",
            framework=framework,
        )
        db.add(template)
        db.flush()

    reqs = (
        db.query(NistRequirement)
        .filter_by(framework=framework)
        .order_by(NistRequirement.function_group, NistRequirement.category_id, NistRequirement.subcategory_code)
        .all()
    )

    for req in reqs:
        existing_q = (
            db.query(AssessmentQuestion)
            .filter_by(template_id=template.id, requirement_id=req.id)
            .first()
        )
        if existing_q:
            continue

        # Use the NIST wording itself as the statement
        # The user rates maturity of this statement one to five
        q_text = req.text

        q = AssessmentQuestion(
            template_id=template.id,
            requirement_id=req.id,
            question_text=q_text,
            answer_type="scale_1_5",
            weight=1.0,
        )
        db.add(q)

    db.commit()
