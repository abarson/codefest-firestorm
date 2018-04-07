import sys
import PyPDF2 as pyPdf
import docx
import pytesseract
import os
from PIL import Image


def get_filetype(filename):
    """
    return the file extension of a filename
    """

    if filename.endswith(".png"):
        return "png"

    if filename.endswith(".docx"):
        return "docx"

    if filename.endswith(".pdf"):
        return "pdf"


def getPDFcontent(path):
    """
    convert a pdf to plain text
    """
    
    content = ""
    
    # load into pypdf
    pdf = pyPdf.PdfFileReader(open(path, "rb"))
    
    # iterate page
    for i in range(0, pdf.getNumPages()):
        # extract text from page
        content += pdf.getPage(i).extractText() + "\n"

    # collapse whitespace
    content = u" ".join(content.replace(u"\xa0", u" ").strip().split())
    return content


def getDOCXcontent(path):
    """
    convert a docx to plain text
    """
    
    doc = docx.Document(path)
    fullText = []

    for para in doc.paragraphs:
        fullText.append(para.text)

    return "\n".join(fullText)


def getPNGcontent(path):
    """
    convert a png to plain text using pytesseract ocr model
    """
    
    tess_path = get_tesseract_path()
    
    pytesseract.pytesseract.tesseract_cmd = tess_path
    return pytesseract.image_to_string(Image.open(path), lang="eng")


def get_tesseract_path():
    platforms = {"linux1": "Linux",
                 "linux2": "Linux",
                 "darwin": "OS X"}
    
    exes = {"Linux": "models/tesseract_linux", "OS X": "models/tesseract_osx"}
    
    if sys.platform in platforms:
        return exes[platforms[sys.platform]]


def convert(filename):
    ft = get_filetype(filename)
    
    no_extension = filename.split(".")[0]

    os.environ['TESSDATA_PREFIX'] = 'models/' 
    with open(no_extension + ".txt", "w+") as f:
        if ft == "pdf":
            f.write(getPDFcontent(filename)) 
            
            # return f.__name__

        elif ft == "docx":
            f.write(getDOCXcontent(filename))
        
        elif ft == "png":
            
            f.write(getPNGcontent(filename))


if __name__ == "__main__":
    p = "daniel_berenberg_224_hw7.pdf"
    convert(p)

    d = "Week2.docx"
    convert(d)

    pg = "img.png"
    convert(pg)
