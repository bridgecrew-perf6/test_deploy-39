from flask import Flask, request, render_template, redirect, url_for
from flask import current_app

@current_app.route("/")
def index():
    return "Hello World!"

@current_app.route("/dashboard")
def dashboard():
    render_template("dashboard.html")

#if __name__ == "__main__":
#    app.run()