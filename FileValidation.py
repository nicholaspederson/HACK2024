import cv2
import pytesseract
from pdf2image import convert_from_path


class TranscriptVal:

    def __init__(self, studentData, transcript_path):
        """Initializes transcript validation object.
        Input:
        studentData -> object containing student data in attributes
        transcript_path -> path of file to validate and check
        Returns:
        transcriptVal object for evaluating data against documents"""

        # Object stores all student data
        self.studentData = studentData
        
        # Store transcript file path
        self.transcript_path = transcript_path


        # Load and store transcript data
        self.transcript_data = self.load_transcript(transcript_path)

    def is_blurry(self, image):
        """Checks if an image is blurry based on the Laplacian variance method.
        Input:
        image -> an image in the form of a numpy array
        Returns:
        bool -> True if blurry, False otherwise"""

        gray = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
        laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
        return laplacian_var < self.blur_threshold

    def load_transcript(self, path):
        """Loads transcript data from a PDF file using Tesseract OCR if pages are not blurry.
        Input:
        path -> path of the PDF transcript file to load
        Returns:
        data -> Parsed text data from the PDF file"""

        try:
            data = ""
            images = convert_from_path(path)  # Convert each page of the PDF to an image
            for i, image in enumerate(images):
                if self.is_blurry(image):
                    print(f"Page {i + 1} is too blurry for OCR.")
                    continue  # Skip this page if it's too blurry

                text = pytesseract.image_to_string(image)  # OCR on each clear page
                data += text + "\n"  # Append extracted text

            if not data:
                print("All pages were too blurry for OCR.")
                return None

            return data
        except Exception as e:
            print(f"An error occurred while reading the PDF with OCR: {e}")
            return None






