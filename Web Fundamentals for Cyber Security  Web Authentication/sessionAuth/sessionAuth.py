from flask import Flask, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import (
    LoginManager,
    UserMixin,
    current_user,
    login_required,
    login_user,
)

#Styling--------------------------------------
pretty = '<title>Sess Auth</title><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">'
css = """
<style>
    h1 { color: #ff5a77; font-family: Monospace; }
    p { color: #07e0fa; font-family: Monospace; }
    body {background-color: #2c3033;}
</style>"""
meme = '<br><iframe src="https://giphy.com/embed/SXftACCpeDzPPTE3yU" width="480" height="238" frameBorder="0"</iframe>'
meme2 = '<br><iframe src="https://giphy.com/embed/XbV2mrHs6ureBPUEuJ" width="480" height="238" frameBorder="0"</iframe>'

#----------------------------------------------




app = Flask(__name__)
app.config.update(
    SECRET_KEY="SecAura1337",
)

loginManager = LoginManager()
loginManager.init_app(app)


auth_users = {
    "SecAura": generate_password_hash("subscribePlease"),
}

# needed for userModel
class User(UserMixin):
    ...


@loginManager.user_loader
def user_loader(username: str):
    if username in auth_users:
        user_model = User()
        user_model.id = username
        return user_model
    return None

#login form
@app.route("/login")
def formPage():
    return f"""
    {pretty}{css}
    <h1> Login </h1>
    <form method="POST" action="submit">
    <div class="input-group mb-6">
        <input name="username" type="text" class="form-control" placeholder="username">
        <div class="input-group-append">
            <input name="password" type="text" class="form-control" placeholder="password">
            <button class="form-control btn-outline-primary" type="submit">Submit Comment</button>
        </div>
        </div>
    </form>
    {meme2}
    """
#processes post input, if login sucessful, issue Cookie
@app.route("/submit", methods=["POST"])
def login_page():
    username = request.form.get("username")
    password = request.form.get("password")

    if username in auth_users:
        if check_password_hash(auth_users.get(username), password):
            user_model = User()
            user_model.id = username
            login_user(user_model)
        else:
            return "Wrong credentials"
    return f"{pretty}{css}<h1>Welcome {current_user.id} :)</h1><p> You have successfully logged in<p> {meme}"



if __name__ == "__main__":
    app.run()
