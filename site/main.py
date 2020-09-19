import logging

from flask import Flask, render_template

logging.basicConfig(level=logging.ERROR)
app = Flask(__name__)
app.config['SECRET_KEY'] = 'DFDVfvfd5fdxv5565856gfbgfbgvbmLKJLGUIl5tfh5ghTHRGHFGHfg985248202h0tgsfd'


# /////////////////
# ГЛАВНАЯ СТРАНИЦА
# /////////////////
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', title="KSA")


if __name__ == '__main__':
    app.run()
