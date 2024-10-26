import os.path

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
def getInfo():
  return None

# validates the student info, and reutrns flags
def validate(files, studentInfo):
  return None

# parses studentInfo to generate
# appropriate file names
# return in format FirstName_LastName
def getStudentName(studentInfo):
  if studentInfo == None:
    return "FirstName_LastName"
  return ""

# populates the given folder with new file names
def populateFolder(files, name):
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
  
  #rows = result.get("values")
  #print(f"{len(rows)} rows retrieved")
  #print(rows)
  return None

# whatever cleaning may or may not need to happen
def clean():
  return None

def main():
  creds = getCreds()

  try:
    service = build("drive", "v3", credentials=creds)
    sheetsService = build("sheets", "v4", credentials=creds)

    #files = getFiles()

    #studentInfo = getInfo()

    #flags = validate(files, studentInfo)

    #name = getStudentName(studentInfo)

    studentInfo = None
    #folderName = getFolderName(studentInfo)

    #studentFolder = createFolder(service, folderName)

    #populateFolder(service, files, name, studentFolder)
    
    sheetID = "1WGz4bI5ioohrY6hDr7KH01k_zXNTG1VgKbc_RtLknOc"
    populateSheet(sheetsService, sheetID, studentInfo)

    clean()
  
  except HttpError as error:
    # TODO(developer) - Handle errors from drive API.
    print(f"An error occurred: {error}")


if __name__ == "__main__":
  main()