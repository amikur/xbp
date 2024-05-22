from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
db = SQLAlchemy(app)

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(2048), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    saved_at = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/submit-url', methods=['POST'])
def submit_url():
    # リクエストからJSONデータを取得
    url_data = request.json
    new_url = URL(url=url_data['url'], title=url_data['title'])
    # データをデータベースに保存
    # ...
    # 成功レスポンスを返す
    return jsonify({"message": "URL saved successfully"})
    
  
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

@app.route('/get-urls', methods=['GET'])
def get_urls():
    urls = URL.query.order_by(URL.saved_at.desc()).all()
    return jsonify([{'url': u.url, 'title': u.title, 'saved_at': u.saved_at} for u in urls])


