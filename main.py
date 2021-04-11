from flask import *

app = Flask(__name__)


@app.route('/')
def render_home_page():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
