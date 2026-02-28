
import spacy

#Modèle NLP chargé
# Modèle spaCy
try:
    nlp = spacy.load("fr_core_news_sm")

except OSError:
    print("⚠️  Modèle spaCy 'fr_core_news_sm' non trouvé.")
    print("👉 Installez-le avec : python -m spacy download fr_core_news_sm")
    nlp = None

# Stopwords
try:
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('french'))
except LookupError:
    import nltk
    nltk.download('stopwords')
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('french'))

custom_stopwords = {
    "serait", "un", "une", "et", "de", "des", "en", "dans", "la", "le", "les", "du", "au", "aux",
    "ou", "car", "donc", "or", "ni", "par", "pour", "sur", "avec", "sans", "trop", "plus", "tres",
    "très", "cela", "ca", "ça", "ce", "mes", "tes", "ses", "son", "leur", "leurs","e", "se","trice","trices","a",
    "specialiste", "stagiaire", "junior", "senior",
    "technicien","superviseur","responsable",
    "agent","manager","assistant",
    "stage","stagiaire",
    "vendeur","secretaire",
    "support","web","specialiste",
    "chef","sdr","software","developer","developpeur"
}
stop_words.update(custom_stopwords)

stop_words = list(stop_words) 

