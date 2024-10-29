from flask import Flask, render_template
import os
import random

app = Flask(__name__)

@app.route('/')
def home():
    image_folder = os.path.join('static', 'popup_images')  # Correct path to popup_images
    images = os.listdir(image_folder)  # Get all image files in the directory
    random_image = random.choice(images)  # Pick a random image

    # List of random messages
    messages = [
        "did you know this is created by a 16 year old boy with chatgpt ",
        "this background changes according to time",
        "refreshing the website will give a different popup image",
        "is this website usefull?",
        "whats the time bro",
        "One Piece is real"
    ]
    random_message = random.choice(messages)  # Pick a random message

    return render_template('index.html', random_image=random_image, random_message=random_message)

if __name__ == '__main__':
    app.run(debug=True)
