from flask import Flask

app = Flask(__name__)
from app import routesApi
from app import routes