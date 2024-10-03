from flask import Flask, request, jsonify, render_template
from googletrans import Translator
from flask_cors import CORS

app = Flask(__name__)
translator = Translator()
CORS(app)

# 支援的語言及代碼
supported_languages = {
    
    "English": "en",
    "Traditional Chinese": "zh-TW",
    "Hebrew": "he",
    "Spanish": "es",
    "Hindi": "hi",
    "French": "fr",
    "Croatian": "hr",
    "German": "de",
    "Hungarian": "hu",
    "Simplified Chinese": "zh-CN",
    
    "Japanese": "ja",
    "Korean": "ko",
    "Russian": "ru",
    "Portuguese": "pt",
    "Arabic": "ar",
    "Danish": "da",
    "Bengali": "bn",
    "Bulgarian": "bg",
    "Catalan": "ca",
    "Czech": "cs",
    "Dutch": "nl",
    "Finnish": "fi",
    "Greek": "el",
    "Thai": "th",
    "Ukrainian": "uk",
    "Vietnamese": "vi",
    "Filipino": "tl",
    "Georgian": "ka",
    "Gujarati": "gu",
    "Persian": "fa",
    "Pashto": "ps",
    "Swahili": "sw",
    "Tamil": "ta",
    "Telugu": "te",
    "Malayalam": "ml",
    "Marathi": "mr",
    "Nepali": "ne",
    "Sinhala": "si",
    "Kannada": "kn",
    "Kurdish": "ku",
    "Lao": "lo",
    "Khmer": "km",
    "Uzbek": "uz",
    "Kyrgyz": "ky",
    "Tibetan": "bo",
    "Afrikaans": "af",
    "Serbian (Latin)": "sr-Latn",
    "Serbian (Cyrillic)": "sr-Cyrl",
    "Bosnian (Latin)": "bs-Latn",
    "Bosnian (Cyrillic)": "bs-Cyrl",
}

# 語言名稱對應
language_names = {
    "en": "English",
    "zh-TW": "繁體中文",
    "ja": "日本語",
}

# 首頁路由
@app.route('/')
def index():
    return render_template('index.html', languages=language_names)

# 翻譯 API 路由
@app.route('/translate', methods=['POST'])
def translate_text():
    try:
        data = request.json
        text = data.get('text')
        src_lang = data.get('src_lang', 'auto')  # 默認為自動偵測
        dest_lang = data.get('dest_lang', 'en')

        if not text:
            return jsonify({
                "error": "Text not provided",
                "message": "Please make sure to include the text you want to translate."
            }), 400

        translated = translator.translate(text, src=src_lang, dest=dest_lang)
        return jsonify({
            "original_text": text,
            "translated_text": translated.text,
            "src_lang": translated.src,
            "dest_lang": dest_lang,
            "message": "Translation successful!"
        })

    except Exception as e:
        return jsonify({
            "error": "Translation service failed",
            "message": f"An error occurred: {str(e)}. Please try again later or contact support."
        }), 500

# 語言 API 路由
@app.route('/languages', methods=['GET'])
def get_languages():
    return jsonify(supported_languages)

if __name__ == '__main__':
    app.run(port=10000, host='0.0.0.0', debug=True)
