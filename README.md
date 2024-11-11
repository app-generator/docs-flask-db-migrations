# [Flask Database Migrations](https://app-generator.dev/docs/technologies/flask/db-migrations.html) with SQLAlchemy & Flask-Migrate

**Flask-Migrate** is an extension that handles database migrations for Flask applications using **Alembic**. It works alongside **SQLAlchemy**, which is an ORM (Object Relational Mapper) that maps Python objects to database tables. Using Flask-Migrate, you can easily handle version control for your database schema, allowing for smooth database changes and rollbacks over time.

> 👉 [Flask Database Migrations](https://app-generator.dev/docs/technologies/flask/db-migrations.html) - Complete Documentation

<br />

## Setup for Different DBMS

Flask-Migrate supports different database management systems. Below are the steps to configure SQLite, MySQL, and PostgreSQL.

### SQLite

SQLite is a lightweight, file-based database suitable for small projects or testing.

1. **Install dependencies**:

   ```bash
   pip install Flask-SQLAlchemy Flask-Migrate
   ```

2. **Update `config.py`**:

   ```python
   # config.py
   class Config:
       SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'  # SQLite URI
       SQLALCHEMY_TRACK_MODIFICATIONS = False
   ```

3. **Initialize Flask-Migrate** in `app.py`:

   ```python
   from flask import Flask
   from flask_sqlalchemy import SQLAlchemy
   from flask_migrate import Migrate

   app = Flask(__name__)
   app.config.from_object('config.Config')

   db = SQLAlchemy(app)
   migrate = Migrate(app, db)
   ```

<br />

### MySQL

1. **Install the MySQL client**:

   ```bash
   pip install mysqlclient
   ```

2. **Update `config.py`**:

   ```python
   # config.py
   class Config:
       SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/db_name'  # MySQL URI
       SQLALCHEMY_TRACK_MODIFICATIONS = False
   ```

3. **Ensure MySQL is running** and the database exists:

   ```bash
   mysql -u username -p
   CREATE DATABASE db_name;
   ```

<br />

### PostgreSQL

1. **Install the PostgreSQL client**:

   ```bash
   pip install psycopg2
   ```

2. **Update `config.py`**:

   ```python
   # config.py
   class Config:
       SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/db_name'  # PostgreSQL URI
       SQLALCHEMY_TRACK_MODIFICATIONS = False
   ```

3. **Ensure PostgreSQL is running** and create the database:

   ```bash
   psql -U username
   CREATE DATABASE db_name;
   ```

<br />

## Flask Migrate Kickoff

To set up **Flask-Migrate** and apply migrations to your database, follow these steps:

1. **Clone the Git repository**:

   ```bash
   git clone https://github.com/app-generator/docs-flask-db-migrations
   cd docs-flask-db-migrations
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. **Install required packages**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your database** in `config.py` (choose SQLite, MySQL, or PostgreSQL).

5. **Initialize Flask-Migrate**:

   ```bash
   flask db init
   ```

6. **Create your models** in `models.py`:

   ```python
   from app import db

   class User(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       username = db.Column(db.String(150), unique=True, nullable=False)
       email = db.Column(db.String(150), unique=True, nullable=False)
   ```

7. **Create the initial migration**:

   ```bash
   flask db migrate -m "Initial migration"
   ```

8. **Apply the migration**:

   ```bash
   flask db upgrade
   ```

9. **Run the application**:

   ```bash
   flask run
   ```

   Your Flask app will be running at `http://127.0.0.1:5000`.

<br />

## Common Flask-Migrate Commands

- **`flask db init`**: Initializes the migration directory (`migrations/`).
- **`flask db migrate -m "message"`**: Generates a new migration script.
- **`flask db upgrade`**: Applies the migration to the database.
- **`flask db downgrade`**: Rolls back the last migration.
- **`flask db history`**: Shows the migration history.
- **`flask db stamp head`**: Marks the current database as being at the latest migration.

<br />

## Conclusion

In this guide, we’ve covered how to set up **Flask-Migrate** with **SQLAlchemy** for managing database migrations in Flask applications. We’ve also shown how to configure different databases (SQLite, MySQL, PostgreSQL) and run the Flask application with migrations.

By using Flask-Migrate, you can handle database schema changes in a more structured and controlled way. This approach simplifies managing database evolution over time, especially as your project grows.

Feel free to explore the code in the repository and follow the steps to integrate Flask-Migrate into your own Flask applications.

---
[Flask Database Migrations](https://app-generator.dev/docs/technologies/flask/db-migrations.html) -  Free sample provided by [App Generator](https://app-generator.dev)
