from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from docx import Document

app = FastAPI()

# Optional: for browser testing and Netlify
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use specific domains in production
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/")  # ← this was '/convert-docx', now root
async def convert_docx(file: UploadFile = File(...)):
    doc = Document(file.file)
    text = "\n".join([p.text for p in doc.paragraphs])
    return {"text": text}
