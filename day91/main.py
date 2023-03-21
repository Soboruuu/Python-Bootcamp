from flask import Flask, render_template, request
from PIL import Image
import extcolors


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        f = request.files['file']
        img = Image.open(f)
        colors, pixel_count = extcolors.extract_from_image(img)
        sorted_colors = sorted(colors, key=lambda x: x[0], reverse=True)[:10]
        hex_colors = [(color[1], '#{:02x}{:02x}{:02x}'.format(*color[0])) for color in sorted_colors]
        return render_template('result.html', colors=hex_colors)

if __name__ == '__main__':
    app.run(debug=True)
