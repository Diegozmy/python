from flask import Flask, request
from g4f import ChatCompletion
import logging
app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.INFO)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        print(user_input)
        output = ChatCompletion.create(model='gpt-3.5-turbo', messages=[{"role": "user", "content": user_input}])
        print(output)
        return f'''
        <form method="post">
            <label for="user_input">请输入问题：</label>
            <input type="text" id="user_input" name="user_input">
            <input type="submit" value="提交">
        </form>
        <h1>GPT:\n {output}</h1>
    '''
    return '''
        <form method="post">
            <label for="user_input">请输入问题：</label>
            <input type="text" id="user_input" name="user_input">
            <input type="submit" value="提交">
        </form>
    '''


if __name__ == '__main__':
    app.run()
