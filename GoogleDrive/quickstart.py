import os.path

from apiclient.http import MediaFileUpload #type:ignore

from google.auth.transport.requests import Request # type: ignore
from google.oauth2.credentials import Credentials # type: ignore
from google_auth_oauthlib.flow import InstalledAppFlow # type: ignore
from googleapiclient.discovery import build # type: ignore
from googleapiclient.errors import HttpError # type: ignore

from DocumentValidation.student_data import StudentData

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/drive"]

# looks for existing token, or asks user to verify and generate a token
# credentials are returned
def getCreds():
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "GoogleDrive/credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())
  return creds

def getInfo():
  return StudentData()

# parses studentInfo to generate
# appropriate file names
# return in format FirstName_LastName
def getStudentName(studentInfo: StudentData):
  studentName = ""
  if studentInfo == None:
    studentName = "FirstName_LastName"
  else:
    studentName = str(studentInfo.first_name + "_" + studentInfo.last_name)
  return studentName

#Goes through all the files, and adds them to the folder
#Changes all of the names to the correct name
def populateFolder(service, files, name, studentFolder):
  for file in files:
    #fileName = file.name.split('\\')[-1]
    fileMetaData = {"name": name+"_"+file.name.split('\\')[-1], "mimeType": "application/pdf", "parents": [studentFolder]}
    media = MediaFileUpload(file.name, resumable=True)
    f = service.files().create(body=fileMetaData, media_body=media, fields='id, name').execute()
  return None

# returns the name for the file (appropriate student name from)
# student info - instance of the StudentData class
# format: LastName_FirstName_MiddleName_DegreeSeeking-Candidate_Country
def getFolderName(studentInfo: StudentData):
  filename = ""
  if studentInfo == None:

    filename = "LastName_FirstName_MiddleName_DegreeSeeking-Candidate_Country"
  else:
    filename = str(studentInfo.last_name + "_" + 
                   studentInfo.first_name + "_" + 
                   studentInfo.mid_name + "_" + 
                   studentInfo.degree_program + "-" + 
                   studentInfo.country)
  return filename

# make the folder in a specific parent
# by using the parent's file ID
# service: access to google drive API
# name: name of the file
# folder ID of test file "Student Files - Nicholas" is 1o0f25LLI9rtfjMGkfMJn6l-fDkXTKfOt
def createFolder(service, folderName):
  # place holder name
  if folderName == "":
    folderName = "LastName_FirstName_MiddleName_DegreeSeeking-Candidate_Country"
  file_metadata = {"name": folderName,
                     "mimeType": "application/vnd.google-apps.folder",
                      "parents": ["1o0f25LLI9rtfjMGkfMJn6l-fDkXTKfOt"]}

  # pylint: disable=maybe-no-member
  file = service.files().create(body=file_metadata, fields="id").execute()
  return file.get("id")

# populates
def populateSheet(sheetsService, sheetID, studentInfo):
  sheet = sheetsService.spreadsheets()
  values = [
    [
      "", #flags
      "", #additional notes
      studentInfo.first_name, #first name
      studentInfo.last_name, #last name
      studentInfo.mid_name, #middle name
      "", #additional name
      studentInfo.degree_program, #program description
      studentInfo.level, #degree level
      studentInfo.gender, #gender
      studentInfo.dob, #date of birth
      "", #personal email
      "", #name of file with ID
      "", #file 1 name
      "", #country associated with file 1
      "", #file 2 name
      "", #country associated with file 2
      "", #file 3 name
      "", #country associated with file 3
      "", #file 4 name
      "", #country associated with file 4
    ],
  ]
  body = {"values":values}
  result = (
        sheetsService.spreadsheets()
        .values()
        .append(
            spreadsheetId=sheetID,
            range="Fields!B5:Z",
            valueInputOption="USER_ENTERED",
            body=body,
        )
        .execute()
    )
  return None

def main():
  creds = getCreds()

  try:
    service = build("drive", "v3", credentials=creds)
    sheetsService = build("sheets", "v4", credentials=creds)

    studentInfo = getInfo()

    #flags = validate(files, studentInfo)

    name = getStudentName(studentInfo)

    folderName = getFolderName(studentInfo)

    studentFolder = createFolder(service, folderName)

    files = [open("GoogleDrive\sample.pdf", "r", encoding='latin-1')]
    populateFolder(service, files, name, studentFolder)

    sheetID = "1WGz4bI5ioohrY6hDr7KH01k_zXNTG1VgKbc_RtLknOc"
    populateSheet(sheetsService, sheetID, studentInfo)
  
  except HttpError as error:
    # TODO(developer) - Handle errors from drive API.
    print(f"An error occurred: {error}")


if __name__ == "__main__":
  main()