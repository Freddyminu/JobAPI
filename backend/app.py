from flask import Flask
from controllers.jobs import jobs_blueprint
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.register_blueprint(jobs_blueprint)

# cria banco de dados se ele n existe ainda
