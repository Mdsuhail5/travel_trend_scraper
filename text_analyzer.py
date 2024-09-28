# analysis/text_analyzer.py

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import spacy

nltk.download('punkt')
nltk.download('stopwords')
nlp = spacy.load("en_core_web_sm")

def extract_locations(text):
    doc = nlp(text)
    locations = [ent.text for ent in doc.ents if ent.label_ in ['GPE', 'LOC']]
    return locations

def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text.lower())
    filtered_text = [w for w in word_tokens if not w in stop_words]
    return filtered_text

def analyze_text(text):
    locations = extract_locations(text)
    preprocessed_text = preprocess_text(text)
    return {
        'locations': locations,
        'keywords': preprocessed_text
    }