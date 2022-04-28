from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def get_html():
    text = ""
    with open('index.html', 'r') as html_file:
        for line in html_file.readlines():
            text += line.replace("\n", " ")
    return text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5002')