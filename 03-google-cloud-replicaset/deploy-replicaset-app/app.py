import os

from flask import Flask
from random_unicode_emoji import random_emoji

app = Flask(__name__)

@app.route('/')
def smiley():
    emoji_list = random_emoji()
    emoji = emoji_list[0]  # Extract the emoji from the list
    return f"<h1>{emoji}</h1>"

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))