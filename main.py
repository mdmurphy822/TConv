from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from docx import Document

app = FastAPI()

# Optional: Allow CORS if calling from browser directly
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your frontend domain in production
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/convert-docx")
async def convert_docx(file: UploadFile = File(...)):
    document = Document(file.file)
    text = "\n".join([para.text for para in document.paragraphs])
    return {"text": text}
