
from flask import Flask

def flask_app():
    flaskapp = Flask(__name__)
    #app.config.from_object('config.Config')

    with flaskapp.app_context():
        # Core flask app pages
        import routes

        # Import Dash app
        from dashboard import init_dashboard
        dashboard = init_dashboard(flaskapp)

    return flaskapp
    
app = flask_app()
print("appdata: ", app)

# Run server
if __name__ == "__main__":
    app.run(debug=False)