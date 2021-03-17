from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/home')
def home():
    return

if __name__ == '__main__':
    app.run()
