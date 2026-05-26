from flask import Flask, request, jsonify
from flask_cors import CORS   # чтобы GitHub Pages мог обращаться к API
# импортируйте ваши функции, например:
# from main import analyze_glosses  – но пока сделаем заглушку

app = Flask(__name__)
CORS(app)  # разрешает запросы с любых сайтов

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    gloss_text = data.get('text', '')

    # Здесь вы вызываете ваши три детектора и format_guess
    # Пока для примера вернём эхо
    result = {
        'analysis': f'Вы ввели: {gloss_text}\nАреалы: ...'  # ваша реальная строка
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
