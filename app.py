from  flask import Flask, render_template, url_for
app = Flask(__name__)

post = [
    {
        "autor": "Natnael Birhanu",
        "title": "blog post 1",
        "content": "This is Nate's post",
        "date_posted": "today"
    },
    {
        "autor": "Tom Cruise",
        "title": "blog post 2",
        "content": "This is Tom's post",
        "date_posted": "today"
    }
]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', post = post)
@app.route("/about")
def about():
    return render_template('about.html', title ='About')

if __name__ == "__main__":
    app.run(debug=True)