from g4f import ChatCompletion


def a(question):
    data.append({"role": "user", "content": f"{question}"})
    back = ChatCompletion.create(model='gpt-3.5-turbo', messages=data)

    data.append({"role": "assistant", "content": f"{back}"})
    if len(data) > 4:
        data.remove(data[1])
        data.remove(data[1])
    return back

if __name__=="__main__":
    data = [{"role": "system", "content": "你是个中文助手"}, {"role": "user", "content": "用中文回答下列问题"}]
    q = ""
    print("输入quit退出！\n正在加载")
    response = ChatCompletion.create(model='gpt-3.5-turbo', messages=data)
    print("GPT:", response)
    data.append({"role": "assistant", "content": f"{response}"})
    while True:
        q = input("you: ")
        if len(q) == 0:
            print("GPT: 请输入问题!")
        elif q == "quit":
            break
        else:
            print("GPT:", a(q))

