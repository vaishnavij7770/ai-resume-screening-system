import nltk
import spacy
from nltk.corpus import stopwords

nltk.download("stopwords")
nlp = spacy.load("en_core_web_sm")
stop_words = set(stopwords.words("english"))

SKILLS_DB = [
    "python", "machine learning", "deep learning",
    "nlp", "sql", "flask", "fastapi", "tensorflow",
    "pytorch", "docker", "aws"
]

def clean_text(text):
    text = text.lower()
    doc = nlp(text)
    tokens = [
        token.text for token in doc
        if token.text.isalpha() and token.text not in stop_words
    ]
    return " ".join(tokens)

def extract_skills(text):
    text = text.lower()
    found_skills = []
    for skill in SKILLS_DB:
        if skill in text:
            found_skills.append(skill)
    return found_skills
