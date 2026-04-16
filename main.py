from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_2026'


@app.route('/')
@app.route('/index')
def index():
    """Одностраничный сайт лагеря"""
    return render_template('index.html', title='Пришкольный лагерь Лицея №3')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
