from flask import Flask, request, jsonify
from flask_cors import CORS
from main import glossing_machine   # импортируем твою главную функцию

app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    gloss_text = data.get('glossed', '')
    tags_text = data.get('tags', '')

    if not gloss_text or not tags_text:
        return jsonify({'analysis': 'Ошибка: нужны оба поля — глоссы и теги.'})

    # Вызываем твою функцию
    result = glossing_machine(gloss_text, tags_text)

    # result — это готовая строка, возвращаем её в JSON
    return jsonify({'analysis': result})

if __name__ == '__main__':
    app.run(debug=True)
