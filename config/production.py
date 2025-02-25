
from config.default import *
from logging.config import dictConfig
from dotenv import load_dotenv

# SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user=os.getenv('DB_USER'),
    pw=os.getenv('DB_PASSWORD'),
    url=os.getenv('DB_HOST'),
    db=os.getenv('DB_NAME')
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xf9\x0b\x9a\xe1\xed\xcb\x00t\xae}\x8bW\x14\xd9\xdc\x0f'

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/myproject.log'),
            'maxBytes': 1024 * 1024 * 5, # 5MB
            'backupCount': 5,
            'formatter': 'default',
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['file']
    }
})