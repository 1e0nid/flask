from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def main_window():
    return 'Миссия Колонизация Марса123123'


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def text():
    main_text = ['Человечество вырастает из детства.',
                 'Человечеству мала одна планета.',
                 'Мы сделаем обитаемыми безжизненные пока планеты.',
                 'И начнем с Марса!',
                 'Присоединяйся!']
    return '</br>'.join(main_text)


@app.route('/image_mars')
def image():
    return f'<title>Привет, Марс!</title>' f'<h1>Жди нас, Марс!</h1></br>' f'''<img src="{url_for('static',
                                                                                                  filename='img/mars.jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась">'''


@app.route('/promotion_image')
def promotive():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-primary" role="alert">
                    <h2>Человечество вырастает из детства</h2>
                    </div>
                    <div class="p-3 mb-2 bg-primary text-white">
                    <h2>Человечеству мала одна планета</h2>
                    </div>
                    <div class="p-3 mb-2 bg-secondary text-white">
                    <h2>Мы сделаем обитаемыми безжизненныу пока планеты</h2>
                    </div>
                    <div class="p-3 mb-2 bg-success text-white">
                    <h2>И начнем с Марса</h2>
                    </div>
                    <div class="p-3 mb-2 bg-danger text-white">
                    <h2>Присоединяйся</h2>
                    </div>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.2')
