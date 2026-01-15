from werkzeug.utils import secure_filename
from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates

from resume_parser import extract_resume_text
from skill_extractor import clean_text, extract_skills
from matcher import bert_similarity

from werkzeug.utils import secure_filename
import os
import shutil

app = FastAPI()

templates = Jinja2Templates(directory="templates")

UPLOAD_RESUME = "uploads/resumes/"
UPLOAD_JD = "uploads/jds/"
OUTPUT_DIR = "output/"

os.makedirs(UPLOAD_RESUME, exist_ok=True)
os.makedirs(UPLOAD_JD, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "show_download": False}
    )


@app.post("/", response_class=HTMLResponse)
async def analyze(
    request: Request,
    resume: UploadFile = File(...),
    jobdesc: UploadFile = File(...)
):
    resume_name = secure_filename(resume.filename)
    jd_name = secure_filename(jobdesc.filename)

    resume_path = os.path.join(UPLOAD_RESUME, resume_name)
    jd_path = os.path.join(UPLOAD_JD, jd_name)

    # Save uploaded files
    with open(resume_path, "wb") as f:
        shutil.copyfileobj(resume.file, f)

    with open(jd_path, "wb") as f:
        shutil.copyfileobj(jobdesc.file, f)

    # NLP processing
    resume_text = extract_resume_text(resume_path)
    jd_text = extract_resume_text(jd_path)

    clean_resume = clean_text(resume_text)
    clean_jd = clean_text(jd_text)

    score = bert_similarity(clean_resume, clean_jd)
    skills = extract_skills(resume_text)

    output_file = os.path.join(OUTPUT_DIR, f"result_{resume_name}.txt")

    # Write downloadable result
    with open(output_file, "w") as f:
        f.write("AI RESUME SCREENING REPORT\n")
        f.write("=" * 35 + "\n\n")
        f.write(f"Match Score: {score}%\n\n")
        f.write("Extracted Skills:\n")
        for s in skills:
            f.write(f"- {s}\n")

        f.write("\nDecision:\n")
        f.write("SHORTLIST\n" if score >= 70 else "REJECT\n")

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "score": score,
            "skills": skills,
            "show_download": True,
            "file_name": os.path.basename(output_file)
        }
    )


@app.get("/download/{file_name}")
async def download(file_name: str):
    file_path = os.path.join(OUTPUT_DIR, file_name)
    return FileResponse(file_path, media_type="text/plain", filename=file_name)
