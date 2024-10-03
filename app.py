from flask import Flask, request, jsonify, render_template
from googletrans import Translator
from flask_cors import CORS
import logging

app = Flask(__name__)
translator = Translator()
CORS(app)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Supported languages and codes
supported_languages = {
    "English": "en",
    "Hebrew": "he",
    "Spanish": "es",
    "Hindi": "hi",
    "French": "fr",
    "Croatian": "hr",
    "German": "de",
    "Hungarian": "hu",
    "Simplified Chinese": "zh-CN",
    "Traditional Chinese": "zh-TW",
    "Japanese": "ja",
    "Korean": "ko",
    "Russian": "ru",
    "Portuguese": "pt",
    "Arabic": "ar",
    # Additional languages
    "Bengali": "bn",
    "Bulgarian": "bg",
    "Catalan": "ca",
    "Czech": "cs",
    "Danish": "da",
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

# Chinese and Japanese versions of supported languages
supported_languages_zh_tw = {
    "英文": "en",
    "希伯來文": "he",
    "西班牙文": "es",
    "印地文": "hi",
    "法文": "fr",
    "克羅埃西亞文": "hr",
    "德文": "de",
    "匈牙利文": "hu",
    "簡體中文": "zh-CN",
    "繁體中文": "zh-TW",
    "日文": "ja",
    "韓文": "ko",
    "俄文": "ru",
    "葡萄牙文": "pt",
    "阿拉伯文": "ar",
    # Additional languages
    "孟加拉文": "bn",
    "保加利亞文": "bg",
    "加泰羅尼亞文": "ca",
    "捷克文": "cs",
    "丹麥文": "da",
    "荷蘭文": "nl",
    "芬蘭文": "fi",
    "希臘文": "el",
    "泰文": "th",
    "烏克蘭文": "uk",
    "越南文": "vi",
    "菲律賓文": "tl",
    "喬治亞文": "ka",
    "古吉拉特文": "gu",
    "波斯文": "fa",
    "普什圖文": "ps",
    "斯瓦希里文": "sw",
    "泰米爾文": "ta",
    "泰盧固文": "te",
    "馬拉雅拉姆文": "ml",
    "馬拉地文": "mr",
    "尼泊爾文": "ne",
    "僧伽羅文": "si",
    "坎那達文": "kn",
    "庫爾德文": "ku",
    "老撾文": "lo",
    "高棉文": "km",
    "烏茲別克文": "uz",
    "吉爾吉斯文": "ky",
    "藏文": "bo",
    "南非荷蘭文": "af",
    "塞爾維亞文（拉丁）": "sr-Latn",
    "塞爾維亞文（西里爾）": "sr-Cyrl",
    "波斯尼亞文（拉丁）": "bs-Latn",
    "波斯尼亞文（西里爾）": "bs-Cyrl",
}

supported_languages_ja = {
    "英語": "en",
    "ヘブライ語": "he",
    "スペイン語": "es",
    "ヒンディー語": "hi",
    "フランス語": "fr",
    "クロアチア語": "hr",
    "ドイツ語": "de",
    "ハンガリー語": "hu",
    "簡体中国語": "zh-CN",
    "繁体中国語": "zh-TW",
    "日本語": "ja",
    "韓国語": "ko",
    "ロシア語": "ru",
    "ポルトガル語": "pt",
    "アラビア語": "ar",
    # Additional languages
    "ベンガル語": "bn",
    "ブルガリア語": "bg",
    "カタルーニャ語": "ca",
    "チェコ語": "cs",
    "デンマーク語": "da",
    "オランダ語": "nl",
    "フィンランド語": "fi",
    "ギリシャ語": "el",
    "タイ語": "th",
    "ウクライナ語": "uk",
    "ベトナム語": "vi",
    "フィリピン語": "tl",
    "グルジア語": "ka",
    "グジャラート語": "gu",
    "ペルシア語": "fa",
    "パシュトー語": "ps",
    "スワヒリ語": "sw",
    "タミル語": "ta",
    "テルグ語": "te",
    "マラヤーラム語": "ml",
    "マラーティー語": "mr",
    "ネパール語": "ne",
    "シンハラ語": "si",
    "カンナダ語": "kn",
    "クルド語": "ku",
    "ラオ語": "lo",
    "クメール語": "km",
    "ウズベク語": "uz",
    "キルギス語": "ky",
    "チベット語": "bo",
    "アフリカーンス語": "af",
    "セルビア語（ラテン文字）": "sr-Latn",
    "セルビア語（キリル文字）": "sr-Cyrl",
    "ボスニア語（ラテン文字）": "bs-Latn",
    "ボスニア語（キリル文字）": "bs-Cyrl",
}

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Translation API route
@app.route('/translate', methods=['POST'])
def translate_text():
    try:
        data = request.json
        text = data.get('text')
        src_lang = data.get('src_lang', 'auto')  # Default is auto-detection
        dest_lang = data.get('dest_lang', 'en')

        if not text:
            return jsonify({
                "error": "Text not provided",
                "message": "Please make sure to include the text you want to translate."
            }), 400

        # Log the translation request
        logging.info(f"Translating text: '{text}' from {src_lang} to {dest_lang}")

        translated = translator.translate(text, src=src_lang, dest=dest_lang)

        return jsonify({
            "original_text": text,
            "translated_text": translated.text,
            "src_lang": translated.src,
            "dest_lang": dest_lang,
            "message": "Translation successful!"
        })

    except Exception as e:
        logging.error(f"Translation error: {str(e)}")
        return jsonify({
            "error": "Translation service failed",
            "message": f"An error occurred: {str(e)}. Please try again later or contact support."
        }), 500

# Language API routes
@app.route('/languages', methods=['GET'])
def get_languages_en():
    return jsonify(supported_languages)

@app.route('/languages-zh-tw', methods=['GET'])
def get_languages_zh_tw():
    return jsonify(supported_languages_zh_tw)

@app.route('/languages-ja', methods=['GET'])
def get_languages_ja():
    return jsonify(supported_languages_ja)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
