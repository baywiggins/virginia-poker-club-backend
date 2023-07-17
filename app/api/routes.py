from flask import Blueprint, jsonify, request, json
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager
from datetime import timedelta, datetime, timezone



bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/top-players', methods=['GET'])
@jwt_required()
def get_top_players():
    # # Get the number of top players you want to retrieve (e.g., from request arguments)
    # n = request.args.get('n', default=10, type=int)

    # # Query the database for the top players based on chip count
    # top_players = Player.query.order_by(Player.chip_count.desc()).limit(n).all()

    # # Format the top players data as needed
    # top_players_data = [{'name': player.name, 'chip_count': player.chip_count} for player in top_players]

    # # Return the top players as JSON
    # return jsonify(top_players_data)
    return {"hello":"world"}

