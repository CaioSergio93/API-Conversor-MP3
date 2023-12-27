import os
import PyPDF2
import pyttsx3

class TextExtractor:

    def __init__(self, file):
        self.reader = PyPDF2.PdfReader(file)

    def extract_text(self):
        text = ""
        for i, page in enumerate(self.reader.pages, start=1):
            text += page.extract_text()
        return text