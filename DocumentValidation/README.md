# Document Validation Team Documentation

## Current Implementation
### Outlined Structure
Our Document validation system takes student data (a .json file) as input. Then to validate a transcript we converted each pdf image into the form of text. For this transcript string produced, we search for the expected student data, and flag (add the attribute name to a list) each instance where student information is not found within the converted text. A flag is then paired with student data for output into the google drive team.

### Technical Tools
In our implementation of the document validation system, we used the Tesseract and OpenCV to read text off of a pdf. OpenCV was utilized to convert the pdf into a png file. Tesseract then takes the png file and extracts readable text elements to be compared against the given student data.

## Validation Process
The student data with all the information on the student was used to check through the pdf to see any matches. If a match was not found, the non-match was denoted in a list that keeps track of all the non-matches. This list was returned to express all the attributes that were not found. This can be used as a flag to check if a certain attribute was found.

## Possible Errors
One major issue was searching for the gender of a person which could be denoted in a variety of ways. Therefore, the accuracy for this particular field was not great. However, looking for specific words like someone’s name was fairly accurate. Also, searching for specific words like “Transcript” could be easily implemented. 

## Future Recommendations
### Overview
The current implementation is extremely limited by image quality, being unable to deal with noise, image rotation, etc. The implementation tends to flag much more aggressively than desired due almost entirely to limitations in extracting data from the model. Using more robust tools for extraction of data would provide a much more powerful tool for automating the document validation workflow. The implementation of **student_data.py** is somewhat compatible with a potential database implementation in the future.

### Recommended Tools
Without a much larger dataset of both good and bad transcripts to pull from, it would be extremely difficult to make a more robust approach (probably based on some machine learning methods). The best way around this, in our opinion, is to utilize API tools from companies such as Google. Google's [Document AI API](https://cloud.google.com/document-ai/docs/reference/rest) is an exceptional tool for this, allowing for definition of fields which Google's AI will search for in a given document and fill out with informaiton it deems relevant. The cost should be low (~$30/1,000 transcripts). This can be further enhanced with Gemini or OpenAI's tools to provide an easily read and understood summary of the issue and potential resolutions. This could be linked with the AI assistant already in development. 

The possibility to extend to different translations also exists with the inclusion of Google's [Translation API](https://cloud.google.com/translate/docs/reference/rest), though Google's Document AI may also include this capability.

The inclusion of these robust tools would be the most optimal way to integrate with Google drive and utilize the capability of well-understood, widely used models for maximal accuracy.

### Other Potential Options
Local options exist as well which utilize Machine Learning Packages (Keras, PyTorch, etc.) or Computer Vision (OpenCV) to determine if certain features exist within a document. These tools may be used to verify a transcript is official, but likely will be unhelpful for anything more. These tools could be helpful for determining if a document is blurry or invalid for some other, more obvious reason. 
