from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from DocumentValidation.StudentData import StudentData
from GoogleDrive import quickstart as google_drive

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


@app.post("/")
async def post_student(request: StudentData):
    print("Sending student data to google drive")
    google_drive.main(request)

    return "student data recieved!"
