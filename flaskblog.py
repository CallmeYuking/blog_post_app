from flask import Flask, render_template, redirect, url_for, flash
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'caf695c92aa3411ea188f74c8fb5027b'

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
    """Show about page."""

    return render_template("about.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    """Register page for user."""

    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account create for {form.username.data}!", "success")
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    """Login page for user."""

    form = loginForm()
    return render_template('login.html', title='Login', form=form)








if __name__ == '__main__':
    
    app.secret_key = 'super secret key'
    app.run(host='0.0.0.0', debug=True)
