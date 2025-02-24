
from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xf9\x0b\x9a\xe1\xed\xcb\x00t\xae}\x8bW\x14\xd9\xdc\x0f'

