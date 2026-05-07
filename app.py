from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_survey', methods=['POST'])
def save_survey():
    data = request.json
    # 여기서 나이, 성별 데이터를 DB에 저장하거나 분석용으로 활용
    print(f"User Data: {data['age']}, {data['gender']}")
    return jsonify(status="success")

if __name__ == '__main__':
    app.run(debug=True, port=5000)