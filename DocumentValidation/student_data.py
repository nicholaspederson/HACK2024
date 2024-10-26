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
    country3: str


if __name__ == "__main__":
    # Parse JSON and create an instance
    json_data = '{"first_name": "Alice", "mid_name": "Bill", "last_name": "Joe", "gender": "M", "dob": "2024-10-26", "country": "USA", "degree_program": "BA", "level": "Good"}'
    student = StudentData.parse_raw(json_data)
    print(student)
