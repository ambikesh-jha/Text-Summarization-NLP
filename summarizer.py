import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import defaultdict
import string

# Download NLTK data files
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

def text_summarization(text, num_sentences=3):
    # Tokenize sentences
    sentences = sent_tokenize(text)
    
    # Tokenize words and remove stop words
    stop_words = set(stopwords.words('english'))
    word_frequencies = defaultdict(int)
    for word in word_tokenize(text):
        word = word.lower()
        if word not in stop_words and word not in string.punctuation:
            word_frequencies[word] += 1
    
    # Normalize word frequencies
    max_frequency = max(word_frequencies.values())
    for word in word_frequencies:
        word_frequencies[word] /= max_frequency
    
    # Score sentences based on word frequencies
    sentence_scores = {}
    for sent in sentences:
        for word in word_tokenize(sent.lower()):
            if word in word_frequencies:
                if len(sent.split(' ')) < 30:  # Consider shorter sentences
                    sentence_scores[sent] = sentence_scores.get(sent, 0) + word_frequencies[word]
    
    # Sort sentences by score and select top sentences
    summarized_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    
    # Join summarized sentences
    summary = ' '.join(summarized_sentences)
    return summary

# # Example text
# text = """
# Automatic text summarization is the process of creating a short and coherent version of a longer document.
# The intention is to reduce the reading time while maintaining the key points of the content. 
# There are two main types of summarization techniques: extractive and abstractive. Extractive summarization selects key phrases or sentences directly from the text. 
# Abstractive summarization involves understanding the content and generating a new summary that may use different words. This technique is more complex but often more human-like.
# """

# # Generate summary
# summary = text_summarization(text)
# print("Original Text:\n", text)
# print("\nSummarized Text:\n", summary)
