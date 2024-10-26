import os.path
import json

from google.auth.transport.requests import Request # type: ignore
from google.oauth2.credentials import Credentials # type: ignore
from google_auth_oauthlib.flow import InstalledAppFlow # type: ignore
from googleapiclient.discovery import build # type: ignore
from googleapiclient.errors import HttpError

from DocumentValidation.student_data import StudentData # type: ignore

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
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())
  return creds

# gets the submitted files
def getFiles():
  return None

# utilizse an API to call to a databse
# with the given unique identifier
# to get relevant student info
def getInfo(UID):
  return None

# parses studentInfo to generate
# appropriate file names
# return in format FirstName_LastName
def getStudentName(studentInfo):
  if studentInfo == None:
    return "FirstName_LastName"
  return ""

# prepends the name to each file
def renameFiles(files, name):
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
  print(f'Folder ID: "{file.get("id")}".')
  return file.get("id")

# populate the folder with the correct files
def populateFolder(service, files, folderID):
  return None

# whatever cleaning may or may not need to happen
def clean():
  return None

def main():
  creds = getCreds()

  try:
    service = build("drive", "v3", credentials=creds)

    files = getFiles()

    studentInfo = getInfo()

    name = getStudentName(studentInfo)

    renameFiles(files, name)

    folderName = getFolderName(studentInfo)

    studentFolder = createFolder(service, folderName)

    populateFolder(service, files, studentFolder)

    clean()
  
  except HttpError as error:
    # TODO(developer) - Handle errors from drive API.
    print(f"An error occurred: {error}")


if __name__ == "__main__":
  main()