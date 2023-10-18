import os


class Config(object):
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DEBUG = True
    SECRET_KEY = os.environ.get("SECRET_KEY") or "hard to guess string"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CORS_HEADERS = "Content-Type"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_BASE_URL", "sqlite:///") + os.path.join(
        BASE_DIR, os.environ.get("DATABASE_FILE", "tmsystem.sqlite")
    )