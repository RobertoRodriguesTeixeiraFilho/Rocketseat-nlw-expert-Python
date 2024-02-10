# Nomear as rotas de tag com um nome especial para saber a responsabilidade das rotas
from flask import Blueprint, request, jsonify
# Indicação que se relaciona as tags
tags_routes_bp = Blueprint('tags_routes', __name__)

@tags_routes_bp.route('/create_tag', methods=['POST'])


def create_tags():
    # Body da requisição http em Flask
    print(request.json)
    return jsonify({ "resp": "ok" }), 200
