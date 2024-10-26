from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from io import BytesIO
from typing import List

from DocumentValidation.StudentData import StudentData

from GoogleDrive import quickstart as google_drive
from DocumentValidation import EvaluateTranscript

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


@app.options("/{any:path}")
async def options(_: str):
    return {}


@app.post("/test")
async def test_files(file: UploadFile):
    print(file.filename)


@app.post("/")
async def post_student(files: List[UploadFile] = File(...), request: str = Form(...)):
    local_files = []
    for file in files:
        content = await file.read()
        local_files += BytesIO(content)

    google_drive.main(request, local_files, "")

    return "student data recieved"
