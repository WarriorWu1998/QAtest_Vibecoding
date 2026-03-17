# app.py
from flask import Flask, render_template, request
from user_system import UserManager

app = Flask(__name__)
system = UserManager()

@app.route('/')
def index():
    # 顯示網頁畫面
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    # 接收網頁傳來的資料
    username = request.form.get('username')
    password = request.form.get('password')
    
    # 呼叫我們之前寫好的邏輯
    result = system.register_user(username, password)
    
    # 回傳結果給網頁
    return f"註冊結果：{result} <br><a href='/'>返回</a>"

if __name__ == '__main__':
    app.run(debug=True)