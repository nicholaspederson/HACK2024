# HACK2024

Google Drive - credentials is sensitive becuase it has client_secret, which could allow someone to impersonate the app.

## Document Validation Team

### Overview

The document validation scripts define a class used by the Google Drive API section to interact with our file cheking utilities. There are two classes defined in this section, given in **student_data.py** and in **TranscriptVal.py**. Each class handles a separate section of the document validation process.

### Uniform Input and Output of Data

**student_data.py** defines a class that creates objects for standardized input and output. This object is designed to take in a JSON file from the UI and convert this into a format usable by the document validation and Google Drive operations. This format includes standard attributes from the form students fill out along with a "flags" attribute. This flags attribute is altered in the document validation process to identify which attributes may have discrepancies between the transcript upload and the form the student filled out with their information.

### Document Validation

**TranscriptVal.py** defines a class that creates an object for evaluating a document. This class defines methods for validating the information students provide against the transcript they uploaded. The current implementation is based on Tesseract and converts a PDF to a text string which is searched for relevant information. Each aspect of the transcript outlined is checked and provided with a flag denoting if an issue has been found. Should the student data have discrepancies, the student data object is updated with flags corresponding the issues.

## Front End Team

### Details

The web page contains two pages. The student page contains all of the information and file uploads that a student would need to fill out. All inputs are required except the additional name field. Additionally, the issuing country fields are only required there are multiple transcripts provided. This means that country 1 is always required and the other countries are only required if that number of transcripts is provided. The UI does not actually make the fields required. However, the API call will only be successful if these rules are followed.

The degree level is not inserted by the student. Instead, the degree level is obtained from the degree program field.

### How to run

Run the following commands while in the FE directory to view the front end:

1. NPM install
2. NPM run dev

## API

The API is used to connect the front end to the back end functions, which includes both the document validation and the Google Drive file uploading functions. The API has only one `POST` endpoint, at the root of the API (`"/"`), which expects form data as its body. The form data must include two parts, namely:

1. `request`: A json blob including the following fields:
   - `first_name` (string)
   - `middle_name` (string)
   - `last_name` (string)
   - `additional_name` (string, optional)
   - `gender` (string)
   - `dob` (string)
   - `degree_level` (string)
   - `degree_program` (string)
   - `email` (string)
   - `country1` (string)
   - `country2` (string, optional)
   - `country3` (string, optional)
2. `files`: A list of files to upload as verification. Each country field should correspond to the country of origin for its respective file.

### Example API request using Typescript:

The following example is a request to the API using `fetch`. Replace apiURL with the URL for the API.

```
let studentData = {
    first_name: fName,
    middle_name: mName,
    last_name: lName,
    additional_name: addlName,
    gender: gender,
    dob: dob,
    degree_level: degreeLevel,
    email: email,
    degree_program: degreeProgram,
    country1: country1,
    country2: country2,
    country3: country3,
};
let jsonData = JSON.stringify(studentData);

const formData = new FormData();
formData.append("request", jsonData);
formData.append("files", transcript1);
if (transcript2) {
    formData.append("files", transcript2);
}
if (transcript3) {
    formData.append("files", transcript3);
}

fetch(apiURL, {
    method: "POST",
    body: formData,
})
    .then((response) => response.json())
```

### Running the API Locally

1. To test the API locally, make sure the following python pip packages are installed:

   ```
   pip install fastapi uvicorn pydantic google-api-python-client google-auth-httplib2 google-auth-oauthlib apiclient python-multipart
   ```

2. Run the API using `python api.py`.

3. Use the url `http://localhost:8080/` to test the API.

### Running the API in Google Cloud

If you want the API to be accessible to the internet, uploading the API to Google Cloud is the best solution because the Google Drive scripts require access to Google Cloud. This is done by compiling a docker image with the `Dockerfile`, and uploading it to Google Cloud Run.

1. Make sure the docker cli tool is installed. This can be done by using the Docker Desktop Install page for the relevant platform, or `sudo apt-get install docker` on Debian/Linux systems. Use `docker --version` to make sure the install worked properly.

2. Install the google cloud client, instructions can be found at https://cloud.google.com/sdk/docs/install. After the tool is installed, run `gcloud init` to authenticate with the Google Cloud Account that will be running the API. Configure gcloud to use the Google Cloud project you want to use for this app.

   (Unfortunately, `gcloud` is the only way to upload a docker image to Google Cloud).

3. Build the docker image with a name `<build-name>`.

   ```
   docker build . -t <build-name>
   ```

   NOTE: if docker doesn't run, follow steps to add your user to the docker user group: for linux, use https://docs.docker.com/engine/install/linux-postinstall/. This works better than using `sudo` to run docker.

4. In the Google Cloud Artifact Registry, create a Repository. This is where the image will be uploaded so it can be ran.

5. Tag the image to relate it to Google Cloud Container Registry. Make sure the gcloud client authenticates docker by first running

   ```
   gcloud auth configure-docker us-central1-docker.pkg.dev
   ```

   Then run the following, using `<build-name>` the name of the docker image from step 3, `<your-project-name>` the name of the Google Cloud project, `<repository-name>` the name of the repository in Google Cloud Artifact Registry from step 4, and `<tag>` an arbitrary tag (such as 1.0.0).

   ```
   docker tag <build-name> us-central1-docker.pkg.dev/<your-project-name>/<repository-name>/transcript-app:<tag>
   ```

6. Use docker to push the image to the registry, using the same values as above.

   ```
   docker push us-central1-docker.pkg.dev/<your-project-name>/transcript-app:<tag>
   ```

7. Lastly, use gcloud to run the image in Google Cloud Run (replace <your-service-name> with any name you want)!

   ```
   gcloud run deploy <your-service-name> --image us-central1-docker.pkg.dev/<your-project-name>/<repository-name>/transcript-app:<tag> --platform managed
   ```

   The command will give you the URL to input into the front end. It will look something like `https://<your-service-name>-<some numbers>.us-central1.run.app`

NOTE: To redeploy a new version of the API, you only need to repeat steps 3, 6, and 7, unless you want to change the configuration for other steps.
