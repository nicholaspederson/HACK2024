from pydantic import BaseModel

class StudentData(BaseModel):
    """
    Parse JSON into a class
    """
    first_name: str = "Alice"
    mid_name: str = "Bill"
    last_name: str = "Joe"
    gender: str = "M"
    dob: str = "2024-10-26"
    country: str = "USA"
    degree_program: str = "BA"
    level: str = "Good"

# Parse JSON and create an instance
json_data = '{"first_name": "Alice", "mid_name": "Bill", "last_name": "Joe", "gender": "M", "dob": "2024-10-26", "country": "USA", "degree_program": "BA", "level": "Good"}'
student = StudentData.parse_raw(json_data)
print(student)