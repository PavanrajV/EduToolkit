from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

from auth.routes import auth
from api.tools_api import tools_api
from api.analytics_api import analytics_api

app.register_blueprint(auth)
app.register_blueprint(tools_api)
app.register_blueprint(analytics_api)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)