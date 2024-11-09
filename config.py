import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class SQLiteConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

class MySQLConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/dbname'

class PostgreSQLConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/dbname'
