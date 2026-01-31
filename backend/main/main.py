from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import get_test as gt

app = FastAPI()

# статика (css, js и т.п.)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def root():
    return FileResponse("static/index.html")

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
