# 🤖 AI Resume Screening System

An AI-powered Resume Screening System that automatically analyzes resumes and job descriptions using Natural Language Processing (NLP) and BERT to generate a matching score and screening report.

---

## 📌 Features

- Upload Resume (PDF / DOCX)
- Upload Job Description (PDF / DOCX)
- Extract resume skills using NLP
- Semantic matching using BERT
- Match score generation
- Automatic shortlist / reject decision
- Downloadable screening report
- Web-based interface

---

## 🧠 Technologies Used

- Python
- FastAPI
- NLP (NLTK, spaCy)
- BERT (Sentence Transformers)
- HTML, CSS
- Uvicorn

---

## 🏗️ Project Architecture

Resume & JD Upload (UI)
↓
Text Extraction (PDF/DOCX)
↓
Text Cleaning (NLP)
↓
Skill Extraction
↓
BERT Similarity Matching
↓
Match Score + Decision
↓
Downloadable Report



---

## 📁 Project Structure

ai-resume-screening/
│
├── main.py
├── matcher.py
├── resume_parser.py
├── skill_extractor.py
├── requirements.txt
├── README.md
│
├── templates/
│ └── index.html
│
├── uploads/
│ ├── resumes/
│ └── jds/
│
├── output/
│
└── .gitignore



---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/<your-username>/ai-resume-screening-system.git
cd ai-resume-screening-system
2️⃣ Create Virtual Environment
bash
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install Dependencies
bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
▶️ Run the Project
bash
uvicorn main:app --reload
Open browser:
http://127.0.0.1:8000
🧪 How It Works
User uploads resume and job description

System extracts text from files

NLP cleans and processes text

BERT model computes semantic similarity

Match score is generated

System recommends SHORTLIST or REJECT

Downloadable result file is created

📄 Sample Output

Match Score: 82%

Extracted Skills:
- Python
- NLP
- Flask

Decision:
SHORTLIST
🚀 Future Enhancements
Multiple resume ranking

Resume feedback generation

PDF report download

User authentication

Cloud deployment

Bias reduction in screening

🎓 Use Cases
HR Resume Screening

Applicant Tracking Systems (ATS)

Final Year Engineering Project

AI / NLP Research

👩‍💻 Author
Vaishnavi Jadhav
B.Tech Computer Science Engineering


📜 License
This project is for educational and research purposes.
