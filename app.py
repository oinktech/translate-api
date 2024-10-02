from flask import Flask, request, jsonify,render_template
from googletrans import Translator
from flask_cors import CORS

app = Flask(__name__)
translator = Translator()
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate_text():
    try:
        # 获取请求的 JSON 数据
        data = request.json
        print("接收到的資料:", data)  # 输出接收到的数据
        text = data.get('text')
        dest_lang = data.get('dest_lang', 'en')  # 目标语言，默认英文

        # 检查是否提供文本
        if not text:
            return jsonify({
                "error": "未提供文本",
                "message": "請確保您在請求中包含要翻譯的文本。"
            }), 400

        # 自动检测源语言并翻译
        translated = translator.translate(text, dest=dest_lang)
        return jsonify({
            "original_text": text,
            "translated_text": translated.text,
            "src_lang": translated.src,  # 自动检测的源语言
            "dest_lang": dest_lang,
            "message": "翻譯成功！"  # 成功的反馈信息
        })

    except Exception as e:
        print("發生錯誤:", str(e))  # 打印错误信息
        return jsonify({
            "error": "翻譯服務失敗",
            "message": f"發生錯誤: {str(e)}。請稍後再試或聯繫技術支持。"
        }), 500

if __name__ == '__main__':
    app.run(port=10000, host='0.0.0.0', debug=True)
