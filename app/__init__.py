import os
from flask import Flask

print(os.environ['APP_SETTINGS'])
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

from app import views
