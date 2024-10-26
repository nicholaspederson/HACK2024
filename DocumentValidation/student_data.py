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

# Parse JSON and create an instance
json_data = '{"first_name": "Alice", "mid_name": "Bill", "last_name": "Joe", "gender": "M", "dob": "2024-10-26", "country": "USA", "degree_program": "BA", "level": "Good"}'
student = StudentData.parse_raw(json_data)
print(student)