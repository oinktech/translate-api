from flask import Flask, request, jsonify
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/translate', methods=['POST'])
def translate_text():
    try:
        data = request.json
        text = data.get('text')
        dest_lang = data.get('dest_lang', 'en')  # 目标语言，默认英文

        if not text:
            return jsonify({"error": "No text provided"}), 400

        # 自动检测源语言并翻译
        translated = translator.translate(text, dest=dest_lang)
        return jsonify({
            "original_text": text,
            "translated_text": translated.text,
            "src_lang": translated.src,  # 自动检测的源语言
            "dest_lang": dest_lang
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=10000, host='0.0.0.0',debug=True)
