from flask import render_template


def configure_routes(app):

    @app.route('/')
    def home():
        return render_template("home.html")

    @app.route("/login", methods=['GET', 'POST'])
    def login():
        return render_template('login.html')