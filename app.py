from flask import Flask
from flask import render_template, request
from summarizer import text_summarization

app = Flask(__name__)

# from app import main

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = None
    if request.method == 'POST':
        input_text = request.form.get('input_text')
        num_sentences = int(request.form.get('num_sentences', 3))
        if input_text:
            summary = text_summarization(input_text, num_sentences)
    
    return render_template('index.html', summary=summary)


if __name__ == '__main__':
    app.run(debug=True)