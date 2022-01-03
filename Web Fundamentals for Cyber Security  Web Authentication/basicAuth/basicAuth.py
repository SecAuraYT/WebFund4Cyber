from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

#Styling--------------------------------------
pretty = '<title>Basic Auth</title><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">'
css = """
<style>
    h1 { color: #ff5a77; font-family: Monospace; }
    p { color: #07e0fa; font-family: Monospace; }
    body {background-color: #2c3033;}
</style>"""
meme = '<br><iframe src="https://giphy.com/embed/fHcBVLr5EWka6ZKO0g" width="480" height="238" frameBorder="0"</iframe>'
#----------------------------------------------

# define flask
app = Flask(__name__)
authentication = HTTPBasicAuth()

# username:password combination to login
auth_users = {
    "SecAura": generate_password_hash("subscribePlease"),
}

# Compares HTTP Basic Auth string with username:password in `auth_users` dictionary
@authentication.verify_password
def verify_password(username, password):
    if username in auth_users and check_password_hash(auth_users.get("SecAura"), password):
        return username


@app.route("/")
@authentication.login_required # forces HTTP basic prompt
def index():
    return f"{pretty}{css}<h1>Welcome {authentication.current_user()} :)</h1><p> You have successfully logged in<p> {meme}"


if __name__ == "__main__":
    app.run()
