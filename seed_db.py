from app.db import engine, Base, SessionLocal
from app.nist.seed_data import seed_csf_template_and_questions


def main():
    print("Creating tables")
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        print("Seeding CSF 2 template and questions")
        seed_csf_template_and_questions(db)
        print("Done")
    finally:
        db.close()


if __name__ == "__main__":
    main()
