from langdetect import detect
from .models import LinguisticData

def extract_linguistic_data(text):
    if not text:
        return {"error": "No text provided"}
    
    # Detect language
    language = detect(text)

    # Calculate linguistic statistics
    word_count = len(text.split())
    char_count = len(text)
    avg_word_length = sum(len(word) for word in text.split()) / word_count if word_count else 0
    
    # Create and save the linguistic data object
    linguistic_data = LinguisticData.objects.create(
        version_id="v1.0",
        word_count=word_count,
        char_count=char_count,
        avg_word_length=avg_word_length,
        language=language,
        original_text=text
    )

    return {
        "id": linguistic_data.id,
        "version_id": linguistic_data.version_id,
        "word_count": linguistic_data.word_count,
        "char_count": linguistic_data.char_count,
        "avg_word_length": linguistic_data.avg_word_length,
        "language": linguistic_data.language,
        "original_text": linguistic_data.original_text
    }

