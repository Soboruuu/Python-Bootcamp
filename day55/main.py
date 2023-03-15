from flask import Flask
from random import randint

random_number = randint(0,10)
print(random_number)

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>0과 9사이의 숫자를 맞추세요</h1>' \
           '<img src="https://i.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.webp" width=200px;>'

@app.route('/<int:guess>')
def number_guess(guess):
    if guess > random_number:
        return '<h1> 더 작은 숫자로 다시 골라보세요! </h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    elif guess < random_number:
        return '<h1> 더 큰 숫자로 다시 골라보세요! </h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    else:
        return '<h1> 맞췄습니다! </h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'

if __name__ == "__main__":
    app.run(debug=True, port=5001)
