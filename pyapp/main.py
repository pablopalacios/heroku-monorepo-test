from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return 'hello world'


if __name__ == '__main__':
    import os
    port = os.environ.get('PORT', 8000)
    app.run(port=port)
