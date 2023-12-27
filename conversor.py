import os
import PyPDF2
import pyttsx3

from leitor_texto import TextExtractor

class PDFConverter:

    def __init__(self, file_path):
        self.file_path = file_path
        self.output_path = os.path.splitext(file_path)[0] + ".mp3"

    def convert_to_mp3(self):
        with open(self.file_path, "rb") as file:
            text_extractor = TextExtractor(file)
            text = text_extractor.extract_text()

            engine = pyttsx3.init()
            engine.setProperty("rate", 200)
            engine.setProperty("volume", 1.0)
            engine.setProperty("pitch", 0.8)
            engine.save_to_file(text, self.output_path)
            engine.runAndWait()