import os


class Settings:
    app_name: str = "NIST CSF 2 Governance Assessment"
    environment: str = os.getenv("ENVIRONMENT", "prod")

    # Database lives in /data inside the container
    database_url: str = os.getenv("DATABASE_URL", "sqlite:////data/csf2.db")


settings = Settings()
