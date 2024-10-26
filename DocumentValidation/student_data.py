from pydantic import BaseModel

class StudentData(BaseModel):
    """
    Parse JSON into a class
    """
    first_name: str
    mid_name: str
    last_name: str
    gender: str
    dob: str
    country: str
    degree_program: str
    level: str