from flask import Flask, redirect, render_template, request, session

from OLP_Init import auth

app = Flask(__name__)
app.secret_key = "dev-secret-key"  # cần có để dùng session (lưu ai đang đăng nhập)


@app.route("/")
def index():
    # Vào trang chủ: nếu đã đăng nhập thì vào dashboard, chưa thì bắt đăng nhập.
    if "username" in session:
        return redirect("/dashboard")
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)
