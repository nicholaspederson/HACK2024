import os.path

from apiclient.http import MediaFileUpload # type:ignore

from google.auth.transport.requests import Request # type: ignore
from google.oauth2.credentials import Credentials # type: ignore
from google_auth_oauthlib.flow import InstalledAppFlow # type: ignore
from googleapiclient.discovery import build # type: ignore
from googleapiclient.errors import HttpError # type: ignore

from DocumentValidation.student_data import StudentData

# If modifying these scopes, delete the file token.json.
#this scope gives all access to all modifications in drive
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
          #credentials contains the information such that if it is not secure it
          #can allow a third party to impersonate the app
          "GoogleDrive/credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())
  return creds

#how we are getting the instance of a class which
#contains the student data
def getInfo():
  return StudentData()

# parses studentInfo to generate
# appropriate file names
# return in format FirstName_LastName
def getStudentName(studentInfo: StudentData):
  #default student name
  studentName = ""
  #no info, default name
  if studentInfo == None:
    studentName = "FirstName_LastName"
  else:
    #combine first and last name concatenateb by an underscore
    studentName = str(studentInfo.first_name + "_" + studentInfo.last_name)
  return studentName

#Goes through all the files, and adds them to the folder
#Changes all of the names to the correct name
def populateFolder(service, files, name, studentFolder):
  #for each submitted file
  for file in files:
    #prepare metadata for the file to be created in drive
    #set the metadata, assumes the file is a pdf
    #name of the file gives format FirstName_LastName_FileName
    fileMetaData = {"name": name+"_"+file.name.split('\\')[-1], "mimeType": "application/pdf", "parents": [studentFolder]}
    #the content of the file in drive is the same as the file we are
    #looking at
    media = MediaFileUpload(file.name, resumable=True)
    #create the file in drive
    service.files().create(body=fileMetaData, media_body=media, fields='id, name').execute()
  return None

# returns the name for the file (appropriate student name from)
# student info - instance of the StudentData class
# format: LastName_FirstName_MiddleName_DegreeSeeking-Candidate_Country
def getFolderName(studentInfo: StudentData):
  #default file name
  filename = ""
  #no info, default name
  if studentInfo == None:
    filename = "LastName_FirstName_MiddleName_DegreeSeeking-Candidate_Country"
  else:
    #combine relevent data separated by _
    filename = str(studentInfo.last_name + "_" + 
                   studentInfo.first_name + "_" + 
                   studentInfo.middle_name + "_" + 
                   studentInfo.degree_program + "-" + 
                   studentInfo.country1)
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
  #name is folder name
  #type is folder
  #parent is the specified folder ID
  file_metadata = {"name": folderName,
                     "mimeType": "application/vnd.google-apps.folder",
                      "parents": ["1o0f25LLI9rtfjMGkfMJn6l-fDkXTKfOt"]}
  #creates the folder as specified
  file = service.files().create(body=file_metadata, fields="id").execute()
  return file.get("id")

# populates the sheet with the student information
def populateSheet(sheetsService, studentInfo):
  #values to put in the row, left to right
  values = [
    [
      "", #flags
      "", #additional notes
      studentInfo.first_name, #first name
      studentInfo.last_name, #last name
      studentInfo.middle_name, #middle name
      studentInfo.additional_name, #additional name
      studentInfo.degree_program, #program description
      studentInfo.level, #degree level
      studentInfo.gender, #gender
      studentInfo.dob, #date of birth
      studentInfo.email, #personal email
      "", #name of file with ID
      "", #file 1 name
      studentInfo.country1, #country associated with file 1
      "", #file 2 name
      studentInfo.country2, #country associated with file 2
      "", #file 3 name
      studentInfo.country3, #country associated with file 3
      "", #file 4 name
      "", #country associated with file 4
    ],
  ]
  #prepares data to be passed to the API
  body = {"values":values}
  #adds the data to the specified spreadsheet ID
  #range is the sheet Fields, and everything past B5 (down and right)
  #we act as if the data was entered by a user
  #body is the data
  sheetsService.spreadsheets().values().append(
            spreadsheetId="1WGz4bI5ioohrY6hDr7KH01k_zXNTG1VgKbc_RtLknOc",
            range="Fields!B5:Z",
            valueInputOption="USER_ENTERED",
            body=body,
        ).execute()
  return None

def main(studentInfo):
  #asks user to authenticate their identity
  #we use the credentials to access the API
  creds = getCreds()

  try:
    #to access drive API
    service = build("drive", "v3", credentials=creds)
    #to access sheets API
    sheetsService = build("sheets", "v4", credentials=creds)
    #uses studentInnfo to get the FirstName_LastName of the student
    name = getStudentName(studentInfo)
    #uses studentInfo to generate the
    #LastName_FirstName_MiddleName_DegreeSeeking-Candidate_Country
    #folder name
    folderName = getFolderName(studentInfo)
    #creates the folder in the drive with the given name
    studentFolder = createFolder(service, folderName)
    #sample file since this is not conencted to the API
    #files = [open("GoogleDrive\\sample.pdf", "r", encoding='latin-1')]
    #populates the created folder with files
    #files should be included in the API call from the front-end
    #populateFolder(service, files, name, studentFolder)
    #populates the google sheet with the student info
    populateSheet(sheetsService, studentInfo)
  
  except HttpError as error:
    # TODO(developer) - Handle errors from drive API.
    #We are assuming proper input
    print(f"An error occurred: {error}")


if __name__ == "__main__":
  main(None)