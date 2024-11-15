from pydantic import BaseModel
from typing import Optional


class StudentData(BaseModel):
    """
    Parse JSON into a class
    """

    first_name: str
    middle_name: str = ""
    last_name: str
    additional_name: Optional[str] = None
    gender: str
    dob: str
    degree_level: str
    degree_program: str
    email: str
    country1: str
    country2: Optional[str] = None
    country3: Optional[str] = None
