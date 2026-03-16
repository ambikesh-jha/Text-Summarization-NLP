# Automatic Text Summarization Tool

A simple yet powerful web application that automatically generates summaries from text using extractive summarization techniques. Built with Flask and NLTK, this tool helps users quickly grasp the main points of any text by extracting the most important sentences.

## Features
- Extract key sentences from any text
- Customizable summary length (1-10+ sentences)
- Real-time text processing
- Automatic stop word removal and punctuation filtering
- Frequency-based sentence scoring
- Clean, responsive web interface
- NLTK-powered NLP processing

## How It Works
1. **Tokenization**: Splits text into sentences and words
2. **Word Frequency Analysis**: Counts word occurrences (excluding stop words)
3. **Normalization**: Normalizes frequencies by the maximum frequency
4. **Sentence Scoring**: Scores sentences based on word frequencies
5. **Extraction**: Selects top-scoring sentences for the summary

## Tech Stack
- **Backend**: Flask (Python)
- **NLP**: NLTK (punkt tokenizer, stopwords corpus)
- **Frontend**: HTML5, CSS3

## Installation

Clone the repository
   git clone https://github.com/yourusername/text-summarization.git
   cd text-summarization

