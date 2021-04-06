from pdfminer.high_level import extract_text
 
FILE_PATH = "sample.pdf"
 
text = extract_text(FILE_PATH)
print(text)