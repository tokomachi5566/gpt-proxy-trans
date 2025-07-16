from flask import Flask, request, jsonify
from dotenv import load_dotenv
import openai
import os

#抓key
load_dotenv(dotenv_path='key.env')
app = Flask(__name__)

#沒抓到就直接指定
client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

@app.route('/gpt-translate', methods=['POST'])
def gpt_translate():
    try:
        data = request.json
        text = data.get('text', '')
        print("get request：", text)
        if not text:
            return jsonify({'translated': '[There si nothing]'}), 400
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": f"請將以下英文字幕翻譯為自然的繁體中文：\n{text}"}],
            temperature=0.2
        )
        print("GPT 回傳:", response)
        return jsonify({'translated': response.choices[0].message.content.strip()})
    except Exception as e:
        print("OpenAI error:", e)
        return jsonify({'translated': f'[OpenAI錯誤: {e}]'}), 500


if __name__ == '__main__':
    app.run(port=5678)
