

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(
     "sqlite+libsql:///embedded.db",
     connect_args={
         "sync_url": "libsql://coll-8988b194455245ab92ba9aff8b6a795a-mayson.aws-ap-south-1.turso.io",
         "auth_token": "eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3NzgyMTk3NzgsInAiOnsicm9hIjp7Im5zIjpbIjAxOWUwNjI4LTc3MDEtNzdkNS1iNDc0LTFjZjBkMWZmOTViMyJdfSwicnciOnsibnMiOlsiMDE5ZTA2MjgtNzcwMS03N2Q1LWI0NzQtMWNmMGQxZmY5NWIzIl19fSwicmlkIjoiM2I5NTJiY2UtYjkwYi00N2NlLWE3MTQtOGVkYjdlOTg0NWQzIn0.6-fXQoL-RjYzJOxGaP4D4X35MSWmsr1eM9SuhyJPWm13MWKHnkyDwh6KJzw_t-kBrhK3eeKAE00WzAIvDxH9CA",
     },
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)
Base = declarative_base()

