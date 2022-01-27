from flask import Flask, request, render_template, redirect, url_for
from flask import current_app

@current_app.route("/")
def index():
    return "Hello World!"

@current_app.route("/dashboard")
def dashboard():
    return redirect("/dashboard/")

#if __name__ == "__main__":
#    app.run()