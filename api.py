from fastapi import FastAPI

from DocumentValidation.student_data import StudentData

app = FastAPI()


@app.post("/")
async def say_hello(request: StudentData):
    print(request)
    return "student data received"
