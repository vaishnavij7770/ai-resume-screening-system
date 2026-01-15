from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from sentence_transformers import SentenceTransformer, util

# Load BERT model once
bert_model = SentenceTransformer("all-MiniLM-L6-v2")

# ---------- TF-IDF MATCHING ----------
def calculate_similarity(resume_text, jd_text):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, jd_text])
    similarity = cosine_similarity(vectors[0], vectors[1])
    return round(similarity[0][0] * 100, 2)

# ---------- BERT MATCHING (ADVANCED) ----------
def bert_similarity(resume_text, jd_text):
    emb1 = bert_model.encode(resume_text, convert_to_tensor=True)
    emb2 = bert_model.encode(jd_text, convert_to_tensor=True)
    score = util.cos_sim(emb1, emb2)
    return round(float(score) * 100, 2)
