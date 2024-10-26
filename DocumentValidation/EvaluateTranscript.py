from TranscriptVal import TranscriptVal
from StudentData import StudentData

JSON_DATA = '{"first_name": "emily", "mid_name": "john", "last_name": "james", "gender": "f", "dob": "2024-10-26", "country": "ugando", "degree_program": "BA", "level": "Good"}'
PDF_PATH = "/PDF/Path/name.pdf"


def main():
    # Parse JSON and create an instance
    student = StudentData.parse_raw(JSON_DATA)

    validation = TranscriptVal(student, PDF_PATH)

    flag = validation.validate_data()

    evalutation = (student, flag)

    return evalutation


if __name__ == "__main__":
    print(main())
