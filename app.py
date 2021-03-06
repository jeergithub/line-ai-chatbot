from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('lWiAVYnKFQHIHon1eNlU374kciQHstnl0QHQbYYDKUQgw1QrxoQQyfIFslKe+X1SmCsWH4jpngUTyEYIBvhQyzaKLqcZRirIlzOn/GPTTcWoQ8nBks5MIQnAEYmgOOaIgb5eP9nWVlWxoJKXVdkH4AdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('0574b54754d1f33881a8fef9f7500f64')

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
