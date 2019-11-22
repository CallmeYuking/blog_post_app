from flask import Flask, render_template, redirect

app = Flask(__name__)

posts = [
    {
        'author': 'Erica Quan',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Tiffany',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    """Show home page."""
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")








if __name__ == '__main__':
    
    app.secret_key = 'super secret key'
    app.run(host='0.0.0.0', debug=True)
