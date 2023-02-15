from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def main_window():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def text():
    main_text = ['Человечество вырастает из детства.',
                 'Человечеству мала одна планета.',
                 'Мы сделаем обитаемыми безжизненные пока планеты.',
                 'И начнем с Марса!',
                 'Присоединяйся213!']
    return '</br>'.join(main_text)


@app.route('/image_mars')
def image():
    return f'<title>Привет, Марс!</title>' f'<h1>Жди нас, Марс!</h1></br>' f'''<img src="{url_for('static', filename='img/mars.jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась">'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')