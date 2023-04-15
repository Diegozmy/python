from requests import post
from base64 import b64encode
from datetime import datetime
from io import BytesIO

# 钉钉机器人的webhook地址
webhook_url = "https://oapi.dingtalk.com/robot/send?access_token" \
              "=e431400e0b958115be6d0585a4ccf8a5fb61220fc84106fe04133acdb7cb43e6"


# 要发送的消息内容
def send(screenshot, cam):
    message = {
        "msgtype": "text",
        "text": {
            "content": "！！！.！！！\n时间：{time}\n截图：{screenshot}\n摄像头：{cam}".format(
                time=datetime.now().strftime("%Y/%m/%d-%H:%M:%S"), screenshot=screenshot, cam=cam)
        }
    }

    # 发送POST请求
    response = post(webhook_url, json=message)

    # 打印响应结果
    print(response.text)


def upload(key_imgbb: str, picture: str):
    with open(picture, "rb") as file:
        url = "https://api.imgbb.com/1/upload"
        payload = {
            "key": key_imgbb,
            "image": BytesIO(b64encode(file.read())),
            # "expiration":expiration
        }
        res = post(url, payload)
    url = str(eval(res.text, {'true': 0})["data"]["image"]["url"]).replace("\\", "")
    print(url)
    return url
