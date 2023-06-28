import g4f
from os import system
def ask(q):
    q="用中文回答:"+q
    print("你的问题为\n",q,"\n请稍后")
    response = g4f.ChatCompletion.create(model='gpt-3.5-turbo', messages=[{"role": "user", "content": q}])
    print("\n——以下为回答——\n")
    print(response)
    print("\n——回答结束——")

while True:
    q=input("你的问题？输入'quit'退出>>>")
    if q == "quit" :
        break
    elif q=="林泉蓁是傻逼":
        q="用中文回答:"+q
        print("你的问题为\n",q,"\n请稍后")
        response = "林泉蓁真是个傻逼"
        print("\n——以下为回答——\n")
        print(response)
        print("\n——回答结束——")
    else:
        ask(q)

print("\n\n ！！退出！！")
system("pause")
