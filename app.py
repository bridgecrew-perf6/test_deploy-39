
from flask import Flask

def flask_app():
    mainapp = Flask(__name__, instance_relative_config=False)

    with mainapp.app_context():
        # Import parts of our core Flask app
        import routes

        # Import Dash application
        from dashboard import init_dashboard
        mainapp = init_dashboard(mainapp)

        return mainapp
    
mainapp = flask_app()
# print("appdata: ", app)

# Run server
if __name__ == "__main__":
    mainapp.run(debug=False)