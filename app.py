from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config

app = Flask(__name__)
app.config.from_object(config.SQLiteConfig)  # Choose SQLiteConfig, MySQLConfig, or PostgreSQLConfig

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Register models
import models

# Route for testing
@app.route('/')
def index():
    return "Flask-Migrate setup is working!"

if __name__ == '__main__':
    app.run(debug=True)
