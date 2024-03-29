#web app
# 網站 = 伺服器
from flask import Flask, request, abort #架設伺服器

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,StickerSendMessage
)

app = Flask(__name__)

#權杖
line_bot_api = LineBotApi('Wt2S0OCnWmUAEjstS+qYEsgnT1ErNUoqCBahmzSaFlEUTyBfEyEaNG7peuwUrLmmNKJwFGrOXLwtK0E8E4oIh01Gnl5JvCXiCB6Bd1u0F7L/+/6P3uAZ1lAjwgmD7LrJmANVTr6dCy9vIHxhH0IdMgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('8b4f42cce3fcf88d6a74366a43bf3d72')


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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '妳好漂亮'
    
    if '給我貼圖' in msg:
        sticker_message = StickerSendMessage(
            package_id='2',
            sticker_id='23')

        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)
        return

    if msg in ['hi', 'Hi'] :
        r = '嗨'
    elif msg == '你吃飯了嗎' :
        r = '等你請我'
    elif msg == '你是誰' :
        r = '我是讚喔機器人'
    elif '訂位' in msg :
        r = '算我一份 謝謝'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()