# Nomear as rotas de tag com um nome especial para saber a responsabilidade das rotas
from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.views.tag_creator_view import TagCreatorView
# Indicação que se relaciona as tags
tags_routes_bp = Blueprint('tags_routes', __name__)

@tags_routes_bp.route('/create_tag', methods=['POST'])


def create_tags():
    # Body da requisição http em Flask
    tag_creator_view = TagCreatorView()

    http_request = HttpRequest(body=request.json)
    response = tag_creator_view.validate_and_create(http_request)

    return jsonify(response.body), response.status_code
