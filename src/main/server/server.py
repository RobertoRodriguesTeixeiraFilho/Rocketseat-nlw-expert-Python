from flask import Flask
from src.main.routes.tag_routes import tags_routes_bp
# Fazendo registro das rotas que blueprint comporta

app = Flask(__name__)

app.register_blueprint(tags_routes_bp)
