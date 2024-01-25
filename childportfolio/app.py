import os
from dotenv import load_dotenv

load_dotenv()  # これにより.envファイルが読み込まれます

LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
LINE_CHANNEL_SECRET = os.getenv('LINE_CHANNEL_SECRET')



from flask import Flask, jsonify, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, ImageMessage, TextSendMessage
)

app = Flask(__name__)



line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

@app.route("/callback", methods=['POST'])
def callback():
    # リクエストヘッダーから署名検証用の値を取得
    signature = request.headers['X-Line-Signature']

    # リクエストボディを取得
    body = request.get_data(as_text=True)

    # 署名の検証とハンドラーの呼び出し
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    # テキストメッセージを受け取った場合の処理
    text = event.message.text

    # 応答メッセージの送信（オプション）
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=f"受け取ったメッセージ: {text}")
    )

@handler.add(MessageEvent, message=ImageMessage)
def handle_image_message(event):
    # 画像のIDを取得
    message_id = event.message.id

    # 画像の内容を取得
    message_content = line_bot_api.get_message_content(message_id)

    # 画像をサーバーに保存
    with open(f"images/{message_id}.jpg", "wb") as f:
        for chunk in message_content.iter_content():
            f.write(chunk)

    # 応答メッセージの送信（オプション）
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="画像を受け取りました")
    )

@app.route('/path/to/images', methods=['GET'])
def get_images():
    image_files = os.listdir('images')  # 画像ファイルのリストを取得
    image_urls = [f"{request.url_root}images/{filename}" for filename in image_files]
    return jsonify(image_urls)

