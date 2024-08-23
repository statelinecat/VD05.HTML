from flask import Flask, render_template

# Создаем экземпляр приложения Flask
app = Flask(__name__)

# Определяем маршруты для страниц
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/blog')
def blog():
    return render_template('about.html')

# @app.route('/contacts')
# def contacts():
#     return render_template('contacts.html')

# Запуск приложения
if __name__ == '__main__':
    app.run(debug=True)
