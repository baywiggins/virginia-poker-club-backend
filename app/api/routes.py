from flask import Blueprint, jsonify, request

# from app.main.models import Player
# from app import db

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/top-players', methods=['GET'])
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
