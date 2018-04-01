import os

basedir = os.path.abspath(os.path.dirname(__file__))

### Need to set a good Secret_Key env variable
class Config(object):
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'poop face ghost killa'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

    print('database url', SQLALCHEMY_DATABASE_URI)
    # Stops notification of app each time DB is going to be modified
    SQLALCHEMY_TRACK_MODIFICATIONS = False