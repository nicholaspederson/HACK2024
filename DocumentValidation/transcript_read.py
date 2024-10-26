from student_data import StudentData
from TranscriptVal import TranscriptVal

# Parse JSON and create an instance
json_data = '{"first_name": "Alice", "mid_name": "Bill", "last_name": "Joe", "gender": "M", "dob": "2024-10-26", "country": "USA", "degree_program": "BA", "level": "Good"}'
student = StudentData.parse_raw(json_data)
#print(student)

validation = TranscriptVal(student,"scripts/Nyuma_Beatrice_Aiya_UGTranscripts.pdf")