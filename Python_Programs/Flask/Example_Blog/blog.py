# Python 3.6.5 -- Flask 1.0.2
from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {'author': 'Author #1',
     'title': 'Blog post #1',
     'content': 'First content.',
     'date_posted:': 'A long time ago.'},
    {'author': 'Author #2',
     'title': 'Blog post #2',
     'content': 'Second content.',
     'date_posted': 'Not as long, but still awhile ago.'}]

@app.route("/")  # Shows content on homepage
@app.route("/home")  # Also shows the content for /home
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    #return "<h1>About</h1>"  # You can directly return HTML w/o template.
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)  # Debug shows your changes instantly.
