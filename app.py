
from flask import Flask

def flask_app():
    app = Flask(__name__)
    #app.config.from_object('config.Config')

    with app.app_context():
        # Core flask app pages
        import routes

        # Import Dash app
        from dashboard import init_dashboard
        app = init_dashboard(app)

        return app
    
app = flask_app()

# Run server
if __name__ == "__main__":
    app.run(debug=False)