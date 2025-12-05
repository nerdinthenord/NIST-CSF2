from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime

from .db import Base


class NistRequirement(Base):
    __tablename__ = "nist_requirement"

    id = Column(Integer, primary_key=True, index=True)
    framework = Column(String(64), index=True)           # e g "NIST_CSF_2_0"
    function_group = Column(String(16), index=True)      # e g "GV"
    category_id = Column(String(16), index=True)         # e g "GV_OC"
    subcategory_code = Column(String(32), index=True)    # e g "GV_OC_01"
    title = Column(String(256))
    text = Column(Text)

    questions = relationship("AssessmentQuestion", back_populates="requirement")


class AssessmentTemplate(Base):
    __tablename__ = "assessment_template"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), unique=True)
    framework = Column(String(64))

    questions = relationship("AssessmentQuestion", back_populates="template")


class AssessmentQuestion(Base):
    __tablename__ = "assessment_question"

    id = Column(Integer, primary_key=True, index=True)
    template_id = Column(Integer, ForeignKey("assessment_template.id"))
    requirement_id = Column(Integer, ForeignKey("nist_requirement.id"))
    question_text = Column(Text)
    answer_type = Column(String(32), default="scale_1_5")
    weight = Column(Float, default=1.0)

    template = relationship("AssessmentTemplate", back_populates="questions")
    requirement = relationship("NistRequirement", back_populates="questions")


class AssessmentRun(Base):
    __tablename__ = "assessment_run"

    id = Column(Integer, primary_key=True, index=True)
    template_id = Column(Integer, ForeignKey("assessment_template.id"))
    organization_name = Column(String(256))
    created_at = Column(DateTime, default=datetime.utcnow)
    created_by = Column(String(128))

    template = relationship("AssessmentTemplate")
    answers = relationship("AssessmentAnswer", back_populates="run")


class AssessmentAnswer(Base):
    __tablename__ = "assessment_answer"

    id = Column(Integer, primary_key=True, index=True)
    run_id = Column(Integer, ForeignKey("assessment_run.id"))
    question_id = Column(Integer, ForeignKey("assessment_question.id"))

    numeric_value = Column(Float, nullable=True)
    text_value = Column(Text, nullable=True)

    run = relationship("AssessmentRun", back_populates="answers")
    question = relationship("AssessmentQuestion")
