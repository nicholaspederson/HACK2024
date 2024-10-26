# Front End
### How to run
Run the following commands while in the FE directory to view the front end. Use the CD command in the terminal to navigate to the  …../Hack2024/HACK2024/FE. The …. in the path represents that the path will be different from computer to computer. Once in the FE directory, run the following commands: 
1. NPM install
2. NPM run dev

### Details
The front end is written in React TypeScript using the React BootStrap library. The main portion of the code is in the App.tsx file. Here, lines 13-28 are the variables for each field. To add another field, use the same convention and add another useState statement. Lines 86-230 contains the markup code that will be displayed to the user. This pattern could also be followed by adding a new Form.Group tag and replacing the value and onChange attributes to the new useState variable to create or modify a field.

The web requests are being sent in the handleSubmit function. This function does correctly send JSON containing the data from the input text boxes to the backend using the API. This method will have to be added for file sending functionality. The files are currently only being stored in the nationalID, transcript1, transcript2, and transcript3 but are not sent to the backend.

When uploading files, currently only PDFs can be uploaded. The code does not check the file size and limit submissions. This is something that should be added but we did not have time to implemment it.
