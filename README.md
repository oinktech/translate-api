# 🌐 翻譯 API - Translate API

![API](https://img.shields.io/badge/API-Translate-blue?style=for-the-badge)
![Language Detection](https://img.shields.io/badge/Auto%20Language%20Detection-%E2%9C%85-brightgreen?style=for-the-badge)
![JSON Supported](https://img.shields.io/badge/Supports-JSON%20Requests-yellowgreen?style=for-the-badge)
![Flask](https://img.shields.io/badge/Flask-%20Python-orange?style=for-the-badge)
![License](https://img.shields.io/github/license/oinktech/GitHub-Repo-Explorer?style=for-the-badge)

## 🗣️ 選擇語言 | Select Language
- [English](#english)
- [繁體中文](#繁體中文)

---

## 繁體中文

### 概述
**翻譯 API** 提供了一個簡單且有效的方式來在不同語言之間進行文本翻譯，並自動檢測源語言。該 API 設計為易於整合到需要即時翻譯功能的網站和應用程式中。

### 功能
- 🌍 **自動語言檢測**：自動檢測源語言，而無需用戶輸入。
- 📝 **可自定義目標語言**：可翻譯為任何所需語言。
- 🚀 **快速且可擴展**：高性能，適合高流量網站。
- 📄 **基於 JSON 的通信**：使用 JSON 格式進行請求和回應，便於整合。
- 🔒 **安全 API**：支持 HTTPS 確保數據安全。
- 🌐 **廣泛的語言支持**：支持多種語言之間的翻譯。

### 安裝與設置
1. 克隆該儲存庫：
   ```bash
   git clone https://github.com/oinktech/Translate-API.git
   cd Translate-API
   ```

2. 安裝所需的依賴：
   ```bash
   pip install -r requirements.txt
   ```

3. 運行 Flask 伺服器：
   ```bash
   python app.py
   ```

4. API 將可在 `http://127.0.0.1:5000/translate` 訪問。

### API 端點
- **基本 URL**: `https://translate-api-s81i.onrender.com/translate`
- **方法**: POST
- **內容類型**: `application/json`

### 請求格式
```json
{
  "text": "Hello, world",
  "dest_lang": "fr"  // 目標語言
}
```

### JavaScript 示例
```javascript
fetch('https://translate-api-s81i.onrender.com/translate', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    text: 'Hello, world',
    dest_lang: 'es',  // 目標語言：西班牙語
  }),
})
.then(response => response.json())
.then(data => console.log('翻譯的文本:', data.translated_text))
.catch(error => console.error('錯誤:', error));
```

### 回應格式
```json
{
  "original_text": "Hello, world",
  "translated_text": "Hola, mundo",
  "src_lang": "en",  // 檢測到的源語言
  "dest_lang": "es"  // 目標語言
}
```

### 支援的語言及代碼

以下是 API 支援的最常見 100 種語言及其 ISO 639-1 語言代碼的列表：

| 語言                      | 代碼   | 語言                      | 代碼   |
|--------------------------|--------|--------------------------|--------|
| 英文                     | en     | 希伯來文                 | he     |
| 西班牙文                 | es     | 印地文                   | hi     |
| 法文                     | fr     | 克羅地亞文               | hr     |
| 德文                     | de     | 匈牙利文                 | hu     |
| 簡體中文                 | zh-CN  | 冰島文                   | is     |
| 繁體中文                 | zh-TW  | 印度尼西亞文             | id     |
| 日文                     | ja     | 愛爾蘭文                 | ga     |
| 韓文                     | ko     | 意大利文                 | it     |
| 俄文                     | ru     | 拉脫維亞文               | lv     |
| 葡萄牙文                 | pt     | 立陶宛文                 | lt     |
| 阿拉伯文                 | ar     | 馬其頓文                 | mk     |
| 孟加拉文                 | bn     | 馬來文                   | ms     |
| 保加利亞文               | bg     | 挪威文                   | no     |
| 加泰隆尼亞文             | ca     | 波蘭文                   | pl     |
| 捷克文                   | cs     | 羅馬尼亞文               | ro     |
| 丹麥文                   | da     | 塞爾維亞文               | sr     |
| 荷蘭文                   | nl     | 斯洛伐克文               | sk     |
| 芬蘭文                   | fi     | 斯洛文尼亞文             | sl     |
| 希臘文                   | el     | 瑞典文                   | sv     |
| 泰文                     | th     | 土耳其文                 | tr     |
| 烏克蘭文                 | uk     | 烏爾都文                 | ur     |
| 越南文                   | vi     | 威爾士文                 | cy     |
| 菲律賓文                 | tl     | 祖魯文                   | zu     |
| 喬治亞文                 | ka     | 阿塞拜疆文               | az     |
| 古吉拉特文               | gu     | 巴斯克文                 | eu     |
| 波斯文                   | fa     | 白俄羅斯文               | be     |
| 普什圖文                 | ps     | 波士尼亞文               | bs     |
| 孟加拉文                 | bn     | 愛沙尼亞文               | et     |
| 斯瓦希里文               | sw     | 法羅文                   | fo     |
| 塔米爾文                 | ta     | 弗里西文                 | fy     |
| 泰盧固文                 | te     | 加利西亞文               | gl     |
| 馬拉雅拉姆文             | ml     | 海地克里奧爾文           | ht     |
| 馬拉地文                 | mr     | 盧森堡文                 | lb     |
| 尼泊爾文                 | ne     | 馬耳他文                 | mt     |
| 僧伽羅文                 | si     | 蒙古文                   | mn     |
| 坎那達文                 | kn     | 阿爾巴尼亞文             | sq     |
| 庫爾德文                 | ku     | 亞美尼亞文               | hy     |
| 寮文                     | lo     | 索馬利文                 | so     |
| 高棉文                   | km     | 塔吉克文                 | tg     |
| 烏茲別克文               | uz     | 哈薩克文                 | kk     |
| 吉爾吉斯文               | ky     | 毛利文                   | mi     |
| 藏文                     | bo     | 意第緒文                 | yi     |
| 南非語                   | af     | 霍薩語                   | xh     |
| 塞爾維亞語（拉丁文）     | sr-Latn| 塞爾維亞語（西里爾文）   | sr-Cyrl|
| 波士尼亞語（拉丁文）     | bs-Latn| 波士尼亞語（西里爾文）   | bs-Cyrl|

此列表包括全球常用的語言，並可在發送請求時用於翻譯 API。

### 常見問題

#### 1. 支持哪些語言？
該 API 支持多種語言，包括英文、西班牙文、法文、中文、日文、韓文等。您可以在上面的完整列表中找到所有語言及其代碼。

#### 2. 我可以自動檢測源語言嗎？
是的，如果您不提供源語言，API 將自動檢測源語言。

#### 3. API 的請求限制是多少？
該 API 可以處理大量請求。不過，如果您需要支持每天數百萬次

的請求，請聯繫我們以獲取企業解決方案。

#### 4. 如何進行錯誤處理？
所有錯誤將以 JSON 格式返回，並提供錯誤代碼和消息，便於您進行調試。

### 貢獻
如果您想對這個項目做出貢獻，請通過拉取請求和問題的方式提出您的改進建議。

### 授權
此項目使用 MIT 許可證。請參閱 [LICENSE](LICENSE) 文件以了解更多詳情。

---

## English

### Overview
**Translate API** provides a simple and efficient way to translate text between different languages and automatically detect the source language. The API is designed for easy integration into websites and applications that require instant translation features.

### Features
- 🌍 **Auto Language Detection**: Automatically detects the source language without user input.
- 📝 **Customizable Target Language**: Translates to any desired language.
- 🚀 **Fast and Scalable**: High performance suitable for high-traffic websites.
- 📄 **JSON-based Communication**: Requests and responses are in JSON format for easy integration.
- 🔒 **Secure API**: Supports HTTPS for secure data transmission.
- 🌐 **Wide Language Support**: Supports translations between multiple languages.

### Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/oinktech/Translate-API.git
   cd Translate-API
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask server:
   ```bash
   python app.py
   ```

4. The API will be accessible at `http://127.0.0.1:5000/translate`.

### API Endpoints
- **Base URL**: `https://translate-api-s81i.onrender.com/translate`
- **Method**: POST
- **Content Type**: `application/json`

### Request Format
```json
{
  "text": "Hello, world",
  "dest_lang": "fr"  // Target language
}
```

### JavaScript Example
```javascript
fetch('https://translate-api-s81i.onrender.com/translate', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    text: 'Hello, world',
    dest_lang: 'es',  // Target language: Spanish
  }),
})
.then(response => response.json())
.then(data => console.log('Translated Text:', data.translated_text))
.catch(error => console.error('Error:', error));
```

### Response Format
```json
{
  "original_text": "Hello, world",
  "translated_text": "Hola, mundo",
  "src_lang": "en",  // Detected source language
  "dest_lang": "es"  // Target language
}
```

### Supported Languages and Codes

Below is a list of the most common 100 languages supported by the API, along with their ISO 639-1 language codes:

| Language                | Code   | Language                | Code   |
|-------------------------|--------|-------------------------|--------|
| English                 | en     | Hebrew                  | he     |
| Spanish                 | es     | Hindi                   | hi     |
| French                  | fr     | Croatian                | hr     |
| German                  | de     | Hungarian               | hu     |
| Simplified Chinese      | zh-CN  | Icelandic               | is     |
| Traditional Chinese     | zh-TW  | Indonesian              | id     |
| Japanese                | ja     | Irish                   | ga     |
| Korean                  | ko     | Italian                 | it     |
| Russian                 | ru     | Latvian                 | lv     |
| Portuguese              | pt     | Lithuanian              | lt     |
| Arabic                  | ar     | Macedonian              | mk     |
| Bengali                 | bn     | Malay                   | ms     |
| Bulgarian               | bg     | Norwegian               | no     |
| Catalan                 | ca     | Polish                  | pl     |
| Czech                   | cs     | Romanian                | ro     |
| Danish                  | da     | Serbian                 | sr     |
| Dutch                   | nl     | Slovak                  | sk     |
| Finnish                 | fi     | Slovenian               | sl     |
| Greek                   | el     | Swedish                 | sv     |
| Thai                    | th     | Turkish                 | tr     |
| Ukrainian               | uk     | Urdu                    | ur     |
| Vietnamese              | vi     | Welsh                   | cy     |
| Filipino                | tl     | Zulu                    | zu     |
| Georgian                | ka     | Azerbaijani             | az     |
| Gujarati                | gu     | Basque                  | eu     |
| Persian                 | fa     | Belarusian              | be     |
| Pashto                  | ps     | Bosnian                 | bs     |
| Tamil                   | ta     | Estonian                | et     |
| Telugu                  | te     | Faroese                 | fo     |
| Malayalam               | ml     | Frisian                 | fy     |
| Marathi                 | mr     | Galician                | gl     |
| Nepali                  | ne     | Haitian Creole          | ht     |
| Sinhala                 | si     | Luxembourgish           | lb     |
| Uzbek                   | uz     | Kazakh                  | kk     |
| Kyrgyz                  | ky     | Maori                   | mi     |
| Tibetan                 | bo     | Yiddish                 | yi     |
| Afrikaans               | af     | Xhosa                   | xh     |
| Serbian (Latin)        | sr-Latn| Serbian (Cyrillic)     | sr-Cyrl|
| Bosnian (Latin)        | bs-Latn| Bosnian (Cyrillic)     | bs-Cyrl|

This list includes commonly used languages globally, and you can use it for the translations with the API.

### Frequently Asked Questions

#### 1. What languages are supported?
The API supports multiple languages, including English, Spanish, French, Chinese, Japanese, Korean, and many more. You can find a complete list above.

#### 2. Can I auto-detect the source language?
Yes, if you don't provide a source language, the API will automatically detect it.

#### 3. What are the request limits for the API?
The API can handle a large number of requests. However, if you need support for millions of requests daily, please contact us for enterprise solutions.

#### 4. How is error handling done?
All errors will be returned in JSON format, providing an error code and message for easier debugging.

### Contributing
If you want to contribute to this project, please suggest your improvements through pull requests and issues.

### License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
