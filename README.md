# HACK2024

Google Drive
    - credentials is sensitive becuase it has client_secret, which could allow someone to impersonate the app. 

## Document Validation Team

### Overview
The document validation scripts define a class used by the Google Drive API section to interact with our file cheking utilities. There are two classes defined in this section, given in **student_data.py** and in **TranscriptVal.py**. Each class handles a separate section of the document validation process. 

### Uniform Input and Output of Data
**student_data.py** defines a class that creates objects for standardized input and output. This object is designed to take in a JSON file from the UI and convert this into a format usable by the document validation and Google Drive operations. This format includes standard attributes from the form students fill out along with a "flags" attribute. This flags attribute is altered in the document validation process to identify which attributes may have discrepancies between the transcript upload and the form the student filled out with their information. 

### Document Validation
**TranscriptVal.py** defines a class that creates an object for evaluating a document. This class defines methods for validating the information students provide against the transcript they uploaded. The current implementation is based on Tesseract and converts a PDF to a text string which is searched for relevant information. Each aspect of the transcript outlined is checked and provided with a flag denoting if an issue has been found. Should the student data have discrepancies, the student data object is updated with flags corresponding the issues.
