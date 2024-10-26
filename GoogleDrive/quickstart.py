import os.path
import shutil

from apiclient.http import MediaFileUpload #type:ignore

from google.auth.transport.requests import Request # type: ignore
from google.oauth2.credentials import Credentials # type: ignore
from google_auth_oauthlib.flow import InstalledAppFlow # type: ignore
from googleapiclient.discovery import build # type: ignore
from googleapiclient.errors import HttpError # type: ignore

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
def populateFolder(service, files, name, studentFolder):
  for file in files:
    new_file = open(name, 'w')
    shutil.copyfileobj(file, new_file)
    fileMetaData = {"name": name, "mimeType": "application/pdf", "parents": [studentFolder]}
    media = MediaFileUpload(name, resumable=True)
    f = service.files().create(body=fileMetaData, media_body=media, fields='id, name').execute()
  return None

# gets the appropriate student name from
# student info
# format: LastName_FirstName_MiddleName_DegreeSeeking-Candidate_Country
def getFolderName(studentInfo):
  if studentInfo == None:
    return "LastName_FirstName_MiddleName_DegreeSeeking-Candidate_Country"
  return ""

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

    folderName = getFolderName(studentInfo)

    studentFolder = createFolder(service, folderName)

    populateFolder(service, files, name, studentFolder)

    clean()
  
  except HttpError as error:
    # TODO(developer) - Handle errors from drive API.
    print(f"An error occurred: {error}")


if __name__ == "__main__":
  main()