from flask import Flask
from flask_httpauth import HTTPDigestAuth

#Styling--------------------------------------
pretty = '<title>Digest Auth</title><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">'
css = """
<style>
    h1 { color: #ff5a77; font-family: Monospace; }
    p { color: #07e0fa; font-family: Monospace; }
    body {background-color: #2c3033;}
</style>"""
meme = '<br><iframe src="https://giphy.com/embed/yN3VNoK7j1nS36gIyH" width="480" height="238" frameBorder="0"</iframe>'
#----------------------------------------------

app = Flask(__name__)
app.config["SECRET_KEY"] = "SecAura1337"
authentication = HTTPDigestAuth()

auth_users = {
    "SecAura": "subscribePlease"
}


@authentication.get_password
def get_user(username):
    if username in auth_users:
        return auth_users.get(username)


@app.route("/")
@authentication.login_required
def index():
    return f"{pretty}{css}<h1>Welcome {authentication.current_user()} :)</h1><p> You have successfully logged in<p> {meme}"


if __name__ == "__main__":
    app.run()
