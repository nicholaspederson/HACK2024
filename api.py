from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
import json
import os
from tempfile import SpooledTemporaryFile
from typing import List
import uvicorn

from DocumentValidation.StudentData import StudentData

from GoogleDrive import quickstart as google_drive

# from DocumentValidation import EvaluateTranscript

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


class TempFile(SpooledTemporaryFile):
    def __init__(self, name=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._name = name  # Private attribute to hold the file name

    @property
    def name(self):
        return self._name


@app.options("/{any:path}")
async def options(_: str):
    return {}


@app.post("/")
async def post_student(files: List[UploadFile] = File(...), request: str = Form(...)):
    local_files = []
    for i, file in enumerate(files):
        with open(file.filename or f"upload_file_{i}.pdf", "wb") as tempfile:
            tempfile.write(await file.read())
            tempfile.seek(0)
            local_files.append(tempfile)

    student = StudentData.parse_obj(json.loads(request))
    google_drive.main(student, local_files, "")

    for local_file in local_files:
        os.remove(local_file.name)

    return "student data recieved"


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
