from flask import Flask, render_template
import random

app = Flask(__name__)

def get_quotes():
    with open('templates/quotes.txt', 'r') as file:
        quotes = file.read().splitlines()
    return quotes

quotes = get_quotes()

@app.route('/')
def show_quote():
    quote = random.choice(quotes)
    return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

