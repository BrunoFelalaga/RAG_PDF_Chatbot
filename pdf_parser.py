# pdf_parser.py
from PyPDF2 import PdfReader
from docx import Document
from langchain.text_splitter import CharacterTextSplitter

# Custom exception class
class NoUploadedFileError(Exception):
    pass

# method to get text from pdf docs into a text string
def get_pdf_text(pdf_doc):
    # Read content of pdf_docs page by page and add to text string
    text_string = ""

    for pdf in pdf_doc:
        pdf_reader = PdfReader(pdf)
        # pdf_reader = PdfReader(pdf.read())  # Read the bytes content
        for page in pdf_reader.pages:
            text_string += page.extract_text()

    return text_string


# method to get text from docx files into a text string
def get_text_from_docx(docx_file):
    doc = Document(docx_file)
    text_string = ""
    for paragraph in doc.paragraphs:
        text_string += paragraph.text + "\n"
    return text_string

# general method to get text from both pdfs and docx docs into a text string.
# here we use the helper methods above
def get_text_from_files(pdf_docs):
    if not pdf_docs:
        raise NoUploadedFileError(f"Upload file to begin parsing")
    raw_text = ""

    for file in pdf_docs:
        
        if file.name.endswith(".pdf"):

            raw_text += get_pdf_text([file]) # pass file in as a list

            
        elif file.name.endswith(".docx"):
            raw_text += get_text_from_docx(file)
        
        else:
            return "Unsupported file type"
    
    return raw_text


# use text splitter from langchain to split text into chunks
# the chunks use an overlap to allow for chunks to overlap. 
# By doing this when splitting is done such that meaning is lost, 
# the overlap of about two hundred words between chunks makes it so meaning can be reconstructed
def get_text_chunks(raw_text):
    text_splitter = CharacterTextSplitter(
        separator="\n", 
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )

    # Get list of split text with the specifications above
    chunks = text_splitter.split_text(raw_text)
    return chunks