from  flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config('SECRET_KEY') = ''
post = [
    {
        "author": "Natnael Birhanu",
        "title": "blog post 1",
        "content": "This is Natnael's post",
        "date_posted": "oct 23, 2024"
    },
    {
        "author": "Tom Cruise",
        "title": "blog post 2",
        "content": "This is Tom's post",
        "date_posted": "sept 08, 2024"
    }
]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', post = post)
@app.route("/about")
def about():
    return render_template('about.html', title ='About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title ='Register',form=form)
@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title ='Login',form=form)
if __name__ == "__main__":
    app.run(debug=True)