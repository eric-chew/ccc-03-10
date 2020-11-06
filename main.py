# Load env variables
from dotenv import load_dotenv
load_dotenv()

# Create Flask Application
from flask import Flask
app = Flask(__name__)

# Connection to Database
from database import init_db
db = init_db(app)

# Controller Registration
from controllers import registerable_controllers

for controller in registerable_controllers:
    app.register_blueprint(controller)