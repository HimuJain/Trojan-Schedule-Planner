from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
from pathlib import Path


app = FastAPI(title="Trojan Schedule Planner API", version="0.0.1")
# CORS (allow frontend dev server)
app.add_middleware(
    CORSMiddleware,
    # allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
DATA_PATH = Path(__file__).parent / "sample_courses.json"
class Course(BaseModel):
    code: str
    title: str
    units: int
    dept: str
    ge: list[str]
    instructor: str
    days: list[str]
    time: str
    location: str

@app.get("/ping")
def ping():
    return {"ok": True}

@app.get("/courses", response_model=list[Course])
def list_courses(q: str | None = None):
    courses = json.loads(DATA_PATH.read_text())
    if q:
        ql = q.lower()
        def hay(c):
            return f"{c['code']} {c['title']} {c['dept']}".lower()
        courses = [c for c in courses if ql in hay(c)]
    return courses