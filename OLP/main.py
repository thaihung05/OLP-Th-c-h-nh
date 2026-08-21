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


@app.route("/register", methods=["GET", "POST"])
def register():
    error = None

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")

        ok, message = auth.register(username, password, email)
        if ok:
            return redirect("/login")
        error = message

    return render_template("register.html", error=error)


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        ok, message = auth.login(username, password)
        if ok:
            session["username"] = username
            return redirect("/dashboard")
        error = message

    return render_template("login.html", error=error)


@app.route("/dashboard")
def dashboard():
    # Chưa đăng nhập thì không cho vào, đá về trang login.
    if "username" not in session:
        return redirect("/login")

    username = session["username"]
    email = auth.users[username]["email"]
    return render_template("dashboard.html", username=username, email=email)


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)
