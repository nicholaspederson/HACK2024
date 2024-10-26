import cv2
import pytesseract
import fitz
from pdf2image import convert_from_path
from PIL import Image
import io
import numpy as np
import json



TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

class TranscriptVal:

    def __init__(self, studentData, transcript_path):
        """Initializes transcript validation object.
        Input:
        studentData -> object containing student data in attributes
        transcript_path -> path of file to validate and check
        Returns:
        transcriptVal object for evaluating data against documents"""

        pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

        # Object stores all student data
        self.studentData = studentData
        
        # Store transcript file path
        self.transcript_path = transcript_path

        # Load and store transcript data
        self.transcript_data = self.extract_text_from_pdf()

    def is_blurry(self, image):
        """Checks if an image is blurry based on the Laplacian variance method.
        Input:
        image -> an image in the form of a numpy array
        Returns:
        bool -> True if blurry, False otherwise"""

        gray = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
        laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
        return laplacian_var < self.blur_threshold

    def extract_text_from_pdf(self):
        text = ""
        doc = fitz.open(self.transcript_path)  # Open the PDF document

        for page_num in range(len(doc)):
            # Render the page as an image
            page = doc.load_page(page_num)
            pix = page.get_pixmap()
            
            # Convert the Pixmap to a PIL Image
            #img = Image.open(io.BytesIO(pix.tobytes("png")))
            img = cv2.imdecode(np.frombuffer(pix.tobytes(), np.uint8), cv2.IMREAD_GRAYSCALE)

            # Use tesseract to extract text from image
            page_text = pytesseract.image_to_string(img)
            text += f"\n--- Page {page_num + 1} ---\n"
            text += page_text
        print(text)

        doc.close()

        return text

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
                #if self.is_blurry(image):
                #    print(f"Page {i + 1} is too blurry for OCR.")
                #    continue  # Skip this page if it's too blurry

                text = pytesseract.image_to_string(image)  # OCR on each clear page
                data += text + "\n"  # Append extracted text

            #if not data:
            #    print("All pages were too blurry for OCR.")
            #    return None

            return data
        except Exception as e:
            print(f"An error occurred while reading the PDF with OCR: {e}")
            return None

    def validate_data(self):
        """Validates the loaded transcript data against student data.
        Returns:
        bool -> True if valid, False if discrepancies are found"""

        if not self.transcript_data:
            print("Transcript data not loaded.")
            return False
        
        discrepancies = list() # List to keep track problems

        # Compare attributes from studentData with transcript
        for attribute in vars(self.studentData):
            if attribute != "flag":
                if getattr(self.studentData, attribute) not in self.transcript_data.lower():
                    discrepancies.append(attribute)

        return discrepancies






