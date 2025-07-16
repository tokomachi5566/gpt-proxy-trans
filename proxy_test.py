from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['POST'])
def hello():
    data = request.json  # 拿到前端傳來的 JSON
    text = data.get('text', '')
    print("Flask收到：", text)
    return jsonify({'reply': f'你說：{text}'})

if __name__ == '__main__':
    app.run(port=5678)
