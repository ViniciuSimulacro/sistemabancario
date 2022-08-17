from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Sistema bancário Simulacro Inc.'


if __name__ == '__main__':
    app.run()