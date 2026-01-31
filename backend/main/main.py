import os
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import get_test as gt

app = FastAPI()

frontend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../frontend/subjects/statistic"))

app.mount("/static", StaticFiles(directory=frontend_path), name="static")

@app.get("/statistic")
def read_index():
    file_path = os.path.join(frontend_path, "index.html")
    return FileResponse(file_path)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/hello")
def hello():
    return {"message": "Привет от FastAPI 🚀"}

class TextIn(BaseModel):
    text: str

@app.post("/api/user_marks")
def reverse_text(data: TextIn):
    return {"result": gt.get_results_by_user_id(data.text)} #af73452e-bbbb-443d-83a2-423f78cd003e

@app.get("/api/columns")
def get_columns():
    return gt.get_columns_in_database()
